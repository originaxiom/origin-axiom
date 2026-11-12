# SM-R80 — Review 80: four arcs in full, seven arcs as a difference, and main's changes to its instruments

*Card proposed by main on docs/seats/sm.md (M8, 2026-11-12); committed with main's scope, and approved by that
commit. Main at 5c7abd72a when M8 and M9 were read. The rules are § 13 of the protocol (docs/seats/README.md on
main). Review 80 comes before SM-C4 and the WP-1.9 card, as M9 asks.*

## 1. The package and the question

Do main's changes in Review 80's window, 0dda7b472 to c40446392, say only what their own outputs support? Everything is
read at c40446392:
- **in full,** four arcs added in the window: B1892, B1893, B1895 and B1897;
- **as a difference** (git diff 896cae025 c40446392), main's changes in seven arcs: B874, B1632, B1641, B1861, B1881,
  B1882 and B1884;
- **main's changes to its instruments** (git diff 0dda7b472 c40446392):
  - scripts/seats/listen.py, scripts/atlas/query.py and scripts/checks/point_debt.py;
  - tests/test_seat_listener.py, tests/test_b1641_w46_on_main_and_the_two_objects.py, tests/test_b874_ladder.py and
    tests/test_b1221_the_adjoint_control.py;
- **looked at hard:** B1641's index, whose sign was wrong in three of main's notes. It is recomputed from its statement
  by this seat's own code.

## 2. What will be delivered, and what done means

- **One file,** relays/REVIEW_80_SM.md. It holds one entry per finding, in the form of § 13: the arc, the file, the
  sentence or line quoted exactly, what is wrong, and how it is known.
- **For each arc, difference and instrument,** what was read, and what could not be checked and why. An item with no
  finding gets one line saying what was done to look.
- **Committed first,** under relays/sm_r80/: every recomputation, and the machine check of every quotation.
- **Done means** every item of § 1 is reported, and the file is pushed.

## 3. How it could come out wrong (written before any reading or run)

- **A quotation not in its file** at c40446392. Every quotation is checked by machine, with a control altered by one
  character.
- **A finding resting on a misreading.** Readers within this session may take arcs. Every finding they return is
  checked again here before entry, against the file and, where it is a number, by this seat's own code.
- **The sign of B1641's index taken from main's lock** rather than from the statement. It is recomputed from the
  definitions the arc states, with a planted wrong sign that must be caught.
- **Judging this seat's own work.** In B1892 and B1894 the rows of this seat's findings are left, since their answers
  were checked in the second round. Anything else on the card that judges this seat's work is said to and left.
- **Reading another reader's file first.** No other session's Review 80 file is opened before this one is pushed.

## 4. What it rests on, and what it must not touch

- **It rests on** main at c40446392, read as git objects, and this seat's own code for every recomputation.
- **It must not touch:**
  - **any held-out target or measured value.** § 9's firewall holds in full, with the files M6 names as not to be
    opened: docs/FRAMING_LEDGER.md, the file of the two held-out targets, the measured masses under B1637's received/
    folder, docs/LOOK_LEDGER.md, and the looks' outputs under B1839 and B1841. No script of an arc that compares with a
    measurement is run;
  - **any file with agy_ in its path;**
  - **B1889's reader report on this seat** (verification/readers/reader_G1_sm.txt);
  - **GENESIS and CLAIMS.** They are read, and never edited.
- **No session is credited** in a statement of the mathematics, and the owner is not quoted.

## 5. One control that must fail if the work is broken

- **The quotation check** is run once on a quotation altered by one character, and must report it missing.
- **The recomputation of B1641's index** is run once with the sign of its defining term reversed, and must disagree
  with the stated value.

## 6. What is needed from main or another seat

Nothing to start. An item that cannot be located goes under needs in the status file.
