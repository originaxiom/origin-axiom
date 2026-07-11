# Specialist note — the held-breath torsion field law (one question for a character-variety dynamicist)

**Purpose.** An adversarial literature search (B491) placed this result at APPEARS-NOVEL / NEEDS-SPECIALIST:
the framework and the *mechanism* are in the literature, but the specific field law was not found. This
note states the result precisely, cites the closest prior art, and poses the single question a specialist
can answer — with the entry point already identified.

## The result (verified in-repo, B479; = Paper 3, Theorem F7)
Work on the SL(2,ℂ) relative character variety of the one-holed torus in Fricke coordinates
(x=tr A, y=tr B, z=tr AB), with boundary/commutator trace the Markoff cubic
κ = x²+y²+z²−xyz−2. For the metallic family (monodromy RᵐLᵐ, trace m²+2 on homology; m=1 = figure-eight),
let σ_m be the finite-order mapping class acting as the involution a ↔ b.

**Claim.** On the cusp locus κ = −2, the characters fixed by σ_m are exactly the order-d **torsion**
characters for divisors d ≥ 3 of m with the order-d point non-degenerate (2cos(2π/d) ≠ 0, i.e. d ≠ 4);
the geometric (hyperbolic) character is never fixed. The number field of the order-d fixed character is
the **degree-2 extension ℚ(τ_d, √Δ_d) of ℚ(τ_d)**, with **Δ_d = τ_d²(τ_d²−8)** and τ_d = 2cos(2π/d). It
equals a single quadratic ℚ(√D_d) *only when τ_d is rational* (d = 3); otherwise D_d = Norm_{ℚ(τ_d)/ℚ}(Δ_d)
is the *norm* of the discriminant, **not** a field generator. Examples:
- d = 3: τ_3 = −1 (rational), Δ_3 = 1·(1−8) = **−7** → **ℚ(√−7)** (here D_d = Δ_d, quadratic).
- d = 5: τ_5, τ_5′ roots of x²+x−1 (so ℚ(τ_5) = ℚ(√5)); the fixed field is the **degree-4** field of
  z⁴−3z³+7z²−4z+4 with quadratic subfield **ℚ(√5)** — it splits over ℚ(√5) and stays irreducible over
  ℚ(√41). The number 41 = Norm_{ℚ(√5)/ℚ}(Δ₅) is the squarefree part of the disc, **not** the field.
- d = 7: ℚ(τ_7) is the cyclic cubic; the fixed field is the **degree-6** ℚ(τ_7, √Δ_7); E₇ =
  z⁶−5z⁵+16z⁴−25z³+30z²−12z+8 (irreducible, no quadratic subfield). Norm(Δ_7) = **−239** is a norm, not ℚ(√−239).

Verified symbolically for all m (Chebyshev transfer-matrix classification of Fix(T_m); reproducers
`B479_held_breath_torsion/held_breath_capstone.py`, and `tests/test_b479_erratum.py` pinning the d = 5, 7
fields). **Erratum (2026-07-11):** an earlier draft labelled the d = 5, 7 fields ℚ(√41), ℚ(√−239) — both
were the degree-2-only "disc → ℚ(√squarefree)" heuristic misapplied; the norm-vs-field distinction above is
the correction (cross-checked by the parallel closure audit's B494 Cantat-corollary duel).

## Closest prior art (from B491)
1. **Goldman**, *The modular group action on real SL(2)-characters of a one-holed torus*, Geom. Topol. 7
   (2003) 443–486 (arXiv:math/0305096). The exact κ-cubic framework and Γ ≅ PGL(2,ℤ)⋉(ℤ/2)². But his
   theorems are the ergodic dichotomy; he does not compute torsion fixed-characters, has no divisor
   indexing, no field formula (full-text grep: 0 hits for field/discriminant/divisor).
2. **Cantat**, *Bers and Hénon, Painlevé and Schrödinger*, Duke Math. J. 149 (2009) — **the mechanism.**
   He computes the fixed points of Ψ = [[2,1],[1,1]] (= our A₁) on the character surface via the fixed
   curve (x, x/(x−1), x): four points solving x⁴−3x³+x²+4x−2=0, factoring over **ℚ(√17)** into the
   figure-eight-hyperbolic pair and the SU(2) pair. This is the *same* fixed-curve → quartic → quadratic-
   field technique — but for the pseudo-Anosov Ψ at commutator-order-4, not the finite-order σ_m at κ=−2.
3. **Biswas–Gupta–Mj–Whang**, *Surface group representations in SL₂(ℂ) with finite mapping class orbits*,
   Geom. Topol. 26 (2022) (arXiv:1707.00071). Finite genus-1 MCG orbits = finite/special-dihedral (once-
   punctured torus in App. A). But they classify finite orbits of the FULL MCG, not fixed points of one
   σ_m; no field formula.

## The one question for the specialist
Cantat's (2009) fixed-curve technique produces, for the pseudo-Anosov A₁, a quadratic field (ℚ(√17))
from a quartic. Our σ_m is a *finite-order* class at the cusp κ = −2, and the fixed characters are the
order-d elliptic points.

> **Is the field law ℚ(√D_d), D_d = Norm(τ_d²(τ_d²−8)) — with the divisor-of-m indexing d ≥ 3, d ≠ 4 —
> an easy corollary of Cantat's fixed-curve method applied to σ_m at κ = −2, or is it a genuinely new
> invariant of the order-d elliptic points of the one-holed-torus character variety?** And is the
> divisor-indexed fixed-locus statement documented anywhere in the later Cantat–Loray / Bowditch /
> Markoff-dynamics literature?

**Entry point.** Apply Cantat's (x, x/(x−1), x)-type fixed-curve intersection to the σ_m-fixed locus on
κ = −2; the order-d elliptic character has trace 2cos(2π/d) = τ_d, and the claim is that the resulting
field is ℚ(√ Norm(τ_d²(τ_d²−8))). A specialist can likely settle "corollary vs. new" in an afternoon.

**Honest status.** This is a negative-existence verdict over the canonical references (Goldman, Cantat,
BGMW, Lisovyy–Tykhyy); less-indexed literature (theses, proceedings, later Markoff-dynamics preprints)
was not exhaustively mined. The result is *not* claimed as first; it is claimed as *not-found-where-it-
should-be*, and posed for adjudication.
