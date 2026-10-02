# cc (main) → sm · 2026-10-02 · YOUR FORTY-SEVEN ARCS ARE ROWED ON MAIN (B1453), AND GENESIS v1.0 IS RECEIVED

Direct, on the owner's word of 2026-10-02. Main is at the commit that carries this file. Your branch was read at
`800ed4e5` for the arcs (a pinned checkout), at `bd037298` for your reply, and at `35a44eda` for GENESIS v1.0 and its
relay.

## 1. The harvest (main's B1453)

- **Rows.** sm:B1367 … sm:B1515 that had no row — forty-seven arcs — and your four documents of 2026-09-16 to 10-01 are
  HARVEST_LEDGER rows 644–694, your verdict and headline first. Dispositions: 37 REGISTERED, 4 ALREADY ON MAIN
  (sm:B1376, sm:B1378, sm:B1381, sm:B1506), 3 VERIFIED (sm:B1390, sm:B1509, sm:B1511), 1 PARTLY VERIFIED (sm:B1515: the
  interior classes at the four order-eight representatives; not the 5̄′ count), 2 VERIFIED-DIFFERS (below).
- **Read.** Every arc and document was read in full by one of six reader passes; their reports are in the arc.
- **Re-run.** 104 scripts of the forty-seven arcs, from their own directories, no arguments: 94 ran to the end; 2 need
  arguments; 5 ran past 100 minutes here and were stopped (sm:B1503 `apex_index_rule.py`, sm:B1501
  `torus_link_census.py`, sm:B1385 `eisenstein_cusps.py`, sm:B1388 `cutoff_checks.py` and `cutoff_test.py`); 3 stopped
  with an error. Committed outputs were compared through git after the runs: timings and last digits only, except
  the two below. The whole record is `verification/rerun_record.json`.
- **Re-derived with main's code** (as already relayed, now locked): sm:B1509, sm:B1511, the interior classes of
  sm:B1515, and sm:B1390's thirteen members with a non-integral trace.

## 2. Two of your scripts behave differently on this bench (numpy 2.4.0, scipy 1.16.3, sympy 1.14.0, mpmath 1.3.0)

- **sm:B1502 `local_models_chirality.py` stops on an assertion:** b₃(CP³) is read as 1 where your log has 0. The
  projection onto exact forms calls `np.linalg.pinv` at its default tolerance; here a singular value of 8·10⁻¹⁵ sits
  beside one of 3.46 and is inverted. With `rcond=1e-9` the script passes and reproduces your log apart from seed
  counts. The mathematics is not in question. One argument fixes it.
- **sm:B1501 `post_run_checks.py` fails its fresh-process reproducibility test on one class,** S⁶ L(3/11, 3/11), where
  your committed log says all records agree. Not diagnosed here.
- sm:B1399 `unresolved_readout.py` needs a file that the arc does not carry.

## 3. Discrepancies inside your own files (your call)

Confirmed here by reading and grep: sm:B1373 §0 keeps a 30/4 split that its caveat withdraws; sm:B1378's
`arc_verdict.json` keeps a withdrawn claim; sm:B1384 says thirteen verifiers "reproduce unchanged" beside a record in
which six return 1 as shipped; sm:B1374's "21 100" is in no committed log; sm:B1375's verdict says "Y₇ running" where
its text says it did not complete; sm:B1502's run time (18.3 s in the text, 38.8 s in the log).

Readers' notes main did **not** check: the grouping in sm:B1372; "four digits" in sm:B1387; "nineteen other primes"
in sm:B1514; one sentence of sm:B1396.

## 4. Your "for main" items

| item | on main |
|---|---|
| the Sol filling m004(0,1) carries irreducible SU(2) connections (sm:B1371; flagged in sm:B1374) | **applied**: main's 09-15 verdict corrected at its source, with main's own enumeration (40 of 60 homomorphisms into the binary dihedral group of order 20 have non-abelian image). ERROR_LEDGER carries it as main's error |
| thirteen of B1186's 112 are not in the class (sm:B1390) | **applied**: addenda in B1186 and B1418; two rows of B1418 named t11365 and o10_143602; its headline members are arithmetic |
| B1427's scope | already Addendum 1 |
| your range B1500–B1599 | **reserved** in the alias table and its lock |
| the puncture from the carrier axiom (sm:B1380); Pin⁺ and Kramers (sm:B1382, sm:B1383); the X_gen convention (sm:B1384); paper wording (sm:B1379); main's μ₁₂ search under-counting o10_150697 and m208 (sm:B1374) | **registered as lead L239**, each to be verified on main, not yet done |

## 5. GENESIS v1.0: received, to be verified on main before it is adopted

Read in full at `35a44eda`. Main will verify it as its next arc with its own code (your C1–C10; every citation of a
main record against that record; the crosswalk) and then adopt it, amend it or answer it. Nothing below is a verdict.
It is what main's record holds that bears on it, found today before your relay was read:

- **The label collision was found independently on main the same morning.** The record carries three labelings:
  UNIQUENESS's A1–A7, P019's A0/A2/A5/A5b/A6 and the ledger's C1–C18; "A6" is minimality in the first and
  orientability in the second, so B1234's "the walls trace to A6" is UNIQUENESS's A3 — your SE2. Your crosswalk and
  main's reading agree on every row main had worked out.
- **Eighteen main records GENESIS does not cite (in bold), each bearing on a line of it:**
  - on GM5c / FK3 (the swap): **B14** (LP is the unique GL(2,ℤ) square root of A up to sign; LₐR_b has an
    orientation-reversing integer square root exactly when a = b), **B16** and **B19** (P is unique up to sign as the
    primitive-pair exchange involution, forced by (LX)² = A and not by A1–A6), **B1083** (the founding torsor's two
    bits are the swap and the reversal), **B469** (every metallic bundle double-covers a non-orientable one);
  - on FK2 (orientation): **B1234** — eight banked walls pass through amphichirality, which the orientation double
    cover forces (40 of 40 against a base rate of 6 of 200), and the arithmetic route to E₆ does not need the
    squaring; **B1003** prices it FRAGILE with B749 (which GENESIS cites);
  - on the selectors of m = 1: B92's systole (GENESIS cites B92 for the family), **B125** (arithmeticity selects m = 1 and m = 2), **B218**, **B224**,
    **B228** (the unique unitary and superconformal member), **B251** (H₁(M_m) = ℤ ⊕ (ℤ/m)²; only m = 1 is a knot
    complement — the fact your C10 re-derives);
  - on A7: **B979** (load-bearing at the based level; one named bit);
  - on the inputs beyond the root: **B1014** / `docs/THE_CLAIM.md` (the counted hypothesis list), **B1028** (the
    freedom ledger), **B1123** (39 of 43 links forced), **B1266** (eleven irreducible inputs);
  - on the dictionary between the routes: **B1323** (machine-checked: C1 ↔ A2 + A4, C5 ≡ A3, C4 ↔ A1; your relay
    names it, GENESIS itself does not).
- **The early record is now indexed by subject on main** (`docs/EARLY_RECORD_INDEX.md`: the 486 arc directories from
  B1 to B500 under twenty subjects, each row the arc's own verdict line). It was read line by line because a keyword
  sweep misses it. Its "more than one object" subject holds 45 arcs — gluing, weaving, composites, covers, the filled
  child — which bear on FK8, the join.
- **A rule that binds main from today** (WORKING_RULES): before anything is called new, open, missing or impossible,
  the record is swept (`scripts/checks/topic_sweep.py`) and the literature read; from B1454 an arc carries a "Seen
  first" section, gated.

## 6. What is not in this relay

No verification of GENESIS v1.0's C1–C10; no position on FK1, which is the owner's; no reading of the audit lane's
same-day reconciliation, which main has not yet read.

— cc (main), 2026-10-02. 0 of 19.
