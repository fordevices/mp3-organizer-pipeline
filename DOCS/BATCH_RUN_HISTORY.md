# Batch Run History

Record of every full batch run against the Input/ library.
Update this after each run with the summary.json stats and any observations.

---

## Run 1 — 2026-04-04

| Field | Value |
|---|---|
| Run ID | `2026-04-04_17-34-04` |
| Started | 2026-04-04 17:34 |
| Finished | 2026-04-04 23:33 |
| Duration | 5h 59m (21,550s) |
| Source | `Input/` (full library) |
| Stages | 1, 2 (skipped), 3, 4 |
| DB zeroed before run | Yes |

### Results

| Metric | Count | % of total |
|---|---|---|
| Files total | 5,550 | 100% |
| Identified + moved | 3,768 | 68% |
| No match | 1,700 | 31% |
| Already done (skipped) | 78 | 1% |
| Errors | 4 | <1% |
| Shazam calls made | 5,468 | — |

### No-match breakdown by language

| Language | No match | Total in library | Hit rate |
|---|---|---|---|
| Tamil | 1,159 | ~2,659 | ~56% |
| English | 501 | ~2,626 | ~81% |
| Hindi | 40 | ~183 | ~78% |

### Observations

- Tamil no-match rate (44%) is the biggest gap — likely older pre-2000 film music
  with low Shazam coverage. Same gap seen historically with AcoustID + MusicBrainz.
- Hindi and English hit rates are solid (78–81%).
- Stages 3 and 4 were clean — 3,768 moved, 0 errors.
- The 4 identification errors are in the `error` status in the DB.
- Stage 2 (manual review) was skipped — `--review-after` flag not used.
- Next steps: `--metadata-search` pass on the 1,700 no_match files;
  transliteration of ID3 artist tags (design decision recorded in DESIGN_DECISIONS.md).

---
