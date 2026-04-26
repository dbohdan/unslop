# Wikipedia as a SEED source — untested draft

This document proposes how to use random Wikipedia articles as Phase 2 SEED
material once Wikipedia egress is available. **It has not been tested in a
live run.** All claims about hit-rate, distribution, and BLP-detection
heuristics are reasoned, not measured. Treat as a starting point for the
first WP-enabled run; refine after.

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

If the probe returns the egress 403 or "Upgrade Required," fall back on the
dictionary procedure documented in CLAUDE.md and stop reading this file.

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

## Hybrid mode

A future variant: draw five candidates from WP-random and five from the
dictionary path, apply the discard rules to the WP candidates, and keep
the strongest five of the merged pool. Higher variance, more setup cost.
Worth trying once a pure-WP run has been completed and characterized; not
worth implementing before that.

## Things to verify on the first WP-enabled run

- **BLP-detection accuracy.** The lead-sentence heuristic is plausible but
  unmeasured. A first run should record how many BLPs the heuristic
  catches and missed.
- **Hit-rate.** Empirical expectation: rules 1–7 discard 60–80% of random
  draws. A first run will produce a real number.
- **Survivor quality.** Are filtered WP articles richer SEEDs than
  dictionary-inflated words, as conjectured? Compare a WP-source run and
  a dictionary-source run on the same `[GENRE]` and `[LENGTH]`. If
  quality is comparable, the simpler dictionary path may be preferred.
- **Article-body extraction.** `wikipedia2text` outputs section
  hierarchies, infobox content, and reference cruft. The protocol assumes
  the lead paragraph is enough, but the lead may be too thin or, for some
  articles, parsed oddly. Inspect.
- **Section flag interaction.** `-s` for summary may help; `-T` for a
  named section may help; experiment.

Update this file with what the first run reveals. The CLAUDE.md Phase 2
section will fold in the verified rules once they exist.
