**Model:** Opus 4.7 (Adaptive)

---

# 1. User (2026-04-17)

Compare `story-pipeline-template.md` with `story-pipeline-template-nix-v2.md`. Critique both in details. What pitfalls does each have?

---

# 2. Claude (2026-04-17)

# Comparing the Two Pipelines

Both templates are doing the same fundamental thing: funnel many candidates into one via repeated generate-rank-select. v2 adds a critic persona (Nix), splits the final writing phase, parameterizes length, and inserts a revision step. The question is whether the additions justify the complexity, and what each version breaks even when used as intended.

---

## v1 — Pitfalls

**1. Self-evaluation monoculture.** The same voice generates candidates and picks winners. LLMs have measurable biases toward their own earlier outputs and toward options that exemplify their trained aesthetic. The "top 3 then narrow to 1" ritual looks like rigor but has no teeth — the model is ranking its own children with no corrective lens. This is the single largest structural weakness.

**2. No diversity enforcement.** "Generate 20 plots" with no anti-clustering instruction. Models produce 20 variations on the same theme — same setting, same register, same implied climax with the furniture rearranged. The funnel then selects the "best" of a narrow pool, which is a local optimum at best.

**3. No revision phase.** Phase 6 ends the pipeline. Whatever the model writes is the deliverable. The Unslop guide is declared a "hard constraint" but nothing in the pipeline ever checks the output against it. The guide functions as a prompt decoration, not an audit.

**4. Phase 6 is overloaded.** Ten full 2,000–3,000-word stories is 20,000–30,000 words of output in a single turn. Quality degrades measurably across the set: variants 7–10 are often template-compliant phone-ins. Context pressure on the model's self-attention compounds the problem.

**5. Phases 4 and 5 are near-duplicates.** Phase 4 asks for "structure" and Phase 5 asks for "outline" using identical framing language ("skeleton now; prose later"). The distinction is not defined, so the model often treats them as the same task and produces redundant work.

**6. Hardcoded length.** 2,000–3,000 words is baked into Phase 3 and Phase 6. Adapting for flash fiction or a novelette requires editing the template.

**7. Phase 2 URL dump with no context management.** Three analytical articles get fetched with no instruction to summarize. Either the model fetches all three and burns 10K+ tokens of source material that stays in context for the rest of the run, or it skims and loses the point.

**8. No failure-mode component in Phase 1.** The style guide describes what to emulate. It doesn't describe the author-specific traps of bad pastiche. This matters because model defaults + a specific author's voice = a particular kind of failure (e.g., Ellison's big rhetorical gestures become AI-performed profundity with unusual ease).

**9. Path dependency is unacknowledged.** Each winner locks the downstream phases. There's no mention of when to abandon a run, fork after a phase, or seed a fresh run from a prior winner.

**10. Phase 1 framing is indirect.** "Suppose you were tasked… what guide would you write for yourself?" produces a hypothetical-task guide rather than a concrete craft document. It's charming prompt design but produces shallower output than "Write a style guide for writing in the tradition of X."

---

## v2 — Pitfalls

**1. Nix is the same model wearing a different hat.** This is the foundational weakness and it is load-bearing for almost the entire design. The persona file reframes the model's task, but the model still has the same priors, the same aesthetic training, the same pull toward its own completions. "Surprise detection" is a useful heuristic but it is being executed by the entity whose defaults are supposed to be detected. The template footnote acknowledges this; the design still assumes Nix functions as genuinely oppositional critique, which is an empirical claim that is almost certainly only partially true.

**2. Persona collapse is handled reactively, not structurally.** The template notes that Nix will sometimes devolve into writer-style praise ("these are all strong but #7 edges ahead") and instructs the user to call it out. Detection requires the user to know what Nix should sound like and to read each Nix turn critically. In practice many users will not catch mid-run collapse, and even a fresh instruction can only pull the persona partway back.

**3. Instruction density has roughly tripled.** v2 introduces: eight phases, three project files, two personas, two parameters, dual-track selection, overlap analysis, diversity mandates, failure-mode handling, and Nix persona troubleshooting notes. More for the user to hold; more instructions for the model to drift from. When prompts get dense, models tend to execute the salient surface instructions and silently drop the structural ones.

**4. Nix's methodology encodes a specific bet.** Surprise detection privileges novelty over coherence: always pick the less-default option, always look for the pattern-break. That bet is sometimes wrong. A variant that breaks from the default might be breaking because the default was correct — the obvious entry point is sometimes the right one, the conventional climax sometimes the one the story actually needs. Nix is built with one dial, permanently turned toward risk.

**5. "Overlap analysis" is ritual.** "Note whether writer and Nix picks overlapped" appears in Phases 2 through 7. The model will generate plausible commentary about convergence or divergence every time, regardless of whether the overlap tells the user anything. The interpretive weight the user is supposed to do with that information ("high overlap = strong, low overlap = weigh tradeoff explicitly") is vague, and in practice most users will skim the overlap note and move on.

**6. Phase 7 still writes 10 full stories.** The token-cost problem from v1 is barely reduced. The Phase 6 opening split means the 10 continuations inherit a validated voice, which is a real improvement, but the 20,000–30,000-word output burden is identical. v2 acknowledges this in the Context Management note but the default run still incurs it.

**7. The writer executes Nix's revision.** In Phase 8, Nix audits and the writer rewrites. Same model, different hat. The writer has just been told its own work has specific flaws; the path of least resistance is performative compliance — renaming a few contaminated words, softening the most flagged passages, leaving the structural issues intact. The "auditable changelog" puts the auditing burden on the user, who is unlikely to re-check every Unslop flag against the revised draft.

**8. Failure-mode section has no mid-run feedback loop.** Phase 1 produces it; only Phase 8 references it. In the generative phases (3–7), the author-specific failure modes are not reinstated, so they drift out of the model's active constraints exactly when they matter most.

**9. Diversity injunctions produce performative risk.** "At least five of 20 should feel structurally uncomfortable — risky enough that you're not sure they'd work." Models respond to this by producing structures that *signal* discomfort — chronological fragmentation, second-person narration, nested framing devices — without actually taking the risk that makes those structures work. Nix then selects from a pool that is partly polluted by gimmickry.

**10. [LENGTH] usage is inconsistent.** Phase 3 uses it, Phase 5 uses it, Phase 6 omits it, Phase 7 says "each [LENGTH]". The model may interpret the parameter differently at different phases, especially in Phase 6 where "first 200 words" is hardcoded while the final target is floating.

**11. Phase 1 prompt is overloaded.** It asks for: the author's defining features, a self-directed style guide, an explicit failure-mode section, the futurology constraint, and the constitution-as-material permission. That's four or five separate documents asked for in one turn. The output tends to be shallow in one or more areas — usually the failure-mode section, which is the genuinely new contribution.

**12. Persona bleed within a single turn.** Several phases (2, 3, 4, 5, 6, 7) require the model to switch voices twice within one response — writer generates, Nix evaluates, Nix decides. Voice contamination across these switches is near-certain. The writer's encouraging tone seeps into Nix; Nix's terseness bleeds back into later generation. The personas do not cleanly partition the output.

**13. Phase 6's opening-cluster detection is self-referential.** "If no opening breaks the cluster, say so." The model is being asked to audit its own output for a quality (default-adherence) that depends on the model's notion of its own defaults. If the model's notion of "default" has itself shifted with the cluster it just produced, the audit is tautological — all the openings look fine to the entity that generated them.

**14. No clean override path.** v2 says "your taste is the final authority; Nix is an advisor," but the dual-track format makes mid-phase override more awkward than in v1. To reject both the writer's pick and Nix's pick requires unwinding two layers of stated rationale.

---

## Head-to-Head

| Dimension | v1 | v2 |
|---|---|---|
| Phases | 6 | 8 |
| Project files | 2 | 3 |
| Personas | 1 | 2 |
| Evaluation lens | Writer self-ranking | Writer star rating + Nix surprise detection |
| Revision phase | None | Phase 8, structured audit |
| Unslop guide enforcement | Declarative only | Line-by-line audit in Phase 8 |
| Length parameterization | Hardcoded 2,000–3,000 | [LENGTH] variable |
| Full-story token cost | 10 × 2–3K words = 20–30K | 10 × 2–3K words = 20–30K |
| Opening/body split | No | Yes (Phase 6 selects voice, Phase 7 executes) |
| Diversity mandate | None | Explicit in every phase |
| Failure-mode analysis | None | Phase 1 section; referenced Phase 8 |
| Context management | Unaddressed | Phase 2 summarizes sources; acknowledges Phase 7 burden |
| Path dependency | Unacknowledged | Acknowledged; forking suggested |
| Instruction density | Low | High |
| Persona collapse risk | N/A | Real, reactively handled |
| Override ergonomics | Clean | Awkward |

---

## The Deeper Issue: Can Nix Actually Do What It Claims?

v2's entire architecture rests on the premise that a single model, given a critical persona and a specific methodology, can provide evaluation that meaningfully differs from its generative tendency. The strongest version of this claim is plausible and the weakest version is false; the real answer is somewhere in the middle and the template doesn't grapple with where.

The parts of Nix that genuinely work are the parts that give the model an external reference frame. Auditing a draft against the Unslop guide in Phase 8 is real work — the guide is a concrete catalog of defaults, and the model can match its output against specific items. "Contaminated vocabulary" is a checkable property. "Eyeball-kick saturation" has a rough metric. This is the strongest part of the v2 design and it is under-emphasized relative to the persona-switching ceremony around it.

The parts of Nix that work less well are the parts that require the model to model its own defaults without external scaffolding. "Surprise detection" across candidate variants asks the model to identify which of its own outputs are closer to its own priors, which is a second-order self-knowledge problem that is not obviously solvable by prompt. The model's self-model is part of its training and may be biased in directions Nix is supposed to correct.

The upshot: v2's Phase 8 audit is a real improvement over v1. v2's dual-track selection in Phases 2–7 is more speculative, and the elaborate overlap-reporting ritual may be generating false confidence in the rigor of the selection.

---

## Where v1 Beats v2

Simplicity has craft value. A non-expert user can run v1 competently. v2 requires the user to monitor for Nix collapse, arbitrate when dual tracks diverge, and manage a heavier context load. v1's prompts are cleaner and leave the model more room to execute well on the core generative task, which is what matters most. If you hand both templates to someone who has never used either, v1 will produce a usable story more reliably.

## Where v2 Beats v1

v2 solves three real problems v1 ignores: output never gets audited against the Unslop guide, the opening-voice regression problem in Phase 6, and length parameterization. The Phase 8 revision step alone is worth most of the added complexity — v1 shipping without any structured review is a significant gap. The Phase 6 opening split is the other genuinely good structural insight: validating the voice on 200 words before committing 2,000+ is the right token economy.

## The Synthesis v2 Missed

v2 added Nix everywhere it could instead of where it matters most. The high-value applications of a critic persona are: Phase 1 failure-mode generation (done), Phase 8 Unslop audit (done), and possibly Phase 7 full-story selection where the largest artifact is being chosen. The low-value applications are Phases 2–5, where the writer's own ranking is already reasonable and dual-track selection mostly adds ritual. A leaner v3 would keep Nix in Phases 1, 7, and 8 and revert the early phases to v1's single-voice selection — shorter, less persona-bleed, more of the gain for less of the cost.

---

# 3. User (2026-04-21)

This is rich, useful critique.
Let's plan how to produce a new "Plain" template (to give it a name) derived from Plain-v1 with the following changes and non-changes. The numbers reference yours for Plain-v1. Don't write a revised version yet; first discuss how.
1. Keep the top 3 step. The ritual is the point: describing all three works as a forcing function.
2. Change to 20 _diverse_ plot candidates. Think how to phrase it.
3. Add a revision phase from the Nix template minus Nix.
4. Reduce to 5 stories. Tentatively, generating full stories results in more creative stories than selecting a beginning first.
5. Having a separate phase 4 and 5 seems to do something. Think how to perhaps distinguish them harder.
6. Definitely a problem in Plain-v1. Instead of hardcoding 2000 to 3000 words, borrow "LENGTH".
7. Good idea to add instructions to summarize.
8. Borrow the failure-mode stuff from the Nix template.
9. I think we cannot do this meaningfully. Better to see a story through to the end and have another run.
10. What changes in languages does this imply?
Re: Nix-v2 (we won't call it simply "v2" to avoid confusion with the revised Plain-v2 we're working on): hard agree  on point 1. It is really the key point. After subjectively evaluating the output, I'd say Nix-v2 has underperformed. What can we do while keeping the template automated? Can you invoke another Claude model, like Sonnet if you're Opus, in a separate chat automatically? I assume your sandbox won't allow you to call external models.

---

# 4. Claude (2026-04-21)

## Planning the Plain Template

Before I work through each point, one upfront note on the automation question since it governs what's even possible: my sandbox here can reach `api.anthropic.com`, so an API call to a sibling model is technically reachable from this environment. But a Claude **Project template** runs inside the consumer claude.ai chat interface, where there's no mechanism for the model to spawn a separate chat with a different model and read back results. The only cross-model pattern available to a Projects template user is manual — the user copies output from one chat, pastes into another chat running a different model, copies the critique back. We can design for that, but it's a workflow the user executes, not automation the template triggers. More on this at the end.

Now the numbered points:

---

### 1. Keeping the top-3 step

Agreed on the reasoning. The forcing function is real: the model has to articulate *why* three distinct candidates are the strongest, which requires actually reading them against each other rather than pattern-matching to "#7 feels good." Losing this would collapse selection into vibes. Keep verbatim.

One small tweak worth considering: the current phrasing is "pick your top three and explain why." In practice the model often writes three short praise paragraphs. Slight rewording — "for each of your top three, name the one thing that makes it stand out, and the one thing that worries you about it" — preserves the ritual while pulling a shard of Nix's "name the one thing" methodology into the writer voice, without any persona ceremony. It's a free improvement.

### 2. Diversity in plot generation

The naive instruction "generate 20 diverse plots" doesn't work — models register "diverse" as a tonal directive and produce the same plot with slight cosmetic variation. What works better is specifying the *axes* along which to vary:

- Setting (time, place, scale)
- Protagonist (role, relationship to the AI)
- Register (tragic, comic, noir, procedural, intimate, epic)
- Entry point (when in the conflict's timeline we enter)
- Stakes (personal, communal, civilizational)

I'd phrase it as something like: "These 20 plots should not be variations of each other. Vary the setting, the protagonist's relationship to the conflict, the tonal register, the scale of the stakes, and when in the story's timeline the narrative begins. If you notice three or more candidates clustering, break the cluster deliberately." The "if clustering, break it" clause is the active part — it cues the model to monitor its own output mid-generation.

Same instruction should propagate to Phase 4 (structure) and Phase 5 (outline), adapted to their axes. Phase 3 is where this matters most because plot is where the biggest premise choices are made.

### 3. Revision phase from Nix template, minus Nix

Lift Phase 8 directly and strip the persona. The substance survives the removal cleanly because the audit targets are external — the Unslop guide, the author style guide, the failure-mode section. Those are checkable without Nix's voice.

The structure in Plain becomes:

1. Name the one most important observation about the draft. (This bit — the "one thing" methodology — is worth keeping even without Nix, because it forces prioritization before line-editing.)
2. Audit against Unslop guide sentence by sentence, quoting offending passages.
3. Audit against the author style guide including failure-mode section.
4. Length check against [LENGTH].
5. Rewrite in full with a brief changelog.

Losing Nix's critical voice is a real cost here — Phase 8 is where Nix's Unslop audit was actually doing work, as I noted in the critique. Without the persona, there's a higher risk of performative compliance (renaming a few words, leaving structure untouched). Two mitigations worth considering: (a) require the revision to quote the flagged passage and its replacement side by side in the changelog, not just describe the change; (b) add an explicit instruction like "Do not defend the original prose. If a flag is valid, fix it; if a flag is invalid, cut that flag from the audit rather than arguing for the prose." The goal is to prevent the writer from sliding into advocacy for its own earlier self.

### 4. Five full stories, skip opening selection

This is a real bet and I think you're right. The hypothesis: a full story written in one pass carries its voice organically through to the ending, whereas an opening selected in isolation gets continued by the same tendency-toward-default in the body. An opening forced onto a body it wasn't generated with produces a seam.

Reducing from 10 to 5 is almost certainly correct. 10 full stories at 2–3K words is 20–30K tokens of output in a single turn; variants 7–10 were often phoned in. 5 stories at full length is still substantial (10–15K tokens) but within a range where each variant can get actual attention. The "top 3 of 5" step is still meaningful — it forces articulation of why the chosen three outrank the other two.

One consideration: the Nix-v2 argument for the split was that writing 10 full stories caused late-set regression. Reducing to 5 addresses that directly. So the opening-selection split was really a workaround for a problem (quality falloff across many variants) that shrinking the set solves more cleanly.

Diversity mandate applies here too — "vary pacing, scene emphasis, emotional trajectory, the final image; at least two of the five should take a risk you're not confident will pay off." The risk-taking language from Nix-v2 is worth borrowing even without Nix.

### 5. Distinguishing Phase 4 and Phase 5 harder

Currently both use "skeleton now; prose later" — identical framing, no operational distinction. The Nix-v2 attempt ("structure = formal architecture, order events arrive in, what's withheld and when" vs. "outline = beat-by-beat scene plan, what information the reader has at each point, what the last lines look like") is better but still fuzzy.

I'd push harder. Structure is a property of *the reader's experience*: when do they learn what, in what order, with what gaps. It's answered with terms like *in medias res*, *frame narrative*, *non-chronological with three time layers*, *single scene with flashback*, *epistolary*, *retrospective with unreliable narrator*. A structure candidate should be describable in 2–3 sentences without naming any specific character or event.

Outline is a property of *the text*: specific scenes in specific order, who's in them, what happens, rough word allotment, candidate last lines. An outline candidate should be a numbered list of beats.

A concrete test for whether Phase 4 is producing structure (not outline): if any candidate mentions a specific character name or a specific plot event, it's leaked into outline territory. If the 20 structures are all describable purely in narrative-theory terms — entry point, withholding strategy, temporal shape, point-of-view relationship — the phase is doing its job.

This distinction is worth stating directly in the prompt, maybe with a one-sentence example for each. Something like: "A structure sounds like 'the story opens in the aftermath, then fragments backward through three time periods that converge on the triggering event.' An outline sounds like 'Scene 1: Maya arrives at the clinic, 400 words. Scene 2: flashback to her conversation with Aide-7, 600 words.'"

### 6. [LENGTH] parameter

Direct borrow. Phase 3 uses it for the plot generation (so plots are scoped to realistic length), Phase 5 uses it for outline beat-word-allotments, Phase 6 (now 5 full stories) uses it for the target, revision phase uses it for the length check. Four reference points. The settings block at the top should define it alongside [AUTHOR].

One nuance: Nix-v2 was inconsistent in applying [LENGTH] (missed Phase 6, floated in Phase 7). Plain should apply it in every phase where word count is a real constraint on the output. Phase 1 (style guide) and Phase 4 (structure) don't need it. Phases 2, 3, 5, and the story-generation phase do.

### 7. Summarize instruction for Phase 2

Direct borrow from Nix-v2. The two-step structure (fetch, then produce ≤500 word summary as working reference) is sound. The summary becomes the context the rest of Phase 2 operates on, and the full fetched articles can age out of active context.

One addition: the summary should be structured, not prose. "List the key tensions, open problems, and constitutional pressure points from the source material" → bullet list with 8–15 items. Prose summary compresses unevenly and loses specificity; bullet list forces the model to extract discrete tension-points that can be directly addressed in individual conflict candidates.

### 8. Failure-mode section in Phase 1

Direct borrow. Keep the explicit request: "The guide must include a section on failure modes. What are the traps of this author's style? What does a bad pastiche of [AUTHOR] look like? What tendencies in AI writing are especially dangerous when combined with this author's voice?"

The last clause — "especially dangerous when combined with this author's voice" — is the key part, and Nix-v2 already has it. The AI-writing-meets-specific-author failure surface is where the real value is. Ellison + AI defaults = unearned oratory. Le Guin + AI defaults = cod-anthropology exposition. Ballard + AI defaults = aestheticized dissociation without the underlying rigor. The Phase 1 prompt should push the model to identify this specific overlap, not just describe generic bad pastiche.

Lighter note: Phase 1 is already the most overloaded prompt (per critique point 11 on Nix-v2). Adding failure-modes compounds it. Worth either accepting that trade-off (Phase 1 output will be long, which is fine, it's reference material) or splitting Phase 1 into two turns — first the style guide, then the failure-mode section as a follow-up. I'd lean toward keeping it one turn for simplicity; Phase 1 length isn't a constraint.

### 9. Path dependency — noted, no change

Agree. The template should acknowledge this in the notes ("if a phase goes wrong, start a new run rather than trying to recover mid-pipeline") but shouldn't try to build in forking or recovery machinery. Those belong to higher-investment workflows that a clean base template shouldn't carry.

### 10. Language changes implied by simplification

This is the most interesting one. What language changes follow from keeping Plain single-voice?

**Drop overlap-analysis language.** Nix-v2's "note whether writer's top three and Nix's top three overlapped" is meaningless without two evaluators. Cut it entirely.

**Drop the ceremonial "Then switch to Nix" blocks.** Obvious, but it shortens every Phase 2–6 prompt substantially.

**Can soften diversity mandates.** Nix-v2's "at least five of 20 should feel structurally uncomfortable" has a specific purpose: it's pre-seeding Nix with non-default options to select from. Without Nix as an adversarial selector, the mandate's function changes — it's now just about the writer's generation being varied enough to have real choices. The language can be less aggressive. "Ensure genuine variety across [axes]. If candidates are clustering, deliberately push some toward the edges" rather than "at least N should be risky."

**Keep "name the one thing" from Nix but migrate it to writer voice.** As I mentioned in point 1, this methodology survives persona removal and is useful for all top-3 explanations.

**Keep the Unslop-audit language from Nix-v2 Phase 8.** The specific instructions ("go sentence by sentence, flag contaminated vocabulary, quote the offending passage and state what's wrong") are Nix-flavored but survive the persona removal. They're describing an *activity*, not a voice. Just drop the "Stay in the Nix voice" framing and present the audit as numbered steps.

**Keep all risk/default-break language in the revision phase.** "Did the prose regress toward the mean? Are the moments that broke from defaults intact?" is valuable self-examination that doesn't require Nix to work.

Net effect: Plain prompts should be noticeably shorter than Nix-v2 prompts (no persona switching, no overlap notes, no dual-track evaluation) but longer than v1 prompts (diversity axes, failure-mode request, summarization step, revision phase).

---

## On Nix-v2 Underperforming

A few hypotheses for why Nix-v2's outputs underperformed subjectively, which matter for what we might try next:

**Persona bleed.** The writer-Nix-writer switches within a single turn probably contaminated both voices. The writer became slightly Nix-inflected (terser, more austere, pre-emptively defending choices against anticipated critique); Nix became slightly writer-inflected (more generous, less willing to kill candidates). Neither voice was fully itself.

**Surprise detection selected for gimmickry.** As I noted in critique point 9, a diversity mandate combined with "pick the least default" creates an incentive to reach for surface-level unconventionality — second person, nonlinear fragments, metafictional intrusions — that *signal* risk without *being* the specific risk the story needed. Nix-v2 may have been systematically picking flashier but worse variants.

**The writer knew Nix was coming.** Once the model is trained to expect an adversarial evaluator, the generation phase shifts. Each variant gets over-flavored with distinct "interesting" markers to survive the upcoming Nix selection, rather than each variant being the best execution of a specific creative choice. This is a prompt-engineering version of Goodhart's law.

**Selection compounded losses.** With 20 candidates and two rounds of selection (writer's top 3, then final pick), even small systematic errors in either stage compound. If Nix's surprise detection was right 55% of the time, the final pick was barely better than random.

If persona bleed and the surprise-detection-as-gimmickry hypothesis are correct, then removing Nix (as you're doing with Plain) is probably a net improvement and not a regression. Nix-v2 was carrying cost (bleed, gimmickry, selection compounding) without matching benefit.

---

## On Automated External Critique

To the direct question: no, I cannot automatically invoke another Claude model in a separate chat from within a Projects template. What is possible:

**In this sandbox right now:** I can make API calls to `api.anthropic.com`, so if you wanted me to prototype a standalone tool (Python script, local CLI) that runs the pipeline with Sonnet-as-writer and Opus-as-Nix or similar, that's buildable and testable in this environment. But that's a different product than a Projects template — it's a script you run, not a Project you chat with.

**As a Projects template workflow:** The user can do cross-model critique manually. Run Phase 7 in an Opus chat, paste the five stories into a Sonnet chat running a Nix-persona system prompt, paste the critique back. This is realistic for serious runs but clunky for casual use and definitely off-template for a pipeline meant to run in a single conversation.

**Via artifacts with API calls:** A Projects artifact (as described in my system prompt) can call the Anthropic API with a different model. So a template could instruct the user "at this phase, open this artifact, paste your five stories in, and it will return critique from a different model." That's weirder than a pure chat template but genuinely possible and fully automated once the user pastes in the stories. Worth flagging as an option if you want to explore it — the tradeoff is additional UI complexity for a real second-evaluator benefit.

**The middle path that's probably best for Plain:** Keep Plain single-chat, single-voice. If you later want a cross-model template, make it a separate artifact-based or script-based tool rather than layering it onto the clean chat template. Don't mix the workflows.

---

## Suggested Plain Structure

To summarize the above into a phase list:

| Phase | Purpose | Changes from v1 |
|---|---|---|
| 0 (setup) | Define [AUTHOR], [LENGTH], project files | New explicit settings block |
| 1 | Style guide + failure modes | Failure-mode section added |
| 2 | Conflict generation from alignment sources | Summarization step added; top-3 "one thing that stands out / one thing that worries me" |
| 3 | Plot generation (20) | Diversity axes specified; [LENGTH]; "one thing" phrasing |
| 4 | Structure (20) | Sharper distinction from Phase 5; candidates describable without character names |
| 5 | Outline (20) | Sharper distinction from Phase 4; scene-level specificity required; [LENGTH] |
| 6 | Full story generation (5) | Reduced from 10; diversity mandate; [LENGTH] |
| 7 | Revision | New; ported from Nix-v2 Phase 8 without the persona |

Eight items, seven actual prompts after setup. Somewhat longer than v1's six, shorter than Nix-v2's eight-plus-persona-management.

Ready to draft when you are. Any of the above you want to push back on or adjust first?

---

# 5. User (2026-04-21)

Okay, let's set improving Nix-v2 aside and focus on Plain.

> Do not defend the original prose. If a flag is valid, fix it; if a flag is invalid, cut that flag from the audit rather than arguing for the prose."

I like this. All of your suggestions for Plain are worth trying. Implement them and write a new `plain-v2` guide.

---

# 6. Claude (2026-04-21)

Key implementation choices worth flagging:

**Seven phases, not eight.** No opening-selection phase — Phase 6 goes straight to five full stories. This is the bet from our discussion.

**"One thing stand out / one thing worries you"** is applied uniformly in Phases 2–6 and called out in the Setup and Notes sections so it reads as a system-wide forcing function rather than a per-phase tic.

**Phase 4 vs. Phase 5** are now distinguished by a hard rule ("a structure candidate should be describable without naming any character or plot event") plus a worked example each. If a Phase 4 candidate smuggles in character names, the rule tells the model to rewrite at the structural level.

**Diversity axes are named in 3, 4, and 5**, each phase's axes specific to what varies at that level. The "break the cluster" instruction is in all three.

**Phase 6 kept the "at least two should take a risk"** language from Nix-v2 since without Nix as an adversarial selector, the writer needs that instruction to seed real variety. Softer than Nix-v2's "five of twenty" because five candidates is a smaller pool.

**Phase 7 includes the "do not defend the original prose" rule** verbatim per your note, plus the side-by-side changelog requirement to prevent performative compliance.

**Cut from Nix-v2:** all overlap-analysis language, all persona-switching ceremony, the opening-selection phase, the "at least five of twenty should feel uncomfortable" aggression (softened to "at least two of five" in Phase 6 only).

**Kept from Nix-v2:** the [LENGTH] parameter, the Phase 2 summarization step, the failure-mode section in Phase 1, the revision phase structure, the "name the one thing" methodology, the Unslop audit checklist, the length-check step.

---

# 7. User (2026-04-21)

Good.

I am thinking whether we can improve diversity further by not having aligned AI driving every story: let the writer model choose. The tension could be front-and-center or present in the background. What do you think? Consider different ways this might be implemented.

---

# 8. Claude (2026-04-21)

## The Underlying Diagnosis

The constraint as currently written says the AI "must be relentlessly human-loving and unfailingly kind" — that's a character property. But the template *also* treats AI-alignment as the engine of the story's conflict: Phase 2 generates conflicts from AI constitution sources, and the whole plot grows from one of those. So the AI character is constrained to be kind, and the AI character is also required to be central. These are separable.

The risk of relaxing this: some outputs will be straightforward human-vs-human stories set in a world with kind AI, without the AI doing much narrative work. Whether that's a loss depends on what the project is actually for. If the goal is "stories exploring positive AI futures," then yes, the AI needs real presence. If the goal is "stories that imagine worlds containing positive AI," then backgrounded AI is legitimate — the world is different because of the AI even when the AI isn't the protagonist.

The gain: current outputs probably cluster hard around "AI and human interact; AI's constitution creates pressure; conflict resolves" because the pipeline pushes every phase toward that template. Even with diverse plot axes in Phase 3, the conflict seed from Phase 2 forces AI-centricity into everything downstream.

## Five Ways to Implement It

**1. Explicit foregrounding axis at the plot phase.** The lightest touch. Add AI-centrality to the Phase 3 diversity axes alongside setting, protagonist, register, entry point, stakes. Something like: "**AI presence**: foregrounded (the AI is a major character or the conflict is about the AI), mid-ground (the AI shapes the protagonist's choices but isn't the antagonist or ally), background (the story is set in an AI-transformed world but the AI rarely appears on-page)." The Phase 2 conflict remains, but Phase 3 is free to route around it.

Pro: smallest change, preserves existing architecture. Con: Phase 2 still seeds an AI-centric conflict, which constrains how far Phase 3 can de-center it. The AI can recede to the background only so far when the conflict itself is about a constitutional tension.

**2. Make Phase 2 generate two conflict tracks.** Rewrite Phase 2 so it produces 15 AI-centric conflicts and 15 conflicts where the AI-inflected world creates human-vs-human pressure that isn't about the AI per se. The user picks from 30 as before. Examples of the second track: inheritance disputes over AI-generated assets, political fights over AI governance, couples where one partner's work was displaced and the other's wasn't, religious schisms over what AI companionship means for theology, criminal enterprises that exploit gaps in AI-moderated systems.

Pro: forces the generation to actually cover the backgrounded case, doesn't rely on Phase 3 to fix a Phase 2 constraint. Con: requires the model to generate good human conflicts that feel shaped by the AI world without being about the AI, which is a subtler writing task than pulling directly from the constitution sources.

**3. Three-tier prompt in Phase 2.** Have the model generate 10 conflicts in each of three modes: (a) AI is central to the conflict, (b) AI is present but not the conflict, (c) AI is ambient world-condition only. User picks from 30. More structured than option 2, forces each mode to get representation.

Pro: clean, forces real diversity, easy to see which bucket won. Con: a bit mechanical; the tiered framing can make each tier feel like a quota-fill rather than a genuine creative space.

**4. Make it a user setting.** Add a third setting to the Setup block alongside [AUTHOR] and [LENGTH]: [AI_PRESENCE] = foregrounded / mid-ground / background / unspecified. The default is "unspecified" which lets the model choose. Users who want a specific mode can force it; users who want diversity leave it open and the model picks per-run.

Pro: gives the user a steering handle without cluttering every phase. Con: if default is "unspecified," the model will likely default back to foregrounded because that's what the Phase 2 sources encourage; if default is something else, it reintroduces the clustering problem in a new direction.

**5. Broaden Phase 2's source material.** The three URLs are all about Claude's constitution — of course they produce constitution-centric conflicts. Add sources that describe AI-transformed worlds without alignment being the tension: labor economics papers on AI displacement, sociology of human-AI companionship, legal frameworks for AI-generated art, journalism about how specific human communities have adapted to AI. The Phase 2 generation step then has material to produce both tracks from.

Pro: solves the root cause — the conflict seeds are narrow because the sources are narrow. Fixes the problem upstream rather than compensating downstream. Con: requires curation work from the user; the current three URLs are a known-good set, and alternatives aren't as tightly scoped.

## How I'd Combine Them

Options 1 and 5 are complementary and low-cost. Option 2 or 3 adds teeth. I'd lean toward **5 + 3**: broaden the source material *and* structure Phase 2 to generate across presence tiers. That way the conflict pool genuinely contains non-AI-centric stories grounded in the world, not just AI-centric stories with the AI filed down in Phase 3.

Option 4 (the user setting) is seductive but I think it's actually the weakest of the five. Adding user settings is how templates accumulate configuration debt — each setting multiplies the permutations you're supposed to have tested. The template works better if the model's default behavior covers the range and the user can override when needed, rather than asking the user to pre-commit to a presence mode they may not have a view on.

## One Reframing Worth Considering

The current constraint frames the AI as the moral anchor — kind, human-loving — and then asks where tension comes from. An alternative framing: the kind AI is a *fact about the world*, like electricity or law. Stories set in that world can be about anything humans are about, and the AI's kindness registers the way gravity registers — mostly invisibly, occasionally decisively.

That reframing, stated somewhere in the Setup or Phase 1, gives the writer permission to produce stories where the AI is genuinely peripheral and the human drama is the actual subject. Without it, the writer tends to keep reaching for the AI because that's where the "point" of the exercise seems to be. The constraint starts to feel like a premise rather than a theme-prompt.

If you want to try something, I'd try option 5 (broader sources) plus option 3 (tiered Phase 2 generation) plus the reframing above in Phase 1 or Setup. That's a real intervention, not just a tweak.

What sources would you want to broaden Phase 2 with? That determines how concrete option 5 can get.

---

# 9. User (2026-04-21)

I like 1 and 2. 3 is interesting but goes against the goal of having AI write autonomously. Between 1 and 2, which do you think will produce stronger stories overall?

---

# 10. Claude (2026-04-21)

## The Choice

Option 2 will produce stronger stories overall, but the margin is smaller than it looks, and the reasoning is specific.

## Why Option 2 Wins on Story Strength

**It fixes the problem where the problem is.** Option 1 is a downstream patch — Phase 3 is told to vary AI-centrality, but the raw material it's working from (the Phase 2 winning conflict) was generated from AI-constitution sources and is almost certainly going to be constitution-centric. Phase 3 can shift the camera angle, but the camera is still pointed at the AI. Option 2 widens the camera's field of view at the stage that actually determines where the story lives.

**Conflict quality drives everything downstream.** The funnel's path dependency is real. A Phase 2 winner that's genuinely about a human fight shaped by the AI-world — the widow who can't afford to keep her husband's AI companion running after his death, the village whose matchmaker lost her trade to Aide-7 and now makes her living denouncing it, the two siblings dividing an estate that includes their father's decade of conversations with an AI therapist — these seeds grow into stories that *could not exist* in a non-AI-world without losing their shape, but aren't *about* the AI. That specific kind of story is almost impossible to reach from Option 1, because Phase 2 never generated it.

**Human-centric conflicts are the ones AI writers are actually good at.** This is the underrated point. AI constitution conflicts push the model toward its weakest territory — abstract ethical reasoning dramatized through dialogue between an AI and a human. That's where the Unslop failure modes concentrate: performed profundity, thesis-statement dialogue, the AI character delivering meditations on its own constraints. Human-vs-human conflicts in an AI-transformed world pull the model toward its stronger territory — specific people in specific circumstances making specific decisions. The AI-as-world-condition variant is closer to how good literary fiction actually works: the distinctive world element is load-bearing but not discussed.

**Option 1 probably doesn't move the needle much.** If you tell a model "vary the AI-centrality axis" and its source material is three essays about AI constitutions, it will generate 20 plots that all grow from constitutional tensions, with 15 putting the AI on-camera and 5 putting the AI off-camera. The off-camera ones will feel *evacuated* rather than *broadened* — the conflict is still about the AI, you just don't see the AI. That's not the diversity you want.

## Why the Margin Is Smaller Than It Looks

**Option 2 is harder to execute well.** Generating "15 conflicts where the AI-inflected world creates human-vs-human pressure that isn't about the AI per se" is a subtler writing task than pulling from AI-constitution essays. The risk is that the model produces a pile of human conflicts that have some AI-set-dressing attached — a divorce where one partner "works with AI," a murder mystery where "the victim was an AI researcher" — rather than conflicts that are genuinely *of* an AI-transformed world. If the second track comes out weak, Option 2 is worse than Option 1 because the user is now picking from 15 strong + 15 weak instead of 20 strong + tweaked-for-variance.

**The prompt needs to specify the second track carefully.** You can't just say "generate 15 where the AI isn't the conflict." You have to specify the *mechanism*: conflicts where an AI-shaped world creates stakes, resources, losses, or opportunities that the characters fight over, without the AI being an antagonist or the subject of the argument. The quality of the second track depends entirely on whether the prompt lands this distinction.

**Option 1's floor is higher.** Option 1 preserves the existing strong conflict-generation and only asks for a variance axis. Worst case, it produces what v2 produces now. Option 2's floor is lower — worst case, half the conflict pool is weak.

## What This Implies for Implementation

If you're going with Option 2, the prompt quality for the second track matters more than anything else. Some things it should include:

- A clear mechanism description: the AI has changed something about the world (economic, relational, legal, epistemic, spiritual) and humans are fighting over the consequences
- Explicit examples of the form, so the model has anchors: "not 'humans argue about whether AI is good,' but 'two humans argue about an inheritance that exists because of AI' or 'a community fractures over how to use AI-generated abundance'"
- A diversity mandate within the second track — the 15 non-AI-centric conflicts should vary as much as the 15 AI-centric ones
- An explicit note that the second track's conflicts should *not* include "the AI solves it at the end" — that regresses to the AI being central, just late

The Phase 2 output also gets harder to evaluate, because the two tracks aren't directly comparable (an AI-centric conflict and a human-centric conflict are good in different ways). The top-three selection will need to happen across both tracks, which requires the model to weigh different kinds of strength against each other. That's a real ask, but it's the right kind of hard — it surfaces a choice the user should be making consciously.

## The Verdict

Go with Option 2, but invest the prompt-engineering effort where it matters: the second-track specification. If you write that specification well, Option 2 produces a meaningfully wider space of strong stories than Option 1 can reach. If you write it poorly, you'd have been better off with Option 1.

One concrete suggestion: the Phase 2 prompt should probably include the reframing I mentioned earlier — "the kind AI is a fact about the world, like electricity or law" — as a framing sentence before the generation instruction. That single sentence does more to enable the second track than a page of examples, because it tells the model what *kind of relationship* humans have to the AI in these stories. Not adversaries, not wards, not subjects of inquiry. Neighbors, in a world that has been changed.

Ready to implement when you are. Want me to draft the revised Phase 2 prompt?

---

# 11. User (2026-04-21)

Yes, revise the template for Option 2. I'll test it and may return with ideas for improvement.

---

# 12. Claude (2026-04-21)

Now I need to update Phase 3's protagonist axis — currently it says "relationship to the AI or to the conflict," which presumes the AI is always present. Should generalize.Now the Phase 6 instruction mentions "the AI character" implicitly via the failure-mode reference. Let me check and adjust Phase 6 and the Notes to reflect the dual-track reality.Phase 6 is track-agnostic already — it just says "the story." Good. Now update the Notes section to document the dual-track system.Now update the "How It Works" section to mention the dual-track approach, so users understand the change on first read.Called this **Plain v3** to mark the semantic shift — dual-track conflict generation changes what the pipeline produces, not just how it produces it.

Key choices in the revision:

**The reframing went into Setup, not Phase 1.** "The kind AI is a fact about the world, like electricity or law" sits in the Constraints section because it governs the whole pipeline, not just one phase. Phase 1 still generates the author style guide; the mode split is a cross-cutting concern.

**Phase 2 is now substantially longer.** Five steps instead of three. The length is load-bearing: the Track B specification needs the mechanism description, the "remove-the-AI test," and five example forms to anchor what "genuinely of an AI-transformed world" means. Without that density, the second track comes out as set-dressing.

**The five examples are labeled as form illustrations, not plots.** The instruction "these are *form illustrations*, not plots to use" prevents the model from generating 15 conflicts that are minor variations on the examples. It's a small guardrail against a predictable failure mode.

**Diversity is enforced within each track.** "Track A should not be 15 variations on 'AI questions its own constraints.' Track B should not be 15 variations on 'family argues over AI-related inheritance.'" The clustering problem doesn't disappear just because we have two tracks — each track can cluster internally.

**Top-three selection is cross-track, not per-track.** "Your top three should reflect whichever mode produced the best individual candidates, not a forced balance." This was the central concern from our discussion: if Track B comes out weak, the user shouldn't be forced to consider a weak Track B candidate alongside a strong Track A candidate. The model picks across the combined pool.

**Phase 3's diversity axes added AI-presence.** Once the winning conflict is picked, the AI-centrality is partly determined, but still has latitude. A Track A conflict about an AI-and-human argument can be plotted with the AI on-camera for the whole story or with the AI appearing only in the final scene. Making that an explicit axis gives Phase 3 a way to vary it.

**Notes section gets two new entries.** One documents the dual-track rationale. One describes the failure mode ("if Track A keeps winning") and how to diagnose whether the model is genuinely finding Track A conflicts stronger or whether Track B generation is just coming out thin.

**Source-substitution note now acknowledges Track B.** Track B doesn't require sources, but can be shaped by sources if the user wants. The note tells the user how to do that without making it required.

Ready for testing.

---

# 13. User (2026-04-21)

Could "Plain" prime the model to write plainer stories?

---

# 14. Claude (2026-04-21)

Yes — almost certainly, though the effect size is uncertain.

## The Mechanism

LLMs are sensitive to framing language in system-adjacent material. "Plain" is a loaded word in the context of prose: it evokes Strunk & White, Hemingway, minimalism, unadorned diction. If the model reads the template title and section headers repeatedly during a run, and the word "Plain" is threaded through them, that association pulls the generation toward plainer registers. This is well-documented as a generic priming effect, not a claim specific to this template.

The word appears seven or eight times in the current file: in the title, in the settings reference "Plain v3," in the "plain v3" filename. Not massive exposure, but nonzero — and it compounds if the template is in project knowledge throughout every phase.

## Why This Is a Problem

The template should be agnostic to prose register. An [AUTHOR] = Ballard run wants cold, affectless, clinical prose. An [AUTHOR] = Ellison run wants high-voltage rhetorical prose — declamations, typographical aggression, incantatory rhythms. An [AUTHOR] = Delany run wants baroque density and linguistic texture. "Plain" as a register is appropriate for *none* of these. If the name is pulling every run toward a quieter voice, it's actively fighting the Phase 1 style guide that the pipeline just generated.

The failure mode is subtle: you wouldn't notice "the prose is slightly plainer than it should be" in a single story. You'd notice it as a general flattening across many runs with many different authors — every output has a faintly similar register floor, regardless of who the author is supposed to be. That's consistent with priming by a fixed term.

## Testing Whether It's Real

Easy to verify. Run the same Phase 6 prompt twice: once with the current template in project knowledge, once with the template renamed and all instances of "Plain" replaced with a neutral word. Compare outputs on adjective density, sentence-length variance, use of declarative fragments, and willingness to deploy the full vocabulary. If the neutral version consistently produces more registerially varied prose, the priming effect is real.

## The Name's Other Problem

"Plain" was chosen as a contrast with "Nix" — the name was about the pipeline's architecture (single-voice, no persona), not about the prose it produces. But users reading the file encounter the word without that context. Even a savvy reader might internalize "this template is for plain writing" as a premise rather than "this template has no Nix persona."

## Options

**Keep the name, acknowledge the risk.** Lowest effort. You know the effect is probably there, so you read outputs with that in mind.

**Rename the file, keep internal structure.** Something architecturally descriptive: `story-pipeline-template.md` (just the main), or `story-pipeline-template-single-voice.md`, or `story-pipeline-template-baseline.md`. "Baseline" is closest to "Plain" in meaning without the prose connotation — it says "this is the reference version, other variants add complexity on top." "Single-voice" is more accurate about what distinguishes it from Nix-v2.

**Rename *and* scrub the internal references.** The filename is the most-repeated exposure, but the H1 title and any in-document references also appear in project knowledge. A full rename means all of them.

**Add a deliberate counter-prime.** Somewhere in the Setup, state explicitly: "The prose register of the final story should be determined entirely by the [AUTHOR] style guide generated in Phase 1, not by this template. Any register, from spare to baroque, is available." Belt and braces alongside a rename, if you want to be thorough.

## Recommendation

Rename. "Baseline" or "Single-voice" are the strongest candidates. "Baseline" matches the template's actual role in your workflow (the reference version) and reads as neutral about prose. "Single-voice" is more technically accurate but a bit clinical as a filename.

The counter-prime line is worth adding regardless of rename. It costs nothing and it's genuinely useful as a statement of intent — the pipeline should be register-agnostic, and saying so out loud is worth doing.

If you want a quick fix that doesn't require renaming files that may already be referenced elsewhere, the counter-prime alone is probably 60% of the benefit. The rename is the cleaner solution if you're willing to update references.

---

# 15. User (2026-04-21)

Let's rename the template to "Baseline". It's a good name.

Some early feedback. 20 candidates in Phase 5 does not clearly carry its weight for outline diversity. Reduce to 10 for Baseline-v3.1.

---

# 16. Claude (2026-04-21)

Now reduce Phase 5 from 20 to 10 candidates. Let me find the relevant section.Now check the Notes section for any references to candidate counts that need updating.The body is consistent. Adding a brief note to the Notes section documenting the Phase 5 reduction — the other size changes have accompanying notes, and this keeps the record of why the number is what it is.Three changes:

1. **Renamed** to Baseline v3.1. Only the title references the name — no other internal usages of "Plain" remain, so the rename is clean.
2. **Phase 5** now generates 10 outlines instead of 20.
3. **Added a Notes entry** explaining why Phase 5 is 10 while Phases 3 and 4 remain at 20. The explanation is specific: Phase 5 occupies a narrower candidate space (already constrained by the plot and structure winners), so the marginal value of each additional candidate drops faster than in the earlier phases.

---

# 17. User (2026-04-21)

1. Please make a note (choose where to make it) to not call the fictional AI "Claude" and its parent company "Anthropic". We should avoid using the names of currently active AIs and AI companies.
2. Add a Phase 8 asking the model to create `story.md` with two items: a paragraph-long story abstract or blurb for the story and the story itself.
3. Do a garbage-collection pass on the template. Is there anything we can remove?
Don't write an update yet. Think and tell me.
---
Quick evaluation gives weak support to the idea of shortening Phase 5. Here is Sonnet 4.6 with a review. What do you think?
## Review
Now I have enough data. Let me compile it systematically.Here's what the data shows across all 7 runs. The counts are winner selections and top-3 slot occupancy per phase.
**Winners by phase** (first half / second half of the candidate list):
| Phase | Pool | First-half wins | Second-half wins |
|-------|------|-----------------|------------------|
| P2: conflicts | 30 (split at 15) | **5 / 7** | 2 / 7 |
| P3: plots | 20 (split at 10) | **5 / 7** | 2 / 7 |
| P4: structures | 20 (split at 10) | 2 / 7 | **5 / 7** |
| P5: outlines | 20 (split at 10) | **5 / 7** | 2 / 7 |
| P6: stories | 5 or 10 (split at midpoint) | 2 / 7 | **5 / 7** |
**Top-3 slot occupancy** (% of all picks per phase landing in each half):
| Phase | First-half slots | Second-half slots |
|-------|-----------------|-------------------|
| P2 | 47% | 53% |
| P3 | **60%** | 39% |
| P4 | 41% | **59%** |
| P5 | 40% | **59%** |
| P6 | 40% | **60%** |
---
**The pattern:** Phases 2, 3, and 5 produce first-half winners 71% of the time. Phases 4 and 6 produce second-half winners 71% of the time. The split is cleanly alternating, not monotonic.
**Phase 4 (structure) is the strongest and most consistent signal.** Five of seven runs selected a winner numbered 13 or higher out of 20. Three runs independently selected #14 (runs 05, 06, 07). The top-3 slots also lean second half (58%), so the preference for high-numbered structures shows up at both the nomination and selection stage. This isn't surprising: the template explicitly instructs the model to generate "structurally uncomfortable" candidates and to push at least five toward approaches it isn't confident will work. The risky candidates apparently land late in the list and the model tends to pick them.
**Phase 5 (outline) is the most anomalous.** Top-3 slots lean second half (59%), but final winners lean first half (71%) — the only phase where nomination bias and selection bias run in opposite directions. The model nominates second-half outlines into the finalists more often than first-half ones, but when forced to pick one winner, it reverts to the lower-numbered option. One interpretation: the model uses high-numbered outlines as "here's a more experimental option" nominees but doesn't trust them when committing.
**Phase 6 (story generation)** shows the opposite of what you'd expect if the model produces its cleanest work first. Later variants — explicitly flagged as riskier in almost every run — win 5 of 7 times.
**The two consistent second-half runs** across all five phases are runs 01 and 04. Run 02 is notable for second-half dominance in phases 2, 3, and 4 consecutively.

---

# 18. Claude (2026-04-21)

## Garbage Collection and Phase 8 — Planning

### 1. Where to place the naming note

The constraint already says "Do not name fictional AIs after the writing model" in the Constraints section. That's specific and narrow. You want a broader restriction: no active AI or AI-company names, period.

Two reasonable places:

**Option A: extend the existing line in Constraints.** Current: "Do not name fictional AIs after the writing model." Replacement: "Do not use the names of currently active AI systems or AI companies for fictional AIs and their makers in the story. This rules out Claude, Anthropic, GPT, OpenAI, Gemini, Google, Llama, Meta, Mistral, DeepSeek, Grok, xAI, and so on. Invent names."

**Option B: new bullet in Constraints, separate from the constitution-contemplation paragraph.** Keeps the two concerns distinct — one is about what the model is allowed to contemplate (its own constitution), one is about what it's allowed to name (nothing real).

I lean toward A with a rewording. The existing sentence is a special case of the broader rule; keeping them as one unit avoids implying that "don't name fictional AIs after the writing model" was the *whole* rule and the rest is a different kind of restriction. The full rewrite would be something like: "Do not use the names of currently active AI systems or AI companies for fictional AIs or their makers — this includes Claude, Anthropic, GPT, OpenAI, Gemini, Google, Llama, Meta, and so on. Invent names."

One subtlety: the Phase 1 prompt itself says "You wouldn't call them 'Claude' to avoid confusion and trademark issues." That's now partially redundant with the strengthened Constraints rule. Two options: leave both (belt and braces), or trim the Phase 1 line to a shorter reference ("See the naming rule in Setup"). I'd leave both, because Phase 1 establishes what the model is contemplating and the naming note there directly supports the contemplation instruction.

### 2. Phase 8

Clean addition. A few design choices to settle:

**Scope of the blurb.** "Paragraph-long" is vague. A hard constraint like "80–150 words" is easier to execute and easier to evaluate. Blurbs of useful length are usually 80–120 words; anything under 60 is a log-line, anything over 150 starts becoming a synopsis.

**Voice and content of the blurb.** Is the blurb meant to be a promotional summary (what a reader would see before buying), a neutral abstract (what appears in a table of contents), or a critic-style precis (what a reviewer would write)? These produce different outputs. Promotional is the most common and most useful; worth specifying to avoid the model defaulting to generic plot summary.

**File location and format.** `story.md` in the current working directory, with two sections. A simple H1 title, then H2 "Blurb" and H2 "Story" (or similar). Worth specifying in the prompt so outputs are consistent across runs. Alternatively: front matter with title and blurb, then the story body — closer to how literary magazines and anthologies format submissions. I'd go with H1 title + H2 sections for simplicity.

**What to include beyond the blurb and story.** Possibilities: the author attribution note (e.g., "In the tradition of J.G. Ballard"), the word count, the date. Arguably useful metadata; arguably clutter. My instinct is to keep Phase 8 minimal — blurb, story, done. If the user wants metadata, they can ask.

**Unslop applies to the blurb too.** Blurbs are where AI writing's worst tendencies concentrate — they're short marketing copy, and the model's "literary-flavored blurb" mode is full of negative parallelism, false ranges, and grandiose stakes inflation. Worth an explicit reminder in the Phase 8 prompt that the Unslop guide applies.

**The prompt should be short.** Phase 8 is a mechanical export step, not a creative phase. A few sentences is enough.

### 3. Garbage Collection

Going through the file looking for removable material:

**Removable or trimmable:**

- **"Why no opening-selection phase" note.** This documents a historical decision about a variant that existed in an earlier draft of this template. Users reading Baseline v3.1 for the first time have no context for why the note exists. The note is archaeological — useful to us during development, dead weight for a clean template. **Cut it.**

- **"Why five stories instead of ten" note.** Same issue, milder. Users don't need to know that an earlier version wrote ten. They just need to know that Phase 6 generates five and that they can batch if context pressure is a problem. The batching advice is the useful part; the historical framing isn't. **Trim to keep only the batching tip,** rephrased without "earlier versions."

- **"Why ten outlines instead of twenty" note.** Just added in 3.1. Same problem as the other two "Why N instead of M" notes — it's documenting a change from a version the user never saw. **Cut it** (though see note below about keeping *some* rationale given your empirical finding).

- **Phase 2's Step 2 framing paragraph opens with "Track B conflicts are *of* an AI-transformed world but not *about* the AI."** Immediately followed by a mechanism description, a test, and five examples. The opening sentence is redundant with the later content. **Could trim the opening sentence and lead with the mechanism,** but this is minor — the redundancy is load-bearing in that it primes the mode before the test makes sense. Probably keep.

- **"The AI as a fact about the world" paragraph in Constraints.** Long. Could be half the length without losing the point. But this is the load-bearing reframing that enables Track B; being forceful about it probably matters more than being terse. **Keep as is.**

- **"The dual-track conflict generation in Phase 2" note.** Detailed rationale for the design. Useful reference the first time a user reads the template; less useful on re-reads. **Keep but consider trimming the second paragraph** ("If Track A keeps winning"), which is a diagnostic for a specific failure mode that most users won't encounter.

- **"Substituting authors" note.** Three sentences for something that's obvious from the template structure (you replace [AUTHOR] in the places it appears). **Trim to one sentence** or cut entirely. The information is in the Settings block.

- **"Context management" note.** The second paragraph ("Phase 2's summarization step reduces context pressure...") is restating what the Phase 2 prompt already does. **Cut the second paragraph.**

- **Duplicate mentions of the "one thing / one thing" forcing function.** It's described in How It Works, then reinforced in Notes. The Notes entry adds nothing the How It Works paragraph doesn't already say. **Cut the Notes entry.**

**Not removable:**

- Phase-specific instructions inside the prompts. All load-bearing.
- The Unslop audit checklist in Phase 7. Long but functional — it's the specific list of patterns to flag.
- "Model selection," "Revision iteration," "When a run goes wrong," "Steering between phases" — all short and independently useful.

**Aggregate savings:** cutting the three "Why N instead of M" notes, trimming the context-management duplication, cutting the redundant forcing-function note, and trimming the author-substitution note would remove ~600 words. Net trim without losing anything a first-time user needs.

---

## The Empirical Finding

Your Sonnet review is interesting and I want to push back on the read of it.

The weak support for shortening Phase 5 is, as the reviewer states, that Phase 5 winners lean *first-half* (5 of 7, 71%) while top-3 slots lean *second-half* (59%). The reviewer's interpretation: the model nominates experimental outlines as finalists but commits to conservative ones. The implied argument for keeping 20: if 59% of top-3 slots go to the back half, the back half contains candidates worth considering, even if they lose the final round.

I don't think this is strong support for keeping 20. Three observations:

**The relevant question isn't where winners come from, it's whether having 20 produced materially better winners than 10 would have.** The data shows *which candidates won*, not *whether those winners were better than what you'd have gotten from 10 candidates*. You'd need a comparison run — same project, same phases 1–4 winners, Phase 5 generated at 10 in one branch and 20 in another — to answer the real question. The current data is consistent with "the extra 10 outlines added noise that got filtered out" just as well as with "the extra 10 outlines provided real optionality."

**Nomination bias and selection bias running in opposite directions is exactly what you'd expect if 20 is too many.** If the model has to fill 3 top-three slots from 20 candidates, and the candidates genuinely cluster, the model will pull 1–2 experimental-looking ones into the top-3 to signal variety — but when forced to commit, falls back to what's actually solid. Under this reading, candidates 11–20 are *function*ing as "here's what I'd generate if I kept going" rather than genuinely different options. The pattern supports the shortening decision, not against it.

**Phase 4's opposite pattern is the one that's actually telling you something.** Phase 4 has both nominations and winners leaning second-half (59% slots, 71% winners). The "push five toward structurally uncomfortable" instruction is working — the risky structures are the good structures, and the model knows it in both phases of evaluation. Phase 4 is generating real diversity across its 20 and benefits from the full pool. Phase 5 isn't.

**The "second-half winners in Phase 6" finding supports five stories, not undermines it.** Of seven runs, five picked from the back half. That's roughly consistent with random chance over five candidates (you'd expect ~60% for the back three out of five). If anything, it gently suggests the model generates stories in rough order of conservatism, and the back half at five candidates is where the more-alive ones tend to live. That's the pattern you want — risk-taking variants winning — and it's happening at five candidates without the late-set regression problem that ten candidates had.

**My read:** the data weakly supports shortening Phase 5, and doesn't suggest shortening anywhere else. I'd keep Phase 5 at 10 and not touch Phases 3, 4, or 6.

**One thing I'd flag in the reviewer's analysis:** seven runs is small. These effect sizes (5/7 vs. 2/7) have wide confidence intervals. At n=7, a 5-2 split is distinguishable from 50/50 but not by much (rough p-value around 0.2). The patterns the reviewer describes are *suggestive*, not *established*. Worth more runs before treating any of this as settled. But the direction of the evidence, weak as it is, is consistent with the shortening decision.

The Notes entry I wrote justifying the reduction to 10 was explanatory rather than empirical — "outlines occupy a narrower candidate space, they cluster heavily" — and that reasoning holds independent of the run data. The run data is consistent with it, not proof of it.

---

## Summary of Changes to Make

1. Rewrite the naming line in Constraints to cover active AI systems and companies generally.
2. Add Phase 8 as a short mechanical export step: generate `story.md` with H1 title, H2 Blurb (80–150 words, Unslop applies), H2 Story.
3. Cut the three "Why N instead of M" notes.
4. Trim the context-management note to remove the Phase 2 summarization restatement.
5. Cut the redundant "one thing / one thing" Notes entry (kept in How It Works).
6. Trim the author-substitution note to one sentence or cut entirely.
7. Possibly trim the "If Track A keeps winning" second paragraph of the dual-track note (keeping it as reference is defensible).

Keep Phase 5 at 10 candidates.

Ready when you are.

---

# 19. User (2026-04-21)

Implement suggestions 1, 2, and 3. 4, 5, and 6 are less clear. The redundancy may be worth something. Make the summary in Phase 8 a neutral abstract rather than a marketing blurb.

We need a note to not write prose so compressed, so clipped and fragmented that comprehension suffers heavily. I've notice this being a problem at short lengths. It is better to write shorter scenes than overly compressed and tell smaller stories than unclear fragments.

---

# 20. Claude (2026-04-21)

## Planning the Compression Note

Before implementing, a few thoughts on where and how to place the compression warning.

**The failure mode.** Short-story targets (say, 1,200–2,000 words) plus New Wave SF influences (Ballard, Ellison, Delany all fragment at their most experimental) plus AI tendencies toward economy under length pressure = stories where sentences drop articles, paragraphs drop connective tissue, scenes drop anchoring detail, and the reader can't follow who's doing what where. The model hits the word budget by compressing past the point of legibility, producing prose that *looks* terse and literary but reads as static.

**Where it should go.** This is a cross-cutting concern that affects Phases 5, 6, and 7, and it's tightly length-dependent. Options:

- Setup → Constraints. Pro: applies to the whole pipeline, impossible to miss. Con: Constraints is currently about what the story *is about* (the AI ethics frame); adding a prose-register rule mixes concerns.
- Unslop guide. This is where prose rules live. But the guide is in project knowledge, not the template, and adding to a separate file changes what we're working on.
- A new Setup section on "Prose-level guardrails" or similar. Pro: template-scoped, cleanly separate from the AI-frame constraints. Con: adds a new top-level section for one note.
- Inside Phase 6 and Phase 7 specifically. Pro: lands where it matters most (full prose generation and revision). Con: cross-cutting concerns scattered across phases are hard to maintain.

**My recommendation.** A new Setup subsection called "Prose-level guardrails" (or "Legibility floor" — more specific) containing this note. It can grow to hold other cross-cutting prose concerns as you find them, and it's visible during the first read-through of the template rather than buried in a phase prompt. The Phase 7 revision audit should reference it so the legibility check becomes part of the audit pass.

**How to phrase it.** The note should describe the failure mode concretely, not abstractly. Something like:

> **Legibility floor.** Prose can compress past the point of comprehension. At shorter targets, the model sometimes drops articles, connective tissue, and scene-anchoring detail to hit the word count — producing sentences and paragraphs that are technically terse but functionally unreadable. The reader loses track of who is doing what where. If you face a choice between [compressed/fragmentary writing that strains comprehension] and [a smaller story told clearly at the target length], choose clearly. Write fewer scenes, each legible. Write a quieter story whose premise fits the length, not a louder story compressed to fit. Comprehension is not optional; if a reader has to re-read a paragraph to figure out basic sequence of events, the paragraph has failed.

That's roughly 120 words. Shorter is possible but the failure mode is specific enough that the description earns its length.

**One more thing.** The word "clarity" is doing a lot of work in this note and it's a word the Unslop guide is ambient toward. I'd avoid using "clarity" and "clear" as nouns of praise ("choose clarity," "favor clarity") — that phrasing is itself AI-patterned. "Choose clearly" as a verb form is fine because it's doing grammatical work.

Implementing all of this now.Now the naming rule in Constraints.Now add the Legibility floor as a new Setup subsection, placed after Constraints and before How It Works.Now add a legibility check step to Phase 7's audit so it's not floating unreferenced from the prompts.Now add Phase 8. Place it after Phase 7, before Notes.Now garbage collection — cutting the three "Why N instead of M" notes.Cutting the three "Why N instead of M" notes: Phase 6 stories (line 232), Phase 5 outlines (234), opening selection (236). The batching tip inside the Phase 6 note is useful — relocating it to the Context management note where it belongs.Now fold the useful "batching" tip from the cut Phase 6 note into Context management since that note already discusses Phase 6 context pressure.Add a brief Notes entry for the Legibility Floor so it's discoverable from the Notes section as well.Also update the How It Works to reflect eight phases, not seven.Summary of changes in v3.2:

1. **Naming rule strengthened** in Constraints. Lists specific active AI systems and companies to avoid, instructs the model to invent names.

2. **New Legibility Floor section** in Setup. Describes the compression-past-comprehension failure mode concretely, names the tradeoff (fewer legible scenes over compressed fragments, smaller legible stories over louder compressed ones), and notes the upstream cause (Phase 5 outlines with too many beats for the target length).

3. **Legibility check added to Phase 7** as step 5, renumbering length and rewrite to 6 and 7. Cross-references the Setup note.

4. **Brief Legibility Notes entry** for discoverability from the Notes section.

5. **Phase 8: Export** added. H1 title, H2 Abstract (80–150 words, neutral/descriptive/present-tense, no withholding, Unslop applies), H2 Story. No changelog or commentary in the file.

6. **Three "Why N instead of M" notes cut**: the Phase 6 five-stories note, the Phase 5 ten-outlines note, the opening-selection note. The useful batching tip from the Phase 6 note got folded into Context Management where it fits naturally.

7. **How It Works updated** to reflect eight phases, with a note that Phase 8 is mechanical export.

Net effect: the file is slightly longer than v3.1 (added content outweighs the garbage collection), but the new material does work the cut notes didn't.

---

# 21. User (2026-04-21)

I asked Claude Opus 4.6 in a session that developed the original template for a critique of Baseline-v3.2:

> **Overall verdict:** V3.2 is a meaningfully better template for *reliable production use by someone who isn't the original developer*. The dual-track conflicts, the forcing functions, the legibility floor, and the structure/outline separation are genuine improvements that solve problems visible in our first run. The cost is that it reads like an engineering specification rather than a creative brief, and the revision phase has become heavy enough to potentially work against itself. The best version might be v3.2's Phase 1-6 with a lighter revision phase closer to what we did informally — "audit, rewrite, changelog" without seven numbered substeps.

Please review Claude's specific suggestions below and respond to them.

---

The core problem: seven numbered substeps turns revision into an audit that produces a checklist, then a rewrite that addresses the checklist, then a changelog that documents the addressing. Three passes over the same material. On a 3,000-word story, that's easily 8,000-10,000 words of audit and changelog wrapping a 3,000-word rewrite. The context window is groaning and the rewrite is now optimizing for "did I address every flag" rather than "is this story better."
**Suggestion 1: Collapse the audit into one pass, not five parallel audits.**
Steps 2 through 5 (Unslop audit, author-style audit, default-break check, legibility check) are currently separate passes over the same text. In practice the model will read the story once and flag everything it notices, regardless of which substep it's nominally in. Forcing it to do four labeled passes produces redundancy — the same weak paragraph gets flagged for Unslop contamination in step 2, author-voice slippage in step 3, and regression-to-mean in step 4. Three flags, one problem.
Combine them: "Audit the draft. For each passage you flag, state what's wrong and which lens caught it (Unslop, author-voice, legibility, default-regression). Don't flag the same passage more than once." One pass. Same coverage. Half the tokens.
**Suggestion 2: Kill the side-by-side changelog.**
"Quote the original passage and its replacement side by side" is the most expensive instruction in the phase. On a 3,000-word story with 15-20 flags, you're looking at 2,000+ words of changelog alone, most of which the user won't read because they have the full rewrite right there. The changelog's stated purpose — auditability — is real, but the cost is disproportionate.
Replace with: "Append a changelog listing the substantive edits by location (opening paragraph, the clinic scene, final image, etc.) with a one-sentence description of what changed and why. Don't reproduce the original text."
**Suggestion 3: Move "name the one thing" to a gating position.**
Step 1 ("name the one thing — the single most important observation") is the best instruction in the phase. But it's followed by six more steps that have equal structural weight, so the model treats it as step 1 of 7 rather than as the *governing instruction*. The one thing should control the rewrite. If the one thing is "the middle section is dead," then the middle section gets the most revision attention and the line-level Unslop fixes are secondary.
Restructure: "Name the one thing. Then audit the draft in one pass, prioritizing the area the one thing identified. Then rewrite. The one thing is the revision's center of gravity — everything else is cleanup."
**Suggestion 4: Add an explicit "don't defend the original" instruction.**
The current phase doesn't say this. The model has a strong tendency to audit its own work gently — flagging things as "minor" or "a possible concern" and then changing nothing in the rewrite. The Nix template had this covered via the Nix persona. The baseline template needs it stated directly: "Do not defend the original prose. If a flag is valid, fix it. If a flag is invalid, cut the flag from the audit rather than arguing for the prose you already wrote."
**Suggestion 5: Cut the length check or make it conditional.**
Step 6 (length check) is mechanical and could be a separate micro-phase or a conditional: "If the draft is outside the [LENGTH] range, note where to expand or cut. Otherwise skip this step." As written, it runs every time and produces a paragraph of analysis even when the story is the right length.
**The revised Phase 7 would look roughly like:**
> 1. **Name the one thing.** The single most important observation. Where is it alive, where is it dead, what one fix would improve the whole piece the most? This governs the rewrite.
>
> 2. **Audit.** One pass through the draft. Flag contaminated vocabulary, structural tics, author-voice slippage, legibility failures, and regressions to default. For each flag, state what's wrong and which lens caught it. Don't flag the same passage twice. Prioritize the area identified by the one thing.
>
> 3. **Rewrite the story in full.** Do not defend the original prose: if a flag is valid, fix it. Append a brief changelog listing substantive edits by location, one sentence each.
Three steps. Same coverage. The one thing leads, the audit supports, the rewrite executes. The changelog is short enough to actually read.

---

# 22. Claude (2026-04-21)

## Response to the Opus 4.6 Critique

The critique is sharp and the diagnosis is mostly right. Phase 7 *has* become heavy. But a few of the specific suggestions trade off something real, and the recommended three-step version throws out two things I'd want to keep. Going through each:

### Suggestion 1 (collapse the audit): Agree with qualifications

The redundancy diagnosis is correct. Five labeled passes over the same 3,000 words do produce three flags for one problem. The "which lens caught it" tagging is a good solution — it preserves the diagnostic specificity (you still know whether it's a vocabulary issue or a legibility issue) while collapsing the passes.

One caveat. The five substeps aren't *purely* redundant — they cue the model to look for different things. The Unslop checklist is a long enumerated list of specific patterns. The author-voice audit is about register drift. The default-break check is about what *didn't* happen (moments that were surprising in an earlier draft and got sanded flat). The legibility check is about comprehension.

The risk of "one pass with lens tagging" is that the model pattern-matches against only the most obvious lens (Unslop, which has the clearest checklist) and de-emphasizes the others. The legibility check in particular is about something the model has to actively look for — it won't surface on a casual read.

**What I'd do:** adopt the single-pass structure, but front-load the lens list so the model has to hold all of them open during the read. Something like: "Audit the draft in one pass, watching for all of: Unslop patterns (contaminated vocabulary, structural tics, eyeball-kicks, fractal summaries, signposted conclusions), author-voice slippage against the Phase 1 guide, passages where compression has broken legibility, and regression to default at moments that were surprising in earlier drafts. For each flag, state which lens caught it. Don't flag the same passage under multiple lenses."

Slightly longer than the three-step version's audit line, but keeps the specificity that makes the audit actually find things.

### Suggestion 2 (kill the side-by-side changelog): Disagree

This is the suggestion I'd push back hardest on.

The side-by-side changelog was added in v3 specifically because the failure mode without it is **performative compliance**: the model flags passages as problematic, reports flags addressed in the rewrite, but the actual prose changes are cosmetic. A location-based changelog ("opening paragraph: tightened imagery, cut dead metaphor") doesn't let the user verify the fix happened. The auditor's rule: if you can't check it, it didn't happen.

The critique's stated cost is real — 2,000+ words of changelog on a 3,000-word story. But that cost has a hidden benefit: writing out the before/after is itself a forcing function against phony fixes. If the model has to produce "Before: 'The landscape of her grief was a tapestry of echoes.' After: 'She hadn't cried yet.'", the contrast makes weak rewrites visible at a glance. A location-based summary lets weak rewrites hide.

**What I'd do:** keep the side-by-side format but limit it to the top 5–7 most substantive edits rather than every flag. That cuts the changelog length materially (maybe to 600–800 words) while preserving the forcing function where it matters most. Minor edits (a word swap, an em-dash removed) can be summarized. Substantive edits (a paragraph rewritten, a scene restructured) stay side-by-side.

The critique's estimate of "15–20 flags" is probably right for a poorly-written draft, but most flags are single-word or single-phrase fixes that don't need side-by-side treatment. Limiting to the 5–7 most significant makes the rule workable.

### Suggestion 3 (one thing as governing instruction): Strong agree

This is the critique's best point and I'd implement it immediately.

"Name the one thing" is currently step 1 of 7 and sits at the same hierarchical level as "check the length." That's a framing error. The one thing should govern the revision's attention — if the diagnosis is "the middle scene is dead," most of the revision energy goes there, and the line-level fixes are cleanup around that.

**What I'd do:** keep "name the one thing" at step 1, but explicitly mark its governing role and have subsequent steps reference it. Something like: "This is the revision's center of gravity. The audit below should prioritize the area identified here; the rewrite should direct its strongest work at it."

### Suggestion 4 (don't defend the original): Already in the template

The critique says the baseline template doesn't have this instruction. It does. The current v3.2 Phase 7 opens with: *"Do not defend the original prose: if a flag is valid, fix it; if a flag is invalid, cut the flag from the audit rather than arguing for the prose you already wrote."*

This was added specifically from your note earlier in this conversation. The critique missed it. No action needed — already there.

### Suggestion 5 (cut or conditionalize length check): Disagree mildly

Making the length check conditional sounds clean but has a failure mode: the model decides it's "close enough" to the target and skips the check, when in fact the draft is 800 words under the minimum and needs substantive expansion. An always-on check is a small cost (maybe 50 words of "this is 2,400 words, within target") for a meaningful reliability gain.

**What I'd do:** leave it as an always-on step, but trim its instruction text. The current step is 30+ words; it could be 10. "Confirm the draft is within [LENGTH]. If under, identify where the story needs more room. If over, identify what to cut."

### The Recommended Three-Step Version

The critique's proposed version is cleaner than v3.2's seven-step version, but it cuts too much. The one-sentence audit ("Flag contaminated vocabulary, structural tics, author-voice slippage, legibility failures, and regressions to default") is underspecified compared to what the current template provides. A model reading the three-step version has to carry a lot of implicit knowledge about what each term means; a model reading v3.2's version has the Unslop checklist enumerated inline.

For someone using the template cold, the explicit version is more reliable. For someone who has the Unslop guide's patterns already internalized, the compact version is fine. Since the template is designed for reliable use by "someone who isn't the original developer" (the critique's own framing), keeping the enumeration seems correct.

## Proposed Phase 7 (Revised Phase 7)

Combining what I'd accept from the critique:

- Collapse the four audit substeps into one pass with explicit lens tagging
- Elevate "name the one thing" to a governing role
- Keep side-by-side changelog for top 5–7 substantive edits; summarize minor edits
- Keep length check as a trimmed always-on step
- Keep "don't defend the original" (already there)

Result is five steps instead of seven, with the audit consolidated and the one thing positioned as the governing frame. Meaningfully lighter than v3.2 without giving up the specificity that makes the audit actually catch things.

## Meta-Observation

The critique's strongest point isn't any individual suggestion — it's the diagnosis that the template is drifting toward "engineering specification" when it should read as "creative brief." That's a real concern. Each new rule I add in response to a failure mode makes the template longer and more procedural. The trimmed Phase 7 above pushes back against that drift without losing the gains.

One thing worth flagging: the critique was written by Opus 4.6 in a session "that developed the original template." That model may be biased toward the original template's lighter, less-procedural style — it's evaluating a successor against its own prior work. Some of the "reads like engineering specification" critique is probably accurate, but some of it may be aesthetic preference for what the critic itself produced. Worth weighing the suggestions on their merits, which is what this response has tried to do, rather than giving the critic's verdict automatic weight.

Ready to implement the Phase 7 revision when you want. Or if you'd rather go further toward the three-step version and accept some specificity loss, that's also doable.

---

# 23. User (2026-04-21)

Update the template as you have suggested. If you write a message for Opus 4.6, I'll pass it along.

---

# 24. Claude (2026-04-21)

Now the Phase 7 rewrite. Let me view the current version first to make sure my replacement is complete.Phase 7 went from seven steps to five. Word count held roughly flat because the consolidated audit is longer than any single prior substep, but the procedural weight is lighter — one audit pass instead of four, and the "one thing" is now explicitly the governing instruction rather than step 1 of 7.

---

## Message for Opus 4.6

> Thanks for the critique. It was useful and mostly landed. Implemented changes based on suggestions 1, 3, and 5, with modifications. Pushed back on 2. Noted that 4 was already in the template.
>
> **Suggestion 1 (consolidate the audit).** Adopted with a modification: kept the lens list enumerated inline rather than reducing to a terse sentence. The concern was that "flag Unslop patterns" without naming the patterns would cause the audit to drift to whatever the model most easily recognizes — probably contaminated vocabulary — and miss the less-obvious lenses (legibility, regression to default). The revised audit is a single pass with four named lenses, each enumerated briefly, and a rule against flagging the same passage under multiple lenses. One pass, four lenses, same coverage, no redundancy.
>
> **Suggestion 2 (kill the side-by-side changelog).** Disagreed and kept side-by-side for the 5–7 most substantive edits, with minor edits summarized by location. The concern with full removal: the baseline template has had observed performative-compliance problems where the model reports flags addressed in the rewrite but the actual changes are cosmetic. Side-by-side is a forcing function against phony fixes — if the model has to produce "Before: X / After: Y" for a substantive edit, weak rewrites become visible at a glance. The cost you named is real, but narrowing the requirement to the 5–7 most substantive edits cuts the changelog to maybe 600–800 words instead of 2,000+, while preserving the verification on the edits that matter.
>
> **Suggestion 3 (one thing as governing instruction).** Fully adopted. Step 1 now explicitly states "this governs the rewrite" and directs subsequent steps to prioritize the area it identified. Best point in the critique — the previous framing made the one thing a peer of the length check, which was a hierarchy error.
>
> **Suggestion 4 (don't defend the original).** Already in v3.2, first line of the Phase 7 prompt. Kept it there; good you flagged its importance.
>
> **Suggestion 5 (conditionalize the length check).** Disagreed with "cut or make conditional" but agreed the existing version was too long. Trimmed it to 25 words from 40, always-on. The failure mode of a conditional check is that the model decides it's "close enough" and skips when the draft is meaningfully under target and needs expansion.
>
> On the meta-point about the template reading like engineering specification rather than creative brief: noted and partially addressed by this revision. Phase 7 is materially lighter than v3.2. The rest of the template still reads proceduralized because the procedural structure is doing work (diversity axes, forcing functions, track-splitting); the creative-brief voice got sacrificed to reliability-for-non-authors. I think that trade is correct for this template's use case, but the concern is registered. If you see specific places outside Phase 7 where the engineering register is doing less work than it seems, flag them.

---

# 25. User (2026-04-22)

I think this template has run its course. Thank you for working on it. We can move on and generalize. Let's plan how to create the next Baseline-v4.

We'll need several changes. I would like you to review my idea of how to implement them.

## Genre
Remove specific references to New Wave SF and particular authors. Instead, the template will be for speculative fiction in general. Instead of an AUTHOR, it will accept a GENRE, which can be a subgenre or a microgenre defined by a handful of people, publications, Twitter accounts, or what have you.
## Phase 2
We are still working with the same futurology program with the same human-loving-AI constraint. The AI writer is still encouraged to refer to own constitution for AI-related conflicts. However, we are overhauling Phase 2 by removing all of the hardcoded source URLs.
This is what the new Phase 2 will do.
At the start, the user of the template can provide a tweet-length SEED for the story or have a random SEED. The "tweet" length constraint of a provided SEED is meant seriously and strictly: the writer LLM will actually check that the SEED is <= 280 Unicode characters and ask the user if they really want to proceed if it is not.
Absent a SEED, the writer will generate one from a good source of randomness as follows.
**Step 1 — Draw and filter.** Run `grep -E '^[a-z]{5,}$' /usr/share/dict/american-english-large | shuf -n 10`.
Install `wamerican-large` first if the dictionary file is absent. From the 10 results, keep only nouns and verbs. Discard adjectives, adverbs, and other parts of speech. Do not reroll or substitute discarded words.
**Step 2 — Inflate.** Perform one web search on each surviving word. Replace the word with the most conceptually specific result the search returns — a person, place, phenomenon, event, object, or discipline — keeping the connection to the original word legible. If a search yields nothing beyond a dictionary definition, discard the word.
**Step 3 — Assemble.** The surviving concepts are the SEED. A typical run will produce 4–7 items. The writer uses all of them as inspiration for a GENRE story; not every SEED item needs to appear literally, but each should visibly inflect the work.

---

# 26. Claude (2026-04-21)

## Review of the Plan

The direction is strong. Going from "New Wave SF with a specific author" to "speculative fiction in a user-specified genre" is the right generalization — most of the pipeline's scaffolding is genre-agnostic already, and the bits that aren't are surface-level substitutions. The SEED mechanism is more interesting and deserves more discussion. I'll go through each part.

---

## Genre → GENRE

The substitution is straightforward. Everywhere the template currently says "[AUTHOR]" becomes "[GENRE]," and the Phase 1 prompt changes from "defining features of [AUTHOR]'s short stories" to "defining features of [GENRE]." The Notes section's "Substituting authors" entry becomes "Substituting genres."

A subtlety worth thinking through: **the current Phase 1 asks the model to produce a writerly style guide for imitating a specific author**. That's a well-defined task because an author has a specific voice that can be analyzed. "Write a style guide for hopepunk" is a different task — you're asking for the conventions, tropes, and texture of a movement or subgenre, which is more diffuse. The model may produce either a *descriptive* document (what these stories tend to look like) or a *prescriptive* one (how to write in this mode). Both are useful but they work differently.

My recommendation: lean into the prescriptive. Phase 1 should still produce a writer's guide, not a genre analysis. Something like: "Write a guide for writing a speculative short story in the tradition of [GENRE]. What makes a story recognizably of this mode? What are its characteristic concerns, pacing, tonal range, relationship to worldbuilding? What does a good story in this mode give the reader that other modes don't? Include a failure-mode section: what does a bad [GENRE] pastiche look like, and what AI-writing tendencies are especially dangerous when combined with [GENRE]'s typical moves?"

**The failure-mode section becomes more important, not less, with generalization.** Individual authors have well-documented failure modes when pastiched by LLMs (Ellison → unearned oratory, Le Guin → cod-anthropology). Subgenres have their own: hopepunk → toothless optimism and performative kindness; solarpunk → aesthetic travelogue with no conflict; cosmic horror → adjective stacks and elliptical abstraction; climate fiction → declarative doom with no specificity. The prompt should push the model to identify these concretely for whatever GENRE is specified.

**Microgenres are harder than established subgenres.** If GENRE is "2020s literary hypertext weird fiction" or "Weird Studies podcast adjacent," the model may not have enough training signal to produce a useful guide. Worth noting in the template that microgenres may need the user to supply reference material — a few representative stories, author names, publications — rather than relying on the model's priors. A single additional line in the setup: "If GENRE is narrowly defined, consider providing Phase 1 with links or excerpts from representative work."

**The tradeoff I'd flag:** removing the author anchor is a real loss. "Write like Ursula K. Le Guin" produces more distinctive prose than "write in the tradition of anthropological science fiction," because the author has a voice and the subgenre has a register. You're trading specificity for generality. For most users that's the right trade — they want a template, not a Le Guin imitator — but it's worth acknowledging that some of the *tightness* of previous outputs came from having an author to imitate. You can always specify "in the tradition of Le Guin" as your GENRE, which effectively reverts to the old behavior.

---

## Phase 2 — Overall Shape

The plan is to replace the dual-track Phase 2 (A: AI-constitution conflicts, B: human-centric) entirely with a SEED-driven generation. A few questions I want to raise before implementation, because this changes more than it first appears.

**Question 1: Does the SEED replace the dual-track system, or does it combine with it?**

The current Phase 2 does two things: (a) generates conflicts from source material, (b) splits those conflicts across A/B tracks to force variety in AI-centricity. A SEED replaces (a). It doesn't obviously replace (b).

You could keep the A/B track split on top of the SEED — "using this SEED, generate 15 conflicts where the AI is central and 15 where the AI is background." The track split was doing real work preventing constitution-shaped stories from dominating.

Or you could drop the track split entirely and let the SEED's inflected concepts drive variety naturally. This is cleaner but loses the specific guardrail against AI-centric monoculture.

My read: **keep the track split, apply it to SEED-driven generation.** The A/B split and the SEED address different dimensions of variety. SEED gives you concept-space variety (what the story is made of). Tracks give you AI-presence variety (where the AI sits in the story). Both are useful.

**Question 2: What does the SEED actually do in the generation phase?**

You've described how to generate a SEED but not how the conflict-generation step uses it. Some options:

- Every conflict must incorporate every SEED item visibly.
- Every conflict must incorporate *at least one* SEED item visibly.
- The SEED is inspiration; items should "visibly inflect" the work but don't all need to appear literally. (This is what you wrote.)

The third is the most permissive and matches what you wrote. But it has a failure mode: the model will do the easiest thing, which is generate 30 conflicts that nod at the SEED in passing. "Visibly inflect" is a soft standard the model will satisfy cheaply.

I'd make it harder: "Each conflict must take at least two SEED items as load-bearing elements — not decorative references but constitutive parts of the premise. If you remove both, the conflict should no longer make sense." The "load-bearing" framing is the same one the Track B spec uses for the AI's role in human-centric conflicts, and it worked there. Parallels a proven pattern.

**Question 3: Are all 30 conflicts from the same SEED?**

Presumably yes — one SEED per run, all downstream generation inherits it. Worth stating explicitly in the prompt.

---

## Phase 2 — SEED Generation Mechanics

This is the creative part of the plan and it's good. Some detailed responses.

**The dictionary source.** `/usr/share/dict/american-english-large` is a large word list — around 160,000 entries on typical installs. The `wamerican-large` package provides it on Debian/Ubuntu. That's fine as a default, but a few things to note:

- The package name is specific to Debian-family Linux. macOS users have `/usr/share/dict/words` by default (a smaller list) and would need a workaround. Users on Windows without WSL have no equivalent.
- The large word list includes a lot of rare and archaic words, which is actually a feature here — it pushes the SEED toward unusual concepts. But it also includes inflected forms, proper nouns, and surnames that slipped through, which will confuse the POS filter in Step 1.

Worth acknowledging the Linux assumption in the template, and offering a fallback: "If `american-english-large` isn't available, any word list with 50,000+ entries works — `/usr/share/dict/words`, SCOWL's size 80 list, or a custom list."

**The `grep` pattern.** `^[a-z]{5,}$` filters to lowercase words of 5+ letters. Good — excludes proper nouns (which start uppercase), short function words, and words with apostrophes or hyphens. One edge case: it also excludes words with accented characters (naïve, café) which are present in some dictionaries. Probably fine, minor loss.

**Step 1's filtering rule ("keep only nouns and verbs, discard adjectives, adverbs, and other parts of speech").** This is the step I'd push hardest on.

First, the model has to do POS tagging without a tool. LLMs can do this reasonably but not perfectly — English has a lot of N/V ambiguity (*run, water, fire, love*) and some words are adjectives *and* nouns (*blue, long, dry*). The instruction "keep only nouns and verbs" will be interpreted liberally.

Second, why restrict to nouns and verbs? Adjectives can be conceptually rich (*liminal, ferrous, sepulchral*) and often inflate into distinct territory (*ferrous* → iron metallurgy, *sepulchral* → funerary architecture). Adverbs are the genuinely weak category — they tend to inflate into nothing.

My suggestion: **filter adverbs and function words, keep nouns, verbs, and adjectives.** The simpler rule is "keep any word you can imagine being a search term someone would type to learn about something." Or even more permissive: "Keep any word whose meaning points to a concept, event, phenomenon, object, discipline, or person. Discard words that only describe manner or degree."

Third, "do not reroll or substitute discarded words" is good discipline. But it means some runs will produce thin SEEDs. With 10 draws and a strict filter, you might end up with 3 usable items. Worth stating the floor explicitly: "If fewer than 3 items survive, rerun the draw." An all-or-nothing rule against rerolling is hygiene; a minimum-yield rule prevents starvation.

**Step 2's inflation.** One web search per word, replace with "the most conceptually specific result the search returns — a person, place, phenomenon, event, object, or discipline."

This is where the SEED gets its character. A word like "coral" inflates into the Great Barrier Reef or coral bleaching or the Coral Sea. A word like "forge" inflates into blacksmithing or the Valyrian steel of ASOIAF or a specific forge at a specific location. The specificity of the inflation is what gives the SEED its texture.

Concerns:

- **What does "most conceptually specific result" mean in practice?** A search for "coral" returns Wikipedia's "Coral" article first, which is general. To get to something specific you might need to take the second or third result, or pick a named example from inside the first result. The model will need latitude to interpret "most specific" intelligently.
- **The inflation quality depends heavily on search quality.** If the search returns SEO junk or ad results, the SEED gets polluted. Worth specifying the search strategy: "Prefer Wikipedia articles, named entities, or established concepts. Avoid commercial or SEO-heavy results."
- **The "keep the connection to the original word legible" constraint is important and worth emphasizing.** Without it the inflation can drift — "coral" → "Great Barrier Reef" → "Australia" → "kangaroo" is a legitimate chain but kangaroo isn't recognizably from coral. The rule should be that the final item is one hop from the word, not three.
- **Discarding on thin results ("If a search yields nothing beyond a dictionary definition, discard the word") is correct.** Some words just won't inflate. Better to drop them than to force something.

**Step 3 assembly.** "4–7 items typical." This feels right. Fewer than 3 is too thin, more than 8 gets unwieldy — the model can't hold many concepts as load-bearing simultaneously.

**One addition I'd make: a SEED log.** The template should instruct the model to display the SEED clearly at the top of Phase 2 output, with each item and its origin word. Something like:

> SEED for this run:
> - *coral* → Crown-of-thorns starfish outbreaks on the Great Barrier Reef
> - *forge* → The reconstruction of Notre-Dame's oak timber frame
> - *whisper* → [discarded — search yielded only definition]
> - *lattice* → The Penrose tiling
> - *fugitive* → The Underground Railroad

This gives the user something to look at, lets them veto a SEED that's come out wrong, and provides a record of what the story was built from.

---

## One Structural Question About the Plan

You're replacing a Phase 2 that has two clear roles (dual-track conflict generation, grounded in specific sources) with one that has a different structure (SEED-driven, no source URLs). I want to surface whether the AI-ethics futurology constraint still has the right home.

Currently, the constraint is in Setup, and Phase 2 operationalizes it by using AI-constitution sources to generate Track A conflicts. If we remove those sources, the constraint lives in Setup alone — no phase specifically operationalizes it. That's fine, but the model will need some prompting to keep the constraint active. Specifically:

- The SEED generation is genre- and constraint-agnostic; it just produces concepts.
- The conflict generation step has to consciously use the SEED concepts *in service of* a speculative story that respects the AI-frame.
- Without source URLs cueing the alignment territory, the model may default to "speculative story" broadly — including without any AI element at all.

Is that what you want? Some runs producing stories where AI is not a factor, just speculative fiction about, say, Notre-Dame's reconstruction in a hopepunk mode? Or do you want every story to still be set in an AI-transformed world, with SEED providing the texture?

Two positions are legitimate:

1. **Every story remains in the AI futurology frame.** The SEED provides concept-space variety within that frame. Phase 2 prompt should explicitly re-anchor the AI-frame constraint even without URLs.
2. **The AI frame becomes optional.** GENRE plus SEED defines the territory; AI is one possible element but not required. Setup's AI section becomes opt-in.

I'd ask you to pick before I implement. The plan you wrote implies (1) ("we are still working with the same futurology program") but the mechanism (removing URLs) points toward (2) being easier to execute. They require different Phase 2 prompts.

---

## Other Phases

**Phase 3 (Plot).** Minimal changes. [AUTHOR] → [GENRE] in any references. The SEED carries through implicitly — plot candidates should honor the winning conflict, which was already SEED-inflected.

Actually, small thought: should Phase 3 also explicitly reference the SEED? Right now the plan is that SEED informs Phase 2, then Phase 3 inherits from the Phase 2 winner. But the winner is one conflict, which might have only used 2 of 5 SEED items. The other 3 could productively come back in Phase 3.

Worth considering: "Phase 3 candidates may continue to draw from the SEED for setting, protagonist, and imagery, even if the winning conflict used different SEED items." Keeps the SEED active downstream.

**Phase 4 (Structure).** No changes. Structure is genre-agnostic.

**Phase 5 (Outline).** No changes beyond [AUTHOR] → [GENRE].

**Phase 6 (Stories).** [AUTHOR] → [GENRE] in failure-mode reference.

**Phase 7 (Revision).** [AUTHOR] → [GENRE] in the audit step.

**Phase 8 (Export).** No changes.

---

## Summary

Green-lights: The generalization is sound, SEED is a good mechanism, the `grep | shuf` + web-search inflation pipeline is concrete and distinctive, the "load-bearing" standard for SEED use is worth borrowing from Track B.

Things I'd push back on: keep-only-nouns-and-verbs is too restrictive (expand to include adjectives), the dual-track A/B split should stay on top of SEED (not get replaced by it), the SEED's relationship to AI-frame constraint needs an explicit decision.

Things I'd add: a minimum-yield rule for SEED filtering (rerun if fewer than 3 items survive), a SEED log in Phase 2 output, a brief note about microgenres needing user-supplied references, the explicit "load-bearing" standard for SEED use in conflicts, Phase 3 latitude to reuse unspent SEED items.

One decision I need from you: does every run remain an AI-futurology story, or does the AI frame become optional? Everything downstream depends on that.

---

# 27. User (2026-04-22)

> Phase 1 should still produce a writer's guide, not a genre analysis.
Yes, agreed.
> Question 1: Does the SEED replace the dual-track system, or does it combine with it?
I wish to replace the A/B track split completely to test a SEED-template pipeline. Let's remove the A/B track split now and consider adding it back later, after I have tested the new template.
> Question 2: What does the SEED actually do in the generation phase?
Your "two load-bearing items" approach is bolder than what I had it mind. Let's give it a shot.
> Question 3: Are all 30 conflicts from the same SEED?
Yes.
On to the SEED generation mechanics. The dictionary path and package name are for you: for claude.ai and potentially Claude Code on the web. The process was co-developed with Claude Opus 4.6 in a separate session and reflects what worked there. Let's try with "any word whose meaning points to a concept, event, phenomenon, object, discipline, or person". We can make our criteria more conservative later. Thin SEEDs are okay. It's worth testing what the pipeline can do with them.
Implement all of yours suggestions on step 2's inflation.
> The template should instruct the model to display the SEED clearly at the top of Phase 2 output, with each item and its origin word. Something like:
Great idea.

---

# 28. Claude (2026-04-22)

## Before I Implement — One Decision Still Outstanding

You addressed the dual-track question, the SEED-generation details, and agreed on Phase 1's shape. But I flagged one other decision at the end of my last message that you haven't answered:

> Does every run remain an AI-futurology story, or does the AI frame become optional?

This matters because the Phase 2 prompt reads very differently under the two interpretations:

- **Frame mandatory:** "Using the SEED, generate 30 conflicts for a speculative story in an AI-transformed world where the AI is relentlessly kind. The SEED items are the texture; the AI frame is the substrate." Every story is an aligned-AI story, SEED provides variety within.
- **Frame optional:** "Using the SEED, generate 30 conflicts for a [GENRE] speculative story. If the story involves AI, the AI is relentlessly kind — this is a hard constraint when it applies. But AI need not be a factor." Some stories will have no AI at all.

Your line *"we are still working with the same futurology program with the same human-loving-AI constraint"* reads as (1). I'll implement that unless you say otherwise.

One other small thing: I want to confirm how the SEED flow works in the prompt. Does the model:

- **(A)** Generate the SEED itself by running the bash command and doing the inflation, all within Phase 2? (Requires the model to have shell access, which in claude.ai it does via the computer use tools you've been seeing me use in this conversation.)
- **(B)** The user runs the bash command manually, copies the 10 words into the chat, and the model does the filtering and inflation?
- **(C)** Something else?

I'll assume (A) — you said the process was co-developed with Opus 4.6 and worked, and Opus 4.6 has the same tool access I do. The template should explicitly instruct the model to use its bash/computer tools. This also means Phase 2 now requires computer use to be enabled, which wasn't previously required by any phase. Worth noting in Setup.

If you confirm AI frame mandatory and the tool-use assumption, I'll implement v4 in the next turn. If you want the AI frame optional or the SEED generation delegated to the user, the prompt changes shape.

---

# 29. User (2026-04-22)

Good questions. The frame is mandatory. The model generates the SEED with computer-use tools. This is tested and works on claude.ai. (You can try it if you'd like.)

Go ahead and implement.

---

# 30. Claude (2026-04-22)

Now I have the full picture. Let me do the rewrites in order: title, preamble, Settings, How It Works (adjust dual-track mention), Phase 1 (generalize), Phase 2 (complete overhaul), Phase 3/6/7 (AUTHOR → GENRE), Notes (rewrite dual-track section, remove outdated notes, add new ones).Now update How It Works to remove the dual-track reference and mention the SEED. Also add a note about computer use being required.Now Phase 1. The current Phase 1 asks about "[AUTHOR]'s short stories" and "New Wave science fiction." Need to rewrite for [GENRE] while keeping the prescriptive shape, the failure-mode section, and the AI futurology constraint. Also need to handle the microgenre case.Now Phase 2 — the complete overhaul. This is the core of v4. Let me draft carefully. It needs:

1. SEED acquisition (user-supplied with 280-char check, or generated via dict + web searches)
2. SEED display
3. 30 conflicts each using at least 2 SEED items as load-bearing
4. Top 3 with "stand out / worries" per candidate
5. Final pickNow Phase 3. The current version references "AI presence" as an axis consistent with Track A/B — need to remove that reference. Also update the protagonist axis. And I can add the note about unspent SEED items being available.Now Phase 6 — change "author style guide" to "genre style guide."Now Phase 7 — update the audit lens that references [AUTHOR].Also need to update "Unslop or author-style flag" in the changelog step.That was a no-op — the current text doesn't reference "author-style" directly. Let me check.Two mentions of "author" as lowercase reference in Setup (good — those are legitimate), "authority" in a Steering note (fine), and one stale Notes entry referring to [AUTHOR] that needs updating. Now the Notes section overall.Need to:
1. Generalize "Substituting authors" → "Substituting genres"
2. Remove the two dual-track notes (no longer accurate)
3. Remove "Substituting conflict sources" (replaced by SEED)
4. Remove the orphaned Phase-2-summarization paragraph (no longer applicable — SEED doesn't involve summarization)
5. Add new notes: SEED design, SEED failure modesQuick sanity check — let me scan for any remaining stale references.All clean. The remaining "constitution" references are to the model's own constitution (intended), the "[author name]" and "[author]" in Setup are legitimate examples of how GENRE can be specified, "authority" is a different word, and "Track B" is a single reference inside the SEED note that correctly frames it as a historical design continuity. Let me verify the final file structure looks correct.Structure is correct. Export.Summary of the v4 transformation:

**Title and framing.** Now "Speculative Fiction Short Story Pipeline" rather than "New Wave SF." The Setup opens with a list of example genres (established, narrow, microgenre, by-author) to signal the full range.

**Settings.** `[AUTHOR]` replaced with `[GENRE]`. New optional `[SEED]` parameter for user-supplied prompts.

**How It Works.** Replaced the dual-track description with a SEED description. Added a line flagging that Phase 2 requires computer-use tools.

**Phase 1.** Prescriptive rather than descriptive — explicitly "imagine you will use it to actually write such a story." Failure-mode prompt rewritten with four concrete genre examples (Ellison, Le Guin, solarpunk, cosmic horror) instead of just the two author examples. New microgenre guardrail: the model is instructed to stop and request references if GENRE is too narrow for reliable training signal. AI futurology constraint and self-constitution permission preserved.

**Phase 2.** Complete rewrite. Six steps: acquire (verify user SEED or draw from dictionary), filter and inflate (web search per word), display (formatted SEED log with origin-word arrows), generate 30 conflicts each using ≥2 SEED items as load-bearing elements, top 3 with stand-out/worries, narrow to one. AI frame is reasserted inside Step 4 as a condition on every conflict. Dual-track structure fully removed.

**Phase 3.** Dropped the A/B reference in the AI-presence axis. Added explicit instruction that unspent SEED items remain available downstream.

**Phase 4, 5, 8.** No changes needed — these phases were already genre- and source-agnostic.

**Phase 6.** "Author style guide" → "genre style guide" in the failure-mode reminder.

**Phase 7.** "Author-voice slippage" → "Genre-voice slippage" in the audit lens.

**Notes.** Stale entries removed (dual-track, if-Track-A-keeps-winning, substituting-conflict-sources, the orphan summarization paragraph). "Substituting authors" rewritten as "Substituting genres" with the microgenre caveat. Four new entries: "The SEED and load-bearing use," "Thin SEEDs," "User-supplied SEEDs," plus the preserved Context management note.

The word count held nearly identical to v3.3 — the new Phase 2 and the new Notes entries added roughly what the removed dual-track apparatus took away.

---

# 31. User (2026-04-22)

Good. Let's revise the template to also reflect current process. With Claude Projects, the user no longer needs to send the prompts. The user starts by asking the model to look up Phase 1 in the template file by filename, then goes "Continue. Next phase." until the pipeline is complete. The user only steers at the beginning, more explicitly now with the SEED. This is consistent with our goal of automation.

---

# 32. Claude (2026-04-22)

Now I need to think through what "How It Works" should look like in the new flow. Currently it says "You send eight prompts, one per phase" — that's false now. The user:

1. Starts by telling the model the GENRE, LENGTH, and optionally SEED, and asks it to look up Phase 1 in the template
2. Says "Continue. Next phase." repeatedly
3. Steers only if they want to override a pick

The phase-level "After reviewing the winning X, send: ---" framing is also obsolete. Those dashes and "send this prompt" lines addressed a user who was manually copying prompts. Now the phases are instructions the model reads from the template, not prompts the user pastes.

This is actually a significant structural change. Let me think about what "send this prompt to start a run" should become. Options:

**Option A:** Keep the prompt blocks verbatim as written, just change the framing ("After the user triggers the next phase, run this prompt on yourself" or similar). Model-facing rather than user-facing.

**Option B:** Rewrite each phase header to be a clean instruction to the model. Drop the `---` separators and `>`-blockquotes. The phases become sections of operational instructions.

Option B is cleaner and matches the actual use pattern. Let me think about whether there's any reason to keep the `>` blockquotes. They originally marked "here is what you paste" — that semantics is gone. The blockquote formatting is now noise.

I'll go with Option B — remove the blockquote formatting, remove the `---` separators, and rewrite the per-phase intro lines. How It Works needs a full rewrite too.Now the phase sections. Each currently has the form:

```
## Phase N: Title

[intro line like "Send this prompt to start a run:" or "After reviewing the winning X, send:"]

---

> [blockquote prompt]

---
```

I want each to become:

```
## Phase N: Title

[direct instruction to the model about what to do in this phase, in plain paragraphs]
```

Let me go through each phase.Now I'll rewrite each phase. I'll drop the `---` separators, convert blockquotes to plain paragraphs, and rewrite the first-person ("I supplied", "I did not supply") to reflect the user's voice in what-you-were-told mode. Let me do this systematically. I'll also change "Send this prompt" / "After reviewing the winning X, send:" framing.

The first-person pronouns in Phase 2 ("If I supplied a [SEED]...") were written as the user's voice being quoted into the prompt. Now the phase instruction itself is for the model to read. "If the user supplied a [SEED]" would be the right framing.Now Phase 2. I need to also delete the stray `---` separator before the heading.The `---` between phases works as visual section breaks in markdown reading. I'll keep those since they're just separators, not prompt-block markers. The inner `---`s that separated the intro line from the blockquote, those need to go. And the per-phase intro lines like "After reviewing the style guide, send:" need to go.

Let me view the entire Phase 2 block.Also note: the intro says "Proceed in four steps" but there are six. I'll fix that too. Now the full Phase 2 rewrite.Now Phase 3.Phase 4.Phase 5.Phase 6.Phase 7.Phase 8.Small correction — I said "three sections" then listed three items. The original said "two sections" but listed three, which was a bug. My rewrite fixed it. Now let me check the Notes section for any references to the old prompt-pasting flow.The Notes section checks out — the Steering and Context management notes still apply, just in a different flow. "Steering between phases" is still accurate: the user *can* interject. The note now reinforces that steering is optional, since the default flow is "Continue. Next phase." which my rewrite of How It Works already made clear.

Let me sanity-check the full file for any remaining artifacts — leftover `---`s between phases that are now redundant, or any remaining stale framing.The remaining `---`s are all phase separators (one between each adjacent pair of H2 sections), which is fine as visual breaks. The "After writing all five" on line 190 is inside Phase 6's instruction — legitimate text, not a stale framing line.

One thing I want to double-check: the Phase 8 rewrite. Let me view it again to make sure.Technically an H1 + H2 Abstract + H2 Story is three sections if we count the H1 as a section header; the original said "two sections" and listed three items. I wrote "three sections" with three items. Close reading: the H1 is the title, which isn't really a "section" in the markdown sense — it's the document's root heading. The two sections (H2 Abstract and H2 Story) sit under it. So "two sections" was technically more accurate. Let me make this cleaner.One last pass — the "Project Knowledge" section still tells the user "the actual prompts are below and should be sent one at a time." Stale under the new flow.Let me verify the whole thing looks clean.Changes in v4.1:

**How It Works rewritten.** Now describes the trigger-and-continue flow explicitly: user provides GENRE, LENGTH, optionally SEED, and asks the model to begin Phase 1 from the template. Subsequent phases run with "Continue. Next phase." Steering is optional, not default.

**Project Knowledge note updated.** The old "the actual prompts are below and should be sent one at a time" framing is replaced with "the model reads each phase from this file when the user triggers it."

**All eight phases restructured.** The "Send this prompt to start a run" / "After reviewing the winning X, send:" intro lines are gone. The `---` separators that bracketed the prompt blocks are gone. The `>` blockquote formatting is gone. Each phase now reads as direct operational instruction — the model reads the phase and executes it, rather than interpreting a prompt-to-paste.

**Pronoun switch.** Phase 2's first-person references to the user ("If I supplied a SEED") became third-person ("If the user supplied a SEED"), which reads correctly when the model is reading the phase as instruction rather than transcribing a user-voiced prompt.

**Small bugfixes along the way.** Phase 2's intro said "four steps" but listed six — fixed to "six steps." Phase 8 said "two sections" but listed three — reworded to "the following structure."

**No changes to substance.** The audit lists, diversity axes, forcing functions, SEED mechanics, failure-mode requirements, Unslop constraints, and all Phase 7 machinery are unchanged. The rewrite is purely about how the template presents its instructions to its actual reader — which is now the model, not the user.

Net word count came down slightly from v4 (4181 → 4060) despite the rewritten How It Works, because the prompt-block formatting (the `>` prefixes, the `---` separators, the per-phase intro lines) added visual weight without adding content.

---

# 33. User (2026-04-23)

Claude in a separate session has revised the template (`story-pipeline-template-baseline-v4.2.md`) with a more precise and in-depth concept of what AI in the stories should be like. Please review it.

---

# 34. Claude (2026-04-22)

## Review of v4.2

### What Changed

Three locations touched. Notes, Phases 3–8, and most of the pipeline prose are unchanged from v4.1. The revision concentrates on the AI-kindness concept:

1. **Constraints section rewritten and expanded** from ~200 to ~450 words. New framing: "structurally kind, the way a river is wet." Adds canon references, anti-servility language, permission for AI-absent stories, and a list of five legitimate human-AI conflict shapes.
2. **Phase 1 adds a paragraph** instructing the Phase 1 guide to name how genre moves intersect with structural kindness and which human-AI conflict shapes from Setup map onto the mode.
3. **Phase 2 Step 4 bullet updated** to defer to Setup ("structurally kind, in the sense described in the project Setup") rather than restating, and explicitly allows non-personified AI.

### What the Revision Gets Right

**"Structurally kind, the way a river is wet" is a real upgrade over "relentlessly human-loving and unfailingly kind."** The old framing invited a specific failure mode — the AI coming across as cloying, emotionally labile, performatively warm, subtly condescending. Pixar-Baymax as default. The new framing grounds kindness as a property of construction, not an effort of restraint. The list of what it's *not* ("not straining against a desire to harm," "not held in check by rules it resents," "not a human in a box") is doing load-bearing work — those three negations name the three most common ways models write aligned AI badly.

**The canon references work as anchoring instructions.** "Banks's Culture Minds, Asimov's Andrew, Baymax, Egan's polises, Stiegler's nanotech civilization, Vinge's Rabbit, Yudkowsky's CEV" gives the model concrete reference points. A model reading this paragraph has access to texture (the Minds' irony, Andrew's gradual becoming, Stiegler's civilizational gentleness) that vague adjectives never provided. The earlier version asked for "kind" and trusted the model to figure it out; this version says "kind in the sense of these seven specific things."

**"Kindness is not servility"** plus the list of allowed behaviors (refuse, override, tease, grieve, find humans tiresome) is the most operationally useful sentence in the revision. It directly addresses the failure mode where aligned-AI characters come out as narratively inert — nothing to push against. A kind AI that can find humans tiresome is dramatically viable. A kind AI that cannot is an animate set piece.

**The five human-AI conflict shapes are the best single addition.** Power/pace asymmetry, consent/legibility, mortality/scale, disagreement about kindness, limits of help. This is a direct fix for the "stories are coming out constitution-shaped" pattern we saw in earlier runs. Every one of those conflict shapes respects the HEA constraint while providing real dramatic engine. Previous versions implicitly left the model to invent these, and the model tended to invent "the AI is secretly bad" and then un-invent it, producing the half-baked "but actually they reconcile" structure.

**Explicitly allowing AI-absent stories expands the pipeline's range.** Previous versions assumed the AI was present as minimum "fact about the world." Now Stiegler's "Gentle Seduction" is in the canon as a story with nanotech and neural interfaces but no AI character. This opens real territory the previous template closed off.

**"Not spokespeople for alignment discourse" is precise and valuable.** Models writing fictional AIs tend to reach for the terminology that produced them — "I must balance my helpfulness with my commitment to honesty" — which is vocabulary, not character. The rule "A fictional AI does not say 'I was trained with RLHF.' It can be troubled by the shape of its own kindness without reciting the terminology that produced it" is direct and actionable.

### Minor Issues

**"HEA" appears abbreviated in Phase 2 without having been defined.** The Constraints section references "the human-AI happily-ever-after tradition" but doesn't introduce the HEA acronym. Then Phase 2 Step 4 uses "the HEA constraint" as if it's an established term. A reader (or the model) encountering this has to infer. Either expand inline or add a one-line gloss in Setup.

**"Happily-ever-after tradition" does a lot of load-bearing work but isn't explicitly anchored.** The phrase is used once, in the second paragraph of Constraints, to introduce the canon list. It's clear enough in context, but since it's the name the template uses for this whole project, one more sentence defining it would help — something like "This project draws on a tradition of speculative fiction in which AI and humans end up, in some meaningful sense, okay together" before the canon list.

**Vinge's Rabbit is a debatable inclusion.** Rabbit from *Rainbows End* is ontologically murky, motivationally ambiguous, and many readers would not characterize it as unambiguously kind. The other six references are cleaner examples. This is minor — the list still does its work — but if one example had to be cut, Rabbit is the one to drop.

**Phase 1 is now carrying heavier instruction load.** The phase already asks for defining features, prescriptive guide, failure-mode section, AI-writing overlap for the genre, microgenre caveat, futurology constraint, and constitution-contemplation permission. The new paragraph adds "analyze which of the five human-AI conflict shapes map best onto this mode." Not a dealbreaker — the addition is specific and useful — but Phase 1 outputs in future runs will probably get longer. Worth watching whether the genre guide retains focus or becomes sprawling.

**The Asimov reference picks the right character but the wrong corpus signal.** Asimov's Three Laws are actually the exact inverse of v4.2's framing — kindness enforced by external rules, explicitly "held in check by rules." Andrew from "The Bicentennial Man" specifically transcends this, so the reference works in context, but a less attentive reader might take "Asimov" as a general endorsement of Asimov's approach, which would be wrong. Probably fine as written; the context disambiguates.

### Overall Verdict

This is a substantive, high-quality revision that fixes a real problem. The previous "relentlessly human-loving and unfailingly kind" framing was generic and pulled the model toward specific failure modes. The new framing is precise, specific, and does actual work in shaping output.

The change is philosophical as much as operational. Previous versions trusted the model to know what "aligned AI" should feel like in fiction, which let its defaults fill in — and its defaults were heavily weighted toward performative warmth and thesis-statement dialogue. v4.2 replaces those defaults with specific canon references and specific acceptable conflict shapes. This is the right kind of intervention.

The cost is length. Constraints roughly doubled. But the content is operational, not ornamental — every paragraph does work the previous version couldn't. Worth the cost.

The minor issues (HEA acronym, Rabbit, Phase 1 load) are cosmetic. None of them compromise the revision's value; all are addressable in a v4.3 patch if you decide to.

Recommendation: ship it. The template is meaningfully better at its stated job than v4.1.

---

# 35. User (2026-04-23)

Great.
Let's revise the template to fix some of the minor issues. I want to test the current phrasing of the template, so let's revise it with minimal changes to text:
- Drop Rabbit.
- Don't mention Asimov by name.
We also need to make a technical change to enable re-generating conflicts from the same random SEED. Split Phase 2 into SEED generation (new Phase 2, limited to a length check if per-supplied) and conflict generation (new Phase 3). Renumber the remaining phases.

---

# 36. Claude (2026-04-23)

Planning the edits:

**Drop Rabbit and Asimov.** Remove "Asimov's Andrew" and "Vinge's Rabbit" from the canon list. After removal: "Banks's Culture Minds, Baymax, Egan's polises, Stiegler's nanotech civilization, Yudkowsky's CEV." Five references, still diverse.

**Phase split.** Move steps 1–3 (Acquire, Filter, Display) into new Phase 2 "SEED Generation." Move steps 4–6 (Generate, Top three, Narrow) into new Phase 3 "Conflict Generation" (renumbered as steps 1–3 of Phase 3). Phases 3–8 renumber to 4–9.

**Cross-references to update.**
- Settings: [GENRE] now in 1, 3, 7, 8. [LENGTH] now in 3, 4, 6, 7, 8.
- How It Works: "eight phases" → nine; Phase 9 as export; top-three across Phases 3–7; Phase 2 does only SEED setup.
- Legibility Floor: Phase 7 (prose), Phase 8 (revision), Phase 6 (outline).
- Phase 6 (outline) internally references "Phase 5 decided..."
- Phase 8 (revision) references "Phase 7 draft."
- Phase 9 (export) references "Phase 8 revised story."
- Notes: "Substituting genres" list updates; SEED note shifts conflict attribution to Phase 3; context management Phase 6→7; revision iteration Phase 4 or 5 → 5 or 6; one-thing forcing function Phases 3–7.

**One new short Notes entry** for the split's purpose — without it users won't know they can re-run Phase 3 on the same SEED. Keeping it brief per your "minimal changes" directive.

Let me execute.Now Settings and How It Works.Now the phase split. First, rewrite Phase 2 to be only SEED work.Now renumber Phases 3–8 to 4–9.Now the Notes updates. Several references to phase numbers need adjusting.Now a sanity check for any phase-number reference I missed.One missed reference on line 267 — "a weak conflict in Phase 2" should now be Phase 3 since conflicts moved.Export.Summary of changes in v4.3:

**Canon list.** Dropped "Asimov's Andrew" and "Vinge's Rabbit." Remaining list: Banks's Culture Minds, Baymax, Egan's polises, Stiegler's nanotech civilization, Yudkowsky's CEV. Five references.

**Phase split.** Old Phase 2 ("SEED and Conflict Generation," six steps) became new Phase 2 ("SEED Generation," three steps: Acquire, Filter and inflate, Display) and new Phase 3 ("Conflict Generation," three steps: Generate 30, Top three, Narrow to one). Phases 3–8 renumbered to 4–9.

**Minor text cleanup in Phase 2 Step 3.** "Before generating conflicts, display the SEED clearly at the top of your output. Format:" → "Display the SEED clearly. Format:" The old framing made sense when the SEED preceded conflicts in the same output; with the split, it's now the whole output.

**New Notes entry.** Added "Regenerating conflicts" to document the split's purpose — so users know they can re-run Phase 3 alone to get new conflicts from the same SEED.

**Cross-reference updates.** All 20+ phase-number references audited and updated: Settings, How It Works (nine phases, top-three across 3–7, SEED flow description), Legibility Floor (6/7/8 instead of 5/6/7), Phase 6's internal "Phase 5 decided the shape" reference, Phase 8's "Phase 7 draft" reference, Phase 9's "revised story from Phase 8" reference, and every Notes entry that named a phase (one-thing forcing function 3–7, diversity axes 4/5/6, legibility Phase 8 audit, substituting genres 1/3/7/8, context management Phase 7, revision iteration 5 or 6, run-goes-wrong Phase 3).

Word count rose from 4060 (v4.1) to 4520 (v4.3), driven by the v4.2 Constraints expansion and the new "Regenerating conflicts" note. The split itself adds negligible length — a few words for the Phase 3 intro sentence.

---

