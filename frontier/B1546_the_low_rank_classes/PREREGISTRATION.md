# B1546 — PREREGISTRATION: THE LOW-RANK CLASSES — where three can still live on N₄₅ at the trivial character: the classes of cup rank one and two, mapped (Proposition L) and read

**Sealed before `run.py` read any count at a class of cup rank one or two.** At the seal this arc has:
- **proved, at design time** (§3):
  - where three can live on N₄₅ at the trivial character: at classes of cup rank one or two (Corollary F′ with sm:B1544);
  - Proposition L: the interior classes of cup rank at most two are, in the deck grading, the classes c of a ten-dimensional
    space Kc0 whose symmetric 4 × 4 matrix S(c) has rank at most two. Here S is a linear isomorphism of Kc0 onto the
    symmetric matrices, and rk δ¹_W(c) = rk S(c). So the classes of cup rank one are the squares S(c) = ℓℓᵀ;
  - Lemma G‴ (a generic class has the least I(W) on its family);
  - Lemma M: at an interior class of Kc0, I(W) = −1 − μ(c) with μ(c) ≥ 0.
- **computed structure only** (§6), in two routes: the cup map δ¹_W on the deck group's eigen-parts, the spaces of
  Proposition L, the squares, the three-cusp strata of K0, the cusps and the deck group on them.
- **read counts only where the record has them banked**: sm:B1541's generic interior classes, sm:B1544's three-cusp strata of
  K0, and the generic class of H¹ (controls K3 and K6).

**Source.**
- The owner, 2026-10-04: "thanks, keep focused. three generations is smth we are after seripuslu"; "make sure nothing is lost.
  make sure we dont abandon the golden pointer".
- The owner, 2026-10-06: "we should verify all load bearing math even if a published paper, because we cant bet our whole
  project against some possible errors bugs or mistakes"; "breakthrough breaktheough breakthrough!!! is expected from you".
- sm:B1544's FINDINGS §10 and its relay of 2026-10-06 (§8 there): on N₄₅, outside the cup map's kernel K0, Corollary F′
  leaves the classes of cup rank one and two. They are the last place three can live on the golden cover at the trivial
  character.

## 0. Seen first, and PRIOR ART:

**The repo sweep.** `git fetch --all` ran first (2026-10-06, 20:15Z). `scripts/checks/prior_work.py` then ran over every head
with twelve terms: "persymmetric", "Veronese", "symmetric 4 x 4", "Sym^2", "Massey rank", "cup rank", "rank-one class",
"low-rank", "secant variety", "determinantal", "rank <= 2", "square of a class".

| head | commit |
|---|---|
| this branch | `c1590205` |
| main | `965f8a45` |
| the audit lane (fork) | `8b89d8fb` |
| the audit lane (physical bridge) | `c161981d` |
| the new web seat's branch (…/web-seat) | `7c5bb737` |
| seat/outside-bench | `13d2c5b6` |
| seat/paper-review-verification | `5d58b935` |
| seat/kind-hypatia | `6a537f89` |
| seat/project-thread | `3a802c0d` |
| sep16-branch | `3205984b` |

What the sweep found:
- "Veronese", "secant variety", "rank-one class" and "square of a class" are absent on every head. "Massey rank" appears
  only in this arc's own uncommitted files.
- "persymmetric" has 119 hits, and every one is inside the word "supersymmetric" (checked with `git grep` on this branch,
  main and the physical-bridge lane: 305 occurrences, all "supersymmetric", "unsupersymmetric" or "nonsupersymmetric"). No
  head names a persymmetric matrix.
- **"cup rank" bears through this seat's own arcs.**
  - sm:B1542 and sm:B1544 use the cup map's rank in Theorem C's terms. They compute K0 and its strata. They map no rank locus
    outside K0.
  - main's B1332 ("the cup product vanishes") is another object: the cup product of boundary-restricted classes behind an
    index, at one cusp.
- "low-rank", "determinantal", "rank <= 2", "symmetric 4 x 4" and "Sym^2" hit other objects: matrix ranks in other arcs'
  scripts (B1275, B1296, B1428, B1431, B1532), Lie-algebra Sym² in the gauge-structure arcs, and the surfaces. None reads a
  class of H¹(N; ρ).

**The literature.**
- T. Nosaka, "Twisted cohomology pairings of knots III; triple cup products", arXiv:1808.08532 (2018), abstract, read
  2026-10-06. It introduces a trilinear form from a representation of a link group. For hyperbolic links it equals the pairing
  of the twisted triple cup product with the fundamental relative 3-class. Lemma M uses a trilinear form of that kind,
  (c, z, x) ↦ ∫ c ∪ z ∪ x. The paper does not compute this cover or these coefficients.
- C. D. Monroe, "Branched bending in finite-volume hyperbolic manifolds", arXiv:2604.22004 (2026), abstract, read 2026-10-06.
  - It works with bending deformations (Johnson–Millson) and with the deformations that do not deform the cusps (the kernel
    of restriction to the boundary).
  - H¹(N; ρ), with ρ the Minkowski representation of the holonomy, is the space of infinitesimal deformations into SO(4, 1).
    Its interior classes are the cusp-preserving ones.
  - No cup-product structure on them is stated there.
- P. Menal-Ferrer and J. Porti, "Twisted cohomology for hyperbolic three manifolds", arXiv:1001.2242 (read for sm:B1544, §0
  and §3.1): the cusp-torus facts behind Lemma F. This frame's ρ = V₂ ⊗ V̄₂ is not among their representations.
- Classical linear algebra, used as stated:
  - a persymmetric matrix P (Pᵀ = JPJ, J the exchange matrix) has PJ symmetric;
  - the symmetric matrices of rank at most one are the ℓℓᵀ, a cone of dimension 4 over the Veronese threefold;
  - those of rank at most two form an irreducible cone of dimension 7, and each is ℓ₁ℓ₁ᵀ + ℓ₂ℓ₂ᵀ over ℂ.

**Standing: NEW-AS-SWEPT** for Proposition L on N₄₅ (a computed structure on one cover, in two routes at two primes) and for
Lemma M as stated. EXTENDS sm:B1544 (its §10's open classes are mapped and read).

## 1. The question

At the trivial character on N₄₅, does any class of H¹(N; ρ) read three, (−3, −3)? sm:B1544 read all of K0 (cup rank 0). This
arc maps every class of cup rank one or two and reads each family at its generic class, plus the deck group's eigen-lines in
it. If no family's generic class reads I(W) = −3, no class of N₄₅ does, and the golden cover carries no three in this frame
at the trivial character.

## 2. Definitions and conventions

- **The frame** is sm:B1536's at the trivial character, as in sm:B1544 §2: W = [[ρ, c], [0, 1]] for c ≠ 0 in H¹(N; ρ). The
  count is (I(W), I(Λ²W)), and the cup map is δ¹_W(c) : H¹(N; ℂ) → H²(N; ρ), y ↦ c ∪ y, of rank r(c). Also:
  - δ¹_{W*}(c) : H¹(N; ρ*) → H²(N; ℂ), z ↦ c ∪ z, has rank s(c);
  - k is the size of the support (the cusps where c is non-zero);
  - a = dim(⟨c_T⟩ ∩ Λ(ρ)), as in sm:B1544 §2.
- **N₄₅** (sm:B1541): five cusps, the deck group τ of order 5 permuting them cyclically (0 → 1 → 4 → 2 → 5 → 0). Its
  cohomology has these dimensions:
  - h¹(ρ) = 23 and n(ρ) = 18, with the interior part H¹_int of dimension 18;
  - h¹(ℂ) = 9 and n(1) = 4;
  - K0 has dimension 5, and H¹ = H¹_int ⊕ K0.
- **The deck grading.**
  - H¹(N; ℂ) = ⊕ E_m and H¹(N; ρ) = ⊕ V_j over τ's eigenvalues ζ^m and ζ^j. E_m has dimension 1, 2, 2, 2, 2.
  - V_j^int, the interior part of V_j, has dimension 2, 4, 4, 4, 4.
  - c_j ∪ E_m lies in the ζ^(j+m) part H²_(j+m) of H²(N; ρ). The block of c_j ∈ V_j on E_m is B_jm(c_j).
  - K_m = {c : c ∪ E_m = 0}.
  - A twisted index is j ≠ 0.
- **The spaces.**
  - Kc = V_0^int ⊕ ⊕_(j≠0) (K_−j ∩ V_j^int), of dimension 2 + 4 · 3 = 14.
  - Kc0 = V_0^int ⊕ ⊕_(j≠0) (K_0 ∩ K_−j ∩ V_j^int), of dimension 2 + 4 · 2 = 10.
- **The eigen-lines of Kc0.**
  - u_j: c ∪ E_m = 0 for m ≠ 2j.
  - w_j: c ∪ E_m = 0 for m ∈ {0, −j, 2j}.
  - v_a: c ∪ E_m = 0 for m ∈ {2, 3}; v_b: for m ∈ {1, 4}.
  - Each is one class up to scale, of cup rank 1 (u_j) or 2 (w_j, v_a, v_b), and together they span Kc0 (K1).
- **The routes** are sm:B1544's, unchanged:
  - route F (route_f.py on the lifted 2-complex of ⟨a, t | ttATAAATA⟩, p_F = 67108201);
  - route R (route_r.py on N₄₅'s own presentation, p_R = 2147482801).
  - Each computes its own eigen-parts, spaces and classes, and the eigenvalue labels are each route's own choice of ζ. The
    lines' definitions (2j, −j) are equivariant under relabelling, so they name the same lines up to the Galois action of §7.

## 3. What is proved at design time

**3.1 Where three can live on N₄₅** (sm:B1544's Corollary F′ with n(1) = 4 and m = 5). A class with I(W) = −3 has
a + r ≤ 2 and k ≤ 3.
- r = 0: c ∈ K0. sm:B1544 read every stratum of K0 on N₄₅: none reads I(W) < 0.
- r = 2: then a = 0, so c is interior (a ≥ 1 otherwise, sm:B1544 §2).
- r = 1, interior; or r = 1 with a = 1 and k ≤ 3. In the last case write c = c_int + κ with κ ∈ K0. Then r(c_int) = 1, and
  κ has the support of c (c_int restricts to coboundaries). κ lies in K0 of its own support, which is closed (sm:B1544 §2).
  The closed supports of K0 on N₄₅ of size ≤ 3 are the ten sets of three cusps, each with dim K0(S) = 1. So κ ∈ K0(S) for one
  of them.

So every class reading I(W) = −3 is an interior class of cup rank 1 or 2, or (cup rank 1 interior) + K0(S) with |S| = 3.

**3.2 Proposition L (the classes of cup rank at most two).** The checks run in both routes (`prop_l.py`, control K1).
- **L0.** The spaces H²_t spanned by the blocks with j + m = t have dimensions 2, 4, 4, 4, 4, and their sum is direct.
- **L1.**
  - (a) For every twisted j and every m ∉ {0, −j}, the pencil y ↦ (c ↦ c ∪ y) on V_j^int (y ∈ E_m) has rank exactly 2 at every
    y ≠ 0, and its kernel lies in K_−j for every y. Two exact checks establish this:
    - the 2 × 2 minors, binary quadratics, have no common zero on ℙ¹;
    - the 3 × 3 minors of [A(y); c ↦ c ∪ E_−j], of degree at most 3, vanish at five points of ℙ¹.
    So a class of V_j^int outside K_−j has blocks of rank 2 at all three m ∉ {0, −j}.
  - (b) The blocks of V_0^int have rank at most 1, and 0 on E_0.
- **L2.**
  - On Kc the image of δ¹_W is 4-dimensional, one line v_t in each H²_t with t ≠ 0. So δ¹_W(c) = Σ_t v_t ⊗ Φ_t(c), and
    rk δ¹_W(c) = rk Φ(c), a 4 × 9 matrix.
  - On Kc0 each block of Φ lies along one direction f_m of E_m*, and the E_0 column vanishes.
  - The γ-part H is a 4 × 5 matrix, linear in the z-coordinates γ of Kc (z_j ∈ K_−j ∖ K_0). Its columns are the E_0 column and,
    in each E_m*, the part off f_m. Every γ_j³ lies in the ideal of H's 3 × 3 minors (a Gröbner basis mod p).
- **L3.**
  - On Kc0 the f-coefficients form a 4 × 4 matrix F(c), rows t = 1…4 and columns m = 1…4.
  - The eigen-lines fill F's entries exactly once: u_j fills (3j, 2j), and each of w_j, v_a, v_b fills a pair (t, m),
    (5 − m, 5 − t).
  - The six ratios of the paired entries' constants form a coboundary. So F is persymmetric after scaling its rows, columns
    and lines, and S(c) = F(c)J (rescaled) is a symmetric 4 × 4 matrix depending linearly and bijectively on c ∈ Kc0.

*Proof that L0–L3 give the Proposition.* Let c be an interior class with r(c) ≤ 2 (a K0 part changes nothing, since δ¹_W
vanishes on K0).
- **c lies in Kc.** Suppose a twisted part c_i lies outside K_−i. By L1(a) its blocks at the three m ∉ {0, −i} have rank 2.
  - Take m with m and m′ = m + i both outside {0, −i}. Two exist, the m ∉ {0, −i, −2i}.
  - The E_m column block of δ¹_W(c) has the rank-2 block B_im(c_i) as its H²_(i+m) component (L0). So the image I of
    δ¹_W(c), of dimension at most 2, is δ¹_W(c)(E_m), and it projects isomorphically onto a plane of H²_(i+m). The same holds
    for m′, so δ¹_W(c)(E_m′) = I as well.
  - Its H²_(i+m) component is then 2-dimensional. But that component is B_(0,m′)(c_0)(E_m′), of rank at most 1 by L1(b). This
    is a contradiction, so c ∈ Kc.
- **c lies in Kc0.** On Kc, H(γ(c)) is a submatrix of Φ(c) after column operations inside each E_m* slot, so
  r(c) ≥ rk H(γ(c)). By L2, rk H(γ) ≤ 2 forces γ = 0.
- **The rank on Kc0.** On Kc0, r(c) = rk F(c) = rk S(c) (L3). □

**Corollary L′ (the families).**
- **Z1**, the interior classes of cup rank 1, is S⁻¹{ℓℓᵀ}: the squares, an irreducible cone of dimension 4.
- **Z2**, the interior classes of cup rank at most 2, is S⁻¹{rank ≤ 2}: an irreducible cone of dimension 7, generically of
  cup rank 2.
- **X_S**, for each of the ten three-cusp sets S, is Z1 + K0(S): the image of (ℓ, t) ↦ S⁻¹(ℓℓᵀ) + tκ_S, irreducible. On a
  dense open part it has r = 1, k = 3 and a constant a, since the boundary restriction is tκ_S's.
- With 3.1, **every class of N₄₅ reading I(W) = −3 at the trivial character lies in Z1, Z2 or one of the ten X_S.**

**How the squares are drawn.** The image of δ¹_W on Kc0 is span{v_t}, of dimension 4. For a vector v of it, the solutions
(c, φ) of δ¹_W(c) = v ⊗ φ form one line: for S(c) = ℓℓᵀ the image of F(c) is the rescaled ℓ, so v fixes ℓ up to scale. A
random v gives a generic square (control K7 checks the solution space and the class's rank and support in both routes).

**Lemma G‴ (generic classes decide each family).** On an irreducible family on which r, k and a are constant on a dense open
subset, route R's identity I(W) = −1 + k + r − s gives the least I(W) at the classes where s is largest. Rank is lower
semicontinuous, so these form a dense open subset. A draw misses the closed exceptional set except with probability below
δ/p, by Schwartz–Zippel through the polynomial parametrisation, with δ its degree. Each family is drawn three times in each
route, at two primes.

**Lemma M (the Massey term).** For an interior class c of Kc0, I(W) = −1 − μ(c) with μ(c) = s(c) − r(c) ≥ 0.

*Proof.*
- At an interior class k = 0, so I(W) = −1 + r − s (route R's identity).
- By Poincaré–Lefschetz duality, H²(N; ℂ) ≅ H¹(N, ∂N; ℂ)* and H¹(N; ρ*) ≅ H²(N, ∂N; ρ)*, through ∫ c ∪ z ∪ x. So s is the
  rank of x ↦ c ∪ x from H¹(N, ∂N; ℂ) to H²(N, ∂N; ρ).
- Its composite with H²(N, ∂N; ρ) → H²(N; ρ) is δ¹_W(c) on the image of H¹(N, ∂N; ℂ), which is H¹_int(N; ℂ). So s is at least
  the rank of δ¹_W(c) on H¹_int(N; ℂ).
- On Kc0, δ¹_W(c) restricted to the line's interior classes x̄_m (one in each E_m, m ≠ 0) is V·F(c)·diag(f_m(x̄_m)). The
  four f_m(x̄_m) are non-zero: K1 checks that the rank on the four interior line classes equals the cup rank at every
  eigen-line and at a generic class of V_0^int, where F is diagonal of rank 4.
- So that rank is r(c), and s ≥ r. □

μ(c) is the rank of the boundary part. The relative products c ∪ x whose absolute part vanishes lie in the image of
H¹(∂N; ρ), a Massey-type term. **So at an interior class of Kc0 the floor I(W) ≥ −1 holds exactly when μ = 0, and three there
needs μ = 2.** Corollary C′ (sm:B1543) bounds I(W) ≥ r − 5, that is −4 on Z1 and −3 on Z2.

## 4. The instruments (`verification/`, written and checked before the seal)

- `lowrank_lib.py`, in both routes. It loads sm:B1544's floor_lib by path, unchanged.
  - The line's and the four's eigen-parts.
  - The cup matrices, the strata, V_j^int and K_m.
  - The eigen-lines, Kc0 and its image.
  - The squares (`rank1`) and the line's interior classes.
- `prop_l.py`: Proposition L's checks L0–L3 in one route.
- `run.py`: the tasks of §5, resumable, one row per reading (`run.jsonl`). The subspaces and their sealed ranks and supports
  are in `run.SUBSPACES`.
- `read_out.py`: the predictions of §7 from the rows, once. `evaluate` is pure.
- `controls.py`: K1–K7 (§6). `identity.py`: the banked identity (§8).

## 5. The population of classes (outcome-blind; seeds crc32 of "B1546|route|subspace|draw")

Three draws of each subspace in route F and three in route R, each route drawing its own classes:

| subspace | the class drawn | cup rank | support |
|---|---|---|---|
| Z1 | a generic square, a·S⁻¹(ℓℓᵀ) | 1 | ∅ |
| Z2 | the sum of two generic squares with generic weights | 2 | ∅ |
| X:S, for each of the ten sets S of three cusps | a generic square plus a generic multiple of κ_S | 1 | S |
| u_j, w_j (j = 1…4), v_a, v_b | the eigen-line, at a random scale | 1 (u), 2 (w, v) | ∅ |

In all, 22 subspaces, 66 tasks and 132 readings. The generic families decide the least I(W) on each family (Lemma G‴). The
eigen-lines are special classes of Z1 and Z2, read for what they are: the deck group's own classes there, where the Λ² count
may differ from the generic one.

## 6. Controls and disclosures (before the seal)

All hold (`verification/controls.json`). This design's controls ran first as a trial (20:16–20:18Z on 2026-10-06), then
for the record (20:27:33–20:29:43Z), unchanged between the two but for Lemma M's input, added to K1 after the trial.
- **K1.** Structure in both routes equals the sealed values (`controls.STRUCTURE`):
  - Proposition L, all of L0–L3;
  - the dimensions of V_j^int (2, 4, 4, 4, 4), (K_−j)^int (3 each), Kc0 (10, meeting K0 in 0) and the image (4);
  - the ten eigen-lines (one class each; cup ranks 1, 2, 2) and the entries of F each fills;
  - Lemma M's input: four interior line classes, and the cup rank on them equal to the cup rank at every eigen-line and at a
    generic class of V_0^int;
  - the ten three-cusp strata of K0 (one class each, support S);
  - the cusp labels and τ on the cusps.
  Both routes give the same supports of F: u₁ (3, 2), u₂ (1, 4), u₃ (4, 1), u₄ (2, 3); w₁ (2, 1) and (4, 3); w₂ (3, 1) and
  (4, 2); w₃ (1, 3) and (2, 4); w₄ (1, 2) and (3, 4); v_a (1, 1) and (4, 4); v_b (2, 2) and (3, 3).
- **K2.** The cochain formula for the cup map equals the long exact sequence's rank, h¹(V) + h¹(L) − h¹(W) − 1. It is checked
  at a class of each kind (Z1, Z2, X:S=0,1,2, u₁, w₁, v_a) in both routes, with the sealed rank.
- **K3.** Banked counts reproduced in both routes:
  - a generic interior class reads (4, −10), a generic class of V_0^int (−1, −10) and of V_1^int (3, −10) (sm:B1541);
  - a generic class of K0({0, 1, 2}) reads (0, 0) (sm:B1544).
- **K4.** The read-out on synthetic rows, thirteen cases. They cover:
  - each prediction's refutation, including a τ-orbit split, a route split, a Galois split and an eigen-line below its
    family;
  - incomplete records and Lemma M's failure;
  - the three verdicts, including OPEN when a family reads I(W) = −3 without three.
- **K5.** Route F's and route R's cusps coincide as point sets, and the deck transformations are the same permutation.
- **K6.** Lemma F's ingredients at a generic class of H¹, which reads the banked (5, −5), in both routes.
- **K7.** The draws, structure only:
  - at three random vectors of the image the square is one class, of cup rank 1 and empty support;
  - the sum of two has cup rank 2;
  - a square plus K0({0, 1, 2}) has cup rank 1 and support {0, 1, 2}.

### 6a. The load-bearing inputs (WORKING_RULES 2026-10-06), each re-derived by own code on every instance used

| | input | source | own check |
|---|---|---|---|
| LB1 | Theorem C (ii), Corollary F′ and route R's identities | sm:B1535, sm:B1536, sm:B1544 | P3: route R's checks at every reading |
| LB2 | Lemma F and its torus facts | sm:B1544 §3 | P3: the ingredients in both routes at every reading |
| LB3 | K0 on N₄₅: its strata, closed supports, and no class below I(W) = 0 | sm:B1544 (banked) | K1, K3: the three-cusp strata and their count re-read |
| LB4 | Proposition L | §3.2 (proved here) | K1: L0–L3 exact in both routes at two primes; P2: every reading's rank and support |
| LB5 | Lemma G‴ and the squares' draw | §3.2, §3 | K7; P1: three draws per route, two routes, two primes |
| LB6 | Lemma M | §3.2 (proved here) | K1 (its input); P4 at every interior reading |
| LB7 | the code paths are the banked ones | sm:B1541, sm:B1544 | K3, K6: banked counts reproduced in both routes |

A reading that a check here does not cover is not used by the verdict.

Disclosed:
- **What was read before the seal.**
  - Structure only, in scratch scripts and then in the library and the controls:
    - the cup map δ¹_W (its ranks, blocks, pencils, images and the Gröbner bases of L2) and supports;
    - the dimensions, and the eigen-lines' ranks;
    - the line's interior classes, the cusps and τ.
  - No count at a class of cup rank one or two. No s = rk δ¹_{W*} at any such class, and no Λ² rank.
  - Counts only at banked classes (K3, K6), in the controls' trial and their sealed run.
- **How the design grew.** The first exploration found the ten eigen-lines by strata and suggested reading them and some
  pairs. Before any count, the structure work found Proposition L: the lines are ten points of a 7-dimensional family.
  So the population is the families' generic classes, with the lines kept as named classes. This is a change made by
  structure, before any reading.
- **The machine.** sm:B1538's Part F′ runs on three workers beside this design (its regeneration, `run_notes.md` there). This
  arc's run takes the fourth.

## 7. Predictions (priors fixed at the seal)

| | prediction | prior |
|---|---|---|
| P1 | one count per subspace (three draws in each route, two routes). The ten X:S read one count within each τ-orbit. Galois-conjugate eigen-lines read one count: u₁…u₄, w₁…w₄, and v_a with v_b. No eigen-line reads an I(W) below its family's generic one (u_j below Z1, w_j and v below Z2; Lemma G‴) | 90% |
| P2 | every reading's class has the sealed cup rank and support | 95% |
| P3 | route R's identities at every reading; Lemma F's ingredients in both routes at every reading | 95% |
| P4 | Lemma M: I(W) ≤ −1 at every reading of an interior class | 93% |
| P5 | the floor I(W) ≥ −1 at every reading (μ = 0 on Kc0's readings) | 40% |
| P6 | some subspace reads a generation-shaped count, I(W) = I(Λ²W) ≠ 0, in both routes | 10% |
| P7 | some subspace reads (−3, −3) in both routes | 5% |
| P8 | all ten X:S read one count: a lifted mirror of N₄₅ carries one τ-orbit of three-cusp sets to the other (sm:B1544's relay, §5) and preserves the count | 85% |

**Why the Galois part of P1.**
- ρ is the holonomy's V₂ ⊗ V̄₂, defined over ℚ(√−3), and the cover and τ are defined over ℚ. ℚ(√−3) ∩ ℚ(ζ₅) = ℚ, so
  (ℤ/5)^× acts on the eigen-decomposition. It sends V_j to V_gj and E_m to E_gm, preserves every rank, and permutes the lines:
  u_j to u_gj, w_j to w_gj, and v_a to v_b for g = ±2.
- The counts are ranks, so conjugate lines read one count at any prime where the reduction is good.

**Why the low prior on the floor (P5).**
- At u_j the absolute products c ∪ x̄_m vanish at three of the four m. Each relative product lies in a one-dimensional
  boundary part, and nothing known forces it to vanish.
- The floor has held at every banked reading, but none of those was a class of cup rank one or two.

A population-wide prediction is True only on complete records (every sealed task with both readings). A refuting row decides
False whatever the coverage.

## 8. BANKED IDENTITY: checked before reading

`identity.py` re-runs K1–K7 and checks every sealed file's sha-256 (`ARTIFACT_HASHES.txt`) before `run.py` reads anything.
A single difference stops the run.

## 9. Reading rules

- **PROVED (three on N₄₅ at the trivial character)** if P1–P4 hold and P7 holds: a subspace reads (−3, −3) in two routes.
  - It is a count at a class, not a selection. Which class and which cover the genesis selects is GENESIS GAP4 and
    THE_BAR's question.
  - **The audit before the bank.** Route F re-reads that subspace's class at its next two primes. A disagreement withholds
    the verdict and goes to ERROR_LEDGER first.
- **NEGATIVE** if P1–P4 hold on complete records, P7 is False, and every generic family (Z1, Z2 and the ten X:S) reads
  I(W) ≥ −2.
  - Then, by Lemma G‴, Corollary L′, §3.1 and sm:B1544, no class of N₄₅ reads I(W) = −3 at the trivial character.
  - So **the golden cover carries no three in this frame at the trivial character**.
- **OPEN** otherwise. In particular a family whose generic class reads I(W) ≤ −3 without three leaves OPEN the classes of that
  family where I(W) = −3 and Λ² may differ.
- Either way the read-out records:
  - every subspace's count;
  - the least I(W) over the families;
  - the Massey rank μ = −1 − I(W) at every interior subspace;
  - every generation-shaped subspace, named.
- 0 of 19 stays 0 either way.
- **NO NEGATIVE FROM A BUG.** The run is its own audit: every count is read in two routes that share no code, at two primes,
  three draws each. Proposition L is checked exactly in both routes. Lemma M is checked at every interior reading (P4).

## 10. What this arc does not decide

- **Other characters ν of N₄₅**, and other covers. sm:B1545 states Lemma F at members. At a member the room for three needs
  cusps where ν is trivial.
- **The Λ² count at special classes** of a family whose generic class reads I(W) = −3 (the OPEN case of §9).
- **What μ is, as an invariant.** Lemma M names it: the rank of a Massey-type boundary term. Its geometry, in terms of the
  cusps and the squares, is not derived here.
- **Which class and which cover the genesis selects** (GENESIS GAP4, THE_BAR).
