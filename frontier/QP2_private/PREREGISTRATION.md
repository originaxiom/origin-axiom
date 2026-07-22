# PREREGISTRATION — QP-2: private states

> B-number pending (requested from cc). Sealed before computation.
> Branch: `phenomenology/theorem-chain`. cc3 seat, 2026-07-22.
> Gate 5-Q throughout; nothing to CLAIMS.

## Question

Does the generic fiber dimension of the boundary-restriction map grow with
representation rank? Concretely: at the geometric representation of the
figure-eight complement, what is

    fiber_dim(n) = dim H^1(M; ad_n) - rank(r_n)

for n = 2, 3, 4 (SL(2), SL(3), SL(4))?

## Definitions

- M = figure-eight complement (m004), T = cusp torus
- ad_n = adjoint representation of sl(n) via the principal embedding Sym^{n-1}
- r_n: H^1(M; ad_n) -> H^1(T; ad_n|_T) = boundary restriction
- fiber_dim = dim(ker r_n) = number of deformation directions invisible from T

## Method

1. Decompose ad_n under the principal sl(2): ad(sl(n)) = ⊕_{k=1}^{n-1} Sym^{2k}.
2. Compute dim H^1(M; Sym^{2k}) via Fox calculus on the Riley presentation
   (B264's method: relator 'abABaBAbaB', geometric rep at t = e^{iπ/3}).
3. Check boundary restriction rank per block: the invariant functional K(f_a, h)
   kills coboundaries; K(f_a, h) ≠ 0 ⟹ rank(r) = 1 for that block.
4. Sum: dim H^1(M; ad_n) = Σ dim H^1(Sym^{2k}); rank(r_n) = Σ rank per block.
5. fiber_dim(n) = dim H^1 - rank.

## Two outcomes (sealed before computation)

**GROWS**: fiber_dim(n) increases with n. The object has more private states at
higher rank — it has a "growing inner life" that the boundary cannot see. A7's
"Markov blanket" reading is challenged (the blanket is leaky).

**FLAT**: fiber_dim(n) = 0 for all n. Every deformation direction is visible from
the boundary — the blanket sees everything. The object has no private states at
any rank. S072's blanket reading is upheld.

## Q2 controls

- **Menal-Ferrer-Porti theorem**: dim H^1(M; Sym^{2k}) = #cusps = 1 for all k ≥ 1.
  The computation should reproduce this exactly.
- **Dehn-filling A-variety**: on the Dehn-filling components (B71 W1/W2: M^3=L,
  M^3L=1; B73: M^4=L; B83 general: L = (-1)^{n-1} M^n), the fiber dimension should
  also be 0 (each component is 1D, mapping to a 1D curve in the boundary).
- **B357 Lagrangian certificate**: the full E6 restriction has rank 6/6, confirming
  injectivity at the tangent level for all six exponent blocks.

## Prereg hash

This file is sealed before compute.py runs.
