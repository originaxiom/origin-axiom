# B1661 — Review 64, the field stage: one Higgs fails, the pull-back is asked, and the seals read in their own form

**Verdict: PROVED** (a process arc: the review's filings are on the page and locked). cc (main), 2026-10-16.

## 0. Seen first

`VERDICT topic-sweep /review 64|decadal review|field stage review/: 6 of 1433 arcs on main match (PROVED 6)` — the
earlier reviews' arcs; this is the 64th. **Literature:** none (a process arc).

## 1. What it records

- The review itself is in `docs/progress/REVIEWS.md` under "Review 64 (2026-10-16)", with its action items and anchor
  `bf44d9032`.
- The mechanical half (`scripts/review/review_tools.py --fresh-clone`) is kept as
  `verification/review_tools_output_fresh_clone.txt`.

## 2. Filed at this review

- **B1654.** The sealed hashes of four reviewer helpers, changed after the seal at S131, are recast as `# sealed at`
  lines, and a findings addendum names the files. The seal check is clean, 69 of 69. An E80 instance.
- **B1660.** The headline separates the pass criteria from the stated expectations, the non-sequitur is rewritten, and
  the post-seal explorations are kept in `verification/after_the_seal/` with their outputs, hashed with the stored
  output. An E65 instance.
- **ERROR_LEDGER.** The E80 and E65 instances.
- **TERMINOLOGY.** Six terms: committed unread, a scoreboard, the canonical end condition and L, the twisted frame and
  the per-field reading, the joint law, the arena.
- **Review 63's block.** R63-3 marked done; R63-2, R63-4, R63-5 and R63-6 carried as R64-2, R64-6, R64-7 and R64-8.
- **The full suite** (parallel; REVIEWS §5b): 7335 passed, 10 failed, 68 skipped.
  - Six failures came from the review's own state mid-run, and all are fixed.
  - Two came from **B1421's lock, stale since S133.** The ledger's price is 4 + 9 = 13, and the lock asserted 8
    sources. It now asserts the live ledger: the selective landing suites had missed it.
  - Two (B186, B616) turn on the BLAS thread count, which the CPU-sharing rule sets to one. B616's census gives
    378 or 384 pairs; B186's band box dimension is ill-conditioned, so its 0.04 margin fails (0.027). Diagnosed,
    not repaired (R64-10).

## 3. What it does not do

- It does not repair B1649, B1651 or B1658. They go to one scope-repair arc (R64-3).
- It promotes nothing and demotes nothing.
- It does not read the eleven arcs outside the sample.

The lock is `verification/test_b1661_review_64.py`. 0 of 19.
