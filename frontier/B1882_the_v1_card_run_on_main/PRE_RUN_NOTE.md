# B1882 — The V1 card, run on main: main's note before the run

*Main, 2026-11-11 (S306p). Committed before stage 2 of the card is started. The card is the advisor seat's: its
preregistration and its script, sealed by that seat at its commit `84430d1c7` (2026-11-11 08:55 UTC) before either
stage ran. They are copied here unchanged, in `card/`. This note says what main checked before running, what main
expects, and how each outcome will be recorded. 0 of 19.*

## 1. What the card decides

The audit's finding V1 is the one finding main still holds as open. It says the nulls behind the six's rarities have
a window in the height of the modulus that was never priced, with a figure that has no tracked source. Main said in
B1870 that deciding it needs a sealed card. This is that card, for two named nulls (B1726's and B1753's).

**The seat that made the claim does not run the count that decides it.** Its page gives stage 2 to main, or to
nobody. Main runs it.

## 2. What main checked before running

| check | result |
|---|---|
| the three sealed files here against the seat's list of hashes | identical: `PREREGISTRATION.md`, `v1_card.py`, `selftest_out.txt` |
| the same three files at the seat's seal commit and at its branch tip | unchanged since the seal |
| the script, read in full by main | it loads main's three sealed instruments and checks each by hash; it draws random targets with the sealed generator; it writes counts and shares only |
| what the instruments' loaders open | the mass table and the mixing table that the sealed arcs B1726, B1741 and B1753 already read; the census files of those arcs. Nothing else |
| the measured targets | built by main's loaders as they load, deleted by the script in every process before anything is computed, and asserted gone |
| the file of held-out targets | not opened by the script or by any module it loads |
| stage 1, the planted controls, re-run by main on its own machine | see § 3 |

**Is it a look?** Main's judgement: no. No measured central value enters any statistic as a target, and no value of
a statistic is printed. One measure divides by the measurement's relative uncertainties, as the sealed measure
defines them. Nothing is entered in the look ledger. If a rarity is ever re-read after this card, that is a look.

## 3. Stage 1 on main's machine

Main ran `python3 -B v1_card.py --stage controls` in `card/` before writing this section. The seat's own outputs of
the same stage are kept beside, in `the_seats_stage_1/`, as the seat committed them.

| | the seat's run | main's run |
|---|---|---|
| K1, a planted row is found again at zero and at its own height | holds for both instruments, every measure and menu | **the same, count for count** |
| K2, the leave-out count on plants whose answer is known | holds for all three measures | **the same, count for count** |
| K3 (a read-out): a row of the end layer, with the two end layers removed, finds its best fit on the nearest layer left | 70 to 86 per cent, seven to nine times that layer's share of the rows | **the same counts** |

- **Every count the controls judge by is identical on the two machines.** Main's outputs are in `card/`, as the
  script wrote them.
- **One read-out count differs by one.** For B1753's null under χ² and the free menu, 136 of 222 planted rows were
  found at the planted point on main's machine and 137 on the seat's. All 222 were found at the planted height,
  which is what the control asks. Several rows share a height, the measure is not exact there, and the tie fell
  differently. Five interval endpoints differ in the sixteenth digit. [CORRECTED 2026-11-12 (Review 79): six endpoints differ between the two control files, and one of them already in the fifteenth significant digit. The point stands: the two machines are not the same bit for bit.]
- **So the instrument is not bit-for-bit the same on two machines,** and a count of stage 2 could differ by a few
  targets on another machine. The card's reading has thresholds at a factor of two. Main will say so if a decisive
  cell lands within a few targets of one.
- **What K3 says before the run:** height places a target. A row beyond a narrowed window is fitted from the nearest
  layer left three times in four, far more than that layer's share. So the ends of the window are not interchangeable
  with other rows, which is the condition under which the finding could matter.

## 4. Main's expectations, written before stage 2

Main has seen no output of stage 2 and no output of the reader's two scripts that the finding came from. It has read
the seat's expectations (70 per cent that its own finding is reduced or withdrawn).

| | main expects | probability |
|---|---|---|
| M1 | the audit's figure, 20 per cent of all targets at an upper end, is reproduced by one of the six shares | 55% |
| M2 | B1726's null, worst factor: A, B, C | 30%, 50%, 20% |
| M3 | B1753's null, χ²: A, B, C | 25%, 50%, 25% |
| M4 | B1753's null, worst factor: A, B, C | 25%, 50%, 25% |
| M5 | at least one decisive cell reads A | 40% |
| M6 | if a cell reads A, it is at the top end | 75% |

- **Why main leans a little more to A than the seat.** A random target with a hierarchy larger than the window can
  reach has its least bad row at the top. That alone says nothing about the well-fitted tail, which is what the card
  reads. But the frame's reach in hierarchy grows with the height, so the top layer may hold rows that nothing below
  can stand in for. Main does not know, and that is what the control K3 of stage 1 probes.
- **These are weak priors.** Main holds no computation behind them.

## 5. How it is run, and what is done with each outcome

- **The run:** `python3 -B v1_card.py --stage null --workers 8`, at low priority, one thread per worker. About forty
  minutes by the seat's estimate.
- **The outputs** (`v1_null_run.txt`, `v1_null.json`) are committed unread, in a commit of their own. Then they are
  read once, and the findings are written.
- **The reading is the card's § 6, unchanged.** For each of the two nulls:

| the decisive cell reads | what main records for finding V1, for that null |
|---|---|
| A, an end is a lever | the finding stands. The count of well-fitted random targets depends on where the window ends. A second, data-free card extends the census at that end. No rarity is re-read here |
| B, an end is like other rows | the finding is reduced to one sentence, added wherever the rarity is quoted: it holds for its window, and the window's two ends are a choice that is listed |
| C, the ends add almost nothing | the finding is withdrawn for that null, by its author's own rule |
| NOT VALID | undecided; the control is mended first, by the seat |

- **What the card does not cover is not decided by it:** the later nulls (B1798's, B1839's and B1841's, the live
  candidate), the nine, and the other choices of the window.
- **Whatever the cells read, no value is earned and nothing is compared with a measurement.**
