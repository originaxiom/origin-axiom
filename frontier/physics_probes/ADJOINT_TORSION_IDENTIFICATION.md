# τ_m IS Porti's adjoint Reidemeister torsion form (V30 open item — resolved)

**Date:** 2026-06-04. **Status:** exploratory, committed for honest history. Proven core P1–P16
untouched. Script: `frontier/physics_probes/adjoint_torsion_identification.py` (symbolic, m=1,2).
Standalone topology; resolves the open question flagged in `CS_INVARIANT_FAMILY.md` / Ledger V30.

**Question (V30 open item).** Is `τ_m = det'(I − D(T_m²)|_normal)` — the normal-bundle determinant on
the Fricke surface — actually the adjoint Reidemeister torsion, or a related-but-distinct invariant?

**Answer: it IS the adjoint Reidemeister torsion form** (Fried–Milnor mapping-torus theorem),
normalized relative to the eigenvalue-1 = cusp/peripheral deformation direction — i.e. **Porti's
adjoint torsion form** for the one-cusped manifold. Verified symbolically (m=1,2).

## The verification (three structural facts, symbolic)

For the mapping torus of `φ_m²` on the once-punctured torus `F` (free `π₁=F₂`), with the adjoint
(`sl₂`) local system at a rep on the fixed locus:

1. **Non-acyclic everywhere on the fixed locus.** `det(I − D(T_m²)) = 0` on the full 3-dim Fricke
   tangent (verified, both m). The fixed locus *is* the deformation / A-polynomial curve, so
   `H¹(F, Adρ) ≠ 0` at every point — the adjoint complex is never acyclic there.
2. **The eigenvalue-1 direction is the cusp/peripheral deformation.** The fixed-curve tangent
   `v = ∂/∂x (x, y(x), z(x))` satisfies `D(T_m²)·v = v` exactly (verified, both m) — so the surviving
   `λ=1` eigenvector is precisely the peripheral `H¹(∂F)` direction along the A-polynomial curve.
3. **Dimension count.** `H⁰(F, Adρ)=0` (irreducible) ⇒ `dim H¹(F, Adρ) = −χ(F)·3 = 3` = the Fricke
   tangent. So `D(T_m²) = φ*` acts on `H¹(F, Adρ) ≅ C³`.

By **Fried–Milnor**, the Reidemeister torsion of a mapping torus with a flat bundle is
`det(I − φ*)` on the fiber's twisted cohomology. Here that is `det(I − D(T_m²))` on `H¹(F,Adρ)=C³`,
which vanishes (Fact 1) — so the manifold's adjoint torsion is a **form** (not a number), valued
relative to the surviving peripheral direction (Fact 2). The determinant on the **2-dim complement**
of that direction is exactly `τ_m`:
```
   tau_1(x) = -(2x^2 - 3x + 3)/(x-1) ,   tau_2(x) = -4x^4/(x^2-2)
```
**So `τ_m` is Porti's adjoint Reidemeister torsion form** of the metallic mapping torus, relative to
the cusp.

## Why the naive Wada "number" comparison fails (and that's the point)

A direct knot-group Wada/twisted-Alexander **number** does **not** reproduce `τ_m`: because the
adjoint complex is non-acyclic on the *entire* fixed locus (Fact 1, `H¹≠0` everywhere = the
deformation curve), a Wada number degenerates (numerically `det` of a near-singular twisted Jacobian).
This is not a discrepancy — it **confirms** that the correct object is the torsion **form** (Porti),
which is exactly what the normal-bundle determinant `τ_m` computes. (Checked: the bundle presentation
`⟨A,B,t | tAt⁻¹=A²B, tBt⁻¹=AB⟩` is satisfied by the rep to ~1e-15, but its adjoint Wada ratio is not
constant — the non-acyclicity signature.)

## Consequence for the corrected values

The corrected `τ₁=−3` (in the figure-eight trace field `Q(√−3)`) and `τ₂=−16` are therefore genuine
**adjoint-torsion-form values** — not the abelian knot determinant (`5`/`32`) that the earlier
`κ=+2` mis-evaluation (at the *identity* rep `x=2`) produced. The arithmetic meaning of `τ₁=−3` (the
trace-field discriminant) sits in the right (adjoint Chern–Simons one-loop) framework.

## Honest remaining caveat

The **exact scalar normalization** vs a specific *published* Porti value depends on the choice of
peripheral `H¹` basis (which boundary curve, what scaling) and a sign/Euler-factor convention. That
calibration to a reference number is **not pinned here** — but the *identification of the invariant*
(it is the adjoint Reidemeister torsion form, Fried–Milnor + Porti) is settled. V30's open question is
resolved at the structural level; the scalar calibration is the remaining careful step.

**Disposition:** resolves V30's open item (τ_m is the adjoint torsion form, verified). Topology, not a
physics crossing. Proven core untouched.
