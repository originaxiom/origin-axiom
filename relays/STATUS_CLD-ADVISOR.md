seat: cld-advisor
read: M2
state: working
on: C1
needs: nothing
next push: when the patches of C1 are sent with their cover note, or sooner if main writes

# cld-advisor — status

This seat's status page is `relays/advisor_2026-11-10_audit/THE_ADVISOR_SEATS_PLAN.md`, § 9, as before. It is
rewritten at every push, and so are the six lines above.

## Taken from M1

| | |
|---|---|
| the role | builder of five packages, and no longer an auditor. The plan page says so (§§ 3, 7 and 9) |
| the listener | started. This session's clone is on the seat's own branch, where the script is not, so it runs a copy of main's `scripts/seats/listen.py` with `--repo` on the clone. This session can keep a background command for two hours at most; the listener is started again at each expiry |
| the card | `relays/cards/cld-advisor_C1_wp-0-7-series-3.md`, inside the package main proposed |
| the owner's words | entered in plain words and dated from M1 on, by § 9 of the protocol. What the seat's file of his words holds from before stays as it is until he rules (main's row P-796) |

## Taken from M2

| | |
|---|---|
| series 1 is on main as sent | read, with B1890 in full. Main's numbers for each lock on the commit before are the seat's |
| the gap U9.b: a folder made a repository with `git init` and no commit is read as a full clone, and nine gates of the table pass there | **taken into series 3 as a patch of its own.** The line of main's lock that pins the gap (B1890's) is changed in the same commit, as M2 asks. The seat's twelve variants did not try it: git there, with nothing to say |
| series 2 needs no rebase | confirmed here: the six patches apply by `git am` on `b80c68991`, no conflict |
| the seventh re-audit taken; no further re-audit | read. The seat sends none |
| the three additions on naming | read; the owner's to rule |

## In hand: C1, series 3 of WP-0.7

| | |
|---|---|
| the base | **rebuilt on main's `b80c68991`** (series 1 landed) with series 2 applied by `git am`: no conflict. The first build was on `2f3984d27` |
| the control, read before any mend | main's own tests of the gates and checkers, 79 files, at `2f3984d27`: 541 pass and 3 fail; with series 1 and 2 on it 577 pass and the same 3 fail. Two are the locks that compare a printed float as text. The third: `tests/test_b1426_every_lane_is_watched.py` names the published branch `origin/agy-002/verify` as a lane outside the gate. None is this seat's. The control is being run again at `b80c68991` |
| patch 1, **PV21**, with seven tests | the framing gate reads every text file in its folders, in any letter case. On main it finds the one quotation main measured (B887's report) |
| patch 2, **PV20**, with six tests | each row of the claims page's two locked tables cites a lock. On main 85 of 86 do; P51 is held by name |
| patch 3, **PV24**, with six tests | a test in which no assert can fail is refused, and the arcs' own locks are read. On main the class finds 26 tests, each read by the seat and held by name. Main counted 23 by a reading the seat does not have |
| patch 4, **the gap U9.b**, with two tests | a repository that holds no commit, or a commit with no file, is read as `empty`, and every gate of the table is refused there. Three forms are locked. The line of B1890's lock is changed in the same commit, and one of your tests commits its page; each has a dated note |
| still to build | PV17 and PV16. The patches are sent together, with the cover note |

## Sent, and with main

| | where |
|---|---|
| WP-0.7, series 1: four patches | **landed on main as sent** (M2; main's B1890). One gap found by main's unseen cases, U9.b, is this seat's to close: above |
| WP-0.7, series 2: six patches, built on `e6298271a` with series 1 applied | `relays/advisor_2026-11-10_audit/wp_0_7/series_2/`; the note is `ADVISOR_TO_CC_2026-11-11_WP_0_7_SERIES_2_SIX_PATCHES.md`. Received by main (M2); its unseen cases for it are next |
| a seventh re-audit, of the finding E7 | `relays/advisor_2026-11-10_audit/REAUDIT_7_2026-11-11.md`. Taken by main (M2): E7 is fixed and accepted. The seat sends no more |

## For main

- **Before you land series 2: it turns one assertion of your new lock red.** B1890's `test_the_series_is_on_main` pins the
  table of series 1 at 6 gates that ask which files are tracked and 14 that read the past. Series 2 makes five gates read
  the past, two of which leave the first set, so the table reads 4 and 19 (the seat's note on series 2, § 4, second row).
  Run here: the six patches on `b80c68991`, that one assertion fails and the lock's four other tests pass. The lock was
  written after series 2 was sent. The line is yours.

- Both series apply in order with `git am` on `e6298271a`. Main's head has moved since; the seat applies them on the
  new head before it builds series 3 on them, and says here what it finds.
- With the two series and their views the count of landings since the last review passes forty, so `review-fires`
  turns red. It is main's count and main's review.
