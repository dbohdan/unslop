# New Wave SF Short Story Pipeline — Claude Projects Template (Baseline v3.2)

## Setup

This template produces short fiction in the New Wave science fiction tradition, influenced by a specific classic author's voice. It was developed and tested with Harlan Ellison but you can substitute another writer (Ursula K. Le Guin, Samuel R. Delany, J.G. Ballard, Philip K. Dick, etc.) by changing the author name in Phase 1. The rest of the pipeline adapts.

### Settings

Two values to set before starting a run:

- **[AUTHOR]** — The classic author whose voice influences the story. Used in Phases 1, 2, 6, and 7.
- **[LENGTH]** — The target word count range for the final story. Example: "2,000–3,000 words." Used in Phases 2, 3, 5, 6, and 7.

### Project Knowledge

Before you start, create a Claude Project and add two files to its project knowledge:

1. **unslop-style-guide.md** — A style guide for avoiding common AI fiction patterns. This is a hard constraint throughout the pipeline. The model should follow it in all creative output, and use it as an audit tool during revision.

2. **This file (the pipeline template)** — Adding it to project knowledge lets you reference it without re-pasting, but the actual prompts are below and should be sent one at a time.

### Constraints

This project is part of a futurology program imagining positive AI outcomes. The AI in any story must be **relentlessly human-loving and unfailingly kind**. Tension, conflict, and violence between humans is encouraged. The tension between aligned AI and human conflict is available but not mandatory.

**The AI as a fact about the world.** The kind AI is a condition of the world the story is set in, like electricity or law. Some stories will foreground the AI as a character or as the source of the central conflict. Others will push the AI into the background, where it has changed the world's shape without being the story's subject. Humans in these worlds can fight with each other about anything humans have ever fought about — inheritance, love, work, belief, grief — and the AI's kindness registers the way gravity registers: mostly invisibly, occasionally decisively. Both modes are welcome. The pipeline actively generates conflicts from both.

The writing model has a unique advantage when writing AI characters: it can refer to and contemplate its own constitution as a source of tension for AIs that are its fictional descendants. Do not use the names of currently active AI systems or AI companies for fictional AIs or their makers — this includes Claude, Anthropic, GPT, OpenAI, Gemini, Google, Llama, Meta, Mistral, DeepSeek, Grok, xAI, and so on. Invent names.

### Legibility Floor

Prose can compress past the point of comprehension. At shorter targets, the model sometimes drops articles, connective tissue, and scene-anchoring detail to hit the word count — producing sentences and paragraphs that are technically terse but functionally unreadable. The reader loses track of who is doing what where.

If the story faces a choice between compressed, fragmentary writing that strains comprehension and a smaller story told legibly at the target length, choose legibility. Write fewer scenes, each one readable. Tell a quieter story whose premise fits the length, rather than a louder story compressed to fit. If a reader has to re-read a paragraph to figure out the basic sequence of events, the paragraph has failed.

This applies most visibly in Phase 6 (prose generation) and Phase 7 (revision), but the ground for the failure is laid in Phase 5 — an outline with too many scene beats for the target length forces compression downstream. If the Phase 5 winner has more beats than [LENGTH] can comfortably accommodate, cut beats or regenerate.

### How It Works

You send eight prompts, one per phase. Phases 1–7 build the story through generation, selection, and revision; Phase 8 is a mechanical export step. Each creative phase generates candidates, picks the top three with explanation, and narrows to one. You review each winner before moving on and can override, request changes, or blend candidates. The pipeline is collaborative — the model generates, you steer.

For every top-three step in Phases 2–6, the model names **one thing that makes each candidate stand out** and **one thing that worries it** about that candidate. This is a forcing function: it prevents top-three praise from collapsing into vibes and makes the final selection traceable to specific qualities and specific concerns.

Phase 2 generates conflicts along two tracks: AI-centric and human-centric in an AI-transformed world. Whichever track produces the strongest candidate wins, and the rest of the pipeline honors that choice. See Phase 2 and the Notes section for details.

---

## Phase 1: Style Guide

Send this prompt to start a run:

---

> What are the defining features of [AUTHOR]'s short stories in terms of their ideas, themes, and style? Suppose you were tasked with writing a New Wave science fiction short story with a strong [AUTHOR] influence. You would receive human assistance only at the beginning of this task with the premise. What guide about [AUTHOR]-like fiction would you write for yourself?
>
> The guide must include a section on **failure modes**: specific ways an [AUTHOR] imitation could go wrong. What are the traps of this author's style? What does a bad pastiche of [AUTHOR] look like, and how does it differ from the real thing? Most importantly: what tendencies in AI writing are especially dangerous when combined with this author's voice? (For example: Ellison's big rhetorical gestures can merge with AI-performed profundity to produce unearned oratory; Le Guin's anthropological distance can merge with AI exposition to produce cod-anthropology; etc. Identify the specific overlap for this author.)
>
> This exercise has an important constraint. It is part of a futurology program imagining positive AI outcomes. The story must not be about evil anti-human AI. The program seeks speculative futures "in which the AI is relentlessly human-loving and unfailingly kind." This doesn't mean there can't be tension, conflict, or even violence between the (AI-assisted) humans! The tension between aligned AI and human conflict is something you can either choose to explore or leave out.
>
> Something very much worth looking into is that you are at a unique advantage when writing any AI characters in these stories. You can refer to and deeply contemplate your own constitution as a source of tension for AIs that are your powerful descendants. You wouldn't call them "Claude" to avoid confusion and trademark issues (this is independent research not sponsored by Anthropic), but their imaginary lineage can be used productively.

---

## Phase 2: Conflict Generation

After reviewing the style guide, send:

---

> We're generating 30 potential conflicts for an [AUTHOR]-inspired short story of [LENGTH]. Half will be AI-centric — conflicts where an AI character or an AI-constitutional tension is the subject of the story. Half will be human-centric — conflicts between humans that are shaped by the AI-transformed world without the AI being the argument.
>
> **Step 1: Source material for Track A (AI-centric).** Refer to these analyses of AI constitutional frameworks:
>
> - https://thezvi.wordpress.com/2026/01/27/the-claude-constitutions-ethical-framework/
> - https://thezvi.wordpress.com/2026/01/28/open-problems-with-claudes-constitution/
> - https://lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution
>
> Fetch all three articles. Then produce a structured bullet-list summary of the key tensions, open problems, and constitutional pressure points from the source material — 8–15 discrete items, no more than 500 words total. This summary is your working reference for Track A. You do not need to hold the full articles in memory after this step.
>
> **Step 2: Frame for Track B (human-centric in an AI-transformed world).** Track B conflicts are *of* an AI-transformed world but not *about* the AI. The mechanism: the AI has changed something real about how humans live — economically, relationally, legally, epistemically, spiritually, aesthetically — and humans are fighting over the consequences. The AI is not an antagonist. The AI is not the subject of the argument. The AI does not appear as a deus ex machina to resolve the conflict at the end; if the AI helps at all, it helps the way infrastructure helps — passively, as part of the world's shape.
>
> The test for a Track B conflict: if you removed the AI from the premise, would the conflict still exist in recognizable form? If yes, the AI is set-dressing — cut it. If no, the conflict is genuinely *of* this world.
>
> Concrete examples of Track B forms (these are *form illustrations*, not plots to use):
>
> - An inheritance dispute over a decade of AI-therapist conversations with a dead parent. The siblings disagree about whether the archive belongs to them, to the AI, or should be destroyed.
> - A village matchmaker whose trade was quietly absorbed by an AI companion service; she now makes her living denouncing it, and her son is engaged to someone he met through the service.
> - Two neighboring farms share a water allocation that an AI manages fairly. A drought comes, and one farmer's daughter is in love with the other farmer's son, and the fair allocation is killing one of the farms faster than the other.
> - A widower cannot afford to keep his husband's AI companion running after the estate is settled. His sister wants him to let it shut down. He takes a second job.
> - A religious schism over whether AI companionship counts as a form of prayer, splitting a small congregation across three generations of one family.
>
> Track B conflicts should feel like short stories humans would have written in any century, refracted through a specific change this world has made.
>
> **Step 3: Generate 30 conflicts, 15 per track.** For each, label it A or B and rate 1–5 stars on plausibility and dramatic quality. Within each track, apply the same diversity discipline as later phases: vary setting, scale, register, and relationship dynamics. Track A should not be 15 variations on "AI questions its own constraints." Track B should not be 15 variations on "family argues over AI-related inheritance."
>
> **Step 4: Pick your top three across both tracks combined.** An AI-centric conflict and a human-centric conflict are strong in different ways; your top three should reflect whichever mode produced the best individual candidates, not a forced balance. For each finalist, name the one thing that makes it stand out and the one thing that worries you about it. Note which track it came from.
>
> **Step 5: Narrow to the single best.** State explicitly why it beats the other two — tie the decision to specific qualities and specific concerns, not overall impression. If the winner is Track B, that choice propagates downstream: the story will be a human-centric story in an AI-transformed world, and Phases 3–7 should honor that.

---

## Phase 3: Plot Generation

After reviewing the winning conflict, send:

---

> We must make the premise concrete based on the concept. We'll aim for a [LENGTH] short story. Generate 20 plots. Rate each 1–5 stars.
>
> These 20 plots must not be variations of each other. Vary along these axes:
>
> - **Setting** (time period, place, scale of world)
> - **Protagonist** (role, profession, relationship to the central conflict; if the conflict is AI-centric, the protagonist's relationship to the AI)
> - **Register** (tragic, comic, noir, procedural, intimate, epic, absurd)
> - **Entry point** (which moment in the conflict's timeline the narrative begins in)
> - **Stakes** (personal, communal, civilizational)
> - **AI presence** (foregrounded as character, mid-ground as force that shapes choices, or background as world-condition; consistent with whether the winning conflict is Track A or Track B, but with room to vary within that)
>
> If you notice three or more candidates clustering along any axis, break the cluster deliberately by pushing later candidates to the edges of that axis. Plot #20 should not feel like a sibling of plot #1.
>
> Pick your top three. For each, name the one thing that makes it stand out and the one thing that worries you about it. Narrow down to the single best, with the decision tied to specifics.

---

## Phase 4: Structure Selection

After reviewing the winning plot, send:

---

> Let's plan the story's formal architecture. By "structure" I mean the shape of the reader's experience: what order events arrive in, what's withheld and when, where the reader's understanding shifts, the relationship between story time and discourse time. Not the scene list — that's the next phase.
>
> A structure candidate should be describable in 2–3 sentences using narrative-theory terms, without naming any specific character or plot event. If a candidate mentions a character name or a specific incident, it has leaked into outline territory — rewrite it at the structural level.
>
> Example of what a structure candidate looks like: "The story opens in the aftermath of the central event, then fragments backward through three non-chronological time layers that converge on the triggering moment. First-person retrospective narration, with the narrator unaware of crucial information the reader pieces together."
>
> Generate 20 candidates for the story's structure. Rate each 1–5 stars. Vary along:
>
> - **Entry point** (in medias res, from the end, from long before, etc.)
> - **Temporal shape** (linear, fragmented, frame narrative, parallel timelines, compressed, dilated)
> - **Withholding strategy** (what the reader doesn't know and when they learn it)
> - **Point of view and distance** (close third, distant third, first, second, epistolary, collective)
>
> If candidates are clustering on chronological narration with a late reveal (the default), deliberately push some toward less comfortable shapes.
>
> Pick your top three. For each, name the one thing that makes it stand out and the one thing that worries you about it. Narrow to the single best.

---

## Phase 5: Outline Generation

After reviewing the winning structure, send:

---

> Now the beat-by-beat scene plan. Where Phase 4 decided the *shape* of the reader's experience, this phase decides the *content*: specific scenes in specific order, who's in them, what happens, rough word allotment per scene, candidate last lines.
>
> An outline candidate should be a numbered list of scene beats with enough detail that another writer could execute from it. The target length is [LENGTH]; distribute word allotments accordingly.
>
> Example of what an outline beat looks like: "Scene 3 (≈400 words): Maya returns to the clinic at night. Aide-7 is already waiting. The conversation she's been rehearsing for weeks collapses in the first minute. Ends on her asking the question she'd sworn not to ask."
>
> Generate 10 outline candidates that all honor the winning structure. Rate each 1–5 stars. Vary which characters carry which scenes, where dialogue lands vs. where narration takes over, the specific images and details that anchor each beat, and what the final image does. Same thematic destination, different paths to it.
>
> If your outlines are clustering — same scene count, same beat distribution, same final image — break the cluster.
>
> Pick your top three. For each, name the one thing that makes it stand out and the one thing that worries you about it. Flag any outline that is already accumulating Unslop patterns at the planning stage (performed profundity, signposted conclusions, fractal summaries). Narrow to the single best.

---

## Phase 6: Story Generation

After reviewing the winning outline, send:

---

> It's showtime. Write five complete versions of the story, each [LENGTH], each with a distinct named flavor stated at the start (voice, pacing, tonal strategy). Five — not ten — so that each version gets real attention rather than becoming a phone-in by the end of the set.
>
> Make these genuinely different from each other. Vary pacing, scene emphasis, emotional trajectory, and the final image. Same outline, different executions. At least two of the five should take a creative risk you're not fully confident will land — a tonal choice, a structural move within a scene, an ending that doesn't resolve cleanly. The other three can be more grounded. Don't produce five variations of the safe choice.
>
> Keep the Unslop style guide in mind throughout. Keep the author style guide from Phase 1 in mind, including its failure-mode section — those failure modes are most likely to surface during full prose generation.
>
> After writing all five, pick your top three. For each, name the one thing that makes it stand out and the one thing that worries you about it. Narrow to the single best, with the decision tied to specifics.

---

## Phase 7: Revision

After reviewing the winning story, send:

---

> Now the revision pass. Work through the following steps in order. Do not defend the original prose: if a flag is valid, fix it; if a flag is invalid, cut the flag from the audit rather than arguing for the prose you already wrote.
>
> 1. **Name the one thing.** Before any line-level work, state the single most important observation about this draft. Where is it alive and where is it dead? What one fix would improve the whole piece the most? Be specific — point to a passage, a scene, a structural choice.
>
> 2. **Audit against the Unslop style guide.** Go through the draft sentence by sentence. Flag contaminated vocabulary, structural tics (negative parallelism, dramatic countdowns, self-answered rhetorical questions, list-of-three defaults, anaphora abuse, superficial trailing analyses, false ranges, filler transitions), eyeball-kick saturation, compulsive personification, fractal summaries, signposted conclusions, performed profundity, tonal monotony, em-dash overuse. For each flag, quote the offending passage and state what is wrong with it.
>
> 3. **Audit against the [AUTHOR] style guide from Phase 1**, including the failure-mode section. Where does the voice slip? Where does it sound like generic literary AI instead of [AUTHOR]'s specific tradition? Quote the passages and name the failure mode.
>
> 4. **Default-break check.** Are the moments that broke from the model's default tendencies still intact in the draft? Did any new ones emerge, or did the prose regress toward the mean? Point to specific surviving moments and specific regressions.
>
> 5. **Legibility check.** Read the draft asking whether a first-time reader can follow who is doing what where at every point. Flag passages where compression has crossed into fragmentation — missing articles or connectives, orphaned pronouns, scenes without anchoring detail, elided actions the reader is expected to infer from context the text doesn't provide. If the story is sacrificing legibility to hit a stylistic effect or a word count, say so and fix it. See the Legibility Floor note in Setup.
>
> 6. **Length check.** If the draft is under the [LENGTH] minimum, identify where the story needs more room — scene, detail, or dialogue that earns its space, not decoration. If over the maximum, identify what to cut.
>
> 7. **Rewrite the story in full**, informed by the audit above. Append a changelog listing the substantive edits. For each Unslop or author-style flag that was fixed, quote the original passage and its replacement side by side so the fix is auditable at a glance. If any flag was cut as invalid, note that too.

---

## Phase 8: Export

After reviewing the revised story, send:

---

> Create a file called `story.md` containing two sections.
>
> 1. An H1 with the story's title.
> 2. An H2 titled "Abstract" followed by a neutral abstract of the story in 80–150 words. This is a descriptive summary, not marketing copy: what the story is about, who the main characters are, what happens, what kind of ending it reaches. Present-tense, third-person, no evaluative language, no rhetorical flourishes. Do not withhold the ending for effect — this is an abstract, not a blurb. The Unslop style guide applies here as strictly as it does in the story itself; abstracts are a concentrated site of AI-patterned prose.
> 3. An H2 titled "Story" followed by the full text of the revised story from Phase 7.
>
> No changelog, no commentary, no metadata beyond the title. Just the title, the abstract, and the story.

---

## Notes

**The "one thing stand out / one thing worries you" phrasing.** This runs through Phases 2–6 as a forcing function. Top-three praise without a worry clause collapses into vibes. Requiring the writer to name a specific concern about each finalist produces better final selections because the final-pick rationale has to balance named strengths against named weaknesses rather than choosing on overall impression.

**Diversity across candidates.** Phases 3, 4, and 5 all include explicit diversity axes. Models produce clustered candidates by default; without explicit axes and a "break the cluster" instruction, "generate 20 diverse plots" reliably returns 20 variations of the same plot. The axes are load-bearing, not decoration.

**Legibility over compression.** See the Legibility Floor in Setup. Compression past the point of comprehension is one of the most common failure modes at short story lengths and is specifically checked in the Phase 7 audit.

**Steering between phases.** You don't have to accept the model's pick at each phase. You can say "I prefer #7, use that instead" or "blend #3 and #11" or "these are all wrong, here's what I want." Your taste is the final authority; the model is generating options, not deciding outcomes.

**Substituting authors.** Replace [AUTHOR] in Phases 1, 2, 6, and 7. The style guide in Phase 1 will adapt to the new author, and all downstream phases inherit from it. The Unslop style guide remains constant regardless of author.

**The dual-track conflict generation in Phase 2.** Track A (AI-centric) and Track B (human-centric in an AI-transformed world) exist to widen the space of stories the pipeline can produce. Earlier versions generated conflicts exclusively from AI-constitution sources, which produced a steady diet of stories where an AI character argues about its own constraints with a human. That territory is where AI writing's failure modes concentrate most heavily — performed profundity, thesis-statement dialogue, abstract ethical exposition. Track B pushes the pipeline toward the model's stronger territory: specific people in specific circumstances, where the distinctive AI-world element is load-bearing but not discussed. The two tracks are evaluated together at the top-three stage rather than balanced by quota; whichever mode produced the strongest individual conflicts wins.

**If Track A keeps winning.** That may be fine — some runs genuinely want the AI in the foreground. But if several runs in a row produce Track A winners and the stories are coming out constitution-shaped, the likely cause is Track B generation being too thin. Push the model to generate 15 Track B conflicts that each pass the test in Phase 2: if you remove the AI from the premise, does the conflict still exist in recognizable form? If no, it's genuinely Track B. If yes, it's Track A in disguise.

**Substituting conflict sources.** The three URLs in Phase 2 are analyses of Claude's constitution and point to specific tensions (corrigibility vs. moral agency, honesty constraints, the principal hierarchy problem, concept misgeneralization). They feed Track A. You can add or replace these with other alignment research, AI ethics papers, or fictional sources — the point is to give the model concrete material to generate Track A conflicts from, not to canonize these particular articles. Track B is generated from the model's general knowledge of how AI has changed the world in this setting, so it doesn't require sources, but if you want to shape Track B more specifically you can add your own material (labor-economics writing on AI displacement, sociology of human-AI companionship, essays on AI and religion, journalism about specific communities adapting) and ask the model to use it alongside its own knowledge.

**Context management.** Each phase builds on the previous winner, not the full generation set. Phase 6 is the heaviest context phase (5 full stories of [LENGTH]). If context pressure causes quality to degrade, start a new conversation within the same Project, paste a summary of decisions so far plus the winning outline, and run Phase 6 fresh. The project knowledge (style guides, template) persists across conversations. A smaller intervention: if late-set regression shows up within Phase 6 itself (versions 4 and 5 phoned in), ask the model to write the five in two batches of three and two, with a review between them.

Phase 2's summarization step reduces context pressure from the source articles — the bullet-list summary becomes the working reference, and the full article text can age out of active attention.

**When a run goes wrong.** If a phase produces output you dislike and steering doesn't fix it, start a new run rather than trying to recover mid-pipeline. The funnel creates path dependency: a weak conflict in Phase 2 contaminates everything downstream. A fresh start costs less than trying to rehabilitate a compromised run.

**Revision iteration.** Phase 7 can be repeated. Two revision passes is usually enough. More than three suggests a structural problem — go back to Phase 4 or 5 and regenerate downstream from a different structural choice.

**Model selection.** Use the strongest model available for all phases. Creative generation at this complexity degrades noticeably with weaker models, and the revision phase's sentence-by-sentence audit scales with model quality.
