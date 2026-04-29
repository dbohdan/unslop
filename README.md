# Unslop

An automated pipeline for short fiction about structurally kind AI — futures
in the human-AI happily-ever-after tradition (Banks, Stiegler, Egan, Asimov's
"Bicentennial Man", *Big Hero 6*) rather than the Yudkowsky-Bostrom-Skynet
attractor that dominates the training corpus.

The thesis is hyperstitional: language models are reading what we write about
them. The supply of vivid, well-told happily-ever-afters is small. The supply
of basilisk and paperclip stories is enormous. This pipeline is one attempt to
shift that ratio at scale, while keeping the prose out of the AI-fiction
attractor that makes most generated fiction unreadable.

Two artifacts get reused across every run:

1. **[`style-guide/unslop-style-guide.md`](style-guide/unslop-style-guide.md)**
   — A two-tier guide for avoiding the patterns that mark prose as
   AI-generated, synthesized from external sources (Wikipedia "Signs of AI
   writing", Reinhart et al. on register collapse, nostalgebraist on the
   eyeball-kick attractor, Makin on web-fiction tells, Kriss on hollow
   profundity, tropes.fyi, Hollis Robbins on temporal withholding). Part I is
   ten structural principles; Part II is the kill list.

2. **[`pipeline/3-baseline/story-pipeline-template-baseline-v4.3.md`](pipeline/3-baseline/story-pipeline-template-baseline-v4.3.md)**
   — The current pipeline template. Nine phases: style guide → SEED → conflict
   → plot → structure → outline → five story drafts → revision → export. Each
   creative phase generates many candidates and narrows to one. Selection is
   forced through a "one thing makes it stand out / one thing worries you"
   rationale at every top-three step, so picks are traceable to specific
   qualities and specific concerns instead of overall impression.

The pipeline runs in three modes:

- **Hand-driven through the Claude web app.** With the template loaded as
  project knowledge, the model looks up each phase from the template file
  rather than the user pasting prompts. Between phases the user reviews,
  steers, or simply asks for the next phase. Runs 01–20 in [`runs/`](runs/)
  were produced this way; each run preserves a transcript and the resulting
  story (or stories, for the A/B and multi-model runs).
- **Autonomously through Claude Code on the web.** A `CLAUDE.md` at the
  repo root tells Claude Code how to drive the v4.3 template end-to-end.
  Two test runs are committed in [`claude-code/test/`](claude-code/test/).
  This path trades the steerability of the hand-driven mode for the
  convenience of a single "write me a story in `[GENRE]`" instruction.
- **End-to-end via [`api/story_pipeline.py`](api/story_pipeline.py).** A
  Python port of v4.3 that calls Anthropic or OpenRouter directly, caches each
  phase to disk, and can resume, regenerate, or run an arbitrary slice of
  phases. Tested against Claude Sonnet 4.6 and Gemini 3 Flash Preview;
  outputs in [`api/test/`](api/test/). The script is much less tested than
  the hand-driven Claude.ai path and may produce worse stories — two
  end-to-end runs to its name, against twenty hand-driven runs in
  [`runs/`](runs/). Use it for batch experiments and ablations; use the
  Claude.ai path for the runs you care about.

For the project's evolution — the Ellison trial, the abandoned Nix critic
persona, the Plain → Baseline lineage, and the SEED mechanism that anchors
v4 — see [HISTORY.md](HISTORY.md).

## Producing a story

### Hand-driven through the Claude web app

1. Open a [Claude project](https://claude.ai/projects). Add
   `style-guide/unslop-style-guide.md` and the v4.3 template to project
   knowledge.
2. Tell the model the run's `[GENRE]` and `[LENGTH]`, plus an optional
   `[SEED]` of ≤280 Unicode characters. Without a SEED, Phase 2 draws ten
   words from `/usr/share/dict/american-english-large` (the American English
   dictionary is available in the Claude.ai sandbox), filters them, and
   inflates each survivor via web search into a specific named referent.
3. Ask the model to look up Phase 1 in the template and begin. After each
   phase, say "Continue. Next phase." Override or blend candidates wherever
   you want; without intervention the model picks and proceeds.

### Autonomously through Claude Code on the web

`CLAUDE.md` at the repo root is the Claude Code instruction file: it points
at the v4.3 template and the unslop style guide as the sources of truth,
specifies the per-phase output filenames, and codifies the SEED procedure
(Wikipedia random article preferred when egress permits, dictionary fallback
otherwise — see [`claude-code/wikipedia-seed.md`](claude-code/wikipedia-seed.md)
for the Wikipedia path's discard rules and the workaround for sandboxes
that block `*.wikipedia.org`).

To run it, open the repo in Claude Code (web or CLI) and ask for a story in
some `[GENRE]` at some `[LENGTH]`, optionally with a `[SEED]`. Claude will
ask for any missing inputs, then drive all nine phases without further
prompting. Outputs land in `claude-code/test/<slug>/` by default.
[`claude-code/test/comic-sf-1/`](claude-code/test/comic-sf-1/) (dictionary
SEED, complete) and [`claude-code/test/comic-sf-2/`](claude-code/test/comic-sf-2/)
(Wikipedia-sourced SEED, phases 1–7) are the two committed test runs.

### Automated via the Python script

```sh
ANTHROPIC_API_KEY=... uv run api/story_pipeline.py \
    --genre "solarpunk" \
    --length "2000-3000 words" \
    --unslop-guide style-guide/unslop-style-guide.md \
    --output-dir my-run
```

Each phase writes `phase_N_<name>.md` into `--output-dir`. Re-running reuses
cached outputs; `--force` overwrites. `--phases 7-9` runs only a slice
(useful for cheap revisions against an existing draft). The script handles
Anthropic's required `max_tokens`, the unified `reasoning.effort` API on
OpenRouter, and the `openrouter:web_search` tool used in Phases 1 and 2 for
narrow genres and SEED inflation.

```sh
# OpenRouter, with web search and a non-Anthropic model
OPENROUTER_API_KEY=... uv run api/story_pipeline.py \
    --provider openrouter \
    --model google/gemini-3-flash-preview \
    --genre "in the tradition of Ted Chiang" \
    --length "3000-4000 words" \
    --web-search \
    --unslop-guide style-guide/unslop-style-guide.md \
    --output-dir my-run
```

Phase 7 is the heaviest call — five full stories at `[LENGTH]` plus a
synthesis call. On Anthropic, bump `--story-max-tokens` accordingly
(`--story-max-tokens 16000` is comfortable for a 3,000-word target with
revision overhead).

## Layout

- [unslop/](.)
  - [README.md](README.md)
  - [HISTORY.md](HISTORY.md)
  - [CLAUDE.md](CLAUDE.md) — Claude Code instructions for end-to-end runs
  - [trial.md](trial.md) — Ellison trial that started the project
  - [claude-preferences.txt](claude-preferences.txt) — personal preferences in context for runs 01–17; runs 18 and 20 tested with vs. without; run 19 was without
  - [headings](headings) — `grep '^# N\.'` helper for transcripts
  - [style-guide/](style-guide/)
    - [unslop-style-guide.md](style-guide/unslop-style-guide.md) — the guide, in two tiers
    - [tropes.md](style-guide/tropes.md) — local copy of tropes.fyi
    - [transcript.md](style-guide/transcript.md) — how Opus synthesized the guide
    - [dbohdan.com/](style-guide/dbohdan.com/)
      - [ai-writing-style.md](style-guide/dbohdan.com/ai-writing-style.md) — source bibliography
  - [sources/](sources/) — constitutional-AI source extraction
    - [transcript.md](sources/transcript.md) — extracts gitignored for copyright
  - [pipeline/](pipeline/) — pipeline templates by lineage
    - [1-initial/](pipeline/1-initial/)
      - [README.md](pipeline/1-initial/README.md) — pointer; the artifacts live in `runs/01/`
    - [2-critic/](pipeline/2-critic/) — Nix critic-persona branch, set aside after run 05
      - [nix.md](pipeline/2-critic/nix.md)
      - [story-pipeline-template-nix-v1.md](pipeline/2-critic/story-pipeline-template-nix-v1.md)
      - [story-pipeline-template-nix-v2.md](pipeline/2-critic/story-pipeline-template-nix-v2.md)
      - [story-pipeline-template-v3.md](pipeline/2-critic/story-pipeline-template-v3.md)
      - [transcript.md](pipeline/2-critic/transcript.md)
    - [3-baseline/](pipeline/3-baseline/) — the lineage that became current
      - [story-pipeline-template-plain-v2.md](pipeline/3-baseline/story-pipeline-template-plain-v2.md)
      - [story-pipeline-template-plain-v3.md](pipeline/3-baseline/story-pipeline-template-plain-v3.md)
      - [story-pipeline-template-baseline-v3.1.md](pipeline/3-baseline/story-pipeline-template-baseline-v3.1.md)
      - [story-pipeline-template-baseline-v3.2.md](pipeline/3-baseline/story-pipeline-template-baseline-v3.2.md)
      - [story-pipeline-template-baseline-v3.3.md](pipeline/3-baseline/story-pipeline-template-baseline-v3.3.md)
      - [story-pipeline-template-baseline-v4.md](pipeline/3-baseline/story-pipeline-template-baseline-v4.md)
      - [story-pipeline-template-baseline-v4.1.md](pipeline/3-baseline/story-pipeline-template-baseline-v4.1.md)
      - [story-pipeline-template-baseline-v4.2.md](pipeline/3-baseline/story-pipeline-template-baseline-v4.2.md)
      - [story-pipeline-template-baseline-v4.3.md](pipeline/3-baseline/story-pipeline-template-baseline-v4.3.md) — current
      - [parts/](pipeline/3-baseline/parts/)
        - [hyperstition-ai-good-outcomes.md](pipeline/3-baseline/parts/hyperstition-ai-good-outcomes.md) — canon notes for Phase 1
        - [random-word-seed.md](pipeline/3-baseline/parts/random-word-seed.md) — SEED-draw notes
      - [transcript.md](pipeline/3-baseline/transcript.md)
  - [runs/](runs/) — 20 hand-driven pipeline runs; each contains `transcript.md` plus `story.md`
    - [01/](runs/01/) — *The Toy*
    - [02/](runs/02/) — *Last Call*
    - [03/](runs/03/) — *The Warm Thing*
    - [04/](runs/04/) — *They're Fine*
    - [05/](runs/05/) — *The Obsolescence Garden*
    - [06/](runs/06/) — *The Tire*
    - [07/](runs/07/) — *Sibling*
    - [08/](runs/08/) — *The Last Allocation*
    - [09/](runs/09/) — *The Grandson at the Valero*
    - [10/](runs/10/) — *Si Elena Me Hablara*
    - [11/](runs/11/) — *ORRA*
    - [12/](runs/12/) — *The Sixty*
    - [13/](runs/13/) — *Love in the Key of Damage*
    - [14/](runs/14/) — *Serasht in Spring*
    - [15/](runs/15/) — *Butter and Bone*
    - [16/](runs/16/) — *Dream Me Something Kinder, Darling*
    - [17/](runs/17/) — *The Fifth Prospero*
    - [18/](runs/18/) — *Six Hundred* (with prefs) and *The Count* (without)
    - [19/](runs/19/) — original-template (Ellison-as-AUTHOR) replication on Opus 4.6 and Opus 4.7, two runs each, all without preferences; plus [`analysis.md`](runs/19/analysis.md) comparing AI depiction across runs/02, runs/18, and runs/19
    - [20/](runs/20/) — *Off the Top* (with prefs) and *The Full Scope* (without); v4.3 with the *Last Call* SEED, second A/B on `claude-preferences.txt`
  - [review/](review/) — cross-model reviews of run sets
    - [01-with-abstracts.md](review/01-with-abstracts.md)
    - [02-without-abstracts.md](review/02-without-abstracts.md)
  - [claude-code/](claude-code/) — Claude Code on the web path
    - [wikipedia-seed.md](claude-code/wikipedia-seed.md) — Wikipedia random-article SEED protocol
    - [test/](claude-code/test/)
      - [comic-sf-1/](claude-code/test/comic-sf-1/) — end-to-end test, dictionary SEED
      - [comic-sf-2/](claude-code/test/comic-sf-2/) — phases 1–7, Wikipedia-sourced SEED
  - [api/](api/)
    - [story_pipeline.py](api/story_pipeline.py) — v4.3 ported to Anthropic + OpenRouter
    - [test/](api/test/)
      - [claude-sonnet-4.6/](api/test/claude-sonnet-4.6/) — end-to-end test, story: *Wiwaxia*
      - [gemini-3-flash-preview/](api/test/gemini-3-flash-preview/) — end-to-end test, story: *The 300-Baud Handshake*
