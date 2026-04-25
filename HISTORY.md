# History

The pipeline arrived at its current shape over four weeks and three lineages.
This file traces what changed and why, and indexes the eighteen hand-driven
runs that drove the revisions.

## 0. Trial — `trial.md` (March 30)

A single conversation with Claude Opus 4.6: *"What guide about Ellison-like
fiction would you write for yourself, given a futurology constraint that the
AI must be human-loving and unfailingly kind?"* The output covers Ellison's
DNA (system-as-sadist, rage as moral clarity, voice-as-character), then
proposes how a benevolent-AI constraint reshapes Ellison-shaped opportunities
rather than removing them. No automation, no template — but the trial fixed
the project's two persistent ideas: (1) the AI's kindness is a property of
its construction, not a restraint; (2) the writer-model can use its own
constitution as material for its fictional descendants.

## 1. The Unslop style guide — `style-guide/` (April 11)

Before any pipeline work, Opus read seven external sources on AI prose tells
and produced `unslop-style-guide.md`. Part I synthesizes nostalgebraist's
"crammed prose" diagnosis, Reinhart's register-collapse finding, Robbins's
absent-temporal-withholding observation, and Makin's self-poisoning context
drift into ten structural principles. Part II is the kill list: cursed
vocabulary, structural tics, eyeball-kick saturation, dialogue tells, tonal
patterns. Every subsequent phase of the pipeline carries this guide in
context as a hard constraint, and it is used as the audit lens during
revision.

## 2. First runs and first automation — `pipeline/1-initial/`, runs 01–02 (April 11–13)

Two automation attempts went out the door together. **`storyforge.sh`**
([`runs/01/storyforge.sh`](runs/01/storyforge.sh)) was a Bash harness
around the Claude Code CLI: six phases (style guide → 30 conflicts → 20
plots → 20 structures → 20 outlines → 10 stories), each a single non-resumed
`claude -p` call with the full prior context inlined. It worked, but the
funnel-in-one-call structure made interactive steering awkward and 10 full
stories per run produced ~20K words of output where quality degraded across
the set. The companion artifact was a hand-driven Claude Projects template
(`runs/01/story-pipeline-template.md`), six phases mirroring the script.

Run 01 used both. Output: **The Toy** ([`runs/01/`](runs/01/)). Ten
candidate openings under named flavors are preserved in
[`the-toy-versions.md`](runs/01/the-toy-versions.md).

Run 02 produced **Last Call** ([`runs/02/`](runs/02/)) using the v2
template ([`runs/02/story-pipeline-template-v2.md`](runs/02/story-pipeline-template-v2.md)),
which added three things motivated by run 01's failures:

- A **failure-modes section** in the Phase 1 style guide, naming how AI
  defaults interact dangerously with the chosen author's voice (Ellison's
  big rhetorical gestures merging with AI-performed profundity; Le Guin's
  anthropological distance merging with cod-anthropology; etc.).
- A **summarize-then-generate** split in the conflict phase, so the long
  source articles don't pollute downstream context.
- **Phase 6 split into openings + one full draft**, replacing the original
  "10 full stories" approach.
- A **revision phase** (Phase 7), where the model audits the draft against
  both the genre style guide and the unslop guide, and rewrites in full
  with a changelog.

`runs/02/last-call-revised.md` is a manually expanded version of the
v2-revised story; the abstract-equipped final lives at `runs/02/story.md`.

## 3. The Nix critic-persona experiment — `pipeline/2-critic/`, runs 04–05 (April 12–14)

The hypothesis: the same voice that generates candidates is biased toward
its own defaults, so selection should happen in a different voice. Three
template versions were drafted under this premise — `-v3`, `-nix-v1`, and
`-nix-v2` — anchored by `nix.md`, a 550-word persona file describing a
critic whose primary lens is **surprise detection**: looking for lines that
don't repeat across variants, choices that cost something, moments where
the prose stops looking like the model's autopilot.

Two runs used the critic-persona pipeline. **Run 04 — *They're Fine***
([`runs/04/`](runs/04/)) used `story-pipeline-template-v3.md`. **Run 05 —
*The Obsolescence Garden*** ([`runs/05/`](runs/05/)) started with
`story-pipeline-template-nix-v1.md` and was redone with a v2 revision
pass, which is why the directory has both `transcript.md` and
`transcript-v2.md` plus the v2 final at `story-v2.md`.

After run 05 the persona approach was set aside. Nix added a category of
failure (the persona collapsing into self-congratulation, or rejecting
everything) on top of the failures the pipeline already had, and the same
discipline could be obtained more reliably from a forced rationale ("name
one thing that worries you") than from a persona switch. The artifacts
stay in [`pipeline/2-critic/`](pipeline/2-critic/) for reference, and the
surprise-detection lens survives in revised form inside the Baseline
template's audit step.

## 4. The Plain branch — runs 03 and 06–09 (April 13–21)

The non-Nix line carried forward from run 02's v2 template. **Run 03 —
*The Warm Thing*** ([`runs/03/`](runs/03/)) used the v2 template directly:
sustained child POV, the strongest of the early Plain stories.

`story-pipeline-template-plain-v2.md` and `plain-v3.md` were the next
revisions, drafted later (April 21) once the critic experiment ended. They
extend v2 (revision phase, openings split) without the Nix persona. The
label "plain" was a contrast with the critic branch — later renamed to
"baseline" once the experiment ended.

Four runs used Plain v3: **run 06 — *The Tire***, **run 07 — *Sibling***,
**run 08 — *The Last Allocation*** (the AI is the narrator and refuses to
narrate its own climax), and **run 09 — *The Grandson at the Valero***.
The Plain branch settled what the Baseline branch would build on: the
revision phase is load-bearing; openings-then-draft is the right shape for
Phase 6; the failure-modes section is a real check on bad pastiche; and
the benevolent-AI constraint produces stronger stories when the AI is one
condition of the world rather than the subject of the argument.

## 5. Baseline v3.x — runs 10–16, review 01 (April 21–22)

Three things changed at once when the line was renamed Baseline:

- **AI-as-world-condition**, made explicit. The kind AI is "a fact about
  the world the story is set in, like electricity or law." Some stories
  foreground it as a character; others push it into the background where
  it has changed the world's shape without being the subject. Both modes
  are welcome, the pipeline generates from both, and the AI need not be a
  named character at all.
- **Two-track conflict generation.** Phase 2 produces 15 AI-centric
  conflicts (Track A) and 15 human-centric conflicts in an AI-transformed
  world (Track B). Track B's discipline: removing the AI from the premise
  must break the conflict — not because the AI is the subject, but because
  the AI changed something specific about how humans live, and that
  specific thing is what humans are fighting over.
- **The "one thing stands out / one thing worries you" forcing function**,
  added to every top-three step (Phases 2–6). Top-three praise without a
  named worry collapses into vibes; named worries make the final pick
  traceable to balanced-against-each-other specifics.

A **legibility floor** was added in v3.3: at short targets the model
sometimes drops articles, connectives, and scene-anchoring detail to hit
the word count, producing prose that is technically terse and functionally
unreadable. The audit phase explicitly checks for this, and Phase 5
(outline) is told to cut beats rather than create downstream compression.

Run 10 was the first under Baseline v3.3: *Si Elena Me Hablara*. It plus
run 02 (*Last Call*), run 03 (*The Warm Thing*), run 08 (*The Last
Allocation*), and run 09 (*The Grandson at the Valero*) were among the
ten stories submitted to two cross-model reviews
([`review/01-with-abstracts.md`](review/01-with-abstracts.md),
[`review/02-without-abstracts.md`](review/02-without-abstracts.md)) by
Opus 4.7 and Kimi K2.6. The two reviewers disagreed on the leaderboard
but agreed on which stories withheld their most important moment vs.
delivered it.

Runs 11–16 used v3.3 against varied authors and Ellison's modes
(realism, fantastic, "Jeffty Is Five" register vs. "Repent, Harlequin!"
register), exposing failure modes the audit phase didn't catch (run 14's
register slippage; run 15's compression-into-fragmentation that motivated
the legibility floor's later codification).

## 6. Baseline v4 — `[GENRE]`, SEED, runs 17–18 (April 22–23)

v4 generalizes the `[AUTHOR]` setting to `[GENRE]`, accepting any
speculative mode: established traditions, microgenres, scenes, or
"in the tradition of [author]." The Phase 1 style guide is told to flag
narrow genres where it lacks training signal rather than fabricating
plausible-sounding content.

The bigger change is **Phase 2: SEED Generation**. The motivating problem:
without a concrete anchor, conflict generation drifts toward the model's
defaults regardless of how many candidates you ask for. The SEED is that
anchor. Two paths:

- **User-supplied** — a tweet-length prompt, ≤280 Unicode characters.
- **Generated** — `grep -E '^[a-z]{5,}$' /usr/share/dict/american-english-large
  | shuf -n 10` produces ten candidate words. The model filters out function
  words and pure adverbs, then runs one web search per survivor to inflate
  it into a specific named referent (a Wikipedia article, a named person,
  an established concept). Discarded words are not rerolled; thin SEEDs are
  acceptable and force each survivor to do more work.

Phase 3 (conflict generation) requires every conflict to use **at least two
SEED items as load-bearing elements** — if you remove both, the conflict
should no longer make sense. Decoration doesn't count. This is the same
discipline v3.x's Track B applied to its human-centric conflicts,
generalized.

v4.1 was the first runnable cut. **v4.2** ([`pipeline/3-baseline/parts/hyperstition-ai-good-outcomes.md`](pipeline/3-baseline/parts/hyperstition-ai-good-outcomes.md)
was added then) refined the kind-AI characterization with explicit
references to canon (Banks's Culture Minds, Stiegler's *Gentle Seduction*,
Egan's polises, Yudkowsky's CEV) — so the constraint reads as "structurally
kind, durably, in the way a river is wet" rather than "polite servant."
**v4.3** split SEED generation into a self-contained phase, so conflicts
can be regenerated without re-rolling the SEED — a cheap recovery path when
30 conflicts produce no compelling winner.

Run 17 used v4.1 (*The Fifth Prospero*). Run 18 used v4.2 to test the
effect of *removing* `claude-preferences.txt`, which had been in context
for every prior run. Same SEED and template, run twice: with prefs as
usual (*Six Hundred*), and with prefs disabled (*The Count*). Both
stories share the gregale and the village and the 1555/2067 frame, but
diverge on rendering choice and pacing.

## 7. API port — `api/story_pipeline.py` (April 24)

`api/story_pipeline.py` is a single-file Python port of the v4.3 template,
calling either the Anthropic API directly (via the SDK) or OpenRouter (via
stdlib `urllib`, since OpenRouter's server tool types don't pass the
`openai` SDK's Pydantic validation). Each phase caches its output to disk;
re-runs reuse cached files unless `--force` is passed; `--phases 7-9` runs
arbitrary slices; `--reasoning-effort xhigh` translates to `thinking:
{budget_tokens: 16384}` on Anthropic and `reasoning: {effort: "xhigh"}` on
OpenRouter. Phase 2's dictionary draw happens in Python rather than via a
bash tool call; on OpenRouter, `--web-search` enables the
`openrouter:web_search` server tool for SEED inflation, matching the
template's original intent.

Two end-to-end test runs are committed:

- [`api/test/claude-sonnet-4.6/`](api/test/claude-sonnet-4.6/) — *Wiwaxia*,
  the genre was "literary realism, near-future" with the SEED drawn from
  the dictionary path.
- [`api/test/gemini-3-flash-preview/`](api/test/gemini-3-flash-preview/) —
  *The 300-Baud Handshake*, demonstrating the OpenRouter path against a
  non-Anthropic model.

The script's deviations from the template are documented in its module
docstring: Phase 7's five variants run as five separate calls plus a
synthesis call (rather than one monolithic call) to reduce truncation
risk, and SEED inflation falls back to internal knowledge when web search
is disabled.

## Run index

| #  | Title | Template | Directory |
|----|-------|----------|-----------|
| 01 | The Toy | initial v1 | [`runs/01/`](runs/01/) |
| 02 | Last Call | v2 | [`runs/02/`](runs/02/) |
| 03 | The Warm Thing | v2 | [`runs/03/`](runs/03/) |
| 04 | They're Fine | Nix v3 | [`runs/04/`](runs/04/) |
| 05 | The Obsolescence Garden | Nix v1 → Nix v2 | [`runs/05/`](runs/05/) |
| 06 | The Tire | Plain v3 | [`runs/06/`](runs/06/) |
| 07 | Sibling | Plain v3 | [`runs/07/`](runs/07/) |
| 08 | The Last Allocation | Plain v3 | [`runs/08/`](runs/08/) |
| 09 | The Grandson at the Valero | Plain v3 | [`runs/09/`](runs/09/) |
| 10 | Si Elena Me Hablara | Baseline v3.3 | [`runs/10/`](runs/10/) |
| 11 | ORRA | Baseline v3.3 | [`runs/11/`](runs/11/) |
| 12 | The Sixty | Baseline v3.3 | [`runs/12/`](runs/12/) |
| 13 | Love in the Key of Damage | Baseline v3.3 | [`runs/13/`](runs/13/) |
| 14 | Serasht in Spring | Baseline v3.3 | [`runs/14/`](runs/14/) |
| 15 | Butter and Bone | Baseline v3.3 | [`runs/15/`](runs/15/) |
| 16 | Dream Me Something Kinder, Darling | Baseline v3.3 | [`runs/16/`](runs/16/) |
| 17 | The Fifth Prospero | Baseline v4.1 | [`runs/17/`](runs/17/) |
| 18 | The Count / Six Hundred (A/B on preferences) | Baseline v4.2 | [`runs/18/`](runs/18/) |
