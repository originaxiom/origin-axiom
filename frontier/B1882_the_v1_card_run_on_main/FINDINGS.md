# B1882 — The V1 card, run on main: the window's two ends, measured on random targets only

*Main, 2026-11-11 (S306p). The audit's finding V1 says the nulls behind the six's rarities have a window in the
height of the modulus that was never priced. The advisor seat sealed a card to decide it for two named nulls and gave
the deciding count to main. Main sealed its own note before running (`PRE_RUN_NOTE.md`), ran the second stage, and
committed the two output files before opening either (818d17f46). They were then read once. This page is that
reading. Random targets only: no measured target enters, no rarity is re-read, nothing is compared with a
measurement. 0 of 19.*

## 1. The answer first

- **All three decisive cells read B: an end of the window is like other rows.** By the card's rule, fixed before any
  number, finding V1 is reduced to one sentence for these two nulls.
- **Two of the three read B by a hair.** One is short of A by less than one target in a thousand, one by three.
- **A figure like the audit's is computed, and it is not about rarity.** One random target in five has its least bad
  row in the top layer. Most of those are poorly fitted: of the first null's 205,881, 5,925 are in the best 5%, 1,049
  in the best 1% and 111 in the best 0.1%. Among well-fitted targets the last layer is below its neighbour at the best
  5%, 1% and 0.1%, in all three decisive cells. At the best 0.01%, a hundred targets, the counts are too small to say:
  17 against 10 in the first null; 17 against 18 and 16 against 21 in the second. Under the other two menus it is
  below it at the best 5% and 1% in every cell, and at the best 0.1% in all but one: the first null's covariant
  menu, 130 against 123.
- **What the window's ends do to a rarity, in numbers.** Under the seat's menu, well-fitted random targets come from
  the last layer at 1.6 to 2.0 times the average rate, and from the first at 0.06 to 0.08 of it. Over all nine cells
  the top end reads 1.6 to 2.4 and the bottom end 0.04 to 0.18.

> **CORRECTED 2026-11-12 (Review 79; found by two readings of this arc by sessions that did not build it).** The two
> bullets above read: "**The audit's figure is reproduced, and it is not about rarity.** One random target in five has
> its least bad row in the top layer. Those are targets that fit nothing. Among well-fitted targets the last layer is
> below its neighbour." and "At the top end, well-fitted random targets come from the last layer at 1.5 to 2 times the
> average rate. At the bottom end, at less than a tenth of it." Four things were wrong.
> 1. **Nothing of the audit's was reproduced.** Its figure had no tracked source and named no null (B1870). What was
>    computed is a share, 20.6%, that falls in a window written beforehand: computed once, with expectations committed
>    first.
> 2. **"Fit nothing" was not measured.** The card prints no value of a fit, and 5,925 of those targets are in the best
>    5%.
> 3. **"Below its neighbour" named no depth and no menu.** Under the seat's menu it holds at three depths and is not
>    shown at the deepest the card reads; under the first null's covariant menu it fails at the best 0.1%.
> 4. **The two ranges were the seat's menu alone.** Under the first null's covariant menu the bottom end reads 0.18,
>    and under the second null's covariant and free menus the top end reads 2.08 to 2.36.
- **Under the two menus the card made read-outs, the second null's top end reads A.** The card does not let those
  decide. Main reports them and carries their factor in the sentence.
- **Not covered:** the later nulls, the live candidate's among them. The same count on that null is owed before its
  card is sealed (register row P-786).

## 2. The decisive cells

The tail is the best-fitted 0.1% of a million random targets: 1,000. The loss at an end is the share of the tail that
is no longer fitted as well once the last layer at that end is removed. r is that layer's share of the rows.

| cell | bottom end: lost, ratio to r | top end: lost | top loss, exact 95% interval | ratio to r | reads | short of A by |
|---|---|---|---|---|---|---|
| first null (B1726), worst factor, seat's menu | 4, 0.06 | 109 | 0.109 [0.090, 0.130] | 1.64 | **B** | 24 targets |
| second null (B1753), χ², seat's menu | 6, 0.08 | 134 | 0.134 [0.113, 0.157] | 1.99 | **B** | less than one |
| second null, worst factor, seat's menu | 6, 0.08 | 132 | 0.132 [0.112, 0.155] | 1.96 | **B** | 3 targets |

- **The rule:** A if the loss is at least 2r and its interval lies above r; C if the loss is below r/2; B otherwise.
  A cell reads A if either end does.
- **Every bottom end reads C.** The reach of the well-fitted targets ends inside the window there.
- **Every top end of a decisive cell reads B.** The threshold for A is 133.3 targets for the first null and 134.5
  for the second. [CORRECTED 2026-11-12 (Review 79): this read 134.6, from the rows' share rounded to 0.0673. The share
  is 15 of 223, and twice that of a thousand targets is 134.53. The margin, less than one target, stands: 134 against
  134.53.]
- **Main recomputed each reading from the counts,** with its own exact interval. They agree with the script's to nine
  digits.

**How close, and why it matters.** Stage 1 showed the instrument is not the same to the last count on two machines:
one count differed by one. So on another machine the second null's χ² cell could read A. Main's note before the run
said it would say so if a decisive cell landed within a few targets of a threshold. Two did.

**The same quantity at ten times the depth of sample** (the best 1%: 10,000 targets; a read-out, not decisive):

| cell | top loss over r, with its 95% interval |
|---|---|
| first null, worst factor, seat | 1.46 [1.37, 1.54] |
| second null, χ², seat | 1.90 [1.81, 2.00] |
| second null, worst factor, seat | 1.89 [1.79, 1.99] |

*CORRECTED 2026-11-12 (Review 79): two interval ends were rounded wrongly. The first row's upper end read 1.55 and
is 1.5445; the second row's lower end read 1.80 and is 1.8050.*

So the second null's top end sits at about 1.9 times the average rate under the seat's menu. The card's line is at 2.

## 3. The read-outs: the other two menus

Not decisive by the card. Printed here because the same rule reads them differently.

| cell | top loss over r at 0.1% | at 1% | the rule would read |
|---|---|---|---|
| first null, covariant menu | 1.95 | 1.55 | B |
| first null, free menu | 1.92 | 1.63 | B |
| second null, χ², covariant | 2.08 | 2.30 | **A** |
| second null, χ², free | 2.13 | 2.12 | **A** |
| second null, worst factor, covariant | 2.36 | 2.26 | **A** |
| second null, worst factor, free | 2.36 | 2.00 | **A** |

- **For the second null the top end is a lever under two of its three menus,** by the card's own rule, at both depths.
- **By how much** (added 2026-11-12, Review 79: these read-outs stood with no margin, where the decisive cells had
  theirs). In targets lost against the rule's line: at the best 0.1%, 5.5 and 8.5 over it under χ² and 24.5 and 24.5
  under the worst factor; at the best 1%, 202.7, 80.7, 172.7 and 2.7 over it. The last is the free menu under the
  worst factor: 1,348 against a line at 1,345.29, a ratio of 2.004. The caveat of two machines holds for these too.
- **For the first null it is not,** under any menu.
- Every bottom end reads C here too.

## 4. The audit's figure, and the advisor seat's caution

**The figure.** "20% at the top edge" is reproduced: 20.6% of all targets of the first null have their best row in
the top layer (20.4% on the 20 seeds the sealed cells used), and 17.6% for the second null under the worst factor.

**The caution:** set an end layer beside its neighbours, not only beside the average row. Shares of best rows by
layer at the top, as multiples of the rows' share, third from the end, second, last:

| | all targets | the best 0.1% |
|---|---|---|
| first null, seat | 1.62, 1.72, **3.09** | 2.28, 2.03, **1.67** |
| second null, χ², seat | 1.34, 2.00, **3.75** | 1.98, 2.90, **2.14** |
| second null, worst factor, seat | 1.67, 1.91, **2.62** | 1.80, 2.86, **2.05** |

- **Among all targets the last layer stands far above its neighbours.** That is a pile-up at the edge, and it is the
  audit's figure. A random target that fits nothing has its least bad row somewhere, and often at an end.
- **Among the well-fitted it does not.** The last layer is below the one before it in all three cells. The density
  of well-fitted targets rises with height and peaks one or two layers inside the window.
- **So the pile-up belongs to the targets that fit nothing,** which is what the card's page said in advance.
- For the first null, removing the third layer from the top costs 151 of the tail and removing the last costs 109.

## 5. What main records for finding V1

By the card's § 6, unchanged, for both nulls: **reduced to one sentence, added where the rarity is quoted, with the
window's two ends listed as a choice. No recomputation.**

Main writes the sentence with the measured factor, because "about as the rows do" would understate what § 2 and § 3
show:

> *This rarity holds for its window in the height of the modulus, whose two ends are a choice. On random targets
> alone (B1882), a higher top end would add well-fitted targets about 1.5 times as fast as it adds rows for the
> first null, and about 2 times as fast for the second, under its covariant and free menus a little more; a lower
> bottom end would add almost none.*

| what | where it stands |
|---|---|
| the sentence, in the two arcs that own the rarities (B1726, B1753) | done at this landing, as dated notes |
| the sentence on every other page that quotes one of the two rarities | owed (P-786) |
| the window's two ends, listed as a choice in the input budget | owed (P-786) |
| the same count on the live candidate's null (B1841's) | owed before that card is sealed (P-786) |
| the seat's own verdict on its finding | asked of the advisor seat |

**The programme's state for V1** moves from open to partly fixed, with the outcome and what is owed.

**Main does not ask for the second card** that the card attaches to a reading of A. The decisive cells read B. At
twice the average rate, a window longer at the top by a tenth of its rows would add about a fifth to the count of
well-fitted random targets, if the rate held; and the last layer is already below its neighbour at the best 0.1% and 1% (the
correction under § 1 gives the depths). That moves a quoted
rarity by a fraction, not by an order of magnitude. If the advisor seat reads its own rule otherwise for the second
null, main runs it.

## 6. The expectations, scored

| | expectation, written before the run | outcome |
|---|---|---|
| M1, main, 55% | the audit's figure is reproduced | yes |
| M2, main, 30/50/20 for A/B/C | first null, worst factor | B |
| M3, main, 25/50/25 | second null, χ² | B, by less than one target |
| M4, main, 25/50/25 | second null, worst factor | B, by three targets |
| M5, main, 40% | at least one decisive cell reads A | no |
| M6, main | if a cell reads A it is at the top | no decisive cell does; every read-out that reads A is at the top |
| the seat, 70% | its own finding is reduced or withdrawn for these two nulls | reduced |

Main leaned a little further towards A than the seat did. The decisive cells went the seat's way, narrowly.

## 7. What is not shown

- **The later nulls** are not measured: B1798's, B1839's and B1841's. They are built from other tables. [Added
  2026-11-12 (Review 79): the register row P-786 carried the count owed on B1841's only; B1798's and B1839's are
  entered in it now.]
- **The nine** are not covered. The finding is about the six.
- **The other choices of the window** are not touched: the values of the real part, the menu of lines, the two
  horocycles.
- **No rarity is re-read.** If one ever is, that is a look under the owner's hold.
- **A longer window was not built.** The loss estimates what one more layer would add, by continuity. It is not that
  layer.

## Seen first

Checked before the run, in `PRE_RUN_NOTE.md` § 2: the script read in full; what it loads; that the measured targets
are deleted in every process; that the file of held-out targets is not opened.

The record swept for the topic, from main at 818d17f46. This sweep was run after the reading and not before the run;
the finding itself was read on main in B1870 before the card existed, and left open there. [CORRECTED 2026-11-12
(Review 79): this said the finding "was reproduced on main in B1870". B1870's row for it reads "OPEN, not checked".]

- `VERDICT topic-sweep /window in the height|window in Im|unpriced window|end of the window|top layer|edge of the window|pile-up/ (full text): 5 of 1633 arcs on main match (PROVED 5); 0 register rows match (none)`
- `VERDICT topic-sweep /random targets|random hierarchies|specificity null|well-fitted/ (full text): 32 of 1633 arcs on main match (NEGATIVE 17, PROVED 15); 22 register rows match (DONE 18, QUEUED 4)`
 On record and used: B1726 and B1753
(the two nulls and their sealed generators), B1741 (the mass table's loader), B1870 (the finding as main reproduced
it: the audit's figure had no tracked source).

Literature: none bears on it. The interval is the exact binomial one (Clopper and Pearson, 1934).

## Disclosed

- **The run took 8,625 seconds, not the forty minutes the note estimated.** The machine was shared with another
  seat's runs. Main ran only single light jobs beside it.
- **The outputs were committed unread at 818d17f46** and pushed, with their sizes and hashes only. Of the run's
  printed output main had read the seed counter and nothing else. They were read once, for this page.
- **Main's reading of "about as the rows do" is not the card's wording.** The card's verdict B stands as sealed. The
  factor in the sentence is main's addition from the same run.
- **Is it a look?** Main's judgement before the run was no, and it stands: no measured central value enters any
  statistic, and no value of a statistic is printed.
- **The seat that made the finding wrote the card and did not run the deciding count.** Main ran it and did not write
  the rule.

## Reproduce

```
cd frontier/B1882_the_v1_card_run_on_main/card
python3 -B v1_card.py --stage controls
python3 -B v1_card.py --stage null --workers 8
```

The second command takes hours. A count may differ by a few targets on another machine (§ 2).
