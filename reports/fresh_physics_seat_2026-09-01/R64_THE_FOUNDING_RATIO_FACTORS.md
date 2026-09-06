# R64 — THE FOUNDING RATIO FACTORS: on the golden E₈ the object's order-3 element is the family rotation TIMES an E₆ Weyl element — B1275's open step, answered by a type computation

**Seat:** fresh physics seat (fc) · **Date:** 2026-09-06 · **Against main @ 87a2eb3d and the SM-derivation branch's B1270** · **Status:** seat report, not banked. Exact over ℚ(√5); script `computations/r64_founding_ratio_type.py`, which rebuilds the icosian E₈ from scratch (nothing imported from either branch) and reproduces B1270's numbers as its control.

## 0. The question and the answer

B1275 verified the E₈ ⊃ E₆ × A₂ family mechanism and isolated the one object-specific step: *"that the object's own order-3 element is this A₂ rotation"* — where B1270 (SM-derivation branch) realises the founding ratio g = −RL⁻¹ as an order-3 unit icosian acting on E₈ by left multiplication, and E₆ as ℤ[g]^⊥.

Order-3 automorphisms of the E₈ lattice have a **type**: the dimension of their fixed subspace. Computed on the rebuilt lattice:

| automorphism | order | fixed dim | acts on E₆ roots | acts on the six 27-classes |
|---|---|---|---|---|
| **L_g** (left multiplication by g) | 3 | **0** | 24 three-cycles, no fixed root | cycles them in two 3-orbits |
| **w_{A₂} = s₁ s_g** (the family Weyl rotation of the plane {1, g}) | 3 | **6** | **fixes all 72** | cycles them in two 3-orbits |
| **w₃ := w_{A₂}⁻¹ L_g** | 3 | **2** (the plane {1,g}) | 24 three-cycles, no fixed root | **preserves every class**; 9 three-cycles inside each 27 |

with **L_g = w_{A₂} · w₃ and [w_{A₂}, w₃] = 0.**

> **The object's order-3 element is not the A₂ family rotation. It is the family rotation times an order-3 Weyl element of E₆ that fixes no vector of E₆.** As lattice automorphisms they are distinguished by type (fixed dimension 0 versus 6). As a statement about the three 27's they agree: both cycle the three classes in the same two orbits. The difference, w₃, lives inside E₆ — it is an element of W(E₆), hence realised by an inner element of E₆, i.e. **a gauge transformation** — and acts within each 27 by cycling its 27 weights in nine triples, the trinification-class element.

So B1275's step is **false literally and true up to E₆-gauge**: the object's g acts on the three generations as the family rotation composed with an E₆ gauge transformation. Which reading the record wants is a choice of what "is" means, and it should be recorded as such rather than left as a yes/no.

## 1. What this explains in the record

- **B1264's "L3 and L4 act by the same ω":** they are the two factors of one element. w₃ (inside E₆, fixed-point-free on the E₆ 6-space, nine triples on each 27) is the trinification-type ℤ/3; w_{A₂} (on the Eisenstein plane) is the commensurator/family ℤ/3. g supplies both at once, which is why they share ω.
- **B1271's "three copies of the 27 permuted by the object's own order-3 element":** correct for the family factor; the same element also acts inside each copy. For a pure generation permutation one quotients by the E₆ factor — legitimate, since it is gauge.
- **The mirror:** L_g maps the (27,3) orbit to itself and the (27̄,3̄) orbit to itself (computed: two 3-orbits). The bit that chooses matter versus mirror-matter is untouched by g; the count on the object stays N = 0 (B1268, B1270, R56, R61). This report changes the *type* of the family element, not the count.

## 2. Controls (this bench, exact)

- 2I rebuilt: 120 units, closed, element orders 1¹ 2¹ 3²⁰ 4³⁰ 5²⁴ 6²⁰ 10²⁴ (B1270's census reproduced).
- E₈: 240 vectors of Euclidean norm 1 (units and φ⁻¹·units), ℤ-rank 8, Gram determinant 1 in the norm-2 scaling.
- The 20 order-3 units form **one** conjugacy class, so the choice of g does not matter.
- Plane {1,g} has the A₂ Gram; its orthogonal complement contains exactly **72** roots; the remaining 162 split **6 × 27** by their pairings (B1270's theorem reproduced without its code).
- Orders and fixed dimensions computed as integer-matrix ranks in a ℤ-basis of the lattice; commutation checked as matrices; w_{A₂} checked to fix each of the 72 E₆ roots individually; w₃ checked to fix 1 and g and to preserve each of the twelve pairing classes.
- Incidental, not headlined: g = −RL⁻¹ and M² = [[2,1],[1,1]] both reduce to [[0,1],[1,1]] in SL(2,𝔽₂), the same 3-cycle on the fiber's half-periods (B366's puncture lemma). SL(2,𝔽₂) has only two elements of order 3, so this is weak evidence of anything.

## 3. What remains open, precisely

- Whether B1264's 85 grading operators (torus-type, eigenvalues 1, ω, ω² on a 27) include the lift of *this* w₃, i.e. whether g selects one of the 85 (a further H5 collapse) — not computed; it needs a lift of w₃ to E₆(ℂ) and B1264's list.
- The physical transport (B1269/B1270's Acharya–Witten with the golden E₈ along Q) and its count are unchanged by this report.

*Swept: B1275 states the step unverified; B1270 computes that L_g cycles the classes but not its type or factorization; "fixed dimension" / "w₃" / the factorization appear in neither branch.*
