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
  element has a 0-dimensional fixed set.** (The 53 split as 23 copies of the ℝ³ plane +
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

---

## ADDENDUM 2026-09-14 — §3's ISOLATION VERDICT IS CORRECT; ITS DERIVATION IS E70-CLASS AND IS HERE REPLACED BY DIRECT COMPUTATION (outside bench, the reopened-G₂-hatch cell)

**Nothing below is struck. The verdict of §3 is unchanged and is now derived validly for the first time.**

§3 reads:

> *"ISOLATION: FAILS, **by the census**. No 0-dim fixed set ⟹ every A₁ locus meets the E₆ locus along a
> LINE, never transversally at a point."*

The census is stated in §2 and in `exact_verify.py` as ranging **over the 95 nontrivial ELEMENTS**
(`# ITEM 2: fixed-subspace dimension census over the 95 nonidentity elements`). An A₁–E₆ intersection,
however, is `Fix(H₁) ∩ Fix(H₂) = Fix(⟨H₁, H₂⟩)` — **the fixed set of a SUBGROUP, which the census does not
range over.** The implication therefore interchanges quantifiers: *no element has a 0-dimensional fixed
set* does not entail *no intersection of loci is 0-dimensional*.

This is exactly the class **B1304** named as **E70** while rescoping B1259, and B1304 supplies a group where
the step fails: on **(ℤ/2)³ ⊂ G₂** the subgroup-order → fixed-dimension map is **{1: 7, 2: 3, 4: 1, 8: 0}** —
**no element reaches dimension 0, a subgroup does**, and *"the origin is an isolated maximal-isotropy stratum
although no element has an isolated fixed point."*

**The direct computation, on this arc's own Ĝ with this arc's own exact ℚ(√2) machinery.** For each of the
30 A₁ planes, the exact linear meet with the E₆ locus, `dim(U ∩ V) = dim U + dim V − dim(U + V)`:

| | |
|---|---|
| population | **30 A₁ loci, 1 E₆ locus, 30 intersections** (printed before any rate) |
| intersection-dimension distribution | **{1: 30}** |
| A₁ loci meeting E₆ in dimension 0 | **0** |

**The structural reason, which the census could not have seen:** the E₆ locus is the common fixed space of
the 24-element 2T copy and equals **ℝ³ ⊕ 0**; each A₁ locus is **(a line in ℝ³) ⊕ (a plane in ℍ)**. Every
pair therefore shares exactly that line. This is not a near miss a finer search could flip.

**So §3's "every A₁ locus meets the E₆ locus along a LINE" is TRUE, and is now a computed fact rather than
an inference from the wrong population.** The downstream chain — *flatness ⟹ non-isolation ⟹ pairing ⟹
vector-like* — is unaffected, and **B1259's theorem already independently closes every flat Ĝ**, so no
verdict anywhere moves.

**What this addendum does not claim.** It says nothing about what an Acharya–Witten construction formally
requires (B1304's fence stands: *"the example is not an Acharya–Witten construction"*); it derives no chiral
matter; I-26 remains **UNEARNED**, so no generation count is licensed; and it concerns only **flat**
orbifolds — B1259's own consequence points onward, that chiral matter *"requires genuine CURVATURE — a
conical G₂ singularity, whose local model is a cone over a 6-manifold rather than a linear action on ℝ⁷."*

Certificate: `outside_bench/certificates/the_reopened_g2_hatch.py`; output
`outside_bench/outputs/the_reopened_g2_hatch_out.txt` (exit 0, four controls PASS, including B1084's own
verifier re-run by exec with **0 items reporting FAIL**). Seal:
`outside_bench/seals/THE_REOPENED_G2_HATCH_PREREG.md` ADDENDUM 1 (**BENCH ERROR #35**: the cell's *number*
reproduces §3 and is not news; its *derivation* is what is new). Gate 5 untouched; nothing promotes to
`CLAIMS.md`.
