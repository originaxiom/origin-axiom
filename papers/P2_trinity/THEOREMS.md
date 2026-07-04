# PAPER 2 — the theorem spine (precise statements + proof sketches, lock-backed)

## §2. The Cornerstone

**Theorem 1 (Double uniqueness → the seam field).**
The figure-eight complement S³∖4₁ is (a) the mapping torus of A = [[2,1],[1,1]] ∈ SL(2,ℤ),
the golden Anosov automorphism of the once-punctured torus, and (b) the unique arithmetic
knot complement, with invariant trace field ℚ(√−3). Consequently its two canonical fields —
the dynamical field ℚ(√5) = ℚ(A's eigenvalues φ^{±2}) and the geometric field ℚ(√−3) —
generate ℚ(√5,√−3), which is the Hilbert class field H of ℚ(√−15), with √5·√−3 = √−15.

*Proof sketch.* (a) is the standard fibering of 4₁ (Cooper–Long; B67). (b) is Reid (1991):
4₁ is the unique arithmetic knot; its trace field is ℚ(√−3). The eigenvalues of A are
φ²,φ^{−2} ∈ ℚ(√5). ℚ(√−15) has discriminant −15 = (−3)(5), class number 2; its genus field
= Hilbert class field = ℚ(√−3,√5) (genus theory). ∎ [Fact (a) lock: B67; (b) Reid 1991.]

## §3–5. The seven-face dictionary

Throughout, A = [[2,1],[1,1]], φ² = A's Perron eigenvalue, F_n / L_n Fibonacci / Lucas.

**Theorem 2 (dynamics).** The trace-map flow of 4₁ on its SL(2,ℂ) character variety is
Anosov with Lyapunov spectrum {0, ±4 log φ} at the discrete faithful point and conserved
invariant κ = tr[a,b]. [lock: test_b416]

**Theorem 3 (symbolic).** The substitution σ:a↦ab, b↦a (whose incidence matrix is A) has
Sturmian subshift: complexity p(n)=n+1, topological entropy 0, gap-labelling group ℤ+ℤφ.
[lock: test_b417]

**Theorem 4 (torsion = periodic orbits — the hinge).** The regularized E₆-adjoint
Reidemeister torsion of 4₁ at the discrete faithful representation is
    τ(E₆) = ∏_{i∈exp(E₆)} τ_{m_i},  τ_m = ∏_{j=1}^{m}(2 − L_{4j}) = ∏_{j=1}^{m}(−5 F_{2j}²),
and 5 F_{2j}² = |det(A^{2j} − I)| = #Fix(A^{2j}). Hence τ(E₆) = ∏(−#Fix(A^{2j})) over the
E₆ exponents: **the adjoint torsion is the golden cat map's periodic-orbit product.**
Its prime content is the Fibonacci apparition primes {2,3,5,7,11,13,17,19,29,41,47,89,199}.
*Proof sketch.* 𝔢₆ = ⊕Sym^{2m_i} over exp(E₆)={1,4,5,7,8,11} (B347: dim H¹=1 per summand).
det(I−Sym^{2m}A) has the invariant vector removed (the H¹=1 direction), leaving
∏_{k≠m}(1−φ^{4(m−k)}) = ∏_{j=1}^m(1−φ^{4j})(1−φ^{−4j}) = ∏(2−L_{4j}); the identity
2−L_{4j} = −5F_{2j}² = −|det(A^{2j}−I)| is classical. ∎ [lock: test_b423, test_golden_cat_map_principle]

**Theorem 5 (Hessian).** The Chern–Simons Hessian spectrum on H¹(4₁,𝔢₆) is the six per-
exponent torsions {τ_{m_i}} (∏ = τ(E₆)); it is Fibonacci-golden and no pairwise ratio equals
an SM mass ratio (exact, within 2%). [lock: test_b424]

**Theorem 6 (quantum invariant).** The Kashaev invariant ⟨4₁⟩_N satisfies
2π log⟨4₁⟩_N/N → Vol(4₁) (volume conjecture regime) and ⟨4₁⟩_N ∈ ℚ(ζ_N)⁺ with nonzero
ℚ(√5)-part exactly when 5|N (⟨4₁⟩₅ = 46+2√5). [lock: test_b384, test_b419]

**Theorem 7 (measure).** The level-N single-seed value distribution refines to a measure on
lim(ℤ/3ᵏ×ℤ/5) whose continuum limit is a Gauss-sum-modulated Haar measure (Fourier
magnitude ≡ mass; phase an exact ℤ[ζ₉] Gauss sum of norm 9). [lock: test_b413, test_b415]

**Theorem 8 (L-function).** entropy = 4·Reg(ℚ(√5)) = 2√5·L(1,χ₅); L(1,χ₋₁₅)=2π/√15; and
ζ_H = ζ·L(χ₋₃)·L(χ₅)·L(χ₋₁₅) — one factor per program pillar. [lock: test_b420, test_b401]

## §6. The walls as correct properties (structural theorems, cited to Paper 1)

**Theorem 9 (no scale).** Every internal value channel contracts up the tower; the tower-
measure is flat. Hence the object emits only dimensionless quantities. [lock: test_b408,
test_b413] **Theorem 10 (no frame).** The golden and ℤ/3 sectors are exactly orthogonal in
the shared W₂-label space under both the ℤ/3 and ℤ/2 (class-group) structures; no canonical
frame exists in the object. [lock: test_b400, test_b422]

**Corollary (the honest boundary).** 4₁ is the unique geometric realization of the arithmetic
of the golden×Eisenstein compositum ℚ(√−15); its invariants are that arithmetic, in seven
languages. It provides neither a scale nor a frame because a number is dimensionless and its
genus characters are independent — the walls are the arithmetic's own properties.
