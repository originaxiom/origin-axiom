# B75 (Path F1) — the two-parameter (m,n) thread: is degree=rank m-independent?

**Date:** 2026-06-05. **Status:** high-precision-numerical (eigenvalue test, ~1e-14); the m-axis is
solid, the even-m / rank-4-metallic corners are honest OPEN. Standalone low-dim topology; **no
Origin-core claim**; proven core P1–P16 untouched. Script: `probe.py`. Test:
`tests/test_b75_metallic_degree_rank.py`.

## Question

Two one-parameter structures in the repo had never met:
- the **metallic family** (`m`): the trace map `φ_m: a→aᵐb, b→a` (B48–B69), at a fixed rank;
- the **degree=rank tower** (`n`): on the rank-`n` **figure-eight** (`m=1`) bundle's principal
  Dehn-filling component `{tr A=tr A⁻¹=1}`, the longitude is the meridian's `n`-th power, `Mⁿ=L`
  (B73/V54: `M³=L` at `n=3`, `M⁴=L` at `n=4`).

**Does degree=rank depend on the bundle (the metallic parameter `m`), or only on the rank `n`?** I.e.
on the rank-`n` **metallic-`m`** bundle (once-punctured-torus bundle with monodromy `φ_m²`, trace
`m²+2`), is the longitude still the `n`-th power of the meridian for every `m`?

## A methodological correction (why the eigenvalue test)

B73's criterion `[A,B]=c·μᵏ` with meridian `μ=A⁻¹t` is calibrated to the figure-eight's **specific**
monodromy convention `tAt⁻¹=A²B, tBt⁻¹=AB`. On a **conjugate** convention (e.g. `φ_1²`:
`tAt⁻¹=ABA, tBt⁻¹=AB` — the *same* mapping class / *same* figure-eight bundle) `μ=A⁻¹t` is **not** the
geometric meridian, and the scalar test fails (verified). The robust, **convention-independent**
statement is the **eigenvalue form**: on a Dehn-filling component `[A,B]` and `t` co-diagonalize and
```
   eig([A,B]) = eig(t)ᵏ   (as multisets)   ⟺   Mᵏ = L
```
(because `eig(meridian)=eig(t)`, V46/B67, and longitude=meridianᵏ). This reproduces `M³=L` for **both**
figure-eight conventions at `n=3` (~1e-13/1e-14), so it is the correct cross-family test. B75 uses it.

## Results

| rank `n` | bundle `m` | A-spectrum | clean degree | `eig[A,B]=eig(t)ᵏ` dev |
|---|---|---|---|---|
| 3 | 1 (figure-eight) | `{1,i,−i}` | **`M³=L`** | `7.5e-15` (8 reps) |
| 3 | 3 (metallic, tr 11) | `{1,i,−i}` | **`M³=L`** | `2.7e-15` (8 reps) |
| 3 | 2 (silver) | 61-spectrum sweep | none found | — |

**The m-axis is real.** At fixed rank 3, the **odd** metallic bundles `m=1` and `m=3` give the *same*
clean `M³=L` (degree = rank = 3). So degree=rank is **not special to the figure-eight** — it persists
across the metallic family to `m=3`, a **different hyperbolic 3-manifold** (monodromy trace
`m²+2=11`). Together with the `n`-axis (`M³=L` at `n=3`, `M⁴=L` at `n=4`, both `m=1` — V47/V54), this
makes degree=rank a genuine **two-parameter `(m,n)`** phenomenon: a rank/topological invariant robust
under metallic deformation (odd `m`).

## Honest open corners

- **Even `m` (m=2, silver):** **no** clean Dehn-filling component found at `n=3` across a broad sweep
  of 61 product-1 finite-order spectra. This is **consistent with the cusp-torsion PARITY** (B69: the
  cusp `k`-set has `k ≡ m (mod 2)`) — the even-`m` bundles localize at even-order torsion, so the
  principal `{1,i,−i}`-type (order-4) spectrum is an odd-`m` phenomenon at this rank. **OPEN** (the
  even-`m` Dehn-filling spectrum was not located), **not refuted**.
- **Rank-4 metallic corner:** the `φ_m²` convention's rank-4 Dehn-filling spectra differ from B73's
  `A²B,AB` spectrum `{1,1,ω,ω²}` and were not located, so the metallic `m≠1` test at `n=4` (the
  higher-rank "always-3 vs degree=rank" discriminator) is **OPEN**. The `n`-axis discriminator is
  already covered at `m=1` (V54: `M⁴=L`).

## Honest reading

A genuine new **two-parameter** result with one axis solid and the complementary corners scoped:
degree=rank (`Mⁿ=L` on the principal Dehn-filling component) holds along the metallic `m`-axis (odd
`m=1,3` at `n=3`) and the rank `n`-axis (`n=3,4` at `m=1`), evidence it is a **rank/topological
invariant**, not a figure-eight accident. The even-`m` and rank-4-metallic corners need their
Dehn-filling spectra located (an explicit-rep search problem). Label **high-precision-numerical**.

## Reproduce

```bash
python frontier/B75_metallic_degree_rank/probe.py          # ~3 min (rep searches)
python -m pytest tests/test_b75_metallic_degree_rank.py -q
```
