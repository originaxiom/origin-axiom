# B711 (Path 2) — the TWO-ℤ/2 DEGENERATION: amphichirality and Galois are ORTHOGONAL (V₄)

*cc banking seat, 2026-07-19. Sealed prereg de24a647. Campaign path 2/3
(compute→3-skeptic-adversarial-verify→refine). Outcome **B**, NOT refuted (multiple
skeptics independently re-derived the curve from the two-bridge word — exact
agreement), high confidence, firewall clean. Verified-on-receipt. Structural only.*

## Verdict (OUTCOME B — as sealed)
On the SL(2,ℂ) character variety X(4₁), **amphichirality and the ℚ(√−3) Galois
involution are two distinct, commuting ℤ/2's that act ORTHOGONALLY at the
geometric point.** B709's koan resolves cleanly: the still point (amphichirality,
CS=0) and the groundlessness (the Galois/measurement swap) are *independent*, not
locked — the two ℤ/2's are the two non-identity legs of a V₄, not one symmetry.

## The discriminating fact: the orbit of Galois on Fix(amphichirality)
- **The curve:** C: y²−(x²−1)y+(x²−1)=0 (x=tr μ, y=tr(ab⁻¹)), from the Riley rep
  of π₁(4₁)=⟨a,b | aw=wb⟩, w=bABa; Alexander poly −(t²−3t+1), SnapPy CS=0, D₄
  amphichiral. **Geometric point:** x=2 → y=(3±√−3)/2 ∈ ℚ(√−3).
- **Fix(amphichirality):** amphichirality τ = conj∘j₂, where j₂:(x,y)→(x,x²−1−y)
  is the unique holomorphic curve-involution sending ρ_geom→ρ̄_geom (realized by
  24 group endomorphisms; the meridian-sign involutions j₁,j₃ by 0). Both
  ρ_geom=(2,(3+√−3)/2) and ρ̄_geom=(2,(3−√−3)/2) lie in Fix(τ), and are DISTINCT.
- **Galois (complex conjugation, √−3→−√−3) SWAPS them** → a **FREE 2-orbit inside
  Fix(τ)**: Fix(τ) is setwise Galois-stable but pointwise-free at the geometric
  point. In V₄={id,c,τ,j₂}: stab(ρ_geom)={id,τ}, and Galois c is in the swapping
  coset. **⟹ orthogonal.**

## The gift: the golden point is the Galois-fixed real end
Galois's ONLY fixed points on Fix(τ) are at disc_y=(x²−1)(x²−5)=0, i.e. x²∈{1,5}:
**x²=5 → the GOLDEN point (√5,2), tr[a,b]=2** (real/reducible — the *hearing*
field's arithmetic end), and x²=1 → a 6th-root singular point. So the being field
(ℚ(√−3), the geometric point) is Galois-*swapped* while the hearing field (ℚ(√5),
the golden point) is Galois-*fixed and real* on the amphichiral slice — the two
faces, again, on one curve.

## Caveats
- Galois is free AT THE GEOMETRIC POINT but not globally on Fix(τ) (it fixes the
  golden/reducible real end x²∈{1,5}); the sealed decision rests on the
  geometric-point orbit (free → B). Disclosed, not fatal.
- amphichirality=j₂ rests on three anchors (unique holomorphic involution
  ρ_geom→ρ̄_geom; realized by group endomorphisms; SnapPy amphichirality), not on
  a peripheral A-polynomial computation (not carried out). "Fix(τ)=CS=0 slice" is
  anchored at the geometric point, not by a CS evaluation along the whole slice.
- CITED (SnapPy): CS=0, D₄-amphichirality, shape e^{iπ/3}. Everything else COMPUTED
  exact (sympy).

## Placement
LAW_MAP: the two ℤ/2's are the orthogonal legs of a V₄ (being-swap vs
amphichirality), with the golden ℚ(√5) point as the Galois-fixed real end.
Sharpens B704/B709. Nothing to CLAIMS.
