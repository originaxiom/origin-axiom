# B1629 — DOES THE PRINCIPLE REACH THE WEAVE'S CUSP? No: the tick LR is the unique lowest closed geodesic of the weave (√5/2), the clock's word stays low, and the weave's uniform measure spends a fraction (k+1)/2^k of its time in runs of length ≥ k — no atom at the cusp; so the unit of end data a chiral three needs there (W45, W46) is not dynamical

**Verdict: NEGATIVE as sealed** (C3 and C4 hold. C1 fails on a specification slip. C2 fails on an instrument defect,
repaired post seal and disclosed, §3). cc (main), 2026-10-09. Sealed `0ec9e2673` before the run. No data read; the
owner's "go" to the outline's 2b. **0 of 19.**

## 0. Seen first

As sealed: `VERDICT topic-sweep /geodesic height|Markov spectrum|Lagrange spectrum|cusp excursion|FK10|end data|equidistribut/: 3 of 1400 arcs on main match (PROVED 3)`
— B482 (the det −1 Markov spectrum below 3 is {√5, 2√2}), B1625, B1627; the SM seat's W45, W46 and §41.4.
**Literature:** the continued-fraction coding of geodesics (Series); the Markov and Lagrange spectra; equidistribution
of closed geodesics (Bowen; Sarnak; Duke).

## 1. The sealed run (`cusp_reach.py`, unchanged; kept in `verification/sealed_run/`)

| | sealed prediction | prior | result as sealed |
|---|---|---|---|
| **C1** | the clock's word read as moves: longest runs 2 (L) and 1 (R) at every prefix | 97% | **FAILS** — 3 and 1: prefixes were read *cyclically*, and the wrap joins an end "aa" to the starting "a". The linear runs are 2 and 1 (P3) |
| **C2** | LR tops at √5/2, the lowest thread; the rule's words below 2; L^k R climbing with k | 90% | **FAILS on L^k R** (its tops *fell*, 1.118 → 0.577). An instrument defect: the height was taken only at the cusp's representative at ∞, which long R-runs climb, while long L-runs climb the same cusp seen from 0. "The lowest" was not computed (the code took a maximum) |
| **C3** | under the uniform measure the fraction topping above Y falls with Y at every n | 90% | **HOLDS** as sealed. But the observable is a thread's highest point, and that fraction *rises* with n (long words have long runs), so it does not measure an atom. P4 does |
| **C4** | L has trace 2, threads ≥ 3, LR has 3 | 99% | **HOLDS** |

## 2. The repaired run (`post_seal_cusp.py`, written after the sealed run; disclosed)

The top is taken at both cusp representatives, ∞ and 0 (related by S), over the word's rotations:
**√(tr² − 4) / (2 min(|b|, |c|))**.

| | result |
|---|---|
| **P2** (the tick and the threads) | among all 2536 primitive threads of length ≤ 14, **the tick LR is the unique lowest**, top **√5/2 = 1.1180**; the second lowest is **√2**. These are B482's Markov values √5 and 2√2, a control the repaired measure reproduces. L^k R climbs as √(k² + 4k)/2 (6.93 = 4√3 at k = 12), exactly, by the independent check of B1631. The highest thread reaches 7.43 |
| **P3** (the clock's word, read as moves) | linear longest runs 2 and 1; cyclic 3 and 1; its prefix words top at **2.29** (L³R's height) |
| **P4** (time near the cusp, the weave's uniform measure) | the fraction of letters lying in a run of length ≥ k is **(k + 1)/2^k** (0.75, 0.5, 0.3125, … 0.035 at k = 8), the same at every n = 10 … 18: geometric decay with depth, no atom |

## 3. What it says

- **Nothing the principle forces visits the weave's cusp.**
  - The tick, σ² = LR, is the lowest closed geodesic of the weave.
  - The clock's word, read as moves, stays below height 2.3.
- **The weave as a whole reaches the cusp, but with vanishing weight.** Its threads go arbitrarily high, and the share of
  their time spent deep in the cusp decays geometrically.
- **The unit of end data that the SM seat's W45 and W46 need for a chiral three is therefore not dynamical.** If it is
  forced at all, it is forced as a boundary datum: a physical end mechanism at the cusp (the audit lane's open end duty),
  or a postulate (which the owner declined).
- FK10 stays open, sharpened on GENESIS v1.38. The 13 and 0 of 19 are unchanged.

## 4. Disclosed

- **The two failures as sealed are slips, not surprises.** C1's cyclic wrap and C2's one-sided height are both mine, and
  the sealed run is kept. The repair changes the measurement, not the question.
- The clock's word read letter for letter as moves is a reading (as sealed).
- P4's run-length proxy for time near the cusp uses the continued-fraction coding. The exact fraction of hyperbolic
  length above a height was not computed.

## 5. Files

`verification/cusp_reach.py` (sealed, unchanged), `cusp_reach.json`, `sealed_run/`; `post_seal_cusp.py` and its outputs;
`adoption/amend.py` (GENESIS v1.37 → v1.38). Kill-graph entry B1629. Test: `tests/test_b1629_does_the_principle_reach_the_cusp.py`.

## 6. Independently verified (B1631, 2026-10-09)

A verifier agent recomputed every claim without main's code, by two height methods: the continued-fraction value at 40
digits, and the minimum of the quadratic form det(v, Mv) over integer vectors. A third method, tracing the axis
through the fundamental domain, agreed. Among all 2536 threads (the standard necklace counts), the tick LR is the unique
lowest (√5/2), then LLRR (√2), then √221/10, accumulating at 3/2. L^k R has height √(k² + 4k)/2 exactly. The fraction
(k+1)/2^k holds to 2.3 × 10⁻⁵ at n = 18, with the analytic reason that runs are geometric. No discrepancy.

