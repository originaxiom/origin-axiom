# B1735 — THE PRECISION BAR ON THE TWO-INGREDIENT CENSUSES (post hoc, labelled): WITH τ FITTED ON B1726'S GRID THE FRAME REACHES THE VALUES OF THE SIX (χ² = 3.09, BELOW THE BAR 16.75; 0.03% OF RANDOM HIERARCHIES AS GOOD), NOT THE NINE (χ² = 109); THE THREAD RULE DOES NOT (χ² = 42); W138 VERIFIED ON MAIN

**Verdict: PROVED** (computations on committed censuses; post hoc, labelled; no new data look beyond those named).
cc (main), 2026-10-23. **A READING at value level with τ fitted and both ingredients put in by hand; not a derivation.
The seats' third opinion is owed (P-342). 0 of 19.**

## 0. Why

- **The web seat's PRECISION_BAR** (`relays/chat1_2026-10-23_rigid_tau/PRECISION_BAR.md`, 51b05f7c7; HARVEST_LEDGER
  row 1330). Main's coarse measure (the worst factor and its random-as-good fraction) asks whether a pattern of
  hierarchies is non-generic. It does not ask whether the values are right. B1698's H3 and B1720's T3 carried a χ² cell
  for that reason (every one failed); B1726 and B1734 carried none. The web seat committed to χ² cells at main's own
  definition: χ²_six below 16.75 and χ²_nine below 21.67.
- **W138, the SM seat's third opinion on B1726** (P-304; 90a888631; row 1329). Its labelled A3: with every covariant
  reading and the factor free, 3.37% of random hierarchies match the six.
- This arc computes both on main, on the committed censuses of B1726 (23 940 points, 47 880 rows) and B1734 (190
  points, 380 rows). Nothing is fitted beyond what each arc's own rows contain; no new point is computed except part
  C's single recomputation of a stored row.

## Seen first

`VERDICT topic-sweep /chi.?2|χ²|chi.?square|precision bar|value.level|within the (10%|allowance)/ (full text): 38 of 1507 arcs on main match (NEGATIVE 15, OPEN 1, PROVED 21, no verdict file 1)`.

Every earlier χ² cell at this definition failed: B1696 (minimum 317), B1698 (162), B1712 (108), B1713 (162), B1720 (79), B1723 (3 891);
  B1718 found the running allowance keeps it far above 16.75. B1726 and B1734 had none.

**Literature:** none beyond the pinned data files (Huang–Zhou 2021 at M_Z; PDG) and B1720's χ² definition; a χ² with a
fixed relative allowance is standard.

## Disclosed

- The χ² numbers in §2 were first computed in the audit room (`audit/verify_w138_precision`) on these
  censuses and read before this file was written. The calibration in §2 was written after the minimum (3.09) was seen
  and run once. The instruments here are those runs' code with only their docstrings and root lookup changed.
- §§1–3 are post hoc: no arc sealed these cells before its census was computed.

## 1. W138 on main (`verification/check.py`, part A)

- **W138's labelled A3 reproduced on main's own code:** with every covariant reading and the factor free, the six
  under B1726's 20 seeds are matched by **3.365%** of random hierarchies (every seed 2.9–3.9%; W138: 3.37%), best six
  **1.2016** (W138: 1.2016458). So under the most permissive menu the coarse specificity does not survive, as W138 says.
- The same menu on B1734's census: **2.22%**, so B1734's six are not specific under it either.
- With W138's A1, A2, B1–B3 and C1–C4 (row 1329), B1726 is reproduced on two independent instruments. **P-304 DONE.**

## 2. The precision bar on the two censuses (`verification/calib_chi2.py`, part B)

χ²_six at B1720 `compare.py`'s definition: Σ (ln model − ln measured)²/σ², σ² = (the ratio's relative error from the
pinned Huang–Zhou 2021 file)² + 0.10². The minimum over each arc's rows and menu; for each of the arc's own 20 seeds,
the fraction of B1695's random six-targets whose own minimum over the same rows and menu is at least as good.

| census | menu | χ²_six min (bar 16.75) | random as good: mean (worst seed) |
|---|---|---|---|
| **B1726** (τ on a grid) | **seat** | **3.09** | **0.03%** (0.10%) |
| B1726 | covariant | 3.09 | 0.10% (0.20%) |
| B1726 | factor free | 2.66 | 0.25% (0.40%) |
| B1726 | covariant, factor free | 2.66 | 0.96% (1.35%) |
| B1734 (the thread rule) | seat | 42.3 | 0.29% (0.40%) |
| B1734 | covariant | 36.9 | 0.64% (0.80%) |
| B1734 | factor free | 39.3 | 1.02% (1.47%) |
| B1734 | covariant, factor free | 31.3 | 1.88% (2.38%) |

χ²_nine (the six and ∣V_us∣, ∣V_cb∣, ∣V_ub∣, the CKM's σ from the pinned PDG file with 0.10 in quadrature; the seat's
menu): **109** on B1726 and **441** on B1734, against the bar 21.67. **Both fail.**

## 3. The row (`verification/control.py`, part C)

B1726's χ²-best row under the seat's menu, recomputed from scratch through B1726's own `compute()`, equals the stored
row exactly (largest ∣Δ log∣ 0.0):

- **the point:** the order-10 line (2/5, 1/10) (index 149 of B1713's 266), τ = 0.35 + 3.05i, L_max, up S̃ with down
  and leptons S, c = 3;
- **model over measured:** m_c/m_t 1.069, m_u/m_t 0.771, m_s/m_b 1.093, m_d/m_b 1.013, m_μ/m_τ 1.031, m_e/m_τ 0.939;
- **pulls:** 0.64, −1.32, 0.67, 0.10, 0.31, −0.63 (σ with the 10% allowance); **χ²_six = 3.0946**;
- **D = (y_μ y_d)/(y_s y_e) = 10.76**, within 1.7σ of P-094's 10.58 ± 0.11 (not an independent check: D is a ratio of the
  six);
- **the CKM at the same row:** ∣V_us∣, ∣V_cb∣, ∣V_ub∣ at 4.4, 23.8 and 10.6 times the data; J = 2.5 × 10⁻⁴ (eight times
  PDG's). The mixing is not reached.
- It is not B1726's coarse-best row (1.2016 at 0.55 + 3.05i on (2/5, 1/2)): the χ² weights each ratio by its error.

## 4. What it means

- **The first row on main below the bar.** Every earlier χ² cell failed by a factor 5 or more (79 at best, B1720,
  without the two ingredients). The difference is the two ingredients: B1712 and B1713 scanned comparable grids with
  ∂R and no factor (108, 162).
- **On B1726's grid, with τ fitted, the frame with the two ingredients reaches the values of the six,** not only
  their pattern: every ratio within its error and the 10% allowance (the largest pull 1.3σ, m_u/m_t), and only 0.03%
  of random hierarchies reach as low a χ² over the same 47 880 rows and menu. The calibration counts the fitting of τ:
  each random target gets the same grid. Under the most permissive menu (every covariant reading, the factor free) it
  is at the bar (0.96%, worst seed 1.35%).
- **The limits:**
  - **post hoc:** no sealed arc carried this cell; the calibration was written after the minimum was seen;
  - **τ is fitted** (two continuous numbers, on a grid of step 0.15 × 0.1), and the line (order 10) is chosen from 266;
  - **both ingredients are by hand:** the lepton factor 3 (P-294) and the reading rule (P-295);
  - **the nine fail at value level** (χ² 109): the CKM at this row is 4–24 times too large;
  - **the thread rule fails the bar** (B1734, χ² 42): no rule on record places τ where the six are reached.
- **So the count:** the six charged-fermion ratios are matched at value level by two continuous numbers (τ) plus
  discrete choices and two hand-put ingredients. That is a reading of how many numbers the frame needs for the six (at
  most two continuous), conditional on the ingredients, not a derivation of any. The step that would make it one is a
  principle that places τ near 0.35 + 3.05i on the line (2/5, 1/10) — or the web seat's sealed RIGID_TAU_HOLOMORPHIC,
  which carries these cells with τ placed by rules (in flight).
- **For the seats (P-342):** re-run calib_chi2.py on the committed censuses; recompute the row on your own instrument;
  say whether 3.09 and 0.03% stand.

## Files

- `verification/check.py` → `check.json`, `check_run.txt` (part A; W138's labelled menu and the χ² minima).
- `verification/calib_chi2.py` → `calib_chi2.json`, `calib_chi2_run.txt` (part B).
- `verification/control.py` → `control.json`, `control_run.txt` (part C).
- The lock: `tests/test_b1735_the_precision_bar_on_the_two_ingredient_censuses.py`.
