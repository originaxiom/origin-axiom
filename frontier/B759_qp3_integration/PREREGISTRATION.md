# PREREGISTRATION — QP-3: the integration cell

> B-number pending (requested from cc). Sealed before computation.
> Branch: `phenomenology/theorem-chain`. cc3 seat, 2026-07-22.
> Gate 5-Q throughout; nothing to CLAIMS.

## Question

At the discrete faithful (geometric) representation of the figure-eight knot
complement m004, do the θ-odd (chord/hearing) and θ-even (sum/being) sectors of
the trace map's Jacobian couple?

## Object

The SL(n,ℂ) trace map T_n: u ↦ {tr Sym^{n-1}(g(u)) : g ∈ generators}, evaluated
at the Riley parametrization of m004 with u = ω = exp(2πi/3), the geometric root
of the Riley polynomial u² + u + 1 = 0.

The amphicheiral involution θ acts on the character variety by complex conjugation
of traces: θ(u) = ū. The θ-fixed locus is the real slice (u ∈ ℝ). The geometric
point u = ω is OFF this locus (Im ω = √3/2 ≠ 0).

## Machinery

- B285: the exact Riley representation A = [[1,1],[0,1]], B = [[1,0],[-u,1]]
- B753: the θ-split at SU(3)₂ — charge conjugation C decomposes the 6D
  representation space into 4D θ-even + 2D θ-odd; eigenphases ±72°
- B98: the trace-map Jacobian at the geometric rep (adjoint torsion τ = −3)
- B746: the two-column law (golden/hearing/ℚ(√5) vs Eisenstein/being/ℚ(√−3))

## Method

For each SL(n) level (n = 2, 3):

1. Compute the trace coordinates {tr Sym^{n-1}(g)} as functions of the Riley
   parameter u
2. Compute the complex derivative dT_n/du at u = ω
3. The off-block of the Jacobian (in the θ-decomposition) = Im(dT_n/du) (the
   imaginary part of the complex derivative, by Cauchy-Riemann)
4. If ||Im(dT_n/du)|| = 0: DISSOCIATED at level n
   If ||Im(dT_n/du)|| ≠ 0: INTEGRATED at level n

## Two outcomes (sealed before computation)

**INTEGRATED**: The Sym² (SL(3)) off-block norm is nonzero at the geometric
point. The object's two voices couple where it lives. The coupling norm is a
program-internal number (a Jacobian norm, nothing more — S072's guard).

**DISSOCIATED**: The Sym² off-block norm is zero at the geometric point. The
voices decouple where the object lives; integration is a non-geometric luxury.

## Q2 controls (non-universality + comparator)

- **θ-fixed locus control**: evaluate the same computation at a real value of u
  (on the θ-fixed locus). The off-block must be zero there.
- **Object-specificity**: the off-block norm depends on Im(u_geom), which encodes
  the trace-field discriminant. For a manifold with trace field ℚ(√−d), the
  coupling is proportional to √d — not universal.
- **Q2b comparator**: compute the adjoint off-block for a different manifold
  (m003 = the sister manifold, and the 5₂ knot complement if feasible) and verify
  the coupling norm differs.

## E20 guard

One object (m004), one trace map, two levels (SL(2), SL(3)). The two-outcome is
forced by the computation; no selection effects. The coupling norm is a single
number — not a search over a space.

## Prereg hash

This file is sealed before compute.py runs.
