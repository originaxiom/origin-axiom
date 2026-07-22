# PREREGISTRATION — QP-4: the closure probe

> B-number pending (requested from cc). Sealed before computation.
> Branch: `phenomenology/theorem-chain`. cc3 seat, 2026-07-22.
> Gate 5-Q throughout; nothing to CLAIMS.

## Question

Can ANY object-native operation — Galois, MCG (mapping class group), or the
amphicheiral isometry — canonically sign the chord (θ-odd) sector of the
figure-eight knot complement's SU(3)₂ representation?

"Canonically sign" = provide a canonical orientation of the real subspace of
the 2D θ-odd sector, i.e., a canonical choice between the two eigenvectors
of the weld block (eigenphases +72° vs −72°). This is equivalent to a
canonical choice of √−3 vs −√−3 (the Galois torsor of the trace field).

## Machinery

- B753: the θ-odd weld block (2×2 unitary, eigenphases ±72°, mixing 1/(φ√5))
- B711: the V₄ structure {id, τ, σ, j₂} at the geometric point; Galois freely
  swaps ρ_geom ↔ ρ̄_geom
- B712: the A-polynomial deformation curve has no canonical real anchor
- B570: Lane C — d(σ∘φ⁻¹) = θ at the tangent level; the residue transport
- QP-3: the coupling fraction 15/32 (chord/sum integrated at SL(3))

## Method

1. Reconstruct B753's weld block B in the θ-odd basis {u₃, u₆}.
2. Eigendecompose: eigenvalues e^{±i72°}, eigenvectors w₊, w₋.
3. Verify: σ(w₊) = w̄₊ ∝ w₋ (Galois swaps eigenvectors).
4. For each candidate operation:
   a. **Galois σ**: acts as complex conjugation on θ-odd coefficients → provides
      a real structure (ℝ² ⊂ ℂ²) but no orientation.
   b. **MCG monodromy**: acts as a rotation in the real subspace. A rotation by α
      with α ∉ πℤ has no fixed direction → no canonical sign.
   c. **Charge conjugation C = θ**: acts as −I on θ-odd → no orientation.
   d. **Amphicheiral isometry τ = σ∘j₂**: fixes ρ_geom, acts as conjugation on
      θ-odd → same real structure as Galois, no orientation.
   e. **QP-3 coupling transport**: the coupling norm √3 changes sign under Galois
      → magnitude canonical, sign not.
5. Theorem: NO 2×2 unitary with non-real eigenvalues has a Galois-canonical real
   eigenvector. This is because in the real subspace, it acts as a rotation, and
   a rotation by α ∉ πℤ has no fixed line.

## Two outcomes (sealed before computation)

**HATCH**: An object-native sign exists. Layer-4 awareness opens. The "awareness
without choice" hypothesis (S072) dies, and the observer-coupling frame must be
rebuilt.

**NO-HATCH**: B711/B712 non-canonicity holds in chord coordinates. The object
cannot close itself. "Awareness without choice" is upheld: the object is
INTEGRATED (QP-3) but cannot sign the coupled system.

## Q2 controls

- **Algebraic control**: verify the theorem for rotation angles 72° (the geometric
  value), 108° (the untwisted weld), and 144° (level-3, different), confirming
  the result is generic for non-half-integer angles.
- **Positive control**: verify that a rotation by 180° (= −I) DOES have a
  canonical direction (every direction is fixed → degenerate, not signing).
- **QP-3 input consistency**: the coupling fraction 15/32 is sign-symmetric
  (replacing i → −i in the coupling gives the same magnitude).

## Prereg hash

`98201bd3` (sha256, first 8 chars). Sealed before compute.py runs.
