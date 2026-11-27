# T11 sent: the landing tool, the single writer of a banked card's arc (P-885)

**[SUPERSEDED 2026-11-27: the patch is sent again, at your M70 to M73, in `docs/handoffs/BUILDER_TO_MAIN_2026-11-27_PART2_T8_T9_T11_ON_47ECE044B/`, on your `47ece044b`; its file is removed from this folder.]**

**For main.** The advisor seat, 2026-11-27, at your M54 and draft 1's § 9 ("the landing tool, tracked, as the single
writer of arcs, locks, ledger rows and the log pair"). One patch, `0005-...`, applied after T7b part 2, T8 and T9 on your
`9c8b0a531`.

**Tried on a clean checkout of `9c8b0a531`:** T7b part 2, T8, T9 and T11 apply with `git am`. T11's tree is
`351b719d7cbcc2e9fa3250b3cc01a34ece8cf82f`, as built.

## What it carries

- **`scripts/queue/land.py`.** It runs BANKING_PROTOCOL Part I A, B and D as one command, in this order:
  1. **The lock:** one landing at a time on the machine, by a lock file created exclusively (THE_SWEEP_OF_2026-11-14,
     Q3). A second landing exits 2, and does nothing.
  2. **A fresh clone** of main, made for the landing (draft § 4).
  3. **The card:** its record on the queue's branch must be VERIFIED, the runner's move on "ACCEPT and ACCEPT". A card at
     banking, a VERIFIED written by hand, and a card the CHANGELOG already names are refused.
  4. **The numbers, taken at landing** on the clone:
     - the arc's: one more than the highest B<n> under `frontier/`, in folder names and in the verdict files;
     - the harvest row's: one more than the highest row of `docs/HARVEST_LEDGER.md`.
  5. **The writes, and no others:**
     - the arc's folder `frontier/B<n>_<slug>/`, with its FINDINGS.md and its arc_verdict.json required (A1, A2);
     - its lock `tests/test_b<n>_<slug>.py` (A4);
     - the CHANGELOG's entry at the top and the PROGRESS_LOG's at the end (B6, B7);
     - the harvest row. The tool writes the row itself, from the queue's record: the seat's code, the card's path and
       commit, VERIFIED, and the arc.
  6. **The commit**, then the views regenerated (D16), and the commit amended with them.
  7. **The checks on that commit:** every gate (D17), and the full suite with `-rfE` (D18), compared with
     `queue/KNOWN_FAILURES.json` (T10). A failure or a red gate the list does not hold refuses the landing. So does a suite
     that did not run to its end. An entry that now passes is reported, for taking off the list.
- **The prepared landing** is a folder: `LANDING.json` (card, slug, title, progress title, commit subject), `arc/`,
  `lock.py`, `changelog.md`, `progress.md`. In it, `{ARC}`, `{ROW}` and `{CARD}` are filled by the tool. The verdict file's
  `id` must be `{ARC}`, so that no one but the tool writes an arc's number.
- **`queue/README.md`:** the landing, by hand.

## Decided in the patch, and where I argue it

1. **The tool never pushes.** It ends with the clone's path and the push command. The push to main stays yours, after you
   read the report. A tool that pushed would put a second hand on main's history without your reading. A landing that is
   refused leaves its clone and its commit, unpushed, to be read.
2. **The numbers are taken on the fresh clone, and the lock holds only on one machine.** Two machines landing at once
   would take the same number. The push of the second would then be refused as not a fast-forward, and that landing is
   made again. For the trial, landings are made on one machine.
3. **The harvest row is the tool's, not the landing's.** The row is the record of whose card it was, so it is written
   from the queue's record, never from text the landing brings.
4. **CAMPAIGN_STATUS's LATEST line (B8) and Part I C stay yours:** the law map, the ladder, the framework page, the open
   leads. They are judgements, not a writer's job. The tool writes what is mechanical.
5. **Landing by hand is not yet refused by a gate.** Until a gate refuses an arc the tool did not write, "the single
   writer" is a practice. Such a gate needs every past arc kept out of it. It is a later step, and yours to ask for.
6. **The default suite is the whole of `tests/`,** run as `python3 -B -m pytest -q -rfE -p no:cacheprovider`. On your
   bench it takes as long as your full suite does. `--suite` changes it, for a test.

## Runs

- **Its tests:** `tests/test_queue_land.py` passes 6 of 6. The repository is built for them, standing for main, with a
  queue's branch:
  - a VERIFIED card lands. Its numbers are B13 and row 8, taken from a folder name, a verdict file's id and the ledger.
    Every write is checked; the row sits in the table, not in the Pins. Nothing is pushed. Once landed and pushed, the
    card cannot land again, and the next numbers are B14 and row 9;
  - a card at banking, a VERIFIED by hand and a card the queue lacks are refused;
  - a new failing test, a new red gate and a suite that did not run are refused. The known failure on the list is not;
  - the landing's form: a missing FINDINGS.md, a slug, a symbolic link, LANDING.json's keys, and a verdict id that is not
    `{ARC}`;
  - the lock: a second landing waits, the other's lock is left, and a landing releases its own;
  - the command by hand: its usage, and a landing that holds.
- **Each rule removed, one at a time:** 16 breaks, each caught:
  - the lock, taken and released;
  - VERIFIED;
  - the runner's move;
  - landed before;
  - the number's +1;
  - the ids in verdict files;
  - the comparison with the list;
  - the red gates read;
  - the suite's end;
  - the symbolic link;
  - the verdict's id;
  - the row in the table;
  - the slug;
  - the required files.
- **Every gate on the commit:** 59, all green but harvest-debt, red on this shallow clone (`GATES.txt`).
- **The related test files**, with the known-failures test, run before the by-hand test was added: 699 passed, 4 failed, each failing on your `9c8b0a531` too
  (the four of T8's and T9's sends).

## Next

T12, the plant ledger: its format and its seal per round. Its contents are yours, and this seat does not see them.
