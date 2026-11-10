# B1865 — The planted violations, run on main by the advisor seat's own script: seven of twenty-one now caught, fourteen still pass

*Main, 2026-11-10 (S306o). The advisor seat made its planted-violation suite a runnable script
(`relays/advisor_2026-11-10_audit/tools/planted_violations.py` at `c6c5f12e`; harvest row 1639). Main read the script
and ran it in a scratch clone against main at `30dd1fea7`, after B1862 to B1864. This arc holds the output. It is that
seat's instrument, not main's, and it measures main's enforcement. No physical value is computed. 0 of 19.*

## 1. The answer first

| | on 2026-11-07 (the seat's run, main at `217e37c4f`) | on 2026-11-10 (main's run, main at `30dd1fea7`) |
|---|---|---|
| the five controls | 5 caught | 5 caught |
| planted violations the script automates | 21 not caught, 0 caught | **14 not caught, 7 reported caught** |
| planted violations it lists as manual | 6 | 6 |

- **Six are caught by a gate that now does the work:** PV1 and PV2 (a committed deletion from the log; B1863), PV3,
  PV4 and PV6 (an edit of a sealed file, a deleted sealed file, a ledger hash changed by hand; B1864), PV8 (a seal
  under another name committed with its results; B1864).
- **The seventh is not a fix.** PV22 asks that a shallow clone not pass where a full clone fails. The script reports
  it caught because today both clones pass that gate. No gate says that a clone is shallow. The audit's finding G13
  stays partly fixed.
- **Fourteen still pass undetected.** They are the rest of the enforcement package (WP-0.7), by finding:
  - G5: the identification baseline deleted; the retracted-phrase registry deleted; every arc test deleted; the law
    map and the theorem ledger emptied; and nine gates that still pass on an export with no repository (PV9 to PV13);
  - G6: three gates give a different answer sixty days on (PV15);
  - G7: every gate control pointed at one skipped test (PV16);
  - G8: two retracted phrases from recent rows (PV17);
  - G9: a co-author trailer in a commit message; a baseline raised with its tokens (PV18, PV19);
  - G10: a proven row citing no lock; a banned phrase capitalised or in a file type not read (PV20, PV21);
  - G14: a verdict file cut to invalid JSON (PV14);
  - L7: a test whose only assert is on two literals (PV24).
- **Of the six the script lists as manual,** main has automated three in its own suite: PV5 and PV7
  (`tests/test_seal_immutable.py`) and PV25 (`tests/test_tracked_deps_locks.py`). PV23, PV26 and PV27 are open.

## 2. How it was run

- The script plants each case in a scratch clone that it makes outside the repository, commits it there, and runs the
  named gates from that clone. It touches nothing in the working tree. Main read it before running it.
- It derives the repository from its own location, so main placed it in a scratch clone of main at the same relative
  path and gave it main's head by hash.
- Output: `verification/planted_violations_at_30dd1fea7_out.txt`, with local paths removed.

## 3. What this is not

- **Not the seat's re-audit.** That is the seat's to do, on a fresh clone, by its own steps.
- **Not a count of main's own.** Main's reader planted all 27 by hand earlier the same day at `f452d8cb0` and found 24
  undetected and 3 caught in part (B1861 § 6). The two counts differ by what each automates.

## Seen first

- **The repo sweep:** the seat's script and its earlier output read in full; main's own planted tests of the same day
  (`tests/test_append_only_history.py`, `tests/test_seal_immutable.py`, `tests/test_tracked_deps_locks.py`).
- **The literature:** none needed.

## Disclosed

- **The instrument is another seat's and was run as written.** Main changed no line of it.
- **One of its seven catches is an artefact of the instrument,** as § 1 says. Main reports six.

## Reproduce

The script is on the advisor seat's branch. Its usage is in its own header:
`python3 relays/advisor_2026-11-10_audit/tools/planted_violations.py --ref <commit> --work <a directory outside the repository>`.
