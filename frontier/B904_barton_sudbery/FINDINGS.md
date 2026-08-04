# B904 — THE BARTON–SUDBERY CAPSTONE: the build IS M(𝕆,ℂ) by explicit exact isomorphism

**Date:** 2026-08-05 · **Seat:** cc (banking) · **Status:** exact end-to-end; every convention derived or Jacobi-fitted, never assumed

## What was owed (B880's priced gap)

B880 established the module-level magic-square signature (three pairwise-inequivalent
so(8) sectors, each an 8-pair). B882 supplied the bibliography. The owed capstone: an
**explicit structure-constants isomorphism** between the build and a concretely
constructed Barton–Sudbery algebra. Since the build is the split form (its measured
charges have real ad-spectra — B898), the right BS cell is **L(𝕆_split, ℂ′_split)**
over ℚ: Zorn vector-matrix octonions, split binarions.

## Stage 1 — the triality algebra (exact)

Split octonions on the Zorn basis; the norm's so(N) has dim 28; the triality algebra
tri(𝕆) = {(A,B,C) : A(xy) = B(x)y + xC(y)} solved as an exact nullspace: **dim 28**,
with the projection to the first component invertible (used later for the dual maps).
tri(ℂ′) = {(s_B+s_C, s_B, s_C)}: dim 2. Predicted tiling 28+2+16·3 = 78 ✓.

## Stage 2 — every product DERIVED, not chosen

- The action pattern follows from the identity: T = (A,B,C) acts on V₁ by B, V₂ by C,
  V₃ by A.
- The cross products were then derived by exact equivariance over all 28 triality
  triples × 64 basis pairs (multiplicity-one Hom): **(1,2)→3: x·y; (2,3)→1: y·x̄;
  (3,1)→2: ȳ·x** — each the unique survivor of the full candidate set (an initially
  incomplete candidate list was caught when two slots returned empty). ℂ′-side,
  same method: zw, z̄w, zw̄.
- The same-summand duals are the Killing-duals of T ↦ ⟨T·x, y⟩ (equivariant by
  construction; the earlier component-weight fitting was abandoned after it broke
  tri-equivariance — the failure mode showed up as pure same-summand Jacobi
  residuals).
- **A real indexing bug caught**: cross-slot (3,1)→2 stores with a > b and the
  unnormalized `add` made the entire third slot silently unreachable — the source of
  every earlier mixed-triple Jacobi failure and of the earlier variant-scan noise.

## Stage 3 — Jacobi closes

With the derived structure, nine scalars remain (three cross scales λᵢ, three
tri(𝕆)-dual scales μᵢ, three tri(ℂ′)-dual scales νᵢ). The probe fit (including the
pure same-summand triples that pin ν) gives the symmetric solution
**λ ≡ 1, μ ≡ −24, ν ≡ −12**, and then:

> **FULL JACOBI: 76,076 unordered basis triples, 0 failures — exact.**

L(𝕆_split, ℂ′_split) exists as a 78-dim Lie algebra over ℚ with the banked tensor.

## Stage 4 — the isomorphism

- The rational torus (4 diagonal triality directions + tri(ℂ′)) splits the adjoint
  into **72 one-dimensional rational root spaces + the 6-dim Cartan** — all over ℚ.
- The Killing form on the torus + a simple system gives a Cartan matrix that matches
  **E₆ exactly** under the relabeling (4,3,1,2,0,5).
- Chevalley generators normalized on both sides ([h,e] = 2e), the isomorphism built
  by parallel extension with identical bracket words, and verified:

> **φ([a,b]) = [φ(a), φ(b)] on ALL 3,003 basis pairs — 0 mismatches; det φ = −2/3.
> The build and L(𝕆_split, ℂ′_split) are isomorphic over ℚ, by explicit matrix.**

The direct sign choice succeeded (no sign search needed). The banked tiling
(so(8)⊕u(1)² core, three 16-tiles, the cyclic law) is now THE magic-square structure
by exact isomorphism, not by signature — the M(𝕆,ℂ) naming (B882) stands on a
theorem.

## Files

- `stage1_construct.py` → `stage1_dims.json`, `stage1_tri.pkl`
- `stage2b_derive.py` → `stage2b_products.json` (the derived conventions)
- `stage2c_final.py` → `stage2c_results.json`, `stage2c_tensor.pkl` (Jacobi 0/76076)
- `stage4_roots.py` → `stage4_roots.json` (72+6 rational)
- `stage4b_iso.py` → `stage4b_cartan.json` (E₆ matched)
- `stage4c_phi.py` → `stage4c_results.json`, `stage4c_phi.pkl` (φ, verified)
- Locks: `tests/test_b904_bs.py`

## Depends on

B854 (the frame), B880 (the signature this upgrades), B882 (the naming), B898 (the
split-form identification).
