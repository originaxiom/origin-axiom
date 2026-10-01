# B1511 PREREGISTRATION — THE PROJECTIVE TOWER: B1509's rank-five extension on the audit lane's harmonic family, carried to m004's finite cyclic covers and twisted by the characters of their fibre torsion. What does it count on each level, by deck orbit, and does any orbit of three count three?

**Sealed 2026-10-01, before any twisted polynomial of a non-trivial character is computed. Seat: cc (the SM-derivation branch).
Occasion: the owner's "aproved. next!", approving B1509's lead 4 (FINDINGS §8: "Pull W₁ back to the family's finite covers … and
read the index and the deck orbit in B1506's frame").**

## 0. The question

B1509 found one 10′ on m004: on the audit lane's harmonic vacuum A ⊕ 1, A = μρ_q (Ballas' projective holonomy with a central twist),
the non-split extension W₁ = [[A, c], [0, 1]] has main's index −1 exactly at q = 17 ± 12√2 with μ = −1, because there the twisted fibre
monodromy has a Jordan block. B1509 §5 closed with "One per background … Three would need covers or several states (lead 4)".

This arc takes the same construction to every cyclic cover Mₙ of m004 (n = 1 … 6; M₂ = m206, M₃ = s961), in B1506's frame: a
background on Mₙ is ν ⊗ ρ_q for a character ν of π₁(Mₙ), the root's deck ℤ/n acts on backgrounds, and an orbit of size k counts
gcd(n, k) times its member's count on Mₙ (B1506 T7). It asks:
- **Q1 (the pullback).** What does B1509's W₁ count on each level, and what is its deck orbit? *(Decided at design time: −1 on every
  level, orbit of size one; Theorem D.)*
- **Q2 (three).** Does any deck orbit of size three on s961 have every member counting ±1? That would be a projective triplet: three
  on s961 and on M₆. *(Open: the census of the five orbits of size three, §6.2.)*
- **Q3 (each level).** On levels 1–6, which twisted rank-five extensions count at all, and with which orbit sizes? *(Reduced at
  design time to two mechanisms, Theorems A and F, and then read from the census.)*

## 1. Setting and notation

- **The group and the fibre.** π = ⟨m, n | mnMNmNMnmN⟩, with meridian m and longitude ℓ = nMNmmNMn (B1509; B1374's index_lib).
  - The fibre group is F = ⟨x, y⟩, free, with x = u₀ = nm⁻¹ and y = u₁ = mnm⁻² (uₖ = mᵏnm⁻⁽ᵏ⁺¹⁾).
  - The monodromy is φ(g) = mgm⁻¹: φ(x) = y, φ(y) = yx⁻¹y². Abelianised, Φ = [[0, −1], [1, 3]], with characteristic polynomial
    x² − 3x + 1 (B1509 T3).
- **The levels.** Mₙ is the n-fold cyclic cover, π₁(Mₙ) = F ⋊ ⟨z⟩ with z = mⁿ acting by φⁿ.
  - The torsion of H₁(Mₙ) is Tₙ = coker(Φⁿ − 1), of orders 1, 5, 16, 45, 121, 320 for n = 1 … 6 (B1506).
  - Its invariant factors are (), (5), (4, 4), (3, 15), (11, 11) and (8, 40). The cusp of Mₙ is connected, with peripheral group
    ⟨z, ℓ⟩.
  - The instrument uses B1506's Reidemeister–Schreier presentation (rebuilt here in the letters m, n and checked equal to B1506's), with
    meridian z and the longitude rewritten from coset 0.
- **Characters and the deck.**
  - A character of π₁(Mₙ) is ν = (ν_F, λ). Here ν_F is a character of F^ab fixed by Φⁿ, that is a character of Tₙ, and λ = ν(z).
  - In exponent form ν_F(x) = ζ_N^a and ν_F(y) = ζ_N^b, where N is the exponent of Tₙ.
  - The root's deck τ (conjugation by m) acts by (a, b) ↦ (b, 3b − a) and fixes λ.
- **Backgrounds.** V = ν ⊗ ρ_q, with V(g) = ν_F(g)ρ_q(g) on F and V(z) = λρ_q(m)ⁿ. Here q > 0 and q ≠ 1 (B1509's family; q = 1 is
  the hyperbolic point and is excluded throughout).
- **Rank-five extensions (the determinant-one frame of B1509's Corollary C).**
  - W₁-type: W = [[V, c·L], [0, L]], with V as sub and the line L = ν⁻⁴ as quotient, and c ∈ Z¹(V ⊗ L⁻¹). Here V ⊗ L⁻¹ = ν⁵ ⊗ ρ_q.
  - W₂-type: the opposite order, read through its dual, which is W₁-type for the dual family ν⁻¹ ⊗ ρ_q*.
  - The SU(5)′ dictionary is B1509's: N(10′) = −I(W) and N(5̄′) = −I(Λ²W).
- **The fibre monodromy.** For any character ν_F of F^ab, the map (S c)(g) = ρ_q(m)⁻¹c(φ(g)) sends Z¹(F; ν_F ⊗ ρ_q) to
  Z¹(F; (ν_F∘φ) ⊗ ρ_q) and coboundaries to coboundaries.
  - In the coordinates (c(x), c(y)) it is S_ν = [[0, A₁], [−αA₂, A₁ + αA₂ + βA₃]], with α = ν_F(y)/ν_F(x) and
    β = ν_F(y)²/ν_F(x).
  - Here A₁ = ρ_q(m)⁻¹, A₂ = A₁ρ_q(y)ρ_q(x)⁻¹ and A₃ = A₂ρ_q(y). Their entries are Laurent polynomials in q with exponents in
    [−2, 2] (control C7).
  - Around a level, S⁽ⁿ⁾_ν = S_{ν∘φⁿ⁻¹} ⋯ S_ν.
  - P_ν(q, s) is its characteristic polynomial on H¹(F; ν_F ⊗ ρ_q) = Z¹/B¹: monic of degree 4 in s.
- **Main's index.** I(V) = n(V) − n(V*), with n(V) = dim ker(H¹(Mₙ; V) → H¹(T; V)) (B1297/B1418).
  - The data are (a0, a1, t0, r1) for V and (b0, b1, s0, q1) for V*.
  - Every reading asserts the annihilator identity r1 + q1 = t1 = s1 and the B1297 identity I = (a0 − b0) + s0 − r1.

## 2. Computed before the seal (disclosed)

`verification/controls.py --record` → `verification/controls_run.txt`. No control computes a twisted polynomial of a non-trivial
character, an exceptional point of one, or the index of a twisted extension.
- **C1 — level one, ν = 1.** The characteristic polynomial of S on H¹(F; ρ_q) is B1509's monic Q(q, s) (symbolic q); S·B = B·ρ(m)⁻¹;
  and the one-step matrix equals the direct computation from the words.
- **C2 — level three, ν = 1.**
  - The product of three one-step matrices equals the computation from the words φ³(x), φ³(y).
  - Its polynomial on H¹ is ∏(s − r³) over the roots r of Q (the cube relation), symbolic in q.
- **C3 — torsion and orbits (B1506, banked).** |Tₙ| and the invariant factors as in §1.
  - Orbit sizes under the root's deck: M₂ 1 + 2·2; s961 1 + 5·3; M₄ 1 + 2·2 + 10·4; M₅ 1 + 24·5; M₆ 1 + 2·2 + 5·3 + 50·6.
  - T₃ = (ℤ/4)². Its orbits are the trivial character, one orbit of the three characters of order 2 (call it O₂), and four orbits of
    characters of order 4: O_A = {(1,0), (0,3), (3,1)} and its inverse Ō_A, and O_B = {(1,1), (1,2), (2,1)} and its inverse Ō_B.
- **C4 — the presentations.**
  - rs_cover(n) equals B1506's after renaming (relators, longitude, generator words, n = 1 … 6).
  - ρ_q satisfies every relator symbolically (n = 1, 2, 3).
  - The deck on the generators induces (a, b) ↦ (b, 3b − a) on every character (n = 2 … 6), equals B1506's closed form, and every
    character kills every relator.
- **C5 — B1509's rows, banked.** At the six points, on this arc's general-presentation index:
  - exactly over ℚ(i)[q]/(g) with g = q² − 34q + 1 and q² − 14q + 1, which covers both roots at once;
  - over GF(p) at p = 1009, 1033, 1129 and every root, through B1374's index_lib.
  The values I(W₁), I(W₂), I(Λ²W₁), I(Λ²W₂), the data of W₁ and W₁* and h¹ are B1509's: −1, +1, 0, 0 at μ = −1 and 0, 0, 0, 0 at
  ±i.
- **C6 — the pullback on s961 (Theorem D's instances).** Take ν_F = 1, λ₃ = −1.
  - At q² − 34q + 1 = 0: h¹ = 1 and I(W₁) = −1.
  - At q² − 7q + 1 = 0: h¹ = 2, from the simple roots e^{±iπ/3} of Q, and every class tried (c1, c2, c1 + c2) counts 0.
  - Both hold exactly and over GF(p) at every root.
- **C7 — the closed form.** S_ν above equals the Fox computation for symbolic character values X, Y. The Laurent ranges of A₁, A₂
  and A₃ are [0, 1], [−2, 1] and [−2, 2].
- **C8 — the GF(p) interpolation.** At levels 1–6 and two primes, interpolating q^{16n}P_ν(q, λ) at 32n + 1 points reproduces the exact
  untwisted q^{16n}∏_j(λ − r_jⁿ) for ν = 1 and every λ ∈ μ₄.
- **C9 — a dry run of the census code on instances decided at design time.**
  - Part A run on the trivial orbit of T₃ reproduces Theorem D. At every exceptional factor of every λ₃ ∈ μ₄, I(W₁) = −1 and
    I(W₂) = +1 only at q² − 34q + 1 with λ₃ = −1, and 0 elsewhere (exactly and over GF(p)).
    - Factors: λ₃ = 1 gives q² − 23q + 1; ±i give q² − 14q + 1 and q⁴ − 34q³ + 99q² − 34q + 1; −1 gives q² − 34q + 1 and
      q² − 7q + 1.
    - The untwisted level-three polynomial is palindromic in s, invariant under q ↦ 1/q, and equal to its own conjugate.
  - Part B run on those points: h¹ on M₆ equals Shapiro's sum over ±λ₃ at all seven, and the count on M₆ is −1 at the Jordan point and
    0 elsewhere.
  - The gcd machinery finds q² − 34q + 1 as the common factor of the untwisted level-2 and level-4 polynomials at λ = 1, and finds an
    untwisted coprime pair coprime.
  - The case-(b) counter, run on m004 itself (where L = ν⁻⁴ = 1 and ν⁵ = ν), returns B1509's −1 and +1.
  - Part C1's exact path over ℚ(ζ₁₂)(q), run on the trivial character at level 4, reproduces the untwisted level-4 polynomial. Its
    f(±1) are rational: (q − 1)²(q² − 34q + 1)(q² − 14q + 1)² and (q⁴ − 32q³ + 130q² − 32q + 1)².
  - The handler for an identically exceptional polynomial runs on the trivial orbit, where h¹ = 0 at q = 2, 3 and ½.
  - At the dry run's Jordan point the kernel dimensions of (S + 1)ʲ on H¹ are 1, 2, 2, 2. At its h¹ = 2 points they are 2, 2, 2, 2,
    which is semisimple.
- **C10 — the case-(b) classification (character arithmetic only).**
  - Orbits with ν_F⁴ ≠ 1: 2 on M₂, 12 on M₄, 24 on M₅, 52 on M₆.
  - Those with ν⁵ in their own deck orbit:
    - M₄'s two orbits of 3-torsion characters (size 4, closed under inversion);
    - M₅'s four orbits on the Φ-eigenlines (size 5, not closed under inversion);
    - M₆'s eight orbits of 2-power order 8 (size 6, not closed under inversion).
  - The pairs needing exact treatment (§3, Theorem F) are exactly M₄'s two 3-torsion orbits at λ = ±1. All other pairs (8, 44, 96 and
    208 on M₂, M₄, M₅ and M₆) go to the GF(p) gcd test.

**Disclosures.**
- The untwisted polynomial of level three and its exceptional set were computed (C2, C9). Theorem D decides them.
- Three instrument repairs were made before any sealed quantity existed:
  - DomainMatrix equality depends on the internal format, so relator checks failed on true identities. Fixed with format-free
    comparison.
  - sympy's fraction-free elimination needs exact division in ℚ(i)[q]; over ℚ(i)[q]/(g) it raised ExactQuotientFailed. Fixed with
    plain Gauss–Jordan using field inverses, over the extension and over GF(p).
  - The conversion into ℚ(ζ₁₂)[q]/(g) failed. Fixed with plain expression conversion.
- The case-(b) mechanism of Theorem A(v) was found in the design reasoning before any twisted polynomial existed: its sign is
  opposite, and for some orbits the coincidence it needs is automatic. It widened the sealed census to levels 2, 4, 5 and 6.

## 3. Proved now (design time)

**Theorem A (the count's shapes, every level).** Let n ≥ 1, q > 0, q ≠ 1, ν = (ν_F, λ) with ν_F of finite order, V = ν ⊗ ρ_q, and W a
determinant-one rank-five extension as in §1.
- (i) *V is boundary-acyclic.*
  - ℓ is a commutator in F: the fibre's boundary; MT's longitude is abAB. So every character is trivial on ℓ, and V(ℓ) has ρ_q(ℓ)'s
    eigenvalues q, q, q, q⁻³ (B1509's control), none equal to 1.
  - ℓ and z commute on T, so the Koszul complex is exact: H*(T; V) = 0. The same holds for V*, for Λ²V (eigenvalues q^{±2}) and for
    V ⊗ L.
- (ii) If L|_T ≠ 1, W is boundary-acyclic and I(W) = 0.
  - L(ℓ) = 1 always, so L|_T = 1 iff λ⁴ = 1.
  - Then L is of finite order, since L_F = ν_F⁻⁴ is.
- (iii) If W splits, I(W) = I(V) + I(L) = 0.
  - I(V) = 0 by (i).
  - For a finite-order line with L|_T = 1 and L ≠ 1, complex conjugation gives r1(L) = r1(L⁻¹) = q1(L). With r1 + q1 = t1 = 2 this
    gives r1 = 1, so I(L) = 1 − r1 = 0.
  - I(1) = 0 trivially.
- (iv) **Case (a): L = 1** (equivalently ν⁴ = 1), W₁ = [[V, c], [0, 1]] with c ≠ 0 in H¹(V). Then I(W₁) = −r1 ∈ {0, −1}, and I = −1 iff
  e ∪ c = 0 in H²(Mₙ; V), where e generates H¹(Mₙ; ℂ). This is B1509 T2's proof, for any h¹(V):
  - a0 = 0, because 1 ↦ c in H¹(V);
  - b0 = 1, because the trivial line is a sub of W₁*;
  - s0 = 1;
  - H¹(W₁) → H¹(T) factors through H¹(Mₙ; ℂ) = ℂe, which restricts injectively, and its image there is ker(∪c).
  The W₂-type count is r1 of the dual-family W₁, in {0, +1}.
- (v) **Case (b): L ≠ 1 with L|_T = 1** (λ⁴ = 1, ν_F⁴ ≠ 1). Here h¹(Mₙ; L) = 1: B1506 T1 and B1381, with L non-trivial on the fibre
  and L(z) = 1. For W₁ with c ∈ H¹(ν⁵ ⊗ ρ_q):
  - a0 = b0 = 0 and s0 = 1.
  - H¹(W₁) → H¹(T; W₁) ≅ H¹(T; L) factors through H¹(Mₙ; L) = ℂx, where x|_T ≠ 0 by (iii).
  - Its image in H¹(L) is ker(∪c: H¹(L) → H²(Mₙ; V)).
  - Hence **I(W₁) = 1 − r1 ∈ {0, +1}, and I = +1 iff x ∪ c ≠ 0.**
  This needs H²(Mₙ; V) ≠ 0, that is h¹(Mₙ; ν ⊗ ρ_q) ≥ 1 (χ = 0, H⁰ = 0), at the same q as h¹(Mₙ; ν⁵ ⊗ ρ_q) ≥ 1. The W₂-type count is
  in {0, −1}. Case (b) has the opposite sign to case (a).
- (vi) Λ²W is filtered by Λ²V and V ⊗ L, both boundary-acyclic by (i). So **I(Λ²W) = 0 on every level, and no 5̄′ arises anywhere in
  the tower** from this family.
- (vii) |I(W)| ≤ 1. (Main's B1440 gives |I| ≤ min(r, n − r) ≤ 2 in rank five; (iv) and (v) are sharper.)

**Theorem B (Wang on the covers; orbit invariance).** Assume H⁰(F; ν_F ⊗ ρ_q) = 0 (checked at every point read).
- H¹(Mₙ; V) = ker(λ⁻¹S⁽ⁿ⁾_ν − 1) and H²(Mₙ; V) = coker(λ⁻¹S⁽ⁿ⁾_ν − 1) on H¹(F; ν_F ⊗ ρ_q). Cup with e is the natural map
  ker → coker.
- So in case (a), I(W₁) = −1 iff c lies in ker ∩ im(λ⁻¹S − 1), the Jordan part. When h¹ = 1, that happens iff the eigenvalue λ of
  S⁽ⁿ⁾ has a Jordan block.
- S_ν S⁽ⁿ⁾_ν = S⁽ⁿ⁾_{ν∘φ} S_ν with S_ν invertible, so P_ν is an invariant of the deck orbit.
- The index is deck-invariant: τ is an automorphism of π₁(Mₙ) that carries the background ν to ν∘τ and the peripheral subgroup to a
  conjugate.
- For an orbit of size k dividing n, S⁽ⁿ⁾ = (S⁽ᵏ⁾)^{n/k}.

**Theorem C (which case occurs on which level).**
- L|_T = 1 forces λ ∈ μ₄. Case (a), ν_F⁴ = 1, occurs on levels 1–6 only for:
  - the trivial character, on every level;
  - T₃'s sixteen characters, on levels 3 and 6.
- The reason: |Tₙ| is odd for n = 1, 2, 4, 5, and the 4-torsion of T₆ ≅ ℤ/8 × ℤ/40 is (ℤ/4)². That is T₃'s character group pulled
  back, since im(Φ⁶ − 1) ⊂ im(Φ³ − 1).
- Every other character with λ ∈ μ₄ is case (b).

**Theorem D (the pullback: Q1).** Let ν_F = 1. Then V is the pullback of μρ_q from m004, for every μ with μⁿ = λ.
- Shapiro gives H*(Mₙ; V) = ⊕_{μⁿ = λ} H*(m004; μρ_q), compatibly with restriction to the connected cusp and with e (e pulls back to
  a multiple of e).
- Hence h¹ = #{μ : μⁿ = λ, Q(q, μ) = 0}, each root contributing 1 (B1509), and e ∪ c = 0 iff every non-zero Shapiro component of c
  sits at a double root of Q(q, ·).
- Q is palindromic, Q = s²P(s + 1/s), and the discriminant of P in x is 4q(q + 1)² ≠ 0. So double roots occur only at s = ±1. Since
  Q(q, 1) = (q − 1)², that leaves s = −1 at q = 17 ± 12√2.
- So the count is −1 (W₁-type) and +1 (W₂-type) exactly at q = 17 ± 12√2 with λ = (−1)ⁿ and c in the μ = −1 component, and 0 at
  every other (q, λ, c). That includes every point with h¹ = 2, e.g. q = (7 ± 3√5)/2 with λ₃ = −1.
- These backgrounds are fixed by the deck. **B1509's W₁ counts −1 on every level with a deck orbit of size one**: one per level, never
  three. This is B1506 T2 ("a pullback keeps the index") for this family.

**Theorem E (where three can come from: Q2).** Three, as a single level's count of one deck orbit of honest backgrounds, needs:
- |I| = 1 per member, by A(vii);
- an orbit of size 3, by B1506's level law, with gcd(n, k) = k = 3.
Orbits of size 3 exist exactly on M_{3j}, and their ν_F are T₃'s characters: ν_F∘φ³ = ν_F. So they are case (a), and the mechanism is
the Jordan block (Theorem B).
- By Shapiro the count of a pulled-back member on M_{3j} is Σ_{λ₃^j = λ_{3j}} I_{s961}(ν_F, λ₃), and only λ₃ ∈ μ₄ contributes, by
  A(ii).
- **So the census of s961's five orbits decides three on every level M_{3j}.**
- Orbits of size six on M₆ restrict to three objects on s961, but those are induced from M₆ and are not backgrounds of s961 (B1506 §5).
  They are case (b) and appear in Part C.

**Theorem F (case (b): where its coincidence is automatic).** By A(v), a +1 needs the background ν and ν⁵ exceptional at the same q.
- If ν⁵ is in ν's deck orbit, Theorem B makes this automatic. On levels ≤ 6 that happens exactly for (C10 lists them):
  - M₄'s 3-torsion characters: Φ² ≡ −1 on T₄[3], so ν∘φ² = ν⁻¹ = ν⁵;
  - M₅'s characters on the two Φ-eigenlines of T₅ = 𝔽₁₁², with eigenvalues 5 and 9 = 5⁻¹, so ν∘φ^{±1} = ν⁵;
  - M₆'s characters of 2-power order 8: Φ³ ≡ 5 mod 8, so ν∘φ³ = ν⁵.
- f_{O,λ} = P_O(q, λ) has real coefficients when O is closed under inversion and λ = ±1. Then real roots are generic.
  - That holds for M₄'s two 3-torsion orbits.
  - It fails for M₅'s eigenline orbits: −1 is not a square mod 11.
  - It fails for M₆'s order-8 orbits: no element of ⟨Φ⟩ acts as −1 there. Φ, Φ², 5Φ and 5Φ² have no eigenvalue −1 even mod 2.
- Hence **case (b) can fire at generic real q only on M₄'s two 3-torsion orbits at λ = ±1** (Part C1). Everywhere else it needs a
  non-generic coincidence: common roots of f_{O,λ} with f_{O⁵,λ}, or for self-coincident complex orbits with f_{O⁻¹,λ⁻¹}. Part C2
  tests these.

## 4. BANKED IDENTITY:

Before any new number is read, the sealed run's own instrument has reproduced:
- B1509's index rows at the six points, exactly and over GF(p) (C5);
- B1509's monic Q at level one (C1), and the cube relation at level three (C2);
- B1506's torsion, orbits, presentations and deck (C3, C4);
- Theorem D's decided instances on s961 and M₆ through the census code itself (C6, C9).

The census run (§7) re-checks C1 and C5's first row before reading Part A, and stops if either fails. Every index reading asserts the
annihilator identity and the B1297 identity.

## 5. PRIOR ART:

### 5.1 The repository

A read-only sweep covered main (7f080e49), this branch (fa44786e), the audit lane (audit/physical-bridge-2026-09-05 at 472a9595), the
paper-review lane (…/paper-review-verification-kaz3f5), outside-bench, the physics seat and sep16-branch.

Patterns searched: twisted Alexander, Alexander polynomial, fibre/fiber monodromy, Ballas, ρ_q, projective with cover, s961, m206, ℤ/4,
T₃, order-4 character, deck orbit, triplet, three generations, generation with cover, Jordan block, the 17 ± 12√2 forms, palindromic.

**No ref computes:**
- the twisted fibre monodromy of Ballas' ρ_q for any character of a cover's fibre torsion;
- ρ_q on any cover;
- main's index of a twisted rank-five extension on any Mₙ.

**This branch.**
- **B1509** (67eb88ad; order record 3edaf1fa) has Q(q, s) and S_ρ on m004 with central twists only. Its lead 4 is this arc.
- **B1506** (sealed 58e3f28f) is the Standard-Model-frame census of M₁–M₆: rank-two doublet modules, s961's 16 orbits of three, the
  level law, T7.
- **B1375** counted lifted backgrounds only. **B1510** is on m004 only.
- **B1280** (c3c3a8ed) uses the same Wang reduction, h¹(Mₙ; V) = dim ker(Φⁿ − 1), for SL(3) W₁/W₂ with central twists.

**The audit lane.**
- **R42** (AFFINE_BACKGROUND.md:11–13, a3a8dfcd; PROOF.md:121–122, :167–169, ecd6e70e) gives the harmonic background for "Ballas'
  nearby projective family and its finite covers". It computes no cohomology, index or characters on any Mₙ.
- **The counts on covers are recorded as owed:**
  - CANONICAL_CUSP_PROOF.md:314–315 (f52629a8): "their counts must be computed for their own group";
  - received projective_global_metric PROOF.md:184–186 (ab9f072a): "Cover multiplicities still need their own cohomology
    computation";
  - received_r47 F14_FINDINGS.txt:161–162 (8f493e68).
- **R54–R56** are on m004 (R55: "one finite-norm neutral mode, not three").
- **R74** (472a9595) is a split Λ²(4 + 1) on a local cone, "not a generation".
- **R69** (LEVEL_ACTION.md:14–20) recomputes B1506's D₀ counts (−1, −1, −3, −1, −1, −3), in rank two.
- **Described there but not in this repository:** another fork's F18 ("an all-degree cyclic-cover, all-mu4-character pairing at the
  exceptional points", GOD_PARTICLE_READING_2026_09_25.md:136–138, 81ae3441) and F17 (CANONICAL_DUALITY.md:71). Both are central μ₄
  twists with a vector-like result. They use no fibre-torsion characters and no extension. Not read.

**Main.**
- **S30/B1441** (05e82020): 564 742 rank-two modules on 74 several-cusped manifolds. Seventeen covers of m009/m010 count two; none
  counts three; "no cover of the root reaches two". m206 and s961 appear only as controls.
- **B1442** (7f080e49): sealed, not run, rank two. Out of scope there: "three; … modules of rank above two".
- **L234**: "Three. It needs three live cusps".
- **B1440**: |I| ≤ min(r, n − r), and "Three needs rank six".
- **B1418**: s961 0 of 2 511, in rank two.
- **B1427, B1432/B1434, B1435/B1438**: rank-two orbits of three, "one generation three times".
- None uses ρ_q or rank five on a cover.

**The other refs.**
- Paper-review computes rank-one h¹(χ²) on covers to degree 8.
- sep16's xB009/xB011 compute twisted Alexander polynomials of Symⁿρ_geo with no covers.
- Outside-bench and the physics seat predate the family.

*Novelty, as far as this sweep reaches:*
- Theorem A(v)–(vi) (case (b) and its sign; no 5̄′ anywhere in the tower);
- Theorem F's classification;
- every computation in §6.

### 5.2 The literature

- **Twisted Alexander polynomials of fibred manifolds.** Wada's polynomial of a fibred 3-manifold is the characteristic polynomial of
  the monodromy on the twisted homology of the fibre (Yamaguchi, arXiv:math/0311155). B1509 T3 used this at level one, and C1/C2 check
  it.
- **Systematic twisted-Alexander computations:** Dunfield–Friedl–Jackson, arXiv:1108.3045.
- **arXiv:2411.04431** (projective rigidity of once-punctured torus bundles via the twisted Alexander polynomial) relates the twisted
  polynomial to the monodromy action on the tangent space of the PGL(4, ℝ) character variety of F₂. That is the adjoint, at the
  geometric point. It does not twist ρ_q by finite characters of covers, and it computes no index.
- **Ballas**, "Finite volume properly convex deformations of the figure-eight knot", is the family itself, as the audit lane cites it
  (AFFINE_BACKGROUND_PRIOR.md:70–72).
- **Heusener–Porti 2015** (B1510 §5.2) covers deformations of reducible representations at simple roots, not main's index.

None of these computes main's index on covers, or reads deck orbits.

## 6. What the sealed run reads

### 6.1 Decided at design time (computed as checks; a failure refutes a step above)

- **D1** — the deck invariance of P_O: the three members of each orbit have the same polynomial (Theorem B).
- **D2** — at every point read, rank B = 4, so H⁰(F) = 0. And h¹ (direct, on the presentation) equals dim ker(S − λ) on H¹ (fibre).
- **D3** — every direct count satisfies the annihilator and B1297 identities, and lies in {0, −1} (W₁) or {0, +1} (W₂) in case (a),
  and in {0, +1} (W₁) or {0, −1} (W₂) in case (b) (Theorem A).
- **D4** — I(Λ²W) = 0 at every point read (Theorem A(vi)).
- **D5** — in case (a), I(W₁) = −1 for a class c exactly when the fibre data put c in the Jordan part. With h¹ = 1, that is exactly
  when dim ker(S − λ)² > dim ker(S − λ) (Theorem B).
- **D6** — Part B: h¹ on M₆ equals h¹(λ₃) + h¹(−λ₃) from the fibre, and the M₆ count of the pulled-back class equals the s961 count
  (Shapiro).
- **D7** — C10's classification is reproduced inside the run: the exact pairs are M₄'s 3-torsion orbits at λ = ±1, and nothing else.

### 6.2 Sealed predictions (open)

Priors are mine at the seal.
- **P1 — O₂'s polynomial is palindromic in s** (~80%). Whatever symmetry makes Q palindromic maps the set of order-2 characters to
  itself. Then P_{O₂}(q, ±1) = 0 forces a double root at ±1.
- **P2 — O₂ fires: a projective triplet on s961** (~40%). At some q > 0, q ≠ 1 and λ₃ ∈ μ₄, each of O₂'s three members has
  I(W₁) = −1 for some class and I(W₂) = +1. That is three on s961 and three on M₆ (Theorem E).
- **P3 — no orbit of order-4 characters fires on s961** (~85%). Their polynomials are complex, so a real double root is non-generic.
- **P4 — some order-4 orbit is exceptional (h¹ ≥ 1) at some positive q ≠ 1** for some λ₃ ∈ μ₄ (~60%).
- **P5 — Shapiro on M₆** (~97%): every Part-B row agrees with D6.
- **P6 — case (b) fires on M₄** (~35%). At some positive q ≠ 1 and λ = ±1, a 3-torsion orbit's four members each have I(W₁) = +1 for
  some class. That is four 10̄′ on M₄, one per member, read with N(10′) = −I.
- **P7 — Part C2 finds no coincidence** (~85%). Every gcd pair, at all three primes, has no common root other than q ∈ {0, 1}.
- **P8 — no orbit of s961 is identically exceptional** (~90%). P_O(q, λ) ≢ 0 for every O and λ.

## 7. The instrument (after the seal)

`verification/tower_census.py --record` → `verification/tower_census_run.txt`. The library is `verification/tower_lib.py`.

**Part A (s961).** For every member of the five orbits:
- P(q, s) exactly over ℚ(i)(q), its symmetries, and the generic rank of B.
- For each λ ∈ μ₄, the real exceptional locus gcd(Re f, Im f) of the numerator f of P(q, λ), and its factors over ℚ.
- At every factor g₀ with a positive root q ≠ 1, the exact fibre data in ℚ(i)[q]/(g₀) (rank B, and dim ker(S − λ)ʲ for j = 1 … 4
  at λ and at −λ).
- The direct counts for every member (h¹, every basis class and c1 + c2, W₁, Λ²W₁, W₂, Λ²W₂):
  - exactly when deg g₀ ≤ 8;
  - over GF(p) always, at the three smallest primes p > 1000 with p ≡ 1 mod 4 at which g₀ is squarefree with a root, at every
    root.
- If some P(q, λ) vanishes identically: the generic kernel dimensions, and the exact counts at q = 2, 3, ½.

**Part B (M₆).** Every Part-A point, the first member pulled back (λ₆ = λ₃²), over GF(p) by the same rule: h¹ and the counts.

**Part C2.** Levels 2, 4, 5, 6, every orbit with ν_F⁴ ≠ 1, every λ.
- q^{16n}P(q, λ) over GF(p), by interpolation at 32n + 1 points.
- The primes are the three smallest p > 1000 with p ≡ 1 mod lcm(4, N): 20, 60, 44 and 40.
- The gcd with the partners; then the multiplicities of q and q − 1, and the degree of what remains.

**Part C1.** M₄'s exact pairs:
- P exactly over ℚ(ζ₁₂)(q), and f = P(q, ±1), which must be rational.
- At every factor with a positive root q ≠ 1:
  - the fibre data exactly;
  - the case-(b) direct counts for all four members, over GF(p) at three primes p ≡ 1 mod 12 (every root), and exactly when
    deg g₀ ≤ 4.

**Part D.** The per-level table, by orbit size.

## 8. Reading rules, and what this arc will and will not claim

- **Reading rules.**
  - A count is read only when every prime–root pair agrees, and agrees with the exact value where one is computed.
  - A disagreement is reported as a GF(p) rank drop when it occurs at one prime and agrees elsewhere. Otherwise it is reported as a
    genuine difference, B1374's convention.
  - "Fires" means a non-zero count for some class at some positive q ≠ 1 with λ ∈ μ₄.
  - A non-trivial Part-C2 gcd (after q and q − 1) at all three primes is reported as UNRESOLVED and registered as a lead. It is not
    counted either way.
  - A NO on P2 (no projective triplet) and the absence of a 5̄′ (Theorem A(vi)) together form the no-go half. They are routed to the
    kill graph as a NEGATIVE arc.
- **Will claim:**
  - Theorems A–F as proved;
  - the census as computed, with its precision stated: exact or GF(p);
  - the per-level table.
- **Will not claim:**
  - a selection of q, of the level, or of an orbit;
  - a finite-energy background beyond R42's;
  - an end condition (main's interior index only);
  - a 5̄′;
  - that an orbit of three is three generations of one vacuum: B1506's fence, three distinct vacua, applies unchanged;
  - any physics beyond the SU(5)′ dictionary's count.
  - **I-26 stays UNEARNED; 0 of 19** unless a result here earns otherwise, which none of P1–P8 can.
