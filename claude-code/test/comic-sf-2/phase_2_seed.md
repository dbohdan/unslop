# Phase 2: SEED

Source: Wikipedia random articles. The user ran `wikipedia2text -r` 15 times
externally (Wikipedia is unreachable from this sandbox) and supplied the
results as `claude-code/test/wp-seed/`. Discard rules from
`claude-code/wikipedia-seed.md` applied.

## Triage of all 15 articles

| # | Title | Disposition | Reason |
|---|-------|-------------|--------|
| 01 | Houdelmont | discard | Ultra-stub geo (rule 7); single-sentence body, French commune pop. 363 |
| 02 | The Gravity Group | **keep** | Wooden roller coaster design firm, Cincinnati, 2002–. Named projects (The Voyage, Hades, Boardwalk Bullet, Cú Chulainn) |
| 03 | *Phragmataecia pacifica* | discard | Single-species moth stub; three sentences total. Below the ultra-stub threshold despite the binomial |
| 04 | Claude Dagens | discard | BLP (rule 1). French Catholic bishop, b. 1940, age 85. Article carries the explicit BLP banner |
| 05 | List of Punjabi tribes | discard | List (rule 3) |
| 06 | Conquer Paralysis Now | discard (tone) | Charity passes the formal rules but the topic — Sam Schmidt's spinal cord injury — is wrong for the comic register and risks tonal harm to a real living person |
| 07 | Mokro Polje | **keep** | Croatian village pop. 163, but with substantive body: Serbian Orthodox Church 1524–1537, Croatian War, Republic of Serbian Krajina, Yugoslav Partisans monument built 1952 and destroyed 1996. Geography + history, not ultra-stub |
| 08 | Forensic accounting | **keep** | Discipline. Strong concept for the Sladek-mode register |
| 09 | Kathleen Belew | discard | BLP (rule 1). American historian b. 1981, age 44 |
| 10 | *Ecliptophanes* | **keep** | Genus of beetles, family Cerambycidae, six named species. Taxonomic specificity in Lem-mode |
| 11 | Ulutaş, Mazıdağı | discard | Ultra-stub geo. Turkish village pop. 574; one sentence of body |
| 12 | Nicolae Esinencu | **keep** | Historical figure (1940–2016), Moldovan poet/screenwriter, "terrible child" reputation, friends organised his 70th birthday celebration and he didn't turn up. Color-only per the "don't use directly" rule |
| 13 | Mill Creek (River aux Vases tributary) | discard | Ultra-stub (2 sentences); Missouri stream named for mills lining its banks |
| 14 | ISR Racing | keep-borderline | Czech racing team founded 1993, multiple series. Decent concept but less rich than 02 |
| 15 | *Desiya Geetham* | keep-borderline | 1998 Tamil political drama film about kidnapping a chief minister to teach him village life. Premise is rich but I'd render the cultural specifics shallowly |

**Discard total:** 8 of 15 (53%). Below the draft expectation of 60–80% — within the wider range, on the lower end. The big BLP/ultra-stub categories accounted for 5 of 8 discards (2 BLPs + 3 ultra-stub geo).

**Survivors:** 7 (02, 07, 08, 10, 12, 14, 15).

## Selection: keep 5 of the 7 survivors

Strongest 5 by conceptual mass and genre fit:

- **08 — Forensic accounting** (the discipline)
- **07 — Mokro Polje** (the village with the destroyed Partisan monument)
- **12 — Nicolae Esinencu** (the writer who skipped his own 70th)
- **02 — The Gravity Group** (the wooden coaster firm)
- **10 — *Ecliptophanes*** (the beetle genus)

Dropped survivors: 14 (ISR Racing — racing team, less specific than the coaster firm) and 15 (*Desiya Geetham* — film with a strong premise but a cultural register I'd render shallowly in 1000–3500 words of comic SF).

## SEED for this run

- **Forensic accounting** — a branch of accounting that investigates financial misconduct and fraud; a sub-discipline of forensic science alongside DNA profiling, palynology, and questioned-document examination.
- **Mokro Polje** — a village in Šibenik-Knin County, Croatia (pop. 163). Site of a Serbian Orthodox Church of St. Luke (1524–1537, on a possibly older Catholic foundation), and of a 1952 Yugoslav-Partisans monument that was destroyed in November 1996 after the Croatian Army's Operation Storm. Serbian-Cyrillic name: Мокро Поље.
- **Nicolae Esinencu** (1940–2016) — Moldovan poet, screenwriter, and writer; alumnus of the Maxim Gorky Literature Institute in Moscow; co-wrote the screenplay for Vlad Ioviță's 1975 film *Calul, pușca și nevasta* ("The Horse, the Gun, and the Wife"). "Terrible child" reputation — friends organised his 70th birthday celebration and he didn't turn up. Color-only: must not be on stage as himself.
- **The Gravity Group** — a wooden roller-coaster design firm headquartered in Cincinnati, Ohio, founded July 2002 by former Custom Coasters International engineers. Notable projects: The Voyage (Holiday World, Santa Claus, Indiana), Hades 360, Boardwalk Bullet (Kemah Boardwalk), Wooden Warrior (Quassy Amusement Park), Ravine Flyer II, Cú Chulainn (Emerald Park).
- ***Ecliptophanes*** — a genus of long-horn beetles (family Cerambycidae, subfamily Cerambycinae, tribe Rhinotragini), described by Melzer in 1935. Six named species: *E. bucki, chacunfrancozi, laticornis, scopipes, silvai, tommyi.*

## Notes for Phase 3 (and after-run revision of `wikipedia-seed.md`)

- **"Uninteresting geography"** — confirmed as a real category. Three of fifteen draws were uninteresting-geography ultra-stubs (01, 11, 13), all caught by the existing rule 7 (ultra-stub). The user's intuition is right and the existing rule already covers it; the rule's wording could call out small populated places explicitly.
- **Mokro Polje** is the case that proves the rule should *not* be "discard all small places." The Croatian War history makes the body substantive even though the population is 163. The ultra-stub rule (~80 words of body) handles this correctly; an over-broad "discard all settlements under N inhabitants" rule would have lost it.
- **Single-species taxonomic stubs** (article 03 *Phragmataecia pacifica*) caught by rule 7. The closely-related genus article (10 *Ecliptophanes*) survives on a roughly comparable body length but lists six species — which adds material. Borderline; defensible to keep.
- **The "tone-fit" discard for article 06** (Conquer Paralysis Now) is not in the rules. Worth adding a soft rule: "if the article concerns a sensitive contemporary subject (mass casualty, individual injury or illness, contemporary atrocity, named victim of crime), discard regardless of whether it formally passes." This is judgement-based and should be acknowledged as such.
- **Esinencu is a strong test of the historical-figure rule.** The "terrible child" detail is a perfect color element — a culture's relationship to its difficult writer — without requiring him on stage.
