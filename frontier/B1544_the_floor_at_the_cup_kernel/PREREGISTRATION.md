# B1544 — PREREGISTRATION: THE FLOOR AT THE CUP KERNEL — where three can live in sm:B1515's frame at the trivial character, and the counts there on N₄₅ and the four degree-60 covers

**Sealed before `run.py` read any count at a non-interior class of the cup map's kernel.** At the seal this arc has:
- **proved, at design time** (§3): Lemma F, I(W) ≥ k − m − 1 at every class, where m is the number of cusps and k the number
  where the class is non-zero. So the floor I(W) ≥ −1 (sm:B1543) holds at every class non-zero on every cusp, and a count
  with I(W) = −3 needs a class that vanishes on at least two cusps. With sm:B1535's Theorem C (ii) this places three
  (Corollary F′). It also gives Lemma G″: the counts at generic classes of the strata K0(S) decide the least I(W) on all of the
  cup map's kernel K0. And it gives Proposition D: on the four degree-60 covers three can live only in K0, at the strata named
  below, and on d10.16's and d10.40's covers nowhere.
- **computed structure only** (§6): K0, its strata and its closed supports, in two routes; the cusps; the deck group's
  action on them.
- **read counts only where the record has them banked**: the generic class of H¹ and the generic interior class on each cover
  (controls K3 and K6).

**Source.**
- The owner, 2026-10-04: "thanks, keep focused. three generations is smth we are after seripuslu"; "make sure nothing is lost.
  make sure we dont abandon the golden pointer".
- The owner, 2026-10-06: "we should verify all load bearing math even if a published paper, because we cant bet our whole
  project against some possible errors bugs or mistakes"; "breakthrough breaktheough breakthrough!!! is expected from you".
- sm:B1543's FINDINGS §2: the floor I(W) ≥ −b0 holds at every banked reading and is not proved. If it is a theorem, the frame
  counts at most one generation; proving it or breaking it is the next question.

## 0. Seen first, and PRIOR ART:

**The repo sweep.** `git fetch --all` ran first (2026-10-06). `scripts/checks/prior_work.py` then ran over every head with
twelve terms: "cup kernel", "kernel of the cup", "the floor", "dual term", "Massey", "secondary invariant", "triple product",
"Milnor invariant", "delta1_W(c) = 0", "c u y = 0", "I(W) >= -b0", "cup map vanishes".

| head | commit |
|---|---|
| this branch | `9bb4adf7` |
| main | `03635498` |
| the audit lane (fork) | `8b89d8fb` |
| the audit lane (physical bridge) | `c161981d` |
| the new web seat's branch (…/web-seat) | `2579ca01` |
| seat/outside-bench | `13d2c5b6` |
| seat/paper-review-verification | `5d58b935` |
| sep16-branch | `3205984b` |

What the sweep found:
- "cup kernel", "kernel of the cup", "delta1_W(c) = 0" and "Milnor invariant" are absent on every head. "c u y = 0" appears
  only in this arc's own uncommitted library.
- **The hits that bear on this arc are all this seat's.**
  - **sm:B1543** (the line must lead): the floor as an observation, its form r¹(W) ≤ h⁰(∂N; W*), and the remark that an
    excess of r¹(W) needs a secondary, Massey-type invariant of (c, y) at the cusps. It proves nothing about the floor.
  - **sm:B1542 and sm:B1541**: the banked counts on these covers. sm:B1542's interior classes of d10.13's and d10.36's covers
    lie in K0 and read (−1, −3), the floor met exactly.
  - **sm:B1535** (Theorem C) and **sm:B1515** (the frame).
  - **The kill graph's entry for sm:B1542**: it names, among the next places, sm:B1538's room-three members where
    n(ν ⊗ ρ) = 0 and the cup map vanishes at every class.
- **The other hits are other objects.**
  - "Massey": in the 16 findings on this branch that use the word, it names one of three things. None computes a Massey
    product of this frame.
    - Higher Massey products as obstructions to integrating a deformation of a representation: B265, B273, B274, B353,
      B370 and B575–B579.
    - Link invariants (Borromean triple linking): B142 and B143.
    - The arithmetic Chern–Simons level: B773.
  - "triple product": this seat's sm:B1510, sm:B1513, sm:B1514 and sm:B1530 use relative triple products of cohomology
    classes for couplings, such as the up-type 10′·10′·5′_H. They compute couplings, not counts, and none reads a class of K0.
    The other hits are other objects: B1251's sign convention, B293's Goldman bracket, B355's Bargmann invariants, and
    B1271's remark on three classes with a non-zero triple product on a closing.
  - "secondary invariant": papers/VALIDATION_LEDGER.md and the physical-bridge lane's flat-domain proof, other objects.
  - "dual term": sm:B1542's FINDINGS and its surfaces, and the audit lane's interface-sewing report (another object).
  - "the floor" is common and names other floors elsewhere.

**The literature.**
- A. Putman, "Half lives, half dies and the signatures of boundaries" (note). The half-lives theorem: the restriction images of
  H¹(N; E) and H¹(N; E*) in H¹(∂N) are mutual annihilators. Used here for the trivial line (r¹(ℂ) = m). Its twisted form is
  checked by route R at every reading.
- P. Menal-Ferrer and J. Porti, "Twisted cohomology for hyperbolic three manifolds", arXiv:1001.2242 (read §0 and §3.1).
  - They compute the cusp-torus cohomology of the holomorphic representations Vₙ: h⁰ = h² = 1 per cusp (for the positive
    lift) and h¹ = 2.
  - They prove that H¹(M; Vₙ) injects into the boundary. There are no interior classes for those representations.
  - This frame's four is ρ = V₂ ⊗ V̄₂, which they do not treat, and it has interior classes (n(ρ) = 3, 7, 18 here). Its
    cusp-torus facts are proved in §3 directly and checked numerically at every reading.
- S. Garoufalidis and J. Levine, "Tree-level invariants of three-manifolds, Massey products and the Johnson homomorphism"
  (2003), §1.1 and §2.2. Massey products on H¹ of 3-manifolds are the first invariants beyond cup products. The invariant on
  which the floor rests at a class of K0 is of that kind, with twisted coefficients and a boundary. This arc does not compute
  it. It reads its effect on the count.

**Standing: EXTENDS.** sm:B1543's floor is proved where the class is non-zero on every cusp (Lemma F). On K0 it is read
everywhere else, by strata, on N₄₅ and the four degree-60 covers.

## 1. The question

On sm:B1541's N₄₅ and sm:B1542's four degree-60 covers, at the trivial character, what is the least I(W) over the classes of
the cup map's kernel K0? Is it below −1 anywhere, so that the floor fails? Is three, (−3, −3), read at a class of K0? And on
the room-3 covers, where Proposition D puts every possible three inside K0: is there any class that reads three?

## 2. Definitions and conventions

- **The frame** is sm:B1536's at the trivial character (§2 there): V = ρ, the four at the hyperbolic point, L = ℂ. A class
  c ≠ 0 of H¹(N; ρ) defines W = [[ρ, c], [0, 1]]. The count is (I(W), I(Λ²W)), with I(E) = n(E) − n(E*), where n is the
  interior supply.
- **The cup map** δ¹_W(c) : H¹(N; ℂ) → H²(N; ρ), y ↦ c ∪ y, is the connecting map of 0 → ρ → W → ℂ → 0. It is linear in c.
  **K0** = {c : δ¹_W(c) = 0}.
- **The cusps.** N has m cusps. Both routes read a cusp as an orbit of the base cusp group on the cover's points, and label it
  by the least point of its orbit. The orbits coincide as point sets (K5).
  - c_T is c's restriction to the cusp T. The **support** of c is the set of cusps where c_T ≠ 0 in H¹(T; ρ), and k is its
    size (route R's k).
  - a = dim(⟨c_T⟩ ∩ Λ(ρ)), where ⟨c_T⟩ is spanned by the c_T, each in its cusp's slot, and Λ(ρ) is the restriction image of
    H¹(N; ρ) in H¹(∂N; ρ). So a ≥ 1 when c is not interior: c|∂N ≠ 0 lies in both.
- **The strata of K0.** For a set S of cusps, K0(S) is the part of K0 whose restriction to every cusp outside S is a
  coboundary. S is a **closed support** when K0(S) is non-zero on every cusp of S. Every class of K0 lies in K0(S_c) for its
  own support S_c, which is closed.
- **The routes.**
  - **Route F**: sm:B1541's `route_f.py` on the lifted 2-complex of ⟨a, t | ttATAAATA⟩, at p_F = 67108201. It uses numpy and
    the standard library only.
  - **Route R**: sm:B1536's `route_r.py` on the cover's own Reidemeister–Schreier presentation (through sm:B1542's `ncyc.py`
    and sm:B1541's `n45.py`), at p_R = 2147482801.
  - The two routes share no code. Each computes its own K0, its own strata and its own classes.

## 3. What is proved at design time

**Lemma F (the floor away from the vanishing cusps).** Let N be a finite cover of a complete finite-volume hyperbolic
3-manifold, with m cusps, at the trivial character. Then every class c ≠ 0 of H¹(N; ρ) has I(W) ≥ k − m − 1.

*Proof.*
- **(1) The identity.** sm:B1527's Lemma E in route R's form, checked at every banked reading:
  I(E) = h⁰(N; E) − h⁰(N; E*) + h⁰(∂N; E*) − r¹(E), where r¹ is the rank of H¹(N; E) → H¹(∂N; E). For E = W:
  - h⁰(N; W) = 0, since H⁰(N; ρ) = 0 and the connecting map sends 1 to c ≠ 0;
  - h⁰(N; W*) = 1, since H⁰(N; ℂ) injects and H⁰(N; ρ*) = 0.
  So I(W) = −1 + h⁰(∂N; W*) − r¹(W).
- **(2) h⁰(T; W*) = 2 at every cusp T, whatever c is.**
  - The cusp group is conjugate to ⟨g₁, g₂⟩ with gᵢ = [[1, zᵢ], [0, 1]] and z₂/z₁ ∉ ℝ, up to signs that ρ does not see. On
    ρ ⊗ ℂ = M₂(ℂ), g acts by X ↦ g X ḡᵀ, and (g − 1)X = [[z x₂₁ + z̄ x₁₂ + |z|² x₂₂, z x₂₂], [z̄ x₂₂, 0]].
  - The invariant functionals form the line spanned by φ(X) = x₂₂.
  - A functional (φ′, s) on W = ρ ⊕ ℂ is invariant iff φ′ is invariant and φ′(c(g)) = 0 on the cusp group.
  - For a cocycle c, the condition (g₁ − 1)c(g₂) = (g₂ − 1)c(g₁), read in its (1, 2) and (2, 1) entries, gives
    z₁ x⁽²⁾ = z₂ x⁽¹⁾ and z̄₁ x⁽²⁾ = z̄₂ x⁽¹⁾, with x⁽ⁱ⁾ = c(gᵢ)₂₂. Since z₂/z₁ is not real, x⁽¹⁾ = x⁽²⁾ = 0, so φ∘c = 0.
  - Hence H⁰(T; W*) is the line's functional plus the invariant functionals of ρ, of dimension 2, and h⁰(∂N; W*) = 2m.
- **(3) r¹(W) ≤ 3m − k.**
  - π : H¹(∂N; W) → H¹(∂N; ℂ) sends the image Λ(W) of H¹(N; W) into the image Λ(ℂ) of H¹(N; ℂ), which has dimension m by
    half lives.
  - The kernel of π is the image of H¹(∂N; ρ), namely H¹(∂N; ρ)/δ⁰_∂H⁰(∂N; ℂ), where δ⁰_∂ sends the constant on T to c_T. Its
    dimension is 2m − k: on a torus h¹(T; ρ) = h⁰(T; ρ) + h⁰(T; ρ*) = 2 (Euler characteristic and duality), and δ⁰_∂ has
    rank k.
  - So r¹(W) ≤ m + (2m − k).
- (1)–(3) give I(W) ≥ −1 + 2m − (3m − k). □

So **the floor holds at every class non-zero on every cusp** (k = m), and **a class with I(W) = −g vanishes on at least g − 1
cusps**.

**Corollary F′ (where three can live, at the trivial character).** A class with I(W) = −g has:
- a + rk δ¹_W ≤ n(1) + 1 − g, from Theorem C (ii), I(W) = a − 1 + rk δ¹_W − dim(im δ¹_{W*} ∩ K_L), whose last term is at most
  n(1);
- k ≤ m + 1 − g, from Lemma F.

For three: a + rk δ¹_W ≤ n(1) − 2 and k ≤ m − 2.

**Lemma G″ (the strata decide K0).** At c ∈ K0, route R's identity I(W) = −1 + k + rk δ¹_W − rk δ¹_{W*} reads
I(W) = −1 + k − rk δ¹_{W*}.
- For a closed support S, the classes of K0(S) with support exactly S form a dense open subset: the complement of the proper
  subspaces K0(S ∖ {T}). There k = |S|.
- The map δ¹_{W*}(c), z ↦ c ∪ z, is linear in c, so its rank takes its largest value on a dense open subset.
- So a generic class of K0(S) has the least I(W) among the classes of K0 with support S.
- Every class of K0 has a closed support. So the generic counts over the closed supports give the least I(W) on all of K0. □

The generic draw is Lemma G's (sm:B1542 §3): a uniform draw misses the closed exceptional set with probability above 1 − δ/p.
Each subspace is drawn three times in each route, at two primes.

**Proposition D (the four degree-60 covers).** It uses the structure K1 reads and sm:B1542's banked readings (re-read in K3
and in the run, S = ∅).
- **(a) d10.13's and d10.36's covers** (m = 6, n(1) = 3). The interior part (dimension 3 = n(ρ)) lies in K0.
  - Its generic class reads (−1, −3) with rk δ¹_{W*} = 0. δ¹_{W*}(c) is linear in c, so its rank at any interior class is at
    most the generic rank, 0. With rk δ¹_W = 0 and k = 0, route R's identity gives I(W) = −1 at every interior class.
  - By Corollary F′, a class with I(W) = −3 is not interior, has a = 1 and rk δ¹_W = 0, and k ≤ 4. So it lies in K0(S) for a
    closed support S with 1 ≤ |S| ≤ 4.
  - The closed supports (K1) are ∅, three sets of four cusps, and all six. So **three at the trivial character on these covers
    can only be at the classes of K0(S) for the three supports of size four**, and the run decides it (Lemma G″).
- **(b) d10.16's and d10.40's covers** (m = 4, n(1) = 3). **No class reads I(W) = −3.**
  - A non-interior class would lie in K0 with k ≤ 2. The closed supports are ∅ and all four, so it would be interior.
  - At an interior class, a = k = 0 and the term dim(im δ¹_{W*} ∩ K_L) is rk δ¹_{W*}(c). Three would need rk δ¹_W ≤ 1 and
    rk δ¹_{W*} = rk δ¹_W + 2.
  - The generic interior class reads (0, −5) with rk δ¹_W = 3 and rk δ¹_{W*} = 2. By linearity rk δ¹_{W*} ≤ 2 on the
    interior, which forces rk δ¹_W = 0, that is c ∈ K0 ∩ interior.
  - The generic class of K0 ∩ interior (the deck group's ζ⁰ interior part) reads (−1, −3) with rk δ¹_{W*} = 0. By linearity
    rk δ¹_{W*} = 0 on all of it, and the class cannot read three. □

**N₄₅** (m = 5, n(1) = 4). In K0, three can only be at the ten 1-dimensional K0(S) with |S| = 3, which the run reads.
Corollary F′ also leaves classes outside K0, with a + rk δ¹_W ≤ 2 and k ≤ 3. Those are not read here (§10).

## 4. The instruments (`verification/`, written and checked before the seal)

- `floor_lib.py`: both routes.
  - For each route: the cup map by the cochain formula, K0, the cusp labels, the strata K0(S), the closed supports, a class's
    support, and Lemma F's ingredients.
  - Route F reads h⁰(T; W) and h⁰(T; W*) from its own cusp transports. Route R reads them from sm:B1536's Coh.
  - It loads sm:B1541's route_f.py and n45.py and sm:B1542's ncyc.py by path, unchanged.
- `run.py`: the tasks of §5 on two workers, resumable, one row per reading (`run.jsonl`). The closed supports are sealed in
  `run.STRUCTURE`.
- `read_out.py`: the predictions of §7 from the rows, once. `evaluate` is pure.
- `controls.py`: K1–K6 (§6). `identity.py`: the banked identity (§8).

## 5. The population of classes (outcome-blind; seeds crc32 of "B1544|cover|route|subspace|draw")

For every closed support S of K0 on each cover, three generic draws of K0(S) in route F and three in route R, each route
drawing its own classes:

| cover | m | closed supports S (dim K0(S)) | subspaces |
|---|---|---|---|
| N₄₅ | 5 | the ten sets of three cusps (1 each), the five sets of four (3 each), all five (5) | 16 |
| d10.13's | 6 | ∅ (3); {0, 1, 3, 5} (4); {0, 1, 7, 13} (4); {3, 5, 7, 13} (5); all six (6) | 5 |
| d10.36's | 6 | ∅ (3); {0, 1, 2, 7} (4); {0, 2, 3, 8} (4); {1, 3, 7, 8} (5); all six (6) | 5 |
| d10.16's | 4 | ∅ (2); all four (3) | 2 |
| d10.40's | 4 | ∅ (2); all four (3) | 2 |

In all, 30 subspaces, 90 tasks and 180 readings.
- Lemma F fixes the floor on the full supports. So the informative subspaces are N₄₅'s fifteen proper supports and the room-3
  covers' three supports of size four each.
- The interior parts (S = ∅) are sm:B1542's banked subspaces, re-read.
- The full supports are Lemma F's check.

The deck group τ permutes the cusps (K1):
- N₄₅: a 5-cycle, 0 → 1 → 4 → 2 → 5 → 0;
- d10.13's: (0 1)(3 13)(5 7);
- d10.36's: (0 2)(1 8)(3 7);
- d10.16's: (2 4);
- d10.40's: (1 3).

τ is an automorphism of the cover that preserves the frame, so supports that τ carries into one another read one count. P1
checks this. On N₄₅ the ten sets of three form two τ-orbits.

## 6. Controls and disclosures (before the seal)

All hold (`verification/controls.json`; this design's controls ran 17:48–17:55Z on 2026-10-06):
- **K1.** Structure in both routes on all five covers equals the sealed values: h¹(ρ), n(ρ), h¹(ℂ), n(1), dim K0, K0 ∩
  interior, K0 over the eigenspaces, the cusp labels, τ on the cusps, and the closed supports with dim K0(S).
- **K2.** The cochain formula for the cup map equals the long exact sequence's rank, h¹(V) + h¹(L) − h¹(W) − 1, at three random
  classes and at a class of K0 (both 0 there), in both routes on every cover.
- **K3.** A generic interior class reads the banked count in both routes: (4, −10) on N₄₅, (−1, −3) on d10.13's and d10.36's
  covers, (0, −5) on d10.16's and d10.40's.
- **K4.** The read-out on synthetic rows, ten cases. They cover every prediction's refutation, the τ-orbit check, the support
  check, Lemma F's check, incomplete records and the three verdicts.
- **K5.** Route F's and route R's cusps coincide as point sets, and their deck transformations are the same permutation.
- **K6.** Lemma F's ingredients at a generic class of H¹ and at K3's interior class, in both routes on every cover:
  h⁰(∂N; W*) = 2m, h¹(∂N; W) = 4m − k, r¹(W) ≤ 3m − k, I(W) = −1 + h⁰(∂N; W*) − r¹(W) ≥ k − m − 1. The generic class reads
  the banked count of the full cusp stratum: (5, −5) on N₄₅, (2, −3) on d10.13's and d10.36's covers, (3, −4) on d10.16's and
  d10.40's.

### 6a. The load-bearing inputs (WORKING_RULES 2026-10-06), each re-derived by own code on every instance used

| | input | source | own check |
|---|---|---|---|
| LB1 | Theorem C (ii) and route R's identities | sm:B1535 (the audit lane's R84 reviewed it), sm:B1536 | P3: route R's checks at every reading |
| LB2 | Lemma F and its torus facts | §3 (proved here) | K6, and P3: the ingredients in both routes at every reading |
| LB3 | K0, its strata and closed supports | §3; computed | K1: two routes at two primes; P2: every reading's support is its S |
| LB4 | the banked interior counts that Proposition D uses | sm:B1542 | K3 and the run's S = ∅ readings |
| LB5 | Lemma G″ (the strata decide K0) | §3 | P1 and P2: three draws per route, two routes, two primes |
| LB6 | the cusps are the same in both routes | the covers' permutation data | K5 |
| LB7 | the code paths are the banked ones | sm:B1541, sm:B1542, sm:B1536 | K3 and K6: banked counts reproduced in both routes |

A reading that a check here does not cover is not used by the verdict.

Disclosed:
- **What was read before the seal.**
  - Structure only: dimensions, K0's strata and closed supports, the cusps' orbits, τ on the cusps. All in two routes, in
    scratch scripts and then in the controls.
  - Counts only at classes whose counts are banked: the generic class of H¹ and the generic interior class of each cover (K3,
    K6, and a scratch test on d10.13's cover that read (2, −3) and (−1, −3)).
  - No count at a non-interior class of K0.
- **The first design, replaced before the seal.** It read generic classes of K0 and of its eigen-parts.
  - Its controls ran twice: 17:17–17:21Z, stopped at K4 by the slip below, and 17:23–17:28Z, all holding. Neither read a count
    at a class of K0 beyond K3's interior classes, which are banked.
  - As the second finished, Lemma F was found. Generic classes of K0, and of its eigen-parts, are non-zero on every cusp (K0 lies
    in no proper stratum, and τ permutes the cusps). So Lemma F fixes the floor there, and that design could neither break the
    floor nor find three.
  - The design was replaced by the strata of §5. This is a change of population before any reading, made because of a proof.
- **A slip, caught by the first trial.** controls.py's bare `import read_out` found sm:B1536's read_out.py, which sm:B1536's
  population.py puts first on sys.path. It is E12 again: sm:B1536's own addendum records the same failure. Every module of this
  arc is now loaded by path under its own name (ERROR_LEDGER).

## 7. Predictions (priors fixed at the seal)

| | prediction | prior |
|---|---|---|
| P1 | one count per subspace (three draws in each route, two routes); supports related by τ read one count | 95% |
| P2 | every reading's class lies in K0 (rk δ¹_W = 0) and has support exactly S | 96% |
| P3 | route R's identities at every reading; Lemma F's ingredients in both routes at every reading | 95% |
| P4 | the floor on K0: I(W) ≥ −1 at every reading | 70% |
| P5 | some subspace reads a generation-shaped count, I(W) = I(Λ²W) ≠ 0, in both routes | 8% |
| P6 | some subspace reads (−3, −3) in both routes | 4% |

A population-wide prediction is True only on complete records (every sealed task with both readings). A refuting row decides
False whatever the coverage.

## 8. BANKED IDENTITY: checked before reading

`identity.py` re-runs K1–K6 and checks every sealed file's sha-256 (`ARTIFACT_HASHES.txt`) before `run.py` reads anything.
A single difference stops the run.

## 9. Reading rules

- **PROVED (the floor fails on K0)** if P1, P2 and P3 hold and P4 is False: a stratum of K0 whose generic class reads
  I(W) < −1 in two routes.
  - If P6 holds too, three, (−3, −3), is read at a class of K0. It is a count at a class, not a selection. Which class and
    which cover the genesis selects is GENESIS GAP4 and THE_BAR's question.
- **NEGATIVE** if P1, P2 and P3 hold and P4 holds on complete records. The floor then holds on all of K0 on the five covers
  (Lemma G″). With Proposition D, no class of the four degree-60 covers reads I(W) = −3 at the trivial character, so they carry
  no three in this frame there.
- **OPEN** otherwise.
- Either way the read-out records:
  - the least I(W) on K0 per cover;
  - every generation-shaped subspace, named;
  - on the room-3 covers, the counts at the three supports of size four.
- 0 of 19 stays 0 either way.
- **The audit before the bank** (NO NEGATIVE FROM A BUG, and the rule of 2026-10-06). The run is its own audit: every count is
  read in two routes that share no code, at two primes. In addition:
  - before a PROVED verdict is banked, route F re-reads one generic class of every subspace below the floor at its next two
    primes;
  - a disagreement withholds the verdict and goes to ERROR_LEDGER first.

## 10. What this arc does not decide

- **N₄₅'s classes outside K0** with rk δ¹_W ∈ {1, 2} and small support. Corollary F′ leaves them as the other places three
  could be on N₄₅. The rank loci of the cup map are not computed here.
- **Other characters ν** of these covers, and other covers. One of them is sm:B1538's room-three members of the silver pair,
  where n(ν ⊗ ρ) = 0 makes every class a class of K0. Lemma F is proved at the trivial character only. At a member ν the
  cusps where ν is non-trivial change its terms.
- **The floor outside K0.** Lemma F covers the classes non-zero on every cusp. The rest of H¹ is not read here.
- **Which class and which cover the genesis selects** (GENESIS GAP4, THE_BAR).
