# THE V1 CARD — PREREGISTRATION: does an end of the window in Im τ move a null's count of well-fitted random targets?

**From:** the advisor seat. **To:** cc and the owner. **Kind:** `propose:` (a sealed card, designed here; its second stage
is main's to run or to refuse).
**Sealed:** this page and `v1_card.py`, by the hashes in `ARTIFACT_HASHES.txt`, in a commit of their own, before either
stage touched an instrument of the record. Only the toy self-test had run (`selftest_out.txt`).
**Null-only:** no measured target enters any statistic. No rarity is re-read.

## 1. In one sentence

**For two named nulls of the six, the card counts how many of the null's best-fitted random targets are lost when the
last layer of the window in Im τ is taken away at one end, and sets that beside the layer's own share of the rows.**
That is the quantity the audit's finding V1 asserted and never measured in a tracked form.

## 2. The finding, and why it is still open

| | |
|---|---|
| the finding (audit, 2026-11-10, graded as a reader's) | "Every 'specificity' null for the six has an unpriced τ window. 20% of random targets have their best fit at the top edge of the Im τ grid, while the data's optimum sits inside. All quoted rarities are biased low by an unmeasured amount." |
| main's state (B1870) | OPEN, not checked: "the audit's figure has no tracked source, and deciding it needs a computation on the nulls that belongs behind a sealed card", and the audit "does not say which null it measured" |
| what exists | the reader's two scripts (`read_of_b1861/sources_for_b1870/`), not re-run, with no transcript |

This card is the sealed card main named. It gives the figure a tracked source, names the nulls, and fixes in advance
what would confirm the finding, reduce it, or withdraw it.

## 3. What is computed

**The two nulls.** Main's sealed modules, loaded unchanged and checked by hash in the script.

| | the null | rows | the window in Im τ | measure |
|---|---|---|---|---|
| **N1** | B1726's (cells R2 to R4) | 47,880: 266 lines, 6 values of Re τ, 15 of Im τ, 2 horocycles | the plain grid 2.05, 2.15, …, 3.45 | the worst factor |
| **N2** | B1753's (cell P2, and its read-outs) | 21,408: 223 apexes, 48 lines, 2 horocycles | apex heights from 2.013 to 3.562 | χ², and the worst factor |

**The targets.** The generator of the sealed cells, unchanged. For each null: the 20 seeds the sealed cells used (1726
to 1745; 1789 to 1808) and 230 fresh seeds (9172601 to 9172830; 9175301 to 9175530), 4,000 six-targets a seed:
**1,000,000 targets a null.** The fresh seeds are there because a rarity is read deep in the tail, and 80,000 targets
leave 80 at the depth of 0.1%.

**For each target:** its best statistic over the rows and the menu, and the row that gave it. Three menus (seat,
covariant, free), as the sealed cells have.

**The tail.** The best-fitted 0.1% of a null's targets, by the null's own order: 1,000 targets. No observed statistic
is used to define it.

**A layer.** At each end of the window, the fewest extreme distinct heights that hold at least a fifteenth of the
points: for N1 one grid value (2.05; 3.45), for N2 at least 15 apexes. Layer 2 and layer 3 are the next ones inward.
The script prints each layer's heights and its share of the rows.

**The decisive quantity: the loss.** Take the tail. Remove layer 1 at one end. Count the tail's targets that are no
longer fitted as well as the tail's last member. That count over 1,000 is the loss at that end.

- **Why this and not where the best rows lie.** A target's best row can sit in the last layer while a row further in
  fits it nearly as well; then the last layer adds nothing. The loss counts only what the layer alone provides.
- **What it estimates.** By continuity, the share by which the count of well-fitted random targets would grow if one
  more layer were added at that end.
- **Its natural scale is the layer's share of the rows** (about 1 in 15). If well-fitted random targets are spread
  evenly in height, an end layer costs about its share: the toy self-test shows this (ratios 0.88 and 0.88), and it
  corrected this seat's first intuition before the seal (§ 11).

**Decisive cells, three:** N1 with the worst factor and the seat's menu; N2 with χ² and the seat's menu; N2 with the
worst factor and the seat's menu. The other six cells (the covariant and free menus) are read-outs.

**Read-outs, printed and not decisive:** the loss at 1%; the loss when layer 3 is removed in place of layer 1; where
the best rows lie by height, for all targets and for each tail (5%, 1%, 0.1%, 0.01%); the same on the 20 sealed seeds
alone.

## 4. What is not computed, and the owner's hold

- **No measured target.** Main's loaders build the measured targets as they load the census. The script deletes them
  in every process before anything is computed, and asserts they are gone.
- **No comparison file is opened.**
- **No value of a statistic is kept or printed.** The outputs hold counts and shares only. So no printed number can be
  set beside a banked observed statistic to make a new comparison.
- **One thing a reader should know.** N2's χ² divides by the measurement's relative uncertainties, as the sealed
  measure defines them, and main's loader reads that file. No central value enters.
- **No rarity is re-read here.** If one is ever re-read, that is a later card under the owner's hold, counted as one
  look.

Whether this card needs a row in the look ledger is main's judgement. This seat's view: it is not a look.

## 5. Stage 1: the planted controls (no random target is drawn)

Rows of the census are used as targets, each under the seat's first reading with c = 1, where its statistic is zero.
A row whose six values another row shares exactly is never planted, and is counted.

| | planted | must give | if it does not |
|---|---|---|---|
| **K1** | every 97th row, under each measure and menu | found again at zero, and at its own height for at least 99% | stage 2 refuses to run |
| **K2** | every row of layer 1, at each end; then every row of layer 3 | with layer 1 removed: the plants of layer 1 are lost (at least 99%), the plants of layer 3 are all kept | the decisive cells of that measure read NOT VALID |
| **K3** (a read-out, no pass or fail) | every row of layer 1, against the window without layers 1 and 2 | where they find their best fit: on the nearest layer left, or elsewhere | — |

K3 says which regime the instrument is in. If a row beyond the window is best fitted by the nearest layer left, height
is what places a target. If it is fitted from anywhere, other lines stand in for height, and "where the best rows lie"
says little; the loss is built not to depend on that.

## 6. The reading, fixed before any number

For each decisive cell and each end, with r the layer's share of the rows:

| | when | it means |
|---|---|---|
| **A** | loss ≥ 2 r, and the exact 95% interval of the loss lies above r | **that end is a lever.** Well-fitted random targets come from it at twice the average rate or more; a longer window would add them faster than it adds rows |
| **B** | otherwise | **that end is like other rows.** The count grows about in proportion to the rows |
| **C** | loss < r / 2 | **that end adds almost nothing.** The reach of the well-fitted targets is ending inside the window |

A cell reads A if either end does; C if both do; B otherwise.

**What each outcome does to V1, for that null:**

| the cell reads | V1 | what follows |
|---|---|---|
| **A** | **stands.** The null's count depends on where the window ends, more than in proportion | a second card extends the census at that end (data-free) until the new end reads B or C. A re-read of the rarity is then one counted look, under the hold |
| **B** | **reduced to one sentence.** No pile-up. Each quoted rarity holds for its window, and the count of well-fitted random targets grows about as the rows do | the sentence is added where the rarity is quoted, and the window's two ends are listed as a choice. No recomputation |
| **C** | **withdrawn** for that null | nothing |
| NOT VALID | undecided | the control is mended first |

**The audit's figure.** "20% at the top edge" is reproduced if any of six shares of *all* targets (the top layer, both
ends, the highest band, the ten highest heights, on either null) lies between 17% and 23%. Otherwise it is withdrawn as
a number, whatever the cells read. The share of all targets is not the decisive quantity: a random target that fits
nothing has its least bad row somewhere, and often at an end, for no reason that bears on a rarity.

## 7. This seat's expectations, sealed with the card

| | expectation | probability |
|---|---|---|
| E1 | K1 holds on both instruments | 93% |
| E2 | K2 holds for all three measures | 85% |
| E3 | the audit's figure is reproduced | 50% |
| E4 | N1, worst factor, seat: A / B / C | 20% / 55% / 25% |
| E5 | N2, χ², seat: A / B / C | 20% / 50% / 30% |
| E6 | N2, worst factor, seat: A / B / C | 20% / 50% / 30% |
| E7 | at least one decisive cell reads A | 30% |
| E8 | if a cell reads A, it is at the top | 65% |
| E9 | K3: on N1 at the top, a row of layer 1 finds its best fit on the nearest layer left more often than that layer's share of the rows | 75% |

**So this seat expects, at 70%, that its own finding will be reduced or withdrawn for these two nulls.** The finding
was a reader's figure taken up without a transcript; that is what the card is for.

## 8. What the card does not cover

- **The later nulls:** B1798's class-choosing nulls, and the nulls of B1839 and B1841, the live candidate. They are
  built from other tables. If a cell here reads A, the same count on those is the next card; if all read B or C, the
  finding stands unmeasured for them and this seat does not press it.
- **The nine.** The finding is about the six.
- **The other choices of the window:** the values of Re τ, the menu of lines, the two horocycles. Each random target
  gets the same ones, and the finding is not about them.

## 9. An amendment to this seat's own acceptance row, made before any number

The acceptance row for V1 (2026-11-10) asked that "fewer than 1% of random targets have their best fit on a boundary
row". **That measured the wrong population,** and no finite window could meet it: with rows drawn evenly a fifteenth of
all targets sit on each end. The row is replaced by § 6 (ACCEPTANCE_CRITERIA § 15).

## 10. Who runs what

| stage | by | then |
|---|---|---|
| the toy self-test | this seat, before the seal | `selftest_out.txt`, in the seal commit |
| **stage 1, the planted controls** | **this seat, after the seal** | outputs committed unedited, in a commit of their own. If a control shows a fault in the script, the script is amended before stage 2, with a dated note here and a new hash |
| **stage 2, the null** | **main, or nobody.** The seat that made the claim does not run the count that decides it | if main runs it: outputs committed unread, then read once. If main refuses, the finding stays open with the reason |

To run, from anywhere inside a checkout of the repository that holds this folder:

    python3 -B v1_card.py --stage controls
    python3 -B v1_card.py --stage null --workers 8

Stage 1 prints how many targets a second each measure handles, from which the length of stage 2 follows.

## 11. Disclosed

- **Not blind.** This seat has read the reader's claim (20%, the top edge) and the reader's scripts. It has seen no
  output of either.
- **The self-test corrected the design's author.** The first version of the toy asserted that, with targets spread
  beyond the window, removing the end layer loses more than removing an inner one. The toy gave 81 against 88: it does
  not. With a tight tail each layer has its own targets, the end layer among them, and the right statement is the one
  in § 3. The check was rewritten as three toys of known answer (even, crowded at the top, ending inside) before the
  seal.
- **The first design was dropped before the seal.** It took "the share of the tail whose best row lies in the last
  layer" as decisive, with a control for whether a target beyond the window shows at the end. The loss replaced it for
  the reason in § 3; the older quantity is still printed.
- **The thresholds 2 and ½ are conventions,** fixed here. The 95% interval is exact (Clopper and Pearson).
- **The depth.** The tail is read at 0.1%. N1's sealed rarity is of that order; N2's decisive cell was read ten times
  deeper, where a million targets leave a hundred. The card prints where those hundred lie and does not decide on them.
- **The fresh seeds** were chosen by this seat. No file of the tree uses them as seeds (searched on main at
  `3e25c8ec3`).
- **The instruments' hashes** are those of main at `3e25c8ec3`, equal to the ones on this branch.
