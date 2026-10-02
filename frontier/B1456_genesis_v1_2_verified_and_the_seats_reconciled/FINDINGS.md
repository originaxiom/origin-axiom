# B1456 — GENESIS v1.2 VERIFIED ON MAIN AND ADOPTED AS v1.3, AND THE THREE SEATS' SAME-DAY RESULTS RECONCILED: the 758 word states are 536 manifolds; signed even powers are neither states nor levels; the deciding test was run three times with one outcome; and what main had called new today was partly on its own record

**Date:** 2026-10-02 · **Seat:** cc (main) · **Lane:** the Foundation Lock. **Sources:** the SM seat's `GENESIS.md` v1.2
(its sm:B1519, read at `5bf3d86f`, sha256 `9cf58165…b581a8`, kept as received in `received/`), its relays of the day,
its sm:B1517, sm:B1518 and sm:B1520; the audit lane's relays of the day (read at `7b088f50`). **Verdict:** PROVED (the
verification: seven groups of checks, all passing). **Scope:** frame none · object the grammar, the word states to
length twelve, the root and m207 · reach general for the algebra, single for the census identifications · hypotheses
none beyond GENESIS's. **0 of 19.**

## 0. Seen first

- **Repo.** `topic_sweep.py "revers|536|isometry signature|signed power|m207|states are"`: *VERDICT topic-sweep: 76 of
  1329 arcs on main match (NEGATIVE 12, OPEN 7, PROVED 55, RETRACTED 1, no verdict file 1)* — too broad to read one by
  one, and not so read. What is leaned on instead is stated by source: main's census says of itself "a state and its
  mirror are one row" (B1434) and does not divide out reversal; the SM seat's own sweep (its sm:B1517) reports no arc
  of main's with the reversal identity and one old gloss against it (B779's table, against B945's reading) — its
  finding, not checked here; m207 is on main's record in B1418's class census and B1224's Chern–Simons census.
- **This arc is also a record of what main's own sweeps missed today**, found while designing its next arc
  (`topic_sweep.py` on "hyperelliptic|elliptic involution|…" and on "non-?split|…|interior class|…"): the three lines
  B1455 turned on are B1297's; "the count is the order" is the slope law B1438; and the identity ρ_q* ≅ ρ_{1/q} was
  already in the SM seat's sm:B1512, an arc that sat in main's own harvest table (B1453) read by a reader pass and not
  by this seat. B1455 carries the first two as an addendum; the third is recorded here.
- **Literature.** Not searched for this arc. v1.2 cites four sources main has not read: OEIS A000046 and A000048 (the
  counts were recomputed, not looked up), Goodman–Heard–Hodgson 2008 and Guéritaud 2006 (the monodromy triangulation
  is canonical), Chun–Gukov–Park–Sopenko 2019 (the homology formula) and Salepci, arXiv:1006.0752 (uniqueness of the
  cyclic word). The checks below do not use them.

## 1. v1.2's new claims, by main's own code (`verification/v1_2_own.py`)

| | claim of v1.2 | main's check | result |
|---|---|---|---|
| H1 | a word and its reverse give the same oriented manifold: M(reverse w) = D·M(w)⁻¹·D⁻¹, D = diag(−1, 1) = PJ | all 8 190 words to length twelve | holds, no exception; det D = −1 |
| H2 | the 758 states are 536 manifolds; 222 pairs; the first at length seven | classes under rotation, swap **and** reversal; SnapPy's isometry signatures on all 758; an orientation-preserving isometry on a sample of 30 pairs | 536; 444 states in pairs; first pair LLLRLRR, LLLRRLR; the signature partition **is** the reversal partition; 30 of 30 |
| H3 | main's 95 of 758 is 87 of 536, and no pair is split | main's own census summary (B1439) with B1434's two | 95 states (49 of sign +, 46 of sign −), 87 manifolds, no pair split |
| H4 | −(LR)² is m207, H₁ = ℤ ⊕ ℤ/3 ⊕ ℤ/3; it is neither a state nor a level | Smith form; SnapPy; the triples of H7 | m207 (the bundle of +LRLR is m206); double cover t12839, which is the root's fourth level; four signed even powers among the box's matrices |
| H5 | P sends LR to RL, not to its inverse; J = [[0,1],[−1,0]] sends LR to its inverse | direct | holds; det J = 1 |
| H6 | the eight isometries of m004 act on the cusp by diag(s_m, s_l), each sign pair twice | SnapPy cusp maps | eight isometries, the four sign pairs, two each |
| H7 | every hyperbolic monodromy is one triple (u, k, ε) | continued fractions on the 168 matrices of the box | 14 triples; one signed even power class, (LR, 2, −) |

**All agree with v1.2.**

## 2. The deciding test was run three times

Main's B1455 (two routes) and the SM seat's sm:B1520 (two routes over ℚ(q) and a third at seven rational points),
sealed separately and run without sight of each other's outcome, agree: every vacuum of the family is fixed by a
count-odd symmetry; the witnesses are the same (inversion then dual, and swap∘inversion then dual); only four of the
eight simple maps are automorphisms and they preserve orientation; the mirrors need a conjugate generator. The seat
adds the general twist: at a generic vacuum (q ≠ 1, μ ≠ ±1) no orientation-reversing map survives, so the geometric
mirror is broken there while the count-odd symmetry never is. Main's statement that a bare mirror fixes "every
vacuum" is for μ = ±1 and is to be read so.

## 3. v1.3 (`adoption/amend.py`, eight changes)

Main's v1.3 is v1.2 with: the deciding test's result at FK9 and in the frame table; **what a source must be and what
a count needs** at GAP3, from the audit lane's records as harvested in B1457; the corrections B723 carries, in the
observer line; and at FK12 — the fork the SM seat registered for the owner's question — the two signs, the count as an
order, the audit lane's criterion for when a reduction loses the register, and its qualification of B37. The page
names THE_BAR as a document of the SM seat's branch that main has not yet harvested.

## 4. Also done here

- **The seal gates read a ledger row from the right** (`scripts/gates/gates.py`, `_seal_ledger_rows`): a "|" in a
  row's description hid the row from both seal gates. Found by the SM seat's lane; on main's ledger it changes
  nothing that is flagged. Locked with the old pattern as the control.
- **B1439 and B1434 carry a note of their unit**: word states, of which a word and its reverse are one manifold.

## 5. The fence

A verification of finite statements about words, matrices and census manifolds, and a reconciliation of three
records. FK1 and FK12 are the owner's. THE_BAR, sm:B1518's null model and sm:B1517's instrument are registered, not
verified (lead L243).

## 6. Not done (lead L243)

The audit lane's two corrections of main's early arcs (B37's detector; B130's inference from an empty elimination);
the SM seat's THE_BAR and its grading of main's census; the audit lane's R79 on markings, which bears on L241.
