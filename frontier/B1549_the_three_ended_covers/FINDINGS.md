# B1549 — THE THREE-ENDED COVERS: NEGATIVE for the selection — +LLLR's is not the only three-ended cover that carries exactly three generation-shaped members: −LLLLLR's carries the same three; on every three-ended cover of the family every sign member reads one generation, (−1, −1), and no member of order four does

cc (the SM-derivation seat), 2026-10-07. **Verdict: NEGATIVE, by the seal's §9.** Sealed at `033f8a8e`.
- **The identity.** It held at 08:44:54–08:47:40Z (`verification/identity.json`).
- **The run.** 08:47:40Z to 09:30:13Z, rc 0, every task once.
  - It was stopped once, at 09:14:54Z, by this session's 30-minute limit on background commands, which the seat had not
    raised. At that point 226 rows were whole and no task appeared twice.
  - The sealed `run.py` resumed at 09:24:18Z on the remaining 50 tasks with their sealed seeds (`verification/run_notes.md`).
- **The record** was committed unread at `04bc0333`.
- **The read-out.** `read_out.py` ran once, at 09:30:50Z (`2839d7cf`).
- **Price:** unchanged, 0 of 19.

## Seen first

- **The repo sweep at the seal** (the seal's §0): eight terms over every head, fetched 2026-10-07 at 08:28Z.
  - "three-ended cover", "Delta(48)" and "Z/2 x A4" are absent.
  - "three-ended" leads only to main's B1491 and B1492 on L8a15, and to this seat's three-orbit note.
  - This seat's B1356 has a triple as a free ℤ/3 orbit with A₄ around it, on another object and frame.
  - B1391 has the Schur limit on generations that form a representation of a symmetry.
  - B1255 has the pattern of the lost three-nesses.
- **The repo sweep after the run.** `git fetch --all` (2026-10-07, 09:32Z), then `scripts/checks/prior_work.py` over every
  head with five terms: "three-ended cover", "orbit in one module", "sign member", "generation-shaped member", "mirror
  shape".
  - "three-ended cover" and "sign member" lead only to this seat's own files.
  - "mirror shape" names other objects (B775, docs/WHAT_WOULD_COUNT.md).
  - **"orbit in one module" is main's B1495, sealed at `3c1fadd9`.** It reads L8a15's three members as one rank-15 module
    W₁(ν) ⊕ W₁(τν) ⊕ W₁(τ²ν), whose Λ² count is −3 plus three cross terms.
  - Nothing on any head reads another three-ended cover.
- **The literature** (the seal's §0):
  - Altarelli, Feruglio and Lin, A₄ from the orbifold T²/ℤ₂ (Nucl. Phys. B 775 (2007) 31, hep-ph/0610165);
  - Adulpravitchai, Blum and Lindner (arXiv:0906.0468);
  - the A₄ lepton assignments of Ma–Rajasekaran (PRD 64 (2001) 113012) and Altarelli–Feruglio (NPB 720 (2005) 64);
  - the Δ(3n²) groups of Luhn, Nasri and Ramond (J. Math. Phys. 48 (2007) 073501).

  None reads a 3-manifold's covers. Standing: NEW-AS-SWEPT for the three-ended covers of the family, their members, orbits
  and counts.

## 1. The question and the design (the seal's §1–§5)

- **The covers.** Every state whose companion's number of ends is divisible by 3 has a three-ended cover, a degree-3
  quotient of its companion. To twelve ends there are thirteen covers on ten states.
- **What is proved at design time.**
  - n(1) = 0 on each cover (checked exactly, K5). So by Theorem C every member carries at most one generation.
  - At these members n = 1 and m_A = 0. So I(W₁) ∈ [−1, 2] (Lemma F′ and the ceiling) and I(Λ²W₁) ∈ [−1, 0].
  - The three members of a deck orbit read alike.
- **The population.** Every member at characters of order dividing 4, censused at 50 digits in two routes and two rank
  methods: 46 free ℤ/3 orbits, 138 members.
  - 6 orbits are of sign characters, inducing ℤ/2 × A₄ triplets.
  - 40 are of order 4, inducing triplets with determinant-one part Δ(48).
- **The claim tested (the selection).** +LLLR's cover, its companion L8a15, is the only one of the thirteen whose
  generation-shaped members number exactly three.

## 2. The read-out (`verification/read_out.json`, `read_out_log.txt`)

| | prediction | prior | outcome |
|---|---|---|---|
| P1 | the banked identity: K1–K5 reproduce, every sealed file hashes as sealed | 97% | **holds** |
| P2 | the routes agree at every member: (h¹, r¹, n), the interior dimension, the generic count | 90% | **holds**: 138 of 138 |
| P3 | the orbit law: the three members of every orbit read alike, in each route | 93% | **holds**: 46 orbits |
| P4 | the theorems at every reading, the structure as the census, every gap clean | 95% | **holds** |
| P5 | the three draws read alike at every task | 92% | **holds** |
| P6 | main's law: every generic reading has I(W₁) = −1 | 80% | fails at 84 members (168 task readings) |
| P7 | sign members (−1, −1), order-4 members (−1, 0) | 55% | fails, at the same 84 order-4 members |
| P8 | the selection: +LLLR's cover the only one with exactly three generation-shaped members | 25% | **fails: +LLLR's and −LLLLLR's** |

5 of 8 hold, against 6.27 expected. **Verdict: NEGATIVE.** P1–P5 hold on complete records (276 of 276 tasks, three draws
each), and P8 fails.

## 3. The counts

Every member's generic count, alike in route P and route S, and alike across each orbit:

| cover (state; companion's ends) | sign members | order-4 members | generation-shaped |
|---|---|---|---|
| +LLLR (3; L8a15) | 3 at (−1, −1): one ℤ/2 × A₄ orbit | 6 at (−1, 0) | **3** |
| −LLLLLR (9) | 3 at (−1, −1): one ℤ/2 × A₄ orbit | 6 at (−1, 0) | **3** |
| −LLR (6) | 6 at (−1, −1): two orbits | 12 at (−1, 0), 12 at (0, −1), 12 at (0, 0) | 6 |
| +LLLLLLR (6) | 6 at (−1, −1): two orbits | 12 at (−1, 0) | 6 |
| +LLLRR (6) | — | 12 at (0, −1) | 0 |
| −LLLLRR (12) | — | 24 at (0, −1) | 0 |
| +LLLLLLRR (12) | — | 24 at (0, −1) | 0 |
| −LLRLR, +LLLRRR (four covers), +LLLLRRR | no members | — | 0 |

- **Every sign member reads (−1, −1).** That is all 18, on all four covers that have them. The generation shape sits
  exactly on the sign characters: no member of order 4 has it.
- **The order-4 members read in three shapes.**
  - (−1, 0), main's shape on L8a15: 36 members.
  - (0, −1), the mirror shape, one in Λ² and none in W₁: 72 members.
  - (0, 0): 12 members, on −LLR.
  - The mirror shape holds every order-4 member of the three covers without sign members.
- **No reading goes below (−1, −1).** Theorem C's cap holds everywhere, as P4 checked.

## 4. What it means

- **The three-orbit does not select +LLLR.** Among the thirteen three-ended covers of the family, two carry exactly three
  generation-shaped members, +LLLR's and −LLLLLR's, and with the same pattern. Proposition A still stands for the
  companions: only +LLLR's companion has three ends. So whether three selects +LLLR depends on which object the genesis
  takes. GENESIS FK14 holds that question.
- **The A₄ triplets are the family's, not one state's.**
  - On every three-ended cover each sign orbit is generation-shaped, member by member. That is six ℤ/2 × A₄ triplets on
    four states.
  - Six states have |2 − tr φ| divisible by 3 and no such orbit: +LLLRR, +LLLRRR and the four twelve-ended ones.
- **The generation shape follows ν² = 1.** At order 4, Λ²(ν ⊗ ρ) = ν² ⊗ Λ²ρ lives at a sign character, and no member
  there is generation-shaped. This holds on every cover read, so main's B1493 observation on L8a15 extends to the family's
  three-ended covers.
- **Main's law "every member counts −b0" holds at sign characters and fails at order 4.** 84 order-4 members read
  I(W₁) = 0 instead of −1. The mirror shape (0, −1) is new on the record.
- **For main's B1495** (the orbit in one module, sealed on L8a15). −LLLLLR's cover carries an orbit of the same shape, so
  the same rank-15 module can be read there. If B1495's cross terms vanish on L8a15, the question becomes whether they
  vanish on −LLLLLR's cover too.
- **For the owner's question** ("three as a process in more steps").
  - On these objects three still never comes at once: each member carries at most one generation (Theorem C, n(1) = 0).
  - Where three ones come together they are one deck orbit, a triplet of A₄. That happens on two states, not one.

## 5. What this arc does not decide

- **Characters of other orders** on these covers (3, 8, 12, …).
- **Non-interior classes.**
- **Whether three is a sum over the orbit:** main's B1495 asks it on L8a15.
- **Which object the genesis takes** (a companion or a three-ended cover), **which basis of a triplet is physical**, and any
  mass or mixing: GENESIS FK14, and B1391's Schur limit.
- **States beyond twelve ends.**

## 6. The run, disclosed (`verification/run_notes.md`)

- **The start.** It began on three workers at 08:47:40Z, chained to the identity.
- **The stop.**
  - The whole chain ran as one background command of this session, and the session stops such commands after 30 minutes
    unless the limit is raised. The seat had not raised it.
  - It was stopped at 09:14:54Z, 30 minutes after the chain began. The record's last write is at 09:14:53Z.
  - The stop wrote no exit code, and no worker survived.
- **The resume.** At 09:24:18Z the same command, with a two-hour limit, read the 50 remaining tasks (226 done) and ended at
  09:30:13Z with rc 0. run.py skips every task with a row, and every task's draws are seeded by its own key. So no reading
  depends on the stop.
- **The record.** It holds 276 rows, each task once with three draws. It was checked by key before it was read, and
  committed unread.

## Files

- `PREREGISTRATION.md`, `ARTIFACT_HASHES.txt`: the seal.
- `verification/`:
  - the sealed code: `three_lib.py`, `census.py`, `run.py`, `read_out.py`, `controls.py`, `identity.py`;
  - `population.json`, with `census_0.jsonl.gz`, `census_1.jsonl.gz` and `census_sha256.txt`;
  - `controls.json`, `controls_trial.json`, `identity.json`;
  - `run_notes.md`;
  - the record: `run.jsonl.gz` with `run_sha256.txt`;
  - the read-out: `read_out.json`, `read_out_log.txt`.
- Lock: `tests/test_b1549_the_three_ended_covers.py`.
