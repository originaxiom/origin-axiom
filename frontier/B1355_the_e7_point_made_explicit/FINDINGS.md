# B1355 — THE E₇ POINT MADE EXPLICIT: the destination's local model is the G₂ cone over CP³/2T — the Bryant–Salamon cone over the nearly-Kähler CP³ divided by the object's McKay group acting on one quaternionic factor, the twistor cone of the self-dual Einstein orbifold S⁴/2T. Its E₆ locus (the cone over the fixed twistor line) and an A₁ locus meet only at a curved, non-orbifold apex whose link has b₂ = 1 and whose E₆-locus class pairs non-trivially with the harmonic two-form — exactly the configuration B1353 proved impossible in the flat class, realised in the curved one — and by Witten's inflow the apex must carry chiral E₆-charged matter with U(1) charge: the E₆ analogue of Acharya–Witten's U(N) point. Acharya–Witten's own hyperkähler-U(1) construction stops at A-type (the centraliser of 2T in the triholomorphic Sp(1) is ±1), so the twistor family is the one that reaches E₆. The count "one 27 per point" is the literature's rule (E₇ ⊃ E₆ × U(1)), not re-derived here. 0 of 19; the closing's local geometry named.

**Verdict: PROVED for the geometry (a finite computation and standard facts), CITED for the physics** (the inflow statement is Witten's, transposed with the one change that E₆'s cubic anomaly vanishes and the mixed anomaly does the work; the integer is Acharya–Witten's rule). Depends on B1353 (why the flat class cannot do this), B1268 (E₆ from 2T, the object's McKay group), B1084 (the flat model whose E₆ locus this curves). Verification: `verification/cone_over_cp3_mod_2t.py` (record `cone_over_cp3_mod_2t_run.txt`). Lock: `tests/test_b1355_the_e7_point_made_explicit.py`.

## 0. Seen from above

Every chirality computation since B1268 has been local deformation theory at one point of the object's E₆ character variety
(B1350–B1354) or a census of flat local models (B1084, B1259, B1353); all of it says the cusped object and the flat class carry no
net count. The destination (`docs/THE_DESTINATION_LEDGER_2026-09-06.md`, item 1) needs an E₆ locus with points where the
singularity enhances and one chiral 27 appears — and the literature's rule (B1353 §3) says such a point is an isolated conical
singularity that is not an orbifold, with an ADE locus through it that cannot be slipped away. The question this arc asks is not
"can the object carry it" but "what is the local geometry", and the answer is in Acharya–Witten's two families of cones, once
one asks which of them reaches E-type.

## 1. Acharya–Witten's two families, and which one reaches E₆

**(A) The hyperkähler-quotient family** (AW §2.2, eqs. (2.4)–(2.7)): X = (ℍ/Z_N × ℍ′)/U(1)′ with Z_N acting on ℍ as
(a, b) ↦ (e^{2πik/N}a, e^{−2πik/N}b) and U(1)′ as (e^{iψ/N}a, e^{−iψ/N}b) — the U(1) *containing* Z_N — giving the cone on
WCP³_{N,N,1,1} with "a family of SU(N) singularities … and an unbroken U(1) carried by the C-field", and "a massless chiral multiplet
in the fundamental representation of U(N)". The construction needs a U(1) acting triholomorphically on ℍ/Γ. For Γ = 2T the
centraliser of 2T in Sp(1) is {±1} (`(v)` of the script: the elements i, j, (1+i+j+k)/2 generate, and only ±1 commutes with all
three; a one-parameter subgroup commuting with i, j, k is trivial), so **no such U(1) exists for E₆ (or for any non-cyclic Γ)**: family
(A) is A-type only.

**(B) The twistor family** (AW §3): the G₂ cone over the twistor space of a self-dual Einstein 4-orbifold M; the orbifold points of M
with SU(2)-type stabilisers Γᵢ give ℝ³-loci of type Γᵢ in the cone, all through the apex ("the cone on SU(3)/U(1)² … gives three
gauge multiplets of chiral fermions"). Take M = S⁴/2T with 2T ⊂ Sp(1)_L acting on ℍP¹ = S⁴ by [q₁ : q₂] ↦ [l q₁ : q₂]: the twistor
space is CP³/2T with CP³ = P(ℂ⁴), ℂ⁴ = ℍ ⊕ ℍ′ in the right complex structure, and 2T acting as diag(g, 1₂), g ∈ 2T ⊂ SU(2). The
Bryant–Salamon cone over the nearly-Kähler CP³ has isometry group Sp(2) ⊃ Sp(1)_L × Sp(1)′_L, so **the cone over CP³/2T is a G₂
cone** (a quotient by structure-preserving isometries), and it is AW's family (B) with M = S⁴/2T.

## 2. The geometry, computed (`cone_over_cp3_mod_2t.py`)

| | 2T | Z_N control (AW's SU(N)), N = 2…6 |
|---|---|---|
| L = P(0 ⊕ ℂ²), the twistor line over the pole [0 : 1] | fixed pointwise by all 24 elements; normal action on ℂ² = 2T ⊂ SU(2) | fixed by all N; normal action Z_N ⊂ SU(2) |
| its cone | **the E₆ locus**, an ℝ³ through the apex | the SU(N) locus |
| L′ = P(ℂ² ⊕ 0), the line over the other pole | fixed pointwise by −1 only; normal weights (−1, −1) | fixed by −1 for even N (an A₁ line), by nothing for odd N |
| its cone | **an A₁ locus** ℝ³/T (T = 2T/±1 acting on L′) through the apex | an A₁ locus (even N) or nothing |
| isolated fixed points on L′ | 14: six with stabiliser Z₄, eight with Z₆ (the octahedron's edge-midpoints and the cube's vertices under T) | two, with stabiliser Z_N |
| their cones | codimension-6 lines (no gauge group; AW: "no known useful description") | the same |
| the link Y = CP³/Γ | b₂(Y; ℚ) = 1 (a linear action fixes the hyperplane class) | 1 |
| the class [U] of the E₆ link L in H₂(Y; ℚ) | the line class, degree 1 against the Kähler form: **∫_U w ≠ 0** | the same |

So the cone over CP³/2T has an E₆ locus and an A₁ locus meeting **only at the apex** (the two lines are disjoint in CP³), the
apex is a conical singularity whose link is not a sphere quotient (CP³/2T, not S⁶/Γ), and there is one U(1) carried by the
C-field. This is the configuration of B1353's Acharya–Witten point with its two obstructions removed: the collision is isolated
because the loci come from different twistor fibres, and b₂(link) = 1 because the link is CP³/Γ.

## 3. The physics, cited and transposed

Witten (hep-th/0108165, §3): "the chiral degrees of freedom at ℝ⁴ × P_α must have a U(1)ᵢ · SU(N)² anomaly (here U(1)ᵢ is the
i-th copy of U(1) in the gauge group, generated by the harmonic form wᵢ) equal to ∫_{U_α} wᵢ" and, for the cone on WCP³_{N,N,1,1},
"The second Betti number of Y is 1, so there is a single U(1) to consider … Such a w has ∫_U w ≠ 0 … So the chiral SU(N) degrees of
freedom found above must be charged under the U(1)." The argument uses only the seven-dimensional coupling ∫_Q C ∧ tr F ∧ F on the
ADE locus Q and the class of its link U in Y; nothing in it is special to SU(N) except that for SU(N) the cubic anomaly also forces
the chiral fields by itself. For E₆ the cubic anomaly vanishes (B1353 §3) and the **mixed U(1) · E₆² anomaly, equal to ∫_U w ≠ 0, does
the forcing**: the apex of the cone over CP³/2T must carry chiral E₆-charged matter with U(1) charge. Which representation and how
many is the literature's rule, not a computation here: in the heterotic dual (AW §2, E₈ ⊃ E₆ × SU(3)′, the (27, 3)) a point where a
weight of the 3 of SU(3)′ has trivial monodromy around all three circles of the T³ fibre carries one chiral 27 — three angles, one per
circle, so the point is isolated in the three-dimensional locus exactly as in AW's SU(5) computation — and the enhancement reading
E₇ ⊃ E₆ × U(1), 56 → 27₁ ⊕ 27̄₋₁ ⊕ 1 ⊕ 1, gives the same: **one chiral 27 per point.**

## 4. What it means for the destination

Item 1 of the destination ledger ("three E₇ points on the E₆ locus, one chiral 27 each") now has a local model with a name: **three
cones over CP³/2T on the E₆ locus of the closing.** The group is the object's own (2T, the McKay group of its E₆, B1268); the E₆
locus is the flat model's ℝ³ (B1084) passing through curved apexes instead of orbifold points; the U(1)s are the C-field's, one per
apex, under which the three 27s are charged (anomaly cancellation by inflow, Witten (3.14): the charges sum to zero over the
apexes of a compact closing, ∑_α ∫_{U_α} w = ∫_{Q′} dw = 0 — so on a compact closing the three points cannot all be charged the same
way under one U(1): the count must be read with the global b₂). What the object has to supply is no longer "a curved closing" in
the abstract but a compact G₂ manifold whose E₆ locus carries three such apexes; the tower's ℤ/3 descent (Y₃) is the first place to
look for the "three", and that is registered (§6).

**The three faces.** Geometric: the twistor cone of S⁴/2T, the two poles giving the E₆ and the A₁ loci. Arithmetic: 2T's centraliser in
Sp(1) is ±1 — the reason AW's U(1) family stops at A-type and the reason the E₆ point needs the twistor family. Quantum: b₂ = 1 and
∫_U w = 1 — the inflow that forces the count, with the mixed anomaly doing for E₆ what the cubic one does for SU(N).

## 5. Caveats

1. The G₂ metric on the cone over CP³/2T is the quotient of the Bryant–Salamon cone metric — explicit, unlike AW's family (A)
   ("we cannot describe it explicitly"); but a *compact* G₂ manifold containing three such apexes on one E₆ locus is not
   constructed here or anywhere I know; AW's existence argument is by heterotic duality, in the large.
2. The count "one 27" is cited (the heterotic-dual computation of AW §2 transposed to E₆ ⊂ E₈ with commutant SU(3)′, and the
   E₇ ⊃ E₆ × U(1) branching); the inflow forces a non-zero mixed anomaly, not the integer.
3. The A₁ locus over the other pole carries an SU(2) gauge group at the apex as well; its effect on the spectrum at the apex
   (bifundamentals of E₆ × SU(2)) is not analysed; a self-dual Einstein orbifold with a single 2T point and no other SU(2)-type
   point would remove it — none is known to me (S⁴/2T's two poles are the minimum for Γ ⊂ Sp(1)_L, and B1353's argument shows a
   larger Γ ⊂ O(4) enlarges the pole stabiliser).
4. The isolated Z₄, Z₆ points give codimension-6 conical lines whose M-theory physics is unknown (AW).

## 6. Registered

- The "three": whether the tower's ℤ/3 descent (Y₃, B1301/B1303) can place three CP³/2T apexes on the closing's E₆ locus; the
  global b₂ and the charge sum rule (3.14). **The sum rule already constrains the design:** ∑_α ∫_{U_α} wᵢ = 0 for every harmonic
  two-form of the compact closing, so with b₂ = 1 the three 27s carry U(1) charges summing to zero (a 2 + 1 structure, e.g.
  (1, 1, −2)), and a ℤ/3 that permutes the apexes and fixes w gives equal charges 3q = 0 and no inflow — a ℤ/3-symmetric triple
  needs b₂ ≥ 2 with the ℤ/3 moving the harmonic forms (H-SUMRULE-TWO-PLUS-ONE, `docs/HINT_LEDGER.md` (16)).
- The E₆ × SU(2) spectrum at the apex from the A₁ locus over the second pole.
- A self-dual Einstein orbifold with exactly one 2T point.
