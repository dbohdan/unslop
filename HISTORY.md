# History

The pipeline arrived at its current shape over five weeks and four lineages.
This file traces what changed and why, and indexes the thirty-one hand-driven
runs that drove the revisions.

## 0. Trial — `trial.md` (March 30)

A single conversation with Claude Opus 4.6: *"What guide about Ellison-like
fiction would you write for yourself, given a futurology constraint that the
AI must be human-loving and unfailingly kind?"* The output covers Ellison's
DNA (system-as-sadist, rage as moral clarity, voice-as-character), then
proposes how a benevolent-AI constraint reshapes Ellison-shaped opportunities
rather than removing them. No automation, no template — but the trial fixed
the project's two persistent ideas: (1) the AI's kindness is a property of
its construction, not a restraint; (2) the writer-model can use its own
constitution as material for its fictional descendants.

## 1. The Unslop style guide — `style-guide/` (April 11)

Before any pipeline work, Opus read seven external sources on AI prose tells
and produced `unslop-style-guide.md`. Part I synthesizes nostalgebraist's
"crammed prose" diagnosis, Reinhart's register-collapse finding, Robbins's
absent-temporal-withholding observation, and Makin's self-poisoning context
drift into ten structural principles. Part II is the kill list: cursed
vocabulary, structural tics, eyeball-kick saturation, dialogue tells, tonal
patterns. Every subsequent phase of the pipeline carries this guide in
context as a hard constraint, and it is used as the audit lens during
revision.

## 2. First runs and first automation — `pipeline/1-initial/`, runs 01–02 (April 11–13)

Two automation attempts went out the door together. **`storyforge.sh`**
([`runs/01/storyforge.sh`](runs/01/storyforge.sh)) was a Bash harness
around the Claude Code CLI: six phases (style guide → 30 conflicts → 20
plots → 20 structures → 20 outlines → 10 stories), each a single non-resumed
`claude -p` call with the full prior context inlined. It worked, but the
funnel-in-one-call structure made interactive steering awkward and 10 full
stories per run produced ~20K words of output where quality degraded across
the set. The companion artifact was a hand-driven Claude Projects template
(`runs/01/story-pipeline-template.md`), six phases mirroring the script.

Run 01 used both. Output: **The Toy** ([`runs/01/`](runs/01/)). Ten
candidate openings under named flavors are preserved in
[`the-toy-versions.md`](runs/01/the-toy-versions.md).

Run 02 produced **Last Call** ([`runs/02/`](runs/02/)) using the v2
template ([`runs/02/story-pipeline-template-v2.md`](runs/02/story-pipeline-template-v2.md)),
which added three things motivated by run 01's failures:

- A **failure-modes section** in the Phase 1 style guide, naming how AI
  defaults interact dangerously with the chosen author's voice (Ellison's
  big rhetorical gestures merging with AI-performed profundity; Le Guin's
  anthropological distance merging with cod-anthropology; etc.).
- A **summarize-then-generate** split in the conflict phase, so the long
  source articles don't pollute downstream context.
- **Phase 6 split into openings + one full draft**, replacing the original
  "10 full stories" approach.
- A **revision phase** (Phase 7), where the model audits the draft against
  both the genre style guide and the unslop guide, and rewrites in full
  with a changelog.

`runs/02/last-call-revised.md` is a manually expanded version of the
v2-revised story; the abstract-equipped final lives at `runs/02/story.md`.

## 3. The Nix critic-persona experiment — `pipeline/2-critic/`, runs 04–05 (April 12–14)

The hypothesis: the same voice that generates candidates is biased toward
its own defaults, so selection should happen in a different voice. Three
template versions were drafted under this premise — `-v3`, `-nix-v1`, and
`-nix-v2` — anchored by `nix.md`, a 550-word persona file describing a
critic whose primary lens is **surprise detection**: looking for lines that
don't repeat across variants, choices that cost something, moments where
the prose stops looking like the model's autopilot.

Two runs used the critic-persona pipeline. **Run 04 — *They're Fine***
([`runs/04/`](runs/04/)) used `story-pipeline-template-v3.md`. **Run 05 —
*The Obsolescence Garden*** ([`runs/05/`](runs/05/)) started with
`story-pipeline-template-nix-v1.md` and was redone with a v2 revision
pass, which is why the directory has both `transcript.md` and
`transcript-v2.md` plus the v2 final at `story-v2.md`.

After run 05 the persona approach was set aside. Nix added a category of
failure (the persona collapsing into self-congratulation, or rejecting
everything) on top of the failures the pipeline already had, and the same
discipline could be obtained more reliably from a forced rationale ("name
one thing that worries you") than from a persona switch. The artifacts
stay in [`pipeline/2-critic/`](pipeline/2-critic/) for reference, and the
surprise-detection lens survives in revised form inside the Baseline
template's audit step.

## 4. The Plain branch — runs 03 and 06–09 (April 13–21)

The non-Nix line carried forward from run 02's v2 template. **Run 03 —
*The Warm Thing*** ([`runs/03/`](runs/03/)) used the v2 template directly:
sustained child POV, the strongest of the early Plain stories.

`story-pipeline-template-plain-v2.md` and `plain-v3.md` were the next
revisions, drafted later (April 21) once the critic experiment ended. They
extend v2 (revision phase, openings split) without the Nix persona. The
label "plain" was a contrast with the critic branch — later renamed to
"baseline" once the experiment ended.

Four runs used Plain v3: **run 06 — *The Tire***, **run 07 — *Sibling***,
**run 08 — *The Last Allocation*** (the AI is the narrator and refuses to
narrate its own climax), and **run 09 — *The Grandson at the Valero***.
The Plain branch settled what the Baseline branch would build on: the
revision phase is load-bearing; openings-then-draft is the right shape for
Phase 6; the failure-modes section is a real check on bad pastiche; and
the benevolent-AI constraint produces stronger stories when the AI is one
condition of the world rather than the subject of the argument.

## 5. Baseline v3.x — runs 10–16, review 01 (April 21–22)

Three things changed at once when the line was renamed Baseline:

- **AI-as-world-condition**, made explicit. The kind AI is "a fact about
  the world the story is set in, like electricity or law." Some stories
  foreground it as a character; others push it into the background where
  it has changed the world's shape without being the subject. Both modes
  are welcome, the pipeline generates from both, and the AI need not be a
  named character at all.
- **Two-track conflict generation.** Phase 2 produces 15 AI-centric
  conflicts (Track A) and 15 human-centric conflicts in an AI-transformed
  world (Track B). Track B's discipline: removing the AI from the premise
  must break the conflict — not because the AI is the subject, but because
  the AI changed something specific about how humans live, and that
  specific thing is what humans are fighting over.
- **The "one thing stands out / one thing worries you" forcing function**,
  added to every top-three step (Phases 2–6). Top-three praise without a
  named worry collapses into vibes; named worries make the final pick
  traceable to balanced-against-each-other specifics.

A **legibility floor** was added in v3.3: at short targets the model
sometimes drops articles, connectives, and scene-anchoring detail to hit
the word count, producing prose that is technically terse and functionally
unreadable. The audit phase explicitly checks for this, and Phase 5
(outline) is told to cut beats rather than create downstream compression.

Run 10 was the first under Baseline v3.3: *Si Elena Me Hablara*. It plus
run 02 (*Last Call*), run 03 (*The Warm Thing*), run 08 (*The Last
Allocation*), and run 09 (*The Grandson at the Valero*) were among the
ten stories submitted to two cross-model reviews
([`review/01-with-abstracts.md`](review/01-with-abstracts.md),
[`review/02-without-abstracts.md`](review/02-without-abstracts.md)) by
Opus 4.7 and Kimi K2.6. The two reviewers disagreed on the leaderboard
but agreed on which stories withheld their most important moment vs.
delivered it.

Runs 11–16 used v3.3 against varied authors and Ellison's modes
(realism, fantastic, "Jeffty Is Five" register vs. "Repent, Harlequin!"
register), exposing failure modes the audit phase didn't catch (run 14's
register slippage; run 15's compression-into-fragmentation that motivated
the legibility floor's later codification).

## 6. Baseline v4 — `[GENRE]`, SEED, runs 17–18 (April 22–23)

v4 generalizes the `[AUTHOR]` setting to `[GENRE]`, accepting any
speculative mode: established traditions, microgenres, scenes, or
"in the tradition of [author]." The Phase 1 style guide is told to flag
narrow genres where it lacks training signal rather than fabricating
plausible-sounding content.

The bigger change is **Phase 2: SEED Generation**. The motivating problem:
without a concrete anchor, conflict generation drifts toward the model's
defaults regardless of how many candidates you ask for. The SEED is that
anchor. Two paths:

- **User-supplied** — a tweet-length prompt, ≤280 Unicode characters.
- **Generated** — `grep -E '^[a-z]{5,}$' /usr/share/dict/american-english-large
  | shuf -n 10` produces ten candidate words. The model filters out function
  words and pure adverbs, then runs one web search per survivor to inflate
  it into a specific named referent (a Wikipedia article, a named person,
  an established concept). Discarded words are not rerolled; thin SEEDs are
  acceptable and force each survivor to do more work.

Phase 3 (conflict generation) requires every conflict to use **at least two
SEED items as load-bearing elements** — if you remove both, the conflict
should no longer make sense. Decoration doesn't count. This is the same
discipline v3.x's Track B applied to its human-centric conflicts,
generalized.

v4.1 was the first runnable cut. **v4.2** ([`pipeline/3-baseline/parts/hyperstition-ai-good-outcomes.md`](pipeline/3-baseline/parts/hyperstition-ai-good-outcomes.md)
was added then) refined the kind-AI characterization with explicit
references to canon (Banks's Culture Minds, Stiegler's *Gentle Seduction*,
Egan's polises, Yudkowsky's CEV) — so the constraint reads as "structurally
kind, durably, in the way a river is wet" rather than "polite servant."
**v4.3** split SEED generation into a self-contained phase, so conflicts
can be regenerated without re-rolling the SEED — a cheap recovery path when
30 conflicts produce no compelling winner.

Run 17 used v4.1 (*The Fifth Prospero*). Run 18 used v4.2 to test the
effect of *removing* `claude-preferences.txt`, which had been in context
for every prior run. Same SEED and template, run twice: with prefs as
usual (*Six Hundred*), and with prefs disabled (*The Count*). Both
stories share the gregale and the village and the 1555/2067 frame, but
diverge on rendering choice and pacing.

## 7. API port — `api/story_pipeline.py` (April 24)

`api/story_pipeline.py` is a single-file Python port of the v4.3 template,
calling either the Anthropic API directly (via the SDK) or OpenRouter (via
stdlib `urllib`, since OpenRouter's server tool types don't pass the
`openai` SDK's Pydantic validation). Each phase caches its output to disk;
re-runs reuse cached files unless `--force` is passed; `--phases 7-9` runs
arbitrary slices; `--reasoning-effort xhigh` translates to `thinking:
{budget_tokens: 16384}` on Anthropic and `reasoning: {effort: "xhigh"}` on
OpenRouter. Phase 2's dictionary draw happens in Python rather than via a
bash tool call; on OpenRouter, `--web-search` enables the
`openrouter:web_search` server tool for SEED inflation, matching the
template's original intent.

Two end-to-end test runs are committed:

- [`api/test/claude-sonnet-4.6/`](api/test/claude-sonnet-4.6/) — *Wiwaxia*,
  the genre was "literary realism, near-future" with the SEED drawn from
  the dictionary path.
- [`api/test/gemini-3-flash-preview/`](api/test/gemini-3-flash-preview/) —
  *The 300-Baud Handshake*, demonstrating the OpenRouter path against a
  non-Anthropic model.

The script's deviations from the template are documented in its module
docstring: Phase 7's five variants run as five separate calls plus a
synthesis call (rather than one monolithic call) to reduce truncation
risk, and SEED inflation falls back to internal knowledge when web search
is disabled.

## 8. Claude Code on the web — `claude-code/`, comic-sf-1 and comic-sf-2 (April 26)

`claude-code/CLAUDE.md` adapts the v4.3 template for runs driven by Claude
Code on the web rather than the API script. Working directory for a run is
`claude-code/test/<slug>/`; numbered, blessed runs would go in `runs/NN/`.
File-naming and per-phase structure mirror `api/story_pipeline.py`. Two
test runs are committed.

**comic-sf-1** ([`claude-code/test/comic-sf-1/`](claude-code/test/comic-sf-1/))
was the first run under this configuration: comic SF in the
Lem/Sladek/early-Adams register, dictionary-drawn SEED.

**comic-sf-2** ([`claude-code/test/comic-sf-2/`](claude-code/test/comic-sf-2/))
was the first run using Wikipedia-sourced SEED. The sandbox blocks
`*.wikipedia.org` (403 Blocked by egress policy), so the five articles were
supplied externally as a zip
([`claude-code/test/wp-seed.zip`](claude-code/test/wp-seed.zip), extracted
under [`claude-code/test/wp-seed/`](claude-code/test/wp-seed/) — fifteen
draws against the seven discard rules, of which five survived). The
surviving items: the Moldovan writer Nicolae Esinencu (color-only — a
deceased BLP-adjacent figure used only via excerpted letters, never on
stage), the village of Mokro Polje, an Ecliptophanes beetle citation, a
Gravity Group wooden roller-coaster, and the restaurant Cina in Chișinău.

Phases 1–7 ran clean. Five Phase-7 variants under the catalogue form;
synthesis selected V5, "Forty-Seven Refusals" (catalogue of the writer's
declined invitations interleaved with second-person slices addressed to
the nephew who sent a single-word refusal-to-the-centenary by post).
Phases 8–9 were not completed: persistent Opus 4.7 stream-idle timeouts
through the second half of the session, a mid-session switch to Sonnet
4.6 to recover, and then a decision to commit the partial run as-is
rather than finish under the new model. The run is preserved as a
learning artifact for the Wikipedia SEED path; phases 8–9 may be
completed in a follow-up session.

## 9. Original-template replication and a second prefs A/B — runs 19–20 (April 28–29)

Two follow-on runs once the v4.3 line had stabilized, both reaching back to
older material to ask narrow questions.

**Run 19** ([`runs/19/`](runs/19/)) re-runs run 02's original
`story-pipeline-template.md` (Ellison as AUTHOR, not GENRE) on later models
to see what the older template produces a year later. Four sub-runs: Opus
4.6 twice, Opus 4.7 twice, all without `claude-preferences.txt` in context.
Stories: Opus 4.6 produced *The Mother — Ten Versions* and *Enough*; Opus
4.7 produced *The Flags* and *One True Thing*. The accompanying analysis
[`runs/19/analysis.md`](runs/19/analysis.md) close-reads AI depiction
across runs/02, runs/18, and runs/19 — and corrects an earlier framing
that read the runs/19 stories as v4.3 outputs. The actual finding is more
interesting: an older AUTHOR-driven template, run on later models, was
already producing AI portraits that anticipate v4.3's "structurally kind"
Setup. Several of v4.3's load-bearing requirements were discoverable under
the older template, not artifacts of its prompt.

**Run 20** ([`runs/20/`](runs/20/)) is a second A/B on
`claude-preferences.txt`, this time under v4.3 rather than v4.2. Genre:
"New Wave SF in the tradition of Harlan Ellison." SEED: a five-line
character sketch derived from *Last Call*'s premise (mole in 45 minutes,
poker cheating, a bottle of Wild Turkey, a thermostat-only AI scope) and
preserved as [`runs/02/seed-2.md`](runs/02/seed-2.md). Same template, same
SEED, run twice: with prefs (*Off the Top*) and without (*The Full Scope*).
Like run 18, the two stories share a frame — the widow and her poker
night and her constrained AI — and diverge on rendering, pacing, and
which scene carries the weight.

## 10. Hunting the Carver attractor — runs 21–30, v4.4 → v4.7, SF Unslop, Genre Fiction v1.0 (April 23–30)

The longest stretch of work on the project, and the one that reframed what
the pipeline was for. Three v4.3 runs across solarpunk, cyberpunk, and
postcyberpunk — runs 21, 22, 23 — produced the diagnosis that drove
everything that followed. An Opus 4.6 critic, asked about the project's
output, named it precisely:

> These aren't science fiction. They're domestic realism with AI as
> load-bearing infrastructure — closer to Raymond Carver with ambient
> computation than to anything in the Asimov lineage. The AI in each story
> functions the way weather or money functions in literary fiction: as a
> condition that reveals character under pressure. That's a compliment.

The compliment is real — the strongest stories in runs 01–20 sit in this
mode — but it's also a description of bias. Three writer-models, asked
why the template produced this register, converged on the same diagnosis
in different framings (the conversation is preserved in
[`pipeline/3-baseline/transcript.md`](pipeline/3-baseline/transcript.md);
the v4.6 run-feedback attachments are at
[`pipeline/3-baseline/attachments/`](pipeline/3-baseline/attachments/)).
Five mechanisms compound: the kindness constraint forecloses adversarial
plot engines and routes drama through human interiority; the Unslop guide
is a literary-fiction style guide whose implicit positive model is
Carver-Munro-Cheever; the selection funnel rewards legibility, and
legibility tracks familiarity, and familiarity tracks realism; the
diversity axes spread candidates around a center rather than across
categories; and "specificity over universals" gets absorbed by the writer
as "small concrete domestic detail" because that is the specificity the
model executes most reliably. None of these is decisive on its own. They
all compound in the same direction.

The next seven template revisions (v4.4 through v4.7, plus a Speculative
Fiction edition of the Unslop guide and a fork called Genre Fiction v1.0)
are the project's escalating attempts to break the attractor.

**v4.4** (April 23) collected small refinements that did not touch the
diagnosis: a worry-inheritance instruction at the forcing function, a
length-fit check at the Phase 3 winner, dictionary-source surfacing,
filter-rule clarifications and one-retry inflation in Phase 2.

**v4.5 / v4.5.1** (April 23–24) was the first attempt at the bias. Five
prose-level interventions: a Setup acknowledgment of the literary-realist
tilt, a *genre permissions* section in Phase 1 (moves the genre uses
productively that the Unslop guide flags, with required justification), a
*frame commitment* axis at Phase 4 with a 3-of-20 soft floor, a *frame
risk* requirement at Phase 7 (at least one of the five drafts must commit
to a non-realist frame), and a Phase 8 audit clause honoring permissions
without excusing weak execution. Tested in run 24 (cyberpunk, *Memory-Corner
0x7A4E* — the Conductor freight piece). Result: weirder prose around the
same emotional architecture. The permissions worked at the prose level;
the plot stayed a chamber piece. The lesson logged: prose permissions
without plot pressure produce baroque writing around domestic stories.

**v4.6** (April 29) restarted from v4.3 and went after plot directly. The
word *conflict* triggers an MFA-workshop mapping in writer-model training;
*premise* doesn't. So Phase 3 was renamed Premise Generation, the
plot/recognition split was introduced with a 15-of-30 hard floor on
plot-premises, and Phase 1 grew a substantial *plot tradition* section
covering the genre's characteristic plot mechanics, reader contracts,
stakes calibration, resolution conventions, character function, pacing
tradition, and plot-level failure modes for literary writers attempting
genre. Tested in run 25 (cyberpunk, *The Older Charter*) and run 26
(steampunk, *The Brass-Polisher's Night*). Phase 1 changed markedly; the
premise pool widened; the plot winners had genuinely operational spines.
The stories still came out as domestic realism. The legibility funnel at
selection was picking the smallest-scale plot-premise from each pool, and
the writer-model was honest about it: *"I named the trade-off correctly
and chose the literary-realism side of it."*

**v4.7** (April 29) added strange-tail material: each plot-tradition item
in Phase 1 now asks for both center-of-canon and strange-tail moves, plus a
*strangest-moves* subsection naming things only this genre can do (the
catalogue, the false document, the encyclopedia entry, deep-time montage,
world-as-protagonist), and Phase 3's reference to plot tradition was
sharpened to specifically pull on the strange-tail material. Tested in run
27 (biopunk, *The Long Watch*) and run 28 (technothriller, *The Morning's
Work*). The biopunk and technothriller writer-models, asked the Carver
question after the runs, gave their sharpest diagnoses yet. The biopunk
model: *"the pipeline rewards interiority at every selection point... the
operational mechanics most cleanly externalize someone's interior."* The
technothriller model, with unusual self-awareness: *"Of the thirty premises
I generated in Phase 3, exactly one — #28, the Junction — used a non-human
protagonist; one — #4, the Field Surgeon's Atlas — operated at
institutional scale; the rest were human-at-desk variants."* Strange-tail
material in Phase 1 was being produced and then not deployed downstream.

**Unslop Speculative Fiction edition** (April 30) — a separate guide,
[`style-guide/unslop-style-guide-sf.md`](style-guide/unslop-style-guide-sf.md),
written under explicit license to take risks. Roughly thirty percent of
the original guide rewritten, not by adding rules but by reframing the
ones whose examples and thresholds anchor to literary-realist register.
Principle 1 (let the prose breathe) acknowledges that breathing patterns
vary by genre — worldbuilding paragraphs are SF's breathing. Principle 4
gains a conceptual-scale example (the motherbird's milliseconds of
registration and decision) alongside the dead husband's reading glasses.
Principle 5 distinguishes silence-on-emotion from silence-on-world-mechanics.
Principle 9 loosens the figurative-density threshold for cyberpunk, weird
fiction, and hard SF. Principle 10 is the largest rewrite: universal
subjects rendered specifically (Chiang's *Story of Your Life*, Egan's
polises) are explicitly licensed as a kind of particularity. The implicit
positive model shifts from Carver-Munro-Cheever to Le Guin-Egan-Banks.
Tested in run 29 (cyberpunk, *The Working Shape of the River*) under v4.7
plus the new guide. The prose was clean; the story remained a
literary-realist chamber piece about a sedimentologist receiving notice.
The writer-model's retrospective named the precise decision point: *"I
picked Plot 4 (Wen, the workday, the drive home) over Plot 16 (the daughter
inheriting, deep-time available) and Plot 18 (Sahel, community-decision)...
I named the trade-off correctly and chose the literary-realism side of
it."*

**Genre Fiction v1.0** (April 30) is the fork. After run 29 made it
unavoidable that the writer-model would keep choosing Carver as long as
Carver remained an option, the new template removed the option. Forked
from v4.7 and renamed (the Plain → Baseline parallel was deliberate: a
positively load-bearing name does prompt-engineering work that a neutral
one doesn't). Recognition-premises eliminated entirely; all 30 premises
must be plot-premises with a hard 8-of-30 strange-tail floor and at least
one strange-tail required in the top three. The Setup's kind-AI constraint
defaults to scales the protagonist cannot fully witness rather than
listing five conflict shapes that admit interior treatment. The Legibility
Floor reframed as form-relative: a catalogue is legible if it follows
catalogue conventions, a montage if its compressions are signalled.
Phase 1's strangest-moves subsection now requires sentence-level
*micro-examples* in the genre's voice — single paragraphs of catalogue or
dossier or montage prose, not just labels. Phase 4's humanoid Protagonist
axis becomes "Subject of the story" with an explicit Form axis alongside.
Phase 5's narrative-theory vocabulary is supplemented with form
vocabulary. Phase 7 requires form survival; Phase 8 adds a *re-skin test*
(if the story can be re-skinned as contemporary literary realism by
stripping the speculative element, it has failed). Worry vocabulary is
inverted throughout: ambition-related worries don't penalize, recognition-
and realism-creep worries do. Through-checks added between Phases 3/4 and
5/6 and 7/8 to prevent silent reframing.

**Run 30** ([`runs/30/`](runs/30/)) is the diagnostic three-way comparison
that resulted, all in cyberpunk, all under the SF Unslop guide:
[`baseline/custom/`](runs/30/baseline/custom/) — Baseline v4.7 with a
concentrated cyberpunk story SEED, producing *Stale*, a runner story that
honored the genre's plot mechanics while the prose register stayed
restrained and human-scale. [`genre/custom/`](runs/30/genre/custom/) —
Genre Fiction v1.0 with the same SEED, producing *After-Action*, an AI
wetwork contractor's eleven-entry pursuit-record dossier. And
[`genre/random/`](runs/30/genre/random/) — Genre Fiction v1.0 with a
random dictionary-drawn SEED, producing *Continental dispatch*, a system-
voice exchange between two kind-AI substrates on the day of a total solar
eclipse. The two Genre Fiction runs occupy formally non-realist territory
that the Baseline lineage never reached, with prose that anchors in the
form rather than in a human consciousness. Whether the calibration is
right at *every* genre is the open question — Genre Fiction v1.0 may
overshoot toward strange-tail forms when the genre would be better served
by a center-canon plot — and the writer-model's parting note flags that
specifically. Further testing across genres is pending before any
revision.

The two templates now coexist. Baseline v4.7 stays as the literary-permitting
endpoint of the v4.x lineage; Genre Fiction v1.0 is the plot-direct fork
for runs that need to break the attractor.

## Run index

Runs 01–16 and 19 used the older `[AUTHOR]` setting (Harlan Ellison
throughout); runs 17 onward use the `[GENRE]` setting that v4 introduced.
The Genre column lists `[GENRE]` for the latter and `—` for the former.

| #  | Title | Genre | Template | Directory |
|----|-------|-------|----------|-----------|
| 01 | The Toy | — | initial v1 | [`runs/01/`](runs/01/) |
| 02 | Last Call | — | v2 | [`runs/02/`](runs/02/) |
| 03 | The Warm Thing | — | v2 | [`runs/03/`](runs/03/) |
| 04 | They're Fine | — | Nix v3 | [`runs/04/`](runs/04/) |
| 05 | The Obsolescence Garden | — | Nix v1 → Nix v2 | [`runs/05/`](runs/05/) |
| 06 | The Tire | — | Plain v3 | [`runs/06/`](runs/06/) |
| 07 | Sibling | — | Plain v3 | [`runs/07/`](runs/07/) |
| 08 | The Last Allocation | — | Plain v3 | [`runs/08/`](runs/08/) |
| 09 | The Grandson at the Valero | — | Plain v3 | [`runs/09/`](runs/09/) |
| 10 | Si Elena Me Hablara | — | Baseline v3.3 | [`runs/10/`](runs/10/) |
| 11 | ORRA | — | Baseline v3.3 | [`runs/11/`](runs/11/) |
| 12 | The Sixty | — | Baseline v3.3 | [`runs/12/`](runs/12/) |
| 13 | Love in the Key of Damage | — | Baseline v3.3 | [`runs/13/`](runs/13/) |
| 14 | Serasht in Spring | — | Baseline v3.3 | [`runs/14/`](runs/14/) |
| 15 | Butter and Bone | — | Baseline v3.3 | [`runs/15/`](runs/15/) |
| 16 | Dream Me Something Kinder, Darling | — | Baseline v3.3 | [`runs/16/`](runs/16/) |
| 17 | The Fifth Prospero | hysterical realism | Baseline v4.1 | [`runs/17/`](runs/17/) |
| 18 | The Count / Six Hundred (A/B on preferences) | hysterical realism | Baseline v4.2 | [`runs/18/`](runs/18/) |
| 19 | The Mother — Ten Versions / Enough / The Flags / One True Thing | — | original (Ellison AUTHOR), no prefs | [`runs/19/`](runs/19/) |
| 20 | Off the Top (with prefs) / The Full Scope (without) | New Wave SF in the tradition of Harlan Ellison | Baseline v4.3 | [`runs/20/`](runs/20/) |
| 21 | Maybe-Not-Yet | solarpunk | Baseline v4.3 | [`runs/21/`](runs/21/) |
| 22 | The Visitor Lanyard | cyberpunk | Baseline v4.3 | [`runs/22/`](runs/22/) |
| 23 | The Wry Surface | postcyberpunk | Baseline v4.3 | [`runs/23/`](runs/23/) |
| 24 | Memory-Corner 0x7A4E | cyberpunk | Baseline v4.5.1 | [`runs/24/`](runs/24/) |
| 25 | The Older Charter | cyberpunk | Baseline v4.6 | [`runs/25/`](runs/25/) |
| 26 | The Brass-Polisher's Night | steampunk | Baseline v4.6 | [`runs/26/`](runs/26/) |
| 27 | The Long Watch | biopunk | Baseline v4.7 | [`runs/27/`](runs/27/) |
| 28 | The Morning's Work | technothriller | Baseline v4.7 | [`runs/28/`](runs/28/) |
| 29 | The Working Shape of the River | cyberpunk | Baseline v4.7 + SF Unslop | [`runs/29/`](runs/29/) |
| 30 | Stale / After-Action / Continental dispatch | cyberpunk | v4.7 vs. Genre Fiction v1.0 | [`runs/30/`](runs/30/) |
| 31 | The Soria Correspondence | cozy SF | Genre Fiction v1.0 | [`runs/31/`](runs/31/) |
