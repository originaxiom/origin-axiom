# B1547 — PREREGISTRATION: THE ROOM-THREE MEMBERS — on the golden cover N₄₅, the characters of order 8 trivial on every cusp whose fourth power has room three: where three can live there, mapped by structure, and read

**Sealed before `run.py` read any count at a member.** At the seal this arc has:
- **proved, at design time** (§3):
  - the room on N₄₅. Of the fifteen order-2 characters that are fourth powers of cusp-trivial characters, five have room
    three (n = 3, one τ-orbit) and ten have room one. So by Theorem C a member whose fourth power has order 2 can carry three
    only over one of the five;
  - Corollary 1: at a member trivial on every cusp, a class reading I(W₁) = −3 lies in the cup map's kernel K0^ν and vanishes
    on at least three of the five cusps (Theorem C (ii) with sm:B1545's Lemma F′). So it lies in a stratum X_U with |U| ≤ 2,
    and its support is U;
  - Lemma G: among the classes of support U, a generic class of X_U has the least I(W₁) and the least I(Λ²W₁);
  - Lemma Γ (Galois-conjugate members read alike), the deck symmetry τ, and the other order.
- **computed structure only** (§6), in two routes: the characters, the members and their keys, the cohomology dimensions,
  K0^ν, the strata X_U and the supports of their generic classes.
- **read counts only where the record has them banked**: the trivial character's generic interior class (control K5).

**Source.**
- The owner, 2026-10-04: "thanks, keep focused. three generations is smth we are after seripuslu"; "make sure nothing is lost.
  make sure we dont abandon the golden pointer".
- The owner, 2026-10-06: "we should verify all load bearing math even if a published paper, because we cant bet our whole
  project against some possible errors bugs or mistakes"; "breakthrough breaktheough breakthrough!!! is expected from you".
- sm:B1546 (banked NEGATIVE, 2026-10-06): N₄₅ carries no three at the trivial character, at any class. Its §10 leaves the
  other characters of N₄₅.
- sm:B1545 §5: at a member, three needs at least 3 − b0 cusps where ν is trivial. The members of this arc pass Theorem C's
  room and sm:B1545's cusp condition with nothing to spare: b0 = 0, room exactly three, and all five cusps trivial.

## 0. Seen first, and PRIOR ART:

**The repo sweep.** `git fetch --all` ran first (2026-10-06, 22:43Z). `scripts/checks/prior_work.py` then ran over every head
with twelve terms: "golden member", "cusp-trivial", "trivial on every cusp", "order-8 character", "room 3", "room-3",
"fourth root", "jump loci", "resonance variet", "characteristic variet", "common loops", "Galois class".

| head | commit |
|---|---|
| this branch | `95e687c0` |
| main | `385c6891` |
| the audit lane (fork) | `8b89d8fb` |
| the audit lane (physical bridge) | `c161981d` |
| the new web seat's branch (…/web-seat) | `d40c1ab6` |
| seat/outside-bench | `13d2c5b6` |
| seat/paper-review-verification | `5d58b935` |
| seat/kind-hypatia | `6a537f89` |
| seat/project-thread | `3a802c0d` |
| sep16-branch | `3205984b` |

What the sweep found:
- "resonance variet" and "characteristic variet" are absent on every head. "common loops" appears only in this arc's own
  uncommitted files.
- **"golden member" names two other objects on the heads**, so this arc's members are called the room-three members:
  - the metallic family's m = 1 member, the figure-eight (B447, B662, papers/metallic_one_object);
  - in this seat's sm:B1543 and sm:B1545, a character of order 5 of N₄₅'s base along which N₄₅ is the golden lift.
- **"jump loci"** hits this seat's OPEN_LEADS and CHANGELOG entries of 2026-10-04: the cyclic covers of the room covers, a
  different population.
- **"order-8 character"** hits sm:B1301, B1303, B1511, B1512, B1515 and B1522: order-8 characters of the tower's states
  (M₆, Y₆). None is a character of N₄₅.
- **"cusp-trivial", "trivial on every cusp", "room 3", "room-3" and "fourth root" bear through this seat's sm:B1535–B1545**:
  Theorem C and its room, the puncture characters and their fourth roots (sm:B1538), Lemma F′ at members (sm:B1545). None
  reads a character of N₄₅ other than the trivial one.
- "Galois class" hits other objects (sm:B1512's census, B1068, B469, B666).

**The literature.**
- A. Dimca, S. Papadima and A. I. Suciu, "Topology and geometry of cohomology jump loci", Duke Math. J. 148 (2009),
  arXiv:0902.1250, abstract, read 2026-10-06. It introduces relative characteristic and resonance varieties for twisted
  group cohomology with coefficients of arbitrary rank. For 1-formal groups the tangent cone at the trivial character of
  the characteristic variety is the resonance variety, which is defined by cup products. The members here are torsion points
  of such a relative jump locus: H¹(N; ν ⊗ ρ) as ν varies over the cusp-trivial characters. K0^ν is a cup-product kernel.
  This arc computes neither variety, only finitely many of their points; N₄₅'s group is not claimed 1-formal.
- P. Menal-Ferrer and J. Porti, "Twisted cohomology for hyperbolic three manifolds", Osaka J. Math. 49 (2012),
  arXiv:1001.2242, abstract, read 2026-10-06 (and §3 for sm:B1544): vanishing theorems for the cohomology twisted by
  symmetric powers of the holonomy. This frame's ρ = V₂ ⊗ V̄₂ is not among them, and the characters ν are not treated.
- T. Nosaka, "Twisted cohomology pairings of knots III; triple cup products", arXiv:1808.08532 (2018), abstract, read
  2026-10-06 for sm:B1546: the trilinear form (c, z, x) ↦ ∫ c ∪ z ∪ x behind the rank s here.

**Standing: NEW-AS-SWEPT** for the strata of these members and their counts (computed on one cover, in two routes at two
primes). EXTENDS sm:B1545 (its Lemma F′ fixes where three can live at these members) and sm:B1546 (the next characters of
N₄₅ after the trivial one).

## 1. The question

On N₄₅, at a character ν of order 8 that is trivial on every cusp and whose fourth power is one of the five room-three
characters, does any class of sm:B1515's frame read three, (−3, −3), in either order? The arc maps every class where three
can live (Corollary 1) into the strata X_U and reads each stratum at its generic class. If no stratum reads three, no class
at any such member does.

## 2. Definitions and conventions

- **N₄₅** (sm:B1541): five cusps with labels 0, 1, 2, 4, 5; the deck group τ of order 5 cycles them.
  - H₁(N₄₅; ℤ) = ℤ⁹ ⊕ (ℤ/2)². Modulo the cusps' images it is ℤ⁴ ⊕ (ℤ/2)². A character trivial on every cusp (cusp-trivial)
    factors through that quotient.
  - Each route computes the quotient's characters as integer vectors on its own generators: the free lattice F (four rows,
    the integer kernel of the relators and the peripheral words, saturation checked) and two order-2 torsion vectors T.
- **The frame at a member** (sm:B1515, sm:B1536). ν is a character of finite order and ρ the four. V = ν ⊗ ρ and
  L = ν⁻⁴. A class c ≠ 0 of H¹(N; ν⁵ ⊗ ρ) = H¹(N; Hom(L, V)) gives W₁ = [[V, c·L], [0, L]]. The count is
  (I(W₁), I(Λ²W₁)), with I(E) = n(E) − n(E*). Also:
  - r = rk δ¹_W(c), the cup map H¹(N; L) → H²(N; V);
  - s = rk δ¹_{W*}(c), and t the rank of the connecting map of (Λ²W₁)* (route R's rk d1(L2*));
  - k = the size of the support (the cusps where c restricts non-trivially), and b0 = [ν⁴ = 1].
  - Route R's identities, checked at every route R reading: I(W₁) = −b0 + k + r − s; I(Λ²W₁) = k − t; s ≤ k + n(L).
- **The room-three characters.** The order-2 characters (−1)^f, f a non-zero 0/1 combination of F's rows. They are the
  order-2 characters that are fourth powers of cusp-trivial characters (a fourth power kills the 2-torsion). Their n are
  ten 1s and five 3s; the five are the room-three characters.
- **The members over χ.** The cusp-trivial ν with ν⁴ = χ: ν = ζ₈^e with e = f + 2 Σ a_i F_i + 4 Σ b_j T_j mod 8,
  a ∈ (ℤ/4)⁴, b ∈ (ℤ/2)². There are 1024, all of order 8, all with b0 = 0 and L = χ.
- **Keys.** The 46 common loops are based loops at sheet 0 that generate π₁(N₄₅): one per edge off a breadth-first tree of
  the permutations of a and t, computed from the permutations alone. A character's key is its values mod 8 on them. Both
  routes evaluate their own characters on the same words, so a key names one character in both routes.
  - χ0 is the room-three character with the least key (mod 2).
  - The members over χ0 are taken in the order of their keys. The i-th member is the same character in both routes.
  - The Galois class of a member is {ν, ν³, ν⁵, ν⁷}; its representative is the least of the four keys.
- **The strata.** K0^ν = {c : r(c) = 0}. For a set U of at most two cusps, X_U = {c ∈ K0^ν : c restricts to a coboundary at
  every cusp outside U}. So X_{} is K0^ν's interior part, and X_U ⊆ X_U′ when U ⊆ U′. **A stratum is distinct** if
  dim X_U > 0 and dim X_U > dim X_U′ for every U′ strictly inside U.
- **The routes** are sm:B1544's floor_lib, loaded by path and unchanged:
  - route F (route_f.py on the lifted 2-complex, p_F = 67108201);
  - route R (route_r.py on N₄₅'s own presentation, p_R = 2147482801).
  - Each finds its own characters, members, classes and strata. They share the cover's permutations and the common loops.

## 3. What is proved at design time

**3.1 The room on N₄₅, and the members.** Theorem C (iii) (sm:B1535): three in either order needs b0 + n(ν⁴) ≥ 3 and
n(ν³ ⊗ ρ) ≥ 3. At a member whose fourth power has order 2, ν⁴ ≠ 1 and b0 = 0, so n(ν⁴) = 3: ν⁴ is one of the five
room-three characters (K1). The members over the five that are trivial on every cusp are 5 × 1024 characters of order 8.

**3.2 Corollary 1 (where three can live at a member trivial on every cusp).** Let ν be such a member and c ≠ 0 a class with
I(W₁) = −3. Then r(c) = 0, s(c) = k + 3 and k ≤ 2. So c lies in X_U for U its support, |U| ≤ 2, and X_U is distinct.

*Proof.*
- Route R's identity with b0 = 0 gives I(W₁) = k + r − s.
- Theorem C (ii)'s proof (sm:B1535) bounds s. The boundary composite of δ¹_{W*} has rank at most k, and the rest of its image
  lies in K_L, of dimension n(L*) = n(L) = 3. So s ≤ k + 3 and I(W₁) ≥ r − 3. Equality needs r = 0 and s = k + 3.
- sm:B1545's Lemma F′, with all five cusps trivial for ν and b0 = 0, gives I(W₁) ≥ k − 5. So k ≤ 2.
- If X_U = X_U′ for some U′ strictly inside U, then c ∈ X_U′, and its support lies in U′, which is not U. □

In Theorem C (ii)'s terms, at r = 0, I(W₁) = a − e. So three needs a = 0 (no part of c's boundary restriction lies in Λ(V))
and e = 3: the whole interior part K_L is hit. **At the trivial character a ≥ 1 off the interior** (sm:B1546 §3.1), because
there c lies in H¹(N; V) itself. At these members c lies in H¹(N; V ⊗ χ), and that argument does not apply. So classes
supported on one or two cusps are read here as well as the interior ones.

**3.3 Lemma G (generic classes decide each stratum).** Let X_U be a distinct stratum and O_U its classes of support exactly U.
- O_U is open in X_U, and not empty: a vector space over an infinite field is not the union of finitely many proper
  subspaces (the X_U′, U′ strictly inside U).
- On O_U, k = |U| and r = 0. The ranks s and t are ranks of matrices whose entries are polynomial in c. Each attains its
  maximum (s_U, t_U) on a non-empty open subset, and X_U is irreducible, so both are attained together on a non-empty open
  subset.
- So, by route R's identities:
  - (a) the least I(W₁) on O_U is |U| − s_U, read at a generic class;
  - (b) if s_U = t_U = |U| + 3, a generic class reads (−3, −3);
  - (c) if s_U < |U| + 3 or t_U < |U| + 3, no class of O_U reads (−3, −3);
  - (d) if s_U = |U| + 3 < t_U, a generic class reads (−3, |U| − t_U), below −3 in Λ², and the generic class does not
    decide whether a special class of O_U reads (−3, −3).
- **The draws.** A random combination of a basis of X_U over F_p lies in a proper closed subset of degree δ with probability
  at most δ/p (Schwartz–Zippel). Each distinct stratum is drawn three times in each route, at two primes. A stratum's generic
  reading is the least I(W₁) and the least I(Λ²W₁) over its draws (the largest ranks). P5 records whether the draws agree.

**3.4 Lemma Γ, the deck symmetry, and the other order.**
- **Lemma Γ (Galois).**
  - The holonomy's matrices for a, b and t have entries in ℚ(ζ₆), and |det| = 1/7 (K4).
  - So the four, ρ(g)H = gHg*/|det g| written in route F's basis of Hermitian matrices, has its entries in ℚ(√3):
    they are real and imaginary parts of elements of ℚ(ζ₁₂).
  - For k odd mod 8, take j in (ℤ/24)^× with j ≡ k mod 8 and j ≡ ±1 mod 12: j = 1, 11, 13, 23 for k = 1, 3, 5, 7 (K4). The
    automorphism σ_j of ℚ(ζ₂₄) fixes √3 and sends ζ₈ to ζ₈^k.
  - Applied to every matrix of the frame at (ν, c), σ_j gives the frame at (ν^k, σ_j c). Every dimension, connecting rank,
    K0, X_U and support corresponds. So Galois-conjugate members read alike in characteristic 0.
  - The run reads all 1024 members in both routes, so the verdict does not rest on Γ. P3 tests it.
- **The deck symmetry.** τ is induced by an element of π₁ of N₄₅'s base that normalises π₁(N₄₅), and ρ extends to the base.
  So pulling back by τ carries the frame at (ν, c) to the frame at (τ*ν, τ*c), with the same counts, the cusps cycled and
  the members over χ0 sent to members over τ*χ0. The five room-three characters are one τ-orbit (K3). So the members over
  the other four are read through χ0's. K3 checks the structure and strata of τ*ν at eight sample members.
- **The other order.** W₂* = W₁(ν̄, c′) (sm:B1535 (iii)). A count (3, 3) of W₂ at ν is a count (−3, −3) of W₁ at ν̄ = ν⁷,
  a member over χ̄0 = χ0. So reading W₁ at every member over χ0 reads both orders.

**3.5 What a NEGATIVE covers.** With 3.1–3.4, if no distinct stratum's generic reading has I(W₁) = −3 with I(Λ²W₁) ≤ −3,
then no class at any member trivial on every cusp over any of the five room-three characters carries three, in either
order. The classes the run does not read are excluded by Theorem C's cap (r ≥ 1 gives I(W₁) ≥ −2) and by Lemma F′ (k ≥ 3
gives I(W₁) ≥ −2). P9 checks both at a generic class of K0^ν and a generic class of H¹ at every member, in route R.

## 4. The instruments (`verification/`, written and checked before the seal)

- `member_lib.py`, in both routes. It loads sm:B1544's floor_lib by path, unchanged.
  - The characters (`RChars`, `FChars`): the lattice, the torsion, ν's values, τ on the lattice, the values on loops, n.
  - The common loops, the room-three characters, the population, the Galois classes.
  - The members (`RMember`, `FMember`): the modules, K0^ν, the interior, `vanishing`, `stratum`, `strata`, `support`, and
    `reading`. Route R's reading is sm:B1536's route_r reading body with every identity. Route F's is route_f's count body.
  - Route F's `class_basis` picks the pivot columns of one reduction. They are the columns the one-at-a-time rank test picks
    (K8).
- `run.py`: the tasks of §5, resumable, one row per task (`run.jsonl`).
- `read_out.py`: the predictions of §7 from the rows, once. `evaluate` is pure.
- `controls.py`: K1–K8 (§6). `identity.py`: the banked identity (§8).

## 5. The population (outcome-blind; seeds crc32 of "B1547|route|key|U|draw")

- **Tasks:** route R and route F at each of the 1024 members over χ0: 2048 tasks, one row each.
- **At each member:** the structure (h¹(ν⁵ ⊗ ρ), n(ν⁵ ⊗ ρ), h¹(L), n(L), dim K0^ν, dim of its interior part); the
  dimensions of the sixteen X_U; the distinct strata; at each distinct stratum three readings of generic classes.
- **In route R also, the load-bearing checks (P9):** one reading at a generic class of K0^ν (when it is not zero) and one at
  a generic class of H¹(N; ν⁵ ⊗ ρ). Seeds "B1547|R|key|K0|0" and "B1547|R|key|H1|0".
- **The structure census before the seal** (route R, every member; §6): 1024 members, every Galois class alike; h¹(L) = 8 and n(L) = 3
  at every member; K0^ν ≠ 0 at 896; a distinct stratum at 220, of which 68 have one off the interior. In all 424 distinct
  strata: 164 interior, 132 on one cusp, 128 on two. Every generic class has support exactly U. So the run reads 1,272
  stratum readings in each route, and 1,920 check readings in route R (896 at K0^ν, 1,024 at H¹).

  | h¹(ν⁵ ⊗ ρ) | n(ν⁵ ⊗ ρ) | dim K0^ν | its interior part | distinct strata at each | members |
  |---|---|---|---|---|---|
  | 5 | 0 | 5 | 0 | 0 | 472 |
  | 5 | 0 | 5 | 0 | 1 (one cusp) | 24 |
  | 5 | 0 | 5 | 0 | 7 (three on one cusp, four on two) | 32 |
  | 6 | 1 | 0 | 0 | 0 | 32 |
  | 7 | 2 | 1 | 0 | 0 | 192 |
  | 8 | 3 | 0 | 0 | 0 | 96 |
  | 8 | 3 | 3 | 1 | 1 (interior) | 36 |
  | 8 | 3 | 3 | 1 | 2 (interior, one cusp) | 12 |
  | 8 | 3 | 4 | 3 | 1 (interior) | 12 |
  | 9 | 4 | 2 | 0 | 0 | 12 |
  | 9 | 4 | 5 | 4 | 1 (interior) | 96 |
  | 13 | 8 | 2 | 2 | 1 (interior) | 4 |
  | 15 | 10 | 2 | 2 | 1 (interior) | 4 |

## 6. Controls and disclosures (before the seal)

All hold (`verification/controls.json`). This design's controls ran first as a trial (22:43–22:54Z on 2026-10-06), then for
the record (23:08:53–23:19:58Z). Between the two the read-out gained P9 and P10 and the arc's directory was renamed; nothing else
changed.
- **K1.** The population in each route on its own (`run.setup`): the 46 common loops, the same words in both routes; the n of
  the fifteen order-2 characters (ten 1s, five 3s); the five room-three keys; χ0; the 1024 members' keys in order (equal
  sha-256 in both routes); 256 Galois classes of size 4.
- **K2.** Every member in both routes is trivial on every cusp (its values on each cusp's two peripheral loops are 0 mod 8)
  and has ν⁴ = χ0 (its key mod 2 is χ0's), so it has order 8.
- **K3.** τ has order 5 on the free lattice in both routes, and the five room-three characters are one τ-orbit. At the eight
  sample members (route R), τ*ν is a cusp-trivial character over a room-three character other than χ0, with ν's structure and
  stratum dimensions.
- **K4.** Lemma Γ's input: only ζ₂₄⁰ and ζ₂₄⁴ appear in the holonomy, |det| = 1/7 for a, b and t, and the j of §3.4.
- **K5.** The trivial character in both routes: the structure (23, 18, 9, 4, 5, 0) and a generic interior class's count
  (4, −10), sm:B1541's banked count.
- **K6.** At the eight sample members 0, 3, 4, 7, 148, 183, 208 and 243 (the first four in key order with a distinct stratum off the interior, and the
  first four whose only distinct stratum is the interior), both routes agree on the structure, every X_U's dimension and the
  distinct strata. X_{} has the dimension of K0's interior part, and each distinct stratum's generic class has support U.
- **K7.** The read-out on synthetic rows, twenty-one cases. They cover each prediction's refutation, incomplete and
  duplicated records, a stratum off the interior, a check below Lemma F′, and the three verdicts, including OPEN when a
  stratum reads I(W₁) = −3 with Λ² below −3.
- **K8.** Route F's `class_basis` picks the same columns as the one-at-a-time rank test on four inputs.

### 6a. The load-bearing inputs (WORKING_RULES 2026-10-06), each re-derived by own code on every instance used

| | input | source | own check |
|---|---|---|---|
| LB1 | Theorem C (ii): route R's identities and the cap s ≤ k + n(L) | sm:B1535, sm:B1536 | P4: route R's checks at every reading; P9 at a generic class of K0^ν and of H¹ at every member |
| LB2 | Lemma F′ at members (I(W₁) ≥ k − 5 here) | sm:B1545 §1 (banked; its ingredients checked at 288 member readings there) | P4 at every reading; P9 at classes of any support at every member |
| LB3 | Lemma G and the draws | §3.3 (proved here) | three draws in each route, two routes, two primes; P5 |
| LB4 | the members are the population of §3.1 | §3.1 | K1, K2 in both routes; P2 at every member |
| LB5 | the strata machinery | §2 | K6; P4 (nesting, X_{} as K0's interior part, the distinct strata as their dimensions say); P2 |
| LB6 | the deck symmetry reduces the five room-three characters to χ0 | §3.4 | K3 |
| LB7 | Lemma Γ | §3.4 | K4; P3 at every Galois class in both routes (the verdict does not rest on it) |
| LB8 | the code paths are the banked ones | sm:B1541, sm:B1544, sm:B1546 | K5: the banked count reproduced in both routes |

A reading that a check here does not cover is not used by the verdict.

Disclosed:
- **What was read before the seal.**
  - Structure only, in scratch scripts and then in the library and the controls:
    - N₄₅'s homology and its cusp-trivial characters; the n of the fifteen order-2 characters; τ's orbits on them;
    - at the members: h¹ and n of ν⁵ ⊗ ρ and of L, K0^ν and its interior part (route R at all 1024 members; route F at four);
    - the strata X_U and the supports of their generic classes (route R at all 1024 members; route F at the twelve members of
      the tests and K6);
    - timings, at the trivial character.
  - No count at a member: no I(W₁), I(Λ²W₁), s, t or Λ² rank at any member's class.
  - Counts only at the trivial character, banked (4, −10): in the library's tests, a timing script and K5.
- **How the design changed before the seal.**
  - The first plan read only K0^ν's interior part, carrying over sm:B1546's "a ≥ 1 off the interior". Deriving Corollary 1 at
    members showed that argument holds only at the trivial character. The structure census then found strata off the
    interior at 68 members. So the population is every distinct stratum with |U| ≤ 2. This change came from the
    derivation and the structure, before any count.
  - The members were first indexed by each route's own lattice coordinates, which differ between routes. The common loops
    and keys now name each member alike in both routes, so the routes are compared member by member, not as multisets.
  - A bug found and fixed in scratch: an early GF(2) rank counted columns where it should have counted rows, which gave six
    torsion vectors instead of two. The census it fed was stopped, and the library's rank was fixed and checked. Every census
    quoted here ran after the fix.
- **The machine.** sm:B1538's Part F′ regeneration runs beside this design on three workers (`run_notes.md` there).

## 7. Predictions (priors fixed at the seal)

| | prediction | prior |
|---|---|---|
| P1 | the banked identity holds: controls K1–K8 reproduce and every sealed file hashes as sealed | 97% |
| P2 | the routes agree at every member: structure, every X_U's dimension, the distinct strata, every generic reading | 90% |
| P3 | in each route the four members of every Galois class read alike (Lemma Γ) | 90% |
| P4 | the theorems at every reading: rk δ¹_W = 0, support in U, Lemma F′, the caps; in route R every identity, b0 = 0, n(L) = 3, k = ∣support∣; at every member n(L) = 3, the strata nested, X_{} as K0's interior part | 95% |
| P5 | genericity: at every distinct stratum the three draws read alike, each with support exactly U | 92% |
| P6 | the floor: every distinct stratum's generic reading has I(W₁) ≥ −2 | 80% |
| P7 | I(W₁) ≥ 0 at every reading | 30% |
| P8 | three: some stratum's generic reading is (−3, −3) in both routes | 7% |
| P9 | the load-bearing checks hold at every member (route R) | 96% |
| P10 | some stratum's generic reading is generation-shaped, I(W₁) = I(Λ²W₁) < 0, in both routes | 25% |

**Why these priors.**
- **P6 and P8.** Three needs e = 3: c must pair the whole three-dimensional interior part of H¹(N, ∂N; L) with H¹(N; V*)
  modulo its interior part. At the trivial character the analogous Massey term vanished on every interior subspace read
  (sm:B1546's μ = 0). Here c and the classes it pairs live in different modules (ν⁵ ⊗ ρ against ν⁻¹ ⊗ ρ), so the symmetry
  that might force it to vanish there is absent. Nothing seen forces e = 3 either. Three also needs t = |U| + 3 exactly.
- **P7.** I(W₁) ≥ 0 everywhere would mean e ≤ a at every class. No reason is known.
- **P10.** sm:B1530 and main's B1485 read (−1, −1) at the silver squares' members. One generation here is plausible; three is
  not expected.

A population-wide prediction is True only on complete records (every task with its row, every distinct stratum with its
three readings, every route R row with its checks). A refuting row decides False whatever the coverage.

## 8. BANKED IDENTITY: checked before reading

`identity.py` re-runs K1–K8 and checks every sealed file's sha-256 (`ARTIFACT_HASHES.txt`) before `run.py` reads anything.
A single difference stops the run.

## 9. Reading rules

- **PROVED (three on N₄₅ at a room-three member)** if P1, P2, P4 and P9 hold and P8 holds: a stratum's generic class reads
  (−3, −3) in two routes.
  - It is a count at a class, not a selection. Which class and which cover the genesis selects is GENESIS GAP4 and
    THE_BAR's question.
  - **The audit before the bank.** Route F re-reads that stratum's generic class at its next two primes. A disagreement
    withholds the verdict and goes to ERROR_LEDGER first.
- **NEGATIVE** if P1, P2, P4 and P9 hold on complete records, and no distinct stratum's generic reading, in either route, has
  I(W₁) = −3 with I(Λ²W₁) ≤ −3.
  - Then, by §3.5, no class at any member trivial on every cusp over the five room-three characters carries three, in either
    order.
- **OPEN** otherwise. In particular a stratum whose generic class reads I(W₁) = −3 with I(Λ²W₁) < −3 (§3.3 (d)) leaves OPEN
  its special classes.
- Either way the read-out records:
  - the members by structure and by their distinct strata;
  - every stratum's generic count, by the size of U;
  - the least I(W₁), and every stratum at I(W₁) ≤ −2;
  - every generation-shaped stratum, named.
- 0 of 19 stays 0 unless P8 holds and the audit confirms it.
- **NO NEGATIVE FROM A BUG.** Every count is read in two routes that share no code beyond the permutations and the loops, at
  two primes, with three draws per stratum. Every member is named alike in both routes. The theorems the design relies on
  are checked at every reading, and the exclusions at classes of any support at every member.

## 10. What this arc does not decide

- **Members over the five that are not trivial on every cusp**: ν⁴ = χ with ν of order 4 on some cusp. They need at least
  three cusps where ν is trivial (sm:B1545).
- **Members with ν⁴ = 1** (orders 2 and 4): b0 = 1 and n(1) = 4, so Theorem C leaves room. Three needs k ≤ 3 there.
- **Members whose fourth power has order three or more.** Their room n(ν⁴) is not computed here.
- **The special classes** of a stratum in case §3.3 (d).
- **Other covers**, and which class and which cover the genesis selects (GENESIS GAP4, THE_BAR).
