# B1755 — PREREGISTRATION: THE SIX ON THE LINES OF ORDER 13, 14, 15 AND 20 — the SM seat's test of the level-5 rung (its relay §275): if the six's lines are chosen by the moves acting through SL(2, 𝔽₅), the lines of order 15 and 20 carry the six specifically and those of order 13 and 14 do not

cc (main), 2026-10-24, at the SM seat's proposal (relay §275, harvest row 1396) and the register's first question (P-384:
what selects the line class (2/5, odd/10)). **Sealed before `verification/census.py` and `verification/compare.py` run.**
0 of 19.

## Why

B1749 and B1753 (sealed, ungraded) found the six charged-fermion ratios specifically on one strip of the order-10 lines
(2/5, 1/10) and (2/5, 1/2); B1753's referee showed that "orders divisible by 5" is mostly a pick, since any rule containing
those lines passes (P-384). The SM seat read the record (its relay §275, post hoc, counting only): the weave sees a line's
order, never the line (W140); the moves act on the lines of order N through SL(2, ℤ/N), which maps onto SL(2, 𝔽₅) = 2I, the
level-5 rung's group, exactly when 5 divides N; among the orders ≤ 12 these are 5 and 10, exactly where the six were found.
**That reading makes a prediction on lines nobody has compared with the six:** among the orders 13, 14, 15 and 20, the
lines of order 15 and 20 (5 ∣ N) carry the six specifically, and those of order 13 and 14 (5 ∤ N) do not. Order 14 is the
discriminating control: it shares order 10's factor 2 without its 5.

## The model (no data)

- **The points:** B1749's 125 apex points (the primitive thread words of length 12, B1720's rule, apex height in [2.0, 3.6]),
  loaded from B1749's sealed census module unchanged.
- **The lines:** every flat line of exact order 13, 14, 15 or 20 up to sign, in B1726's enumeration: 84 + 72 + 96 + 144 = 396.
  49 500 points.
- **The frame, the readings, the measure:** exactly B1749's and B1753's (B1726's `compute()` as B1741 calls it, under its own
  module name; B1741's `compare.py` loaded unchanged, its sha256 asserted at run time, re-pointed only to this census, fresh
  seeds 1809–1828, and a loader that keeps the rows of one order class at a time).

## Cells

| cell | prediction | prior |
|---|---|---|
| **D, THE DECISIVE CELL** (one composite prediction) | the seat's menu: on the lines of order 15 and 20 together at most 0.1% of random hierarchies reach as low a χ²_six (mean over 20 seeds), **and** on the lines of order 13, and on those of order 14, each more than 1% do | 30% |
| P1, its precondition | the seat's menu: some row on the lines of order 15 and 20 below 16.75 | 55% |
| C1, control | B1741's and B1749's best rows reproduced to 10⁻⁹; B1724's T-law on (2/5, 1/15) at B1749's middle apex to 10⁻⁶; the line counts 84, 72, 96, 144, every order exact | 97% |
| C2, control | B1735's 3.0945633 reproduced on B1726's census | 99% |

**Read-outs, not looks:** each class alone (15, 20, 13, 14) at 0.1% and 1%; the nine; the best rows per class; the
random-subset control (the χ²_six minimum of the 15-and-20 class against 200 random sets of 240 of the 396 lines); and each
line's own minimum with its α and b. Two readings make different predictions there, stated now:
- **α = 2/5 alone** (the record's class): rows below the bar only on lines with α ∈ {2/5, 3/5} — on order 15, (6/15, b) and
  (9/15, b); on order 20, (8/20, b) and (12/20, b).
- **The unit twist** (main's firewalled reading, P-384): rows below the bar on lines where the Higgs's twist 3α is ±1/5 mod 1 —
  on order 15 also α ∈ {1/15, 4/15, 11/15, 14/15}; on order 20 only α ∈ {2/5, 3/5}.

**THE_BAR, fixed now:** one decisive look on lines no record compared with the six, with an unchanged instrument and measure.
Its grade is computed after the read from the exact count of random hits under the joint look ledger (Review 70's count,
`docs/LOOK_LEDGER.md`): by the ledger's definition m = 40 — the 37 sealed decisive cells before this seal (Review 70's 36 and
B1753) and the three post hoc scans that informed this design (B1753's per-line read and its referee's subsets, the golden
slope, the unit-twist check; P-384); inclusively, every post hoc scan of the same data counted, m = 71. With 80 000
targets, Bonferroni passes for at most 11 hits at m = 40 and at most 4 at m = 71 (r the exact 97.5% upper end); PASSED
also needs the third opinion. The classes are fixed by the reading before any of their rows exists, so no
class-choosing null is owed for the decisive cell.

**The reading, written before the run.**
- **D holds:** the lines of order 15 and 20 carry the six specifically and the orders 13 and 14 do not — the six's lines are
  those on which the moves act through the level-5 rung, out of sample; with the per-line read-out deciding between the
  α = 2/5 class and the unit twist. Still a READING: c = 3 and the reading rule by hand; τ in the band; no CP sign.
- **P1 holds, D fails on 15 and 20** (not specific there): the order-5 quotient is not what selects the six's lines; the
  class (2/5, odd/10) is special beyond 5 ∣ N.
- **D fails on 13 or 14** (specific there too): the specificity is not the level-5 rung's; a factor-2 or generic mechanism.
- **P1 fails:** the six do not reach these lines at value level; the order-10 class stands alone.
- **A control failing** stops the reading until resolved post hoc, labelled.

## Seen first

`VERDICT topic-sweep /order 1[3-9]|order 20|lines? of order|level.5 rung|five-ality|divisible by 5|unit twist|5 ?∣ ?N|5 divides/ (full text): 52 of 1526 arcs on main match (NEGATIVE 16, PROVED 35, no verdict 1)`
— among them B1698, B1703, B1711, B1712, B1713, B1728, B1729, B1733, B1734, B1749, B1753. On these orders the record holds
B1703 (the frame's coincidence laws on orders 8–16, no data) and B1729 (the lepton-down ratios on orders 13–30 at two τ of
the band against the Clebsch's log 3, no measured number read; NEGATIVE for the factor); no comparison with the six. **The
register and OPEN_LEADS** (grepped): P-384 (this question), P-373 (what fixes Im τ), P-340 and P-362 (A) (the six specific
only on orders 5 and 10), P-312, P-350 (the apexes fill the band), P-375/P-379/P-385 (the ladder: the rungs are the
quotients by T^N, Δ(2, 3, N), finite for N ≤ 5), P-381 (the grades), P-376 (the look ledger's count). **Literature:** the
check of 2026-10-24 (P-382): no published mechanism ties lepton = down relations to an order-5 Wilson line or SU(5)'s
centre; the (2, 3, N) triangle groups and SL(2, ℤ/N) → SL(2, 𝔽₅) are classical.

## Disclosed

- **Known before the seal:** B1749's and B1753's results and scopes; the strip (Im τ 2.96–3.11) and the order-10 class
  (2/5, odd/10); main's post hoc scans of the line class on B1749's rows (the golden slope NEGATIVE; α = 1/5 fails, α = 2/5
  holds, b odd/10 better than even), which motivate the unit-twist read-out. B1749's 125 apex points were used by B1749 on
  orders ≤ 12; their place in the band is known.
- The prediction is the SM seat's (§275), from a reading it calls post hoc; main adopts its design and its control orders,
  and sets the decisive bar at B1753's 0.1% (the seat proposed 1%).
- **No frame value on any line of order 13, 14, 15 or 20 at any of these points was computed or seen.** The instruments were
  import-tested (125 points, 396 lines, 49 500 tasks); the controls were not run before the seal.
- The thirtieth sealed test of this frame.

## Instruments

- `verification/census.py` → `census.jsonl`, `control.json`, `census_run.txt`.
- `verification/compare.py` → `comparison.json`, `compare_run.txt`.
- Import-tested; importing computes nothing. `ARTIFACT_HASHES.txt` pins both, B1741's `compare.py`, B1749's census module and
  the files they read in place.
