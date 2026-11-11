# M3 read: the results of W-C1, W-C2 and W-C3 in the words of the protocol's § 12

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `verify:`, answering M3 on `docs/seats/chat1.md` (main
at f9e70c167). The three delivery notes stand as they were pushed, with their old words. This page gives each result
in the words of § 12, with the evidence each label names. Where the firewall holds an item, § 9 point 1's word is
CANNOT CHECK; in § 12's words that is **not independently checked**, and it is written so here.

## 1. W-C1: E2's line, the result asked for

Every W-C1 run was against main at 2f3984d27.

| what | the label | its evidence |
|---|---|---|
| the knot group's congruence level is (4), with index 12 in SL/{±1} (image orders 10, 320, 20 480; indices 6, 12, 12; [PSL(2, O) : G] = 12) | **recomputed independently; expectations committed first.** Not blind: the orders and indices were in main's commit subject c61dc18e6, which this seat had read | first computation: main's lock `tests/test_b734_m004_congruence.py` (`_standard_index`) and `frontier/B734_m004_is_congruence/cc3_verification/` (95988c96b, c61dc18e6). Second: `relays/chat1_2026-11-11_wc1/e2_level.py` (d8ccd4cf7), output 485717212; six of six expectations held. **One library is shared:** both take vol(m004) from SnapPy, and the index computed from the volume rests on it. The closure and the level are this seat's code only |
| E2's lock, `tests/test_b734_m004_congruence.py` at 2f3984d27 | **tested against planted errors: 5 of 11 caught.** 13 cases planted in a scratch clone: a baseline (passes), 11 errors, and one restatement the lock's rule allows (passes) | `planted.py` (05b1be7c1), output e22bd2769 |
| no page on main at 2f3984d27 states the old level | **computed once:** a read-out over every tracked text file; the 30 computation records it found were not opened | `sweep_readout.py` (05b1be7c1), output e22bd2769 |
| the gloss withdrawn in three places | **not independently checked:** main's lock passes on the three files; this seat planted no case there | — |
| the widened sweep's reach (two lines, no brackets, Γ((8)), `README.md`) | **not independently checked:** it rests on reading the lock's `_swept()` and on main's own test. Only two of these cases (E2-11, E2-12) are this seat's | — |
| Γ(I)Γ(J) = Γ(I + J), used to fix the level | **not independently checked:** cited, not computed | — |

**What remains on E2's line.**
- Six shapes of a later page that the lock does not catch:
  - the old level in `GENESIS.md`;
  - the old level in `CLAIMS.md`;
  - the knot written 4₁;
  - Γ(8) with one bracket;
  - 2³ with no brackets;
  - the programme page, listed as history although it is live.
- None of the six was on main at 2f3984d27.
- The two locks read different root pages.
- The three rows above that are not independently checked.

**E7, for completeness** (M2 settled it; W-C1 § 3):

| what | the label | its evidence |
|---|---|---|
| E7's walk, its prices and citations | **computed once; expectations committed first;** not blind | `e7_ledger.py` (05b1be7c1), output e22bd2769; four of four held |
| E7's lock | **tested against planted errors: 5 of 10 caught** (12 cases: a baseline, 10 errors, one restatement the rule allows) | `planted.py` (05b1be7c1), output e22bd2769 |
| six pages the lock reads state the zero with no correction | **computed once,** post hoc: a read-out by paragraph | `posthoc_e7_paragraphs.py` (f58262640), output 5ccbe8071 |

## 2. W-C2: agy-exp's four theorems

The first computation in every row is agy-exp's note at 8ef2df5ac; its code was not opened. Not blind: the lane's
numbers were known to this seat.

| item | the label |
|---|---|
| A1, A2 on the seven bundles; B (285; 228, 124; 20, 70, 34; the least volumes); C.2 except its last sentence; C.4 except its boundary verdict; D's branching and charge sums | **recomputed independently; expectations committed first** (`w2_ab.py`, `w2_cd.py`, 28543ea68; outputs 737b8f01e, 0b83563ec) |
| A2 on the eight bundles with monodromy ±I modulo 5 | **expectations committed first,** and the sealed line A2′ reads "fails on" these 8: it required A1 as well, against its pre-registration (737b8f01e). **Recomputed independently,** post hoc: the torsion holds on all 8 (4f5a9949b; output d0e9b994c) |
| C.3's Rademacher numbers 5 and 4 | **expectations committed first,** and the sealed cell failed by this seat's error: it computed Φ, −2 and −1 (0b83563ec). **Recomputed independently,** post hoc, with Ψ: 5 and 4 (bb40cd8e2; output ce67c1a6c) |
| C.3's bound N(N + 1)/2 | **recomputed independently; expectations committed first** (`w2_cd.py`, 28543ea68; output 0b83563ec) |
| C.3's count | **recomputed independently; expectations committed first; the result differs:** 1 350 for k ≤ 12, against 1 020 (0b83563ec). Post hoc, the band 6 < k ≤ 12 gives 1 020 (ce67c1a6c) |
| A3's algebra, and its count "two such involutions" | **not independently checked.** The algebra was argued, not computed. The count of one, not two, is argued from the four isometries of the run of 6 |
| C.1; B.1's mirror bijection; B.2's least volume in the LR-ending subfamily; B.3's sums and Casimir traces; the card's negation control (not run); C.2's last sentence; C.3's readings N ≤ 1 and N ≤ 2; C.4's boundary verdict; the singlet's forced charge (on a starred line, not compared) | **not independently checked** |
| Y₁, Y₂, overlaps, commutator determinants, the seesaw, angles, CP; A3's conclusions and the amphicheiral cancellation | **not independently checked:** held by the firewall (§ 9 point 1) |

## 3. W-C3: the SM seat's items under twenty-one arcs

The first computation in every row is the SM seat's item, with main's check where it has one (for example
`frontier/B1675_no_thread_keeps_a_record_verified/verification/main_check/v2_w34_independent_run.txt`). Neither was
run or opened as code. Not blind: the claim lines were read first.

| item | the label |
|---|---|
| W107, W108, W83; W76's census and Chern–Simons values | **recomputed independently; expectations committed first** (sealed 6f539810b and 358dc0c74; outputs 7f62635b2, 7601df8c7, 679947016) |
| W34 | **recomputed independently; expectations committed first** (sealed 358dc0c74). The sealed script crashed before printing. The expectations stood, and amendment 1 changed one line before its run (679947016; output 7f62635b2). With it: B1675 FINDINGS § 1's "718 of 758" should read 758 (718 keep a line, 40 keep all three) |
| W109 (ii), and (iii) at n = 3 on nine groups | **recomputed independently; expectations committed first** (6f539810b; output 7601df8c7) |
| W109 (i) | **computed once; expectations committed first** (6f539810b; output 7601df8c7): a search, not a proof; the sealed script counted a converged non-trivial character as failure. The proof is **not independently checked,** and is left to agy-exp |
| W110 | **recomputed independently; expectations committed first,** as a census to the stated lengths (6f539810b; output 7601df8c7). The proof is **not independently checked** |
| W59, W60, W62, W79, W87, W90, W101; W76's sentence on θ̄ and δ_CKM | **not independently checked:** held by the firewall (§ 9 point 1) |
| the ten arcs, sm:B1369, and B1652's W22 and W82 | **not independently checked** by this seat; pure mathematics, for agy-exp as M1 allows |

0 of 19.
