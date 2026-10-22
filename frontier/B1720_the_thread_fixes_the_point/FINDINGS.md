# B1720 — THE THREAD FIXES THE POINT (the completion map's C1, P-284; the owner's directive of 2026-10-22): NEGATIVE AS SEALED, AND THE FRAME'S CLOSEST APPROACH — WITH NO CONTINUOUS NUMBER FREE, THE THREAD L⁵RLR² AT ITS APEX (Im τ = 2.993) ON THE ORDER-28 LINE IT FIXES PUTS ALL SIX RATIOS WITHIN A FACTOR 1.80, BUT 1.65% OF RANDOM HIERARCHIES FIT AS WELL (THE BAR WAS 1%)

**Verdict: NEGATIVE as sealed.** T1 holds; T2 fails narrowly (1.65% against 1%); T3 fails. K1 holds; K2, K3 and K4 fail.
The control C1 holds. cc (main), 2026-10-22. Sealed `a93ff339a` (sha256 a0d2a726) before its instruments ran. The
outputs were committed unread at `ceabd0407` and read once. A test of a structure, not a value derived. **0 of 19.**

## 1. The model and the result

**The model (no data).**
- 121 primitive positive thread classes (length 2–9, apex Im τ ≤ 4).
- τ at each class's apex, Im τ = Lagrange/2, the thread's height.
- Every flat line the class's monodromy fixes up to sign: 3 249 points.
- ∂R at B1667's canonical end in B1656's frame, both horocycles, three up readings.
- **No continuous number is free.** The calibration fits each random target with the same 19 494 rows.

| cell | prediction (prior) | result |
|---|---|---|
| **T1** | all six ratios within a factor 3 (40%) | **HOLDS — 1.80** |
| **T2, specific** | at most 1% of random hierarchies fit as well (3%) | **FAILS — 1.65%** (median 3.92; the best 1% reach 1.74) |
| **T3** | minimum χ² below 16.75 (3%) | **FAILS** — 79.4 |
| **K1** | CKM moduli within a factor 3 (50%) | **HOLDS** — 1.20 |
| **K2, specific** | at most 1% of random mixings (3%) | **FAILS** — 32.6% |
| **K3, K4** | all nine within 3 (8%); at most 1% (2%) | **FAIL** — 6.51; 39.0% |
| **C1, control** | basis covariance: T-moves ≤ 10⁻⁶, R-moves ≤ 10⁻⁵ | **HOLDS** — 5.9 × 10⁻⁸ and 1.3 × 10⁻¹⁰ |

**The best point.**
- **The thread:** L⁵RLR², with runs (5, 1, 1, 2), trace 30, discriminant 896.
- **Its apex:** τ = 3.6 + 2.993i, height √896/10, the Lagrange value √896/5 (min ∣c∣ = 5 over the class).
- **The line:** (11/28, 2/7), order 28 = ∣det(A − I)∣, fixed by A outright.
- **The rest:** the maximal horocycle, the up reading S̃.
- **Model over measured:** m_c/m_t 1.12, m_u/m_t 1.53, m_s/m_b 1.80, m_d/m_b 1.28, m_μ/m_τ 0.585, m_e/m_τ 1.58.
- The same factor comes from its three mirror and reversal partners. The next classes are L⁵R² at 3.61 and
  L⁴RLRLR at 4.08.

**The mixing.** The best is L⁴RL²R² on the line (2/19, 10/19), giving ∣V_us∣ 0.271, ∣V_cb∣ 0.0476, ∣V_ub∣ 0.00424 and
J = 2.3 × 10⁻⁵. Matches like this are generic (32.6%).

**The read-outs.**
- **The height's correlation with m₂/m₃** (L_max, reading S) is −0.62, −0.57 and −0.82 by sector. That is the frame's
  τ-free baseline (−0.63, −0.56, −0.77): the threads add nothing to the hierarchy beyond what τ alone gives.
- **Along the geodesic** (after the read, labelled, with the sealed functions; `audit/drafts/b1720_after/`): on each of
  the 10 best classes, the fit is best exactly at the apex.
  - L⁵RLR²'s points at ±ℓ/8 give 52 and 184, the apex 1.80.
  - Away from the apex Im τ falls and the hierarchy collapses. The apex is the natural point of a thread.

## 2. What it means

**Read as written before the run** (T2 fails): no thread with its fixed lines reproduces the data specifically at its
apex. The selection needs more than the thread: a measure over threads (C2, P-285), or another point on the thread.

**The closest approach in this frame, with every number fixed by the thread.**
- A factor 1.80 on all six ratios, with no continuous parameter, beats every census with τ free: 2.33 for B1698 and
  B1713, 2.37 for B1712.
- Its specificity, 1.65%, sits just above the sealed bar. That is close to B1698's 1.675%, also on lines a thread fixes.
- **This is not evidence.** About one random hierarchy in sixty is matched as well by some thread in the census.
- **It names the next question precisely.** A measure over threads (B1629's uniform measure; the action weight at c = 6)
  would have to single out L⁵RLR², or its class of high single-run threads, from the 121.
- It also confirms the frame's limits. The mixing is generic. The masses and the mixing do not meet at one point.

**What it does not do.**
- Threads longer than 9, or with apex above Im τ = 4.
- Points other than the apex, beyond the read-out.
- Other Higgs sections.
- A measure.

## 3. Seen first

As sealed: `VERDICT topic-sweep /thread frame|hierarchy is height|closed geodesic|Lagrange|apex|height of (the|a) thread|fixed lines?|thread fixes/ (full text, aliases: the lowest geodesic): 77 of 1492 arcs on main match (NEGATIVE 22, OPEN 4, PROVED 51)`. It bears on B1668, B1698, B1629, B482, B1703, B1712, B1713 and B1716, and on the web seat's thread frame. **Literature:** the Markov and Lagrange spectra; closed geodesics of the modular surface; standard.

## 4. Disclosed

- **As sealed:** the record above.
- **The covariance pre-check:** T ≤ 5.9 × 10⁻⁸ and R ≤ 1.3 × 10⁻¹⁰.
- **The redundancies:** 51 distinct heights, and mirror classes identical.
- **The Re τ = 0 family** (P-292).
- **The draft's first control** was defective and was replaced before the seal.
- **After the read:** the geodesic read-out, labelled. Its first version used the wrong up reading (S, where the best row
  uses S̃). It was corrected and re-run, and the corrected version is the one reported.

## Files

- `PREREGISTRATION.md` (sealed) and `ARTIFACT_HASHES.txt`.
- `verification/thread_geometry.py`, `the_thread_census.py` → `the_thread_census.json`, `the_thread_census_run.txt`.
- `verification/compare.py` → `comparison.json`, `compare_run.txt`.
- `verification/b1656_funcs.py`.
- The lock: `tests/test_b1720_the_thread_fixes_the_point.py`.

## Addendum 2026-10-22 (B1724): the reading S* is not SL(2, ℤ)-covariant

B1724 found that of B1660's three up readings, S and S̃ are SL(2, ℤ)-covariant in this frame, and S* is covariant exactly
under Γ⁰(2) (index 3). The classes' apexes sit at Re τ up to 3.6, so an S* row depends on which sheet each apex lies on.
- **The six-ratio result stands:** the best row (1.804) used S̃. Without the S* rows, on the same random targets, 1.475%
  of random hierarchies fit as well (1.65% as sealed), **still above the 1% bar: T2 still fails.**
- **The mixing best (1.203) was an S* row,** one sheet's value; with the covariant readings it is **1.225** (29.48% of
  random mixings as good). K2 fails either way.
