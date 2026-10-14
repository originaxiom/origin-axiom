# B1647 — REVIEW 63: THE FIELD WINDOW — the work is banked, mostly verified as the rules say; the label VERIFIED was stretched in nine rows, the foundation leans on some seat results never recomputed, and every premise-level error in the window was caught from outside main's seal loop

**Verdict: PROVED** (a process arc: the review loop, the owner's banking-and-verification audit, and the register's
premise audit). cc (main), 2026-10-14. **0 of 19.** POINT_REGISTER P-026–P-029, P-086.

The review is written in full in `docs/progress/REVIEWS.md` under "Review 63 (2026-10-14)". This page records what it
did and what it found.

## 0. Seen first

`VERDICT topic-sweep /Review 6[0-9]|decadal review|banking.and.verification|premise audit|frame audit/: 17 of 1419 arcs on main match (PROVED 17)`
— the earlier reviews (B1608, B1622) and the frame audit (B1640).
`docs/progress/REVIEW_TEMPLATE.md`, Review 62 (B1622) and its block; the owner's P-086 (a)–(e) and the register's
P-026–P-029. The mechanical half is `scripts/review/review_tools.py --fresh-clone --json`
(`verification/review_tools_output_fresh_clone.txt`). **Literature:** none (a process arc).

## 1. How it was done

- **Main ran the tools.** The fresh clone passes at `0bbbb6ca`. The seeded sample (B1625, B1626, B1634, B1638, B1645)
  was read in full and re-run in the clone.
- **Three read-only agents of main's did the long reading:**
  - every lane against its head (P-086 a);
  - the VERIFIED rows, the relied-on seat results and the register's DONE rows (P-086 b–d);
  - the window's premises (P-026–P-029).
- **Main checked every finding taken against the pages before writing it, and rejected two.** xB003's and the referee
  sweep's rows are claims about main's own record, where reading the record is the check.

## 2. What it found

- **Banked.**
  - Every lane's pin equals its head. Three audit-lane relays were harvested but not rowed; they are rowed now.
  - Every one of the window's sixteen seals preceded its results.
  - The sampled locks pass in a fresh clone (12 of 12), and the six instruments of the sampled computing arcs, re-run
    there, rewrite their outputs byte-identical to the banked ones.
- **Verified, mostly.** Nine ledger rows carried a stronger label than their evidence. They are corrected with dated notes:
  - a census that timed out on main;
  - a reading labelled VERIFIED;
  - five checks filed under arcs that never mention them (they sit in B1600's verification/, and B1600 now lists them);
  - W51, registered not recomputed;
  - W53's arc.

  One row was under-labelled (xB031, B1470) and is upgraded. The seat results the foundation relies on with neither a
  verification nor a row are rowed (P-124).
- **Premises.** The window disclosed 29 errors:
  - the seals and main's read-back caught the computation-level ones;
  - every premise-level error came from outside main's seal loop;
  - two sealed cells passed vacuously (filed, E82).

  Four scope repairs are owed (P-119–P-122). The Seen-first sweep missed the record's own earlier statements under
  older words (B1290 posed FK10's question in September; P-123).

## 3. Filed at the review

- the ledger corrections;
- B1600's addendum;
- three relay rows and the smlaws marker;
- B1629's "Independently verified" retitled (main's own agents);
- B1644's hash line;
- the E82 instance;
- eight terms in TERMINOLOGY;
- P-119–P-127, with P-019, P-078 and P-114 amended and P-026–P-029 and P-086 closed.

Six action items, one of them the Codeberg mirror carried from R62-1.

## 4. Files

`verification/review_tools_output_fresh_clone.txt`; the lock `verification/test_b1647_review_63.py`.
