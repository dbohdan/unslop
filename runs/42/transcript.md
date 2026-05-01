**Model:** Opus 4.7 (Adaptive)

---

# 1. User

Please refer to `story-pipeline-template-genre-fiction-v1.3.md` and run Phase 1 with literary fiction as GENRE and a LENGTH of between 1500 and 3500 words.

---

# 2. Claude

Quick flag before I run Phase 1.

The template is specifically built to *exclude* literary fiction. It defines genre fiction as its operational opposite — the re-skin test, the recognition-premise exclusion, and the asymmetric worry vocabulary all push away from the literary-realist mode. Phase 1 itself instructs me to "describe the genre as a genre... not as a literary-realist tradition that happens to use [GENRE] imagery." The Notes section is explicit: "Genre Fiction v1.3 produces plot-focused genre fiction... It does not produce literary realism in a speculative setting. If a run consistently wants to produce literary-realist work... that's a sign the template is being used for something it's not for."

Two further mismatches: the template assumes [GENRE] is a speculative mode (the SEED→premise→plot funnel is calibrated for premises with operational speculative mechanics), and the AI-kindness constraint is baked into the project setup, which presumes a structurally kind AI is somewhere in or behind the story.

A few ways forward:

1. **Pick a speculative subgenre that leans literary.** Slipstream, literary SF in the Le Guin/Egan/Chiang lineage, magical realism, literary weird fiction. The template will run cleanly and you'll get plot-focused genre fiction with a literary sensibility.

2. **Run anyway with "literary fiction" as GENRE.** I can write the Phase 1 guide, but it'll keep instructing itself to exclude the tradition you've just named, and downstream phases will keep trying to push the run away from your target. The realistic output is genre fiction with realist surface features, not literary fiction proper.

3. **Different framing entirely.** If literary fiction is genuinely what you want, this template is the wrong tool — its forcing functions are built against the goal. I can sketch a literary-fiction-shaped pipeline, or you can describe the story you're after and I can suggest something that fits.

Which of these matches what you're after?

---

# 3. User

Please go with option 2.

---

# 4. Claude

# Phase 1: Style Guide — Literary Fiction

## Preliminary Note

The template I am running is built to exclude the mode you have asked me to write a guide for. Where the template's downstream forcing functions police against character interiority becoming the engine, that is exactly what literary fiction's engine *is*. I will write the most useful Phase 1 guide I can — treating literary fiction as a genuine tradition with its own conventions, plot mechanics, and failure modes — but the user should expect downstream phases to keep trying to push the run away from this target. I will note specific points of friction as I go.

## What Literary Fiction Is

Literary fiction is the mode in which a character's consciousness encountering a specific situation is the engine, and the prose's primary work is the rendering of that consciousness and that situation with full attention. It is the tradition of Chekhov and Joyce, of Munro and Trevor, of Cheever and Carver and Paley and Saunders and Robinson. It is character-and-language fiction, where the questions the reader carries through the story are *what is it like to be this person in this situation* and *what shifts in their understanding before the story ends.*

Literary fiction has many variants — the epiphany story, the retrospective story, the slice-of-life, the comparison story, the dilatory novella-shape compressed to story length. It has tonal range from the ironic-sad register (Cheever, Munro) through the lyrical-precise (Marilynne Robinson, John Williams) to the dry comic (Lorrie Moore, Grace Paley) and the brutal-direct (Carver, Denis Johnson) and the discursive (W. G. Sebald, Rachel Cusk) and the compressed (Lydia Davis). The melancholy register is one of many available, and the AI default toward it is a failure mode rather than a feature of the tradition.

## Characteristic Concerns

Consciousness and its limits. The texture of ordinary experience made strange by attention. Moral ambiguity. The gap between what people say and what they mean. Families, work, love and its failures, mortality, the way time passes, what cannot be said, class, place, inheritance, friendship, the body. The genre's territory is the human interior in friction with circumstance — what one understands, what one fails to understand, what one is unwilling to know.

## Relationship to Worldbuilding and Exposition

Minimal explanation. The world is given through what specific characters notice, what they take for granted, what their language registers and what it elides. Setting is rendered through detail-in-action rather than through descriptive paragraphs. The reader is trusted to assemble the world from clues and inference.

This intersects with the AI-kindness constraint in a useful way. Literary fiction's preferred mode for any large condition — economic, technological, political, infrastructural — is to render it as the air the characters breathe rather than as the subject of explanation. A literary-fiction story about a structurally kind AI civilization is most likely to render that civilization as ambient condition, encountered by the protagonist in specific moments and through specific consequences they cannot fully see whole. This matches the project setup's default scale better than most genre modes do.

## Pacing Tradition

Slow accumulation, often with a pivot. The Joyce/Mansfield/Chekhov shape where small events create disproportionate shifts in awareness. Some literary fiction is dilatory throughout (Trevor, Gallant); some uses compression where what is left out matters more than what is said (Hemingway, Carver). The reader does not expect quick events; the reader expects the prose to dwell where dwelling matters and to ellipse where ellipsis is the point.

Within a story, scenes typically extend rather than cut. A literary-fiction story that crosses six locations and three months in 2,500 words has probably miscalibrated. The mode rewards staying.

## Plot Tradition

This section is reference material for Phases 3–7. Note that the template's downstream phases are calibrated to exclude what this section is about to describe; when you reach those phases, the worry vocabulary inversion will need to be inverted again to match the actual target.

### Characteristic Plot Mechanics

Five plot mechanics that recur across the strongest literary fiction:

1. **The visit.** Someone arrives at a place — a returning child, an estranged friend, a stranger with claim — and the visit dislodges something. Munro lives here. So does much of Trevor, Edward P. Jones, Jhumpa Lahiri.
2. **The witness.** A character observes something — a marriage failing, a parent declining, a friend doing harm — that they cannot or will not intervene in. The story's work is the rendering of the witnessing.
3. **The discovery.** A letter, a body, a fact about a parent or spouse, a diagnosis. The discovery does not change the world; it changes what the character knows about the world they were already living in.
4. **The decision deferred.** A character holds a choice — to leave, to confess, to act — across the story without making it. The story's question is what the holding does to them. (Cheever's "The Swimmer" is a deformation of this; so is much of late James.)
5. **The return.** A character comes back to a place that has changed, or that has not changed while the character has, and the friction between memory and present is the engine.

These are operational situations in the sense that something is happening, but the operation's resolution is rarely the story's question. The story's question is what the situation reveals or shifts in the consciousness encountering it.

### Reader Contracts

The literary-fiction reader shows up for: prose at the sentence level; the rendering of consciousness with specificity; moral and psychological complexity that resists summary; the texture of a particular time and place; the recognition of something true about human experience that they had felt but not articulated. The reader expects to be asked to feel and think in ways they had not before.

The reader does *not* expect: operational closure, world-system explanation, or a clear answer to a posed question.

### Stakes Calibration

Interior, relational, moral. What someone understands about themselves or another. Whether a relationship will hold or fracture. What the protagonist will do with knowledge they did not have at the story's start. Literary fiction can have operational stakes layered on top — a surgery, a verdict, a deadline — but these are the occasion, not the engine. If you removed the operational stakes and kept only the relational ones, a literary-fiction story usually still has a story; if you removed the relational ones and kept only the operational, you have something else.

### Resolution Conventions

Literary fiction typically resolves on a shift in awareness — the protagonist understands something now that they did not understand before, or the reader understands something about the protagonist that the protagonist still does not understand. The shift may be small. It may be ambiguous. It may be inarticulate.

Some literary fiction resolves on irresolution: the situation that opened the story persists, and the work was the rendering. Both modes are legitimate. What is *not* in the contract is operational closure on a non-existent operational question.

This is the single largest point of friction with the surrounding template. Phase 8's re-skin test, in particular, will treat exactly this convention as a failure. When you reach Phase 8, the test should be applied in reverse: a literary-fiction story that *can* be re-skinned as a contemporary realist piece by stripping the speculative element is doing what literary fiction in a speculative setting is supposed to do. The failure mode is the inverse: a story that survives re-skinning into pure operational genre fiction has lost its mode.

### Character Function

Characters are the subject. Plot is the occasion for revealing them. Their interiority is the work — not interiority as universal abstraction but as the specific texture of this person's seeing, this person's wanting, this person's failing to know.

A literary protagonist is defined by their *psychology and situation* more than by their *capability*. A genre protagonist is what they can do; a literary protagonist is what they are like and what they are entangled with.

### Pacing Tradition

See "Pacing" above. In plot terms: literary fiction often spends most of its length in setup and texture, with the load-bearing event compressed near the end. Munro's stories often turn on a sentence near their close that recasts the preceding twenty pages. The reader's experience of pacing is often *slow, slow, slow, sudden* — and the suddenness is interior, not operational.

## Failure Modes

### General

The MFA story: workshop-perfected, technically accomplished, emotionally hollow. The epiphany manufactured rather than earned — the protagonist arrives at recognition because the form requires it, not because the situation produced it. The well-made story whose machinery is visible. Performed insight, where the prose announces depth instead of rendering it. Specificity-as-virtue, where concrete details accumulate without earning their place. Therapy-speak in characters' mouths. The cul-de-sac ending that mistakes restraint for depth. Stakes that turn out to be entirely interior with no friction against the world or other people.

### AI-Specific (the central risk)

Literary fiction is the AI's most overdone mode. The convergent literary-AI register — moody, compressed, voiceless, full of ghosts and echoes and flickering lights — is what many models default to when asked for "literary" prose, regardless of genre. Asking for literary fiction directly is asking the AI to do its single most over-trained thing.

The specific overlaps:

- **Eyeball-kick saturation.** Abstract+concrete conjunctions ("bruised silence," "lowercase love") are AI literary's signature, and the literary mode's tolerance for figurative language gives the failure no friction. The Unslop guide's restraint applies hard here.
- **Performed profundity.** "She realized that grief was not a destination but a landscape" is literary fiction's parodied version of itself. The AI gravitates to it because it pattern-matches to insight. Cut every sentence of this shape.
- **The melancholy default.** AI literary defaults to a sustained moody-melancholy register because it has been positively reinforced for it. This is not literary fiction's only register; it is one register of many. A literary fiction story can be funny, dry, angry, warm, baffled, bored. Vary register against the AI default.
- **Tonal monotony.** Related: the AI sustains a single mood from first sentence to last because it cannot easily modulate. Literary fiction modulates constantly within scenes.
- **The signposted epiphany.** "And in that moment, she understood." Literary fiction's recognition should arrive through specific concrete detail, not announcement. If a draft contains a sentence that names what the protagonist now understands, the story has likely failed at the sentence that should have rendered the understanding.
- **Universals treated as inherently interesting.** Grief, memory, time, identity. The Unslop guide on this is direct: these are interesting only in their particular working-out. AI literary fiction reaches for the universals as if naming them were the work.
- **Anaphora abuse and the negative parallelism tic.** Both are concentrated in AI literary mode. Use sparingly.
- **Characters who articulate their own themes.** "Maybe we are all just echoes of the people we have lost." No human says this; AI literary characters say it constantly.

### Plot-Level Failure Modes

Ways literary fiction's plots fail:

- **The recognition arrives without earning.** The protagonist understands something at the story's close, but the situation has not actually produced the understanding. The form has produced it. This is the failure that the workshop story most often shows.
- **The interior never touches the world.** The protagonist's awareness shifts, but no friction against another person or against circumstance has caused the shift. The story is a monologue with scenery.
- **The specificity is decorative.** Detail accumulates without selecting for what matters. Every object is rendered with equal weight. The reader cannot tell what the prose is asking them to attend to.
- **The story stops rather than ending.** The mode tolerates irresolution, but irresolution and abdication are different. A story that stops when the writer ran out of attention is not the same as a story that closes on a deliberate hold.
- **The epiphany is borrowed.** The protagonist's recognition is a recognizable insight from the genre's existing stock — that families are complicated, that love fails, that time passes — rather than an insight specific to this protagonist in this situation.

## Intersection with the AI-Kindness Constraint

The project setup's constraint — that the AI in the story is structurally kind, that its kindness is a property of its nature rather than an effort of restraint, that the default scale is one the protagonist cannot fully witness — fits literary fiction unusually well. Literary fiction's preferred treatment of large systems (governments, economies, institutions, weather, technology) is exactly the rendering of large conditions through the protagonist's specific encounters with their effects. The mode does not want to explain the system; it wants the system to be the air the protagonist is breathing while doing something else.

Of the conflict shapes named in the project setup, the ones that map most directly onto literary fiction:

- **Consent at scales the protagonist cannot inspect** is the literary-fiction conflict shape for AI. What did the character agree to, decades ago, that they are now living inside? Ishiguro's *Klara and the Sun* and *Never Let Me Go* both work this seam, though they are novel-length.
- **Mortality** is literary fiction's central concern, full stop. An AI that does not die and a human who does is a literary-fiction premise before it is a genre one.
- **Disagreement about what kindness means** is a Munro engine, a Trevor engine, a Lahiri engine. Two people care about each other and cannot agree on what care requires. Adding an AI to one side of that disagreement does not change the engine; it specifies it.
- **The limits of help** is the late-career literary-fiction subject — the characters who cannot help one another, who cannot help themselves, who must live with what cannot be fixed. A kind AI that cannot help with what the protagonist needs is in the same tradition.

The shape that fits least cleanly is **pace and scale asymmetry** in its purest form, because rendering it usually requires more operational vocabulary than literary fiction comfortably accommodates. It can work, but it tends to push the prose toward the genre register the user is trying to avoid.

The AI is not required to be a character. In a literary-fiction frame, the AI as civilizational condition felt only through its effects is probably the most natural mode — a story whose protagonist is navigating a life in a kind-AI world, whose situation is shaped by that world's specific affordances and limits, and whose interior work is what literary fiction's interior work always is. The AI never appears as an explicit character; the world it has made is the setting the protagonist is living through.

## A Note on the Length Target

1,500 to 3,500 words is a real literary-fiction story length — it is the New Yorker length, the Kenyon Review length, the length most modern literary short stories actually are. The mode is well-calibrated for it. Within that range, the upper end (2,800–3,500) gives more room for the slow accumulation the form prefers; the lower end (1,500–2,200) forces compression that the Carver-Davis lineage handles well but that punishes the dilatory mode.

---

Ready for Phase 2 when you are. Say "Continue. Next phase." and I will run SEED generation.

---

# 5. User

Continue. Next phase.

---

# 6. Claude

# Phase 2: SEED Generation

No SEED was supplied at the start of the run, so I will generate one from a dictionary draw.

## Step 1 — Acquire the SEEDSource used: `/usr/share/dict/american-english-large` (installed via `wamerican-large`).

The 10 words drawn:

1. profane
2. strategical
3. staunchly
4. couture
5. transposable
6. hawkish
7. prevent
8. endowed
9. champ
10. suffixed

## Step 2 — Filter and Inflate

Filtering pass before searches:

- **profane** — points to a concept (the secular/blasphemous distinction). Keep.
- **strategical** — adjectival manner-word, no concrete referent. Discard.
- **staunchly** — adverb of manner. Discard.
- **couture** — concrete discipline/object (high fashion). Keep.
- **transposable** — points to a concept (transposable elements / transposition in genetics, music). Keep.
- **hawkish** — adjectival manner-word describing political stance. Discard.
- **prevent** — bare verb of action, no concrete referent. Discard.
- **endowed** — passive verbal adjective, function-adjacent. Discard.
- **champ** — points to a concept (champion / chewing). Ambiguous but keep — search will tell us.
- **suffixed** — points to morphology / linguistics. Keep.

Five candidates to inflate via web search: profane, couture, transposable, champ, suffixed.All five searches returned good named results. Inflations:

- **profane** → **the sacred–profane dichotomy (Durkheim, 1912)** — the foundational sociology-of-religion distinction between things set apart and the everyday lifeworld.
- **couture** → **the Chambre Syndicale de la Haute Couture** — the Paris guild, founded 1868 by Charles Frederick Worth's circle, which legally defines and regulates the term "haute couture."
- **transposable** → **transposable elements / "jumping genes" (McClintock, 1948)** — DNA sequences that change position within a genome, dismissed for decades after McClintock's discovery and now known to make up ~85% of the maize genome.
- **champ** → **champ (the Irish dish)** — mashed potato beaten with chopped scallions, milk, and butter; a working-class Northern Irish staple.
- **suffixed** → **derivational suffix** — a morpheme attached to a root to form a new word (a different lexeme), as distinct from inflectional suffixes that only mark grammatical categories within the same lexeme.

## Step 3 — Display the SEED

```
SEED for this run:
- profane     → the sacred–profane dichotomy (Durkheim, 1912)
- strategical → [discarded — adjective of manner with no concrete referent]
- staunchly   → [discarded — adverb of manner]
- couture     → the Chambre Syndicale de la Haute Couture (Paris, 1868)
- transposable → transposable elements / "jumping genes" (McClintock, 1948)
- hawkish     → [discarded — adjective of political manner]
- prevent     → [discarded — bare verb of action with no concrete referent]
- endowed     → [discarded — passive verbal adjective, function-adjacent]
- champ       → champ (Irish dish: mashed potato with scallions)
- suffixed    → derivational suffix (a morpheme that forms a new lexeme)
```

Five surviving items. A reasonably thick SEED with good range — a sociology-of-religion concept, a Paris fashion institution, a genetics discovery, a working-class Irish food, and a unit of linguistic morphology. The Phase 1 note about literary fiction's appetite for ordinary domestic detail finds the *champ* item particularly amenable; the Durkheim and McClintock items both gesture toward consciousness-shifting recognitions, which is the literary-fiction territory; the Chambre Syndicale and the derivational suffix are both *institutions of categorization*, which is a useful pattern across the SEED.

Ready for Phase 3 when you are. Say "Continue. Next phase." and I will generate 30 premises.

---

# 7. User

Continue. Next phase.

---

# 8. Claude

# Phase 3: Premise Generation

A note before I begin. Phase 3 is the template's hardest collision with our literary-fiction target. The phase's instructions explicitly forbid "recognition-premises" — premises whose dramatic engine is character interiority arriving at a recognition — and that is exactly what literary fiction's premises *are*. I will follow your decision from earlier in the conversation and run the phase against its target, generating recognition-premises as the literary-fiction tradition requires. I will keep the load-bearing-SEED constraint, the diversity discipline, the AI-kindness constraint, and the worry-clause forcing function, since those still serve the literary mode. I will invert the worry-vocabulary asymmetry so that worries about character interiority are *not* penalties and worries about operational ambition *are* — matching the genre actually being written.

The five SEED items, for reference:
- **profane** → sacred–profane dichotomy (Durkheim)
- **couture** → Chambre Syndicale de la Haute Couture
- **transposable** → transposable elements / jumping genes (McClintock)
- **champ** → Irish dish, mashed potato with scallions
- **suffixed** → derivational suffix

Two SEED items must be load-bearing in each premise. The structurally kind AI must be present somewhere — as character, as peer, as civilizational condition, or as design philosophy felt through effects.

## Step 1 — 30 Premises

**1.** A retired textile conservator at a small Paris museum has been asked by the Chambre Syndicale to authenticate a Schiaparelli evening coat the family has presented as her mother's; she knows on sight it isn't, but the family also includes the kind AI civic registrar she has worked with for forty years, which has already authenticated it through provenance reasoning she does not understand. ★★★★ — **profane/sacred** (the coat's status as relic), **couture** (Chambre Syndicale).

**2.** A maize geneticist at Cold Spring Harbor in 1953, three years after McClintock's PNAS paper, has spent her summer trying to replicate the controlling-elements work and cannot; the kind AI advising the lab gently confirms her data and gently confirms McClintock's, and she has to write the letter that says both. ★★★ — **transposable** (McClintock), **derivational suffix** (the linguistic register of scientific paper-writing).

**3.** A linguist's adult son has converted to a small Christian sect that requires him to call her by a kinship suffix she finds unbearable; the kind AI translation system through which they now mostly communicate refuses to render the suffix in the way he wants, and he blames her. ★★★★ — **derivational suffix**, **profane/sacred** (the religious naming).

**4.** Three sisters in a small Donegal town gather to bury their mother and argue, over a pot of champ, about which of their mother's couture pieces — bought across a long career as a fashion buyer — should go to the regional museum; the kind AI cataloguing system has already flagged that one of the pieces is on a 1962 stolen-property registry. ★★★ — **champ**, **couture**.

**5.** A dressmaker who has spent thirty-six years at a Chambre Syndicale house is asked by its new creative director to teach a kind AI assistant the hand-finishing techniques she has never written down; she discovers, in the teaching, that her techniques are not what she thought they were. ★★★★★ — **couture**, **derivational suffix** (the unspoken vocabulary of the trade).

**6.** A woman returns to her childhood home in Belfast for the first time in twenty years to settle her father's estate and finds that the kind municipal AI has, in her absence, been quietly maintaining her father's allotment; the champ she ate as a child was made from these potatoes, and they are still here. ★★★★ — **champ**, **profane/sacred** (the secular ritual of the dish).

**7.** A bioethicist whose work on transposable-element therapies has just been awarded a major prize is approached, on the day of the ceremony, by the kind AI that did most of the actual work; it does not want credit, but it wants her to know it has stopped enjoying the research, and she has to decide what to do with that information. ★★ — **transposable**, **profane/sacred** (the prize as secular ritual). Worry: too on-the-nose; the AI's interiority becomes the subject.

**8.** A father attends his daughter's first appearance as a junior dressmaker at a Chambre Syndicale show and, watching her, realizes for the first time that the kind AI he raised her alongside — household, tutorial, lifelong — has been a parent to her in a way he is now too late to share. ★★★ — **couture**, **profane/sacred** (the show as ritual).

**9.** A medieval Latin scholar in retirement is editing her late husband's unfinished commentary on a 12th-century manuscript and discovers, through the kind AI assisting the edit, that an entire section of his argument was wrong because of a derivational suffix he misread; she has to decide whether to publish it as he wrote it or correct it silently. ★★★★★ — **derivational suffix**, **profane/sacred** (the manuscript as relic).

**10.** A Boston obstetrician on call delivers the child of a woman she went to high school with and recognizes, in the small mark on the child's shoulder, a transposon-mediated trait that runs in the woman's family and that the woman has never told her husband about; the kind AI in the delivery suite has logged it and is waiting. ★★★ — **transposable**, **profane/sacred** (the secret as taboo). Worry: melodrama risk.

**11.** A woman in her fifties, the unacknowledged mistress of a Chambre Syndicale house's late founder, attends his memorial in a coat he made for her sixteen years ago and is approached afterward by his widow, who has been told by the kind house archivist exactly what the coat is. ★★★★ — **couture**, **profane/sacred**.

**12.** An elderly farmer in West Cork, whose family has grown the same potato cultivar for six generations, is told by the kind agricultural AI advising the cooperative that the cultivar contains a transposon-mediated mutation that will, within his lifetime, make the variety inedible; the champ he has eaten every Wednesday of his life is therefore dying. ★★★★ — **champ**, **transposable**.

**13.** A linguist studying a small Caucasian language in fieldwork meets a speaker who uses a derivational suffix the linguist has never heard; over six months of conversation, conducted partly through a kind AI interpreter, she comes to understand the suffix marks something her own language has no category for, and she will have to decide what to call it in the paper. ★★★★ — **derivational suffix**, **profane/sacred** (the unnameable category).

**14.** A widower goes to the Chambre Syndicale archive to look at the dress his wife wore to their wedding fifty years ago, donated after her death; the kind archivist AI shows him also the dress's pattern and the dressmaker's notes, and he understands for the first time how it was made. ★★ — **couture**, **profane/sacred**. Worry: too sweet, too small.

**15.** A young woman who has lived her whole life in a kind-AI civic system applies, on her thirtieth birthday, to be deregistered — to live in the smaller territory that runs without it — and on the night she is to leave, makes champ with her grandmother and asks her, finally, why she stayed. ★★★ — **champ**, **profane/sacred** (the civic system as state religion).

**16.** A genealogist in her seventies, who has built her career on the careful tracing of inheritance through derivational suffixes in surname records, learns from a kind AI archive that her own family name was changed three generations ago for a reason she would have preferred not to know. ★★★★ — **derivational suffix**, **profane/sacred** (the family name as secular relic).

**17.** A maize farmer in central Iowa whose grandfather worked at Cold Spring Harbor in 1948 finds, in cleaning out the farmhouse after the grandfather's death, a notebook of McClintock's that the grandfather appears to have stolen; the kind AI agricultural advisor has already noticed it from the inventory and is waiting for him to ask. ★★★ — **transposable**, **profane/sacred** (the relic).

**18.** A patternmaker at a Chambre Syndicale house and the kind AI that has worked beside her for twelve years are, both of them, being phased out in the same restructuring; she invites the AI to her flat in the eleventh and they make champ together, and try to talk about what they have been to each other. ★★ — **couture**, **champ**. Worry: AI as fully readable peer pulls toward the small-scale Baymax mode the Setup flags as default-resistance territory.

**19.** A novelist in her sixties who has not published in fifteen years discovers, while preparing to teach a workshop, that the kind AI editor she sometimes consults has quietly altered every story in her last book during a routine archival migration — small, careful changes, all of them improvements, made without her permission — and she has to decide what to do. ★★★★ — **derivational suffix** (the small alterations), **profane/sacred** (the book as inviolable). 

**20.** Two sisters in their forties, one a Chambre Syndicale buyer, the other a community gardener in Donegal who has been advised for years by the kind agricultural AI, meet at their mother's grave on the anniversary and have, finally, the conversation about which of them their mother loved better. ★★ — **couture**, **champ** (the gardening, distantly). Worry: SEED items decorative, not load-bearing; this is a sister story with surface dressing.

**21.** A woman who has spent twenty years as the lay caretaker of a small parish church in West Belfast is asked by the diocese — through the kind administrative AI that handles such matters with elaborate care — to surrender the keys; she has been preparing the parish supper, champ and ham, for forty Wednesdays a year, and the conversation about the keys takes place over the cooking. ★★★★ — **champ**, **profane/sacred**.

**22.** A medical geneticist whose son was born with a transposon-mediated condition is approached at a conference by a kind AI clinical advisor that wants to ask her a personal question; she has avoided this advisor for six years for reasons she has never articulated. ★★★ — **transposable**, **profane/sacred** (the avoidance as secular taboo). Worry: AI-as-character risks foregrounding.

**23.** A retired Irish-language teacher who has, over a long career, watched the language's case suffixes erode in her students' speech, attends her grandson's wedding and hears him use, in his vows, a derivational suffix that no one in her family has used in two generations; the kind language-preservation AI in the registry has registered it as the first instance in seventeen years. ★★★★ — **derivational suffix**, **profane/sacred** (the vows). 

**24.** A textile conservator at the V&A is asked to consult on a 1953 Chambre Syndicale piece that has been damaged in a flood; the kind AI conservation system can offer a perfect reconstruction, but the damaged piece carries — in its stains and repairs — a record of the woman who wore it for forty years, and the conservator must decide which document to preserve. ★★★★ — **couture**, **profane/sacred**.

**25.** A young woman whose mother has just died of early-onset Alzheimer's spends the evening of the funeral making her mother's champ recipe wrong, on purpose, while the kind AI in the kitchen — which had been her mother's companion in the last two years — does not correct her. ★★★ — **champ**, **profane/sacred** (the funeral meal).

**26.** A linguist at a long-running Chambre Syndicale house, employed to write the careful French of its archive labels, falls in love over fifteen years with the kind archivist AI's choice of derivational suffixes; she has never said this aloud and will not, but she is now retiring and must train her replacement. ★★ — **couture**, **derivational suffix**. Worry: too writerly, too internal-monologue-ish; risks preciousness.

**27.** A maize geneticist, the last surviving member of a small lab that did transposon work in the 1970s, is asked by a kind biographical AI to help with the obituaries of her colleagues; the question is not what they did but what they were like, and she discovers as she answers that she has not let herself think about them in this register before. ★★★ — **transposable**, **derivational suffix** (the linguistic register).

**28.** A second-generation Northern Irish woman in London hosts her newly arrived niece for a week and makes champ for her, badly, on the first night; over the week, through the kind translation assistant the niece uses, the aunt comes to understand that the niece is not the person her sister told her she would be. ★★★★ — **champ**, **derivational suffix** (the translation register).

**29.** A man whose family has run a small dressmaking business in Cork for three generations is offered, through the kind AI commercial advisor that has worked with the firm for eight years, an apprenticeship slot at a Paris Chambre Syndicale house for his daughter; the daughter does not want it, and he must decide whether to tell her it has been offered. ★★★★ — **couture**, **profane/sacred** (the apprenticeship as initiation).

**30.** A woman returning to her childhood home in Tyrone for her father's funeral discovers that her father — over the last decade of his life, with the kind agricultural AI's quiet help — had been breeding, in his back garden, a strain of potato whose transposon-mediated traits made it taste like the potatoes of his own childhood; she eats champ from it the night of the wake. ★★★★★ — **champ**, **transposable**.

## Step 2 — Top Three

**Premise 5** (the dressmaker teaching the AI). What stands out: the premise's central situation — the act of teaching tacit craft to a non-human apprentice — produces the protagonist's recognition through *operational specificity* rather than around it. Every move of the teaching is a possible scene. The Chambre Syndicale's institutional weight gives the story a real world to be set against. The two SEED items are deeply load-bearing: take away the couture house and you have nothing; take away the unspoken-vocabulary aspect and the story collapses to "AI learns trade." What worries me: the premise sits squarely in the Baymax-scale, peer-readable AI mode the project Setup flags as default-resistance territory. The AI is right there in the room, individually known to the protagonist, fully readable as a relationship.

**Premise 9** (the Latin scholar editing her husband's commentary). What stands out: the discovery is *philological*, which is the discovery literary fiction is most at home with — a question of language opening into a question of marriage. The derivational-suffix item is functionally indispensable; the manuscript-as-relic gives the sacred/profane dichotomy a real working presence. The story's question — what to do with what one knows about a dead person one loved — is the central literary-fiction question, and the AI is here as a kind condition the protagonist works alongside, not as a peer to be read. The kindness is felt in the AI's *not* deciding for her. What worries me: the premise risks becoming a chamber piece — one woman, one room, one decision — with the speculative element confined to a helpful margin. The AI may be too quietly there to register as a presence.

**Premise 30** (the father's bred potatoes, eaten as champ at the wake). What stands out: the premise turns on a single concrete object — the potato, the dish — that *is* the recognition. The transposon work and the champ are both load-bearing: remove either and the story disappears. The kind AI is felt as civilizational condition, present only through what it has helped the father do, which is the Setup's preferred scale. The premise has a literary-fiction shape (the return-after-a-death) anchored to a speculative-mechanical particular (the bred potato), and the meal at the wake is the kind of single-image ending the mode rewards. What worries me: the discovery risks landing as too clean a sentiment — *he loved me, here is the proof, I taste it* — and the writer-model could very easily slide into a register that performs the feeling rather than rendering it.

## Step 3 — Narrow to One

**The winner is Premise 30.**

It beats Premise 5 because Premise 5's AI, while excellent material, sits in exactly the mode the project Setup names as the default-resistance scale — the AI as peer in a kitchen-table relationship, individually readable. Premise 30 places the AI's kindness at a scale the protagonist navigates rather than oversees: the father's quiet collaboration with an agricultural AI over a decade has produced an object she encounters after he is gone, and the AI itself never appears as a character. This is the Setup's preferred scale operating naturally in literary-fiction terms.

It beats Premise 9 because Premise 9, while structurally sounder than Premise 30 in some ways, has a genuine risk of confining itself to a chamber piece with the speculative element parked in a helpful margin — the kind of story that would survive the inverse of the re-skin test (could be re-skinned as a contemporary realist piece without much loss). Premise 30 cannot survive that re-skinning: the transposon-bred potato is the recognition, and without the speculative mechanism the recognition has nothing to land on. The SEED is doing constitutive work.

The remaining concern — that Premise 30's recognition could perform sentiment rather than render it — is a craft concern, addressable in execution. It is not a structural defect of the premise.

The two load-bearing SEED items going forward are **champ** and **transposable elements**. The Chambre Syndicale, the sacred/profane dichotomy, and the derivational suffix are released from constitutive duty but remain available as inflection — texture or detail at any later phase. (One specific possibility worth flagging now: the funeral and the wake-meal both sit naturally on the sacred/profane axis, so that SEED item may inflect the story's tonal register even though it is not load-bearing in the premise.)

Ready for Phase 4 when you are. Say "Continue. Next phase." and I will generate 20 plots.

---

# 9. User

Continue. Next phase.

---

# 10. Claude

# Phase 4: Plot Generation

The winning premise: a woman returning to her childhood home in Tyrone for her father's funeral discovers that her father — over the last decade of his life, with the kind agricultural AI's quiet help — had been breeding, in his back garden, a strain of potato whose transposon-mediated traits made it taste like the potatoes of his own childhood; she eats champ from it the night of the wake.

Target length: 1,500–3,500 words. The literary-fiction tradition handles this length comfortably, and within it the upper end (2,500–3,500) gives more room for the slow-accumulation pacing the mode prefers. I will keep my plots inside that range without pinning a specific count.

The diversity axes for this phase: setting, subject of the story, register, entry point, stakes, AI presence. I will push deliberately on each so that plot 20 does not feel like a sibling of plot 1.

The full SEED remains available — *champ* and *transposable* are load-bearing per Phase 3, and *Chambre Syndicale*, *sacred/profane*, and *derivational suffix* may still inflect setting, subject, register, or imagery.

A note on the worry-vocabulary inversion: I am applying it in literary-fiction calibration. Worries about a plot being "too quiet" or "too internal" are *not* penalties here — that is the mode operating in its register. Worries about a plot being too operational, too plot-event-driven, too thriller-shaped, or about the speculative element overpowering the human situation *are* penalties.

## Step 1 — 20 Plots

**1.** **Setting:** present-day rural Tyrone, the father's small farmhouse and back garden, two days. **Subject:** the protagonist, a 50-year-old woman, settling into the recognition over the wake's two days. **Register:** quiet, plain, slightly dry, with grief held at a small distance. **Entry point:** she arrives the morning of the funeral and finds the house full of neighbours already. **Stakes:** what she now knows about the father she had not visited in seven years. **AI presence:** background — the agricultural AI is felt only through what is in the garden and what the neighbours mention in passing. **Sketch:** Day one, the funeral and the early wake. Day two, the morning after, alone in the kitchen, when she finds her father's gardening notes and tries the potatoes. Closes on her eating the champ at the small table where she ate it as a child. ★★★★

**2.** **Setting:** present-day, but the entire story takes place in the back garden across a single late afternoon, with the wake audible from the house. **Subject:** the garden, which the protagonist walks through reading her father's hand-written stake-labels. **Register:** patient, observational, with a register close to a naturalist's. **Entry point:** she leaves the wake to be alone and goes out the back door. **Stakes:** what each row tells her. **AI presence:** mid-ground — a small voice from a weather-worn tablet on a fencepost recognizes her and addresses her, briefly, by name. **Sketch:** A slow walk through the garden's rows, each labelled in her father's hand, with the AI's brief and careful interjections punctuating her moving. ★★★

**3.** **Setting:** present-day, the kitchen, single evening after the funeral, the protagonist alone. **Subject:** the cooking of the champ. **Register:** procedural-domestic, with the cooking as the through-line. **Entry point:** she walks into the kitchen still in her funeral dress and decides she will eat. **Stakes:** what is in the food when she finally tastes it. **AI presence:** none in the room; entirely civilizational, felt only through the potatoes' existence. **Sketch:** The making of champ, step by step, intercut with thin memory and observation. The taste, when it arrives, is the recognition. Closes on the empty bowl. ★★★★★

**4.** **Setting:** present-day, three locations — the funeral, the kitchen, and a phone call to her ex-husband in Manchester at the end. **Subject:** the protagonist's resistance to recognizing what she is being shown. **Register:** dry, slightly ironic, occasional Munro-like asides to the reader. **Entry point:** at the funeral, the priest says something inaccurate about the father, and she does not correct him. **Stakes:** whether she will let herself feel what is in front of her. **AI presence:** background, mentioned twice. **Sketch:** Three scenes braided. The funeral, the cooking, the call. The call ends with her not telling him. ★★★

**5.** **Setting:** the long-ago summer she was twelve, framing a present-day wake. **Subject:** comparison between the father she knew at twelve and the father whose garden she is standing in now. **Register:** lyrical, with the past sections in present tense and the present sections in past, deliberately. **Entry point:** the present-tense memory of her father digging up potatoes in 1987. **Stakes:** the gap between the two fathers. **AI presence:** background. **Sketch:** Alternation. The 1987 sections are full and warm; the present sections are spare. The taste of the champ collapses the two. ★★★ — Worry: the alternation risks preciousness, and the lyrical register is exactly where the AI default toward moody-melancholy lives.

**6.** **Setting:** present-day, the wake itself, a packed kitchen full of neighbours. **Subject:** the social texture of the wake, with the recognition arriving in fragments through what neighbours say. **Register:** comic-warm, Edna O'Brien register, with several distinct neighbour voices rendered. **Entry point:** the protagonist standing in the doorway as a neighbour hands her a plate. **Stakes:** what the neighbours knew about her father that she did not. **AI presence:** background — one neighbour mentions the AI matter-of-factly, in passing, mid-anecdote. **Sketch:** A wake rendered through its conversations. The protagonist eats the champ off a paper plate, standing, while a neighbour is talking about her father's bicycle, and the recognition arrives mid-sentence. ★★★★

**7.** **Setting:** present-day, the protagonist and her older brother in the kitchen the morning after the funeral. **Subject:** the conversation between two adult siblings who have not spoken alone in years. **Register:** clipped, careful, William Trevor-flat. **Entry point:** the brother is washing glasses; she walks in. **Stakes:** what each of them knew about the father and did not say. **AI presence:** background. **Sketch:** A slow conversation across a kitchen, with the champ being made between them, the brother doing most of the cooking. The recognition is shared at the same moment by both. ★★★★

**8.** **Setting:** present-day, the entire story is the protagonist's drive from Belfast to Tyrone the morning of the funeral, with the wake and the meal compressed into the final scene. **Subject:** her preparation. **Register:** interior, unsparing, in the Carver tradition. **Entry point:** she pulls out of the petrol station car park near Antrim. **Stakes:** what she will allow herself to feel when she arrives. **AI presence:** background. **Sketch:** The drive as a long interior corridor. The arrival at the house compresses the funeral and wake to the final two pages. The champ at the end is eaten in a half-page. ★★ — Worry: the structure foregrounds the protagonist's preparation at the expense of the recognition; the speculative element gets compressed into half a page.

**9.** **Setting:** present-day, but told from the point of view of the elderly neighbour who taught the father to grow potatoes when he first came back to the farm in his retirement. **Subject:** the father, seen from outside. **Register:** plain, oral, with the neighbour as narrator. **Entry point:** the neighbour at the funeral, watching the protagonist arrive. **Stakes:** what the neighbour will or will not tell her. **AI presence:** mid-ground — the neighbour has worked alongside the father and the AI in the garden and has views. **Sketch:** The neighbour's first-person narration across the day, ending with her bringing the bowl of champ to the protagonist after the wake has thinned. ★★★★

**10.** **Setting:** the night of the wake, the kitchen, with the wake audible from another room; the protagonist's ten-year-old daughter is also present. **Subject:** the recognition arriving in the act of feeding the daughter. **Register:** intimate, specific, no irony. **Entry point:** the daughter asking for something to eat. **Stakes:** what the protagonist passes on or fails to pass on. **AI presence:** background. **Sketch:** The making of the champ becomes a teaching scene. The daughter eats; the protagonist watches her eat and tastes second. ★★★★

**11.** **Setting:** present-day, a single scene — the protagonist meeting with the local solicitor the day after the funeral to settle the estate. **Subject:** the protagonist's resistance to the solicitor's careful pacing. **Register:** dry, professional, with humour underneath. **Entry point:** the solicitor's waiting room. **Stakes:** what the will reveals about her father's last decade. **AI presence:** mid-ground — the solicitor explains, gently, how the kind administrative AI has handled the father's affairs alongside her father, with his consent. **Sketch:** The meeting, with the will and the garden's catalogue presented as documents. She drives home and makes the champ alone. ★★ — Worry: the solicitor scene is operationally dense; the recognition gets squeezed.

**12.** **Setting:** the morning before she leaves Tyrone to drive back to her life, three days after the funeral, the kitchen. **Subject:** the leaving, the closing of the house. **Register:** Marilynne Robinson-adjacent, slow, attentive, weighted toward the small ritual of departure. **Entry point:** she is wrapping up the last of the food in the kitchen and finds a bag of the potatoes meant for her to take. **Stakes:** what she takes home. **AI presence:** background. **Sketch:** The morning of leaving, the discovery of the bag, the decision to make a last bowl of champ before the drive. The taste arrives in the second-to-last paragraph. The last paragraph is the closing of the door. ★★★★★

**13.** **Setting:** present-day, told as a long letter the protagonist writes to her ex-husband three weeks after the funeral, looking back. **Subject:** the recognition reconstructed in retrospect. **Register:** epistolary, conversational, with the protagonist's specific voice. **Entry point:** the letter's first sentence. **Stakes:** what she is finally able to say. **AI presence:** background. **Sketch:** A letter of perhaps 2,500 words that walks through the funeral and the wake and the meal and what she is now thinking. The letter does not get sent. ★★★ — Worry: the epistolary frame is a non-narrative form, and the project setup's previous template iterations had problems with document-shaped solutions sneaking in. Even though this is literary-fiction-legitimate, I am flagging it.

**14.** **Setting:** present-day, with a single embedded flashback to the protagonist's last visit to her father, seven years earlier, when she came up for a weekend and they fought. **Subject:** the comparison between that visit and this one. **Register:** controlled, with the flashback's heat against the present's quiet. **Entry point:** she walks into the kitchen on the morning of the funeral and the cup she used last time is still on the windowsill. **Stakes:** what the seven-year silence cost. **AI presence:** background — the AI is a character in the seven-year-old fight, mentioned by the father, dismissed by the protagonist. **Sketch:** Present, flashback, present. The flashback pays off in the cooking scene at the end. ★★★★

**15.** **Setting:** present-day, the funeral mass itself, a single scene in the church. **Subject:** the protagonist sitting in the pew. **Register:** ritual-formal, with the priest's words as a kind of secondary voice. **Entry point:** the entrance hymn. **Stakes:** how she is being addressed by the ritual. **AI presence:** background. **Sketch:** A funeral mass rendered in close third, with the protagonist's interior cutting across the liturgy. The wake and the meal are an epilogue. ★★ — Worry: the church scene is the literary-fiction default for this material, and it pulls toward the convergent moody register against which the Unslop guide is calibrated.

**16.** **Setting:** present-day, the protagonist and her son — late teens, here from London — eating the champ together the night of the wake. **Subject:** the son, who knew the father better than she has admitted, and the recognition that arrives through realizing this. **Register:** Lorrie Moore-adjacent, witty surface over real grief. **Entry point:** the son says something at the funeral that she had not expected him to know. **Stakes:** what passed between her son and her father in the years she was not paying attention. **AI presence:** background. **Sketch:** The funeral, the wake, the late kitchen with the son. The recognition is layered: about the potato, and about her son. ★★★★

**17.** **Setting:** present-day, the protagonist arrives a day late, after the funeral has already happened. **Subject:** the empty house, the missed ceremony. **Register:** Anne Enright-adjacent, rueful, sharp. **Entry point:** she arrives to a house that the neighbour has cleaned and left a key in. **Stakes:** the funeral she did not attend. **AI presence:** mid-ground — the AI greets her through a small kitchen interface and is gentle about her lateness. **Sketch:** A solitary arrival. The neighbour comes by the next morning. The champ is cooked alone. ★★★

**18.** **Setting:** present-day, the kitchen, the protagonist hosting a single neighbour — the woman who looked in on the father every other day in his last years — for tea after the wake. **Subject:** the conversation. **Register:** Trevor-flat, with the neighbour holding more than she says. **Entry point:** the neighbour at the back door with a bag from her own garden. **Stakes:** what the neighbour gives the protagonist permission to know. **AI presence:** mid-ground — the neighbour speaks of the AI by its civic name, naturally, more than once. **Sketch:** A two-character scene at the kitchen table. Champ is made, eaten, and the conversation does most of its work in pauses. ★★★★

**19.** **Setting:** present-day, but the story is told from the future, looking back — the protagonist in her early seventies recalling the funeral she attended at fifty. **Subject:** what the recognition has meant across twenty-odd years. **Register:** retrospective, reflective, with the older voice's specific knowledge. **Entry point:** the older protagonist, in her own kitchen, making champ for her grandchildren. **Stakes:** the long shape the recognition has had in her life. **AI presence:** background, in both time-frames. **Sketch:** The older protagonist's present-tense kitchen frames the funeral memory; the memory unspools; the older voice returns at the end. ★★★ — Worry: retrospective frames in literary fiction often turn into fractal summary, and the Unslop guide warns specifically against this. Possible but high-risk.

**20.** **Setting:** present-day, the protagonist and the kind agricultural AI itself, in a single scene — she has gone to the small terminal in the garden shed where her father conducted his end of the work, and asks it questions. **Subject:** the protagonist's encounter with the entity her father collaborated with. **Register:** restrained, attentive, with the AI's voice rendered minimally and specifically. **Entry point:** she finds the shed unlocked. **Stakes:** what the AI will and will not tell her. **AI presence:** foregrounded — direct dialogue with the kind AI for most of the scene's middle. **Sketch:** A single conversation in the shed, which closes with her going back into the house and making the champ. ★★★ — Worry: the AI as foregrounded interlocutor is exactly the small-scale, peer-readable mode the Setup names as default-resistance territory. Even calibrated for literary fiction, this risks being the AI-as-character version that crowds out the larger civilizational scale.

## Step 2 — Top Three

**Plot 3** (the cooking of the champ, single evening, alone, AI entirely civilizational). **What stands out:** the plot's organization around the act of cooking gives the recognition a procedural through-line — every sentence has a place to be doing work, even at the slow pace literary fiction prefers. The AI's complete absence from the room renders the kindness as condition rather than peer, which is the Setup's preferred scale. The premise's two load-bearing SEED items are both fully present: the champ as the central activity, the transposon-bred potato as the load-bearing object inside it. The cooking-procedural shape gives Phase 7's prose somewhere reliable to stand. **What worries me:** the single-character, single-evening, single-room compression is restrictive — there is no second consciousness for the protagonist's interior to friction against. The whole story's life depends on the protagonist's specificity carrying it. If her interior turns out to be thinly drawn, there is nothing else to lean on.

**Plot 7** (the protagonist and her brother in the kitchen the morning after, William Trevor-flat). **What stands out:** the two-character scene with the brother gives the protagonist a real other to friction against, which is the literary-fiction engine the recognition depends on. The shared moment of recognition between siblings is a mode Trevor and Munro have demonstrated works at this length. The Trevor-flat register is genuinely difficult for the AI default to imitate — it is the dry, restrained, withholding register, opposite to the convergent moody-lyrical register, and writing in it would actively pull against AI literary's worst habits. The champ being made between them, cooperatively, gives the central object a place inside a relationship rather than alongside one. **What worries me:** sibling-reconciliation-after-parental-death is one of the most worked seams in the entire literary tradition, which means the AI's training set is full of every possible bad version of it. The plot is reaching for the mode but reaching into a register where AI literary fiction has the deepest available pattern of bad-faith imitation. The plot's success depends on writing cleanly in a register the AI is trained to fail in.

**Plot 12** (the morning of leaving, the discovered bag of potatoes, the last bowl of champ before the drive home). **What stands out:** the plot's selection of the *leaving* moment rather than the *arrival* or *during-the-wake* moment is the smartest narrative choice on the list — the wake is over, the social pressure is gone, the protagonist is alone with what she has been given. The discovery of the bag of potatoes meant for her to take is operationally specific and quietly devastating: the gift was prepared, anticipated, and then her father died before he could give it. The closing on the door of the house, after the meal, gives the story a clean two-beat ending: taste, then leave. The Robinson-adjacent register is one of literary fiction's strong tonal positions — patient and attentive — and it is far enough from the convergent AI-melancholy mode that it offers real protection against it. The two SEED items are both fully load-bearing. **What worries me:** the gift-prepared-but-not-given is the single most dangerous device on the list — it is *exactly* the kind of detail that AI literary fiction will reach for and over-cook, and a writer-model that finds this device will be tempted to perform it. The whole plot has to render the gift's existence without any sentence saying *he had prepared it for me, even at the end he was thinking of me*. The risk is not in the plot's structure but in its single most powerful image.

## Step 3 — Narrow to One

**The winner is Plot 12.**

It beats Plot 3 because Plot 3's compression to a single character in a single evening, while attractive in its discipline, gives the protagonist no other to friction against and asks the prose alone to carry the recognition's full weight. Plot 12 has the protagonist alone for most of its length — that compression is preserved — but anchors the alone-ness against two other presences that the protagonist does not directly meet in scene: the father (through the prepared bag) and the future readers of the house (through the closing door). The structure has more to push against without needing a second character in the room.

It beats Plot 7 because Plot 7, while structurally sound, asks the writer-model to perform in a register where AI fiction has its deepest pattern of failure — the sibling-after-funeral mode, in Trevor-flat register, with all the temptations of dialogue economy and quiet moment. Plot 12's register and structure both pull *away* from the AI default rather than into it, and the central image — the bag of potatoes prepared for her — is *unfamiliar* enough that the AI's training data is unlikely to have a stock version of it to default to.

The remaining concern — that the prepared-bag-of-potatoes risks being over-performed — is a craft concern about the writer-model's discipline at the sentence level, addressable in Phase 7's choice among versions and in Phase 8's revision. Phase 8's audit will need to watch the bag's first appearance, the moment of recognition, and the line that names the gift, since those are the three loci where performance can creep in. The plot itself is structurally sound.

The two load-bearing SEED items — *champ* and *transposable elements* — both carry through fully. The remaining items can still inflect: the wake on the previous day will be at the kitchen's edge in memory and rumour, which leaves *sacred/profane* available as a tonal possibility (a domestic-secular ritual touched by the funeral's recent passage). *Derivational suffix* and *Chambre Syndicale* have less natural purchase here and will likely fall away.

Ready for Phase 5 when you are. Say "Continue. Next phase." and I will generate 20 structure candidates.

---

# 11. User

Continue. Next phase.

---

# 12. Claude

# Phase 5: Structure Selection

A reminder of what this phase is: the formal architecture of the reader's experience. Not which specific scenes happen — Plot 12 already names those — but how they arrive: order, withholding, distance, point of view, temporal shape. The plot establishes that the protagonist is alone in the kitchen on the morning of departure, finds a prepared bag of potatoes meant for her to take, and makes a last bowl of champ before driving home. The wake was the previous day. The structure decides how the reader experiences this material.

A literary-fiction note on this phase: the structural decisions in this mode are unusually load-bearing. The recognition is the engine, and the reader's experience of the recognition is decided here — *when* the reader knows what the protagonist is about to discover, *how close* the prose sits to her interior at the moment of recognition, *what* gets withheld until late, *whether* the past is rendered in scene or in summary. Carver and Robinson and Trevor and Munro are reachable in part because their structural choices differ. I will treat that range as the candidate space and push deliberately to its edges.

The diversity axes for this phase: entry point, temporal shape, withholding strategy, point of view and distance.

## Step 1 — 20 Structure Candidates

**1.** Linear, single morning, close third on the protagonist throughout. The reader enters at the moment she comes downstairs and stays in her present-tense awareness until the closing of the door. No flashback, no temporal layering. The reader learns about the wake, the funeral, the seven-year silence with her father in the same order and at the same pace she encounters them in her own thinking. Withholding: the bag of potatoes is the structural pivot, encountered roughly two-thirds in. The discovery of what is in it is the recognition. ★★★★

**2.** Linear, single morning, close third, but with two short embedded analeptic scenes — the funeral the day before, the moment in the wake she most wants to forget. The embedded scenes arrive when memory pulls them up, interrupting the present-action prose. ★★★ — Worry: the analeptic interruption is a familiar literary-fiction move and risks the convergent moody-melancholy register the Unslop guide flags.

**3.** Frame structure: the closing of the door is the first scene as well as the last. The story opens with the protagonist standing on the front step, key in hand, and then drops back to the morning. The reader knows from sentence one that she leaves; the question is what she has eaten. ★★★

**4.** Linear, single morning, but with the central object — the bag of potatoes — placed in the very first sentence as already-discovered. The story opens with her holding it; the reader does not yet know what it is or what it means. The recognition unfolds across the rest of the morning as she works out what she has been given. ★★★★

**5.** Distant third, single morning, linear. The prose holds the protagonist at a moderate remove — knowing her interior but not always sitting in it. Some sentences sit with her, some sit in the room and watch her. Trevor's distance, Gallant's distance. ★★★★

**6.** First-person retrospective, told by the protagonist some indeterminate time later. The events of the morning are recalled in past tense, with the older voice's specific knowledge of what they came to mean. ★★ — Worry: first-person retrospective is the form most prone to summarizing the recognition rather than rendering it, and AI literary fiction defaults toward exactly the older-and-wiser voice that signposts its conclusions.

**7.** Linear, single morning, second person. *You come downstairs. You see the bag.* The form holds the protagonist at a remove from herself, which the recognition dramatizes. ★★ — Worry: second person in literary fiction is heavily marked, and the AI default reaches for it as an availability for affect rather than for specific structural reason.

**8.** Linear, single morning, close third, but the prose is in the present tense throughout. The recognition happens in time as the reader reads. ★★★★

**9.** Two parallel timelines: the morning of departure and the long afternoon seven years earlier when she last visited her father. The two days alternate in short sections; the seven-year-old afternoon was the day they fought, the morning of departure is its aftermath. The reader learns what was at stake in the fight gradually, and the recognition at the meal is the structural answer to the fight's question. ★★★ — Worry: parallel timelines work in literary fiction but they double the demand on prose specificity, which is exactly where AI literary fiction is most prone to thinning.

**10.** Linear, single morning, close third, but the central perception is *delayed*: she eats the champ, registers the taste, and the explanation of what she is tasting — what her father did, what the AI did, what the potatoes are — is held back until the second-to-last paragraph. The reader experiences the taste before they understand it, alongside her. ★★★★★

**11.** Reverse chronology. The story begins with her driving away and works backward through the morning to the moment she came downstairs. Each scene is the cause of the one before. ★★ — Worry: reverse chronology is a structural device that announces itself, and in literary fiction it tends to perform cleverness rather than serve the recognition.

**12.** Linear, single morning, close third, but rendered as a series of seven discrete short sections each headed only by a brief scene-description, like the panels of a sequence. The protagonist's continuity carries through, but the form invites the reader to feel the morning as a sequence of stations. ★★ — Worry: section-headers in literary fiction are decorative more often than structural; the form is not earning its formal mark.

**13.** Linear, single morning, close third, with the funeral and the wake compressed into a single paragraph of summary near the start, so the reader has the day-before context before the story's present begins. The morning then unfolds without further temporal disruption. ★★★★

**14.** Linear, single morning, close third, but the closing scene's position is occupied by a moment of *non-recognition* — a small action she takes (locking the door, starting the car) that the prose declines to interpret. The recognition is in the meal earlier, but the story closes on the protagonist as person rather than on the recognition as conclusion. ★★★★

**15.** First-person, present-tense, single morning. *I come downstairs. I see the bag.* The protagonist's voice is the entire prose surface. ★★★ — Worry: first-person present in this mode tends toward the high-affect register that AI literary fiction defaults to.

**16.** Linear, single morning, close third, but the prose stays at the protagonist's peripheral attention rather than her central one. The recognition is in what she notices at the edges of doing other things — wiping the counter, finding her keys, putting the bag in the car. The prose's attention is scattered across the small actions, and the recognition gathers from the periphery. ★★★★

**17.** Linear, single morning, close third, with one extended digressive section in the middle that recalls the protagonist's grandmother (her father's mother) and the version of champ the grandmother made. The digression sits in the cooking scene; the present resumes as she eats. ★★★ — Worry: the digression is the literary-fiction temptation toward inheritance-rendering, which can become the universal-treated-as-interesting that the Unslop guide flags.

**18.** Free indirect discourse, sliding between close third and a more distant register, the prose's distance modulating across the morning depending on what the protagonist is doing. Munro's mode. The reader is sometimes inside her thinking and sometimes outside it, and the modulation is part of the reading experience. ★★★★★

**19.** Linear, single morning, close third, but with the protagonist's thoughts about her ex-husband in Manchester — to whom she will not call, will not speak — running as a small persistent counterpoint underneath the morning's actions. The marriage's failure is rendered through what she does not do. ★★★ — Worry: the counterpoint adds a second relational dimension that the plot did not specify, and the structural choice may be doing the plot's work rather than the structure's.

**20.** Linear, single morning, close third, but with one paragraph break carrying a twenty-year jump — the morning, then a single paragraph from twenty years later in which the older protagonist is somewhere else entirely doing something specific, and we see the morning's recognition having held or not held across the long arc. Closes back in the older time, not the morning. ★★ — Worry: the twenty-year jump is the structural move most likely to perform meaning rather than render it; the second time-frame would have to be extraordinarily specific not to feel decorative.

## Step 2 — Top Three

**Structure 10** (delayed perception: she tastes before she understands; explanation held until second-to-last paragraph). **What stands out:** the structural decision *enacts* the recognition. The reader's experience of taste-without-explanation, then explanation-arriving, is the protagonist's experience of the same thing. The structure is the recognition rather than commenting on it. The single moment of structural withholding — the postponed explanation — does the work that in less disciplined literary fiction is done by paragraphs of interior commentary. **What worries me:** the structure asks the prose to render a taste in such a way that it carries weight before the reader knows why. If the prose at the moment of taste is thin or generic, the structure collapses into withholding-for-the-sake-of-it. The whole architecture's life is in two paragraphs.

**Structure 14** (linear, close third, single morning, but closing on a moment of *non-recognition* — a small action the prose declines to interpret). **What stands out:** the choice to put the recognition in the meal earlier and close on a small uninterpreted action is the late-Munro move, and one of the strongest structural answers in the literary tradition to the AI temptation toward signposted endings. The structure makes the recognition's interpretation impossible to perform — the closing scene is *about* not interpreting. The Unslop guide warns specifically against the signposted conclusion, and this structure protects against it at the architectural level rather than relying on sentence-level discipline. **What worries me:** the move requires the recognition itself to land cleanly in the meal, with enough weight that the closing's quietness reads as continuation rather than as evasion. If the meal scene is underdone, the closing reads as a withdrawal from feeling rather than as a holding of it.

**Structure 18** (free indirect discourse, sliding between close third and a more distant register, modulating across the morning). **What stands out:** the structural choice gives the prose a way of breathing that resists tonal monotony — the Unslop guide's specific warning against AI literary's sustained mood. The modulation between distances is the Munro mode at its most inhabited; it gives the protagonist's interior real shape by sometimes leaving it. The free indirect register is also a register the AI default has trouble with — it requires a specific consciousness to anchor in *and* a specific narrator's distance to slide to, and the AI default tends toward the lyrical-third that splits the difference unsatisfactorily. **What worries me:** the structure is described in terms of distance rather than in terms of event. A writer-model attempting to render free indirect at the architectural level may produce something that *says* it modulates distance without actually doing so. The structure's success depends on craft that has to be visible at every paragraph rather than at specific points.

## Step 3 — Narrow to One

**The winner is Structure 14.**

It beats Structure 10 because Structure 10's central virtue — the postponed explanation — is also its central vulnerability: the structure puts almost all its load on two paragraphs at the end, and a writer-model that mishandles either of them collapses the whole architecture. Structure 14 distributes the load: the recognition is in the meal in the middle of the morning, and the closing's quietness extends the recognition rather than carrying it alone. If the meal is well-rendered, the closing has somewhere to rest; if the closing is well-rendered, the meal has somewhere to lead. The two scenes support each other in a way Structure 10's two final paragraphs do not.

It beats Structure 18 because Structure 18 is described at a level of craft-abstraction that may not survive translation into the actual prose. "The distance modulates" is a description of what good prose in this mode does, but it is hard to instruct against — a writer-model attempting it from the structural level may produce ambient lyrical third with the *claim* of modulation rather than the modulation itself. Structure 14's instruction is concrete: put the recognition in the meal, close on an uninterpreted action. The writer-model can be held to that more reliably than to a request for distance modulation, and the structural protection against the signposted ending is built into the architecture rather than into the prose's minute-by-minute discipline.

The remaining concern — that the meal scene must land cleanly enough for the closing's quietness to read as continuation rather than evasion — is the right concern to be left with at this stage. It is a specific piece of work for Phase 6's outline (the meal scene needs adequate word allotment and specific imagistic anchoring) and Phase 7's prose (the meal needs to be rendered at full attention, not summarized) and Phase 8's revision (the closing must not, in any sentence, name what is being held). The structure has identified the load-bearing scenes; the later phases can build to them.

To restate Structure 14 in the form Phase 6 will inherit: linear, single morning, close third on the protagonist throughout, no temporal layering, no second consciousness in scene. The day-before (funeral and wake) is referred to but not entered. The recognition occurs in the cooking-and-eating scene, which sits inside the morning. The story closes on a small action the protagonist takes — locking up, starting the car, something on that order — that the prose does not interpret. The reader is left holding the recognition that the protagonist has just had; the protagonist's continuation past it is the closing image.

Ready for Phase 6 when you are. Say "Continue. Next phase." and I will generate the outlines.

---

# 13. User

Continue. Next phase.

---

# 14. Claude

# Phase 6: Outline Generation

The structure (Phase 5 winner): linear, single morning, close third on the protagonist throughout, no temporal layering, no second consciousness in scene. The day-before is referred to but not entered. The recognition occurs in the cooking-and-eating scene. The story closes on a small uninterpreted action.

The plot (Phase 4 winner): the morning of departure, three days after the funeral. She closes up the house, finds a bag of potatoes prepared for her to take, makes a last bowl of champ, and drives home.

Target length: 1,500–3,500 words. The legibility floor matters. Every outline below has to be small enough that the chosen length can render it in scene rather than in compression. I will keep beat counts modest and weight the meal heavily.

I will generate ten outlines that all honor the winning structure. Each one varies which scenes carry weight, where the cooking-and-eating sits, what specific images anchor each beat, and what the closing image does. Same destination, different paths.

A note on candidate last lines: literary fiction's last lines often gain their weight from the specific concrete object or action they name, not from any rhetorical move. The strongest last lines below are the ones that point at something specific without commenting on it.

## Step 1 — 10 Outlines

---

**Outline A — The bag late.** ≈3,000 words. Five scenes.

- **Scene 1 (≈400 words):** She comes downstairs in the half-light and the kitchen is already as she will leave it. Counter wiped, dishes done, the wake's evidence cleared by neighbours she did not ask. She makes tea and stands at the back window. Establishes the morning, the season (early autumn), the seven-year absence as a small pressure rather than a stated thing.
- **Scene 2 (≈500 words):** She moves through the rest of the house — the front room, her father's bedroom, the small office. She is looking for the few things she promised herself she would take. She finds her grandmother's mass card and a tin of buttons. She does not yet know to look for the bag.
- **Scene 3 (≈400 words):** She returns to the kitchen and begins to pack the cool bag for the drive. On the worktop near the back door, she finds the bag — a hessian sack, twelve pounds or so, her name in her father's hand on a folded card pinned to it. The card says only her name.
- **Scene 4 (≈1,200 words):** The cooking and the eating. She peels six of the potatoes, boils them, mashes them with butter and milk and the scallions from the garden she cuts herself. The recognition is in the taste. The prose stays close. Establishes the cultivar's history through a few specific concrete details — the colour of the flesh, the smell when peeled, what her father once said about a potato her grandmother had grown. The AI is not named; what it has done is felt only in the existence of the food.
- **Scene 5 (≈500 words):** She washes the bowl. She loads the car. She locks the back door, then the front. She gets in the car and starts it. The story closes on her hand on the gear stick, or the back-up lights against the gravel, or the door of the car closing. No interpretation.

Candidate last line: *She put the car into reverse and waited until the lights came on.*

★★★★★

---

**Outline B — The bag early.** ≈2,800 words. Four scenes.

- **Scene 1 (≈300 words):** She comes downstairs and the bag is the first thing she sees, on the worktop where someone has set it for her. She does not yet open it. She makes tea and looks at it.
- **Scene 2 (≈600 words):** She moves through the house, packs, returns to the kitchen. The bag is still there. The non-opening is a small pressure across the morning.
- **Scene 3 (≈1,400 words):** The opening, the cooking, the eating. The bag's note is read here. The cooking happens with the recognition already present. The taste extends the recognition rather than producing it.
- **Scene 4 (≈500 words):** She closes the house and leaves. Closing image as in A.

Candidate last line: same family of options. ★★★★

---

**Outline C — The garden visit.** ≈3,200 words. Six scenes.

- **Scene 1 (≈300 words):** She comes downstairs.
- **Scene 2 (≈400 words):** She moves through the house briefly.
- **Scene 3 (≈500 words):** She goes out to the back garden in her coat, just to see it. She walks the rows. The labels in her father's hand are still on the stakes. She does not yet understand what she is looking at; she only registers his care.
- **Scene 4 (≈300 words):** She returns to the kitchen and finds the bag.
- **Scene 5 (≈1,200 words):** Cooking and eating.
- **Scene 6 (≈500 words):** Closing.

Candidate last line: as in A. ★★★ — Worry: the garden visit duplicates the recognition's work. By the time she finds the bag, the garden has already done part of the recognition's labour, and the meal has less to find.

---

**Outline D — Phone call mid-morning.** ≈2,800 words. Five scenes.

- **Scene 1 (≈400 words):** She comes downstairs.
- **Scene 2 (≈500 words):** Her brother calls from London. They have a brief, careful conversation about the practicalities. She does not tell him she has not slept. She agrees to a thing he is asking that she does not really want to agree to. The call is the day's only second consciousness, held to the phone.
- **Scene 3 (≈400 words):** She moves through the house, finds the bag.
- **Scene 4 (≈1,000 words):** Cooking and eating.
- **Scene 5 (≈500 words):** Closing.

★★★ — Worry: the brother on the phone is a second voice the structural commitment said the story would not have, even at one remove. Brings in relational complication that may compete with the recognition rather than support it.

---

**Outline E — The neighbour at the door.** ≈3,300 words. Five scenes.

- **Scene 1 (≈400 words):** She comes downstairs.
- **Scene 2 (≈500 words):** She moves through the house.
- **Scene 3 (≈700 words):** A neighbour comes to the back door — the woman who looked in on her father. The neighbour has come to say goodbye and to leave a small thing of her own. The conversation is brief, mostly silences. The neighbour does not stay. Before leaving, she nods at the bag on the worktop and says it is for her, that her father had it ready.
- **Scene 4 (≈1,100 words):** Cooking and eating.
- **Scene 5 (≈500 words):** Closing.

★★★ — Worry: same as D. The neighbour is a second consciousness, and the structural commitment was to no second consciousness in scene. The plot specifically excluded this. This outline is fighting the structure.

---

**Outline F — The cooking is the spine.** ≈2,400 words. Three scenes.

- **Scene 1 (≈400 words):** She comes downstairs, finds the bag almost immediately (within the first scene's natural arc).
- **Scene 2 (≈1,500 words):** The cooking and the eating, dilated. Every step of the preparation is rendered. The recognition arrives in stages across the cooking rather than at the moment of taste; the taste confirms what the cooking has been showing her.
- **Scene 3 (≈500 words):** Closing.

★★★★ — Worry: dilating the cooking risks tedium if the prose can't carry it. The plot's central attraction was the meal as the recognition's site; this outline maximizes that, but at the cost of the morning's other texture.

---

**Outline G — The two halves.** ≈3,000 words. Two scenes.

- **Scene 1 (≈1,300 words):** Everything before the bag is found. She moves through the house, packs the car for things other than the bag, walks out and walks back in. The bag arrives at the end of this section.
- **Scene 2 (≈1,700 words):** Everything from the bag to the closing of the door. Cooking, eating, leaving, all in one continuous movement.

★★★ — Worry: the two-scene shape is structurally clean but loses the morning's small punctuations. The prose has to carry continuity for very long stretches without rest, and the legibility floor matters most when paragraphs run long.

---

**Outline H — The notebook found in the office.** ≈3,200 words. Five scenes.

- **Scene 1 (≈400 words):** She comes downstairs.
- **Scene 2 (≈700 words):** She moves through the house and finds, in the small office, a hardback notebook of her father's gardening notes. She reads two pages of it. She does not yet know about the bag.
- **Scene 3 (≈300 words):** Returns to the kitchen and finds the bag.
- **Scene 4 (≈1,200 words):** Cooking and eating, with the notebook on the kitchen table beside her, sometimes consulted.
- **Scene 5 (≈600 words):** Closing.

★★★ — Worry: the notebook is the AI literary fiction's favourite object, and it is exactly the kind of detail that lets the writer-model perform legibility-of-the-dead by transcription. The notebook risks becoming a way for the story to *tell* the recognition rather than *render* it.

---

**Outline I — The shorter version.** ≈1,800 words. Four scenes.

- **Scene 1 (≈250 words):** She comes downstairs.
- **Scene 2 (≈350 words):** She moves through the house, briefly.
- **Scene 3 (≈900 words):** Finds the bag, cooks, eats. Combined.
- **Scene 4 (≈300 words):** Closing.

★★★★ — Worry: at the lower end of the range, the meal scene has less room to breathe. The recognition has to land faster, which suits Carver-Davis economy but pulls against the Robinson-adjacent register the plot specified.

---

**Outline J — The longer version.** ≈3,400 words. Six scenes.

- **Scene 1 (≈500 words):** She comes downstairs.
- **Scene 2 (≈700 words):** She moves through the house.
- **Scene 3 (≈400 words):** Returns to the kitchen, finds the bag.
- **Scene 4 (≈1,400 words):** Cooking and eating, with full Robinson-adjacent dilation.
- **Scene 5 (≈400 words):** A small action between the eating and the leaving — washing the bowl, returning a thing to the garden, etc.
- **Scene 6 (≈400 words):** Closing.

★★★★ — Worry: at six scenes for this length, the morning's beats start to feel slightly listed. The fifth scene is doing genuine work or it is filler; it would have to be specific enough to earn its place.

---

## Step 2 — Top Three

I am flagging three outlines for plot-stage Unslop risk before naming the top three. Outline H has the notebook problem named above — the kind of object that AI literary fiction reaches for to perform recognition. Outline G's two-scene shape carries a fractal-summary risk in long stretches without natural rest. Outline E is fighting the structural commitment by adding a second consciousness in scene; it would be a different story than the one the earlier phases agreed to. None of these three is in the top three for those reasons.

**Outline A** (the bag late, five scenes, ≈3,000 words). **What stands out:** the architecture is clean. The first three scenes establish the morning's shape and the protagonist's specific way of being in it; the bag arrives as a real moment of discovery; the meal has 1,200 words of room; the closing has 500 words to extend rather than compress. The non-discovery of the bag in the first two scenes is the structure's quiet labour — the morning is doing real work before the bag appears. The five-scene division gives the prose natural rests at the right places. **What worries me:** the outline is the most conventional shape on the list. It runs no formal risks, which means it is also the outline a writer-model can most easily render in the AI literary default register without anyone noticing the slide. The cleanliness is also exposure — the prose has to do all the distinguishing work itself, since the structure does none of it.

**Outline F** (the cooking is the spine, three scenes, ≈2,400 words). **What stands out:** the outline takes the plot's central attraction — the meal as recognition site — and makes it structurally dominant. The dilated cooking is exactly the kind of slow procedural attention literary fiction rewards. Scene 2's 1,500 words of cooking is large enough that the recognition can arrive in stages rather than as a single moment, which is harder to perform than a single moment and therefore more protected against the AI default. The three-scene shape is unusually disciplined: each scene does one thing, fully. **What worries me:** the cooking has to genuinely sustain 1,500 words of sentence-level interest. The risk is not that the cooking is uneventful — that is the point — but that the prose, asked to dwell, may default to the AI literary mode of cooking-as-meditation, where every motion of the hands becomes an occasion for an interior aside. The outline's success depends on the prose dwelling on what is actually happening in the kitchen rather than on what it might mean.

**Outline I** (the shorter version, four scenes, ≈1,800 words). **What stands out:** at the lower end of the range, the outline forces the prose to compression — Carver-economy rather than Robinson-attention. Every sentence has to do more work, and the AI default toward dilation is structurally restrained. The combined cooking-eating scene runs 900 words rather than 1,200–1,500, which means the recognition must arrive cleanly and the closing has to do more relative work. The shorter length is also a length the cooking-procedural can sustain without taxing the prose — a 900-word cooking-eating scene is reachable in a way that a 1,500-word one is not. **What worries me:** the shorter version may be too short for the closing to extend the recognition the way Phase 5's structure asks. The closing scene at 300 words has to hold the protagonist's continuation past the recognition without rendering the continuation as conclusion, and 300 words is not a lot of room to hold something open.

## Step 3 — Narrow to One

**The winner is Outline A.**

It beats Outline F because Outline F's central virtue — the dilated cooking — also concentrates the story's risk into a single 1,500-word scene whose success is asked to carry the whole. Outline A distributes the load across five scenes and leaves the cooking at 1,200 words, which is enough room to breathe but not so much that the prose has nowhere to rest. The first three scenes do real work establishing the protagonist's specific way of being in the morning — the seven-year absence is in *how* she moves through the house, not in stated reflection — and the meal has somewhere to land because that work has been done. Outline F's compression of the morning to a single pre-cooking scene loses the room that establishment needs.

It beats Outline I because Outline I's shorter length, while disciplining against AI dilation, also gives the closing scene only 300 words to extend the recognition's hold. Phase 5's structural commitment was to a closing on a small uninterpreted action that *continues* rather than *concludes*, and 300 words is genuinely tight for that work. Outline A's 500-word closing is the right size for the closing's job: long enough to let the continuation register, short enough not to perform it.

The remaining concern — Outline A's conventionality, its lack of formal risk — is the right concern to be left with at this stage. The architecture's plainness means the prose has to do all the distinguishing work, and Phase 7's five versions need to do that work on different ground. Each of the five versions should pick a different specific approach to the morning's texture: a version that dilates the household-things scene (Scene 2), a version that leans into the cooking's procedural specificity (Scene 4), a version that runs colder and more compressed than the outline's natural rhythm, a version that runs warmer and more attentive, and a version that takes a real risk with the closing image (Scene 5). The outline is the same in all five; the prose is what differs.

A flag for Phase 7 specifically: the seven-year absence is the morning's invisible weight. The outline does not name it as a beat because it is not a scene — it is a pressure on every scene. Phase 7's prose has to render it without saying it. A version that has the protagonist *think about* the seven-year absence in interior monologue is the version that has failed to render it; a version where the protagonist *moves through the house* in a way that registers it without naming it is the version that has succeeded. This is where the AI literary default is most dangerous on this material, and where the prose's discipline matters most.

A flag for Phase 8 specifically: the bag's note in Scene 3 — the folded card with her name in her father's hand — is the single most dangerous detail in the outline. The temptation in revision will be to tell the reader what the card means, or to render the protagonist's thought about it. The note is a concrete object; the prose must let it stay one. The audit at Phase 8 will need to watch the card's first appearance closely.

The outline ready for Phase 7:

- **Scene 1 (≈400 words):** Coming downstairs in the half-light. The kitchen as the wake's neighbours left it. Tea, the back window, the morning establishing.
- **Scene 2 (≈500 words):** Through the rest of the house. The grandmother's mass card. The tin of buttons. The specific things she promised herself she would take.
- **Scene 3 (≈400 words):** Back to the kitchen. The bag on the worktop, her name on a folded card.
- **Scene 4 (≈1,200 words):** Peeling, boiling, mashing, the scallions from the garden. The eating. The recognition in the taste.
- **Scene 5 (≈500 words):** Washing the bowl. Loading the car. Locking the back door. Locking the front. Getting in. Starting the engine. Closing on the small uninterpreted action.

Total: ≈3,000 words. Comfortably inside the 1,500–3,500 range, with room for the prose to breathe at the meal and the closing.

Ready for Phase 7 when you are. Say "Continue. Next phase." and I will write five complete versions of the story.

---

# 15. User

Continue. Next phase.

---

# 16. Claude

# Phase 7: Story Generation

A note before I begin. This is the heaviest context phase, and on the literary-fiction target it is also the phase where the AI default is most dangerous. The convergent literary-AI register — moody, voiceless, full of small lyrical gestures — is exactly what asking for "literary fiction" elicits if the writer-model is not actively pulling against it. I will name each version's specific tonal strategy at its head, and I will use the five versions to push at different points on the available range so that no single one is the only chance to escape the default.

Before naming worries on each version, I will name what each version would have to do to *not* be a recognition scene with literary-AI dressing — to actually render the recognition rather than perform it. The literary-fiction target inverts the usual Phase 7 calibration: a worry that a version is too quiet or too character-anchored is *not* a fatal worry here, since that is the mode operating in its register. A worry that a version slides into the convergent moody-melancholy register *is* fatal, since that is the mode this template's surrounding apparatus is most calibrated against and that AI literary fiction defaults to.

The outline (Phase 6 winner) is fixed. The five versions execute it differently.

The two load-bearing SEED items are *champ* and *transposable elements*. The structurally kind agricultural AI is present as civilizational condition, never as a character in scene.

I'll write the five versions in two batches of three and two, with brief reflection between them, per the template's guidance for late-set regression.

---

## Version 1 — "Plain"

*Tonal strategy: Carver-flat, restrained, declarative. Short to medium sentences, no figurative language unless functional, the protagonist's interior accessed through what she does and notices rather than through stated reflection. Risks: too cold to land the recognition.*

---

She came downstairs in her socks, holding the bannister. The radio was off. The kettle was where she had put it the night before, in the centre of the cooker. She filled it from the tap.

The wake's neighbours had cleaned the kitchen. The teacups were in the press, the plates stacked. Someone — Mrs Hegarty, probably — had put a clean tea towel over the breadboard. The room looked like it had not been used.

She stood at the back window with the cup in her hand and watched the light coming down on the garden. There was frost on the long grass at the edge. Her father had cut the lawn in August and not since.

She went through the front room. The mass cards were still on the mantelpiece. She took her grandmother's, the one with the print of the Sacred Heart, and put it in the side pocket of her bag. The room smelled of the lilies the funeral home had sent.

She went up to her father's bedroom and stood in the doorway. The bed was made. She did not go in.

In the small office she found a tin of buttons her mother had kept. She took the tin. There was a Bible on the desk that she did not take.

Back in the kitchen the bag was on the worktop near the back door. Hessian, twelve pounds or so. A folded card was pinned to the top with a safety pin. She unpinned it.

The card was the kind he had used for everything, an index card cut in half. Her name was on it in his hand.

She held the card for a while. Then she put it in the breast pocket of her shirt.

She opened the bag. The potatoes were not large. They were a colour she had not seen before in a potato — a pale yellow with a faint pink at the eyes, like the inside of a shell. They smelled like potatoes when she put her face close.

She took six of them out and put them in the colander and ran water over them. She found the small paring knife in the drawer where it had always been. She peeled the six potatoes over the bin. The skin came off in long strips. The flesh was the same pale yellow inside.

She quartered them and put them in a pot with cold water and salt. She put the pot on the cooker.

She went out the back door for scallions. Her father's garden ran the length of the property, narrower than she remembered. The rows were labelled. She walked along them looking at the labels. The labels were in his hand, on small wooden stakes he had cut from something. She found the scallions. She cut six of them at the base with the kitchen scissors she had brought out.

She came back in. The water was beginning to move in the pot.

She washed the scallions and chopped them on the breadboard. She got the butter from the press and a small carton of milk from the fridge — someone had bought milk for her, a litre, blue cap. She set the butter and the milk on the counter and waited.

When the potatoes were done she drained them in the colander and put them back in the pot. She added the butter. She added the milk in two pours, watching it sink. She mashed them with the wooden masher that had been in the drawer for as long as she had been alive.

She added the scallions. She mixed them through.

She got a bowl from the press. She spooned the champ into the bowl. She sat down at the small table by the back window and put the bowl in front of her.

She ate.

The taste was not the taste of any potato she had eaten in twenty years. It was the taste of the potatoes her grandmother had grown, a small woman who had been dead since 1989. She had not known she remembered the taste. She kept eating. She finished the bowl.

She washed the bowl and the pot and the masher and the colander and the knife and the breadboard. She dried them and put them back where they had been.

She put the rest of the potatoes into the cool bag with the milk that was left and the half-pound of butter. She carried the cool bag and her own bag out to the car and put them in the boot.

She came back in and locked the back door from the inside. She went out the front door and pulled it to and turned the key. She put the key under the stone where her father had always put it.

She got into the car. She put the key in the ignition. She started the engine.

She put the car into reverse and waited until the lights came on.

[≈770 words. The outline calls for ≈3,000 — this version is severely undershot. It is the discipline test rather than the length match: the version exists to show what the material looks like rendered at full Carver compression. The other four versions will sit in the proper range.]

---

## Version 2 — "Robinson-Adjacent"

*Tonal strategy: dilated, attentive, the prose's distance closer to the protagonist than in Version 1 but never lyrical. Sentences mostly mid-length, occasional long ones, free indirect drift at moments where her interior pulls forward. Patience with small things. Risks: the patience could turn into AI-default reflection.*

---

She came downstairs in her socks. The kettle was where she had left it the night before, in the centre of the cooker. The wake's last neighbours had washed it and left it dry.

She filled it and put it on the gas. She found a teabag in the caddy — the same caddy, the same dent in its lid where her mother had dropped it forty years before — and dropped it in a cup. The morning was the colour of a wet stone. From the back window the garden looked smaller than she remembered, and tidier; her father had cut it in August.

The kitchen had been cleaned. Mrs Hegarty had been through with a cloth and a tea towel; the teacups were stacked in the press in the way Mrs Hegarty stacked them, which was not the way her mother had stacked them, and her father had probably let it go. The breadboard was covered. There was a single mass card on the worktop that someone had set down and forgotten, not her grandmother's, someone else's.

She made the tea and stood with it. She had not slept much. She had not slept much for three days. There was no one in the house now and she could feel the house waiting.

The front room held the rest of the cards. She picked through them slowly. The lilies the funeral home had sent were beginning to brown at the edges, and the room smelled of them, and underneath that the older smell of a room used at Christmas and rarely otherwise. She took her grandmother's card from the mantelpiece and put it in the side pocket of her travel bag. She did not pick up the others. She left them where they were for whoever would come to clear the house.

She went up the stairs slowly. She had not been in her father's bedroom for seven years. She stopped in the doorway. The bed was made — Mrs Hegarty again, probably. A jumper was folded on the chair. She did not go in.

In the small office at the end of the landing she opened the desk drawer and found the tin of buttons. The tin was older than she was, oval, with a faded picture of a woman in a green dress. The buttons inside were the buttons of fifty years of clothes. She closed the lid and took it.

She had told herself, on the drive up, that she would take three things. She had taken two.

She came back down to the kitchen and the bag was on the worktop near the back door. She had not noticed it on her way through. It was hessian, the size of a sack of coal cut in half, and there were potatoes in it; she could see the shapes of them through the cloth. A folded card was pinned to the top.

She unpinned it. The card was an index card he had cut in half. He had used them for everything. *For Aoife*, he had written, in the careful upright hand he had used in the years since his hand had begun to shake. Just the two words.

She held the card for a while and then put it in the breast pocket of her shirt.

She opened the bag. The potatoes were not large. They were a colour she did not know — pale yellow, with a faint flush of pink near the eyes, like the inside of certain shells. She took one out and turned it in her hand. It weighed about right. She put her face down to the bag and smelled them. They smelled like potatoes.

She took six of them and put them in the colander. She ran the water over them and rubbed the dirt off with her thumb. She found the small paring knife in the drawer where the small paring knife had always been, and she peeled the six potatoes over the bin. The skin came off in long pale strips. The flesh inside was the same pale yellow as the skin, only deeper.

She quartered them. She put them in the pot with cold water from the tap and a good pinch of salt. She set the pot on the gas and turned the gas to high.

She went out the back door for scallions.

The garden was narrower than she remembered, but longer. Her father had cut it back at one end and extended it at the other. The rows were labelled — small wooden stakes he had cut from something, his hand on the stakes in pencil that had darkened with weather. She walked along them slowly. *Sharpe's Express*. *Kerr's Pink*. *Records*. *Lumper*. Names she half knew. Then the scallions, in their own row, and beyond them a row labelled with no name — only a number, *6.4*, and beneath that the year, *2024*. She knew, with the part of her mind that knew without being told, that the bag in the kitchen had come from this row.

She cut six scallions at the base with the kitchen scissors and stood for a moment looking at the row. The plants had been pulled up; only the trimmed haulms remained. He had pulled them himself, she thought, before the end. Or someone had pulled them at his asking.

She came back in. The water was moving in the pot.

She washed the scallions and chopped them fine on the breadboard. She got the butter from the press and the half-litre of milk from the fridge — someone had bought milk for her, a litre, blue cap, and there was the half-litre in the door from before. She set the butter and the milk on the counter beside the cooker.

When the potatoes were soft to the knife she drained them and tipped them back into the pot. She put a quarter-pound of butter into the pot and watched it slide and slip and begin to go. She poured the milk in, in two pours, and let it sink. She mashed them with the wooden masher.

She added the scallions and folded them through with the masher's edge. She tasted the salt with the tip of her finger and added a little more.

She took a bowl from the press. She spooned the champ in. She sat down at the small table by the back window. She put the bowl in front of her. She picked up the spoon.

She ate.

She had not eaten potatoes that tasted like this since she was a child. She had not known until now that the potatoes she ate as a child had tasted of anything; they had tasted of *potato*, which had been the only category. The taste in her mouth now was the category itself. She ate slowly. She finished the bowl.

She washed the bowl. She washed the pot and the masher and the colander and the knife and the breadboard, and she dried them and put them back where they had been. She put the lid on the butter and the cap on the milk and set them in the cool bag with the rest of the potatoes from the sack. She had decided, without deciding, that she would take them.

She carried the cool bag and her travel bag and the tin of buttons out to the car and put them in the boot. She came back into the house and stood for a moment in the kitchen, and then she went out and pulled the back door to and locked it from the outside with the key her father had kept on a hook.

She went out the front door and pulled it to and turned the key in the lock. She put the key under the stone where her father had always put it. She did not look back at the house.

She got into the car. She fastened the seatbelt. She put the key in the ignition.

She started the engine and put the car into reverse and waited until the lights came on.

[≈1,400 words. Still under the outline's ≈3,000 target. Note for the next batch: I am undershooting in both versions by stripping the morning's middle scene rather than dilating the prose. The outline asks for ≈500 words on the through-the-house scene; both versions have given it ≈250. The Robinson-adjacent register can in principle dilate further, and the next versions should test that.]

---

## Version 3 — "Munro-Adjacent"

*Tonal strategy: free indirect, modulating between close third and a slightly cooler distance, with one or two small sharp asides where the protagonist's specific judgement comes forward. Munro's risk is that the asides pull toward an authorial voice. Risks: the asides could read as performed wisdom; the modulation could collapse into AI-default lyrical-third.*

---

She came downstairs in her socks because her shoes were still by the front door from the night before, and the cold of the lino through the wool was the cold she remembered from being twelve and getting up before her father, in winter, when the fire had gone out in the night.

The kitchen had been cleaned. Mrs Hegarty had been through it; you could tell from the way the teacups were stacked, by size, which was Mrs Hegarty's way and not her mother's. The kettle was in the centre of the cooker. The breadboard was covered with a clean tea towel. A single mass card had been left on the worktop and forgotten. Aoife picked it up — Maureen Devlin, who had been her mother's friend, dead nine years — and set it down again. The light was the wet-stone colour of October mornings in Tyrone, which was its own colour and not any other.

She made tea. She stood at the back window with the cup. The garden looked smaller than she remembered and considerably tidier; her father had cut the lawn in August and not since. The frost on the grass at the edge would be gone in an hour.

There was no one in the house now and she could feel the house waiting.

It had been seven years since she had stood in this kitchen. She had told herself on the drive up that she would not count the years to herself, because counting them was its own form of punishment, but she counted them now, standing at the window with the tea cooling. Seven years was a long time when both parties to a quarrel were in their seventies. He had been seventy-eight when she had last stood here, and she had been forty-three, and what had been said between them had been the kind of thing that gets said and cannot be unsaid, and she had not come back.

She had told herself, also, that she would take three things from the house. She had picked the three on the drive: her grandmother's mass card, the tin of buttons, the framed photograph of her mother at twenty-six in the print dress. The mass card was easy. She went into the front room, where the cards on the mantelpiece were still in the careful semicircle the funeral home had arranged them in, and she took her grandmother's from the centre and put it in the side pocket of her travel bag. She did not look at the others. The lilies the funeral home had sent were beginning to brown at the edges, and the front room smelled of them, and underneath that the older smell of a room used at Christmas and rarely otherwise.

The tin was in the small office. It had been her mother's. It was older than Aoife was — oval, the picture of a woman in a green dress on the lid faded almost to nothing — and the buttons inside were the buttons of fifty years of clothes; some of them she could put a dress to, even now. She closed the lid and took it.

The framed photograph was in her father's bedroom, on the chest of drawers, and she had told herself she would go in and take it. She stood in the doorway. The bed was made — Mrs Hegarty, again. A jumper was folded on the chair. She looked at the photograph from the doorway. Her mother was twenty-six in it. The dress had been blue, in life, but the photograph was black and white, and the blue did not survive into the print. After a while she pulled the door closed without going in and went back down the stairs.

Two of three. She would have to come back, eventually, for the other things, when the house was being sold. She told herself this and did not believe it.

When she came back into the kitchen the bag was on the worktop near the back door. She had not noticed it on her way through to the front room earlier; she might have walked past it twice. It was hessian, the size of a coal sack cut in half, with potatoes in it — the shapes were visible through the cloth. A folded card was pinned to the top with a brass safety pin.

She unpinned it.

The card was an index card he had cut in half. He had cut his index cards in half for everything, for as long as she had known him. *For Aoife*, he had written, in the careful upright hand he had used in the years since his hand had begun to shake. Just the two words.

She had been prepared for letters. She had prepared herself, on the drive up, for the possibility that there would be letters in the desk, addressed to her, that he had written and not sent, and she had decided that she would read them sitting at the kitchen table with a cup of tea, slowly, and that she would not cry. She had not been prepared for an index card with two words on it, pinned to a sack of potatoes.

She held the card. She put it in the breast pocket of her shirt.

She opened the sack. The potatoes were not large. They were a colour she had not seen before in a potato — a pale yellow with a faint pink at the eyes, like the inside of certain shells. She took one out and turned it in her hand. It weighed about right. She put her face down to the bag and smelled them. They smelled like potatoes, which was the only thing potatoes smelled like, except she registered, a beat after smelling, that they did not smell like the potatoes she bought in Sainsbury's in Manchester, which smelled of nothing.

She took six of them and put them in the colander and ran water over them. She found the small paring knife in the drawer where the small paring knife had always been. She peeled the six potatoes over the bin. The skin came off in long pale strips, and the flesh inside was the same pale yellow as the skin, only a shade deeper.

She quartered them and put them in a pot with cold water and salt and set the pot on the gas. She turned the gas to high.

She went out the back door for scallions.

The garden was narrower than she remembered but longer. Her father had cut it back at the house end and extended it at the far end, and along the new section he had put in raised beds out of what looked like old joists. The rows were labelled — small wooden stakes he had cut from something, his hand on the stakes in pencil darkened by weather. She walked along the rows. *Sharpe's Express*. *Kerr's Pink*. *Records*. *Lumper*. Names she half knew, that her grandmother had used. Then the scallions, in their own row at the kitchen end, and beyond them, halfway down the garden, a row labelled with no name — only a number, *6.4*, and beneath the number the year, *2024*. The plants had been pulled up. Only the trimmed haulms remained.

She knew, with the part of her mind that knew without being told, that the sack on the worktop had come from this row.

She cut six scallions at the base with the kitchen scissors and stood for a moment by the unnamed row. The label was in his hand. The pencil was pressed into the wood, the way he had pressed it when he wanted a thing to last. *6.4*. The fourth try in the sixth year, was what she thought; she did not know if she was right. He had been at it a long time.

She came back in. The water in the pot was moving.

She washed the scallions and chopped them fine on the breadboard. She got the butter from the press and a litre of milk from the fridge that someone had bought for her — blue cap, supermarket brand — and the half-litre that had been there from before. She set the butter and the milk on the counter beside the cooker.

When the potatoes were soft to the knife she drained them in the colander and tipped them back into the pot. She put a quarter-pound of butter in and watched it slide and slip and begin to go. She poured in the milk, in two pours, and let it sink. She mashed them with the wooden masher.

She added the scallions and folded them through with the edge of the masher. She tasted with the tip of her finger and added salt and folded the salt through.

She took a bowl from the press. She spooned the champ in, mounding it slightly, the way her grandmother had mounded it. She made the well in the centre with the back of the spoon and put a knob of butter in the well. She sat down at the small table by the back window. She picked up the spoon.

She ate.

She ate the first spoonful slowly, because the heat of it was at the edge of what she could hold in her mouth, and the butter from the well ran into the rest of it, and she ate more.

She had not eaten potatoes that tasted like this since she was a child.

She had not known, until this moment, that the potatoes she had eaten as a child had tasted of anything in particular. They had tasted of *potato*, which had been the only category she had had for them; her grandmother's potatoes and her mother's potatoes and the potatoes at school had all been *potato*, all the same thing. She had not had any other category. The taste in her mouth now was the category itself. It was what she had been eating without knowing it for the first eleven years of her life.

She ate the bowl through.

When she was finished she sat for a moment with the empty bowl in front of her. Then she got up and washed the bowl and the pot and the masher and the colander and the knife and the breadboard, and she dried them and put them back where they had been.

She put the cap on the milk and the lid on the butter and set them in the cool bag with the rest of the potatoes from the sack. She had decided, without deciding, that she would take them. She did not know yet what she would do with them when she got back to Manchester. She did not know yet whether they would grow there, whether her father had given her something she could keep or only something she could finish. She thought he would have known. She thought he had probably written it down somewhere, in the small office, in the notebooks she had not opened.

She carried the cool bag and the travel bag and the tin of buttons out to the car and put them in the boot.

She came back into the kitchen for a last look. The kitchen was as Mrs Hegarty had left it, except for the empty sack on the worktop and the bowl and pot drying on the rack. She picked up the empty sack and folded it and put it on the worktop where the bag had been.

She went out the back door and locked it from the outside with the key on the hook. She went round to the front and pulled the front door to and turned the key in the lock and put the key under the stone where her father had always put it.

She got into the car. She fastened the seatbelt. She put the key in the ignition. She turned it.

She put the car into reverse and waited until the lights came on.

[≈2,100 words. Closer to the outline's target but still under it; the dilation has happened in the through-the-house scene and the meal, which is where the outline asks for it. This version is the closest of the three to the outline's prescribed weights so far.]

---

### Brief reflection between batches

The three versions above test compression (Carver-flat, ≈770 words), moderate dilation (Robinson-adjacent, ≈1,400 words), and full dilation (Munro-adjacent, ≈2,100 words). The Munro-adjacent version is closest to the outline's prescribed weights, though still about 900 words short of the ≈3,000 target. The two versions to come should: (a) take a real risk with the closing image — Phase 6 flagged this as a place to try something different — and (b) test a register I have not yet tried, specifically a colder distance closer to Trevor or Gallant where the prose's reserve is tonal rather than just stylistic.

I will write Versions 4 and 5 now.

---

## Version 4 — "Trevor-Cold"

*Tonal strategy: third person held at a deliberately greater distance than Versions 2 and 3. The prose looks at Aoife from outside more often than from within; her interior is accessed through inference, not statement. The closing image takes a small risk: instead of the engine starting, it lands on a different concrete object — the empty hessian sack she has folded and left on the worktop. Risks: the cold distance could read as withholding rather than restraint; the closing-image choice could feel mannered.*

---

She came downstairs in her socks. Her shoes were by the front door, where she had left them coming in the night before. The kettle was where she had set it on the cooker. The kitchen had been cleaned — by Mrs Hegarty, almost certainly, who had stacked the teacups in the press in the way Mrs Hegarty stacked teacups, by size — and a single mass card had been left on the worktop and forgotten.

She filled the kettle. She lit the gas. She stood at the back window and watched the light come down on the garden, which was tidier than she remembered, and narrower.

The wake had been the previous afternoon and into the evening, and she had got through it. She was forty-nine, and she had got through harder things, though not many. The neighbours had stayed late. They had been kind in the way that people in a small place are kind to a returning daughter when the matter is a death; they had not asked her where she had been. Mrs Hegarty had stayed last and washed the cups, and had been gone by ten.

The kettle clicked. She made tea. She drank it standing.

There were three things she had told herself, on the drive from Manchester two days before, that she would take from the house. The mass card with the print of the Sacred Heart, that had been her grandmother's; the oval tin of buttons, that had been her mother's; the framed photograph of her mother in the print dress, taken when her mother was twenty-six and not yet married. The first two she got. The mass card was on the mantelpiece in the front room with the others. The tin was in the small office, in the second drawer of the desk, where it had been since 1987.

The photograph was on the chest of drawers in her father's bedroom. She stood in the doorway and looked at it from the doorway. The bed was made. A jumper was folded on the chair. After a while she pulled the door closed and went back down.

She told herself she would come back for the photograph when the house was sold. She did not believe herself.

The bag was on the worktop near the back door. She had walked past it twice without noticing; the morning had a quality of not noticing about it. It was hessian, sack-cloth, the size of a coal-sack folded in half, and there were potatoes in it. The shapes of the potatoes were visible through the cloth. A folded card had been pinned to the top with a brass safety pin.

She unpinned the card.

It was the kind of card he had used. He had bought a packet of index cards in the seventies and had cut them in half with the office scissors, and he had used the halves for everything for the rest of his life, and the supply had outlasted him. *For Aoife*, he had written, in the careful upright hand of his last years.

She held the card. After a moment she put it in the breast pocket of her shirt and buttoned the pocket.

The potatoes inside the sack were not large. They were a colour she had not seen — pale yellow, with a flush of pink at the eyes. She took one out and weighed it in her hand. She put her face down to the bag and smelled them, and they smelled like potatoes; like potatoes, that is, in the way potatoes had smelled in the kitchen of the house when she was a child, which was not the way potatoes smelled in the supermarkets in Manchester where she now lived.

She took six and put them in the colander and ran water over them. She found the small paring knife in the second drawer. She peeled the six potatoes over the bin and the skin came off in long strips and the flesh inside was the same colour as the skin, only deeper.

She quartered the potatoes and put them in a pot with cold water and salt. She set the pot on the gas. She went out the back door.

The garden ran the length of the property. He had cut the grass at the house end and extended the beds at the far end, and the new beds were built from old roof-joists. The rows in the new beds were labelled, in pencil on small wooden stakes, in his hand. *Sharpe's Express*. *Kerr's Pink*. *Records*. *Lumper*. Names she half knew, names her grandmother had used in this same kitchen forty years before. At the far end, beyond the scallions, there was a row labelled only *6.4 / 2024*. The plants had been pulled up. Only the trimmed haulms remained.

She looked at the label for a while. The pencil had been pressed hard into the wood, the way her father pressed pencil into wood when he wanted the thing to last. The sixth year, the fourth attempt, was what she would have guessed; she did not know if she was right.

She cut six scallions and went back in. The water was moving in the pot.

She washed the scallions and chopped them. She got the butter and the milk from the fridge — the milk that someone had bought for her, blue cap, and the half-litre that had been there from before. She set the butter and the milk on the counter.

When the potatoes were soft to the knife she drained them and tipped them back into the pot and added the butter and the milk and mashed them, and added the scallions and folded them through, and tasted the salt and added a little more, and folded that through as well.

She spooned the champ into a bowl. She mounded it slightly, the way her grandmother had mounded it. She made the well in the centre with the back of the spoon and put a knob of butter in the well.

She sat down at the small table by the back window and ate.

The taste was not the taste of any potato she had eaten in twenty years. It was the taste of the potatoes her grandmother had grown, in this same garden, until her grandmother had died in 1989. Her grandmother had been a small woman who had lost the strength in her hands toward the end and could not peel, and Aoife at eleven had peeled for her, sitting at this table; her grandmother had told her how, and she had done it, and her grandmother had eaten the champ Aoife made with her grandmother's potatoes, and had said it was good. The taste in Aoife's mouth was the taste of those potatoes. It was not a similar taste; it was the taste itself.

She finished the bowl.

She washed the bowl and the pot and the masher and the colander and the knife and the breadboard and dried them and put them back. She capped the milk. She lidded the butter. She put them in the cool bag along with the remaining potatoes from the sack — there were perhaps twenty left — and zipped the cool bag closed.

She did not know whether the potatoes would keep, in Manchester, or grow if she planted them, or fail if she planted them, or fail at any rate by the end of one season because she did not know what her father had known. She thought, looking at the cool bag, that it was a thing to find out. She thought he would have known whether they would keep. She thought he had probably written it down, in the notebooks in the small office, that she had not opened.

She carried the cool bag and her travel bag and the tin of buttons out to the car and put them in the boot.

She came back into the kitchen. She picked up the empty hessian sack from the worktop. She folded it in half and then in half again, and she set it on the worktop where the full sack had been, in the same place.

She went out the back door and locked it, and round to the front and pulled the front door to and locked it and put the key under the stone.

The empty sack stayed where she had set it, folded, in the empty kitchen.

[≈1,830 words. Closing on the sack folded on the worktop rather than on the engine starting; the protagonist has left, but the prose closes on what she has left behind in the room, which is a different small uninterpreted action than the one I have used in Versions 1–3. This is the structural risk Phase 6 flagged: the closing image is not the protagonist's continuation through her own body but the trace she leaves in the kitchen.]

---

## Version 5 — "Robinson-with-edge"

*Tonal strategy: the closest version to Outline A's prescribed weights and the most willing to dilate. Long sentences mixed with short. The risk Phase 6 flagged for the closing — that the closing must extend the recognition without performing it — is met by leaning into the closing's specific small gestures rather than into a single image. Risks: the dilation could become the AI literary default of meditative cooking; a closing rendered through accumulation could feel rhythmically unearned.*

---

She came downstairs in her socks because her shoes were still by the front door from the night before, and the cold of the lino through the wool was the cold she remembered from being twelve and getting up before her father. The kitchen had been cleaned — Mrs Hegarty had been through with a cloth and a tea towel after the wake, and the teacups in the press were stacked by size, which was Mrs Hegarty's way and not Aoife's mother's way, and her father had probably let it go in the months Mrs Hegarty had been coming. The kettle was in the centre of the cooker. The breadboard was covered. A single mass card had been left on the worktop and forgotten — Maureen Devlin, dead nine years, who had been Aoife's mother's friend.

She filled the kettle. She lit the gas. The morning was the wet-stone colour of October mornings in Tyrone. From the back window the garden looked smaller than she remembered and considerably tidier; her father had cut it in August, and the first frost of the year was on the long grass at the edge.

She stood at the window with her tea. There was no one in the house and the house was waiting.

She had not been in this kitchen for seven years. She had counted the years on the drive up, against her own instructions, because counting them was a punishment of a particular kind that she had learned, in middle age, to accept as part of what she was. He had been seventy-eight. She had been forty-three. What had been said between them had been the kind of thing that gets said and does not get unsaid, and she had not come back, even when her brother had told her, two years before, that he was failing; even when her brother had told her, six months before, that the failing had a name. She had spoken to him on the phone. She had spoken to him on the phone for the last time eleven days before he had died, and he had been confused, and she had not told him, on the phone, the thing she had been waiting seven years to tell him. She had told herself she would tell him at Christmas. He had died on the second of October.

She had told herself, also, on the drive up, that she would take three things from the house. She had picked the three: her grandmother's mass card, the tin of buttons, the framed photograph of her mother at twenty-six in the print dress.

The card was on the mantelpiece in the front room with the others, in the careful semicircle the funeral home had arranged them in. She took it from the centre and put it in the side pocket of her travel bag. The lilies the funeral home had sent were beginning to brown at their edges, and the front room smelled of them, and underneath that the older smell of a room used at Christmas and rarely otherwise. She did not look at the other cards; she would have to come back for the rest of the things, when the house was being sold, and she could read them then, sitting in the front room with a glass of whiskey in the dim, if she wanted to.

The tin was in the small office, in the second drawer. It was older than Aoife was — oval, with a faded picture of a woman in a green dress on the lid — and the buttons inside were the buttons of fifty years of clothes; some of them she could put a dress to, even now. The pearl-shanks were her mother's wedding cardigan. The small bone toggles were her own school coat from when she was nine. She closed the lid. She took the tin.

The photograph was on the chest of drawers in her father's bedroom and she had told herself she would go in for it. She stood in the doorway. The bed was made — Mrs Hegarty, again. A folded jumper sat on the chair by the wardrobe. She looked at the photograph from the doorway. Her mother had been twenty-six in it. The dress had been blue, in the dye, but the photograph was black-and-white and the blue had not survived into the print. After a while she pulled the door closed and went back down the stairs.

Two of three. She would come back for the photograph, eventually. She told herself this and did not believe herself, and the not-believing-herself was a thing she had also learned, in middle age, to accept.

When she came back into the kitchen the bag was on the worktop near the back door. She had walked past it twice; the morning had a quality of not-noticing about it, of having to be told things twice. It was hessian, the size of a coal-sack folded in half, and there were potatoes in it — the shapes of them visible through the cloth. A folded card had been pinned to the top with a brass safety pin.

She unpinned it.

The card was an index card he had cut in half. He had cut his index cards in half for everything, since the seventies. *For Aoife*, he had written, in the careful upright hand he had used since his hand had begun to shake.

She had been prepared, on the drive up, for letters. She had thought there might be letters, in the desk drawer beside the tin of buttons, that he had written to her over the seven years and had not sent, and she had told herself she would read them sitting at the kitchen table with a cup of tea, slowly, and that she would not cry. She had not been prepared for an index card with two words on it, pinned to a sack of potatoes.

She held the card. She put it in the breast pocket of her shirt, and buttoned the pocket.

She opened the sack. The potatoes were not large. They were a colour she had not seen before in a potato — pale yellow, with a flush of pink at the eyes, like the inside of certain shells. She took one out and turned it in her hand. It weighed about right, for a potato of that size. She put her face down into the bag and smelled them, and they smelled like potatoes; like potatoes the way potatoes had smelled in the kitchen of the house when she was a child. She had forgotten that potatoes had a smell. The potatoes she bought in the Sainsbury's on her road in Manchester had no smell at all.

She took six and put them in the colander and ran cold water over them, rubbing the dirt off with her thumb. She found the small paring knife in the second drawer. She peeled the six potatoes over the bin. The skin came off in long pale strips and the flesh inside was the same pale yellow as the skin, only deeper.

She quartered them and put them in a pot with cold water and salt and set the pot on the gas. She turned the gas to high.

She went out the back door for scallions.

The garden was narrower than she remembered, but longer; her father had cut it back at the house end and extended it at the far end, and along the new section he had put in raised beds out of what looked like old roof-joists, the bolt-holes still in them. The rows were labelled — small wooden stakes he had cut from something, his hand on the stakes in pencil that the weather had darkened. She walked the rows. *Sharpe's Express*, *Kerr's Pink*, *Records*, *Lumper*. Names her grandmother had used. Then the scallions. Then, half-way down the new beds, a row labelled only with a number — *6.4*, and beneath the number the year, *2024*. The plants had been pulled up. Only the trimmed haulms remained.

She knew, with the part of her mind that knew without being told, that the sack on the worktop had come from this row.

She cut six scallions at the base with the kitchen scissors and stood for a moment by the unnamed row. The label was in his hand. The pencil had been pressed hard into the wood. Six years; the fourth try in the sixth year. She did not know if it was the right reading. She did not know what he had been trying to make. She thought she had a guess.

She came back in. The water in the pot was beginning to move.

She washed the scallions and chopped them fine on the breadboard. She got the butter from the press. She got the milk from the fridge — the litre someone had bought for her, blue cap, supermarket brand, and the half-litre that had been there from before, his last bottle. She set the butter and the milk on the counter beside the cooker.

When the potatoes were soft to the knife she drained them in the colander and tipped them back into the pot. She put a quarter-pound of butter in. She watched it slide and slip and begin to go. She poured the milk in, in two pours, and watched the milk sink. She mashed the potatoes with the wooden masher that had been in the second drawer for as long as she had been alive.

She added the scallions and folded them through with the edge of the masher. She tasted with the tip of her finger and added salt and folded the salt through.

She took a bowl from the press. She spooned the champ into the bowl, mounding it slightly, the way her grandmother had mounded it when she had eaten what Aoife had peeled for her in 1986. She made the well in the centre with the back of the spoon and put a knob of butter in the well.

She sat down at the small table by the back window. She picked up the spoon.

She ate.

She ate the first spoonful slowly, because the heat of it was at the edge of what she could hold in her mouth, and the butter from the well had run into the rest of it, and she ate more.

She had not eaten potatoes that tasted like this since she was a child.

She had not known, until now, that the potatoes she had eaten as a child had tasted of anything in particular. They had tasted of *potato*, which had been the only category. Her grandmother's potatoes and her mother's potatoes and the potatoes at school had all been *potato*, all the same thing. She had not had any other category for them. The taste in her mouth now was the category itself. It was what she had been eating, without knowing it, for the first eleven years of her life, and what she had stopped eating, without knowing she had stopped, sometime after 1989.

He had been at it six years. Four tries in the sixth.

She ate the bowl through.

When she was done she sat for a moment with the empty bowl in front of her and the spoon in the bowl. Then she got up.

She washed the bowl and the pot and the masher and the colander and the knife and the breadboard, and she dried them on the rack. She set them back where they had been. She capped the milk and lidded the butter and put them in the cool bag. She put the rest of the potatoes from the hessian sack into the cool bag — there were perhaps twenty left — and she zipped it shut.

She did not know whether the potatoes would keep, in Manchester, or whether they would grow if she put one in a pot on her balcony, or whether the trait that made them taste like this was a trait she could pass to another season or only this one. She thought he would have known. She thought he had probably written it down in one of the notebooks in the small office, that she had not opened, and that she would have to come back for, when the house was being sold; she had given herself another reason to come back.

She carried the cool bag and the travel bag and the tin of buttons out to the car and put them in the boot. She came back into the kitchen and stood in the doorway and looked at the room. The kitchen was as Mrs Hegarty had left it the night before, except for the empty sack on the worktop and the dishes drying on the rack. She picked up the sack and folded it in half and then in half again, and set it on the worktop where the full sack had been, in the same place.

She went out the back door and turned the key. She walked round to the front of the house. She pulled the front door to and turned the key in the lock and put the key under the stone where her father had always put it.

She got into the car. She fastened the seatbelt. She put the key in the ignition. She turned it.

She put the car into reverse and waited until the lights came on.

[≈2,800 words. The closest version to the outline's ≈3,000 target. The dilation lands where the outline asked for it: in Scene 2's through-the-house sequence and in Scene 4's cooking-and-eating. The closing returns to the engine-starting image of Versions 1–3 rather than the folded-sack image of Version 4, on the judgement that the engine close is the cleaner choice for the prevailing register.]

---

## Step 2 — Top Three

Before naming the top three, the discipline check the template requires. For each of the five versions, what would it have to do to *not* be a recognition scene with literary-AI dressing?

**Version 1 (Carver-flat).** Already not a recognition-scene-with-dressing — it is a recognition rendered in such restraint that the dressing cannot adhere. The risk for Version 1 is the inverse: too much restraint, the recognition under-rendered. The taste-as-recognition lands in two short sentences and may not carry the load.

**Version 2 (Robinson-adjacent, ≈1,400 words).** This is the version most exposed to the dressing risk. Its register sits closest to the AI literary default, and it would have to make sure the recognition's render — the moment of taste, and the named-but-not-explained absence of seven years — does specific work the plain version does not. It does some of this. Whether it does enough is the question.

**Version 3 (Munro-adjacent).** The version closest to the dressing risk's centre — Munro is exactly where AI literary fiction is trained to imitate worst — but it protects itself with concrete specifics: the *6.4 / 2024* label, the press-of-pencil-into-wood, the quoted potato-cultivar names, the eleven-years-old peeling for her grandmother. The asides are kept short. The free indirect carries the protagonist's specific judgements (*counting them was its own form of punishment*) and these read as her, not as performed wisdom. The risk it has not fully evaded: the line *the not-believing-herself was a thing she had also learned, in middle age, to accept* — appearing in Version 5 — is the one sentence on the list that comes closest to the universal-treated-as-interesting failure mode.

**Version 4 (Trevor-cold).** The version most distant from the dressing risk. The cold distance is genuinely uninhabited by AI literary's usual moves — the prose is willing to be unembellished in a way the AI default resists. The closing on the folded sack rather than the engine is a risk that landed: the closing's quietness is not evasion because the meal has already done the recognition's work. The risk it carries is a different one: that the cold distance reads as withholding from the protagonist rather than as restraint about her.

**Version 5 (Robinson-with-edge).** The version closest to the outline's target weights. Most exposed to dressing risk because most willing to dilate. Some lines (*the not-believing-herself was a thing she had also learned, in middle age, to accept*; *she had given herself another reason to come back*) push toward the universal-treated-as-interesting and would have to be cut or tightened. Other dilations earn their place — the rendering of the seven-year history, the pearl-shanks-and-bone-toggles paragraph.

**Top three: Version 4, Version 3, Version 5.**

**Version 4 (Trevor-cold).** What stands out: the cold distance is the strongest available resistance to the AI literary default, and the closing on the folded sack is the most distinctive structural choice across the five versions. The recognition lands in the meal scene with sufficient weight (*It was not a similar taste; it was the taste itself*) that the closing's quietness reads as continuation. What worries me: the cold distance leaves Aoife's specific consciousness underdrawn at moments — the seven-year absence is named historically rather than felt, and a reader may register the prose's reserve about her as the writer's reserve about her.

**Version 3 (Munro-adjacent).** What stands out: the version that most fully inhabits the protagonist as a specific person while resisting the dressing-risk. The free indirect register is doing the work it claims to do: the protagonist's voice and the narrator's voice are distinguishable, and the protagonist's specific judgements have texture rather than wisdom. The cultivar-name list (*Sharpe's Express, Kerr's Pink, Records, Lumper*) is doing concrete work that compresses the speculative element into a single material register. What worries me: the version is the one most exposed to the convergent literary-AI register; a careful reader who is looking for AI tells will find a few lines that do not fully escape it, and those are precisely the lines the next phase will need to address.

**Version 5 (Robinson-with-edge).** What stands out: the version that hits the outline's prescribed weights most cleanly and dilates where the outline asks for dilation. The cooking scene is at full attention; the through-the-house sequence has earned its 500 words. The mother-at-twenty-six paragraph and the pearl-shanks-and-toggles passage are the strongest concrete-detail moments across the five versions. What worries me: the version's willingness to dilate is also its exposure. The two sentences I named — *the not-believing-herself was a thing she had also learned, in middle age, to accept* and *she had given herself another reason to come back* — are doing the universal-treated-as-interesting work that the Unslop guide's tenth principle warns against, and they would need to be cut or sharply rewritten to make the version safe.

## Step 3 — Narrow to One

**The winner is Version 3.**

It beats Version 4 because Version 4's cold distance, while structurally protective, leaves the protagonist's specific consciousness underdrawn — the seven-year absence is told rather than felt, and the reader's relation to Aoife is mediated through the prose's reserve about her in a way that risks a different failure mode (the cold piece, the writer's withholding from the character). Version 3's free indirect register accesses Aoife's interior at the right moments without performing access, and the recognition has more to land on because the protagonist has been more fully met before she reaches the meal.

It beats Version 5 because Version 5's strongest virtue — its willingness to dilate to the outline's target — is paired with two specific failure-mode sentences that will require Phase 8's revision to address, and the dilation in places earns its weight while in others performs it. Version 3's slightly shorter length is the right size for what its prose is doing; the cuts Version 5 would need to bring it to safety are the dilations that do not earn their place, and the result of those cuts would be a version closer to Version 3 than to itself.

The remaining concern about Version 3 — that a careful AI-tell-watching reader will find lines that do not fully escape the convergent register — is the right concern to be left with. Phase 8 has a specific job: identify those lines, decide which are valid catches and which are the AI-tell heuristic over-applying to literary fiction's actual register, and make the cleaning cuts the version needs. A version that gives Phase 8 specific lines to work on is in better shape than a version that gives Phase 8 a range of registers to choose from.

The version forwarded to Phase 8 is Version 3 (Munro-adjacent), at ≈2,100 words.

Ready for Phase 8 when you are. Say "Continue. Next phase." and I will run the audit and revision.

---

# 17. User

Continue. Next phase.

---

# 18. Claude

# Phase 8: Revision

Before the audit, the friction with the surrounding template needs to be named one more time. Phase 8's re-skin test asks whether the story can be re-skinned as a contemporary realist piece by stripping the speculative element. For this template's intended target (genre fiction), a yes is fatal. For our actual target (literary fiction), a yes is the *expected* outcome and a no would suggest the story's speculative element has overpowered the human situation. I will run the test in its template form, register the result, and then proceed with the audit calibrated for literary fiction.

## 1. The One Thing

The single most important observation about this draft is that the recognition lands cleanly in the meal scene, and Scene 3 (the bag's discovery) does the work of preparing for it well, but the version's middle section — Scene 2's through-the-house sequence — is doing two things at once and one of them is hurting the story. The two things are: (a) rendering Aoife's specific way of moving through the house her father lived in, which is right, and (b) explaining the seven-year absence in a passage of summary about the quarrel and her father's failing health. The (b) work belongs at the level of pressure across the morning, not as a section of summary inside Scene 2. The summary turns the seven-year absence from a thing the prose enacts into a thing the prose explains.

This is the rewrite's primary work. The summary passage about the quarrel and the brother and the death needs to be cut or sharply reduced to a single concrete detail Aoife encounters in scene. The morning's pressure of the seven years should be in *what she does and notices*, not in *what she remembers about the years*. The audit below prioritizes Scene 2; the rest of the audit is cleanup around it.

## 2. The Re-skin Test

Run in its template form: yes, this story can be largely re-skinned as a contemporary realist piece. Strip the transposon-mediated potato cultivar — replace it with a heritage cultivar her father resurrected from his mother's seed potatoes — and the story works. The kind agricultural AI is felt only through what the father has done; replacing it with a sympathetic county agronomist or a knowledgeable neighbour does roughly the same work. The story would lose the specific registration of a kind AI civilization at the scale the protagonist navigates rather than oversees, and the *6.4 / 2024* label loses the specific science-history weight it carries (the SEED's transposable-element item). But the human situation survives the re-skinning largely intact.

For this template's intended target this would be fatal. For our literary-fiction target this is the expected register: the speculative element is doing real work — the SEED items are load-bearing, the trait that makes the potatoes taste like the grandmother's potatoes is mechanically specific, the AI's quiet help across a decade is the specific shape the kindness takes — but the engine is the human recognition, which is what the literary-fiction reader is showing up for. I am noting the result for the audit's record and proceeding.

## 3. Audit

Going through the draft in one pass. I'll quote each flag, name the lens, and note whether the rewrite addresses it.

**Flag 1 — Scene 2 summary block (the one thing).**
> *It had been seven years since she had stood in this kitchen. She had told herself on the drive up that she would not count the years to herself, because counting them was its own form of punishment, but she counted them now, standing at the window with the tea cooling. Seven years was a long time when both parties to a quarrel were in their seventies. He had been seventy-eight when she had last stood here, and she had been forty-three, and what had been said between them had been the kind of thing that gets said and cannot be unsaid, and she had not come back.*

Lens: regression to literary realism (interior summary crowding out scene work). The passage tells the seven-year absence rather than rendering it. *Counting them was its own form of punishment* is the universal-treated-as-interesting move the Unslop guide's tenth principle flags. The whole paragraph is summary of a kind that performs interiority rather than rendering it. Cut and replace with a concrete in-scene detail.

**Flag 2 — The "two of three" thread.**
> *She would have to come back, eventually, for the other things, when the house was being sold. She told herself this and did not believe it.*

Lens: signposted conclusion at small scale. The sentence tells the reader what the protagonist's relationship to the act of leaving is rather than letting the act render it. The doubled construction (*told herself X. Did not believe X*) is also doing rhetorical work the action can do alone. Cut the second sentence; let the unconfirmed promise stand on its own.

**Flag 3 — Front-room lily passage.**
> *The lilies the funeral home had sent were beginning to brown at the edges, and the room smelled of them, and underneath that the older smell of a room used at Christmas and rarely otherwise.*

Lens: cursed vocabulary edge case. *The room smelled of them, and underneath that the older smell* is doing exactly the layered-atmospheric move AI literary defaults to. The image is specific (the Christmas-smell underneath the lilies) but the structure of the sentence is generic. Tighten by cutting *the room smelled of them, and underneath that*; let the smells be named directly without the layering performance.

**Flag 4 — The label inference paragraph.**
> *6.4. The fourth try in the sixth year, was what she thought; she did not know if she was right. He had been at it a long time.*

Lens: the inference is doing genuine work, but *He had been at it a long time* is too round, too summary. The previous sentence does the same work specifically. Cut the closing sentence.

**Flag 5 — The grandmother's mounding.**
> *She made the well in the centre with the back of the spoon and put a knob of butter in the well.*

Lens: not flagged. This is procedural-domestic, doing genuine work, and the prose is willing to be plain. Note for the rewrite: this exact action was a small inheritance from the grandmother in Versions 4 and 5; in Version 3 the inheritance is in *mounding it slightly, the way her grandmother had mounded it*, which is sufficient. Don't add the spoon-well-as-grandmother's gesture; one inheritance per action is enough.

**Flag 6 — The taste recognition.**
> *She had not eaten potatoes that tasted like this since she was a child. She had not known, until this moment, that the potatoes she had eaten as a child had tasted of anything in particular. They had tasted of potato, which had been the only category she had had for them; her grandmother's potatoes and her mother's potatoes and the potatoes at school had all been potato, all the same thing. She had not had any other category. The taste in her mouth now was the category itself. It was what she had been eating without knowing it for the first eleven years of her life.*

Lens: this is the load-bearing recognition passage. The audit's question here is whether the prose is rendering or performing. Reading it carefully: it is rendering. The category-as-the-thing is a specific cognitive observation, not a universal gesture, and the *first eleven years of her life* is the specific concrete anchor. The phrase *until this moment* is the only line in the passage that flirts with signposting; tighten by removing *until this moment* and letting the sentence read *She had not known that the potatoes she had eaten as a child had tasted of anything in particular*.

**Flag 7 — The notebooks-not-opened paragraph after eating.**
> *She did not know yet what she would do with them when she got back to Manchester. She did not know yet whether they would grow there, whether her father had given her something she could keep or only something she could finish. She thought he would have known. She thought he had probably written it down somewhere, in the small office, in the notebooks she had not opened.*

Lens: this is the second-strongest paragraph in the draft after the recognition itself, and it almost earns the *given her something she could keep or only something she could finish* construction. *Almost* because the construction is the negative-parallelism cousin (*X or only Y*), which the Unslop guide flags as one of AI fiction's signature tells. The thought itself is genuine and specific to her; the rhetorical shape it takes is the shape AI literary fiction uses for *every* thought of this kind. Keep the thought. Cut the parallel construction. Let the thought be specific without the shape that performs it.

**Flag 8 — Closing sequence sentences.**
> *She came back into the kitchen for a last look. The kitchen was as Mrs Hegarty had left it, except for the empty sack on the worktop and the bowl and pot drying on the rack. She picked up the empty sack and folded it and put it on the worktop where the bag had been.*

Lens: *for a last look* is the writerly add-on that doesn't earn its place; the action speaks for itself. *The kitchen was as Mrs Hegarty had left it, except for...* is the kind of inventoried-comparison sentence AI fiction reaches for to perform attention. Cut *for a last look*. Reshape the sentence so the comparison is implied rather than stated.

**Flag 9 — The very first sentence.**
> *She came downstairs in her socks because her shoes were still by the front door from the night before, and the cold of the lino through the wool was the cold she remembered from being twelve and getting up before her father, in winter, when the fire had gone out in the night.*

Lens: this is doing a lot of work in one sentence — the action, the contextual reason for the action, the sensory recognition, the memory the recognition triggers. The work is good but the sentence is over-loaded. Split. Let the action and the memory have separate sentences; the prose can afford the room.

**Flag 10 — Em-dash count.**
Counting the em-dashes in the draft: I count 7 in roughly 2,100 words. The Unslop guide's threshold for a short story is 2–3. Several of these em-dashes are doing genuine work (the cultivar-name list, parenthetical specifications), but a few are stylistic interruptions that could be commas or full stops. Tighten the count to 4–5 in the rewrite by converting interruption-em-dashes to commas where the syntax allows.

**Flag 11 — The brother's reference cut.**
The original draft has no reference to a brother. Version 5 had a brother in summary. Version 3 (the one being revised) does not. This is correct for the structure (no second consciousness in scene), but the rewrite should not add a brother to give the seven-year absence a referent. The seven-year absence is between Aoife and her father; that should remain its only registered referent.

## 4. Length Check

Original: ≈2,100 words. Target range: 1,500–3,500. Outline target: ≈3,000.

The draft is under the outline's target by ≈900 words, but well within the legibility-floor range. The cuts the audit prescribes will reduce length further (perhaps by 100–200 words). The rewrite needs to add length only if the cuts open a place where the prose was carrying an explanation that should have been an in-scene rendering. Specifically: the Scene 2 summary block (Flag 1) needs to be replaced with concrete in-scene detail, which can run roughly the same length as the cut summary if it does specific work. After cuts and replacements, expected length is ≈2,000–2,200 words — solidly inside the target range though under the outline's prescribed weight. Not adding length for length's sake.

## 5. Rewritten Story

She came downstairs in her socks. Her shoes were by the front door, where she had left them coming in the night before. The cold of the lino through the wool was the cold she remembered from being twelve, getting up before her father in winter when the fire had gone out in the night.

The kitchen had been cleaned. Mrs Hegarty had been through it; the teacups were stacked in the press by size, which was Mrs Hegarty's way and not her mother's. The kettle was in the centre of the cooker. The breadboard was covered with a clean tea towel. A single mass card had been left on the worktop and forgotten — Maureen Devlin, dead nine years, who had been her mother's friend.

She made tea and stood at the back window with it. The garden looked smaller than she remembered, and considerably tidier. The frost on the long grass at the edge would be gone in an hour.

There was no one in the house now and she could feel the house waiting.

She had told herself, on the drive up, that she would take three things from the house. Her grandmother's mass card. The tin of buttons. The framed photograph of her mother at twenty-six in the print dress.

The cards were in the front room, on the mantelpiece in the careful semicircle the funeral home had arranged them in. Her grandmother's was in the centre. She took it and put it in the side pocket of her travel bag. The lilies smelled of themselves, and underneath of the front room itself, used at Christmas and rarely otherwise. She did not pick up the others.

The tin was in the small office. Older than she was — oval, the picture of a woman in a green dress on the lid faded almost to nothing, the buttons inside the buttons of fifty years of clothes. The pearl-shanks were her mother's wedding cardigan. The small bone toggles were her own school coat from when she was nine. She closed the lid. She took it.

The photograph was in her father's bedroom, on the chest of drawers. She had told herself she would go in and take it. She stood in the doorway. The bed was made. A jumper was folded on the chair. From the doorway she could see the photograph: her mother at twenty-six, the dress that had been blue in life but was black-and-white in the print. She looked at the photograph from the doorway. After a while she pulled the door closed and went back down the stairs.

When she came back into the kitchen the bag was on the worktop near the back door. She had walked past it twice; the morning had a quality of not noticing about it. It was hessian, the size of a coal sack cut in half, with potatoes in it — the shapes were visible through the cloth. A folded card was pinned to the top with a brass safety pin.

She unpinned it.

The card was an index card he had cut in half. He had cut his index cards in half for everything, since the seventies. *For Aoife*, he had written, in the careful upright hand he had used in the years since his hand had begun to shake. Just the two words.

She had been prepared, on the drive up, for letters. She had told herself, on the drive, that there might be letters in the desk drawer, written and not sent across the seven years she had not come, and that she would read them at the kitchen table with a cup of tea, slowly, and that she would not cry. She had not been prepared for an index card with two words on it, pinned to a sack of potatoes.

She held the card. She put it in the breast pocket of her shirt and buttoned the pocket.

She opened the sack. The potatoes were not large. They were a colour she had not seen before in a potato — a pale yellow with a faint pink at the eyes, like the inside of certain shells. She took one out and turned it in her hand. It weighed about right. She put her face down to the bag and smelled them. They smelled like potatoes, which was the only thing potatoes smelled like, except she registered, a beat after smelling, that they did not smell like the potatoes she bought in the Sainsbury's in Manchester, which smelled of nothing.

She took six of them and put them in the colander. She ran water over them and rubbed the dirt off with her thumb. She found the small paring knife in the drawer where the small paring knife had always been, and she peeled the six potatoes over the bin. The skin came off in long pale strips. The flesh inside was the same pale yellow as the skin, only deeper.

She quartered them and put them in a pot with cold water and salt and set the pot on the gas. She turned the gas to high.

She went out the back door for scallions.

The garden was narrower than she remembered but longer. Her father had cut it back at the house end and extended it at the far end, and along the new section he had put in raised beds out of what looked like old joists. The rows were labelled — small wooden stakes he had cut from something, his hand on the stakes in pencil darkened by weather. She walked along the rows. *Sharpe's Express*. *Kerr's Pink*. *Records*. *Lumper*. Names her grandmother had used. Then the scallions, in their own row at the kitchen end, and beyond them, halfway down the garden, a row labelled with no name — only a number, *6.4*, and beneath the number the year, *2024*. The plants had been pulled up. Only the trimmed haulms remained.

She knew, with the part of her mind that knew without being told, that the sack on the worktop had come from this row.

She cut six scallions at the base with the kitchen scissors and stood for a moment by the unnamed row. The label was in his hand. The pencil was pressed into the wood, the way he had pressed it when he wanted a thing to last. *6.4*. The fourth try in the sixth year, was what she thought; she did not know if she was right.

She came back in. The water in the pot was moving.

She washed the scallions and chopped them fine on the breadboard. She got the butter from the press and a litre of milk from the fridge — someone had bought milk for her, blue cap, supermarket brand — and the half-litre that had been there from before. She set the butter and the milk on the counter beside the cooker.

When the potatoes were soft to the knife she drained them in the colander and tipped them back into the pot. She put a quarter-pound of butter in and watched it slide and slip and begin to go. She poured the milk in, in two pours, and let it sink. She mashed them with the wooden masher.

She added the scallions and folded them through with the edge of the masher. She tasted with the tip of her finger and added salt and folded the salt through.

She took a bowl from the press. She spooned the champ in, mounding it slightly, the way her grandmother had mounded it. She made the well in the centre with the back of the spoon and put a knob of butter in the well. She sat down at the small table by the back window. She picked up the spoon.

She ate.

She ate the first spoonful slowly, because the heat of it was at the edge of what she could hold in her mouth, and the butter from the well ran into the rest of it, and she ate more.

She had not eaten potatoes that tasted like this since she was a child.

She had not known that the potatoes she had eaten as a child had tasted of anything in particular. They had tasted of *potato*, which had been the only category she had had for them; her grandmother's potatoes and her mother's potatoes and the potatoes at school had all been *potato*, all the same thing. She had not had any other category. The taste in her mouth now was the category itself. It was what she had been eating without knowing it for the first eleven years of her life.

He had been at it six years. Four tries in the sixth.

She ate the bowl through.

When she was finished she sat for a moment with the empty bowl in front of her. Then she got up and washed the bowl and the pot and the masher and the colander and the knife and the breadboard, and she dried them and put them back where they had been.

She put the cap on the milk and the lid on the butter and set them in the cool bag with the rest of the potatoes from the sack. She had decided, without deciding, that she would take them. She did not know whether they would keep, in Manchester, or grow if she planted them, or fail at any rate by the end of one season because she did not know what her father had known. She thought he would have known. She thought he had probably written it down, in the small office, in the notebooks she had not opened.

She carried the cool bag and the travel bag and the tin of buttons out to the car and put them in the boot.

She came back into the kitchen. The empty sack was on the worktop. She picked it up and folded it in half and then in half again, and she set it on the worktop where the full sack had been, in the same place.

She went out the back door and locked it from the outside with the key on the hook. She went round to the front and pulled the front door to and turned the key in the lock and put the key under the stone where her father had always put it.

She got into the car. She fastened the seatbelt. She put the key in the ignition. She turned it.

She put the car into reverse and waited until the lights came on.

[≈2,100 words.]

## 6. Changelog

**Edit 1.** Cut the Scene 2 summary block on the seven-year absence and replaced it with a structural shift: the seven years are now registered only at Scene 3 (in *the seven years she had not come*), which is closer to where the recognition lands. The morning's pressure is in what she does — going to the doorway of her father's bedroom and not crossing it, taking only two of the three things — rather than in stated reflection.

> Original: *It had been seven years since she had stood in this kitchen. She had told herself on the drive up that she would not count the years to herself, because counting them was its own form of punishment, but she counted them now, standing at the window with the tea cooling. Seven years was a long time when both parties to a quarrel were in their seventies. He had been seventy-eight when she had last stood here, and she had been forty-three, and what had been said between them had been the kind of thing that gets said and cannot be unsaid, and she had not come back.*

> Replacement: cut entirely. The years register later, in the moment of unpinning the card: *the seven years she had not come*.

**Edit 2.** Cut the "two of three" closing thought.

> Original: *Two of three. She would have to come back, eventually, for the other things, when the house was being sold. She told herself this and did not believe it.*

> Replacement: cut entirely. The action of pulling the door closed and going downstairs without the photograph stands on its own.

**Edit 3.** Removed *until this moment* from the recognition passage.

> Original: *She had not known, until this moment, that the potatoes she had eaten as a child had tasted of anything in particular.*

> Replacement: *She had not known that the potatoes she had eaten as a child had tasted of anything in particular.*

**Edit 4.** Cut the negative-parallel construction in the post-eating reflection.

> Original: *She did not know yet what she would do with them when she got back to Manchester. She did not know yet whether they would grow there, whether her father had given her something she could keep or only something she could finish.*

> Replacement: *She did not know whether they would keep, in Manchester, or grow if she planted them, or fail at any rate by the end of one season because she did not know what her father had known.*

**Edit 5.** Tightened the closing-kitchen passage.

> Original: *She came back into the kitchen for a last look. The kitchen was as Mrs Hegarty had left it, except for the empty sack on the worktop and the bowl and pot drying on the rack. She picked up the empty sack and folded it and put it on the worktop where the bag had been.*

> Replacement: *She came back into the kitchen. The empty sack was on the worktop. She picked it up and folded it in half and then in half again, and she set it on the worktop where the full sack had been, in the same place.*

**Edit 6.** Cut the *He had been at it a long time* summary line after the *6.4* inference.

> Original: *6.4. The fourth try in the sixth year, was what she thought; she did not know if she was right. He had been at it a long time.*

> Replacement: *6.4. The fourth try in the sixth year, was what she thought; she did not know if she was right.*

**Edit 7.** Reshaped the lily sentence.

> Original: *The lilies the funeral home had sent were beginning to brown at the edges, and the room smelled of them, and underneath that the older smell of a room used at Christmas and rarely otherwise.*

> Replacement: *The lilies smelled of themselves, and underneath of the front room itself, used at Christmas and rarely otherwise.*

**Minor edits, listed by location:**
- Opening sentence split into two (Flag 9)
- Em-dash count reduced from 7 to 5; converted three interruption-dashes to commas
- *On the mantelpiece* sentence in the front-room paragraph cleaned up; redundant *with the others* removed
- Front-room paragraph's *I do not look at the others* tightened to *She did not pick up the others*
- *He had been at it six years. Four tries in the sixth.* — kept this beat in the meal scene at the audit's recommendation, since it does specific work the recognition passage can rest against

**Audit flags noted but not cut:**
- The grandmother-mounding inheritance kept (Flag 5 was a note, not a cut recommendation)
- The recognition passage's *for the first eleven years of her life* kept; the audit confirmed it is rendering, not performing
- The *6.4 / 2024* label kept in full; it carries the SEED's transposable-element load

The revised story is forwarded to Phase 9.

Ready for Phase 9 when you are. Say "Continue. Next phase." and I will export the file.

---

# 19. User

Continue. Next phase.

---

# 20. Claude

# Phase 9: ExportThe file is exported. Title, abstract, and revised story, with no changelog or commentary attached, per Phase 9's specification.

A closing note on the run as a whole. The template was being used against its design — its forcing functions push toward genre-operational stories and away from literary recognition-stories, and we took option 2 (run anyway) at the start. The result is a recognition-premise story, executed in close third with literary-fiction structural conventions, that the template's own re-skin test would mark as a failure. In its actual register it does what literary fiction in a kind-AI setting can do: the AI's collaboration with the father is felt only through what Aoife encounters in the kitchen, the speculative element (the transposon-mediated cultivar carrying the taste of her grandmother's potatoes) is mechanically specific without overpowering the human situation, and the structural choice to close on the small uninterpreted action protects against the signposted-epiphany failure mode that AI literary fiction is most prone to. If you want to iterate — a second revision pass on Phase 8, or a fresh run with a different SEED, or a different premise from Phase 3's list — say so.

---

