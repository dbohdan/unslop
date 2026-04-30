# CLAUDE.md — Story-writing instructions for Claude Code

This repository's primary use is running the fiction pipeline. Two templates
are available; default to **Baseline v4.7** unless the user picks otherwise.
When the user asks for a story, follow the procedure below.

## Source of truth

Two pipeline templates, each paired with a style guide:

- **Default — Baseline v4.7.**
  - Template: [`pipeline/3-baseline/story-pipeline-template-baseline-v4.7.md`](pipeline/3-baseline/story-pipeline-template-baseline-v4.7.md).
  - Style guide: [`style-guide/unslop-style-guide.md`](style-guide/unslop-style-guide.md).
  - Produces speculative fiction in any genre. Documented bias toward
    domestic realism with AI as ambient infrastructure (the "Carver
    attractor" — see [HISTORY.md](HISTORY.md) §10). Use this template
    unless the user asks for the genre-only fork.
- **Genre Fiction v1.0** — the plot-direct fork.
  - Template: [`pipeline/4-genre-fiction/story-pipeline-template-genre-fiction-v1.0.md`](pipeline/4-genre-fiction/story-pipeline-template-genre-fiction-v1.0.md).
  - Style guide: [`style-guide/unslop-style-guide-sf.md`](style-guide/unslop-style-guide-sf.md).
  - Eliminates recognition-premises, defaults to scales the protagonist
    cannot fully witness, requires form-survival and a Phase 8 re-skin
    test. Use when the user asks for plot-focused genre fiction or
    explicitly wants to push past the Carver attractor.

Read each phase from the chosen template when you reach it; do not work
from memory. The selected style guide is a hard constraint at every phase
and the audit lens during Phase 8.

The Python port at [`api/story_pipeline.py`](api/story_pipeline.py) is a
reference for tooling shape (file naming, Phase 7 split) but not the
source of truth for the prompts themselves; it currently mirrors v4.3
and lags the active templates.

## Inputs to ask the user for

Before starting, get:
- **Template choice** — Baseline (default) or Genre Fiction. If the user's
  request explicitly favors one (e.g. "plot-focused genre fiction" or "in
  the literary tradition of X"), pick accordingly without asking.
- `[GENRE]` — required. Subgenre, movement, microgenre, or "in the tradition of [author]".
- `[LENGTH]` — required. e.g. "1500-3000 words".
- `[SEED]` — optional. ≤280 Unicode chars; if absent, generate one.
- Run directory name — slug for `claude-code/test/<name>/` (or `runs/NN/` for
  numbered runs once the user is ready). Suggest a default if none given.

## Run directory

Working directory for a run is `claude-code/test/<slug>/` unless the user
specifies otherwise. Numbered, blessed runs go in `runs/NN/`.

## File-naming convention

```
phase_1_style_guide.md
phase_2_seed.md
phase_3_premise.md
phase_4_plot.md
phase_5_structure.md
phase_6_outline.md
phase_7_variant_1.md           # named flavor + full story
phase_7_variant_2.md
phase_7_variant_3.md
phase_7_variant_4.md
phase_7_variant_5.md
phase_7_synthesis.md           # top-three + winner reproduced verbatim
phase_8_revision.md            # one-thing + audit + length check + rewrite + changelog
phase_9_export_metadata.md     # title + abstract
story.md                       # final, assembled
```

The earlier `phase_3_conflict.md` name (used in `claude-code/test/comic-sf-1/`
and `comic-sf-2/` and in the api script) corresponds to Baseline v4.3's
"Conflict Generation" phase. v4.6 renamed it to "Premise Generation"; both
v4.7 and Genre Fiction v1.0 inherit that name, so use `phase_3_premise.md`
for new runs.

Each phase's full output (analysis + the winner) goes in its file. Subsequent
phases need only the winning content; extract it cleanly when reading prior
phases as input.

## Per-phase guidance

### Phase 1 — Style guide for the genre
Read the template's Phase 1 prompt. Write a prescriptive style guide for
`[GENRE]` including a failure-modes section. Save to `phase_1_style_guide.md`.
If `[GENRE]` is narrow and you lack training signal, say so before
fabricating.

### Phase 2 — SEED
- **User-supplied.** Verify ≤280 Unicode chars; record verbatim.
- **Random Wikipedia articles** (preferred when egress permits). Five articles
  from `https://en.wikipedia.org/wiki/Special:Random` (or the Wikipedia API's
  `list=random`). Each article title is treated as an already-inflated SEED
  concept. **Probe first**: try one `WebFetch` to `Special:Random`; if it
  returns 403 or "Blocked by egress policy" (Claude Code on the web sandboxes
  often block Wikipedia), fall back on the dictionary procedure. `WebSearch`
  is usually still available even when `WebFetch`/`curl` to Wikipedia is not.
- **Dictionary fallback.**
  ```sh
  grep -E '^[a-z]{5,}$' /usr/share/dict/american-english-large | shuf -n 10
  ```
  If `american-english-large` is missing, install (`apt-get install -y
  wamerican-large`) or fall back to `/usr/share/dict/words`. Filter the ten
  draws: keep words pointing to a concept, event, phenomenon, object,
  discipline, or person. Discard adverbs, function words, and anything
  vague. Inflate each survivor via `WebSearch` to a specific named referent
  (Wikipedia article, named entity, established concept). Discard rather
  than guess. `WebSearch` calls for the surviving words can be made in
  parallel.
- Output the SEED clearly in `phase_2_seed.md`.

### Phases 3–6 — generate, top three, narrow to one
Honor the template's "one thing makes it stand out / one thing worries you"
forcing function at every top-three step. Output in each phase file:
candidates → top three with stand-out/worry → winner with reasoning.

Template-specific notes:
- **Baseline v4.7.** Phase 3 requires at least 15 of 30 premises to be
  plot-premises (vs. recognition-premises). The plot-tradition section
  written in Phase 1 is reference material for premise and plot
  generation, not just for prose.
- **Genre Fiction v1.0.** All 30 premises must be plot-premises;
  recognition-premises are not allowed. At least 8 of 30 must be
  strange-tail; at least one of the top three must be strange-tail. The
  through-checks at the end of Phases 3, 4, and 5 lock the form
  commitment for downstream phases — honor them.

### Phase 7 — story drafts
Split into five separate Write steps. One variant per file, each with a
distinct named flavor stated at the start. Three variants are grounded
executions; two take a creative risk you're not fully confident will land.
For Genre Fiction v1.0, at least one of the two creative risks must be at
the level of the form's voice or structure, not tonal level. After all
five are written, read them and produce `phase_7_synthesis.md` with the
top-three analysis and the winning variant reproduced in full.

**Word-count vigilance.** Run `wc -w` on each variant immediately after
writing it. Markdown footnoted prose, dialogue-heavy scenes, and other
formally compressed forms come in shorter than they read; aim each variant
at the *middle* of `[LENGTH]`, not the floor, so that variants under floor
need only minor expansion. Expand on the spot — once you're three variants
deep, going back to extend an earlier one is more disruptive.

### Phase 8 — revision
One-thing, audit, length check, rewrite, changelog. Output the full revised
story in the phase file. Don't argue for the original prose: if a flag is
valid, fix it; if invalid, drop the flag. For Genre Fiction v1.0, the
audit also runs the **re-skin test** (does the story survive being
re-skinned as contemporary literary realism? if yes, the form has failed)
and the **form-survival check** (did the form committed in Phases 3–6
survive Phase 7's prose generation, or has it quietly normalized to
realist scene?).

### Phase 9 — export
Title + 80–150-word abstract. Assemble the final `story.md`:
```
# <title>

## Abstract

<abstract>

## Story

<revised story from Phase 8>
```

## Operational notes

- **No pause for user review** between phases on autonomous runs. The user
  can stop at any point; otherwise barrel through.
- **Each phase reads only what it needs** from prior files. Don't reload
  every prior phase into context.
- **Phase 7 is the heaviest.** Five full stories at `[LENGTH]` plus a
  synthesis. Writing each variant to disk before reading the next keeps
  context bounded.
- **Tools to use:** `Read`, `Write`, `Bash` (Phase 2 dictionary), `WebSearch`
  (Phase 2 inflation, narrow Phase 1 genres), `WebFetch` (Wikipedia
  Special:Random when egress permits), `TodoWrite` (the nine phases plus
  five Phase-7 variants is a 14-step run; tracking helps).
- **Pre-load deferred tools.** If `Write`, `Edit`, and `TodoWrite` appear as
  deferred tools at session start (i.e. names listed but schemas not loaded),
  load all three upfront with `ToolSearch select:Write,Edit,TodoWrite` before
  starting Phase 1. Every run uses all three repeatedly; lazy-loading them
  costs a load step at the head of nearly every phase.
- **Self-evaluation caveat.** Phases 3–7 ask the same model that generated
  candidates to rank them. The forcing function ("one thing worries you") is
  the only guardrail — apply it strictly. If the model can't name a
  worry for a candidate, that's a sign the rating is sloppy, not that the
  candidate is unimpeachable.
- **Long Write operations sometimes time out** (observed: Phase-3-sized
  outputs of ~700+ lines occasionally fail with "Stream idle timeout").
  When this happens, check whether the file was written despite the error —
  often it was. Otherwise, split the output: write a partial file, then use
  `Edit` to extend it.
- **Surface repeated infrastructure failures.** If the same phase fails twice
  in a row with infrastructure errors (stream-idle timeouts, network errors,
  partial-response truncation that isn't recoverable by re-reading the
  partial file), stop and tell the user before a third attempt. The "no pause
  for review" rule above is for editorial flow, not for hammering on a broken
  tool path; the user may want to switch models (Sonnet 4.6 has been more
  reliable than Opus 4.7 1M for the heavy Phase-7/8 writes) or save and
  abandon, neither of which the model can choose unilaterally.

## When the user provides feedback after a run

Treat the run as a learning artifact. If something failed in a way the
template doesn't anticipate, propose an update to this file or to the
template (preserving the next version number).
