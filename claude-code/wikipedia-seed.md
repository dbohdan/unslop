# Wikipedia as a SEED source

This document describes how to use random Wikipedia articles as Phase 2 SEED
material. The protocol was drafted before any live run and first exercised in
[`claude-code/test/comic-sf-2/`](test/comic-sf-2/) (April 26) under the
external-supply workaround below. Measured results from that run are folded
in; protocol changes it motivated are marked **(after run 1)**.

## Probe before committing

The Claude Code-on-the-web sandbox blocks all `*.wikipedia.org` and Wikimedia
hosts at the egress layer (403 with "Blocked by egress policy"). The
`wikipedia2text` Ubuntu package is installable but its `-r` flag returns
"Upgrade Required" — that's lynx rendering the egress 403's body, not a real
Wikipedia response.

Before assuming WP is available, probe with one of:

```sh
wikipedia2text -r          # exits with article body, or "Upgrade Required"
curl -s -o /dev/null -w '%{http_code}\n' https://en.wikipedia.org/wiki/Special:Random
```

If the probe returns the egress 403 or "Upgrade Required," either fall back
on the dictionary procedure documented in CLAUDE.md, or use the
external-supply workaround below.

## External-supply workaround

Used in comic-sf-2. The user runs `wikipedia2text -r` (or any equivalent)
10–15 times on a host with WP egress, packages the outputs as numbered
`.txt` files in a zip, and supplies the zip to the run. The pipeline reads
the dump as if it had drawn the articles itself and applies the discard
rules below.

The dump for comic-sf-2 is preserved at
[`claude-code/test/wp-seed/`](test/wp-seed/) (extracted) and
[`claude-code/test/wp-seed.zip`](test/wp-seed.zip) (archive). Format: one
article per file, `01.txt` … `NN.txt`, lead title and body as
`wikipedia2text -r` produces them.

## Protocol when WP is available

1. Run `wikipedia2text -r` 10–15 times. Save each article's title and lead
   paragraph (typically the first one or two paragraphs of the article body).
2. Apply the discard rules below in order. Stop applying further rules to an
   article as soon as one rule discards it.
3. Keep the first five survivors. Each kept article is treated as an
   already-inflated SEED concept; no further WebSearch is needed.
4. If fewer than five survive after fifteen draws, accept the thin SEED.
   Like the dictionary path's thin SEEDs, this is a feature: it forces each
   survivor to do more work in Phase 3.

## Discard rules

In priority order, with detection heuristics from `wikipedia2text`'s text
output:

1. **Biographies of living people (BLPs).** *Discard.*
   - Heuristic: lead sentence has "(born YYYY)" with no death date, or
     present-tense main verb ("is a", "is an"). If the article has any
     ambiguity about whether the subject is currently alive, discard
     (conservative).
   - Why: fictionalizing living people is legally and ethically risky;
     contest submissions should not depict identifiable living figures.
2. **Disambiguation pages.** *Discard.*
   - Heuristic: lead reads "X may refer to:" or article body is a list of
     short link entries.
3. **Lists.** *Discard.*
   - Heuristic: title begins with "List of " or "Index of ".
4. **Calendar-year and decade articles.** *Discard.*
   - Heuristic: title is `\d{1,4}s?` alone (e.g., "2014", "1990s").
5. **Sports seasons and individual matches.** *Discard.*
   - Heuristic: title contains a year + team/league name (e.g.,
     "1973 Tampa Bay Buccaneers season", "2019 Allsvenskan").
6. **Election articles.** *Discard.*
   - Heuristic: title contains "election" or "by-election" with a year or
     constituency.
7. **Ultra-stubs.** *Discard.*
   - Heuristic: article body is under ~80 words after `wikipedia2text -s`
     (summary mode) or under ~150 words full.
   - **(after run 1)** This rule subsumes "uninteresting small populated
     places." In run 1, three of fifteen draws were small-village stubs
     (Houdelmont, pop. 363; Ulutaş, Mazıdağı, pop. 574; Mill Creek
     tributary), all caught here on body length. **Do not** generalise this
     into "discard all settlements under N inhabitants" — Mokro Polje
     (pop. 163) survived run 1's selection on body weight (Croatian War
     history, destroyed Partisan monument) despite the small population
     and went on to be load-bearing for the winning variant.
8. **Sensitive contemporary subjects.** *Discard, judgement-based.* **(after run 1)**
   - Articles that formally pass rules 1–7 but concern named victims of
     crime, individual injury or illness, mass-casualty events, or
     contemporary atrocities. Run 1's *Conquer Paralysis Now* (a charity
     founded after Sam Schmidt's 1999 spinal-cord injury) passed all
     prior rules but was wrong-tone for comic SF and risked tonal harm
     to a real living person. Discard rather than try to bend the
     story around the topic.
   - This rule is judgement-based, not heuristic. The model should name
     the discard reason in its triage.

## Historical figures: keep, but don't use directly

A biography of a deceased historical figure (Cleopatra, Napoleon III, Hypatia,
Genghis Khan, Florence Nightingale) is rich SEED material — large enough to
color a story without being small enough to vanish in the genre's interior.
**Keep these articles.** Apply one usage constraint at Phase 3:

> A historical-figure SEED item may inflect a story's setting, era,
> ideology, technologies, social structure, or world-feel. It must not be
> the protagonist or a named viewpoint character. The figure can be
> referenced in dialogue or narration, can have descendants or successors
> in the story's present, can be the subject of a museum plaque or a
> re-enactment society or a tradition, but must not be on stage as
> themselves.

Examples of legitimate use:
- Phase-3 conflict that sets up a futurology version of the Diet of Worms,
  with Luther as the historical inheritance the conflict reshapes — but
  the on-stage characters are someone else.
- A character named for Cleopatra, or working in a building named for her,
  or attending an annual festival commemorating her — none of which puts
  Cleopatra on stage.
- A historical figure as the subject of a fictional academic discipline
  ("Hypatian rhetoric"), referenced only.

Examples of misuse: any story where the historical figure speaks, is
described physically, or is the perspective the reader sees through.

The reasoning: historical figures are large enough that fictionalizing them
on-stage tends to make the story *about* the figure rather than *colored
by* them, which dilutes the SEED's role and risks the kind of historical
fiction the pipeline isn't designed for. The "don't use directly" rule
preserves the figure's value as referent without converting them into a
character.

**(after run 1)** The rule held up. Comic-sf-2 used the Moldovan writer
Nicolae Esinencu (1940–2016) as a centrally-organising SEED item — the
catalogue form of the winning variant is built around his correspondence —
and he never appears on stage. He is present only via excerpted letters and
the village's relationship to his "terrible child" reputation. The
difficult writer's relationship to a difficult village is what the story is
*colored by*; the writer himself is not a character. This is the rule
working as intended on a real run.

## Hybrid mode

A future variant: draw five candidates from WP-random and five from the
dictionary path, apply the discard rules to the WP candidates, and keep
the strongest five of the merged pool. Higher variance, more setup cost.

**(after run 1)** Not exercised. Run 1's fifteen draws produced seven
survivors after discard rules — more than the five needed — so no
dictionary backfill was required. The hybrid path is still worth trying
when a future run lands at fewer than five WP survivors, but is not the
default.

## What run 1 measured

Run: comic-sf-2, April 26, fifteen draws supplied externally as
`wp-seed.zip`. Triage table: [`comic-sf-2/phase_2_seed.md`](test/comic-sf-2/phase_2_seed.md).

- **Discard rate: 53% (8 of 15).** Below the 60–80% conjecture, on the
  lower end of the wider plausible range. Big categories were ultra-stub
  geography (3) and BLPs (2), with one list, one tone-fit discard, and one
  single-species moth stub.
- **BLP heuristic: 2 caught, 0 missed.** Both BLPs (Claude Dagens, b. 1940;
  Kathleen Belew, b. 1981) had the "(born YYYY)" lead pattern with no
  death date. Both articles also carried the explicit BLP banner. Sample
  is too small to claim the heuristic is reliable, but it is at least not
  obviously broken.
- **Ultra-stub threshold ~80–150 words holds.** All three ultra-stubs
  caught had 1–3 sentences of body and were correctly discarded. The
  borderline case — *Ecliptophanes* (genus stub, but with six named
  species enumerated) — was kept and proved load-bearing in Phase 7. A
  pure word count on body would have miscategorised it; the species list
  earned the keep.
- **Survivor quality.** Five surviving SEED items (Forensic accounting,
  Mokro Polje, Nicolae Esinencu, The Gravity Group, *Ecliptophanes*)
  inflated cleanly into Phase 3 conflicts and survived through to Phase
  7's winning variant. Direct A/B against a dictionary-source run on the
  same `[GENRE]` and `[LENGTH]` was not done; that comparison is still
  worth making.
- **Article-body extraction.** `wikipedia2text -r` output as supplied was
  usable as-is. No noted parsing oddities. The lead one or two paragraphs
  were sufficient for triage; full body was useful for the survivors at
  Phase 3.

## Still to verify on future runs

- **BLP heuristic on edge cases.** No run-1 article had ambiguous
  living-status (e.g., "(born YYYY)" with the subject having died but the
  death date missing from the lead). The conservative-discard rule for
  ambiguity is untested.
- **Hit-rate variance across draws.** One run's 53% is a sample of one.
  Expect future runs to land anywhere in 40–80%.
- **A/B against dictionary path.** Same `[GENRE]`, same `[LENGTH]`,
  WP-source vs. dictionary-source. The comic-sf-1 run is dictionary-source
  in a comparable register but used a different `[LENGTH]` and was
  written in a different session, so it doesn't quite serve.
- **Tone-fit rule (rule 8) calibration.** Run 1 had one tone-fit discard
  (*Conquer Paralysis Now*) and the call was clean. The rule's
  judgement-based nature means future runs may surface harder cases —
  articles that are partly sensitive, or sensitive in registers other
  than comic SF, or where the SEED could be re-angled to avoid the
  sensitive material. Add notes here when those cases arise.
- **External-supply reproducibility.** Run 1's dump was `wikipedia2text -r`.
  Future runs may use the Wikipedia API's `list=random` or
  `Special:Random` directly. Confirm that other extraction tools produce
  comparable lead-paragraph quality and that the protocol still applies
  without modification.

Update this file with what each subsequent run reveals. Once the rules
have stabilised across two or three runs, the CLAUDE.md Phase 2 section
can fold them in directly and this file can be slimmed to a reference
appendix.
