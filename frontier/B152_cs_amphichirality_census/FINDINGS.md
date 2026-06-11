# B152 — Chern–Simons as a parity order parameter: the census test

**Date:** 2026-06-11. **Status:** NUMERICAL / census — a verified data extension of B128 (CS as a
parity/chirality order parameter) and B136 (general amphichirality). Standalone low-dimensional
topology; **no Origin-core claim**; proven core P1–P16 untouched. Nothing promotes to `../../CLAIMS.md`.
Script: `probe.py`. Test: `tests/test_b152_cs_amphichirality_census.py`. Ledger: V141.

## The question

B128 established (and K011/B136 generalize) that the Chern–Simons invariant behaves as a one-sided
parity order parameter for these bundles. B128 validated the **criterion** on a handful of control
manifolds but never ran a census. This stage supplies the missing data: a scan of SnapPy's
`OrientableCuspedCensus[:240]` testing the one-sided law

> **amphichiral ⟹ CS is 2-torsion** (i.e. `CS mod ½ ∈ {0, ¼}`),

and counting how the converse fails.

## Method (with the documented guard)

Amphichirality is read from `M.symmetry_group().is_amphicheiral()` **gated on `is_full_group()`**
(REPRODUCIBILITY: naive `is_isometric_to(mirror)` is orientation-blind and false-positives on
known-chiral census knots). CS is reduced modulo ½ and tested for 2-torsion by circular proximity to
`{0, ¼}` (a tolerance of `1e-6`). The circular distance matters: a genuinely-zero CS can read as a tiny
*negative* float that wraps to `≈0.4999` under `%0.5` — the proximity test must treat `0` and `½` as the
same point (a bug caught and fixed in-session; see the probe).

## Result (reproduced in-session)

Over the first 240 census manifolds (all with a full symmetry group — `0` indeterminate):

- **7 amphichiral:** `m003, m004, m135, m136, m203, m206, m207`.
- **0 necessity violations:** every amphichiral manifold has 2-torsion CS — the law
  `amphichiral ⟹ CS ∈ {0,¼} mod ½` holds with no exception in the census.
- **exactly 1 converse counterexample:** `m208` is **chiral** (`is_full_group=True`,
  `is_amphicheiral=False`) yet has `CS ≈ 0` — so `CS` 2-torsion does **not** imply amphichirality.
  (No chiral manifold in the census has `CS ≈ ¼`; `m208`, at `CS=0`, is the unique converse failure.)
- **Calibration (P9):** `m004` (figure-eight) `CS=0`, amphichiral; `m003` (sister) `CS=¼`, amphichiral.

## Reading

The data confirm CS-2-torsion as a **necessary but not sufficient** condition for amphichirality — the
correct one-sided behaviour of an order parameter, with `m208` the explicit witness that the converse
fails. This is exactly what B128's "CS as a parity order parameter" predicts at the level of a real
census: amphichirality forces the order parameter into its 2-torsion values, but a chiral manifold may
land there too. No physics; a fact about the census. The figure-eight (`m004`, `CS=0`) and its chiral-CS
twin sit on opposite sides of the converse, with `m208` the third corner (chiral but `CS=0`).

## Reproduce

```bash
python frontier/B152_cs_amphichirality_census/probe.py     # writes census.json
python -m pytest tests/test_b152_cs_amphichirality_census.py -q
```
