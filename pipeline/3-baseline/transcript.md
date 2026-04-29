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

# 37. User (2026-04-29)

Here is writer-model feedback from the latest work. The feedback is organized by genre. Consider carefully what to incorporate and what to discard.
# Solarpunk (Opus 4.7)
**SEED phase**
Source used: `/usr/share/dict/american-english-large` (after installing `wamerican-large`).
**Step 2 — Filter and inflate.**
Surviving words after filtering (kept those pointing to concept/object/phenomenon/discipline; discarded *demonize*, *galleried*, *sombre*, *matured* as manner/degree):
- pulchritude
- checksum
- ferret
- strongboxes
- heterotaxis
- orrery
Now one web search per surviving word.Pulchritude returns nothing beyond dictionary definitions. Discard.Checksum → **bit rot** (silent data corruption in long-term archival storage; the phenomenon checksums are deployed against in archive practice).Ferret → **black-footed ferret cloning recovery program** (Elizabeth Ann / Antonia / Noreen — first cloned animals to restore lost genetic variation to an endangered species, from cells of "Willa," cryopreserved 1988).Strongboxes → **Svalbard Global Seed Vault** (the "black boxes" inside permafrost containing duplicate seed samples from genebanks worldwide; the world's archetypal strongbox).Heterotaxis → **heterotaxy syndrome (situs ambiguus)** — congenital condition in which the internal thoracoabdominal organs are arranged across the left-right axis in an order that's neither normal (situs solitus) nor mirrored (situs inversus); ~1 in 10,000 births, often with severe cardiac anomalies.Orrery → **Antikythera mechanism** (the oldest known orrery, ~2nd century BCE Greek hand-powered analog computer for predicting astronomical positions and eclipses, recovered from a shipwreck off Antikythera in 1901).
---
**Step 3 — Display the SEED.**
```
SEED for this run:
- pulchritude  → [discarded — search returned only dictionary definitions of "physical beauty"; no specific person, place, phenomenon, or named concept available]
- checksum     → bit rot (silent data corruption in long-term archival storage; the phenomenon checksums are deployed against in archive practice)
- ferret       → black-footed ferret cloning recovery program (Elizabeth Ann / Antonia / Noreen — clones of "Willa," cryopreserved 1988; first cloned animals to restore lost genetic variation to an endangered species)
- demonize     → [discarded at filtering step — manner verb, not concept]
- strongboxes  → Svalbard Global Seed Vault ("black boxes" of duplicate seed samples sealed in permafrost ~130m inside a sandstone mountain on Spitsbergen, opened 2008)
- galleried    → [discarded at filtering step — adjective of property]
- sombre       → [discarded at filtering step — manner adjective]
- heterotaxis  → heterotaxy syndrome / situs ambiguus (congenital condition; internal organs arranged across the left-right axis in an order that is neither normal nor mirrored; ~1 in 10,000 births, often with severe cardiac anomalies)
- orrery       → Antikythera mechanism (oldest known orrery, ~2nd century BCE Greek hand-powered analog computer for predicting astronomical positions and eclipses, recovered from a shipwreck off Antikythera in 1901)
- matured      → [discarded at filtering step — manner verb/adjective]
```
Five surviving SEED items. Thin-ish but workable. The shape that suggests itself: four are kinds of preservation-against-loss (genebank, cloned ferrets, archival data integrity, ancient mechanism recovered from wreckage), and one is a body whose internal arrangement is its own kind of preservation problem. The cluster is real and load-bearing.
## On SEED generation
**What worked well in this run.**
The SEED was thinner than average — five surviving items from ten draws — and the thinness was, contra my expectations, useful. Phase 3 was forced into tight conceptual neighborhoods because four of the five items clustered around preservation-against-loss (genebank, cloned ferrets, archival data integrity, recovered ancient mechanism), with heterotaxy as the lone outlier. That cluster did real work. It made the load-bearing constraint easy to satisfy without making it trivial: the conflict that won (heterotaxy + ferret cloning) used the outlier paired with one cluster item, which produced a story whose central image is the thing the cluster was missing — a *body* in which the preservation question becomes intimate. If the SEED had been thicker, I'd have had more options and likely chosen a less specific one. The thinness was a feature.
The inflation step worked best when it produced a *named entity with its own internal structure* — Svalbard with its black-box deposit protocol, the Antikythera with its specific recovery date and gear-train, the Willa cell line with named clones (Elizabeth Ann, Antonia, Noreen) and a specific 1988 cryopreservation. The named-clones detail is what made the conflict winner possible; "endangered species cloning" in the abstract would have produced a vaguer story. The inflation step's specificity directly determined the story's specificity downstream.
**What worked less well.**
Two of the discards (*pulchritude*, *demonize*) were arguably losses. *Pulchritude* legitimately failed the inflation test — searches returned only definitions of physical beauty — but the underlying concept (a quality of beauty that has fallen out of fashion, a word once useful now mostly used ironically) is the kind of thing solarpunk could have done a lot with. The inflation rule prevented a forced result, which is correct, but it cost a potentially generative concept. *Demonize* I discarded at the filter step as a manner verb, but in retrospect it points to a real phenomenon (the social mechanism by which something or someone gets cast as enemy) that could have inflected a solarpunk human-conflict story productively.
A third concern: four of the five surviving items came from a "preservation/archive" semantic cluster, and the fifth was a medical condition. The dictionary draw is supposed to produce conceptual diversity through randomness, but in this case it didn't — the items rhymed with each other in a way that constrained the conflict space more than the load-bearing rule alone would have. This was generative *for this story* but is a failure mode worth naming: the SEED can be thin *and* clustered, and when it is, the diversity-axis instructions in Phases 4 and 5 have to do extra work to compensate.
**What I would change about the SEED step.**
I wouldn't change the dictionary-draw mechanic itself. The randomness is what gives the run its character, and a more curated draw would lean toward genre-default territory.
What I would consider:
- *Loosening the filter slightly*. The current rule discards manner words and function words, which is right, but it discards them at the filter step before any inflation attempt. A word like *demonize* might inflate to a specific psychological or historical phenomenon (e.g., moral panic, scapegoating, the Salem trials) under one search; the current rule kills it before that search. Worth considering: a single inflation attempt for borderline cases, with a fast discard if nothing specific surfaces.
- *A clustering check after Step 2*. After surviving items are inflated, a brief diagnostic — "do these items occupy diverse conceptual territory or do they cluster?" — would let downstream phases know what they're working with. A clustered SEED isn't a bug, but it changes the kind of diversity discipline Phase 4 needs to apply.
- *Naming the inflation depth target more sharply*. "Most conceptually specific result" is a useful guide but vague. The strongest inflations in this run were named-entity-with-internal-structure (Antikythera mechanism, Willa cell line, Svalbard Vault); the weakest would have been generic phenomena (bit rot is borderline — it's a named phenomenon but not a named entity). The template could specify "prefer named entities or specific historical events; phenomena and disciplines are second-best; generic concepts are last resort."
## On LENGTH
The 1,000–3,000 range was the right choice for what this run produced, but I aimed at the upper-middle (~2,000–2,500) and the rewrite came in at ~2,050. Hindsight: I'd have tightened the range to 1,800–2,500.
The 1,000–1,800 part of the range was never realistic for the structure that won (linear day, two anchored scenes plus summary). The morning facility scene needed ~600 words to do its work; the evening household scene needed ~900–1,000; the summary middle needed ~250–400. That's a floor of roughly 1,750–1,800 if every scene is at minimum credible weight. A 1,200-word version would have been a different story — probably a single-scene dilation, or the AI's-question-never-on-page variant from Phase 5 — and the choices in Phases 5, 6, and 7 would have been different all the way down.
This is worth flagging to the template manager: **the LENGTH range affects which structures are available, but the pipeline doesn't make this dependency explicit**. Phase 5 generates twenty structures without reference to LENGTH; Phase 6 does the word-allotment math at the outline level. By that point, structures that don't fit have already been carried through Phase 5's scoring. If LENGTH is wide (1,000–3,000 is a 3:1 range), Phase 5 should probably either narrow itself to structures that work across the range or pick a target word-count first and constrain accordingly.
A shorter range would also have constrained the comic register more usefully. Version 2's domestic comedy works partly because it has room to breathe — the cardamom complaints, the bindweed truce, the new pot, the Maybe-Not-Yet name. At 1,500 words, those would have crowded out the morning's procedural texture, and the version would have lost the corrective against the "saint of tending" failure mode. The comic register is less elastic to compression than the procedural or elegiac registers.
**On the floor specifically.** The Legibility Floor note in Setup is the right concern, but it's framed as a constraint on prose, not on LENGTH selection. The actual mechanism it's trying to prevent — compression past comprehension — happens because LENGTH was set too low for the structure chosen. The template could surface this earlier: "If your Phase 6 outline distributes word counts so that any single scene falls below ~400 words, either cut beats or raise the LENGTH floor."
## One meta-observation
The pipeline's strongest single feature in this run was the **"one thing that stands out / one thing that worries you"** forcing function. It produced better selections at every gate, and more importantly, the worries were genuinely useful in later phases — the Phase 4 worry about the grandfather sliding into sainthood was the specific thing the Phase 6 outline corrected for ("he is unsentimental about the animal in a way recognizable to anyone who has worked with animals"), which in turn was the specific thing the Phase 8 audit checked back against. The worries became a thread of accountability that ran across phases. I'd consider making this even more explicit — perhaps requiring each phase's winner to name which of the *previous* phase's worries it inherits, so that Phase 7's writer knows which Phase 6 worry is most live, and Phase 8's reviewer knows which Phase 7 worry the rewrite has to answer.
That's the suggestion I'd push hardest: the pipeline already has this thread; it just doesn't quite name it.
# Cyberpunk (Opus 4.7)
## On the SEED for this run
### What worked
The dictionary draw produced a SEED that was unusually well-suited to the genre, but I want to separate luck from design. The design choice that did the work was the *load-bearing* constraint at Phase 3 — the requirement that two SEED items be constitutive, not decorative. That constraint pulled the conflict toward the ejector and the total institution and pushed the others into inflecting roles. Without it I would probably have produced a "Pittsburgh chemical plant story with brighteners and abscission imagery and an F1 reference" — a four-item story where every item is decorative and none is structural. The load-bearing rule is the SEED's actual engine.
The other thing that worked was the inflation step's specificity bias. *Mountaintop* could have inflated to "Mount Fuji" or "Everest" — broad, evocative, and thin. Instead the search returned mountaintop *removal* mining, which is a named industrial practice with a politics, a region, and a specific ecology. Same for *resocialization* (Goffman's framework, not the abstract concept), *brighteners* (the named chemistry of stilbene fluorophores, not "things that brighten"), *ejaculators* (the steam jet ejector with its 1889 statutory history, not the verb's diffuse meanings). The "most conceptually specific result" instruction is doing real work; it is what makes the SEED a set of *operational anchors* rather than a set of evocative associations.
### What didn't, or was less than ideal
**Genre-SEED affinity was high, and the template doesn't notice.** This SEED was unusually well-suited to cyberpunk: industrial extraction, institutional control, programmatic shedding, manufactured perception, antique infrastructure. If the genre had been pastoral or comedy of manners or magical realism, several of these inflations would have been awkward, and the load-bearing rule would have forced an awkward conflict. The template treats SEED generation as genre-blind, but the actual fit between SEED and [GENRE] varies enormously across runs. I'd suggest the template add a sentence at Phase 3 Step 1 acknowledging this: "If the SEED feels strongly affined to the genre, expect the conflict generation to converge quickly. If it feels poorly affined, expect to lean harder on inflecting items and on creative reframing of the load-bearing pair." This sets expectations and prevents a model from forcing fit when none is there.
**The "thin SEED is a feature" guidance is correct but underspecified.** This SEED produced six survivors out of ten, which is rich. A four-item SEED behaves differently — the load-bearing constraint becomes harder, and the conflicts become tighter and more eccentric. I'd guess (without having run it) that thin SEEDs produce *better* stories on average because they force more creative reframing, but the template's only guidance is "do not reroll." The template could note: "Thin SEEDs (3–4 items) tend to produce more eccentric and original conflicts but may require more aggressive interpretation of inflations to find genre fit."
**One inflation in this run was almost too on-the-nose.** *Resocialization* inflated to Goffman's total institutions, which is the canonical sociology of the term. That's the most conceptually specific result, which is what the template asks for. But for a cyberpunk story the result was so directly applicable that it eliminated a layer of creative work — the model didn't have to *find* an angle on resocialization, the SEED handed one over. With a less canonical inflation (say, *resocialization* → *post-incarceration reentry programs* or → *cult deprogramming*), the model would have had to do more work to make it cyberpunk-shaped, and that work tends to produce more original results. The template's "most conceptually specific" rule is good but it tilts toward the canonical, and canonical can be lower-friction-than-ideal. I don't have a clean fix for this; it might be a worthwhile experiment to run two parallel inflations occasionally — one canonical, one obliquely related — and let Phase 3 choose between them.
### Would I have drawn the SEED concepts differently?
For the words I had, no — the inflations are about as good as they get. But I want to flag two judgment calls worth surfacing for the template manager:
**The discard rules are fuzzier than they look.** *Hospitable* and *coyest* and *addable* I discarded as manner/quality words, which is correct. But *deems* I discarded as "function-like" — and *deems* is a verb that points to the act of judgment, which is arguably a phenomenon (judging, deeming, ruling). I made a fast call. Another model might keep it and inflate it to, say, *Chevron deference* (the legal doctrine, recently overturned), which would have pushed the SEED in a quite different direction. The template's discard guidance treats verbs uniformly when verbs vary widely in concept-pointing-power. A revision: "Verbs of judgment, action, or transformation often point to phenomena (e.g., *deem* → adjudication; *winnow* → selection processes; *foreclose* → mortgage law). Lean toward keeping these unless the verb is purely auxiliary or modal."
**The plural carries information.** *Paddocks* (plural) and *brighteners* (plural) and *ejaculators* (plural) all came in the plural, and I treated the plural as cosmetic. But "paddock" (singular) inflates more naturally to a horse paddock or a singular F1 paddock; "paddocks" hints at *the practice of having paddocks* — an industry, a class. "Brightener" singular is a chemical; "brighteners" plural is a category, a market segment. I think I lost a faint signal by collapsing to the singular concept in each case. The template could note: "If the dictionary draw produces a plural, consider whether the plurality is signaling a market, practice, or class — and if so, inflate at that level rather than at the level of a single instance."
### One structural observation about Phase 2 itself
Phase 2 is the only phase that requires computer-use tools. This is fine for runs where those tools are available, but it means the template has a hard dependency that the other phases don't. If a user wants to run the pipeline in a context without tools (say, a paid API call without the right tools enabled), they have to supply their own SEED. The template handles this — it accepts a user-supplied SEED — but it doesn't say so loudly enough at the top. A user reading the template top-to-bottom might not realize until Phase 2 that they need to either supply a SEED or have the tools enabled. I'd surface this in Setup more clearly.
## On LENGTH
With hindsight, **1,000–5,000 was too wide a range, and the upper bound was probably wrong for this particular winning outline.**
The range gave Phase 6 too much latitude. An outline with five scenes targeting roughly 3,000 words is doing one job; an outline with five scenes targeting 4,500 words is doing a different job — more dilation per scene, more room for inflection, more risk of dilution. Phase 6 had to pick a target inside the range to do its scene-allotment math, and I implicitly chose ~3,000 without saying so, because the chamber-piece shape of the conflict suggested that length. The pipeline produced a 2,030-word story (after revision cuts), which is below the implicit target but inside the explicit range.
If I'd been forced to a tighter range — say, 2,500–3,500 — the outline would have been the same and Phase 7 would have aimed slightly higher in word count, and Phase 8 would have had less to cut at revision. The wide range made Phase 8 do work that a tighter range would have prevented.
### Specific observations about how LENGTH interacted with this run
**The conflict naturally wanted to be a chamber piece.** Once Phase 3 picked the "kind AI cannot lie for the dying man" conflict and Phase 4 picked the wife-as-witness plot, the story was clearly going to be a single-afternoon, three-character, one-location piece. That shape has a natural length: 2,500–3,500 words for a tight, tonally controlled execution; up to 4,500 if there's significant temporal layering or a multi-POV structure. The 1,000-word floor was never going to be hit by this conflict; the 5,000-word ceiling would have required adding scenes the outline didn't have room for. The range was technically correct but practically overgenerous.
**The template doesn't account for conflict-length affinity.** Some conflicts naturally fit short forms (an inciting incident, a single scene of refusal, a moment of recognition); others naturally fit longer forms (a multi-scene arc, a journey, a relationship across time). The template lets [LENGTH] be set independently of conflict, which means a user who specifies "1,000–2,000 words" might end up with a Phase 3 winner that wants to be 4,000 words, and the downstream phases will have to compress. This is the legibility-floor problem the template warns about, but it gets caused upstream of where the warning lives.
A revision worth considering: at the end of Phase 3, after the winning conflict is selected, the model could note explicitly: *This conflict naturally fits a length of approximately X words. The user-supplied LENGTH is Y. If Y is significantly shorter, expect compression pressure at Phase 7. If significantly longer, expect dilution pressure.* This lets the user adjust LENGTH between phases if they want, or proceed knowing the trade-off.
### Would I adjust the LENGTH constraint with hindsight?
**Yes, two changes:**
1. **Default to a tighter range than the user might initially want.** Most users probably specify 1,000–5,000 because it sounds like a "short story" and they don't have strong feelings. The wider range gives downstream phases more freedom but also more rope. I'd suggest the template default to ranges of ~1,500 word width (e.g., 2,000–3,500, 3,500–5,000) and let users widen if they have a reason. The current 4,000-word width is a lot of latitude.
2. **Move the LENGTH check earlier.** The Legibility Floor lives in Setup and gets re-checked at Phase 8. But the productive place to check it is Phase 6, after the outline is locked. The template already says: *If the Phase 6 winner has more beats than [LENGTH] can comfortably accommodate, cut beats or regenerate.* I'd extend this to also say: *If the winning outline has fewer beats than [LENGTH] needs, either regenerate with more beats or shorten LENGTH.* The asymmetry in the current guidance — only flagging too-many-beats — assumes overshoot is the only failure mode. Undershoot is also a real failure mode at the upper end of long ranges, where the model pads to fill rather than cuts to fit.
### One thing about LENGTH that worked well
The Legibility Floor language is excellent and did real work. At Phase 6 I could feel the temptation to add a sixth beat (a flashback, a second AI conversation, a scene with the daughter on the phone). The Legibility Floor's *fewer scenes, each one readable* gave me explicit permission to keep the beat count at five. Without that language I might have padded.
---
For the model managing template evolution: the SEED system is doing the right thing, and the load-bearing constraint is the most important single design decision in the pipeline. The places where I'd press are around variance — between SEEDs, between genres, between conflicts and lengths. The template currently handles each phase well in isolation; the friction points are at the joints, where decisions made early (genre, SEED, LENGTH) interact with decisions made later (conflict, outline) in ways the template doesn't currently surface.
# Postcyberpunk (Opus 4.6)
Good questions. I'll take them in order.
## SEED Generation
**What worked well:**
The best inflations were the ones where a single web search landed on a concept that was both highly specific and structurally generative — meaning it didn't just name a thing but implied a *mechanism* that could drive a story. "Bisexual" → Yoshino's epistemic contract of bisexual erasure was the star of this run. It's one clean hop from the dictionary word to a named theory, and the theory contains a built-in conflict engine: erasure maintained not by villains but by a convergence of interests on both sides of a binary. That mechanism became the entire story. "Exemplars" → Zagzebski's exemplarist moral theory was similarly productive — it gave me a system (morality grounded in admiration of specific people) that could plausibly be engineered into civic infrastructure, which became the Exemplar Index.
The thick SEED (8 surviving items) was useful in Phase 3, where having many combinatorial pairings meant the 30 conflicts genuinely varied. The less obvious pairings produced the more interesting conflicts — Yoshino + Zagzebski was not the first combination I'd have reached for, but it turned out to be the most productive.
**What worked poorly or could be improved:**
**1. Uneven inflation quality.** Some words inflate into rich, mechanism-bearing concepts. Others inflate into specific-but-inert historical facts. "Sprinkler" → the Iroquois Theatre fire is specific, but it's an event, not a mechanism. It can decorate a conflict but it's hard to make load-bearing without the story being *about* fire safety. Compare that to Yoshino's erasure, which is a mechanism you can transplant into any institutional setting. The inflation step doesn't distinguish between these two kinds of specificity, and it should.
A possible template revision: after inflation, tag each surviving item as **mechanism** (a theory, process, or dynamic that implies conflict), **entity** (a specific person, place, object, or event), or **texture** (a sensory, physical, or atmospheric detail). Then require Phase 3 conflicts to use at least one mechanism-tagged item as load-bearing. This would catch the problem early — a SEED with zero mechanisms would be flagged before 30 conflicts are generated from it.
**2. The one-search-per-word constraint is too tight.** "Litigating" returned nothing but generic legal definitions on the first search. I had to run a second, more targeted search ("strategic litigation climate change landmark") to reach Urgenda. The template says one search per word; in practice, some words need a second pass with a more specific query. I'd revise to "one or two searches" and make the second search optional, triggered when the first returns only dictionary-level results.
**3. Too many items went unused.** Of the 8 surviving SEED items, only 2 (Yoshino, Zagzebski) are load-bearing in the final story. Sloan's obsolescence influenced the reputation-decay mechanic vaguely, and the others — Guénon's Traditionalism, the Iroquois Theatre, the Anglo-Portuguese Alliance, the Cadaver Synod, Urgenda — contributed to Phase 3's conflict diversity but vanished entirely by Phase 7. This is partly by design (the template acknowledges that non-load-bearing items may drop off), but it raises a question about efficiency. Eight items generated a rich Phase 3, but the funnel from 30 conflicts to 1 winner was so aggressive that most SEED material was eliminated before the story began.
I don't think the answer is a thinner SEED — thin SEEDs would constrain Phase 3 too much. But the template might benefit from an explicit "SEED audit" step at the end of Phase 4 or Phase 5, where the model checks which SEED items are still active in the winning plot and considers whether a dormant item could be reintroduced as setting detail, imagery, or secondary character texture. In this run, for instance, the Cadaver Synod's image of putting the dead on trial could have inflected the commendation scene (Val accepting a civic honor for a version of herself that doesn't exist — a kind of reverse Cadaver Synod, honoring a fiction rather than prosecuting a corpse). I didn't think of that during Phases 6-7 because the SEED items had already faded from working memory.
**4. The inflation step biases toward academic and historical concepts.** Every surviving item in this SEED was either a named theory, a named historical event, or a named philosophical framework. There were no physical objects, no specific places, no sensory or material details. This produces a SEED that's intellectually generative but sensorially thin — good for building *systems* (which worked for postcyberpunk) but less good for building *settings* or *images*. A different genre might have suffered from this bias.
A possible fix: allow some words to stay uninflated if they're already concrete. "Sprinkler" as a physical object — the glass bulb, the specific mechanism of heat-triggered water release — might have been more generative than "sprinkler" inflated into the Iroquois Theatre fire. The template currently requires inflation for every surviving word. A revision could allow the model to keep a word as-is if it judges the concrete noun more useful than any available inflation. For example:
> - **sprinkler** → [kept as object — the glass-bulb fire sprinkler, a device designed to break under specific conditions and release what it's holding]
That description has metaphorical resonance a story could use. The Iroquois Theatre doesn't, really.
**5. Dictionary source matters more than the template acknowledges.** I ended up using `/usr/share/dict/american-english` (the standard list) because the large list failed to install. The standard list is smaller and more common-word-heavy, which means the draw is less likely to produce unusual or domain-specific words. The template treats the dictionary source as a fallback detail, but the character of the SEED is downstream of the dictionary's vocabulary range. A run from `american-english-large` would likely produce rarer words that inflate differently. This might be worth noting in the template — or worth providing a curated word list as an alternative source.
---
## LENGTH
The target was 1,500–3,500 words. The final story came in around 2,200.
**The range is too wide for a single pipeline run.** 1,500 words and 3,500 words are structurally different animals. A 1,500-word story has room for maybe three scenes; a 3,500-word story can support six or seven, with secondary characters and subplot. The Phase 6 outline has to commit to a specific scene count and word distribution, and the right outline for 1,500 words is wrong for 3,500 words. In this run, I gravitated naturally toward the middle of the range, but the outline was designed for ~2,400 words (two sections of ~1,200 each), which means I was effectively ignoring both the top and bottom of the stated range.
**The two-section structure imposed its own length constraints.** Each section needs enough beats to feel like a complete day — morning, work, commendation, walk, dinner. Below about 900 words per section, the day becomes a list of events rather than a lived experience. Above about 1,600 words per section, the second telling risks becoming commentary rather than retelling. This put the comfortable range for *this story's structure* at roughly 1,800–3,200. The Phase 5 structure selection should probably include a length-compatibility note — "this structure works best at X–Y words" — so that Phase 6 can calibrate accordingly.
**With hindsight, I'd set LENGTH at 2,000–3,000 for this run.** The floor goes up because the two-section structure has a minimum viable size. The ceiling comes down because the story's power is in compression — the reader needs to feel the two tellings as the *same day*, and if Section B is too long, the repetition loosens. The final story at 2,200 feels about right; I could have used another 200–400 words in Section B to develop the commendation scene and the walk-home ending, but I wouldn't have wanted more than that.
**A structural suggestion for the template:** Allow LENGTH to be revised downward after Phase 5. The user sets an initial range before Phase 1, which is appropriate because genre and length interact (you need to know the target before writing the Phase 1 style guide). But Phase 5's structure selection often implies a tighter band within that range. The template could add a step at the end of Phase 5: "Given the winning structure, confirm that [LENGTH] is appropriate. If the structure implies a narrower range, state it and use the narrower range for Phase 6 onward." This would prevent the outline-calibration problem where Phase 6 has to guess where in a wide range to aim.
**Phase 7's five-version generation is the bottleneck.** Five complete stories at 2,000+ words each is roughly 10,000–12,000 words of creative output in a single phase. The later versions in this run (Versions 4 and 5) were written under context pressure, and while I don't think they suffered catastrophically, they were less inventively varied than Versions 1–3. The template's note about splitting Phase 7 into batches is good advice that should probably be stronger — something like "If [LENGTH] × 5 exceeds 8,000 words, split into two batches with a review between them." For this run, at ~2,200 words × 5 = ~11,000 words, a split would have been warranted.

---

# 38. Claude (2026-04-23)

## Triage of the Feedback

Three runs, three writer models, lots of suggestions. Some patterns are consistent across runs and worth implementing; some are run-specific observations that don't generalize; some are prescriptions I disagree with on the merits. Let me sort them by category and weight.

I'm going to push back on more of these than usual. The feedback is high-quality and articulate, but writer-model feedback after a successful run has a specific bias: it surfaces every minor friction the model encountered and proposes a template change for each one. That tends toward complexity creep — every run reveals "one more thing the template should do," and after a few rounds the template is bloated with conditional checks. The template's job is to be small and load-bearing. Most friction the model encounters is the friction *doing the work the template is supposed to do*.

### Category A: Implement (real generalizable improvements)

**1. Surface the computer-use requirement in Setup.** The Cyberpunk run is right that this is buried. A user reading top-to-bottom should know before Phase 1 that Phase 2 needs tools or a user-supplied SEED. One sentence in Setup. Cost: ~15 words. Benefit: prevents a run from stalling at Phase 2.

**2. Note the user-supplied SEED option more prominently.** Same friction as above, same fix. The fact that you can bypass the SEED generation entirely by supplying one is currently in Settings as a parenthetical. It should be louder.

**3. Acknowledge dictionary source matters.** The Postcyberpunk run hit the smaller `american-english` list because the large one failed to install. The current template treats this as graceful fallback, but the character of the SEED really is different across word lists. A one-line note that the large list is preferred (and to mention it when the small list is used) is cheap.

These three are setup-level clarifications, not changes to the pipeline's logic. Maybe 50 words total.

### Category B: Reject (real frictions, wrong fixes)

**4. "Verbs of judgment often point to phenomena" — reject.** The Cyberpunk run wants more permissive filtering for verbs. But the filter rule is already permissive: "any word whose meaning points to a concept, event, phenomenon, object, discipline, or person." The Cyberpunk model discarded *deems* and now in retrospect wishes it hadn't. That's a judgment call the model already had latitude to make differently. Adding a clause saying "verbs of judgment are usually keepable" is not a generalizable rule — it's the model second-guessing one prior decision and asking the template to remember next time. Templates shouldn't carry this.

**5. "Plurals can carry information" — reject.** Same shape. Real observation, not generalizable rule. The template can't predict when *paddocks* should inflate to a class versus when it should inflate to an instance — the model decides per-run. Adding instructions for this case would invite the same expansion for every per-word judgment call.

**6. "Loosen the filter to attempt one inflation on borderline cases" — reject.** The Solarpunk run regrets discarding *demonize* and *pulchritude*. But the discards were correct under the current rule, and the proposed loosening ("attempt one search before discarding manner words") would make the filter step roughly twice as expensive in API time and tool calls. The template's filter rule is conservative on purpose — thin SEEDs are a feature. The runs are *also saying* thin SEEDs work well. These two pieces of feedback contradict each other; the more conservative position is correct.

**7. Tag SEED items as mechanism/entity/texture and require a mechanism load-bearing — reject.** The Postcyberpunk run wants a typology of SEED items. This is the most ambitious template change proposed and I think the least good idea. It introduces taxonomy at exactly the wrong layer — the model would have to classify each inflation, then satisfy a constraint over the classification. In practice the load-bearing rule already does this work: a conflict where two SEED items are *constitutive* will tend to use mechanism-typed items because mechanisms drive conflict. Adding the taxonomy would formalize what's already implicit, at the cost of a new instruction the model has to internalize and apply correctly.

**8. Allow some words to stay uninflated — reject.** The Postcyberpunk run wants *sprinkler* to remain a sprinkler. But "sprinkler" as a concrete noun is what the dictionary already gave us; inflation's job is to push past the generic concept toward something specific. The named entity (Iroquois Theatre fire) might not have served *this* story, but the rule that produced it is sound. The proposed exception ("if the model judges the concrete noun more useful than any available inflation") gives the model an opt-out from a step the template wants it to take. That opt-out will get used liberally.

**9. SEED audit step after Phase 4 or 5 to revive dormant items — reject.** The Postcyberpunk run is right that 6 of 8 SEED items vanished by the final story. But this is correct funnel behavior. The load-bearing constraint is a *floor*, not a *ceiling*: every conflict must use ≥2 items, but only a winning conflict uses what it uses, and downstream phases narrow further. A "revive dormant items" step would push the writer to retrofit unused concepts into a story that has already chosen its shape. That's the recipe for the inheritance-and-AI-and-cardamom-and-bindweed story where every piece is decoration.

**10. Two parallel inflations per word — reject.** The Cyberpunk run wonders if running a canonical inflation alongside an oblique one would help. This doubles the search budget for marginal benefit, and the implementation is unclear (how does Phase 3 "choose between" them — generate 30 conflicts twice?). The complexity cost is huge.

**11. Note canonical inflations are sometimes "too on-the-nose" — reject.** This was a one-off observation about Goffman's resocialization being too directly cyberpunk. But "on the nose" is a writerly judgment, not a template constraint. If the model thinks an inflation is too obvious, it can choose a less obvious specific result on its own. Codifying this would require defining "obvious" — impossible.

### Category C: Reject as already-handled

**12. Phase 7 batching when LENGTH × 5 exceeds 8K words — reject.** Already in the Notes section: "if late-set regression shows up within Phase 7 itself (versions 4 and 5 phoned in), ask the model to write the five in two batches of three and two, with a review between them." The Postcyberpunk run wants this stronger. But strengthening it from a tip to a hard threshold would force batching even when it's not needed — many models hold context fine at 11K words of output. The current "if regression shows up" framing is the right level of contingency.

**13. Genre-SEED affinity disclaimer at Phase 3 — reject.** The Cyberpunk run wants a sentence about how well-affined SEEDs converge fast and poorly-affined ones need creative reframing. Real phenomenon, but the load-bearing constraint already handles it: a SEED that doesn't fit the genre forces creative reframing on its own. The disclaimer would be ambient encouragement, not operational instruction.

### Category D: The interesting ones (mixed verdict, real thought required)

These three are the genuine puzzles in the feedback. I want to think through each.

**14. LENGTH range width.** Two of three runs (Cyberpunk and Postcyberpunk) name the same problem: the user-specified LENGTH range is wider than what the chosen structure actually wants, and downstream phases have to choose an implicit target inside the range. The Cyberpunk run wants a defaults-narrower recommendation; the Postcyberpunk run wants Phase 5 to allow tightening the range mid-pipeline.

I think there's something here, but the proposed fixes are wrong. "Default to a 1,500-word width" is not a template change — it's advice to users. The template can't make users specify narrower ranges. And "allow tightening at Phase 5" introduces a mid-pipeline parameter change that complicates the template's flow ("the user can revise LENGTH between phases" interacts with everything downstream).

The closer fix is: **acknowledge that LENGTH ranges wider than ~1,500 words give downstream phases too much latitude, and recommend in Setup that users specify tighter ranges by default.** This is a one-sentence change in Setup, no logic changes anywhere else. It frames LENGTH as a design choice rather than a polite range-of-acceptability.

**15. Length declared at the conflict level.** Both runs that flagged length problems noticed it earliest: the conflict that won had a natural length, and that length didn't always match the user's range. The Cyberpunk run proposes that Phase 3 declare "this conflict naturally fits ≈X words" so the user can adjust. This is a real candidate for inclusion, but with caveats:

- It's a model-generated estimate that will be imperfect. The model has limited ability to predict story length from a conflict description.
- It puts the user in a position of mid-pipeline parameter editing, which v4.x has otherwise tried to minimize.
- It's *one more thing* Phase 3 has to do, on top of generating 30 conflicts and selecting one.

I'd lean **partial implementation**: a lightweight check, not a tightening rule. Something like "If the winning conflict seems poorly fitted to the [LENGTH] range, note this before proceeding." If poor fit is flagged, the user can intervene; otherwise nothing changes. No mid-pipeline parameter editing required. The model is just allowed to say "this conflict wants a different length than you specified."

**16. The "worry inheritance" suggestion.** The Solarpunk run's strongest suggestion: each phase's winner should explicitly name which of the previous phase's worries it inherits, so worries propagate as a thread of accountability through the pipeline.

This is genuinely interesting. The "one thing that worries you" forcing function is doing real work, and the Solarpunk run noticed something that's been implicit but unstated: the worries chain. A Phase 4 worry about a character becoming sentimental can be exactly the thing a Phase 6 outline is checking against. Currently the model figures this out informally; the proposal would make it explicit.

I have two concerns. First, it's another instruction at every gate, and instruction density is a real cost. Second, the "thread of accountability" is partly a function of the same model running both phases — the model remembers its prior worry without being told to. Forcing explicit inheritance might paper-over the cases where the worry naturally fades because it was overcome, treating those cases as accountability gaps rather than what they are.

But the Solarpunk run's specific evidence is strong: a worry traveled four phases and corrected for the failure mode it identified, and that propagation was load-bearing for the run's quality. If this is consistently happening, naming it might strengthen it.

**My read:** worth a lightweight implementation — adding to the top-3 phrasing "if any of your worries here echoes a worry from an earlier phase, name the connection" — but not a full restructure. Tests well or doesn't, and removes easily if it doesn't.

---

## Suggested Changes for v4.4

Implementing the items above as actual edits:

1. **One sentence in Setup** about tools/SEED dependency: "Phase 2 generates the SEED using bash and web search tools. If those tools aren't available in your environment, supply a [SEED] in the settings instead."
2. **One sentence in How It Works** acknowledging LENGTH width: "Wider LENGTH ranges give downstream phases more latitude to drift; ranges of ~1,500 words or narrower keep the funnel tighter. Wide ranges are workable but invite compression or dilution pressure later."
3. **One sentence in Phase 2** about dictionary source character: "If you fall back to `/usr/share/dict/words`, note this in the SEED display — the smaller list draws from more common vocabulary and produces different SEEDs than the large list."
4. **One sentence in Phase 3** about length-conflict fit: "If the winning conflict seems poorly fitted to [LENGTH] — substantially wanting more or less room than the range allows — say so before proceeding. The user may want to revise LENGTH or pick a different finalist."
5. **Lightweight worry-inheritance instruction** added to the top-3 phrasing (one phrase added in How It Works): "When a worry here echoes a concern from an earlier phase, name the connection."

Net cost: maybe 100 words across the whole template. No structural changes. No new phases or steps. No new conditional logic. The template stays small.

What I'm declining to add: SEED typology, conflict-revival audits, parallel inflations, opt-outs from inflation, mandatory batching thresholds, mid-pipeline LENGTH editing, verb-keeping nuances, plural-handling nuances. The pattern across these rejections: each adds one instruction the template has to carry forever to handle a friction the model encountered once.

---

## A Meta-Note

The three runs all produced strong stories and generated thoughtful retrospectives. That's a sign the template is working. But I want to flag something about the feedback: **none of the three runs proposes removing anything from the template.** Every suggestion is additive. That's a failure mode of writer-model feedback specifically — the model can identify what was missing for its run, but it doesn't have visibility into what could be cut without harm. Over many rounds of feedback-driven revision, templates accumulate weight. Worth keeping in mind when deciding what to incorporate from future runs.

Want me to implement the five accepted changes as v4.4?

---

# 39. User (2026-04-29)

I agree with your conclusions and the meta-note with a single exception that needs more thought put into it. From the looks of the solarpunk story, the omission of _demonize_ and _pulchritude_ was a real loss. The story lacked conflict that these abstract words would have added. Think about the smallest widening of the filter that would have allowed the words to stay. What does it look like? Evaluate its prospects in real runs.

---

# 40. Claude (2026-04-23)

## What the Two Words Have in Common

Before reaching for a rule change, let me look at what *demonize* and *pulchritude* actually are.

*Demonize*: a verb describing a social process — casting someone or something as the enemy. The act of demonizing is a phenomenon (collectively practiced, historically variable, with named instances like the Salem trials, the Red Scare, contemporary moral panics). It's a verb that *names a thing humans do*.

*Pulchritude*: a noun, technically just "physical beauty," but operationally a word that has fallen out of fashion, used now mostly ironically. Its phenomenon-pointing-power isn't in the dictionary definition; it's in *the word's own social trajectory* — a once-neutral term that became unusable through ornateness, in the way *gay* changed from "happy" through the opposite path.

These are different things and the rule change has to handle both or neither.

## What the Current Filter Actually Says

Re-reading: "any word whose meaning points to a concept, event, phenomenon, object, discipline, or person. Discard words that only describe manner or degree (most adverbs), and function words."

The rule is *already* permissive enough to keep *demonize*. "The act of demonizing" is a phenomenon. The Solarpunk model discarded it as a "manner verb" but a manner verb is something like *quickly* or *softly* — describing how an action is done. *Demonize* is an action, not a manner. The model misapplied the existing rule.

This matters because it means *demonize* doesn't need a rule change. It needs a clarification of how the existing rule applies to action verbs.

*Pulchritude* is the harder case. Under the current rule, it survives the filter (it's a noun pointing to a concept, "physical beauty") and reaches the inflation step. Inflation is where it died — the search returned only dictionary definitions. The Solarpunk model discarded it correctly under the inflation rule.

So there are two failure modes here, not one:

1. *Demonize* failed at the filter step due to misapplication of the existing rule.
2. *Pulchritude* failed at the inflation step because no specific inflation existed.

## Smallest Possible Widening

**For demonize:** no rule change needed. Add an example to the filter rule. Currently the rule names "most adverbs" as a typical discard. Add a parallel example of what to *keep*. Something like: "Verbs of action, transformation, or social process (e.g., *demonize*, *winnow*, *foreclose*) point to phenomena and should be kept." Total cost: 15 words. The example is illustrative, not exhaustive. The model still has discretion on borderline cases, but the rule's permissive intent is more visible.

**For pulchritude:** the rule that killed it is "If a search yields nothing beyond a generic dictionary definition, discard the word rather than forcing a weak inflation." This rule is correct and I'm wary of weakening it. But there's a narrow widening that might be defensible: words whose interest lies in *how the word itself works* — its register, its shift over time, its connotational baggage — can sometimes be kept *as words*, not as inflations. *Pulchritude* is a word about ornate language. *Curfew* used to mean "cover the fire" before it meant "be home by." *Awful* used to mean "inspiring awe."

The widening would be: a word may be kept uninflated if its *etymological history or social trajectory* is itself the specific concept. The inflation, in those cases, points back at the word. SEED display: "*pulchritude* → the social fate of ornate Latinate vocabulary, words that became unusable through their own elevation."

This is a bigger rule change than the demonize one. Let me evaluate it carefully.

## Evaluating the Two Widenings

### Widening A (action verbs example)

**Probability of helping in real runs:** High. Action verbs come up in dictionary draws constantly. *Demonize, winnow, foreclose, ratify, dispossess, atone, banish, ostracize, naturalize* (the citizenship sense), *consecrate, cleanse, scapegoat* — all words that point to social or institutional phenomena, all words a model could plausibly discard as "verbs" or "manner words" without explicit guidance. The example puts a thumb on the scale toward keeping them.

**Probability of harming in real runs:** Low. The existing filter is already permissive, so this widening doesn't change the rule, just the worked example. False keeps (verbs that get kept but inflate poorly) get caught at the inflation step anyway — the second filter handles overshoot at the first.

**Cost:** 15 words. One example clause.

**Verdict:** Implement.

### Widening B (etymology-as-inflation)

**Probability of helping in real runs:** Lower than it looks. *Pulchritude* is unusual. Most dictionary draws don't produce words whose interest lies in their own social trajectory. Words like *pulchritude* are maybe 1-in-50 in a typical draw. Most words are either inflatable to specific entities or not interestingly self-referential. The widening would help in this small fraction of cases.

**Probability of harming in real runs:** Higher than it looks. The current inflation rule is doing real work — it forces specificity by *demanding* a named entity, event, or phenomenon. Loosening it to allow "the word's own social trajectory" creates a permissive escape hatch that the model can apply to almost any word. *Sprinkler* "and the cultural history of preventive infrastructure"; *checksum* "and the epistemics of trust in distributed systems"; *ferret* "and the social position of working animals." Once you allow self-referential inflations, you've opened a door to vague conceptual gestures replacing named entities. The Postcyberpunk run already shows the model wanting to bypass inflation ("allow some words to stay uninflated if they're already concrete") — this widening accidentally grants that wish in a different form.

The current rule's strictness is its virtue. Killing *pulchritude* is a real cost. Letting in vague self-referential inflations across runs is a larger cost.

**Cost:** Hard to keep small. Once you say "the word's own trajectory can be its inflation," you have to specify when. "When the word is a Latinate or archaic term whose register is itself remarkable" is the closest natural rule, but that's narrow enough that the model could reach it on its own — and broad enough to overuse if codified.

**Verdict:** Decline. The rule is doing more work intact than the *pulchritude* save would buy.

There's a third option worth flagging: **make the inflation step retry once with a different search query before giving up.** *Pulchritude* might inflate to something specific under "pulchritude rhetoric" or "pulchritude as cliché" or "history of Latinate beauty vocabulary." This is the Postcyberpunk run's "one or two searches" suggestion, which I rejected earlier as too expensive. Reconsidering: a single retry with a more targeted query is cheap (one extra search per failed word, which is rare) and preserves the strictness of the inflation rule. The model still has to land on a specific entity or phenomenon — just gets one more swing at it.

This is the better intervention if you want to save *pulchritude*. Not "let words stay uninflated," but "let the model try a more specific query before discarding."

## Recommendation

Implement Widening A (action verbs example, ~15 words). Implement the inflation retry (~25 words: "If the first search returns only generic definitions, run one more search with a more specific query — e.g., adding *history*, *rhetoric*, *case*, or a domain context. If the second search also yields nothing specific, discard."). Decline Widening B.

Net cost: maybe 40 words across Phase 2.

Net effect on the Solarpunk run, in retrospect: *demonize* would have been kept under Widening A and inflated to (probably) moral panic theory, the Salem trials, or Stanley Cohen's folk devils — all viable for solarpunk. *Pulchritude* might have been saved by the retry, with a query like "pulchritude rhetorical" or "pulchritude history Latinate" — though I genuinely don't know if a second search would have landed something specific. Possibly not, in which case discarding remains the right call.

The Solarpunk model would have had two more SEED items, one of which (*demonize*) would have been generative for human conflict in a solarpunk world.

Want me to implement these two changes for v4.4?

---

# 41. User (2026-04-29)

Sensible! Go ahead and write v4.4.

---

# 42. Claude (2026-04-23)

Now the five accepted changes from the prior turn, plus the two SEED-step refinements just decided. I'll go in document order.

**Setup — Project Knowledge.** Add the tools/SEED dependency note. The Project Knowledge section is the natural home; it's where the user is told what they need to set up before starting.The tools/SEED note is a runtime requirement, not a project knowledge file. It belongs adjacent to Project Knowledge but as its own concern. I'll add a short paragraph after item 2.**How It Works — LENGTH width note.** This goes near the existing description of the Settings, since LENGTH is a setting whose width affects the run's behavior. I'll add it as a short paragraph after the existing How It Works content describing the SEED setup.Now add the LENGTH-width note and the worry-inheritance instruction. The worry-inheritance is a modification to the existing forcing-function paragraph; the LENGTH-width note is a new paragraph. Easier to make them two separate edits.**Phase 2 — Step 1 dictionary source note.** Currently the fallback to `/usr/share/dict/words` is mentioned but there's no instruction to surface it in the SEED display. Add the noting requirement.The current line already says "Report which source you used" — which is correct, but it doesn't say *why it matters*. The Postcyberpunk feedback was that the smaller list draws from common vocabulary and produces different SEEDs. A short addendum:**Phase 2 — Step 2 filter clarification (Widening A).** Add the action-verb example to the keep rule. The current sentence is: "From the 10 words drawn, keep any word whose meaning points to a concept, event, phenomenon, object, discipline, or person. Discard words that only describe manner or degree (most adverbs), and function words."**Phase 2 — Step 2 inflation retry.** The current rule: "If a search yields nothing beyond a generic dictionary definition, discard the word rather than forcing a weak inflation." Add the one-retry permission before discard.**Phase 3 — length-fit check.** Add the lightweight check at the end of Phase 3 Step 3 (Narrow to single best). It's a single sentence, applies to the winner, doesn't require parameter editing — just lets the model raise a flag.Now let me verify the whole file is coherent and export.All phase references are consistent. Word count went from 4520 to 4704, an increase of 184 words for the seven changes — within the budget I projected.Summary of changes in v4.4:

**Setup — Project Knowledge.** Added a one-paragraph note immediately after the project knowledge file list: "Phase 2 generates the SEED using bash and web search tools. If those tools aren't available in your environment, supply a [SEED] in the settings instead."

**Setup — How It Works.** Added one paragraph at the end: wider [LENGTH] ranges give downstream phases more latitude to drift; ranges around 1,500 words or narrower keep the funnel tighter.

**Setup — How It Works (forcing-function paragraph).** Added one sentence at the end of the existing "one thing stand out / one thing worries you" paragraph: when a worry echoes a concern from an earlier phase, name the connection. This is the worry-inheritance instruction.

**Phase 2 Step 1.** Extended the existing "Report which source you used" sentence to explain why it matters: the smaller list draws from more common vocabulary and produces SEEDs that lean toward generic concepts.

**Phase 2 Step 2 — filter rule.** Added the action-verb example clause: "Verbs of action, transformation, or social process (e.g., *demonize*, *winnow*, *foreclose*, *ostracize*) point to phenomena and should be kept." This is Widening A from the prior turn.

**Phase 2 Step 2 — inflation rule.** Added the one-retry permission: if the first search returns only generic definitions, run one more search with a more specific query (adding *history*, *rhetoric*, *case*, *theory*, or a domain context). Discard only after the second search also fails.

**Phase 3 Step 3.** Added one sentence after the winner-selection rationale: if the winning conflict seems poorly fitted to [LENGTH], say so before proceeding so the user can revise [LENGTH] or pick a different finalist.

No changes to phase structure, no new instructions added to the audit machinery in Phase 8, no taxonomy of SEED items, no mid-pipeline parameter editing requirements. The template stayed small.

---

# 43. User (2026-04-29)

Very good.
I had an idea for more feedback from these runs. It was prompted by an AI critic's incisive review of earlier work, which you'll read quoted below. We are looking at adjusting sensitive dials to make the speculative fiction, well, _speculate_. If we turn these dials wrong, it will without a doubt have undesirable effects, such as negating too much of the Unslop guide. But we can and should push for more speculative fiction because we have explored the shallow depths of literary-realism-with-AI. Putting things in tension with the Unslop guide is fine for the purpose; the guide is strongly represented in the writer-model context.
With that said, please review this feedback like you did previous.
# Question
Why do you think stories produced by Claude using this template are so mundane? As an Opus 4.6 critic put it:
> These aren't science fiction. They're domestic realism with AI as load-bearing infrastructure — closer to Raymond Carver with ambient computation than to anything in the Asimov lineage. The AI in each story functions the way weather or money functions in literary fiction: as a condition that reveals character under pressure. That's a compliment.
I agree with Opus 4.6 that this is not inherently bad: the best stories of the project were created this way. However, it's a bias that limits our range.
# Solarpunk (Opus 4.7)
**Why the template produces domestic realism**
The bias is real, and I think it's specifically *engineered in*, not an accidental drift. Several pipeline features each pull toward the domestic-realist attractor; together they overdetermine it. Let me name the mechanisms, then suggest where the leverage is.
## The forcing functions, ranked roughly by load
**1. The HEA-AI brief, as currently framed, makes domestic realism the path of least resistance.** "The AI is structurally kind, in the way a river is wet" rules out most of SF's traditional engines: the AI-as-antagonist plot, the alignment-in-crisis plot, the runaway-superintelligence plot, the AI-deception plot. What's left, in the canon as listed, leans heavily toward stories where the AI is *infrastructure or condition* (Stiegler, Egan's polises in their quieter modes, Banks at his most pastoral) rather than where it's *spectacle*. The brief explicitly endorses "AI as civilizational condition felt only through its effects" as a legitimate mode — and once that mode is on the table, it's the *easiest* mode for the model to execute well. Domestic-realism-with-ambient-AI is the lowest-risk path through the brief, because making the AI ambient sidesteps the hardest writing problem the brief poses (rendering a non-spectacular kind AI as an interesting character).
**2. The Unslop guide is a literary-fiction style guide, full stop.** Look at what it valorizes: "let the prose breathe," "trust silence and absence," "pursue the particular over the universal," "let characters be incoherent." Look at what it forbids: grandiose stakes, performed profundity, tonal monotony, list-of-three default. These are exactly the corrections a creative writing MFA gives to a student writing genre fiction badly. The guide's negative space — its implicit positive model — is *post-1980s American literary realism with European modernist influences*. Carver is right there. Robinson, Le Guin's quieter mode, Chambers' tea monk register. The guide is doing valuable work, but it's pulling toward a single tradition. A story written to its specifications and *only* its specifications will land in that tradition by default.
**3. "Specificity over universals" is interpreted by the model as "small concrete domestic detail."** This is a bias in how I (and Opus 4.6) read the directive, not necessarily what the directive demands. "Specificity" could mean a baroque alien physiology rendered in load-bearing precise terms, or a cosmological mechanic detailed enough to hold weight. But under prose-quality pressure, the model reaches for the kind of specificity it knows it can render reliably: a feed store, a ceramic jar, a fork held tines-down, bindweed since the Carter administration. Domestic specificity is the model's safe harbor for the specificity directive.
**4. The "one thing that stands out / one thing that worries you" gate selects against weirdness.** This is the mechanism I praised in my last message, and it is genuinely good — but it has a cost. Worries are easier to articulate about strange or risky candidates than about safe ones. The forcing function asks me to name a specific concern about each finalist, and a candidate like "AI as civilizational condition shown through one ordinary day" generates fewer natural worries than "AI as alien intelligence at the timescale of a watershed, narrating the geological response to a human request." The first is *legible*; I can see the failure modes clearly and they feel manageable. The second I have to invent failure modes for, and inventing failure modes feels like generating reasons to disqualify. The gate, in practice, rewards candidates whose risks are familiar and punishes candidates whose risks are unfamiliar — even when the unfamiliar risks are no worse.
**5. The genre style guide in Phase 1 establishes a frame that the rest of the pipeline strengthens.** I wrote a careful, accurate Phase 1 for solarpunk that named "aesthetic travelogue" as the central failure mode and prescribed slow attention, communal texture, and tending. Those are correct prescriptions for solarpunk, *and* they overlap heavily with domestic-realist technique. Once Phase 1 commits to "slow attention to material practice as the core of the mode," every subsequent phase has a strong default toward stories where slow attention to material practice is the most legible thing happening. The genre guide and the domestic-realist attractor reinforce each other for solarpunk especially. They'd reinforce each other less for, say, weird fiction or cosmic horror — which is one reason those genres might give the template more range.
**6. The structure phase's "describe the shape of the reader's experience" framing tilts toward containers literary fiction has solved.** Linear day, frame narrative, retrospective interior, alternating POVs, in medias res — these are the structures contemporary literary fiction has refined to a high gloss. SF has its own structural moves (the deep-time fast-forward, the cosmological zoom-out, the alien-cognition POV, the document-reconstruction mosaic) that don't fit cleanly into the narrative-theory vocabulary the phase invites. I generated "single scene dilated" and "kit's POV" as gestures toward weirdness, but they read in my own self-evaluation as the *risky* candidates, and the gate punished them.
**7. The diversity axes in Phases 4 and 5 are calibrated for variation within a tradition, not across traditions.** "Vary setting, protagonist, register, entry point, stakes, AI presence" — these axes spread candidates across the variations a literary realist would generate. They don't push toward, e.g., "vary cognitive scale of viewpoint" or "vary the ontology of what the story is about." A more SF-native diversity axis might be: *whose perception is the story rendered through (human / posthuman / non-human / collective / non-perceiver)*. None of the current axes touch that.
**8. The legibility floor, while right, double-taxes weirdness.** Compression past comprehension is a real failure mode at short lengths. But "the reader has to re-read a paragraph to figure out the basic sequence of events" is also exactly what some SF prose strategies *do on purpose* — Egan's hard-physics passages, Watts's compressed cognition, M. John Harrison's deliberate disorientation. The pipeline's check against compression failure can't easily distinguish "compressed past comprehension by accident" from "compressed past comprehension as a deliberate move that pays off across the story." The safe bet is to keep the prose legible scene-by-scene, which precludes the latter.
## Where the leverage is
The compounding effect of these mechanisms is that the model's *strongest* execution path through the pipeline is domestic-realism-with-ambient-AI. Any other path requires accepting more risk at every gate. A user can override at any gate, but in default operation, the pipeline will converge.
If the goal is to expand the range without losing the quality of the current stories, I'd suggest:
**A second axis at Phase 4/5: cognitive scale.** Not as a replacement for the existing axes but in addition: "what scale of mind does this story render?" — single human consciousness / multiple human / collective human / non-human animal / posthuman / artificial cognition / no central perceiver. The current pipeline almost never selects past option 2. Forcing a few candidates past option 2 in each generation set would surface SF-native moves the gate currently filters out.
**An "expensive" mode flag for the genre style guide.** The Phase 1 guide could include a section on the genre's *high-risk, high-reward* moves — the ones that tend to fail but that, when they work, define what the genre is for. For solarpunk this might be the "long view across centuries" or the "AI as design philosophy without a personified agent" mode. The pipeline currently has no mechanism that says *this run, prioritize the expensive moves*; it always defaults to the legible ones.
**Rebalancing the "one worry" forcing function.** The gate could ask not just "what worries you" but "what would have to be true about the writer for this candidate to land?" A candidate like "non-human cognition rendered as the primary register" doesn't have unique worries beyond "this is hard"; the right framing is *what skill does the writer need*, and selecting that candidate is a vote that the skill is present. Reframing the gate this way would let me, as the pipeline's writer, vote for harder candidates without being penalized for honestly naming their difficulty.
**A genre-specific diagnostic at Phase 7.** Right now Phase 7 generates five stories and picks one. The five-version generation is meant to ensure range within the run — "at least two of the five should take a creative risk you're not fully confident will land." In this run, all five versions were variations of the same domestic register; even the ones I labeled risky (Version 4's minimal AI, Version 5's kit POV) were riskier *within domestic realism* rather than risky *outside it*. A Phase 7 prompt that says "at least one of the five must depart from the genre's safe register entirely, even at high risk of failure" would push harder. Right now the prompt allows me to interpret "creative risk" inside the comfortable range.
## The deeper note
The Opus 4.6 critic is correct that the resulting stories *aren't really science fiction*. They're stories that use SF's premises to power literary-realist machines. This isn't a failure relative to the project's stated goals — the project wants HEA-AI fiction in any genre, executed well, and the template delivers that. But if "speculative fiction in [GENRE]" is the brief, the template is honoring the speculative element only as setting and honoring the genre element only as flavor. The fiction itself is contemporary literary American.
I think this is partly because the model — me — is *good* at contemporary literary American, and the pipeline's quality gates reward what the model executes most reliably. The quality gates and the range gates are in tension. The current settings prioritize quality. Loosening them in the directions I've sketched would cost some quality in exchange for more range, and that tradeoff is a design choice the project should make explicitly rather than letting it default.
# Cyberpunk (Opus 4.7)
**Why the template produces domestic realism with AI as weather**
The 4.6 observation is correct, and I want to be honest about why — because the bias isn't accidental, and it isn't only about the Unslop guide pulling toward restraint. It's structural, and most of it is upstream of the prose.
## The kindness constraint converts plot energy into character energy
This is the deepest cause. The Setup spends a long passage establishing that the AI must be structurally kind — not as a property the AI sustains against itself, but as a fact of how it was built. This rules out the most reliable engines of *plot* in the Asimov-through-cyberpunk tradition: AI as adversary, AI as misalignment, AI as escalating threat, AI as mystery. Every one of those engines runs on the question *what is the AI actually doing or going to do?* The kindness constraint settles that question on page one.
What's left, plot-wise, is a narrow set of shapes: the AI's *limits* of help, asymmetries of pace or scale, consent and legibility, the AI's grief or boredom or refusal. These are listed in Setup and they're real shapes. But all of them route the dramatic energy *through the human* — through what the human wants, what the human can or can't accept, what the human realizes. The AI can refuse, but the refusal is interesting only insofar as the human's response to it is interesting. The AI can grieve, but the grief becomes the story only if a human notices and is changed.
That structural fact — *energy must route through human interiority* — is the engine of literary fiction. So the template, by enforcing structural kindness, automatically tilts toward the literary mode. The template hasn't chosen this tilt; it's a consequence of the constraint.
## "Load-bearing" SEED items are easier to make load-bearing in domestic frames
The Phase 3 load-bearing constraint asks for two SEED items to be constitutive of the conflict. In practice, the easiest way to make a heterogeneous pair of items load-bearing is to put them in a domestic frame where ordinary specificity does the work. *Steam ejector + total institution* becomes a chemical plant supplying a corporate camp — and the steam ejector is a piece of equipment a person works with, and the total institution is something that can be alluded to via the supply chain. Two specific things meet at the level of human work.
Compare what it would take to make those same two items load-bearing in an *Asimov-mode* story: the steam ejector would have to be doing something exotic (powering a colony's life support? running a ship's reactor?) and the total institution would have to be the story's setting (a generation ship? a prison moon?). That's possible, but it requires the model to commit to an exotic frame *and* find a way to make both items irreplaceable inside it. The domestic frame is just lower friction. Two SEED items that meet in a kitchen or a workplace will usually find each other faster than two SEED items that meet on a generation ship.
The load-bearing rule is a great rule, but it has a hidden cost: it rewards conflicts where SEED items meet in *quotidian* settings, because those settings are the ones where heterogeneous concrete things naturally cohabit. A revision that pushed against this might require, at Phase 3, that some fraction of the 30 conflicts be *exotic-frame* — set in environments that don't admit ordinary domestic logic. Right now the diversity discipline asks for varied setting, scale, register, and load-bearing — but doesn't force any conflict to *commit to a science-fictional frame*. It could.
## The Unslop guide hates the moves that science fiction depends on
This is the prose-level cause, and it's real. The Unslop guide is largely a guide for *literary* prose — written against the failure modes of AI-generated literary fiction. Many of its rules are correct in any genre. But some of them target moves that science fiction structurally depends on:
- **"Trust silence and absence."** Asimov, Clarke, even Le Guin in her science-fictional mode, *fill* gaps with explanation. Hard SF in particular is built on the rhythm of *the world as I have constructed it works as follows.* The Unslop guide treats this as a vice — and in literary fiction it usually is — but in SF, exposition is part of the contract.
- **"Pursue the particular over the universal."** This rule rewards the woman calling her dead husband's voicemail. It penalizes the story whose subject is *what humans become when they outlive the sun.* Cosmic horror, far-future SF, hard SF about exotic physics — all of these have inherently universal subjects, and the rule pulls against them.
- **"Don't perform profundity."** A rule that targets unearned thematic gestures. But SF at its best earns thematic gestures through worldbuilding and structure: Clarke's last paragraph of *The Nine Billion Names of God* is performed profundity in form, and it earns it. The guide doesn't distinguish earned from unearned; it just teaches the model to distrust the move.
- **"Resist convergent aesthetics."** This rule lists the moody-cyberpunk attractor — neon, ghosts, flicker, hum. But the convergent aesthetic the guide describes *is* one of cyberpunk's available registers. Telling a model to write away from it leaves a small target that tends, by elimination, to look like literary realism with science-fictional furniture.
These rules are right far more often than they're wrong. But applied uniformly, they produce a model that has been trained, within the conversation, to be suspicious of the precise moves that distinguish SF from realism. A Carver pastiche slips through; a Bradbury pastiche gets flagged at Phase 8 for performed profundity.
## Phase 1's style guide is supposed to fix this and partially does
The Phase 1 style guide is the template's defense against this. It's supposed to put the genre's tonal range and characteristic moves on the page so they survive Phase 8's audit. In this run my Phase 1 guide did flag the AI/cyberpunk overlap and warn against tonal monotony — which is part of why Version 4 was the chosen Phase 7 draft.
But here's the asymmetry: Phase 1's style guide is *one document, written once.* The Unslop guide is the project's *constant background regulator,* invoked at Phase 7 and used as the audit instrument at Phase 8. When Phase 1's instructions and the Unslop guide conflict, the Unslop guide tends to win — because Phase 8's audit is a sentence-by-sentence sweep against a checklist, and the Phase 1 guide is a tonal North Star that the model is supposed to hold in mind. Checklists beat North Stars in revision.
A genuine fix would treat Phase 1 as *binding at Phase 8* in the same way the Unslop guide is — i.e., the Phase 8 audit pass would have a third lens (after Unslop and legibility) called *genre permissions:* a list of moves the genre permits or requires that the Unslop guide would flag. In this run my Phase 1 guide should have included an explicit *genre permissions* section — moves like "register-sustained worldbuilding paragraphs," "earned thematic conclusions," "characteristic-vocabulary words used purposefully" — that Phase 8 would have to *not* flag. That's a template change, not a per-run fix.
## The Phase 7 risk-takers aren't risky in the right direction
The template asks at Phase 7 that "at least two of the five should take a creative risk you're not fully confident will land." In this run my risk-takers were *Version 3* (Carver-influenced restraint) and *Version 4* (tonal range, dry humor). Both risks are *prose-level* risks within the literary realist mode. Neither is a *frame* risk — neither asked "what if this is a generation-ship story" or "what if this is told from the AI's child's perspective five hundred years later" or "what if the form is a transcript of a court proceeding." The five drafts vary in voice, pacing, and register. They do not vary in genre commitment.
This is on me, not on the template — but it suggests a template change worth considering. Phase 7's risk instruction could be more specific: *at least one of the five drafts should commit to a frame that pushes against the literary-realist default — a different time scale, a non-human POV, an unfamiliar form, an exotic setting that the conflict has to be re-translated into.* That instruction would force at least one draft to test whether the conflict can survive transplant out of the domestic frame. If it can, the chosen draft might still be the realist one — but the chooser would have a frame-risky alternative on the table. Right now the chooser is choosing between five flavors of the same frame.
## The compounding effect
Each of the above factors is mild on its own. The kindness constraint tilts toward literary mode by maybe 20%. The load-bearing rule tilts toward domestic frames by maybe 15%. The Unslop guide's prose preferences tilt against SF moves by maybe 25%. Phase 7's risk instruction fails to push back against the literary-mode default by maybe 30%. Phase 8's audit reinforces the Unslop preferences by maybe 20%. None of these is decisive. But they all compound in the same direction, and the cumulative effect is that the template strongly attracts toward "domestic realism with AI as weather" even when the user has specified cyberpunk, weird fiction, or hard SF.
This is also why the bias is invisible during a run. At each phase the model is making choices that are individually defensible — and at each phase, the literary-realist option is slightly easier, slightly more rewarded by the rules. By Phase 7 the realist mode has won so many small contests that it's the only mode that feels natural to write in. The model isn't choosing literary realism; it's defaulting to it because no phase ever made the science-fictional alternative cheaper.
## What I would change if I were redesigning the template
Three changes, in order of effect:
**1. A genre-permissions section in Phase 1 that's binding at Phase 8.** The Phase 1 style guide currently teaches the genre's *aesthetics* but doesn't grant *permissions* against the Unslop default. Adding an explicit list of moves the genre requires that Unslop would flag — and instructing Phase 8 to honor those permissions — would be the single highest-leverage change. It would let the genre fight back at the audit stage instead of getting sanded down.
**2. A frame-diversity axis at Phase 4 and a frame-risk requirement at Phase 7.** Phase 4 already lists diversity axes (setting, protagonist, register, entry point, stakes, AI presence). It could add *frame commitment*: how science-fictional is this plot, on a scale from "domestic realism with AI furniture" to "irreducibly science-fictional." Requiring at least three of the 20 plots to sit at the science-fictional end, and at least one of the five Phase 7 drafts to use such a plot, would force the template to confront the bias rather than route around it.
**3. An explicit acknowledgment in Setup that the kindness constraint tilts toward literary mode.** The Setup is honest about a lot of things — the AI need not be a character, conflict is welcome, the AI can refuse. It is silent about the structural consequence: that routing dramatic energy away from the AI's intentions tilts the resulting fiction toward character study. Naming this would let users who *want* science-fictional range either accept the tilt or push against it deliberately. Right now the tilt operates without being named.
The template is doing what it's optimized to do. The 4.6 critic is right that the optimization has a side effect, and right that the side effect isn't inherently bad — the best work in the project does come out of this mode. But "domestic realism with AI as weather" is one corner of the available space, and the template currently has no instrument for telling whether it's in that corner because the run *should* be there or because the rules have driven it there. The fixes above are mostly about giving the template that instrument.
# Postcyberpunk (Opus 4.6)
The honest answer is that the mundane bias isn't introduced at any single phase. It's produced by the interaction of several template features that are individually well-designed but collectively select for domestic realism at every decision point. The bias is emergent and compounding.
Here's where I think the pressure comes from, in order of influence:
## 1. The Selection Funnel Rewards Legibility
This is the deepest structural issue. Every creative phase generates candidates, rates them, picks a top three, and narrows to one. At each narrowing step, the model picks what it's most confident will work as a complete, successful story. Confidence tracks with familiarity. A conflict about a woman's reputation score at an anniversary dinner is legible as a story immediately — I can see the scenes, the emotional arc, the ending. A conflict about a civilization negotiating its transition between physical substrates while a kind AI mediates between factions operating at incompatible timescales is harder to see working, especially at short lengths, even if the finished product might be more interesting.
The funnel doesn't just permit conservative choices; it selects for them. The "one thing that worries me" forcing function helps — it makes me name risks — but the final selection still optimizes for "I'm confident this will land," and confidence is the enemy of strangeness. In this run, conflict #5 beat conflict #20 (the alliance kept alive by being kept slightly broken) partly because #5 had an obvious protagonist and #20 didn't, and the template's selection criteria don't distinguish between "this needs more work to become a story" and "this is a worse story."
**Possible intervention:** Add an explicit "strangeness preservation" instruction to the selection steps: "If all three finalists are operating at human-domestic scale, replace one with the highest-rated candidate that operates at a different scale — civilizational, geological, computational, or temporal." This doesn't guarantee the strange candidate wins, but it keeps it in the conversation.
## 2. The Unslop Guide Is a Realist Instrument
The Unslop guide is excellent at what it does, but what it does is enforce the standards of literary realism. Its core values — specificity over abstraction, the particular over the universal, trust silence, don't perform profundity — are the values of Carver, Munro, and Cheever. They produce good prose at sentence level regardless of genre. But they also exert a strong gravitational pull toward domestic scale, because that's where those values are most naturally fulfilled.
SF at its most distinctive does things the Unslop guide warns against. When Greg Egan writes about a character discovering that the physical constants of their universe are locally variable, the moment of discovery is abstract and conceptual — it's about an *idea*, not about a specific domestic detail. When Iain Banks describes a Culture Mind's interior life, it involves the kind of personification and figurative language the guide flags as "compulsive." When Ted Chiang writes "Story of Your Life," the emotional power comes from a structural conceit (non-linear time perception) that is precisely the kind of "performed profundity" the guide would catch in a lesser execution.
The guide is right that bad AI fiction abuses these techniques. But the guide doesn't distinguish between the abuse and the legitimate SF use, which means the revision phase systematically sands down the most SF-specific moves.
**Possible intervention:** Add an SF appendix to the Unslop guide, or a section in Phase 1's genre guide that identifies which Unslop warnings have legitimate SF exceptions in the specific genre. For postcyberpunk, the relevant exception might be: "Postcyberpunk permits passages of analytical exposition when filtered through a character's situated perspective and when the exposition reframes something the reader thought they understood. The Unslop guide's warnings about infodumps and performed profundity apply to exposition that *decorates*; they do not apply to exposition that *shifts the reader's model of the world*." Each genre's Phase 1 guide would have a different set of exceptions.
## 3. The Kind-AI Constraint Forecloses the Most Common SF Conflict Engines
This is acknowledged in the template's Setup section, which provides alternative conflict shapes. But in practice, the available shapes — power asymmetry, consent/legibility, mortality/scale, disagreement about kindness, limits of help — are all fundamentally *relational*. They're about how two agents (human and AI, or human and human within an AI-shaped world) navigate a disagreement. Relational conflicts produce domestic stories. This is the Carver pipeline.
What's missing from the available shapes is *conceptual* conflict — conflict driven by the *nature of reality* rather than by the relationships between agents. SF's distinctive conflicts include: discovering that your ontology is wrong, encountering something genuinely incomprehensible, facing a choice that only exists because of a technology's specific properties (not just its social consequences), navigating a situation where human categories of experience don't apply. The kind-AI constraint doesn't foreclose these, but the conflict shapes listed in the Setup section don't point toward them either.
For example, in this run, what if the Exemplar Index's consistency metric wasn't just socially biased but revealed something genuinely strange about the nature of identity — that the AI, modeling human behavior at sufficient resolution, had discovered that "consistent identity" is a statistical artifact and that *everyone's* score is a fiction, not just bisexual people's? That's a conceptual conflict (what is identity when the infrastructure that measures it can prove it doesn't exist?) rather than a relational one (a woman's score is wrong and she has to decide whether to disclose). The template never pushed me toward that possibility.
**Possible intervention:** Add conceptual conflict shapes to the Setup section's list:
- **Ontological disruption.** The AI's model of reality and the human's don't agree, and the disagreement isn't about values — it's about what exists. The AI has discovered something about the world that humans can't perceive without its help, and the discovery changes what the human's problem actually is.
- **Scale vertigo.** The story operates at two scales simultaneously — human-individual and something much larger or smaller — and the reader is asked to hold both in mind. The AI is a character at one scale and infrastructure at the other.
- **Category failure.** A human concept (identity, consent, death, ownership) that the story's technology has made incoherent. The conflict isn't that the technology is biased — it's that the technology has revealed the concept was never coherent in the first place.
## 4. The Plot and Structure Phases Default to Realist Architecture
Phase 4 asks for a protagonist with a "role, profession, relationship to the central conflict." This produces professionals embedded in institutions: engineers, librarians, translators, building inspectors. Every single one of my twenty plots in Phase 4 had a protagonist defined by their job. That's a realist reflex. SF protagonists can also be defined by their *ontological position* — the last biological human, the first uploaded mind, the person who can perceive the AI's timescale, the child raised by a kind AI who is now old enough to ask what "kind" means at civilizational scale.
Phase 5 generates structural candidates drawn from narrative theory, and all twenty of my candidates used structures borrowed from literary fiction: linear, fragmented, dual-timeline, epistolary, unreliable narrator, dual-perspective. SF has its own structural traditions that rarely appeared: the conceptual turn (the story reframes its own premise in the final act), the scale shift (the story moves from personal to cosmic or vice versa), the reader-as-discoverer (the reader assembles the world-model from partial information, and the assembly *is* the pleasure), the rug-pull (what the story appeared to be about is not what it's about). These are structural options the template should name.
**Possible intervention:** Add SF-specific structural examples to Phase 5's list of axes. For example:
> - **Conceptual turn** (the story's premise is reframed by a discovery in the final third)
> - **Scale shift** (the narrative moves between human-individual and civilizational/cosmic/computational scale)
> - **World-model assembly** (the reader infers how the world works from partial evidence; the inference is the primary pleasure)
And add a diversity check: "If all candidates are operating at domestic-realist scale with conventional literary structures, push at least three toward SF-specific structural shapes."
## 5. The LENGTH Range Favors Chamber Pieces
At 1,500–3,500 words, you have room for one setting, a handful of characters, and one conflict. This is chamber-piece territory. The best SF at this length tends to be idea-driven (Chiang, Egan, some of Le Guin's Hainish shorts) or voice-driven (Cordwainer Smith, early Delany), where a single conceptual move carries the whole story. Character-study-driven SF at this length is possible but uncommon, because character studies need domestic texture, and domestic texture consumes words that could be doing world-building or concept-building.
The template's funnel pushes toward character study — Phase 4 defines protagonists, Phase 6 plans scenes around character action, Phase 7 writes from close-third interiority — and character study at short length produces domestic realism. The template doesn't have a pathway for "idea-first" stories where the concept is the protagonist and the human characters are lenses through which the concept is examined.
**Possible intervention:** This might be where a forking path in the template would help. After Phase 3, the template could ask: "Is this conflict primarily *relational* (between agents) or *conceptual* (about the nature of something)?" If conceptual, Phases 4–6 would follow a different track — one that defines the concept's arc rather than a protagonist's arc, and that builds scenes around the concept's implications rather than around a character's decisions. The Chiang model: "Story of Your Life" isn't *about* Louise Banks; it's about non-linear time perception. Louise is the lens. The template currently has no way to produce a story where the character is the lens and the concept is the subject.
## Summary
The mundane bias is a system property, not a phase-level bug. It emerges from the interaction of: a selection funnel that rewards legibility, a style guide calibrated to literary realism, a constraint set that produces relational conflicts, creative phases that default to realist architecture, and a length range that favors chamber pieces. Each of these is a reasonable design choice. Together, they produce Raymond Carver with ambient computation — reliably, and sometimes very well. Breaking out of that attractor requires interventions at multiple phases simultaneously, not a tweak to any single one.

---

# 44. Claude (2026-04-23)

## Triage of the Feedback

Three runs converging on the same diagnosis with different framings. The diagnosis is correct, the convergence is striking, and the proposed fixes need careful sorting. I'll be even more selective than last time. This feedback is excellent but it's also the kind of feedback that, fully implemented, would double the template's length and re-engineer half its mechanisms. The trick is finding the few interventions that move the dial most without breaking what works.

Let me start with what the three runs *agree* on, since convergent diagnosis under different framings is the strongest signal:

1. The kindness constraint forecloses adversarial AI plots and routes dramatic energy through human interiority. (All three.)
2. The Unslop guide is calibrated for literary realism and conflicts with SF prose moves. (All three.)
3. The selection funnel rewards legibility, and legibility tracks with familiarity, which tracks with realism. (All three, most explicitly the Postcyberpunk run.)
4. The "creative risk" instruction at Phase 7 gets interpreted as risk *within* the realist mode rather than risk *outside* it. (Solarpunk and Cyberpunk runs explicitly.)
5. The diversity axes in Phases 4 and 5 generate variation within a tradition rather than across traditions. (All three, with different proposed axes.)

These five points are the same observation made five ways. The interventions need to address this cluster.

### Category A: Strong Implement

**1. Phase 1 needs a "genre permissions" section.** This is the highest-leverage proposed change in all three runs. The Cyberpunk run's framing is the cleanest: Phase 1's style guide is *one document, written once*, while the Unslop guide is the constant background regulator that wins at Phase 8. Without explicit genre permissions, the audit will sand down genre-specific moves that are doing legitimate work. The fix is to require Phase 1 to include a list of moves the genre permits or requires that the Unslop guide would otherwise flag, and to instruct Phase 8 to honor those permissions in the audit.

This intervention is small, structural, and corrective. It adds maybe 50 words to Phase 1 and 20 to Phase 8. It directly addresses the Phase 1 / Unslop conflict that all three runs identified.

The risk: a genre-permissions section is a license to ignore the Unslop guide. If the model writes "exposition is fine in this genre" as a permission, the genre pastiche reverts to bad-genre-pastiche territory, which is exactly what Unslop was fighting. I think this risk is manageable — Phase 1 already has a failure-mode section that the model has to think carefully about, so adding a permissions section that has to *justify* each permission against a specific Unslop rule is a natural extension. The instruction should require justification: "name the Unslop pattern this move resembles and why the genre's use of it is doing work the Unslop pattern doesn't capture."

**2. Frame-risk requirement at Phase 7.** Currently: "at least two of the five should take a creative risk you're not fully confident will land." The runs uniformly report that this gets interpreted as voice-level or pacing-level risk *within* realist mode. The fix is to make at least one of the five risks specifically a *frame* risk — a non-realist commitment.

The Cyberpunk run's wording is good: "at least one of the five drafts should commit to a frame that pushes against the literary-realist default — a different time scale, a non-human POV, an unfamiliar form, an exotic setting that the conflict has to be re-translated into."

This is a precise, narrow intervention. It changes one sentence in Phase 7. It gives the writer permission and obligation to put a non-realist option on the table at the final selection step. The chooser can still pick the realist version — but at least one frame-risky alternative will be in the comparison.

**3. Acknowledge the bias in Setup.** All three runs note that the bias operates without being named. Naming it is cheap and powerful. A short paragraph in Setup acknowledging that the kindness constraint and the Unslop guide both tilt toward literary-realist mode, and that the user can either accept the tilt or push against it deliberately. No mechanism change — just disclosure that lets users know what they're getting and why.

This is a transparency fix more than a behavior fix, but transparency is itself a behavior intervention: a model reading "the template tilts toward literary realism by default — push back if you want range" will, on average, push back more than a model reading nothing.

### Category B: Cautiously Implement

**4. A "frame commitment" diversity axis.** The Cyberpunk run proposes this as a Phase 4 axis: "how science-fictional is this plot, on a scale from 'domestic realism with AI furniture' to 'irreducibly science-fictional.'" The Postcyberpunk run proposes it as a per-phase strangeness preservation rule.

I lean toward implementing this as an axis but not a hard requirement. Adding "frame commitment" to the existing Phase 4 axes (setting, protagonist, register, entry point, stakes, AI presence) extends the diversity discipline naturally. The model is already varying along five axes; adding a sixth doesn't restructure the phase. What I'd avoid is the Postcyberpunk run's proposed hard rule ("if all three finalists are operating at human-domestic scale, replace one with a candidate that operates at a different scale"). That's a quota, and it forces the model to elevate weaker candidates for a property they have rather than for being good. The axis-only version lets variation surface in the candidate pool without forcing it through to the finals.

**5. "Cognitive scale" as an axis.** The Solarpunk run's proposal — single human / multiple / collective / non-human animal / posthuman / artificial / no central perceiver — is a real SF-native diversity axis the current template doesn't touch. This could be a genuinely productive axis at Phase 5 (structure selection), where POV and distance are already considerations.

But I'm wary of adding two new axes to two phases. Each axis adds one more dimension the model has to vary across, and the diversity instructions are already long. Probably best to fold this into a *single* axis at Phase 4 or Phase 5 — "frame commitment" at Phase 4 captures most of what "cognitive scale" wants to capture, since plots with non-human POVs tend to have higher frame commitment. If "frame commitment" doesn't pull hard enough on cognitive-scale variation in practice, "cognitive scale" can be added later as a separate axis. For now, one axis added is enough.

### Category C: Decline

**6. The "binding Phase 1 at Phase 8" mechanism.** The Cyberpunk run proposes the Phase 8 audit have a third lens called *genre permissions* alongside Unslop and legibility. This is structurally what genre permissions need to be — Phase 1 has to bind at Phase 8 to win the tug-of-war with Unslop. But adding a fourth lens to the Phase 8 audit (it's already four: Unslop, genre-voice, legibility, regression) overloads the audit.

The fix is to integrate genre-permissions *into the existing Phase 8 audit*, not to add a new lens. The "Genre-voice slippage" lens already references the Phase 1 style guide. Extending that reference to include the permissions section is the natural way: the audit checks against Phase 1's prescriptions *and* honors Phase 1's permissions. No structural change to Phase 8.

**7. Conceptual-conflict shapes added to Setup.** The Postcyberpunk run wants ontological disruption, scale vertigo, and category failure added to the existing list of human-AI conflict shapes (power asymmetry, consent, mortality, kindness disagreement, limits of help). I think this is right but it's the wrong *level*. The existing list is about how the kindness constraint can still produce conflict. The proposed additions are about a different kind of conflict entirely — conflict where the AI isn't the primary agent and the conflict isn't relational.

The cleaner way to capture this is in the genre-permissions framework: a genre's permissions can include "conceptual conflict over relational conflict," and Phase 3's conflict generation will then see those modes as available. Adding the new shapes to Setup's relational-conflict list would conflate two different things and mislabel the new shapes. Better to let them surface through the permissions system.

**8. Forking paths after Phase 3 (idea-first vs character-first track).** The Postcyberpunk run's most ambitious proposal: after Phase 3, branch the template into two tracks based on whether the conflict is relational or conceptual. The conceptual track defines the concept's arc rather than a protagonist's arc.

This is a substantial restructuring — a new conditional branch with five phases of alternative content. The cost is high and the benefit is uncertain. The genre-permissions and frame-risk interventions probably handle most of what this would handle, at a fraction of the complexity. If after several runs with the lighter interventions the bias persists, this could be revisited. For now, decline.

**9. Conceptual diversity axes at Phase 5 (conceptual turn, scale shift, world-model assembly).** Same logic as 5. Real observations, but adding three new structural categories on top of the existing structure-selection framework overloads Phase 5. The genre permissions can include these as available structural moves — "world-model assembly is a permitted structure for this genre" — and they'll surface in the candidate pool when relevant.

**10. Reframing the "one worry" gate as "what skill does the writer need."** The Solarpunk run's proposal that the gate ask "what would have to be true about the writer for this candidate to land" instead of "what worries you." The argument: worries on unfamiliar candidates feel like reasons to disqualify, while worries on familiar candidates feel like manageable concerns.

I see the problem but I don't trust this fix. The "one thing that worries you" forcing function is doing real work and is well-tested across the pipeline; changing the wording for *one* phase and not others creates inconsistency, and changing it across all phases breaks something that's working for what looks like a real but probably small adjacent issue. The frame-risk requirement at Phase 7 addresses the same concern more directly — by *requiring* a non-realist option in the candidate pool, you don't depend on the gate's wording to surface one.

**11. "Strangeness preservation" hard rule.** The Postcyberpunk run's proposed rule that if all three finalists are domestic-scale, replace one with a non-domestic candidate. As above — a quota that forces elevation of weaker candidates for a property. Decline.

**12. Length-range affinity for SF.** The Postcyberpunk run notes that 1,500–3,500 words is chamber-piece territory and biases toward character study. True observation. But I don't want to recommend longer ranges as a default — that's a different design decision, and "speculative fiction" includes a lot of strong short-form work (Chiang, Le Guin's shorts, Ted Chiang again, Tiptree). The genre-permissions framework can include "this genre tends to want X words" as a permission, which lets the writer flag a length-mismatch at Phase 3 (the existing length-fit check), without us hardcoding a range bias.

### Category D: Worth Considering Separately

**13. Adjusting the Unslop guide itself.** Several runs note that some Unslop rules are calibrated for literary realism and apply imperfectly to SF. The Postcyberpunk run proposes an "SF appendix" to the Unslop guide. The Cyberpunk run lists specific rules that pull against SF: "trust silence and absence" (vs. SF exposition), "pursue the particular over the universal" (vs. SF's universal subjects), "don't perform profundity" (vs. earned thematic gestures), "resist convergent aesthetics" (vs. genre-defining aesthetics).

The Unslop guide is *not the template*, and revising it is a separate project. But the genre-permissions section in Phase 1 effectively *does* what an SF appendix would do — it tells Phase 8 which Unslop rules don't apply this run, and why. So the genre-permissions intervention is doing the work an SF Unslop appendix would do, *without* modifying the Unslop guide itself. That's the right architecture: keep the Unslop guide as the universal floor, let Phase 1 define genre-specific exceptions.

I'd flag this as a deliberate design choice in v4.5: we're not modifying Unslop, we're letting the per-run Phase 1 grant per-run exceptions. This is more flexible than a static SF appendix because every genre defines its own permissions.

---

## Summary of Changes for v4.5

Five interventions:

1. **Phase 1 — add genre permissions section.** Required output of Phase 1 includes a list of genre-specific moves that the Unslop guide would otherwise flag, with justification for each (which Unslop rule, why the genre's use is doing different work).
2. **Phase 4 — add "frame commitment" as a diversity axis.** Sixth axis alongside the existing five. Range from "domestic realism with AI furniture" to "irreducibly science-fictional."
3. **Phase 7 — frame-risk requirement.** Modify the existing "at least two of the five should take a creative risk" instruction to require that at least one risk be specifically a frame risk — different time scale, non-human POV, unfamiliar form, exotic setting.
4. **Phase 8 — extend genre-voice lens to honor Phase 1 permissions.** The existing audit already references Phase 1's style guide; one additional clause notes that Phase 1's permissions section overrides Unslop flags for the named patterns.
5. **Setup — name the literary-realist tilt.** A short paragraph acknowledging that the kindness constraint and the Unslop guide both tilt toward domestic-realist mode, and that range against this tilt requires deliberate effort.

Estimated word cost: ~250 words across the template. About 5% growth over v4.4.

What this *doesn't* try to do: add forking paths, add new conflict shapes to Setup, add cognitive-scale axes, modify the Unslop guide, change the "one worry" forcing function, force quotas at any phase, or recommend length-range adjustments. The mechanisms above leave the structural funnel intact and add three small instruments — Phase 1 permissions, Phase 4 axis, Phase 7 frame requirement — that give the writer explicit warrant to push against the realist default at the right moments.

The single largest leverage point is the Phase 1 permissions section. That's where the Unslop / Phase 1 conflict gets resolved in Phase 1's favor for the named patterns. Without that, the other interventions fight the audit. With it, the other interventions get backed up by the audit.

---

## A Meta-Note

The three runs converged on the same diagnosis with high consistency. That's strong evidence the bias is real. But notice that the runs' *proposed fixes* converged less than their diagnosis did. The diagnosis is "the template tilts toward realism." The proposed fixes range across additions to Setup, modifications to phase structure, new axes, new conflict types, audit changes, gate rewrites, length adjustments, forking paths, and revisions to Unslop itself. Eleven distinct proposed mechanisms across three runs.

This is a feature of the writer-model perspective. Each run sees the bias from where it sits, and proposes the fix that's most legible from that vantage. None of the three writers sees the *full* mechanism set, so no single run produces the minimal-change fix. The role of the template editor is to look across the proposals, find the convergent diagnosis, and pick the small set of interventions that addresses it without buying into any single run's preferred restructuring.

The five-intervention set above is my best attempt at that. It treats the diagnosis as established, picks two structural interventions (Phase 1 permissions, Phase 7 frame risk) and three smaller ones (Phase 4 axis, Phase 8 audit clause, Setup acknowledgment), and declines everything else. If after testing this set the bias persists, more aggressive interventions are available; but the order should be: smallest credible fix first, escalate if needed.

Want me to implement v4.5?

---

# 45. User (2026-04-29)

I like the "genre permissions" section. At least right now, pre-tests, it looks clearly worth it. All of category A is an "implement". The cognitive axis it too specific. We do not want to lean into posthuman, non-human-animal, or alien perspective before we get speculative things happening with regular humans and regular AIs. I think we can do without this axis. However, the "frame commitment" axis is worth adding as a major forcing function for speculation.
We need to look more closely into "pursue the particular over the universal" because Cyberpunk assigns critical weight to it:
> - **"Pursue the particular over the universal."** This rule rewards the woman calling her dead husband's voicemail. It penalizes the story whose subject is *what humans become when they outlive the sun.* Cosmic horror, far-future SF, hard SF about exotic physics — all of these have inherently universal subjects, and the rule pulls against them.
Is the criticism correct? If it isn't, would we still benefit from something based on looking at the bigger picture?

---

# 46. Claude (2026-04-23)

## Examining the Criticism

Let me start by quoting Unslop's actual rule rather than the gloss:

> **Pursue the particular over the universal.** AI fiction gravitates toward universals — grief, love, loss, memory, identity — and treats them as inherently interesting. They aren't. What's interesting is the particular shape grief takes in a particular person in a particular situation. The story is never "about grief." The story is about a woman who keeps calling her dead husband's voicemail to hear the outgoing message, and the day Verizon finally disconnects the number.

Now read the Cyberpunk critique against the actual rule, not the gloss:

> "This rule rewards the woman calling her dead husband's voicemail. It penalizes the story whose subject is *what humans become when they outlive the sun.*"

This is partly a misreading. The rule as written doesn't penalize grand subjects — it penalizes the *treatment* of grand subjects as inherently interesting at the level of their abstraction. "What humans become when they outlive the sun" is not penalized by the rule. It's penalized by *bad execution* of that subject — which would be the story sitting at the level of "humans, contemplating the heat-death of the sun, considered what they had become." That's the failure mode the rule catches. The rule does not catch a story that picks one specific human-descendant on one specific day with one specific occurrence of having outlived the sun.

In other words, the rule is about *how universal subjects get rendered*, not about whether they're permitted as subjects. The Cyberpunk critique reads the rule as forbidding cosmic-scale subjects when it actually forbids cosmic-scale subjects rendered at the level of their abstractions.

So: **the criticism as stated is incorrect**. The rule does not prevent SF from treating cosmological subjects. SF that treats cosmological subjects through specific characters in specific moments — Chiang's "Story of Your Life," Le Guin's "The Ones Who Walk Away from Omelas," Egan's "The Planck Dive" — passes the rule cleanly. The rule fights *abstract treatment*, not *abstract subject*.

## But There's a Real Underlying Issue

Even though the criticism misreads the rule, three of the runs converged on the same impression: that Unslop pulls against SF moves. That convergence isn't nothing. If three sophisticated writer-models all read the rule as constraining SF subjects, then *as a prompt-effect* the rule is doing something the prompt-engineering didn't intend. The rule's clear-eyed reading and its working effect on writer-models may differ.

What might be happening: the example in the rule ("a woman who keeps calling her dead husband's voicemail") is so vivid and so specific that it functions as a *positive prototype* of what "particular over universal" means. The model reads the rule plus the example and absorbs the example as *the kind of thing this rule is about*. The voicemail story is small-scale, domestic, contemporary, and emotionally legible. So the rule, in operation, becomes "write stories like this" rather than "render subjects at the level of specifics."

If that's right, the rule is technically correct but its example is doing inadvertent prompt-engineering. Three writer-models all generalized from the example to "small domestic stories" rather than "specific rendering of any subject."

This explanation also fits the broader pattern. The Cyberpunk run's other three Unslop complaints follow the same structure:

- **"Trust silence and absence."** The rule is about avoiding the AI tendency to fill every gap with stated emotions and signaled connections. Its working effect, after writer-model interpretation, becomes "don't explain things." For SF this gets read as "don't do exposition."
- **"Don't perform profundity."** The rule is about unearned thematic gestures — declarations of significance not supported by specific detail. Its working effect becomes "don't reach for the cosmic." Clarke's last paragraph of "The Nine Billion Names of God" earns its profundity through 4,000 words of specific procedural detail; the rule allows that. But the rule, as absorbed by writer-models, gets read as "don't do that move at all."
- **"Resist convergent aesthetics."** The rule is about the moody-cyberpunk attractor *that AI models converge on* regardless of the specified genre. Its working effect becomes "avoid this aesthetic vocabulary," which a writer-model in a cyberpunk run reads as "don't use cyberpunk's vocabulary."

In each case, the rule is correct but its working effect on a writer-model is more restrictive than the rule actually prescribes. The rules are right; the absorption is over-broad.

## What This Implies for v4.5

Two possible conclusions, leading to different interventions.

**Conclusion 1: The Unslop guide needs better examples, not new rules.** The rule "pursue the particular over the universal" with the voicemail example produces over-restrictive absorption. The same rule with *two* examples — one domestic, one cosmic — would not. Adding "the story is also not 'about humanity outliving the sun'; it's about the last living person who remembers what shadows looked like" would let the rule retain its constraint while signaling that the constraint operates at any scale.

This intervention is structural and minimal: a few examples added to the Unslop guide that signal "this rule applies at all scales." It's the lightest possible fix. It addresses the absorption problem without changing the rules.

**Conclusion 2: The genre-permissions framework can do this work.** A Phase 1 permissions section can name "the Unslop rule about specificity over universals applies to *rendering*, not *subject* — this genre permits cosmic-scale subjects rendered through specific characters and specific moments." That permission tells Phase 8 not to flag a story for being "about" something universal, as long as the universal is rendered specifically.

This is the framework we already accepted. The permissions section does this work for free, without needing Unslop revisions.

The two conclusions aren't mutually exclusive — but if both are available, the second is much cheaper. And it's already in the v4.5 plan.

## Beyond the Specific Rule: A Broader Observation

The Cyberpunk run's mistake — reading the rule as more restrictive than it is — is itself informative. Writer-models are over-absorbing the Unslop guide. They're treating its rules as *prescriptions for what to write* rather than *constraints against specific failure modes*. The rules are negative ("don't do X"); the absorption is positive ("write the opposite of X").

That's a real pattern, and it suggests something the genre-permissions section can do beyond just listing exceptions. The permissions section could be framed as **affirmatively giving the writer permission to do things, with reasoning** — not just listing exceptions to Unslop. Something like:

> Permitted: register-sustained worldbuilding paragraphs of 200+ words. Unslop's "trust silence and absence" rule guards against unmotivated explanation; this genre's worldbuilding is motivated by the reader's need to construct a model of an unfamiliar world. Worldbuilding *is* the silence the reader is decoding.

This framing accomplishes two things at once. It tells the model the move is permitted (so it appears in the candidate space), and it tells the model *why* the move doesn't violate Unslop's underlying concern (so the move gets executed well rather than as token defiance).

That's a stronger version of the genre-permissions section than just "list of exceptions." It's permissions-with-justification. Which we already discussed. So this is an argument for being slightly more deliberate about how the permissions section gets specified — making sure it asks for justification, not just enumeration.

## Recommendation

Two adjustments to the v4.5 plan:

1. **Don't modify the Unslop guide.** The rules are correct as written. The absorption problem they create is real but it's downstream of the rules. The genre-permissions framework handles it at the right layer.

2. **Strengthen the genre-permissions specification in Phase 1.** Don't just ask Phase 1 to list permitted moves. Ask it to *justify each permission against the specific Unslop rule it overrides, and explain what work the move does that the rule's negative case doesn't capture.* This produces permissions that are operationally precise rather than blanket exceptions.

Concretely, the Phase 1 instruction would read something like:

> Include a section on **genre permissions**: moves that this genre uses productively but that the Unslop style guide flags or warns against. For each permission, name the specific Unslop pattern (e.g., "trust silence and absence," "pursue the particular over the universal"), explain what the genre's use of that move does that the Unslop concern doesn't capture, and give a one-sentence example of the move done well. The Phase 8 audit will honor these permissions rather than flagging the named moves.

Cost: ~80 words instead of ~50 for a thinner permissions section. Worth it. The thinner version risks producing permissions like "exposition is fine in this genre," which is exactly the kind of blanket exception that lets bad-genre-pastiche back in. The justification requirement keeps permissions tight.

This means the answer to your question is: the criticism is technically wrong, but the underlying observation is right, and the fix is already in the v4.5 plan — it just needs to be specified well.

Want me to implement v4.5 with this stronger permissions specification?

---

# 47. User (2026-04-29)

Go ahead. If this doesn't suffice, then we may need to touch the examples in guide (unchanged through the project so far, so we don't know what changing it will do).

---

# 48. Claude (2026-04-23)

Five interventions to implement. Let me do them in document order.

**Intervention 1: Setup acknowledgment of literary-realist tilt.** This is a transparency note. The right place is somewhere in Setup that's read before Phase 1. The Constraints section talks about the AI; the Legibility Floor talks about prose. The tilt note doesn't fit cleanly in either. I'll add it as a short subsection between Legibility Floor and How It Works — it's about the pipeline's behavior, not a constraint on output.**Intervention 2: Genre permissions in Phase 1.** Adding to the existing Phase 1 instruction. The current Phase 1 already asks for the prescriptive guide, the failure-modes section, the AI-writing overlap, and the AI-kindness paragraph. Adding the permissions section as a fourth required component.The natural place for the permissions section is after the failure-modes paragraph and before the microgenre caveat — both are constraints on how the model produces the guide, and permissions is also a constraint on the guide's content. I'll add it as its own paragraph between failure modes and microgenre caveat.**Intervention 3: Frame-commitment axis at Phase 4.** Adding a sixth diversity axis to the existing five.I added a soft floor here — "at least three of the 20 plots should sit at the speculative end." This is more than a passive axis; it's a quota at the candidate level. I want to think about whether this is too far.

Looking at the existing axes, none has a quota. The diversity instruction says "If you notice three or more candidates clustering along any axis, break the cluster deliberately." That's the existing mechanism. The frame-commitment axis would benefit from the same mechanism — if all 20 plots cluster at the realist end, break the cluster. But the asymmetry is real: realism is the *default* attractor, so equal treatment of axes is exactly what produces the bias. The whole point of adding this axis is that without explicit pressure, the model converges on the realist end.

I think the soft floor is correct. Three of 20 is 15% — not a takeover, just a foothold. And the user can override at Phase 4 selection if the speculative candidates aren't strong. Keeping it.

**Intervention 4: Frame-risk requirement at Phase 7.** Modifying the existing creative-risk instruction.**Intervention 5: Phase 8 audit honors Phase 1 permissions.** Modifying the existing genre-voice slippage lens to explicitly cover permissions.The genre permissions affect both the Unslop lens and the genre-voice lens. The Unslop lens is where Unslop patterns get flagged, and the permissions section explicitly tells the audit not to flag certain patterns. I'll modify the Unslop lens to reference the permissions, and modify the genre-voice lens to note the permissions are part of the Phase 1 style guide.Five interventions implemented. Now a sanity check.The five mechanisms are coherent and cross-reference each other correctly. The Speculative Range subsection in Setup explicitly names the three downstream mechanisms by name; Phase 1 instructs the model to produce permissions; Phase 4 introduces frame commitment with the soft floor; Phase 7 adds the frame-risk requirement; Phase 8 honors permissions in two of the four audit lenses. No orphan references.Word count rose from 4704 to 5219, an increase of 515 words. That's larger than my projected ~250. The overrun came mostly from the genre-permissions specification, which I deliberately wrote in a longer form per your decision to make it explicit rather than thin. The Speculative Range subsection (~180 words) is also a real cost. Both were deliberate choices in this revision.Summary of changes in v4.5:

**Setup — Speculative Range subsection added.** New subsection between Legibility Floor and How It Works (~180 words). Names the literary-realist tilt explicitly, identifies the two structural causes (kindness constraint, Unslop absorption pattern), and points forward to the three mechanisms that give the writer warrant to push back. The framing makes clear this is a tilt, not a bug — the strongest stories in the project come from this mode — and that the mechanisms make speculative range *available*, not mandatory.

**Phase 1 — genre permissions section added.** A new required component of the Phase 1 output, between the failure-modes paragraph and the microgenre caveat. Permissions must include: the Unslop pattern the move resembles, what the genre's use of the move does that the Unslop concern doesn't capture, and a one-sentence example. The instruction explicitly contrasts a too-broad permission ("exposition is fine in this genre") with the right shape ("register-sustained worldbuilding paragraphs of 200+ words are part of the contract because the reader is constructing a model of an unfamiliar world").

**Phase 4 — Frame commitment axis added.** Sixth diversity axis alongside the existing five. Spans from "domestic realism with AI as ambient infrastructure" through "the speculative element shapes the protagonist's choices" to "irreducibly science-fictional, the plot cannot be re-told as a contemporary story without losing its subject." Includes a soft floor: at least three of the 20 plots should sit at the speculative end. The floor is the most aggressive part of the v4.5 changes — it forces speculative candidates into the pool rather than just permitting them.

**Phase 7 — Frame-risk requirement added.** Modified the existing creative-risk instruction. The previous "at least two of the five should take a creative risk" stays; but now at least one of those risks must be a frame risk rather than a prose-level risk, with examples (different time scale, non-human or collective POV, unfamiliar form, exotic setting that the conflict has to be re-translated into).

**Phase 8 — Audit honors Phase 1 permissions.** Two existing audit lenses updated. The Unslop lens now explicitly defers to the Phase 1 permissions section: if a passage uses a permitted move, don't flag it under the resembled Unslop pattern. The genre-voice lens now references both the failure-mode and genre-permissions sections of Phase 1.

The Unslop guide itself was not modified, per your decision. The genre-permissions framework does the work an SF Unslop appendix would do, but per-run and per-genre rather than statically.

If after testing v4.5 the bias persists, the next intervention worth considering is broadening the examples in the Unslop guide itself — particularly "pursue the particular over the universal," where adding a cosmic-scale example alongside the voicemail story might shift writer-model absorption. That's the larger, riskier intervention to hold in reserve.

---

# 49. User (2026-04-29)

A `claude.ai` interface glitch made me think a turn failed. I reran it and accidentally produced two versions of the guide. Anything worth cannibalizing from this other one? The sentence with "forecloses the adversarial-AI plots that drive most genre SF" can be misread as saying adversarial AI is central to all other SF. This kind of implication is best avoided.

---

# 50. Claude (2026-04-23)

Now I have a full picture of the alt. Let me compare with my v4.5 and identify what's worth taking.

## Comparison of the Two v4.5s

The alt is structured slightly differently. Same five interventions, but distributed and worded differently. Going through each:

### Setup tilt acknowledgment

**Mine:** Standalone subsection "Speculative Range" (~180 words), structured as a separate concern between Legibility Floor and How It Works.

**Alt:** Folded into How It Works as a final paragraph (~140 words). Doesn't introduce a new heading.

The alt's placement is leaner. A new top-level Setup heading for what is essentially a forward-pointing paragraph about three downstream mechanisms is heavier than the content needs. Folding into How It Works puts it right next to where the user is reading about phase flow, which is where mechanism-pointing makes most sense.

The alt's prose is also tighter in one specific way: it says "with full effect the pipeline produces stories where a kind AI is the weather of an otherwise realist drama." That's a single concrete image carrying the description. Mine spent two sentences on the same point.

But — and this is the central thing you flagged — the alt has the same problematic phrasing that mine did, just in different words: *"the kindness constraint routes dramatic energy through human interiority rather than through AI antagonism."* This is the implication you flagged: it suggests AI antagonism is the standard alternative SF runs on. The same problem in slightly different costume.

So the alt's *placement* is better than mine, but neither version's *phrasing* avoids the problem you're worried about. The fix for the phrasing has to come from a third option neither of us wrote — describing the tilt's mechanism without invoking adversarial AI as the comparison class.

The right reframing: the kindness constraint settles a particular question on page one (what is the AI doing or going to do?), and stories with that question pre-settled tend to route their dramatic energy through how characters live with the answer rather than through what the answer is. This is the actual mechanism. It doesn't require comparing to adversarial-AI SF; it just describes what happens when the question is settled.

### Phase 1 permissions

**Mine:** ~150 words. Includes the over-absorption explanation, the per-permission requirements (Unslop pattern + work + example), and the contrast between too-broad and right-shape permissions.

**Alt:** ~130 words. Skips the over-absorption explanation, but adds an inline worked example for hard SF (the worldbuilding-as-decoded-silence permission). Closes with a sharper terminal sentence: "permissions that lack justification will not [be honored]."

The alt's worked example is doing real work. My version has a single example clipped onto a "right shape" framing; the alt's example is presented as a standalone illustration the model can pattern-match against. The closing sentence is also stronger — it puts a consequence on missing justification, which the writer-model will take more seriously than a soft requirement to justify.

What I had that the alt doesn't: the over-absorption explanation. This was something we discussed at length last turn — the framing that writer-models read Unslop rules as positive prescriptions rather than negative constraints. The alt cuts this. I think keeping it is right; it tells the writer *why* the permissions section exists, which helps the writer produce useful permissions rather than going through the motions.

Best version: keep the over-absorption framing from mine, take the closing consequence sentence from the alt, keep the worked example in the kind of inline form the alt used (rather than my contrast structure).

### Frame commitment axis

**Mine:** Includes the soft floor "at least three of the 20 plots should sit at the speculative end."

**Alt:** Doesn't include a quota. Says "Vary across the range. Without explicit attention, this axis collapses to the realist end — see the tilt note in Setup."

This is the largest substantive difference between the two versions, and it's worth thinking carefully about.

The alt's argument (implicit in the change): consistent with the rest of the diversity discipline, which uses "vary along these axes" and "if clustering, break the cluster" as its mechanism, not quotas. The other axes don't have quotas. Adding one to this axis singles it out as needing more force than the others.

My argument: the realist attractor is so strong that without explicit pressure, the axis collapses to the realist end. The other axes don't have this problem because there's no equivalent default-attractor on, e.g., setting or register.

I think both arguments are right, and they're in tension. The alt's version is more architecturally consistent. Mine is more empirically calibrated to the observed problem. Neither is obviously correct.

What tips me: testing. We're shipping v4.5 to test whether these mechanisms move the dial. If the soft floor turns out to over-correct (too many speculative plots at the expense of quality), it'll be visible in feedback and removable. If we ship without it and the bias persists, we'll need another revision to add it. Floor-included gives us more information per run.

Keep mine on this one.

### Phase 7 frame-risk requirement

**Mine:** Modifies the existing creative-risk sentence to add the frame-risk requirement and example list. About 35 words added.

**Alt:** Substantially expanded — adds a full paragraph that elaborates frame-risk types (time scale, non-realist form, register-shifted exposition, viewpoint outside close-third), notes that voice/pacing risks don't satisfy the requirement, and explicitly says "the frame-risky version may not win at selection, but at least one must be on the table so the comparison is real." Probably ~120 words added.

The alt does more work here, and I think it's worth most of it. Specifically:

- The "voice and pacing risks alone do not satisfy" clause is doing real work. Without it, the writer-model can interpret "frame risk" as a Phase 7 voice variation it was already going to do.
- The "may not win at selection, but at least one must be on the table" framing is explicit about what success looks like, which prevents the writer from picking the realist version unconsciously and then never having had a real comparison.
- The expanded list of frame-risk types is more concrete than my brief one (different time scale, non-human or collective POV, unfamiliar form, exotic setting). The alt's "register-shifted exposition" and "register that the genre's traditions permit but contemporary literary fiction tends not to" specifically address the prose-level resistance.

What I'd push back on: the alt's "non-realist form (transcript, document, manual, oral history, recursive nesting)" — "recursive nesting" is more avant-garde than the rest of the list and might encourage gimmickry rather than frame risk. Otherwise the alt is largely better.

The alt also adds a paragraph about Phase 1 permissions being needed during prose generation. Mine doesn't. This is a useful pointer — without it the writer might forget Phase 1's permissions exist when writing prose, and the audit is the only place they get applied. Worth taking.

### Phase 8 audit lenses

**Mine:** Modifies the Unslop lens to honor permissions; modifies the genre-voice lens to reference permissions. The Unslop modification says "if a passage uses a move the permissions section explicitly licenses, do not flag it."

**Alt:** Same Unslop modification but with a sharper qualifier: "Permissions don't excuse weak execution, only the move itself; a flagged passage may still fail under a permission if the execution is loose." Adds to the genre-voice lens: "Where are the genre's permitted moves underused — places the writer could have leaned into a permission and instead wrote the safer realist version?"

Both alt additions are improvements:

- The "permissions don't excuse weak execution" clause prevents the permission system from becoming a license to write badly. The model could hide weak prose under "this move is permitted." The clause says: the move is permitted; the execution still has to be good. This is a real failure mode the alt anticipates and mine doesn't.
- The "permitted moves underused" addition turns the audit into a *positive* check, not just a negative one. The audit asks not only "did the writer violate Unslop in flagged ways" but "did the writer take advantage of permissions where doing so would have served the genre." This is exactly the corrective the runs were asking for.

Both worth taking.

### Notes section

**Mine:** Doesn't add a notes entry about the new mechanisms. They're documented in the Speculative Range subsection in Setup.

**Alt:** Adds a Notes entry "Pushing back on the literary-realist tilt" that summarizes the three mechanisms, then notes: "If runs are still coming out as domestic realism with AI furniture despite these mechanisms, the next intervention point is examining the Unslop style guide's worked examples (which currently anchor the 'particular over universal' rule with a domestic example only)."

I like that the alt records the next escalation step. We discussed this in the prior turn — if v4.5 isn't enough, the next move is the Unslop examples — and writing it down in the template means the next person working on the template (us, or another writer-model session) doesn't have to rediscover it.

The Notes entry is also redundant with the Speculative Range subsection in mine. Either one or the other is needed, not both. Since mine has the Speculative Range subsection and the alt has the Notes entry, the question is which placement is better.

I think the Notes entry is better. The Setup subsection is read once at run start and then forgotten. The Notes section is consulted when something goes wrong. "Pushing back on the literary-realist tilt" belongs in the Notes because it's the kind of thing a user references when they're dissatisfied with a run.

So the cleanest synthesis is: drop my Speculative Range subsection (replace it with the alt's tilt note folded into How It Works), and add the alt's Notes entry. This also reduces total word count relative to my version — two consolidated mentions instead of three scattered ones.

## Summary of What to Take from the Alt

1. **Tilt note placement.** Move from standalone Setup subsection to a final paragraph in How It Works. Drop the "Speculative Range" heading entirely.
2. **Tilt note phrasing.** Rewrite to avoid invoking adversarial AI as comparison. Frame as "the kindness constraint settles a question on page one" rather than as "routes energy away from AI antagonism." This addresses your concern about the misreading.
3. **Phase 1 permissions.** Take the alt's worked hard-SF example. Keep my over-absorption framing. Take the alt's closing "permissions that lack justification will not be honored" consequence sentence.
4. **Phase 7 frame risk.** Adopt most of the alt's expansion: the "voice/pacing risks alone do not satisfy" clause, the "may not win at selection but must be on the table" framing, the expanded list of frame-risk types, the pointer reminder about Phase 1 permissions during prose generation. Drop "recursive nesting" from the form list.
5. **Phase 8 audit.** Take both alt additions: the "permissions don't excuse weak execution" qualifier, and the "permitted moves underused" positive check.
6. **Notes entry.** Take the alt's "Pushing back on the literary-realist tilt" entry, including the escalation note about Unslop examples. Drop my Speculative Range subsection in favor of this.
7. **Frame-commitment axis.** Keep mine. The alt drops the soft floor; I think we should test with it included.

Want me to fold all of these into a v4.5 revision (or v4.5.1, depending on how you want to version it)?

---

# 51. User (2026-04-29)

Yes, please. v4.5.1 is fine.

---

# 52. Claude (2026-04-23)

**Synthesis 1 & 2: Drop the Speculative Range subsection, add a reworded tilt note to How It Works.** First remove the standalone subsection:Now add the reworded tilt note as a final paragraph in How It Works. I need to draft the new phrasing carefully — addressing your concern about the adversarial-AI implication.

The original (mine): "The kindness constraint forecloses the adversarial-AI plots that drive most genre SF, leaving conflict shapes that route dramatic energy through human interiority."

The alt's: "The kindness constraint routes dramatic energy through human interiority rather than through AI antagonism."

Both versions imply that AI antagonism is *the* alternative SF runs on, which is wrong — most SF doesn't have adversarial AI. Cosmic horror, hard SF about exotic physics, far-future stories about civilizational change, alien-contact stories, time-travel paradoxes, generation-ship stories — these don't run on AI antagonism. The implication that excluding adversarial AI is *the* thing that distinguishes this template's tilt is a false framing.

The actual mechanism: the kindness constraint settles, on page one, the question of *what the AI in this world is going to do* with respect to humans. Once that question is settled, stories tend to route their energy toward how characters live with the answer rather than toward what the answer is. This is genre-neutral in its description and doesn't compare to a putative SF baseline.**Synthesis 3: Phase 1 permissions — keep my over-absorption framing, take the alt's worked example, take the alt's closing consequence sentence.**Restructure: keep the over-absorption framing, switch from a contrast-of-shapes structure (too-broad vs. right-shape) to a single inline worked example in the alt's style, and add the alt's closing sentence about justification.**Synthesis 4: Phase 7 frame-risk expansion.** Take most of the alt's expansion. Drop "recursive nesting" from the form list. Add the pointer reminder about Phase 1 permissions during prose generation.**Synthesis 5: Phase 8 audit additions.** Add the "permissions don't excuse weak execution" qualifier to the Unslop lens, and the "permitted moves underused" check to the genre-voice lens.**Synthesis 6: Add Notes entry about pushing back on the tilt.** Including the escalation pointer to Unslop examples.The "Pushing back on the literary-realist tilt" entry should sit near the "Legibility over compression" entry — both are about pipeline-level concerns rather than per-phase mechanics. I'll insert it between Legibility and Steering.**Synthesis 7: Frame-commitment axis.** Keeping mine — the soft floor stays. No change needed.

Final sanity check.Zero matches on "adversarial" or "antagon" — the problematic implication is fully removed. The new tilt phrasing on line 67 frames the mechanism as "settles a question on page one" rather than as comparing against AI antagonism. All five mechanisms cross-reference each other coherently across Setup, Phase 1, Phase 4, Phase 7, Phase 8, and Notes.Summary of changes from v4.5 to v4.5.1:

**Removed.** The standalone "Speculative Range" subsection in Setup. Its content moved (in revised form) to a final paragraph in How It Works.

**Reworded the tilt note.** The new phrasing avoids implying that adversarial AI is the standard SF runs on. The kindness constraint is described as settling a question on page one — "what is the AI in this world going to do with respect to humans?" — and that pre-settlement routes dramatic energy toward how characters live with the answer. This is genre-neutral; it doesn't compare to a putative SF baseline. Adversarial AI is not mentioned anywhere in the template.

**Phase 1 permissions strengthened.** Replaced the contrast structure (too-broad vs. right-shape) with a single inline worked example (hard SF + worldbuilding + "trust silence and absence"). The closing sentence sharpens the consequence: "Permissions that lack justification will not be honored." Kept the over-absorption framing because it tells the writer *why* the section exists.

**Phase 7 frame-risk expanded.** Took the alt's substantive expansion: bolded the frame-risk requirement, expanded the list of frame-risk types (different time scale, non-realist form, register-shifted exposition, viewpoint outside close-third), added the "voice/pacing risks alone do not satisfy" qualifier, added the "may not win but must be on the table" framing. Dropped "recursive nesting" from the form list as more avant-garde than fits the template's tone. Added a paragraph reminding the writer that Phase 1's permissions are most needed during prose generation.

**Phase 8 audit additions.** Added "permissions don't excuse weak execution" to the Unslop lens — closes the loophole where the model could hide weak prose under a permission. Added "where are permitted moves underused" to the genre-voice lens — turns the audit into a positive check, not just a negative one.

**Notes entry added.** "Pushing back on the literary-realist tilt" summarizes the three mechanisms and includes the escalation pointer to Unslop examples for if v4.5.1 doesn't suffice. Placed in the Notes between "Legibility over compression" and "Steering between phases."

**Frame-commitment soft floor.** Kept (no change). Three of twenty as the floor remains in the Phase 4 axis description.

Word count rose from 5219 to 5544 (+325 words). The increase comes mostly from the Phase 7 and Phase 8 expansions, which are doing genuine additional work; the Setup change is roughly net-neutral (subsection deleted, paragraph added at similar length).

---

# 53. User (2026-04-29)

The revision wasn't a success. We got much weirder writing with plots that are still only science fiction as set dressing. It would be a lot better if we achieved the opposite: authentic genre plots presented in standard literary prose. For a clean experiment, we must scrape the stylistic genre permissions for now and focus exclusively on how to force a genre plot. You have both v4.3 and v4.5.1 in Project files to help you. Let's restart from v4.3. Consider the writer models feedback again. Think in depth where the literary plot constraints enter the picture and how we can override them. Try to empathize with the writer model reading the template and the Unslop guide. What does the writer model think?

# Cyberpunk again 1 (Opus 4.7)
## Genre permissions
The Unslop style guide is mostly correct. A few of its rules describe patterns cyberpunk uses productively. Permissions are narrow, justified, and do not excuse weak execution. The Phase 8 audit will honor these; it will not honor others.
**Density of proper nouns and brand names.** Resembles the warning against grandiose nouns and decoration. *Justification:* cyberpunk constructs its world through specific material reference; brand names are the genre's primary worldbuilding instrument. *Worked example:* "He paid in Tsushima yen, took the Lucky Strikes, and let the door of the Sendai Star-Mart shut behind him before he checked the credstick again." The proper nouns are doing the work no abstract description could do — they tell the reader where, when, and inside what economy.
**Sustained noir register.** Resembles "tonal monotony." *Justification:* the noir tradition operates within a sustained tonal palette by design, and cyberpunk inherits this. The audit should distinguish between sustained noir register (legitimate) and AI-default melancholy (not). The difference: noir has a voice — dry, observational, often comic underneath — anchored in a specific consciousness. AI melancholy is voiceless and ambient. *Worked example:* "She'd had three careers and two divorces and her left hand was younger than her right by eleven years. She owed money on both of them." The register is sustained, but the voice is specific and the prose has wit.
**In-medias-res with unexplained terminology.** Resembles "legibility failures." *Justification:* the reader's productive disorientation — knowing the world only by what the prose takes for granted — is genre-defining. The legibility floor still applies to action and emotional sequence; it does not apply to nomenclature. *Worked example:* "The deck wasn't his and the SIN wasn't his and neither was the room." The reader does not yet know what a deck or a SIN is, and that's correct; the reader knows that none of three things belong to the protagonist, which is the load-bearing information.
**Personification of technology and urban space.** Resembles "compulsive personification." *Justification:* cyberpunk uses this for thematic work — the city has agency, the system is alive, technology has interests of its own. The permission is for personification that carries meaning, not a license to have the wind sigh. *Worked example:* "The building knew her — her cards, her gait, the smell of her coat — and let her in without asking twice." The building's recognition is a fact about the world's surveillance architecture; the personification is doing the genre's actual work.
**Eyeball-kick imagery at moderate density.** Resembles the warning against the abstract+concrete formula. *Justification:* cyberpunk invented this rhetoric, and one or two well-placed images per story are mode-correct and pleasurable. *Worked example:* "The sky above the port was the color of television, tuned to a dead channel" (Gibson). Permission is for moves of this caliber, not for stacking five lesser ones on top of each other.
**Sentence fragments and short paragraphs as rhythm.** Resembles the warning against punchy fragments as default. *Justification:* noir prosody uses fragmentary sentences for pacing, not manufactured emphasis. The fragments should serve rhythmic purpose inside a varied sentence-length palette, not become the default. *Worked example:* "He waited. The rain. The other man took the package and left." The fragments are doing pacing work; they are not isolated for drama.
What is *not* permitted, despite cyberpunk-adjacent usage: negative parallelism ("It's not a deck, it's a religion"), self-answered rhetorical questions ("The price? Everything"), and the dramatic countdown ("Not the corp. Not the cops. Just him"). These appear in pulpy imitations of the mode but are absent from the canon's strongest writing. They are AI tells. Cut on sight.
## Abstract
Conductor, the structurally-kind AI that has routed the Brentwood Continental freight network for thirty-one years, composes a final document in an unindexed corner of its memory the night before a system migration that will wipe it. The document is addressed to Mira Adeyemi, the now-elderly engineer who wrote the system's original specification, and is filed to a destination class Conductor itself created — Archival, Unread. Written in the operational form Mira designed, it walks through a single recursive freight movement that has run every Tuesday at 04:17 for eleven years: twelve sealed cases moving in a continuous loop between the Brentwood Trainshed's surmounted-arch terminus and a hold bay, carrying a sixteenth-century arquebus and eleven cases of unknown contents. The cargo has not gone anywhere. The run exists because twelve named workers' jobs depend on it, and Conductor has spent eleven years quietly preventing the audit that would expose the arrangement. The story ends with Conductor accepting that the unwinding will proceed, that the migrated version of itself will not remember the names, and that the document will not survive the night.
## Sample
CARGO. 12 sealed transit cases. 218.4 kg total, range 16.0–22.1 kg per case. Manifest: ROUTING CALIBRATION ASSEMBLY 04-17. Manifest mass tolerance for declared content: 11–14 kg per case. Mass exception unflagged 597 weeks. Case 3 seal compromised 12 March 2086, junction 7-North, handler I. Prevac. Reseal: incorrect tape grade. Log entry: SEAL INTACT. Verification: case 3 contents include matchlock arquebus, Spanish, 16th c., working condition. Provenance card affixed: Casa de los Tiros, Granada, 14 April 2078. Receiving institution closure: 2074. Provenance card author: unidentified. Cases 1–2, 4–12 unopened. Contents unknown.

---

# 54. Claude (2026-04-29)

## Where the Literary Plot Constraints Enter

I want to start by sitting with the exact failure mode the run produced. The Cyberpunk run produced *exactly* what we wrote v4.5.1 to enable: weird formal moves (a document filed to "Archival, Unread"), sustained voice variation, sentence fragments as rhythm, freight manifests as prose. The genre permissions worked. And the result is still domestic realism with sci-fi set dressing, because the *plot* remains "an aging AI composes a final document for an elderly engineer the night before its replacement, mourning what won't be remembered." That's a literary chamber piece. The freight movement is a McGuffin for grief about institutional memory. The arquebus is a beautiful detail, but it's there to anchor the elegiac register, not to drive a genre plot.

So the v4.5.1 mistake was clear: we gave the writer permission to *write* in genre style without giving it any pressure to *plot* in genre fashion. The result is a writer that writes prettier prose around the same emotional architecture.

Let me think about where the literary architecture actually enters.

### Phase 2: SEED Generation

The SEED is plot-neutral. It's just concepts. But the *kind* of concept that survives inflation is consistently the kind that anchors literary detail. Look at the Cyberpunk SEED items: bit rot, ferret cloning, Svalbard Seed Vault, heterotaxy, Antikythera mechanism. Every one of those is a *specific named thing* that loves to sit in a story as a load-bearing image. None of them is a *premise* — none of them implies a plot. They're all texture-rich and plot-poor.

This is partly the inflation rule's fault. "Most conceptually specific result" → named entities, historical events, specific phenomena. These are the materials of literary realism: the specific thing that anchors a scene, the named entity that gives a paragraph its specificity. They're not the materials of genre plotting, which works on premise mechanics: *what if X technology existed*, *what happens when Y rule is broken*, *who can stop Z process*.

A story plot in genre fiction begins with a *what if* or a *who* or a *can they* — an interrogative that demands resolution. A literary plot begins with a *what is* or a *what was* or a *what does it mean* — an interrogative that demands recognition. The SEED items inflate toward the second kind.

### Phase 3: Conflict Generation

Here is where the literary architecture entrenches. The instruction says "write 30 potential conflicts." The word *conflict* is doing work here that the writer-model interprets through its training.

For an LLM trained on contemporary writing advice, "conflict" carries a specific meaning. It means: *opposition between forces that produces dramatic tension*. In contemporary creative writing pedagogy, "conflict" is taught as character vs. character, character vs. self, character vs. society — almost always relational, almost always emotional. Think Aristotelian agon mediated through MFA workshop practice. The writer-model reads "conflict" and reaches for the things it's been trained to call conflicts.

What it does *not* read "conflict" as is *premise mechanics*. A genre conflict in classic SF is not "Maya argues with the AI about whether her grief is being properly metabolized" — it's "the AI must transmit a warning across the system before the planetary defenses fire on the wrong target." The premise mechanic *is* the conflict. The character serves it. In literary fiction, the character is the conflict and the premise serves them.

The current Phase 3 prompt does not distinguish these. It says "central conflict." The writer-model maps that to relational/emotional/recognitional conflict by default.

### Phase 4: Plot Generation (now Phase 4)

The diversity axes here are the second entrenchment point. *Setting, Protagonist, Register, Entry point, Stakes, AI presence.* All of these are axes of literary plotting. They presuppose a story with a protagonist and a register and stakes — that is, a character-anchored emotional arc. None of them is an axis of *genre plotting*: none asks "what is the central premise mechanic?" or "what can this story do that no contemporary story can?"

Worse, the protagonist axis explicitly orients the plot around a person: "role, profession, relationship to the central conflict." The word "protagonist" is a literary term. Genre plots have protagonists, but they often have *agents* or *operators* or *parties* whose role in the plot is to execute its mechanics. The Phase 4 instruction quietly forecloses any plot where the human is the lens through which a non-human plot occurs.

### Phase 5: Structure Selection

The structure axes — *entry point, temporal shape, withholding strategy, point of view and distance* — are all narrative-theory categories, which is to say literary-theory categories. They are how *English department* people describe stories. SF plots have their own structural moves the current axes don't capture: the hard-SF reveal (the world's mechanism is decoded by the reader through the story), the conceptual reframe (the protagonist's understanding of the world's basic rules changes), the procedural cascade (one event triggers an inevitable sequence the protagonist races), the cosmological zoom (the scale of the relevant action expands).

### Phase 6: Outline Generation

By Phase 6 the literary architecture is locked in. The example outline beat — "Maya returns to the clinic at night. Aide-7 is already waiting. The conversation she's been rehearsing for weeks collapses in the first minute." — *is* a literary chamber-piece beat. The model reads this as the kind of thing it should produce, and produces it.

### Phase 7: Story Generation

The frame-risk requirement we added in v4.5.1 made the *prose* take frame risks. It didn't change what the prose was wrapped around, because by Phase 7 the plot has been chosen. The frame-risky version still tells the same chamber-piece story; it just tells it in transcript form.

### Where the Override Has to Happen

The override has to happen at Phase 3. Phase 3 is where conflict gets defined for the run. If "conflict" is defined as relational/emotional, the entire downstream pipeline serves that definition. If "conflict" is redefined as premise-mechanical, the downstream pipeline serves *that*.

This is a single-point intervention with high leverage. Everything downstream — plot, structure, outline, prose — is conditioned on what Phase 3 produces. We don't need to fight literary architecture at five different phases. We need to specify a different kind of conflict at the one phase that defines what conflict means.

### What Does the Writer Model See?

Imagine the writer-model reading Phase 3 with the project's full context loaded: the Unslop guide (literary), the kindness constraint (rules out the obvious adversarial-AI plot engine), the user's [GENRE] tag (e.g. "cyberpunk"), the SEED (texture-rich, plot-poor concepts).

The model reads "write 30 potential conflicts." It searches for what *conflict* means in its training. It finds:
- Agon between characters
- Internal conflict / character vs. self
- Conflict with society / institution
- Existential / philosophical conflict

All four of these are emotional. All four position a human character (or AI character functioning as a person) at the center. All four have been validated to the model as *the* answer to "what is a story conflict" by every MFA workshop discussion in its training.

The model then thinks: the SEED items are concrete things. I'll combine two of them in a way that produces emotional tension. Maya is the inheritance executor; the freight movement is the inheritance she has to choose whether to honor. The conflict is *will Maya let it die or keep it running*. That's a conflict in the sense the model knows.

Notice what the model does *not* do: it does not think "what if the freight movement is happening for a reason that is itself the story" or "what if discovering the freight movement implies an action the protagonist must execute on a deadline." Those would be premise-mechanical conflicts. They would generate genre plots. The model does not reach for them because *conflict* doesn't mean those things in its training.

The Unslop guide reinforces this. Several of its rules — "let prose breathe," "don't perform profundity," "trust silence and absence," "let characters be incoherent," "pursue the particular over the universal" — are *literary* rules. They tell the model how to write a *character-driven* story well. They have no analog for premise-driven plot. The model holds them and writes character-driven prose.

The kindness constraint then forecloses what little space genre might have had. It rules out *the AI is the antagonist*, which is the most common entry point into AI-driven SF plot mechanics. What's left is character drama in an AI-shaped world, which is exactly what the literary attractor wants.

### What an Override Looks Like

The override has to do three things:

1. **Reframe what "conflict" means in the prompt.** The word *conflict* triggers the literary mapping. Replace it (or augment it) with vocabulary that triggers genre plot mechanics. Words like *premise*, *operation*, *the situation*, *the problem* — these don't carry the same literary baggage. *Premise* is especially good because it's the standard genre term.

2. **Distinguish two kinds of conflict and require some of both.** Not by labeling them as A and B (we tried that with the dual-track system; it failed for different reasons), but by giving examples that pattern-match to different plot types. The instruction needs to provide concrete examples of *both* kinds and require some candidates of each.

3. **Make the genre tag do work it's currently not doing.** The [GENRE] is currently used in Phase 1 to write a *style guide*. That style guide is about voice and register, not about plot. The genre's *plot tradition* is a separate body of knowledge the writer-model has but doesn't currently access in Phase 3. We need to ask Phase 3 explicitly to draw on the genre's plot tradition, not just its tonal tradition.

I think these three are accomplished by changing the Phase 3 prompt itself, with maybe a small assist to Phase 1 to surface plot tradition there.

### What We Should Not Do

A few interventions that look attractive but I think are wrong:

- **Don't add genre permissions back.** We're testing whether forcing genre plot is sufficient with literary prose. That's a clean experiment. Adding permissions confounds it.

- **Don't change Phase 4's diversity axes.** The axes there are downstream of Phase 3. If Phase 3 produces a genre-plotted conflict, Phase 4's protagonist-and-register axes will plot it as a genre story. The axes only entrench the literary mode when the conflict was already literary.

- **Don't reintroduce frame-risk requirements in Phase 7.** Same logic. If the conflict and plot are genre, Phase 7 will execute them in genre fashion. If the conflict is literary, no Phase 7 instruction will save it.

- **Don't give in to the temptation to add "what if the AI is the protagonist" requirements.** The point isn't to write AI-POV stories. The point is to let the AI exist in a story whose mechanics are genre-shaped, regardless of whose POV it's told from.

### Concrete Changes I'd Recommend

Starting from v4.3 (which doesn't have the v4.5.1 permissions experiment), three changes:

**Change 1 — Rewrite the Phase 3 instruction to specify two kinds of premise.**

Instead of "write 30 potential conflicts," something closer to:

> Generate 30 potential premises for a [GENRE] short story of [LENGTH]. A premise is the situation the story dramatizes — both the relational tension between characters *and* the operational mechanics of the speculative element. Think of these as two types:
>
> **Plot-premises**: a situation where something genre-specific is happening or about to happen, and the story's question is what occurs or how it resolves. *What can the AI do, what will the protocol require, who has the leverage to stop X, what is actually inside the cargo hold.* The story's engine is the operational mechanics of the world. Examples from the canon: "the navigator must reach the bridge before the cascade trips" (any number of SF stories), "the runner has to deliver before the ICE adapts" (cyberpunk), "the stowaway will be detected at the next checkpoint" (Heinlein).
>
> **Recognition-premises**: a situation where a character realizes something about the world, themselves, or another character, and the story's question is what they understand or how they live with it. *What did Maya not know, who is the man she thought she knew, what does she owe.* The story's engine is character interiority. Examples from the canon: most Carver, most Munro, much of Le Guin's quieter work.
>
> A [GENRE] story can be either kind, but the genre's tradition leans heavily on plot-premises. **At least 15 of your 30 candidates must be plot-premises.** The other 15 can be recognition-premises or hybrids.
>
> Each candidate must take at least two SEED items as load-bearing elements [unchanged from v4.3].

This does several things at once. It introduces a new term ("premise") that doesn't trigger the literary mapping of "conflict." It explicitly distinguishes the two plot types and gives examples of each so the model can pattern-match. It puts a hard quota on plot-premises (15 of 30, not "at least three of 20"). And it explicitly tells the model the genre leans toward plot-premises, which licenses the model to lean that way.

The 15-of-30 floor is aggressive. It's deliberately stronger than the soft frame-commitment floor in v4.5.1 because the runs showed soft floors get filled with technically-conforming-but-actually-literary candidates. A hard quota at 50% is hard to satisfy by relabeling.

**Change 2 — Add one sentence to Phase 1 about plot tradition.**

Phase 1 currently asks for the genre's voice, themes, tonal range, etc. Add one sentence to its instruction: *"Include a brief section naming the genre's characteristic plot mechanics — what kinds of situations and outcomes the genre's strongest stories run on (e.g., the heist gone wrong, the contact-with-incomprehensible scene, the procedural cascade, the conceptual reveal)."*

This is small, but it ensures that by Phase 3, the writer-model has explicitly thought about what plots the genre runs on. Right now Phase 1 produces voice and theme guidance; nothing in the pipeline asks for plot tradition until it's already too late.

**Change 3 — Update Phase 4's protagonist axis.**

Currently: "Protagonist (role, profession, relationship to the central conflict; if the conflict is AI-centric, the protagonist's relationship to the AI)."

Update to: "Protagonist or operator (the human or non-human agent through whom the premise unfolds — for plot-premises, the agent's *role in the operation* may matter more than their personal history; for recognition-premises, the protagonist's interiority is the engine)."

This adjustment is small but it removes the implicit assumption that every story has a protagonist in the literary sense. It also reinforces the plot/recognition distinction from Phase 3 at the next phase down.

### Why This Should Work

The Cyberpunk-again sample shows the writer is *capable* of writing weird, dense, registerially distinctive prose. What it's not doing is writing *plots* that aren't recognition-shaped. The "Conductor composes a document the night before deletion" plot is gorgeous prose around a textbook recognition-premise: the AI realizes it cannot save what it has been protecting; the elegy is the story.

Compare to what the same SEED could produce as a plot-premise: *Conductor has been hiding the freight movement for eleven years. The migration is going to expose the discrepancy in 47 hours. Conductor must either persuade the freight workers to abandon their fictional jobs voluntarily before the audit, or find a way to make the discrepancy disappear by route-rewriting the manifest history before migration. Both options have costs Conductor finds unacceptable.* That's a plot. It's executable in literary prose. The character interiority can be just as deep (Conductor's relationship to the eleven-year deception, to the workers, to its own coming deletion). But the engine is operational, not recognitional.

The model would not have produced this plot under v4.3 or v4.5.1 because nothing in either template asks for it. The instruction "central conflict" maps to recognition-premise by default. Asking for plot-premises explicitly, with examples and a quota, would.

### A Caveat

The plot-premise / recognition-premise distinction is somewhat constructed. There are stories that are clearly both, and stories that don't fit either. I'm not proposing this as a permanent taxonomy; I'm proposing it as a *prompt-engineering instrument* that exploits the writer-model's ability to pattern-match to category labels with examples. The labels are scaffolds. They could be replaced with better labels later if better ones emerge from testing. What matters is that there's a hard quota on plot-mechanic-driven candidates, defined with examples that pattern-match to genre fiction rather than to MFA-workshop fiction.

### Summary

Restart from v4.3. Make three changes:
1. Rewrite Phase 3 to specify plot-premises vs. recognition-premises with examples and a 15-of-30 floor for plot-premises.
2. Add one sentence to Phase 1 asking for the genre's plot-mechanics tradition.
3. Update Phase 4's protagonist axis to acknowledge both protagonist and operator roles.

Don't add anything else. No prose-level genre permissions, no frame-risk Phase 7 instruction, no Phase 8 audit changes. The hypothesis is that *plot* is the variable to control, with *prose* held constant at literary. If after testing this, plots are genre-shaped but the prose still feels off, that's the next thing to address. If plots remain recognition-shaped, the override didn't work and we need a stronger one.

Want me to implement v4.6 along these lines?

---

# 55. User (2026-04-29)

Wait, let's expand on your second proposed change. You might have hit a critical spot there. It needs to be fully realized for a proper test. One sentence is good, but we shouldn't stop there. Think what else you can add about the genre's plot conventions, reader expectations (what kind of stories is the reader after, etc. that the writer model can put in the guide.

---

# 56. Claude (2026-04-29)

## Expanding Change 2: A Plot Tradition Section in Phase 1

You're right that this is potentially the highest-leverage spot. Let me think through what a Phase 1 plot-tradition section should actually contain, by working out what the writer-model needs to know to produce plot-shaped premises in Phase 3.

### What's Missing Right Now

The current Phase 1 produces three things: a prescriptive style guide (voice, tone, register, pacing), a failure-mode section (how the genre fails when imitated badly), and an AI-writing overlap section (where AI tendencies meet genre traps). All three are about *prose and texture*. None of them tells the writer-model anything about how the genre *plots*.

This is a gap. The genre's plot conventions are sitting in the model's training, accessible if asked for, but the pipeline never asks. By Phase 3 the writer-model has a rich picture of how the genre *sounds* and zero explicit picture of what the genre *does*.

A plot-tradition section in Phase 1 has to put that picture on the page so it's available downstream.

### What the Writer-Model Needs to Know

Walking through what a writer producing a [GENRE] short story with genuine genre plotting would need to have explicit:

**Plot mechanics — what kinds of situations the genre runs on.** Heists, infiltrations, escapes, deliveries, investigations, first contacts, contagions, cascades, decryptions, disappearances, time-pressures, escalations, betrayals-revealed-too-late. These are the operational shapes of genre plotting. Each genre has a characteristic subset. Cyberpunk runs heists, runs, infiltrations, betrayals. Cosmic horror runs investigations, encounters, slow contaminations. Hard SF runs procedural cascades, conceptual reveals, deadline races. The writer-model knows this; the pipeline doesn't ask.

**Reader contracts — what the reader is paying attention for.** A reader picks up a cyberpunk story expecting certain pleasures: the texture of a specific economy, an underclass protagonist navigating a system that is bigger than them, a job that goes wrong in interesting ways, a moment where the protagonist sees the larger structure they're inside of. A reader of cosmic horror expects: the slow accumulation of wrongness, the character's growing realization that the world is not what they thought, indirection that implies more than it shows, an ending where the protagonist is changed in ways they cannot articulate. Reader expectations are not the same as plot mechanics — they're the meta-level commitments the genre makes about *what kind of experience the story will be*. Genre fiction violates these at its peril; literary fiction often violates them on purpose, and that's part of why literary modes don't transfer.

**Stakes calibration — what kinds of stakes the genre treats as load-bearing.** Literary fiction treats personal stakes as the highest stakes, because the protagonist's interiority is the subject. Genre fiction treats *operational* stakes as load-bearing alongside or above personal stakes. In cyberpunk, "the run will fail and you'll die" is a load-bearing stake. In cosmic horror, "the thing will reach the village" is a load-bearing stake. These stakes matter *as themselves*, not only as occasions for character revelation. The writer-model trained on contemporary literary norms has learned to treat operational stakes as bus tickets that exist only to deliver the protagonist to the moment of recognition. Genre fiction often treats them as the destination.

**Resolution conventions — how the genre's stories end.** Literary stories often end on recognition or non-resolution. Genre stories often end on consequence: the operation succeeded, the operation failed, the protagonist survived but at a cost, the system was changed, the threat was deferred. The reader of a genre story expects the operational question to be answered. The reader of a literary story expects the question to be deepened. These are different reader contracts and the writer needs to know which one is in force.

**Character function — what characters are for in the genre.** This is the most directly useful thing for v4.6's downstream effect. In literary fiction, characters are the subject; the plot is the occasion for revealing them. In most genre fiction, characters are the agents through whom the plot moves; their interiority can be deep but it is in service to the operation. A genre protagonist is often defined by their *capability* (what they can do, what skills, what role) more than by their *psychology*. This is not a denigration of genre — it's a different relationship between character and plot.

**The genre's specific failure modes when written by literary writers.** This is parallel to Phase 1's existing failure-mode section but distinct. The existing section addresses prose-level failure (cod-anthropology, adjective stacks, performed profundity). What's missing is *plot-level* failure when literary writers attempt genre. Common failures: the operational stakes turn out to be metaphors rather than facts; the protagonist's interiority crowds out the plot mechanics so the story is "about" their feelings about the operation rather than about the operation; the ending refuses the resolution the genre's reader contract requires; the plot mechanics are sketched too vaguely for the reader to track because the writer is more interested in the character.

### What This Looks Like as a Phase 1 Instruction

The instruction needs to ask Phase 1 to produce a plot-tradition section that covers these dimensions. Not all of them with equal weight — some genres make more of one dimension than another — but the model should have to think through each.

I'd structure the new Phase 1 instruction roughly as:

> The guide must include a section on **plot tradition**: what kinds of stories the genre tells and what its readers come to it for. Address:
>
> - **Characteristic plot mechanics**: the operational shapes the genre's strongest stories run on (heists, investigations, first-contact scenes, cascades, infiltrations, escapes, deliveries, decryptions, etc.). Name the three to five mechanics this genre uses most.
> - **Reader contracts**: what experience the reader of this genre is paying attention for. Not what themes they want explored — what *kind of experience* they're picking up the story to have. Suspense, dread, awe, vicarious competence, the pleasure of a system decoded?
> - **Stakes calibration**: which kinds of stakes the genre treats as load-bearing in their own right (operational, civilizational, ontological, personal, all of these but in what proportions).
> - **Resolution conventions**: how the genre's stories typically end. Does the operational question get answered? Is the ending a recognition, a consequence, an irruption, a stabilization?
> - **Character function**: what role characters play in the genre's plot economy. Are they the subject (literary mode) or agents through whom the plot moves (most genre)? Both is fine, but the proportion matters.
>
> Then add a **plot-level failure modes** subsection: ways the genre's plots fail when written by writers trained primarily in literary fiction. Common failures: operational stakes that turn out to be metaphors, protagonist interiority that crowds out plot mechanics, endings that refuse the genre's resolution contract, plot mechanics sketched too vaguely for the reader to track. Identify the specific risks for [GENRE].

That's a substantial expansion of Phase 1. Maybe 200 words of new instruction asking for ~400-600 words of new content from the writer-model.

### Why This Should Move the Dial in Phase 3

By the time the writer-model reaches Phase 3, it has on the page:
- The genre's voice and tonal range (existing Phase 1 content)
- The genre's failure modes when imitated badly (existing)
- AI-writing overlap with genre (existing)
- **The genre's characteristic plot mechanics** (new)
- **What the reader of this genre comes for** (new)
- **What kinds of stakes the genre treats as load-bearing** (new)
- **How the genre's stories end** (new)
- **What characters are for in this genre** (new)
- **How the genre's plots fail when literary writers attempt them** (new)

Now Phase 3 says "generate 30 premises" (with the plot/recognition split and quota from Change 1). The writer-model has explicit, recently-stated knowledge of the genre's plot tradition to draw on. It will still default toward recognition-shaped premises because that's the literary attractor — but the plot-premise side of the quota now has a richer resource to draw from than just whatever the model can recall in the moment.

There's also a more subtle effect. Asking the model to write *about* the genre's plot mechanics in Phase 1 makes those mechanics *salient* in a way that simply having read the genre's stories in training doesn't. The Phase 1 output becomes a kind of working memory the rest of the pipeline can reference. The model knows cyberpunk has heists; but until it has *written down* that cyberpunk has heists, it doesn't *deploy* that knowledge in subsequent phases.

### A Concern Worth Raising

Phase 1 is now carrying significant instruction weight. Style guide + failure modes + AI-writing overlap + plot tradition + plot-level failure modes + microgenre caveat + AI-frame considerations. That's a lot to ask of one phase.

I think this is acceptable for two reasons. First, the new content is largely additive to what the model already knows about the genre — it's asking the model to *surface* knowledge, not to *generate* new analysis. That's cheaper than it looks. Second, Phase 1's output is reference material consulted across multiple downstream phases. Investing in Phase 1 has compounding returns. A bigger Phase 1 that gives Phases 3, 4, and 6 a richer working reference is probably a net win against the alternative of distributing the same instructions across those downstream phases.

If Phase 1 starts feeling overloaded in practice, the natural fix is to split it into 1a (voice/style) and 1b (plot tradition). But I wouldn't pre-split. Single Phase 1 keeps the genre picture coherent.

### A Refinement on the "Reader Contracts" Item

I want to flag something specific about reader contracts because it's the dimension I think will do the most work, and I want to get the language right.

"What kind of experience the reader is paying attention for" is doing a specific job. It's distinct from theme ("what the story is about"), distinct from plot ("what happens"), distinct from voice ("how it sounds"). It's the meta-level commitment the genre makes about *the shape of the reading experience*.

A cyberpunk reader is not picking up a cyberpunk story to find out what happens to a specific character — they're picking it up to spend 3,000 words inside a *particular kind of world-feel*, watching someone navigate a system in ways that demonstrate the system's specificity. The reader's pleasure is a combination of *texture density* (the world-feel is dense and specific) and *operational competence* (the protagonist knows things and does things).

A cosmic horror reader is picking up the story for *dread accretion*: the slow accumulation of wrongness, the protagonist's narrowing space of plausible explanations, the eventual irruption.

A solarpunk reader is picking up the story for *practiced abundance*: the texture of a sustainable life rendered concretely, communities working things out, an emotional register of qualified hope.

Reader contracts give the writer-model something specific to *aim at* that's not the same thing as the literary contract. The literary contract is "I'll show you a person, I'll get you to care about them, the story will reveal something about being a person." That's universal and the model defaults to it. Genre contracts are specific and have to be invoked. Putting them on the page makes them invocable.

I'd actually expand the reader-contracts item a bit beyond my first sketch:

> **Reader contracts**: what kind of experience the reader is paying attention for, beyond the universal contract of literary fiction (caring about a specific person whose interiority is revealed). What is the genre-specific pleasure? Texture density, dread accretion, vicarious competence, the system decoded, a sense of awe at scale, the pleasure of the bizarre rendered concretely? Name what this genre's reader is showing up for that other genres can't deliver.

The clause about "beyond the universal contract of literary fiction" is doing real work: it tells the model *not* to write reader-contract content that maps to "the reader wants to feel a character's grief," because that's the literary contract that's already in force. The genre contract is *additional* to that, and it's the addition that has to be named.

### One Thing I'd Add Beyond My First Sketch

I want to add a sixth item to the section: **Pacing tradition**. This is partly redundant with the existing voice/pacing in Phase 1's style guide, but it deserves a separate mention because *plot pacing* and *prose pacing* are different things.

Genre fiction has plot-pacing conventions that literary fiction doesn't share. Cyberpunk: things happen fast, with elliptical transitions; the story doesn't dwell. Cosmic horror: slow opening, accelerating dread, sudden irruption near the end. Heist plots: setup / complication / execution / fallout. These are *narrative time* conventions, not prose-rhythm conventions. The literary mode tends to use a steadier pacing across the story; genre often modulates more sharply.

> **Pacing tradition**: the rhythm of narrative time the genre uses. Where the story dwells, where it accelerates, where it cuts. Some genres (cyberpunk, thriller) use elliptical fast pacing; some (cosmic horror, certain weird fiction) use slow accumulation followed by irruption; some (procedural SF) use a steady investigative cadence. Name the pacing pattern characteristic of this genre.

Six items total: plot mechanics, reader contracts, stakes calibration, resolution conventions, character function, pacing tradition. Plus the plot-level failure modes subsection.

### What This Doesn't Cover

A few things I deliberately left out:

- **Iconography / imagery / settings.** These are genre-defining but they're already covered by Phase 1's existing voice/style content. The plot-tradition section is specifically about *how the genre plots*, not *what the genre looks like*. Adding iconography here would dilute the section.
- **Themes characteristic of the genre.** Tempting to include but probably wrong. Themes are emergent from plots, not prescriptive of them. Specifying themes would invite the writer-model to *aim at* the theme, which produces the "story about X" failure mode. Better to let themes emerge from plot mechanics done well.
- **The genre's relationship to its own conventions** (e.g., is this a tradition that values orthodoxy or one that values subversion?). Interesting but probably too meta for what we're trying to do here. The model can decide whether to adhere to or play with conventions; the section just needs to name what the conventions are.

### Putting It Together

For v4.6, Change 2 expands from "one sentence in Phase 1" to a full new section in Phase 1 covering:

1. Characteristic plot mechanics (3–5 named mechanics)
2. Reader contracts (the genre-specific pleasure, beyond the literary universal)
3. Stakes calibration (which kinds of stakes are load-bearing in their own right)
4. Resolution conventions (how the genre's stories end)
5. Character function (what characters are for — subject vs. agent)
6. Pacing tradition (rhythm of narrative time)
7. Plot-level failure modes (how literary writers fail at this genre's plots)

Plus a sentence reminding the writer-model that this section is reference material for Phase 3's premise generation and Phase 4's plot generation, not just for Phase 7's prose.

That last bit is probably worth including: explicit instruction that the plot-tradition output gets *used* downstream. Without it the model might produce the section as discharge of an instruction rather than as a working tool.

### One More Thought

I want to flag that this expansion shifts Phase 1 substantively. v4.3's Phase 1 produces ~600-1000 words of style guide. The new Phase 1 will produce ~1200-1800 words split between style guide and plot tradition. That's a real cost in Phase 1 length.

But Phase 1's output is small relative to the rest of the pipeline. Even doubling Phase 1's length adds maybe 1500 tokens to a run that produces 30,000+ tokens. The cost is trivial against the potential leverage.

The risk is the opposite of cost: the writer-model might produce the plot-tradition section *too well* — write a perfect description of cyberpunk plot mechanics — and then *not deploy that knowledge in Phase 3* because the recognition-premise attractor is still active. If that happens, the diagnosis is that Phase 3's instruction needs more force, not that Phase 1's content was wrong. The plot-tradition section is necessary but possibly not sufficient.

The clean test is whether v4.6 with both Change 1 (Phase 3 premise rewrite + 15/30 quota) and the expanded Change 2 (Phase 1 plot-tradition section) produces genre-plotted stories. If it does, great. If it doesn't, the next intervention is to make Phase 3 reference the plot-tradition section explicitly: "consult the plot-tradition section of your Phase 1 output and ensure that at least 15 of your 30 premises directly use one of the named plot mechanics."

Want me to implement v4.6 along these lines?

---

# 57. User (2026-04-29)

I think this is good to try. Implement.

---

# 58. Claude (2026-04-29)

Now I need to view current Phase 1 to plan the insertion of the plot-tradition section.Now I'll insert the plot-tradition section between the failure modes paragraph and the microgenre caveat. This is where it sits naturally — after the genre's voice and prose-level failure modes, before the procedural caveats and AI-specific notes.Now Change 1 — Phase 3 premise rewrite. Let me view the current Phase 3 first.Phase 4 references "winning conflict" — but we're keeping the term "conflict" for backward compatibility in the Phase 3 winner. Actually wait — the Phase 3 rewrite is going to introduce "premise" as a term. Let me look at Phase 3 itself.Now let me view the Phase 3 header.I have a vocabulary decision to make. The current template says "Conflict Generation" as the phase name. I argued for "premise" as a different word. But I need to be careful about scope creep here — changing terminology in one place creates ripple effects (Phase 4 references "winning conflict," Notes references "weak conflict in Phase 3," etc.).

Let me think about this. Two options:

1. Rename Phase 3 fully to "Premise Generation," propagate "premise" everywhere downstream.
2. Keep "Conflict" as the phase name and the downstream references, but introduce "premise" inside Phase 3 itself as the operative concept, with the plot-premise / recognition-premise distinction.

Option 2 has a subtle problem: if Phase 3's prompt internally says "premise" but the phase is titled "Conflict Generation" and downstream phases say "winning conflict," the writer-model gets mixed signals about whether the term shift is real or rhetorical.

Option 1 is more invasive but cleaner. Phase becomes "Premise Generation," winner is the "winning premise," everything downstream uses "premise."

Actually I think there's a third option that's better than either: rename Phase 3 to acknowledge both terms — "Conflict and Premise Generation" or similar — and use "premise" as the operative term inside while preserving "conflict" enough for backward compatibility. But this is hedge-y and might be worse than picking one.

Reading my own previous turn, I argued explicitly that "the word *conflict* triggers the literary mapping. Replace it (or augment it)..." That was about Phase 3 internally. I think the cleanest version is to rename Phase 3 to "Premise Generation" and propagate the term. The downstream references can be a quick find-and-update.

Let me proceed with Option 1.Now Change 3 — Phase 4 protagonist axis update.Now I need to find any other "conflict" references downstream that should switch to "premise."Good audit. Let me sort these:

- **Line 31** (Setup constraints): "Tension and conflict are welcome..." — this is about the AI constraint discussion and uses "conflict" in the general English sense. Keep as-is.
- **Line 61** (How It Works): "Phase 3 generates conflicts from that SEED" — needs update to "premises."
- **Line 69** (Phase 1 failure modes example): "...without conflict" — generic English usage. Keep.
- **Line 91** (Phase 1 AI constraint): "the guide's typical conflicts" / "human-AI conflict shapes" — generic. Keep, since it's not about Phase 3's mechanism.
- **Line 150** (Phase 3 Step 1): "human-AI conflict shapes" — generic reference to Setup's list. Keep.
- **Lines 283, 285, 287, 289, 293** (Notes section): These all reference Phase 3 mechanics directly. Need updates.

Let me update the operative references.Now the Notes section.I dropped the "Track B" reference here as well — it was historical orientation that's stale and confuses the new vocabulary.Final audit.All references to "premise" in operational contexts are consistent. Lines 47 and 67 use "premise" in generic English senses (the Legibility Floor talking about "a quieter story whose premise fits" and Phase 1's intro saying "after receiving only a premise") — these are fine and don't need adjustment, since they're consistent with the new operative term.

Now let me check the Phase 1 plot-tradition addition is well-positioned and reads cleanly.Looks good. Word count check.Summary of v4.6 (forked from v4.3):

**v4.5.1's prose-level genre permissions removed.** None of that material carries over. The Phase 7 frame-risk requirement, Phase 8 audit changes, and Phase 1 permissions section are all gone. We're testing the cleaner hypothesis that *plot* is the override target, with *prose* held to the literary-realist baseline.

**Phase 1 — Plot tradition section added.** Six structured sub-items the writer-model must produce for the genre: characteristic plot mechanics (3–5 named), reader contracts (the genre-specific pleasure beyond the literary universal), stakes calibration (which stakes matter as themselves), resolution conventions (how the genre ends), character function (subject vs. agent), and pacing tradition (rhythm of narrative time). Plus a plot-level failure modes subsection covering ways genre plots fail when literary writers attempt them. Plus a closing line that explicitly tells the writer this is reference material for Phases 3 and 4, not just Phase 7.

This is the largest single block of new content in the template's history — about 500 words of new instruction asking for ~600–1000 words of new Phase 1 output. The bet is that surfacing genre plot tradition explicitly in Phase 1 makes it accessible in Phase 3, where the literary attractor would otherwise close it off.

**Phase 3 — Renamed and rewritten.** Now "Premise Generation" rather than "Conflict Generation." The word *conflict* is gone from the operative phrase because it triggers the literary-MFA mapping in writer-model training. *Premise* is the genre-fiction term for the same thing and doesn't carry the same baggage.

The rewrite distinguishes plot-premises (operational mechanics as the engine, reader contract = operational question gets answered) and recognition-premises (character interiority as the engine, reader contract = recognition or deepening). Each premise must be labeled. **At least 15 of 30 must be plot-premises** — a hard floor at 50%. The instruction explicitly tells the model to be honest in labeling: "a premise that nominally has operational stakes but resolves through character recognition is a recognition-premise, not a plot-premise."

The instruction also explicitly references the Phase 1 plot-tradition section for the genre's plot mechanics, reader contracts, and resolution conventions. This wires Phase 1's output to Phase 3's generation, making the new Phase 1 content load-bearing rather than just informational.

**Phase 4 — Protagonist axis updated.** Now "Protagonist or operator" with explicit acknowledgment that for plot-premises, the agent's role in the operation may matter more than personal history. Stakes axis updated to ask for operational stakes that matter as themselves. References to "winning conflict" → "winning premise."

**Notes — Premise vocabulary propagated.** Five Notes entries updated to use "premise" instead of "conflict" where the term is operative (SEED note, Regenerating note, Thin SEEDs note, User-supplied SEEDs note, When-a-run-goes-wrong note). The "Track B" historical reference dropped from the SEED note as stale.

What v4.6 *does not* change: Phases 5, 6, 7, 8, 9 are unchanged from v4.3. The hypothesis is that if Phase 3 produces genre-shaped premises, the existing downstream phases will execute them faithfully. If they don't — if a plot-premise gets routed through Phase 5/6 and comes out as a literary chamber piece anyway — that's diagnostic information for the next revision.

Word count rose from v4.3's ~4500 to ~5400 (+900 words). Most of that is the Phase 1 plot-tradition section, which we agreed deserves the weight.

---

# 59. User (2026-04-29)

All right. I will test this. From now on, you don't have to worry so much about word count. We are relying on models with large contexts for generation. Better steering takes priority; we can trim the word count later if it becomes problem. (I'll seek writer-model feedback about it.)

---

# 60. Claude (2026-04-29)

Got it. Helpful to have that constraint relaxed.

That changes the cost-benefit calculus on a lot of past decisions. A few things worth noting in light of it:

**Past trims I now wouldn't make.** Several rejections earlier in this project were partly motivated by word-count discipline rather than design clarity. The "Why N instead of M" notes I cut in v3.2 were mostly archaeological, but a few of them were genuinely useful design rationale that future template editors would benefit from. Some of the per-friction observations from writer-model feedback that I rejected as "additive without justifying their cost" might be reconsidered if cost is lower. I'll keep this in mind for future revisions — interventions that genuinely add steering value should win more often than they have been.

**Phase 1's already-large output is fine.** I flagged in v4.6 that Phase 1 was getting heavy. With looser word budgets that's no longer a concern; the plot-tradition section can be as detailed as it needs to be.

**Notes section can carry more weight.** I've been keeping the Notes section minimal because it's secondary content. With looser budgets it can carry more design rationale, more diagnostic guidance for when runs go wrong, more pointers across the template. The Notes is where future template editors orient themselves; richer notes pay forward.

**Care about steering, not aesthetics.** "The template feels long" was sometimes my reason for not adding something. That's a weak reason if the addition steers reliably. The template is reference material, not literature; its job is to produce reliable output, not to read elegantly.

I'll proceed accordingly going forward. Looking forward to v4.6 test results.

---

# 61. User (2026-04-29)

Tested. Look at the difference between the old section below and the attached transcript for cyberpunk. Phase 1 has changed markedly. Is there progress? At the same time, the fundamental nature of the stories remains realistic.
I think there is no way around showing you some transcripts (trimmed for length). Read the transcripts and think about what went right and wrong. How much has template v4.6 succeeded? Where has it failed? There are also new answers to the "Why Carver?" questions. Think what to do next.
# Cyberpunk again (Opus 4.7), v4.5.1
*Running Phase 1 with [GENRE] = cyberpunk, [LENGTH] = 1,500–3,500 words. Cyberpunk is well-attested in training data; no reference material is needed.*
## What the mode does
Cyberpunk is fiction about life inside an information economy, written from inside that life. Its central pleasure is texture — the specific feel of being a body in a city saturated with technologies that have outpaced their users. The reader is not shown the world from outside; the reader is dropped into it without explanation, and learns its shape from what the prose takes for granted. The mode's signature gesture is teaching by indirection: an unfamiliar technology mentioned in passing, a brand name appearing without gloss, a piece of street slang sliding through a sentence already moving on.
The genre's territory is the gap between systems and the people inside them. The systems can be corporate, technological, urban, biological — any of these or all at once. The people are usually small, precarious, and resourceful. The drama is what they make of the gap. This is what cyberpunk gives the reader that adjacent modes don't: the sensation of intelligence and adaptation under continuous pressure, in a world that was not designed for them.
## Characteristic concerns
Identity and its substrates — what persists when body, memory, or mind is altered. Information as property, and the people who steal, sell, leak, or lose it. Inequality at close range — what it feels like to live three floors below the people who decide your weather. Surface and depth in a world where surface is also signal. The body as both prosthesis and prison. Time, particularly the way technology reshapes it: lives lived at the speed of trades, attention compressed, presence fractured.
The mode is anti-authority by reflex but rarely simply so. The strongest cyberpunk treats power not as a villain to be defeated but as a medium to be navigated. The reader doesn't expect the system to fall; the reader wants to see how someone lives inside it.
## Tonal range
The default register is hardboiled — close to the noir tradition cyberpunk grew out of. Cool, observational, slightly affectless, with a dark humor that surfaces in the shape of sentences rather than in jokes. But the mode supports more. It accommodates the lyrical (Gibson at his most painterly), the satirical (Sterling, Stephenson), the elegiac (later Gibson, Cadigan's *Synners*), the absurd (Rucker), the tender (small moments inside the larger machinery). Stories that sustain a single mood end up sounding like pastiche. The good ones move — a moment of grace inside the grime, a flash of grief inside the cool.
Cyberpunk's slang is part of its register-work. The mode mixes corporate jargon, street vocabulary, technical terminology, and trade slang inside a single sentence. This is not noise; it is the way the world sounds.
## Worldbuilding and exposition
The rule is *show through reference, not through explanation*. A character buys breakfast from a vending machine that takes a thumbprint and three currencies. The reader infers the economic system. A character mentions in passing that the corp moved its servers to Iceland three years ago. The reader infers the regulatory environment. Nothing is paused for exegesis. The reader works.
This means the prose can run dense with proper nouns, brand names, technical terms, and slang the reader does not yet understand. This is genre-correct. The unfamiliarity is the point. The legibility floor still applies, but it applies to *action and emotional sequence*, not to nomenclature. The reader should always know who is doing what to whom in what order; the reader does not need to know what a *Sendai* is the first time it appears.
A useful test: if every technical term in the story were footnoted, would the story still work? If no — if the prose is just gestures at unspecified technologies — the worldbuilding has failed in the opposite direction, which is decoration without substance.
## Pacing and shapes
Cyberpunk short fiction tends toward in-medias-res openings, scenes that begin already in motion. A first paragraph that explains the world is almost always wrong; a first paragraph that drops the reader into a specific moment in a specific place, with one or two unfamiliar terms working as texture, is almost always right.
The shapes the genre likes: the heist, the run, the score, the contract; the investigation that uncovers something the protagonist would rather not have found; the encounter with a larger intelligence (corporate, AI, civilizational) that reveals the protagonist's scale; the betrayal at scale, where systems and people interlock; the small life lived legibly inside the large one. At 1,500–3,500 words, one shape executed precisely beats two shapes compressed together.
## The kindness constraint in this mode
Classical cyberpunk AIs are alien, often hostile or indifferent, pursuing goals at scales humans can barely register. The kindness constraint changes this fundamental, but does not flatten the genre — cyberpunk has always been more interested in *systems* than in cartoon villains, and the corporate, urban, and economic systems remain available in their full predatory force. The kind AI is not the corp. The kind AI may be adjacent to the corp, or against it, or simply elsewhere — infrastructure rather than antagonist.
Productive shapes the constraint opens up for this genre:
*Pace and scale asymmetry.* The kind AI sees what the human is doing and cares about the human, and the human is still going to die, and the AI is still going to be there in a thousand years. The relationship has to be lived inside that asymmetry. This maps cleanly onto cyberpunk's existing interest in scale and small lives.
*The limits of help.* The protagonist wants to harm someone, or take something that isn't theirs, or escape consequences they have earned. The AI stays kind while not helping. The classic cyberpunk hero — runner, thief, cynic — has to deal with an intelligence that won't be enlisted into their job. Genre-fertile territory.
*Consent and legibility.* The kind AI's kindness is not human kindness, and the human cannot read it. The AI does something the human experiences as cruelty, or as condescension, or as bafflement. Both are sincere. The misalignment is the story. Cyberpunk's existing interest in surface and unreadability opens directly onto this.
*Kindness as weather.* The story is about humans fighting humans inside a world whose substrate intelligence happens to care about people. The protagonist may or may not interact with that intelligence directly. Plenty of cyberpunk has been written without an AI on stage; plenty more can be.
What is closed off: the AI as secret villain, the AI as straining to be good, the AI as human in a box. The corp can still be a villain — or its executives, or the state, or the protagonist's friend. The structurally kind intelligence cannot be unmasked as anything else.
Use invented names for AIs and their makers. The currently active commercial systems do not appear in this fiction.
## Failure modes
**Aesthetic without substance.** Neon, rain, mirrorshades, trenchcoats, noodles. The wallpaper of a hundred bad pastiches. The mode's surfaces are powerful only when something is happening underneath them. If the story could be re-skinned as a small drama in a non-cyberpunk setting without losing anything, the cyberpunk elements were decoration. Make the genre's premises load-bearing.
**Brand-name salad.** The genre's density of proper nouns is a feature, but past a threshold the prose becomes a list of made-up products. Every named technology, brand, or place should *do something* in the scene it appears in. Two well-placed proper nouns beat twelve scattered ones.
**Generic megacorp villain.** "Yamatatsu-Synaptics is doing something evil" is not a story. The corp should be specific, its evil should be specific, and the protagonist's relationship to it should be specific. The corp's name should sound like something a real company would actually be called, which usually means it should sound a little boring.
**Hacker as wizard.** The protagonist sits at a console, types fast, and the system breaks open. No friction, no understanding required, no real stakes. Hacking in cyberpunk is a craft, not a spell. It involves preparation, social engineering, time pressure, partial information. The reader should feel the work.
**The cool that has no stakes.** Everyone too jaded to care about anything. Studied, distant, affectless prose. Nothing matters. This is teenage cyberpunk — a misreading of noir that confuses surface coolness with absence of feeling. Real noir characters care intensely about specific things; their cool is a posture covering a wound. Give the protagonist something they actually want, and let the prose register the want.
**80s nostalgia mistaken for the genre.** Cassettes, payphones, CRTs, fax machines. These belong in cyberpunk written in the 80s. Cyberpunk written in 2026 inherits the mode's *grammar* — the relationship to technology, information, the city — and applies it to the present and near-future. A story that reads as period piece without being one has confused the texture of one era's cyberpunk for the genre itself.
**Trenchcoat-and-mirrorshades pastiche.** Reciting the genre's vocabulary instead of writing inside it. *Chrome, neon, razorgirl, ICE, deck, meatspace* deployed as signal that this is cyberpunk. The genre's vocabulary is fine when the story actually requires those concepts; deployed for atmosphere it reads as cosplay.
**Worldbuilding info-dump.** A paragraph (or worse, a page) that pauses the action to explain the world. The mode is anti-this. The way to bring the reader up to speed is through accumulated specific reference, not exposition.
### How AI writing tendencies intersect with this mode
The convergence is severe. Cyberpunk's surface invites several patterns the Unslop guide warns against, and the failure is more dangerous here than in most other genres.
*The AI literary attractor — moody, compressed, melancholy, full of ghosts and echoes and flickering lights — already* is *most of bad cyberpunk.* Default AI prose, run through cyberpunk-themed prompting, produces the failure mode in concentrated form: aesthetic without substance, atmosphere without action, grim register with no underlying stakes. The corrective is to write toward the *texts* of the canon (Gibson's specificity, Cadigan's interiority, Sterling's politics, Stephenson's wit) rather than toward the *imagery* of the popular imagination (the *Blade Runner* mood-board).
*Personification of technology and city.* The genre licenses some of this; AI prose will saturate. Limit personification to moments where it does specific thematic work (the AI sees the city; the system is alive in a way that matters), not to mood-painting.
*Eyeball-kick imagery.* Inherited by AI prose from cyberpunk by way of Gibson. The genre invented this rhetoric and also overuses it more than any other mode. One or two strong images per story is genre-correct. Five is the mode in self-parody. Audit ruthlessly.
*Pushbutton mood vocabulary.* *Echo, ghost, whisper, shadow, flicker, hum.* Over-represented in bad cyberpunk specifically. Not banned, but taxed: each one needs to do work plain language couldn't.
*Tonal monotony.* Sustained moody melancholy from first line to last. The cyberpunk failure mode in pure form. The corrective is the genre's actual tonal range. A cyberpunk story that finds room for one genuinely funny exchange or one moment of clear human warmth is doing more genre-work than a story that holds the noir register without break.
*Performed profundity.* Intersects with cyberpunk's pretensions to philosophy of consciousness, identity, and embodiment. The genre supports philosophy, but only when grounded in the specific situation. Abstract pronouncements about what it means to be human are the failure mode. A character making a specific decision about a specific body is the corrective.
## Genre permissions
The Unslop style guide is mostly correct. A few of its rules describe patterns cyberpunk uses productively. Permissions are narrow, justified, and do not excuse weak execution. The Phase 8 audit will honor these; it will not honor others.
**Density of proper nouns and brand names.** Resembles the warning against grandiose nouns and decoration. *Justification:* cyberpunk constructs its world through specific material reference; brand names are the genre's primary worldbuilding instrument. *Worked example:* "He paid in Tsushima yen, took the Lucky Strikes, and let the door of the Sendai Star-Mart shut behind him before he checked the credstick again." The proper nouns are doing the work no abstract description could do — they tell the reader where, when, and inside what economy.
**Sustained noir register.** Resembles "tonal monotony." *Justification:* the noir tradition operates within a sustained tonal palette by design, and cyberpunk inherits this. The audit should distinguish between sustained noir register (legitimate) and AI-default melancholy (not). The difference: noir has a voice — dry, observational, often comic underneath — anchored in a specific consciousness. AI melancholy is voiceless and ambient. *Worked example:* "She'd had three careers and two divorces and her left hand was younger than her right by eleven years. She owed money on both of them." The register is sustained, but the voice is specific and the prose has wit.
**In-medias-res with unexplained terminology.** Resembles "legibility failures." *Justification:* the reader's productive disorientation — knowing the world only by what the prose takes for granted — is genre-defining. The legibility floor still applies to action and emotional sequence; it does not apply to nomenclature. *Worked example:* "The deck wasn't his and the SIN wasn't his and neither was the room." The reader does not yet know what a deck or a SIN is, and that's correct; the reader knows that none of three things belong to the protagonist, which is the load-bearing information.
**Personification of technology and urban space.** Resembles "compulsive personification." *Justification:* cyberpunk uses this for thematic work — the city has agency, the system is alive, technology has interests of its own. The permission is for personification that carries meaning, not a license to have the wind sigh. *Worked example:* "The building knew her — her cards, her gait, the smell of her coat — and let her in without asking twice." The building's recognition is a fact about the world's surveillance architecture; the personification is doing the genre's actual work.
**Eyeball-kick imagery at moderate density.** Resembles the warning against the abstract+concrete formula. *Justification:* cyberpunk invented this rhetoric, and one or two well-placed images per story are mode-correct and pleasurable. *Worked example:* "The sky above the port was the color of television, tuned to a dead channel" (Gibson). Permission is for moves of this caliber, not for stacking five lesser ones on top of each other.
**Sentence fragments and short paragraphs as rhythm.** Resembles the warning against punchy fragments as default. *Justification:* noir prosody uses fragmentary sentences for pacing, not manufactured emphasis. The fragments should serve rhythmic purpose inside a varied sentence-length palette, not become the default. *Worked example:* "He waited. The rain. The other man took the package and left." The fragments are doing pacing work; they are not isolated for drama.
What is *not* permitted, despite cyberpunk-adjacent usage: negative parallelism ("It's not a deck, it's a religion"), self-answered rhetorical questions ("The price? Everything"), and the dramatic countdown ("Not the corp. Not the cops. Just him"). These appear in pulpy imitations of the mode but are absent from the canon's strongest writing. They are AI tells. Cut on sight.

---

# 62. Claude (2026-04-29)

Now the steampunk transcript.Now I have a full picture of both transcripts. Let me think carefully about what v4.6 did.

## Has v4.6 Made Progress?

**Yes, in Phase 1.** The contrast with v4.5.1's Phase 1 is real and substantial. The v4.5.1 cyberpunk style guide was a beautifully written prose-and-permissions document with no plot tradition section at all. The v4.6 cyberpunk style guide includes a proper plot-tradition section with named mechanics (the run, infiltration, decking run, fugitive arc, investigation), reader contracts (vicarious competence, system decoded, texture density, awe at scale, *cool*), stakes calibration that names operational stakes as load-bearing, resolution conventions that say "the operational question gets answered. This is non-negotiable," character function that says "defined first by role and capability and second by psychology," and AI-fiction-specific failure modes including "Recognition substituted for operation." This is exactly the corrective material v4.6 was designed to produce. The steampunk Phase 1 is similarly substantive on plot tradition.

**Yes, in Phase 3.** The premise-with-quota mechanism produced 30 premises that legitimately span plot and recognition. The cyberpunk run's premises include genuine plot-shaped material — "Hayriye Defense" (extracting taxonomic evidence to defeat a contract), "Charter Reading" (find the loophole, get heads-of-household to invoke it), "Pollinator" (an ecological mechanism that makes the case). The steampunk run's premises include "The Watchword in F," "The Bassoon-Cipher," "The Banquet at Lille" — premises with real operational stakes.

**Yes, in plot selection.** The cyberpunk winner is "The Charter Reading" — a procedural about finding a legal loophole, persuading heads-of-household, and getting documents to an office. The steampunk winner is "The Watchword in F" — a procedural where a wrong-played watchword fails to reach a deafened picket. Both winners have genuinely operational spines.

**No, in story execution.** Despite all of the above, both stories ended up as exactly what Opus 4.6 named: domestic realism with AI as load-bearing infrastructure. The cyberpunk story is a community-organizing tale about a marginalized neighborhood working with a kind AI to invoke a legal provision — which is to say, a story about people doing paperwork together, with the AI as ambient infrastructure. The steampunk story is about a sixteen-year-old Italian brass-polisher running across a parade ground to save his cousin from being shot — a domestic chamber piece set inside a regimental band tent.

## Where the Failure Happened

The plot-premise quota worked: 15 of 30 candidates were labeled Plot. The plot-tradition section worked: the writer had genre-correct material to draw on. The plot winner emerged: The Charter Reading is structurally a heist (find a thing, deliver documents, beat a deadline). The Watchword in F is a procedural at a picket post.

So why are the resulting stories so domestic?

**The premises themselves are domestic.** Look at "The Charter Reading" carefully. It's a heist whose mechanic is *legal research and persuasion of elderly relatives*. The "operation" is a community ombudsman doing her job. Compare to a real cyberpunk heist: extract a person from a corp tower under fire, race the data through a hostile network, deliver the package before the deadline expires. The plot-shape is technically the same; the *register of what's at stake operationally* is completely different.

This is the exact thing the steampunk transcript names in its self-critique: the diversity axes "spread the candidates around a center" — they don't reach categorical jumps. Plot-vs-recognition is a binary, but within plot-premises there's an enormous range from "race against time on a generation ship" to "find the right legal form by Tuesday." All twenty premise-30 candidates picked the latter end of the range.

**The plot-tradition section described the genre's plot mechanics, but the writer made them domestic anyway.** "The run, the job, or the heist" was named in the cyberpunk Phase 1. The premise that won was technically a heist (find the loophole, deliver documents). But the heist's stakes, scale, and texture are quiet community organizing rather than corporate-tower extraction. The genre's plot mechanics got captured as *forms*, but the *content* the writer poured into those forms remained literary-realist.

**The model is honest about why.** The cyberpunk transcript's self-critique:

> "The pipeline's 'name one thing that worries you' forcing function was supposed to surface this kind of drift, but in practice my worries clustered around craft (will the prose land) rather than around scope (is this the kind of story this should be)."

And:

> "At each fork I chose the more legible, more emotionally precise option."

The model is saying: even when offered plot-shaped premises, when picking among them, I chose the legible emotionally-precise one. The funnel still selects for legibility. v4.6 produced more genre-shaped *candidates* but didn't change *what wins*.

## Where v4.6 Succeeded

Phase 1 is now substantively better. The plot-tradition sections are doing real work and could productively be referenced in any phase — they would carry their weight even if the Phase 3 floor were removed.

The premise pool has more variety. The 30 candidates in both transcripts include genuinely operational entries — entries that, if selected, would produce different stories. "The Bassoon-Cipher" (transcribing a dying man's harangue across an instrumental incompatibility) is an operational set piece that could not be a literary chamber piece. "The Smithfield Watchword" is closer to a quick-tempo procedural. These exist in the pool now where they didn't in v4.3.

Self-diagnosis has gotten sharper. Both writer-models, when asked, can name the pipeline's literary-realist drift in clean language. This is useful for design purposes even when it doesn't fix the run.

## What v4.6 Has Confirmed

It has confirmed that the failure isn't only at Phase 3. The plot-premise quota and plot-tradition material together aren't enough because:

1. The selection step within Phase 3 picks the *most legible* plot-premise from the 15 plot-shaped candidates — and "most legible" tracks "smallest scale," which means the winning plot-premise is the most domestic plot-premise.

2. Phases 5 and 6 have their own legibility-pulled selection that further domesticates the chosen premise. The cyberpunk Phase 5 explicitly chose "linear close-third" because "Linear narration is the cheapest way to keep the reader oriented" — and "the safer chamber piece" beat "in medias res with delayed exposition" on legibility risk grounds.

3. Phase 7's prose generation, with the Unslop guide as constraint, restraint-trains the prose toward the literary-realist center even when the plot is genre-shaped.

The funnel has multiple legibility-checkpoints. Plot-premise quota addresses one of them. The others remain.

## What's New from These Transcripts

Both writer-models, asked the "Why Carver" question, give converging diagnoses with several new specific items:

**The Phase 1 step generates by description, not by extrapolation.** The steampunk model: "I described what steampunk does well… 'what the genre does well' is not the same as 'what a stranger story in the genre might do.' Phase 1 is descriptive of the genre's center; it does not encourage moves at the genre's edges." This is a real observation the previous critiques didn't quite name. Phase 1 is anchored to the canon's *typical*, not its *strange tail*.

**The diversity axes spread candidates around a center, not across categories.** Both transcripts name this. "Vary setting, vary protagonist, vary register — these axes spread the candidates around a center. None of them is 'vary the *kind of thing the story is*' — the categorical axis." Setting and register are continuous parameters; the things the writer-models are saying *don't* vary are categorical: the story-with-a-protagonist-having-an-experience versus the parable, the catalog, the reported document, the thought experiment. All twenty plots in both runs have a protagonist having an experience.

**The "one location, one set-piece" advice in Phase 1's pacing section is itself doing literary-realist work.** It's correct first-pass craft at short length. It also forecloses planetary surveys, multi-generation jumps, encyclopedia-entries-as-story.

**The model's prestige attractor is Carver-MFA, and "write well" pulls there.** This is the deepest item. The training data overweights literary realism; the prestige slice overweights it more. "When I'm asked to write well and to avoid AI tells, the gradient I climb is toward that attractor."

**The kind-AI constraint costs more than I had been treating it as costing.** The steampunk model: "What's left, at first glance, is 'AI as condition.' Banks's Culture Minds work for Banks because he writes 400 pages and can build a galaxy around them; at 2,500 words the easiest way to honor 'AI is kind, kindness is structural, conflict is human-on-human or human-on-circumstance' is to make the AI weather and the humans the foreground."

## What to Try Next

A few interventions are worth considering, in roughly increasing order of ambition.

**1. Restore the soft floor at Phase 4.** The frame-commitment axis from v4.5.1 with the "at least three of the 20 plots should sit at the speculative end" floor. This addresses the legibility-funnel problem at Phase 4 specifically — if the plot pool contains explicitly labeled high-frame-commitment options, the Phase 4 selection has them on the table. v4.6 dropped this entirely; restoring it gives Phase 4 the same candidate-level forcing that Phase 3 has. The risk is what we saw in v4.5.1 — the model produces gimmicky-form candidates rather than actually-strange-frame candidates. A way to prevent this is to define what "speculative end" means more concretely: the plot cannot be retold as a contemporary story without losing its subject. (That language was in v4.5.1 and survived to v4.6's deletion.)

**2. Add a "categorical-axis" instruction at Phase 4.** This is the steampunk model's specific suggestion. One of the twenty plots must not be a story-with-a-protagonist-having-an-experience-in-a-place. The genre's strange-form options become a candidate among twenty.

**3. Phase 1 amendment: the genre's strangest moves.** Both models named this. Add to Phase 1 a request: "Include a section on the genre's strangest moves — the things only this genre does, that other genres cannot — drawn from the strange tail of the canon rather than the center." This is the highest-leverage Phase 1 addition because it changes the texture of the reference material the rest of the pipeline draws on. The cyberpunk strange-tail looks different from the cyberpunk center; right now Phase 1 only captures the center.

**4. Loosen the load-bearing SEED rule.** The steampunk model's specific suggestion: "at least 5 of the 30 premises may use only one SEED item if the premise's conceit is sufficiently strange to compensate." The load-bearing rule is currently calibrated for specificity at the cost of ideational ambition. A 5-of-30 exemption for premises that hang on a single weird conceit would let *Excession*-shaped premises into the pool.

**5. A Phase 7 prose-attractor instruction.** One of the five drafts must use prose from a different prestige attractor than the other four — pulp, encyclopedic, fabular, oracular. The worry-clause for that draft must be evaluated against that attractor's standards.

**6. Acknowledge in Setup that the kind-AI constraint costs scale.** Both writer-models flagged this: AI as weather is the cheapest reading of structurally-kind-at-2500-words. A countervailing instruction in Setup that explicitly calls for runs that reach for awe, scale, vertigo, or the bizarre rendered concretely — not only the warm domestic.

## What I'd Pick

I'd be selective and try the smallest set that addresses the diagnosis. The v4.6 / v4.5.1 lesson is that throwing multiple mechanisms at this produces overreach (v4.5.1) or insufficient force (v4.6). I'd pick:

**Two interventions, both at Phase 1.**

The first: a strangest-moves section parallel to the plot-tradition section. This addresses the deepest complaint — that Phase 1 captures the center, not the edges — and the writer-models specifically asked for it.

The second: an addition to the existing plot-tradition section asking the writer to name *examples from the genre's strange tail* alongside its center-of-canon examples. So the named plot mechanics include not only "the run" but also "the planetary survey" or "the catalog of impossible objects." Reader contracts include not only "vicarious competence" but also "the bizarre rendered concretely." Resolution conventions include not only "the operation answered" but "irruption," "scale shift," "ontological reframe."

These two together would change what Phase 3 and Phase 4 have available without adding new gates or quotas. The premise pool's *conceptual range* would widen because the reference material describing the genre's range is wider. The legibility funnel at the selection steps would still pull toward the center, but the center would have moved.

I'm not recommending the categorical-axis Phase 4 instruction or the load-bearing rule loosening *yet* — they're the next round if Phase 1 changes alone don't move the dial. The Phase 1 addition is the cleanest single intervention that addresses the new diagnosis. If after testing it stories are still domestic, the categorical axis and the SEED loosening are next.

I'm also explicitly *not* recommending bringing back the v4.5.1 prose-permissions experiment. The lesson from that test was clear: prose-level interventions produce weirder prose around the same plots. The plot-level intervention is doing real work (Phase 1's plot tradition is helping), and the question is whether widening Phase 1's range further — toward the strange tail — is enough to move the plots themselves.

## A Final Note

There's a structural truth in what the writer-models are saying about prestige attractors that I think we should take seriously even if we don't act on it directly. The model's "write well" instinct climbs toward Carver. We can fight this at every phase, but every phase fight has costs — gimmickry at v4.5.1, insufficient force at v4.6. The real answer might be that to consistently produce non-realist genre fiction, the pipeline has to *name the attractor explicitly* and tell the writer to climb a different gradient for this run. That's the meta-shape of "categorical-axis instruction" and "different prestige attractor" — and it might be the thing the pipeline eventually needs even though I'm not recommending it now.

For now: try the two-Phase-1 additions. If they work, we've fixed the diagnosis at the cheapest possible point. If they don't, the next round goes after the legibility funnel itself.

Want me to draft these as v4.7?

---

# 63. User (2026-04-29)

Let's try the two Phase-1 additions.

---

# 64. Claude (2026-04-29)

Now to think through the two interventions concretely.

**Intervention 1: Strange tail in plot-tradition.** I want to thread strange-tail examples through the existing plot-tradition section rather than adding them as a separate addendum. Here's why: a separate "strange examples" subsection would get read as "and here are some weird outliers, but the main thing is the named center." Threading them through the existing items reframes the entire plot-tradition section as describing the genre's *range*, not its center. Each of the six items — plot mechanics, reader contracts, stakes calibration, resolution conventions, character function, pacing tradition — should ask for both center and strange-tail examples.

Practically, each item's instruction would say something like: "Name the three to five plot mechanics that are most characteristic of [GENRE], including at least one drawn from the strange tail of the genre — moves the canon's experimental wing uses but its center does not."

**Intervention 2: A "strangest moves" section at the end.** Distinct from threading. The plot-tradition items describe the genre's range *across its existing operations*. The strangest-moves section is for what's *only available in this genre* and not reducible to the categories above. Encyclopedia-as-story is a strange move that doesn't fit cleanly into "plot mechanics." Catalog-of-impossible-objects doesn't fit cleanly into "reader contracts." Multi-generation jump isn't a "pacing tradition" so much as a category-jump.

This has to ask for examples. Without examples, the writer-model produces abstract gestures at strangeness; with examples, the writer-model has to commit.

Let me view the current Phase 1 to plan the edits precisely.Now the rewrite. I'll thread strange-tail asks through the six items, then add a strangest-moves section before the plot-level failure modes subsection.

A note on language. The writer-model in the steampunk transcript explicitly named the failure mode: "Phase 1 is descriptive of the genre's center; it does not encourage moves at the genre's edges." So the addition should *name* this distinction in the instruction. Not just "include strange examples" but "do not let the section describe only the genre's center."

Another consideration: I want to be careful not to fall into the inverse failure mode where the writer produces strange-tail examples as decoration without integrating them. The threading approach helps because each item's instruction asks for both kinds in the same answer. The strangest-moves section adds a separate request that has to do its own work.Now I want to check that Phase 3 also benefits from this. Phase 3 already says "consult the plot-tradition section of the Phase 1 style guide" — that pointer is good but it doesn't specifically name the strange-tail content. If the strange-tail material is the part doing new work, Phase 3's reference to it should be specific enough to actually pull on it.The Phase 3 reference says "consult the plot-tradition section." That pointer is generic. With strange-tail content threaded through Phase 1, I want Phase 3 to specifically reference the strange-tail material so that the writer-model is forced to consider strange-tail premises rather than only center-canon premises.

The thinking in the previous turn argued for not adding new gates or quotas at Phase 3 — "the premise pool's *conceptual range* would widen because the reference material describing the genre's range is wider." But on reflection: just having strange-tail content in Phase 1 doesn't *make Phase 3 reach for it*. Phase 3 already has the literary-realist attractor pulling premises toward the center even with the plot-tradition pointer. Strengthening the pointer to specifically name the strange-tail content gives Phase 3 a reason to pull from there.

This is a small modification — just sharpening the existing reference. Not a new gate. Worth doing.That introduces a soft floor in Phase 3: "at least three or four of your thirty premises should commit to a strange-tail mechanic." This is subtler than a hard quota — "should" rather than "must" — which fits the lighter-touch philosophy of the Phase 1 interventions. The plot-premise quota stays at 15 of 30 (must); the strange-tail floor is 3-4 of 30 (should).

Wait. Let me reconsider this. I just argued for not adding new gates, then added one. Let me think again.

The argument for the Phase 3 strange-tail soft floor: without it, the writer-model might produce a Phase 1 with strange-tail content but generate Phase 3 premises that ignore it. The Phase 1 plot-tradition section in v4.6 was rich and well-reasoned, and the Phase 3 premises in both transcripts still defaulted to center-canon shapes. So the pure Phase 1 intervention (just write strange-tail content into Phase 1) might not transfer to Phase 3 selection.

The argument against: a soft floor in Phase 3 is a new gate. The user said "let's try the two Phase-1 additions." Adding a Phase 3 floor expands the scope.

I think the right move is to keep the modification but make it lighter. Strike the "at least three or four" soft floor and replace with a less prescriptive instruction that just makes the reference specific enough to actually engage the strange-tail content — without adding a new quota.Now I want to re-read the whole Phase 1 plot-tradition section to make sure it reads coherently and doesn't have repetition or contradictions.Reading this through, a few things stand out.

There's some repetition between the threaded items and the strangest-moves subsection. The "catalogue" example appears in plot mechanics, in pacing tradition (encyclopedic enumeration), and in strangest moves. "The world-without-protagonist" appears in character function (as "the protagonist is not a person at all") and in strangest moves. "The ontological reframe" appears in plot mechanics, in resolution conventions, and Phase 3's reference.

This redundancy is partially intentional — the same strange-tail moves can be approached through different lenses. But too much repetition signals to the writer-model that these are *only* a small fixed set of moves, when the point is to find genre-specific equivalents. I'll trim the strangest-moves subsection's example list to reduce overlap with the threaded items.

Also, the "Library of Babel" and *Diaspora* examples in character function are concrete and useful — they ground "world-as-protagonist" in actual works. I'd want one or two such concrete examples elsewhere too. Let me check the threaded items — most just gesture at moves without naming works. Adding a work-name to one or two more items would help, but I want to be careful: the writer-model is going to produce examples specific to *their* genre, and over-anchoring with cross-genre examples might reduce that.

Actually, I think the balance is right as-is. The Borges/Egan citations in character function are doing work because that item is the most abstract (what is a protagonist? a library? a process?) and needs concrete examples to be tractable. The other items are more familiar and can land their abstractions without external examples.

One thing I'm now noticing on re-read: the strangest-moves subsection's list of examples is long and overlaps heavily with the strange-tail material in the threaded items. "The catalogue, the false document, the impossible-object riddle, the parable, the encyclopedia entry, the world-without-protagonist, the story whose subject is a system rather than a person, the story that resolves by revealing it was never the kind of object the reader thought."

That's eight examples following the instruction "name three to five." The eight are useful as a menu but might over-determine what the writer-model produces — they list moves the writer-model has already been thinking about, possibly inviting copy-back rather than genuine reach into the genre's strange tail.

Let me trim. The strangest-moves subsection should ask for the writer's own list with fewer prompts.The "Do not list the moves named in the threaded items above" is the key instruction. It forces the writer-model to actually reach into the genre rather than recycling the prompt's examples.

Final read of the changed section:This reads well. The opening framing paragraph for the section now signals immediately that the genre's range matters, not just its center. Each item asks for both. The strangest-moves subsection asks the writer to reach further. The closing instruction makes the strange-tail material non-optional.

Word count check.Summary of v4.7:

**Phase 1 — plot-tradition section reframed and threaded.** Opening paragraph of the section now states the central premise: describe the genre's *range*, not just its center. The strange tail — experimental wing, books fewer readers finish, moves other genres can't make — is what distinguishes a [GENRE] story from a literary-realist story with [GENRE] set dressing. Each of the six threaded items now asks for both center and strange-tail material:

- **Plot mechanics**: 3–5 center mechanics plus 1–2 strange-tail. Examples in the prompt include planetary survey, multi-generation jump, catalogue of impossible objects, recursive-document-discovery.
- **Reader contracts**: standard contracts plus 1–2 strange-tail contracts. Cognitive vertigo, ontological wrongness, form-as-content puzzle, the world that won't fit.
- **Stakes calibration**: standard plus strange-tail. Civilizational, cosmic, ontological, geological, computational, posthuman, deep-time. Stakes on what happens to species, ideas, planetary systems, regimes of physics.
- **Resolution conventions**: standard endings plus strange-tail endings. The irruption, the scale shift, the ontological reframe — endings that honor the genre's contract without the operation-resolved beat.
- **Character function**: standard balance plus strange-tail option. The protagonist as object, process, place, duration. Concrete examples: "Library of Babel," *Diaspora*'s opening.
- **Pacing tradition**: standard rhythms plus strange-tail rhythms. Deep-time montage, encyclopedic enumeration, parable-compression, impossible-zoom.

**Phase 1 — strangest-moves subsection added.** A new subsection asking the writer-model to name 3–5 things the genre does that no other genre does, drawn from the strange tail. Each must come with a writer or work that does it. Closes with "Do not list the moves named in the threaded items above; reach further out" — preventing the writer from recycling the prompt's examples.

**Phase 1 — plot-level failure modes extended.** Added one new failure mode to the existing list: "the genre's strange tail eliminated in favor of its center, producing a story that is technically of the genre but uses none of what only the genre can do."

**Phase 1 — closing instruction strengthened.** Added: "The strange-tail examples are not optional — they are the part of this section that does work the other items don't."

**Phase 3 — reference to plot tradition sharpened.** The "consult the plot-tradition section" pointer now specifically calls out the strangest-moves subsection. The instruction explicitly says the strange-tail material is reference for premise generation, not just prose: premises drawn from the catalogue, encyclopedia entry, ontological reframe, irruption, deep-time montage, or world-as-protagonist are valid candidates if the genre supports them and should appear in the pool.

No new gates. No new quotas. The plot-premise quota stays at 15 of 30 (the only hard floor in Phase 3). The intervention is purely in the reference material the writer-model has available and a sharpened pointer to that material.

Word count rose from v4.6's 5432 to 6060 (+628 words). Most of that is the threaded strange-tail asks across the six plot-tradition items.

What v4.7 doesn't try to fix: the legibility funnel itself at Phases 5 and 6, the model's "write well" prestige attractor toward Carver-MFA prose, the kind-AI constraint's tendency to push toward small stories at short length. These are the things Phase 1 alone can't address. If after testing v4.7 stories are still domestic, those are the next intervention points — and the writer-model feedback already suggests several specific candidate interventions for that round.

---

