# Unslop

This repository contains [D. Bohdan](https://dbohdan.com/)'s work for the [Unslop](https://www.hyperstitionai.com/unslop) AI-generated short story contest.
The rest of the README is written by AI.

---

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
   ten structural principles; Part II is the kill list. A Speculative Fiction
   edition lives alongside it at
   [`unslop-style-guide-sf.md`](style-guide/unslop-style-guide-sf.md), with
   the same rules but with the principles whose examples or thresholds anchor
   to literary-realist register reframed for SF; its implicit positive model
   is Le Guin–Egan–Banks rather than Carver-Munro-Cheever.

2. **[`pipeline/3-baseline/story-pipeline-template-baseline-v4.7.md`](pipeline/3-baseline/story-pipeline-template-baseline-v4.7.md)**
   — The current Baseline pipeline template. Nine phases: style guide →
   SEED → premise → plot → structure → outline → five story drafts →
   revision → export. Each creative phase generates many candidates and
   narrows to one. Selection is forced through a "one thing makes it stand
   out / one thing worries you" rationale at every top-three step, so picks
   are traceable to specific qualities and specific concerns instead of
   overall impression. Phase 1 produces both a genre style guide and a
   *plot tradition* section covering the genre's characteristic plot
   mechanics, reader contracts, stakes calibration, and strangest moves;
   Phase 3 requires at least 15 of 30 premises to be plot-premises (the
   distinction tracks plot-mechanic stories from interiority-driven ones).
   Baseline produces both literary-realist and genre fiction in a
   speculative setting, with a documented bias toward the former — what
   runs 21–29 surfaced as the "Carver attractor" and what motivated the
   Genre Fiction fork below.

A third template is a Genre-Fiction-only alternative:

3. **[`pipeline/4-genre-fiction/story-pipeline-template-genre-fiction-v1.3.md`](pipeline/4-genre-fiction/story-pipeline-template-genre-fiction-v1.3.md)**
   — A fork of v4.7 that produces plot-focused genre fiction only.
   Recognition-premises are eliminated, all 30 premises must be plot-
   premises, the Setup defaults to scales the protagonist cannot fully
   witness, every plot is rendered as a narrative scene, and Phase 8
   adds a *re-skin test* — if the story can be re-skinned as
   contemporary literary realism by stripping the speculative element,
   the audit fails. Use this template when you want fiction that reads
   as the genre advertised rather than as literary fiction with the
   genre's set dressing. Pairs naturally with the SF edition of the
   Unslop guide. Genre Fiction's evolution from v1.0 (which let
   compositional-structure outputs through as the workaround that
   replaced literary realism) to v1.3 (every reference to compositional
   structure removed, narrative scene the only form) is documented in
   [HISTORY.md](HISTORY.md) §11.

The pipeline runs in three modes:

- **Hand-driven through the Claude web app.** With the template loaded as
  project knowledge, the model looks up each phase from the template file
  rather than the user pasting prompts. Between phases the user reviews,
  steers, or simply asks for the next phase. Runs 01–43 in [`runs/`](runs/)
  were produced this way; each run preserves a transcript and the resulting
  story (or stories, for the A/B and multi-model runs).
- **Autonomously through Claude Code on the web.** A `CLAUDE.md` at the
  repo root tells Claude Code how to drive Baseline v4.7 (default) or
  Genre Fiction v1.3 end-to-end. Two test runs are committed in
  [`claude-code/test/`](claude-code/test/). This path trades the
  steerability of the hand-driven mode for the convenience of a single
  "write me a story in `[GENRE]`" instruction.
- **End-to-end via [`api/story_pipeline.py`](api/story_pipeline.py).** A
  Python port of Baseline v4.7 that calls Anthropic or OpenRouter
  directly, caches each phase to disk, and can resume, regenerate, or
  run an arbitrary slice of phases. Tested against Claude Sonnet 4.6
  and Gemini 3 Flash Preview; outputs in [`api/test/`](api/test/). The
  script is much less tested than the hand-driven Claude.ai path and
  may produce worse stories — two end-to-end runs to its name, against
  forty-three hand-driven runs in [`runs/`](runs/). The Genre Fiction
  fork is not ported. Use the script for batch experiments and
  ablations; use the Claude.ai path for the runs you care about.

For the project's evolution — the Ellison trial, the abandoned Nix critic
persona, the Plain → Baseline lineage, the SEED mechanism that anchors
v4, and the Carver-attractor diagnosis that motivated v4.4 → v4.7 and the
Genre Fiction fork — see [HISTORY.md](HISTORY.md).

## Producing a story

### Hand-driven through the Claude web app

1. Open a [Claude project](https://claude.ai/projects). Add
   `style-guide/unslop-style-guide.md` and the v4.7 template to project
   knowledge. (For genre-only runs, swap in
   `style-guide/unslop-style-guide-sf.md` and the Genre Fiction v1.3
   template instead.)
2. Open a chat in the project and start the run with a prompt like:

   > Please refer to `story-pipeline-template-baseline-v4.7.md` and run
   > Phase 1 with solarpunk as GENRE and a LENGTH of 2,000–3,000 words.

   With no `[SEED]` supplied, Phase 2 draws ten words from
   `/usr/share/dict/american-english-large` (the American English dictionary
   is available in the Claude.ai sandbox), filters them, and inflates each
   survivor via web search into a specific named referent. To supply a
   `[SEED]` instead, append `SEED:` and up to 280 Unicode characters to the
   prompt.
3. After each phase, say "Continue. Next phase." The model picks and moves
   on without further input. You can step in to override a pick, blend
   candidates, or regenerate, but the default flow runs end-to-end.

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
    - [unslop-style-guide-sf.md](style-guide/unslop-style-guide-sf.md) — Speculative Fiction edition; reframes the principles whose examples or thresholds anchor to literary-realist register
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
    - [3-baseline/](pipeline/3-baseline/) — the Baseline lineage; v4.7 is current
      - [story-pipeline-template-plain-v2.md](pipeline/3-baseline/story-pipeline-template-plain-v2.md)
      - [story-pipeline-template-plain-v3.md](pipeline/3-baseline/story-pipeline-template-plain-v3.md)
      - [story-pipeline-template-baseline-v3.1.md](pipeline/3-baseline/story-pipeline-template-baseline-v3.1.md)
      - [story-pipeline-template-baseline-v3.2.md](pipeline/3-baseline/story-pipeline-template-baseline-v3.2.md)
      - [story-pipeline-template-baseline-v3.3.md](pipeline/3-baseline/story-pipeline-template-baseline-v3.3.md)
      - [story-pipeline-template-baseline-v4.md](pipeline/3-baseline/story-pipeline-template-baseline-v4.md)
      - [story-pipeline-template-baseline-v4.1.md](pipeline/3-baseline/story-pipeline-template-baseline-v4.1.md)
      - [story-pipeline-template-baseline-v4.2.md](pipeline/3-baseline/story-pipeline-template-baseline-v4.2.md)
      - [story-pipeline-template-baseline-v4.3.md](pipeline/3-baseline/story-pipeline-template-baseline-v4.3.md)
      - [story-pipeline-template-baseline-v4.4.md](pipeline/3-baseline/story-pipeline-template-baseline-v4.4.md)
      - [story-pipeline-template-baseline-v4.5.md](pipeline/3-baseline/story-pipeline-template-baseline-v4.5.md)
      - [story-pipeline-template-baseline-v4.5-alt.md](pipeline/3-baseline/story-pipeline-template-baseline-v4.5-alt.md)
      - [story-pipeline-template-baseline-v4.5.1.md](pipeline/3-baseline/story-pipeline-template-baseline-v4.5.1.md)
      - [story-pipeline-template-baseline-v4.6.md](pipeline/3-baseline/story-pipeline-template-baseline-v4.6.md)
      - [story-pipeline-template-baseline-v4.7.md](pipeline/3-baseline/story-pipeline-template-baseline-v4.7.md) — current
      - [attachments/](pipeline/3-baseline/attachments/) — run transcripts attached as feedback during template revisions
        - [transcript-cyberpunk-yet-again.md](pipeline/3-baseline/attachments/transcript-cyberpunk-yet-again.md)
        - [transcript-steampunk.md](pipeline/3-baseline/attachments/transcript-steampunk.md)
      - [parts/](pipeline/3-baseline/parts/)
        - [hyperstition-ai-good-outcomes.md](pipeline/3-baseline/parts/hyperstition-ai-good-outcomes.md) — canon notes for Phase 1
        - [random-word-seed.md](pipeline/3-baseline/parts/random-word-seed.md) — SEED-draw notes
      - [transcript.md](pipeline/3-baseline/transcript.md)
    - [4-genre-fiction/](pipeline/4-genre-fiction/) — Genre Fiction fork, plot-focused only
      - [story-pipeline-template-genre-fiction-v1.0.md](pipeline/4-genre-fiction/story-pipeline-template-genre-fiction-v1.0.md)
      - [story-pipeline-template-genre-fiction-v1.1.md](pipeline/4-genre-fiction/story-pipeline-template-genre-fiction-v1.1.md) — narrative-scene default, document-form caution
      - [story-pipeline-template-genre-fiction-v1.2.md](pipeline/4-genre-fiction/story-pipeline-template-genre-fiction-v1.2.md) — every mention of false-document forms removed
      - [story-pipeline-template-genre-fiction-v1.3.md](pipeline/4-genre-fiction/story-pipeline-template-genre-fiction-v1.3.md) — current; strange-tail premise category eliminated, narrative scene the only form
      - [transcript.md](pipeline/4-genre-fiction/transcript.md) — symlink to the Baseline transcript that walks through v1.0 → v1.3
  - [runs/](runs/) — 43 hand-driven pipeline runs; each contains `transcript.md` plus `story.md`. Runs 01–16 and 19 used the older `[AUTHOR]` setting (Harlan Ellison throughout); runs 17 onward use `[GENRE]`. The genre parenthetical is given for the latter.
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
    - [17/](runs/17/) — *The Fifth Prospero* (hysterical realism)
    - [18/](runs/18/) — *Six Hundred* (with prefs) and *The Count* (without) (hysterical realism)
    - [19/](runs/19/) — original-template (Ellison-as-AUTHOR) replication on Opus 4.6 and Opus 4.7, two runs each, all without preferences; plus [`analysis.md`](runs/19/analysis.md) comparing AI depiction across runs/02, runs/18, and runs/19
    - [20/](runs/20/) — *Off the Top* (with prefs) and *The Full Scope* (without) (New Wave SF in the tradition of Harlan Ellison); v4.3 with the *Last Call* SEED, second A/B on `claude-preferences.txt`
    - [21/](runs/21/) — *Maybe-Not-Yet* (solarpunk, v4.3)
    - [22/](runs/22/) — *The Visitor Lanyard* (cyberpunk, v4.3)
    - [23/](runs/23/) — *The Wry Surface* (postcyberpunk, v4.3); these three runs were the prompt for the Carver-attractor diagnosis
    - [24/](runs/24/) — *Memory-Corner 0x7A4E* (cyberpunk, v4.5.1 — the prose-permissions experiment)
    - [25/](runs/25/) — *The Older Charter* (cyberpunk, v4.6)
    - [26/](runs/26/) — *The Brass-Polisher's Night* (steampunk, v4.6)
    - [27/](runs/27/) — *The Long Watch* (biopunk, v4.7)
    - [28/](runs/28/) — *The Morning's Work* (technothriller, v4.7)
    - [29/](runs/29/) — *The Working Shape of the River* (cyberpunk, v4.7 + SF Unslop)
    - [30/](runs/30/) — three-way cyberpunk comparison: *Stale* (Baseline v4.7, custom SEED), *After-Action* (Genre Fiction v1.0, same custom SEED), *Continental dispatch* (Genre Fiction v1.0, random SEED)
    - [31/](runs/31/) — *The Soria Correspondence* (cozy SF, Genre Fiction v1.0)
    - [32/](runs/32/) — *The Eleventh Refusal of Sefa-on-the-Slow* (space opera, Genre Fiction v1.0)
    - [33/](runs/33/) — *Page Seventy-Three* (military SF, Genre Fiction v1.1)
    - [34/](runs/34/) — *The Third Closeness* (hard SF, Genre Fiction v1.2)
    - [35/](runs/35/) — *Independent Confirmation* (hard SF, Genre Fiction v1.3); first v1.3 run
    - [36/](runs/36/) — *Forty-Eight, Minus* (cyberpunk, Genre Fiction v1.3); same SEED as run 30 *After-Action*
    - [37/](runs/37/) — *The Long Watch* (cozy SF, Genre Fiction v1.3)
    - [38/](runs/38/) — *The Last Inspector* (space opera, Genre Fiction v1.3)
    - [39/](runs/39/) — *The Calcium Bath* (self-consistent time travel in the tradition of *Primer*, Genre Fiction v1.3 + SF Unslop)
    - [40/](runs/40/) — *What Henry Will Remember* (self-consistent time travel in the tradition of *Primer*, Genre Fiction v1.3 + regular Unslop)
    - [41/](runs/41/) — *The Numbers* (rationalist fiction, Genre Fiction v1.3)
    - [42/](runs/42/) — *For Aoife* (literary fiction against the template, Genre Fiction v1.3)
    - [43/](runs/43/) — *The Asymmetric Counsel* (hard SF in the tradition of Greg Egan, writer's choice, Genre Fiction v1.3)
  - [review/](review/) — cross-model reviews of run sets
    - [01-with-abstracts.md](review/01-with-abstracts.md)
    - [02-without-abstracts.md](review/02-without-abstracts.md)
  - [claude-code/](claude-code/) — Claude Code on the web path
    - [wikipedia-seed.md](claude-code/wikipedia-seed.md) — Wikipedia random-article SEED protocol
    - [test/](claude-code/test/)
      - [comic-sf-1/](claude-code/test/comic-sf-1/) — end-to-end test, dictionary SEED
      - [comic-sf-2/](claude-code/test/comic-sf-2/) — phases 1–7, Wikipedia-sourced SEED
  - [api/](api/)
    - [story_pipeline.py](api/story_pipeline.py) — Baseline v4.7 ported to Anthropic + OpenRouter; Genre Fiction is intentionally not ported
    - [test/](api/test/)
      - [claude-sonnet-4.6/](api/test/claude-sonnet-4.6/) — end-to-end test, story: *Wiwaxia*
      - [gemini-3-flash-preview/](api/test/gemini-3-flash-preview/) — end-to-end test, story: *The 300-Baud Handshake*
