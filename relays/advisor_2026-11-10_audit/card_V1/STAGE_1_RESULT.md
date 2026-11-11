# THE V1 CARD — STAGE 1: the planted controls hold; the card is ready for main to run or to refuse

**From:** the advisor seat. **To:** cc and the owner. **Kind:** `verify:` (of this seat's own instrument).
**Sealed at** `84430d1c7`. **Run once, with the sealed script** (sha256 `beef66a2caa96fae…`; the hash list still
verifies). **Outputs committed unedited at** `b4bdc02f0`, before this page was written: `v1_controls_run.txt`,
`v1_controls.json`.
**No random target was drawn. No measured target entered.** Stage 2, the null, has not been run by anyone.

## 1. The result

| | the control | result | this seat's sealed expectation |
|---|---|---|---|
| **K1** | a planted row is found again, at zero and at its own height | **holds on both instruments,** under each measure and menu: 495 of 495 rows on B1726's census; 222 of 222 on B1753's | E1, 93%: held |
| **K2** | with the last layer removed, its planted rows are lost and the planted rows of layer 3 are kept | **holds for all three measures,** at both ends and under each menu: every plant of layer 1 lost, none of layer 3 | E2, 85%: held |
| **K3** (a read-out) | where a row of layer 1 finds its best fit once layers 1 and 2 are gone | **on the nearest layer left, for 70% to 86% of them,** which is 7.5 to 8.6 times that layer's share of the rows | E9, 75% that it exceeds the share on B1726's top: held (74%) |

So the script does on main's real instruments what the toy self-test showed on a toy. Nothing was amended.

## 2. What K3 says about the instruments

**Height is what places a target.** A row that sits beyond a narrowed window is best fitted, three times in four, by
the nearest layer left, and almost never from the far end (0 to 88 of some 1,400 to 3,200). Other lines do not stand
in for height. So "where the best rows lie" is readable on these instruments, and a target whose true best lies
beyond the window does show at the window's end.

That is the premise the audit's finding needs. It is not the finding: whether well-fitted *random* targets crowd an
end is stage 2.

## 3. Two things the run showed about the censuses

- **No row of either census shares its six values exactly with another** (0 of 47,880; 0 of 21,408).
- **On B1753's census, under χ², a planted row is often found at another point of the same height** (130 of 222 at
  the planted point; 222 of 222 at the planted height). The apexes come in mirror pairs whose rows agree to rounding,
  and the expanded χ² cannot tell them apart. The card's layers are sets of heights, so this does not touch its
  count. The worst-factor measure finds the planted point every time.

## 4. The layers, as the script fixed them

| | bottom layer 1 | top layer 1 |
|---|---|---|
| B1726's census | Im τ = 2.05: 6 points, 6.67% of the rows | Im τ = 3.45: 6 points, 6.67% |
| B1753's census | heights 2.013 to 2.064: 16 apexes, 7.17% | heights 3.381 to 3.562: 15 apexes, 6.73% |

## 5. How long stage 2 will take

| | targets a second, one process, three menus | a million targets |
|---|---|---|
| B1726's census, the worst factor | 90 | 3.1 hours of one process |
| B1753's census, χ² | 235 | 1.2 hours |
| B1753's census, the worst factor | 239 | 1.2 hours |

**About 5.4 process-hours: some 40 minutes on 8 workers.** Measured here on this seat's machine.

## 6. A plumbing test of stage 2, on planted targets (added after the page above)

Stage 1 ran the card's counting one function at a time. It never ran the second stage's own code: the pool, the
pooling of seeds, the tails, the leave-out recount, the reading, the files. Since this seat does not run stage 2, a
fault there would have been met first by main. So the sealed script was run from end to end with its generator of
random targets replaced, in memory, by rows of the census chosen evenly and moved by a small step
(`plumbing_test_of_stage_2.py`, committed before its run; output beside it). **No random target was drawn.**

| expectation, written first | result |
|---|---|
| the second stage runs to its last line on both instruments and writes its files | held |
| planted evenly, every decisive cell reads B | held. The six losses are 0.53 to 1.65 times the layer's share, on tails of 200 planted targets: 7 to 22 lost where 13 are expected. A tail of 200 is noisy, and 0.53 is close to the bound of C; the card's own tail is 1,000 |
| the share of targets found in each end layer is the share planted there | held, to 0.0018 |

Its outputs went to a temporary folder. Nothing in this folder is a run of stage 2.

**A caution the test raised, stated before any null is run.** "Planted evenly over the rows" did not come out quite
even in the tail on B1726's census: 7 of 200 at the bottom end and 22 at the top, and over the fifteen heights a χ² of
26.6 on 14 degrees of freedom. The rows are not equally spaced in the space of the six ratios, so a row's share of a
tail need not be its share of the rows. The sealed reading sets the loss beside the layer's share of the rows and
allows a factor of two either way; that margin is what covers this, and it is not wide. **So a reader of stage 2
should also set each end layer beside its neighbours,** which the card prints (the loss without layer 3; the shares by
height), and not only beside the average row. The sealed reading is not changed.

## 7. For main

    python3 -B v1_card.py --stage null --workers 8

It refuses to run unless `v1_controls.json` stands beside it with K1 holding, which it now does. It writes
`v1_null_run.txt` and `v1_null.json`, which hold counts and shares only. The reading of every outcome is fixed in
`PREREGISTRATION.md`, § 6. If main refuses the stage, the finding stays open with main's reason.
