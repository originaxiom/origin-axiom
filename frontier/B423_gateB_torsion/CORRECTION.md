# B423 — CORRECTION (2026-07-04): this is the DYNAMICAL ZETA, not the geometric torsion

**The computation is correct; the LABEL was wrong. Superseded/clarified by [[B425]].**

## What B423 actually computed

τ_m = det(I − Sym^{2m}(A)) with **A = [[2,1],[1,1]]**. That A is the figure-eight's **homological
monodromy** — the golden cat map (eigenvalues φ², φ⁻²) acting on H₁ of the fiber. So B423 computed
the **dynamical zeta / Milnor–Fried torsion** of the mapping torus with respect to the *homological*
representation. This is **golden by construction** (A is golden), and it IS a genuine Reidemeister
torsion — the closed-form τ_m = (−5)^m·(∏F₂ⱼ)², the Fibonacci-apparition prime spectrum, and the
control-distinctiveness (Fibonacci vs Pell) all STAND as correct results about the dynamical zeta.

## Where the prereg overclaimed

B423's PREREGISTRATION.md said it was computing "the E₆ adjoint Reidemeister torsion of the
figure-eight **at its holonomy**" / "the twisted torsion in Sym^{2m}(A) **at the parabolic/geometric
point**." **That is not what A = [[2,1],[1,1]] is.** The holonomy is ρ_geo, the discrete faithful
SL(2,ℂ) rep, whose entries carry ω (Eisenstein, ℚ(√−3)) — a genuinely different representation from
the homological monodromy. The dynamical zeta and the geometric torsion are two DIFFERENT invariants.

## The correct geometric torsion (B425)

At ρ_geo, the geometric E₆ Reidemeister torsion is **Eisenstein/rational**, not golden: the twisted
Alexander coefficients are rational integers (√−3 cancels — Galois-invariant at all six exponents),
and the canonical adjoint value is **−3** (= disc ℚ(√−3)), reproducing the already-banked **V30**
(normal torsion) and **V31** (Porti adjoint-torsion form). B423's −5 (golden) and B425's −3
(Eisenstein) are the object's **two torsions = the two double-uniqueness cornerstone sides**
(√5 · √−3 = √−15 = the seam).

## Net

B423 is retained as the correct computation of the **dynamical zeta** (rename it so in any write-up:
"the E₆-graded dynamical zeta," not "the E₆ Reidemeister torsion at the holonomy"). The geometric
torsion it named-but-did-not-compute is done in [[B425]]. The emergence-bar verdict is unchanged and
now doubly grounded: both torsions are named arithmetic (golden; Eisenstein), neither is the SM.
