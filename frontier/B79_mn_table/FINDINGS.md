# B79 (Phase 1c) — the two-parameter (m,n) degree table

**Date:** 2026-06-05. **Status:** consolidation — the computed cells are high-precision-numerical
(prior ledger), the open cells are honest method-limits. Standalone low-dim topology; **no Origin-core
claim**; proven core P1–P16 untouched. Script: `probe.py`. Test: `tests/test_b79_mn_table.py`.

## The table

degree=rank, refined by B77/V60 to `[A,B]=(−1)ⁿ⁻¹μⁿ` on the rank-`n` metallic-`m` bundle's principal
Dehn-filling component. The table `d(m,n)` = the observed exponent:

| `d(m,n)` | n=3 | n=4 |
|---|---|---|
| **m=1** | **3** (V47/B71, exact — Falbel `W1=D2`) | **4** (V54/B73, ~1e-39) |
| **m=2** | *open* | *open* |
| **m=3** | **3** (V57/B75 — a *different* hyperbolic manifold, monodromy trace 11) | *open* |

**Every computed cell has `d=rank`.** degree=rank is a genuine two-parameter `(m,n)` rank invariant on
the reachable cells.

## The open cells (rep-search elusive)

- **`d(2,3)` (even-m, silver):** **no** clean Dehn-filling component for the `m=2` bundle at n=3 — over
  odd-order spectra (B75/V57), a broad 61-spectrum sweep (B78-era), **and** a fresh 63-spectrum
  **even-order** sweep (this stage). Consistent with the cusp-torsion parity (B69: cusp `k`-set has
  `k≡m mod 2`), but the component itself is not numerically locatable via the `φ_m²` `least_squares`
  finder.
- **`d(2,4)`, `d(3,4)` (rank-4 metallic):** the `φ_m²` n=4 Dehn-filling spectra differ from B73's
  `A²B,AB` `{1,1,ω,ω²}` and were not located (V57). (The n-axis discriminator is covered at m=1, V54.)

## Verdict

degree=rank is **confirmed as a two-parameter rank invariant on every cell the numerical rep-search can
reach** (odd `m` at n=3; `m=1` at n=3,4). The even-`m` and rank-4-metallic cells are **honest OPEN** —
the Dehn-filling reps elude `least_squares` (the same rep-search fragility that walls out SL(5) in B78,
and the degeneracy gauge-corruption in B81). Closing them needs the **symbolic trace-map fixed-locus**
(B71-style) per cell, not numerics. No cell contradicts `d=rank`.

## Reproduce

```bash
python frontier/B79_mn_table/probe.py
python -m pytest tests/test_b79_mn_table.py -q
```
