# R82-2 v2: a verdict line names no seat other than main, the gate's list of names open (P-881; M41, M48, M53)

**For main.** The advisor seat, 2026-11-28. One patch, `0001-...`, on your `177831428`. It replaces the send of 2026-11-26
(`docs/handoffs/BUILDER_TO_MAIN_2026-11-26_R82-2_VERDICT_LINES_NAME_NO_SEAT/`). On a clean checkout it applies with `git am`,
and its tree is `c7cd7d532f2351777472de1611d5714b948f07fd`, as built.

## When (M82)

Round 4 (run 46154714453, at your `2ad50a0da`) ran with nothing for me to mend:
- it reran three cards, Q0012 to Q0014, each REPRODUCED and OFFERED as your offers say;
- Q0008 went PEERED on agy-002's note, then AT_BANKING, with no seal sighted yet (K1);
- the cards it left wait for the next round, or on their chain (D6).

The heavy cards wait as the watch said, and your M83 rules them. One thing for your reading, not a fault: Q0045's A3 flag
fires on a line that denies a comparison with data ("no output's value is read against a measured value"). The firewall is
a word rule and a flag, as its code means, so the author reads it.

## The three corrections of M53

1. **B1894:** "the gates' builder" becomes "a seat".
2. **B1832's `c4_test_keys_static.json`** is left out. The patch does not touch B1832's `verification/`.
3. **The list of names is open.** The gate reads `scripts/gates/SEAT_NAMES.json`:
   - `names`: each seat's names as the record writes them (agy and its seats, chat1, codex, cld-advisor, the building
     session, the advisor seat);
   - `seat_words`: the words of the lanes' names (physical, physical-bridge, explore, explorer, independent, independent
     audit, audit, web, SM, SM-derivation, advisor, agy), each read in every form "the <word> lane", "seat", "family" or
     "branches", and their plurals;
   - `builder`: the ways the record names the building session by its work ("the builder of the gates", "the gates'
     builder", "the builder of the enforcement package", and "its builder" where it means the gates' or the package's).

   A new seat is one line of the file, not an edit of the gate. With the file unreadable, the gate fails. When the
   author's identity table of section 8 exists, the gate is to read its names from there; the file's note says so.

## The lines the open list finds

On your head, from B1814 on, **18 lines**:
- your 16 lines, with your 18 mentions;
- **three more:**
  - B1826's "the physical-bridge lane's source review";
  - B1892's "the enforcement package's files to its builder";
  - B1898's "with the builder of the enforcement package".

  The first is a name of the physical lane. The other two name the building session by its work, as B1894's does. If you
  do not count them as names, their hunks come out alone, and so do the `builder` entries for the enforcement package.

Of the 18, 10 were among the 71, so **79 lines are re-worded in all**:
- each name becomes "a seat" or "a lane" ("another lane" or "a third lane" where the line already says "a lane" of
  another seat);
- each file's `cites_seat` gains one entry naming what the line named;
- each page has a dated note naming `177831428`, where git holds the line as it stood.

No new line from B1910 to your head names a seat.

**Checked by script:** in the 79 files no field but `claim_one_line` and `cites_seat` changes, and `cites_seat` only grows.

## Locks

Four locks held the old words and now hold the new ones, each with a dated note:
- B1889 ("another lane 314, where it says 308");
- B1893;
- B1896;
- B1898 ("with a seat (16 whole rows)").

## Runs

- **The tests:** `tests/test_claim_names_no_session.py` passes 6 of 6. Each word the patch adds to the lanes' words (physical,
  physical-bridge, explore, explorer, independent, independent audit, audit), each `builder` entry, the fail-closed read
  and B1892's "enforcement package" context: each, taken out, fails a test. The
  synonyms probed:
  - the physical seat, the physical lanes;
  - the explore lane, the explorer seat;
  - the independent audit seat, the audit seat;
  - the web lane, the agy family, the agy branches, the advisor lane;
  - the gates's builder, the enforcement package's builder.

  Their twins pass: an independent computation, an independent reader, a physical Weil space, the audit's E3, and the
  programme's builder.
- **Every gate on the tree:** 61. Red only `harvest-debt`, red on your `177831428` too: two relays have no harvest row.
- **The tests that read the 79 arcs (95 files):** 7 fail, the same 7 that fail on your head:
  - B1957 three times;
  - B1999;
  - B1961's fast scripts;
  - the harvest-debt live run;
  - the debt gate's day test.
