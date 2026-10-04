# B1541 — PREREGISTRATION: THE COUNT ON THE ROOM — the frame's counts (I(W), I(Λ²W)) at the classes of H¹(N₄₅; ρ), on the degree-45 cover of m003 where room for three first appears

**Sealed before `run.py` read any count except the one the banked rows fix.** At the seal this arc has computed only:
- **The cover and its supplies.** N₄₅ is the 5-fold cyclic cover of m003's degree-9 cover d9.2, along the order-5 character
  χ pulled back from m003's ℤ/5 torsion. It is connected, of degree 45, with 5 cusps. At its trivial character
  (n(1), n(ρ)) = (4, 18), so room = min(capW, capL2) = min(5, 18) = 5. These values are fixed by sm:B1536's banked rows and
  Lemma A, and were read directly in two routes (the golden covers dossier's §7, `gc_room_three_n45.py`; to be banked as
  sm:B1540).
- **The class space, as structure.** h¹(N₄₅; ρ) = 23 in both routes. The deck group ℤ/5 splits it into eigenspaces of
  dimensions 3, 5, 5, 5, 5, one for each character χʲ of d9.2 (Lemma A).
- **One count, fixed by the banked rows: (0, 0)** at the class pulled back from m003. sm:B1536's Part P counts at d9.2's five
  members (u, 0) are all (0, 0), and Shapiro adds them. It was read directly in both routes before the seal (§6, K4).
- **The controls** (§6): structure, the transport between the routes, and sm:B1536's own banked Part O readings at d10.4.

**Source.**
- The owner, 2026-10-04: "thanks, keep focused. three generations is smth we are after seripuslu"; "aleays verify, make sure
  we dont hit negatives because of bugs"; "make sure nothing is lost. make sure we dont abandon the golden pointer".
- The golden covers dossier's §7: room is not a count; the counts at the other classes of H¹(N₄₅; ρ) are the next question,
  sealed before any of them is read.

## 0. Seen first, and PRIOR ART:

**The repo sweep.** `git fetch --all` ran first (2026-10-04, 16:00Z). `scripts/checks/prior_work.py` then ran over every
head with twelve terms: "N_45", "degree-45", "degree 45", "room for three", "class strata", "isotypic", "deck group",
"generation-shaped", "torsion cover", "Z/5 torsion", "pulled-back class", "Part O".

| head | commit |
|---|---|
| this branch | `6fdf6d69` |
| main | `37bde38e` |
| the audit lane (fork) | `8b89d8fb` |
| the audit lane (physical bridge) | `8522a27a` |
| seat/determined-hopper | `7cda35aa` |
| seat/magical-wright | `0043be2b` |
| seat/outside-bench | `13d2c5b6` |
| seat/paper-review-verification | `5d58b935` |
| seat/physics-seat-evaluation | `659487bb` |
| sep16-branch | `3205984b` |
| art/camper-van-bar | `b3745696` |

"torsion cover" is absent everywhere. "N_45", "degree-45" and "degree 45" appear only in this seat's golden covers dossier
(§7, written today) and, as false matches, in a filename ("…_run_456.txt", B1375). The hits that bear on this arc:
- **This seat's sm:B1536** (the finite covers): its route N and route R, its Part P (the pulled-back class) and Part O (random
  classes in every cusp stratum, at members with room ≥ 2) are this arc's code paths, loaded by path and unchanged. Its banked
  rows fix N₄₅'s supplies and its pulled-back count. It reads no cover of degree above 12 except the Q₈ towers, and no class
  of N₄₅.
- **This seat's sm:B1535** (Theorem C, the cap) and **sm:B1515** (the frame): the counts are read in their frame. Theorem C
  bounds them here: I(Λ²W) ∈ [−18, 0] and I(W) ≥ −5.
- **The golden covers dossier's §6 and §7**: Lemma A and the finding of N₄₅.
- "isotypic", "deck group", "generation-shaped", "Z/5 torsion", "pulled-back class" and "Part O" are common in the record. The
  hits read do not read any class of a cover of degree above 12 in this frame.

**The literature.** No source read states counts of this frame (it is this program's construction). The two facts used are
banked in this repo: Shapiro's lemma with Mackey at the cusps (sm:B1536's Lemma S′, after sm:B1532's citation), and the
frame's identities (sm:B1535). The probability statement in §3 is proved there.

**Standing: EXTENDS.** sm:B1536's Part O is read for the first time on a cover with room above two, and the deck group's
eigenspaces are read as classes for the first time.

## 1. The question

On N₄₅, the first explicit finite cover of a golden state where sm:B1535's Theorem C does not exclude three generations,
which counts (I(W), I(Λ²W)) does the frame give at the classes of H¹(N₄₅; ρ)? Is any of them generation-shaped
(I(W) = I(Λ²W) ≠ 0), and is any of them three, (−3, −3)?

## 2. Definitions and conventions

- **The states and the frame** are sm:B1536's (§2 there): m003 = −LR on sm:B1527's presentation; ρ the four at the hyperbolic
  point; at the trivial character ν = 1, V_η = ρ, and a class c ∈ H¹(N; ρ) defines W_c = [[ρ, c], [0, 1]]. The count is
  (I(W), I(Λ²W)) with I(E) = n(E) − n(E*), read by sm:B1536's `reading` in route N and route R, with every identity checked.
- **Generation-shaped**: I(W) = I(Λ²W) ≠ 0. Three: (−3, −3). (k, −k) is anomalous, not generation-shaped (sm:B1536).
- **N₄₅** (`n45.build`): Γ = π₁(m003) acting on d9.2's points × ℤ/5, (x, k)^g = (x^g, k + e(x, g)), e the exponent of χ on the
  edge's Schreier generator. The deck transformation τ: (x, k) ↦ (x, k + 1).
- **Route N's classes**: cocycles of ρ ⊗ ℂ[X] on Γ (generator-major, then point, then coordinate), at p_N = 16775281.
  **Route R's**: values on N₄₅'s Schreier generators, at p_R = 2147482801 for its own classes, and at p_N for the transported
  ones.
- **The transport** (`n45.transport`): Shapiro's map, the block at the base point along each Schreier word. It carries route
  N's classes to route R's, so both routes read the same class at the same prime.
- **The cusp strata** (sm:B1536's Part O): for S a subset of the five cusps, the classes whose restriction to every cusp
  outside S is a coboundary. S = ∅ is the interior (dimension 18), S = all five is everything (dimension 23).
- **The eigenspaces**: τ acts on H¹ (route N by moving blocks, `deck_N`; route R by conjugation, `deck_R_matrix`); P_j projects
  onto the eigenvalue ζʲ, ζ a primitive 5th root of unity mod p. Each eigenspace has an interior part.

## 3. What is proved at design time

**Lemma A (the class space).** H¹(N₄₅; ρ) = ⊕_{j mod 5} H¹(d9.2; ρ ⊗ χʲ), of dimensions 3 + 4 · 5 (sm:B1536's banked
h¹ at d9.2 and the route R′ readings at χʲ), and τ acts on the j-th piece by ζʲ.
- *Proof.* Shapiro for the normal subgroup π₁(N₄₅) ⊂ π₁(d9.2) with quotient μ₅ (sm:B1536's Lemma S′ with ℂ[μ₅]). □

**Proposition P (one count fixed).** At the class pulled back from m003, the count on N₄₅ is the sum of the counts on d9.2 at
its five members (u, 0): every one is (0, 0) in sm:B1536's banked Part P, so the count is (0, 0).
- *Proof.* Shapiro splits W_c on N₄₅ into W_c ⊗ χᵏ on d9.2, compatibly with the cusps. On the 5-torsion ν⁵ = 1, so W at the
  member ν = χᵏ is χᵏ ⊗ W at the trivial character, and likewise Λ²W, with ν = χ^{3k} (2 · 3 ≡ 1 mod 5). □

**Lemma G (one count per subspace).** On a linear subspace of classes, the count is constant off a proper closed subset (the
connecting ranks drop only where minors vanish). A class drawn with uniform coefficients mod p lies in that subset with
probability at most δ/p, δ the largest degree of the minors involved.
- *Proof.* A nonzero polynomial of degree δ in r variables over GF(p) has at most δ p^{r−1} zeros (induction on r). □
- With p_N ≈ 1.7 · 10⁷ and δ well below 10³, a draw is generic with probability above 0.9999. P2 checks it.

**Theorem C's bounds** (sm:B1535), at ν = 1 on N₄₅: I(Λ²W) ∈ [−n(ρ), 0] = [−18, 0] and I(W) ≥ −(b0 + n(1)) = −5.

## 4. The instruments (`verification/`, written and checked before the seal)

- `n45.py`: the cover, τ, both routes' class spaces, `transport`, `deck_N`, `deck_R_matrix`, `project`. sm:B1536's route_n,
  route_r, cover_lib, gf and population are loaded by path, unchanged.
- `run.py`: the tasks of §5 on four workers, resumable, one row per reading (`run.jsonl`).
- `read_out.py`: the predictions of §7 from the rows, once; `evaluate` is pure.
- `controls.py`: K1–K6 (§6); `identity.py`: the banked identity (§8).

## 5. The population of classes (outcome-blind; seeds crc32 of "B1541|route|subspace|draw")

- **Part A, the cusp strata.** All 32 subsets S of the five cusps, three draws each. Route N draws its class at p_N and reads
  it; route R reads the same class through the transport at p_N; route R draws its own class at p_R and reads it.
- **Part B, the eigenspaces.** For j = 0..4, three draws in τ's eigenspace for ζʲ and three in its interior part: route N by
  `deck_N` at p_N, then transported; route R's own by `deck_R_matrix` at p_R.
- **Part C, the pulled-back class**, in both routes at their own primes.
- In all, 127 tasks and 380 readings: 42 subspaces × 3 draws × 3 readings, and 2 more for Part C.

## 6. Controls and disclosures (before the seal)

All hold (`verification/controls.json`):
- **K1.** N₄₅ is connected, of degree 45, with 5 cusps; τ commutes with Γ and has order 5. Its supplies are
  (n(1), n(ρ)) = (4, 18) in both routes, the value the banked rows fix.
- **K2.** h¹ = 23 in route N (p_N), route R (p_N) and route R (p_R). τ's eigenspaces have dimensions (3, 5, 5, 5, 5) in route
  N and in route R at p_R.
- **K3.** The transport sends cocycles to cocycles, has rank 23 on H¹, and carries `deck_N` to `deck_R` (τ to τ).
- **K4.** The pulled-back class: (0, 0), every identity holding, in route N, in route R, and in route R at p_N on route N's
  class transported.
- **K5.** sm:B1536's Part O code path reproduces its banked Part O readings at m003's d10.4, trivial character, in both
  routes, with its own seeds.
- **K6.** The read-out on synthetic rows, eight cases.

Disclosed:
- **What was read before the seal:**
  - N₄₅'s supplies (fixed by the banked rows) and its pulled-back count (0, 0) (fixed by the banked rows), both read
    directly as controls;
  - no other class of N₄₅.
- **A pre-seal slip, caught by K2's first trial.** Route R's own eigenspace projection multiplied int64 matrices at p_R
  (≈ 2³¹), and the products overflowed. K2 read eigenspace dimensions (27, 27, 27, 27, 27) and failed. The projection now
  uses route_r's modular product, and K2 holds. ERROR_LEDGER records it.
- **The arc numbers.** sm:B1539 (the own characters' census) has pre-seal instruments and is not sealed. sm:B1540 is reserved
  for N₄₅'s supplies as a proved arc.

## 7. Predictions (priors fixed at the seal)

| | prediction | prior |
|---|---|---|
| P1 | the transport: at every class of Parts A and B, route R at p_N reads route N's count, k and connecting ranks exactly | 97% |
| P2 | across primes: within every subspace, all draws in both routes give one count | 92% |
| P3 | every reading's identities hold (sm:B1536's and Theorem C's checks) | 97% |
| P4 | some class read has a generation-shaped count, in route N and route R at p_N | 20% |
| P5 | some class read has the count (−3, −3), in route N and route R at p_N | 7% |
| P6 | the pulled-back class reads (0, 0) in both routes (the run reproduces K4) | 99% |

A population-wide prediction is True only on complete records (every sealed task with exactly its readings); a refuting row
decides False whatever the coverage.

## 8. BANKED IDENTITY: checked before reading

`identity.py` re-runs K1–K6 and checks every sealed file's sha-256 (`ARTIFACT_HASHES.txt`) before `run.py` reads anything.
A single difference stops the run.

## 9. Reading rules

- **PROVED (three generations at a class of N₄₅)** if P1, P3 and P6 hold and P5 holds: a class of H¹(N₄₅; ρ) where the frame
  counts (−3, −3), read in two routes at the same class. It is a count at a class, not a selection: which class the genesis
  selects is GENESIS GAP4 and THE_BAR's question.
- **NEGATIVE (scoped)** if P1, P2, P3 and P6 hold and P4 is False on complete records: no generation-shaped count at the generic
  classes of the 42 subspaces read.
- **OPEN** otherwise. A generation-shaped count other than three is recorded and named.
- 0 of 19 stays 0 either way.

## 10. What this arc does not decide

- The special classes inside each subspace (its proper closed subsets, where the count can jump), and subspaces other than
  the 42 read.
- Other characters ν of N₄₅, and other covers with room for three.
- Which class, and which cover, the genesis selects (GENESIS GAP4, THE_BAR).
