# STRUCTURE PAPER — skeleton

**Working title:** *The measurement cascade of the figure-eight knot's E₆*
(title candidates and the abstract in `ABSTRACT_DRAFT.md`)

**Status: DRAFT SKELETON ONLY. Publication is owner-gated.** Mathematics only —
no physics identification is made anywhere in the paper body; the two data
contacts (the crossings) appear ONLY as sealed negatives in Discussion §12.2.
Gate 5 stands throughout. Internal names ("measurement", "matter", "vacuum",
"flavor", "color", "generation") are names of mathematical objects, glossed at
first use and in Appendix C; the paper claims nothing about physics under them.

**Scope of this skeleton:** section plan with per-section content lists, the
exact banked citation (arc + lock) per claim, the five headline theorem
statements formalized, the figures list, and the honest-limitations subsection.
Prose drafting comes after owner sign-off on this structure.

---

## 0. The paper in one paragraph

One abelian subalgebra u(1)⁴ of the Chevalley algebra 𝔢₆ over ℚ — spanned by
the four Klein invariants of the binary tetrahedral group 2T under the
principal sl(2) — generates, by nothing but successive centralizers of its own
elements ("measurements"), a forced cascade: 𝔢₆ → so(10)⊕u(1) (three
Galois-conjugate ways, the FMT) → su(3)⊕su(2)⊕u(1)³ exactly, skipping
su(5)⊕u(1) (the SMT). The ambient decomposition is the Barton–Sudbery magic
square M(𝕆,ℂ) by explicit structure-constants isomorphism. The unique real
form of E₆ in which the second wall is real is the quaternionic form e₆(2),
reached only through outer-twisted alignments, with a sign-locking theorem
making the wall pattern unique. The Hermitian twist D₂ that carries the entire
derived scale hierarchy is characterized with no residual freedom: it is the
second wall conjugation's sign character acting on the 27. Every
verdict-bearing computation is exact (over ℚ or a number field), locked by a
re-runnable test suite, and cross-verified by independent internal pipelines.

---

## 1. The five headline theorems (formal statements)

Notation: 𝔢₆ is the B854 Chevalley algebra of type E₆ over ℚ;
C = ⟨x₈, x₁₄, x₁₆, x₂₂⟩ is the span of the four 2T-invariant vectors (Klein
forms of degrees 8, 14, 16, 22 — twice the exponents 4, 7, 8, 11); μ is the
charge cubic (irreducible over ℚ, constant term 13³); K = F = ℚ[ρ]/μ;
z(·) denotes the centralizer in 𝔢₆.

### Theorem A — the First Measurement Theorem (FMT)

*(CLAIMS.md row P69; two-seat: B877 reviewing the solo seat's theorem, with
independent legs B866/B872/B874/B875.)*

Let C be as above. Then:

(i) **(Abelianness)** C is abelian: z-closure gives u(1)⁴; the four Klein
    forms are the complete list of 2T-invariants in 𝔢₆ under the principal
    sl(2) (degrees 8, 14, 16, 22). [B854 · `tests/test_b854_centralizer.py`]

(ii) **(Stratification)** On the plane ⟨x₈, x₁₆⟩ the centralizer dimension
    stratifies as: 12 (generic in the torus), 30 (generic in the plane), and
    **exactly three lines at 46**. The three lines are the S₃-Galois orbit of
    the roots of the irreducible cubic μ, with the exact pencil identities
    det₃₆ = c·μ¹² and det₁₂ = c·μ⁴ over ℚ.
    [B866 · `tests/test_b866_charge_cubic.py`; B877 · `tests/test_b877_fmt_review.py`]

(iii) **(Types)** z(plane) = so(8)⊕u(1)²; for each distinguished line Kᵢ,
    z(Kᵢ) ≅ so(10)⊕u(1); Kᵢ∩Kⱼ = z(Π) by identity.
    [B877 · `tests/test_b877_fmt_review.py`]

(iv) **(The tiling and the cyclic law)** 𝔢₆ = (so(8)⊕u(1)²) ⊕ V₁ ⊕ V₂ ⊕ V₃
    with dim Vᵢ = 16, Vᵢ = ad(x_j)(Kᵢ) independent of j, satisfying
    [Vᵢ,Vᵢ] ⊆ core and [Vᵢ,Vⱼ] = V_k (the weight-line lemma a priori;
    sum-freeness certified at two primes × all three roots).
    [B875 · `tests/test_b875_tiling.py`; B877 · `tests/test_b877_fmt_review.py`]

(v) **(The coset)** Each 𝔢₆/Kᵢ ≅ Vⱼ⊕V_k = 16⊕16̄ as an so(10)⊕u(1)-module.
    [B872 · `tests/test_b872_coset.py`]

### Theorem B — the magic-square isomorphism

*(CLAIMS.md row P70; B904.)*

The algebra L(𝕆_split, ℂ′_split) — constructed over ℚ from Zorn vector-matrix
octonions with tri(𝕆) the exact 28-dimensional triality nullspace, the cross
products the unique equivariant bilinears (multiplicity-one certified over all
28 triality triples × 64 basis pairs), the same-summand duals the
Killing-duals, and the nine remaining scalars fixed by Jacobi to λ ≡ 1,
μ ≡ −24, ν ≡ −12 — satisfies the Jacobi identity on all 76,076 unordered basis
triples exactly; its adjoint splits over its rational torus into 72
one-dimensional rational root spaces plus a 6-dimensional Cartan with Cartan
matrix E₆; and there is an explicit linear map φ, verified to be a Lie-algebra
isomorphism on all 3,003 basis pairs (det φ = −2/3), onto the B854 Chevalley
𝔢₆. Consequently the FMT tiling (so(8)⊕u(1)² core, three 16-dimensional tiles,
the cyclic law) **is** the (𝕆,ℂ) magic-square algebra by explicit
structure-constants isomorphism — not merely by module-level signature.
[B904 · `tests/test_b904_bs.py`; module-level precursor B880 ·
`tests/test_b880_signature.py`]

### Theorem C — the Second Measurement Theorem (SMT)

*(B892, two-seat verification of the solo seat's theorem; the complex-wall
clause B892 §2 + B893.)*

Over F = ℚ[ρ]/μ, on the block-12 matter pencil:

(i) The perfect-square gate C₂² − 4C₀ = 0 holds exactly; γ² = −C₂/2 with the
    +γ eigenspace 2-dimensional; a² = −det₁₄ ∈ F(γ) with det₁₄ ≠ 0; the wall
    point y* = γx₁₄ − a·x₁₆ satisfies λ₊(y*) = 0 by construction.

(ii) **(The landing)** dim z(x₁, y*) = 14 (lower bound by construction:
    kernel-12 plus two antipodal lines; upper bound by the tower prime),
    derived algebra dimension = 11, center ≥ 3, whence
    **z(x₁, y*) = su(3) ⊕ su(2) ⊕ u(1)³ exactly.**

(iii) **(The skip)** The within-C centralizer ladder is
    {78, 46, 30, 18, 14, 12}; the dimension 26 of su(5)⊕u(1) is not attained
    by these charges — the second measurement skips SU(5).

(iv) **(The wall is complex in the split frame)** det₁₄ > 0 at the real root
    with γ-part exactly 0, so a is imaginary: y* is not a real point of the
    split torus; on the real (x₁₄,x₁₆) projective line the only stratum jump
    is the known nullity-30 plane point — no real nullity-14 point exists
    there. This holds at **all three** Galois roots of μ.

[B892 · `tests/test_b892_smt.py`; B893 · `tests/test_b893_omega.py`]

### Theorem D — the e₆(2) selection with sign-locking

*(B907, sealed preregistration, outcome A; completeness addendum
banking-verified. Constraint input B901.)*

(i) **(±-diagonal constraint)** n(C) = z(C) = 12: every C-stabilizing
    automorphism of 𝔢₆ (linear or antilinear) acts ±-diagonally on the four
    charges, i.e. carries an ε-pattern (ε₈, ε₁₄, ε₁₆, ε₂₂) ∈ {±1}⁴; no real
    C-stabilizing symmetry swaps split/compact directions or x₈ ↔ x₁₆.
    [B901 · `tests/test_b901_stab.py`]

(ii) **(Sign-locking)** Every C-stabilizing automorphism satisfies
    ε₈ε₁₆ = +1 and ε₁₄ε₂₂ = +1 — proved by two exact rational trace moments of
    degree 6 (every mixed moment of degree ≤ 4 vanishes in the odd parity
    classes). Twelve of the sixteen ε-patterns are impossible for every
    automorphism.

(iii) **(Uniqueness)** The wall-real pattern (sealed criterion ε₁₄ = +1 ∧
    ε₁₆ = −1, root-uniform by the banked Galois-uniformity) is unique:
    ε = (−1, +1, −1, +1), with ε₈ and ε₂₂ forced, not observed.

(iv) **(Realization and the form)** In the 128-representative census (64
    frame-diagonal inner sign-characters; 64 outer composites with the exact
    τ-lift of the diagram flip), exactly two representatives are C-compatible
    and wall-real — the outer pair χ = (1,−1,1,−1,1,1) and its global
    negation, each verified φ² = id — and for both, the composite with the
    Chevalley involution has fixed dimension 38 = su(6)⊕su(2):
    **the wall is real in e₆(2), the quaternionic form, and in no other form
    reached; the two wall-real conjugations are τ-twisted (outer-adapted)
    alignments — no standard alignment works.** Feasible = realized at the
    pattern level: the sweep is complete there.

[B907 + addendum · `tests/test_b907_selector.py`]

### Theorem E — the D₂ characterization (the carrier of the hierarchy)

*(B928, sealed preregistration, outcome FORCED; inputs B907/B912/B916/B923.)*

Let D₂ be the eleven-flip diagonal of the value arc (H′ = H₊D₂, B916), and let
χ₋ = −χ₊ be the second wall conjugation's sign vector. Then:

(i) **(The character form)** D₂ = ±ρ₂₇(σ_χ₋); explicitly
    D₂ = −(−1)^⟨a*, w⟩ with a* = s(χ₋) = (1,0,1,0,1,1) — the affine (shifted)
    character, the unique match in the 128-member family (no un-shifted
    character matches; all 64 fail).

(ii) **(The wall-conjugation equation)** H₊D₂ = H(φ*) where
    φ* = τ∘φ₊∘φ₋ = φ₊∘σ_χ₋ is an involution and an automorphism (verified on
    all 78² bracket pairs) and is the **unique** member of the census whose
    invariant Hermitian structure is H₊D₂. The equation is built from banked
    objects with no residual choice.

(iii) **(The Klein group)** {I, D₂, D, D₂D} = ±ρ₂₇({1, σ_χ₋, σ₋₁, σ_χ₊}):
    the two Hermitian instruments of the value arc are the two wall-real
    alignments' data through the same τ-lift; the wall pair's whole 2-torsion
    acts on the 27.

(iv) **(The torsor theorem)** Every inner twist admits no invariant pairing
    (weight-support empty, proven); every outer composite σ_χ∘τ admits exactly
    one, H_χ = H₊·ρ₂₇(σ_{χ·χ₊}) (all 64 verified), and H_χ is symmetric (a
    Hermitian structure) exactly when the composite is an involution.

(v) **(Derived arithmetic)** From the characterization alone: the twist
    ratios obey d = 1 − 2m per atom family with
    N_{K/ℚ}(d_S) = N_{K/ℚ}(d_A) = −(953/2304)² exactly (the sign supplied by
    the affine polarity); on the 3-dimensional colored atoms the norm law
    cubes: N_{K/ℚ}(det G⁻¹G′) = −(953/2304)³; the flip rank obeys the sum
    rule Tr_{K/ℚ}(m_S) + Tr_{K/ℚ}(t_oct) = tr Π_F = 11 exactly; and the
    banked hierarchy polynomial HIER is recovered coefficient-for-coefficient
    (the canonical gauge collapses to (x+3)³ — the entire hierarchy is
    carried by D₂).

[B928 · `tests/test_b928_decode.py`; B916 · `tests/test_b916_bridge.py`;
B923 · `tests/test_b923_exact.py`]

---

## 2. Section plan (content lists + exact citations)

### §1 Introduction

- The cascade in one figure (Fig. 1) and one paragraph (as §0 above).
- Definition of "measurement" as used here: passing to the centralizer of an
  element of the fixed abelian torus C — a purely Lie-algebraic operation.
  Fence: the word is an internal name; no physical measurement is claimed.
- Why the figure-eight knot is in the title, stated honestly: the banked chain
  attaches E₆ to the knot's arithmetic (trace field ℚ(√−3)); per the B727
  self-audit the ADE-classification step is general and the object-specific
  content is the arithmetic atom (ℚ(√−3), the unique arithmetic knot). The
  title wording is an owner decision; the alternative neutral title is listed
  in `ABSTRACT_DRAFT.md`. [B347; B727 — background citations, no lock claimed
  here; the paper's theorems stand on the E₆ frame independently.]
- Statement of Theorems A–E in brief; roadmap; the verification model
  (forward-pointer to §12.4 and Appendix A).

### §2 The frame: the Chevalley 𝔢₆ and the four 2T-charges

- The B854 build of 𝔢₆ over ℚ; the conventions block (basis, signs,
  normalizations — GOVERNANCE §13 discipline) reproduced in Appendix C.
- The principal sl(2) ↪ 𝔢₆; 2T ⊂ SL(2) the binary tetrahedral group (24 unit
  quaternions); exact averaging in Sym^n; the four invariants are Klein's
  classical forms ΦΨ, t·ΦΨ, (ΦΨ)², t·(ΦΨ)² in degrees 8, 14, 16, 22 (= twice
  the exponents 4, 7, 8, 11); Burnside count = 4.
  [B854 · `tests/test_b854_centralizer.py`]
- C = u(1)⁴ abelian, computed exactly (the su(2)×u(1) relay claim refuted en
  route — an honest-correction note). [B854 · `tests/test_b854_centralizer.py`]
- The charge cubic μ, irreducible /ℚ, constant 13³; the field K = ℚ[ρ]/μ.
  [B866 · `tests/test_b866_charge_cubic.py`]

### §3 The First Measurement Theorem (Theorem A)

- Proof architecture, in the order it convinces:
  1. the exact pencil identities det₃₆ = c·μ¹², det₁₂ = c·μ⁴ over ℚ;
  2. the squeeze pattern — mod-p rank as a LOWER bound (the direction that
     cannot lie) + reductivity + exact dimensions + the classification table;
  3. Kᵢ∩Kⱼ = z(Π) by identity, no computation;
  4. the weight-line lemma (a priori): 48 nonzero Π-weights = 16·3 exhausted
     by the three annihilator lines ⟹ [Vᵢ,Vⱼ] ⊆ V_k;
  5. sum-freeness via the one-prime lemma, certified at two primes × all
     three roots.
- Two-seat status: solo-seat theorem, banking-seat review with independent
  legs (B866 interpolation, B872 mod-p radical + coset, B874 census, B875
  tiling numerics + the projector-trap record).
- Citations: [B877 · `tests/test_b877_fmt_review.py`],
  [B866 · `tests/test_b866_charge_cubic.py`], [B872 · `tests/test_b872_coset.py`],
  [B875 · `tests/test_b875_tiling.py`], [B880 · `tests/test_b880_signature.py`].

### §4 The magic-square identification (Theorem B)

- Stage 1: split octonions on the Zorn basis; tri(𝕆) as an exact nullspace,
  dim 28; tri(ℂ′) dim 2; predicted tiling 28+2+16·3 = 78.
- Stage 2: every product DERIVED, not chosen — the action pattern from the
  triality identity; cross products as unique equivariant survivors
  ((1,2)→3: xy; (2,3)→1: y·x̄; (3,1)→2: ȳ·x; ℂ′-side zw, z̄w, zw̄);
  Killing-duals; the nine scalars λ ≡ 1, μ ≡ −24, ν ≡ −12 fixed by Jacobi.
- Stage 3: full Jacobi — 76,076 triples, 0 failures, exact.
- Stage 4: 72+6 rational root decomposition; Cartan matrix E₆ under
  relabeling (4,3,1,2,0,5); φ verified on all 3,003 pairs; det φ = −2/3.
- The upgrade narrative: B880's module-level signature (three pairwise
  inequivalent so(8) sectors) → B904's theorem-level identification; the B882
  naming now stands on a theorem.
- Citations: [B904 · `tests/test_b904_bs.py`], [B880 · `tests/test_b880_signature.py`].

### §5 The Second Measurement Theorem (Theorem C)

- The block-12 matter pencil over F; the perfect-square gate; construction of
  the wall point y*; the squeeze to (14, 11, ≥3); the exact landing.
- The within-C ladder {78, 46, 30, 18, 14, 12} and the su(5)⊕u(1) skip; the
  B874 amendment recorded honestly (the earlier "torus does not supply the
  step-2 charge" overgeneralization, corrected — the correction trail is part
  of the paper's verification story).
- The u(1)-assignment rank fact (exact direction): rank 3 for exactly the
  conjugation pair of assignments; all 14 mixed assignments fail at rank 4.
  (Mathematics phrasing only; the physics-flavored name for this computation
  stays out of the body.) [B892 · `tests/test_b892_smt.py`]
- The wall is complex in the split frame, at every Galois root; the Chevalley
  involution ω of this frame (ω(e_α) = e₋α, d ≡ 1) is transverse to the
  measurement frame. [B893 · `tests/test_b893_omega.py`]

### §6 The concordance, the spectrum dichotomy, and the sign law

- The four-column concordance: measured plane ⟺ θ-odd exponents (4,8) ⟺
  τ_m > 0 ⟺ split ad-spectrum; unmeasured pair ⟺ (7,11) ⟺ compact;
  7·11 = 77 the resolvent assembled from the two unmeasured exponents; 5 by
  ramification. [B894 · `tests/test_b894_bridge.py`;
  B898 · `tests/test_b898_census.py`; B888 · `tests/test_b888_two_fields.py`]
- The signature dichotomy theorem: ad(x₈) ≡ ad(x₁₆): {0³⁰, 48 real};
  ad(x₁₄) ≡ ad(x₂₂): {0¹², 66 imaginary}; zero generic-complex on C; the
  kernels are the FMT centralizer and the floor.
  [B898 · `tests/test_b898_census.py`]
- The sign-law mechanism: all six torsion quotients exactly anti-palindromic;
  sign(τ_m) = sign(lc)·(−1)^{p_m}, p_m ≡ m (mod 2) in every block.
  [B903 · `tests/test_b903_sign.py`]
- The diagonal cocycle theorem: all four Π-label cubics have a root in K
  (each led by 13³); one S₃ root permutation acts on both orbits; the exact
  frame twists. [B900 · `tests/test_b900_cocycle.py`]

### §7 The real form: the e₆(2) selection (Theorem D)

- B901's no-go as the constraint that made the sealed cell decisive.
  [B901 · `tests/test_b901_stab.py`]
- The sealed cell: the inner sweep (fixed dims {78×1, 46×27, 38×36}; all 27
  so(10)⊕u(1)-class members C-incompatible — the e₆(−14) obstruction banked
  as computed); the exact τ-lift (the flip-symmetric-character ansatz provably
  empty first — logged; the general F₂-cocycle solve, rank 66); the outer
  sweep; the two survivors; the form identification (38 = su(6)⊕su(2)).
- The sign-locking addendum (C1–C3): the degree-6 moment kill; the unique
  wall pattern; feasible = realized at the pattern level.
- The prereg discipline note: the disclosed prior (e₆(−14)) was WRONG — the
  third sealed cell to decide against its prior; part of the paper's
  methodology story (Appendix A).
- Citations: [B907 + addendum · `tests/test_b907_selector.py`].

### §8 The 27: atoms, exactness, the signature split

- The rational-atoms theorem: the four charges commute rationally on the 27;
  the fifteen flavor atoms are joint eigenlines of a rational commuting family
  (the tower never enters the atom lines); the colorless nine form a 3×3 grid
  — rows the even transversals of a determinant, columns the odd; the first
  derived value I = −1 is that determinant's orientation parity (the Leibniz
  sign), exact (P_R = −P_C as 106-digit integers; c_S = −disc(μ);
  B(ρ) = −3w²). [B908 · `tests/test_b908_pin.py`]
- The unified ℤ₂ law (three faces: matter gluing = gauge commutation =
  mixed-texture type, 8/8 and 48/48 at two primes); the 15 atoms' bijective
  tri-partition; the colorless grid = two pencils of AG(2,3); K₃,₃.
  [B906 · `tests/test_b906_flavor.py`]
- The signature split of matter: the canonical Hermitian structure has
  signature (15,12) = e₆(2)'s K-type split; nine colorless atoms
  positive-definite with nine exact scales; all six colored atoms Lorentzian
  (1,2,0). [B912 · `tests/test_b912_norm.py`]
- The sealed generation-shape (outcome A), stated inside its fence:
  G₂₀'s su(3)′ replicates fixed color⊗su(2)′ types into triplets; the 3+6
  lepton split; Casimirs 4/9, 4/9, 3/8; mechanism-hood explicitly NOT claimed.
  [B897 · `tests/test_b897_g20.py`]

### §9 The value layer

- The inter-breaking laws (exact minimal-polynomial theorems on the matter
  pencil). [B885 · `tests/test_b885_interbreaking.py`;
  B886 · `tests/test_b886_matter_pencil.py`]
- The annihilation theorem: [α_vac] = [α_μ]⁻¹ in the Knus–Paques group;
  vacuum ⊕ charge = the split algebra. [B902 · `tests/test_b902_kp.py`]
- The one-class theorem + the numerator law: [α_μ] = [α_gen] = [α_κ] = C,
  [α_vac] = C⁻¹; 13⁶ noncompact / 19⁶ compact Kummer elements.
  [B910 · `tests/test_b910_kappa.py`]
- The one-number table: all six normalization-free colorless couplings
  exactly equal T = σ₂(t_K). [B914 · `tests/test_b914_table.py`]
- The unimodularity identity + the twist-norm law: λ = 1 exactly in the
  charge-equivariant gauge (c² = −q_iq_jq_k); the τ-twisted gauge gives
  2304/953; ∏d_i = −(953/2304)² = N_{K/ℚ}(d); pin H by equivariance, never
  primitivity. [B916 · `tests/test_b916_bridge.py`;
  B917 · `tests/test_b917_value_arc.py`]
- The product law v₁v₂v₃ = 3^{3/2}λ² (27·2304⁴ = 760840571584512 exact) and
  the prime biography: structure primes (13, 17, 19) inert in K, value primes
  (953, 1129, 421493) split [1,2]. [B917 · `tests/test_b917_value_arc.py`]
- The value-layer one-class extension + the observer's-place theorem:
  den(V) = 𝔭₁(953)⁴ — the hierarchy's pole entirely on the unique degree-one
  place. [B918 · `tests/test_b918_v.py`]
- The exactified identities: CCC = 3!·λ; v_g² = roots(HIER); the colored
  eigenvalue field K(√−231); the canonical gauge is generation-degenerate
  ((x+3)³) — the hierarchy is carried entirely by D₂ (the bridge into §10).
  [B923 · `tests/test_b923_exact.py`]
- Coupling rigidity: all three stage-field involutions collapse to one forced
  value per face pair. [B924 · `tests/test_b924_rigidity.py`]

### §10 The D₂ characterization (Theorem E)

- The sealed question and the candidate list (a)–(d); the verdict FORCED via
  (c) with (a) as its character form; the two in-cell refutations (11 = 8+3
  numerology; the naive-character miss explained by the affine polarity) as
  the discipline working mid-cell.
- The derived arithmetic (Theorem E(v)) and the exact residue: 953 and
  2304 = 2⁸3² enter through the atom-solve eigenline coordinates; the
  derivation stops exactly there (registered open — §12.3).
- The shape sheet as a list of abstract K-invariants (m_S, m_A, trM_col,
  t_oct; minpolys; the square/cube norm laws; the forced equalities; the sum
  rule 11) — computed blind; no measured value consulted; its comparison
  stage is owner-gated and NOT part of this paper.
- Citations: [B928 · `tests/test_b928_decode.py`].

### §11 The compact chain (the CMT lane)

- The Compact Measurement Theorem: at κ's genuine roots (five (root, prime)
  pairs including the fully-split 40039) the compact wall centralizer types
  uniformly as so(8)⊕u(1)² (30/28/18/2), core-shaped, core-distinct; the
  corrected-instrument story told whole (the retracted-septic phantom roots,
  caught by root mismatch). [B909 · `tests/test_b909_frame.py`]
- The One-Field theorem (κ splits [1,2] over K; one S₃); ν = c·κ⁶ exact;
  κ's constant −19³; the six-cubic √77 law; the Killing-perp/invisible 12
  and its SMT-block identification. [B909 · `tests/test_b909_frame.py`]
- The trace-ratio 3/8 on the SMT block (mathematics phrasing in the body;
  the ratio's conventional physics name appears only in §12.2's sealed
  negatives context, if at all). One-prime tier, second prime open-diagnosed —
  flagged in §12.4. [B919 · `tests/test_b919_traces.py`]

### §12 Discussion

**12.1 What is proved vs what is named.** The naming fence, in one honest
paragraph: "measurement", "matter", "vacuum", "flavor", "color", "generation"
are internal names for the mathematical objects defined in §§2–11; the paper
asserts no correspondence with physics. The su(3)⊕su(2)⊕u(1)³ landing is a
statement about centralizers in 𝔢₆, full stop.

**12.2 The sealed negatives (the crossings).** The only two data contacts in
the programme's record, both owner-authorized, both preregistered with sealed
two-outcome criteria, both negative, reported verbatim:

- **The first crossing (B915, sealed `7a423aed…`, outcome MISS):** one
  measured input plus the E₆ boundary value 3/8 propagated across a pure
  two-loop desert misses the measured pair at d = 15.97 σ_tot (14.63
  max-component), α_s-dominated; the miss survives any honest inflation of
  the truncation band. Killed exactly as pre-stated: the naive
  boundary-plus-desert identification. Standing exactly as pre-stated: every
  structural theorem of this paper. The banked failure geometry (pairwise
  meeting scales 1.09×10¹³ / 1.72×10¹⁴ / 2.91×10¹⁶ GeV) is reported as a
  negative-result datum. [B915 · `tests/test_b915_crossing.py`]
- **The second crossing (B925, sealed, outcome B):** the compact chain admits
  no unbroken su(2) above the banked color inclusion — exact centralizer
  certificates C(su3_c, su4) = u(1)_{B−L}-type line and C(su3_c, so8) = u(1)²
  in both directions; the D-chain RG-ladder identification dies by algebra.
  [B925 · `tests/test_b925_crossing2.py`]
- The registered continuation R4b (the compact D-chain E₆ ⊃ D₅ ⊃ D₄ ⊃ D₃ ⊃ A₂
  as the desert's replacement) awaits its own seal; nothing about it is
  claimed here.

**12.3 Open problems (registered).**
- The Q2 residue: a pipeline-free closed form for 953 and 2304 = 2⁸3²
  (B928's registered open).
- The second prime for the 3/8 trace-ratio tier (B919's open diagnosis).
- Census-scope completeness beyond the pattern level: an automorphism outside
  every swept class is not excluded by B907/B928 (banked caveat).
- Branch naming: the identification of Galois branches with B900's frames is
  by the banked vacuum_frame_map (cited, not recomputed in B928).
- A closed-form mechanism for the FMT constant 13³ and the CMT constant −19³
  beyond the banked pencil identities.

**12.4 Honest limitations.** *(Required subsection — full text drafted here,
to survive editing verbatim.)*

1. **Verification provenance (per `PROVENANCE.md` §0).** From day 0, every
   verification of this material has been INTERNAL: the owner plus AI
   assistant seats cross-checking one another. Nothing has been externally
   verified, peer-reviewed, or endorsed by any third party. Wherever this
   paper says "verified", "independently verified", or "two-seat", it means:
   recomputed or attacked by a second internal pipeline (a different in-repo
   implementation, a different seat, a mod-p certificate, an exact-arithmetic
   lock) — never an external referee. The intended verification path for a
   reader is the re-runnable lock suite (Appendix B).
2. **One-prime tiers.** Squeeze arguments use mod-p ranks only as lower
   bounds (the direction that cannot lie), closed by exact dimensions and
   reductivity; but the certificate tier varies by claim and is disclosed per
   claim: the FMT sum-freeness is certified at two primes × three roots; the
   CMT typing at five (root, prime) pairs; the 3/8 trace ratio sits at a
   ONE-PRIME tier with the second prime open-diagnosed (B919). One-prime
   claims are labeled as such in the body.
3. **Novelty: NEEDS-SPECIALIST.** No specialist in exceptional Lie theory /
   composition algebras has assessed novelty. Internal prior-art checks
   (Barton–Sudbery, magic-square literature, real-form classifications) found
   no statement of Theorems A, C, D, E in the forms given, and Theorem B's
   construction-plus-explicit-isomorphism appears stronger than the
   module-level statements we located — but this is an internal reading. The
   paper must not claim novelty beyond "we did not find it"; the caveat is
   carried in the abstract's final sentence.
4. **Frame dependence.** All computations are in the B854 Chevalley frame
   with a declared conventions block; Galois-uniformity (B898) and the
   diagonal cocycle (B900) control root-choice dependence, and the B928
   structures are re-solved from their defining equations (handoff-free);
   residual frame dependence beyond these controls is not excluded.
5. **Census scope.** Real-form and carrier uniqueness statements are relative
   to the 128-representative census, complete at the ε-pattern level by the
   sign-locking theorem; representatives outside every swept class are not
   excluded (see §12.3).
6. **Corrected-en-route record.** Several banked inputs were corrected during
   the campaign (B874's amendment; the B909 instrument correction; two B928
   draft conjectures refuted by the run). The paper cites the corrected
   statements; the correction trail is part of the record and is summarized
   in Appendix A, not hidden.

### Appendix A — methodology

- Exact arithmetic for every verdict-bearing claim; number-field certificates;
  50-digit numerical belts as cross-checks only, never as verdicts.
- The squeeze pattern (mod-p lower bound + reductivity + exact dims) and the
  one-prime lemma, with the valid-direction discipline stated.
- Preregistration: sha-256-sealed designs committed before compute; the seal
  scoreboard reported honestly (seven sealed cells at B928's banking: four
  object-overrules of the disclosed prior, three disciplined wins) — the
  discipline works in both directions.
- The error classes that shaped the instruments (oblique-readout rule: no
  Rayleigh-quotient eigenreads on non-normal matrices — violated and caught
  four times, the fourth inside B907; the projector trap of B875; the
  retraction-propagation failure caught in B909).

### Appendix B — reproducibility

- The lock table: every claim row of this paper → arc → test lock (the §2–§11
  citations, gathered as one table; seed rows in §3 below).
- How to run: the repo's test suite and gates (`REPRODUCIBILITY.md`); locks
  assert mathematics, not transcripts, wherever feasible.

### Appendix C — notation and internal-term glossary

- The conventions block of the B854 frame (basis, signs, normalizations,
  root order, the relabeling (4,3,1,2,0,5) of §4).
- Glossary rows from `TERMINOLOGY.md` for every internal term used
  ("measurement", "wall", "atom", "core", "tile", "charge", "value layer",
  "twist", "flip mass", …).

---

## 3. The citation registry (claim → arc → lock; the paper's spine)

| # | Claim (short) | Arc | Lock |
|---|---|---|---|
| 1 | C = u(1)⁴; the four Klein forms | `frontier/B854_centralizer_exact` | `tests/test_b854_centralizer.py` |
| 2 | μ irreducible, constant 13³; pencil identities | `frontier/B866_charge_cubic` | `tests/test_b866_charge_cubic.py` |
| 3 | FMT (Thm A), two-seat | `frontier/B877_fmt_review` | `tests/test_b877_fmt_review.py` |
| 4 | Coset 16⊕16̄ | `frontier/B872_coset_leg` | `tests/test_b872_coset.py` |
| 5 | Tiling + cyclic law numerics | `frontier/B875_triality_tiling` | `tests/test_b875_tiling.py` |
| 6 | Module-level magic-square signature | `frontier/B880_triality_signature` | `tests/test_b880_signature.py` |
| 7 | Magic-square isomorphism (Thm B) | `frontier/B904_barton_sudbery` | `tests/test_b904_bs.py` |
| 8 | SMT (Thm C) | `frontier/B892_second_measurement` | `tests/test_b892_smt.py` |
| 9 | Wall complex at every root; ω transverse | `frontier/B893_omega_vs_measurement` | `tests/test_b893_omega.py` |
| 10 | Four-column concordance | `frontier/B894_meditation_trio` | `tests/test_b894_bridge.py` |
| 11 | Signature dichotomy; Galois-uniformity | `frontier/B898_exact_census` | `tests/test_b898_census.py` |
| 12 | 77 = 7·11 resolvent | `frontier/B888_two_fields` | `tests/test_b888_two_fields.py` |
| 13 | Sign-law mechanism | `frontier/B903_sign_law` | `tests/test_b903_sign.py` |
| 14 | Diagonal cocycle theorem | `frontier/B900_frame_cocycle` | `tests/test_b900_cocycle.py` |
| 15 | C-stabilizer no-go | `frontier/B901_c_stabilizers` | `tests/test_b901_stab.py` |
| 16 | e₆(2) selection + sign-locking (Thm D) | `frontier/B907_real_form_selector` | `tests/test_b907_selector.py` |
| 17 | Rational atoms + I = −1 | `frontier/B908_exactness_pin` | `tests/test_b908_pin.py` |
| 18 | Unified ℤ₂ law; atoms; AG(2,3) | `frontier/B906_flavor_verification` | `tests/test_b906_flavor.py` |
| 19 | Signature split (15,12) | `frontier/B912_norm_cell` | `tests/test_b912_norm.py` |
| 20 | Generation-shape (outcome A, fenced) | `frontier/B897_27_under_g20` | `tests/test_b897_g20.py` |
| 21 | Inter-breaking laws | `frontier/B885_interbreaking` | `tests/test_b885_interbreaking.py` |
| 22 | Matter pencil | `frontier/B886_matter_pencil` | `tests/test_b886_matter_pencil.py` |
| 23 | Annihilation theorem | `frontier/B902_knus_paques` | `tests/test_b902_kp.py` |
| 24 | One-class + numerator law | `frontier/B910_kappa_class` | `tests/test_b910_kappa.py` |
| 25 | One-number table T | `frontier/B914_ratio_table` | `tests/test_b914_table.py` |
| 26 | λ = 1; twist-norm law | `frontier/B916_lambda_bridge` | `tests/test_b916_bridge.py` |
| 27 | Product law; prime biography | `frontier/B917_value_arc_verification` | `tests/test_b917_value_arc.py` |
| 28 | Observer's-place theorem | `frontier/B918_v_kummer` | `tests/test_b918_v.py` |
| 29 | Exactification; hierarchy carrier | `frontier/B923_exactification` | `tests/test_b923_exact.py` |
| 30 | Coupling rigidity | `frontier/B924_involution_couplings` | `tests/test_b924_rigidity.py` |
| 31 | D₂ characterization (Thm E) | `frontier/B928_d2_decode` | `tests/test_b928_decode.py` |
| 32 | CMT; six-cubic law; invisible 12 | `frontier/B909_frame_arc` | `tests/test_b909_frame.py` |
| 33 | 3/8 trace ratio (one-prime tier) | `frontier/B919_weinberg_traces` | `tests/test_b919_traces.py` |
| 34 | Crossing 1 (sealed negative) | `frontier/B915_the_crossing` | `tests/test_b915_crossing.py` |
| 35 | Crossing 2 (sealed negative) | `frontier/B925_second_crossing` | `tests/test_b925_crossing2.py` |

*(All arc directories and lock files verified to exist at skeleton time.
CLAIMS.md rows P69 (Thm A) and P70 (Thm B) are the banked claim registers for
the two headline theorems. The 27 itself is built in `frontier/B883_the_27`,
cited where §8 needs it.)*

---

## 4. Figures list

| Fig | Content | Source data |
|---|---|---|
| 1 | **The cascade ladder**: 78 → 46 → 14 (𝔢₆ → so(10)⊕u(1) → su(3)⊕su(2)⊕u(1)³), the three Galois-conjugate first breakings drawn as one triple, the skipped 26 = su(5)⊕u(1) marked with a strike | Thm A, Thm C |
| 2 | **The (x₈,x₁₆)-plane stratification**: strata 12 / 30 / 46, the three μ-root lines as the S₃ orbit | B866/B877 |
| 3 | **The tiling**: core so(8)⊕u(1)² + three 16-tiles with the cyclic bracket law [Vᵢ,Vⱼ] = V_k drawn as a 3-cycle | B875/B877 |
| 4 | **The magic square**: M(𝕆,ℂ) with the sector Hom-matrix diag(4,4,4) and the φ-isomorphism arrow to the Chevalley frame | B880/B904 |
| 5 | **The four-column concordance table** (rendered as a figure): measured/unmeasured × exponents (4,8)/(7,11) × τ-sign × split/compact | B894/B898 |
| 6 | **The ε-pattern census**: 16 patterns, the 12 killed by sign-locking shaded, the unique wall pattern (−1,+1,−1,+1) marked, the two e₆(2) representatives | B907 |
| 7 | **The 15 atoms**: the tri-partition; the colorless 3×3 grid with row/column transversal pencils (AG(2,3)); the K₃,₃ | B906/B908 |
| 8 | **The Klein group on the 27**: {I, D₂, D, D₂D} = ±ρ₂₇({1, σ_χ₋, σ₋₁, σ_χ₊}), with H₊/H₋/H′ attached to their conjugations | B928 |
| 9 | **The compact chain**: E₆ ⊃ D₅ ⊃ D₄ ⊃ D₃ ⊃ A₂ with the CMT centralizer types | B909 |
| 10 | *(Discussion only, owner-gated since it renders measured data)* the first crossing's failure triangle | B915 |

---

## 5. Drafting notes (for the next pass; not paper content)

- Per `WORKING_RULES.md` rule 10, when this skeleton is banked the PR must
  update PROGRESS_LOG + CHANGELOG + CAMPAIGN_STATUS. Banking is the banking
  seat's step, not this drafting pass's.
- The title's knot attribution needs the owner's call (§1 bullet 3); the
  neutral fallback title is in `ABSTRACT_DRAFT.md`.
- Theorem numbering A–E here is skeleton-local; the paper will interleave
  lemmas (the weight-line lemma, the one-prime lemma, the torsor theorem
  deserve displayed statements of their own).
- Nothing in this file may acquire an absolute machine path; all paths are
  repo-relative.
