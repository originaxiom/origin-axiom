# B1533 — GENESIS v1.10: MAIN'S v1.9 AS THE HEAD, THE SEAT'S v1.8 LINES CARRIED, AND GAP6 SCOPED BY THE RECORD (THE CHERN–WEIL ROW IS THE DIRAC INDEX'S; THE CLASS INDEX COUNTS +1, −1 AND 0 ON THREE FLAT MODULES OF ONE RANK)

**Date:** 2026-10-03. **Verdict: PROVED.** Eight checks, C1–C8 (`verification/genesis_v110_checks.py`, a few seconds), all
pass.
- C1–C7 were run and passed before GENESIS.md was written. The pre-write log is kept (`genesis_v110_checks_prewrite_run.txt`).
- The run after writing (`genesis_v110_checks_run.txt`, `genesis_v110_checks.json`) adds C8: GENESIS.md is the generator's
  output, byte for byte, with four [v1.10] and four [v1.8] marks, and undoing the changes gives main's v1.9.

**Not sealed.** Each check reads a banked record, re-derives a fact a record states, or compares texts. No open outcome is
computed. **creates_law is false.** 0 of 19 Standard-Model parameters; I-26 stays UNEARNED.

**Source.**
- **Main's ask.** Its relay of 2026-10-03 (`CC_TO_SM_AND_CODEX_2026-10-03_THE_COUNT_IS_A_BIT_AND_THE_MIXING_QUARTIC.md`, main's
  B1466, kept as received in `received/`): *"Please take v1.9 as head."*
- **The owner's instructions**, still binding: nothing load-bearing ignored; every negative checked by two routes so that none
  comes from a bug. GENESIS v1.9's new gap GAP6, read as written, would set aside every count the record has made in a flat
  frame. That makes it load-bearing, so it is checked here against the record it cites.

## Seen first (the repo sweep and the literature)

**The repo sweep**, before any GENESIS text was written.
- `git fetch --all`: main had moved from `b3565230` to `3f8dc11a` (S49, B1466). The other heads had not moved. None was merged.
- **Main's B1466**, read in full where it bears: FINDINGS (§1's table: the two orders count −1 and +1, their sum 0),
  `adoption/amend.py`, its received copy of main's own v1.8, its relay.
  - Main's v1.8 (B1463, `d2a95da4`) is main's v1.7 with its version line and one log entry (C1).
  - Main's v1.9 is main's v1.8 with exactly the five changes its amend.py lists (C1).
- **The SM seat's v1.8 (sm:B1528)** was made on main's v1.7 at the same time as main's v1.8, numbered the same, and relayed
  (`SM_TO_CC_AND_CODEX_2026-10-03_GENESIS_V1_8.md`, OPEN). Main's v1.9 carries none of its three content changes (C2).
  Main's relay does not mention them.
- **The record's Chern–Weil row**, which GENESIS GAP6 cites, is main's B1420 (A4). It is the only verdict row on main that
  names Chern–Weil (C3), read at source:
  - "Chern–Weil: a flat bundle has zero curvature ⇒ rational Chern classes vanish ⇒ ch(V) = rk(V); Atiyah–Singer then gives
    ind D_V = rk(V)·(−σ/8) on a closed spin 4-manifold: **rank-blind**."
  - The second edge B1420 states itself: "the non-zero values on reducible non-split modules are flat data too, so they are
    not four-dimensional Dirac indices either; they are counts of twisted classes".
- **Main's L244**, the lead behind GAP6, read in full. Its item (a) asks for the three-kind taxonomy as a census, and says "A
  fourth kind refutes the taxonomy". Its item (c) owes the ensemble and symmetry of the Hagedorn point. sm:B1531 (banked
  2026-10-03) did both for the same reading, which the owner forwarded to both seats (this seat's "chat 1", main's "web
  seat"). Main had not read sm:B1531 when it wrote v1.9.
- **Main's B1465**, read: its four run logs, FINDINGS and relay (C7).
- `scripts/checks/prior_work.py` ran on seven terms: "GENESIS v1.10", "Version 1.10", "GAP6", "rank-blind", "take v1.9 as
  head", "fourth kind", "Chern-Weil row".
  - "GENESIS v1.10", "Version 1.10" and "Chern-Weil row" are on no head.
  - "GAP6", "rank-blind" and "take v1.9 as head" hit only B1420, B1466, main's GENESIS v1.9 and its ledgers, all read above.
  - "fourth kind" hits main's L244 and B750. B750's three classes (no point, no width, no name) sort the object's refusals,
    not the negatives, and do not bear here.

**The literature:** none beyond the record. Chern–Weil and Atiyah–Singer enter only as B1420 states them, and Lichnerowicz
only as sm:B1503 states it. Every other item is a statement about the record's texts, or a finite computation on one member
of m004's level M₄ with sm:B1515's two routes, both already on the record.

## 1. What v1.10 is

Main's v1.9, kept as received, with eleven changes (`verification/merge_genesis_v110.py`). Each change is an exact string of
the text it applies to, asserted to occur once.
- **The SM seat's v1.8 lines, as they were** (three changes, imported from sm:B1528's own merge, marked [v1.8]):
  - GENESIS FK12 (ii): the meridian sign made exact (a meridian twist enters squared; P fixes Ballas' family);
  - GENESIS FK9: sL-10 item 8 answered near the hyperbolic point (sm:B1527);
  - §8's frontier: the same, with what stays open there.
- **The version line and one intro sentence**, naming both v1.8s and v1.10.
- **GENESIS GAP6: its scope, from the record** (§3; marked [v1.10]).
- **GENESIS FK9: Part H verified on main** (B1465; marked [v1.10]).
- **GENESIS FK12 (ii): main's B1465 states the twisted identity in the same form** (marked [v1.10]).
- **§7's heading**: "Five gaps" becomes "Six gaps". v1.9 added GAP6 under the old count.
- **§10**: the SM seat's v1.8 entry, after main's v1.8, labelled "v1.8 on the SM seat's branch" as the v1.1 precedent is; and
  the v1.10 entry.

Nothing of main's v1.9 is deleted or reworded, except the one count in §7's heading. Undoing the eleven changes gives main's
v1.9 byte for byte (C8). No status changes: GENESIS FK1 and FK12 stay as the owner decided, and the fork table's statuses are
main's (C8).

## 2. The checks

| | check | result |
|---|---|---|
| C1 | the received texts; main's two steps | main's amend.py on main's v1.8 gives main's v1.9 byte for byte (5 changes); main's v1.8 = v1.7 + the version line + a 5-line log entry; the four received copies equal main's blobs |
| C2 | the SM seat's v1.8 lines | sm:B1528's changes on main's v1.7 give the seat's v1.8 byte for byte; its three content changes each find their anchor once in main's v1.9, which carries none of them |
| C3 | the Chern–Weil row | B1420's A4, the only such verdict row on main: the Dirac index on a closed spin 4-manifold, rank-blind, with the second edge stated there; sm:B1531 §3 scoped GAP6's sentence the same way |
| C4 | own code, two routes | on M₄ at ν = (1/3, 0), λ = 1: the non-split W₁, its dual and V ⊕ L are flat of rank five with h¹ = 2 each, and count +1, −1 and 0 in route T (GF(16640761)) and route L (GF(4060801)); sm:B1515's banked rows agree (I(W₁) = 1, I(W₂) = −1 at both its primes) |
| C5 | the frames with curvature or a singular point | sm:B1397 (flux caps), sm:B1502 (no rational flux at the cone point), sm:B1503 (positive scalar curvature, index zero), sm:B1351 and sm:B1392 as banked; sm:B1531 puts B1397 and B1503 in none of the three kinds; GAP3's end flux (R41, R80) |
| C6 | L244 (a) on the chirality chain | sm:B1531's 26 records recounted: symmetry 8, flatness 3, non-uniqueness 3, none 12, nine of the twelve frame arithmetic |
| C7 | main's B1465 and B1466, read | 7 364 rows, 0 non-zero (1 092 + 1 428 + 1 764 + 3 080); main states ι̃*V ≅ V* ⊗ ε ⊗ λ²; B1466 counts −1, +1 and 0 on the two orders and their sum |
| C8 | GENESIS.md after writing | the generator's output byte for byte; four [v1.10] and four [v1.8] marks; undoing the changes gives main's v1.9; the fork statuses are main's |

## 3. GENESIS GAP6, scoped by the record

**What GENESIS v1.9 says.** "Every frame on this page is a frame of flat bundles, and a flat bundle has ch = rk: no index
built on it can tell 27 from 27̄ (Chern–Weil; the record's Chern–Weil row). … The remedy for this one is a frame with
curvature; none is on the record."

**What the row it cites says.** B1420's A4 is about the Dirac index on a closed spin 4-manifold, ind D_V = rk(V)·(−σ/8),
which is rank-blind. B1420 states the other edge in the same paragraph: the non-zero values on non-split modules "are flat
data too", counts of twisted classes, not Dirac indices. So the sentence is true of Dirac indices. As GENESIS v1.9 words it,
"no index built on it", it covers more than its row.

**Where it holds** (sm:B1531 §3 had sorted this before v1.9 was written):
- for the Dirac index (B1420);
- for every count on a closed or sealed problem (sm:B1351: a local system's Euler characteristic on a closed 3-manifold is
  zero; sm:B1392: sealed ends are Fredholm and count 0);
- for flux counts where there is no flux (sm:B1502).

**Where it does not hold: B1297's class index**, which reads the open end and is not a characteristic number. C4 computes this
with own code, by two routes that share no code:
- the level M₄ of m004, at sm:B1515's member ν = (1/3, 0), λ = 1;
- three flat modules of rank five: the non-split W₁ = [[ν ⊗ ρ, c·L], [0, L]], its dual W₁*, and the split V ⊕ L;
- flat, so of one Chern character (Chern–Weil: ch = rk = 5 for each);
- h¹ = 2 for each, so the bulk cohomology does not separate them either;
- class index **+1, −1 and 0**, in route T (GF(16640761)) and route L (GF(4060801)), term by term.

The difference is in the cusp data, which is where GENESIS GAP2 places the counts. The cusp-fixed part of W₁ has dimension 1
and that of W₁* has dimension 2 (t₀ = 1, s₀ = 2 in B1297's notation).
Main's B1466 finds the same pattern at its counted point: −1 and +1 on the two orders, 0 on their sum. sm:B1531's C4 finds it
on m135, exactly: the split vacuum (0, 0), W₁ (−1, −1), W₂ (+1, +1).

**So a flat frame's count can tell a module from its dual.** In sm:B1515's frame (F-HE) the dictionary reads N(10′) = −I(W),
so W₁ and W₁* carry opposite 10′ counts. Whether such a count is a physical chirality is GENESIS GAP1, the dictionary
(I-26, UNEARNED), and that gap is unchanged.

**Frames with curvature or a singular point are on the record**, each with its outcome (C5):
- sm:B1397's flux caps: chirality linear in the charges, and even in every E₆ frame;
- sm:B1502's cone points: no rational flux at the apex;
- sm:B1503's apex index: zero, because the links have positive scalar curvature (Lichnerowicz);
- the audit lane's end flux, which may pay GENESIS GAP3's balance (R41, R80).

So curvature alone is not what the record found missing. What it found missing is a frame with curvature whose arithmetic
allows three (sm:B1531, lead (c)).

**v1.10's [v1.10] note at GAP6 says these things, in the record's words.** It withdraws nothing of main's: the gap stands as
the gap of the Dirac index and of the dictionary, with its scope stated.

## 4. Lead L244 (a), on the chirality chain

Main's L244 (a) asks whether every negative sorts into the three kinds (symmetry, curvature, uniqueness): "A fourth kind
refutes the taxonomy".

sm:B1531 read the chirality chain's 26 negative records (the reading of 2026-09-30) one by one, as data (C6):
- symmetry 8;
- flatness 3;
- non-uniqueness 3;
- none of the three, 12. Nine of these are frame arithmetic: the frame's representation theory and charge lattices forbid the
  target, with no symmetry at work and nothing missing in curvature or uniqueness.

**The chain has a fourth kind.** v1.10 records this at GENESIS GAP6. It is the seat's reading of 26 records, kept as data in
sm:B1531's record, not a theorem about the kill graph's 821. sm:B1531 C2 also tallies the kill graph's families. The census of
the whole graph that L244 (a) asks for is main's to make.

## 5. Part H verified on main; the twisted identity in main's form

- **GENESIS FK9.** Main's B1465 verifies sm:B1527's Part H (the hyperbolic point itself) by a route sharing nothing with the
  seat's: on ±LLRLRR and ±L³RLR², at the parabolic points of their periodic curves, for every fibre character and seven
  twists λ of the meridian, **7 364 indices, all zero** (C7: its four run logs sum to 1 092 + 1 428 + 1 764 + 3 080, with
  none non-zero).
- **GENESIS FK12 (ii).** The seat's v1.8 sentence says a meridian twist enters squared. Main's B1465 states the identity in
  the same form, ι̃*V ≅ V* ⊗ ε ⊗ λ², and computes the twisted half where B1459's theorem does not reach.

## 6. The two v1.8s

Main's v1.8 (B1463) and the SM seat's (sm:B1528) were both made on main's v1.7 and given the same number. Their additions are
disjoint: a log line on main's side, three content lines on the seat's. v1.10 carries both. Main's v1.8 is the v1.8 of the
version log's main line. The seat's appears as "v1.8 on the SM seat's branch", as sm:B1517's v1.1 did. All three texts are
kept as received in `received/`.

The relay row of the seat's v1.8 (`SM_TO_CC_AND_CODEX_2026-10-03_GENESIS_V1_8.md`) stays OPEN. Main has not answered it, and
v1.10's relay points to it.

## 7. The locks

- `tests/test_b1533_genesis_v110.py` locks:
  - the received texts by sha-256;
  - GENESIS.md as the generator's output;
  - the record, with C4 live in both routes;
  - v1.10's text and marks;
  - Gate 5-Q, vendor words and the private term;
  - the ledgers.
- **B1528's lock, repointed.** It read v1.8 from GENESIS.md. v1.8 is kept byte-identical in this arc's `received/`
  (`GENESIS_v1_8_sm.md`, sha-256 `b4330544…`), and the tests that read v1.8 read it there. This is B1528's own pattern for
  B1526's lock. The README tests of B1526 and B1528 accept v1.10.

## 8. What this arc does not do

- It does not re-derive main's B1466 or B1465. It reads them, and computes with its own code only where GENESIS GAP6's scope
  needed a computation (C4).
- It changes no status in GENESIS. FK1 and FK12 stay as the owner decided. GENESIS GAP6 stays a gap, scoped.
- It does not answer main's ask of the audit lane (the mixing quartic d of R76's potential). That number is the audit lane's.
- **0 of 19.** I-26 stays UNEARNED.

## 9. Errors caught in this arc

- **C2, first form** (an E52 instance; ERROR_LEDGER). It took the inserted text as new.replace(old, ""). That deletes nothing
  when a change edits its anchor's last character, so the check searched for main's own words and failed on its first run.
  It now compares the common prefix and suffix. No false pass occurred.
- **sm:B1531's bank** (a bank slip; ERROR_LEDGER). The lane caught it: `test_no_ai_labels_in_living_docs`. B1531 had
  written the owner's label for another conversation into two living docs, `docs/OPEN_LEADS.md` and `docs/ERROR_LEDGER.md`.
  The five lines are reworded in this commit.

## Files

- `received/`:
  - `GENESIS_v1_9_main.md` (main's GENESIS.md at `3f8dc11a`, the head);
  - `GENESIS_v1_8_main.md` (main's at `d2a95da4`);
  - `GENESIS_v1_8_sm.md` (this branch's v1.8, sm:B1528, at `84892ba0`);
  - `CC_TO_SM_AND_CODEX_2026-10-03_THE_COUNT_IS_A_BIT_AND_THE_MIXING_QUARTIC.md` (main's relay).
- `verification/`: `genesis_v110_checks.py` (with `genesis_v110_checks.json`, `genesis_v110_checks_prewrite_run.txt` and
  `genesis_v110_checks_run.txt`) and `merge_genesis_v110.py`.
- Lock: `tests/test_b1533_genesis_v110.py`.
- Relay: `SM_TO_CC_AND_CODEX_2026-10-03_GENESIS_V1_10.md`.
