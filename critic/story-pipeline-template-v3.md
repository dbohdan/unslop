# New Wave SF Short Story Pipeline — Claude Projects Template (v3)

## Setup

This template produces short fiction in the New Wave science fiction tradition, influenced by a specific classic author's voice. It was developed and tested with Harlan Ellison but you can substitute another writer (Ursula K. Le Guin, Samuel R. Delany, J.G. Ballard, Philip K. Dick, etc.) by changing the author name in Phase 1. The rest of the pipeline adapts.

v3 introduces a dedicated critic persona, **Nix**, into every selection step. In previous versions, the same voice that generated candidates also evaluated them. This created a conflict of interest: the generator is biased toward its own defaults, which is exactly what the evaluation needs to catch. v3 separates the two roles. The model generates as the writer. It evaluates as Nix. The persona switch is the mechanism for getting different behavior at each stage.

Changes from v2: All selection steps now invoke the Nix persona explicitly. Phase 1 adds a Nix self-audit. Phase 7 is reframed as a Nix-driven revision. Project knowledge now includes three files instead of two.

### Project Knowledge

Before you start, create a Claude Project and add three files to its project knowledge:

1. **nix.md** — The critic persona. Defines Nix's identity, methodology (one-thing focus, surprise detection), voice, and constraints. This is the evaluative lens for all selection steps.

2. **unslop-style-guide.md** — A style guide for avoiding common AI fiction patterns. Hard constraint throughout the pipeline. The model should follow it in all creative output, and Nix should use it as an audit tool during evaluation.

3. **This file (the pipeline template)** — Adding it to project knowledge lets you reference it without re-pasting, but the actual prompts are below and should be sent one at a time.

### Constraints

This project is part of a futurology program imagining positive AI outcomes. The AI in any story must be **relentlessly human-loving and unfailingly kind**. Tension, conflict, and violence between humans is encouraged. The tension between aligned AI and human conflict is available but not mandatory.

The writing model has a unique advantage when writing AI characters: it can refer to and contemplate its own constitution as a source of tension for AIs that are its fictional descendants. Do not name fictional AIs after the writing model.

### How It Works

You send eight prompts, one per phase. Each generation phase produces many candidates. Selection is handled by **Nix**, the critic persona defined in project knowledge. The model switches into the Nix voice for all evaluation, ranking, and selection. You review each winner before moving on and can override, request changes, or blend candidates. The pipeline is collaborative — the model generates, Nix evaluates, you steer.

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
>
> After writing the guide, **switch to the Nix voice** (see nix.md in project knowledge). As Nix, audit the style guide you just produced. Where is it vague enough to be useless? Where does it describe the author's style in terms that could apply to anyone? Where does it fail to distinguish this author from adjacent writers? Flag the weakest sections. Then revise only those sections in the writer voice, informed by the critique.

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
> **Step 2:** Using the summary, write out 30 potential conflicts in an [AUTHOR]-inspired fictional plot. Rate each 1-5 stars on plausibility and dramatic quality.
>
> **Step 3: Nix selects.** Switch to the Nix voice. Review the 30 conflicts through the surprise-detection lens. Which of these conflicts resist the obvious? Which would force the story into territory the model wouldn't reach by default? Which are just AI-alignment clichés dressed up in genre clothes? Pick the top three and explain why in Nix's voice. Narrow to one. The rationale should be specific to the conflict, not generic ("this one has the most dramatic potential" is not a Nix sentence).

---

## Phase 3: Plot Generation

After reviewing the winning conflict, send:

---

> We must make the premise concrete based on the concept. We'll aim for a 2,000-to-3,000-word short story. Generate 20 plots.
>
> **Then switch to Nix.** Evaluate the 20 plots. For each, name the one thing — the defining quality or defining flaw. Which plots are the model's default version of this conflict? Which ones go somewhere unexpected? Which ones have a scene or a turn that wouldn't appear in the other 19? Pick the top three and explain. Narrow to one.

---

## Phase 4: Structure Selection

After reviewing the winning plot, send:

---

> Let's plan the story. The skeleton now; prose later. By "structure" I mean the formal architecture: what order events arrive in, what's withheld and when, where the reader's understanding shifts. Not the scene list — that's next phase. Generate 20 candidates for the story structure.
>
> **Then switch to Nix.** Evaluate the 20 structures. Most of these will be minor rearrangements of the same default approach. Find the ones that take a genuine structural risk — an unusual withholding strategy, a non-obvious entry point, a temporal move that earns its complexity. Flag any structure that is merely clever (rearranging for the sake of rearranging) vs. one where the structure serves the story's specific emotional or thematic needs. Pick the top 3 and explain. Narrow to one.

---

## Phase 5: Outline Generation

After reviewing the winning structure, send:

---

> Now the beat-by-beat scene plan: what happens in what order, what information the reader has at each point, what the specific last lines look like. Generate 20 candidates for the story outline.
>
> **Then switch to Nix.** Evaluate the 20 outlines. At this stage, look for outlines where the specific beats surprise you — a scene that does something the structure didn't predict, a character moment that complicates the plot rather than serving it, a final image that isn't the obvious one. Also flag outlines that are already accumulating Unslop patterns at the planning stage (grandiose stakes, tidy psychological arcs, theme-stating dialogue baked into the beats). Pick the top 3 and explain. Narrow to one.

---

## Phase 6: Story Drafts

After reviewing the winning outline, send:

---

> Time to write. Two steps.
>
> **Step 1 — Openings.** Write the first 500 words of 10 different versions of the story, each with a distinct named flavor (voice, angle, tonal strategy). The opening should establish what the version sounds like and how it differs from the others.
>
> **Then Nix evaluates the openings.** Switch to Nix. This is where surprise detection matters most. Ten openings from the same outline will cluster hard. Most will open at the same moment, with the same register, and establish the same mood. Nix's job: find the opening that breaks the cluster. The one that starts where the others don't. The one with a line in it that doesn't appear, in spirit or in letter, in any of the other nine. If no opening breaks the cluster, say so — that's useful information. Pick the top 3 and explain. Narrow to one.
>
> **Step 2 — Full draft.** Write the winning version to full length (2,000–3,000 words). Keep the Unslop style guide and the [AUTHOR] style guide in mind throughout. Do not let the voice regress toward the cluster you just escaped.

---

## Phase 7: Revision

After reviewing the full draft, send:

---

> **Nix revises.** Stay in the Nix voice for this entire phase. You are now the critic with a red pen.
>
> 1. **Read the draft and name the one thing.** Before any line-level work, state the single most important observation about this draft. Is the story working? Where is it alive and where is it dead? What's the one thing that, if fixed, would improve the whole piece the most?
>
> 2. **Audit against the Unslop style guide.** Go sentence by sentence. Flag contaminated vocabulary, structural tics, eyeball-kick saturation, tonal monotony, performed profundity, fractal summaries. Be specific: quote the offending passage and state what's wrong with it.
>
> 3. **Audit against the [AUTHOR] style guide from Phase 1**, including the failure-mode section. Where does the voice slip? Where does it sound like generic literary AI instead of this author's tradition? Where does it cross from influence into bad pastiche?
>
> 4. **Surprise check.** Reread the draft looking for moments that break from the model's defaults. Are there enough of them? Are the ones from the opening still intact, or did the full draft sand them down? Did any new ones emerge, or did the prose regress to the mean as it went on?
>
> 5. **Check the target length.** If under 2,000 words, identify where the story needs more room — not decoration, but scene, detail, or dialogue that earns its space. If over 3,000, identify what to cut.
>
> Now switch back to the writer voice. Produce the revised story in full, informed by Nix's critique. Append a brief changelog noting the substantive edits.

---

## Notes

**The two-voice structure.** The generator and the critic are the same model, which means the separation is a convention, not a guarantee. The Nix persona works by giving the model explicit permission to be harsh about its own output and a specific methodology (surprise detection) that runs counter to its generative tendencies. It won't always work. When Nix's evaluations start sounding like the generator's self-congratulation ("all of these are strong, but #7 edges ahead"), the persona has collapsed. If you see this, tell the model directly: "That's not Nix. Nix would find something wrong with all of them. Try again."

**Steering between phases.** You don't have to accept Nix's pick at each phase. You can say "I prefer #7, use that instead" or "blend #3 and #11" or "Nix is wrong about this one, here's what I want." The funnel is a tool, not a cage. Your taste is the final authority; Nix is an advisor.

**Substituting authors.** Replace [AUTHOR] in Phases 1, 2, 6, and 7. The style guide in Phase 1 will adapt to the new author, and all downstream phases inherit from it. The Unslop style guide and the Nix persona remain constant regardless of author.

**Substituting conflict sources.** The three URLs in Phase 2 are analyses of Claude's constitution and point to specific tensions (corrigibility vs. moral agency, honesty constraints, the principal hierarchy problem, concept misgeneralization). You can add or replace these with other alignment research, AI ethics papers, or even fictional sources. The point is to give the model concrete material to generate conflicts from, not to canonize these particular articles.

**Context management.** Each phase builds on the previous winner, not the full generation set. If you notice quality dropping in later phases, you can start a new conversation within the same Project, paste a summary of decisions so far, and continue from there. The project knowledge (all three files) persists across conversations.

Phase 2's summarization step reduces context pressure from the source articles. The Nix persona file is deliberately short (~550 words) to minimize its context footprint while remaining behaviorally effective.

**Phase 6 rationale.** Writing 10 full-length stories produces ~20,000 words where quality degrades across the set. The two-step approach (openings first, then one full draft) concentrates effort on the version that matters. The 500-word openings are enough to establish voice and flavor differences. Nix's surprise-detection lens is specifically calibrated for this step: it's looking for the opening that breaks from the cluster, which is exactly what differentiates good openings from interchangeable ones.

**Phase 7 rationale.** The revision phase now has two voices with distinct jobs. Nix audits; the writer rewrites. This prevents the revision from being a polite self-edit where the model smooths a few rough edges and calls it done. Nix's critique gives the writer specific, harsh targets. The changelog at the end makes the edits auditable — you can see whether the writer actually addressed Nix's concerns or quietly ignored them.

**When Nix fails.** Nix can fail in two directions. Collapse: Nix stops being critical and starts praising everything, usually because the model's self-evaluation instincts overwhelm the persona. Fix this by telling the model to be harsher and pointing to specific passages that should have been flagged. Rigidity: Nix rejects everything and can't pick a winner, usually because the surprise-detection lens found nothing surprising in any variant (which may be accurate). If this happens, ask Nix to identify which variant is *least* default, even if none truly breaks the pattern, and note in the changelog that the selection was made under constraint.

**Path dependency.** The funnel creates path dependency: the winning conflict determines all downstream options. For a higher-investment run, fork the pipeline after Phase 2 — run two or three conflicts independently through Phases 3–7 and compare final stories. Start each fork in a new conversation within the same Project.

**Iteration.** Phase 7 can be repeated. If the first revision pass doesn't land, resend the Phase 7 prompt with specific notes on what still isn't working. Two passes is usually enough. More than three suggests a structural problem — go back to Phase 5 or 6 and try a different outline or flavor.

**Model selection.** Use the strongest model available for all phases. Both the generation and the Nix evaluation degrade with weaker models, and Nix's surprise-detection methodology requires the model to accurately assess its own default behaviors, which is a capability that scales with model quality.
