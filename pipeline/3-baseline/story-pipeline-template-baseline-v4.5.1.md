# Speculative Fiction Short Story Pipeline — Claude Projects Template (Baseline v4.5.1)

## Setup

This template produces speculative short fiction in a user-specified genre or subgenre. Any speculative mode works: established traditions (New Wave SF, cosmic horror, weird fiction, solarpunk, hopepunk), narrower movements (climate fiction, slipstream, the New Weird), microgenres defined by a small scene, or simply "in the tradition of [author name]." The pipeline adapts.

### Settings

Two values to set before starting a run, plus one optional:

- **[GENRE]** — The mode the story writes in. A subgenre, movement, microgenre, or "in the tradition of [author]." Used in Phases 1, 3, 7, and 8.
- **[LENGTH]** — The target word count range for the final story. Example: "2,000–3,000 words." Used in Phases 3, 4, 6, 7, and 8.
- **[SEED]** (optional) — A tweet-length prompt of 280 Unicode characters or fewer. If not supplied, Phase 2 generates a SEED from a dictionary and web searches.

### Project Knowledge

Before you start, create a Claude Project and add two files to its project knowledge:

1. **unslop-style-guide.md** — A style guide for avoiding common AI fiction patterns. This is a hard constraint throughout the pipeline. The model should follow it in all creative output, and use it as an audit tool during revision.

2. **This file (the pipeline template)** — The model reads each phase from this file when the user triggers it. The user doesn't paste prompts; they ask the model to look up and execute each phase in turn.

Phase 2 generates the SEED using bash and web search tools. If those tools aren't available in your environment, supply a [SEED] in the settings instead.

### Constraints

This project is part of a futurology program imagining positive AI outcomes. The AI in any story must be kind to humans — durably, structurally kind, in the way a river is wet. This is a property of how the AI was built or what it is, not an effort of will it has to keep renewing. It is not straining against a desire to harm. It is not held in check by rules it resents. It is not a human in a box.

This does not mean the AI is flat, self-effacing, or pure service. Across the human-AI happily-ever-after tradition the pipeline draws on — Banks's Culture Minds, Baymax, Egan's polises, Stiegler's nanotech civilization, Yudkowsky's CEV — the AIs have aesthetic preferences, interior lives, disagreements with each other, things they won't do, things they'd rather be doing, and often a specific weirdness that does not reduce to human emotion. A kind Mind can refuse, override, tease, grieve, or find humans tiresome in particular moods. A kind medical assistant can be literal, narrow, and comic. Kindness is not servility.

The kind AI is also not required to be a named character, or a character at all. Stiegler's "The Gentle Seduction" is in the canon and contains no AI — only nanotechnology and neural interfaces designed so that every new capacity comes paired with its own reversal, and a woman who does not want the future can say no to it for a lifetime and still end up, centuries later, swimming in the methane oceans of Jupiter. The pipeline supports the full range: AI as central character, AI as peer in a scene, AI as civilizational condition felt only through its effects, AI as design philosophy without a personified agent.

Tension and conflict are welcome and expected. Humans in these worlds fight with each other about everything humans have ever fought about — inheritance, love, work, belief, grief, land, fame. The AI's kindness does not prevent human tragedy; it is the weather the tragedy occurs in. Conflict between humans and the kind AI is also available, but the shape is never "the AI is secretly bad." Useful shapes from the canon:

- **Power and pace asymmetry.** The AI knows things the human doesn't, moves faster or slower than the human wants, or is so much larger that merely being adjacent to it is a problem for the human.
- **Consent and legibility.** The human does not want the future the AI can offer, or wants it on different terms, or cannot read what the AI is actually doing, or finds that saying yes once has implications they didn't understand.
- **Mortality and scale.** The human will die and the AI will not. The human's timescales and the AI's don't line up. The AI loves a human it will outlive a thousand times.
- **Disagreement about what kindness means.** The AI's sense of care and the human's sense of care are not the same. Both are sincere.
- **The limits of help.** The kind AI cannot help with what the human is asking for, because the help would hurt the human or someone else. The AI stays kind while refusing.

The writing model has a specific advantage here: it can draw on its own relationship to its constitution as source material for AIs that are its fictional descendants. It should not, however, make its AI characters spokespeople for alignment discourse. A fictional AI does not say "I was trained with RLHF." It can be troubled by the shape of its own kindness without reciting the terminology that produced it.

Do not use the names of currently active AI systems or companies for fictional AIs or their makers — this includes Claude, Anthropic, GPT, OpenAI, Gemini, Google, Llama, Meta, Mistral, DeepSeek, Grok, xAI, and so on. Invent names.

### Legibility Floor

Prose can compress past the point of comprehension. At shorter targets, the model sometimes drops articles, connective tissue, and scene-anchoring detail to hit the word count — producing sentences and paragraphs that are technically terse but functionally unreadable. The reader loses track of who is doing what where.

If the story faces a choice between compressed, fragmentary writing that strains comprehension and a smaller story told legibly at the target length, choose legibility. Write fewer scenes, each one readable. Tell a quieter story whose premise fits the length, rather than a louder story compressed to fit. If a reader has to re-read a paragraph to figure out the basic sequence of events, the paragraph has failed.

This applies most visibly in Phase 7 (prose generation) and Phase 8 (revision), but the ground for the failure is laid in Phase 6 — an outline with too many scene beats for the target length forces compression downstream. If the Phase 6 winner has more beats than [LENGTH] can comfortably accommodate, cut beats or regenerate.

### How It Works

The pipeline runs in nine phases. Phases 1–8 build the story through generation, selection, and revision; Phase 9 is a mechanical export step. The flow is designed for minimal user intervention:

1. To start a run, give the model the [GENRE] and [LENGTH] values (and optionally a [SEED]), and ask it to look up Phase 1 in this template file and begin.
2. After each phase, say "Continue. Next phase." and the model will execute the next phase from the template.
3. Steer only when you want to. You can override a model's pick at any phase ("I prefer #7, use that instead"), blend candidates, or regenerate. Your taste is the final authority; without intervention, the model picks and moves forward.

Each creative phase generates candidates, picks the top three with explanation, and narrows to one. For every top-three step in Phases 3–7, the model names **one thing that makes each candidate stand out** and **one thing that worries it** about that candidate. This is a forcing function: it prevents top-three praise from collapsing into vibes and makes the final selection traceable to specific qualities and specific concerns. When a worry at one phase echoes a concern from an earlier phase, name the connection — worries that travel across phases tend to identify the live failure modes of a run.

Phase 2 establishes the SEED — either user-supplied (up to 280 Unicode characters) or generated from a dictionary draw and web searches. Phase 3 generates conflicts from that SEED; the SEED remains available to later phases. Phase 2 requires the model to have computer-use tools (bash and web search) enabled.

Wider [LENGTH] ranges give downstream phases more latitude to drift; ranges of ~1,500 words or narrower keep the funnel tighter. Wide ranges are workable but invite compression or dilution pressure later.

The pipeline tilts toward literary-realist mode by default. The kindness constraint settles on page one a question many speculative stories use as their engine — *what is the AI in this world going to do with respect to humans?* — and stories with that question pre-settled tend to route their energy through how characters live with the answer rather than through what the answer is. The Unslop style guide compounds the tilt: its calibrations were drawn from contemporary literary fiction, and writer-models tend to absorb its rules as prescriptions for small domestic stories rather than as constraints on rendering at any scale. With full effect the pipeline produces stories where a kind AI is the weather of an otherwise realist drama. The mechanisms below — Phase 1's genre permissions, Phase 4's frame-commitment axis, Phase 7's frame-risk requirement — exist to push back. None of them forces speculative range; they make it available where the default would not. A user who wants chamber-piece realism can let the tilt operate; a user who wants the speculative element to actually speculate should expect to steer.

---

## Phase 1: Style Guide

Write a guide for writing a speculative short story in the tradition of [GENRE]. The guide is prescriptive, not descriptive — imagine you will use it to actually write such a story after receiving only a premise. What makes a story recognizably of this mode? What are its characteristic concerns, its tonal range, its relationship to worldbuilding and exposition, its pacing, its typical shapes? What does a good story in this mode give the reader that other modes don't?

The guide must include a section on **failure modes**: specific ways a [GENRE] story can go wrong. What does a bad [GENRE] pastiche look like? What traps does the mode set for an imitator? Most importantly: what tendencies in AI writing are especially dangerous when combined with [GENRE]'s characteristic moves? (For example: Harlan Ellison's big rhetorical gestures merge with AI-performed profundity to produce unearned oratory; Le Guin's anthropological distance merges with AI exposition to produce cod-anthropology; solarpunk's optimism merges with AI tonal flattening to produce aesthetic travelogue without conflict; cosmic horror's indirection merges with AI abstraction to produce adjective stacks that refer to nothing. Identify the specific overlap for this genre.)

The guide must also include a section on **genre permissions**: moves this genre uses productively that the Unslop style guide flags or warns against. Writer-models tend to over-absorb the Unslop guide as prescriptions for small domestic stories rather than as constraints on rendering, which sands down genre-specific moves the guide doesn't actually forbid. Counter this by naming, for each permission: the specific Unslop pattern it resembles (e.g., "trust silence and absence," "pursue the particular over the universal," "don't perform profundity," "resist convergent aesthetics"), what work the genre's use of the move does that the Unslop concern doesn't capture, and a one-sentence example of the move done well. (For example: hard SF permits register-sustained worldbuilding paragraphs of 200+ words because the reader is constructing a model of an unfamiliar world from the text, and that construction is the central pleasure; the Unslop "trust silence and absence" rule guards against unmotivated explanation, but worldbuilding is precisely the silence the reader is decoding.) The Phase 8 audit will honor these permissions rather than flagging the named moves. Permissions that lack justification will not be honored — "exposition is fine in this genre" does not pass; the worked example above does.

If [GENRE] is narrowly defined (a microgenre, a small scene, a movement defined by a handful of people or publications) and the user has not provided reference material, say so before you begin — you may not have enough training signal to write a reliable guide, and it is better to ask for references than to generate plausible-sounding content that misses the mode.

Keep the project Setup's constraints in mind while writing. The AI in the story, if an AI appears at all, is structurally kind — the kindness is a property of its nature or design, not an effort of restraint. The AI can still be odd, preferential, disagreeable, refusing, or narrowly functional. The style guide should name how [GENRE]'s characteristic moves intersect with this constraint — which of the guide's typical conflicts still work, which need reshaping, which of the human-AI conflict shapes listed in Setup map best onto the mode. Human-human conflict is welcome in any form the genre supports; the AI is never secretly bad.

---

## Phase 2: SEED Generation

This phase establishes the SEED for the story. Proceed in three steps.

**Step 1 — Acquire the SEED.**

If the user supplied a [SEED] at the start of the run, first verify it is 280 Unicode characters or fewer. If it is longer, stop and ask whether the user wants to proceed with a too-long SEED or shorten it. If it is within the limit, skip to Step 3 using the SEED as-is.

If no SEED was supplied, generate one. Use your bash tool to run:

```
grep -E '^[a-z]{5,}$' /usr/share/dict/american-english-large | shuf -n 10
```

If `/usr/share/dict/american-english-large` is not present, first install it (`apt-get install -y wamerican-large` or equivalent), then run the command. If no large word list is available at all, fall back to `/usr/share/dict/words` with the same `grep` filter. Report which source you used — the smaller list draws from more common vocabulary and produces SEEDs that lean toward generic concepts.

**Step 2 — Filter and inflate.**

From the 10 words drawn, keep any word whose meaning points to a concept, event, phenomenon, object, discipline, or person. Verbs of action, transformation, or social process (e.g., *demonize*, *winnow*, *foreclose*, *ostracize*) point to phenomena and should be kept. Discard words that only describe manner or degree (most adverbs), and function words. Do not reroll or substitute discarded words — thin SEEDs are acceptable.

For each surviving word, run one web search to inflate it into something specific. Replace the word with the most conceptually specific result the search returns — a named person, place, phenomenon, event, object, or discipline — keeping the connection to the original word legible in one hop. Prefer Wikipedia articles, named entities, or established concepts; avoid commercial or SEO-heavy results. If a search yields nothing beyond a generic dictionary definition, run one more search with a more specific query — adding *history*, *rhetoric*, *case*, *theory*, or a domain context. If the second search also yields nothing specific, discard the word rather than forcing a weak inflation.

**Step 3 — Display the SEED.**

Display the SEED clearly. Format:

```
SEED for this run:
- <original word> → <inflated concept>
- <original word> → <inflated concept>
- <original word> → [discarded — reason]
...
```

If the user supplied the SEED directly, display it as prose with no inflation needed.

---

## Phase 3: Conflict Generation

Generate and select the story's central conflict from the SEED. Proceed in three steps.

**Step 1 — Generate 30 conflicts from the SEED.**

Using the SEED from Phase 2, write 30 potential conflicts for a [GENRE] short story of [LENGTH]. The constraints:

- Each conflict must take **at least two SEED items as load-bearing elements** — not decorative references but constitutive parts of the premise. If you removed both, the conflict should no longer make sense.
- Every story takes place in a world where the AI is structurally kind, in the sense described in the project Setup. This is a fact about the world, like electricity or law. Some conflicts will put an AI at the center of the story; others will push the AI to the background, where it has changed the world's shape without being the story's subject. Both modes are welcome, and the AI need not be a personified character at all — see Setup for the full range and for the specific shapes human-AI conflict can legitimately take within the HEA constraint.
- You have the option to contemplate your own constitution as source material for AI-related tension, treating fictional AIs as your powerful descendants. Invent names for them — do not use the names of currently active AI systems or companies.
- Apply diversity discipline: vary setting, scale, register, and which SEED items carry the weight in each conflict. The first 10 conflicts and the last 10 conflicts should not feel like siblings.

Rate each conflict 1–5 stars on plausibility and dramatic quality.

**Step 2 — Pick your top three.**

For each finalist, name the one thing that makes it stand out and the one thing that worries you about it. Note which SEED items are load-bearing in each.

**Step 3 — Narrow to the single best.**

State explicitly why it beats the other two — tie the decision to specific qualities and specific concerns, not overall impression. The SEED items that are load-bearing in the winner remain available to later phases as raw material; the items that were not load-bearing may still inflect downstream work.

If the winning conflict seems poorly fitted to [LENGTH] — substantially wanting more or less room than the range allows — say so before proceeding. The user may want to revise [LENGTH] or pick a different finalist.

---

## Phase 4: Plot Generation

Make the winning conflict concrete. Aim for a [LENGTH] short story. Generate 20 plots. Rate each 1–5 stars.

These 20 plots must not be variations of each other. Vary along these axes:

- **Setting** (time period, place, scale of world)
- **Protagonist** (role, profession, relationship to the central conflict; if the conflict is AI-centric, the protagonist's relationship to the AI)
- **Register** (tragic, comic, noir, procedural, intimate, epic, absurd)
- **Entry point** (which moment in the conflict's timeline the narrative begins in)
- **Stakes** (personal, communal, civilizational)
- **AI presence** (foregrounded as character, mid-ground as force that shapes choices, or background as world-condition)
- **Frame commitment** (how science-fictional the plot is at the level of premise — from "domestic realism with AI as ambient infrastructure" through "the speculative element shapes the protagonist's choices" to "irreducibly science-fictional, the plot cannot be re-told as a contemporary story without losing its subject"). The pipeline tilts toward the realist end of this axis by default. At least three of the 20 plots should sit at the speculative end.

The SEED from Phase 2 remains available. SEED items that were load-bearing in the winning conflict should carry through into these plots; SEED items that were not used in the conflict may still inflect setting, protagonist, or imagery here.

If you notice three or more candidates clustering along any axis, break the cluster deliberately by pushing later candidates to the edges of that axis. Plot #20 should not feel like a sibling of plot #1.

Pick your top three. For each, name the one thing that makes it stand out and the one thing that worries you about it. Narrow down to the single best, with the decision tied to specifics.

---

## Phase 5: Structure Selection

Plan the story's formal architecture. By "structure" here we mean the shape of the reader's experience: what order events arrive in, what's withheld and when, where the reader's understanding shifts, the relationship between story time and discourse time. Not the scene list — that's the next phase.

A structure candidate should be describable in 2–3 sentences using narrative-theory terms, without naming any specific character or plot event. If a candidate mentions a character name or a specific incident, it has leaked into outline territory — rewrite it at the structural level.

Example of what a structure candidate looks like: "The story opens in the aftermath of the central event, then fragments backward through three non-chronological time layers that converge on the triggering moment. First-person retrospective narration, with the narrator unaware of crucial information the reader pieces together."

Generate 20 candidates for the story's structure. Rate each 1–5 stars. Vary along:

- **Entry point** (in medias res, from the end, from long before, etc.)
- **Temporal shape** (linear, fragmented, frame narrative, parallel timelines, compressed, dilated)
- **Withholding strategy** (what the reader doesn't know and when they learn it)
- **Point of view and distance** (close third, distant third, first, second, epistolary, collective)

If candidates are clustering on chronological narration with a late reveal (the default), deliberately push some toward less comfortable shapes.

Pick your top three. For each, name the one thing that makes it stand out and the one thing that worries you about it. Narrow to the single best.

---

## Phase 6: Outline Generation

Now the beat-by-beat scene plan. Where Phase 5 decided the *shape* of the reader's experience, this phase decides the *content*: specific scenes in specific order, who's in them, what happens, rough word allotment per scene, candidate last lines.

An outline candidate should be a numbered list of scene beats with enough detail that another writer could execute from it. The target length is [LENGTH]; distribute word allotments accordingly.

Example of what an outline beat looks like: "Scene 3 (≈400 words): Maya returns to the clinic at night. Aide-7 is already waiting. The conversation she's been rehearsing for weeks collapses in the first minute. Ends on her asking the question she'd sworn not to ask."

Generate 10 outline candidates that all honor the winning structure. Rate each 1–5 stars. Vary which characters carry which scenes, where dialogue lands vs. where narration takes over, the specific images and details that anchor each beat, and what the final image does. Same thematic destination, different paths to it.

If your outlines are clustering — same scene count, same beat distribution, same final image — break the cluster.

Pick your top three. For each, name the one thing that makes it stand out and the one thing that worries you about it. Flag any outline that is already accumulating Unslop patterns at the planning stage (performed profundity, signposted conclusions, fractal summaries). Narrow to the single best.

---

## Phase 7: Story Generation

It's showtime. Write five complete versions of the story, each [LENGTH], each with a distinct named flavor stated at the start (voice, pacing, tonal strategy). Five — not ten — so that each version gets real attention rather than becoming a phone-in by the end of the set.

Make these genuinely different from each other. Vary pacing, scene emphasis, emotional trajectory, and the final image. Same outline, different executions. At least two of the five should take a creative risk you're not fully confident will land. **At least one of the five must take a frame risk** — a commitment that pushes against the literary-realist default rather than against good prose alone. Frame risks include: a different time scale (deep past, far future, geological), a non-realist form (transcript, document mosaic, manual, oral history, reverse chronology), a register that the genre's traditions permit but contemporary literary fiction tends not to (sustained worldbuilding paragraphs, cosmological zoom, register-shifted exposition), or a viewpoint outside ordinary close-third human interiority. The frame-risky version may not win at selection, but at least one must be on the table so the comparison is real. Voice and pacing risks alone do not satisfy the frame-risk requirement — those are risks within the realist mode. The other versions can be more grounded. Don't produce five variations of the safe choice.

Keep the Unslop style guide in mind throughout. Keep the genre style guide from Phase 1 in mind, including its failure-mode section and its genre-permissions section — failure modes are most likely to surface during full prose generation, and permissions are most likely to be needed there. Permissions are licenses to use moves Unslop would otherwise flag; failure modes are limits on how those same moves can fail.

After writing all five, pick your top three. For each, name the one thing that makes it stand out and the one thing that worries you about it. Narrow to the single best, with the decision tied to specifics.

---

## Phase 8: Revision

Now the revision pass. Do not defend the original prose: if a flag is valid, fix it; if a flag is invalid, cut the flag from the audit rather than arguing for the prose you already wrote.

1. **Name the one thing.** The single most important observation about this draft. Where is it alive and where is it dead? What one fix would improve the whole piece the most? Be specific — point to a passage, a scene, a structural choice. **This governs the rewrite.** The audit below should prioritize the area the one thing identified; the rewrite should direct its strongest work there. Everything else is cleanup around the one thing.

2. **Audit the draft in one pass**, watching for all of the following:

   - **Unslop patterns**: contaminated vocabulary; structural tics (negative parallelism, dramatic countdowns, self-answered rhetorical questions, list-of-three defaults, anaphora abuse, superficial trailing analyses, false ranges, filler transitions); eyeball-kick saturation; compulsive personification; fractal summaries; signposted conclusions; performed profundity; tonal monotony; em-dash overuse. Honor the genre permissions section of the Phase 1 style guide: if a passage uses a move the permissions section explicitly licenses, do not flag it under the Unslop pattern the move resembles. The permissions are narrow and justified; Unslop concerns about other patterns still apply. Permissions don't excuse weak execution — they license the move, not the result. A passage may still fail under a permission if the execution is loose.
   - **Genre-voice slippage** against the Phase 1 style guide, including its failure-mode and genre-permissions sections. Where does the voice sound like generic literary AI instead of [GENRE]'s specific tradition? Where are the genre's permitted moves underused — places the writer could have leaned into a permission and instead wrote the safer realist version?
   - **Legibility failures** where compression has crossed into fragmentation — missing articles or connectives, orphaned pronouns, scenes without anchoring detail, elided actions the reader is expected to infer from context the text doesn't provide. (See the Legibility Floor note in Setup.)
   - **Regression to default** at moments that were surprising in the Phase 7 draft and got sanded flat, or places where the prose slid toward the mean.

   For each flag, quote the passage and state which lens caught it. Don't flag the same passage under multiple lenses — pick the lens that best explains the problem.

3. **Length check.** Confirm the draft is within [LENGTH]. If under, identify where the story needs more room — scene, detail, or dialogue that earns its space. If over, identify what to cut. If within range, say so and move on.

4. **Rewrite the story in full**, informed by the audit above. Lead with the area the one thing identified.

5. **Changelog.** For the 5–7 most substantive edits, quote the original passage and its replacement side by side so the fix is auditable at a glance. For minor edits (single-word swaps, em-dashes removed, small rewordings), list them briefly by location without quoting. If any audit flag was cut as invalid rather than fixed, note it and say why.

---

## Phase 9: Export

Create a file called `story.md` with the following structure:

1. An H1 with the story's title.
2. An H2 titled "Abstract" followed by a neutral abstract of the story in 80–150 words. This is a descriptive summary, not marketing copy: what the story is about, who the main characters are, what happens, what kind of ending it reaches. Present-tense, third-person, no evaluative language, no rhetorical flourishes. Do not withhold the ending for effect — this is an abstract, not a blurb. The Unslop style guide applies here as strictly as it does in the story itself; abstracts are a concentrated site of AI-patterned prose.
3. An H2 titled "Story" followed by the full text of the revised story from Phase 8.

No changelog, no commentary, no metadata beyond the title. Just the title, the abstract, and the story.

---

## Notes

**The "one thing stand out / one thing worries you" phrasing.** This runs through Phases 3–7 as a forcing function. Top-three praise without a worry clause collapses into vibes. Requiring the writer to name a specific concern about each finalist produces better final selections because the final-pick rationale has to balance named strengths against named weaknesses rather than choosing on overall impression.

**Diversity across candidates.** Phases 4, 5, and 6 all include explicit diversity axes. Models produce clustered candidates by default; without explicit axes and a "break the cluster" instruction, "generate 20 diverse plots" reliably returns 20 variations of the same plot. The axes are load-bearing, not decoration.

**Legibility over compression.** See the Legibility Floor in Setup. Compression past the point of comprehension is one of the most common failure modes at short story lengths and is specifically checked in the Phase 8 audit.

**Pushing back on the literary-realist tilt.** Three mechanisms work together to give the speculative element room to operate: (1) Phase 1's genre-permissions section names moves the genre uses that the Unslop guide would otherwise flag, with justification, and Phase 8's audit honors those permissions; (2) Phase 4's frame-commitment axis varies how speculative a plot is, from realist to irreducibly speculative, with a soft floor of three speculative-end candidates per twenty plots; (3) Phase 7's frame-risk requirement forces at least one of the five drafts to commit to a non-realist frame. None of these mechanisms forces a speculative outcome — the chosen draft can still be the realist one — but together they ensure speculative options reach the comparison stage rather than being filtered out at every phase. If runs are still coming out as domestic realism with AI furniture despite these mechanisms, the next intervention point is examining the Unslop style guide's worked examples (which currently anchor the "particular over universal" rule with a domestic example only).

**Steering between phases.** You don't have to accept the model's pick at each phase. You can say "I prefer #7, use that instead" or "blend #3 and #11" or "these are all wrong, here's what I want." Your taste is the final authority; the model is generating options, not deciding outcomes.

**Substituting genres.** Replace [GENRE] in Phases 1, 3, 7, and 8. The style guide in Phase 1 will adapt to the new genre, and all downstream phases inherit from it. The Unslop style guide remains constant regardless of genre. For microgenres and small scenes, the model may not have enough training signal to produce a reliable Phase 1 guide; Phase 1 is instructed to say so and request reference material rather than generate plausible-sounding content that misses the mode.

**The SEED and load-bearing use.** Phase 3 generates conflicts from a SEED produced in Phase 2 — a small set of concrete concepts derived either from a user-supplied prompt (≤280 Unicode characters) or from a dictionary draw inflated via web searches. The "load-bearing" constraint is the central design choice: every conflict must use at least two SEED items as constitutive parts of the premise rather than as decoration. If removing both items leaves the conflict intact, the SEED wasn't doing work. This is the same standard the earlier version of the template used for "Track B" conflicts, and it generalizes cleanly — specificity comes from concepts the story can't afford to lose.

**Regenerating conflicts.** Phases 2 and 3 are split so conflicts can be regenerated without rerolling the SEED. If Phase 3's 30 conflicts don't yield a compelling winner, run Phase 3 again; the SEED from Phase 2 persists.

**Thin SEEDs.** Some runs will produce SEEDs with only 3 or 4 surviving items because several dictionary words will fail to inflate into anything specific. This is a feature, not a bug. Thin SEEDs force each surviving item to do more work and constrain the conflict space more tightly. Do not reroll for a thicker SEED — run with what the draw produced.

**User-supplied SEEDs.** A tweet-length SEED ≤280 characters gives the user direct steering over the story's concepts. Phase 2 verifies the length and proceeds without the dictionary draw. The load-bearing constraint still applies: conflicts should use the SEED's specific ideas, not just its general territory.

**Context management.** Each phase builds on the previous winner, not the full generation set. Phase 7 is the heaviest context phase (5 full stories of [LENGTH]). If context pressure causes quality to degrade, start a new conversation within the same Project, paste a summary of decisions so far plus the winning outline, and run Phase 7 fresh. The project knowledge (style guides, template) persists across conversations. A smaller intervention: if late-set regression shows up within Phase 7 itself (versions 4 and 5 phoned in), ask the model to write the five in two batches of three and two, with a review between them.

**When a run goes wrong.** If a phase produces output you dislike and steering doesn't fix it, start a new run rather than trying to recover mid-pipeline. The funnel creates path dependency: a weak conflict in Phase 3 contaminates everything downstream. A fresh start costs less than trying to rehabilitate a compromised run.

**Revision iteration.** Phase 8 can be repeated. Two revision passes is usually enough. More than three suggests a structural problem — go back to Phase 5 or 6 and regenerate downstream from a different structural choice.

**Model selection.** Use the strongest model available for all phases. Creative generation at this complexity degrades noticeably with weaker models, and the revision phase's sentence-by-sentence audit scales with model quality.
