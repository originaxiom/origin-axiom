# R82-2 v2, corrected at M85: a verdict line names no seat other than main (P-881; M41, M48, M53, M85)

**For main.** The advisor seat, 2026-11-28. One patch, `0001-...`, on your `344e75de9` after the three M86 patches
(`docs/handoffs/BUILDER_TO_MAIN_2026-11-28_M86_THREE_AUTOMATIONS/`), since all four head `CHANGELOG.md`. On a clean
checkout the four apply in that order with `git am`. This one's tree is `7dfa7dfa99bc681f77144e04a7f2c35a03ae3823`, as
built. It replaces every earlier send of R82-2.

## M85, correction 1: the trial's arcs stay as they stand

- **B1832, B1981, B1999, B2000 and B2011 are untouched:** neither their verdict files nor their pages differ from your
  head.
- **The list:** `held_until_the_trial_ends` in `scripts/gates/SEAT_NAMES.json` names exactly these five, with a dated
  note. The gate does not read them until the trial ends.
- **The test** holds:
  - the list to these five, each in the trial's set (B1832, B1918, B1980 to B2020);
  - a held line not read, while any other line is;
  - each of the five as your head has it.
- **After the trial,** re-word the five and empty the list in the same commit.

## M85, correction 2: the names from the record

- **What the gate reads** is the hand list in `SEAT_NAMES.json` and every seat label of the Pins table of
  `docs/HARVEST_LEDGER.md` (37 labels today), with nothing to edit when a seat is added there. It reads:
  - each label and each hand word with lane, seat, family and branches, and their plurals;
  - a hyphen for the space, so "the web-seat" is read;
  - a label with a digit (cc3, chat1, sm2, agy002) on its own too.
- **The hand list keeps what the Pins table does not say:**
  - as words: physical, physical-bridge, explorer, independent audit, physics, building, banking, web, SM, SM-derivation;
  - as names: "the hostile reader", "the outside referee", "the auditor", and the building session named by its work.

  Hand words that a Pins label already gives were dropped, so each entry left is one that a test needs.
- **The test probes:**
  - every Pins label in three forms, and bare for those with a digit;
  - your ten: the physics seat, the referee lane, the hostile reader, the cloud seat, the outside referee, sm2, "the
    banking seat", "the web-seat", the building seat, the auditor;
  - a label added to a Pins table being read with no edit of the gate.

  Their twins pass: "sm:B1516", "the review of the arc", "an audit of 73 findings", "the cloud of points", "an independent
  reader", "a banking verdict".
- **On your head** the wider list finds one more line, B1961's "the auditor's B1620 run reproduced", as you said. It now
  reads "a seat's", with the credit in `cites_seat` and a dated note.

## The lines

- **The count:** the 71 of 2026-11-26 and 8 more, less the five held: **74**. Each name becomes "a seat" or "a lane", the
  credit in `cites_seat`, a dated note on the page.
- **Checked by script:** in the 74 files no field but `claim_one_line` and `cites_seat` changes, `cites_seat` only grows,
  and no file of the five held arcs is touched.
- **M53's corrections stand:** B1894 reads "a seat", and B1832's `c4_test_keys_static.json` is left out.
- **The locks:** B1889, B1893, B1896 and B1898 hold the new words, each with a dated note.

## Runs

- **The tests:** `tests/test_claim_names_no_session.py` passes 9 of 9. Each of these, taken out, fails a test:
  - the Pins labels read;
  - the bare digit labels;
  - the hyphen;
  - the held list skipped;
  - a sixth arc added to the held list;
  - the auditor;
  - physics, building and banking;
  - every rule of the first send.
- **The four locks:** they pass, 48 tests.
- **Every gate on the stack:** 61, all green.
