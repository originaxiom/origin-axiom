# B1546 — THE LOW-RANK CLASSES: the classes of N₄₅ where three could still live at the trivial character are a symmetric matrix's rank locus (Proposition L), and every one of them sits at I(W) ≥ −1 — N₄₅ carries no three at the trivial character, at any class

cc (the SM-derivation seat), 2026-10-06. **Verdict: NEGATIVE, by the seal's §9.** Sealed at cc48131a. The banked identity held
(20:45:23–20:47:27Z). The run went as sealed, 20:47:27–21:05:02Z on one worker, rc 0, and its record was committed unread at
5dd6682a. `read_out.py` ran once, at 21:05:27Z (c4f9d5ee).

- **Proposition L, proved at design time** (§1). On N₄₅ the interior classes of cup rank at most two are, in the deck
  grading, the classes c of a ten-dimensional space Kc0 whose symmetric 4 × 4 matrix S(c) has rank at most two.
  - S is a linear isomorphism onto the symmetric matrices, and rk δ¹_W(c) = rk S(c).
  - So the classes of cup rank one are the squares S(c) = ℓℓᵀ, and the classes of cup rank at most two are the sums of two.
  - The checks are exact mod p, in two routes at two primes.
- **So every class of N₄₅ that could read three lies in twelve families** (with Corollary F′ and sm:B1544):
  - the squares Z1;
  - the sums of two, Z2;
  - for each of the ten sets S of three cusps, a square plus a class of K0(S).
  A generic class has the least I(W) on its family (Lemma G‴).
- **The run read every family's generic class, and the ten eigen-lines, in two routes: 132 readings.**
  - Every family reads I(W) ≥ −1: the squares (−1, −9), their sums (−1, −10), and all ten square-plus-K0(S) families (0, −7).
  - The lines read (−1, −9) and (−1, −8).
  - **No class of N₄₅ reads I(W) = −3 at the trivial character**, so the golden cover carries no three in this frame there.
- **Lemma M, and the floor.** At an interior class of Kc0, I(W) = −1 − μ, where μ ≥ 0 is the rank of a Massey-type boundary
  term. The run reads μ = 0 at every interior subspace (route R's s = r at every reading).
  - With semicontinuity, I(W) = −1 exactly at every interior class of cup rank one or two (Corollary L″, §4).
  - The floor held where it was least protected. Its prior was 40%.
- **Predictions:** P1–P5 and P8 hold; P6 and P7 are False. That is 6 of 8, against 5.13 expected from the priors.

**0 of 19 stays 0.**

## 1. The theorems (the seal's §3, as sealed)

**Where three can live on N₄₅** (sm:B1544's Corollary F′, n(1) = 4, m = 5).
- A class with I(W) = −3 has a + r ≤ 2 and k ≤ 3, where r = rk δ¹_W.
- r = 0 is the cup map's kernel, which sm:B1544 read in full: nothing below 0.
- r = 2 forces a = 0, so the class is interior.
- r = 1 is an interior class, or an interior class of cup rank one plus a class of K0(S) for a set S of three cusps (the
  only closed supports of size ≤ 3).

**Proposition L.** Notation: E_m and V_j are the deck group's eigen-parts of H¹(N; ℂ) and H¹(N; ρ), K_m = {c : c ∪ E_m = 0},
and Kc0 = V_0^int ⊕ ⊕_(j≠0) (K_0 ∩ K_−j ∩ V_j^int), of dimension 10. Every interior class of cup rank ≤ 2 lies in Kc0, and
there rk δ¹_W(c) = rk S(c) for a linear isomorphism S of Kc0 onto the symmetric 4 × 4 matrices.
- The proof (seal §3.2) rests on four checks, each exact mod p in route F (p_F = 67108201) and route R (p_R = 2147482801):
  - **L0:** the grading of H²(N; ρ) by j + m is a direct sum.
  - **L1:** the pencils y ↦ (c ↦ c ∪ y) on V_j^int have rank 2 at every y, with kernels in K_−j; V_0^int's blocks have rank
    at most 1.
  - **L2:** the image on Kc = V_0^int ⊕ ⊕(K_−j ∩ V_j^int) is four lines, one in each H²_t. The part of the cup matrix off
    those lines' common directions forces the z-coordinates to vanish: every γ_j³ is in the ideal of its 3 × 3 minors, by a
    Gröbner basis.
  - **L3:** on Kc0 the 4 × 4 matrix F(c) is persymmetric after scaling, and its ten entries are the ten eigen-lines.
- **The ten eigen-lines are the unit matrices of S.** u_j sits on the diagonal, and w_j, v_a, v_b sit on off-diagonal pairs.
  - In τ's weights, S(c) ∈ Sym²(U) with U graded 1, 2, 3, 4.
  - So u_j = e_t² with 2t ≡ j, w_j = e_a e_b with a + b ≡ j, and v_a, v_b = e₁e₄, e₂e₃.

**Corollary L′.** The squares Z1 (an irreducible cone of dimension 4) and the rank-≤2 classes Z2 (irreducible, dimension 7)
are all the interior classes of cup rank one and at most two. With the K0 translates above, **every class of N₄₅ reading
I(W) = −3 at the trivial character lies in Z1, Z2 or one of the ten families X_S = Z1 + K0(S).**

**Lemma G‴.** On an irreducible family with r, k and a constant on a dense open set, the least I(W) = −1 + k + r − s is at
the classes where s = rk δ¹_{W*} is largest. Those form a dense open set, since rank is lower semicontinuous.

**Lemma M.** At an interior class c of Kc0, I(W) = −1 − μ(c) with μ(c) = s − r ≥ 0.
- By Poincaré–Lefschetz duality, s is the rank of x ↦ c ∪ x from H¹(N, ∂N; ℂ) to H²(N, ∂N; ρ).
- Composing with H²(N, ∂N; ρ) → H²(N; ρ) gives δ¹_W(c) on H¹_int(N; ℂ), whose rank on Kc0 is r. Control K1 checks this:
  the cup rank on the four interior line classes equals the cup rank at every eigen-line and at a generic class of V_0^int.
- μ is the rank of the boundary part: the relative products whose absolute part vanishes.

## 2. The run and the read-out

Coverage: 66 of 66 tasks, 132 readings, every one read alike in route F and route R and across the three draws of each
route.

| subspace | count (I(W), I(Λ²W)) | cup rank r | support | route R: rk δ¹_W, rk δ¹_{W*}, rk δ¹ of Λ²W, of (Λ²W)* |
|---|---|---|---|---|
| Z1, a generic square | (−1, −9) | 1 | ∅ | 1, 1, 0, 9 |
| Z2, a generic sum of two squares | (−1, −10) | 2 | ∅ | 2, 2, 0, 10 |
| X:S, each of the ten three-cusp sets | (0, −7) | 1 | S | 1, 3, 0, 10 |
| u₁ … u₄ | (−1, −9) | 1 | ∅ | 1, 1, 0, 9 |
| w₁ … w₄ | (−1, −9) | 2 | ∅ | 2, 2, 0, 9 |
| v_a, v_b | (−1, −8) | 2 | ∅ | 2, 2, 0, 8 |

Route F's supplies (n(W), n(W*), n(Λ²W), n(Λ²W*)) agree with every count:
- Z1 and u_j: (20, 21, 9, 18);
- Z2: (19, 20, 8, 18);
- w_j: (19, 20, 9, 18);
- v: (19, 20, 10, 18);
- X:S: (21, 21, 11, 18).

**Predictions** (`verification/read_out.json`):
| | prediction | prior | read |
|---|---|---|---|
| P1 | one count per subspace; τ-orbits; Galois-conjugate lines; no line below its family | 90% | True |
| P2 | every class has the sealed cup rank and support | 95% | True |
| P3 | route R's identities; Lemma F's ingredients | 95% | True |
| P4 | Lemma M: I(W) ≤ −1 at every interior reading | 93% | True |
| P5 | the floor I(W) ≥ −1 at every reading | 40% | True |
| P6 | a generation-shaped subspace | 10% | False |
| P7 | (−3, −3) | 5% | False |
| P8 | all ten X:S read one count (the lifted mirror) | 85% | True |

The verdict, by the seal's §9: P1–P4 hold on complete records, P7 is False, and every family's generic class reads
I(W) ≥ −2 (in fact ≥ −1). **NEGATIVE.**

## 3. What the ranks say

- **The Massey term vanishes where it was read.** At every interior subspace s = r, so μ = 0 and I(W) = −1. The relative
  products of a low-rank class with the line's interior classes never land in the boundary part beyond what the absolute cup
  product already gives.
- **The squares plus a cusp stratum.** There k = 3, r = 1 and s = 3, so I(W) = 0. Theorem C's form gives a − e = 0. Three
  would have needed s = 6.
- **The Λ² side.** Route R's connecting rank for Λ²W is 0 at every class read, and its dual's is 8 to 10.
  - I(Λ²W) is k minus the dual rank. Both facts are sm:B1536's identities, which route R checks at every reading.
  - Three needs I(Λ²W) = −3, and the low-rank classes sit at −7 to −10.
- **The deck group and the mirror.** The ten X:S read one count, so the two τ-orbits of three-cusp sets agree, as the lifted
  mirror predicts. Galois-conjugate lines read alike.

## 4. Consequences (derived after the read-out from the sealed theorems and the readings)

**Corollary L″ (the floor on the low-rank classes of N₄₅).** At the trivial character, every interior class of N₄₅ of cup
rank one or two has I(W) = −1 exactly.
- On Z1 ∖ 0 every class has r = 1. By Lemma M, s ≥ 1. By semicontinuity, s ≤ the generic s, which the run reads as 1. So
  s = 1 and I(W) = −1.
- On the rank-2 part of Z2 the same argument gives s = 2.
- This uses the read generic values, so it holds at the two primes read. Both routes agree.

**N₄₅ at the trivial character, for three.** By Corollary L′, Lemma G‴ and sm:B1544, no class of N₄₅ reads I(W) = −3. The
golden cover is closed for three in this frame at the trivial character, at every class.

**What is left on N₄₅ below the floor.** With Theorem C (ii), I(W) = a − 1 + r − e and e ≤ 4:
- a class with I(W) = −2 needs a + r ≤ 3, so cup rank at most 3;
- ranks one and two read −1 or more (above);
- so only interior classes of cup rank exactly 3 could read −2 (two, not three). Proposition L's methods would map them, and
  this arc does not.

## 5. Where three can still live in this frame

- **Other characters ν of N₄₅**, and of other covers. sm:B1545's Lemma F at members puts three at a member only where 3 − b0
  cusps have ν trivial and the class vanishes there.
- **sm:B1538's puncture-character members.** Its read-out of 2026-10-04 found room for two (PROVED, scoped). Its records are
  being regenerated, and its four room-3 covers are closed by sm:B1545's Corollary G.
- **Other covers**, where the line leads by two (sm:B1543) or where the low-rank loci are larger. On N₄₅ the cup map on the
  low-rank classes is a symmetric matrix in disguise; whether that is a pattern of cyclic covers is open.
- Which class and which cover the genesis selects is GENESIS GAP4 and THE_BAR's question.

## Seen first

The repo sweep (twelve terms over every head, fetched 2026-10-06, 20:15Z; the seal's §0):
- "Veronese", "secant variety", "rank-one class" and "square of a class" are absent.
- "persymmetric" occurs only inside "supersymmetric".
- "cup rank" leads to this seat's own cup-map arcs.
- main's B1332 ("the cup product vanishes") is another object, an index at one cusp.

The literature read for this arc:
- Nosaka's twisted triple cup products (arXiv:1808.08532, abstract). Lemma M's trilinear form is of that kind.
- Monroe's branched bending (arXiv:2604.22004, abstract). H¹(N; ρ) is the space of bending deformations into SO(4, 1), and its
  interior classes are the cusp-preserving ones.
- Menal-Ferrer and Porti (arXiv:1001.2242), for the cusp-torus facts.

None states Proposition L or Lemma M. Standing: NEW-AS-SWEPT, extending sm:B1544.

## Disclosures

- **The design grew before the seal.** The first exploration found the ten eigen-lines by strata, and the plan was to read
  them and some pairs. Before any count, the structure work found Proposition L: the lines are ten points of a 7-dimensional
  family. The population became the families' generic classes, with the lines kept as named classes.
- **Read before the seal:** structure only, plus counts at banked classes (controls K3 and K6, in a trial at 20:16–20:18Z and
  for the record at 20:27:33–20:29:43Z).
- **The machine.** sm:B1538's Part F′ ran on three workers throughout, and this arc's run took the fourth.
- **The audit before the bank.** The run is its own audit: two routes that share no code, at two primes, three draws each,
  agreeing at all 132 readings. Proposition L was checked exactly in both routes.

## Files

- `PREREGISTRATION.md` (sealed; sha-256 in `docs/SEAL_LEDGER.md`), `ARTIFACT_HASHES.txt`.
- `verification/lowrank_lib.py`, `verification/prop_l.py`, `verification/run.py`, `verification/read_out.py`,
  `verification/controls.py`, `verification/identity.py`.
- `verification/controls.json`, `verification/identity.json`.
- `verification/run.jsonl.gz` with `verification/run_sha256.txt`.
- `verification/read_out.json`, `verification/read_out_log.txt`.
- The lock: `tests/test_b1546_the_low_rank_classes.py`. It re-derives the read-out from the gzipped record in memory.
