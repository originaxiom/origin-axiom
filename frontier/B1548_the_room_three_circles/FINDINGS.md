# B1548 — THE ROOM-THREE CIRCLES: NEGATIVE — a THREAD result: on the golden cover N₄₅, no class at any point of orders 3 to 60 of the five room-three circles carries three, in either order; every member's one stratum reads (0, −5), and the W₁ side is three short at every reading

cc (the SM-derivation seat), 2026-10-14. **Verdict: NEGATIVE, by the seal's §9.**

**THE WEAVE: a THREAD result.** N₄₅ is a cover of one thread, the degree-45 cover of m003 (sm:B1541). This arc read
characters of that one cover. It answers no weave question, and nothing here is offered as an answer to one. It was
sealed and run at the owner's ruling of 2026-10-14, "Seal and run it, labelled", on a draft held since 2026-10-07.

- **The seal** at `aa350651` (2026-10-14). It was sealed after sm:B1547's read-out, which the seat had read; the seal
  says so.
- **The identity** held at 18:19:44–18:23:13Z (`verification/identity.json`).
- **The run.** As sealed, 18:23:13Z to 19:00:56Z, rc 0, on three workers; one start and no stop. Every task appears
  once and every line is whole (`verification/run_notes.md`). The seat's own session restarted at about 18:53Z; the
  detached run did not, and nothing of it was touched.
- **The record** was committed unread at `7c8c99e9` (`run.jsonl.gz`, `run_sha256.txt`).
- **The read-out.** `read_out.py` ran once, at 19:04:39Z (`0372c9a6`).
- **The post-run tables**, labelled, were committed before their run (`70b80487`, output `7f228285`). They change no
  verdict.
- **Price:** unchanged, 0 of 19.

## Seen first

- **The repo sweep at the seal** (the seal's §0): nine terms over every head, fetched 2026-10-14 at 16:38Z.
  "room-three circle" and "circle of characters" appear only in this arc's own dossier, draft and pointers. No arc
  on any head reads a character of N₄₅ of order 3 or more.
- **The repo sweep after the run** (2026-10-14, after a fetch). The heads were main `6d6f7f66`, the audit lane
  `f0760049`, the web seat's branch `39bfc86f` and the archive branch `efadcdea`. The terms were "room-three circle",
  "boundary Massey" and "circle of characters".
  - Every hit that bears is this seat's own, in its dossier, relays and sm:B1543–B1547.
  - On main and the archive branch, "boundary Massey" appears in rows that read this seat's sm:B1547.
- **Seen before the seal, and disclosed there:** sm:B1547's read-out and FINDINGS. Four of this arc's members, the
  circle's points of order 8, are sm:B1547 members, banked at (0, −5).
- **The literature** (the seal's §0): Dimca, Papadima and Suciu on cohomology jump loci (arXiv:0902.1250). Standing:
  NEW-AS-SWEPT for the circles and the counts at their points of order 3 or more. EXTENDS sm:B1547.

## 1. The question and the design (the seal's §1–§5)

- **The circles.** On N₄₅ the cusp-trivial characters with room three lie on five circles t ↦ exp(2πi·t·φᵢ), one
  τ-orbit. At orders 2 to 5 the room-three characters are exactly their points (control K9).
- **The members.** The 84 points of the circle through χ0 of orders 3, 5, 6, 8, 10, 12, 15, 20, 24, 30, 40 and 60.
  None of these orders divides 4, so b0 = 0 and the room is exactly three. sm:B1547's Corollary 1 and Lemma G then
  hold verbatim: three can live only in a distinct stratum X_U, |U| ≤ 2, and a generic class decides each.
- **The structure, before the seal** (`census.py`). Every member has one distinct stratum, the interior one, of
  dimension 2. Every order but 5 has (h¹, n) = (15, 10) for ν⁵ ⊗ ρ and dim K0^ν = 2. Order 5 has (23, 18) and
  dim K0^ν = 5.
- **The run.** Route R and route F at all 84 members (168 tasks), three draws at each stratum (252 readings per
  route), and route R's load-bearing checks at a generic class of K0^ν and of H¹ at every member (168 readings).

## 2. The read-out (`verification/read_out.json`, `read_out_log.txt`)

| | prediction | prior | result |
|---|---|---|---|
| P1 | the banked identity holds | 97% | holds |
| P2 | the routes agree at every member | 90% | holds |
| P3 | the Galois classes read alike in each route | 88% | holds (fifteen per route) |
| P4 | the theorems at every reading; the room and the strata at every member | 95% | holds |
| P5 | genericity: the draws read alike, with support exactly U | 92% | holds |
| P6 | the floor: every stratum's generic I(W₁) ≥ −2 | 90% | holds |
| P7 | I(W₁) ≥ 0 at every reading | 65% | holds |
| P8 | three: some stratum reads (−3, −3) in both routes | 2% | does not |
| P9 | the load-bearing checks at every member (route R) | 96% | holds (168 of 168) |
| P10 | some stratum generation-shaped in both routes | 8% | does not |

All ten came out as their priors leaned, against 9.03 expected. The records are complete (168 of 168), and no stratum
reads I(W₁) = −3 with I(Λ²W₁) ≤ −3. By §9 the verdict is NEGATIVE.

## 3. The counts

- **Every member's interior stratum reads (0, −5)** at its generic class, in both routes, at every order: 3, 5, 6, 8,
  10, 12, 15, 20, 24, 30, 40 and 60. That includes the four members of order 5, whose structure differs, (23, 18, 5,
  2). The least generic I(W₁) is 0.
- **The four members of order 8 read (0, −5), as sm:B1547 banked them.** They are the same four characters, read
  again by this arc's own sealed run, so the two arcs agree on them.
- **Where three stops** (`verification/post_run_tables.py`, labelled). Three needs s = rk δ¹_{W*} = k + 3 and
  t = rk δ¹_{(Λ²W₁)*} = k + 3 at an interior class.
  - Over all 252 route R stratum readings, s − k = 0. The boundary Massey rank at the interior classes is zero here,
    where three needs three. On sm:B1547's members it reached two.
  - t − k = 5 at every reading. So, as on sm:B1547's members, the Λ² side has room, and the W₁ side is short.
- **The load-bearing checks** (route R, at every member). A generic class of H¹ reads (6, −5) at all 84 members. A
  generic class of K0^ν reads (0, −5) at 80, and (1, −5) at the four of order 5, where it lies on four cusps. Every
  identity and cap holds.

## 4. What it means (a THREAD result)

- **No three on the room-three circles at the orders read.** By the seal's §3.5, no class at any point of order 3, 5,
  6, 8, 10, 12, 15, 20, 24, 30, 40 or 60 of any of the five circles carries three, in either order. That covers
  5 × 84 characters, with the other four circles through the deck symmetry τ (K3) and the other order through
  ν̄ = ν^{m−1}.
- **The count does not move along the circle.** At every order read, every member's one place for three reads
  (0, −5). The circle's room is three everywhere on it, but the boundary Massey map at its interior classes has rank
  zero. So the W₁ side is three short at every member, and is shorter here than on sm:B1547's members (two).
- **N₄₅ on the record now.** No three at the trivial character (sm:B1546), at the 5,120 order-8 members over the
  room-three characters (sm:B1547), or at the circles' points of these orders (this arc).
- **Under THE WEAVE this changes nothing at the weave's level.** It is one cover of one thread. The weave's own count
  is the weave dossier's (`docs/dossiers/the_weave_2026-10-07/NOTE.md`): F-HE's count is (0, 0) at every class on
  every thread at every tick (W11).

## 5. What this arc does not decide

- Points of the circles of other orders, including orders whose roots of unity the two primes lack.
- The circles' points with ν⁴ = 1 (orders 1, 2 and 4), where b0 = 1.
- Room-three characters of N₄₅ off the circles at orders above 5, if any (K9 covers orders 2 to 5).
- Members over the circles that are not on them, beyond sm:B1547's order 8.
- Other covers, and which class and which cover the genesis selects (GENESIS GAP4, FK14, THE_BAR).
- Any weave question.

## 6. The run, disclosed (`verification/run_notes.md`)

- **The machine.** The seal said the run would start when the seat's W80 ended, and it did. Three workers, not four,
  for memory headroom, after sm:B1547's lesson.
- **A slip of the seat's shell at the launch.** A foreground `cat` of the log read an unset path. The launch was not
  affected.
- **The seat's session restarted at about 18:53Z.** The detached run continued: its process and three workers were
  alive, at 133 of 168. The waiter and the pre-push suite were started again.

## Files

- `PREREGISTRATION.md`: the seal (sha-256 in `docs/SEAL_LEDGER.md`); `ARTIFACT_HASHES.txt`: the nine sealed files.
- `verification/circle_lib.py`, `run.py`, `read_out.py`, `controls.py`, `identity.py`, `census.py`: the instruments;
  `controls.json`, `census.json`, `identity.json`: the checks before the run.
- `verification/run.jsonl.gz`, `run_sha256.txt`, `run_notes.md`: the record and its notes.
- `verification/read_out.json`, `read_out_log.txt`, `read_out_time.txt`: the read-out, once.
- `verification/post_run_tables.py` → `post_run_tables.json`: the labelled tables after the read-out.
- Lock: `tests/test_b1548_the_room_three_circles.py`.
