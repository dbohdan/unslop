# storyforge

Automated pipeline for generating Ellison-influenced New Wave SF short stories via Claude Code CLI.

## Setup

1. Install [Claude Code](https://docs.claude.com/en/docs/claude-code/overview) and authenticate
2. Place `unslop-style-guide.md` in this directory (or point to it with `--style-guide`)
3. `chmod +x storyforge.sh`

## Usage

```bash
# Interactive mode — pauses between phases for review
./storyforge.sh

# Full auto — runs all 6 phases without stopping
./storyforge.sh --auto

# Inject a seed concept at the plot phase
./storyforge.sh --seed "A child asks the AI why people die"

# Use custom source URLs for constitutional analysis
./storyforge.sh --sources my-sources.txt

# Resume a previous run from phase 4
./storyforge.sh --resume SESSION_ID --start-phase 4
```

## Pipeline

| Phase | Input | Output | Candidates |
|-------|-------|--------|------------|
| 1. Style Guide | (none) | Ellison fiction guide | 1 |
| 2. Conflicts | Guide + source URLs | Best conflict | 30 → 3 → 1 |
| 3. Plots | Guide + conflict | Best plot | 20 → 3 → 1 |
| 4. Structure | Guide + conflict + plot | Best structure | 20 → 3 → 1 |
| 5. Outline | All above | Best outline | 20 → 3 → 1 |
| 6. Story | All above | Best story | 10 → verdict |

Each phase passes only its output forward. The funnel (generate many → rank → pick 3 → pick 1) is executed in a single Claude call per phase.

## Interactive checkpoints

Between phases you can:
- **Enter** — proceed
- **v** — view the output
- **e** — edit the output before continuing
- **r** — rerun the phase
- **q** — quit (outputs saved in `output/TIMESTAMP/`)

## Options

```
--auto              Skip checkpoints, run everything
--model MODEL       Default: claude-opus-4-20250514
--output DIR        Default: ./output
--style-guide FILE  Default: ./unslop-style-guide.md
--sources FILE      Custom source URLs, one per line
--seed CONCEPT      Inject a concept at Phase 3
--word-min N        Default: 2000
--word-max N        Default: 3000
--resume ID         Resume a previous session
--start-phase N     Start from phase N (needs --resume)
```

## Output structure

```
output/
  20260411-143022/
    unslop-style-guide.md    # Frozen copy of style guide used
    phase1.md                # Ellison guide
    phase2.md                # 30 conflicts → winner
    phase3.md                # 20 plots → winner
    phase4.md                # 20 structures → winner
    phase5.md                # 20 outlines → winner
    phase6.md                # 10 story versions → verdict
    final-story.md           # Clean copy of phase 6
```

## Customization

**Different author influences:** Replace Phase 1's prompt in the script. The pipeline structure works for any author — swap "Ellison" for "Octavia Butler," "Ursula Le Guin," "Samuel Delany," etc.

**Different source material:** Use `--sources` to point to different constitutional/philosophical analyses.

**Different constraints:** Edit the system prompt in the script to change the program constraint (e.g., from "benevolent AI" to "post-scarcity society" or "first contact").

## Cost notes

Each full run makes 6 Claude Opus calls with large prompts (the style guide alone is ~4K tokens, and context accumulates). Expect roughly 100-150K input tokens and 50-80K output tokens per run. In auto mode on an API key, budget ~$5-10 per run at current Opus pricing. On a Max subscription, this fits comfortably within daily limits.
