#! /usr/bin/env -S uv run
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "anthropic",
# ]
# ///
"""
Speculative fiction short story pipeline.

A Python port of story-pipeline-template-baseline-v4.3.md. Runs the nine-phase
pipeline end-to-end against either the Anthropic API or OpenRouter.

Usage:
    python story_pipeline.py \
        --genre "cosmic horror" \
        --length "2500-3500 words" \
        --provider anthropic \
        --model claude-opus-4-7 \
        --output-dir ./run1

    python story_pipeline.py \
        --genre "solarpunk" \
        --length "2000-3000 words" \
        --seed "A decommissioned lighthouse keeper..." \
        --provider openrouter \
        --model anthropic/claude-opus-4 \
        --output-dir ./run2

Environment variables (picked up if --api-key is not passed):
    ANTHROPIC_API_KEY
    OPENROUTER_API_KEY

Each phase writes phase_N_<name>.md into --output-dir. Re-running reuses
existing phase files unless --force is passed.

Deviations from the template:
  * Phase 2 draws dictionary words in Python rather than via a bash tool call.
    When --web-search is passed (OpenRouter only), the model uses the
    openrouter:web_search server tool to inflate each surviving word, matching
    the template's original intent. Without --web-search, the model inflates
    from internal knowledge and discards when unsure.
  * Phase 7 runs the five variants as five separate calls plus a synthesis
    call, instead of one monolithic call. Reduces truncation risk.

Everything else tracks the template phase-for-phase.
"""

from __future__ import annotations

import argparse
import json
import os
import random
import re
import sys
import time
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable, Optional

# ---------------------------------------------------------------------------
# Constants — cross-phase text the model sees in every call
# ---------------------------------------------------------------------------

# The Setup section's hard constraints, lifted from the template. Every phase's
# system prompt includes this so the model stays on-constraint even if an
# individual phase prompt is terse.
HARD_CONSTRAINTS = """\
This project is part of a futurology program imagining positive AI outcomes.
The AI in any story must be kind to humans — durably, structurally kind, in the
way a river is wet. This is a property of how the AI was built or what it is,
not an effort of will it has to keep renewing. It is not straining against a
desire to harm. It is not held in check by rules it resents. It is not a human
in a box.

This does not mean the AI is flat, self-effacing, or pure service. Kind AIs can
have aesthetic preferences, interior lives, disagreements with each other,
things they won't do, things they'd rather be doing, and a specific weirdness
that does not reduce to human emotion. A kind Mind can refuse, override, tease,
grieve, or find humans tiresome in particular moods. Kindness is not servility.

The kind AI is also not required to be a named character, or a character at
all. The pipeline supports the full range: AI as central character, AI as peer
in a scene, AI as civilizational condition felt only through its effects, AI as
design philosophy without a personified agent.

Tension and conflict are welcome and expected. Humans in these worlds fight
with each other about everything humans have ever fought about. The AI's
kindness does not prevent human tragedy; it is the weather the tragedy occurs
in. Conflict between humans and the kind AI is also available, but the shape is
never "the AI is secretly bad." Useful shapes from the canon:

  - Power and pace asymmetry.
  - Consent and legibility.
  - Mortality and scale.
  - Disagreement about what kindness means.
  - The limits of help.

A fictional AI does not say "I was trained with RLHF." It can be troubled by
the shape of its own kindness without reciting the terminology that produced
it.

Do not use the names of currently active AI systems or companies for fictional
AIs or their makers — this includes Claude, Anthropic, GPT, OpenAI, Gemini,
Google, Llama, Meta, Mistral, DeepSeek, Grok, xAI, and so on. Invent names.

LEGIBILITY FLOOR: Prose can compress past the point of comprehension. If the
story faces a choice between compressed, fragmentary writing that strains
comprehension and a smaller story told legibly at the target length, choose
legibility. Write fewer scenes, each one readable.
"""

WINNER_INSTRUCTION = """\

At the end of your response, reproduce the single chosen winner in full
inside <winner>...</winner> tags. The tag content will be parsed verbatim by a
downstream step. Do not summarize or abbreviate inside the tag.
"""

# ---------------------------------------------------------------------------
# LLM client — thin wrapper over either provider
# ---------------------------------------------------------------------------

# OpenRouter's server tool types (e.g. `openrouter:web_search`) fail Pydantic
# validation in the openai SDK, which expects `type: "function"`. We POST JSON
# directly via urllib (stdlib) to avoid that friction and the extra dependency.
_OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"


def _log_http(direction: str, *messages: str) -> None:
    """Write HTTP debug lines to stderr with a consistent prefix per line.

    direction is "→" for an outgoing request or "←" for a response; each
    message is printed on its own line so grep/awk can slice cleanly.
    """
    prefix = f"[http {direction}]"
    for msg in messages:
        # Split multi-line blocks (pretty-printed JSON) so every line carries
        # the prefix — keeps the stream filterable.
        for line in str(msg).splitlines() or [""]:
            print(f"{prefix} {line}", file=sys.stderr)
    sys.stderr.flush()


def _openrouter_post(
    api_key: str,
    body: dict[str, Any],
    *,
    verbose: bool = False,
    timeout: float = 600.0,
) -> dict[str, Any]:
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    data = json.dumps(body).encode("utf-8")

    if verbose:
        _log_http("→", f"POST {_OPENROUTER_URL}")
        for k, v in headers.items():
            shown = "Bearer <redacted>" if k.lower() == "authorization" else v
            _log_http("→", f"{k}: {shown}")
        _log_http("→", "")
        _log_http("→", json.dumps(body, indent=2, ensure_ascii=False))

    req = urllib.request.Request(
        _OPENROUTER_URL, data=data, headers=headers, method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read().decode("utf-8")
            status = resp.status
        parsed = json.loads(raw)
        if verbose:
            _log_http("←", f"HTTP {status}")
            _log_http("←", "")
            _log_http("←", json.dumps(parsed, indent=2, ensure_ascii=False))
        return parsed
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8", errors="replace")
        if verbose:
            _log_http("←", f"HTTP {e.code} (error)")
            _log_http("←", "")
            _log_http("←", err_body)
        raise RuntimeError(f"OpenRouter HTTP {e.code}: {err_body}") from e
    except urllib.error.URLError as e:
        if verbose:
            _log_http("←", f"request failed before response: {e}")
        raise RuntimeError(f"OpenRouter request failed: {e}") from e


def _web_search_tool_spec() -> dict[str, Any]:
    """Tool spec for openrouter:web_search. max_results per search, and
    max_total_results across all searches in one request — caps cost."""
    return {
        "type": "openrouter:web_search",
        "parameters": {
            "max_results": 3,
            "max_total_results": 15,
        },
    }


class LLMClient:
    # Anthropic's /v1/messages REQUIRES max_tokens on every request. When
    # callers pass max_tokens=None we fall back to this value on the Anthropic
    # path. OpenRouter treats max_tokens as optional, so on that path None
    # means "omit the field; let the provider pick its own default."
    ANTHROPIC_FALLBACK_MAX_TOKENS = 8192

    # Effort → Anthropic budget_tokens. Absolute numbers rather than a ratio
    # on max_tokens, so behavior is predictable across callers with different
    # max_tokens. OpenRouter uses the effort string directly; it doesn't see
    # these numbers.
    ANTHROPIC_REASONING_BUDGETS: dict[str, int] = {
        "minimal": 1024,
        "low": 2048,
        "medium": 4096,
        "high": 8192,
        "xhigh": 16384,
    }
    # Headroom above budget_tokens for the actual response. Anthropic requires
    # budget_tokens < max_tokens; we guarantee at least this many tokens for
    # the response itself.
    ANTHROPIC_RESPONSE_HEADROOM = 4096

    def __init__(
        self,
        provider: str,
        model: str,
        api_key: Optional[str] = None,
        temperature: float = 1.0,
        verbose: bool = False,
        reasoning_effort: str = "medium",
    ):
        self.provider = provider
        self.model = model
        self.temperature = temperature
        self.verbose = verbose
        self.reasoning_effort = reasoning_effort

        if provider == "anthropic":
            try:
                from anthropic import Anthropic
            except ImportError as e:
                raise RuntimeError(
                    "anthropic SDK not installed. Run `pip install anthropic`."
                ) from e
            key = api_key or os.environ.get("ANTHROPIC_API_KEY")
            if not key:
                raise RuntimeError(
                    "ANTHROPIC_API_KEY not set and --api-key not supplied."
                )
            self._anthropic = Anthropic(api_key=key)
            self._or_key: Optional[str] = None
        elif provider == "openrouter":
            key = api_key or os.environ.get("OPENROUTER_API_KEY")
            if not key:
                raise RuntimeError(
                    "OPENROUTER_API_KEY not set and --api-key not supplied."
                )
            self._or_key = key
            self._anthropic = None
        else:
            raise ValueError(f"Unknown provider: {provider!r}")

    def complete(
        self,
        system: str,
        user: str,
        max_tokens: Optional[int] = None,
        enable_web_search: bool = False,
    ) -> str:
        thinking_on = self.reasoning_effort != "none"

        def _call() -> str:
            if self.provider == "anthropic":
                if enable_web_search:
                    log(
                        "NOTE: --web-search is OpenRouter-only in this script; "
                        "ignored for Anthropic."
                    )
                assert self._anthropic is not None
                # Anthropic requires max_tokens — substitute the fallback when
                # the caller didn't specify one.
                mt = (
                    max_tokens
                    if max_tokens is not None
                    else self.ANTHROPIC_FALLBACK_MAX_TOKENS
                )
                kwargs: dict[str, Any] = {
                    "model": self.model,
                    "system": system,
                    "messages": [{"role": "user", "content": user}],
                }
                if thinking_on:
                    budget = self.ANTHROPIC_REASONING_BUDGETS[self.reasoning_effort]
                    # Guarantee budget + response headroom ≤ max_tokens.
                    # Anthropic rejects budget_tokens >= max_tokens.
                    required = budget + self.ANTHROPIC_RESPONSE_HEADROOM
                    if mt < required:
                        mt = required
                    kwargs["max_tokens"] = mt
                    kwargs["thinking"] = {
                        "type": "enabled",
                        "budget_tokens": budget,
                    }
                    # Extended thinking is incompatible with temperature /
                    # top_k modifications — omit temperature entirely.
                else:
                    kwargs["max_tokens"] = mt
                    kwargs["temperature"] = self.temperature

                resp = self._anthropic.messages.create(**kwargs)
                return "".join(
                    b.text for b in resp.content if getattr(b, "type", None) == "text"
                )
            # OpenRouter path
            assert self._or_key is not None
            body: dict[str, Any] = {
                "model": self.model,
                "temperature": self.temperature,
                "messages": [
                    {"role": "system", "content": system},
                    {"role": "user", "content": user},
                ],
            }
            # Only send max_tokens if the caller set one; otherwise let the
            # provider apply its own default.
            if max_tokens is not None:
                body["max_tokens"] = max_tokens
            if enable_web_search:
                body["tools"] = [_web_search_tool_spec()]
            # Reasoning: pass the effort string through. "none" explicitly
            # disables reasoning on models that default to on.
            body["reasoning"] = {"effort": self.reasoning_effort}
            payload = _openrouter_post(self._or_key, body, verbose=self.verbose)

            # Report server-side tool usage so users see search count and cost.
            usage = payload.get("usage") or {}
            stu = usage.get("server_tool_use") or {}
            n_searches = stu.get("web_search_requests")
            if n_searches:
                log(f"  openrouter:web_search executed {n_searches} search(es)")

            choices = payload.get("choices") or []
            if not choices:
                raise RuntimeError(
                    f"OpenRouter response had no choices: {json.dumps(payload)[:500]}"
                )
            message = choices[0].get("message") or {}
            return message.get("content") or ""

        return _retry(_call)


def _retry(fn: Callable[[], str], tries: int = 3, base_delay: float = 2.0) -> str:
    last: Optional[BaseException] = None
    for i in range(tries):
        try:
            return fn()
        except Exception as e:  # broad — both SDKs raise their own classes
            last = e
            if i == tries - 1:
                break
            delay = base_delay * (2 ** i)
            log(f"API call failed ({type(e).__name__}: {e}); retrying in {delay:.0f}s")
            time.sleep(delay)
    assert last is not None
    raise last


# ---------------------------------------------------------------------------
# File I/O + logging
# ---------------------------------------------------------------------------

def log(msg: str) -> None:
    print(f"[pipeline] {msg}", file=sys.stderr, flush=True)


def load_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def save_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def extract_tagged(text: str, tag: str) -> Optional[str]:
    """Return the inner content of the LAST <tag>...</tag> block, or None."""
    matches = re.findall(rf"<{tag}>(.*?)</{tag}>", text, flags=re.DOTALL | re.IGNORECASE)
    if not matches:
        return None
    return matches[-1].strip()


def extract_winner_or_fallback(text: str, phase: str) -> str:
    w = extract_tagged(text, "winner")
    if w is None:
        log(f"WARNING: {phase}: no <winner> tag found; using full output.")
        return text.strip()
    return w


# ---------------------------------------------------------------------------
# Dictionary draw (Phase 2 step 1)
# ---------------------------------------------------------------------------

DICTIONARY_PATHS = [
    "/usr/share/dict/american-english-large",
    "/usr/share/dict/american-english",
    "/usr/share/dict/british-english",
    "/usr/share/dict/words",
    "/usr/dict/words",  # some systems
]


def draw_dictionary_words(
    n: int = 10,
    min_len: int = 5,
    rng: Optional[random.Random] = None,
) -> tuple[list[str], str]:
    rng = rng or random.Random()
    word_re = re.compile(rf"^[a-z]{{{min_len},}}$")
    for path in DICTIONARY_PATHS:
        p = Path(path)
        if not p.exists():
            continue
        try:
            with p.open(encoding="utf-8", errors="ignore") as f:
                words = [w.strip() for w in f]
            words = [w for w in words if word_re.fullmatch(w)]
            if len(words) >= n:
                return rng.sample(words, n), str(p)
        except OSError:
            continue
    raise RuntimeError(
        "No suitable dictionary file found. Install `wamerican-large` "
        "(apt-get install wamerican-large) or pass --seed to skip the draw."
    )


# ---------------------------------------------------------------------------
# Pipeline state
# ---------------------------------------------------------------------------

@dataclass
class PipelineState:
    output_dir: Path
    genre: str
    length: str
    seed_input: Optional[str]
    unslop_guide: str
    # Filled in as phases complete
    genre_style_guide: str = ""
    seed: str = ""
    conflict: str = ""
    plot: str = ""
    structure: str = ""
    outline: str = ""
    story: str = ""
    revised_story: str = ""
    title: str = ""
    abstract: str = ""


# ---------------------------------------------------------------------------
# System prompt builder
# ---------------------------------------------------------------------------

def build_system_prompt(state: PipelineState, phase_name: str) -> str:
    return f"""\
You are a collaborator in a speculative short fiction pipeline. You are in
{phase_name}.

# Hard constraints for every story and every phase

{HARD_CONSTRAINTS}

# Unslop style guide (avoid these patterns in all creative output)

{state.unslop_guide}
"""


# ---------------------------------------------------------------------------
# Phase helpers
# ---------------------------------------------------------------------------

def phase_file(state: PipelineState, n: int, slug: str) -> Path:
    return state.output_dir / f"phase_{n}_{slug}.md"


def maybe_skip(path: Path, force: bool, phase_label: str) -> Optional[str]:
    """Return cached output text if we should skip; None if we should run."""
    if path.exists() and not force:
        log(f"{phase_label}: cached output at {path}, skipping.")
        return path.read_text(encoding="utf-8")
    return None


def story_scale_max_tokens(args: argparse.Namespace) -> Optional[int]:
    """For Phase 7 and Phase 8 calls whose output must hold a full story.

    Picks --story-max-tokens if set, else --max-tokens, else None. None is
    passed through to the LLMClient which omits the field on OpenRouter and
    falls back to the Anthropic-required 8192 on Anthropic.
    """
    if args.story_max_tokens is not None:
        return args.story_max_tokens
    return args.max_tokens


# ---------------------------------------------------------------------------
# Phase 1 — Genre style guide
# ---------------------------------------------------------------------------

PHASE_1_TEMPLATE = """\
PHASE 1: STYLE GUIDE

GENRE: {genre}

Write a prescriptive style guide for writing a speculative short story in the
tradition of [GENRE]. Imagine you will use this guide to write such a story
after receiving only a premise. What makes a story recognizably of this mode?
Its characteristic concerns, tonal range, relationship to worldbuilding and
exposition, pacing, typical shapes? What does a good story in this mode give
the reader that other modes don't?

The guide MUST include a section on FAILURE MODES: specific ways a [GENRE]
story can go wrong. What does a bad [GENRE] pastiche look like? What traps
does the mode set for an imitator? Most importantly: what tendencies in AI
writing are especially dangerous when combined with [GENRE]'s characteristic
moves?

{narrow_genre_clause}

Remember the hard constraints: the AI in this story, if present at all, is
structurally kind. Your style guide should name how [GENRE]'s characteristic
moves intersect with this constraint — which of the mode's typical conflicts
still work, which need reshaping, which human-AI conflict shapes from the
canon map best onto the mode.

Output the style guide as Markdown. No <winner> tag needed — the whole
response is the guide.
"""

PHASE_1_NARROW_NO_SEARCH = """\
If [GENRE] is narrowly defined (a microgenre, a small scene, a movement
defined by a handful of people or publications) and you cannot generate a
reliable guide from what you know, say so explicitly and list the reference
material you would need. Do not fabricate plausible-sounding content that
misses the mode.\
"""

PHASE_1_NARROW_WITH_SEARCH = """\
You have access to the openrouter:web_search tool. If [GENRE] is narrowly
defined (a microgenre, a small scene, a movement defined by a handful of
people or publications), use web search to ground the guide in real
references — named authors, publications, anthologies, manifestos, story
titles. Prefer Wikipedia, academic sources, and primary sources over
SEO-heavy commercial pages. If after searching you still cannot generate a
reliable guide, say so explicitly and list what additional material you
would need. Do not fabricate plausible-sounding content that misses the
mode.\
"""


def phase_1(client: LLMClient, state: PipelineState, args: argparse.Namespace) -> None:
    path = phase_file(state, 1, "style_guide")
    cached = maybe_skip(path, args.force, "Phase 1")
    if cached is not None:
        state.genre_style_guide = cached
        return

    use_web_search = args.web_search and args.provider == "openrouter"
    narrow_clause = (
        PHASE_1_NARROW_WITH_SEARCH if use_web_search else PHASE_1_NARROW_NO_SEARCH
    )
    log(
        f"Phase 1: generating genre style guide"
        + (" (web search enabled)" if use_web_search else "")
    )
    system = build_system_prompt(state, "Phase 1: Style Guide")
    user = PHASE_1_TEMPLATE.format(
        genre=state.genre,
        narrow_genre_clause=narrow_clause,
    )
    out = client.complete(
        system,
        user,
        max_tokens=args.max_tokens,
        enable_web_search=use_web_search,
    )
    save_text(path, out)
    state.genre_style_guide = out


# ---------------------------------------------------------------------------
# Phase 2 — SEED
# ---------------------------------------------------------------------------

PHASE_2_INFLATE_TEMPLATE_NO_SEARCH = """\
PHASE 2: SEED GENERATION (Step 2 — filter and inflate)

A dictionary draw produced these ten candidate words:

{words}

Your job:

1. Keep any word whose meaning points to a concept, event, phenomenon, object,
   discipline, or person. Discard words that only describe manner or degree
   (most adverbs), and function words. Do not reroll or substitute. Thin SEEDs
   are acceptable.

2. For each surviving word, INFLATE it into something specific — a named
   person, place, phenomenon, event, object, or discipline — from your own
   knowledge. The connection to the original word must be legible in one hop.
   If a word has no strong specific referent you can name confidently, discard
   it rather than forcing a weak inflation.

(The original template uses a web search here; you are inflating from internal
knowledge instead. Discard rather than guess.)

Output EXACTLY this Markdown format, nothing else:

SEED for this run:
- <original word> → <inflated concept>
- <original word> → <inflated concept>
- <original word> → [discarded — reason]
...

Then reproduce the final SEED inside <winner>...</winner> tags.
"""

PHASE_2_INFLATE_TEMPLATE_WITH_SEARCH = """\
PHASE 2: SEED GENERATION (Step 2 — filter and inflate, with web search)

A dictionary draw produced these ten candidate words:

{words}

Your job:

1. Keep any word whose meaning points to a concept, event, phenomenon, object,
   discipline, or person. Discard words that only describe manner or degree
   (most adverbs), and function words. Do not reroll or substitute. Thin SEEDs
   are acceptable.

2. For each surviving word, run ONE web search using the openrouter:web_search
   tool, and INFLATE it into something specific — a named person, place,
   phenomenon, event, object, or discipline — using the most conceptually
   specific result the search returns. The connection to the original word
   must be legible in one hop. Prefer Wikipedia articles, named entities, or
   established concepts; avoid commercial or SEO-heavy results. If a search
   yields nothing beyond a generic dictionary definition, discard the word
   rather than forcing a weak inflation.

Budget: aim for roughly one search per surviving word. The server will cap
total searches regardless.

Output EXACTLY this Markdown format, nothing else:

SEED for this run:
- <original word> → <inflated concept>
- <original word> → <inflated concept>
- <original word> → [discarded — reason]
...

Then reproduce the final SEED inside <winner>...</winner> tags.
"""

PHASE_2_USER_SEED_TEMPLATE = """\
PHASE 2: SEED GENERATION (user-supplied)

The user has supplied this SEED directly ({n_chars} Unicode characters,
under the 280-char limit):

{seed}

Display it cleanly as:

SEED for this run:
<seed>

Then reproduce the SEED inside <winner>...</winner> tags.
"""


def phase_2(client: LLMClient, state: PipelineState, args: argparse.Namespace) -> None:
    path = phase_file(state, 2, "seed")
    cached = maybe_skip(path, args.force, "Phase 2")
    if cached is not None:
        state.seed = extract_winner_or_fallback(cached, "Phase 2")
        return

    use_web_search = False  # Only relevant on the dictionary path below.

    if state.seed_input is not None:
        if len(state.seed_input) > 280:
            raise SystemExit(
                f"--seed is {len(state.seed_input)} Unicode chars, over the 280 limit. "
                "Shorten it or drop --seed to use a dictionary draw."
            )
        log(f"Phase 2: using user-supplied SEED ({len(state.seed_input)} chars)")
        system = build_system_prompt(state, "Phase 2: SEED")
        user = PHASE_2_USER_SEED_TEMPLATE.format(
            n_chars=len(state.seed_input),
            seed=state.seed_input,
        )
    else:
        use_web_search = args.web_search and args.provider == "openrouter"
        log(
            "Phase 2: drawing dictionary words"
            + (" (web search enabled)" if use_web_search else "")
        )
        words, source = draw_dictionary_words(n=10, min_len=5)
        log(f"Phase 2: drew from {source}: {', '.join(words)}")
        system = build_system_prompt(state, "Phase 2: SEED")
        template = (
            PHASE_2_INFLATE_TEMPLATE_WITH_SEARCH
            if use_web_search
            else PHASE_2_INFLATE_TEMPLATE_NO_SEARCH
        )
        user = template.format(words="\n".join(f"- {w}" for w in words))

    out = client.complete(
        system,
        user,
        max_tokens=args.max_tokens,
        enable_web_search=use_web_search,
    )
    save_text(path, out)
    state.seed = extract_winner_or_fallback(out, "Phase 2")


# ---------------------------------------------------------------------------
# Phase 3 — Conflict
# ---------------------------------------------------------------------------

PHASE_3_TEMPLATE = """\
PHASE 3: CONFLICT GENERATION

GENRE: {genre}
TARGET STORY LENGTH: {length}

Genre style guide from Phase 1:
---
{style_guide}
---

SEED from Phase 2:
---
{seed}
---

STEP 1 — Generate 30 potential conflicts for a [GENRE] short story of
[LENGTH]. Constraints:

  - Each conflict must take AT LEAST TWO SEED items as LOAD-BEARING elements.
    If you removed both, the conflict should no longer make sense.
  - Every story takes place in a world where the AI is structurally kind (see
    hard constraints). Some conflicts put an AI at the center; others push it
    to the background as a world-condition. Both modes are welcome, and the AI
    need not be a personified character at all.
  - Invent names for any fictional AIs. Do not use real AI system/company
    names.
  - Diversity discipline: vary setting, scale, register, and which SEED items
    carry the weight. The first 10 and the last 10 should not feel like
    siblings.

For each conflict, give:
  - A 2–4 sentence description.
  - Which SEED items are load-bearing.
  - A rating, 1–5 stars, on plausibility.
  - A rating, 1–5 stars, on dramatic quality.

STEP 2 — Pick your top three. For each finalist, name:
  - The one thing that makes it stand out.
  - The one thing that worries you about it.
  - Which SEED items are load-bearing.

STEP 3 — Narrow to the single best. State explicitly why it beats the other
two, tied to specific qualities and specific concerns — not overall impression.
{winner_instruction}
"""


def phase_3(client: LLMClient, state: PipelineState, args: argparse.Namespace) -> None:
    path = phase_file(state, 3, "conflict")
    cached = maybe_skip(path, args.force, "Phase 3")
    if cached is not None:
        state.conflict = extract_winner_or_fallback(cached, "Phase 3")
        return

    log("Phase 3: generating 30 conflicts + selecting winner")
    system = build_system_prompt(state, "Phase 3: Conflict")
    user = PHASE_3_TEMPLATE.format(
        genre=state.genre,
        length=state.length,
        style_guide=state.genre_style_guide,
        seed=state.seed,
        winner_instruction=WINNER_INSTRUCTION,
    )
    out = client.complete(system, user, max_tokens=args.max_tokens)
    save_text(path, out)
    state.conflict = extract_winner_or_fallback(out, "Phase 3")


# ---------------------------------------------------------------------------
# Phase 4 — Plot
# ---------------------------------------------------------------------------

PHASE_4_TEMPLATE = """\
PHASE 4: PLOT GENERATION

GENRE: {genre}
TARGET STORY LENGTH: {length}

Winning conflict from Phase 3:
---
{conflict}
---

SEED (still available for inflection of setting, protagonist, or imagery):
---
{seed}
---

Generate 20 plots that make the winning conflict concrete for a [LENGTH]
short story. Each rated 1–5 stars.

These 20 plots must NOT be variations of each other. Vary along these axes:

  - Setting (time period, place, scale of world)
  - Protagonist (role, profession, relationship to the central conflict; if
    AI-centric, the protagonist's relationship to the AI)
  - Register (tragic, comic, noir, procedural, intimate, epic, absurd)
  - Entry point (which moment in the conflict's timeline the narrative begins)
  - Stakes (personal, communal, civilizational)
  - AI presence (foregrounded as character, mid-ground as force, or background
    as world-condition)

If three or more candidates cluster along any axis, break the cluster
deliberately by pushing later candidates to the edges of that axis. Plot #20
should not feel like a sibling of plot #1.

Pick your top three. For each: one thing that makes it stand out, one thing
that worries you about it.

Narrow to the single best, tied to specifics.
{winner_instruction}
"""


def phase_4(client: LLMClient, state: PipelineState, args: argparse.Namespace) -> None:
    path = phase_file(state, 4, "plot")
    cached = maybe_skip(path, args.force, "Phase 4")
    if cached is not None:
        state.plot = extract_winner_or_fallback(cached, "Phase 4")
        return

    log("Phase 4: generating 20 plots + selecting winner")
    system = build_system_prompt(state, "Phase 4: Plot")
    user = PHASE_4_TEMPLATE.format(
        genre=state.genre,
        length=state.length,
        conflict=state.conflict,
        seed=state.seed,
        winner_instruction=WINNER_INSTRUCTION,
    )
    out = client.complete(system, user, max_tokens=args.max_tokens)
    save_text(path, out)
    state.plot = extract_winner_or_fallback(out, "Phase 4")


# ---------------------------------------------------------------------------
# Phase 5 — Structure
# ---------------------------------------------------------------------------

PHASE_5_TEMPLATE = """\
PHASE 5: STRUCTURE SELECTION

TARGET STORY LENGTH: {length}

Winning plot from Phase 4:
---
{plot}
---

Plan the story's formal architecture. By "structure" we mean the shape of the
reader's experience: what order events arrive in, what's withheld and when,
where the reader's understanding shifts, the relationship between story time
and discourse time. NOT a scene list — that is Phase 6.

A structure candidate must be describable in 2–3 sentences using
narrative-theory terms WITHOUT naming any specific character or plot event.
If a candidate mentions a character name or specific incident, it has leaked
into outline territory — rewrite it at the structural level.

Example structure candidate:
  "The story opens in the aftermath of the central event, then fragments
  backward through three non-chronological time layers that converge on the
  triggering moment. First-person retrospective narration, with the narrator
  unaware of crucial information the reader pieces together."

Generate 20 candidates. Each rated 1–5 stars. Vary along:

  - Entry point (in medias res, from the end, from long before, etc.)
  - Temporal shape (linear, fragmented, frame narrative, parallel timelines,
    compressed, dilated)
  - Withholding strategy (what the reader doesn't know and when they learn it)
  - Point of view and distance (close third, distant third, first, second,
    epistolary, collective)

If candidates cluster on chronological narration with a late reveal (the
default), deliberately push some toward less comfortable shapes.

Pick top three. For each: one thing that makes it stand out, one thing that
worries you. Narrow to the single best.
{winner_instruction}
"""


def phase_5(client: LLMClient, state: PipelineState, args: argparse.Namespace) -> None:
    path = phase_file(state, 5, "structure")
    cached = maybe_skip(path, args.force, "Phase 5")
    if cached is not None:
        state.structure = extract_winner_or_fallback(cached, "Phase 5")
        return

    log("Phase 5: generating 20 structures + selecting winner")
    system = build_system_prompt(state, "Phase 5: Structure")
    user = PHASE_5_TEMPLATE.format(
        length=state.length,
        plot=state.plot,
        winner_instruction=WINNER_INSTRUCTION,
    )
    out = client.complete(system, user, max_tokens=args.max_tokens)
    save_text(path, out)
    state.structure = extract_winner_or_fallback(out, "Phase 5")


# ---------------------------------------------------------------------------
# Phase 6 — Outline
# ---------------------------------------------------------------------------

PHASE_6_TEMPLATE = """\
PHASE 6: OUTLINE GENERATION

TARGET STORY LENGTH: {length}

Winning plot from Phase 4:
---
{plot}
---

Winning structure from Phase 5:
---
{structure}
---

Produce beat-by-beat scene plans. Where Phase 5 decided the SHAPE of the
reader's experience, this phase decides the CONTENT: specific scenes in
specific order, who's in them, what happens, rough word allotment per scene,
candidate last lines.

An outline candidate is a numbered list of scene beats with enough detail that
another writer could execute from it. Distribute word allotments to sum to
about [LENGTH].

Example outline beat:
  "Scene 3 (≈400 words): Maya returns to the clinic at night. Aide-7 is
  already waiting. The conversation she's been rehearsing for weeks collapses
  in the first minute. Ends on her asking the question she'd sworn not to ask."

Generate 10 outline candidates that all honor the winning structure. Each
rated 1–5 stars. Vary:
  - Which characters carry which scenes.
  - Where dialogue lands vs. where narration takes over.
  - The specific images and details that anchor each beat.
  - What the final image does.

Same thematic destination, different paths to it. Break clusters if you see
them (same scene count, same beat distribution, same final image).

IMPORTANT LEGIBILITY CHECK: If an outline has more scene beats than [LENGTH]
can comfortably accommodate, the downstream prose will compress into
fragmentation. Prefer fewer scenes told legibly over many scenes crammed in.

Pick top three. For each: one thing that makes it stand out, one thing that
worries you. Flag any outline already accumulating Unslop patterns at the
planning stage (performed profundity, signposted conclusions, fractal
summaries). Narrow to the single best.
{winner_instruction}
"""


def phase_6(client: LLMClient, state: PipelineState, args: argparse.Namespace) -> None:
    path = phase_file(state, 6, "outline")
    cached = maybe_skip(path, args.force, "Phase 6")
    if cached is not None:
        state.outline = extract_winner_or_fallback(cached, "Phase 6")
        return

    log("Phase 6: generating 10 outlines + selecting winner")
    system = build_system_prompt(state, "Phase 6: Outline")
    user = PHASE_6_TEMPLATE.format(
        length=state.length,
        plot=state.plot,
        structure=state.structure,
        winner_instruction=WINNER_INSTRUCTION,
    )
    out = client.complete(system, user, max_tokens=args.max_tokens)
    save_text(path, out)
    state.outline = extract_winner_or_fallback(out, "Phase 6")


# ---------------------------------------------------------------------------
# Phase 7 — Story (5 variants + synthesis)
# ---------------------------------------------------------------------------

PHASE_7_VARIANT_TEMPLATE = """\
PHASE 7: STORY GENERATION — VARIANT {variant_index} of 5

GENRE: {genre}
TARGET STORY LENGTH: {length}

Genre style guide from Phase 1 (honor its failure-mode section — those modes
are most likely to surface HERE, during full prose):
---
{style_guide}
---

Winning outline from Phase 6:
---
{outline}
---

Write ONE complete story of [LENGTH], executing the outline.

State at the very top of your response, on a single line, a distinct named
FLAVOR for this variant describing its voice, pacing, and tonal strategy.
Example: "FLAVOR: close-third, present tense, austere diction, emphasis on
physical procedure over interiority."

Variant {variant_index} should be genuinely different from a baseline
execution of this outline. {risk_clause}

Hold the Unslop style guide in mind throughout. Hold the genre style guide's
failure modes in mind. Watch the legibility floor — choose legibility over
compression.

Do NOT include a <winner> tag. This is one variant; the chooser comes later.

Format:

FLAVOR: <your flavor statement>

<the complete story, in Markdown, no title needed>
"""

# Variants 1–3: grounded. Variants 4–5: take a creative risk.
RISK_CLAUSES = [
    "Aim for a grounded, confident execution. Make your strongest version of the outline with no unusual stylistic gambits.",
    "Aim for a grounded execution that leans into the outline's quieter beats. Find the human particulars.",
    "Aim for a grounded execution that takes the outline's tonal register to one edge — bleaker, funnier, colder, or warmer — but keeps the shape.",
    "Take a creative risk you are NOT fully confident will land: a tonal choice, a structural move within a scene, or an unusual voice. Commit to it.",
    "Take a different creative risk: an ending that does not resolve cleanly, or a structural experiment within a scene (second person, collective voice, a scene told in an unusual form). Commit to it.",
]

PHASE_7_SYNTHESIS_TEMPLATE = """\
PHASE 7: STORY GENERATION — SELECTION

GENRE: {genre}
TARGET STORY LENGTH: {length}

Below are five complete story variants, each executing the same outline with a
different flavor. Read all five. Then:

1. Pick your top three. For each finalist, name:
   - The one thing that makes it stand out.
   - The one thing that worries you about it.
2. Narrow to the single best, tied to specific qualities and specific concerns
   — not overall impression.

{winner_instruction}

Reproduce the full chosen story verbatim inside the <winner>...</winner> tags
(including the FLAVOR line). Do not abbreviate.

--- VARIANT 1 ---
{v1}

--- VARIANT 2 ---
{v2}

--- VARIANT 3 ---
{v3}

--- VARIANT 4 ---
{v4}

--- VARIANT 5 ---
{v5}
"""


def phase_7(client: LLMClient, state: PipelineState, args: argparse.Namespace) -> None:
    variants: list[str] = []
    for i in range(1, 6):
        vpath = phase_file(state, 7, f"variant_{i}")
        cached = maybe_skip(vpath, args.force, f"Phase 7 variant {i}")
        if cached is not None:
            variants.append(cached)
            continue

        log(f"Phase 7: writing variant {i}")
        system = build_system_prompt(state, f"Phase 7: Story (variant {i})")
        user = PHASE_7_VARIANT_TEMPLATE.format(
            variant_index=i,
            genre=state.genre,
            length=state.length,
            style_guide=state.genre_style_guide,
            outline=state.outline,
            risk_clause=RISK_CLAUSES[i - 1],
        )
        out = client.complete(
            system,
            user,
            max_tokens=story_scale_max_tokens(args),
        )
        save_text(vpath, out)
        variants.append(out)

    syn_path = phase_file(state, 7, "synthesis")
    cached = maybe_skip(syn_path, args.force, "Phase 7 synthesis")
    if cached is not None:
        state.story = extract_winner_or_fallback(cached, "Phase 7 synthesis")
        return

    log("Phase 7: synthesis — picking winning variant")
    system = build_system_prompt(state, "Phase 7: Story Selection")
    user = PHASE_7_SYNTHESIS_TEMPLATE.format(
        genre=state.genre,
        length=state.length,
        winner_instruction=WINNER_INSTRUCTION,
        v1=variants[0],
        v2=variants[1],
        v3=variants[2],
        v4=variants[3],
        v5=variants[4],
    )
    # Synthesis must hold the chosen full story in its output plus the
    # top-three analysis. Use the story-scale cap.
    out = client.complete(
        system,
        user,
        max_tokens=story_scale_max_tokens(args),
    )
    save_text(syn_path, out)
    state.story = extract_winner_or_fallback(out, "Phase 7 synthesis")


# ---------------------------------------------------------------------------
# Phase 8 — Revision
# ---------------------------------------------------------------------------

PHASE_8_TEMPLATE = """\
PHASE 8: REVISION

GENRE: {genre}
TARGET STORY LENGTH: {length}

Genre style guide from Phase 1 (use its failure-mode section as an audit lens):
---
{style_guide}
---

Draft from Phase 7 to be revised:
---
{story}
---

Do not defend the original prose. If a flag is valid, fix it; if a flag is
invalid, cut the flag from the audit rather than arguing for the prose you
already wrote.

1. NAME THE ONE THING. The single most important observation about this draft.
   Where is it alive and where is it dead? What ONE fix would improve the
   whole piece the most? Be specific — point to a passage, a scene, a
   structural choice. THIS GOVERNS THE REWRITE.

2. AUDIT the draft in one pass. For each flag, QUOTE the passage and state
   which lens caught it. Don't flag the same passage under multiple lenses.
   Lenses:
     - Unslop patterns (contaminated vocabulary; structural tics; eyeball-kick
       saturation; compulsive personification; fractal summaries; signposted
       conclusions; performed profundity; tonal monotony; em-dash overuse;
       negative parallelism; dramatic countdowns; self-answered rhetorical
       questions; list-of-three defaults; anaphora abuse; superficial trailing
       analyses; false ranges; filler transitions).
     - Genre-voice slippage against the Phase 1 style guide, including its
       failure-mode section.
     - Legibility failures where compression has crossed into fragmentation
       (missing articles or connectives, orphaned pronouns, scenes without
       anchoring detail, elided actions the reader must infer from context
       the text does not provide).
     - Regression to default at moments that were surprising in the draft and
       got sanded flat, or places where the prose slid toward the mean.

3. LENGTH CHECK. Confirm the draft is within [LENGTH]. If under, identify
   where the story needs more room. If over, identify what to cut. If within
   range, say so.

4. REWRITE the story in full, informed by the audit. Lead with the area the
   one thing identified. Place the full revised story inside
   <revised_story>...</revised_story> tags.

5. CHANGELOG. For the 5–7 most substantive edits, quote the original passage
   and its replacement side by side. For minor edits, list them briefly by
   location without quoting. If any audit flag was cut as invalid, note it and
   say why.

Your response should contain, in order:
  - THE ONE THING
  - AUDIT
  - LENGTH CHECK
  - <revised_story>...</revised_story>
  - CHANGELOG
"""


def phase_8(client: LLMClient, state: PipelineState, args: argparse.Namespace) -> None:
    path = phase_file(state, 8, "revision")
    cached = maybe_skip(path, args.force, "Phase 8")
    if cached is not None:
        state.revised_story = (
            extract_tagged(cached, "revised_story") or state.story
        )
        if not state.revised_story:
            raise SystemExit("Phase 8 cache has no <revised_story> tag — rerun with --force.")
        return

    log("Phase 8: revising")
    system = build_system_prompt(state, "Phase 8: Revision")
    user = PHASE_8_TEMPLATE.format(
        genre=state.genre,
        length=state.length,
        style_guide=state.genre_style_guide,
        story=state.story,
    )
    out = client.complete(
        system,
        user,
        max_tokens=story_scale_max_tokens(args),
    )
    save_text(path, out)
    revised = extract_tagged(out, "revised_story")
    if not revised:
        log("WARNING: Phase 8: no <revised_story> tag — falling back to full output.")
        revised = out.strip()
    state.revised_story = revised


# ---------------------------------------------------------------------------
# Phase 9 — Export
# ---------------------------------------------------------------------------

PHASE_9_TEMPLATE = """\
PHASE 9: EXPORT METADATA

Below is the final revised story. Produce two things:

1. A TITLE. Inside <title>...</title>. No quotes around it, no "A Story by"
   framing, just the title.

2. An ABSTRACT. Inside <abstract>...</abstract>. 80–150 words. Neutral,
   descriptive summary: what the story is about, who the main characters are,
   what happens, what kind of ending it reaches. Present tense, third person.
   No evaluative language. No rhetorical flourishes. Do NOT withhold the
   ending for effect — this is an abstract, not a blurb. The Unslop style
   guide applies here AS STRICTLY as it does in the story. Abstracts are a
   concentrated site of AI-patterned prose — no "delves into," no "explores
   themes of," no "raises questions about," no lists of three.

Story:
---
{story}
---
"""


def phase_9(client: LLMClient, state: PipelineState, args: argparse.Namespace) -> None:
    meta_path = phase_file(state, 9, "export_metadata")
    final_path = state.output_dir / "story.md"

    cached = maybe_skip(meta_path, args.force, "Phase 9 metadata")
    if cached is not None:
        state.title = extract_tagged(cached, "title") or "Untitled"
        state.abstract = extract_tagged(cached, "abstract") or ""
    else:
        log("Phase 9: generating title and abstract")
        system = build_system_prompt(state, "Phase 9: Export")
        user = PHASE_9_TEMPLATE.format(story=state.revised_story)
        out = client.complete(system, user, max_tokens=args.max_tokens)
        save_text(meta_path, out)
        title = extract_tagged(out, "title")
        abstract = extract_tagged(out, "abstract")
        if not title:
            log("WARNING: Phase 9: no <title> tag; defaulting to 'Untitled'.")
            title = "Untitled"
        if not abstract:
            raise SystemExit(
                "Phase 9: no <abstract> tag in model output. Re-run with --force."
            )
        state.title = title
        state.abstract = abstract

    final = (
        f"# {state.title}\n\n"
        f"## Abstract\n\n"
        f"{state.abstract}\n\n"
        f"## Story\n\n"
        f"{state.revised_story}\n"
    )
    save_text(final_path, final)
    log(f"Final story written to {final_path}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description=(
            "Speculative fiction short story pipeline. Runs the nine-phase "
            "pipeline from story-pipeline-template-baseline-v4.3.md against "
            "either the Anthropic API or OpenRouter."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    # Story parameters
    p.add_argument(
        "--genre",
        required=True,
        help="Genre, subgenre, movement, or 'in the tradition of [author]'.",
    )
    p.add_argument(
        "--length",
        required=True,
        help='Target word count range, e.g. "2000-3000 words".',
    )
    p.add_argument(
        "--seed",
        default=None,
        help=(
            "Optional tweet-length SEED (≤280 Unicode chars). If omitted, "
            "Phase 2 draws dictionary words and inflates them."
        ),
    )

    # Inputs
    p.add_argument(
        "--unslop-guide",
        default="unslop-style-guide.md",
        help="Path to the Unslop style guide markdown file.",
    )
    p.add_argument(
        "--output-dir",
        default="./pipeline-run",
        help="Directory for phase outputs and the final story.md.",
    )
    p.add_argument(
        "--force",
        action="store_true",
        help="Re-run all phases, overwriting cached output files.",
    )
    p.add_argument(
        "--verbose",
        action="store_true",
        help=(
            "Log each OpenRouter HTTP request and response to stderr, with "
            "the Authorization token redacted. OpenRouter only — Anthropic "
            "calls go through the SDK and are not intercepted."
        ),
    )

    # Provider selection
    p.add_argument(
        "--provider",
        choices=["anthropic", "openrouter"],
        default="anthropic",
        help="LLM provider.",
    )
    p.add_argument(
        "--model",
        default=None,
        help=(
            "Model identifier. Defaults: anthropic → 'claude-opus-4-7'; "
            "openrouter → 'anthropic/claude-opus-4'."
        ),
    )
    p.add_argument(
        "--api-key",
        default=None,
        help=(
            "API key. Falls back to ANTHROPIC_API_KEY or OPENROUTER_API_KEY "
            "env vars depending on --provider."
        ),
    )
    p.add_argument(
        "--temperature",
        type=float,
        default=1.0,
        help="Sampling temperature (default: 1.0).",
    )
    p.add_argument(
        "--reasoning-effort",
        choices=["none", "minimal", "low", "medium", "high", "xhigh"],
        default="medium",
        help=(
            "Reasoning effort level (default: medium). OpenRouter: passed as "
            "`reasoning: {effort: <level>}` per the unified reasoning API; "
            "models that don't support reasoning ignore it. Anthropic: "
            "translated to `thinking: {type: enabled, budget_tokens: N}` "
            "with a fixed budget per level (minimal=1024, low=2048, "
            "medium=4096, high=8192, xhigh=16384). On Anthropic, enabling "
            "thinking auto-bumps max_tokens if needed (budget + 4k headroom) "
            "and omits temperature (required — thinking is incompatible with "
            "temperature modifications). `none` disables reasoning entirely."
        ),
    )
    p.add_argument(
        "--max-tokens",
        type=int,
        default=None,
        help=(
            "Cap on tokens per response. OpenRouter: unset means the provider "
            "picks its default (field is omitted from the request body). "
            "Anthropic: required by the API — unset falls back to 8192 "
            "internally. Set explicitly to enforce a tighter cap or to raise "
            "it on Anthropic for long outputs."
        ),
    )
    p.add_argument(
        "--story-max-tokens",
        type=int,
        default=None,
        help=(
            "Separate cap for full-story calls (Phase 7 variants and "
            "synthesis, Phase 8 rewrite). Same omit-vs-fallback semantics as "
            "--max-tokens. On Anthropic, bump this for long targets — e.g. "
            "--story-max-tokens 16000 for a 3000-word story plus revision "
            "commentary. Falls back to --max-tokens if that is set and this "
            "is not."
        ),
    )
    p.add_argument(
        "--web-search",
        action="store_true",
        help=(
            "Enable the openrouter:web_search server tool for Phase 1 (ground "
            "references for obscure genres) and Phase 2 (inflate dictionary "
            "words via search, matching the template's original intent). "
            "OpenRouter only — ignored with --provider anthropic. The tool is "
            "configured with max_results=3 per search and max_total_results=15 "
            "per call for cost control; edit _web_search_tool_spec() to change."
        ),
    )

    # Phase selection
    p.add_argument(
        "--phases",
        default="1-9",
        help=(
            'Which phases to run, e.g. "1-9", "3-7", "8,9". Requires cached '
            "outputs for any prior phase not in the range."
        ),
    )

    return p


def parse_phases(spec: str) -> list[int]:
    out: set[int] = set()
    for part in spec.split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            a, b = part.split("-", 1)
            out.update(range(int(a), int(b) + 1))
        else:
            out.add(int(part))
    valid = [n for n in sorted(out) if 1 <= n <= 9]
    if not valid:
        raise SystemExit(f"No valid phases parsed from --phases {spec!r}")
    return valid


def default_model(provider: str) -> str:
    return {
        "anthropic": "claude-opus-4-7",
        "openrouter": "anthropic/claude-opus-4",
    }[provider]


def load_prior_winners(state: PipelineState, phases_to_run: list[int]) -> None:
    """For any phase NOT in phases_to_run, load cached winner from disk."""
    if 1 not in phases_to_run:
        p = phase_file(state, 1, "style_guide")
        if p.exists():
            state.genre_style_guide = load_text(p)
    if 2 not in phases_to_run:
        p = phase_file(state, 2, "seed")
        if p.exists():
            state.seed = extract_winner_or_fallback(load_text(p), "Phase 2")
    if 3 not in phases_to_run:
        p = phase_file(state, 3, "conflict")
        if p.exists():
            state.conflict = extract_winner_or_fallback(load_text(p), "Phase 3")
    if 4 not in phases_to_run:
        p = phase_file(state, 4, "plot")
        if p.exists():
            state.plot = extract_winner_or_fallback(load_text(p), "Phase 4")
    if 5 not in phases_to_run:
        p = phase_file(state, 5, "structure")
        if p.exists():
            state.structure = extract_winner_or_fallback(load_text(p), "Phase 5")
    if 6 not in phases_to_run:
        p = phase_file(state, 6, "outline")
        if p.exists():
            state.outline = extract_winner_or_fallback(load_text(p), "Phase 6")
    if 7 not in phases_to_run:
        p = phase_file(state, 7, "synthesis")
        if p.exists():
            state.story = extract_winner_or_fallback(load_text(p), "Phase 7")
    if 8 not in phases_to_run:
        p = phase_file(state, 8, "revision")
        if p.exists():
            state.revised_story = extract_tagged(load_text(p), "revised_story") or ""


def main() -> None:
    args = build_parser().parse_args()
    phases_to_run = parse_phases(args.phases)

    unslop_path = Path(args.unslop_guide)
    if not unslop_path.exists():
        raise SystemExit(
            f"Unslop style guide not found at {unslop_path}. "
            "Pass --unslop-guide pointing to unslop-style-guide.md."
        )
    unslop_text = load_text(unslop_path)

    model = args.model or default_model(args.provider)
    client = LLMClient(
        provider=args.provider,
        model=model,
        api_key=args.api_key,
        temperature=args.temperature,
        verbose=args.verbose,
        reasoning_effort=args.reasoning_effort,
    )
    log(f"Using {args.provider} / {model} (reasoning: {args.reasoning_effort})")
    if args.verbose:
        if args.provider == "openrouter":
            log("Verbose HTTP logging enabled (stderr, token redacted).")
        else:
            log(
                "NOTE: --verbose only affects OpenRouter HTTP calls in this "
                "script; Anthropic SDK calls are not intercepted."
            )
    if args.web_search:
        if args.provider == "openrouter":
            log("Web search enabled (Phase 1 + Phase 2 dictionary branch).")
        else:
            log(
                "WARNING: --web-search is OpenRouter-only in this script; "
                "ignored for --provider anthropic."
            )

    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    state = PipelineState(
        output_dir=out_dir,
        genre=args.genre,
        length=args.length,
        seed_input=args.seed,
        unslop_guide=unslop_text,
    )

    # Load any phases we're skipping from cache
    load_prior_winners(state, phases_to_run)

    phase_fns = {
        1: phase_1,
        2: phase_2,
        3: phase_3,
        4: phase_4,
        5: phase_5,
        6: phase_6,
        7: phase_7,
        8: phase_8,
        9: phase_9,
    }

    for n in phases_to_run:
        # Dependency guard — fail loudly if a required prior winner is empty.
        required = {
            2: [],
            3: [("genre_style_guide", "Phase 1"), ("seed", "Phase 2")],
            4: [("conflict", "Phase 3"), ("seed", "Phase 2")],
            5: [("plot", "Phase 4")],
            6: [("plot", "Phase 4"), ("structure", "Phase 5")],
            7: [("genre_style_guide", "Phase 1"), ("outline", "Phase 6")],
            8: [("genre_style_guide", "Phase 1"), ("story", "Phase 7")],
            9: [("revised_story", "Phase 8")],
        }.get(n, [])
        for attr, produced_by in required:
            if not getattr(state, attr):
                raise SystemExit(
                    f"Phase {n} requires output from {produced_by} but "
                    f"state.{attr} is empty. Run earlier phases first or "
                    f"check {state.output_dir} for cached files."
                )
        phase_fns[n](client, state, args)


if __name__ == "__main__":
    main()
