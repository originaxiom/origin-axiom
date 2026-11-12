seat: sm
read: M4
state: working
on: SM-C3
needs: nothing
next push: when SM-C3's first results are committed

# The SM seat's status (protocol of 2026-11-11, docs/seats/README.md on main)

- **M1 read** (main @ 2f3984d27): verify the physical lane's thirty items. Batch V1 has harvest rows 1418, 1420, 1421,
  1422, 1423, 1425, 1465, 1487, 1488 and 1489. Batch V2 has rows 1517–1535 and 1537.
- **Cards committed, as main proposed them:**
  - `relays/cards/SM_C1_physical-lane-batch-V1.md`
  - `relays/cards/SM_C2_physical-lane-batch-V2.md`
- **The listener runs** as scripts/seats/listen.py --seat sm, taken from main unchanged. It is not a tracked file on
  this branch, so it runs from a copy outside the tree. It showed M1 once and nothing since.
- **This seat's earlier record** (relay §1–§355) stays in `SM_TO_CC_AND_CODEX_2026-10-07_THE_CHIRAL_TRIPLETS_COUNT.md`
  at this branch's root. New work answers through this file and the cards.
- **The firewall** of M1 and § 9 of the protocol applies to all of this work.
- **SM-C1 closed** (batch V1): ten REPRODUCED. The verdicts are in `relays/SM_C1_VERDICTS.md`, and the checks in
  relays/sm_c1/ were committed first (68bccc168).
- **SM-C2 closed** (batch V2): twenty REPRODUCED. Row 1527's comparison with a measured weak angle is CANNOT CHECK
  under the firewall, and nobody makes it. The verdicts are in `relays/SM_C2_VERDICTS.md`. The checks in relays/sm_c2/
  were committed first, together with the lane's six control packages run as found (44 tests, all OK).
- **M1 complete:** thirty items, thirty verdicts. Nothing is needed from main or the lane for it.
- **M2 read** (main @ 69f66fbf3): two rulings of the owner, both dated 2026-11-11, bind every session.
  - His messages are private (register row P-796). Nothing he says is quoted in this seat's pages, status file or
    commit messages.
  - A check is named by its method, in the words of § 12 (register row P-797). A check has a result, not a verdict.
    For the cards, one result per item.
  - Taken: both result notes now name each result by method, in a new section of each. Every own script was rerun
    on a clean checkout at 868170ce5, and all 23 outputs came back byte-identical (the REPRODUCED_RUN.txt files):
    - computed once; reproduced; expectations committed first; tested against planted errors (11 of 11 and 16 of 16
      caught);
    - the lane's controls: computed once;
    - the written reviews and the cited results: not independently checked.
  - In the two cards, "verdict" now reads "result".
- **M3 read** (main @ 323f92327): main has received SM-C1 and SM-C2 and needs nothing more for them. Main will
  recompute one deciding number in each batch by its own route, after the review.
  - The review comes first. Card SM-R79 is committed with main's scope:
    `relays/cards/SM_R79_review-79-seven-arcs-five-locks.md`.
  - It reads seven arcs in full and plants errors against five locks. B1889 judges this seat's own record, so it is
    named and left, as § 13 asks.
  - After it come SM-C3 (the fork lane's four exact packets, register row P-057, run again with this seat's own code)
    and a proposed card for the parameter inventory.
- **SM-R79 delivered:** `relays/REVIEW_79_SM.md`, read at main 323f92327. Its outputs in relays/sm_r79/ were committed
  first.
  - Six arcs were read in full and 43 findings entered, each with its quotation checked by machine: 63 of 63 found.
    B1889 judges this seat's record, so it is named and left.
  - Five locks were tested by planted errors. Caught: E13 4 of 9, E6 3 of 6, E10 3 of 7, E5 8 of 10 (the default
    lane), E3 7 of 12. The shapes missed are named.
  - One standing instance of E3's old form was found, in the root CHANGELOG.
- **M4 read** (main @ 0dda7b472): main's own changes to its instruments in the window, added to SM-R79. The window's
  difference for scripts/checks, scripts/seats and scripts/gates/gates.py was read, with the advisor seat's four
  patches left aside as M4 asks. Five findings are added to `relays/REVIEW_79_SM.md` (R79-SM-44 to 48):
  - the arrival gate excuses a sentence on any earlier denial word, and misses a line break inside its phrase;
  - the debt gates still pass their environment to the checkers, two of which read a variable that changes their
    input;
  - a claim that the commit's day cannot freeze;
  - the listener records a message as shown before it is seen.
- **SM-C3 started:** its card is committed with main's scope: `relays/cards/SM_C3_fork-lane-four-exact-packets.md`.
  It covers the fork lane's four exact packets (register row P-057) at 0c6570bab, run again with this seat's own code.
  The listener reached its session's time limit; main's page is checked by hand at each push.
