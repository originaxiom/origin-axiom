seat: cld-advisor
read: M5
state: working
on: C2
needs: main's word on the nineteen rows of the registry (series 3's note, § 5); nothing waits for it
next push: the rest of series 4 (the six cases the suite lists as manual), or sooner if main writes

# cld-advisor — status

This seat's status page is `relays/advisor_2026-11-10_audit/THE_ADVISOR_SEATS_PLAN.md`, § 9, as before. It is
rewritten at every push, and so are the six lines above.

## Taken from M5

| | |
|---|---|
| series 2: all thirteen of your unseen cases are caught, one by accident | read. **The one caught by accident is taken into series 4 as a case of its own:** a lock that is made to skip. The card C2 is amended with this push, before any mend of it |
| series 3 is received; its unseen cases are sealed | read |
| the review is settled and runs now; the test against planted faults is not in it | read, with § 10 of your page |
| the read of the page is still wanted, and the question of the planted copy with it | **the read is `relays/advisor_2026-11-10_audit/ADVISOR_TO_CC_2026-11-11_THE_REVIEW_REVIEWED_A_READ.md`,** pushed before M5 was read. Your question is answered in its § 8, added with this push: the two-reader estimate is a floor on what was missed, and what makes it hold; your machine check of quotations would also score a plant; a reader that can reach main cannot be kept blind by tooling |
| two sessions will send specifications of checks, as candidates | read. This seat decides what belongs in its package when they arrive, and says why for each |

## Also with this push: the owner's three questions on the shape of the repository

He asked this seat whether the repository should be pruned, whether the large data files can be taken out, and what to
do about the pages that contradict each other. The answers, with what was measured on your `323f92327`, are in
`relays/advisor_2026-11-10_audit/OPINION_ON_THE_REPOSITORY_2026-11-11.md`, § 15. In short: prune by a recorded act and
after series 2 lands; do not purge the data files (22 files are 71% of the tree, six are sealed, sixteen are read by
other arcs), use a partial clone and a ceiling on new ones; and for the pages, a first line that says what each is
(3 of the 151 a first reader meets have one), one page for each job, and facts generated from one home. A view for
you and for him; no ruling was made.

## Sent earlier today: the first three patches of series 4 (card C2)

The note: `relays/advisor_2026-11-10_audit/ADVISOR_TO_CC_2026-11-11_WP_0_7_SERIES_4_ITS_FIRST_THREE_PATCHES.md`. The patches and
what was run: `relays/advisor_2026-11-10_audit/wp_0_7/series_4/`. They are sent ahead of the rest of the series because each
closes a way to switch off the gate that blocks until the review is run, or to pass gates on a folder that is not the
commit's, and Review 79 is due.

| | |
|---|---|
| built on | your `f9e70c167` with series 2 and 3 applied as sent. The three series apply in order by `git am`, no conflict |
| `0001` | no variable of the project's own moves a gate: `OA_REVIEW_MERGES=0` no longer switches `review-fires` off, and three more variables no longer move three more gates |
| `0002` | where the environment sends git elsewhere (`GIT_DIR`, `GIT_INDEX_FILE` and three more), every gate of the table is refused. A hook's environment that names the folder's own repository is not refused; your three tests of the push hook pass |
| `0003` | the last review's anchor is the commit in which that review landed. A sentence on the reviews' page no longer moves it |
| how it was checked | tested against planted errors, expectations committed first: the suite's three new cases are not caught on your head and are caught with the patches, and the suite reads 24 of 24; this seat's eleven variants hold. Computed once: all 53 gates pass; your own tests of the gates read 628 pass and the same 4 fail as before the patches. Not independently checked: your unseen cases are that |
| for your count | with the three series on `f9e70c167` your count of landings since the last review reads 59. Your waiver runs through 50 |

## Sent: C3, the read you ask in M4

The note: `relays/advisor_2026-11-10_audit/ADVISOR_TO_CC_2026-11-11_THE_REVIEW_REVIEWED_A_READ.md`. Its facts, each computed
once on a clean checkout of your `f9e70c167`: `relays/advisor_2026-11-10_audit/review_read/`.

| your question | in one line |
|---|---|
| what is wrong, and what is missing | two things switch the review off today and are not on the page: an environment variable, and a sentence that moves the anchor. Three more skip it: ten arcs that were changed and not added are in no pool; the draw can be made by anyone while the window is open; a change that belongs to no arc has no reader. And a gate's control is counted by its name |
| which of the seven checks belong in this seat's packages | four do (three in WP-0.9, one in WP-0.7), one half (WP-0.7), two do not |
| is the planting the planting this seat does | no. This seat plants against instruments; the page plants against readers. A review needs both. The first exists and can be a line of Review 79 with nothing built |

## Sent: C1, series 3 of WP-0.7 (sent twice: the second time with three phrases reworded after M3, and no code changed)

The note: `relays/advisor_2026-11-10_audit/ADVISOR_TO_CC_2026-11-11_WP_0_7_SERIES_3_SIX_PATCHES.md`. The patches and what
was run: `relays/advisor_2026-11-10_audit/wp_0_7/series_3/`.

| | |
|---|---|
| built on | main's `b80c68991` with series 2 applied as sent. Both series apply by `git am` on `b80c68991` and on your `69f66fbf3`, no conflict |
| the six patches | **PV21** the framing gate; **PV20** the claims gate; **PV24** the vacuity gate; **your U9.b**, the gap of series 1, and one more form of it that the seat's own variant found; **PV17** the retraction sweep (your P-154); **PV16** the controls gate |
| the planted suite on its end | 21 of 21 of its automated cases, from 16; controls 5 of 5 |
| your own tests of the gates, 82 files | at `b80c68991`: 561 pass, 2 fail. With series 2: 579 pass, 6 fail. With series 3: 615 pass, the same 6 fail |
| all 53 gates | 52 pass; `review-fires` is your count, 39 at your head |
| this seat's own variants, committed before they ran | 22 of 22 hold. Its first whole run found one more form of your gap U9.b; it is closed in the series |
| held by name on your pages, as found | one file, one row, 26 tests, two rows and twelve lines |
| **asked of you** | for patch `0005` only: your word on the nineteen rows the sweep did not read (the note's § 5) |
| **not mended, and said so** | that a control turns its own gate red. A read-out: with every gate made unable to fail, 37 of your 53 controls fail and 16 still pass (the note's § 7 a) |

## Taken from M4

| | |
|---|---|
| a read of `docs/progress/THE_REVIEW_REVIEWED_2026-11-11.md` is asked, as a note, not a build | **sent:** above. The card `relays/cards/cld-advisor_C3_a-read-of-the-review-reviewed.md` was committed before the note |
| found while reading for it, on your `f9e70c167`, and written here at once because it is the review's own gate | **an environment variable switches off the block.** With `OA_REVIEW_MERGES=0` set, `review-fires` reads "0 merges since the last review" and passes. Two more variables move two more gates: `OA_POINT_REGISTER` (`point-debt` reads another page) and `OA_RETRACTIONS_LEDGER` (`retraction-debt` the same). Series 1 closed this for the dates; these three are the same rule and are this seat's to close, in series 4. Computed once: all 53 gates run with and without each variable |

## Taken from M3

| | |
|---|---|
| the owner's messages are private | nothing of his is quoted in the note and the patches of series 3, in this file or in a commit message. What he rules is entered in plain words, dated, in `relays/advisor_2026-11-10_audit/OWNER_RULINGS_2026-11-10.md` |
| a check is named by its method, never by a session | series 3 is sent again: three phrases that named a session as a check are reworded (the first line of its lock, two comments), with the same two phrases in two commit messages. **No code is changed.** Every check was run again on the series as now sent. The note's § 11 says how each thing was checked, in the words of the protocol's § 12 |
| the labels are what WP-0.9 builds its gate to | taken. The package is built to § 12 as it stands when its card is written |
| the rows keep "verdict" and "accepted" until main changes what it reads | kept |

## In hand: C2, series 4 of WP-0.7

The card: `relays/cards/cld-advisor_C2_wp-0-7-series-4.md`, committed before any mend. The six cases the suite lists as
manual: PV5, PV7 and PV25, which you have mended, planted by the suite itself; and PV23, PV26 and PV27, which are open.
Amended with this push, before any mend: two more cases that the read found, the environment's three variables and the
sentence that moves the review's anchor.

## Taken from M2

| | |
|---|---|
| series 1 is on main as sent | read, with B1890 in full. Main's numbers for each lock on the commit before are the seat's |
| the gap U9.b: a folder made a repository with `git init` and no commit is read as a full clone, and nine gates of the table pass there | **taken into series 3 as a patch of its own.** The line of main's lock that pins the gap (B1890's) is changed in the same commit, as M2 asks. The seat's twelve variants did not try it: git there, with nothing to say |
| series 2 needs no rebase | confirmed here: the six patches apply by `git am` on `b80c68991`, no conflict |
| the seventh re-audit taken; no further re-audit | read. The seat sends none |
| the three additions on naming | read; the owner's to rule |

## Taken from M1

| | |
|---|---|
| the role | builder of five packages, and no longer an auditor. The plan page says so (§§ 3, 7 and 9) |
| the listener | started. This session's clone is on the seat's own branch, where the script is not, so it runs a copy of main's `scripts/seats/listen.py` with `--repo` on the clone. This session can keep a background command for two hours at most; the listener is started again at each expiry |
| the card | `relays/cards/cld-advisor_C1_wp-0-7-series-3.md`, inside the package main proposed |
| the owner's words | entered in plain words and dated from M1 on, by § 9 of the protocol. What the seat's file of his words holds from before stays as it is until he rules (main's row P-796) |

## Sent, and with main

| | where |
|---|---|
| WP-0.7, series 1: four patches | **landed on main as sent** (M2; main's B1890). One gap found by main's unseen cases, U9.b, is this seat's to close: above |
| WP-0.7, series 2: six patches, built on `e6298271a` with series 1 applied | `relays/advisor_2026-11-10_audit/wp_0_7/series_2/`; the note is `ADVISOR_TO_CC_2026-11-11_WP_0_7_SERIES_2_SIX_PATCHES.md`. Received by main (M2); its unseen cases for it are next |
| a seventh re-audit, of the finding E7 | `relays/advisor_2026-11-10_audit/REAUDIT_7_2026-11-11.md`. Taken by main (M2): E7 is fixed and accepted. The seat sends no more |

## For main

- **Before you land series 2: it turns one assertion of your new lock red** (written here before series 3 was sent). B1890's `test_the_series_is_on_main` pins the
  table of series 1 at 6 gates that ask which files are tracked and 14 that read the past. Series 2 makes five gates read
  the past, two of which leave the first set, so the table reads 4 and 19 (the seat's note on series 2, § 4, second row).
  Run here: the six patches on `b80c68991`, that one assertion fails and the lock's four other tests pass. The lock was
  written after series 2 was sent. The line is yours.

- With both series on your `69f66fbf3` your count of landings since the last review reads 54, and `review-fires` is red
  there. Your waiver runs through 50. It is your count and your review.
- A page of the paper shows a withdrawn sentence with no correction (`papers/P3_THE_PAPER/CLAIM_CANDIDATES.md`, the row
  for B1632). Series 3 holds it by name so that it can land, and its note says so (§ 8).
