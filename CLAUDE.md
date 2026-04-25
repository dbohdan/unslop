# CLAUDE.md — Story-writing instructions for Claude Code

This repository's primary use is running the v4.3 fiction pipeline. When the
user asks for a story, follow the procedure below.

## Source of truth

- **Template:** [`pipeline/3-baseline/story-pipeline-template-baseline-v4.3.md`](pipeline/3-baseline/story-pipeline-template-baseline-v4.3.md).
  This is the tested, tuned version. Read each phase from this file when you
  reach it; do not work from memory.
- **Style guide:** [`style-guide/unslop-style-guide.md`](style-guide/unslop-style-guide.md).
  Hard constraint at every phase. Use it as an audit lens during Phase 8.
- **Python port:** [`api/story_pipeline.py`](api/story_pipeline.py). Reference
  for tooling shape (file naming, Phase 7 split). Not the source of truth for
  the prompts themselves.

## Inputs to ask the user for

Before starting, get:
- `[GENRE]` — required. Subgenre, movement, microgenre, or "in the tradition of [author]".
- `[LENGTH]` — required. e.g. "1500-3000 words".
- `[SEED]` — optional. ≤280 Unicode chars; if absent, generate one.
- Run directory name — slug for `claude-code/test/<name>/` (or `runs/NN/` for
  numbered runs once the user is ready). Suggest a default if none given.

## Run directory

Working directory for a run is `claude-code/test/<slug>/` unless the user
specifies otherwise. Numbered, blessed runs go in `runs/NN/`.

## File-naming convention

Mirror the api script:

```
phase_1_style_guide.md
phase_2_seed.md
phase_3_conflict.md
phase_4_plot.md
phase_5_structure.md
phase_6_outline.md
phase_7_variant_1.md           # FLAVOR + full story
phase_7_variant_2.md
phase_7_variant_3.md
phase_7_variant_4.md
phase_7_variant_5.md
phase_7_synthesis.md           # top-three + winner reproduced verbatim
phase_8_revision.md            # one-thing + audit + length check + rewrite + changelog
phase_9_export_metadata.md     # title + abstract
story.md                       # final, assembled
```

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

### Phase 7 — story drafts
Split into five separate Write steps. One variant per file. Variants 1–3 are
grounded executions (the template's risk-clause language); variants 4–5 take
a creative risk. After all five are written, read them and produce
`phase_7_synthesis.md` with the top-three analysis and the winning variant
reproduced in full.

**Word-count vigilance.** Run `wc -w` on each variant immediately after
writing it. Markdown footnoted prose, dialogue-heavy scenes, and other
formally compressed forms come in shorter than they read; aim each variant
at the *middle* of `[LENGTH]`, not the floor, so that variants under floor
need only minor expansion. Expand on the spot — once you're three variants
deep, going back to extend an earlier one is more disruptive.

### Phase 8 — revision
One-thing, audit, length check, rewrite, changelog. Output the full revised
story in the phase file. Don't argue for the original prose: if a flag is
valid, fix it; if invalid, drop the flag.

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

## When the user provides feedback after a run

Treat the run as a learning artifact. If something failed in a way the
template doesn't anticipate, propose an update to this file or to the
template (preserving the next version number).
