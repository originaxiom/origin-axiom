# B1536 — PREREGISTRATION: THE FINITE COVERS — sm:B1515's frame on every connected finite cover of degree ≤ 12 of the golden state m004 and its sister m003, and on their Q₈ towers, at every pulled-back finite-order character, at the pulled-back class and at the covers' own classes wherever Theorem C allows two

**Sealed before `run.py` read any outcome.** At the seal this arc has computed only:
- **The population, as structure.** The covers (176 of m004 and 148 of m003 of degree ≤ 12, by low_index on sm:B1527's
  presentation; the same counts by degree on SnapPy's presentation), the eight Q₈ tower covers of each state, their cusps and
  t-periods, and the characters that can count (Lemma Z″): 8,148 (m004) and 35,100 (m003). No cohomology of a cover in the
  population has been read, except where §6 says: banked values at the trivial character on the covers K1 and the dry run
  share with the population, the two states themselves (K4), and the timing tests.
- **Two facts about the bases** (the states themselves, not their covers), used to define the members (§3):
  - T_C, the stable letter's action on H¹(F; ρ), has characteristic polynomial (s − 1)²(s² − 6s + 1) on m004 and
    (s − 1)²(s² + 6s + 1) on m003, exact over ℚ(ζ₂₄) (sm:B1530's exact_lib);
  - φ induces on F/K = Q₈ the automorphism i ↦ k, j ↦ i (m004) and i ↦ k, j ↦ −i (m003), both of order 3.
- **The controls** (§6), on banked or literature data only: K1 (sm:B1532's census on the levels as bases), K2 (sm:B1534's 148
  silver rows), K3 (sm:B1535's own-class readings), K4 (the two states themselves), K5 (the covers' counts and cusps against
  SnapPy), K6 (the read-out on synthetic rows), K7 (Lemma G's strata on m135's abelian covers) and the dry run of `run.py` on
  banked covers.
- **A design-time test of the strata** (§3, Lemma G) on m135's abelian covers, the banked population of sm:B1535's Part M,
  kept as K7. Its first form exposed an overflow in route R (§6), fixed before any control was recorded.
- **Timing tests** on three of m004's tower covers (§6): times only, except one printed row of supplies, disclosed there.

**Source.**
- **The owner, 2026-10-03:** "are u sure about the math behind your negative conclusions about three generatiosn, sure sure
  sure?"
- The day's binding rules: "aleays verify, make sure we dont hit negatives because of bugs"; "do it correctly, informedly, and
  bug free in all load bearing math"; "all oallowed not just m004, choice might be golden".
- **sm:B1535 Corollary C3**, second place: three needs n(ν³ ⊗ ρ) ≥ 3 and b0 + n(ν⁴) ≥ 3, and on non-abelian covers both supplies
  can grow. This arc reads the first such covers.

## 0. Seen first, and PRIOR ART:

**The repo sweep.** `git fetch --all` was run first. `scripts/checks/prior_work.py` ran over every head with sixteen terms:
"Q8", "quaternion cover", "non-abelian cover", "nonabelian cover", "totally geodesic", "bending", "cuspidal cohomology", "Bart",
"Scannell", "Kapovich", "Putman", "Long 1987", "PH^1", "virtual Betti", "low-index", "covers(".

| head | commit |
|---|---|
| this branch | `536dfba1` |
| main | `98714379` |
| the audit lane | `c7aa3a29` |
| seat/determined-hopper | `7cda35aa` |
| seat/magical-wright | `0043be2b` |
| seat/outside-bench | `13d2c5b6` |
| seat/paper-review-verification | `5d58b935` |
| seat/physics-seat-evaluation | `659487bb` |
| sep16-branch | `3205984b` |
| art/camper-van-bar | `b3745696` |

"quaternion cover", "nonabelian cover", "Putman", "Long 1987" and "virtual Betti" are absent everywhere. The hits that bear on
this arc:
- **B349** (frontier, a structural census): every cover of the figure-eight through index 6, by SnapPy, with H₁ of each. It read
  no twisted cohomology. **Seen first:** its H₁ table (index 4: one irregular cover with H₁ = ℤ²; index 5: ℤ³ and two ℤ/2 ⊕ ℤ²;
  index 6: ten irregular covers). From it and the mod-√−3 reduction of the holonomy (the cusp maps onto an order-3 parabolic of
  PSL(2, 𝔽₃) ≅ A₄, the longitude to 1), the design reasoned that the A₄ four-point cover has two cusps and b₁ = 2, so
  n(1) = 0 there. This is disclosed; it is not a reading, and the run reads that cover like every other.
- **sm:B1532, sm:B1534, sm:B1535.** The abelian covers: sm:B1532's census on the levels (no generation-shaped count), sm:B1534's
  silver covers (one generation at most), sm:B1535's Theorem C and Lemma W (one generation at most on every abelian cover of a
  word state at puncture-trivial characters). Every abelian cover of m004 is cyclic (H₁(m004) = ℤ), so every non-cyclic cover
  in this population is non-abelian.
- **sm:B1530** cites Kapovich and Bart–Scannell for PH¹ of the four, and states Proposition P (every κ = 1 member of a word state
  is simple except m135's two).

No head computes twisted cohomology, or sm:B1515's frame, on a non-abelian cover.

**The literature**, searched and read on 2026-10-04:
- **Putman and Wieland, "Abelian quotients of subgroups of the mapping class group and higher Prym representations"**,
  J. London Math. Soc. 88 (2013) 79–96, arXiv:1106.2747, read at ar5iv.
  - Conjecture 1.2 (no finite orbits of the higher Prym representations on V_K = H₁(K; ℚ)/(boundary)) is stated for genus ≥ 2;
    the paper notes it fails for genus 0 and 1.
  - Appendix A: π₁(Σ₁¹) = F₂ → Q₈ on a free basis; the cover has genus 3 and 4 punctures; V_K ≅ ℚ² ⊕ ℍ_ℚ, and the mapping
    class group acts on ℍ_ℚ through a finite group.
- **Bart and Scannell, "The generalized cuspidal cohomology problem"**, Canad. J. Math. 58 (2006) 673–690, read in full (the
  publisher's PDF).
  - Proposition 4.1 (after Kapovich, Math. Ann. 299 (1994)): a lattice generated by two parabolics has PH¹(Δ, ℝ⁴₁) = 0; so the
    figure-eight's is 0, and Example 1 (§4.3) confirms it with the Mendoza complex.
  - §4.3: dim PH¹(Γ, ℝ⁴₁) = dim H²(M, ℝ⁴₁) − t, and (Proposition 4.6) dim H¹ = dim ker res + t.
  - §1.3: "by the main result of [27] there always exist (probably large) finite covers which admit bending deformations", [27]
    being D. D. Long, "Immersions and embeddings of totally geodesic surfaces", Bull. London Math. Soc. 19 (1987). Long's paper
    was not read at source; it is cited through Bart–Scannell.
  - Theorem 3.1 (branched totally geodesic surfaces) and §5 (the link 8²₁₄, PH¹ = 1).
- **Scannell, "Infinitesimal deformations of some SO(3,1) lattices"**, Pacific J. Math. 194 (2000) 455–464: the abstract was read
  (bending along closed embedded totally geodesic surfaces; the Fibonacci manifolds).
- **Culler and Dunfield, low_index** (the Python package, version 1.3): the enumeration of transitive permutation
  representations. Its counts by degree agree on two presentations of each state.
- **Shapiro's lemma and Mackey's formula** as sm:B1532 cites them (Kedlaya, *Notes on class field theory*, Lemma 3.2.3).
- **Not found:** a computation of PH¹(ℝ⁴₁), or of b₁ − t, on any named finite cover of the figure-eight; sm:B1515's frame
  anywhere outside this repository.

**Standing: EXTENDS.** sm:B1532's Lemma S is extended from abelian covers to every finite cover (Lemma S′), sm:B1535's Part M from
circulant to permutation modules (Lemma O), and sm:B1535's Corollary C3 is read on non-abelian covers for the first time.

## 1. The question

On a connected finite cover N of m004 or m003, of degree ≤ 12 or in the Q₈ tower, does sm:B1515's frame carry three generations
at a finite-order character pulled back from the state, at any class of N? More generally: where are Theorem C's two supplies
both large, and which generation-shaped counts occur?

## 2. Definitions and conventions

- **The states.** m004 = +LR and m003 = −LR on sm:B1527's presentation Γ = F ⋊ ⟨t⟩, F = ⟨a, b⟩, with the cusp P = ⟨ℓ, t′⟩,
  ℓ = abAB, t′ = t (+) or abt (−). ρ is the four (h ⊗ h̄) at the hyperbolic point, exact over ℚ(ζ₂₄) (sm:B1530's
  exact_states.eisenstein_sl2 and four).
- **A cover** is a transitive right action x ↦ x^g of Γ on X = {0, …, d − 1} with base point 0; H = Stab(0) = π₁N. P is the
  permutation module, P(g)_{x,y} = [x^g = y] (so P ≅ ℂ[Γ/H]).
- **Its cusps** are the orbits O of ⟨ℓ, t′⟩ on X. The stabiliser of a point of O is a lattice in ℤ²; j₀(O), the gcd of its
  second coordinates, is O's t-period. L is the lcm of the j₀(O).
- **The characters.** ν = (u, κ): u a fibre character fixed by φ (m004: u = 0; m003: the five characters of order 1 or 5),
  κ = ν(t′); ν(ℓ) = 1. Pulled back to N they are characters of π₁N. ν is trivial on the cusp O exactly when κ^{j₀(O)} = 1.
- **The frame** (sm:B1515, verbatim in substance). V = ν ⊗ ρ, L = ν⁻⁴, V_η = ν⁵ ⊗ ρ; for a class c ≠ 0 in H¹(N; V_η),
  W₁(c) = [[V, c·L], [0, L]]; a **member** is a character with h¹(N; V_η) ≥ 1. The index is main's I(E) = n(E) − n(E*). In
  sm:B1509's dictionary N(10′) = −I(W₁), N(5̄′) = −I(Λ²W₁); **three** is (I(W₁), I(Λ²W₁)) = (−3, −3). The other stacking order
  reads W₁ at the conjugate character (sm:B1515 Lemma 7), which is in the population with all its classes.
- **The caps** (sm:B1535 Theorem C): capW = b0 + n(L) with b0 = h⁰(N; L), and capL2 = n((V ⊗ L)*) = n(ν³ ⊗ ρ*). A count of g
  generations needs min(capW, capL2) ≥ g.
- **The classes.** The pulled-back class c₀ (the state's class, at κ⁵ = 1), and the cover's own classes. For S a set of cusps
  where ν is trivial, the **stratum** C_S is the set of classes whose restriction to every other cusp where ν is trivial is zero.

## 3. The theorems (proved at design time)

**Lemma S′ (every finite cover is read on the base).** For any finite-dimensional H-module W,
H*(H; W) ≅ H*(Γ; Ind W) and H*(∂N; W) ≅ H*(P; Ind W), compatibly with restriction. So n_N(W) = n_M(Ind W) and, since
Ind(W*) = (Ind W)*, I_N(W) = I_M(Ind W). For W = Res E, Ind W ≅ E ⊗ P.
- *Proof.* Shapiro for H ⊂ Γ (finite index, so Ind = Coind). Mackey: Res_P Ind_H^Γ W is the sum over the double cosets
  P∖Γ/H, which are the cusps O, of Ind_{P_O}^P of a conjugate of W, and Shapiro on P identifies its cohomology with H*(P_O; W).
  Both identifications are natural, so they commute with restriction, and the interior parts correspond. This is sm:B1532's
  Lemma S with ℂ[A] replaced by P; for P = ⊕ m_σ σ the count is Σ m_σ I(E ⊗ σ). □

**Lemma O (the cover's own classes on the base).** Let c ∈ Z¹(H; V ⊗ L⁻¹) and let ĉ ∈ Z¹(Γ; V ⊗ L⁻¹ ⊗ P) be a cocycle with
ĉ(h)₀ = c(h) for h ∈ H (Shapiro's correspondence: restrict to H, evaluate at the base point). Then Ind W₁(c) is the module
whose generator g acts by the block matrix with (x, x^g) block W_x(g) = [[V(g), ĉ(g)_x L(g)], [0, L(g)]] and all other blocks 0;
and Ind Λ²W₁(c) has the blocks Λ²W_x(g).
- *Proof.* W_x(g) W_{x^g}(h) = W_x(gh) is ĉ's cocycle condition (g acts on V ⊗ L⁻¹ ⊗ P by V(g)L(g)⁻¹ ⊗ P(g), and
  (P(g)f)_x = f_{x^g}), so the blocks define a module, and Λ² of it by functoriality. e₀ is fixed by H, and (v, l) ↦ (v e₀, l e₀)
  is an H-map W₁(c) → Res because the base block of h ∈ H is c(h). By Frobenius it gives a Γ-map from Ind W₁(c), which is the
  standard isomorphism on the submodule Ind Res V ≅ V ⊗ P and on the quotient; by the five lemma it is an isomorphism. The
  same argument applies to Λ². At the pulled-back class ĉ = c₀ ⊗ 1 and the module is W₁(c₀) ⊗ P. □

**Lemma Z″ (the characters that can count).** If κ ∉ μ_{12L}, then I(W₁) = I(Λ²W₁) = 0 on N at every class.
- *Proof.* The pieces of W₁, Λ²W₁ and their duals are ν^m ⊗ E with m ∈ {±1, ±2, ±3, ±4} and E ∈ {1, ρ, Λ²ρ}, unipotent on each
  cusp group P_O. Such a piece is non-acyclic on P_O only if ν^m is trivial on P_O, that is κ^{m j₀(O)} = 1, which puts κ in
  μ_{12L}. Otherwise every module is acyclic on ∂N and I = 0 (sm:B1515 Lemma 4). This includes κ not a root of unity. □
So the characters (u, κ), κ ∈ μ_{12L}, carry every count of every pulled-back character, at every class.

**The members on the states.** On m004 and m003 the only root of unity among T_C's eigenvalues is 1 (§ the characteristic
polynomials above), so h¹(M; ν⁵ ⊗ ρ) ≥ 1 exactly when κ⁵ = 1, and then V_η = ρ and h¹(M; ρ) = 1: the pulled-back class c₀ exists
exactly at κ⁵ = 1 and is unique up to scale. On a cover, other κ ∈ μ_{12L} can be members through the cover's own classes.

**Theorem C on the cover** (sm:B1535, proved there and tested by its sealed run). At every pulled-back character of finite order
and every class of N: −n(ν³ ⊗ ρ*) ≤ I(Λ²W₁) ≤ 0 and I(W₁) ≥ −b0 − n(L), with b0 = h⁰(N; ν⁻⁴). Its assembly
I(W₁) = −b0 + k + rk δ¹(W₁) − rk δ¹(W₁*) and I(Λ²W₁) = k − rk δ¹((Λ²W₁)*), with k the number of cusps where ν is trivial and
the class is non-zero, is checked at every reading.

**Lemma G (the strata bound every class).** Fix (N, ν) and a stratum C_S, and let C°_S ⊂ C_S be the classes non-zero on every
cusp of S. On C°_S, k = |S|. The ranks of δ¹((Λ²W₁)*) and δ¹(W₁*) are ranks of matrices linear in the class, so on C_S they are
largest on a Zariski-open dense set; if C°_S is non-empty it is Zariski-open dense in C_S, and the generic reading has k = |S|.
Hence for every class in C°_S:
- −I(Λ²W₁) ≤ bound_L2(S) := rk_gen δ¹((Λ²W₁)*) − |S|;
- −I(W₁) ≤ bound_W(S) := b0 − |S| + rk_gen δ¹(W₁*).
Every class lies in exactly one C°_S. So three is impossible in C°_S if either bound is below 3. A stratum with both bounds
≥ 3 and a generic count other than (−3, −3) is **open**: its special classes are not read.
- *Proof.* The rank statements are lower semicontinuity of rank. The two inequalities follow from the assembly above with
  rk δ¹(W₁) ≥ 0. □

**Proposition Q (the Q₈ tower's line).** K = ker(F → Q₈), a ↦ i, b ↦ j, is characteristic in F (Aut(Q₈) acts simply transitively
on the 24 generating pairs, so every surjection F → Q₈ has kernel K). So φ preserves K, H_m = K ⋊ ⟨t^m⟩ has index 8m, and its
cosets (fK, s), 0 ≤ s < m, carry the action of `cover_lib.q8_tower`. The cover N_{8,m} fibres with fibre the Q₈ cover of the
once-punctured torus (genus 3, 4 punctures) and monodromy ψ^m, ψ = φ|_K. At κ = 1, n(1) = dim(H₁(K; ℚ)_ℍ)^{ψ^m}, the ψ^m-fixed
part of the ℍ-isotypic component (4-dimensional over ℚ).
- *Proof.* Gaschütz: H₁(K; ℚ) ≅ ℚ ⊕ ℚ[Q₈]: the trivial isotypic part (2-dimensional, ≅ H₁(F; ℚ) by transfer), the three sign
  characters once each, and ℍ_ℚ. The puncture classes span exactly the sign part (ℚ[Q₈/⟨−1⟩] minus the trivial line, since the
  punctures are the cosets of ⟨[i, j]⟩ = ⟨−1⟩). ψ normalises the deck action, so it preserves the trivial and the ℍ parts and
  permutes the sign part as it permutes the punctures. Then b₁(N) = 1 + dim H₁(K)^{ψ^m} = 1 + 0 + (t − 1) + dim ℍ^{ψ^m} (φ is
  Anosov on H₁(F), and a permutation module has one fixed vector per orbit), and n(1) = b₁ − t. □
By Putman–Wieland's Appendix A the action on the ℍ part has finite image. ψ³ commutes with the deck group (β³ = 1), so it acts on
the ℍ part by right multiplication by a unit of a ℤ-order in the definite quaternion algebra, of order 1, 2, 3, 4 or 6. So
ψ^m is trivial there for some m ∈ {3, 6, 9, 12, 18}, all in the population, where n(1) = 4 and capW = 5 at κ = 1.

## 4. The instruments (`verification/`, written and tested before the seal)

- **`cover_lib.py`** (shared: the population). The states and their exact holonomy; low_index covers; the canonical form of a
  Γ-set; the Q₈ tower; the cusps with their stabiliser lattices (Hermite normal form) and t-periods.
- **`gf.py`** (shared: the input data mod p). ℚ(ζ₂₄) → GF(p) for p ≡ 1 mod N, with every root of unity of order dividing N.
- **`route_n.py`, route N.** The cover read on the base (Lemmas S′ and O): block-monomial modules, Fox calculus on the base's
  presentation, every rank and kernel by FLINT's nmod_mat (python-flint 0.9.0) at a prime p < 2²⁴ (so every int64 product sum
  is exact). The supplies, the frame's twelve cohomologies per reading, B1297's identity, the annihilator identity and sm:B1527's
  Lemma E on every module and piece, Theorem C's identities, and the strata.
- **`route_r.py`, route R.** It shares no linear algebra with route N: the cover's own Reidemeister–Schreier presentation
  (spanning tree, Schreier generators, rewritten relators, rank check), the cover's cusps read from the orbits (each cusp group
  generated by the rewrites of its two lattice vectors), every module restricted to the Schreier words, every rank and kernel
  by PARI over GF(p) (cypari's matrank and matker) at a prime p < 2³¹, products and small inverses by numpy (sm:B1535's banked
  rs_lib), Λ² through the tensor square, and its own classes for the strata.
- **`population.py`, `run.py`** (the run, one route at a time, resumable), **`read_out.py`** (the predictions),
  **`identity.py`** (§8).
- **`control_k1.py` … `control_k5.py`, `read_out_selftest.py` (K6), `control_k7.py`, `dry_run.py`** (§6).

## 5. The population

| state | covers of degree ≤ 12 | Q₈ tower | characters (u, κ ∈ μ_{12L}) |
|---|---|---|---|
| m004 | 176 | m = 1, 2, 3, 4, 6, 9, 12, 18 | 8,148 |
| m003 | 148 | m = 1, 2, 3, 4, 6, 9, 12, 18 | 35,100 |

At each (N, ν):
- **Part S** reads the supplies: h¹(V_η) (membership), n(V_η), b0, n(L), n(ν³ ⊗ ρ*), and the caps.
- **Part P** reads the pulled-back class at every member with κ⁵ = 1.
- **Part O** reads, at every member with min(capW, capL2) ≥ 2, every stratum C_S, at two random classes each, in full.
Each route reads everything: Part S at every (N, ν), and Part P and Part O wherever they apply, each route deciding membership
and the caps by its own cohomology.

## 6. Controls and disclosures (before the seal)

Every control reads banked or literature data only. Some of the covers they read are also in this arc's population:
- **K4** reads the two states themselves (the covers of degree 1), whose values are banked.
- **K1 and the dry run** read the finite abelian covers of the levels M₂ and M₃ (K1 also M₆'s, of order ≤ 4). Those of
  degree ≤ 12 over m004 are covers in the population, and the trivial character is one of its characters. There K1's Part P
  counts are sm:B1532's banked values. The dry run also computed Part S there and recorded only whether the routes agree; no
  value was printed or read.
No other cover of the population was read at any character, except in the timing tests disclosed below.

- **K1** (`control_k1.py` → `k1.json`, 174 s; `k1_m6.json`). sm:B1532's census with the levels as bases: every finite abelian
  cover of M₂ and M₃ (2 and 15 subgroups) at every λ = 1 member, at the pulled-back class, in both routes (primes 16,776,961
  and 2,147,482,921). The histograms equal the banked ones exactly: M₂ (0, 0) × 10; M₃ (0, 0) × 40, (1, 0) × 144, (3, 0) × 44,
  (5, 0) × 12. On M₆ (`k1_m6.json`, 3,500 s), at the 11 subgroups of order ≤ 4 and all 320 members, route N's histogram
  equals the banked one at all 4,840 readings, the two-class members read at the interior class and at a generic class;
  route R reads the one-class members only, and its histogram equals the banked one at their 2,200 readings
  (`k1_m6_check.py` → `k1_m6_check.json`). No reading failed an identity, and at the one-class members the routes agree
  reading by reading.
- **K2** (`control_k2.py` → `k2.json`, 39 s). sm:B1534's 148 banked rows (each member's count over each subgroup at its
  non-special classes), in both routes: all 148 reproduced, the 28 generation-shaped rows (−1, −1) among them.
- **K3** (`control_k3.py` → `k3.json`, 193 s). sm:B1535 Part M's own classes on the silver squares' abelian covers: 328 pure
  readings ('the class' and 'c_int', placed through Lemma O in route N and on the Schreier words in route R) and, at all 102
  pairs, two random classes of the full class space in each route. Every pure reading equals Part M's in count and k. Every
  generic draw equals the banked reading of largest connecting ranks, in count, k and every connecting rank.
  - Disclosed: K3 was written before sm:B1535's read-out and first compared the draws with both of Part M's generic classes.
    That read-out failed its P6 at one pair, where one of Part M's small-coefficient classes is special. The comparison was
    then changed to the banked reading of largest ranks (the generic rank is the largest, by lower semicontinuity), and pairs
    whose banked draws differ are listed. The one such pair (m136, ν = (½, 0; ½), order 4) reads rank 4 in all four draws.
- **K4** (`control_k4.py` → `k4.json`, 2 s). The two states themselves (degree 1), both routes, through `run.py`. On m004 at
  κ = 1: h¹(ρ) = 1, n(ρ) = 0 (Kapovich, as Bart–Scannell Prop. 4.1 and Example 1 state it), n(1) = 0 and the count (0, 0)
  (sm:B1515's M₁ row); no member at κ ∈ {−1, ±i, ω, ω²}. On m003 every κ = 1 member is simple (sm:B1530 Proposition P). The
  routes agree.
- **K5** (`control_k5.py` → `k5.json`, 32 s). The population's structure. The covers by degree agree on sm:B1527's presentation
  and on SnapPy's through degree 12 (m004: 1, 1, 1, 2, 4, 11, 9, 10, 11, 38, 26, 62; m003: 1, 1, 1, 2, 8, 7, 5, 10, 7, 40, 22,
  44), and the (degree, cusps) table agrees with SnapPy's covers through degree 8.
- **K6** (`read_out_selftest.py` → `k6.json`). `read_out.py`'s logic on synthetic rows. The clean record gives every prediction
  and completeness true; each of 17 planted defects turns false exactly the predictions it bears on (none, for the two that
  bear on none).
- **K7** (`control_k7.py` → `k7.json`, 13 s). Lemma G's strata on three of sm:B1535 Part M's covers of m135 (two of order 2, one
  of order 4 with four cusps): all 24 strata, two draws each, agree between the routes in count, k and every connecting rank,
  with every identity holding.
- **The dry run** (`dry_run.py` → `dry_run.json`). `run.py`'s `read_cover` on M₂'s and M₃'s abelian covers at λ = 1, both
  routes: Part P's census equals the banked one and Part S agrees on all 250 rows. Part O did not trigger.

**Disclosures.**
- **Route R's overflow** (ERROR_LEDGER). K7's first form found route R's random combination of class-space vectors summing
  products near 2⁶² before reducing mod p. Its draws disagreed with route N's, and an empty stratum read k = 4. The combination
  now reduces at every step. This was found before any control was recorded.
- **Route R's elimination moved from numpy to PARI.** numpy row reduction took 61 s on a 1,440-column matrix where PARI takes
  2.5 s. After the switch K1 (M₂, M₃), K2, K4, the dry run and the strata test were re-run and hold. K1's M₆ run was restarted
  under PARI.
- **Route R's coverage, changed before the seal.** The draft read the tower covers of degree 72, 96 and 144 in route R only at
  a sample of characters, which would have left Part O there read by one route. Route R now reads every character of every
  cover and decides membership and the caps by its own cohomology. With it:
  - `read_out.py` checks each route's rows against the population (completeness);
  - P8 and P9 look at every reading of both routes;
  - Lemma G's bounds take each connecting rank's larger value over the two draws;
  - P7's text says "member", as its code always read.
  K6 tests each change, and K4 and the dry run were re-run on the changed `run.py`.
- **K1's route R comparison on M₆.** `control_k1.py`'s flag 'route R = banked' compared route R's histogram with the whole
  banked one, which on M₆ also holds the two-class members' classes. Route R reads one-class members only, so the flag read
  false by construction while every reading agreed. Found while the M₆ run was going; the run was not touched.
  `k1_m6_check.py` compares the recorded histograms as intended (nothing recomputed), and `control_k1.py` now compares
  route R at the one-class members. On M₂ and M₃ every member has one class, so `k1.json` is unchanged by the fix.
- **Timing tests on the population**, before the seal, to plan the run. Route R's supplies were timed on m004's Q₈.m9, Q₈.m12
  and Q₈.m18 at one character each, and one full reading at the split class c = 0 in each route on Q₈.m18 (route N 467 s,
  route R 117 s, on a loaded machine). The first script printed the supplies it computed at one character of Q₈.m9
  (κ = 7/108): all zero, not a member. Every later script printed times only.
- **Seen first** (§0): K5's (degree, cusps) table, B349's H₁ table and the A₄ inference.

## 7. Predictions (sealed; `read_out.py` reads them)

| | prediction | prior |
|---|---|---|
| P1 | the routes agree on every quantity both read: every supply, every Part P count, k and connecting rank, every Part O stratum's generic reading | 95% |
| P2 | every reading in either route has its identities and Theorem C's identities and caps holding | 97% |
| P3 | on every abelian cover in the population, n(L) = 0 at every pulled-back character (sm:B1535 Lemma W) | 99% |
| P4 | n(1) = 0 at κ = 1 on every cover of degree ≤ 12 of both states | 45% |
| P5 | on each state's Q₈ tower, n(1) at κ = 1 reaches 4 at some m and never exceeds 4 (Proposition Q) | 90% |
| P6 | n(ρ) = 0 at κ = 1 on every cover of degree ≤ 12 of both states | 50% |
| P7 | no member (N, ν) has both caps ≥ 3 | 60% |
| P8 | no class read carries three, in either route | 92% |
| P9 | no pulled-back class carries a generation-shaped count of any size | 70% |
| P10 | no stratum is open (Lemma G) | 90% |

The priors sum to 7.88.

## 8. BANKED IDENTITY: checked before reading

`identity.py` runs before `run.py` reads anything:
- `control_k2.py` must reproduce `k2.json` (sm:B1534's 148 rows, both routes) in every field but the timings;
- `control_k4.py` must reproduce `k4.json` (the two states, both routes);
- `control_k1.py` on M₂ and M₃ must reproduce `k1.json` (sm:B1532's census histograms, both routes);
- `control_k5.py` must reproduce `k5.json`, and `read_out_selftest.py` (K6) `k6.json`;
- every sealed file's sha-256 must equal ARTIFACT_HASHES.txt.
A single difference stops the run, and nothing is read.

## 9. Reading rules, and what this arc will and will not claim

- **The verdict on three.**
  - **NEGATIVE** if both routes read the whole population (the read-out's completeness check) and P1, P2, P8 and P10 hold: no
    class of any cover in the population carries three at any pulled-back character. Where min(capW, capL2) < 3 this holds at
    every class by Theorem C; elsewhere at every class by Lemma G.
  - If P8 holds and P10 fails, the negative is scoped to the strata that are not open, and the open strata are listed as OPEN.
  - **POSITIVE** only if a three is read in both routes, and then read again at a third prime and by an exact or numeric check
    before anything is claimed.
  - A disagreement between the routes is investigated before anything is banked. A bug is fixed, disclosed and re-read.
- **The kill record**, if NEGATIVE: F-HE at the hyperbolic point; m004 and m003; every connected finite cover of degree ≤ 12 and
  the Q₈ tower at the eight m; every pulled-back character of finite order (Lemma Z″); every class (Theorem C and Lemma G).
- **Not claimed.**
  - The covers' own characters: characters of π₁N not pulled back from the state.
  - Covers of larger degree, other states, non-unitary characters.
  - Held vacua (R76), selection, anything off the hyperbolic point.
  - The index is the frame's count; its reading as generations is sm:B1509's dictionary. **0 of 19 stays 0.**

## 10. What this arc does not decide (the next questions)

- **The covers' own characters**, on the non-abelian covers and on the abelian ones (sm:B1535's item 15). On the Q₈ tower the
  line's supply n(ν⁴) at characters of π₁N not pulled back from the state is not read here.
- **Larger covers**: the congruence covers of higher level (A₅ at degree 60, PSL(2, 𝔽₇) at 168), and covers carrying embedded
  closed totally geodesic surfaces (Long, through Bart–Scannell), where the four's supply grows by bending.
- **The silver squares and the other word states** on non-abelian covers.
