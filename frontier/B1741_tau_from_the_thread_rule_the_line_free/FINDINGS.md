# B1741 — τ FROM THE THREAD RULE, THE LINE FREE (P-347): PROVED AS SEALED FOR ITS QUESTION — WITH τ AT A THREAD'S APEX (NO CONTINUOUS NUMBER FITTED) AND THE LINE CHOSEN FROM 266, THE SIX CHARGED-FERMION RATIOS ARE REACHED AT VALUE LEVEL (χ²_six 14.93 < 16.75) AND SPECIFICALLY (0.60%); NOT PASSED UNDER THE_BAR'S LOOK CORRECTION (1.2–3.6%); THE NINE FAIL

**Verdict: PROVED as sealed for its question (P1, P2, R1, R2, R3 hold; P2c, R4–R7, P3, P4 fail; C1, C2 hold)** — a
READING: τ placed by a rule and the line chosen from a finite list, both ingredients by hand, the mixing failed. cc
(main), 2026-10-23, at the owner's recheck of τ. Sealed `acd2fec77` (sha256 7a8eeb8a) before its instruments ran; the
census outputs committed unread at `3da06f258`, the comparison's at `624f93419`, then read once. **0 of 19.**

> *2026-10-30 (S276, P-546; found by Step B's fifth pre-seal review): verification/compare.py's constant J_PDG =
> 3.08 × 10⁻⁵ (+0.15 −0.13), labelled the 2024 edition, is the PDG 2022 global fit's value; the PDG 2024 CKM review's
> § 12.3 reads J = 3.12^{+0.13}_{−0.12} × 10⁻⁵. This arc's grades did not use J; its verdict stands.*

## 1. The result

75 distinct apex points of B1720's 121 thread classes (Im τ = Lagrange/2) × all 266 lines of order 1–12 = 19 950
points, 39 900 rows; B1726's frame, ∂R, the readings and menus; main's measure and calibration and P-341's precision
cells; 20 fresh seeds (1741–1760).

| cell | prediction | prior | result |
|---|---|---|---|
| **P1, precision** | χ²_six (seat's menu) below 16.75 | 40% | **HOLDS: 14.93** |
| **P2, precision specific** | ≤ 1% of random hierarchies reach as low | 20% | **HOLDS: 0.60%** (worst seed 0.83%) |
| P2c | the same under the covariant menu | 12% | fails: 2.26% |
| R1 | the six within a factor 2 (seat) | 85% | holds: 1.289 |
| R2, R3 | coarse specificity, seat and covariant | 45%, 30% | hold: 0.22%, 0.87% |
| R4 | the factor free | 30% | fails: 1.39% |
| R5 | the nine (seat) | 8% | fails: 1.30% |
| R6, R7 | J at the best nine-row; D at the best six-row | 5%, 10% | fail (D = 11.05, 4.3σ) |
| P3, P4 | χ²_nine below 21.67 (seat; the Standard Model's reading) | 1%, 1% | fail: 204; 1 410 |
| C1, C2 | the instrument and the χ² code | 95%, 99% | hold: 0.0 and 3.3 × 10⁻¹⁰; 3.0946 |

**The best six-row** (all three menus): the apex 3.4 + 2.993i of the thread classes L⁵R²LR and L²R⁵LR, the line
(2/5, 9/10), L_max, the Standard Model's reading (S̃, S, S), c = 3. Model over measured 1.29, 1.12, 1.22, 1.24, 1.15,
1.12 (pulls 2.44, 0.55, 1.49, 1.78, 1.39, 1.16); D 11.05; ∣V_us∣ 0.99, ∣V_cb∣ 0.996, ∣V_ub∣ 0.053, ∣V_ud∣ 0.12.

**C1 (ii), disclosed:** main first misread the T-covariance control as 3.25 from a display cut at 80 characters; it is
3.25 × 10⁻¹⁰. A labelled check (`verification/c1_diagnosis.py`) confirmed B1724's law at that apex (3.3 × 10⁻¹⁰)
and the frame's period 1 in b (1.4 × 10⁻¹¹) before the comparison ran.

## 2. What it means (the reading written before the run, applied)

- **P1 and P2 hold:** the six reached at value level with τ placed by a rule (a thread's apex) and the line chosen from
  266, priced by the calibration — no continuous number fitted. Against B1735 (τ fitted on a grid, χ² 3.09) the price of
  placing τ by the rule is χ² 3.09 → 14.93: the apex height 2.993 sits just below the fitted optimum (≈ 3.05), and every
  ratio comes out 12–29% high.
- **THE_BAR (labelled, after the read):** Bonferroni over the arc's looks — P2 × 2 (the two precision looks) = 1.2%, × 6
  (every specificity look) = 3.6%; R2 × 6 = 1.3%. **Not PASSED** at the 0.01 gate. A reading, sharper than B1734's.
- **The limits:** both ingredients by hand (the factor 3, P-294; the reading, P-295); the line from a finite list; the
  mixing fails as B1739 predicts (∣V_ud∣ 0.12 under the Standard Model's reading); D 4.3σ off.

## 3. After the read (labelled; `verification/posthoc_read.py`)

- **The line is B1735's own.** In the census frame (Re τ 0.4, by B1724's law b → b + 3α) the line (2/5, 9/10) is
  (2/5, 1/10), B1726's line 149, where B1735's fitted minimum sits (0.35 + 3.05i). The rule-placed point is the same line
  at the apex height.
- **The line is not one of the thread's own** (B1733's Smith rule: not fixed by A up to sign). The doubled thread A²
  fixes it, **but vacuously**: for this class A² ≡ −I mod 10, so A² fixes every line of order 5 and 10 (12 of 12, 36 of
  36). [Corrected 2026-10-23, before the push: main first wrote this as "a candidate line rule"; sizing P-349's sealed
  test showed the criterion cannot fail on this class (the E2/MB12 vacuity class).] No line rule from the thread is on
  record; the line stays chosen from 266, priced by the calibration.
- **For the seats (P-348, the third opinion):** re-run compare.py on census.jsonl; recompute the best row on your own
  instrument; check the 75 apex points and the line count; apply THE_BAR's correction your way.

## 4. Main's hostile referee (before the push; a read-only subagent, scratch in `audit/referee_b1741/`)

- **Reproduced:** χ²_six 14.9324 at the best row and the per-seed fractions (0.00525, 0.0035 for seeds 1741, 1742) with
  its own direct loop; a fresh `compute()` matches the stored row to 1.9 × 10⁻⁹; the T-covariance at the apex 3.2 × 10⁻¹⁰;
  all eleven hashes. The data's σ does not favour the data: a uniform 0.10 gives χ² 19.61 and 0.40%, 0.25%.
- **The A² reading is vacuous** (Cayley–Hamilton: tr A = 30, so A² = 30A − I ≡ −I mod 10), as corrected in §3.
- **Post-selection, the weakness that matters most:** the tested row is B1735's fitted line at the nearest apex height,
  and the preregistration disclosed a by-eye χ² of 10–20 there; C1 (ii) names that very point. So P1 was close to
  foreknown, and P2 is a p conditional on a hypothesis chosen with the data in view. The specificity also leans on c = 3,
  chosen from the data: with c free over {1, …, 5} the fraction rises to about 1.0–1.1% (two seeds); with c = 1 alone χ²
  is 171. **The referee's estimate of the true p: about 1–7%, with 0.60% a lower bound.**
- **The looks:** six sealed specificity looks, eleven fractions computed (P2 × 11 = 6.6%); the third test of the apex
  rule (B1720, B1734, B1741; × 3 = 1.8%).
- **The rows:** 66 distinct (Re τ mod 1, Im τ) and 99 494 distinct model vectors of 159 600; a minimum-based calibration
  is unaffected, but "39 900 rows" overstates the looks.
- **A correction to the preregistration's wording:** its seeds 1741–1760 are not fresh — they overlap B1740's (19 of
  20), B1734's (13), B1732's (11) and B1726's (5), so the calibrations across these arcs are correlated (no leak). B1740's
  preregistration carries the same slip.
- **The referee's verdict:** the sealed result stands as stated; "not PASSED under THE_BAR" is right.

## Dated note (2026-10-24, S217; B1749, the replication on fresh apexes)

- **Replicated in a narrower sense.** B1749 ran this arc's instrument and measure unchanged on 125 fresh apexes (words of
  length 12) with fresh seeds: the six's specificity holds again (0.02% of random hierarchies as good; χ²_six 3.57). Main's
  hostile referee showed the specific rows form one strip, Im τ 2.96–3.11, on the order-10 lines (2/5, b), which any ~100
  points in the band find (P-350). So the specificity is the frame's, with c = 3 and the seat's reading; that the thread
  rule *places* τ is not shown, and this FINDINGS' phrase "with τ placed by a rule" should be read so.

## Dated note (2026-10-24, S216; W145, the SM seat's third opinion, row 1356)

- **The best six-row is a mirror pair.** The χ²_six minimum is a tie: line 150 = (2/5, 3/10) at Re τ 3.6 and line 153 =
  (2/5, 9/10) at Re τ 3.4, at the same apex height, symmetric about Re τ = 3.5 — χ²_six 14.93237624 at both, line 150
  lower by 2.9 × 10⁻¹⁰ (recomputed on main from census.jsonl). § 1 names line 153 because `best_six` ranks by the largest
  factor; by χ² alone the minimum sits on line 150, which is why W145's A2 "failed as worded". No cell changes. W145
  reproduces B1741 in full on main's code, a second code and the seat's own instrument (no number of main's wrong);
  P-348 DONE.

## Seen first

From the preregistration: `VERDICT topic-sweep /apex rule|thread.s apex|line free|every line at (the|each) apex|Lagrange/2|tau from the thread|τ from the thread|thread fixes the point/ (full text): 4 of 1512 arcs on main match`;
bearing on it B1720, B1722, B1733, B1734, B1735 and P-347. **Literature:** as the preregistration.

## Disclosed

- Everything in the preregistration's Disclosed (B1735's χ² map and main's by-eye estimate of roughly 10–20 at this
  point, behind P1's prior).
- The C1 misreading above. B1740's census was paused at 3 608 points to run this census first; it resumes after.
- §§2's THE_BAR line and §3 were written after the read.

## Files

- `PREREGISTRATION.md`, `ARTIFACT_HASHES.txt`.
- `verification/census.py` → `census.jsonl`, `control.json`, `census_run.txt`.
- `verification/compare.py` → `comparison.json`, `compare_run.txt`.
- Post hoc (labelled): `verification/c1_diagnosis.py` → `c1_diagnosis.json`, `c1_diagnosis_run.txt`; `verification/posthoc_read.py`
  → `posthoc_read_run.txt`.
- The lock: `tests/test_b1741_tau_from_the_thread_rule_the_line_free.py`.

## Dated note (2026-10-28, S238; the web seat's THE EXACT END, reproduced on main)

This arc's L_max is the small-cut norm 2πL + c_s evaluated at L = L_max(Im τ) (B1726's compute()), not the maximal horoball's exact norm. At L_max the exact twisted norms lie 35–38% below it, and with them the six fail near the four families' rows (RETRACTIONS; P-421). Nothing else in this arc changes.

> *Noted 2026-10-29 (P-436): this arc's preregistration did not fill the input-completeness ledger (docs/INPUT_COMPLETENESS_LEDGER.md, 12 rows). Sealed preregistrations are not edited; the gap is recorded here. From B1811 on the ledger is filled (B1811, B1814) and a lock enforces it for new seals (tests/test_input_completeness_in_every_new_seal.py). The six's inputs are carried by the scoreboard's rows (harvest 1478, 1479).*
