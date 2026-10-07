# B1549 — PREREGISTRATION: THE THREE-ENDED COVERS — on every three-ended cover of the generated family to twelve ends, every member at characters of order dividing four, its orbit under the symmetry that cycles the ends, and its count: does the three-orbit select +LLLR?

**Sealed before `run.py` read any count at a member outside the controls.**

At the seal this arc has:
- **proved at design time** (§3):
  - which states have a three-ended cover;
  - that each member carries at most one generation (n(1) = 0);
  - the orbit law;
  - the flavor group's shape.
- **computed structure only** (§5, §6): the population and the flavor group of every member orbit, at 50 digits, in two
  routes and two rank methods.
- **read counts only where the record has them banked** (§6, K2 and K3):
  - main's B1492 and B1493 on L8a15;
  - main's B1492 on o10_150729;
  - sm:B1545 and main's B1485 on m136's companion.

**Source.**
- The owner, 2026-10-07: "maybe three generations font emerge in at once ir in one place, but as a process in more steps /
  what did we learn from these results?"
- The owner, the same day: "make sure you dont lean on m004 alone but in all alloed objects or family of objects. this is
  our number1 error we keep doing. interaction between objects in relationship should produce reality, not single objects
  alone".
- The three-orbit note (`docs/dossiers/the_three_orbit_2026-10-07/NOTE.md`):
  - main's three one-generation members on L8a15 are one orbit of the deck group ℤ/3, and +LLLR is the only state whose
    companion has three ends;
  - its update finds that they induce a triplet of π₁(+LLLR) with image ℤ/2 × A₄.
- The census of the line's room (`docs/dossiers/the_lines_room_on_every_companion_2026-10-07/`, Proposition N): no single
  member of order dividing 8 on any companion of the family carries three. So three, if it comes on these objects, comes
  as several members.
- At design time this arc found that **every state whose companion has a number of ends divisible by 3 has a three-ended
  cover**: ten states, thirteen covers to twelve ends. The three-orbit's selection of +LLLR therefore has to be tested
  against all thirteen.

## 0. Seen first, and PRIOR ART:

**The repo sweep.**
- `git fetch --all` ran first (2026-10-07, 08:28Z).
- `scripts/checks/prior_work.py` then ran over every head with eight terms: "three-ended cover", "three-ended", "deck
  orbit", "tetrahedral", "flavor group", "flavour group", "Delta(48)", "Z/2 x A4".

| head | commit |
|---|---|
| this branch | `f1be6b2f` |
| main | `0b45b1fb` |
| the audit lane (fork) | `8b89d8fb` |
| the audit lane (physical bridge) | `c161981d` |
| the new web seat's branch (…/web-seat) | `d40c1ab6` |
| seat/kind-hypatia | `6a537f89` |
| seat/outside-bench | `13d2c5b6` |
| seat/paper-review-verification | `5d58b935` |
| seat/project-thread | `8b6df98f` |
| sep16-branch | `3205984b` |

What the sweep found:
- **"three-ended cover", "Delta(48)" and "Z/2 x A4" are absent on every head.**
- **"three-ended"** hits main's B1491 and B1492 (L8a15, +LLLR's companion) and this seat's three-orbit note and relays. No
  head reads a three-ended cover of any other state.
- **"deck orbit" bears through this seat's B1356** (2026-09-15, the G₂ tower):
  - a deck-symmetric triple of E₇ apexes on Y₃ is a free orbit of a ℤ/3 deck, and the quotient's holonomy is
    T = A₄ = 2T/±1;
  - the sum rule there kills every deck-invariant charge.
  - So a triple as a free ℤ/3 orbit with A₄ around it has been on the record since September, on another object and in
    another frame.
  - This arc's A₄ is the image of an induced representation of a punctured-torus bundle's group, not an orbifold's
    holonomy.
- **"flavour group" bears through this seat's B1391** (2026-09-27, NEGATIVE for Yukawa ratios as an output of the
  symmetric geometry):
  - the frame of B1389 on cube~3.24 has two generations forming the doublet of its isometry group D₃;
  - by Schur they are exactly degenerate at the symmetric point.
  - **The same limit applies here.** An exact A₄ makes its triplet's three alike, so a hierarchy needs the symmetry
    broken.
- **"flavour group" also bears through this seat's B1255** (2026-09-05): the pattern behind twelve lost three-nesses.
  - Every lost three was built on ℚ(√−3), which can only make 1 + 2.
  - A genuine three needs the three permuted transitively, with none distinguished.
  - This arc's three members are permuted transitively by a geometric ℤ/3: copies, not Galois conjugates.
  - But in the basis of deck charges (1, ω, ω²) the triplet is again 1 + 2 over ℚ: B1255's warning.
  - Which basis is physical, and whether the base or the cover is the physical space, is GENESIS FK14's question. This arc
    records the structure and decides neither.
- **"tetrahedral" and "flavor group"** otherwise hit unrelated objects (B660's structure campaign, B1522, B487, B1041,
  B1070, B1166).

**The literature** (read 2026-10-07):
- G. Altarelli, F. Feruglio and Y. Lin, "Tri-bimaximal neutrino mixing from orbifolding", Nucl. Phys. B 775 (2007) 31–44,
  hep-ph/0610165, abstract. A₄ arises from a six-dimensional model on the orbifold T²/ℤ₂: the tetrahedral symmetry
  connects the four fixed points. The nearest known geometric origin of A₄.
  - Here the torus is the fibre of a punctured-torus bundle.
  - The ℤ/3 is translation by the monodromy's three fixed points.
  - The ℤ/2's are sign characters.
- A. Adulpravitchai, A. Blum and M. Lindner, "Non-Abelian discrete flavor symmetries from T²/Z_N orbifolds",
  arXiv:0906.0468, abstract: the discrete groups that orbifolds of T² can give.
- E. Ma and G. Rajasekaran, Phys. Rev. D 64 (2001) 113012, and G. Altarelli and F. Feruglio, Nucl. Phys. B 720 (2005) 64:
  A₄ with the lepton doublets in its triplet and the right-handed charged leptons in its singlets 1, 1′ and 1″.
- C. Luhn, S. Nasri and P. Ramond, J. Math. Phys. 48 (2007) 073501: the Δ(3n²) groups, Δ(48) among them.
- A post by M. Gentry on Substack, "The HFG Programme: From Derivation to Selection", read 2026-10-07. It claims that the
  observed mixing matrices sit near points defined by minimum-volume arithmetic hyperbolic 3-manifolds. It gives no
  construction, no flavor group and no covers, so it bears on nothing here.

**Standing: NEW-AS-SWEPT** for the three-ended covers of the family, their members, orbits and flavor groups, and the
counts there. It EXTENDS main's B1492 and B1493, which read L8a15 (one of the thirteen covers), and this seat's
three-orbit note (the selection question asked of every three-ended cover).

## 1. The question

On every three-ended cover of the generated family to twelve ends:
- at every character ν of order dividing 4 whose module ν ⊗ ρ has an interior class (a member), what does that class
  count?
- Which members are generation-shaped, (I(W₁), I(Λ²W₁)) = (−1, −1)?
- How do they sit in the orbits of the ℤ/3 that cycles the three ends?

**The claim under test (the selection).** The three-orbit selects +LLLR: its three-ended cover, which is its companion
L8a15, is the only cover of the thirteen whose generation-shaped members number exactly three.

## 2. Definitions and conventions

- **The states.** Every word in L and R of length 2 to 8 that uses both letters and is primitive, up to rotation and the
  swap, with either sign: sm:B1527's presentation, with generators a, b, t, two relators and the cusp ⟨l, t′⟩.
- **A three-ended cover.** One of sm:B1538's fibre-direction covers of degree 3 with three cusps: a lattice Λ of index 3
  with MΛ = Λ, and a class w̄. Its deck group ℤ/3 permutes the three ends.
- **The frame.** sm:B1515 at ν⁴ = 1: ρ is the four, L = 1 and b0 = 1.
  - A class c of H¹(N; ν ⊗ ρ) gives W₁ = [[ν ⊗ ρ, c], [0, 1]].
  - I(E) = n(E) − n(E*) and n = h¹ − r¹, with r¹ the rank of the restriction to every cusp.
  - The count is (I(W₁), I(Λ²W₁)).
- **A member** is a character with n(ν ⊗ ρ) ≥ 1. Its classes are the interior ones, which vanish on every end.
- **Generation-shaped** means I(W₁) = I(Λ²W₁) < 0.
- **The cusp decomposition of a count.**
  - m_A is the number of ends where ν is trivial; m_B = 3 − m_A at ν⁴ = 1.
  - k is the number of ends where c restricts non-trivially among those in A. Interior classes have k = 0.
  - b0 = 1.
- **The two routes.** They share only the cover's action, the character's definition and the holonomy.
  - **Route P** uses N's own presentation (sm:B1538's punct_present).
  - **Route S** is Shapiro on M:
    - a class z of H¹(M; Ind ν ⊗ ρ) gives c(h) = z(h)₀ on N;
    - then Ind W₁(g)_{x,y} = W₁(u_x g u_y⁻¹) and Ind(Λ²W₁) on M;
    - N's cusps are read through M's one cusp (Mackey).
- **Precision.**
  - The holonomy is sm:B1527's family_lib.hyperbolic_sl2 at 60 digits, and the four is built from it in mpmath.
  - Everything is at 50 digits.
  - Ranks are by Gauss–Jordan elimination with column pivoting. An entry is zero below 10⁻³⁰ of the matrix's largest.
  - The gap (least live pivot, largest dead entry, both relative) is recorded at every rank.
- **The flavor group of an orbit.** The image of π₁(M) under Ind χ, as monomial matrices with exponents mod 4, computed
  exactly.

## 3. What is proved at design time

**3.1 The three-ended covers.**
- If a state has a three-ended cover with lattice Λ, its monodromy fixes each of the three punctures. So (M − 1)ℤ² ⊆ Λ, and
  3 divides |ℤ²/(M − 1)ℤ²|, which is the number of ends of the companion.
- Conversely, if 3 divides that number, coker(M − 1) has a quotient of order 3. Its Λ is M-invariant, because
  MΛ ⊆ Λ + (M − 1)ℤ² = Λ.
- The census (§5) finds a class w̄ with three cusps on every such Λ:
  - ten states have one: −LLR, +LLLR, +LLLRR, −LLRLR, −LLLLLR, −LLLLRR, +LLLRRR, +LLLLLLR, +LLLLRRR, +LLLLLLRR;
  - that is thirteen covers, since +LLLRRR's coker is (ℤ/3)², with four quotients of order 3;
  - every one is a quotient of its state's companion.

**3.2 At most one generation per member.**
- On each cover b₁ = 3, the number of ends. So the restriction H¹(N; ℂ) → H¹(∂N; ℂ) is injective and n(1) = 0 (checked
  exactly, K5).
- By Theorem C (sm:B1535) every class at a member with ν⁴ = 1 has I(W₁) ≥ −b0 − n(1) = −1.
- Also I(Λ²W₁) ∈ [−n(ν³ ⊗ ρ), 0], and n(ν³ ⊗ ρ) = n(ν ⊗ ρ), since ν³ = ν or ν̄ and ρ is real.
- At every member of the population n(ν ⊗ ρ) = 1 and m_A = 0 (§5). Lemma F′ (sm:B1545) gives I(W₁) ≥ k − m_A − b0 = −1.
  The ceiling gives I(W₁) ≤ 2m_A + m_B − b0 = 2.
- So **a generic reading is (I(W₁), I(Λ²W₁)) with I(W₁) ∈ {−1, …, 2} and I(Λ²W₁) ∈ {−1, 0}. Generation-shaped means
  (−1, −1): exactly one generation.**
- Since the interior is one-dimensional at every member, its classes are the multiples of one class. A generic class is
  that class, and the three draws differ only by scale.

**3.3 The orbit law.**
- For x in the deck group, χ ↦ χ ∘ conj(u_x) carries ν ⊗ ρ to a module isomorphic to the pullback of ν ⊗ ρ under the
  automorphism conj(u_x) of π₁N, through ρ(u_x), because ρ extends to π₁M.
- Pullback by an automorphism that permutes the cusps preserves h¹, the restriction rank and the counts at corresponding
  classes.
- So **the three members of a deck orbit read alike, in each route.** P3 checks it at every orbit.

**3.4 The flavor group.**
- For a free ℤ/3 orbit, Ind χ is irreducible (Mackey). Its image lies in (μ₄)³ ⋊ ℤ/3, and for a sign character in
  (ℤ/2)³ ⋊ ℤ/3 ≅ ℤ/2 × A₄.
- §5 computes it at every member orbit. It is structure, seen before the seal, and no prediction rests on it.

## 4. The instruments (`verification/`, written and checked before the seal)

- `three_lib.py`: the states, the three-ended covers, the deck orbits, the four at 50 digits, the linear algebra (elimination
  with gaps), module cohomology with the interior classes, the frame, route P, route S, and the flavor group.
- `census.py` → `census_0.jsonl`, `census_1.jsonl`, `population.json`: the structure census (§5).
- `run.py`: every member in both routes, three draws, resumable, one row per task (`run.jsonl`).
- `read_out.py`: the predictions of §7 from the rows, once. `evaluate` is pure.
- `controls.py` (`controls.json`): K1–K5 (§6). `identity.py` (`identity.json`): the banked identity (§8).

## 5. The population (outcome-blind; seeds crc32 of "B1549|route|state|lattice|wbar|character|draw")

- **The census.** `census.py` read all 672 deck orbits of characters of order dividing 4 on the thirteen covers, in both
  routes at 50 digits.
  - The routes agree at every orbit.
  - The least live pivot is 3.4 × 10⁻¹¹ and the largest dead entry 3.1 × 10⁻⁴².
- **46 member orbits, 138 members.** Every one:
  - is a free ℤ/3 orbit;
  - is trivial on no end (m_A = 0);
  - has n(ν ⊗ ρ) = 1 in both routes;
  - has an irreducible induced triplet.

| cover (state, lattice, w̄; companion's ends) | sign member orbits (ℤ/2 × A₄) | order-4 member orbits (det-1 part Δ(48)) |
|---|---|---|
| −LLR, (3, 1, 1), 0; 6 | 2 | 12 |
| +LLLR, (1, 0, 3), 0; 3 (L8a15) | 1 | 2 |
| +LLLRR, (1, 0, 3), 0; 6 | 0 | 4 |
| −LLRLR, (3, 0, 1), 1; 12 | 0 | 0 |
| −LLLLLR, (3, 1, 1), 0; 9 | 1 | 2 |
| −LLLLRR, (3, 2, 1), 2; 12 | 0 | 8 |
| +LLLRRR, four covers; 9 | 0 | 0 |
| +LLLLLLR, (1, 0, 3), 0; 6 | 2 | 4 |
| +LLLLRRR, (3, 0, 1), 0; 12 | 0 | 0 |
| +LLLLLLRR, (1, 0, 3), 0; 12 | 0 | 8 |

- **The flavor groups.** Every sign member orbit's image is ℤ/2 × A₄: order 24, centre ±1, and determinant-one part A₄.
  Every order-4 member orbit's determinant-one part has Δ(48)'s order, centre, derived group and element orders. The whole
  image has order 96 at 24 orbits and 192 at 16.
- **The tasks.** Every member in both routes: 276 tasks, each with the structure and three generic interior classes, each
  class with its count and the four module readings.

## 6. Controls and disclosures (before the seal)

All hold (`verification/controls.json`, 08:37:09–08:43:07Z on 2026-10-07). The controls ran first as a trial (`verification/controls_trial.json`, K1–K4). They then ran for the record after K5 was added, K3 was corrected (below) and the census was banked compressed. A first start of the record run was stopped by exact PID after a minute, before any output, to make the scripts read the compressed census.
- **K1. An independent rank method.** Every member orbit, and the first two non-member orbits of every cover, are re-read in
  both routes with ranks by complex SVD (mpmath) instead of elimination. (h¹, r¹, n) equal the census's.
- **K2. Main's banked counts**, in both routes, one draw:
  - on L8a15, the sign member reads (−1, −1) (B1492) and the order-4 member (1, 1, i) reads (−1, 0) (B1493);
  - on o10_150729 (m003's companion, five ends), a member trivial on one end and one trivial on two ends read (−1, −1)
    (B1492).
- **K3. sm:B1545's banked reading on m136's companion** (m136.D4.2-0-2.w0) at the fibre sign: the interior class reads
  I(W₁) = −1. The Λ² component is recorded, not checked: nothing on the record banks it on the companion. Both routes.
- **K4. The read-out on synthetic rows.** Nine cases cover:
  - the PROVED and NEGATIVE verdicts;
  - incomplete and duplicated records;
  - disagreeing routes;
  - disagreeing draws;
  - a reading below the cap;
  - a failed control;
  - a murky gap.
- **K5. n(1) = 0 on every cover**, exact: sm:B1538's reader at the trivial character, two primes.

Disclosed:
- **What was read before the seal.**
  - Structure only:
    - the three-ended covers;
    - the deck orbits;
    - the census in double precision, where the routes disagreed on the twelve-ended covers, which is why everything here
      is at 50 digits;
    - the census at 50 digits by elimination in `census.py`, and in scratch by complex SVD (the seat's scratch reader,
      not committed because it loads the seat's scratch modules). The two agree at all 672 orbits in both routes. K1
      repeats the SVD reading, in committed code, at every member orbit and two non-member orbits per cover;
    - the flavor groups;
    - the room of the line on every companion (the dossier).
  - Counts at members, before the seal and only where banked:
    - +LLLR's sign member and its order-4 member, in the library's test and in K2 (main's B1492 and B1493);
    - o10_150729's members (K2, main's B1492);
    - m136's companion (K3).
  - Earlier on 2026-10-07 this seat's scratch route P read every ν⁴ = 1 member of L8a15 (the same three orbits). No count
    at a member of any other cover in the population was read.
- **How the design changed before the seal.**
  - The first plan read the members on the 27 companions. On the twelve-ended companions double precision was not
    reliable.
  - Finding that every state with 3 | ends has a three-ended cover made the selection testable across those covers, so
    the population became the thirteen covers. That change came from structure, before any count.
- **An error found and fixed in scratch.** The design census's first SVD nullspace took the thin SVD and lost the kernel
  of wide matrices. It was fixed with full matrices before any reading quoted here.
- **A control that failed in the trial, and why.**
  - The trial run of the controls (`controls_trial.json`) expected (−1, −1) at K3, citing main's B1485 and B1492. Both
    routes read (−1, −2).
  - Main's (−1, −1) is at m136's own two members, on m136 itself with one end. B1492 used them as controls there.
  - On the companion, those two members pull back to one character with a two-dimensional interior (h¹ = 2, r¹ = 0, n = 2).
  - The only banked reading there is sm:B1545's I(W₁) = −1, and both routes reproduce it.
  - So K3 was corrected to the banked component before the record run, and its Λ² value (−2) is recorded as a new reading,
    not a control.
  - It is also a fact in its own right. Two one-generation members of m136 merge, on its companion, into one member that is
    not generation-shaped.
  - It bears on no member of this population, where n = 1 everywhere bounds I(Λ²W₁) ≥ −1.

## 7. Predictions (priors fixed at the seal)

| | prediction | prior |
|---|---|---|
| P1 | the banked identity holds: controls K1–K5 reproduce and every sealed file hashes as sealed | 97% |
| P2 | the routes agree at every member: (h¹, r¹, n), the interior dimension and the generic count | 90% |
| P3 | the orbit law: in each route the three members of every deck orbit read alike | 93% |
| P4 | the theorems at every reading: −1 ≤ I(W₁) ≤ 2, −n ≤ I(Λ²W₁) ≤ 0, Lemma F′; the structure as the census; every gap clean (live ≥ 10⁻²⁰, dead ≤ 10⁻²⁵) | 95% |
| P5 | the three draws read alike at every task | 92% |
| P6 | main's law: every generic reading has I(W₁) = −1 | 80% |
| P7 | the shape follows the square: every sign member reads (−1, −1) and every order-4 member reads (−1, 0) | 55% |
| P8 | the selection: +LLLR's cover is the only one whose generation-shaped members number exactly three | 25% |

**Why these priors.**
- **P6.** On L8a15 every member at every order counts exactly −b0 (main's B1493). m136's companion reads −1 (sm:B1545).
- **P7.**
  - The two shapes are seen on L8a15.
  - The mechanism is general: Λ²(ν ⊗ ρ) = ν² ⊗ Λ²ρ, so the Λ² side lives at the trivial character when ν² = 1 and at a
    sign character otherwise.
  - But no other cover has been read.
- **P8.**
  - −LLLLLR's cover has, like +LLLR's, exactly one sign member orbit.
  - If its members are generation-shaped, as P7 expects, the selection fails.
  - P8 holds only if they are not, or if +LLLR's are not.

A population-wide prediction is True only on complete records: every task with its row, every row with its three draws. A
refuting row decides False whatever the coverage.

## 8. BANKED IDENTITY: checked before reading

`identity.py` checks every sealed file's sha-256 (`ARTIFACT_HASHES.txt`) and re-runs K2–K5 before `run.py` reads
anything. A single difference stops the run.

## 9. Reading rules

- **PROVED (the selection)** if P1–P5 hold on complete records and P8 holds. Then among the thirteen three-ended covers only
  +LLLR's carries exactly three generation-shaped members, and they are its one sign orbit.
- **NEGATIVE (the selection)** if P1–P5 hold on complete records and P8 fails. Then another cover carries exactly three as
  well, or +LLLR's does not. The three-orbit does not single out +LLLR among the three-ended covers. Every cover with
  generation-shaped members is named with their number.
- **OPEN** otherwise.
- Either way the read-out records:
  - the generic counts by cover and order;
  - the generation-shaped members by cover, with their orbits;
  - the covers with exactly three.
- 0 of 19 is unchanged either way. Which object the genesis takes, a companion or a three-ended cover, and which basis of
  a triplet is physical, are GENESIS FK14's.
- **NO NEGATIVE FROM A BUG.**
  - Every count is read in two routes that share no code beyond the cover's action, the characters and the holonomy.
  - Three draws per member.
  - Every member of every orbit is read.
  - The theorems of §3 are checked at every reading.

## 10. What this arc does not decide

- **Characters of other orders** on these covers (8, 3, 12, …): Proposition N bounds order 8 on the companions, not here.
- **The companions themselves**, except +LLLR's, which is its three-ended cover.
- **Non-interior classes** (boundary-type): main's B1492 reads them on L8a15 and o10_150729.
- **Which basis of a triplet is physical** (the members, or the deck charges 1, ω, ω²), **whether the base or the cover is
  the physical space**, and any mass or mixing: GENESIS FK14, and B1391's Schur limit.
