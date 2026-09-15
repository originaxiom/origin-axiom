# B1358 — THE E₆ APEX FAMILY: the twistor cones of S⁴/(2T × Γ_R) are G₂ cones with an E₆ locus and a companion of type {±1}·Γ_R (A₁, A₃, A₅, D₄, E₆ — never A₂) plus mixed A-loci over the cone circles whenever Γ_R shares eigenvalues with 2T; only Γ_R = 1 (B1355's cone) has no extra loci and a companion the object's own background supplies — the SU(2) copy of Y₃ — with the inflow coefficients of E₆ and SU(2) at the apex in the exact ratio 12 : 1; the apex-on-the-knot model (Γ_R = Z₃) comes with an A₅ companion and four A₂ branches the background does not have (L213 (ii) negative in the twistor family)

**Date:** 2026-09-15 · **Seat:** cc (the SM-derivation branch) · **Status:** PROVED (a finite census over seven groups at double precision with tolerance 10⁻⁷ on groups of order ≤ 576 — every count an integer; the ADE typing of the mixed loci uses the G₂ argument of §2; the companion table uses B1357's census; the inflow ratio uses Witten's coefficient as B1355 §3 states it) · **Price: unchanged** · **Numbering:** B1358 (L213 (ii), (iv); feeds L212).

## 0. Seen from above

B1357 left the destination's item 1 as a design with two unknowns: which locus of the object's own background can touch the E₆
copy of Y₃ at the apexes, and whether the apex could sit on the knot instead. Both are questions about one family: the twistor
cones of S⁴/Γ with Γ = 2T × Γ_R, 2T on the first quaternionic factor (the E₆ pole) and a finite Γ_R ⊂ Sp(1)_R on the second (the
companion pole). The family is computed here for Γ_R ∈ {1, Z₂, Z₃, Z₄, Z₆, Q₈, 2T}. The companion at the second pole is always
{±1}·Γ_R ⊂ SU(2) — the −1 of 2T is there whatever Γ_R is, so the companion has even order: A₁, A₃, A₅, D₄ or E₆, never A₂ — and
whenever Γ_R shares an eigenvalue with an element of 2T, the pairs (g, h) with g ~ h fix lines over the cone circles of S⁴/Γ and
put further A-type loci through the apex. Only Γ_R = 1 (or Z₂, the same effective group) is clean: E₆ and A₁, nothing else — B1355's
cone — and its companion is exactly the SU(2) copy of Y₃ that B1357 found at fibre distance ½ from the E₆ copy. The apex on the
knot (L213 (ii)) is Γ_R = Z₃: its E₆ locus is ℝ³/Z₃ as the descent requires, but its companion is A₅ = SU(6) and four A₂ branches
pass through it — neither exists in the object's own background. So the touching design is pinned to one picture: the SU(2) copy
of Y₃ meets the E₆ copy at a deck orbit of three apexes, each B1355's cone.

## 1. The census (`apex_family.py`; record `apex_family_run.txt`)

Γ = 2T × Γ_R acts on ℂ⁴ = ℂ²_a ⊕ ℂ²_b as diag(g, h) and on CP³ = P(ℂ⁴); Γ ⊂ Sp(1) × Sp(1) ⊂ Sp(2) preserves the nearly-Kähler structure,
so the cone over CP³/Γ is a G₂ cone (B1355 §1), the twistor cone of S⁴/Γ. Scalars ±(1, 1) act trivially. For each Γ_R: the lines
fixed pointwise by some element (2-dimensional eigenspaces), in Γ-orbits, with the effective pointwise stabiliser and its abstract type;
the enhanced points on those lines; the degree of each pole line onto its image (|effective group| / |stabiliser| / |orbit|).

| Γ_R | effective order | first pole L_b: type, degree | second pole L_a: type, degree | mixed loci (orbits × lines: type) | enhanced points |
|---|---|---|---|---|---|
| 1 | 24 | E₆, 1 | **A₁**, 12 | none | 14 on L_a (8 with Z₆, 6 with Z₄ — B1355's "isolated" points) |
| Z₂ | 24 | E₆, 1 | A₁, 12 | none | 14 |
| Z₃ | 72 | E₆, **3** | **A₅**, 12 | 4 × 4: A₂ | 16 |
| Z₄ | 48 | E₆, 2 | A₃, 12 | 2 × 6: A₁ | 16 |
| Z₆ | 72 | E₆, 3 | A₅, 12 | 4 × 4: A₂ | 16 |
| Q₈ | 96 | E₆, 4 | **D₄**, 12 | 3 × 12: A₁ | 20 |
| 2T | 288 | E₆, 12 | **E₆**, 12 | 1 × 36: A₁; 4 × 16: A₂ | 28 |

No fixed point lies off every fixed line in any case: the codimension-six lines of the cone all sit inside the ADE loci (the cone
points of the loci's links). b₂(CP³/Γ; ℚ) = 1 throughout (a linear action fixes the hyperplane class).

## 2. Two facts used

**The companion has even order.** The pointwise stabiliser of L_a = P(ℂ²_a ⊕ 0) is {(g, h): g = ±1}, acting on the normal ℂ² of the
line by (±1)⁻¹h: the group {±1}·Γ_R. Since −1 ∈ 2T always, this group contains −1: cyclic of even order (A_{odd}), Q₈ (D₄), 2T (E₆).
An A₂ companion is impossible in the family — the SU(3) locus of the object's own background (fibre stabiliser Z₃) can never be the
companion of an E₆ apex.

**The mixed loci are ADE.** An element (g, h) with g and h sharing an eigenvalue λ (with multiplicity one each) fixes the line
P(v_g ⊕ v_h) pointwise; in the twistor complex structure its normal weights are (λ̄/λ, λ̄/λ), whose determinant is 1 only for λ = ±i
(the census's "determinant = 1: False" rows are the λ = ω cases). That is not a failure of the ADE property: the fixed set of a
non-identity element of G₂ on ℝ⁷ is a line or an associative 3-plane, and the cone over the fixed line is such a 3-plane; the
pointwise stabiliser of an associative 3-plane in G₂ is an SU(2) acting on the normal ℝ⁴, so the stabiliser Z₃ of a mixed line acts
on its normal as Z₃ ⊂ SU(2) in the G₂-adapted complex structure — the twistor structure is the other one on that ℝ⁴ (B1356 §3 met the
same pair: ω on the fibre in one structure, (ω, ω̄) in the other). The abstract group therefore types the locus: cyclic n → A_{n−1},
Q₈ → D₄, 2T → E₆. These lines lie over the cone circles of S⁴/Γ (the points [q₁ : q₂] with q₁⁻¹ g q₁ = q₂⁻¹ h q₂), codimension-three
strata of the 4-orbifold, not orbifold points.

## 3. The companion table against the object's own background

B1357's background has loci with fibre stabilisers 2T (E₆ on Y₃), Q₈ (SO(8) on Y₃), ±1 (SU(2) on Y₃), Z₃ (SU(3) on T³). Reading the
census against it:

| apex model | companion | fits the background? |
|---|---|---|
| Γ_R = 1 (B1355) | A₁ = the SU(2) copy of Y₃ | **yes, with nothing else through the apex** |
| Γ_R = Q₈ | D₄ = the SO(8) copy of Y₃ | only if three further A₁ branches pass through each apex (the single SU(2) copy would have to pass through thrice) |
| Γ_R = 2T | E₆ = the E₆ copy itself (a self-touching) | needs one A₁ and four A₂ branches through each apex: no |
| Γ_R = Z₃, Z₆ (the apex on the knot, L213 (ii)) | A₅ | **no**: no SU(6) locus in the background, and four A₂ branches (the descent has two along the knot, B1357) |
| Γ_R = Z₄ | A₃ | no SU(4) locus in the background |

So L213 (ii) is negative within the twistor family (the deck-fixed apex's model is forced to Γ_R = Z₃ by B1356 §3 — the deck's lift
normalises 2T inside 2T and rotates the E₆ line — and that model's companion is A₅), and L213 (iv) is pinned: the touching design is
the SU(2) copy of Y₃ meeting the E₆ copy at a free deck orbit of three points, each apex B1355's cone.

## 4. The inflow at the clean apex, exactly

Witten's coefficient for the mixed anomaly U(1)·G² of the chiral matter at the apex is ∫_{U_G} w over the link of G's locus (B1355 §3).
Both links are images of lines of degree 1 in CP³; the E₆ line maps to its image with degree 1 (fixed pointwise by all of 2T), the A₁
line with degree 12 (2T acts on it through T = A₄, image the orbifold sphere S²/A₄ with the 14 cone points). Hence, for the same
harmonic form, **A(U(1)·E₆²) : A(U(1)·SU(2)²) = 12 : 1** at B1355's apex (and 4 : 1, 6 : 1, 3 : 1, 1 : 1 for Z₃, Z₄, Q₈, 2T). With one
27 of charge q on the E₆ side (T(27) = 3 in the normalisation T(2) = ½) the SU(2)-charged chiral matter at the apex has
∑ q_i T(R_i) = q/4, i.e. ∑ q_i = q/2 over doublets: the inflow fixes the charge-weighted count, not the number of doublets. The number
matters: the SU(2) copy of Y₃ touches the E₆ copy at three points, and SU(2) with an odd number of chiral doublets has Witten's global
anomaly; whether the apex carries an even number is a question for the local model's spectrum (L213 (v)), registered — it is the one
consistency condition the touching design must meet that the geometry alone does not settle.

## 5. What it means

The design of the destination's item 1 is now a single picture with exact local data: the object's own Joyce orbifold (B1357), the
E₆ copy and the SU(2) copy of Y₃ brought to touch at three deck-related points, each with B1355's cone as local model, the three 27s
told apart by the apexes' own U(1)s in sum-zero combination (B1356), the SU(2) copy receiving chiral doublets in the exact ratio of
§4. What is excluded: the apex on the knot (A₅), the SU(3) locus as companion (parity of the companion's order), the self-touching and
the SO(8) touching without extra branches. The three faces: the family is indexed by the finite subgroups of the second Sp(1)
(arithmetic); the companion sits at the antipode, the mixed loci over the cone circles of S⁴/Γ (geometry); the inflow ratios are the
degrees of the pole lines onto their images (quantum).

## 6. Caveats

1. The family is Acharya–Witten's twistor family with Γ ⊂ Sp(1) × Sp(1); Γ ⊂ Sp(2) not of product form, and cones that are not twistor
   cones, are outside this census. The negative for the apex on the knot is within the family.
2. The census is floating-point (tolerance 10⁻⁷) on groups of order ≤ 576; every reported number is an integer count of orbits,
   stabilisers and degrees. The ADE typing of the mixed loci rests on the G₂ argument of §2.
3. The inflow ratio is normalisation-free; the translation to doublet counts uses the standard Dynkin indices and the cited "one 27"
   (B1355 caveat 2); the doublet number itself is not derived.
4. The touching design remains a design (B1357 §5.4).

## 7. Registered

- L213 (v) sharpened: the spectrum of B1355's apex on the SU(2) side — the doublet count per apex (even or odd) decides whether three
  apexes are consistent with Witten's SU(2) anomaly.
- Cones outside the product family (Γ ⊂ Sp(2) irreducible on ℂ⁴) as further apex models.

## Verification

`verification/apex_family.py` (seconds; record `apex_family_run.txt`): the seven groups, the fixed lines with stabilisers, types,
orbits and degrees, the enhanced and isolated points, the summary table with the companion reading and the inflow ratios. Lock:
`tests/test_b1358_the_e6_apex_family.py`.

**Sources.** B1355 (the cone over CP³/2T; Witten's inflow), B1356 (the deck's lift, the two complex structures), B1357 (the background).
Witten, hep-th/0108165 §3; Acharya–Witten, hep-th/0109152 §3.
