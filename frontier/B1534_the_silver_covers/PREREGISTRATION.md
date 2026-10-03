# B1534 — PREREGISTRATION: THE SILVER COVERS — sm:B1515's frame pulled back to every finite abelian cover of m135 and m136, at every member and every class: does any cover carry three generations?

**Sealed before `run_terms.py` read any twisted term.** At the seal this arc has computed only:
- `controls.py` (K0–K9), all hold (`controls_run.txt`, `controls.json`). They read:
  - banked members and banked χ = 1 terms (sm:B1530);
  - characters outside the population (Lemma Z′);
  - structure: the contributing groups, the pencils at χ = 1 (located, not read), and two covers whose counts are banked.
- `members_every_twist.py` (K10), which holds (`members_every_twist_log.txt`, `members_every_twist.json`). It reads which
  characters are members at every twist κ ∈ ℂ*, and no term.

No term T(ν, χ, c) with χ ≠ 1 in the population has been read. No term at a special class has been read.

**Source.**
- **The owner, 2026-10-03:** "are u sure about the math behind your negative conclusions about three generatiosn, sure sure
  sure?", the day's binding rules ("aleays verify, make sure we dont hit negatives because of bugs"; "do it correctly,
  informedly, and bug free in all load bearing math"), and the standing goal.
- **Re-deriving the design note's bound before any relay** found it one-sided. The note said "the silver squares' covers
  trivial on the cusp count at most two generations".
  - It bounded W₁'s generations at the interior class, I(p*W₁) ≥ −2.
  - It bounded neither the other sign (the dual order's generations) nor the boundary-type classes.
  - It is withdrawn: sm:B1530 §7, and ERROR_LEDGER (E9 instance).
- sm:B1530 reduced the question to finitely many exact readings and registered them as **sL-10 item 11**. This arc reads them.

## 0. Seen first, and PRIOR ART:

**The repo sweep.** `git fetch --all` was run first. `scripts/checks/prior_work.py` ran over every head with twelve terms:
"silver cover", "covers of m135", "covers of m136", "cover of m135", "cover of m136", "abelian cover", "permutation module",
"restriction of scalars", "pulled-back member", "pullback keeps", "silver squares", "Shapiro".

The heads read:

| head | commit |
|---|---|
| this branch | `762b72b0` |
| main | `d295fc5d` |
| the audit lane | `c7aa3a29` |
| seat/determined-hopper | `7cda35aa` |
| seat/outside-bench | `13d2c5b6` |
| seat/paper-review-verification | `5d58b935` |
| seat/physics-seat-evaluation | `659487bb` |

Main retired seat/magical-wright at `0043be2b` and art/camper-van-bar at `b3745696` (B1467).

What bears:
- **sm:B1532 (sealed at `97fdce6d`, running): three from the cusps.** Its Lemmas S, Z, D and J, its Proposition H, its Corollary
  I and its route C are the method here, carried from m004's levels M₂–M₆ to m135 and m136.
  - Its Lemma Z assumes W₁ unipotent on P (λ = 1). Lemma Z′ below replaces it, because m136's κ = −1 members are not
    unipotent there.
  - Its seal quotes the withdrawn bound (§0 and §10). Its FINDINGS will carry the correction.
- **sm:B1530 (banked at `cc1fa6d5`): the interior extensions.** The members and their χ = 1 readings (the banked identity).
  - Route E (exact_lib, exact_states) and route N (route_n), imported unchanged.
  - The exact holonomies of m135 and m136, and the common double cover's count.
- **sm:B1515, sm:B1509, main's B1297:** the frame, the dictionary, the index.
- **Main's B1466 (the count is the order)** and **sm:B1515 Lemma 7:** the two orders count opposite (Lemma D below).
- **sm:B1506 T2 and main's T-THE-LEVEL ("a pullback keeps the index"):** the case B = 1, along the level tower. The cyclic
  levels of ±L²R² are abelian covers, so they are among this arc's covers, at their pulled-back members.
- **"silver cover" elsewhere:** B129 and B771 (W3-068) read SL(3) trace fields on the silver bundle's cyclic covers. They
  compute no index and are another frame.
- **Not found on any head:** "covers of m136" and "cover of m136". "Covers of m135" is in sm:B1530's text and relay only.
  Nothing reads F-HE on a cover of m135 or m136 beyond sm:B1530's common double cover.
- **Main's B1467 (S50, `d295fc5d`, read at this seal):**
  - It rows sm:B1529, B1530 and B1532 as sealed and running.
  - It adopts sm:B1528's FK12 (ii) sentence into a GENESIS v1.10 of main's own, made before main read sm:B1533's v1.10.
    That is a second version collision; this seat will answer it separately.
  - It reads the audit lane's R81 as B1466's axis.
  - It does not bear on the covers.

**The literature** (read at source for sm:B1532 on 2026-10-03, and cited from that record):
- Shapiro's lemma: Kedlaya, *Notes on class field theory*, §3.2, Lemma 3.2.3.
- The subgroups of ℤ/m × ℤ/n: L. Tóth, arXiv:1312.1485, Theorem 4.1, eq. (5). Here it gives 8 subgroups of ℤ/4 × ℤ/2 and 5 of
  (ℤ/2)²; (ℤ/2)³ has 16 by direct count. The instrument's closures find these numbers (K3).
- Mackey's double cosets and the restriction of scalars are standard and are used as stated in sm:B1532.

**Not found in the sources read:** any reading of a rank-five extension of a twisted four on a cover of a punctured-torus
bundle.

## 1. The question

In sm:B1515's frame F-HE, at the hyperbolic point of m135 = −LLRR and m136 = +LLRR, take any member ν and any class c, and
pull W₁(c) back to any finite regular abelian cover. Is the count three generations?

That is, I(p*W₁) = I(Λ²p*W₁) = −3 (W₁'s order), or +3 (the dual order's three, by Lemma D). And more generally: which counts
occur?

## 2. Definitions and conventions

- **The states, the frame, the index and the dictionary** are sm:B1530's §2, unchanged.
  - Γ = F ⋊ ⟨t⟩, P = ⟨ℓ, t′⟩, ν = (u, κ) with κ = ν(t′).
  - V = ν ⊗ ρ, L = ν⁻⁴, V_η = ν⁵ ⊗ ρ, W₁(c) = [[V, c·L], [0, L]].
  - The index is main's I(E) = n(E) − n(E*) (B1297). N(10′) = −I(W) and N(5̄′) = −I(Λ²W).
  - **Generation-shaped:** I(W) = I(Λ²W) = a ≠ 0, carrying ∣a∣ generations.
- **The members.**
  - **m135:** eight at κ = 1. The two non-simple ones are u₁ = (0, ½) and u₂ = (½, 0), with h¹(V_η) = 2 and one interior line.
    The other six are simple, with one boundary-type class.
  - **m136:** four simple members at κ = 1, each with one boundary-type class. Two at κ = −1, at u₁ and u₂, each with one
    class, interior (the cusp is acyclic for V).
  - Every member is case (a): ν⁴ = 1, so L = 1 and V_η = V.
  - These are the members at the twists sm:B1530 read, κ ∈ {1, −1, ±i, ω, ω²}. Members exist at other twists. Every
    ν = (u, κ) with κ⁵ = 1 is one, and so is every κ⁵ = −1 at m136's u₁ and u₂, and every fifth root of a real eigenvalue
    in K10. Lemma Q shows that these add no count: the members listed here carry every member's counts, at every twist.
- **The term.** For a character χ of Γ, T(ν, χ, c) = (I(W₁(c) ⊗ χ), I(Λ²W₁(c) ⊗ χ)). Λ²W₁ ⊗ χ is not Λ²(W₁ ⊗ χ).
- **The covers.**
  - A finite regular abelian cover M_A → M has deck characters B ⊂ Hom(Γ, ℂ*).
  - **Its count** at a pulled-back member is S(ν, c, B) = (I_{M_A}(p*W₁(c)), I_{M_A}(Λ²p*W₁(c))), with n read on all of
    M_A's cusps.
- **The classes.**
  - At a one-class member: its class.
  - At m135's two-class members: c_int and c_s = c_b + s·c_int, with c_b route E's fixed non-interior class (sm:B1530's
    choice).
  - The **special** s are those of Lemma J. The **generic** classes are s = 3/7 and s = −11/5, checked off every special s.

## 3. The theorems (proved at design time)

**Lemma S (sm:B1532, for every finite regular abelian cover).** I_{M_A}(p*E) = Σ_{χ∈B} I_M(E ⊗ χ).
- sm:B1532's proof assumed ψ(P) = 1. It is not needed.
  - The cusps of M_A are the double cosets P\Γ/Γ_A = A/ψ(P), with peripheral groups P ∩ Γ_A.
  - Mackey and Shapiro give H*(∂M_A; p*E) = H*(P; E ⊗ ℂ[A]) = ⊕_χ H*(P; E ⊗ χ). Shapiro gives
    H*(Γ_A; p*E) = H*(Γ; E ⊗ ℂ[A]).
  - Both isomorphisms commute with restriction, so n and I add over χ (Maschke over a field holding the |A|-th roots of
    unity).
- Λ²p*W₁ = p*Λ²W₁. □

**Lemma Z′ (the contributing characters).** If E ⊗ χ is acyclic on P, then I(E ⊗ χ) = 0 (sm:B1515 Lemma 4; B1392).
- On P, ℓ is a commutator, so χ(ℓ) = 1, and ρ(ℓ) is unipotent.
- On t′, the composition factors have eigenvalues κχ(t′) and κ⁻⁴χ(t′) for W₁, and κ²χ(t′) and κ⁻³χ(t′) for Λ²W₁, each times
  a unipotent.
- So a term can be non-zero only if χ(t′) ∈ {κ⁻¹, κ⁴, κ⁻², κ³}:
  - for κ = 1, χ(t′) = 1: the eight characters trivial on P on m135, and four on m136;
  - for κ = −1, χ(t′) = ±1: eight characters on m136, ≅ (ℤ/2)³.
- These form a subgroup C_ν. Every finite abelian cover's count at ν is Σ_{χ ∈ B ∩ C_ν} T(ν, χ, c): a sum over a subgroup
  of C_ν, and every subgroup occurs (B = H).
- So the arc reads every count of every finite abelian cover at a pulled-back member. □

**Lemma D (the opposite order).** W₂(ν)* = [[ν̄ ⊗ ρ, c′], [0, 1]] = W₁(ν̄) at the class c′ (ρ* ≅ ρ through β; ν̄ = ν⁻¹).
- So the dual order's counts at ν are minus W₁'s counts at the member ν̄, on the same covers.
- Over all members, three in either order is a W₁ count (a, a) with ∣a∣ = 3. □

**Lemma Q (the members at every twist; K10).** Let ν = (u, κ) be any member of m135 or m136 at the hyperbolic point, κ ∈ ℂ*.
- Every fibre character here has order dividing 4, so ν⁵ = (u, κ⁵). By sm:B1529's Lemma F,
  h¹(ν⁵ ⊗ ρ) = dim ker(T_C(u) − κ⁵), with T_C(u) the stable letter's action on H¹(F; u ⊗ ρ), a 4 × 4 matrix. So ν is a member
  exactly when κ⁵ is an eigenvalue of T_C(u).
- K10 reads those eigenvalues for every u, by route T, with route E exact at all of μ₂₄ (288 comparisons, all agreeing):
  - 1 at every u;
  - −1 at m136's u₁ and u₂ only;
  - otherwise real and off the unit circle (four at u = (0, 0) and (½, ½) on each state, each at least 0.55 from it).
- **κ not a root of unity.** Every term with χ of finite order is (0, 0) by Lemma Z′. A factor's cusp is non-acyclic only if
  κʲ·χ(t′) = 1 for some j ∈ {1, −4, 2, −3}, which makes κ a root of unity. So such a member counts (0, 0) on every finite
  abelian cover.
- **κ a root of unity.** Then κ⁵ ∈ {1, −1}, so κ = κ′ζ with κ′ = ±1 and ζ⁵ = 1.
  - So ν = ν′ε, with ν′ = (u, κ′) a member listed in §2 (ν′⁵ = ν⁵) and ε the character trivial on F with ε(t) = ζ.
  - Since ν′⁴ = 1 and ε⁵ = 1, W₁(ν, c) = W₁(ν′, c) ⊗ ε at the same class (H¹(ν⁵ ⊗ ρ) = H¹(ν′⁵ ⊗ ρ)), and
    Λ²W₁(ν, c) = Λ²W₁(ν′, c) ⊗ ε². So T(ν, χ, c) = (T_W(ν′, εχ, c), T_Λ(ν′, ε²χ, c)).
  - If ε ∈ B, then p*ν = p*ν′, and the count is ν′'s on the same cover.
  - If ε ∉ B, every term vanishes, and the count is (0, 0). A non-zero term would need χ ∈ B with εχ or ε²χ in C_ν′, so
    χ(t′) of order 5 or 10. Its 16th power is then a non-trivial power of ε (the fibre parts have exponent 4), which puts ε
    in B.
- **So the members of §2 carry every count of every member of the two states, at every twist, on every finite abelian
  cover.** □

**Lemma J (sm:B1532, verbatim in substance).** At a two-class member, each of the four modules
M ∈ {E, E*, Λ²E, (Λ²E)*}, E = W₁(c) ⊗ χ, is an extension 0 → S → M(c) → Q → 0 whose off-diagonal block is linear in c.
- h¹(M(c)) = h¹(S) − rank δ⁰ + h¹(Q) − rank δ¹_c, with δ¹_{c_s} = P_b + s·P_int.
- a0, b0, t0 and s0 do not depend on s (c_int restricts to a coboundary on P).
- So the term changes with s only where a pencil's rank drops: at a root in K, or at a conjugate pair over K. A conjugate pair
  is read through the restriction of scalars, I(R(M)) = 2 I(M). □

**Proposition H′ (where special classes can be, at m135's two-class members ν ∈ {u₁, u₂}).** As sm:B1532's Proposition H: a
pencil can drop rank only where h²(M; S) > h⁰(P; S*). By Lemma 3 of sm:B1515 (Menal-Ferrer–Porti on ker χ) and the census:
- **E** (S = νχ ⊗ ρ): only where νχ is non-simple.
- **E*** (S a character): never.
- **Λ²E** (S = χ ⊗ Λ²ρ, h² = 2 = h⁰(P; Λ²ρ)): never.
- **(Λ²E)*** (S ≅ (νχ)⁻¹ ⊗ ρ): only where νχ is non-simple.

Since ν² = 1 and NS = {u₁, u₂}, the special classes lie at χ ∈ {1, (½, ½)} only. At χ = 1 the controls locate one special
point on each member, in the (Λ²E)* pencil (K4; K9 in route N). It is not read before the seal. □

**Corollary I′ (the interior class; three is impossible there).** At c_int of m135's member ν, every χ ∈ C_ν is trivial on P.
So (W₁ ⊗ χ)|_P ≅ ρ_P ⊕ 1 and (Λ²W₁ ⊗ χ)|_P ≅ Λ²ρ_P ⊕ ρ_P, with (t0, s0) = (2, 2) and (3, 3).
- **χ = 1:** (−1, −1), banked.
- **νχ simple:** (0, 0).
  - W term: H¹(W₁ ⊗ χ) is spanned by the boundary class of νχ ⊗ ρ and the lift of x_χ. H¹(M; χ) is a line (Wang's sequence
    and χ(M) = 0), and x_χ restricts non-trivially (half lives, half dies). It lifts because c_int ∪ x_χ restricts to 0 and
    H²(M; νχ ⊗ ρ) → H²(P; ρ) is injective. So r1 = 2 = s0, and I = 0.
  - Λ² term: H¹(Λ²W₁ ⊗ χ) is spanned by Λ_A(χ) (2-dimensional, with no interior class by Menal-Ferrer–Porti) and the lift of
    the boundary class. So r1 = 3 = s0, and I = 0.
- **χ = (½, ½)** (νχ the other non-simple member): the W term is in {0, 1} (r1 = 1 + [x_χ lifts]), and the Λ² term in
  {0, −1} (r1 = 3 + [the interior class's lift restricts outside the rest]).
- **So at m135's interior class every abelian cover counts (−1, −1) + [(½, ½) ∈ B]·(a, b), with a ∈ {0, 1} and b ∈ {0, −1}.**
  The count lies in {(−1, −1), (0, −1), (−1, −2), (0, −2)}: three is impossible there, and the only generation-shaped count
  is (−1, −1). □

**The boundary-type classes (design-time ranges, both signs).** Take c with c|_P = c_P ≠ 0, and χ with νχ simple, χ ≠ 1. The
cusp module is [[ρ_P, c_P], [0, 1]], with Lemma T's torus table: the torus cups with c_P vanish.
- **W term = 1 − δ_χ ∈ {0, 1}.** δ_χ = [the boundary line of νχ ⊗ ρ differs from ℂ·c_P]. The lift of x_χ always counts in r1,
  and the boundary class of νχ ⊗ ρ counts unless its line is ℂ·c_P.
- **Λ² term = bit_χ ∈ {0, 1}.** bit_χ = [e ∧ c_P ∈ Λ_A(χ)], as sm:B1515 Lemma 8 at the member itself.
- At a non-simple twist (νχ ∈ NS) the W term lies in {0, 1, 2} and the Λ² term in {−1, 0, 1}.
- So positive counts are not bounded away at the boundary-type classes.
  - At m136's four κ = 1 members, the largest cover (B = C_ν, order 4) counts (3, 3) exactly when all three non-trivial terms
    read (1, 1).
  - At m135's members, sums up to six or more are allowed by these ranges.
- **Three is excluded at design time only at the interior class.** Everywhere else the reading decides.

## 4. The instruments (`verification/`, written and tested before the seal)

- **`silver_lib.py`, route E (exact over ℚ(ζ₂₄)).** sm:B1530's exact_lib and exact_states, imported unchanged; m136's exact
  holonomy by sm:B1530's post_run_e136.
  - The members, classes and contributing characters.
  - The terms, by exact_lib.class_index, which asserts B1297's identity, the annihilator identity and Lemma E at every index.
  - The pencils: H²(S) as the cokernel of S's Fox matrix, and δ¹ as the S-part of the Fox coboundary of the lifted
    Q-cocycles. Linearity in c is asserted at every pencil.
  - The special points: the roots of the gcd of the pencil's maximal minors. Whether a quadratic splits over
    K = ℚ(i, √2, √3) is decided exactly by sympy.
  - Conjugate pairs are read through the restriction of scalars.
  - The subgroups of C_ν, by closure.
- **`silver_n.py`, route N (60 digits).** sm:B1527's cusp_lib and sm:B1530's route_n, on family_lib's numerical four.
  - Route E's classes are carried across frames by the conjugator X, so the s-coordinate is shared.
  - Route N computes its own pencils and special points numerically, and reads conjugate pairs at both complex roots
    directly.
- **`run_terms.py`, the sealed run.** Every member, every χ ∈ C_ν, both modules:
  - one-class members at their class;
  - two-class members at c_int, c_{g1}, c_{g2} and every special class, each pencil compared between the routes.

  Then every subgroup's count at every class read.
- **`run_route_c.py`, route C.** Lemma S's middle term, I(W₁ ⊗ ℂ[A]) with the permutation module, never split into
  characters. It is read on the cover of H₄ (the first subgroup of order min(4, ∣C_ν∣) in the instrument's order), at c_int
  or the one class and at c_{g1}, for every member.
- **`members_every_twist.py`, K10 (Lemma Q).** Route T (sm:B1529's fibre_lib, banked) gives T_C(u)'s characteristic
  polynomial: its order of vanishing at ±1, and the other roots with their distance from the unit circle. Route E gives
  h¹(ν ⊗ ρ) exactly at every κ ∈ μ₂₄.
- **`read_out.py`** reads §7 from terms.json and route_c.json.

## 5. The population

- **m135:** eight members, each with C_ν of order 8 (ℤ/4 × ℤ/2, eight subgroups).
- **m136:** four κ = 1 members with C_ν of order 4 ((ℤ/2)², five subgroups), and two κ = −1 members with C_ν of order 8
  ((ℤ/2)³, sixteen subgroups).
- The classes are as in §2. Lemma S and Lemma Z′ make this every finite abelian cover of the two states. Lemma Q makes it
  every pulled-back member, at every twist κ ∈ ℂ*.

## 6. Controls and disclosures (before the seal; `controls.json`, all hold, 242 s)

- **K0:** the exact holonomies satisfy the relators in PGL(2, ℚ(i)), the cusp generators commute and are parabolic, and the
  four satisfies the relators exactly.
- **K1, the banked identity:** every member (h¹, interior dimension, κ ∈ {1, −1, ±i, ω, ω²}) and every χ = 1 term at the
  banked classes reproduce sm:B1530:
  - m135's interior classes (−1, −1), c_b (0, −1), the simple members (0, 0);
  - m136's κ = −1 members (−1, −1), its κ = 1 members (0, 0).
- **K2, Lemma Z′:** 28 characters outside C_ν, at every member, have an acyclic cusp (t0 = s0 = 0 in both modules) and term
  (0, 0).
- **K3:** each C_ν is closed under the group law. The (order, subgroups) pairs are (8, 8), (4, 5) and (8, 16).
- **K4, Lemma J at χ = 1** (m135's two-class members, all four modules, c ∈ {c_b, c_int, c_b + c_int}): the pencil's
  prediction of h¹ equals h¹ computed directly in every case.
  - The generic ranks are 0 for E, E* and Λ²E, and 2 for (Λ²E)*.
  - (Λ²E)* has one special point on each member, rational, located and not read.
- **K5:** the quadratic test splits (s − 1)(s − i), s² − 2 and s² + 1 over K, and finds s² − 5 and s² − 7 irreducible.
- **K6:** the restriction of scalars at s = 2 + 0·√5 reproduces the direct reading at c_b + 2c_int, (0, −1). At s = √5, a
  generic irrational class, it reads the banked generic value (0, −1).
- **K7, route C** on two covers whose counts are banked: the 3-fold cyclic cover along t at m135's interior class reads
  (−1, −1), as Lemma Z′ gives; m136's common double cover at its κ = −1 member reads (−1, −1), as sm:B1530 found.
- **K8:** route N reproduces every banked χ = 1 term at route E's carried classes, every identity holding.
- **K9:** route N's own pencils at χ = 1 have route E's generic ranks and special points (agreement to 10⁻²⁵).
- **K10, the members at every twist** (`members_every_twist.json`, 20 s; Lemma Q).
  - **m135:** eigenvalue 1 at all eight u. Its algebraic multiplicity is 4 with geometric multiplicity 2 at u₁ and u₂, 4
    with 1 at the four characters of order 4, and 2 with 1 at (0, 0) and (½, ½). At (0, 0) and (½, ½) the other roots are
    −25.274…, −0.03957… and −2.2398…, −0.44646… (reciprocal pairs).
  - **m136:** eigenvalue 1 at all four u. Eigenvalue −1 at u₁ and u₂ (multiplicity 2, geometric 1). The other roots are
    +25.274…, +0.03957… at (0, 0) and +2.2398…, +0.44646… at (½, ½).
  - No other root lies on the unit circle; the nearest is 0.55 from it.
  - Route E's exact h¹ on μ₂₄ is non-zero only at κ = 1 (every u) and at κ = −1 (m136's u₁, u₂). It agrees with route T at
    all 288 points.
- **Disclosed:**
  - A first run of the controls (without K9) held and was replaced by this one.
  - K10 and Lemma Q were added at the seal's last review. The draft stated the population as sm:B1530's members without their
    twist scope, and members at κ ∈ μ₁₀ ∖ {±1} (case (b)) were missing from it. Lemma Q shows they add no count. This is
    logged as a self-caught scoping slip (ERROR_LEDGER, an E9 instance).
  - The run's route C was moved into its own script and set to order-4 subgroups before the seal. The exact permutation
    module on order-8 covers (dimensions 40 and 80) would take hours per reading on this bench.

## 7. Predictions (sealed; `read_out.py` reads them)

| | prediction | prior |
|---|---|---|
| P1 | Corollary I′: at m135's interior class every term with νχ simple is (0, 0), and every cover's count there lies in {(−1, −1), (0, −1), (−1, −2), (0, −2)} | 97% |
| P2 | the term at χ = (½, ½) at m135's interior class is (0, 0), so every abelian cover counts (−1, −1) there | 50% |
| P3 | Proposition H′: special classes only at χ ∈ {1, (½, ½)} | 95% |
| P4 | **the question:** no finite abelian cover of m135 or m136 carries three generations at a pulled-back member (any twist, by Lemma Q), in either order: no count (a, a) with ∣a∣ = 3 | 85% |
| P5 | every Λ² term at a simple twist (χ ≠ 1, χ(t′) = 1) at a boundary-type class is 0 | 85% |
| P6 | every generation-shaped count that occurs has ∣a∣ = 1 | 60% |
| P7 | the routes agree: E and N on every term and every special point, route C on every cover it reads | 95% |
| P8 | conjugation (Lemma D's input): conjugate members of m135 carry the same multiset of terms at each class kind | 97% |

The priors:
- **P4 and P5.** P5 rests on sm:B1530's Part C. Λ_A ∩ π_A = 0 at all 31,489 squares χ = ν² of the census, and bit_χ = 1
  needs that meet non-zero. Here χ runs over non-squares too.
  - If every bit is 0, the Λ² counts at the boundary-type classes stay at or below 1, and three needs Λ² = ±3. So P4 leans on
    P5.
  - The interior class is a theorem (P1).
- **P2 is a coin.** The (½, ½) term at c_int turns on whether c_int ∪ x_χ vanishes in the kernel of H²(M; u₂-four) → H²(P),
  which nothing banked decides.

## 8. BANKED IDENTITY: checked before reading

- `controls.py` and `members_every_twist.py` are re-run unchanged first. They must reproduce `controls.json` and
  `members_every_twist.json` in every field but the timings (and K10's start time), K1 included. Otherwise nothing is read.
- Every term the run reads at χ = 1 and a banked class must equal sm:B1530's. Every index carries B1297's identity, the
  annihilator identity and Lemma E (route E asserts them; route N checks them).

## 9. Reading rules, and what this arc will and will not claim

- **The routes must agree:** E and N on every term and every special point, and route C with the sum of route E's terms. A
  disagreement withholds the verdict and goes to ERROR_LEDGER first (the owner's rule, NO NEGATIVE FROM A BUG).
- **The verdict.**
  - If P7 fails, **WITHHELD**.
  - Else, if P4 holds, **NEGATIVE**: no finite abelian cover of m135 or m136 carries three generations at a pulled-back member
    of sm:B1515's frame at the hyperbolic point (any twist), in either order. It goes to the kill graph, with that population
    in its sentence.
  - Else, **PROVED**: three generations on an abelian cover of a silver square, both routes, read with sm:B1530's caveats.
- **Recorded either way:** every count that occurs, the special classes and their readings, the counts of two, and which
  covers carry what.
- **What the arc will not claim:**
  - anything about the covers' own members (characters or classes not pulled back from the base; §10's first question);
  - anything about non-abelian covers, where Mackey gives Ind of irreducibles of dimension > 1;
  - anything off the hyperbolic point, or about other states;
  - which cover, if any, is physical (sL-5's one bit);
  - anything bearing on I-26, the experiential question (GENESIS FK12, under Gate 5-Q), or a parameter.
- **0 of 19 stays 0.**

## 10. What this arc does not decide (the next questions)

- **The covers' own members.** These are characters fixed by the deck action but not pulled back, and the classes on a cover
  not pulled back. A count of three there is not excluded by anything here (sm:B1532 §10; the seat's task list).
- **Non-abelian covers** of the silver squares.
- **sm:B1532's levels of m004** (running), and its correction.
