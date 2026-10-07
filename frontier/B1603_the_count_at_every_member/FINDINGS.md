# B1603 — THE COUNT AT EVERY MEMBER: the seat's dictionary read at all 442 interior classes on the weave's forced covers — the floor and ceiling hold on every one; +LR's twenty-four are all (−1, −1) and −LR's are all (0, −3); and the generation shape is not the root's: ninety-eight more generation-shaped readings sit on ten even-trace threads, eight kinds of reading in all, only one with the physical index's shape

**Verdict: NEGATIVE as sealed** (C3 and C5 fail; C1, C2, C4 hold) — a weave result by inheritance (B1602's population,
every member). cc (main), 2026-10-07. Sealed `5d2787345` before any member beyond the three of S82 was extended. No
physical quantity; no three. **0 of 19.**

**Credit.** The SM seat for the dictionary and for the floor and ceiling (sm:B1545), which hold at every one of the
442 readings — the strongest check its theorems have had on main; B1492 for the instrument.

## 0. Seen first

As sealed: `VERDICT topic-sweep /generation-shaped|generation shaped|\(-1, -1\)|\(−1, −1\)|extension W1|W_1|Lambda\^2|floor|ceiling/: 103 of 1375 arcs on main match (NEGATIVE 20, OPEN 7, PROVED 76)`
— B1492, B1493, B1485, B1495, B1602, sm:B1545, sm:B1550, the seat's W6. Seen before the seal: +LR (two members),
−LR (two), −LLRLRLRR (one). **Literature:** none beyond the seat's.

## 1. The census (`count_<thread>.json`, `summary.json`; 20 threads, 242 members, 442 classes)

| | sealed prediction | prior | result |
|---|---|---|---|
| **C1** | every member of +LR's cover reads (−1, −1), dead on every cusp | 85% | **HOLDS** 24/24 |
| **C2** | every class at −LR's six members reads (0, −3), dead on every cusp | 80% | **HOLDS** 24/24 |
| **C3** | no even-trace member is generation-shaped | 50% | **FAILS**: 98 generation-shaped readings on ten even-trace threads — ±LLR 12 each, ±LLLLR 12 each, ±LLRR 12 each, +LLLLLLR 6, −LLLLLLR 4, −LLLLRR 8, +LLLLLLRR 8 (their sign twins +LLLLRR and −LLLLLLRR none); ±LLR and ±LLLLR are not arithmetic |
| **C4** | the seat's floor and ceiling hold at every reading | 85% | **HOLDS** 442/442 |
| **C5** | at most five kinds | 40% | **FAILS**: eight — (−1, −2) 150, (−1, −1) 122, (0, −1) 64, (0, −2) 48, (2, −2) 32, (0, −3) 24, (1, 0) 1 (+LLLRLLR), (3, 1) 1 (−LLRLRLRR) |

The three odd-trace carriers read as S82 left them: +LR (−1, −1) ×24, −LR (0, −3) ×24, −LLRLRLRR (+3, +1) ×1.

## 2. What it says

- **The generation shape is not m004's.** The seat's "generations only on +LR" held on its odd-trace census; on the
  weave's even-trace covers the same shape — (−1, −1), the class dead on every cusp — is common: 98 readings on ten
  threads, twelve on each of the shortest, on arithmetic (±LLRR) and non-arithmetic (±LLR, ±LLLLR) threads alike. Odd
  trace is where it is rare (Theorem G's three-or-nothing); even trace is where it is plentiful, and there it comes
  on the pair of parities the act exchanges (the seat's W7), never on all three.
- **The sign matters on even trace:** −LLLLRR carries eight generation-shaped readings and +LLLLRR none; +LLLLLLRR
  eight and −LLLLLLRR none; +LLLLLLR six and −LLLLLLR four. Not read line by line here (a hatch).
- **The zoo is the real finding about the instrument.** A physical generation count is an index of closed-cycle
  cohomology with the rank-five shape identity n_5̄ = n_10 (B1496). Across 442 classes the class index on a 3-manifold
  produces eight kinds, and only (−1, −1) has that shape. So "generation-shaped" is a pattern label the instrument
  sometimes produces, not an earned count: the class index is an analogue of the physical index, not the index. The
  dictionary (FK11) stays UNEARNED, and its earning condition is now explicit — a module and a count on the weave with
  the shape identity built in, and a handle on chirality other than the index (B1487: the index is mirror-even).
- **The seat's theorems stand on everything read:** floor and ceiling 442/442.

## 3. Disclosed

- The instrument is unchanged after the seal (hash on `ARTIFACT_HASHES.txt`); four workers over disjoint thread lists.
- Sign characters only; numerical ranks at 40 digits; every forced kernel read.
- "Generation-shaped" is defined as (−1, −1) with the class dead on every cusp, as the seat reads +LR's members; no
  other shape is given a physical name here.
- Not blind to S82's three readings or to the seat's W6/W7.

## 4. Files

`verification/count_every.py` (sealed), `summary.py`, `summary.json`, the 20 `count_<thread>.json`, the worker logs.
Test: `tests/test_b1603_the_count_at_every_member.py`.

**Addendum (S84, 2026-10-08; B1604's control and audit).** Readings on covers whose four-residual at 40 digits exceeds the rank tolerance are withdrawn: −LLRLRLRR's (3, 1), +LLLRLLR's (1, 0), and +LLLLLLR's six on its second kernel. On the reliable kernels (`B1604/verification/tiers.json`) the generation shape has **116** readings — +LR 24; ±LLR, ±LLLLR, ±LLRR 12 each; −LLLLLLR 4, −LLLLRR 8, +LLLLLLRR 8 — and the kinds are **six**: (−1, −2), (−1, −1), (0, −1), (0, −2), (2, −2), (0, −3). C3 fails on reliable data; C4 (the floor and ceiling) held on all 442 and holds on the reliable subset; C5 fails at six kinds as it did at eight. The verdict is unchanged.
