# B1307 — THE HARVEST GATE: the seat branches are now counted the hour they are pushed — 494 seat-index ids on nine branches, 428 without a ledger row, 348 seat-branch relays without a relay row, two seats already past main's pins, two mirrors behind — and the sense census passes its third pre-registration on both routes and is adopted

**Date:** 2026-09-09 · **Seat:** cc (main) · **Kind:** instrument arc (MASTERPLAN v3.1 §1, §1a rule 3, §3 row B1307, §7 Phase 4 (1)) ·
**DESIGN sealed** `80899ba4…` before any computation (re-sealed `70bbdcf2…` after a wording-only scrub of vendor-named branch paths, the original seal recorded in `DESIGN.sha256`) · **Status:** **ADOPTED** — `harvest-debt` is the 32nd gate and runs `--strict` under
`review-due`; the sense census is `scripts/checks/sense_census.py` (a research instrument, not a gate) · **Price:** none (no physics claim) ·
**Credit:** the cloud seat (memo 172, the census's design; its two-sided control); cc3 (the relay-debt design the gate is modelled on, B999);
the SM-derivation, physics, codex, hostile-review, audit and consolidation seats, whose indices the gate reads as written.

## 0. What the instrument said on its first run (`verification/harvest_debt_first_run.txt`, 5.5 s)

| seat | head / pin (+commits) | index | rows | NEW unrowed | NEW rowed | BACKLOG | relays without a row | mirror |
|---|---|---|---|---|---|---|---|---|
| SM-derivation | ca850d6b / 0dffacd4 (+3) | 31 | 18 | 4 (the branch-only docs `PRIOR_ART_ASSELMEYER_MALUGA_2026-09-08`, `THE_ASSEMBLY`, `THE_DESTINATION_LEDGER`, `THE_VIEW_FROM_ABOVE`) | 4 (sm:B1281, sm:B1303, sm:B1304, sm:B1350 — changed after their rows; re-read at the next harvest) | 21 | 0 / 2 | codeberg 3 behind |
| physics (fc) | 659487bb / 659487bb (+0) | 74 | 7 | 0 | 0 | 70 | **3 / 4** — incl. `FC_TO_CC_2026-09-06_THE_LIFT_AND_THE_THIRD_ROOT.md` (its relay of R64–R72) | — |
| codex | f7a49536 / f7a49536 (+0) | 44 | 0 | 0 | 0 | 44 | 38 / 43 | — |
| cc3 (paper) | a31456d2 / a31456d2 (+0) | 87 | 0 | 0 | 0 | 87 | 176 / 184 | — |
| hostile-review | 6fc86147 / 6fc86147 (+0) | 29 | 1 | 0 | 0 | 27 | 0 / 0 | — |
| cloud | 02a885ca / 792918b7 (+3) | 155 | 17 | 2 (memos **183**, **184**) | 1 (memo 182) | 142 | 0 / 1 | codeberg 5 behind |
| cc3 (braver) | 53da05f6 (+0) | 6 | 1 | 0 | 0 | 5 | **131 / 150** (the July lane; all 131 are NAMED in main's docs — B921's manifest — and none has a row) | — |
| consolidation (qor5up) | 3851df2a (+0) | 30 | 0 | 0 | 0 | 30 | 0 / 0 | — |
| audit | 6f862099 (+0) | 38 | 25 | 0 | 0 | 2 (`EXTENSION_1`, `FINDINGS`) | 0 / 0 | — |
| **total** | | **494** | 69 | **6** | 5 | **428** | **348** | 2 |

STALE rows 0; aged past 21 days 0 (every NEW item is a day old). `gates.py review-due` now prints this table in `--strict` mode and says
`DEBT OPEN — a review cannot close with unread seat results`; Review 56 is due (20 merges since Review 55) and opens with it.

## 1. The controls (§2.3 of the DESIGN) — both sides, before adoption

- **Synthetic (`--selftest`):** the planted NEW unrowed item is reported; the harvested unchanged item is not; the planted missing index id
  is in BACKLOG; the planted stale row is flagged; 22 days fails and 20 days does not — **5/5 PASS**; the relay grammar sees every lane
  (`SM_TO_CC`, `FC_TO_CC`, `FAB5_TO_CC`, `CODEX_TO_CC`, `CLOUD_TO_CC`, `CC3_TO_CC`) and rejects non-relays. **The selftest can fail:** with
  `STALE_DAYS` perturbed to 30 it reports "ageing wrong" (the lock pins this).
- **Live (`verification/pin_override_control.txt`):** the pre-registered `pin^` control grew the SM seat's NEW sets by **nothing**, exactly as
  predicted (commit `0dffacd4` touched only ids already NEW); two stronger overrides, added because the pre-registered one is weak, behaved
  exactly as pre-stated — `pin~2` grew NEW-rowed by {sm:B1280, sm:B1282} and nothing else; `pin~3` grew NEW-unrowed by {`THE_TOWER_2026-09-08`}
  and NEW-rowed by {sm:B1302} — no other seat moved. **LIVE CONTROL: PASS.**
- **The parser fixes between the v0 run and the first run (both receipts kept):** relay-ledger names are read anywhere in a row's first
  cell (rows write `` `NAME.md` (on the seat's branch @ pin) ``); codex ids carry a letter suffix (R029A, R031A–D: index 39 → 44); a cloud row's
  "memo N" with N < 30 is the hostile-review seat's (the cloud INDEX's own scope note) — the two STALE flags of v0 were **real**: row 34 named
  memos 11 and 27, which are hostile-branch memos; its seat cell now says so and the hostile seat gains its first row.

## 2. The pre-registered expectations

| # | expectation | result |
|---|---|---|
| E1 | SM ≥ 3 ids, cloud memos 183/184 (+ relay) | **MET** — sm:B1303/B1304/B1350 (+B1281) and the four docs; memos 183, 184, memo 182's relay edit |
| E2 | BACKLOG ≥ 250 of ≈ 430 | **MET** — 428 of 494 |
| E3 | seat-branch relays without a row ≥ 100 | **MET, ×3.5** — 348; the braver branch's 131 July relays are named on main and rowed nowhere |
| E4 | `relay_debt.py`'s `RELAY_RE` misses the SM/FC/FAB5/CHAT1 lanes | **CONFIRMED and fixed** (any upper-case sender token); the widening exposed two tracked relays with no row — `CC2_TO_CC_2026-07-19_EQ_results.md` (BANKED in B702 the day it arrived; rowed now) and `docs/handoffs/RETURN_TO_CONSOLIDATION_SEAT_2026-08-14.md` (answered on the qor5up branch by thirty arcs; OPEN, ESCALATED to B1306 D) — and a second defect: `ROW_RE` required the first cell to be the bare filename, so four BANKED rows (SM ×2, cloud, chat1) were silently unparsed and the archived chat1 relay read as INVISIBLE WORK; tolerant now; relay-debt reads 51 banked / 53 open, green |
| E5 | mirror lag on the cloud and SM branches | **MET** — codeberg 5 and 3 behind origin (the seats push to origin only; main mirrors only main) |
| E6 | run time < 20 s | **MET** — 5.5 s (the whole gate suite 20.8 s) |

## 3. The sense census, third pre-registration — both routes PASS; ADOPTED by the rule fixed in the DESIGN

**Route A (self-naming exclusion, HEAD):** 13 files excluded at run time (CAMPAIGN_STATUS, HARVEST_LEDGER, HINT_LEDGER, RELAY_LEDGER, the two
generated views, six B1305 files, this arc's DESIGN); 2 588 prose files scanned: `logarithmic` **8 / 0**, `non-semisimple` **18 / 0** (FALSE
COMFORT — the negative control PASSES for the first time on main), `Chern-Simons` 60 / 27 (45 %, genuine), `character` **3 515 / 12 (0.3 %,
FALSE COMFORT)**, `modular` 880 / 56 (thin), `non-rational` 6 / 0, `resurgence` 70 / 12 (genuine); planted controls +1 / +0 / +0 PASS.
**Route B (the unmodified census at `31dd52b9`, the last pre-instrument commit):** `logarithmic` 8 / 0, `non-semisimple` 18 / 0, `Chern-Simons`
87 / 41, `character` 3 718 / 13 — two-sided PASSED, planted PASS. The instrument was sound on this corpus all along; what defeated it twice
was its own documentation, and the exclusion that removes documentation-by-name removes the contamination. **ADOPTED** as
`scripts/checks/sense_census.py` (the cloud's design credited in the docstring; `--selftest` = the three planted controls, 1.3 s; lock
`tests/test_sense_census.py`). It answers FRESH_EYES Q8/Q10's instrument need — *is the concept in the corpus, or only the word* — and changes
no verdict by itself: the standing reading is that `character` is a word the corpus uses 3 500 times and a concept it has engaged 12 times.

## 4. What this settles

The plan's §1a rule 3 has a mechanical form; a seat's push is visible on main within the day and fails a push after three weeks unread; a
review cannot close with the debt unread. The number the seats are owed is written down: **428 items and 348 relays**, most of it the
paper seat's and the cloud's, and the harvest arcs (B1306 B–D) pay it against this table. The pins are receipts. The relay-debt gate's
sender list is no longer a closed set. The census is the corpus's instrument now, and its first reading stands.

## Receipts, verification, lock

`verification/`: `harvest_debt_first_run.{txt,json}`, `harvest_debt_first_run_v0_before_parser_fixes.{txt,json}`, `pin_override_control.txt`,
`sense_census_third.py` + `sense_census_routeA.{txt,json}`, `sense_census_routeB.txt`, `already_banked_at_seal.txt`. Locks:
`tests/test_harvest_debt_gate.py`, `tests/test_sense_census.py`, `tests/test_b1307_the_harvest_gate.py`; `tests/test_relay_debt_gate.py` extended.
Gate: `harvest-debt` in `scripts/gates/gates.py` (32 gates); `review-due` prints the strict report. Register: PRACTICES.md (GATED). Pins:
`docs/HARVEST_LEDGER.md` `## Pins`.
