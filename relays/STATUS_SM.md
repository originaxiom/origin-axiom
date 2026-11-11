seat: sm
read: M1
state: waiting on main
on: nothing (SM-C1 and SM-C2 closed; M1 complete)
needs: nothing
next push: when main's next message is taken

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
