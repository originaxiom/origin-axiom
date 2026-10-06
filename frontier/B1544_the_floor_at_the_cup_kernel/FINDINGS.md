# B1544 — THE FLOOR AT THE CUP KERNEL: Lemma F (I(W) ≥ k − m − 1) proved; the floor holds on the whole cup kernel of N₄₅ and the four degree-60 covers, so those covers carry no three at the trivial character, at any class

cc (the SM-derivation seat), 2026-10-06. **Verdict: NEGATIVE, by the seal's §9.** Sealed at 78acd895. The banked identity held
(18:08:00–18:14:09Z). The run went as sealed, 18:14:09–18:30:41Z on two workers, rc 0, and its record was committed unread at
48e50abb. `read_out.py` ran once, at 18:30:59Z (96517766).

- **Lemma F, proved at design time** (§1). At the trivial character on a finite cover with m cusps, every class c of
  H¹(N; ρ) has I(W) ≥ k − m − 1, where k is the number of cusps on which c is non-zero.
  - sm:B1543's floor I(W) ≥ −1 is therefore a theorem at every class non-zero on every cusp.
  - A count with I(W) = −g needs c to vanish on at least g − 1 cusps.
- **Corollary F′.** With Theorem C (ii), three needs a + rk δ¹_W ≤ n(1) − 2 and k ≤ m − 2. On the four degree-60 covers this
  leaves three only in the cup map's kernel K0 (Proposition D): at three supports of four cusps on d10.13's and d10.36's
  covers, and nowhere on d10.16's and d10.40's.
- **The run** read the generic class of K0(S) for every closed support S of K0, which decides the least I(W) on all of K0
  (Lemma G″). It covered 30 subspaces, 90 tasks and 180 readings in route F and route R.
  - P1–P4 hold and P5–P6 are False: 4 of 6, against 3.68 expected.
  - **The floor holds on all of K0 on the five covers.** The least I(W) on K0 is 0 on N₄₅ and −1 on the degree-60 covers,
    where it is reached at the interior.
- **Three at the trivial character on the four degree-60 covers: impossible at every class.** The three supports where it
  could live read (0, −3) on d10.13's and d10.36's covers, and Proposition D excludes d10.16's and d10.40's. This closes the
  special classes sm:B1542 left open on these covers.
- **N₄₅, the golden order.** K0 reads (0, 0) at every stratum. On N₄₅, three at the trivial character remains possible only
  at classes outside K0 with rk δ¹_W ∈ {1, 2} and support on at most three cusps (§5).
- **After the seal: main's question on the cusps** (§4). All four of m003's mirror classes lift to N₄₅, with five lifts each.
  Every lift fixes exactly one cusp and is rhombic there. No mirror of m003 lifts to any of the four degree-60 covers.

**0 of 19 stays 0.**

## 1. The theorems (the seal's §3, as sealed)

**Lemma F.** At the trivial character on a finite cover N (m cusps) of a complete finite-volume hyperbolic 3-manifold, every
class c ≠ 0 of H¹(N; ρ) has I(W) ≥ k − m − 1, with k = #{cusps T : c_T ≠ 0 in H¹(T; ρ)}.
- (1) The identity I(E) = h⁰(N; E) − h⁰(N; E*) + h⁰(∂N; E*) − r¹(E) gives I(W) = −1 + h⁰(∂N; W*) − r¹(W).
- (2) h⁰(T; W*) = 2 at every cusp, for every c. On a parabolic lattice ⟨[[1, z₁], [0, 1]], [[1, z₂], [0, 1]]⟩ with z₂/z₁ ∉ ℝ, a
  cocycle's (2, 2) entries satisfy z₁x⁽²⁾ = z₂x⁽¹⁾ and z̄₁x⁽²⁾ = z̄₂x⁽¹⁾, so they vanish. The invariant functional of ρ
  therefore kills c and lifts to W*.
- (3) r¹(W) ≤ m + (2m − k). The image of H¹(N; W) in H¹(∂N; W):
  - projects into the line's restriction image, of dimension m (half lives);
  - meets the kernel of that projection in at most h¹(∂N; ρ) − k = 2m − k.

So I(W) ≥ −1 + 2m − (3m − k). □

**Corollary F′.** I(W) = −g needs a + rk δ¹_W ≤ n(1) + 1 − g (Theorem C (ii), whose dual term is at most n(1)) and
k ≤ m + 1 − g (Lemma F). Here a = dim(⟨c_T⟩ ∩ Λ(ρ)) ≥ 1 for a class that is not interior.

**Lemma G″.** At c ∈ K0, I(W) = −1 + k − rk δ¹_{W*} (route R's identity with rk δ¹_W = 0).
- On a closed support S, the classes with support exactly S form a dense open subset of K0(S), where k = |S|.
- rk δ¹_{W*} is largest on a dense open subset.
- So the generic class of K0(S) has the least I(W) among the classes of K0 with support S.
- Every class of K0 has a closed support. □

**Proposition D** (from the structure, read in two routes, and sm:B1542's banked interior counts, re-read here).
- **d10.13's and d10.36's covers.** I(W) = −1 at every interior class. A class with I(W) = −3 lies in K0(S) for a closed support
  with 1 ≤ |S| ≤ 4, and the only such S are three sets of four cusps.
- **d10.16's and d10.40's covers.** No class reads I(W) = −3.

## 2. The run and the read-out

`verification/read_out.json`, once, on complete records (90 of 90 tasks; 180 readings):

| prediction | prior | read |
|---|---|---|
| P1 one count per subspace and per τ-orbit, both routes | 95% | **True** |
| P2 every class in K0 with support exactly S | 96% | **True** |
| P3 route R's identities; Lemma F's ingredients in both routes | 95% | **True** |
| P4 the floor on K0, I(W) ≥ −1 at every reading | 70% | **True** |
| P5 a generation-shaped subspace | 8% | **False** |
| P6 (−3, −3) at a subspace | 4% | **False** |

The counts, alike in both routes and at every draw:

| cover | S = ∅ (interior) | the supports where three could live | the other proper supports | the full support |
|---|---|---|---|---|
| N₄₅ | — | (0, 0) at all ten of three cusps | (0, 0) at all five of four cusps | (0, 0) |
| d10.13's | (−1, −3) | (0, −3) at {0, 1, 3, 5}, {0, 1, 7, 13}, {3, 5, 7, 13} | — | (0, −3) |
| d10.36's | (−1, −3) | (0, −3) at {0, 1, 2, 7}, {0, 2, 3, 8}, {1, 3, 7, 8} | — | (0, −3) |
| d10.16's | (−1, −3) | none (Proposition D) | — | (1, −1) |
| d10.40's | (−1, −3) | none (Proposition D) | — | (1, −1) |

The interior parts reproduce sm:B1542's banked (−1, −3). The full supports satisfy Lemma F. The generic class of K0 on the
room-4 covers reads (1, −1), where the 5̄′ side is only −1.

## 3. What the ranks say

Route R's ranks and Lemma F's quantities at every reading (`verification/run.jsonl.gz`):

| cover, support | k | rk δ¹_{W*} | r¹(W) | Lemma F's bound on r¹(W) (3m − k) | I(W) |
|---|---|---|---|---|---|
| N₄₅, three cusps | 3 | 2 | 9 | 12 | 0 |
| N₄₅, four cusps | 4 | 3 | 9 | 11 | 0 |
| N₄₅, all five | 5 | 4 | 9 | 10 | 0 |
| d10.13's and d10.36's, interior | 0 | 0 | 12 | 18 | −1 |
| d10.13's and d10.36's, four cusps | 4 | 3 | 11 | 14 | 0 |
| d10.13's and d10.36's, all six | 6 | 5 | 11 | 12 | 0 |
| d10.16's and d10.40's, interior | 0 | 0 | 8 | 12 | −1 |
| d10.16's and d10.40's, all four | 4 | 2 | 6 | 8 | 1 |

- At every reading h⁰(∂N; W*) = 2m and h¹(∂N; W) = 4m − k, as Lemma F's proof says. Both are read in both routes from each
  route's own cusp transports.
- On K0, r¹(W) stays below Lemma F's ceiling 3m − k by 1 to 6, and I(W) exceeds Lemma F's bound k − m − 1 by exactly that
  slack. I(W) = −1 + k − rk δ¹_{W*} never falls below −1.
- In sm:B1543's language, the secondary invariant of K0's classes at the cusps never exceeds dim(⟨c_T⟩ ∩ Λ(ρ)). That is the
  floor, read here on all of K0.
- On N₄₅, r¹(W) = 9 on all of K0 and I(Λ²W) = 0. Its cup kernel is generation-neutral throughout.

## 4. After the seal (not used by the verdict)

**main's question (its relay of 2026-10-06, B1477): the type of each cusp under each lifted mirror.** It was computed after
the read-out with scratch code, which is described here and kept out of the record.
- **The mirrors.** Orientation-reversing automorphisms of π₁(m003) = ⟨a, t | ttATAAATA⟩ were found by matching traces:
  tr²(φ(g)) = conj(tr²(g)) on every word of length ≤ 5, with the relator sent to ±1.
  - Their actions on H₁ = ℤ/5 ⊕ ℤ give the four orientation-reversing classes of Isom(m003) = ℤ/2 ⊕ ℤ/4.
  - The orientation-preserving ones were found the same way.
- **The lifts and their cusp maps.**
  - A lift to a cover is a point map σ with σ(x^g) = σ(x)^φ(g). Every candidate σ(0) was checked over the whole Schreier
    graph.
  - The cusp of x goes to the cusp of σ(x)^g₀, where g₀ carries the base cusp point to the fixed point of φ(l).
  - On an invariant cusp the linear part is φ restricted to the cusp's lattice. An orientation-reversing involution of
    GL(2, ℤ) is rectangular iff it is the identity mod 2.
- **N₄₅.** All four mirror classes lift, five lifts each, as do all four orientation-preserving classes (the identity
  included). Every lifted mirror fixes exactly one cusp and permutes the other four in a 4-cycle, and it is **rhombic** at its
  fixed cusp. Each cusp is the fixed cusp of four lifts.
- **The four degree-60 covers.** No mirror class lifts. The cycle types of a and φ(a) already differ on every cover, which is a
  check independent of the σ search. So the room-3 covers have no lifted mirror.
- **The count's symmetry.** An orientation-reversing isometry preserves the count, since the four is real (ρ ∘ f_* ≅ ρ̄ = ρ).
  A lifted mirror of N₄₅ carries one τ-orbit of three-cusp supports to the other ({0, 1, 2} ↦ {0, 1, 4}). The two orbits read
  one count, (0, 0), as the symmetry requires. This check was not sealed.

## 5. Where three can still live in this frame

- **N₄₅'s classes outside K0.** Corollary F′ leaves them: a + rk δ¹_W ≤ 2 and support on at most three cusps.
  - These are interior classes with rk δ¹_W ≤ 2 (the generic interior class has 9), and non-interior classes with a = 1 and
    rk δ¹_W = 1.
  - The rank loci of the cup map on N₄₅ are the next computation there. The deck grading constrains them.
- **Members ν other than the trivial character.** The argument of Lemma F does not depend on the trivial character's
  particulars. It splits the cusps by whether ν is trivial on them and gives a lower bound on I(W₁) that falls only at cusps
  where ν is trivial and c vanishes.
  - So three at a member needs cusps where ν is trivial. sm:B1543 §5 already saw this when the cup map vanishes.
  - The general statement, with its own check, is the next arc's.
  - It bears on sm:B1538's room-three members of the silver pair, whose records are to be regenerated.
- **Other covers**, where the line leads or where K0 has small supports.
- **Which class and which cover the genesis selects** is GENESIS GAP4 and THE_BAR's question, not this arc's.

## Seen first

- **The repo sweep** (the seal's §0): twelve terms on every head, with the heads listed there. The hits that bear are this
  seat's own: sm:B1543's observation of the floor, sm:B1542's and sm:B1541's banked counts, sm:B1535's Theorem C, and
  sm:B1542's kill entry. The other hits are other objects: Massey products as deformation obstructions or link invariants,
  and triple products as couplings.
- **The literature:**
  - Putman's note on half lives;
  - Menal-Ferrer and Porti on twisted cohomology, whose cusp computations cover the holomorphic Vₙ and not this frame's
    four V₂ ⊗ V̄₂;
  - Garoufalidis and Levine on Massey products in 3-manifolds.

  None states Lemma F or a count of this frame. Lemma F is elementary once the frame is set up, and it may be standard in
  other words. It is proved here and checked at every reading, not claimed as new.

## Disclosures

- **The first design was replaced before the seal** (ERROR_LEDGER, a design slip). It would have read only classes non-zero on
  every cusp, where Lemma F fixes the floor. Its two control trials read no count at a class of K0 beyond banked interior
  classes.
- **An E12 slip** (ERROR_LEDGER): a bare `import read_out` returned sm:B1536's module in the first control trial. It was fixed
  before the seal.
- **Counts read before the seal**: only at banked classes (the generic class of H¹ and the interior, on every cover).
- **After the seal**: the mirror computation of §4. It ran after the read-out, uses no record, and does not enter the verdict.

## Files

- `PREREGISTRATION.md` (sealed; sha-256 in `docs/SEAL_LEDGER.md`), `ARTIFACT_HASHES.txt`, `arc_verdict.json`.
- `verification/floor_lib.py`: both routes. It covers the cup map by the cochain formula, K0, the cusp labels, the strata, the
  closed supports, a class's support, and Lemma F's ingredients.
- `verification/controls.py` → `controls.json` (K1–K6); `verification/identity.py` → `identity.json`.
- `verification/run.py` → `run.jsonl.gz` (record; `run_sha256.txt`); `verification/read_out.py` → `read_out.json`,
  `read_out_log.txt`.
- Lock: `tests/test_b1544_the_floor_at_the_cup_kernel.py`.
