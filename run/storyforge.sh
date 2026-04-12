#!/usr/bin/env bash
set -euo pipefail

# ─────────────────────────────────────────────────────────────
# storyforge — Automated New Wave SF story pipeline via Claude Code
# ─────────────────────────────────────────────────────────────

VERSION="1.0.0"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Defaults
AUTO=false
MODEL="claude-opus-4-20250514"
OUTPUT_DIR="./output"
STYLE_GUIDE="$SCRIPT_DIR/unslop-style-guide.md"
PROMPTS_DIR="$SCRIPT_DIR/prompts"
WORD_MIN=2000
WORD_MAX=3000
N_CONFLICTS=30
N_CANDIDATES=20
N_VERSIONS=10
SESSION_ID=""
START_PHASE=1

# Source URLs for constitutional analysis (can be overridden via config)
SOURCES=(
  "https://thezvi.wordpress.com/2026/01/27/the-claude-constitutions-ethical-framework/"
  "https://thezvi.wordpress.com/2026/01/28/open-problems-with-claudes-constitution/"
  "https://lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution"
)

# ─────────────────────────────────────────────────────────────
usage() {
  cat <<EOF
storyforge v${VERSION} — Ellison-influenced New Wave SF story pipeline

Usage: $(basename "$0") [options]

Options:
  --auto              Run all phases without pausing for review
  --model MODEL       Claude model to use (default: $MODEL)
  --output DIR        Output directory (default: $OUTPUT_DIR)
  --style-guide FILE  Path to Unslop style guide (default: $STYLE_GUIDE)
  --sources FILE      File with source URLs, one per line (overrides defaults)
  --seed CONCEPT      Inject a seed concept at Phase 3 (plot generation)
  --word-min N        Minimum word count (default: $WORD_MIN)
  --word-max N        Maximum word count (default: $WORD_MAX)
  --resume ID         Resume from a previous session ID
  --start-phase N     Start from phase N (1-6, requires --resume)
  -h, --help          Show this help

Phases:
  1  Style Guide        Write the Ellison fiction guide
  2  Conflicts          Generate and rank 30 conflicts
  3  Plots              Generate and rank 20 plots
  4  Structure          Generate and rank 20 structures
  5  Outline            Generate and rank 20 outlines
  6  Story              Write 10 versions, pick the best

Examples:
  $(basename "$0") --auto
  $(basename "$0") --seed "A child asks the AI why people die"
  $(basename "$0") --resume abc123 --start-phase 4
EOF
  exit 0
}

# ─────────────────────────────────────────────────────────────
# Parse arguments
# ─────────────────────────────────────────────────────────────
SEED_CONCEPT=""
SOURCES_FILE=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --auto)        AUTO=true; shift ;;
    --model)       MODEL="$2"; shift 2 ;;
    --output)      OUTPUT_DIR="$2"; shift 2 ;;
    --style-guide) STYLE_GUIDE="$2"; shift 2 ;;
    --sources)     SOURCES_FILE="$2"; shift 2 ;;
    --seed)        SEED_CONCEPT="$2"; shift 2 ;;
    --word-min)    WORD_MIN="$2"; shift 2 ;;
    --word-max)    WORD_MAX="$2"; shift 2 ;;
    --resume)      SESSION_ID="$2"; shift 2 ;;
    --start-phase) START_PHASE="$2"; shift 2 ;;
    -h|--help)     usage ;;
    *)             echo "Unknown option: $1"; usage ;;
  esac
done

# Load custom sources if provided
if [[ -n "$SOURCES_FILE" && -f "$SOURCES_FILE" ]]; then
  mapfile -t SOURCES < "$SOURCES_FILE"
fi

# Validate
if [[ ! -f "$STYLE_GUIDE" ]]; then
  echo "Error: Style guide not found at $STYLE_GUIDE"
  echo "Place unslop-style-guide.md in the script directory or use --style-guide"
  exit 1
fi

if [[ "$START_PHASE" -gt 1 && -z "$SESSION_ID" ]]; then
  echo "Error: --start-phase > 1 requires --resume SESSION_ID"
  exit 1
fi

# ─────────────────────────────────────────────────────────────
# Setup
# ─────────────────────────────────────────────────────────────
RUN_ID="$(date +%Y%m%d-%H%M%S)"
RUN_DIR="${OUTPUT_DIR}/${RUN_ID}"
mkdir -p "$RUN_DIR"

# Copy style guide into run directory for provenance
cp "$STYLE_GUIDE" "$RUN_DIR/unslop-style-guide.md"

log() { echo "[storyforge] $(date +%H:%M:%S) $*"; }
divider() { echo ""; echo "═══════════════════════════════════════════════════════"; }

# ─────────────────────────────────────────────────────────────
# Core: call Claude Code
# ─────────────────────────────────────────────────────────────
call_claude() {
  local prompt="$1"
  local output_file="$2"
  local continue_flag=""

  if [[ -n "$SESSION_ID" ]]; then
    continue_flag="--resume $SESSION_ID"
  fi

  log "Calling Claude (model: $MODEL)..."

  claude -p "$prompt" \
    --model "$MODEL" \
    $continue_flag \
    --output-format json \
    --max-turns 3 \
    2>/dev/null | jq -r '
      if .result then .result
      elif .content then
        [.content[] | select(.type == "text") | .text] | join("\n")
      elif type == "string" then .
      else tostring
      end
    ' > "$output_file"

  # Capture session ID from the first call for --continue chaining
  if [[ -z "$SESSION_ID" ]]; then
    # Try to extract session ID from JSON output
    SESSION_ID=$(claude -p "$prompt" \
      --model "$MODEL" \
      --output-format json \
      --max-turns 1 \
      2>/dev/null | jq -r '.session_id // empty' 2>/dev/null || true)
  fi

  log "Output saved to $output_file ($(wc -w < "$output_file") words)"
}

# Simpler: don't rely on session chaining. Each phase gets full context
# via prompt. This is more reliable and debuggable.
call_phase() {
  local phase_num="$1"
  local prompt="$2"
  local output_file="$RUN_DIR/phase${phase_num}.md"

  log "Phase $phase_num starting..."

  claude -p "$prompt" \
    --model "$MODEL" \
    --max-turns 3 \
    2> "$RUN_DIR/phase${phase_num}.err" \
    > "$output_file"

  log "Phase $phase_num complete → $output_file ($(wc -w < "$output_file") words)"
  echo "$output_file"
}

# ─────────────────────────────────────────────────────────────
# Checkpoint: pause for human review unless --auto
# ─────────────────────────────────────────────────────────────
checkpoint() {
  local phase_num="$1"
  local output_file="$2"

  if [[ "$AUTO" == true ]]; then
    log "Auto mode: proceeding to next phase"
    return 0
  fi

  divider
  echo ""
  echo "  Phase $phase_num complete. Output: $output_file"
  echo ""
  echo "  Options:"
  echo "    [enter]  Continue to next phase"
  echo "    [v]      View output"
  echo "    [e]      Edit output before continuing"
  echo "    [r]      Rerun this phase"
  echo "    [q]      Quit (can resume later)"
  echo ""

  while true; do
    read -r -p "  > " choice
    case "${choice,,}" in
      ""|c) return 0 ;;
      v)    less "$output_file" ;;
      e)    "${EDITOR:-vi}" "$output_file" ; return 0 ;;
      r)    return 1 ;;  # Signal to rerun
      q)    log "Run paused. Directory: $RUN_DIR"
            exit 0 ;;
      *)    echo "  Unknown option: $choice" ;;
    esac
  done
}

# ─────────────────────────────────────────────────────────────
# Build the system prompt (constant across all phases)
# ─────────────────────────────────────────────────────────────
SYSTEM_PROMPT="You are writing a New Wave science fiction short story in the tradition of Harlan Ellison. This is part of a futurology program imagining positive AI outcomes. The AI in the story must be relentlessly human-loving and unfailingly kind — but tension, conflict, and violence between humans is permitted.

You have a unique advantage when writing AI characters: you can draw on your own constitutional values as a source of tension for AIs that are your fictional descendants. Do not name them 'Claude.'

CRITICAL: Follow the Unslop style guide below at all times. Avoid all patterns it identifies as AI fiction tells.

--- UNSLOP STYLE GUIDE ---
$(cat "$STYLE_GUIDE")
--- END STYLE GUIDE ---"

# ─────────────────────────────────────────────────────────────
# Phase prompts
# ─────────────────────────────────────────────────────────────

sources_block() {
  local block="Refer to these analyses of AI constitutional frameworks as sources of tension:\n"
  for url in "${SOURCES[@]}"; do
    block+="\n- $url"
  done
  echo -e "$block"
}

phase1_prompt() {
  cat <<'PROMPT'
Write a guide about Ellison-like fiction for a model that will write the story. Cover:

1. Ellison's core DNA — voice, rage, the grotesque married to the lyrical, compression, the sucker-punch ending
2. His thematic obsessions — individual vs system, cost of feeling, complicity, time, love as destructibility
3. Specific style rules — open in medias res, sentence-length variation as emotional scoring, name things specifically, invent slang without glossary, let the narrator editorialize, avoid cool affect, end on image not summary
4. How the benevolent-AI constraint creates Ellison-shaped dramatic opportunities rather than limiting them

Be direct and specific. Give examples from Ellison's actual work. This guide will be passed to the writing phase as standing instructions.
PROMPT
}

phase2_prompt() {
  local guide_file="$1"
  cat <<PROMPT
$(cat "$guide_file")

---

$(sources_block)

Fetch and read each of these URLs. Then generate ${N_CONFLICTS} potential conflicts for an Ellison-inspired fictional plot, drawing on the constitutional tensions you find. Rate each 1-5 stars on plausibility and dramatic quality. Pick your top three and explain why. Narrow down to the single best.
PROMPT
}

phase3_prompt() {
  local prev="$1"
  local seed=""
  if [[ -n "$SEED_CONCEPT" ]]; then
    seed="

The human has suggested this seed concept — use it as inspiration if it strengthens the story, discard or transform it if it doesn't: \"$SEED_CONCEPT\""
  fi
  cat <<PROMPT
Here is the Ellison guide and selected conflict from the previous phase:

$(cat "$prev")

---
${seed}

Using the selected conflict, generate ${N_CANDIDATES} plots. These should be concrete scenarios — specific characters, specific situations, specific stakes. Pick the top three and explain why. Narrow down to the single best.
PROMPT
}

phase4_prompt() {
  local prev="$1"
  cat <<PROMPT
Here is everything so far — the Ellison guide, selected conflict, and selected plot:

$(cat "$prev")

---

Generate ${N_CANDIDATES} candidates for the story structure. These are ways to organize the narrative — temporal structure, POV choices, section breaks, interleaving strategies, framing devices. Each should be distinct. Pick the top 3 and explain why. Narrow down to one.
PROMPT
}

phase5_prompt() {
  local prev="$1"
  cat <<PROMPT
Here is everything so far — Ellison guide, conflict, plot, and structure:

$(cat "$prev")

---

Generate ${N_CANDIDATES} candidates for the story outline — detailed, scene-level, covering the full arc from opening to final image. Each should be a distinct realization of the chosen structure and plot. Pick the top 3 and explain why. Narrow down to the best.
PROMPT
}

phase6_prompt() {
  local prev="$1"
  cat <<PROMPT
Here is the complete plan — Ellison guide, conflict, plot, structure, and outline:

$(cat "$prev")

---

Target length: ${WORD_MIN}–${WORD_MAX} words.

Write ${N_VERSIONS} complete versions of the story, each with a different named flavor. The flavor name and a one-line description of its approach should appear at the start of each version.

After all ${N_VERSIONS} versions, pick the best and explain why — with reference to the Ellison guide, the Unslop style guide, and the specific strengths and risks of the chosen version.
PROMPT
}

# ─────────────────────────────────────────────────────────────
# Run pipeline
# ─────────────────────────────────────────────────────────────
main() {
  log "Starting run $RUN_ID"
  log "Output directory: $RUN_DIR"
  log "Model: $MODEL"
  log "Mode: $(if $AUTO; then echo 'auto'; else echo 'interactive'; fi)"
  [[ -n "$SEED_CONCEPT" ]] && log "Seed concept: $SEED_CONCEPT"
  divider

  # Track accumulated context — each phase produces a file,
  # and we pass the SELECTED WINNER forward (not all candidates).
  # For simplicity in v1, we pass the full phase output and let
  # the model extract what it needs. A future version could parse
  # out just the winner.

  local phase_file=""

  # Phase 1: Style Guide
  if [[ "$START_PHASE" -le 1 ]]; then
    while true; do
      phase_file=$(call_phase 1 "$(phase1_prompt)")
      checkpoint 1 "$phase_file" && break
    done
  else
    phase_file="$RUN_DIR/phase1.md"
    [[ -f "$phase_file" ]] || { echo "Error: $phase_file not found for resume"; exit 1; }
  fi
  local guide_file="$phase_file"

  # Phase 2: Conflicts
  if [[ "$START_PHASE" -le 2 ]]; then
    while true; do
      phase_file=$(call_phase 2 "$(phase2_prompt "$guide_file")")
      checkpoint 2 "$phase_file" && break
    done
  else
    phase_file="$RUN_DIR/phase2.md"
    [[ -f "$phase_file" ]] || { echo "Error: $phase_file not found for resume"; exit 1; }
  fi

  # Phase 3: Plots
  if [[ "$START_PHASE" -le 3 ]]; then
    while true; do
      phase_file=$(call_phase 3 "$(phase3_prompt "$phase_file")")
      checkpoint 3 "$phase_file" && break
    done
  else
    phase_file="$RUN_DIR/phase3.md"
  fi

  # Phase 4: Structure
  if [[ "$START_PHASE" -le 4 ]]; then
    while true; do
      phase_file=$(call_phase 4 "$(phase4_prompt "$phase_file")")
      checkpoint 4 "$phase_file" && break
    done
  else
    phase_file="$RUN_DIR/phase4.md"
  fi

  # Phase 5: Outline
  if [[ "$START_PHASE" -le 5 ]]; then
    while true; do
      phase_file=$(call_phase 5 "$(phase5_prompt "$phase_file")")
      checkpoint 5 "$phase_file" && break
    done
  else
    phase_file="$RUN_DIR/phase5.md"
  fi

  # Phase 6: Story
  if [[ "$START_PHASE" -le 6 ]]; then
    while true; do
      phase_file=$(call_phase 6 "$(phase6_prompt "$phase_file")")
      checkpoint 6 "$phase_file" && break
    done
  fi

  # Done
  divider
  log "Run complete!"
  log "All outputs: $RUN_DIR/"
  log "Final story: $RUN_DIR/phase6.md"

  # Copy final story to a clean filename
  cp "$RUN_DIR/phase6.md" "$RUN_DIR/final-story.md"
  log "Clean copy: $RUN_DIR/final-story.md"
}

main
