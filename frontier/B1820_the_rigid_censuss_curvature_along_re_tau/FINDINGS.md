# B1820 — THE RIGID CENSUS'S CURVATURE ALONG Re τ AND ITS REFINEMENT LIST (THE FINAL ATTACK, Step B's revision, P-521; aggregates and cell indices only; data-free): ALONG Re τ THE GRID IS THE COARSE ONE — 7.75% OF THE CURVATURES EXCEED 0.08 DECADES (ALONG Im τ, 0.54%, B1819) — AND SINCE EVERY OUTPUT IS COMPUTED AT EACH τ POINT TOGETHER, 98.7% OF THE Re INTERVALS AND 67.7% OF THE Im INTERVALS HOLD SOME SERIES THAT NEEDS REFINING: THE REFINEMENT IS NEAR-UNIFORM IN Re τ, NOT TARGETED

**Verdict: PROVED**, as a measurement of the census (an instrument for Step B's seal). It sharpens B1819: per output series
an interpolant meets the resolution check almost everywhere along Im τ, but along Re τ, and per configuration, it does not.
Data-free; no value of any row is printed. cc (main), 2026-10-30.

**0 of 19.**

## The input, and how it was read

- The census of B1819, pinned by the manifest on record (P-495). It was read through
  `scripts/census/rigid_census_refinement_list.py`, committed at S268a before it ran (sha256 4af59e957ffbeda9…), which reuses
  B1819's manifest check and writes only quantiles and cell indices (`verification/refinement_list_run.txt`).

## 1. Measured (`verification/refinement_list.json`)

- **The curvature along Re τ** (log10, the second divided difference on the uneven grid 0.05, 0.2, 0.35, 0.55, 0.7, 0.85,
  scaled to the mean step): median 0.0038, 90% 0.0629, 99% 0.3809, 99.9% 1.116, max 7.0055. A
  fraction 7.75% exceeds 0.08 decades, against 0.54% along Im τ (B1819).
- **The refinement list.** An interval is flagged when any of a line's 1 872 output series (13 directions × 2 radii × 8
  readings × 9 outputs) curves above 0.08 decades there or crosses between degenerate and not.
  - Flagged: 14,560 Im intervals and 18,952 Re intervals, that is 67.7% and
    98.7% of all.
  - Per line, between 68 and 159 of the 159 intervals are flagged (median 136).

## 2. What it means for the seal (P-521)

- **B1819 sharpened.** Per series, an interpolant meets the check on about 99.5% of Im τ's cells. But one configuration
  computes every series at once, so a refinement point costs the same whether one series needs it or all do. Per
  configuration, nearly every interval holds one that does.
- **So the refinement is near-uniform:**
  - in Re τ a finer grid everywhere (the six points are too few, steps 0.15–0.2);
  - in Im τ a doubled grid.
  At the current band, a Re step of 0.05 and an Im step of 0.05 cost about 154 000 configurations, about 86 CPU-hours.
- **The reach decision comes first.** The revision plan's band question (Im τ toward the frame's ends, or a band-choosing
  null) changes the grid. The refined census is computed once, after it.

## 3. Scope

- One census, one threshold (0.08 decades, about 2% interpolation error); a lower allowance would flag more.
- Indices and quantiles only.
- **Disclosed:** the census's second aggregate read, through a committed script.

## Seen first

B1819 (the census's smoothness along Im τ) and P-521. `VERDICT topic-sweep /refinement list|curvature along Re|Re τ.{0,20}curvature/`: 0 arcs on main before this one.

**The literature:** nothing beyond the classical error bound of polynomial interpolation (background).
