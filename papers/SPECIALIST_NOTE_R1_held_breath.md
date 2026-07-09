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

**Claim (field statement corrected 2026-07-09; B491 round-2 re-panel).** On the cusp locus κ = −2, the
characters fixed by σ_m are exactly the order-d **torsion** characters for divisors d ≥ 3 of m with the
order-d point non-degenerate (2cos(2π/d) ≠ 0, i.e. d ≠ 4); the geometric (hyperbolic) character is never
fixed. The number field of the order-d fixed character is the quadratic extension
**ℚ(τ_d, √(τ_d²(τ_d²−8)))** of ℚ(τ_d), τ_d = 2cos(2π/d) — degree 2·[ℚ(τ_d):ℚ] over ℚ. The rational
invariant **D_d = Norm_{ℚ(τ_d)/ℚ}(τ_d²(τ_d²−8))** is a norm/discriminant factor of that field, **not**
in general its generator:
- d = 3: τ_3 = −1 is rational, so the tower collapses: D_3 = 1·(1−8) = −7 and the field **is** ℚ(√−7)
  (minpoly z²−z+2).
- d = 5: τ_5, τ_5′ roots of x²+x−1; the field is a **degree-4 extension of ℚ containing ℚ(√5)**
  (character minpoly z⁴−3z³+7z²−4z+4, discriminant 5²·41). D_5 = 41 appears as the discriminant factor;
  the earlier statement "→ ℚ(√41)" conflated the norm with the field and is **withdrawn**.

Verified numerically/symbolically to order 13 (reproducer `B479_held_breath_torsion/held_breath_capstone.py`);
the d=5 field correction re-verified independently (quartic irreducible over ℚ, disc factors 5²·41, ℚ(√5)
subfield; the per-conjugate values are quadratic over ℚ(√5), only their norm is rational).

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

> **Is the field law ℚ(τ_d, √(τ_d²(τ_d²−8))) — with the divisor-of-m indexing d ≥ 3, d ≠ 4, and rational
> norm-invariant D_d = Norm(τ_d²(τ_d²−8)) — an easy corollary of Cantat's fixed-curve method applied to
> σ_m at κ = −2, or is it a genuinely new
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
