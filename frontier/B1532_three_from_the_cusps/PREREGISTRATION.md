# B1532 — PREREGISTRATION: THREE FROM THE CUSPS — sm:B1515's frame pulled back to every finite abelian cover of m004's levels M₂–M₆: does any cover carry three generations?

**Sealed before any twisted term of the population is read.** At the seal this arc has computed only:
- the banked identity: every χ = 1 term of M₂–M₆ in both routes against sm:B1515's census rows (§6 K1);
- quantities outside the population or about its structure: the shared labels (K2), Lemma Z on twists that are non-trivial on
  the cusp (K3), the subgroup counts (K4), route C's h¹ against banked h¹ sums (K5), the class structure (K6), the pencils'
  h¹ prediction at χ = 1 (K7), Lemma D on banked rows (K8), the conjugate-pair reader split at a square d₀ (K9);
- the design-time bound of §3 from banked h¹ only.

No term T(ν, χ, c) with χ ≠ 1 has been read. No χ = 1 term at an interior or special class has been read.

**Source.** The owner, 2026-10-03: "continue with the next arc". The arc was planned in the B1531 session, whose design note bounded the
covers of the silver squares (m135, m136) trivial on the cusp by two generations and left M₆'s covers open. Standing goal: the
Standard-Model derivation. Binding: "dont ignore anything loadbearing", "do it correctly, informedly, and bug free in all load
bearing math", "aleays verify, make sure we dont hit negatives because of bugs".

## 0. Seen first, and PRIOR ART:

**The repo sweep.** `git fetch --all` was run first (origin/main at b3565230; this branch at 9680728e). Then
`scripts/checks/prior_work.py` and `git grep` on every head, with these terms: "three from the cusps", "Shapiro", "trivial on the
cusp", "covers of M6", "(LR)^6", "induced background", "multi-cusp", "one background, one count", "R69", "fibre covers",
"pullback keeps".
- **Absent on every head:** F-HE read on any cover of a level; "covers of M6"; "fibre covers". The fibre-direction covers, which
  are trivial on the cusp, are new territory.
- **sm:B1506 T2 and main's T-THE-LEVEL ("a pullback keeps the index"; "one background, one count").** These concern twists by
  deck characters of the level tower, which move the meridian value off 1. In B1532 those terms vanish by Lemma Z. B1532 reads
  the complementary family, the characters trivial on the cusp, where the twisted terms survive.
  - R69 scoped "one background, one count" to rank-two T5 doublets.
  - An induced background counts −gcd(n, 3) on the levels (sm:B1506 RS3).
  - Direct image, pullback and quantum gauging are not interchangeable (R69, LEVEL_ACTION.md:50–53).
  - B1532 counts the pullback p*W on the cover, one rank-five F-HE vacuum of the cover state. It does not count Ind on the base.
- **sL-7, B1384 S3 and sm:B1506 (the scope fence).** "A three from a cover is a cover-resolution question, not a derivation."
  - A three found here is a three on that cover-state of X_gen (GENESIS §3's commensurability move makes every finite cover a
    state).
  - Which cover is physical stays open. That is sL-5's one bit, unchanged.
- **sm:B1377, sm:B1381 and main's B1427: |I| ≤ 2 in one F-CI doublet sector on the levels.** These differ in frame (F-CI), module
  (rank two) and covers (the level tower). Their logic gives no bound here.
- **sm:B1515: the frame, the members of M₁–M₆, routes T and L.**
  - Its census is the banked identity.
  - Its Lemma 3 (MFP), Lemma 7 (the mirror), Lemma 8 (the mechanism at a simple member) and Remark 9 (Λ_A ∩ π_A) are used or
    cited below.
  - Its FINDINGS: "By Shapiro they are interior classes of the geometric four on a finite abelian cover of M6". This is the
    four's interior classes, not the cover's count in F-HE.
- **sm:B1530 (sealed, census running): the interior extensions.**
  - Its Part A is m135. Its Parts B and C read population B and Λ_A ∩ π_A on the word states and M₂–M₆.
  - M₆'s 120 two-class members at their interior classes are in no sealed population before this one.
  - B1530's Part C reads the quantity that governs B1532's simple Λ² terms. It will be compared after both read-outs. It is not
    used.
- **sm:B1531: the symmetric phase.** Its design note gave the bound on m135/m136's covers (two at most).
- **Main's B1466 (sealed at b3565230): THE COUNT IS THE ORDER.** It works at Ballas' counted point q₀ = 17 ± 12√2, μ = −1, on m004
  itself. The two stacking orders count opposite there. B1532's Lemma D is the same statement for its own pair (sm:B1515 Lemma 7).
  This is adjacent, not overlapping.
- **Main's B1465 (S48): the mirror-broken states carry no count at their complete points.** Not this frame.

**The literature**, searched and read on 2026-10-03:
- **Shapiro's lemma.** Kedlaya, *Notes on class field theory*, §3.2: Definition 3.2.2 (Ind^G_H M = M ⊗_{ℤ[H]} ℤ[G]) and Lemma 3.2.3
  ("If H is a subgroup of G and N is an H-module, then there is a canonical isomorphism H^i(G, Ind^G_H N) → H^i(H, N)").
  Read at kskedlaya.org/cft/sec_cohom2.html.
- **The subgroups of ℤ/m × ℤ/n.** L. Tóth, *Subgroups of finite Abelian groups having rank two via Goursat's lemma*, Tatra Mt.
  Math. Publ. 59 (2014) 93–103, arXiv:1312.1485, Theorem 4.1, eq. (5): s(m, n) = Σ_{i|m, j|n} gcd(i, j). Read at the
  arXiv HTML. The instrument's closure count equals it on every level (K4).
- **Menal-Ferrer and Porti, Theorem 0.1**, through sm:B1515 Lemma 3 (read at source there).
- **Garland-type rigidity** through sm:B1515 Remark 9. Cited for a prior only, never used as a proof.

## 1. The question

In sm:B1515's frame F-HE at the hyperbolic point, take a λ = 1 member W₁(ν, c) of a level M_n (n = 2, …, 6). Does its pullback to
some finite abelian cover of M_n carry three generations? That is, I(p*W₁) = I(Λ²p*W₁) = −3, or +3 in the opposite order.

More generally: which generation-shaped counts occur, on which covers, members and classes?

## 2. Definitions and conventions

- **The levels.** M_n is the n-fold cyclic cover of m004 = b++LR. π_n = F ⋊ ⟨tₙ⟩, with T_n = coker(Φⁿ − 1) of order
  N_n = |tr Aⁿ − 2| = 5, 16, 45, 121, 320 (n = 2…6).
- **The characters.** A character of π_n trivial on the cusp P is a fibre character ν with ν(tₙ) = 1 (λ = 1). They form
  T_n^ ≅ T_n, labelled (a, b) ∈ (ℚ/ℤ)² with ν(x) = e^{2πia}, ν(y) = e^{2πib}, x = nm⁻¹, y = mnm⁻². Both routes use these words
  (K2).
- **The frame** (sm:B1515, verbatim in substance).
  - V = ν ⊗ ρ, L = ν⁻⁴, V_η = ν⁵ ⊗ ρ.
  - W₁(c) = [[V, c·L], [0, L]] for c ≠ 0 in H¹(V_η).
  - W₂ is the opposite order.
  - The index is main's I(E) = n(E) − n(E*) (B1297).
  - The dictionary: N(10′) = −I(W), N(5̄′) = −I(Λ²W).
  - **Generation-shaped:** I(W) = I(Λ²W) ≠ 0, carrying N = −I(W) generations (anomaly cancelled).
- **The term.** For χ ∈ T_n^: T(ν, χ, c) = (I(W₁(c) ⊗ χ), I(Λ²W₁(c) ⊗ χ)). Note that Λ²W₁ ⊗ χ is not Λ²(W₁ ⊗ χ).
- **The covers.**
  - A subgroup B ≤ T_n^ cuts out ψ: π_n → A = B^, with ψ(P) = 1, and the regular cover M_A with |A| cusps.
  - On M_A, the index of a module uses the whole boundary: n(E) is the dimension of the classes vanishing on every cusp.
  - **The count** of the pulled-back member on M_A is S(ν, c, B) = (I_{M_A}(p*W₁(c)), I_{M_A}(Λ²p*W₁(c))).
- **The classes** (sm:B1515's banked census).
  - M₂–M₅ and 200 members of M₆ have h¹(V_η) = 1. The class is unique up to scale and W₁ does not depend on the scale: the
    **one-class** members.
  - M₆'s other 120 members (ν⁵ in the 24 non-simple characters of order 8) have h¹(V_η) = 2, with a one-dimensional interior line
    ⟨c_int⟩ (n(V_η) = 1): the **two-class** members.
  - At a two-class member every class is either c_int or c_s = c_b + s·c_int up to scale, with c_b a fixed non-interior class.
- **Special points** (Lemma J) are the s at which the term changes. The **generic class** is any c_s outside every special point.

## 3. The theorems (proved at design time)

**Lemma S (the count is a sum of twisted terms).** For B ≤ T_n^ and any module E of π_n:

  I_{M_A}(p*E) = I_{M_n}(E ⊗ ℂ[A]) = Σ_{χ∈B} I_{M_n}(E ⊗ χ).

Hence S(ν, c, B) = Σ_{χ∈B} T(ν, χ, c).

- **Proof.**
  - p*E restricted to π_A induces back to E ⊗ ℂ[π_n/π_A] = E ⊗ ℂ[A] (the tensor identity).
  - Shapiro (Kedlaya, Lemma 3.2.3) gives H*(π_A; p*E) = H*(π_n; E ⊗ ℂ[A]).
  - The cusps of M_A are the double cosets P\π_n/π_A = A, since ψ(P) = 1. Each has peripheral group P, and Mackey gives
    H*(∂M_A; p*E) = ⊕_{a∈A} H*(P; E) = H*(P; E ⊗ ℂ[A]).
  - Both isomorphisms commute with restriction, so the interior classes correspond and n_{M_A}(p*E) = n_{M_n}(E ⊗ ℂ[A]).
  - The same holds for E*, since (p*E)* = p*(E*) and ℂ[A] is self-dual.
  - Over a field holding the |A|-th roots of unity, ℂ[A] = ⊕_{χ∈B} χ (Maschke), and n is additive.
  - Λ²p*W₁ = p*Λ²W₁, which gives the second component. □
- **Route C** computes the middle term directly, with ℂ[A] the permutation module, never split into characters.

**Lemma Z (every finite abelian cover reduces to a subgroup B).** Let χ be a character of π_n with χ|_P ≠ 1. Then
I(W₁ ⊗ χ) = I(Λ²W₁ ⊗ χ) = 0.
- At λ = 1, W₁|_P and Λ²W₁|_P are unipotent. So (· ⊗ χ)|_P has no eigenvalue 1 on some generator of P, and H*(P; ·) = 0.
- An acyclic torus gives I = 0 (sm:B1515 Lemma 4; B1392).
- Hence for any finite abelian ψ′: π_n → A′, by Lemma S the count is Σ over the characters of A′ trivial on P. Those form a
  subgroup B of T_n^. Every finite abelian cover of M_n counts what the cover of some B counts.
- The record's "a pullback keeps the index" (sm:B1506 T2) is the case B = 1 of this lemma, along the level tower. □

**Lemma D (the opposite order counts the opposite).** By sm:B1515 Lemma 7, W₂(ν)* ≅ W₁(ν̄) and W₁(ν̄) = conj W₁(ν). Hence the W₂
order's count on M_A is minus the W₁ count at the conjugate class. The conjugation symmetry is checked in-run as D6:
T(ν̄, χ̄, c̄) = T(ν, χ, c) at the canonical classes. So |N| = 3 in either order is a (±3, ±3) count of the W₁ family, and only
W₁ is read.

**Lemma J (the classes of a two-class member).** Fix ν and χ. Each of the four modules M ∈ {E, E*, Λ²E, (Λ²E)*}, with
E = W₁(c) ⊗ χ, is an extension 0 → S → M(c) → Q → 0 whose class is linear in c. (Block upper-triangular matrices, the off-diagonal
block linear in c. For Λ², a 2 × 2 minor meets the single off-diagonal column at most once.)
- The long exact sequence gives h¹(M(c)) = h¹(S) − rank δ⁰_c + dim ker δ¹_c.
  - δ⁰ is constant in c ≠ 0.
  - δ¹_c: H¹(Q) → H²(S) is [y] ↦ [Φ(c)y], with Φ(c)y the S-part of d¹_{M(c)}(0, y).
  - On a deficiency-one presentation h¹(S) = k + h⁰(S), with k = dim coker d¹_S.
- By Lemma E of sm:B1527, I(E) = h¹(E*) − h¹(E) + 2(a0 − b0) + s0 − t0, and the same for Λ²E.
  - a0, b0 are constant in c ≠ 0.
  - At c_s the P-module does not depend on s, since c_int|_P is a peripheral coboundary. So s0 and t0 are constant in s.
- Hence off c_int the term changes only where one of the four pencils δ¹_{c_b} + s·δ¹_{c_int} drops rank. That happens:
  - at most at one rational s, when the pencil's generic rank is one;
  - at the common roots of its 2 × 2 minors, of degree ≤ 2, possibly a conjugate pair over GF(p²), when the generic rank is two.

  The rank never exceeds two (Proposition H). □
- **Reading a special class.** Every special class is read directly. A conjugate pair is read through the restriction of
  scalars: R(E) has twice E's cohomology, so I(E) = I(R(E))/2. Its matrix is [[X, d₀Y], [Y, X]] for E(u + v√d₀) = X + Y√d₀.

**Proposition H (where special points can be).** H²(M_n; S) → H²(T; S) is onto whenever H⁰(M_n; S*) = 0, by Lefschetz duality.
- δ¹_c followed by it is the torus cup product with c|_P, which does not depend on s.
- So a pencil can drop rank only where h²(M_n; S) > h²(T; S) = h⁰(T; S*). Using χ(M) = 0, sm:B1515 Lemma 1 and Lemma 3:
  - **E** (S = νχ ⊗ ρ): only at νχ non-simple (h¹(νχ ⊗ ρ) ≥ 2).
  - **E*** (S = ν⁴χ⁻¹, a character): never (h² = h⁰(T) = 1, or 0 at the trivial character).
  - **Λ²E** (S = ν²χ ⊗ Λ²ρ, h² = 2 = h⁰(T; Λ²ρ)): never.
  - **(Λ²E)*** (S = ν³χ⁻¹ ⊗ ρ): only at ν³χ⁻¹ non-simple. Since NS⁻¹ = NS by conjugation, this is ν⁻³χ ∈ NS.
- So a member has at most 28 + 28 χ with special points. Accidental coincidences mod p are negligible (about 10⁻⁴ per member).
- The run checks Proposition H as P7. It is not assumed. □

**Corollary I (the interior class counts only the non-simple twists).** At c_int, (W₁ ⊗ χ)|_P = V|_P ⊕ 1. So t0 = s0 = 2, t1 = 4,
and for Λ²W₁ ⊗ χ, t1 = 6.
- **W term with νχ simple.**
  - h¹(E*) ≤ h¹(L⁻¹χ⁻¹) + h¹((Vχ)*) = 1 + 1 (sm:B1506 T1; conjugation).
  - The annihilator identity r1(E) + r1(E*) = t1 gives r1(E) ≥ 2, so I(W₁ ⊗ χ) ≤ −[χ = ν⁴] ≤ 0.
  - The bound below gives I ≥ 0. So I = 0, and χ ≠ ν⁴ at a two-class member, since there ν⁵ is non-simple.
- **Λ² term with ν⁻³χ simple.** h¹((Λ²E)*) ≤ 1 + 2 gives r1 ≥ 3, so I ≤ 0 ≤ I.
- **So at the interior class every simple twisted term is (0, 0).** The count S(ν, c_int, B) comes only from the χ ∈ B with
  νχ ∈ NS (the W part) or ν⁻³χ ∈ NS (the Λ² part).
- In particular, the 96 two-class members of order 40 (ν and ν⁻³ simple) read (0, 0) at c_int on M₆ itself (B = 1). Only the 24
  of order 8, with ν ∈ NS, can count there.
- **The same argument at a boundary-type class** (t1 = 3 for W, 5 for Λ²): a simple W term lies in [0, 1 − [χ = ν⁴]] and a simple
  Λ² term in [0, 1]. □
- The run checks these term by term (D7). A violation is a bug.

**The design-time bound (banked h¹ only).** At every class:
- I(W₁ ⊗ χ) ≥ 1 − h¹(νχ ⊗ ρ), since r1 ≤ h¹(E) ≤ h¹(νχ ⊗ ρ) − [χ = ν⁴] + 1 and s0 = 2;
- I(Λ²W₁ ⊗ χ) ≥ 1 − h¹(ν⁻³χ ⊗ ρ), since s0 = 3 and h¹(ν²χ ⊗ Λ²ρ) = 2 by MFP.

What follows:
- **M₂–M₅** have no non-simple character, so every count there is ≥ 0 in both components.
- **M₆:** 8,631 of the 23,680 pairs (ν, B) have both lower sums ≤ −3. The smallest such |B| is 4 (bounds (−4, −4)). Three is not
  excluded at design time.
- **Positive counts** are not bounded away anywhere. A simple W term lies in [0, 1 − [χ = ν⁴]] and a simple Λ² term in [0, 1].

## 4. The instruments (`verification/`, scripts written before the seal)

- **`cover_lib_t.py`, route T.** sm:B1515's route T, imported unchanged: B1511's Reidemeister–Schreier presentation and tower_lib,
  and B1374's index_lib over GF(p).
  - c_int is the restriction solved modulo the peripheral coboundaries.
  - The pencils come from route T's Fox Jacobian and cokernel.
  - Conjugate pairs are read through the restriction of scalars.
- **`cover_lib_l.py`, route L.** sm:B1515's route L, imported unchanged: the mapping-torus presentation ⟨x, y, t⟩, B1513's
  backend and numpy elimination. It shares no code with route T.
  - Its own c_int comes from its joint system K.
  - Its own c_b and hash give it its own s-coordinate. The two routes' coordinates differ by an affine map, so special points are
    compared through the multisets of their readings and their coincidence structure, not by value.
- **`route_c.py`, route C.** I_{M_n}(E ⊗ ℂ[A]) with the permutation module (Lemma S's middle term), on route T's index.
- **`run_terms.py`, the sealed run.** Part 0 is the banked identity and stops the run if it fails. Part A reads every
  (n, ν, χ) term.
  - One-class members are read at c.
  - Two-class members are read at c_int, at the generic class c_{s_g}, and at every special class. gen2, a second generic class,
    is read on the members whose hash falls in one-in-eight.
  - Output is resume-safe JSONL per route, at sm:B1515's first prime of each level in each route (route T above 2²³, route L
    below 2²²).
- **`read_out.py`, the read-out.**
  - The subgroups by closure, checked against Tóth.
  - The sums at every class (Lemma S).
  - The census in each route, on its own data.
  - Checks D1–D6: the banked identity; the pencils' h¹ prediction at every generic class; the h¹ jump at every rational special
    point; gen2 = gen; route T = route L term by term under route L's signature; conjugation.
  - D7: Corollary I and the bounds, term by term.
  - The two censuses compared.
- **`run_route_c.py`** (P1, after the read-out). Route C on its sealed sample and on the hits, against route T's sums.
- **`adjudicate.py`** (after the read-out). D5's disagreements re-read at the second primes in both routes; three of four stand.
- **`controls.py`, K1–K9** (§6).

**Time, from the controls' timings:** route T about 10 core-hours, route L about 5. The run waits until sm:B1530's census and
sm:B1529's pole brackets free the cores.

## 5. The population

| level | members (one-class + two-class) | χ | terms (ν, χ) | subgroups B | (ν, B) |
|---|---|---|---|---|---|
| M₂ | 5 + 0 | 5 | 25 | 2 | 10 |
| M₃ | 16 + 0 | 16 | 256 | 15 | 240 |
| M₄ | 45 + 0 | 45 | 2,025 | 12 | 540 |
| M₅ | 121 + 0 | 121 | 14,641 | 14 | 1,694 |
| M₆ | 200 + 120 | 320 | 102,400 | 74 | 23,680 |

Every class of every member is read:
- the one-class c;
- at each two-class member: c_int, the generic class, and every special class.

## 6. Controls and disclosures (before the seal; `controls_run.txt`)

- **K1 (the banked identity).** In route T, 507 of 507 χ = 1 terms equal sm:B1515's census rows. In route L, also 507 of 507. This
  holds in I and in every B1297 dimension of W₁ and Λ²W₁, on M₂–M₆, at the same primes. Two-class members are compared at the
  generic class.
- **K2.** Fibre words and φ are equal. The label sets of T_n^ agree on every level, and the two deck maps agree on every label.
- **K3 (Lemma Z).** χ(t) ∈ {−1, i, ω}. On one member of every level and on a two-class member of M₆ (full reader: pencils,
  specials, gen2), both routes give every index 0.
- **K4.** Subgroup counts are 2, 15, 12, 14, 74, equal to Tóth's s(1, 5), s(4, 4), s(3, 15), s(11, 11), s(8, 40).
- **K5 (route C on banked h¹).** h¹(V ⊗ ℂ[A]) = Σ_coset banked h¹, and h¹(Λ²V ⊗ ℂ[A]) = 2|A|. Read on the subgroups of order ≤ 8
  of M₃ and of order ≤ 4 of M₆, for two members each: 50 subgroup readings, all equal.
- **K6.** Both readers find exactly the 120 two-class members on M₆ and none elsewhere. Each interior line is one-dimensional.
- **K7.** At χ = 1, at every two-class member's generic class, the four pencils predict h¹ of E, E*, Λ²E, (Λ²E)* exactly, in both
  routes. The special classes were located, not read. The pencils' shapes (m, k, generic rank, number of points) are recorded in
  `controls.json`, and the two routes' shapes are identical.
  - E, E* and Λ²E have no special point at χ = 1. Their generic ranks are 0 or 1.
  - (Λ²E)* has rank one at the 96 members of order 40.
  - (Λ²E)* has rank two, with one special point, at the 24 of order 8, exactly where ν⁻³ ∈ NS. This is Proposition H at χ = 1.
  - So the rank-one and rank-two paths of the pencil reader are exercised.
- **K8 (Lemma D, banked rows).** I(W₂) = −I(W₁) and I(Λ²W₂) = −I(Λ²W₁) at every one-class member: route T's record 783 of 783 rows
  (both fields), route L's 1,171 of 1,171.
- **K9 (the conjugate-pair reader, split).** With w² = d₀ a square, R(M(u + vw)) = [[X, d₀Y], [Y, X]] splits as
  M(u + v√d₀) ⊕ M(u − v√d₀). So its raw B1297 data must equal the sum of the two direct readings at those rational classes.
  - Read at χ = 1 at generic classes (banked-level) of three two-class members of M₆, d₀ = 4 and 9, in both routes.
  - This tests the restriction-of-scalars construction without reading a conjugate pair of the population.
  - 12 split readings; every raw datum equals the sum.
- **The read-out, dry-run on synthetic rows only** (`dry_run.py`, `dry_run2.py`, labels of M₂ and M₃, no instrument output).
  - Planted faults are all caught: a route mismatch (D5), a conjugation asymmetry (D6) and a negative simple W term (D7).
  - The census's generation-shaped list equals an independent recount: 54 synthetic counts.
  - A synthetic two-class member with a shared special class, the routes in different s-coordinates (s_L = 3s_T + 5), gives D5 = 0,
    equal coincidence structures, and special-class sums equal to the recount.
  - The dry run found one read-out bug, fixed before the seal: the conjugation check assumed a member and its conjugate have the
    same kind, and raised an error where they differed. A difference is now reported as D6. In true rows the kinds agree, since
    h¹(V_η) is conjugation-invariant.
- **Disclosed smoke tests.** Before the controls were written, the same χ = 1 comparisons were run on M₂ (route T, 5 members), M₂
  and M₃ (route L, 21) and two M₆ generic classes per route. Lemma Z was run at λ = −1 on one M₆ two-class member with three χ.
  The pencil algebra was unit-tested on synthetic matrices.
  - One smoke-test bug: the test passed a label where the reader takes exponents. It was fixed in the test, not in the reader.

## 7. Predictions (sealed; `read_out.py` reads them)

- **P1 (Lemma S numerically).** Route C equals route T's sum on every (ν, c, B) route C reads. The sample is
  `run_route_c.py`'s:
  - eight members per level, first by sha256 (M₂'s five);
  - every |B| ≤ 5, at c, or at c_int and the generic class;
  - one subgroup of order 11 on M₅ for two members;
  - every |N| = 3 hit with |B| ≤ 16 at its class (a conjugate pair excepted);
  - up to 20 further generation-shaped hits with |B| ≤ 8.

  **97%.**
- **P2 (two routes).** D5 shows no disagreement left after adjudication (§9). **90%.**
- **P3 (M₂–M₅).** No generation-shaped count on any cover of M₂–M₅. The negative direction is excluded by the bound. The positive
  needs a non-zero simple Λ² term, which the rigidity of Remark 9, applied on the cover, forbids. **85%.**
- **P4 (M₆, any count).** Some cover of M₆ carries a generation-shaped count at some class. **60%.**
- **P5 (M₆, three).** Some cover of M₆ carries |N| = 3, generation-shaped, at some class. **30%.**
- **P6 (interior classes, χ = 1).** At least one of M₆'s 24 two-class members of order 8 is generation-shaped on M₆ itself (B = 1)
  at its interior class. Corollary I sets the other 96 to (0, 0) there. This is the analogue of sm:B1530's m135 member, which is
  case (a), where these are case (b). **40%.**
- **P7 (Proposition H).** Every special point found lies at νχ ∈ NS (family E) or ν⁻³χ ∈ NS (family (Λ²E)*). No other family has
  one. **92%.**
- **P8 (the simple Λ² terms).** Every Λ² term at a pair (ν, χ) with ν⁻³χ simple, at a non-interior class, is 0. This is the
  twisted form of sm:B1515 Lemma 8(ii) with Remark 9. **85%.**
- **P9 (the degree law).** At every (ν, c, B) the pullback multiplies the base count by the degree:
  S(ν, c, B) = |B|·T(ν, 1, c). In sm:B1386's frame on cube~3.24 the record states this law (OPEN_LEADS, sL-7). Here it would
  need every twisted term to equal the χ = 1 term, and simple twisted W terms in {0, 1} make that unlikely. **10%.**
- **G (golden).** Every level of m004 is a golden state, so the golden hypothesis is not informative in this population. Stated so
  and not read.

## 8. BANKED IDENTITY: checked before reading

Part 0 of `run_terms.py` repeats K1 in each route before any term is read. A single difference stops the run, and nothing of the
census is read.

## 9. Reading rules, and what this arc will and will not claim

- **Adjudication.** A D5 disagreement on a term is re-read at sm:B1515's second prime of that level, in both routes. The value that
  three of four readings share stands. A term with no such value is excluded and named, and every count that contains it is
  reported as unresolved.
- **A three (|N| = 3, generation-shaped).** It needs both routes, route C (when |B| ≤ 16) and the second prime.
  - It is reported with its cover (B, |A|, the cover's number of cusps), member, class and the terms that make it.
  - Reading: three generations of the frame on that cover-state of X_gen. **Selection stays open** (sL-5, sL-7). It is a count,
    not a held vacuum (R76: the split configuration is the minimum of the bare model).
- **No three.** Both routes agree, with no unresolved count in the population. Then the arc is NEGATIVE within its scope and goes
  to the kill graph: F-HE, the hyperbolic point, λ = 1, M₂–M₆, every finite abelian cover, pulled-back members at every class.
- **D2/D3/D4/D6 failures** are bugs until shown otherwise. They are fixed, disclosed (ERROR_LEDGER) and re-run before anything is
  read from the affected rows.
- **Not claimed.**
  - The covers' own members: characters of the cover not pulled back, and classes in the other χ-summands of H¹(M_A; p*V_η).
  - Non-abelian covers.
  - Other states, or other frames.
  - Held vacua.
  - Selection.
  - The index is the frame's count. Its reading as generations is sm:B1509's dictionary.

## 10. What this arc does not decide (the next questions)

- The covers' own members, from characters of π_A not pulled back. Lemma S does not apply to them.
- Non-abelian covers, where Mackey gives Ind of irreducibles of dimension > 1.
- The word states' covers. m135/m136 are bounded by two at design time, and a census member would need three members in one coset.
- Which cover, if any, is physical: sL-5's one bit.
