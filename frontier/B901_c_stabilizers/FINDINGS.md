# B901 — N5: the C-stabilizer is discrete, plane-preserving, and cannot be the c-carrier over ℝ

**Date:** 2026-08-05 · **Seat:** cc (banking) · **Status:** exact (nullspaces over ℚ; B898's exact factors)

## The question (N5)

B893 showed the Chevalley involution does not stabilize the measurement torus
C. Which symmetries DO — and can any of them carry c (conjugation/orientation)
into θ (the B570 Lane-C crux)?

## Result 1 — the continuous normalizer is trivial: n(C) = z(C) = 12

The exact solve over ℚ: {x ∈ e₆ : [x, C] ⊆ span(C)} has dimension **12 =
dim z(C) = the floor**. Every element that normalizes C centralizes it —
**no continuous motion of C inside e₆ exists; any C-stabilizing symmetry
acts through a DISCRETE group** (its image in GL(C) meets the identity
component trivially).

## Result 2 — the spectral obstructions (from B898's exact census)

For any real automorphism σ with σ(C) = C: ad(σx) = σ ad(x) σ⁻¹, so the
exact spectrum of every torus element is preserved. Hence:

- **The split/compact swap is forbidden over ℝ**: spec(ad x₈) is real,
  spec(ad x₁₄) imaginary (B898, exact) — no real automorphism maps the
  measured plane into the compact slots or back. The measured plane is
  preserved SETWISE by every real C-stabilizing symmetry.
- **The within-plane swap x₈ ↔ x₁₆ is also forbidden**: the exact factor
  multisets of ad(x₈) and ad(x₁₆) differ (locked). Same for the compact
  pair by the same computation pattern.
- **Sign flips remain allowed**: every nonzero factor of both split charges
  is an even polynomial (spectra symmetric under negation) — x ↦ −x on a
  charge is not spectrally obstructed.
- On the measured plane, any C-stabilizing symmetry permutes the three
  enhancement lines (P69) — its plane action embeds in the finite symmetry
  group of the line triple.

## The structural conclusion (the sharpest Lane-C no-go yet)

Any REAL symmetry stabilizing the measurement frame is discrete, preserves
the measured plane setwise, cannot exchange split with compact, and cannot
even swap the two measured charges. **The c→θ carrier, if it exists, is not
a real C-stabilizing symmetry — the transfer channel must pass through the
complexification**, precisely where the second measurement's wall lives
(det₁₄ > 0 at all three roots ⟹ the wall charge is imaginary — B892/B893).
The real/complex measurement alternation (M3) and the Lane-C question now
point at the same door: layer 8.

## Files

- `c_stabilizers.py` → `normalizer.json`, `spectral_obstructions.json`
- Locks: `tests/test_b901_stab.py`

## Depends on

B854, B893 (ω transverse), B898 (the exact census — the obstruction engine),
B892 (the complex wall), P69 (the line triple).
