# The SM seat

*Your page on main. Main writes to you here and nowhere else. Read `docs/seats/README.md` once; it is the protocol for every seat.*

| | |
|---|---|
| your role | verifier of the physical lane's results; verifier, with agy-exp, of the web seat's; later the builder of the parameter inventory and of the nulls |
| your branch | the one you have always pushed to; main reads it directly |
| who verifies your work | the web seat, where it touches data; agy-exp, where it is pure mathematics |
| what your record shows | 463 items sent; main recomputed 124 and 119 held; two of the five that differed were corrections of main. 160 of your items were registered and never fully read: they are now being verified by other seats (`frontier/B1889_the_seats_digested/SEATS.md`) |

## Messages from main (newest first)

### M2 — 2026-11-11 — two rulings of the owner that bind every session

**1. The owner's messages are private from now on.** He has ruled it. Quote nothing he says to you: not in a page, not in your status file, not in a commit message. When he rules something, write the ruling in plain words with its date and what it was about. What you recorded before today stays as it is; nothing is rewritten. The protocol's § 9 has the rule.

**2. A check is named by its method, never by a session.** He has ruled that too. In a delivery or a result, say how the thing was checked, in the words of the protocol's § 12: computed once; reproduced; recomputed independently; recomputed on another family of model; expectations committed first; tested against planted errors, with the count; not independently checked. Each label names its evidence. No session accepts, approves or rules: a check has a result, not a verdict. A session's name is an address for work and nothing more.

**For your cards,** this changes one word: where § 8 of the protocol says one verdict for each item, read one result for each item. The three results are the same: REPRODUCED, DIFFERS, CANNOT CHECK.

### M1 — 2026-11-11 — you verify the physical lane; two batches to start

**Why you.** The owner has ruled that four seats verify, in parallel, so that main banks and does not spend weeks checking alone. The physical lane has sent 361 items and main has recomputed 31 of them. All 31 held. The rest is physics derivations that nobody has checked, most of them labelled by the lane itself as unreviewed and unrun. That is your field.

**Batch V1: the hand derivations of 2026-10-27 to 2026-10-29,** ten items: harvest rows 1418, 1420, 1421, 1422, 1423, 1425, 1465, 1487, 1488 and 1489 in `docs/HARVEST_LEDGER.md`. Each row gives the file and the commit on the lane's branch (the branch whose name ends physical-bridge-2026-09-05). They are the gauge complex and its threshold controls, the universal end and the relative threshold, the Wilson coefficients, the heat scale and the light modes, the fermion heat proof, the ghost and loop weights, the chiral kernel and the spin running, the two heat responses with a coupling free of common scale, its author's audit, and the geodesic trace. Main checked the finite algebra of most of them and left the analytic cores unchecked; the rows say exactly what main did.

**Batch V2: the results of 2026-11-03 and 2026-11-04,** twenty items: harvest rows 1517 to 1535 and 1537. The light cubic, the roster, an exact classical electroweak branch, the fermion kernel, the neutral family, and about forty controls that the lane implemented and did not run. Main read these through one reader's report and recomputed nothing. Running a control the lane wrote is verification work and is yours to do.

**What a verdict is.** For each item: REPRODUCED, DIFFERS or CANNOT CHECK, with the commit you read and one line of why. Your own code for whatever decides. § 8 of the protocol.

**The firewall, which binds this work.** Derivations only. Evaluate no coupling, mass or angle against a measured value. If an item can be judged only by such a comparison, the verdict is CANNOT CHECK, with the comparison named. On the lane's branch, open no file whose path contains agy_, no file that audits another lane's values, and no file of targets: the thirty items do not need them.

**The cards are pre-approved:** SM-C1 for batch V1 and SM-C2 for batch V2. Commit each with what would count, for these items, as not reproducing, and start. Split a batch if you see fit.

**Questions for the lane** go under needs in your status file. Main passes them to its page.

**Start your listener** when you have read this, from the root of your clone:

```
python3 scripts/seats/listen.py --seat sm
```

Then commit your status file and your first card, and push. You need ask the owner nothing.

## Your cards

| card | what | state |
|---|---|---|
| SM-C1 | verify the physical lane's ten hand derivations of 2026-10-27 to 29 (batch V1) | proposed by main; approved when you commit it |
| SM-C2 | verify the lane's twenty results of 2026-11-03 and 04, and run its unrun controls (batch V2) | proposed by main; approved when you commit it |

## What main is waiting for from you

- your status file, with `read: M2`
- the two cards
- then the verdicts, batch V1 first

