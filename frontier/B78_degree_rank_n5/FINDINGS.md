# B78 (Phase 1b) — the n=5 degree=rank test: an honest method-limit

**Date:** 2026-06-05. **Status:** the finder is high-precision-numerical (validated n=3,4); the n=5
result is an honest **method-limit** (no confirmation, no refutation). Standalone low-dim topology; **no
Origin-core claim**; proven core P1–P16 untouched. Script: `probe.py`. Test:
`tests/test_b78_degree_rank_n5.py`.

## The test

degree=rank (B73/V54), refined by B77/V60 to `[A,B] = (−1)ⁿ⁻¹ μⁿ` on the principal Dehn-filling
component, rests on **two points** (n=3, n=4). The decisive question: does **n=5** give `M⁵=L` with
`c=+1` (`(−1)⁵⁻¹`)? Two points is a guess; three is a pattern.

## What was built and validated

An **n-generic figure-eight Dehn-filling rep finder** (the `A²B,AB` convention, so `μ=A⁻¹t` is the
genuine meridian): `A=diag(spec)`, `B` solved from the bundle condition `(A²B,AB)~(A,B)`, monodromy `t`
via the `2n²×n²` Kronecker null-space, irreducibility by rank, and the scalar test `[A,B]=c·μᵏ`.
**Validated:** it reproduces the known sign law —
- n=3 `{1,i,−i}` → `M³=L`, `c=+1` (scalar-dev ~5e-14);
- n=4 `{1,1,ω,ω²}` → `M⁴=L`, `c=−1` (scalar-dev ~1e-8).

## The n=5 outcome (method-limit)

Across the natural SL(5) finite-order spectra — degenerate (`{1,1,1,−1,−1}`, `{i,−i,i,−i,1}`,
`{ζ₆,ω,ω²,ζ₆⁵,1}`), distinct (`Φ₈={prim 8th roots,1}`, `Φ₁₂`), and `tr=0` (`{5th roots}`,
`{1,i,−i,ω,ω²}`) — the figure-eight bundle condition is **solvable to machine precision** (best residual
~1e-15) but **every converged rep is REDUCIBLE**: ~100 converged solutions per spectrum, **0
irreducible**. `least_squares` descends into the reducible basins; the irreducible principal
Dehn-filling rep is **not numerically locatable** this way. This is the documented SL(5) rank-loss /
gauge difficulty (B61–B66) amplified to the rep-search setting.

> **The decisive n=5 third point is OPEN** — neither confirmed nor refuted. degree=rank stays
> **confirmed at n=3,4** with the `(−1)ⁿ⁻¹` sign law (B77/V60); n=5 is a flagged method-limit.

## What would close it

- The **symbolic SL(5) trace-map fixed-locus** (the B71 route at rank 5: `Fix(T_1²)` on the 24 SL(5)
  trace coordinates, then explicit realization on the Dehn-filling component) — robust but heavy.
- A **homotopy / continuation** rep-finder seeded from a known irreducible rep, or an
  irreducibility-promoting objective that avoids the reducible basins.

Honest negative banked plainly; the central law's third data point remains the key open experiment.

## Reproduce

```bash
python frontier/B78_degree_rank_n5/probe.py
python -m pytest tests/test_b78_degree_rank_n5.py -q
```
