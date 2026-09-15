# B1084 — THE FLAT G₂ CONE: the corpus's certified hole filled, and the Acharya–Witten verdict

**Date:** 2026-08-19 · **Verdict: PROVED (structure) + a routed NEGATIVE (no isolated chiral matter on the unresolved cone)**
**Provenance:** the outside bench's handoff II.5/VI.1–VI.2. **Independence: verified on
this bench by a commissioned two-implementation rebuild** (exact ℚ(√2) arithmetic with
hand-rolled field/RREF code AND a structurally different SVD/float pipeline — neither
opened the source scripts; both agree on every number) plus the source certificates
(g2cone.py, g2strata.py) re-run green here.

## 1. The object (new to the corpus — the docs sweep's one certified absence, filled)

Ĝ of order 96 acting on ℝ⁷ = ℝ³ ⊕ ℍ: the binary tetrahedral 2T by left quaternion
multiplication on ℍ (trivial on ℝ³); g_τ = right-mult by i × π-rotation about axis 1;
g_σ = left-mult by w=(1+i)/√2 · right-mult by k × π-rotation about axis 3. The quotient
(ℂ²×ℝ³)/Ĝ is a flat G₂ orbifold (the associative 3-form preserved by every generator —
under the cone metric g = dx²_ℝ³ + 2dx²_ℍ; the Euclidean Gram is the wrong test, an error
the source bench caught itself).

## 2. The stratification (every number two-implementation verified here)

- |Ĝ| = 96 exactly; the 2T copy has index 4.
- **The fixed-dimension census over the 95 nontrivial elements: {3d: 53, 1d: 42} — NO
  element has a 0-dimensional fixed set.** *(Currency 2026-09-09, B1353: the census is reproduced exactly — Ĝ is the Goursat group (D*₂, C₄; 2O, 2T) — and the apex is an isolated fixed point of the group as a whole, though of no element; what fails is not isolation but the collision: every one of the 30 A-planes meets the E₆ plane in a line.)* (The 53 split as 23 copies of the ℝ³ plane +
  30 axis⊕2-plane planes; internally consistent, 23+30+42 = 95.)
- Gauge loci (codim-4): ONE E₆ locus (the ℝ³ plane; pointwise stabilizer exactly the 2T
  copy, order 24) + THREE A₁ families (30 planes in orbits of 6, 12, 12; pointwise
  stabilizers exactly ℤ₂). Codim-6: the three axis lines, stabilizers order 48 each.
  The apex: all of Ĝ.

## 3. The Acharya–Witten verdict (physics-standard register, mechanism CITED)

- **COLLISION: MET.** ADE loci of different types (E₆ and A₁) meet at the codim-7 apex —
  a geometry the corpus never possessed.
- **ISOLATION: FAILS, by the census.** No 0-dim fixed set ⟹ every A₁ locus meets the E₆
  locus along a LINE, never transversally at a point ⟹ every localized state extends
  along a flat direction ⟹ vector-like in 4d (matter on a line = a 5d field on ℝ).
- **The mechanism, located: flatness ⟹ non-isolation ⟹ pairing.** The corpus's 32
  chirality walls, the equivariant sign balance, and this AW reading are one statement in
  three languages; the AW language names the cause most sharply.
- **The constructive flip (the hatch):** chirality costs a deformation making an A₁ locus
  meet the E₆ locus at an isolated transversal point — resolving the enhancement lines.
  Whether the object's own data admits it = B1036's multiplicity question = L79's cell
  (executed this same day, B1086) and the h¹_q grading (B1087).

**Kill-graph node routed** (the negative half). **Locks:** tests/test_b1084_g2_cone.py
(census + stabilizer orders + orbit sizes, float pipeline — fast). Full verification
record: the commissioned rebuild's two scripts archived in the arc dir.

*(Currency 2026-09-15, B1356: the deck's action on the E₆ fibre, computed with the octonionic G₂ form. Along the knot of the
descent (the ℤ/3 quotient of the Hantzsche–Wendt closing) the deck rotates the locus's normal plane by 2π/3 and is forced by
det = 1 on the normal ℂ³ to act on the fibre ℂ²/2T as the scalar ω — the centre of SU(3), inner on E₆, unlike Ĝ's holonomy twist
through 2O/2T; the local group is 2T × Z₃ (order 72) with two A₂ loci through the knot. In the compact flat orbifold over the
Hantzsche–Wendt manifold the three A₁ families of this cone are absent (the V₄ elements are 2₁ screws without fixed points);
they are this linear model's, at its apex. `frontier/B1356_the_three_on_y3` §3.)*

*(Currency 2026-09-15, B1357: the compact version. On the Hurwitz torus the 2O twist of Ĝ cannot act (it does not preserve the
lattice), so the compact flat orbifold over Hantzsche–Wendt has linear group inside (2T × 2T)/±1, no E₆ diagram flip, and its A₁
locus is not this cone's three families through the apex but a separate copy of Y₃ over the twelve 2-torsion points of stabiliser
±1 at fibre distance ½ from the E₆ copy; the D₄ points give a third copy with SO(8). `frontier/B1357_the_objects_own_joyce_orbifold`.)*
