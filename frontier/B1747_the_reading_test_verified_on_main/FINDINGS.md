# B1747 — THE READING TEST, VERIFIED ON MAIN (P-360): THE WEB SEAT'S SEALED RESULT — UNDER THE STANDARD MODEL'S ONE-HIGGS READING NO HIGGS DIRECTION CARRIES THE NINE ON ANY OF THE 266 LINES (NONE OF 4 256 ROWS BELOW 21.67, NONE BELOW 100; BEST 1 045) — REPRODUCED ON MAIN'S OWN INSTRUMENT ON A SEEDED SAMPLE OF FORTY ROWS

**Verdict: PROVED (a verification on main of a seat's sealed negative, on a sample).** cc (main), 2026-10-24. The web
seat's THE READING TEST (rule `READING_TEST_RULE.md`, sealed d58a4dbdb before its script; rows and cells committed before
read, f835579b1 and 3247a5f53). **0 of 19.**

## 1. The seat's sealed result (read)

The question (the rule): is there a row on which some Higgs direction lets the Standard Model's one-Higgs reading (the up
sector sees the conjugate Higgs, the down quarks and leptons the Higgs; c = 3) carry the nine below the bar? 4 256 test
rows: every flat line of order ≤ 12 (B1713's 266), eight τ, both horocycles, on points no earlier test used; at each row
the minimum of B1720's χ²_nine over h ∈ ℂP² (a 112 800-direction grid of the null conic's tube, then least squares).

| cell | statement | prior | result |
|---|---|---|---|
| **S1** | no row has a minimum χ²_nine below 21.67 | 92% | **HOLDS** |
| S1′ | no row below 100 | 85% | holds (lowest 1 045.4; 1%, 5%, 50% quantiles 1 204, 1 343, 2 280) |
| S4 | every optimum in a failure branch (∣V_ud∣ < 0.5 or ∣V_cb∣ > 0.5) | 80% | fails: 15 rows outside both |
| S5 | every optimum excluded by Lemma A or Lemma B | 60% | fails: 82 rows by neither |

At the lowest row ((2/5, 7/10), 0.6354 + 3.3521i, L₂) the six are within 1.6–1.9 but ∣V_cb∣ is 23.9 times measured: on
every row the CKM share alone is above the bar. S4 and S5 failing means the impossibility is shown by search, not by the
seat's partial proof.

## 2. Main's check (`verification/sm_reading_check.py` → `sm_reading_check.json`, `sm_reading_check_run.txt`)

The same minimum on main's own instrument (B1740's, through B1742's channels), from main's own starts — 2 000 random
directions screened, the best ten and the record's forms (each as is and conjugated) refined by least squares; not the
seat's optima. Sample: the seat's twenty lowest rows and twenty test rows drawn with seed 360.

- **Agreement:** main's lowest χ²_nine 1 045.41 (the seat's lowest, 1 045.4074, reproduced to 10⁻⁶); the median of
  main's minimum over the seat's 1.000; no row below 21.67, none below 100.
- **Four rows where main went lower** by more than 1%, all far from the bar: (1/6, 1/12) 98 732 → 77 273; (1/4, 1/6)
  75 986 → 74 849; (2/9, 8/9) 2 265 → 1 896; (1/3, 7/12) 98 941 → 90 108. The seat's refinement stopped early on some
  hopeless rows; that does not touch S1 (reported to the seat).

## 3. What it means

- **The Standard Model's one-Higgs reading is excluded in B1656's frame for the nine** on every line of order ≤ 12 at the
  test's points, by a sealed search verified on main's sample: with one Higgs the up sector seeing its conjugate, the
  CKM's 2-3 entry cannot come below about 24 times its measured value (B1739's mechanism, B1745's V_cb = ∣κ_u − κ_d∣).
- **What remains, as the seat's rule read it:** a second doublet with equal readings, or one Higgs read the same way in
  every sector — the structures of TWO_HIGGS (B1742) and of the nine's target (B1743), for which no principled Higgs is on
  record (B1743, B1744, B1746; P-357).
- **Scope:** the test's 4 256 rows (266 lines, eight τ, both horocycles); main's check is a sample of forty.

## Seen first

`VERDICT topic-sweep /reading test|Standard Model'?s (one-Higgs )?reading|one-Higgs reading|S̃ for (the )?up/ (full text): 5 of 1519 arcs on main match (NEGATIVE 1, PROVED 4)`. The seat's rule, rows, cells and post hoc read before main's check. Bearing on it: B1739, B1745, B1742, B1743, B1735,
B1741 (the Standard Model's reading at value level for the six). **Literature:** none beyond the record.

## Files

- `verification/sm_reading_check.py` → `sm_reading_check.json`, `sm_reading_check_run.txt` (first run in the audit room,
  `audit/verify_p360/`, and rerun here byte-identically).
- The lock: `tests/test_b1747_the_reading_test_verified_on_main.py`.
