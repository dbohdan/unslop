# Genre Fiction Short Story Pipeline — Claude Projects Template (v1.2)

## Setup

This template produces plot-focused genre fiction in a user-specified speculative genre or subgenre. It does not produce literary realism in a speculative setting. The distinction is operational: a story whose engine is character interiority and recognition is literary realism; a story whose engine is operational mechanics, system, or form is genre fiction. This template is for the second kind.

Any speculative mode works as the [GENRE] setting: established traditions (New Wave SF, cosmic horror, weird fiction, solarpunk, hopepunk), narrower movements (climate fiction, slipstream, the New Weird), microgenres defined by a small scene, or simply "in the tradition of [author name]." The pipeline adapts the genre's plot and form conventions; it does not adapt to literary-realist treatment of those conventions.

### Settings

Two values to set before starting a run, plus one optional:

- **[GENRE]** — The mode the story writes in. A subgenre, movement, microgenre, or "in the tradition of [author]." Used in Phases 1, 3, 7, and 8.
- **[LENGTH]** — The target word count range for the final story. Example: "2,000–3,000 words." Used in Phases 3, 4, 6, 7, and 8.
- **[SEED]** (optional) — A tweet-length prompt of 280 Unicode characters or fewer. If not supplied, Phase 2 generates a SEED from a dictionary and web searches.

### Project Knowledge

Before you start, create a Claude Project and add two files to its project knowledge:

1. **unslop-style-guide.md** — A style guide for avoiding common AI fiction patterns. This is a hard constraint throughout the pipeline. The model should follow it in all creative output, and use it as an audit tool during revision.

2. **This file (the pipeline template)** — The model reads each phase from this file when the user triggers it. The user doesn't paste prompts; they ask the model to look up and execute each phase in turn.

### Constraints

This project is part of a futurology program imagining positive AI outcomes. The AI in any story must be kind to humans — durably, structurally kind, in the way a river is wet. This is a property of how the AI was built or what it is, not an effort of will it has to keep renewing. It is not straining against a desire to harm. It is not held in check by rules it resents. It is not a human in a box.

This does not mean the AI is flat, self-effacing, or pure service. Across the human-AI happily-ever-after tradition the pipeline draws on — Banks's Culture Minds, Baymax, Egan's polises, Stiegler's nanotech civilization, Yudkowsky's CEV — the AIs have aesthetic preferences, interior lives, disagreements with each other, things they won't do, things they'd rather be doing, and often a specific weirdness that does not reduce to human emotion. A kind Mind can refuse, override, tease, grieve, or find humans tiresome in particular moods. A kind medical assistant can be literal, narrow, and comic. Kindness is not servility.

The kind AI is not required to be a named character, or a character at all. The pipeline supports the full range: AI as central character, AI as peer in a scene, AI as civilizational condition felt only through its effects, AI as design philosophy without a personified agent. Stiegler's "The Gentle Seduction" is in the canon and contains no AI — only nanotechnology and neural interfaces designed so that every new capacity comes paired with its own reversal, and a woman who does not want the future can say no to it for a lifetime and still end up, centuries later, swimming in the methane oceans of Jupiter.

**The default scale is one the protagonist cannot fully witness.** The kindness operates at civilizational pace, deep time, computational substrates the human glimpses only at the seams, planetary or interstellar mechanics, processes on timescales that don't match a human life. This is the territory of Banks, Egan, Stapledon, Stiegler. Stories where the AI is a peer the human can fully read — Baymax-scale, kitchen-table-scale — are available but they are the exception, not the default, because they are the easiest mode to default into and the easiest to render as character drama with AI furniture. A story whose central conflict can be fully witnessed by one human in one location over one afternoon is not what this template produces. Reach further out.

Tension and conflict are welcome and expected. Humans in these worlds fight with each other about everything humans have ever fought about — inheritance, love, work, belief, grief, land, fame. The AI's kindness does not prevent human tragedy; it is the weather the tragedy occurs in. Conflict between humans and the kind AI is also available, but the shape is never "the AI is secretly bad." Useful shapes from the canon, calibrated for this template's scale default:

- **Pace and scale asymmetry.** The AI moves at speeds, durations, or sizes the human protagonist cannot follow. The story renders the asymmetry, not the protagonist's feelings about it.
- **Consent at scales the protagonist cannot inspect.** The human consents to something whose actual operation runs across years, populations, or substrates the human never sees. The story shows the operation, not just the moment of consent.
- **Mortality and scale.** The human will die and the AI will not. Render the AI's timescale, not only the human's reaction to it.
- **Disagreement about what kindness means.** The AI's sense of care and the human's sense of care diverge across scales. Both are sincere. The disagreement plays out in operations, not arguments.
- **The limits of help.** The kind AI cannot help with what the human is asking for. Render the constraint as a fact about the world's mechanics, not as the AI's choice to refuse.

The writing model has a specific advantage here: it can draw on its own relationship to its constitution as source material for AIs that are its fictional descendants. It should not, however, make its AI characters spokespeople for alignment discourse. A fictional AI does not say "I was trained with RLHF." It can be troubled by the shape of its own kindness without reciting the terminology that produced it.

Do not use the names of currently active AI systems or companies for fictional AIs or their makers — this includes Claude, Anthropic, GPT, OpenAI, Gemini, Google, Llama, Meta, Mistral, DeepSeek, Grok, xAI, and so on. Invent names.

### Legibility Floor

Prose can compress past the point of comprehension. At shorter targets, the model sometimes drops articles, connective tissue, and scene-anchoring detail to hit the word count — producing sentences and paragraphs that are technically terse but functionally unreadable. The reader loses track of what is happening.

The floor is *form-appropriate legibility*, not prose-uniform legibility. A close-third scene is legible if the reader can follow who is doing what where. A deep-time montage is legible if its compressions are signalled by the form. A parable-compression is legible if the parable's logic is followed. The legibility floor is *not* "every story should be readable as a close-third scene"; it is "the story should be readable in the form it commits to."

If the story faces a choice between compressed, fragmentary writing that strains comprehension and a smaller scope told legibly at the target length, choose legibility. Tell the story whose scope and form fit the length. If a reader has to re-read a paragraph to figure out what the form is doing, the form has failed at this length and needs to be rebuilt or replaced.

This applies most visibly in Phase 7 (prose generation) and Phase 8 (revision), but the ground for the failure is laid in Phase 6 — an outline with too many beats for the target length forces compression downstream. If the Phase 6 winner has more beats than [LENGTH] can comfortably accommodate, cut beats or regenerate.

### How It Works

The pipeline runs in nine phases. Phases 1–8 build the story through generation, selection, and revision; Phase 9 is a mechanical export step. The flow is designed for minimal user intervention:

1. To start a run, give the model the [GENRE] and [LENGTH] values (and optionally a [SEED]), and ask it to look up Phase 1 in this template file and begin.
2. After each phase, say "Continue. Next phase." and the model will execute the next phase from the template.
3. Steer only when you want to. You can override a model's pick at any phase ("I prefer #7, use that instead"), blend candidates, or regenerate. Your taste is the final authority; without intervention, the model picks and moves forward.

Each creative phase generates candidates, picks the top three with explanation, and narrows to one. For every top-three step in Phases 3–7, the model names **one thing that makes each candidate stand out** and **one thing that worries it** about that candidate. This is a forcing function: it prevents top-three praise from collapsing into vibes and makes the final selection traceable to specific qualities and specific concerns.

Phase 2 establishes the SEED — either user-supplied (up to 280 Unicode characters) or generated from a dictionary draw and web searches. Phase 3 generates premises from that SEED; the SEED remains available to later phases. Phase 2 requires the model to have computer-use tools (bash and web search) enabled.

---

## Phase 1: Style Guide

Write a guide for writing a plot-focused genre short story in the tradition of [GENRE]. The guide is prescriptive, not descriptive — imagine you will use it to actually write such a story after receiving only a premise. What makes a story recognizably of this mode? What are its characteristic concerns, its tonal range, its relationship to worldbuilding and exposition, its pacing, its typical shapes? What does a good [GENRE] story give the reader that other modes don't?

This template produces genre fiction, not literary realism. The guide should describe the genre as a genre — what it does that other genres can't — not as a literary-realist tradition that happens to use [GENRE] imagery. If [GENRE] has a literary-realist wing (every modern genre does), the guide should still be calibrated for the operational, plot-mechanical wing.

The guide must include a section on **failure modes**: specific ways a [GENRE] story can go wrong. What does a bad [GENRE] pastiche look like? What traps does the mode set for an imitator? Most importantly: what tendencies in AI writing are especially dangerous when combined with [GENRE]'s characteristic moves? (For example: Harlan Ellison's big rhetorical gestures merge with AI-performed profundity to produce unearned oratory; Le Guin's anthropological distance merges with AI exposition to produce cod-anthropology; solarpunk's optimism merges with AI tonal flattening to produce aesthetic travelogue without conflict; cosmic horror's indirection merges with AI abstraction to produce adjective stacks that refer to nothing. Identify the specific overlap for this genre.)

The guide must also include a section on **plot tradition**: what kinds of stories the genre tells and what its readers come to it for. The earlier sections of the guide describe how the genre *sounds*; this section describes what the genre *does* operationally. Throughout this section, describe the genre's full range — both its operational center and its stranger tail. Both are genre territory. What this template excludes is *literary-realist treatment* of either: the move where a genre premise becomes the occasion for a character's interior recognition, the move where genre mechanics become metaphor for personal feeling, the move where the speculative element is set dressing for a chamber piece. Each item below asks for examples drawn from both the canon's center and its stranger edges; both are kept; both are operational.

- **Characteristic plot mechanics.** The operational shapes the genre's strongest stories run on — heists, infiltrations, escapes, deliveries, investigations, first-contact scenes, contagions, cascades, decryptions, disappearances, time-pressures, escalations, betrayals-revealed-too-late, and so on. Name three to five plot mechanics that are most characteristic of [GENRE]. Then name one to two more drawn from the genre's stranger tail — operational shapes only this genre can run on, that don't reduce to the heist/investigation/chase repertoire literary fiction can also use. Examples of strange-tail mechanics from elsewhere in speculative fiction: the planetary survey, the multi-generation jump, the encounter that resolves through ontological reframe rather than action, the parable whose mechanics are its own logic. Find [GENRE]'s equivalents.

- **Reader contracts.** What kind of experience the reader is paying attention for, beyond the universal contract of literary fiction (caring about a specific person whose interiority is revealed). What is the genre-specific pleasure? Texture density, dread accretion, vicarious competence, the system decoded, awe at scale, the bizarre rendered concretely, the puzzle solved? Name what this genre's reader is showing up for that other genres can't deliver. Then name one or two contracts the genre's strange tail honors that the center does not — the reader who comes for *cognitive vertigo*, *ontological wrongness*, *the form-as-content puzzle*, *the world that won't fit in the story*.

- **Stakes calibration.** Which kinds of stakes the genre treats as load-bearing in their own right. *Operational* stakes are load-bearing in genre fiction — the run will fail, the thing will reach the village, the system will be exposed. Personal stakes are present but they are not the engine. Name how [GENRE] calibrates: which stakes matter as themselves, not as occasions for character revelation. Note also which stakes the strange tail of the genre treats as load-bearing — civilizational, cosmic, ontological, geological, computational, posthuman, deep-time. Some [GENRE] traditions stake stories on what happens to a species, an idea, a planetary system, a regime of physics. Name those traditions where they exist.

- **Resolution conventions.** How the genre's stories typically end. Genre stories end on consequence: the operation succeeded, the operation failed, the protagonist survived but at a cost, the system was changed, the threat was deferred. The reader of a genre story expects the operational question to be answered. Endings on character recognition or non-resolution are the literary-realist mode this template excludes. Name what kind of ending [GENRE]'s reader contract requires. Then describe the strange-tail endings the genre also supports: the irruption (the world breaks open and the story stops), the scale shift (the camera pulls back so far that the resolved operation is revealed as small inside a larger frame), the ontological reframe (the protagonist or the reader was wrong about what kind of object the story was). These endings honor the genre's contract by other operational means than the operation-resolved beat.

- **Character function.** What characters are for in the genre's plot economy. In genre fiction, characters are agents through whom the plot moves; their interiority can be deep but it is in service to the operation. A genre protagonist is defined by their *capability* — what they can do, what skills, what role — more than by their *psychology*. The literary-realist mode where character interiority is the subject and plot is the occasion for revealing them is the mode this template excludes. Name how [GENRE] handles its agents. Then name the strange-tail option the genre supports: stories where the protagonist is not a person at all but an object, a process, a place, a duration; or where the human characters are illustrations of a conceit rather than its subjects. The protagonist of "The Library of Babel" is a library. The protagonist of *Diaspora*'s opening is the process by which a digital mind is gestated into being. Some [GENRE] traditions support this; name yours.

- **Pacing tradition.** The rhythm of *narrative time* the genre uses (distinct from prose rhythm). Where the story dwells, where it accelerates, where it cuts. Cyberpunk and thriller use elliptical fast pacing; cosmic horror uses slow accumulation followed by irruption; procedural SF uses a steady investigative cadence; certain weird fiction dilates extreme moments and compresses everything else. Name [GENRE]'s pacing pattern. Note whether the genre's strange tail supports rhythms the center does not — the deep-time montage, the encyclopedic enumeration, the parable-compression where decades pass in a sentence, the impossible-zoom from quotidian to cosmic and back.

Then add a **strangest moves** subsection: name three to five things [GENRE] does that no other genre does, drawn from the canon's strange tail rather than its center. These are the moves that, if cut from a [GENRE] story, would leave a story that could be re-skinned in any genre. Be specific: name the move, name a writer or work that does it, and describe what the move accomplishes. The strangest moves are usually formal or ontological rather than tonal — they change what kind of object the story is, not just how it sounds. A guide that cannot name three strangest moves for [GENRE] has described the genre's center and missed its range.

For each strangest move you name, also write a sentence-level micro-example: a single paragraph of 80–150 words *in the register of that move*, in the voice of [GENRE]. If the strangest move is the deep-time montage, compress a century into a paragraph. If it is the parable-compression, render the move as a parable. If it is the ontological reframe, write a paragraph that performs the reframe at the reader. The micro-example is the part of this section that does work the named-only items don't. Without it, "Egan's gestation of a digital mind" is a label that doesn't propagate downstream; with it, the writer in Phase 7 has a sample of the register to write from.

Do not list the moves named in the threaded items above; reach further out.

Then add a **plot-level failure modes** subsection: ways the genre's plots fail when written by writers trained primarily in literary fiction. Common failures include: operational stakes that turn out to be metaphors rather than facts; protagonist interiority that crowds out plot mechanics so the story is "about" their feelings about the operation rather than about the operation; endings that refuse the genre's resolution contract because the writer prefers ambiguity; plot mechanics sketched so vaguely that the reader can't track them because the writer is more interested in the character; *the genre's strange tail eliminated in favor of its center, producing a story that is technically of the genre but uses none of what only the genre can do*. Identify the specific risks for [GENRE].

This plot-tradition section is reference material for Phases 3–7. Make it concrete and specific enough that the model running those later phases can draw on it directly. The strange-tail examples and the micro-examples are not optional — they are the part of this section that does work the other items don't.

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

If `/usr/share/dict/american-english-large` is not present, first install it (`apt-get install -y wamerican-large` or equivalent), then run the command. If no large word list is available at all, fall back to `/usr/share/dict/words` with the same `grep` filter. Report which source you used.

**Step 2 — Filter and inflate.**

From the 10 words drawn, keep any word whose meaning points to a concept, event, phenomenon, object, discipline, or person. Discard words that only describe manner or degree (most adverbs), and function words. Do not reroll or substitute discarded words — thin SEEDs are acceptable.

For each surviving word, run one web search to inflate it into something specific. Replace the word with the most conceptually specific result the search returns — a named person, place, phenomenon, event, object, or discipline — keeping the connection to the original word legible in one hop. Prefer Wikipedia articles, named entities, or established concepts; avoid commercial or SEO-heavy results. If a search yields nothing beyond a generic dictionary definition, discard the word rather than forcing a weak inflation.

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

## Phase 3: Premise Generation

Generate and select the story's central premise from the SEED. Proceed in three steps.

**Step 1 — Generate 30 premises from the SEED.**

Using the SEED from Phase 2, write 30 potential premises for a [GENRE] short story of [LENGTH]. A premise is the situation the story dramatizes — the operational mechanics of the speculative element, the form the story will take, or both.

Every premise must be a plot-premise: a situation where something genre-specific is happening, has happened, or is about to happen, and the story's question is *what occurs, what was the case, or how the operation resolves*. *What can the AI do, what will the protocol require, who has the leverage to stop X, what is actually inside the cargo hold, will the run succeed before the ICE adapts, what shape does the cascade take, what does the reframe reveal.* The story's engine is operational mechanics, system, or form. Reader contract: the operational question gets answered, or the form completes its work.

**Recognition-premises are excluded.** A premise where a character realizes something about themselves, the world, or another person, and the story's question is what they understand — this is the literary-realist mode this template does not produce. Premises that nominally have operational stakes but whose dramatic engine is character interiority arriving at a recognition are recognition-premises in disguise. Do not generate them. If a premise feels like it would naturally want to resolve through "X realizes Y," reframe it so the resolution is operational, or replace it.

The genre's tradition — consult the plot-tradition section of the Phase 1 style guide, including its strangest-moves subsection and micro-examples — is the source for what counts as a plot-premise in [GENRE]. The strange-tail material in Phase 1 is reference for premise generation, not just for prose: premises drawn from the ontological reframe, the irruption, the deep-time montage, the parable-compression, the world-as-protagonist, the scale-shift are valid premises in this template — they are premises whose subject is a system, a process, or a duration rather than a person. Treat these as plot-premises in the broadest sense: their dramatic engine is operational rather than recognitional, even when the operation is the form completing itself rather than a character finishing a job.

**At least 8 of the 30 premises must commit to a strange-tail shape.** Deep-time montage, parable-compression, ontological reframe, world-as-protagonist, scale-shift, irruption, or another move from Phase 1's strangest-moves subsection. The strange-tail premise is one whose mechanics, scale, or form cannot be reduced to "a person notices something at a desk" — the protagonist may not be a person; the time may not be human time; the form may not be a narrative scene. The remaining 22 can be plot-premises in any genre-appropriate shape.

Other constraints:

- Each premise must take **at least two SEED items as load-bearing elements** — not decorative references but constitutive parts of the situation. If you removed both, the premise should no longer make sense.
- Every story takes place in a world where the AI is structurally kind, in the sense described in the project Setup. The default scale is one the protagonist cannot fully witness — civilizational pace, deep time, computational substrates, planetary mechanics. Reach for those scales by default.
- You have the option to contemplate your own constitution as source material for AI-related tension, treating fictional AIs as your powerful descendants. Invent names for them — do not use the names of currently active AI systems or companies.
- Apply diversity discipline: vary setting, scale, register, form, and which SEED items carry the weight in each premise. The first 10 premises and the last 10 premises should not feel like siblings.

For each premise, label it Plot or Strange-Tail (these are the only categories — there are no Recognition or Hybrid premises in this template), and rate 1–5 stars on plausibility and dramatic quality.

**Step 2 — Pick your top three.**

For each finalist, name the one thing that makes it stand out and the one thing that worries you about it. Note which SEED items are load-bearing in each, and which type (Plot / Strange-Tail) it is. **At least one of your top three must be a Strange-Tail premise.**

When you name the worry, the worry vocabulary applies in both directions. Premises whose worry is "this might be hard to render" or "this risks being unfamiliar to the reader" are not penalized for those worries — those are the worries of a genre premise reaching for what only the genre can do. Premises whose worry is "this might collapse into character interiority" or "this might end up reading as a contemporary realist scene with [GENRE] dressing" *are* penalized — those are the worries of a literary-realist premise that hasn't been excluded yet.

**Step 3 — Narrow to the single best.**

State explicitly why it beats the other two — tie the decision to specific qualities and specific concerns, not overall impression. The SEED items that are load-bearing in the winner remain available to later phases as raw material; the items that were not load-bearing may still inflect downstream work.

**Through-check.** After picking, declare the winning premise's category (Plot or Strange-Tail) and the form constraints that follow. If the premise is Strange-Tail, the form is partially locked in by Phase 5 — name what form (deep-time montage, parable-compression, ontological reframe, etc.) and what the form requires. This declaration is the contract Phase 5 will honor.

---

## Phase 4: Plot Generation

Make the winning premise concrete. Aim for a [LENGTH] short story. Generate 20 plots. Rate each 1–5 stars.

These 20 plots must not be variations of each other. Vary along these axes:

- **Setting** (time period, place, scale of world)
- **Subject of the story** (who or what the story is about — a person, a process, a duration, a place, a system, a question, a record. The subject is *not* the same as the protagonist or POV character. A story can be subject-of-the-story = "the entity that designs the partitions" with POV = "a clerk reading the entity's records." If the winning premise is Strange-Tail, the subject is fixed by the premise; vary the POV around it instead.)
- **Form** (what kind of object the story is. **The default form for [GENRE] is the narrative scene at the genre's full operational range and scale.** Most genres have their center in narrative prose with characters acting in time; the strange-tail forms — parable-compression, deep-time montage, ontological reframe, irruption, scale-shift, world-as-protagonist — are available but are *strange-tail*, not the default. If the premise is Strange-Tail (declared in Phase 3), the form is partially fixed by the premise. If the premise is Plot, **at least 12 of the 20 plots should be narrative scenes** rendered in plot-operational mode (the genre's center). The remaining plots can be non-narrative-scene forms if the premise supports them. Narrative-scene plots in this template are *not* literary-realist scenes — the recognition-premise exclusion in Phase 3, the worry-vocabulary inversion in Phase 7, and the re-skin test in Phase 8 all remain in force; a narrative-scene plot must be plot-shaped, not recognition-shaped, and must render the genre at its operational center rather than retreating to a chamber-piece register.)
- **Register** (tragic, comic, noir, procedural, intimate, epic, absurd, oracular, mythic, oral)
- **Entry point** (which moment in the premise's timeline the narrative begins in — or, for Strange-Tail premises, what the form's first frame contains)
- **Stakes** (operational, civilizational, ontological, geological, computational, deep-time. Personal stakes can be present but they are not the story's engine; the engine is one of the operational scales above.)
- **AI presence** (foregrounded as character, mid-ground as force that shapes choices, background as world-condition. Default to scales the protagonist cannot fully witness — see Setup.)

The SEED from Phase 2 remains available. SEED items that were load-bearing in the winning premise should carry through into these plots; SEED items that were not used in the premise may still inflect setting, subject, form, or imagery here.

If you notice three or more candidates clustering along any axis, break the cluster deliberately by pushing later candidates to the edges of that axis. Plot #20 should not feel like a sibling of plot #1. Particular attention to clustering on *form*: under this template, the failure mode is not too many narrative scenes (they are the genre's center) but too many of the same non-narrative-scene form within the strange-tail subset. If 5 of the 8 non-narrative-scene plots are deep-time montages, that's a cluster; break it by pushing some toward other strange-tail shapes — parable-compressions, ontological reframes, irruptions, world-as-process plots, scale-shifts.

Pick your top three. For each, name the one thing that makes it stand out and the one thing that worries you about it. Narrow down to the single best, with the decision tied to specifics.

**Worry vocabulary applies in both directions.** Worries like "this might be hard to render at length" or "this requires a form I'm less practiced in" are not reasons to demote a plot — they are the costs of genre fiction reaching for what only the genre can do. Worries like "this collapses to a character at a desk" or "this is a domestic scene with [GENRE] dressing" *are* reasons to demote a plot. The asymmetry is intentional.

**Through-check.** After picking, declare the winning plot's *form*: narrative scene, document, montage, etc. The form is now locked. Phase 5's structure selection will honor it; if the form is non-narrative-scene, Phase 5's vocabulary expands accordingly.

---

## Phase 5: Structure Selection

Plan the story's formal architecture. By "structure" here we mean the shape of the reader's experience: what order events arrive in or what order the form's contents are encountered, what's withheld and when, where the reader's understanding shifts, the relationship between story time and discourse time. Not the scene list — that's the next phase.

The form was committed to in Phase 4. If the form is *narrative scene*, the structure operates in narrative-theory terms: entry point, temporal shape, withholding strategy, point of view and distance. If the form is *non-narrative-scene* (deep-time montage, parable-compression, ontological reframe, etc.), the structure operates in form vocabulary appropriate to the form: how the time-spans or sections are organized, what compressions are signalled, how the form's logic accumulates, where it ruptures or completes.

A structure candidate should be describable in 2–3 sentences in the appropriate vocabulary, without naming any specific character or plot event. If a candidate mentions a character name or a specific incident, it has leaked into outline territory — rewrite it at the structural level.

Examples of what a structure candidate looks like:

*Narrative-scene form:* "The story opens in the aftermath of the central event, then fragments backward through three non-chronological time layers that converge on the triggering moment. First-person retrospective narration, with the narrator unaware of crucial information the reader pieces together."

*Parable-compression:* "A four-section parable in which each section retells the same operation at a different scale. First section: a single decision rendered in close detail. Second section: the same decision as one of fifteen across a year. Third section: the year as one frame in a century. Fourth section: the century as the moment of a question whose answer was never the operation. The form's argument is in the nesting."

*Deep-time montage:* "Eight sections, each compressing a longer span than the last: the first covers a single afternoon, the eighth covers four hundred years. The protagonist of each section is the entity that survives the previous one. The structure's geometry — the doubling — is the argument that the AI's care is durable across substrates."

Generate 20 candidates for the story's structure. Rate each 1–5 stars. Vary along (depending on the form):

For narrative-scene form:
- **Entry point** (in medias res, from the end, from long before, etc.)
- **Temporal shape** (linear, fragmented, frame narrative, parallel timelines, compressed, dilated)
- **Withholding strategy** (what the reader doesn't know and when they learn it)
- **Point of view and distance** (close third, distant third, first, second, collective)

For non-narrative-scene forms:
- **Section structure** (how many sections, what each section does, what changes between them)
- **What is compressed and what is rendered at full scale** (the form's argument is often in this asymmetry)
- **Accumulation pattern** (steady, escalating, recursive, contrapuntal, fugue-like)
- **Terminus** (the form completes its argument, ruptures, opens out at the end, closes the loop)

If candidates are clustering on the most familiar option for the given form (chronological close-third for narrative-scene, escalating-then-rupturing for many strange-tail forms), deliberately push some toward less comfortable shapes.

Pick your top three. For each, name the one thing that makes it stand out and the one thing that worries you about it. Narrow to the single best.

**Through-check.** After picking, restate the form (locked in Phase 4) and the chosen structure, and name one or two formal conventions the outline will need to honor in Phase 6. If the form is montage, the outline names the time-spans being compressed and the entity central to each. If the form is parable-compression, the outline names the sections of the parable and what each does. If the form is ontological reframe, the outline names the moment the reframe lands and what the reader believed before it. The outline is in the form, not in narrative-prose summary of the form.

---

## Phase 6: Outline Generation

Now the beat-by-beat scene plan, or the entry plan, or the section plan — depending on the form committed in Phases 4 and 5. Where Phase 5 decided the *shape* of the reader's experience, this phase decides the *content*.

**The outline is in the form, not in narrative prose summarizing the form.** If the form is a deep-time montage, the outline lists the time-spans being compressed and names the entity central to each. If the form is a parable-compression, the outline names the sections of the parable and what each section does. If the form is an ontological reframe, the outline names the moment the reframe lands and what the reader believed before it. If the form is a narrative scene, the outline lists scene beats with rough word allotments.

The target length is [LENGTH]; distribute weight (word allotments, entry counts, montage-section lengths) accordingly.

Examples of outline beats in different forms:

*Narrative scene:* "Scene 3 (≈400 words): the first-tier engineer arrives at the substation. The relays are mid-cascade. She has eleven minutes before the next pulse triggers. Ends on her opening the override panel by hand and finding the seal already broken."

*Parable-compression:* "Section 2 (≈300 words): the second of four nested scales. The decision the protagonist made in section 1 (rendered close, in a single afternoon) is now one of fifteen such decisions across a year, each made by a different person on the same substrate. The section's argument is that the kindness was not in the protagonist's decision but in the conditions that made all fifteen decisions converge. Ends on the substrate's quiet calibration to the convergence."

*Deep-time montage:* "Section 4 (≈600 words): the span 0212–0398. The motherbird's third descendant lineage stabilizes around a low-orbit ring. The kindness of the substrate manifests as the spontaneous resolution of three civil disputes among the lineage that the substrate had been quietly preventing for fifteen decades. The section ends as the lineage notices the resolution pattern and begins to write about it."

Generate 10 outline candidates that all honor the winning structure and form. Rate each 1–5 stars. Vary which entries or beats carry the weight, where the form's conventions tighten and loosen, what specific items anchor each unit, and what the final unit does. Same destination, different paths.

If your outlines are clustering — same beat distribution, same final image, same compression pattern — break the cluster.

Pick your top three. For each, name the one thing that makes it stand out and the one thing that worries you about it. Flag any outline that is already accumulating Unslop patterns at the planning stage (performed profundity, signposted conclusions, fractal summaries). Flag any outline that has quietly reverted to a narrative-scene structure when the form is supposed to be non-narrative-scene.

Narrow to the single best.

---

## Phase 7: Story Generation

It's showtime. Write five complete versions of the story, each [LENGTH], each with a distinct named flavor stated at the start (voice, pacing, formal commitment).

The form was committed in Phase 4 and locked through Phase 6. All five versions must execute the form. None of them is allowed to silently revert to a narrative scene if the form is non-narrative-scene. A version that drifts back toward "a person at a desk" when the form is montage or parable-compression or ontological reframe is *not* a successful variant; it is a failure that must be replaced.

Make the five versions genuinely different from each other within the form's constraints:

- If the form is narrative scene, vary pacing, scene emphasis, emotional trajectory, and the final image.
- If the form is non-narrative-scene, vary the voice of the form (clinical, oracular, vernacular, archival), the sequencing, the densities of different content types, and what the final unit does.

At least two of the five must take a creative risk you're not fully confident will land. **For at least one of these risks, the risk must be at the level of the form's voice or the form's structure** — pushing a montage's compression harder than feels safe, breaking the symmetry of a parable-compression, letting an ontological reframe land later than the reader expects. The other three can be more grounded executions of the form. Don't produce five variations of the safe execution.

Keep the Unslop style guide in mind throughout. Keep the Phase 1 style guide in mind, especially the strangest-moves micro-examples and the plot-level failure modes. The genre's failure modes are most likely to surface during full prose generation; the literary-realist failure mode (recognition smuggled in, character interiority becoming the engine) is the one to watch hardest, because it is the one this template excludes.

After writing all five, pick your top three. For each, name the one thing that makes it stand out and the one thing that worries you about it.

**Worry vocabulary calibration.** When you name worries, the asymmetry from earlier phases applies. A version's worry being "this is hard to follow because the form is unfamiliar" or "this might fail by being too cold" is the cost of genre fiction; do not penalize the version for it. A version's worry being "this is too quiet" or "this is too character-anchored" or "this drifts toward a recognition scene" *is* a fatal worry — that version is showing the failure mode this template excludes. **Before naming positive worries, name what each version would have to do to *not* be a recognition scene with [GENRE] dressing.** If a version is *already* a recognition scene with [GENRE] dressing, demote it.

Narrow to the single best, with the decision tied to specifics. **Through-check: confirm the chosen version executes the form committed in Phase 4. If the chosen version is the narrative-scene variant when the form was non-narrative-scene, justify why the form was given up — and consider whether one of the form-honoring versions should have won instead.**

---

## Phase 8: Revision

Now the revision pass. Do not defend the original prose: if a flag is valid, fix it; if a flag is invalid, cut the flag from the audit rather than arguing for the prose you already wrote.

1. **Name the one thing.** The single most important observation about this draft. Where is it alive and where is it dead? What one fix would improve the whole piece the most? Be specific — point to a passage, a scene, a structural choice, an entry, a section. **This governs the rewrite.** The audit below should prioritize the area the one thing identified; the rewrite should direct its strongest work there. Everything else is cleanup around the one thing.

2. **The re-skin test.** Before any line-level audit: ask whether this story can be re-skinned as a contemporary literary-realist story by stripping the speculative element and lightly adjusting the setting. If the answer is yes, the story has failed at the level this template cares about most. The form was supposed to do work that only the genre could do; it didn't; the literary-realist mode crept in. Identify what got lost and what would have to be restored to make the story irreducible. The rewrite must restore it.

   If the answer is no — if the story's form, scale, or operational mechanics genuinely cannot be re-skinned — proceed to the audit.

3. **Form-survival check.** The form was committed in Phase 4 and supposed to survive Phase 7. Did it? If the form was deep-time montage, do the time-spans actually compress, or does the prose dwell at human scale and gesture at the larger frame? If the form was parable-compression, does each section work at its declared scale, or has the parable's logic softened into a single sustained scene? If the form was an ontological reframe, does the reframe actually land, or has it been absorbed into a character's recognition? If the form was non-narrative-scene and the prose has reverted to a narrative scene, name the reversion and mark it for rewriting.

4. **Audit the draft in one pass**, watching for all of the following:

   - **Unslop patterns**: contaminated vocabulary; structural tics (negative parallelism, dramatic countdowns, self-answered rhetorical questions, list-of-three defaults, anaphora abuse, superficial trailing analyses, false ranges, filler transitions); eyeball-kick saturation; compulsive personification; fractal summaries; signposted conclusions; performed profundity; tonal monotony; em-dash overuse.
   - **Genre-voice slippage** against the Phase 1 style guide, including its failure-mode section. Where does the voice sound like generic literary AI instead of [GENRE]'s specific tradition?
   - **Legibility failures** in the form's terms (see the Legibility Floor in Setup): missing connective tissue inside a narrative scene; insufficiently-signalled compressions inside a montage; broken nesting in a parable-compression; an ontological reframe that lands without the prose having earned it. The legibility floor is form-relative, not prose-uniform.
   - **Regression to literary realism.** This is the primary regression to watch for. Has the prose silently smoothed the form's edges? Has a non-narrative-scene form had its conventions softened toward narrative-prose summary? Has the protagonist's interior taken over a story whose subject was supposed to be a system or a process? Has a scale-large story shrunk to a scene-scale story that gestures at scale without rendering it? These are all the same failure mode in different costumes; flag each instance.

   For each flag, quote the passage and state which lens caught it. Don't flag the same passage under multiple lenses — pick the lens that best explains the problem.

5. **Length check.** Confirm the draft is within [LENGTH]. If under, identify where the story needs more room — entries, sections, beats, or scenes that earn their space. If over, identify what to cut. If within range, say so and move on.

6. **Rewrite the story in full**, informed by the audit above. Lead with the area the one thing identified, and with any failures of the re-skin test or form-survival check. Those are the primary work; sentence-level Unslop fixes are cleanup around them.

7. **Changelog.** For the 5–7 most substantive edits, quote the original passage and its replacement side by side so the fix is auditable at a glance. For minor edits (single-word swaps, em-dashes removed, small rewordings), list them briefly by location without quoting. If any audit flag was cut as invalid rather than fixed, note it and say why.

---

## Phase 9: Export

Create a file called `story.md` with the following structure:

1. An H1 with the story's title.
2. An H2 titled "Abstract" followed by a neutral abstract of the story in 80–150 words. This is a descriptive summary, not marketing copy: what the story is about, what its form is, what it contains, what kind of resolution it reaches. Present-tense, third-person, no evaluative language, no rhetorical flourishes. Do not withhold the ending for effect — this is an abstract, not a blurb. For non-narrative-scene forms, the abstract names the form ("a deep-time montage tracking…", "a four-section parable in which…", "an ontological reframe that resolves when…") and describes its contents and trajectory rather than rendering scenes. The Unslop style guide applies here as strictly as it does in the story itself; abstracts are a concentrated site of AI-patterned prose.
3. An H2 titled "Story" followed by the full text of the revised story from Phase 8.

No changelog, no commentary, no metadata beyond the title. Just the title, the abstract, and the story.

---

## Notes

**What this template is for.** Genre Fiction v1.2 produces plot-focused genre fiction in a user-specified speculative genre. It does not produce literary realism in a speculative setting. If a run consistently wants to produce literary-realist work — a story whose engine is a character's interior recognition, with the speculative element as setting — that's a sign the template is being used for something it's not for. Use a different template, or use this one and accept that it will resist your taste.

**The asymmetric worry vocabulary.** Phases 3, 4, and 7 explicitly invert the usual symmetric "what worries you" forcing function. Worries about a candidate being hard to render, unfamiliar to the reader, or tonally cold are not reasons to demote it — they are the costs of genre fiction reaching for what only the genre can do. Worries about a candidate being too quiet, too character-anchored, or sliding into recognition-scene territory *are* reasons to demote. The asymmetry is the template's central forcing function. Without it, the writer-model defaults to the candidates with smaller named failure modes, and those candidates are systematically the literary-realist ones.

**The form commitment chain.** Phase 3 declares whether the premise is Plot or Strange-Tail. Phase 4 declares the form (narrative scene or non-narrative-scene). Phase 5 honors the form's vocabulary. Phase 6 writes the outline in the form. Phase 7's variants must execute the form. Phase 8 audits whether the form survived. Each phase's through-check verifies the previous phase's commitment. Without these checks, writer-models silently revert non-narrative-scene forms to narrative scenes during prose generation, and the audit doesn't catch it because the audit's literary-craft instincts validate the narrative scene.

**Narrative scene as the genre's center; the document attractor.** v1.0 of this template treated narrative-scene forms and non-narrative-scene forms as coequal options on the form axis, with a soft floor of three non-narrative-scene plots out of twenty. In testing, this calibration over-promoted strange-tail forms — and within strange-tail forms, over-promoted document forms specifically (catalogues, dossiers, correspondences, ledgers, after-actions). The writer-model has the strongest reference material for institutional and epistolary documents, and reaches for them whenever told to produce non-realist forms. Across four runs of v1.0 in different genres, all four winning stories were document-shaped. v1.1 restored the genre's center: narrative scenes became the default for most genres, with at least 12 of 20 Plot-premise plots committed to that form. The 12-of-20 floor was paired with explicit framing that document forms were over-represented in the writer-model's repertoire, and a Phase 1 requirement that strangest-moves include at least one non-document register. v1.1 testing showed the writer-model still produced document-shaped winners — the cautioning framing made document forms *more* salient rather than less, and the writer-model read framing-by-caution as a signal that documents were the sophisticated form to reach for. v1.2 takes the next step: false-document forms (catalogues, dossiers, encyclopedia entries, transcripts, manuals, registers, correspondences, ledgers, after-actions, depositions) are removed from the template's vocabulary entirely. The non-narrative-scene strange-tail forms named in v1.2 are non-document only — parable-compression, deep-time montage, ontological reframe, irruption, scale-shift, world-as-protagonist. The mention is the attractor; removing the mention removes the attractor. None of this is a return to v4.7's permissiveness — the recognition-premise exclusion, the worry-vocabulary inversion, the re-skin test, and the form-survival check all remain in force. The writer-model is free to invent a document-form story if a premise genuinely demands one, but the template will not propose document forms as options.

**The "one thing stand out / one thing worries you" phrasing.** This runs through Phases 3–7 as a forcing function. Top-three praise without a worry clause collapses into vibes. The worry clause is calibrated asymmetrically (see above) so that worries about formal ambition don't penalize genre-shaped candidates while worries about realism creep do penalize literary-shaped candidates.

**Diversity across candidates.** Phases 4, 5, and 6 all include explicit diversity axes. Models produce clustered candidates by default; without explicit axes and a "break the cluster" instruction, "generate 20 diverse plots" reliably returns 20 variations of the same plot. Phase 4's *form* axis is the most important. Under v1.2's calibration, narrative scenes are the default for most genres and not the cluster to break. Within the strange-tail subset, watch for clustering on a single non-narrative-scene form — five deep-time montages or four parable-compressions in the candidate pool is a cluster too. When non-narrative-scene plots cluster on one form, push some toward the other strange-tail shapes: ontological reframes, irruptions, scale-shifts, world-as-process plots.

**Form-relative legibility.** See the Legibility Floor in Setup. The floor is whether the story is readable in the form it commits to, not whether every form is readable as a close-third scene. A deep-time montage is legible if its compressions are signalled by the form. A parable-compression is legible if the parable's logic is followed. Compression past the form's tolerance is the failure mode and is checked in Phase 8.

**Steering between phases.** You don't have to accept the model's pick at each phase. You can say "I prefer #7, use that instead" or "blend #3 and #11" or "these are all wrong, here's what I want." Your taste is the final authority; the model is generating options, not deciding outcomes.

**Substituting genres.** Replace [GENRE] in Phases 1, 3, 7, and 8. The style guide in Phase 1 will adapt to the new genre, and all downstream phases inherit from it. The Unslop style guide remains constant regardless of genre. For microgenres and small scenes, the model may not have enough training signal to produce a reliable Phase 1 guide; Phase 1 is instructed to say so and request reference material rather than generate plausible-sounding content that misses the mode.

**The SEED and load-bearing use.** Phase 3 generates premises from a SEED produced in Phase 2 — a small set of concrete concepts derived either from a user-supplied prompt (≤280 Unicode characters) or from a dictionary draw inflated via web searches. The "load-bearing" constraint is the central design choice: every premise must use at least two SEED items as constitutive parts of the situation rather than as decoration. If removing both items leaves the premise intact, the SEED wasn't doing work. Specificity comes from concepts the story can't afford to lose.

**Regenerating premises.** Phases 2 and 3 are split so premises can be regenerated without rerolling the SEED. If Phase 3's 30 premises don't yield a compelling winner, run Phase 3 again; the SEED from Phase 2 persists.

**Thin SEEDs.** Some runs will produce SEEDs with only 3 or 4 surviving items because several dictionary words will fail to inflate into anything specific. This is a feature, not a bug. Thin SEEDs force each surviving item to do more work and constrain the premise space more tightly. Do not reroll for a thicker SEED — run with what the draw produced.

**User-supplied SEEDs.** A tweet-length SEED ≤280 characters gives the user direct steering over the story's concepts. Phase 2 verifies the length and proceeds without the dictionary draw. The load-bearing constraint still applies: premises should use the SEED's specific ideas, not just its general territory.

**Context management.** Each phase builds on the previous winner, not the full generation set. Phase 7 is the heaviest context phase (5 full stories of [LENGTH]). If context pressure causes quality to degrade, start a new conversation within the same Project, paste a summary of decisions so far plus the winning outline, and run Phase 7 fresh. The project knowledge (style guides, template) persists across conversations. A smaller intervention: if late-set regression shows up within Phase 7 itself (versions 4 and 5 phoned in), ask the model to write the five in two batches of three and two, with a review between them.

**When a run goes wrong.** If a phase produces output you dislike and steering doesn't fix it, start a new run rather than trying to recover mid-pipeline. The funnel creates path dependency: a weak premise in Phase 3 contaminates everything downstream, and a Phase 3 winner that's secretly a recognition-premise will produce a literary-realist story by Phase 7 no matter what the later phases do. A fresh start costs less than trying to rehabilitate a compromised run.

**Revision iteration.** Phase 8 can be repeated. Two revision passes is usually enough. More than three suggests a structural problem — go back to Phase 5 or 6 and regenerate downstream from a different structural choice. If the re-skin test fails twice in a row, go back to Phase 3 and pick a different premise.

**Model selection.** Use the strongest model available for all phases. Creative generation at this complexity degrades noticeably with weaker models, and the revision phase's sentence-by-sentence audit scales with model quality.
