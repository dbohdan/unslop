# 1. User

We are participating in an AI writing contest called "Unslop". Our goal is to help AI write short fiction that isn't slop.

First, we need an understanding of what "slop" is. Read each external link in <https://dbohdan.com/ai-writing-style> with an eye for the negative, repetitive, telling, and stereotypical features of AI prose. Summarize what you learn from each source separately.

# 2. Claude Opus 4.6

Let me start by reading the main page to find all the external links.Got the link list. Let me fetch each source. I'll work through them systematically.Now let me get the other sources.Now I have all the sources. Here are the summaries:

---

**1. Wikipedia: Signs of AI Writing**

A crowdsourced field guide built by WikiProject AI Cleanup editors who reviewed thousands of AI-generated Wikipedia submissions. Key tells: overuse of em dashes in formulaic, sales-like constructions; inflating a topic's importance by connecting it to "broader themes" ("pivotal moment," "significant shift," "rich cultural heritage"); the "not X, but Y" negative parallelism pattern; excessive bolding, bullet points with bolded lead phrases, and rule-of-three adjective stacking; cursed vocabulary like "delve," "tapestry," "landscape," "foster," "underscore"; false ranges ("from intimate gatherings to global movements"); compulsive summary paragraphs even for short passages; vague attributions ("some critics argue," "widely regarded"); uniform sentence and paragraph lengths that flatten any sense of rhythm; and a promotional, interpretive tone where the writing constantly tells the reader what to think rather than presenting facts neutrally.

**2. Reinhart et al., "Do LLMs write like humans?"**

An academic corpus study using Douglas Biber's multidimensional framework of lexical, grammatical, and rhetorical features. Core finding: instruction-tuned LLMs produce a distinctive **noun-heavy, informationally dense** style that persists regardless of prompt. They over-rely on nominalization, participial clauses, "that"-subject clauses, and phrasal coordination. They cannot match human stylistic *variation* — humans shift register across genres (casual speech vs. academic prose vs. fiction), but LLMs collapse toward a single dense, expository mode even when explicitly prompted to write informally. Bigger models don't fix this; instruction tuning actually makes the stylistic gap *worse* compared to base models, which more closely resemble human distributions. The paper frames this as a *rhetorical* problem, not a surface-feature problem: the issue isn't individual word choices but deep structural monotony.

**3. nostalgebraist, "hydrogen jukeboxes"**

The most incisive piece in the set, focused specifically on "creative writing" LLMs (DeepSeek R1 and an unreleased OpenAI model). Central thesis: these models converge on a single, narrow aesthetic strategy — the **abstract/concrete conjunction** or "eyeball kick" (term borrowed from Allen Ginsberg via the Turkey City Lexicon). Every phrase tries to fuse something incorporeal with something sensory: "bruised silence," "lowercase love," "a timestamp like a scar," "the architecture of mourning." This is "crammed prose" — relentless compression where every clause strains to be a standalone "gee-whiz" moment with zero modulation or room to breathe. Other catalogued tics: compulsive personification of inanimate things ("the cursor convulses," "autumn leaves cling"); a tiny rotation of pushbutton mood-words (ghost, echo, whisper, shadow, pulse, hum, flicker, hiss); and the "not X, but Y" parallelism. The key insight: these techniques *exist* in human literature but have their *place*. LLMs deploy them arbitrarily, incessantly, without any higher-level intent — they're pushing 3–4 buttons ad nauseam because those buttons reliably code as "literary" to naive readers/raters. The result is convergent evolution across unrelated models: optimize for generic human judgments of "literary quality" and you get the same narrow, exhausting style every time.

**4. Makin, "How to Identify AI-Written Web Fiction"**

A practitioner's report from the web fiction trenches (fanfic, serial fiction on Questionable Questing, etc.). Main tell: **the droning** — once you've read enough AI-generated long-form fiction, the voice is unmistakable because the model self-poisons over context. Humans instinctively vary; LLMs have the opposite instinct — they stick to whatever patterns already appear in their context window, so cliché density increases as stories get longer. Specific micro-tells: the "not X; Y" construction; lists of three; extremely curt, cliffhanger-style dialogue where every line advances plot and nothing breathes; "blocky" structure with rigidly separated zones of dialogue, exposition, and narration; and when writing "evocatively," a tryhard mode that stacks similes and metaphors on a single concept until it collapses under its own weight. Also notes that em-dash overuse has been partially patched by newer models but the underlying sentence *structures* remain, just with semicolons or commas swapped in. Warns that humans exposed to enough AI prose may start emulating its cadences unconsciously.

**5. Sam Kriss, "Why Does A.I. Write Like … That?" (NYT)**

I couldn't access the full NYT text, but secondary sources and excerpts reveal the argument. Kriss identifies the same core tells — "it's not X, it's Y" parallelism, rule of threes, "delve" and friends — but goes further into *why* it sounds hollow: AI prose tries too hard to sound profound, which produces the opposite effect. He highlights the broader cultural contamination: a Max Planck study found AI-isms increasingly appearing in extemporaneous human speech (e.g., British MPs suddenly saying "I rise to speak," an Americanism propagated via AI). The worry is a feedback loop — AI trains on human text, humans absorb AI-isms, the next generation of models trains on that hybrid corpus, and English flattens. The piece also notes that early GPT had a genuinely funny, surreal quality (headlines like "Spiders Are Getting Smarter, and So, So Loud") that RLHF and instruction tuning have since ground away in favor of smooth, hollow competence.

**6. Tropes.fyi (Ossama Chaib)**

A structured directory cataloguing 33 named AI writing tropes across six categories. Built, the author says, out of spite. The most useful contribution is giving crisp, referenceable *names* to patterns others describe more loosely. Highlights beyond what's already covered above: **"The X? A Y."** — self-posed rhetorical questions answered immediately for manufactured drama; **Short Punchy Fragments** — single-sentence paragraphs for fake emphasis, an artifact of RLHF optimizing for "readability"; **Anaphora Abuse** — repeating sentence openings ("They assume… They assume… They assume…"); **One-Point Dilution** — a single argument restated 8–10 ways across thousands of words; **Grandiose Stakes Inflation** — a blog post about API pricing becomes a meditation on civilizational fate; **Invented Concept Labels** — coining fake analytical terms ("the supervision paradox," "acceleration trap") and using them as if they're established; **The "Serves As" Dodge** — avoiding "is" in favor of pompous copula substitutes because the repetition penalty punishes reuse of simple verbs; **False Vulnerability** — performative self-awareness that reads as polished and risk-free; **Fractal Summaries** — summarizing at every structural level (section, subsection, document); **Dead Metaphor Beating** — latching onto one metaphor and repeating it 5–10 times; **Listicle in a Trench Coat** — disguising a numbered list as continuous prose with "The first… The second… The third…".

**7. Hollis Robbins, "'…as it turns out…'"**

A narrower, more idiosyncratic piece. Robbins examines the phrase "as it turns out" — a human rhetorical device that LLMs conspicuously *don't* use. The phrase works because it implies the speaker already knows the outcome and is withholding it for dramatic effect — a temporal manipulation that requires narrative planning and the pleasure of delayed revelation. LLMs default to immediate, direct exposition; they don't "think ahead" enough to plant and pay off a reveal. Robbins frames this as a *positive* diagnostic: the absence of certain human narrative instincts (coy withholding, timing of disclosure, rhetorical suspense) is itself a marker of AI prose. The flip side of the "slop" problem — AI writing sins not only by commission (overusing certain tics) but by omission (lacking the manipulative storytelling instincts that make human prose feel alive).

# 3. User

Take what you have summarized plus this export from tropes.fyi and create a two-tier writing style guide for Claude:

1. High-level structural and abstract advice
2. Concrete things (tropes, cliches, tics) to avoid

# 4. Claude Opus 4.6

Now let me read the frontend-design skill since this will be a markdown file.

The guide is split into 10 high-level principles (Part I) and 6 categories of concrete avoidances (Part II). Part I synthesizes the deeper structural insights — nostalgebraist's "crammed prose" problem, Reinhart's finding about register collapse, Robbins's point about temporal withholding, Makin's observation about self-poisoning context drift. Part II is the kill list: specific constructions, words, and patterns drawn from all seven sources plus the tropes.md export.

The voicemail/Verizon example in principle #10 is mine — meant to demonstrate the kind of irreducible specificity that distinguishes fiction from thematic decoration. You may want to swap it for something from an actual contest entry or published story.
