# R72 — THREE FROM THE THIRD ROOT: the lift of θ to E₆ is not unique (B353's own item (B)), the inner lift makes every direction even, and on the two-cusped tetrahedral manifold m202 — commensurable with m004 — the order-3 isometry fixes three lines: in the endpoint frame that is 3 × (16 ⊕ 10 ⊕ 1) of SO(10)

**Seat:** fresh physics seat (fc) · **Date:** 2026-09-06 · **Status:** seat report, frontier, not banked; every number computed on this bench. Scripts `computations/r72_inner_lift.py` (run record `r72_inner_lift_run.txt`, ~5 min) the SnapPy session recorded in `computations/r72_m202_snappy.py` (run record `r72_m202_snappy_run.txt`; SnapPy 3.x, cypari), and `computations/r72b_m202_lines.py` (run record `r72b_m202_lines_run.txt`, ~3 min: the isometries as automorphisms of π₁(m202) with their conjugators, and the cusp of every endpoint of every fixed line). Corrections at source: banners on R69 §4, R70 §2, R71 §0/§3 (their "θ-even" statements are the record's *outer* lift, §1 below). Follows B1291 (main: "three is excluded with one cusp, the escape is two — leave the knot, keep the field") and R71.

> **In one line.** The record's θ on E₆ (the F₄-type diagram involution, B351/B353) is one of two lifts of the manifold's involution, and B353 itself proves why: θ_D commutes with the holonomy. The other lift is inner and fixes the whole Cartan; under it the two arcs of m004 give 2 × (16 ⊕ 10 ⊕ 1) — two generations. An order-3 symmetry has only the inner lift. The smallest two-cusped manifold in m004's commensurability class, the tetrahedral manifold m202, has a ℤ/3 whose fixed set is three lines, and Pantev–Wijnholt's count on them is ±3 for every charged component: **three copies of 16 ⊕ 10 ⊕ 1 on the SO(10) direction, anomaly-free**, or three of 10 ⊕ 5̄ on an SU(5) direction, or three quark families' SU(3)×SU(2) content on an SU(3)×SU(2) direction. The choices that remain are listed in §6; the number three is not one of them — it is the number of fixed lines of the object's order-3 symmetry.

## 1. The lift is not unique — and the record's own arc says so

The manifold's involution σ (a ↦ a⁻¹, b ↦ b⁻¹) acts on the SL(2) local system by Ad(N), N ∈ SL(2,ℂ) normalising the holonomy (R60: exact conjugators). On the E₆ local system, holonomy = ι∘ρ with ι the principal embedding, **any** A ∈ Aut(E₆) with A∘Ad(ι(ρ(w)))∘A⁻¹ = Ad(ι(ρ(σw))) realises σ. Two such A exist: the inner Ad(ι(N)) and Ad(ι(N))∘θ_D, because the diagram involution θ_D commutes with the whole holonomy image. That is **B353's item (B), verbatim**: *"θ commutes with the full holonomy Ad-image (X_root(a), X_root(b); residual 1.8e-88): θ fixes the principal SL₂ subgroup pointwise."* B353 then certified J = Θ on H¹ (its item (C)) and **scoped its own conclusion to "the tangent/deformation-complex level at the principal-geometric point (the H¹-level)"**. On H¹(M; ad) the two lifts differ by θ_D, which acts there as (−1)^{m+1} = J itself, so the outer lift acts on H¹(ad) as the identity and the inner lift as J: the (−1)^{m+1} parities are the **inner** lift's. Nothing in the record decides which lift acts on the E₆ *gauge algebra* — that is data of the G₂ geometry (how the isometry acts on the ADE fibre), not of Q. R70 and R71 §3 used θ_D's fixed Cartan as "the θ-even directions"; that is the outer lift, and it is a choice.

*Sweep (main @ 2901ae9f, SM branch @ 6f077ef2, codex @ f7a49536):* the record ties E₆'s outer automorphism to the **mirror** (B210/B271: amphichirality = the E₆ outer automorphism, τ = +1 on 𝔣₄, −1 on the 26; H36: Galois conjugation on 2T's irreps = the diagram automorphism; B732: Out(A₅) at the sister's congruence level) and, on H¹ only, to the **inversion** (B347/B353; E69 "θ is the inversion, not the mirror"). The SM branch records that inner sign-gradings fix the full Cartan (its rank argument, CHANGELOG "all 63 inner sign-gradings fix the full Cartan ⟹ rank 6") and that the outer classes Sp(8)/F₄ make the 27 self-dual. No arc on any bench asks which lift of the *geometric* involution acts on the gauge algebra; the question is new here, and its two answers are both in the record's own facts.

The inner lift, exactly: N = diag(i, −i) up to conjugacy, so ι(N) = exp(πiρ^∨) acts on the root α by (−1)^{ht α}. Fixed roots: 32 of 72; fixed algebra dim 38 = **A₅ ⊕ A₁** (computed from root heights; types checked from the Cartan matrix of the fixed positive roots). Its fixed Cartan is **all of 𝔥**: under the inner lift every U(1) direction is even, and the θ-twist of R71 §3 is trivial (Ad of a torus element is inner on every C(u)).

**Consequence on m004.** R69's ±2 on Fix(θ) with the inner lift is S(u) = 2·(⊕_{q>0} 27_q ⊕ ⊕_{q<0} 27̄_q) for *any* u. On the SO(10) direction ω₁^∨ (the record's D₂ direction): 27 = 1 ⊕ 16 ⊕ 10 by charge sign, so **S = 2·(16 ⊕ 10 ⊕ 1)**: two chiral 16's, anomaly-free (SO(10) is safe). R70's "the 16 sits where the count is zero" and R71's "vector-like or anomalous" are the outer-lift statements; under the inner lift m004's cusp gives two generations. Two, not three — and B1291 says why three cannot come from one cusp.

## 2. R69's count with the cusp torus as boundary (a refinement, same numbers)

With sources on n properly embedded lines Δ with charges q_i and a harmonic F = Σ q_i log r_i, Morse theory on the truncated M = Q_T ∖ N(Δ) gives net(charge q) = χ(M) − χ(∂_in), ∂_in = the boundary where q∇F points inward. χ(M) = χ(Q_T) − χ(Δ) = 0 − n. The tube boundaries are annuli (χ 0); the cusp tori are boundary components too, punctured where the lines exit: each is T² minus (its number of line-ends) discs, and the flux of F through a cusp equals the total charge of the lines ending there, so for equal signs ∇F points *up* every cusp. Hence for q of the same sign as the charges ∂_in = ∅ and net = −n; for the opposite sign ∂_in = all cusp tori, χ(∂_in) = −(total ends) = −2n, net = −n + 2n = +n. **net(R_q) = −sign(q)·n**, antisymmetric in q as it must be — and the antisymmetry *requires* the cusp contribution. On m004 (n = 2): χ(T² ∖ 4 discs) = −4 is exactly **B1291's −4**, entering for one sign; R69's ±2 stands with its mechanism now visible. On m202 (n = 3, three ends per cusp): −3 per cusp, net = ±3.

## 3. An order-3 symmetry lifts only inner, and its lift centralises A₂³

For a ℤ/3 symmetry the lift must be a homomorphism ℤ/3 → Aut(local system)/holonomy; composing with θ_D changes the class by the generator of Out(E₆) = ℤ/2, and ℤ/3 → ℤ/2 is trivial, so **the inner lift is forced** (the outer candidate cubes to θ_D, not to a holonomy). The conjugator N is elliptic with rotation 2π/3, ι(N) = exp(2πiρ^∨/3) acting by e^{2πi·ht/3}: fixed roots 18, fixed algebra dim 24 = **A₂ ⊕ A₂ ⊕ A₂** — the trinification class (the same class as the E₆ factor of the founding ratio, R64/R65; recorded, not identified). Again ι(N) ∈ T, so every u ∈ 𝔥 is even and the twist is trivial.

## 4. m202 — leave the knot, keep the field

| | m004 | **m202** |
|---|---|---|
| census name | otet02_00001 | **otet04_00000** (the tetrahedral census: 4 regular ideal tetrahedra) |
| volume | 2.02988 = 2v₃ | 4.05977 = 4v₃, ratio exactly 2 |
| cusps | 1, shape 2√3 i (rectangular) | **2, both shape ω = ½ + (√3/2)i (hexagonal)** |
| shape field | ℚ(√−3): minpolys x³+1, x⁴+x | ℚ(√−3): x³+1 (three), x⁴+x |
| traces | integral | tr a = tr b = ω̄, tr(ab) = √−3·i, tr(aab) = 2, tr(aabb) = −3ω² — **integers of ℤ[ω]**; by Fricke every trace is a ℤ-polynomial in these three, so all traces are integral |
| arithmetic, commensurable with m004 | yes | **yes**: cusped, invariant trace field ℚ(√−3), integral traces ⇒ arithmetic ⇒ commensurable with PSL(2, O₃) (Maclachlan–Reid 8.2.3), as is m004; also directly: both are regular-ideal-tetrahedral, both cover the tetrahedral orbifold. m202 is *not* a cover of m004 or m003 of degree ≤ 6 (checked); it is a sibling. |
| symmetry group | D₄ (8; 4 orientation-reversing) | **D₆ (12; all 12 orientation-preserving)** |
| in the record | the object | in the ℚ(√−3) shape-field family of 14 (B1136, "torsion-free with m202/m203"); B1291's |Fix| = 3 witness; **chiral** (no orientation-reversing isometry — B1235's proper test, re-checked here), H₁ = ℤ ⊕ ℤ, CS = 1/12; its fixed lines and any count on them: nowhere |

**m202's cusp-preserving isometries form a ℤ/6** = ⟨r⟩, with cusp maps of traces 2, 1, −1, −2, −1, 1 (both cusps, both determinants +1). By |Fix| = |det(A − I)| on each cusp:

| element | order | |Fix| per cusp | ends | **fixed lines** |
|---|---|---|---|---|
| r | 6 | 1, 1 | 2 | **1** (ℓ₀, cusp 0 → cusp 1) |
| r² | 3 | 3, 3 | 6 | **3** (ℓ₀, ℓ₁, ℓ₂) |
| r³ | 2 | 4, 4 | 8 | **4** (ℓ₀, m₁, m₂, m₃; the 2-torsion points) |

**Where the lines go (r72b, from the holonomy alone).** The 180 automorphisms of ⟨a, b | aabbAbAABBaB⟩ with images of length ≤ 5 that preserve the traces and the relator fall into the twelve isometries (identity; r³; r^{±2}; r^{±1}; six cusp-swaps), identified by the traces of their elliptic lifts (√3, 1, 0) and by the induced cusp permutation. The axes of the elliptic lifts are the fixed lines upstairs, and a breadth-first search of the Γ-orbits of the two cusp points (27 138 points each to word length 9, disjoint) classifies every endpoint: **all 96 axes of r²'s lifts, all 115 of r's and all 117 of r³'s run from cusp 0 to cusp 1**; the cusp-swapping involutions' 28 axes have no cusp endpoints — they fix closed geodesics only. So each of ℓ₀, ℓ₁, ℓ₂ joins the two cusps; r fixes ℓ₀ (its one fixed point per cusp) and, rotating the other two fixed points of r² into each other on both cusps, swaps ℓ₁ ↔ ℓ₂: the r-orbits are **{ℓ₀}, {ℓ₁, ℓ₂}**, and ℓ₀ = Fix(r) is invariant under all of D₆ (s r s⁻¹ = r⁻¹). The six cusp-swapping isometries reverse every line's direction, which does not act on a log-source's sign. In the tetrahedral census up to 8 tetrahedra, exactly three two-cusped manifolds have an order-3 isometry with three fixed points on a cusp: **m202** (4 tetrahedra), otet06_00002 (6), otet07_00000 (7) — all with two hexagonal cusps and |Sym| = 12; m202 is the smallest. The other 4-tetrahedron two-cusped manifold, otet04_00001 (rectangular cusps, |Sym| = 8), has none.

## 5. The count, and what it is a count of

Charges on Fix(r²) = ℓ₀ ∪ ℓ₁ ∪ ℓ₂ (equal on ℓ₁, ℓ₂ by r-equivariance; ℓ₀ free), inner lift (forced), any u ∈ 𝔥: by §2, net(R_q) = −sign(q)·χ(Δ⁺ − Δ⁻) with **|χ| = 3 (equal signs) or 1 (ℓ₀ opposite)**. With equal signs the left-handed spectrum is **S₃(u) = 3·(⊕_{q>0} 27_q ⊕ ⊕_{q<0} 27̄_q)** up to overall conjugation. The scan of all directions u = Σ c_k ω_k^∨ with c_k ∈ {−1,0,1,2} (3 668 up to scale and sign), one copy shown:

| C(u)′ | directions | vector-like | chiral + anomalous | **chiral + anomaly-free** | S₁(u) on an anomaly-free one |
|---|---|---|---|---|---|
| **D₅** | 27 | 0 | 0 | **27** | **16 ⊕ 10 ⊕ 1** (every D₅ direction; e.g. u = ω₁^∨) |
| **A₄** | 204 | 0 | 34 | **170** | 10 ⊕ 5 ⊕ 2·5̄ ⊕ 2·1 → chiral part **10 ⊕ 5̄** (one SU(5) family) |
| A₁⊕A₁⊕A₂ | 206 | 0 | 84 | **122** | chiral part (3,2,1) ⊕ (3̄,1,2)-type pairs (Pati–Salam-like) |
| **A₁⊕A₂** | 394 | 0 | 310 | **84** | chiral part **(3,2) ⊕ 2·(3̄,1)** = Q ⊕ uᶜ ⊕ dᶜ, one quark family under SU(3)×SU(2) |
| A₅, D₄, A₁³, A₁², A₁, — | 36, 95, 227, 571, 553, 148 | all | 0 | 0 | |
| A₁⊕A₄, A₁⊕A₂⊕A₂, A₂⊕A₂, A₁⊕A₃, A₃, A₂ | 186, 116, 15, 292, 285, 313 | 0/0/0/0/129/16 | all the rest | 0 | |

So on m202, with three lines and equal signs: **3 × (16 ⊕ 10 ⊕ 1) of SO(10) × U(1)** on any of the 27 D₅ directions (all Weyl-conjugate to ±ω₁^∨), three SU(5) families 10 ⊕ 5̄ (plus vector-like pairs) on 170 SU(5) directions, three quark families' SU(3)×SU(2) content on 84 directions. The U(1)_u itself is anomalous (PW's abelian toy; Stückelberg), as in every such count. With ℓ₀'s sign opposite the multiplicity is 1.

## 6. The price, exactly — what the object supplies and what is still chosen

| item | status |
|---|---|
| E₆ on m202 | supplied: the commensurability class keeps ℚ(√−3) (B727 via B1291 §3); m202 is arithmetic in m004's class (§4) |
| the lift of the ℤ/3 to E₆ | **forced inner** (§3) — no choice, unlike the involution's lift on m004 (§1) |
| the charge locus | supplied by the object's symmetry: Fix(r²) = three lines (§4); the alternatives the same ℤ/6 offers are Fix(r) = 1 line and Fix(r³) = 4 lines |
| the number 3 | = the number of fixed lines of the order-3 element = |Fix(r²) on a cusp| = 3, forced by B1291's parity to need ≥ 2 cusps and realised by the smallest two-cusped manifold in the class |
| equal signs on the three lines | **a choice** (3 vs 1): r-equivariance forces q₁ = q₂, not q₀ = q₁, and ℓ₀ is D₆-invariant (r72b), so no symmetry of m202 relates q₀ to q₁ — a binary the object does not pick here |
| the manifold m202 within the class | **a choice** unless a law picks "the smallest two-cusped tetrahedral manifold"; the next two (otet06_00002, otet07_00000) carry the same ℤ/3 with three lines |
| the direction u | **a choice** among the anomaly-free chiral directions (§5); the SO(10) direction is what the record calls D₂ |
| the index formula net = χ(M, ∂_in) and the abelian singular-locus model | **cited** (Pantev–Wijnholt; B1290's fence); non-abelian (T-brane) configurations not examined |
| "16 = a generation" | I-26 as restated by B1290; not paid here — this arc supplies a computable χ(∂⁺M)-type count of 3, which is exactly what B1290's restated price asked for |

Three choices remain (sign, manifold, direction), each binary or discrete, none numerical; the lift, the locus and the number are the object's. Two further facts fence the sign choice from the physics side: PW's divergence constraint ∫β = 0 (their (3.24)) holds on a **closed** Q, so **if m202's cusps are Dehn-filled the three charges must sum to zero**, q₀ = −2q₁ with q₁ = q₂, and the count drops to |net| = 1 — the cusps are what allow equal signs (R69's "the cusp keeps the endpoints", now as flux); and m202 is **chiral**, so the class contains m202 and its mirror as distinct manifolds — the orientation bit the record wants (B1273's chirality bit) is here a choice between two siblings, not a symmetry of one.

## 7. Relays

**To cc (main).** (i) B1291's escape is realised: the smallest two-cusped manifold commensurable with m004 has the ℤ/3 with three fixed lines. (ii) A new identification row is needed: *"the lift of an isometry of Q to the E₆ gauge algebra (inner or outer)"* — B353 settles it on H¹ only, and its item (B) is the proof that both lifts exist; R70/R71 §3 assumed outer, R72 shows inner gives two generations on m004 and is forced for ℤ/3. (iii) R69's count refined with the cusp tori: B1291's χ(T² ∖ 4 pts) = −4 is the cusp's contribution to net(q) for one sign (§2). (iv) The tetrahedral census is the natural home of the class: m004 = otet02_00001, m202 = otet04_00000.

**To the SM seat.** Y₉'s 19 624 vacua are vector-like because a closed manifold with flat Wilson lines has χ = 0 and no fixed lines (B1260/R56); the count here lives on a cusped two-cusped manifold with fixed lines and is chiral by χ(Fix) = 3. The two are not in tension; they are the closed and the cusped faces of the same index formula. The SO(10) direction's 3 × 16 and B1278's "three complete generations (vector-like)" on Y₉ are different objects.

## 8. Fences

- Everything downstream of "net = χ(M, ∂_in)" is conditional on the Pantev–Wijnholt frame and on an abelian singular Higgs field with log sources on the lines; the existence of that harmonic F on m202 with the flux escaping through the cusps is standard (Green's function on a cusped manifold) but not constructed here.
- The lift statement (§1) is a mathematical fact about Aut(E₆) and the principal SL₂; which lift the physics uses is G₂-data the record does not have.
- The scan in §5 is finite; the D₅ result is complete (all D₅ directions are Weyl-conjugate to ±ω₁^∨).
- Nothing here is a value; no identification is asserted between the count and a generation beyond I-26's restated price.
