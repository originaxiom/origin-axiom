# B88 (Task 2) — the SL(4) Dehn-filling census: degrees {3, 4} at rank 4

**Date:** 2026-06-05. **Status:** high-precision-numerical (the census is "over the spectra searched";
completeness needs the symbolic `Fix(T_1²)`). Standalone low-dim topology; **no Origin-core claim**;
proven core P1–P16 untouched. Script: `probe.py`. Test: `tests/test_b88_sl4_census.py`.

## The census

Over a sweep of finite-order (root-of-unity) product-1 A-spectra at `n=4`, **exactly two** clean
Dehn-filling components appear:

| A-spectrum | `tr A` | char | degree | scalar `c` |
|---|---|---|---|---|
| `{1,1,ω,ω²}` | 1 | `(z−1)²(z²+z+1)` | **`M⁴=L`** (degree 4 = rank; **principal**) | `c=−1` (root of unity) |
| `{prim 8th roots}` | 0 | `z⁴+1` | **`M³=L`** (degree 3) | rep-dependent (not a root of unity) |

So at rank 4 the Dehn-filling tower exposes **degrees 3 and 4** — consistent with the conjecture *"rank
`n` exposes degrees ~3..n"* (`n=4 → {3,4}`). The `{1,1,ω,ω²}` member is degree = rank (the principal
component, B73/V54); the `{prim 8th}` member is degree 3 (a *different* component, B73).

## Two honest clarifications (both real)

1. **The degree `k` is the invariant; the scalar `c` is not.** On the **principal** `{1,1,ω,ω²}`
   component, `det(μ)=1`, so `c⁴=det[A,B]/det(μ)⁴=1` and the observed `c=−1=(−1)ⁿ⁻¹` is a clean root of
   unity (B77/V60). On the `{prim 8th}` component, `det(μ)≠1` (the bundle-monodromy `t` normalization
   branch), so `c` is **rep-dependent** (it varied across runs) — *only the degree* `k=3` is robust.
   The clean "`c=(−1)ⁿ⁻¹`" of B77 is a **principal-component** statement.
2. **Not every irreducible figure-eight bundle rep is on a Dehn-filling component.** Some finite-order
   spectra (e.g. `{ζ₈,ζ₈⁻¹,i,−i}`, the primitive 12th-root tuple) admit **irreducible reps** but with
   **no clean `[A,B]=c·μᵏ` relation** (scalar-dev `~O(1)`) — generic bundle reps, not Dehn-filling. So
   the Dehn-filling components are a special locus, not all bundle reps.

## Honest scope

The census is **"over the spectra searched"**: no additional clean Dehn-filling component was found, but
**true completeness needs the symbolic `Fix(T_1²)`** (the B71 route at rank 4 — Task 1a/the symbolic
decomposition), not a numerical search (most SL(4) finite-order spectra admit no rep at all). The m=1
sanity baseline (the two known components) reproduces.

## Reproduce

```bash
python frontier/B88_sl4_census/probe.py
python -m pytest tests/test_b88_sl4_census.py -q
```
