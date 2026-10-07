# B1547 — THE ROOM-THREE MEMBERS: NEGATIVE — on the golden cover N₄₅, no class at any order-8 character trivial on every cusp over the five room-three characters carries three, in either order; the least I(W₁) is −2, and the W₁ side stops two short at every stratum

cc (the SM-derivation seat), 2026-10-07. **Verdict: NEGATIVE, by the seal's §9.** Sealed at `32cc4ff6` (2026-10-06).
- **The identity.** It held at 23:35:31–23:46:27Z on 2026-10-06 (`verification/identity.json`).
- **The run.** As sealed, 23:46:27Z to 04:25:41Z on 2026-10-07, rc 0, every task once and every line whole. Two stops by exact
  PID, both resumed by the sealed `run.py` on whole tasks with the sealed seeds (§6, and `verification/run_notes.md`):
  - at 00:03:44Z, to move from three workers to four;
  - at 04:24:14Z, after the kernel's memory limit had killed three workers and the pool hung on their three tasks.
- **The record** was committed unread at `2ad01176` (`run.jsonl.gz`, `run_sha256.txt`).
- **The read-out.** `read_out.py` ran once, at 04:29:29Z (`d0c3592f`).
- **Price:** unchanged, 0 of 19.

## Seen first

- **The repo sweep at the seal** (the seal's §0): twelve terms over every head, fetched 2026-10-06 at 22:43Z.
  - "resonance variet" and "characteristic variet" are absent; "common loops" is only in this arc's own files.
  - "golden member" names two other objects, so this arc's members are called the room-three members.
  - "cusp-trivial", "room 3" and "fourth root" lead to this seat's own sm:B1535–B1546, none of which reads a character of N₄₅
    other than the trivial one.
- **The repo sweep after the run.** `git fetch --all` (2026-10-07, 06:27Z), then `scripts/checks/prior_work.py` over every
  head with six terms: "boundary Massey", "room-three member", "order-8 member", "Massey map", "s - k", "generation-shaped
  stratum".
  - The heads were this branch (`d0c3592f`), main (`5ef37c79`), the audit lane's two branches (`8b89d8fb`, `c161981d`), the new
    web seat's branch (…/web-seat, `d40c1ab6`), the other seat branches and sep16-branch (`3205984b`).
  - Every hit that bears is this seat's own: sm:B1535's Theorem C, sm:B1543–B1546's cup-map and Massey arcs, this arc's seal,
    and this seat's relays.
  - main's B143 names a Massey product of the 3-chain link, another object.
  - main's B1492 (S72) read this seat's frame at the sign characters of two companions and rowed this arc's read-out at
    headline level. Nothing on any head reads these members.
- **The literature** (the seal's §0):
  - Dimca, Papadima and Suciu on cohomology jump loci (arXiv:0902.1250);
  - Menal-Ferrer and Porti (arXiv:1001.2242);
  - Nosaka's triple cup products (arXiv:1808.08532).

  None computes these members. Standing: NEW-AS-SWEPT for the strata of these members and their counts.

## 1. The question and the design (the seal's §1–§5)

- **The members.** On N₄₅ (m003's d9.2 along the golden order; five cusps; a degree-9 cover of m003's companion
  o10_150729), the characters ν of order 8, trivial on every cusp, with ν⁴ = χ0.
  - χ0 is the room-three order-2 character with the least key. There are 1024 members, all with b0 = 0, room exactly three,
    and all five cusps trivial.
  - The five room-three characters are one orbit of the deck symmetry τ, so χ0's members stand for all 5 × 1024.
- **Corollary 1** (proved at design time). A class reading I(W₁) = −3 has r = 0 and s = k + 3, and vanishes on at least three
  cusps. So it lies in a distinct stratum X_U = K0^ν ∩ {c vanishes off U}, |U| ≤ 2, with support exactly U.
- **Lemma G.** On the classes of support U, a generic class of X_U has the least I(W₁) and the least I(Λ²W₁).
- **The population.** Both routes at every member: 2048 tasks, 424 distinct strata at 220 members, three draws each. In route R
  also a generic class of K0^ν and one of H¹ at every member (1,920 load-bearing readings).

## 2. The read-out (`verification/read_out.json`, `read_out_log.txt`)

| | prediction | prior | outcome |
|---|---|---|---|
| P1 | the banked identity: K1–K8 reproduce, every sealed file hashes as sealed | 97% | **holds** |
| P2 | the routes agree at every member: structure, every X_U, the distinct strata, every generic reading | 90% | **holds**: 1024 of 1024 |
| P3 | Lemma Γ: the four members of every Galois class read alike, in each route | 90% | **holds**: 256 classes per route |
| P4 | the theorems at every reading (rk δ¹_W = 0, support in U, Lemma F′, the caps, route R's identities, the nesting) | 95% | **holds**: no reading fails |
| P5 | genericity: every stratum's three draws read alike, each with support exactly U | 92% | **holds** |
| P6 | the floor: every distinct stratum's generic reading has I(W₁) ≥ −2 | 80% | **holds** |
| P7 | I(W₁) ≥ 0 at every reading | 30% | fails |
| P8 | three: some stratum's generic reading is (−3, −3) in both routes | 7% | fails |
| P9 | the load-bearing checks at every member (route R) | 96% | **holds**: 1,920 readings |
| P10 | some stratum's generic reading is generation-shaped, I(W₁) = I(Λ²W₁) < 0, in both routes | 25% | fails |

7 of 10 hold, against 7.02 expected. **Verdict: NEGATIVE.** P1, P2, P4 and P9 hold on complete records, and no distinct
stratum's generic reading has I(W₁) = −3 in either route.

## 3. The counts

**Every distinct stratum's generic count**, alike in route R and route F at every member:

| member structure (h¹(ν⁵ρ), n(ν⁵ρ), dim K0, its interior part) | members | with a distinct stratum | generic counts |
|---|---|---|---|
| (5, 0, 5, 0) | 528 | 56 | (−2, 0) on one cusp ×120; (−1, 0) on two ×96; (−2, 0) on two ×32 |
| (8, 3, 3, 1) | 48 | 48 | interior (−2, −3) ×48; on one cusp (−1, −2) ×12 |
| (8, 3, 4, 3) | 12 | 12 | interior (−2, −3) ×12 |
| (9, 4, 5, 4) | 96 | 96 | interior (−2, −1) ×96 |
| (13, 8, 2, 2) | 4 | 4 | interior (0, −3) ×4 |
| (15, 10, 2, 2) | 4 | 4 | interior (0, −5) ×4 |
| (6, 1, 0, 0), (7, 2, 1, 0), (8, 3, 0, 0), (9, 4, 2, 0) | 332 | 0 | — |

- **The least generic I(W₁) is −2**, at 308 strata in each route, on the interior and on one and two cusps.
- No stratum reads (−3, −3) or I(W₁) = −3 with Λ² below. None is generation-shaped.
- **Where it stops** (`verification/post_run_tables.py` → `post_run_tables.json`, from the committed record after the
  read-out). Three needs s = rk δ¹_{W*} = k + 3 and t = rk δ¹_{(Λ²W₁)*} = k + 3.
  - Over all 1,272 route R stratum readings, s − k is 2 at 924, 1 at 324 and 0 at 24. It is never 3.
  - t − k reaches 3 at 192 readings and 5 at 12.
  - **So the W₁ side is the one short.** At an interior class s − k is the rank of the boundary Massey map β ↦ [w(β)] (this
    seat's relay of 2026-10-07, §2(a)), into a space of dimension m_A = 5. It never exceeds 2, although n(L) = 3 leaves room
    for 3.
- **The load-bearing checks** (route R, a generic class of K0^ν and of H¹ at every member, support on every cusp): all hold.
  Their counts pair a positive I(W₁) with a negative I(Λ²W₁) up to (6, −5): (3, −3) at 120 members, (4, −4) at 12, (5, −5)
  at 4. None is generation-shaped.

## 4. What it means

- **No three at these members.** By the seal's §3.5, no class at any member trivial on every cusp over the five room-three
  characters carries three, in either order. N₄₅ now carries no three:
  - at the trivial character, at any class (sm:B1546);
  - at these 5,120 order-8 characters, at any class (this arc).
- **The order of the character moves the count and the ends do not.** main's B1492 read the sign characters of L8a15 and
  o10_150729 and found one at every member. Here, at order 8 with b0 = 0 and every end trivial, the count reaches two but
  never three, and never in the generation shape.
- **Where three is short.** In the boundary Massey map at interior classes (s − k ≤ 2), and in its analogue on one and two
  cusps. Not in the line's room n(L) = 3, and not in the Λ² side.
- **For the owner's question of 2026-10-07** ("what if the three generations dont emerge at once or in one place, but as a
  process in more steps"). This is one more place that holds no three at once. On the record the counts that reach one come
  one per member, and on the only three-ended companion its three members are one orbit of the deck symmetry
  (`docs/dossiers/the_three_orbit_2026-10-07/NOTE.md`).

## 5. What this arc does not decide

- Members over the five that are not trivial on every cusp. Members with ν⁴ = 1 (b0 = 1). Members whose fourth power has order
  three or more: the circle points of `docs/dossiers/room_three_circles_2026-10-07/`, whose arc is held pending the owner's
  ruling.
- The special classes of a stratum. No stratum reached I(W₁) = −3, so the seal's case (d) did not arise.
- Other covers, and which class and which cover the genesis selects (GENESIS GAP4, FK14 and THE_BAR).

## 6. The run, disclosed (`verification/run_notes.md`)

- **The start.** It began on three workers at 23:46:27Z, after the identity.
- **The first stop.** It was stopped by exact PID at 00:03:44Z, after 148 whole rows, and relaunched on four workers at
  00:03:49Z.
- **The memory kills.** On 2026-10-07 the kernel's memory limit killed three of the four workers, at about 01:45:42Z,
  02:14:28Z and 02:40:58Z. Their resident sizes were 3.6–5.1 GB, and the seat's other jobs shared the memory then.
- **The hang and the second stop.** The three tasks they held (route R, members 611, 743, 910) never returned, and the pool
  waited from 03:42Z. It was stopped by exact PID at 04:24:14Z, launcher first, and relaunched on two workers at 04:24:25Z. It
  read those three tasks in 31–46 s each and ended with rc 0 at 04:25:41Z.
- **A shell slip.** While writing the run notes, backquotes in an unquoted here-document ran a stray `gzip`, which waited on
  its input until killed by exact PID. It touched no file: the gzipped record decompresses to the raw record's sha-256, and
  no read-out file existed.

## Files

- `PREREGISTRATION.md`, `ARTIFACT_HASHES.txt`: the seal.
- `verification/`:
  - the sealed code: `member_lib.py`, `run.py`, `read_out.py`, `controls.py` (`controls.json`), `identity.py`
    (`identity.json`);
  - `run_notes.md`;
  - the record: `run.jsonl.gz` with `run_sha256.txt`;
  - the read-out: `read_out.json`, `read_out_log.txt`;
  - `post_run_tables.py` → `post_run_tables.json`.
- Lock: `tests/test_b1547_the_room_three_members.py`.
