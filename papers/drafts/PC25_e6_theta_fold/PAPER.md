# The Amphichiral Fold: E₆ → F₄ on the Figure-Eight Character Variety, and Why It Stops There

**Author:** originaxiom

**Status:** draft (PC25). Target: *Letters in Mathematical Physics* (letter format); alternative: *Communications in Mathematical Physics* (letter-length submission).

---

## Abstract

Let ρ₀ be the discrete-faithful holonomy of the figure-eight knot complement and ρ its composition with the principal homomorphism SL(2,ℂ) → E₆(ℂ). The Zariski tangent to the E₆(ℂ)-character variety at ρ decomposes as six lines, one per E₆ exponent m ∈ {1,4,5,7,8,11} — the dimension count is a known consequence of twisted-cohomology theory for cusped hyperbolic 3-manifolds, and we claim no novelty for it. Our contributions are three. **First**, the knot's own orientation-preserving (hyperelliptic) involution acts on these six lines by the exponent parity (−1)^{m+1}, and this action is gauge-certifiably *equal* to the E₆ diagram involution θ on the deformation complex: the fixed sector is exactly the F₄ exponents {1,5,7,11}, so the E₆ → F₄ folding is forced by the knot's symmetry. **Second**, the fold terminates at F₄: five candidate mechanisms for a further symmetry-selected reduction — an Eisenstein ℤ/3, the golden Galois ℤ/2, the tangent grading itself, the cusp boundary condition, and the recently proposed nested-Jordan-algebra route — are each closed by explicit computation. **Third**, and structurally deepest, the geometric holonomy lands in F₄(ℂ) ⊂ E₆(ℂ) *in no real form*: the adjoint traces are exactly non-real in ℚ(√−3), and the regular-unipotent meridian independently excludes the compact forms. Consequently the Todorov–Dubois-Violette/Krasnov identification of the Standard-Model algebra inside compact F₄ transfers to this geometry only after complexification: compactness is precisely the structure the hyperbolic geometry does not supply. We state all results with explicit status labels (proved / computed-with-precision / cited / conjectural) and record the negatives plainly.

---

## 1. Introduction

The figure-eight knot 4₁ is the simplest hyperbolic knot: amphichiral, fibred over the circle with once-punctured-torus fibre, with trace field ℚ(√−3) and isometry group of order 8. Its SL(2,ℂ)-character variety is classical; its SL(3,ℂ)-character variety was determined by Heusener–Muñoz–Porti [HMP]. Higher-rank and exceptional targets are largely unexplored terrain, although the *dimension* theory of the relevant twisted cohomology is well understood: for a finite-volume cusped hyperbolic 3-manifold, the twisted-cohomology results of Menal-Ferrer–Porti [MFP] and the character-variety dimension framework of Falbel–Guilloux [FG] govern the tangent spaces of character varieties along the principal (Sym^{2m}-decomposed) composition of the geometric representation.

This letter studies the E₆(ℂ)-character variety of 4₁ at the principal-composed geometric representation and asks a sharply bounded question:

> *What part of the exceptional structure is forced by the knot itself, and where does the forcing stop?*

The answer has three layers.

**1. The fold is forced** (Theorem 1). The knot's orientation-preserving elementary symmetry — the hyperelliptic involution of the once-punctured-torus fibre, a → a⁻¹, b → b⁻¹ — acts on the six tangent lines by (−1)^{m+1} and is identified, at the operator level on the deformation complex, with the E₆ diagram involution θ. Its fixed sector is spanned by the lines at exponents {1,5,7,11} — exactly the F₄ exponents. The E₆ → F₄ folding is thus not a choice of subalgebra but a consequence of the knot's ℤ/2 symmetry.

**2. The fold terminates** (Theorem 2). One might hope the object supplies a *second* selector continuing F₄ to one of its maximal-rank subalgebras. Five concrete routes have been proposed, and each is closed by computation: the figure-eight's arithmetic at its hyperbolic point is Klein-four (ℤ/2 × ℤ/2), not ℤ/3; the golden conjugation acts on a different face of the object; the tangent grading is uniform and non-selecting; the cusp boundary condition is uniform across all six exponents and the centralizer at the cusp-constrained point is zero; and the object selects no structure in the octonion arithmetic that the fifth (nested-Jordan) route requires.

**3. The real form is absent** (Theorem 3). The recent literature identifies the Standard-Model gauge algebra canonically inside *compact* F₄ and E₆ (Todorov–Dubois-Violette [TDV], Krasnov [K], Boyle [B], Baez–Schwahn [BS]). The geometric holonomy, however, generates a subgroup of F₄(ℂ) ⊂ E₆(ℂ) lying in *no* real form of either group: its adjoint traces are exact non-real elements of ℚ(√−3), and its meridian is regular unipotent, which independently excludes the compact forms. The compact-real-form hypothesis on which the Jordan-algebraic Standard-Model identifications rest is therefore exactly the structure the hyperbolic geometry fails to provide. The identification transfers only at the complexified level.

We regard the terminus and the missing real form as the honest content of the paper: a precise statement of what a hyperbolic knot's exceptional character variety does and does not determine. No physical claim is made; a firewalled structural remark (§7) records two suggestive exact matches for future work.

### 1.1 Status conventions

Every claim below carries one of four labels:

- **[PROVED]** — exact or symbolic: integer/rational/algebraic-number arithmetic, Smith normal forms, exact Gauss elimination, finite group theory. Computer-assisted exact computation is included in this tier.
- **[COMPUTED]** — numerical, with working precision and residuals stated (mpmath at 60–100 decimal digits; residuals at the precision floor of each object). However small the residuals, these are not symbolic proofs and are labelled accordingly.
- **[CITED]** — literature, not re-derived here.
- **[CONJECTURE]** — flagged open.

### 1.2 A calibration from the literature, stated up front

A group-level match to the Standard-Model gauge group is *cheap*: at least three independent mechanisms in the literature (ADE-singularity/McKay engineering, the noncommutative-geometry spectral triple, and the Jordan-algebra stabilizer chain) all land on SU(3)×SU(2)×U(1), so producing the group clears no evidential bar. The one falsifiable value-level prediction ever made along the noncommutative route (a Higgs mass prediction) failed and was subsequently patched [CCM]. This letter is calibrated accordingly: it proves *structural* theorems about one knot and one fold, records the negatives, and claims no physics.

---

## 2. Setup

### 2.1 The object

Let M = S³ \ 4₁ with the SnapPy census presentation

  π₁(M) = ⟨a, b | a b³ a b⁻¹ a⁻² b⁻¹⟩,

the relator verified against the hard-coded geometric representation to ~10⁻⁷⁰. Let ρ₀ : π₁(M) → SL(2,ℂ) be the discrete-faithful (geometric) holonomy, and let

  ρ = ι ∘ ρ₀ : π₁(M) → E₆(ℂ),

where ι is the principal homomorphism SL(2) → E₆ in the sense of Kostant [Ko]. The E₆ adjoint decomposes under the principal 𝔰𝔩₂ as

  𝔢₆ = ⊕_{m ∈ {1,4,5,7,8,11}} Sym^{2m}(ℂ²),  dims 3 + 9 + 11 + 15 + 17 + 23 = 78.  **[CITED]** (Kostant; the exponents of E₆.)

Hence the Zariski tangent to the E₆(ℂ)-character variety at ρ is the block sum of twisted cohomologies

  H¹(π₁(M), 𝔢₆) = ⊕_m H¹(M, Sym^{2m}).

### 2.2 The tangent dimensions (not ours)

**Proposition 0 (tangent dimension).** *dim H¹(M, Sym^{2m}) = 1 for every E₆ exponent m; hence*

  *dim H¹(π₁(M), 𝔢₆) = 6 = rank E₆,*

*one line per exponent.*

*Status:* **[CITED]** as a theorem — the twisted-cohomology dimension theory of [MFP] and the framework of [FG] govern exactly this situation, and we claim **no novelty** for the existence or dimension statement. Independently **[COMPUTED]**: Fox calculus on the census presentation at high precision reproduces each dimension unambiguously, with singular-value rank gaps of 10⁸⁵–10¹¹⁹ per block, and with the 𝔰𝔩₂ anchor dim H¹(M, Sym²) = 1 recovered exactly as required by the A-polynomial curve.

### 2.3 The two involutions

Two elementary symmetries of 4₁ act on this tangent space.

- **σ₋ (amphichirality, orientation-reversing):** a → abab a⁻¹b⁻¹, b → bab⁻¹a⁻¹, verified ρ∘σ₋ = D ρ̄ D⁻¹. It acts on each of the six lines as a real structure J with J² = +1, *uniformly* — it does not select among exponents. **[COMPUTED]** (eigenvalue imaginary parts down to 10⁻⁵⁵; cocycle residuals 10⁻⁴⁰–10⁻⁸⁸.) This uniformity is itself load-bearing below (Theorem 2(iii)).
- **σ (the hyperelliptic involution, orientation-preserving):** a → a⁻¹, b → b⁻¹, with σ² = id exactly. It is ℂ-linear on the tangent space and is the subject of Theorem 1.

---

## 3. Theorem 1 — the amphichiral fold E₆ → F₄

### 3.1 Statement

**Theorem 1.** *Let θ be the E₆ diagram involution, acting on the principal-composed tangent space.*

*(a)* **[PROVED]** *θ acts on the exponent-m tangent line by (−1)^{m+1}. The (+1)-eigenspace is spanned by the lines at exponents {1,5,7,11} — exactly the exponents of F₄ — and the (−1)-eigenspace by the lines at {4,8}, matching the 26-dimensional coset 𝔢₆/𝔣₄. (θ is realised exactly, with matrix entries in {0, ±1} in the root basis; the eigenvalue on each exponent line is exact; the identity {θ-even E₆ exponents} = {F₄ exponents} is elementary.)*

*(b)* **[COMPUTED]** *(mpmath, 100 decimal digits)* *The hyperelliptic involution σ induces* **exactly θ** *on the tangent space — as operators on the deformation complex, not merely as matching sign patterns. Specifically:*

  *(i) transporting the exact θ from the root basis through the module intertwiner into the chain/Sym-representation basis yields the block-scalar operator ⊕_m (−1)^{m+1} Id_{2m+1} as a full 78×78 matrix identity, maximal residual 7.1×10⁻¹⁰²;*

  *(ii) θ commutes with the full holonomy Ad-image (residual 1.8×10⁻⁸⁸); since θ fixes the principal SL₂ subgroup pointwise, the σ-twisted and θ-twisted Fox complexes are the same complex and Θ(z) = θ∘z is a chain map;*

  *(iii) for every exponent m ∈ {1,4,5,7,8,11}, the hyperelliptic cocycle action satisfies J(z₀) = (−1)^{m+1} z₀ + d⁰(v) with an explicit coboundary v — gauge-certificate residuals 9.9×10⁻⁷² to 3.6×10⁻⁷⁹, eigenvalues exactly (−1)^{m+1} with imaginary parts ≤ 10⁻⁶⁵.*

*Consequently the manifold's own ℤ/2 symmetry realises the E₆ → F₄ folding on the deformation space of its character variety: the F₄ sector is the σ-fixed sector.*

### 3.2 The grading table

| exponent m | 1 | 4 | 5 | 7 | 8 | 11 |
|---|---|---|---|---|---|---|
| block Sym^{2m}, dim 2m+1 | 3 | 9 | 11 | 15 | 17 | 23 |
| hyperelliptic / θ sign (−1)^{m+1} | + | − | + | + | − | + |
| sector | F₄ | 𝔢₆/𝔣₄ | F₄ | F₄ | 𝔢₆/𝔣₄ | F₄ |

The θ-even exponents {1,5,7,11} are exactly the integers in [1,11] coprime to 6; they are the F₄ exponents, and (rank of the fixed sector) = 4.

### 3.3 Remarks

1. By Schur's lemma the block-scalar form of θ is forced once θ commutes with the principal 𝔰𝔩₂ (each Sym^{2m} occurs with multiplicity one); the computation verifies the full matrix identity rather than inferring it from Schur.
2. The (−1)-eigenspace {4,8} is the sector previously shown to generate all of 𝔢₆ under bracketing (the E₆-Zariski-dense "escape" directions). The fold thus gives a symmetry origin for the escape/trapped split of the deformation directions.
3. The identification is established at the tangent/deformation-complex level at the principal-geometric point, with explicit gauge certificates. The global, variety-level statement (σ* = θ* as automorphisms of the whole E₆-character variety away from this point) is the natural conjectural frame and is **[CONJECTURE]** — untested. Higher-order (cup-product/Massey) integrability of the θ-odd directions is likewise open.

---

## 4. Theorem 2 — the terminus: five selector routes closed

### 4.1 What a continuation would require

By Borel–de Siebenthal **[CITED]** [BdS], applied to the extended Dynkin diagram of F₄ (marks 1,2,3,4,2), the maximal-rank proper subalgebras of 𝔣₄ are:

| subalgebra | centralizer of |
|---|---|
| B₄ = 𝔰𝔬(9) | an order-2 element |
| C₃ × A₁ = 𝔰𝔭(6) ⊕ 𝔰𝔲(2) | an order-2 element |
| A₂ × Ã₂ = 𝔰𝔲(3) ⊕ 𝔰𝔲(3) | the order-3 element (mark-3 node) |

A continuation of the fold "F₄ → G" therefore requires the object to supply a distinguished finite-order automorphism acting on the F₄ sector, or an equivalent selecting structure. Theorem 2 says it supplies none.

### 4.2 Statement

**Theorem 2.** *No structure intrinsic to the figure-eight at its complete hyperbolic point selects a proper subalgebra of the F₄ sector. Specifically:*

**(i) No Eisenstein ℤ/3.** **[PROVED]** *The θ-even exponents {1,5,7,11} coincide with (ℤ/12)^× ≅ ℤ/2 × ℤ/2 (Klein four): every non-identity element has order 2, so no order-3 structure exists in the F₄ deformation grading. The isometry group of M is D₄ of order 8 (SnapPy* **[COMPUTED]***), which by Lagrange contains no order-3 element, so no geometric ℤ/3 acts on the character variety. The trace field ℚ(√−3) has Galois group ℤ/2 (complex conjugation); the Eisenstein unit ω = (−1+√−3)/2 is a field* element*, and multiplication by ω is not a character-variety automorphism. The genuine order-3 Eisenstein structure (meridian rotation by ζ₆, with ζ₆² = ω) exists only at the collapsed Euclidean transition point x = 1 of the deformation curve, where the geometry degenerates and the trace field collapses to ℚ — not at the complete hyperbolic structure. Finally, the cyclic ℤ/3 permuting the three factors of E₆ ⊃ SU(3)³ (trinification) does not survive the fold: θ merges two of the three SU(3) factors, breaking the cyclic symmetry, so no residual ℤ/3 descends to the F₄ sector. Were an order-3 automorphism present, Borel–de Siebenthal would indeed hand it the centralizer 𝔰𝔲(3) ⊕ 𝔰𝔲(3); the conditional is true and its premise fails.*

**(ii) No golden ℤ/2.** **[PROVED]** *The second candidate involution γ = Gal(ℚ(√5)/ℚ) (the golden conjugation √5 → −√5, a genuine field automorphism) fixes ℚ(√−3) pointwise. The F₄ deformation sector is defined over ℚ(√−3) — its cusp/Gram datum is τ = −2√3·i = −2√(−3), with no √5 anywhere — so γ acts* trivially *on all four θ-even directions: there is nothing to flip, hence no (3,1)-versus-(2,2) exponent split, and no selection of 𝔰𝔬(9) over 𝔰𝔭(6) ⊕ 𝔰𝔲(2). γ does act nontrivially on a different face of the same knot — the quantum/Witten–Reshetikhin–Turaev data, e.g. coloured Jones evaluations in ℚ(√5) — so the knot's Klein-four arithmetic is real, but its two generators act on two different faces: θ (over √−3) folds E₆ → F₄; γ (over √5) conjugates the quantum face. Neither is a second selector within the F₄ sector.*

**(iii) The grading is non-selecting.** **[COMPUTED]** *The tangent grading itself is uniform: one deformation direction per exponent, none privileged (rank gaps 10⁸⁵–10¹¹⁹), and the amphichiral involution σ₋ acts as a real structure J² = +1 uniformly across all six lines (§2.3). There is no degenerate cascade, no preferred flag among the exponents, and hence no grading-selected subalgebra.*

**(iv) The cusp is uniform, and the cusp-point centralizer is zero.** *One might reframe: perhaps the reduction is effected not by a symmetry but by the boundary condition — the cusp killing some directions. This fails in a precise way, in two halves.*

  *(iv-a)* **[COMPUTED]** *(mpmath, 60 digits)* *The boundary restriction r : H¹(M, 𝔢₆) → H¹(T², 𝔢₆) has* **rank 6/6** *— there are no peripherally-invisible deformations. At the principal-composed geometric representation the peripheral holonomy is regular unipotent, so per block H⁰(T², Sym^{2m}) = 1 and H¹(T², Sym^{2m}) = 2, giving a 12-dimensional boundary space, block-diagonal over the six exponents and symplectic via cup product with the invariant pairing. Each of the six interior classes restricts to a nonzero boundary class (class residuals 1.5×10⁻⁶⁰–1.1×10⁻²⁷, at the per-block precision floor), and each "opens the cusp" at leading order (φ_μ ≠ 0 in every block). The image is 6-dimensional — half of 12 — and each block image is a line in a 2-dimensional symplectic plane, hence isotropic: the image of r is* **Lagrangian** *(the classical integration datum an exceptional 3d-3d state integral would use, were one to exist; see §8.6).*

  *(iv-b) The universal-τ identity.* **[COMPUTED]** *On every boundary cocycle (u,v) ∈ Z¹(T², Sym^{2m}), the leading Neumann–Zagier functionals satisfy K(v,h) = τ·K(u,h) with the* single *constant τ = −2√3·i — the figure-eight cusp shape, matched to SnapPy to 12 digits (the sign is the orientation convention) —* uniformly in m *(cross-block deviation ≤ 1.3×10⁻⁵²). The leading peripheral datum therefore does not split by exponent: there are no "higher cusp shapes" at first order, the E₆ boundary sees the same τ as SL(2), and in particular the cusp condition cannot distinguish θ-even from θ-odd directions. The cusp is achiral and uniform; it effects no 6 → 4 (or any) reduction. The E₆ → F₄ split is the symmetry θ of Theorem 1, not the boundary condition.*

  *(iv-c)* **[PROVED]** *(exact rational Gauss elimination)* *At the cusp-constrained point itself — the principal-composed geometric representation at the complete structure, whose meridian is parabolic — the algebra centralizer is zero:*

    *𝔠_{𝔢₆}(principal 𝔰𝔩₂) = 0,*

  *computed as the joint kernel of ad(e), ad(h), ad(f) in exact arithmetic. The mechanism is visible: ker(ad e) has ad-h weights {2, 8, 10, 14, 16, 22} — twice the exponents, all strictly positive — so the weight-0 intersection is empty (the Kostant structure). Control gate: 𝔠_{𝔢₆}(long-root A₁) = 35 = 𝔰𝔩₆, reproducing the known value exactly. Hence the group centralizer is finite (Kostant* **[CITED]***: it is the centre of E₆), and no continuous unbroken subgroup exists at the geometric point. The one branch this leaves open — centralizers at non-principal,* reducible *points satisfying the peripheral constraints — requires the uncomputed E₆ A-polynomial and is recorded as open in §8.5.*

**(v) No selection in the octonion arithmetic.** **[PROVED]** *The fifth proposed route — Baez–Schwahn's identification of the Standard-Model group as the stabilizer of a nested Jordan pair 𝔥₂(ℂ) ⊂ 𝔥₃(ℂ) ⊂ 𝔥₃(𝕆) inside the exceptional Jordan algebra [BS] — requires the object to select such a nested pair canonically. Its candidate arithmetic structures fail to act. The automorphism group of the octavian (integer octonion) ring has order*

  *|G₂(2)| = 12096 = 2⁶ · 3³ · 7,*

*with element orders {1, 2, 3, 4, 6, 7, 8, 12} — in particular* no element of order 11, *so the object's ℤ/11 charge (the Smith-normal-form torsion of its substitution dynamics) cannot act on the octavian arithmetic at all; 11 divides none of the relevant group orders up the chain. Moreover the Eisenstein axes (28) and the unit axes (63) of the octavian ring are disjoint strata, so the object's Eisenstein structure selects no unit-axis datum. No structure of the object canonically selects a nested pair; the fifth door closes like the four before it — by computation, not analogy.*

### 4.3 Scope of the terminus

Theorem 2 closes five *specific* proposed selectors at the complete hyperbolic point. It is **not** a claim that "F₄ → Standard Model is impossible in general" — only that this object's own symmetry and arithmetic, at its geometric point, provide no selector beyond θ. The object's arithmetic there is constitutively ℤ/2 × ℤ/2; the order-3 structure it does possess lives at a different, degenerate point of its deformation family.

---

## 5. Theorem 3 — the real-form theorem: compactness is the gap

### 5.1 Context

The Jordan-algebraic Standard-Model literature works with the *compact* groups. Todorov–Dubois-Violette [TDV] identify (with Krasnov's streamlined proof [K] and Boyle's extension [B]) the intersection of two distinguished subgroups of compact F₄ = Aut(𝔥₃(𝕆)) as

  G_SM = [SU(3) × SU(2) × U(1)] / ℤ₆,

canonically up to conjugation. Theorem 1 gives a geometric origin for F₄ — but *which* F₄?

### 5.2 Statement

**Theorem 3 (the real-form theorem).** *The image of the geometric holonomy under the principal composition lies in F₄(ℂ) ⊂ E₆(ℂ) as complex groups and is contained in* **no real form** *of either:*

*(a)* **[PROVED]** *(exact arithmetic in ℚ(√−3); two independent group-element witnesses; two independent code paths)* *the adjoint trace of the holonomy generator is non-real:*

  *tr Ad_{𝔢₆} ρ(a) = 37437270 + 38799960·√3·i ∈ ℚ(√−3) \ ℝ.*

*Any subgroup conjugate into a real form of E₆ has real adjoint traces (the adjoint representation of a real form is defined over ℝ); hence the holonomy image lies in no real form — compact or non-compact — of E₆, nor of F₄ acting through 𝔣₄ ⊂ 𝔢₆.*

*(b)* **[PROVED]** *(exact Jordan type)* *independently of (a), the meridian holonomy is regular unipotent, with adjoint Jordan type {3, 9, 11, 15, 17, 23} — one block per exponent, of sizes 2m+1. In a compact real form every element is Ad-semisimple; a nontrivial unipotent is impossible. The compact forms F₄^{compact} and E₆^{compact} are thus excluded by the cusp alone.*

*(c) Consequence: the transfer is complexified only.* *The TDV/Krasnov identification survives complexification: on our F₄(ℂ), the complexified intersection is*

  *H₁ℂ ∩ H₂ℂ = 𝔰𝔩(3,ℂ) ⊕ 𝔰𝔩(2,ℂ) ⊕ ℂ*  **[COMPUTED]** *(exact dimensions).*

*Krasnov's underlying theorem was verified by our own computation rather than cited: building the Clifford algebra Cl(9) on 𝕆² = ℝ¹⁶ from scratch gives dim 𝔰𝔬(9) = 36 exactly, J² = −I exactly, and the centralizer of J of dimension 12 = 1 + 11, of type 𝔲(1) ⊕ 𝔰𝔲(2) ⊕ 𝔰𝔲(3)* **[PROVED]** *(exact linear algebra). But the* compact slice *— the structure that makes G_SM a gauge group of a unitary theory rather than a complex algebraic datum — is exactly what the hyperbolic geometry does not provide. Compactness is the gap between the knot and a gauge group.*

### 5.3 Remark

Theorem 3 sharpens Theorem 2 from "no selector" to "no arena": even granting F₄ from Theorem 1, the knot delivers F₄(ℂ) with a unipotent cusp and non-real traces, not the compact F₄ in which the Standard-Model intersection theorems live. Any programme connecting hyperbolic 3-manifolds to Jordan-algebraic gauge structure must either produce the compact form from additional structure (unitarity of an associated quantum theory, a real polarisation, a real structure compatible with the knot's symmetries) or accept the complexified statement as terminal. We know of no mechanism in the present geometry that does the former; we flag it as the central open problem (§8.2, §9).

---

## 6. Summary of the logical structure

| step | statement | status | mechanism |
|---|---|---|---|
| 0 | six tangent lines, one per E₆ exponent | [CITED] + [COMPUTED] | [MFP]/[FG]; Fox calculus, gaps 10⁸⁵–10¹¹⁹ |
| 1 | hyperelliptic involution = θ; fixed sector = F₄ exponents | [PROVED] (signs) + [COMPUTED] (operator, dps 100) | Theorem 1 |
| 2 | no continuation past F₄: five routes closed | [PROVED] ×4 + [COMPUTED] (grading, cusp numerics) | Theorem 2 |
| 3 | holonomy in no real form; compact forms doubly excluded | [PROVED] | Theorem 3(a),(b) |
| 4 | Standard-Model intersection transfers complexified only | [PROVED]/[COMPUTED] + [CITED] | Theorem 3(c) |

---

## 7. Firewalled structural remark (not a claim)

Two exact matches deserve recording as *structure*, explicitly not as physics.

**7.1 The Eisenstein lattice is the G₂ root lattice.** **[PROVED]** (elementary) The Eisenstein integers ℤ[ω] realise the G₂ root system exactly: 6 short roots (the units, norm 1) and 6 long roots (norm 3), hexagonal at 30° spacing. Hence the figure-eight's trace field ℚ(√−3) is precisely the root field of G₂ = Aut(𝕆): the knot's arithmetic and the octonions' automorphism arithmetic share one lattice. We draw no inference; the coincidence is exact and cheap to state, and Theorem 2(v) already shows it does not by itself select Jordan-algebraic structure.

**7.2 The triality match.** **[COMPUTED]** (exact weight-level check) A (θ, φ) ℤ₃ × ℤ₃ action on the 27-dimensional representation, constructed previously from the knot's structure, coincides at the weight level with Boyle's SO(8)-triality action [B]: both generators 3-cycle the SU(3)³ trinification factors identically, and the 9 free orbits of size 3 on the 27 hit each trinification block exactly once — the cyclic-triality signature, exact on 100 % of weights. This is a *structure match* and explicitly **not** a claim about particle generations: three generations are derived nowhere in the literature, and this paper adds no derivation. Whether the match is forced or generic (how many ℤ₃ × ℤ₃ actions on the 27 match triality at weight level?) is a finite computation, posed in §9.

Both items are outlook only, firewalled from the theorems.

---

## 8. Limitations

We state the boundaries of the results plainly.

**8.1 The dimension count is not ours.** Proposition 0 (six lines, one per exponent) is governed by cited theory [MFP], [FG]; our computation is confirmation, not discovery. The novelty claims of this paper are confined to: the operator-level fold (Theorem 1(b)) with its sign theorem (Theorem 1(a)), the five closures (Theorem 2), the rank-6/6 boundary restriction with the Lagrangian certificate and the universal-τ identity (Theorem 2(iv)), and the real-form theorem (Theorem 3).

**8.2 Computer-assisted, two tiers.** Results labelled [COMPUTED] are high-precision numerics with residuals at the precision floor, not symbolic proofs. In particular: Theorem 1(b) is a gauge-certified numerical identity at 100 digits; the rank-6/6 statement and the universal-τ identity are numerically exact per block at 60 digits, and the mechanism proposed for universal-τ (at the complete structure U = exp(N̂), V = exp(τN̂) share one nilpotent direction, and the leading functional kills both im N̂ and ker N̂) is stated but not formalised as a proof. Results labelled [PROVED] are exact computer algebra and finite group theory.

**8.3 Local, not global.** Theorem 1 is established at the tangent/deformation-complex level at the principal-geometric point. The global statement σ* = θ* on the whole E₆-character variety is [CONJECTURE]. Higher-order (cup-product/Massey) integrability of the θ-odd directions is open.

**8.4 The terminus is scoped.** Theorem 2 closes five *specific* proposed selectors at the complete hyperbolic point. It does not assert that no continuation of F₄ exists under different hypotheses, at other points of the character variety, or for other manifolds. The centralizer statement (Theorem 2(iv-c)) is specific to the principal lift: long-root lifts have large centralizers (the 35 = 𝔰𝔩₆ control gate is exactly such a case), so the kill is embedding-specific by construction.

**8.5 Reducible cusp points are open.** The one surviving branch of the boundary-condition reframe: centralizers at non-principal, *reducible* representations satisfying the peripheral constraints could be larger. Deciding this requires the E₆ A-polynomial / full E₆-character variety of 4₁, which is uncomputed (SL(2) classical; SL(3) known [HMP]; E₆ open). Nothing computed here selects any particular subgroup at such points, and a reducible degeneration is in any case not the geometric structure.

**8.6 No quantum theory is invoked.** The 3d-3d correspondence of Dimofte–Gaiotto–Gukov [DGG] is engineered for A-type gauge groups only; no exceptional T[4₁; E₆] exists in the literature, and we construct none. The Lagrangian certificate of Theorem 2(iv-a) is the *classical* integration datum such a theory would use — no more.

**8.7 No physics.** Theorem 3 is a negative on the natural bridge: the compact form required by the Jordan-algebraic Standard-Model identifications is absent from this geometry. Per §1.2, a gauge-*group*-level match would clear no evidential bar even if the real form were present. The remarks of §7 are structure matches, firewalled, with no claim about generations, couplings, masses, or dynamics.

---

## 9. Outlook

Three directions look decidable.

**9.1 Formalise the fold.** Theorem 1(b) at 100 digits invites an exact proof: θ and the principal 𝔰𝔩₂ are exact objects, the holonomy is algebraic over ℚ(√−3), and the gauge certificates should lift to exact identities in the trace field. The same holds for the universal-τ mechanism of §8.2, whose shared-nilpotent argument is one lemma away from a proof.

**9.2 The compactness gap.** Is there *any* natural structure on the figure-eight's E₆(ℂ)-character variety whose stabiliser is a compact real form — a polarisation, a harmonic metric, a real structure compatible with amphichirality? (Note that σ₋ acts as J² = +1, a real structure, uniformly on every tangent line — raw material, at least, for a reality discussion.) A positive answer would rejoin the geometry to the compact-F₄ literature; a proof of absence would close the bridge cleanly. This is, in our view, the single sharpest question the paper raises.

**9.3 The two firewalled matches.** The Eisenstein/G₂-root-lattice identity and the exact triality match (§7) both deserve either a common structural explanation or a demonstration of genericity — how many ℤ₃ × ℤ₃ actions on the 27 reproduce the cyclic-triality signature at weight level? The latter is a finite computation.

The overall picture the letter defends: the figure-eight knot forces E₆ → F₄ by its own ℤ/2 symmetry, refuses every proposed continuation past F₄, and delivers the result in the complex group only. What a hyperbolic knot supplies is symmetry structure; what it withholds — selectors and compactness — is exactly what a gauge theory would additionally need.

---

## Methods note (reproducibility)

All computations are reproducible from the repository test suite. The exact layer uses rational/algebraic-number linear algebra (Python `fractions`, sympy): the centralizer computations of Theorem 2(iv-c) (joint kernel of ad(e), ad(h), ad(f) by exact Gauss elimination, with the long-root control gate); Smith normal forms; the finite-group arithmetic of Theorem 2(i, v); the exact θ in the root basis; the adjoint-trace witnesses of Theorem 3(a) (two code paths); and the Cl(9) construction of Theorem 3(c). The high-precision layer uses mpmath at 60–100 decimal digits: Fox calculus on the census presentation (relator gate ~10⁻⁷⁰); per-block Sym^{2m} twisted cohomology (rank gaps 10⁸⁵–10¹¹⁹); the θ-transport identity (residual 7.1×10⁻¹⁰²); the gauge certificates (9.9×10⁻⁷²–3.6×10⁻⁷⁹); and the boundary restriction with the universal-τ identity (cross-block deviation ≤ 1.3×10⁻⁵², SnapPy cusp-shape control to 12 digits). Every computation carries an internal control reproducing a known value (the 𝔰𝔩₂ anchor dim H¹(Sym²) = 1; the long-root centralizer 35 = 𝔰𝔩₆; the SnapPy cusp shape; symplectic-form gates — invariance ≤ 10⁻³⁹, antisymmetry ≤ 10⁻⁵⁵). One development incident is recorded as method: a first boundary-cocycle basis was ω-degenerate and mis-spanned H¹; it was caught by exactly these gates (class residual 0.23 against a floor of 10⁻²⁷) and replaced by the honest Z¹/B¹ orthonormal complement. The SL(3,ℂ) machinery underlying the toolchain has been corroborated against the published equations of [HMP]. Peripheral conventions: μ = ABB, λ = BAbabABa in the presentation ⟨a,b | abbbaBAAB⟩, gated in-module (commuting; both parabolic of trace −2 at the geometric point).

---

## References

- [BS] J. C. Baez, P. Schwahn, *The Standard Model Gauge Group from the Exceptional Jordan Algebra*, arXiv:2606.15235 (2026).
- [B] L. Boyle, *The Standard Model, the exceptional Jordan algebra, and triality*, arXiv:2006.16265; J. Math. Phys. 67 (2026).
- [BdS] A. Borel, J. de Siebenthal, *Les sous-groupes fermés de rang maximum des groupes de Lie clos*, Comment. Math. Helv. 23 (1949) 200–221.
- [CCM] A. H. Chamseddine, A. Connes, M. Marcolli, *Gravity and the standard model with neutrino mixing*, hep-th/0610241; and A. H. Chamseddine, A. Connes, *Resilience of the Spectral Standard Model*, arXiv:1208.1030.
- [DGG] T. Dimofte, D. Gaiotto, S. Gukov, *Gauge Theories Labelled by Three-Manifolds*, arXiv:1108.4389; Comm. Math. Phys. 325 (2014) 367–419. (A-type constructions only; no exceptional 3d-3d theory is available to cite.)
- [FG] E. Falbel, A. Guilloux, *Dimension of character varieties for 3-manifolds*, Proc. Amer. Math. Soc. 145 (2017).
- [HMP] M. Heusener, V. Muñoz, J. Porti, *The SL(3,ℂ)-character variety of the figure eight knot*, Illinois J. Math. 60 (2016); arXiv:1505.04451.
- [K] K. Krasnov, *SO(9) characterisation of the Standard Model gauge group*, arXiv:1912.11282.
- [Ko] B. Kostant, *The principal three-dimensional subgroup and the Betti numbers of a complex simple Lie group*, Amer. J. Math. 81 (1959) 973–1032.
- [MFP] P. Menal-Ferrer, J. Porti, *Twisted cohomology for hyperbolic three manifolds*, Osaka J. Math. 49 (2012) 741–769.
- [TDV] I. Todorov, M. Dubois-Violette, *Deducing the symmetry of the standard model from the automorphism and structure groups of the exceptional Jordan algebra*, arXiv:1806.09450; Int. J. Mod. Phys. A 33 (2018).
- [SnapPy] M. Culler, N. Dunfield, M. Goerner, J. Weeks, *SnapPy, a computer program for studying the geometry and topology of 3-manifolds*, http://snappy.computop.org.

---

## Note added (the two-descriptions complement to Theorem 3)

Theorem 3 locates the obstruction on the classical side: the holonomy selects the complex
groups, and no real form — in particular no compact form — is available to it. The program's
*quantum* description of the same object (the Weil representation on ℂ¹⁵ = ℂ³ ⊗ ℂ⁵, and the
WRT/modular data) is by contrast **unitary with finite image** [COMPUTED: the Heisenberg
operators satisfy X¹⁵ = Z¹⁵ = 1 exactly; the Weil-image scale is |SL(2,ℤ/15)| = 2880], and its
tensor factors 3 and 5 are precisely the residue characteristics of the object's two arithmetic
ends (ℚ(√−3) and ℚ(√5)), with compositum ℚ(√−15). Thus compactness — the ingredient Theorem 3
shows the geometry does not supply — is constitutively a feature of the *measurement* face of
the object, not of its *algebra* face; the two faces are connected asymptotically by the volume
conjecture for 4₁ (Kashaev; verified numerically in the program's records). We record this as a
structural observation, not a mechanism: the finite unitary image is not the compact Lie form
F₄(₋₅₂), so the gap identified by Theorem 3 is thereby *located* (at the interface between
algebra and measurement) rather than crossed.
