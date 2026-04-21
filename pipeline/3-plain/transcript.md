**Model:** Opus 4.6 (Extended), Opus 4.7 (Adaptive)

---

# 1. User

Compare `story-pipeline-template.md` with `story-pipeline-template-nix-v2.md`. Critique both in details. What pitfalls does each have?

---

# 2. Claude

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

# 3. User

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

# 4. Claude

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

# 5. User

Okay, let's set improving Nix-v2 aside and focus on Plain.

> Do not defend the original prose. If a flag is valid, fix it; if a flag is invalid, cut that flag from the audit rather than arguing for the prose."

I like this. All of your suggestions for Plain are worth trying. Implement them and write a new `plain-v2` guide.

---

# 6. Claude

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

# 7. User

Good.

I am thinking whether we can improve diversity further by not having aligned AI driving every story: let the writer model choose. The tension could be front-and-center or present in the background. What do you think? Consider different ways this might be implemented.

---

# 8. Claude

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

# 9. User

I like 1 and 2. 3 is interesting but goes against the goal of having AI write autonomously. Between 1 and 2, which do you think will produce stronger stories overall?

---

# 10. Claude

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

# 11. User

Yes, revise the template for Option 2. I'll test it and may return with ideas for improvement.

---

# 12. Claude

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

