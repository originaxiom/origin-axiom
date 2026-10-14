# B1548 — PREREGISTRATION: THE ROOM-THREE CIRCLES — on the golden cover N₄₅, room three lies on five circles of characters; the members on the circle through χ0, of every order in ORDERS (all dividing 120, none dividing 4), read at every stratum where three can live

**THE WEAVE: a THREAD result, labelled at the owner's ruling.** N₄₅ is a cover of one thread: the degree-45 cover of m003,
the 5-fold cyclic cover of its d9.2 (sm:B1541). This arc reads characters of that one cover. Whatever it reads, it answers
no weave question, and nothing in it is offered as an answer to one (`docs/THE_WEAVE.md`).

**Sealed before `run.py` read any count at a member of the circle. Sealed after sm:B1547's read-out and bank**, which this
seat has read. At the seal this arc has:
- **found, as structure** (§3.1; the dossier `docs/dossiers/room_three_circles_2026-10-07/`; control K9): on N₄₅ the
  cusp-trivial characters with room three (n = 3) are exactly the points of five circles t ↦ exp(2πi·t·φᵢ), one τ-orbit,
  at every order from 2 to 5. Along a circle the room is three at every point read.
- **proved, at design time** (§3): at a point ν of a circle whose order m does not divide 4, b0 = 0 and the room is exactly
  three. So sm:B1547's Corollary 1 and Lemma G hold unchanged. Lemma Γ holds on the automorphisms that fix √3.
- **computed structure only** (§5, §6), in two routes.
- **read counts only where the record has them banked**:
  - the trivial character's generic interior class (control K5);
  - sm:B1547's banked counts by structure (its FINDINGS §3), which include the four members of this arc that are
    sm:B1547 members (§6).

**Source.**
- The owner, 2026-10-04: "thanks, keep focused. three generations is smth we are after seripuslu"; "make sure we dont abandon
  the golden pointer". The owner, 2026-10-06: "breakthrough breaktheough breakthrough!!! is expected from you".
- **The hold, 2026-10-07.** The draft (`docs/dossiers/room_three_circles_2026-10-07/draft_b1548/`) was held, not sealed.
  Main's audit of this seat's generation lane recommended to the owner that the search over covers, characters and classes
  pause until the GENESIS fork FK14 is ruled. The owner then fixed THE WEAVE rule (2026-10-07): covers of one object are
  thread results.
- **The owner's ruling, 2026-10-14.** Asked what should happen to the held draft, the owner answered:
  "Seal and run it, labelled". So it is sealed and run, and labelled a thread result throughout. The pause main
  recommended is not ruled away by this arc. FK14 stays GENESIS's open fork, and nothing here bears on it.
- sm:B1547 (banked NEGATIVE, 2026-10-07): no class at any of N₄₅'s cusp-trivial order-8 characters over the five room-three
  characters carries three, in either order. Its §10 leaves the members whose fourth power has order three or more. The
  dossier's census, made while it ran, found the circles.

## 0. Seen first, and PRIOR ART:

**The repo sweep.** `git fetch origin` ran first (2026-10-14, 16:38Z), and every remote head was listed.
`scripts/checks/prior_work.py` then ran over every head with nine terms: "room-three circle", "circle of characters",
"one-parameter family", "subtorus", "room three", "room-three members", "jump loci", "characteristic variet", "B1548".

| head | commit |
|---|---|
| this branch | `87cf7f55` |
| main | `60c5470a` |
| the audit lane (fork) | `0c6570ba` |
| the audit lane (physical bridge) | `e0f51c49` |
| the web seat's branch (…/web-seat) | `67821b8e` |
| the archive branch (…/weave-physics-archive-2026-10-11) | `efadcdea` |
| seat/outside-bench | `13d2c5b6` |
| seat/paper-review-verification | `5d58b935` |
| seat/kind-hypatia | `6a537f89` |
| seat/project-thread | `8b6df98f` |
| sep16-branch | `3205984b` |

What the sweep found:
- **"room-three circle" and "circle of characters"** appear only on this branch: in this arc's own dossier and draft, and
  in this seat's relays, OPEN_LEADS and ledger rows that pointed to it.
- **"B1548"** names no arc on any head. Its other hits are this arc's draft and a number inside a JSON array of the audit
  lane's (`reports/physical_bridge_2026_09_05/INDEX_STABILITY_HISTORY_REPEAT.json`), which is not an arc id.
- **"room three" and "room-three members"** lead to this seat's sm:B1538–B1547. On main and the archive branch they are
  ledger and changelog rows reading this seat's work, and main's B1493 seal, which quotes sm:B1547's members. None reads a
  character of N₄₅ of order 3 or more.
- **"jump loci" and "characteristic variet"** hit sm:B1547's own files, this seat's OPEN_LEADS (the cyclic covers of the room
  covers, another population), and the audit lane's NEXT_TEST note on the rank-jump loci of pair mass maps (another object).
- **"one-parameter family" and "subtorus"** hit other objects across the record (sm:B1523's flexible states, B874's
  measurement ladder, B1079's Wilson menu). None is a family of characters of N₄₅.

**The literature.** As sm:B1547's: Dimca, Papadima and Suciu (arXiv:0902.1250, abstract, read 2026-10-06) on the relative
characteristic varieties of twisted cohomology. A circle along which h¹ jumps is a component of such a jump locus, a
torsion-translated subtorus in their picture (here through the identity). This arc computes the component's points, not the
variety.

**Standing: NEW-AS-SWEPT** for the circles of room three on N₄₅ and for the counts at their points of order 3 or more.
EXTENDS sm:B1547: the same frame and theorems, with a one-parameter family of members in place of one order.

## 1. The question

On N₄₅, at a point ν of the room-three circle through χ0, of an order that does not divide 4, does any class of sm:B1515's
frame read three, (−3, −3), in either order? The run reads the members of orders 3, 5, 6, 8, 10, 12, 15, 20, 24, 30, 40 and
60 on that circle (84 characters), at every stratum where three can live at each.

## 2. Definitions and conventions

As sm:B1547 §2 (N₄₅, the frame, r, s, t, k, b0, the keys, the strata, the routes), with the following.
- **The circles.** A circle is a homomorphism φ: π₁(N₄₅) → ℤ, trivial on every cusp and primitive. Its points are the
  characters exp(2πi·j·φ/m), j a unit mod m, of exact order m.
  - Its values on the 46 common loops, W ∈ ℤ⁴⁶, name it in both routes.
  - The population's circle is the one whose order-2 point is χ0. Its values W_CIRCLE are sealed in `run.py`. They were
    found by route R's census (orders 2 and 3, the five circles' directions with entries in {−1, 0, 1}).
  - Each route solves for φ in its own lattice basis from W_CIRCLE. It checks that φ is primitive, that its order-2 point
    is the route's own χ0, and that its order-3 points are room-three in the route's own census.
- **The members**: the circle's points of exact order m for m in ORDERS = (3, 5, 6, 8, 10, 12, 15, 20, 24, 30, 40, 60),
  taken in the order (m, key). There are Σ φ(m) = 84. Both routes' primes are 1 mod 120, so every order here has its roots
  of unity there.
- **The Galois classes**: the orbits of ν ↦ ν^k over the automorphisms that fix √3 (Lemma Γ). They are every unit k mod m
  when 12 does not divide m, and k ≡ ±1 mod 12 when it does. So there is one class per order, and two at 12, 24 and 60:
  fifteen in all.

## 3. What is proved or found at design time

**3.1 The circles (structure; control K9, and the dossier).** At orders 2, 3, 4 and 5, the cusp-trivial characters of N₄₅
with n ≥ 3 are exactly the points of five circles, each with n = 3. In route R's lattice basis their directions are
(0, −1, −1, −1), (−1, 0, 1, 0), (0, 0, −1, 0), (0, −1, 1, 0) and (−1, 0, 0, −1), up to sign. τ permutes them (K3).

**3.2 The members satisfy sm:B1547's hypotheses.** Let ν be a point of the circle of order m, where m does not divide 4.
- ν is trivial on every cusp (φ is), so all five cusps are trivial.
- ν⁴ = exp(2πi·4j·φ/m) is a point of the same circle, of order m/gcd(m, 4) ≥ 2. So ν⁴ ≠ 1, b0 = 0, L = ν⁻⁴, and
  n(L) = 3. This is checked at every member (P4: n(ν⁴) = 3 and n(L) = 3).
- So sm:B1547's Corollary 1 (Theorem C (ii) with sm:B1545's Lemma F′) and Lemma G hold verbatim. Three at ν lies in a
  distinct stratum X_U, |U| ≤ 2, with support U, and the generic class of each has the least counts on the classes of
  support U.

**3.3 Lemma Γ at these orders.** The four is defined over ℚ(√3) (sm:B1547 §3.4, control K4). An automorphism of
ℚ(ζ_{lcm(m, 24)}) that fixes √3 sends ν to ν^k exactly for the units k above. Galois-conjugate members over such k read
alike in characteristic 0. Both routes read every member, so the verdict does not rest on Γ. P3 tests it.

**3.4 The other order, and the deck symmetry.** As sm:B1547 §3.4.
- The other order at ν is W₁ at ν̄ = ν^{m−1}, a member of the same order on the same circle.
- τ carries χ0's circle to the other four with the same counts (K3, at four sample members).

**3.5 What a NEGATIVE covers.** No class at any point of order 3, 5, 6, 8, 10, 12, 15, 20, 24, 30, 40 or 60 of any of the
five room-three circles carries three, in either order. Points of other orders are not read. P9 checks Theorem C's cap and
Lemma F′ at a generic class of K0^ν and of H¹ at every member.

## 4. The instruments (`verification/`, written and checked before the seal)

- `circle_lib.py`: the circles (`directions`, `int_values`, `solve_direction`, `circle_points`), the members (`member`) and
  the room (`line_n`). It loads sm:B1547's sealed `member_lib.py` by path, unchanged (K8 checks its sha-256).
- `run.py`: the population and the tasks of §5. `read_out.py`: the predictions of §7, once. `controls.py`: K1–K9.
  `identity.py`: the banked identity (§8). `census.py`: the structure census of §5 (no count).

## 5. The population (outcome-blind; seeds crc32 of "B1548|route|m|key|U|draw")

- **Tasks:** route R and route F at each of the 84 members: 168 tasks, one row each.
- **At each member:** its order and key, n(ν⁴), the structure, the sixteen strata, the distinct strata, and three
  readings at each distinct stratum.
- **In route R also,** the load-bearing checks at a generic class of K0^ν and of H¹. Seeds "B1548|R|m|key|K0|0" and
  "B1548|R|m|key|H1|0".
- **The structure census before the seal** (route R, every member; `verification/census.py` → `census.json`):
  84 members, and the fifteen Galois classes are alike
  in structure. At every member n(ν⁴) = n(L) = 3 and h¹(L) = 8; K0^ν ≠ 0, with an interior part of dimension 2; and there
  is exactly one distinct stratum, the interior one (U = {}), whose generic class has support exactly U. So the run reads
  252 stratum readings in each route (84 strata, three draws) and 168 check readings in route R (84 at K0^ν, 84 at H¹).

  | orders | h¹(ν⁵ ⊗ ρ) | n(ν⁵ ⊗ ρ) | dim K0^ν | its interior part | distinct strata at each | members |
  |---|---|---|---|---|---|---|
  | 3, 6, 8, 10, 12, 15, 20, 24, 30, 40, 60 | 15 | 10 | 2 | 2 | 1 (interior) | 80 |
  | 5 | 23 | 18 | 5 | 2 | 1 (interior) | 4 |

## 6. Controls and disclosures (before the seal)

All hold (`verification/controls.json`). The structure census ran 16:43:03–16:50:07Z on 2026-10-14 and the controls
16:50:07–16:53:43Z, each once, for the record.
- **K1.** The population in each route on its own. The direction is solved from W_CIRCLE, is primitive, passes through the
  route's own χ0, and has room-three order-3 points. The members' orders and keys are in order and equal in both routes,
  with φ(m) members of each order.
- **K2.** Every member in both routes is trivial on every cusp, of exact order m, and on the circle.
- **K3.** τ maps each circle's direction to another's. At four sample members, τ*ν has ν's structure and strata.
- **K4.** Lemma Γ's input, and the Galois classes: one per order, two at 12, 24 and 60.
- **K5.** The trivial character's banked count (4, −10) in both routes.
- **K6.** At the first member of each order, in both routes: the structure, n(ν⁴) = 3, the strata, the distinct strata and
  the generic supports agree.
- **K7.** The read-out on twenty-two synthetic cases.
- **K8.** sm:B1547's `member_lib.py` hashes as sealed there.
- **K9.** The circles: at orders 2 to 5 the room-three characters are exactly their points.

### 6a. The load-bearing inputs

| | input | source | own check |
|---|---|---|---|
| LB1 | Theorem C (ii): route R's identities and the cap s ≤ k + n(L) | sm:B1535, sm:B1536 | P4 at every reading; P9 at a generic class of K0^ν and of H¹ at every member |
| LB2 | Lemma F′ at members (here k − 5) | sm:B1545 | P4; P9 |
| LB3 | Corollary 1 and Lemma G | sm:B1547 §3.2–3.3 | three draws per stratum in each route, two routes, two primes; P5 |
| LB4 | the members are the circle's points with room three | §3.2 | K1, K2; P4 (n(ν⁴) = 3 at every member); P2 |
| LB5 | the circles | §3.1 | K9 (route R), K1 (route F at orders 2 and 3) |
| LB6 | the deck symmetry carries χ0's circle to the other four | §3.4 | K3 |
| LB7 | Lemma Γ | §3.3 | K4; P3 (the verdict does not rest on it) |
| LB8 | the code paths are the banked ones | sm:B1541, sm:B1544, sm:B1547 | K5; K8 |

Disclosed:
- **What was read before the seal.**
  - Structure only, at design time (2026-10-07): the census of n(χ) at orders 2 to 6 (route R), the five circles'
    directions and loop values, and at every member n(ν⁴), the cohomology dimensions, K0^ν, the strata and their generic
    supports (route R at all 84, route F at twelve). At the seal (2026-10-14) the same structure was read again, by the
    sealed `census.py` and `controls.py`.
  - Counts only at the trivial character, banked (K5).
  - **sm:B1547's read-out and FINDINGS, read in full** (banked 2026-10-07). This seal is not blind to them. Four of this
    arc's members, the circle's points of order 8, are sm:B1547 members, and their counts are banked there: the census puts them at the structure
    (15, 10, 2, 2) with one interior stratum. sm:B1547 has exactly four members of that structure, and its FINDINGS §3
    reads their generic interior count as (0, −5). So this arc's order-8 members read (0, −5) on the banked record, and
    their rows here are a re-reading.
    The priors of §7 were set after reading them.
- **How the design changed between the draft and the seal.** Only these, all before any count at a member of the circle:
  - the label (a thread result), the source (the owner's ruling) and the disclosure of sm:B1547's read-out;
  - §0's sweep, run again on 2026-10-14 with every head fetched;
  - a slip in the draft's §3.2, which read "4 ∤ m" where the argument needs "m does not divide 4" (the orders 8, 12,
    20, 24, 40 and 60 are divisible by 4, and the argument holds at each);
  - `census.py`, added so that §5's census is reproducible from a sealed file;
  - the priors, moved after reading sm:B1547 (§7);
  - the code of `circle_lib.py`, `run.py`, `read_out.py`, `controls.py` and `identity.py` is the draft's, byte for byte.
- **The machine.** This seat's W80 (a fit, in the weave dossier) runs on four workers beside the seal's census and
  controls. This arc's run starts when W80 ends.

## 7. Predictions (priors fixed at the seal)

| | prediction | prior |
|---|---|---|
| P1 | the banked identity holds | 97% |
| P2 | the routes agree at every member | 90% |
| P3 | in each route the members of every Galois class read alike | 88% |
| P4 | the theorems at every reading, and the room (n(ν⁴) = n(L) = 3) and the strata at every member | 95% |
| P5 | genericity: at every distinct stratum the draws read alike, each with support exactly U | 92% |
| P6 | the floor: every distinct stratum's generic reading has I(W₁) ≥ −2 | 90% |
| P7 | I(W₁) ≥ 0 at every reading | 65% |
| P8 | three: some stratum's generic reading is (−3, −3) in both routes | 2% |
| P9 | the load-bearing checks hold at every member (route R) | 96% |
| P10 | some stratum's generic reading is generation-shaped in both routes | 8% |

**Why these priors.** The draft (2026-10-07, before sm:B1547's read-out) set P6 80%, P7 35%, P8 6% and P10
25%. They were moved at the seal after reading sm:B1547:
- The census gives one structure at every order but 5: one interior stratum of dimension 2, inside K0^ν of dimension 2.
  sm:B1547 read that structure, (15, 10, 2, 2), as (0, −5) at all four of its members, and its (13, 8, 2, 2) as (0, −3).
  Its least I(W₁) anywhere was −2. So P6 rises to 90% and P7 to 65%.
- Order 5 is the place the counts may change. There ν⁵ = 1, so c lies in H¹(N; ρ), of dimension 23 as at the trivial
  character, and K0^ν has dimension 5. Order 3 is the other: there ν³ = 1, so V ⊗ L = ν⁻³ ⊗ ρ = ρ, and the Λ² side
  meets n(ρ) = 18.
- Three needs the boundary Massey map of an interior class to be injective on the three-dimensional interior part of
  H¹(N; L) (sm:B1547 §3.2: I(W₁) = −e there). sm:B1547 found that rank at most 2 at every reading. So P8 falls to 2% and
  P10, which needs I(W₁) < 0, to 8%.

A population-wide prediction is True only on complete records. A refuting row decides False whatever the coverage.

## 8. BANKED IDENTITY: checked before reading

`identity.py` re-runs K1–K9 and checks every sealed file's sha-256 (`ARTIFACT_HASHES.txt`) before `run.py` reads anything.
A single difference stops the run.

## 9. Reading rules

As sm:B1547 §9, with this population.
- **PROVED (three)** if P1, P2, P4 and P9 hold and P8 holds. The audit at two more primes comes before the bank. It is a
  count at a class on one thread's cover, not a selection and not a weave result.
- **NEGATIVE** if P1, P2, P4 and P9 hold on complete records, and no distinct stratum's generic reading, in either route,
  has I(W₁) = −3 with I(Λ²W₁) ≤ −3. Then §3.5.
- **OPEN** otherwise.
- The read-out records every stratum's generic count by order, the least I(W₁), and every generation-shaped stratum.
- 0 of 19 stays 0 unless P8 holds and the audit confirms it.

## 10. What this arc does not decide

- **Points of the circles of other orders**, including orders whose roots of unity the two primes lack.
- **The circles' points with ν⁴ = 1** (orders 1, 2 and 4), where b0 = 1.
- **Room-three characters of N₄₅ off the circles at orders above 5**, if any. K9 covers orders 2 to 5.
- **Members over the circles that are not on them.** sm:B1547 reads order 8; other orders are not read.
- **Other covers**, and which class and which cover the genesis selects (GENESIS GAP4, FK14, THE_BAR).
- **Any weave question.** This is a thread result (THE WEAVE rule). The weave's own count is the weave dossier's
  (`docs/dossiers/the_weave_2026-10-07/NOTE.md`).
