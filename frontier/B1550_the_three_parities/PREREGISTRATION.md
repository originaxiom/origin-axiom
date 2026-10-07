# B1550 — PREREGISTRATION: THE THREE PARITIES — on the tetrahedral cover that an odd trace forces (the A₄ cover whose four ends sit at the fibre's four 2-torsion points), every member at characters of order dividing four, its golden orbit and its count: are the root's generation-shaped members exactly its parity-labelled sign members, three labels cycled by the golden map?

**Sealed before `run.py` read any count at a member outside the controls.**

At the seal this arc has:
- **proved at design time** (§3):
  - the parity lemma: an odd trace makes the monodromy a 3-cycle on the three non-zero parities, and GENESIS's SE1 gives
    the root an odd trace;
  - the tetrahedral cover, its four ends and its A₄;
  - the golden-triplet law (§3.3);
  - at most one generation per member;
  - the orbit law.
- **computed structure only** (§5): the census of all 336 A₄ orbits of characters of order dividing 4 on the four
  tetrahedral covers, at 50 digits, in two routes; K1 repeats the member orbits with a second rank method.
- **read counts only where disclosed** (§6): the two sign-orbit representatives on the root's cover, read in the
  exploration that found the cover, and one count the record banks (main's B1492 on L8a15).

**Source.**
- The owner, 2026-10-07: "derive three generations from oa principle".
- The owner, the same day: "maybe three generations font emerge in at once ir in one place, but as a process in more
  steps", and "make sure you dont lean on m004 alone but in all alloed objects or family of objects. this is our number1
  error we keep doing."
- Main's B1496 (S76, GENESIS v1.22), the specification from the verified physics:
  - every known construction obtains three by selection: a free quotient divides a cover's count by ∣G∣, and the
    characters of G select;
  - "nobody derives three", and a derivation would be new.
- Main's B1495 (S75): the direct sum of L8a15's three members reads (3, 9), not (3, 3).

## 0. Seen first, and PRIOR ART:

**The repo sweep.**
- `git fetch --all` ran first (2026-10-07, 11:20Z).
- `scripts/checks/prior_work.py` then ran over every head with eight terms: "tetrahedral cover", "three parities",
  "Pisano", "2-torsion", "A4 cover", "parity label", "mod 2", "non-zero parit". A further `git grep` on main searched for
  "t^2 + t + 1", "Phi_3", "cyclotomic … mod 2" and "Alexander polynomial … mod 2".

| head | commit |
|---|---|
| this branch | `ce122640` |
| main | `b7706bb6` |
| the audit lane (fork) | `8b89d8fb` |
| the audit lane (physical bridge) | `c161981d` |
| the new web seat's branch (…/web-seat) | `d40c1ab6` |
| seat/kind-hypatia | `6a537f89` |
| seat/outside-bench | `13d2c5b6` |
| seat/paper-review-verification | `5d58b935` |
| seat/project-thread | `8b6df98f` |
| sep16-branch | `3205984b` |

What the sweep found, read:
- **"three parities", "A4 cover" and "non-zero parit"** are on no head.
- **B326** (main, 2026-07-01, "the generation ℤ/3-breaking is finite congruence torsion"):
  - H₁ of m004's 3-fold cyclic cover is ℤ ⊕ (ℤ/4)²;
  - the deck ℤ/3 acts on the torsion with characteristic polynomial Φ₃ = x² + x + 1, irreducible mod 4 and mod 2;
  - "the three generations are bound into one irreducible ω-module".
  - There the deck ℤ/3 was called the generation ℤ/3 by assumption. The reduction Δ ≡ Φ₃ (mod 4), the "Eisenstein end",
    is recorded there as an observation.
  - **So the parity lemma's arithmetic is on the record for the root.** This arc adds that GENESIS's SE1 forces it for
    any root (§3.1), the cover it builds (§3.2), and the frame's members and counts there.
- **B1067's hook** (main, dormant): "Δ = Φ₃ mod 2" as the Eisenstein ramification of t² − 3t + 1. The same fact, mod 2.
- **B298** (main, 2026-06-30, "the figure-eight does not force three generations"):
  - its invariant trace field ℚ(√−3) has Galois group ℤ/2, so its Galois multiplicities are 1 or 2;
  - "3-fold covers of m004: multiplicity 1".
  - The three here is not a Galois multiplicity over ℚ. It is the size of the monodromy's orbit on F₂[t]/Φ₃ = F₄ minus
    zero: ∣F₄^×∣ = 3, a quadratic structure over F₂ with three units. B298's argument does not reach it. Its
    "multiplicity 1" counts the 3-fold covers, and m004 has one.
- **B1255** (main, the pattern behind twelve lost three-nesses): "a genuine three needs … the three permuted
  transitively, with none distinguished".
  - The golden map permutes the three non-zero parities transitively, and no parity is distinguished: as an F₂[t]-module,
    F₂² ≅ F₄ with no canonical 1.
  - B1255's warning stands: in the basis of characters of ℤ/3 (1, ω, ω²) a triplet is 1 + 2 over ℚ.
- **B486** (the figure-eight's cusp is rectangular) and **main's B1496** ("no global order-3 isometry"): both about m004
  itself.
  - The golden map is not an isometry of m004. It is the deck group of the third level over m004, and on the
    tetrahedral cover it is an isometry of order 3 acting freely.
  - So this arc's mechanism is B1496's smooth one (a free quotient, characters selecting), not the orbifold one.
- **This seat's B1356** (A₄ = 2T/±1 around a free ℤ/3 triple on Y₃), **the three-orbit note** and **sm:B1549** (A₄
  triplets as ℤ/2 × A₄ on three-ended covers): A₄ triplets on other objects and other covers.
- **"Pisano"** hits main's level-tower identity P59 (ord(W₁) = π(N)/2 at N = 15, …, 225), the WRT clock (B775) and P3's
  π(3) = 8. None is the period mod 2 or a parity. **"2-torsion"** and **"parity label"** hit unrelated objects.
- **"tetrahedral cover"** hits a harvested reader (B1457, "arithmetic membership of the tetrahedral covers"), about
  other covers.

**The literature** (read 2026-10-07):
- G. Altarelli, F. Feruglio and Y. Lin, "Tri-bimaximal neutrino mixing from orbifolding", Nucl. Phys. B 775 (2007) 31,
  hep-ph/0610165, abstract.
  - A₄ connects the branes at the four fixed points of T²/ℤ₂, which are the four 2-torsion points of the torus.
  - **The nearest prior art.** Here the four points are the ends of a hyperbolic cover, and the ℤ/3 is the golden
    monodromy mod 2, forced by GENESIS's SE1, not a lattice rotation.
- T. Kobayashi, H. P. Nilles, F. Plöger, S. Raby and M. Ratz, "Stringy origin of non-Abelian discrete flavor
  symmetries", Nucl. Phys. B 768 (2007) 135, hep-ph/0611020, abstract.
  - The repetition of families is the multiplicity of equivalent fixed points.
  - Their permutations, with the space group's selection rules, give D₄ (from T²/ℤ₂) and Δ(54).
- C. Hattori, M. Matsunaga, T. Matsuoka and K. Nakanishi, "Flavor symmetry and Galois group of elliptic curves",
  arXiv:0903.2718, abstract.
  - Generation structure from the torsion points of an elliptic curve with complex multiplication, with the Galois group
    as the flavour symmetry.
  - The nearest prior art for "generations at torsion points of a torus".
- T. Asselmeyer-Maluga, "Braids, 3-manifolds, elementary particles: number theory and symmetry in particle physics",
  Symmetry 11 (2019) 1298, arXiv:1910.09966, abstract. Fermions as hyperbolic knot complements, three generations from
  3-fold branched covers. Another mechanism.
- The Pisano period: π(2) = 3 is the only odd Pisano period (standard).
- Main's B1496 report (23 primary sources on how three is obtained): selection everywhere, by free quotients and
  characters.

**Standing: EXTENDS** B326 and B1067, which have the Φ₃ arithmetic on the root, and AFL, which has A₄ on the four
2-torsion points. **NEW-AS-SWEPT:**
- the tetrahedral covers of the family;
- their members, golden orbits, parity labels and counts;
- the parity lemma's statement for every root that GENESIS's SE1 admits.

## 1. The question

On the tetrahedral cover N of each state of the selection (every generated state of odd trace whose word has length at
most 4: +LR = m004, the root; −LR = m003; +LLLR = m023; −LLLR):
- at every character ν of order dividing 4 whose module ν ⊗ ρ has an interior class (a member), what does that class
  count?
- Which members are generation-shaped, (I(W₁), I(Λ²W₁)) = (−g, −g) with g ≥ 1?
- How do they sit under A₄, and under the golden map?

**The claim under test (the derivation's computed step).** On the root's tetrahedral cover the generation-shaped members
are exactly its 24 sign members. Each has an edge's parity as its label, eight carry each non-zero parity, and the
golden map permutes the three labels as a 3-cycle.

## 2. Definitions and conventions

- **The states.** sm:B1527's presentation: F = ⟨a, b⟩, t g t⁻¹ = φ(g), the cusp ⟨l, t′⟩, l = abAB.
- **The parities.** H₁(F; F₂) = F₂², the two records mod 2. φ acts on them by its homology matrix mod 2.
- **The tetrahedral cover N.** For tr φ odd: the kernel of π₁M → F₂² ⋊ ℤ/3 = A₄, given by a ↦ e_a, b ↦ e_b and t ↦ the
  3-cycle. It is built as sm:B1538's fibre-direction cover of the third level M₃ (the word three times; sign as the
  state's) with lattice 2ℤ² and the one class w̄ that gives four cusps:
  - 0 for a + state;
  - (1, 1) for a − state, where M₃'s own stable letter is t₃ = t³c with φ₃ = φ³ ∘ Ad(c) (`tetra_lib.twist`).
- **The A₄ action on N's characters.**
  - V₄ is N's deck group over M₃ (sm:B1549's `deck_action`).
  - ℤ/3 is the golden map: conjugation by M's stable letter t (`tetra_lib.golden_action`).
- **The label** of a character. Its values on the four puncture loops l_x, x ∈ ℤ²/2ℤ², form its pattern.
  - When the pattern is non-zero at exactly two points x, y (an edge of the tetrahedron), the label is the parity
    x − y ≠ 0.
  - Opposite edges share a label. V₄ preserves labels, and the golden map moves them by φ mod 2.
- **The frame.** sm:B1515 at ν⁴ = 1: ρ is the four, L = 1 and b0 = 1.
  - A class c of H¹(N; ν ⊗ ρ) gives W₁ = [[ν ⊗ ρ, c], [0, 1]].
  - I(E) = n(E) − n(E*), n = h¹ − r¹, with r¹ the rank of the restriction to every cusp.
  - The count is (I(W₁), I(Λ²W₁)).
- **A member** is a character with n(ν ⊗ ρ) ≥ 1. Its classes are the interior ones.
- **Generation-shaped** means I(W₁) = I(Λ²W₁) < 0.
- **The cusp decomposition.** m_A is the number of ends where ν is trivial, m_B = 4 − m_A, k = 0 at interior classes,
  b0 = 1.
- **The two routes** (sm:B1549's library, banked; they share only the cover's action, the character's definition and the
  holonomy):
  - **route P** uses N's own presentation (sm:B1538's punct_present);
  - **route S** is Shapiro on M₃: a class z of H¹(M₃; Ind ν ⊗ ρ) gives c(h) = z(h)₀, then Ind W₁ and Ind Λ²W₁ on M₃,
    with N's cusps read through M₃'s one cusp (Mackey).
- **Precision.**
  - The holonomy is sm:B1527's at 60 digits, and everything else is at 50.
  - Ranks are by Gauss–Jordan elimination with column pivoting, with an entry zero below 10⁻³⁰ of the matrix's largest.
  - The gap is recorded at every rank.

## 3. What is proved at design time

**3.1 The parity lemma.** For φ ∈ ±SL(2, ℤ) the following are equivalent:
- tr φ is odd;
- det(φ − I) = 2 − tr φ is odd;
- φ mod 2 fixes no non-zero parity;
- φ mod 2 has order 3 in GL(2, F₂) ≅ S₃, and so permutes the three non-zero parities as a 3-cycle;
- the Alexander polynomial Δ(t) = t² − (tr φ)t + 1 reduces mod 2 to Φ₃ = t² + t + 1, so F₂² ≅ F₂[t]/Φ₃ = F₄ with t
  acting as a primitive cube root of unity.

*Proof.*
- φ − I is invertible mod 2 iff its determinant is odd, and that determinant is 2 − tr φ.
- In GL(2, F₂) ≅ S₃ (acting on the three non-zero vectors), the elements without fixed vectors are the two 3-cycles.
- The characteristic polynomial mod 2 is t² + (tr φ)t + 1, which is Φ₃ exactly when tr φ is odd. □

- **SE1 forces it.** GENESIS's SE1 is ∣2 − tr φ∣ = 1, so det(φ − I) = ±1 is odd. The genesis root m004 = +LR (tr 3)
  therefore permutes the three non-zero parities of its two records cyclically, with period 3: the Pisano period π(2).
- **This is no more than arithmetic.** Every state of odd trace shares it. The census (§5) asks which of them carry
  members.

**3.2 The tetrahedral cover.**
- For tr φ odd, π₁M → A₄ is onto, and its kernel is the 2ℤ² cover of M₃ with the four-cusp class. The kernel is ⟨K, t³⟩
  in M's own letters, and `tetra_lib.tetra_cover` finds the class.
- φ³ ≡ I mod 2, so every lift of the puncture is fixed, and N has four ends: the four 2-torsion points of the fibre torus.
- A₄ = F₂² ⋊ ℤ/3 acts on them as the affine group of F₂² acts on its four points, which is the rotation group of a
  tetrahedron acting on its vertices.
  - V₄'s translations fix no vertex.
  - Each element of order 3 fixes one vertex and cycles the other three.
- **Checked exactly (K3).** On every state of the selection, at orders 2 and 4, the deck group and the golden map
  generate a group of order 12 with A₄'s element orders.

**3.3 The golden-triplet law.**
- An A₄ orbit of characters is a union of V₄ orbits, and ℤ/3 = A₄/V₄ permutes those.
- The permutation is free, giving three V₄ blocks, unless the orbit's stabilizer contains an element of order 3. That
  happens only for orbits of size 1 or 4.
- On M₃ each V₄ block is one local system Ind_N^{M₃} ν, which carries the block's count (Shapiro). So **every member orbit
  of size 12, 6 or 3 gives three local systems on the third level, carried into one another by the golden map.**
- A golden-fixed sign character has a pattern fixed by a 3-cycle of the vertices: none, or all four. A 3-cycle moves
  every edge. So **no sign member with an edge pattern is golden-fixed.**

**3.4 At most one generation per member.**
- On each tetrahedral cover b₁ = 4, the number of ends, so n(1) = 0 (K5, exact).
- By Theorem C (sm:B1535), at ν⁴ = 1 every class has I(W₁) ≥ −b0 − n(1) = −1 and I(Λ²W₁) ∈ [−n(ν³ ⊗ ρ), 0], with
  n(ν³ ⊗ ρ) = n(ν ⊗ ρ) since ν³ = ν or ν̄ and ρ is real.
- Lemma F′ and the ceiling (sm:B1545) give −m_A − 1 ≤ I(W₁) ≤ m_A + 3.
- So **a member carries at most one generation, and generation-shaped means (−1, −1).**

**3.5 The orbit law.** For g ∈ π₁M, χ ↦ χ ∘ Ad(g) carries ν ⊗ ρ to a module isomorphic, through ρ(g), to the pullback of
ν ⊗ ρ by an automorphism of π₁N that permutes the cusps. So **every member of an A₄ orbit reads alike**, in each route.
P3 checks it at every orbit.

## 4. The instruments (`verification/`, written and checked before the seal)

- `tetra_lib.py`:
  - the selection, the level, the tetrahedral cover with its class, the twist;
  - the golden action, the A₄ orbits with their V₄ blocks and golden images, the pattern and label.
  - It loads sm:B1549's banked `three_lib.py` (the two routes, the frame, the linear algebra) by path, unchanged.
- `census.py` → `census_0.jsonl`, `census_1.jsonl`, `census_2.jsonl`, `population.json`: the structure census (§5).
- `run.py`: every member in both routes, three draws, resumable, one row per task (`run.jsonl`).
- `read_out.py`: the predictions of §7 from the rows, once. `evaluate` is pure.
- `controls.py` (`controls.json`): K1–K6 (§6). `identity.py` (`identity.json`): the banked identity (§8).

## 5. The population (outcome-blind; seeds crc32 of "B1550|route|state|character|draw")

**The census.** `census.py` read all 336 A₄ orbits of characters of order dividing 4 on the four tetrahedral covers, in
both routes at 50 digits.
- The routes agree at every orbit.
- The least live pivot is 4.2 × 10⁻¹³ and the largest dead entry 3.7 × 10⁻⁴⁰.

| state (tetrahedral cover: level word, w̄) | H₁(N) | sign member orbits | order-4 member orbits | members |
|---|---|---|---|---|
| +LR = m004 (+LRLRLR, 0) | ℤ⁴ ⊕ (ℤ/2)² | 2, free: every member an edge, (h¹, r¹, n) = (1, 0, 1), m_A = 0 | 4 of size 6 (no puncture value, (3, 2, 1), m_A = 2); 2 of size 3 (−1 on all four puncture loops, (4, 0, 4), m_A = 0) | 54 |
| −LR = m003 (−LRLRLR, (1, 1)) | ℤ⁴ ⊕ ℤ/5 | 1 of size 6: −1 on all four puncture loops, (4, 0, 4), m_A = 0 | none | 6 |
| +LLLR = m023 (+LLLRLLLRLLLR, 0) | ℤ⁴ ⊕ ℤ/3 ⊕ ℤ/9 | none | none | 0 |
| −LLLR (−LLLRLLLRLLLR, (1, 1)) | ℤ⁴ ⊕ ℤ/2 ⊕ ℤ/14 | none | none | 0 |

- **No member orbit has size 1 or 4.** So no member is golden-fixed, and by §3.3 every member orbit gives golden
  triplets on the third level. This is structure, seen at design.
- **The root's sign members** (the two free orbits, A and B):
  - each orbit holds every edge twice, and so 4 members of each label;
  - its V₄ blocks are exactly its label classes;
  - the golden map carries each label class to another.
  - B = A ⊗ ε, where ε is the A₄-invariant sign character with value −1 on all four puncture loops and on τ.
  - So on the third level each orbit gives three one-member local systems, one per non-zero parity, cycled by the golden
    map: two types, each three times.
- **The root's order-4 members of the size-6 orbits** are fixed by the translation by one non-zero parity, two members per
  parity: labelled by their stabilizer, not by an edge. **Those of the size-3 orbits** are V₄-invariant.
- **−LR's sign members** are fixed by the translation by one non-zero parity, two per parity.
- **The tasks.** Every member in both routes: 120 tasks, each with the structure and three generic interior classes, each
  class with its count and the four module readings.

## 6. Controls and disclosures (before the seal)

All hold (`verification/controls.json`, 11:27:29–11:33:36Z on 2026-10-07, 366.5 s).
- **K1. An independent rank method.** Every member orbit, and the first two non-member orbits of every state, are re-read
  in both routes with ranks by complex SVD (mpmath). (h¹, r¹, n) must equal the census's.
- **K2. The counts seen, and one banked**, in both routes, one draw:
  - the root's sign-orbit representatives (sign exponents [0, 0, 0, 0, 1, 1] and [0, 0, 0, 1, 0, 1]) read (−1, −1);
  - L8a15's sign member reads (−1, −1) (main's B1492, banked by sm:B1549).
- **K3. The A₄ action, exact,** on every state at orders 2 and 4 (§3.2). The library also asserts that N is the kernel
  of π₁M → A₄.
- **K4. The read-out on synthetic rows.** Eleven cases:
  - the PROVED and NEGATIVE verdicts;
  - P9 alone failing;
  - incomplete and duplicated records;
  - disagreeing routes and draws;
  - a reading below the cap;
  - a failed control;
  - a murky gap.
- **K5. n(1) = 0 on every tetrahedral cover**, exact: sm:B1538's reader at the trivial character, two primes, h¹ = 4.
- **K6. Below the root's tetrahedral cover**, in both routes, at every character of order dividing 4:
  - m004, its levels M₂ and M₃, the root's 4-fold (ℤ/2)² cover (not regular, two cusps) and the six fibre-direction
    double covers of M₃ carry **no sign member**;
  - their order-4 members are recorded: the three two-cusped double covers of M₃ have 20 each.

Disclosed:
- **What was read before the seal.**
  - Structure only:
    - the census (§5);
    - the A₄ group checks;
    - the stabilizers and ε;
    - the members of m004, M₂, M₃ and the covers below N in route P (scratch, then K6 in both routes).
  - Counts at members, before the seal: the two root sign-orbit representatives, in both routes with one draw each. That
    was in the exploration that found the root's A₄ cover, earlier on 2026-10-07, at the seat's scratch copy of
    sm:B1549's library. Both read (−1, −1). K2 repeats them.
  - By the orbit law (§3.5), that fixes the expectation for all 24 root sign members. P6's prior says so.
  - No count at any other member of the population was read.
- **A correction made in the exploration, before the seal.** This seat's working note first said that m004 and M₃ "have no
  members (Lemma W)". Lemma W (sm:B1535) is about the line, n(ζ), not about n(ν ⊗ ρ). The absence of members there is
  computed (K6), not proved.
- **How the design changed before the seal.**
  - The first plan read the root alone. The owner's rule on families made the selection the odd-trace states, and the
    instrument's reach limited it to words of length at most 4.
    - Longer words make the third level's relators long. ±LLLR's level words have length 12, and −LLLR's least live
      pivot in route P is 4.2 × 10⁻¹³ (largest dead 3.7 × 10⁻⁴⁰). On the root's cover the least live pivot is
      2.7 × 10⁻⁸.
  - An error in the first census start: every worker read every orbit. It was stopped by exact PID after a minute and
    restarted with the orbits partitioned. No reading changed.
  - After the census, `tetra_lib.tetra_cover` gained one assertion: N's stable letter t₃w = t³cw lies in t³K, and N has
    index 12. That makes N the kernel of π₁M → A₄. No output changed. The controls ran with the sealed file, after the
    first controls run was stopped by exact PID to include it.
- **Main's head moved** to `b7706bb6` during the design, with B1495, B1496 and B1497's seal. They were read before this
  seal (§0, and the relay that follows the bank).

## 7. Predictions (priors fixed at the seal)

| | prediction | prior |
|---|---|---|
| P1 | the banked identity holds: K2–K5 reproduce and every sealed file hashes as sealed (K1, K6 as recorded) | 97% |
| P2 | the routes agree at every member: (h¹, r¹, n), the interior dimension and the generic count | 90% |
| P3 | the orbit law: in each route every member of an A₄ orbit reads alike | 93% |
| P4 | the theorems at every reading: −1 ≤ I(W₁), −m_A − 1 ≤ I(W₁) ≤ m_A + 3, −n ≤ I(Λ²W₁) ≤ 0; the structure as the census; every gap clean (live ≥ 10⁻²⁰, dead ≤ 10⁻²⁵) | 95% |
| P5 | the three draws read alike at every task | 92% |
| P6 | every sign member of the root reads (−1, −1) in both routes | 95% |
| P7 | no order-4 member of the root is generation-shaped | 70% |
| P8 | **THE THREE:** the root's generation-shaped members are exactly its 24 sign members, with labels 8, 8, 8, and the golden map, carrying generation-shaped members to generation-shaped members, permutes the three labels as a 3-cycle | 65% |
| P9 | the family: −LR's six sign members are not generation-shaped, so of the four tetrahedral covers only the root's carries generation-shaped members | 70% |

**Why these priors.**
- **P6.** Two of the 24 were read, one per orbit, and the orbit law carries them to the rest. sm:B1549 read every sign
  member of every three-ended cover at (−1, −1).
- **P7.**
  - sm:B1549 read 120 order-4 members on three-ended covers, and none was generation-shaped. The mechanism: at order 4,
    Λ²(ν ⊗ ρ) = ν² ⊗ Λ²ρ lives at a sign character.
  - But the root's order-4 members are of new kinds: m_A = 2 at the size-6 orbits, and n = 4 at the size-3 orbits.
- **P8** is P6 and P7 with the structure of §5.
- **P9.**
  - At n = 4, I(Λ²W₁) can reach −4, and the connecting map from a four-dimensional interior is likely to have rank above
    one.
  - m136's two members merged on its companion (n = 2) read (−1, −2) (sm:B1549's §6).

A population-wide prediction is True only on complete records: every task with its row, every row with its three draws. A
refuting row decides False whatever the coverage.

## 8. BANKED IDENTITY: checked before reading

`identity.py` checks every sealed file's sha-256 (`ARTIFACT_HASHES.txt`) and re-runs K2–K5 before `run.py` reads
anything. A single difference stops the run.

## 9. Reading rules

- **PROVED (the three)** if P1–P5 hold on complete records and P8 holds.
  - Then on the root's tetrahedral cover the frame's generation sector at orders dividing 4 is exactly the 24
    parity-labelled sign members, each one generation.
  - On the third level each of the two types appears exactly three times, once per non-zero parity, and the golden map
    carries each to the next. The three is the order of the root's monodromy on its parities, which GENESIS's SE1
    forces (§3.1).
- **NEGATIVE (the three)** if P1–P5 hold on complete records and P8 fails. Then either:
  - a root sign member is not generation-shaped;
  - or an order-4 member is generation-shaped. It would still be in a golden triplet (§3.3, §5), but labelled by its
    stabilizer or by nothing.
  - The read-out names which.
- **OPEN** otherwise.
- P9 is scored and reported either way. It decides whether the root's generation sector is the golden pair's or the
  root's alone.
- **NO NEGATIVE FROM A BUG.**
  - Every count is read in two routes that share no code beyond the cover's action, the characters and the holonomy.
  - Three draws per member.
  - Every member of every orbit is read.
  - The theorems of §3 are checked at every reading.
- 0 of 19 is unchanged either way.

## 10. What this arc does not decide

- **Whether the third level's three are the physical three generations.**
  - That is a reading: GENESIS FK14 (which object) and FK9 (which state).
  - Main's B1496 grades it as the smooth mechanism (a free quotient, characters selecting). Here the quotient's group is
    forced by SE1, not chosen.
- **The glued module.** One module of index three (main's B1496, item 3) rather than three summands. B1495's (3, 9) on
  L8a15's direct sum warns that a direct sum's Λ² has cross terms. This arc reads members one by one.
- **The two types.** Orbit B = A ⊗ ε. Whether ε's obstruction to descending is the Schur class of A₄ (the binary
  tetrahedral group), and what the two types are physically, is not read.
- **Characters of other orders** (3, 8, 12, …), **non-interior classes**, **states with longer words** (+LLLLLR,
  −LLLLLR, +LLLRLR, +LLLRRR, ±LLLLLLLR to twelve ends), and **states of even trace**, where the parities are not one orbit.
- **Masses and mixings.** An exact A₄ makes a triplet's three alike (B1391's Schur limit).
