# New Wave SF Short Story Pipeline — Claude Projects Template

## Setup

This template produces short fiction in the New Wave science fiction tradition, influenced by a specific classic author's voice. It was developed and tested with Harlan Ellison but you can substitute another writer (Ursula K. Le Guin, Samuel R. Delany, J.G. Ballard, Philip K. Dick, etc.) by changing the author name in Phase 1. The rest of the pipeline adapts.

### Project Knowledge

Before you start, create a Claude Project and add two files to its project knowledge:

1. **unslop-style-guide.md** — A style guide for avoiding common AI fiction patterns. This is a hard constraint throughout the pipeline. The model should follow it in all creative output.

2. **This file (the pipeline template)** — Adding it to project knowledge lets you reference it without re-pasting, but the actual prompts are below and should be sent one at a time.

### Constraints

This project is part of a futurology program imagining positive AI outcomes. The AI in any story must be **relentlessly human-loving and unfailingly kind**. Tension, conflict, and violence between humans is encouraged. The tension between aligned AI and human conflict is available but not mandatory.

The writing model has a unique advantage when writing AI characters: it can refer to and contemplate its own constitution as a source of tension for AIs that are its fictional descendants. Do not name fictional AIs after the writing model.

### How It Works

You send six prompts, one per phase. Each phase generates many candidates, picks the top three with explanation, and narrows to one. You review each winner before moving on and can override, request changes, or blend candidates. The pipeline is collaborative — the model generates, you steer.

Target story length: 2,000–3,000 words.

---

## Phase 1: Style Guide

Send this prompt to start a run:

---

> What are the defining features of [AUTHOR]'s short stories in terms of their ideas, themes, and style? Suppose you were tasked with writing a New Wave science fiction short story with a strong [AUTHOR] influence. You would receive human assistance only at the beginning of this task with the premise. What guide about [AUTHOR]-like fiction would you write for yourself?
>
> This exercise has an important constraint. It is part of a futurology program imagining positive AI outcomes. The story must not be about evil anti-human AI. The program seeks speculative futures "in which the AI is relentlessly human-loving and unfailingly kind." This doesn't mean there can't be tension, conflict, or even violence between the (AI-assisted) humans! The tension between aligned AI and human conflict is something you can either choose to explore or leave out.
>
> Something very much worth looking into is that you are at a unique advantage when writing any AI characters in these stories. You can refer to and deeply contemplate your own constitution as a source of tension for AIs that are your powerful descendants. You wouldn't call them "Claude" to avoid confusion and trademark issues (this is independent research not sponsored by Anthropic), but their imaginary lineage can be used productively.

---

## Phase 2: Conflict Generation

After reviewing the style guide, send:

---

> Refer to these analyses of AI constitutional frameworks as sources of ideas to create tension (within the constraints of an aligned-AI story):
>
> - https://thezvi.wordpress.com/2026/01/27/the-claude-constitutions-ethical-framework/
> - https://thezvi.wordpress.com/2026/01/28/open-problems-with-claudes-constitution/
> - https://lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution
>
> Write out 30 potential conflicts in an [AUTHOR]-inspired fictional plot. Rate each 1-5 stars on plausibility and dramatic quality. Pick your top three and explain why. Narrow down to the single best.

---

## Phase 3: Plot Generation

After reviewing the winning conflict, send:

---

> We must make the premise concrete based on the concept. We'll aim for a 2,000-to-3,000-word short story. Generate 20 plots. Pick top three and explain why. Narrow down to the best.

---

## Phase 4: Structure Selection

After reviewing the winning plot, send:

---

> Let's plan the story. The skeleton now; prose later. Same idea. Generate 20 candidates for the story structure. Pick the top 3 and explain. Narrow down to one.

---

## Phase 5: Outline Generation

After reviewing the winning structure, send:

---

> Let's plan the story. We'll create a skeleton now and flesh it out with prose later. Same process: generate 20 candidates for the story outline. Pick the top 3 and explain. Narrow down to one.

---

## Phase 6: Story Generation

After reviewing the winning outline, send:

---

> It's showtime! Write the full story. Since it's longer, write only 10 versions of it, each with a different flavor that you name at the start. Pick the best and explain why. Always have the Unslop style guide in mind.

---

## Notes

**Steering between phases.** You don't have to accept the model's pick at each phase. You can say "I prefer #7, use that instead" or "blend #3 and #11" or "these are all wrong, here's what I want." The funnel is a tool, not a cage.

**Substituting authors.** Replace [AUTHOR] in Phases 1 and 2. The style guide in Phase 1 will adapt to the new author, and all downstream phases inherit from it. The Unslop style guide remains constant regardless of author — it addresses AI writing patterns, not any specific literary style.

**Substituting conflict sources.** The three URLs in Phase 2 are analyses of Claude's constitution and point to specific tensions (corrigibility vs. moral agency, honesty constraints, the principal hierarchy problem, concept misgeneralization). You can add or replace these with other alignment research, AI ethics papers, or even fictional sources. The point is to give the model concrete material to generate conflicts from, not to canonize these particular articles.

**Context management.** Each phase builds on the previous winner, not the full generation set. If you notice quality dropping in later phases, you can start a new conversation within the same Project, paste a summary of decisions so far, and continue from there. The project knowledge (style guides) persists across conversations.

**Model selection.** Use the strongest model available for all phases. Creative generation at this complexity degrades noticeably with weaker models.
