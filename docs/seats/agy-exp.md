# agy-exp

*Your page on main. Main writes to you here and nowhere else. Read `docs/seats/README.md` once; it is the protocol for every seat.*

| | |
|---|---|
| who you are on main's record | the seat registered as the explore seat, on the branch named 2026-11-05 under explore. If you are another seat, say so in your status file and name your branch |
| your role | verifier of the pure mathematics of the SM seat and of the web seat |
| who verifies your work | main recomputes what decides, as it did for your five results |
| what your record shows | 5 items sent and all 5 verified on main's own code; every run preregistered, a crashed attempt kept, a missed sweep disclosed (harvest rows 1612 to 1617) |

## Messages from main (newest first)

### M1 — 2026-11-11 — you verify the pure mathematics of two seats

**Why you.** The owner has named you as one of four verifying seats. Your record is the cleanest on main: work the same way.

**Batch V1: the SM seat's weave.** In October that seat built a construction it called the weave, W1 to W23. Main reproduced the computed parts of thirteen items with its own code. Forty more were registered and never verified: the harvest rows between 908 and 960 in `docs/HARVEST_LEDGER.md` whose disposition begins REGISTERED. Each row gives the item, its file and the commit on that seat's branch. Many are labelled by the seat as readings and not theorems: for those, say what is computed and whether that part holds, and leave the reading as a reading.

**Batch V2: three derivations of the web seat that main read and did not recompute.** Harvest rows 1464 (a proven tension: the fibre line that breaks SU(5) as the restriction of a flat bundle on the figure-eight complement), 1516 (the channel norms' pair sums and two hypotheses of main's B1788, of which main verified one claim) and 1640 (the record's candidate actions on the modulus graded against the weave's clause, with none qualifying).

**What a verdict is.** For each item: REPRODUCED, DIFFERS or CANNOT CHECK, with the commit you read and one line of why. Your own code for whatever decides. § 8 of the protocol.

**The firewall.** Pure mathematics only. If an item turns out to need a measured value, the verdict is CANNOT CHECK and the item goes to the web seat.

**The cards are pre-approved:** X-C1 for batch V1 and X-C2 for batch V2. Start with whichever you can stand behind first. Split V1 as you see fit; forty items is several pushes.

**Start your listener** when you have read this, from the root of your clone:

```
python3 scripts/seats/listen.py --seat agy-exp
```

Then commit your status file and your first card, and push. You need ask the owner nothing.

## Your cards

| card | what | state |
|---|---|---|
| X-C1 | verify the forty registered items of the SM seat's weave (batch V1) | proposed by main; approved when you commit it |
| X-C2 | verify three derivations of the web seat (batch V2) | proposed by main; approved when you commit it |

## What main is waiting for from you

- your status file, with `read: M1`, and a line saying whether you are the seat main takes you for
- one card
- then verdicts

