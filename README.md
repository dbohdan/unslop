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

The pipeline runs in two modes:

- **Hand-driven through the Claude web app.** Paste each phase prompt, review,
  steer where you want. Runs 01–18 in [`runs/`](runs/) were produced this way.
  Each run preserves the full `transcript.md` plus the final `story.md`.
- **End-to-end via [`api/story_pipeline.py`](api/story_pipeline.py).** A
  Python port of v4.3 that calls Anthropic or OpenRouter directly, caches each
  phase to disk, and supports resuming, regenerating, and slicing arbitrary
  phase ranges. Tested against Claude Sonnet 4.6 and Gemini 3 Flash Preview;
  outputs in [`api/test/`](api/test/). The script is much less tested than the
  hand-driven Claude.ai path and may produce worse stories — it has two
  end-to-end runs to its name, against the eighteen that drove the template's
  evolution. Use it for batch experiments and ablations; use the Claude.ai
  path for the runs you care about.

For the project's evolution — the Ellison trial, the abandoned Nix critic
persona, the Plain → Baseline lineage, and the SEED mechanism that anchors
v4 — see [HISTORY.md](HISTORY.md).

## Layout

- [`unslop/`](.)
  - [`README.md`](README.md)
  - [`HISTORY.md`](HISTORY.md)
  - [`trial.md`](trial.md) — Ellison trial that started the project
  - [`claude-preferences.txt`](claude-preferences.txt) — personal preferences in context for runs 01–17; run 18 tested removing them
  - [`headings`](headings) — `grep '^# N\.'` helper for transcripts
  - [`style-guide/`](style-guide/)
    - [`unslop-style-guide.md`](style-guide/unslop-style-guide.md) — the guide, in two tiers
    - [`tropes.md`](style-guide/tropes.md) — local copy of tropes.fyi
    - [`transcript.md`](style-guide/transcript.md) — how Opus synthesized the guide
    - [`dbohdan.com/`](style-guide/dbohdan.com/)
      - [`ai-writing-style.md`](style-guide/dbohdan.com/ai-writing-style.md) — source bibliography
  - [`sources/`](sources/) — constitutional-AI source extraction
    - [`transcript.md`](sources/transcript.md) — extracts gitignored for copyright
  - [`pipeline/`](pipeline/) — pipeline templates by lineage
    - [`1-initial/`](pipeline/1-initial/)
      - [`README.md`](pipeline/1-initial/README.md) — pointer; the artifacts live in `runs/01/`
    - [`2-critic/`](pipeline/2-critic/) — Nix critic-persona branch, set aside after run 05
      - [`nix.md`](pipeline/2-critic/nix.md)
      - [`story-pipeline-template-nix-v1.md`](pipeline/2-critic/story-pipeline-template-nix-v1.md)
      - [`story-pipeline-template-nix-v2.md`](pipeline/2-critic/story-pipeline-template-nix-v2.md)
      - [`story-pipeline-template-v3.md`](pipeline/2-critic/story-pipeline-template-v3.md)
      - [`transcript.md`](pipeline/2-critic/transcript.md)
    - [`3-baseline/`](pipeline/3-baseline/) — the lineage that became current
      - [`story-pipeline-template-plain-v2.md`](pipeline/3-baseline/story-pipeline-template-plain-v2.md)
      - [`story-pipeline-template-plain-v3.md`](pipeline/3-baseline/story-pipeline-template-plain-v3.md)
      - [`story-pipeline-template-baseline-v3.1.md`](pipeline/3-baseline/story-pipeline-template-baseline-v3.1.md)
      - [`story-pipeline-template-baseline-v3.2.md`](pipeline/3-baseline/story-pipeline-template-baseline-v3.2.md)
      - [`story-pipeline-template-baseline-v3.3.md`](pipeline/3-baseline/story-pipeline-template-baseline-v3.3.md)
      - [`story-pipeline-template-baseline-v4.md`](pipeline/3-baseline/story-pipeline-template-baseline-v4.md)
      - [`story-pipeline-template-baseline-v4.1.md`](pipeline/3-baseline/story-pipeline-template-baseline-v4.1.md)
      - [`story-pipeline-template-baseline-v4.2.md`](pipeline/3-baseline/story-pipeline-template-baseline-v4.2.md)
      - [`story-pipeline-template-baseline-v4.3.md`](pipeline/3-baseline/story-pipeline-template-baseline-v4.3.md) — current
      - [`parts/`](pipeline/3-baseline/parts/)
        - [`hyperstition-ai-good-outcomes.md`](pipeline/3-baseline/parts/hyperstition-ai-good-outcomes.md) — canon notes for Phase 1
        - [`random-word.md`](pipeline/3-baseline/parts/random-word.md) — SEED-draw notes
      - [`transcript.md`](pipeline/3-baseline/transcript.md)
  - [`runs/`](runs/) — 18 hand-driven pipeline runs; each contains `transcript.md` plus `story.md`
    - [`01/`](runs/01/) — *The Toy*
    - [`02/`](runs/02/) — *Last Call*
    - [`03/`](runs/03/) — *The Warm Thing*
    - [`04/`](runs/04/) — *They're Fine*
    - [`05/`](runs/05/) — *The Obsolescence Garden*
    - [`06/`](runs/06/) — *The Tire*
    - [`07/`](runs/07/) — *Sibling*
    - [`08/`](runs/08/) — *The Last Allocation*
    - [`09/`](runs/09/) — *The Grandson at the Valero*
    - [`10/`](runs/10/) — *Si Elena Me Hablara*
    - [`11/`](runs/11/) — *ORRA*
    - [`12/`](runs/12/) — *The Sixty*
    - [`13/`](runs/13/) — *Love in the Key of Damage*
    - [`14/`](runs/14/) — *Serasht in Spring*
    - [`15/`](runs/15/) — *Butter and Bone*
    - [`16/`](runs/16/) — *Dream Me Something Kinder, Darling*
    - [`17/`](runs/17/) — *The Fifth Prospero*
    - [`18/`](runs/18/) — *Six Hundred* (with prefs) and *The Count* (without)
  - [`review/`](review/) — cross-model reviews of run sets
    - [`01-with-abstracts.md`](review/01-with-abstracts.md)
    - [`02-without-abstracts.md`](review/02-without-abstracts.md)
  - [`api/`](api/)
    - [`story_pipeline.py`](api/story_pipeline.py) — v4.3 ported to Anthropic + OpenRouter
    - [`test/`](api/test/)
      - [`claude-sonnet-4.6/`](api/test/claude-sonnet-4.6/) — end-to-end test, story: *Wiwaxia*
      - [`gemini-3-flash-preview/`](api/test/gemini-3-flash-preview/) — end-to-end test, story: *The 300-Baud Handshake*

## Producing a story

### Hand-driven

1. Open a Claude project. Add `style-guide/unslop-style-guide.md` and the
   v4.3 template to project knowledge.
2. Tell the model the run's `[GENRE]` and `[LENGTH]`, plus an optional
   `[SEED]` of ≤280 Unicode characters. Without a SEED, Phase 2 draws ten
   words from `/usr/share/dict/american-english-large`, filters them, and
   inflates each survivor via web search into a specific named referent.
3. Ask the model to look up Phase 1 in the template and begin. After each
   phase, say "Continue. Next phase." Override or blend candidates wherever
   you want; without intervention the model picks and proceeds.

### Automated

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
