# B1968 — On a grid of 2,016 points, frame C's own channels never reach the tuned region: with any Higgs triplet, alignment under the charge rule forces m₂/m₃ above 0.45

**Verdict: OPEN.** An adversarial search found no counterexample anywhere on the grid. A search is not a proof.
Main, 2026-11-19. Data-free. Register row P-879. **0 of 19.**

## Seen first

- **Swept:** `VERDICT topic-sweep /tuned region|channels? (the frame|frame C)|reach(es)? the tuned|nearly null|non-null Higgs|dichotomy|trade-off/: 29 of 1709 arcs on main match (NEGATIVE 6, OPEN 4, PROVED 19); 9 register rows match (DONE 6, QUEUED 3)`.
- **B1966:** the trade-off's two ends are exact for every channel.
- **B1967:** with free channels a nearly null Higgs (reality 0.003) escapes, so any exclusion must come from the channels
  frame C produces (P-879 restated).
- **B1965:** the search at four points, with frame C's channels.
- **B1736:** the closed form used here.
- **The literature:** none bears on this coupling.

## What was run

- **`verification/reach.py`.** At each point, frame C's code gives each sector's channel matrix. Its quaternion
  components give B1736's channels (u, w).
  - The closed form with them reproduces the frame's coupling to 1e-16 (main's check before the run).
  - Under the charge rule an adversary searches h ∈ ℂ³ (unit, global phase fixed), with Nelder–Mead from 8 starts of
    2,000 evaluations each.
  - **A counterexample** is: smallest diagonal |V| ≥ 0.9, both m₂/m₃ in [1e-6, 1e-2], both m₁/m₂ ≤ 0.5. This is
    B1967's corrected criterion, which requires three distinct nonzero masses.
- **The grid:** the 24 points of order 5 and the 48 of order 7; columns x = 0, 0.13, 0.25 and 0.5; heights 1, 1.5, 2,
  3, 4, 6 and 10. That is 2,016 points.
- **`verification/reach_column.py`** runs reach.py's own loop for one column, with reach.py imported unchanged.
  - The single run was stopped after three rows, because at about 10 minutes a row it would have taken nearly five
    hours (kept as `reach_run_single_stopped.txt`).
  - The four columns then ran in parallel. Their only difference is the seeding of the random starts. Column 0's first
    three rows reproduce the stopped run's exactly.
- **The hashes** of both scripts were recorded before their runs (`verification/EXPECTATIONS_HASHED.md`).

## The results

- **No counterexample at any of the 2,016 points.**
- **Alignment 0.9 is reachable at 52 to 64 of the 72 points in every row,** but only with the heavy pair nearly
  together. The least max m₂/m₃ at alignment, row by row, is 0.457 to 0.476: 0.473 to 0.476 at height 1, 0.463 to
  0.464 at 1.5, 0.460 at 2, 0.457 at 3, and 0.459 from height 4 on.
- **The expectations:**
  - Q1 (no counterexample, prior 0.6) holds.
  - Q2 (if any, at height 1.5 or below) does not arise.
  - Q3 (the floor above 0.1 from height 3, prior 0.6) holds, with a floor of 0.457.
- **No single channel invariant explains the floor** (`verification/invariants.py`, at 16 cases). Each varies widely
  across the grid: |u·u|/|u|² from 0 to 1, |w|²/|u|², the channel quaternion's nullity, and the overlap of the up and
  down channel vectors.
  - The search always ends at the real-Higgs end, where B1727's floor of 1/3 holds, raised to about 0.46 by the demand
    that all three generations align.
  - The escape B1967 found needs the two sectors' channels tuned to each other near reality 0. Frame C's charges
    never produce that pairing on this grid.

## What it means for the goal

- **On this grid, no Higgs of any kind rescues frame C's mixing under the charge rule.** The choice of Higgs direction
  (A:A04) cannot give an aligned mixing with a hierarchy anywhere it was searched.
- **A proof** (P-879) would characterise the tuning condition between the up and down channels and show that frame
  C's charges cannot meet it. Together with B1966's exact ends, that would make the exclusion of the mixing a theorem
  of frame C.

## Not established

- **A proof:** the search is not exhaustive over h.
- **Points of other orders.**
- **Heights above 10,** where B1963 finds the charge-consistent mixing deranged for the frame's own Higgs.
- **Any comparison with data.**

## Files

`verification/reach.py`, `reach_column.py`, the four column runs `reach_run_<x>.txt`, the stopped single run,
`invariants.py` with its run, and `EXPECTATIONS_HASHED.md`. The lock is `verification/test_b1968_reach.py`.

0 of 19.
