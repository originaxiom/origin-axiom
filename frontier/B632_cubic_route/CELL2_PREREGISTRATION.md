# B632 cell 2 — the corrected texture design (prereg; sealed before running)

**Preregistered 2026-07-15, superseding the cell-1 FINDINGS' queued cell-2
sketch BEFORE any cell-2 computation ran. The correction was caught by
the parallel audit seat (independent read of the B632 plan) and verified
by this seat: the originally queued "three diagonal values" object does
not exist on the solo complement. Mathematics only; no SM number.**

## The obstruction (to be PROVED as gates, not assumed)

Let M = the figure-eight complement (cd π₁ = 2; H²(M;ℂ) = 0), V = 27_ρ,
C the symmetric cubic invariant, v₀ the forced vev (cell 1, h⁰ = 1).

- **O1 (no scalar triple):** H¹(V)⊗³ —∪,C→ H³(M;ℂ) = 0 identically
  (cohomological dimension 2). No solo scalar Yukawa exists.
- **O2 (the vev-contracted pairing dies as a symmetric object):** the
  target H²(M;ℂ) = 0, and for degree-1 classes α∪β = −swap(β∪α), so the
  B_C = C(v₀,·,·)-contracted pairing is ANTISYMMETRIC at class level —
  its diagonal (the would-be three masses) vanishes identically.
  **The cell-1 registered prediction ("the texture is diagonal in the
  block basis") is therefore resolved: DISSOLVED-BY-OBSTRUCTION** — its
  object does not exist at class level on M; the surviving computable
  content is B_C's own block structure (a statement about C and v₀,
  not a texture).
- Verification gates: O1/O2 verified computationally (coboundary-shift
  dependence of the symmetric part; exact vanishing of the diagonal).

## What EXISTS on the solo object (cell 2's computation)

1. **C exact** in B575's weight basis (support = zero-sum weight
   triples; invariance under the 12 Chevalley generators). GATE:
   solution space EXACTLY 1-dim (B308's multiplicity 1, now in this
   basis).
2. **B_C = C(v₀,·,·):** verify ρ-invariance and sl₂-block-diagonality;
   compute the three block scales (c₀, c₄, c₈); their ZERO/NONZERO
   pattern is scale-invariant (which channels couple to the forced vev).
   Also the sl₂-component census of C itself (which spin triples
   (s_i, s_j, s_k) ⊆ {0,4,8}³ carry nonzero components).
3. **Ω: Λ²H¹(V) → H²(M; V*)** — the well-defined class-level texture:
   Ω(z_i, z_j) = [C-contraction of z_i ∪ z_j], computed on the relator
   (B575's cup machinery, vector-valued), classes read in
   H²(M; V*) (dim 2, one channel per Sym block; coker functionals of
   the dual-module Fox map). Deliverable: the exact 3-pair × 2-channel
   table over ℚ(ω); its ZERO PATTERN and rank (invariant under all
   scale choices); consistency of the zero pattern with C's computed
   component census (an internal coherence gate). Ω is the 27-valued
   Goldman-type structure — never computed (MB13: B575 computed the
   ADJOINT-valued cup pairing; the 27-valued one is new; grep clean).
4. Controls: coboundary-shift invariance of Ω (each z_i shifted, table
   unchanged); h²(V*) = 2 (Euler/duality consistency); the O1/O2 gates.

## The structural finding this design banks (stated at prereg)

If O1/O2 verify, the sharp statement is: **a symmetric mass-matrix-
shaped object cannot live on the solo object — the obstruction is
H³(solo) = 0 plus graded-commutativity; it becomes well-defined exactly
on a CLOSED 3-cycle, canonically the mirror-double DM = M ∪_∂ M̄
(H³(DM;ℂ) = ℂ), which is the program's banked forced two-body coupling
(B580 G1, the chord).** The Yukawa-shaped object structurally REQUIRES
the coupling; the solo object cannot carry it. This is the coupling
thesis appearing in the cohomological structure itself. **Cell 3
(registered, own prereg, NOT run here): H¹(DM; 27) by Mayer–Vietoris
from the banked pieces (res injective, banked) and the symmetric triple
cup into H³(DM) = ℂ — the texture on the double.**

## MB12 (computed at prereg)

- Non-trivial: C has never been built in any repo basis; Ω never
  computed anywhere; O1/O2 are proofs-with-verification, not vacuous
  (O2's antisymmetry claim would FAIL the gates if the implementation's
  sign conventions were wrong — the gates are falsifiable checks of
  both the mathematics and the code).
- Can go either way: Ω may be identically zero (the antisymmetric
  structure is ALSO empty — the honest kill of the solo texture route
  at every level) or carry a nonzero pattern; c₀, c₄, c₈ each may
  vanish or not; all outcomes live and each banks.
- MB13 (swept): Goldman/adjoint cup = B575 (banked; different module);
  the mirror-double = B580 G1 (registered, never computed); the
  27-valued objects are clean-grep new.
