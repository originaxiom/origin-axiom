# B1819 — THE RIGID CENSUS'S SMOOTHNESS IN τ (THE FINAL ATTACK, Step B's revision, P-521; aggregates only; data-free): ON B1726'S GRID THE FRAME'S OUTPUTS ARE SMOOTH IN Im τ ALMOST EVERYWHERE — THE MEDIAN CURVATURE IS 0.0008 DECADES PER STEP AND 99% OF IT BELOW 0.041 — SO A CERTIFIED INTERPOLANT MEETS THE RESOLUTION CHECK ON ABOUT 99.5% OF CELLS; THE REST (THE ORDER-4 LINES, 0.54% OF CURVED CELLS, AND 7568 DEGENERACY CROSSINGS) NEEDS LOCAL REFINEMENT, NOT A 5× GRID

**Verdict: PROVED**, as a measurement of the census (an instrument for Step B's seal). Data-free: no row's value is
printed and nothing is compared with a measured value. cc (main), 2026-10-30.

**0 of 19.**

## The input, and how it was read

- The census is the rigid-direction census on the full menu (B1810's thirteen directions × the 266-line menu's other
  256 lines × B1726's 90-point τ grid × two radii × eight readings; 23 040 configurations, 4 792 320 rows). It is unread
  before the seal and lives in the audit room until the seal commits it. Its manifest's sha256,
  4683a000bd09dda1cbf22dae68117530fb6c3f09691528347f55177b4a9804d1, was put on record at S266 (P-495).
- The pre-seal review allows it to be read before the seal only through a committed script that outputs aggregates. That
  script is `scripts/census/rigid_census_smoothness_map.py`, committed at S267a before it ran (sha256 4f3df1d02ffa0b08…). It
  refuses to read unless every file matches the recorded manifest; it did (`verification/smoothness_map_run.txt`).

## 1. Measured (`verification/smoothness_map.json`; log10 of the six ratios and the three CKM moduli)

| difference | median | 90% | 99% | 99.9% | max |
|---|---|---|---|---|---|
| first, along Im τ (step 0.1) | 0.0559 | 0.1657 | 0.2603 | 0.4691 | 3.673 |
| first, along Re τ (steps 0.15–0.2) | 0.0098 | 0.1024 | 0.4182 | 0.8071 | 3.8741 |
| second, along Im τ | 0.0008 | 0.0049 | 0.041 | 0.4642 | 6.4575 |

- Second differences above 0.08 decades: 0.54% of 33,126,742 (`fraction_above_0.08`).
- By the line's order, the 99th percentile of the curvature is at most 0.048 except on the order-4 lines (1.7034), where
  the first generation has exact zeros (B1713).
- Degenerate entries (a ratio at or below 1e-9) number 4,903,288; an entry changes between degenerate
  and not between neighbours 5,654 times along Im τ and 1,914 along Re τ.

## 2. What it means for the seal (P-521)

- A quadratic interpolant's error is about a curvature over 8: below 0.01 decades (about 2%) wherever the second
  difference is below 0.08. That holds on about 99.5% of cells, well inside the record's 10% allowance.
- The rest needs local refinement before the seal: the order-4 lines, the 0.5% of curved cells, and every degeneracy
  crossing, where no interpolant is smooth.
- Re τ's steps are coarser, and its curvature is not measured here. It gets its own check before the interpolant is
  certified.
- **So the resolution check (S0, INPUT_COMPLETENESS row 13) is met by an interpolant plus targeted refinement, not a 5×
  grid (about 225 CPU-hours).** The refined census's own check is part of the seal's design (STEP_B's revision plan).

## 3. Scope

- One census on one grid; aggregates of differences only. The interpolant's error is estimated here, not certified:
  certification needs fresh points on a staggered grid.
- **Disclosed:** this is the census's first read since it was computed, and it is an aggregate read, through a committed
  script, as the pre-seal review requires.

## Seen first

The census and its design are THE FINAL ATTACK's (docs/THE_FINAL_ATTACK_2026-10-29.md § 5; P-495) and the pre-seal
review's (P-520, P-521). `VERDICT topic-sweep /smoothness.{0,20}(census|τ|tau)|resolution check|certified interpolant/`: 1 of 1565 arcs on main match
(this arc); 1 register row matches (P-521, QUEUED).

**The literature:** nothing beyond the classical error bound of polynomial interpolation (background); the census is
the record's own, and no outside source tabulates this frame's outputs.
