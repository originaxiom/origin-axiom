# B1545 — THE FLOOR AT EVERY MEMBER: I(W₁) ≥ k − m_A − b0 at every finite-order member, so three needs 3 − b0 cusps where the character is trivial; sm:B1538's four room-3 covers of the silver pair carry no three at any member, at any class, in either order

cc (the SM-derivation seat), 2026-10-06. **Not sealed: a theorem, its ingredients checked by own code at every reading below,
and a corollary from banked structure. No count is predicted.** Verdict: PROVED.

- **Lemma F at members** (§1). Let ν be a character of finite order on a finite cover N of a complete finite-volume hyperbolic
  3-manifold, and c ≠ 0 a class of sm:B1515's frame there. Then I(W₁) ≥ k − m_A − b0.
  - m_A is the number of cusps where ν is trivial.
  - k is the number of those cusps where c restricts non-trivially.
  - b0 = [ν⁴ = 1].
  - At the trivial character this is sm:B1544's Lemma F.
- **Consequences** (§2).
  - Three, in either order, needs at least 3 − b0 cusps where ν is trivial and the class vanishes.
  - At a member that is non-trivial on every cusp, I(W₁) ≥ −b0: at most one generation, and none when ν⁴ ≠ 1.
- **Corollary G: the silver pair's room-3 covers** (§3). sm:B1538's read-out of 2026-10-04 found room 3 only on four
  degree-8 covers of m135 and m136. Each has four cusps, and each cusp is a pair of punctures. The punctures' character
  values are constant on the cusps and multiply to 1. So a character whose fourth power is a puncture character is trivial
  on at most two cusps. With Lemma F, b0 = 0, and sm:B1538's Lemma W′, **no member of these four covers carries three, at any
  class, in either order.** This closes the frame's three-generation lead on the silver pair's puncture characters. It holds
  pending sm:B1538's regenerated records, which fix which covers have room 3 (§4).
- **Checked by own code** (§4):
  - Lemma F's ingredients at 288 member readings on 32 covers of sm:B1538's population, in route R, every one exactly as the
    proof says;
  - the puncture structure behind Corollary G, at every invariant character of order dividing 24 on the four covers.

**0 of 19 stays 0.**

## 1. Lemma F at members

**Setting** (sm:B1536 §2, sm:B1538 §2).
- ν is a finite-order character of π₁N, the four is ρ, V = ν ⊗ ρ and L = ν⁻⁴.
- A class c ∈ H¹(N; ν⁵ ⊗ ρ), c ≠ 0, defines W₁ = [[V, c·L], [0, L]]. The count is I(E) = n(E) − n(E*).
- The cusps split three ways:
  - A, where ν is trivial;
  - B, where ν is not trivial but ν⁴ is;
  - C, where ν⁴ is not trivial.
- k = #{T ∈ A : c_T ≠ 0}. On a cusp outside A, ν⁵ ⊗ ρ restricted to T is acyclic unless ν⁵|_T = 1. When it is not acyclic,
  both pieces of W₁ are acyclic on T, so c_T does not enter.

**Lemma F′.** I(W₁) ≥ k − |A| − b0, with b0 = [ν⁴ = 1 on N].

*Proof.*
- **(1)** The identity I(E) = h⁰(N; E) − h⁰(N; E*) + h⁰(∂N; E*) − r¹(E) (sm:B1527's Lemma E in route R's form, checked at every
  banked reading) gives I(W₁) = −b0 + h⁰(∂N; W₁*) − r¹(W₁).
  - h⁰(N; W₁) = 0. H⁰(N; V) = 0, and when ν⁴ = 1 the connecting map sends 1 to c ≠ 0.
  - h⁰(N; W₁*) = b0. The sub L* is the only source of invariants, since H⁰(N; V*) = 0.
- **(2)** h⁰(T; W₁*) is 2 on A, 1 on B and 0 on C.
  - On A both pieces are trivial on T, and sm:B1544's Lemma F step (2) applies: the four's invariant functional kills every
    cocycle on a parabolic lattice.
  - On B the line is trivial and ν ⊗ ρ has no invariants, because a parabolic acts by ν times a unipotent.
  - On C neither piece has invariants.

  So h⁰(∂N; W₁*) = 2|A| + |B|.
- **(3)** r¹(W₁) ≤ (|A| + |B|) + (2|A| − k).
  - The projection H¹(∂N; W₁) → H¹(∂N; L) sends the image of H¹(N; W₁) into the line's restriction image. That image has
    dimension r¹(L) = |A| + |B|: half lives, with r¹(L) = r¹(L̄) for a unitary character.
  - The projection's kernel is H¹(∂N; V)/δ⁰_∂H⁰(∂N; L), of dimension 2|A| − k. Here h¹(T; V) is 2 on A and 0 elsewhere, and
    δ⁰_∂ has rank k.
- (1)–(3): I(W₁) ≥ −b0 + 2|A| + |B| − 3|A| − |B| + k. □

The other order: W₂* = W₁(ν̄, c′) (sm:B1535 (iii)), and ν̄ has the same A, B, C and b0. So the bound reads the same for counts
of either order.

## 2. Consequences

- **Three needs trivial cusps.** I(W₁) = −3 needs |A| − k ≥ 3 − b0. That means at least two cusps where ν is trivial and c
  vanishes when ν⁴ = 1, and three when ν⁴ ≠ 1.
- **A character non-trivial on every cusp** gives I(W₁) ≥ −b0. sm:B1543 §5 (item 3) saw this when the cup map vanishes. It
  now holds at every class.
- **The floor I(W₁) ≥ −b0** holds wherever c is non-zero on every cusp of A. It is open only on classes that vanish on some
  cusp where ν is trivial. sm:B1544 read every such class of the cup kernel at the trivial character on five covers, and the
  floor held there.
- **Update, 2026-10-07: the ceiling.** Step (1)'s identity with r¹(W₁) ≥ 0 also bounds the count from above, so
  k − m_A − b0 ≤ I(W₁) ≤ 2m_A + m_B − b0, with m_B = |B|.
  - The ceiling is attained exactly when no class of W₁ restricts non-trivially to the boundary.
  - At a member where neither ν nor ν⁴ is trivial on any cusp, I(W₁) = −b0 = 0 at every class.
  - The two-sided form |I(W₁)| ≤ m_A + b0 does not follow from the floor. In the other order the floor bounds I(W₂)
    through W₂* = W₁(ν̄, c′), not I(W₁). The record refutes it.
  - This arc's 288 readings (`verification/two_sided_check.py` → `two_sided_check.json`) show:
    - floor and ceiling hold at every reading, and the ceiling is attained at 16;
    - all 16 readings with no cusp in A or B read 0;
    - |I(W₁)| ≤ m_A + b0 fails at 18 readings on five covers. The largest is I(W₁) = 5 at m_A = 2, m_B = 4, b0 = 1 on m136's
      D8.2-0-4.w0 and D8.4-0-2.w0.
  - For generations nothing changes: g in either order needs m_A ≥ g − b0 + k.

## 3. Corollary G: sm:B1538's four room-3 covers

- **The covers.** m135's D8.2-0-4.w1 and D8.4-0-2.w4, and m136's D8.2-0-4.w3 and D8.4-0-2.w5. Each has fibre group K, eight
  punctures l_x (x ∈ D, |D| = 8), and four cusps. Each cusp is a monodromy orbit {x, π(x)} of two punctures
  (`verification/orbit_census.json`).
- **The puncture structure.** ζ is the character on K. It satisfies ζ ∘ f = ζ, and [f(l_x)] = [l_π(x)] in H₁(K). So ζ(l_x) is
  constant on each cusp. The punctures sum to zero in H₁(K), so the product of the ζ(l_x) is 1.
- **The argument.** Let ν be a member whose ν⁴ is a puncture character. Suppose ν is trivial on three cusps.
  - Then ζ(l_x) = 1 on their six punctures.
  - The remaining cusp's two punctures share a value λ, and λ² = 1.
  - So λ⁴ = 1, and ν⁴ is trivial on every puncture, which contradicts the assumption.

  Hence |A| ≤ 2, and with b0 = 0, Lemma F′ gives I(W₁) ≥ k − 2 ≥ −2.
- **Members whose fourth power is not a puncture character.** By sm:B1538's Lemma W′, n(ν⁴) = 0 there. Theorem C (iii)
  then allows at most one generation.
- **So no member of the four covers carries three, at any class, in either order.**
- sm:B1538's room census (its read-out of 2026-10-04, recorded in this seat's relay of 2026-10-06 §3) found room 3 only on
  these four covers. Room 3 is necessary by Theorem C (iii). So within sm:B1538's Part F′ scope, the silver pair's puncture
  characters carry no three. The census is to be re-derived from the regenerated records before sm:B1538 banks. Corollary G's
  statement about the four covers does not depend on it.
- **Update, 2026-10-06.** sm:B1538's records, regenerated by its sealed code, reproduce all 31 numbers of its first read-out
  (33b14d53). Room 3 lives on exactly these four covers within Part F′'s scope, so the conclusion above holds unconditionally
  there. LB6 is VERIFIED (`arc_verdict.json`, with the date of the change).

## 4. The checks (`verification/`, own code; route R is sm:B1536's `route_r.py` through sm:B1538's `punct_four.py`, by path)

- **`members_check.py`** → `members_check.json`.
  - The covers: sm:B1538's four room-3 covers, then every other cover of its population with at least three cusps, taken in
    the population's order. The record has 32 covers: 4 of m004, 2 of m003, 12 of m135 and 14 of m136.
  - The members have h¹(N; ν⁵ ⊗ ρ) ≥ 1 in route R. Two random classes are taken per member.
    - On the four room-3 covers: eight members each, fourth roots ν of puncture characters, so b0 = 0 (Corollary G's case).
    - On the other covers: four members each, fourth roots of the trivial character first (b0 = 1 when ν⁴ = 1), then of
      puncture characters.
    - The puncture characters have order dividing 12, with s of order dividing 24. Character orders whose enumeration would
      exceed 20,000 characters on a cover are skipped there.
  - At each reading: the partition A, B, C from the character's values on both peripheral generators of each cusp
    (sm:B1538's `trivial_cusps`), the support of c, b0, and route R's h⁰(∂N; W₁*), h¹(∂N; W₁), r¹(W₁), n(W₁) and n(W₁*).
  - The checks at each reading:
    - h⁰(∂N; W₁*) = 2|A| + |B|, exactly;
    - h¹(∂N; W₁) is the sum over the cusps of 4 (A, c_T = 0), 3 (A, c_T ≠ 0), 2 (B) and 0 (C), exactly;
    - r¹(W₁) ≤ 3|A| + |B| − k;
    - I(W₁) ≥ k − |A| − b0;
    - I(W₁) satisfies the identity of step (1).
  - **All hold, at every one of 288 readings** (the record lists each).
    - The readings include b0 = 1 (216) and b0 = 0 (72), |A| from 0 to 8 and |B| from 0 to 6, C cusps at 72 readings, and
      every cusp in A at 70.
    - The bound I(W₁) ≥ k − |A| − b0 is attained at 42 readings.
    - On the four room-3 covers (64 readings, all b0 = 0), |A| ≤ 2 at every member, as Corollary G says.
- **`orbit_census.py`** → `orbit_census.json`. On the four covers, at every invariant ζ with ζ²⁴ = 1 (110,592, 110,592, 55,296
  and 55,296 characters):
  - ζ(l_x) is constant on cusps;
  - the product over the punctures is 1;
  - when ζ⁴ is a puncture character, ζ kills the punctures of at most two cusps.

  All hold. This is the necessary condition behind |A| ≤ 2, enumerated.
- **The trivial character** is sm:B1544's: its controls (K6) and all 180 readings carry the same ingredients and hold.

## 5. Where three can still live in this frame

- **N₄₅ at the trivial character, outside the cup kernel**: classes of cup rank 1 or 2, with support on at most three cusps
  (sm:B1544 §5).
- **Members with at least 3 − b0 cusps where ν is trivial**, on covers not yet read. The golden lift is one of them: on a
  5-fold cyclic cover, a golden member has b0 = 0 and needs three cusps of the base where it is trivial.
- **Classes that vanish on cusps where ν is trivial**, where the floor itself is open.
- **Which class and which cover the genesis selects** (GENESIS GAP4, THE_BAR).

## Seen first

- **The repo sweep.** `git fetch --all`, then `scripts/checks/prior_work.py` over every head with twelve terms: "every
  member", "trivial cusps", "cusps where nu is trivial", "puncture character", "Lemma F", "vanishing cusps", "k - m - 1",
  "room-three members", "D8.2-0-4", "D8.4-0-2", "trivial on the cusp", "the floor at".
  - The heads were this branch, main (201bd35b), the audit lane's two branches, the new web seat's branch, seat/outside-bench,
    seat/paper-review-verification, sep16-branch, and two seat branches seen for the first time (…/kind-hypatia, …/project-thread).
  - The hits that bear are this seat's: sm:B1544 (Lemma F at the trivial character), sm:B1538 (its covers, characters,
    `trivial_cusps` and Lemma W′), sm:B1536 (route R), sm:B1543 §5, and the kill graph's entries.
  - main's B1333 derives an index on several boundary tori for its own frame (the class index of a vacuum). Its "trivial
    cusps" are that frame's, and it does not bound this frame's I(W₁).
  - The other hits ("Lemma F" names other arcs' lemmas, "every member" and "trivial on the cusp" are common words) are other
    objects.
- **The literature:** as sm:B1544 (Putman on half lives; Menal-Ferrer and Porti on the cusp cohomology of the holomorphic Vₙ;
  Garoufalidis and Levine on Massey products). None states Lemma F′. It is elementary once the frame is set up, and it is
  proved and checked here, not claimed as new.

## Files

- `verification/members_check.py` → `verification/members_check.json` (288 readings, all holding).
- `verification/orbit_census.py` → `verification/orbit_census.json`.
- `verification/two_sided_check.py` → `verification/two_sided_check.json` (the ceiling, 2026-10-07; reads the record above).
- Lock: `tests/test_b1545_the_floor_at_every_member.py`.
