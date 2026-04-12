# New Wave SF Short Story Pipeline — Claude Projects Template (v2)

## Setup

This template produces short fiction in the New Wave science fiction tradition, influenced by a specific classic author's voice. It was developed and tested with Harlan Ellison but you can substitute another writer (Ursula K. Le Guin, Samuel R. Delany, J.G. Ballard, Philip K. Dick, etc.) by changing the author name in Phase 1. The rest of the pipeline adapts.

v2 incorporates revisions from a full Ellison test run. Changes from v1: Phase 1 now includes a failure-mode section. Phase 2 adds a summarization step to manage context. Phase 6 is split into two steps (openings, then full drafts). Phase 7 (revision) is new. Notes section is expanded with observations on path dependency and forking.

### Project Knowledge

Before you start, create a Claude Project and add two files to its project knowledge:

1. **unslop-style-guide.md** — A style guide for avoiding common AI fiction patterns. This is a hard constraint throughout the pipeline. The model should follow it in all creative output, and should also use it as a filter in upstream decisions (conflict selection, plot design, structure choices) — not only at the prose stage.

2. **This file (the pipeline template)** — Adding it to project knowledge lets you reference it without re-pasting, but the actual prompts are below and should be sent one at a time.

### Constraints

This project is part of a futurology program imagining positive AI outcomes. The AI in any story must be **relentlessly human-loving and unfailingly kind**. Tension, conflict, and violence between humans is encouraged. The tension between aligned AI and human conflict is available but not mandatory.

The writing model has a unique advantage when writing AI characters: it can refer to and contemplate its own constitution as a source of tension for AIs that are its fictional descendants. Do not name fictional AIs after the writing model.

### How It Works

You send eight prompts, one per phase. Each phase generates many candidates, picks the top three with explanation, and narrows to one. You review each winner before moving on and can override, request changes, or blend candidates. The pipeline is collaborative — the model generates, you steer.

Target story length: 2,000–3,000 words.

---

## Phase 1: Style Guide

Send this prompt to start a run:

---

> What are the defining features of [AUTHOR]'s short stories in terms of their ideas, themes, and style? Suppose you were tasked with writing a New Wave science fiction short story with a strong [AUTHOR] influence. You would receive human assistance only at the beginning of this task with the premise. What guide about [AUTHOR]-like fiction would you write for yourself?
>
> The guide must include a section on **failure modes**: specific ways an [AUTHOR] imitation could go wrong. What are the traps of this author's style? What does a bad pastiche of [AUTHOR] look like, and how does it differ from the real thing? What tendencies in AI writing are especially dangerous when combined with this author's voice?
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
> **Step 1:** Fetch all three articles. Then produce a condensed summary of the key tensions, open problems, and constitutional pressure points from the source material — no more than 500 words total. This summary is your working reference for the rest of the phase. You do not need to hold the full articles in memory after this step.
>
> **Step 2:** Using the summary, write out 30 potential conflicts in an [AUTHOR]-inspired fictional plot. Rate each 1-5 stars on plausibility and dramatic quality. Pick your top three and explain why. Narrow down to the single best.

---

## Phase 3: Plot Generation

After reviewing the winning conflict, send:

---

> We must make the premise concrete based on the concept. We'll aim for a 2,000-to-3,000-word short story. Generate 20 plots. Pick top three and explain why. Narrow down to the best.

---

## Phase 4: Structure Selection

After reviewing the winning plot, send:

---

> Let's plan the story. The skeleton now; prose later. By "structure" I mean the formal architecture: what order events arrive in, what's withheld and when, where the reader's understanding shifts. Not the scene list — that's next phase. Generate 20 candidates for the story structure. Pick the top 3 and explain. Narrow down to one.

---

## Phase 5: Outline Generation

After reviewing the winning structure, send:

---

> Let's plan the story. We'll create a skeleton now and flesh it out with prose later. By "outline" I mean the beat-by-beat scene plan: what happens in what order, what information the reader has at each point, what the specific last lines look like. Same process: generate 20 candidates for the story outline. Pick the top 3 and explain. Narrow down to one.

---

## Phase 6: Story Drafts

After reviewing the winning outline, send:

---

> Time to write. We'll do this in two steps.
>
> **Step 1 — Openings.** Write the first 500 words of 10 different versions of the story, each with a distinct named flavor (voice, angle, tonal strategy). The opening should be enough to establish what the version sounds like and how it differs from the others. Pick the top 3 and explain why. Narrow to one.
>
> **Step 2 — Full draft.** Write the winning version to full length (2,000–3,000 words). Always have the Unslop style guide in mind.

---

## Phase 7: Revision

After reviewing the full draft, send:

---

> Revise the story. Specifically:
>
> 1. **Audit against the Unslop style guide.** Check every sentence. Flag and fix any contaminated vocabulary, structural tics, eyeball-kick saturation, or tonal monotony. Be specific about what you changed and why.
>
> 2. **Audit against the [AUTHOR] style guide from Phase 1**, including the failure-mode section. Is the voice consistent? Where does it slip into generic AI prose or bad pastiche? Fix it.
>
> 3. **Read it aloud in your head.** Does the prose have the rhythm of speech? Are there sentences that exist only to sound literary? Cut them. Are there stretches that are too uniform in length or density? Vary them.
>
> 4. **Check the target length.** If the draft is under 2,000 words, identify where the story needs more room and expand those sections — not by adding decoration, but by adding scene, detail, or dialogue that earns its space. If over 3,000, cut.
>
> Produce the revised story in full with a brief changelog at the end noting the substantive edits.

---

## Notes

**Steering between phases.** You don't have to accept the model's pick at each phase. You can say "I prefer #7, use that instead" or "blend #3 and #11" or "these are all wrong, here's what I want." The funnel is a tool, not a cage.

**Substituting authors.** Replace [AUTHOR] in Phases 1, 2, and 7. The style guide in Phase 1 will adapt to the new author, and all downstream phases inherit from it. The Unslop style guide remains constant regardless of author — it addresses AI writing patterns, not any specific literary style.

**Substituting conflict sources.** The three URLs in Phase 2 are analyses of Claude's constitution and point to specific tensions (corrigibility vs. moral agency, honesty constraints, the principal hierarchy problem, concept misgeneralization). You can add or replace these with other alignment research, AI ethics papers, or even fictional sources. The point is to give the model concrete material to generate conflicts from, not to canonize these particular articles.

**Context management.** Each phase builds on the previous winner, not the full generation set. If you notice quality dropping in later phases, you can start a new conversation within the same Project, paste a summary of decisions so far, and continue from there. The project knowledge (style guides) persists across conversations.

Phase 2's summarization step is specifically designed to reduce context pressure. The source articles are long (10,000+ words each) and are only needed for conflict generation — not for any downstream phase. Summarizing them into working notes before generating conflicts keeps the context window focused.

**Phase 6 rationale.** v1 asked for 10 full-length stories. In practice, this produces ~20,000 words of output where quality degrades across the set — later versions recycle details from earlier ones and the comedy engines (or whatever the story's main register is) get less inventive. The two-step approach (openings first, then one full draft) concentrates effort on the version that matters. The 500-word openings are enough to establish voice and flavor differences; you don't need 2,000 words to tell whether a version is working.

**Phase 7 rationale.** v1 had no revision pass. The pipeline produced a winner and stopped. In practice the winning draft needs expansion (often coming in under the 2,000-word minimum), tightening, and a close edit against both style guides. The revision phase formalizes this. It also catches Unslop violations that slip through during generation — the model is less prone to contaminated vocabulary when it's specifically auditing for it than when it's generating at speed.

**Path dependency.** The funnel creates path dependency: the winning conflict determines all downstream options. A strong conflict that produces a weak plot may foreclose a weaker conflict that would have produced a better story. For a higher-investment run, you can fork the pipeline after Phase 2 — run two or three conflicts independently through Phases 3–6 and compare final stories. This doubles or triples the cost but eliminates the risk of a locally-optimal-but-globally-suboptimal path. If forking, start each fork in a new conversation (within the same Project) to avoid context contamination between paths.

**Model selection.** Use the strongest model available for all phases. Creative generation at this complexity degrades noticeably with weaker models.

**Iteration.** Phase 7 can be repeated. If the first revision pass doesn't land, you can send the Phase 7 prompt again with specific notes on what still isn't working. Two revision passes is usually enough. More than three suggests a structural problem that revision can't fix — at that point, go back to Phase 5 or Phase 6 and try a different outline or flavor.
