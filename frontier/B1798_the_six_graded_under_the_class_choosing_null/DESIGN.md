# R71-1 — the grade of B1749 and B1753 under the class-choosing null (design, written before any computation)

Draft for main (Review 71's R71-1; P-381, P-384). Written 2026-10-28 before any census row, feature matrix or random
target of this draft was computed. Nothing in a tracked file is edited; nothing is committed.

## What each arc's sealed cell was (from its PREREGISTRATION and FINDINGS)

- **B1749:** 125 fresh apexes (thread words of length 12, Im τ in [2.0, 3.6]) × ALL 266 lines of B1713 (orders 1–12),
  both horocycles, B1741's seat menu. P2 (decisive): fraction of random six-targets (B1741's draws, seeds 1769–1788,
  80 000) whose minimum χ²_six over the same rows and menu is ≤ the data's 3.573708662 — sealed result 16 / 80 000.
  The cell has ONE conjunct (min ≤ obs); it says nothing about other lines staying above 16.75.
- **B1753:** 223 fresh apexes (length 13) × the 48 lines whose order is divisible by 5 (orders 5 and 10), the same
  measure, seeds 1789–1808. P2 (decisive, 0.1%): sealed result 7 / 80 000 at the data's 2.739034461. ONE conjunct. The
  class (orders divisible by 5) was stated after the order-5/10 preference was seen on B1749's rows (its Disclosed;
  `order5_restriction` priced it on B1749's rows), so a fair null must let each random target choose its own class.

## The class partitions (and why)

- **B1749 — slope classes over the 266 lines** (α as stored by B1713's `lines()`, after its sign normalisation; as
  B1786's referee). B1749 chose no class: it used all 266 lines. Since the classes partition the 266 lines, *some class's
  minimum ≤ obs* is identical to *the all-lines minimum ≤ obs*, i.e. **the class-choosing null for B1749 is its sealed
  null** (a mathematical identity, checked numerically below). What this draft adds for B1749 is (i) precision — r from
  10⁷ fresh targets instead of 8 × 10⁴ — and (ii) the stricter read-out. The strip/class story for B1749 is not a
  selection the cell made; the earlier searches that pointed to the strip are priced by the ledger's m, not by r.
- **B1753 — the order-divisibility family** D_d = {lines whose order is divisible by d}, d = 1, …, 12, over all 266
  lines at B1753's 223 apexes (D_5 is the data's class; D_1 is "no restriction", B1749's rule). This mirrors how the
  class was chosen (the referee's "every simple order rule"). **Secondary partition:** slope classes over the 266 lines
  (as for B1749). Both families cover all 266 lines, so the primary form below is the same number for both: the
  all-266-lines rarity at B1753's apexes with obs = the data's minimum on its chosen class (2.739034461). Without D_1
  the union drops only the trivial line (0, 0); that count is reported too.
- **The census this needs:** B1753's committed census holds only the 48 lines (P-381's 2026-10-27 note). The other 218
  lines at its 223 apexes (48 614 points) are computed here with B1726's sealed `compute()`, loaded unchanged under its
  own module name exactly as B1753's census.py calls it (B1753's `apexes()` and `_K()` imported unchanged; no memo — the
  τ-only theta part is 1% of the cost, timed before any row; a sample of the committed 48-line rows is recomputed and
  must agree exactly). The data's minimum over the 218 new lines is read once, labelled post
  hoc, only to (i) confirm the data's own best class (if a non-five-ality line went below 2.739 the data's class-choosing
  statistic would be that lower value — reported, and the primary kept at 2.739 as the conservative choice) and (ii) state
  whether the data satisfies the stricter read-out's "every other class ≥ 16.75".

## The statistics (seat menu; B1741's chi2_features('seat', False) and min_chi2 expansion; obs + 1e-9 as B1741)

- **Primary (mirrors the sealed one-conjunct cell): ANY-CLASS** — the fraction of random targets for which some class's
  minimum χ²_six ≤ obs. This is the grade's r.
- **Read-outs (not grades; the sealed cells did not contain the second conjunct):** STRICT — some class ≤ obs AND every
  other class ≥ 16.75 (for the overlapping D_d family: some d ≥ 2 with min(D_d) ≤ obs AND min(lines not in D_d) ≥ 16.75;
  d = 1 excluded since its complement is empty); for B1749 also "the 2/5 slope class ≤ obs AND every other ≥ 16.75";
  for B1753 also "D_5 ≤ obs" (the sealed cell, on fresh targets) and the order-exact partition (N = 1..12) strict form.
- **Method:** B1786's referee's: a KD-tree over the seat-menu feature points finds every target whose nearest point has
  χ² ≤ obs + 0.5; for those candidates only, per-class minima are computed with B1741's own expansion; every decision
  uses B1741's arithmetic (no target with all-lines χ² > obs + 0.5 can carry an event of any form above).

## Targets

- **Validation (a):** the sealed seeds — B1749 1769–1788 on its census → must give 16 / 80 000 and min 3.573708662;
  B1753 1789–1808 on its 48-line census → 7 / 80 000 and min 2.739034461. Also: the per-class identity (ANY-CLASS = the
  all-lines count) on the validation seeds.
- **The null (b):** fresh seeds 5001–7500 (2 500 × 4 000 = 10⁷ targets, B1741's draws(seed) unchanged; not used by any
  earlier null on record: B1786's referee 2001–4500, B1792 4501–4540, W164 9001–10250). The same targets for both arcs.

## THE_BAR (c)

- r = the exact 97.5% one-sided Clopper–Pearson upper end of hits / n (= the upper end of the exact two-sided 95%
  interval, as the ledger's r = 3.25 × 10⁻⁴ and 1.80 × 10⁻⁴ are); Bonferroni p = m·r; **PASSED iff m·r < 0.01** at the
  ledger's m (and s chosen by a fixed rule).
- **m, from docs/LOOK_LEDGER.md and Review 70 § 1b:**
  - **B1753: m = 39** (36 sealed decisive cells before its seal + the three post hoc scans that informed it). Flag: the
    web seat's THE UNIFICATION-SCALE TEST (two looks, one per arm; rule ef08144e1 at 2026-10-24 14:45 +0200) was sealed
    before B1753's seal (33b197340, 20:05 +0200) and is not in the 36; with it m = 41. Inclusive reading: 68 (+2 = 70).
  - **B1749: Review 70 says "at least 33".** Counting the ledger's sealed rows by commit time against B1749's seal
    (32f29ad98, 2026-10-24 14:11:50 +0200): main 20 (B1660 … B1748), the web seat 10 (all sealed 10-22 to 10-24 06:25
    +0200), the SM seat 5 (W88, W90, W94 on 10-15; W146 04:06 UTC, W151 11:00 UTC on 10-24) → **m = 35**; no post hoc
    scan in the ledger is marked as informing B1749. Reported at 33 and 35. Inclusive (every earlier post hoc scan:
    main 7, the web seat 17) ≈ 59.
- **Grade words:** PASSED if m·r < 0.01 at every defensible ledger m above; **on the gate** if it passes at one
  defensible m (or at the point estimate) and fails at another (or at r); **not PASSED** if m·p̂ ≥ 0.01 at the ledger's m.
- **Not computed here (flag):** P-381's "exact joint law of the looks" (each earlier look's statistic recomputed per
  random target, which could undercut Bonferroni because the looks are correlated). This draft is Bonferroni with a
  class-choosing r, as R71-1 asks.
