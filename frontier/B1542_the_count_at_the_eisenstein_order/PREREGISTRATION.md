# B1542 — PREREGISTRATION: THE COUNT AT THE EISENSTEIN ORDER — the frame's counts (I(W), I(Λ²W)) at the classes of H¹(N; ρ), on the four degree-60 covers of m003 with room 3 and 4

**Sealed before `run.py` read any count on a degree-60 cover.** At the seal this arc has computed only:
- **The covers and their supplies.** Each cover N is the 6-fold cyclic cover of one of m003's degree-10 covers d10.13, d10.16,
  d10.36 and d10.40, along the order-6 character ψ = (u, κ) = ((0, 0), 1/6) of m003 restricted to it (the fibre direction).
  Each N is the fibre product of the degree-10 cover with m003's 6-fold cyclic cover along the fibration, of degree 60. At the
  trivial character, sm:B1540 (`room_60.json`) read:
  - on d10.13's and d10.36's covers, 6 cusps and (n(1), n(ρ)) = (3, 3), so room = min(capW, capL2) = min(4, 3) = 3;
  - on d10.16's and d10.40's covers, 4 cusps and (n(1), n(ρ)) = (3, 7), so room = min(4, 7) = 4.
  The six degree-60 covers of sm:B1540 fall into four conjugacy classes, {d10.13, d10.14}, {d10.16}, {d10.36, d10.38} and
  {d10.40}. This arc reads one cover of each class.
- **The class spaces, as structure** (§3, K2):
  - h¹(N; ρ) = 9 on d10.13's and d10.36's covers, split over the deck group's eigenvalues ζ⁰ and ζ³ as 5 + 4, with interior
    parts 2 + 1;
  - h¹(N; ρ) = 11 on d10.16's and d10.40's covers, split over ζ⁰, ζ², ζ³ and ζ⁴ as 5 + 2 + 2 + 2, with interior parts
    2 + 2 + 1 + 2.
  Both readings hold in two routes.
- **The controls** (§6): structure, the transport between the routes, the generalized library against sm:B1541's banked N₄₅,
  sm:B1536's banked Part O readings at d10.4, and the identification of the state's group with the census manifold m003.

**Source.**
- The owner, 2026-10-04: "thanks, keep focused. three generations is smth we are after seripuslu"; "make sure nothing is lost.
  make sure we dont abandon the golden pointer".
- The owner, 2026-10-06: "we should verify all load bearing math even if a published paper, because we cant bet our whole
  project against some possible errors bugs or mistakes" (WORKING_RULES, the rule of that date; §6a below is its first
  application); "breakthrough breaktheough breakthrough!!! is expected from you".
- sm:B1540's FINDINGS: room is not a count; the degree-60 covers' counts are the next sealed question after sm:B1541's N₄₅.

## 0. Seen first, and PRIOR ART:

**The repo sweep.** `git fetch --all` ran first (2026-10-06, 12:27Z). `scripts/checks/prior_work.py` then ran over every
head with twelve terms: "degree-60", "degree 60", "Eisenstein order", "order-6 character", "fibre direction", "6-fold
cyclic", "d10.13", "d10.16", "d10.36", "d10.40", "room for three", "generation-shaped".

| head | commit |
|---|---|
| this branch | `5869a056` |
| main | `88ed6981` |
| the audit lane (fork) | `8b89d8fb` |
| the audit lane (physical bridge) | `c161981d` |
| seat/outside-bench | `13d2c5b6` |
| seat/paper-review-verification | `5d58b935` |
| sep16-branch | `3205984b` |

The hits that bear on this arc are all this seat's:
- **sm:B1540** (the room for three): it found these covers and read their supplies in two routes (`room_60.json`). It reads
  no class of them.
- **sm:B1541** (the count on the room, sealed): its library and run are this arc's, generalized from order 5 to order k. Its
  read-out has not run at this seal, so its outcome is unknown here.
- **sm:B1536** (the finite covers): its route N, route R and Part O are this arc's code paths, loaded by path and unchanged. Its
  banked rows fix the degree-10 covers' supplies. It reads no cover of degree above 12 except the Q₈ towers.
- **sm:B1535** (Theorem C, the cap) and **sm:B1515** (the frame): the counts are read in their frame. Theorem C bounds them here:
  I(Λ²W) ∈ [−n(ρ), 0], so [−3, 0] or [−7, 0], and I(W) ≥ −(b0 + n(1)) = −4.
- **sm:B1378 and its notes** (the M₆ deck triplet, a "6-fold cyclic" hit): on M₆, m004's 6-fold cyclic cover along the
  fibration, an earlier frame (main's index on a non-semisimple background, B1374/B1375) gives a three-generation-shaped index
  (−3)⁶, fenced there as "index ≠ physical generation count". Its three is a deck orbit, Shapiro plus Mackey (sm:B1384), and it
  descends to s961 (sm:B1506). In this arc's frame, sm:B1536 found no interior class of the four on m004's levels M₂–M₆ at the
  trivial character, so their room there is 0. The idea that three can come as a sum over a deck group's characters is
  Lemma A's here; this arc reads the counts directly and does not assume it.
- The other hits are other objects:
  - "degree 60": sm:B1536's untested icosian A₅ covers, and the golden covers dossier's twelve congruence covers;
  - "Eisenstein order": an order-3 rotation in B302;
  - "order-6 character": other groups' characters (B1068, B1418, the referee rounds);
  - "6-fold cyclic": the closed branched cover Y₆ (B1278);
  - "fibre direction": sm:B1538's covers M_{D,w} of the silver pair.
  "generation-shaped" is common in the record, and the hits read do not read a class of a cover of degree above 12 in this
  frame.

**The literature.** No source read states counts of this frame (it is this program's construction). The facts used are banked
in this repo and re-derived here by own code on every instance used (§6a): Shapiro's lemma with Mackey at the cusps (sm:B1536's
Lemma S′, after sm:B1532's citation), and the frame's identities (sm:B1535).

**Standing: EXTENDS.** sm:B1541's design is read on covers of a second order (6, the Eisenstein order), where the deck group's
eigenspaces include a real one (ζ³ = −1).

## 1. The question

On the four degree-60 covers of m003 that are the Eisenstein order's room for three and four, which counts (I(W), I(Λ²W)) does
the frame give at the classes of H¹(N; ρ)? Is any of them generation-shaped (I(W) = I(Λ²W) ≠ 0), and is any of them three,
(−3, −3)?

## 2. Definitions and conventions

- **The states and the frame** are sm:B1536's (§2 there): m003 = −LR on sm:B1527's presentation; ρ the four at the hyperbolic
  point; at the trivial character ν = 1, V_η = ρ, and a class c ∈ H¹(N; ρ) defines W_c = [[ρ, c], [0, 1]]. The count is
  (I(W), I(Λ²W)) with I(E) = n(E) − n(E*), read by sm:B1536's `reading` in route N and route R, with every identity checked.
- **Generation-shaped**: I(W) = I(Λ²W) ≠ 0. Three: (−3, −3). (k, −k) is anomalous, not generation-shaped (sm:B1536).
- **The cover N** (`ncyc.build("m003", cid, (0, 0), 1/6, 6)`): Γ = π₁(m003) acting on the degree-10 cover's points × ℤ/6,
  (x, i)^g = (x^g, i + e(x, g)), e the exponent of ψ on the edge's Schreier generator. The deck transformation τ:
  (x, i) ↦ (x, i + 1).
- **Route N's classes**: cocycles of ρ ⊗ ℂ[X] on Γ (generator-major, then point, then coordinate), at p_N = 16775281.
  **Route R's**: values on N's Schreier generators, at p_R = 2147482801 for its own classes, and at p_N for the transported
  ones.
- **The transport** (`ncyc.transport`): Shapiro's map, the block at the base point along each Schreier word. It carries route
  N's classes to route R's, so both routes read the same class at the same prime.
- **The cusp strata** (sm:B1536's Part O): for S a subset of N's cusps, the classes whose restriction to every cusp outside S is
  a coboundary. S = ∅ is the interior (dimension n(ρ): 3 or 7), S = all cusps is everything (9 or 11).
- **The eigenspaces**: τ acts on H¹ (route N by moving blocks, `deck_N`; route R by conjugation, `deck_R_matrix`); P_j projects
  onto the eigenvalue ζʲ, ζ a primitive 6th root of unity mod p (`ncyc.zeta`, its order checked at 2 and 3). Each eigenspace
  has an interior part.

## 3. What is proved at design time

**Lemma A (the class space).** H¹(N; ρ) = ⊕_{j mod 6} H¹(d10.x; ρ ⊗ ψʲ), and τ acts on the j-th piece by ζʲ.
- *Proof.* Shapiro for the normal subgroup π₁(N) ⊂ π₁(d10.x) with quotient μ₆ (sm:B1536's Lemma S′ with ℂ[μ₆]). □
- K2 reads the dimensions directly in two routes: [5, 0, 0, 4, 0, 0] on d10.13's and d10.36's covers, and
  [5, 0, 2, 2, 2, 0] on d10.16's and d10.40's. The pieces at ζ¹ and ζ⁵ are zero on all four, so they are not read. Every
  non-zero piece is read.

**Lemma G (one count per subspace).** On a linear subspace of classes, the count is constant off a proper closed subset (the
connecting ranks drop only where minors vanish). A class drawn with uniform coefficients mod p lies in that subset with
probability at most δ/p, δ the largest degree of the minors involved.
- *Proof.* A nonzero polynomial of degree δ in r variables over GF(p) has at most δ p^{r−1} zeros (induction on r). □
- With p_N ≈ 1.7 · 10⁷ and δ well below 10³, a draw is generic with probability above 0.9999. P2 checks it.

**Theorem C's bounds** (sm:B1535), at ν = 1 on N: I(Λ²W) ∈ [−n(ρ), 0] and I(W) ≥ −(b0 + n(1)) = −4. On d10.13's and d10.36's
covers, I(Λ²W) ∈ [−3, 0], so (−3, −3) needs the bound to be met exactly. On d10.16's and d10.40's, I(Λ²W) ∈ [−7, 0].

**Why the class pulled back from m003 is not fixed here.** The frame's W at a member ν is [[ν ⊗ ρ, c·ν⁻⁴], [0, ν⁻⁴]] (sm:B1536
§2). The twist of the trivial character's W_c = [[ρ, c], [0, 1]] by a character μ is [[μ ⊗ ρ, μc], [0, μ]]. That is the frame's
W at a member only if μ = ν = ν⁻⁴, that is μ⁵ = 1. On N₄₅ (sm:B1541) the twists have order 5, so they are frame members of d9.2
and the banked rows fixed the count. Here ψʲ has order 1, 6, 3, 2, 3 or 6, so only the j = 0 piece is a frame member. The
banked rows do not fix the count, and P6 asks only that both routes read one count.

## 4. The instruments (`verification/`, written and checked before the seal)

- `ncyc.py`: the cover, τ, both routes' class spaces, `transport`, `deck_N`, `deck_R_matrix`, `zeta`, `project`. It is
  sm:B1541's `n45.py` with the cover, the character and the order as arguments. sm:B1536's route_n, route_r, cover_lib, gf and
  population are loaded by path, unchanged.
- `run.py`: the tasks of §5 on four workers, resumable, one row per reading (`run.jsonl`).
- `read_out.py`: the predictions of §7 from the rows, once; `evaluate` is pure.
- `controls.py`: K1–K7 (§6); `identity.py`: the banked identity (§8).

## 5. The population of classes (outcome-blind; seeds crc32 of "B1542|cover|route|subspace|draw")

On each of the four covers:
- **Part A, the cusp strata.** Every subset S of N's cusps, three draws each: 64 subsets on d10.13's and d10.36's covers (6
  cusps), 16 on d10.16's and d10.40's (4 cusps). Route N draws its class at p_N and reads it; route R reads the same class
  through the transport at p_N; route R draws its own class at p_R and reads it.
- **Part B, the eigenspaces.** For every j with a non-zero eigenspace (j = 0, 3; or j = 0, 2, 3, 4), three draws in τ's
  eigenspace for ζʲ and three in its interior part. Route N works by `deck_N` at p_N, then transports; route R's own classes
  use `deck_R_matrix` at p_R.
- **Part C, the class pulled back from m003**, in both routes at their own primes.

In all, 556 tasks and 1,664 readings:
- 205 tasks on each of d10.13's and d10.36's covers: 68 subspaces × 3 draws, plus Part C;
- 73 on each of d10.16's and d10.40's: 24 × 3, plus Part C.

## 6. Controls and disclosures (before the seal)

All hold (`verification/controls.json`):
- **K1.** Each cover is connected, of degree 60, with its cusps. It is the cover sm:B1540 read: its canonical form equals that
  of sm:B1540's `room_lib.cyclic_cover` along the banked own character. At the trivial character, route N and route R give
  `room_60.json`'s primes, (n(1), n(ρ)) and caps.
- **K2.** h¹, τ's eigenspaces and their interior parts, in route N (p_N; route R at p_N gives the same h¹) and in route R at
  p_R, equal the values in §3. Their support is the sealed list of subspaces (`run.STRUCTURE`), and the interior parts sum to
  n(ρ).
- **K3.** On each cover the transport sends cocycles to cocycles, has rank h¹ on H¹, and carries `deck_N` to `deck_R` (τ to τ).
- **K4.** The generalized library at order 5 rebuilds sm:B1541's N₄₅: the same canonical cover, h¹ = 23, and eigenspaces
  (3, 5, 5, 5, 5) in both routes, as sm:B1541's banked K2. The class pulled back from m003 reads (0, 0), with every identity,
  in route N, in route R, and in route R at p_N transported, as sm:B1541's banked K4.
- **K5.** sm:B1536's Part O code path reproduces its banked Part O readings at m003's d10.4, trivial character, in both routes,
  with its own seeds.
- **K6.** The read-out on synthetic rows, fifteen cases. They cover every prediction's True, False and None cases where it has
  them, and the three verdicts.
- **K7.** The state's group is the census manifold m003's. For every index n ≤ 7, the run's group (sm:B1536's
  `cover_lib.state`) has as many conjugacy classes of subgroups of index n as SnapPy's m003 fundamental group, counted by
  low_index, an enumerator the cover code does not use. The same check on m004 gives m004's numbers, which differ from m003's
  at n = 5, 6, 7. SnapPy's bundle b+-LR is isometric to m003 and not to m004.

### 6a. The load-bearing inputs (WORKING_RULES 2026-10-06), each re-derived by own code on every instance used

| | input | source | own check |
|---|---|---|---|
| LB1 | the four covers are the ones with room 3 and 4 | sm:B1540 | K1: canonical forms; supplies in two routes |
| LB2 | the group is the census manifold m003's, and the bundle convention is right | sm:B1527, SnapPy's census | K7 |
| LB3 | Shapiro's lemma (route N reads H¹(N; ρ) as H¹(m003; ρ ⊗ ℂ[X])) | sm:B1536's Lemma S′, sm:B1532 | P1 at every class read: route R reads the class on N's own presentation at the same prime; K3 |
| LB4 | Lemma A's split of H¹ over the deck group | §3 | K2: in two routes, with two independent deck actions |
| LB5 | the frame's identities and Theorem C's bounds | sm:B1535, sm:B1536 | P3: checked at every reading |
| LB6 | one generic count per subspace (Lemma G) | §3 | P2: across draws, routes and primes |
| LB7 | the code paths are the banked ones | sm:B1536, sm:B1541 | K4, K5 |

A reading that a check here does not cover is not used by the verdict.

Disclosed:
- **What was read before the seal:**
  - the four covers' supplies, read directly in two routes as controls (fixed by sm:B1540's banked `room_60.json`);
  - the class spaces' dimensions, as structure;
  - N₄₅'s values in K4, fixed by sm:B1541's banked controls;
  - no class of any degree-60 cover.
- **A lost first draft.** This arc's first instruments were lost uncommitted when the seat's container was replaced (found on
  2026-10-06). They were rewritten on 2026-10-06 from the design notes and sm:B1541's sealed code. Before the
  loss they had computed structure only: the same dimensions as K2, and N₄₅ rebuilt. One trial of their controls ran to the end
  without printing a value. No class was read then.
- **The rewritten controls' first trial** (2026-10-06, 12:18–12:22Z) held K1–K6. K7 was added after it, for the 2026-10-06
  rule.
- **Three slips in this document's draft, caught before the seal** (ERROR_LEDGER):
  - The draft said the pieces at ψʲ and ψ⁻ʲ have equal dimension because they are complex conjugate. That needs the conjugate of
    ρ to be ρ, and for an amphichiral manifold it is ρ only up to an orientation-reversing automorphism, which can move ψ. The
    sentence is removed; K2 reads the dimensions directly.
  - The draft said the twist by ψʲ is a frame member for even j. Derived from the frame's definitions, it is a member only when
    (ψʲ)⁵ = 1, so only for j = 0 here (§3).
  - The draft said three of the sweep's terms appear only in sm:B1540. The sweep's own output listed other hits, among them
    sm:B1378's index on M₆. §0 now reports them.
- **sm:B1541 at this seal.** Its banked identity was re-checked in the new container at 12:11Z and held: controls K1–K6 were
  reproduced, and the seven sealed hashes matched. Its sealed run restarted from the beginning, since its first record was
  lost unread, and finished at 12:31Z (127 tasks, rc 0). Its record was committed unread (0e126a17). Its read-out waits for
  this seal, so this arc's priors do not know its outcome.

## 7. Predictions (priors fixed at the seal)

| | prediction | prior |
|---|---|---|
| P1 | the transport: at every class of Parts A and B, route R at p_N reads route N's count, k and connecting ranks exactly | 97% |
| P2 | across primes: within every subspace of every cover, all draws in both routes give one count | 90% |
| P3 | every reading's identities hold (sm:B1536's and Theorem C's checks) | 97% |
| P4 | some class read has a generation-shaped count, in route N and route R at p_N | 25% |
| P5 | some class read has the count (−3, −3), in route N and route R at p_N | 8% |
| P6 | on every cover, the class pulled back from m003 reads one count in both routes | 97% |

A population-wide prediction is True only on complete records (every sealed task with exactly its readings). A refuting row
decides False whatever the coverage.

## 8. BANKED IDENTITY: checked before reading

`identity.py` re-runs K1–K7 and checks every sealed file's sha-256 (`ARTIFACT_HASHES.txt`) before `run.py` reads anything.
A single difference stops the run.

## 9. Reading rules

- **PROVED (three generations at a class of a degree-60 cover)** if P1, P3 and P6 hold and P5 holds: a class of H¹(N; ρ) where
  the frame counts (−3, −3), read in two routes at the same class. It is a count at a class, not a selection. Which class and
  which cover the genesis selects is GENESIS GAP4 and THE_BAR's question.
- **NEGATIVE (scoped)** if P1, P2, P3 and P6 hold and P4 is False on complete records: no generation-shaped count at the generic
  classes of the subspaces read.
- **OPEN** otherwise. A generation-shaped count other than three is recorded and named.
- 0 of 19 stays 0 either way.
- **The audit before the bank, either way** (NO NEGATIVE FROM A BUG, 2026-10-01; and the 2026-10-06 rule, since the count
  carries the headline). A verdict other than OPEN is banked only after route F re-derives counts that the run read. Route F is
  written after the run. It imports nothing from sm:B1536's routes, this arc's library, or the libraries they compute with
  (PARI, FLINT). From each cover's permutation action, kept as data, it builds a second presentation of the cover: another
  presentation of π₁(m003) and another Schreier tree. It then computes the supplies and the count with its own linear algebra
  at three primes. It reads generic classes of the same subspaces (Lemma G: the generic count belongs to the subspace):
  - for NEGATIVE, at least one subspace per cover of each kind read: a cusp stratum, an eigenspace and an interior part;
  - for PROVED, the subspace where (−3, −3) was read.
  Its positive control is a subspace whose count the record gives as non-zero, read on route F's own code path. If route F
  disagrees with the run, the verdict is withheld and the disagreement goes to ERROR_LEDGER first.

## 10. What this arc does not decide

- The special classes inside each subspace (its proper closed subsets, where the count can jump), and other subspaces.
- Other characters ν of these covers, the conjugate covers d10.14's and d10.38's (equal counts, by conjugacy), and other covers
  with room for three: sm:B1538's room-three members of the silver pair, and covers of higher degree.
- The golden order: N₄₅ is sm:B1541's question, and m004's covers with room ≥ 3 have not been found. m004's best room on a fixed
  pulled-back cyclic cover is 1 (sm:B1540), which is a statement about the covers searched only.
- Which class, and which cover, the genesis selects (GENESIS GAP4, THE_BAR).
