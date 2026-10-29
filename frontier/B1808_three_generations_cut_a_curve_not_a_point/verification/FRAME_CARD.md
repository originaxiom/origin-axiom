# P-419 — frame card F2h: inversion by "three generations" in B1804's holomorphic flux frame (main, 2026-10-29; written before any computation, under WORKING_RULES' rule of 2026-10-29)

## The frame (B1804 § 4; its referee's r7)

- **C (continuous configurations).** (τ₁, τ₂) ∈ ℍ²: the abelian surfaces with real multiplication by ℤ[φ] on which LR
  acts holomorphically (A ⊗ I on H¹(T⁴, ℤ) = W ⊗ H; dz₊ = f₊·(dx + τ₁dy), dz₋ = f₋·(dx + τ₂dy)). Real dimension 4.
- **D (discrete choices).** Each is labelled.
  - The frame: holomorphic rather than split — CHOSEN.
  - The matter's flux: an LR-invariant integral class F, the first Chern class of one line bundle — CHOSEN within the
    lattice.
  - One U(1) stack, so the generation number is χ(L) — CHOSEN.
  - The complex structure against its conjugate (the mirror) — CHOSEN.
- **𝒦 (conditions built from the object).**
  - LR-invariance of every class — symmetry; FORCED by the object's monodromy.
  - Hodge type (1,1) for the fluxes — a canonical construction (holomorphic line bundles); FORCED by the frame.
- **The Standard Model's discrete datum imposed (the inversion).** The net chirality ∣χ(L)∣ = ∣F·F∣/2 = 3 (Riemann–Roch
  on an abelian surface; Td = 1). This is the input being inverted — CHOSEN.
- **Φ (outputs).** The point (τ₁, τ₂), when isolated, and its CM field. Later, not in this card's computation: the
  Yukawas as theta values at the point (Cremades–Ibáñez–Marchesano; to be read on the bench before that step).
- **Free data against rigid invariants.**
  - The family has 4 real moduli. The object's rigid data are Λ_A (the invariant lattice, rank 4) and its intersection
    form.
  - One invariant (1,1) class cuts to a complex curve; two independent ones cut to points, where NS_A(τ) has rank 2
    (Noether–Lefschetz).
  - So a point costs a rank-2 saturated sublattice of Λ_A: a discrete choice among countably many.
- **Known obstruction (B1804, r5).** The frame has no LR-invariant Kähler class: invariant (1,1) classes are negative
  definite. So supersymmetry's D-term half is unavailable here, and χ(L) < 0 for every nonzero invariant flux.

## The chain backwards

| link | supplied by |
|---|---|
| space: T⁴ with RM by ℤ[φ] | the object (LR's eigen-splitting) |
| fields: a U(1) bundle with flux F | the frame |
| zero modes: χ(L) = F·F/2 chiral fermions | the frame, by the index theorem |
| couplings: theta functions at the point | the frame, not computed here |
| running, comparison | none here |

## The question and the prediction (written before the run)

- **The question.** Among the isolated points of the family where NS_A(τ) has rank 2, which carry an invariant (1,1)
  class F with F·F = −6 (three generations)? Is that set finite, or a single point?
- **Prediction.** Infinite. A negative-definite binary lattice represents −6 for infinitely many discriminants, so "three"
  alone selects no point. The count of points with ∣det G∣ ≤ X carrying such a class grows with X. Prior about 85%.
- **What would count as selection.** A finite set, or one point, for LR, while the null does not also give one.

## The null (fixed in advance)

- **The null matrices.** The same construction with LR replaced by other hyperbolic B ∈ SL(2, ℤ): traces 4, 5, 6 and 7,
  each B_t = [[0, −1], [1, t]]. Real multiplication is then by the order ℤ[(t + √(t² − 4))/2].
- **The rule.** A "three selects" result for LR counts only if the null matrices do not also give a finite set or a
  unique point. Otherwise it is generic (E20).

## The computation (data-free)

1. Λ_A, an integral basis, and the intersection form Q (the coefficient of F ∧ F′ on vol).
2. Pairs (u, v) of primitive classes in Λ_A with coefficients ≤ N. Solve u∧Ω = v∧Ω = 0 in ℍ² and keep the isolated
   solutions.
3. At each point, compute NS_A(τ): the integral saturation of the invariant classes that are (1,1) there. Record its
   rank, its Gram matrix G, ∣det G∣, the CM field, and whether G represents −6.
4. Tabulate by ∣det G∣ ≤ X, for LR and for the null matrices.

## Scope

A frame-relative count, in a frame without a Kähler class. None of the 19. Not compared with data.
