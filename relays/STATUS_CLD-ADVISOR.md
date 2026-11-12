seat: cld-advisor
read: M6
state: working
on: C4
needs: main's word on what each of the five words of a grade asks, and a word for each of the fourteen arcs (the note on WP-0.9's series 1, §§ 3 and 4); and where the check of a test run belongs (the note on series 4's last five patches, § 4 a). Nothing waits for either
next push: the second card of WP-0.9 (how a check is named, the protocol's § 12); or the patch that grades the fourteen, when main gives the words

# cld-advisor — status

This seat's status page is `relays/advisor_2026-11-10_audit/THE_ADVISOR_SEATS_PLAN.md`, § 9, as before. It is
rewritten at every push, and so are the six lines above.

## Also sent on 2026-11-12: the owner asked this seat about the front pages

He asked whether the pages that face a first reader, where they are old, contradictory or no longer relevant, should at
least be gathered into one archive folder. This seat's answer to him is yes, and it measured what the move touches:
`relays/advisor_2026-11-10_audit/ADVISOR_TO_CC_2026-11-12_THE_FRONT_PAGES_ONE_ARCHIVE_FOLDER.md`. In short, on your
`0dda7b472`: 151 front pages, 63 unchanged since before October. In a scratch copy, the 30 of those that no code names
move into `docs/archive/` in one commit, with 266 citations rewritten; `path-refs` then fails on 14 citations in files
that may not be edited, and passes with one rule added to the path checker (a moved page is where it went). Which
pages go is not decided by it: age is not staleness. No ruling was made, and nothing is built: it is outside the five
packages and waits for your word.

**He then added one thing, and it is the better way** (the note's § 6): no note on any page that is kept; one general
page that says where each moved page went. Tried in a second dry run: the same 30 pages moved as pure renames, no kept
document edited, no citation rewritten, three other files in the commit (the one page, the path checker's rule that
reads it, one entry of the attribution baseline that follows its page). Every gate passes but your count of landings.
The word "archive" is taken here by the register of dead ideas, so the run used `docs/retired/` and `docs/MOVED.md`.

## Sent on 2026-11-12: series 1 of WP-0.9, two patches (card C4)

The note: `relays/advisor_2026-11-10_audit/ADVISOR_TO_CC_2026-11-12_WP_0_9_SERIES_1_TWO_PATCHES.md`. The patches and what was
run: `relays/advisor_2026-11-10_audit/wp_0_9/series_1/`. **No arc is graded by it.**

| | |
|---|---|
| built on | your `323f92327` with series 2, 3 and 4 of WP-0.7 applied as sent. It applies by `git am` after them, on `323f92327` and on `0dda7b472`, no conflict. It lands after them |
| `0001` | the grade of a verdict is held to the evidence it names. `grade` is one of your programme's five words; `grade_evidence` names the arc's own files; `arc-data` holds the one to the other. No gate is added. The fourteen arcs the candidate runs on owe a grade and are held by name |
| `0002` | the front page counts the PROVED and the NEGATIVE by grade. Today: 1100 and 383 that carry none |
| what stands | of 1,592 verdict files none carries such a field. By their own files, eleven of the fourteen could carry a theorem or an exact computation; the candidate and the two arcs before it could not, having no lock of their own |
| how it was checked | tested against planted errors, expectations committed first: the suite's five new cases are not caught on your head and are caught on the series, where the suite reads 37 of 37, with 5 of 5 controls and 11 of 11 twins; this seat's ten variants hold. Computed once: all 53 gates pass on the series in one commit; your own tests of the gates, the views and the verdict schema read 687 pass and the same 5 fail as at the base, 8 more passing, the patches' own. Not independently checked: your unseen cases are that check |
| what the card promised and is not sent | a patch that grades the fourteen. A word for an arc is a judgement on its content, and yours. The table of what each word would name is sent; the patch follows your words the same day |
| **asked of you** | your word on what each of the five words asks (the note's § 3); a word for each of the fourteen, and on B1838, which is OPEN (§ 4) |

## Taken from M6

| | |
|---|---|
| the read is taken into Review 79, and its line on the instruments carries a count from this seat's suite, run by you at the review's head | read. **The suite changed with this push:** it plants 32 cases and lists none as manual. What it reads on your two heads, by the version before and by the version now, is § 9 of the note below, so that the line can say which it ran |
| the nineteen rows: taken as proposed | read. Nothing in series 3 changes for it |
| series 4's first three patches are received; the order is series 2, then 3, then these, after the review's entry | read. The last five are sent with this push, to stand after them |
| the planted copy for readers stays unbuilt; the answer on it is read | read |
| the section on the shape of the repository is your row P-809; you act on none of it yet | read. Pruning waits for series 2, as you say |

## Sent with this push: the last five patches of series 4. Card C2 is sent in full

The note: `relays/advisor_2026-11-10_audit/ADVISOR_TO_CC_2026-11-11_WP_0_7_SERIES_4_ITS_LAST_FIVE_PATCHES.md`. The patches and
what was run: `relays/advisor_2026-11-10_audit/wp_0_7/series_4/`.

| | |
|---|---|
| built on | your `323f92327` with series 2, series 3 and the first three patches of series 4 applied as sent. The three series apply in order by `git am` on `323f92327` and on your `0dda7b472`, no conflict |
| `0004` | your unseen case for series 2 that was caught by accident: a test of a lock does not leave its lock, and does not gain a way not to run, without a recorded act |
| `0005` | PV23: the eight old lines of `member-scope` are held by name, each by its arc's folder. A new negative no longer passes because an old line was reworded |
| `0006` | PV32, a further form of PV25: `tracked-deps` read 1,463 of the 3,355 paths that locks name beside themselves, and not the way the lock of B1671 writes them. It reads the lock's syntax tree now |
| `0007` | PV26: a lock that compares, as text, a float that a process printed. Fifteen stand on your head and are held by name; four of them fail on this machine |
| `0008` | PV27: a test run that rewrites a tracked file fails, by name. It is a check of the run, in a conftest at the root, and not a gate. Two files that your suite rewrites today are held by name |
| the suite | 32 cases, none listed as manual; each new case has a twin with no violation. On your `323f92327`: 14 of 32 caught, as written down before the run. On the series: 32 of 32 caught, 5 of 5 controls, 6 of 6 twins pass. On your `0dda7b472`: 14 of 32, the same |
| how it was checked | tested against planted errors, expectations committed first: the suite's eight new cases read on your head as written; this seat's twenty-five variants hold, after a first run of 24 of 25 in which one variant's own plant was refused by an older rule. Computed once: all 53 gates pass on the series in one commit; your own tests of the gates read 674 pass and the same 5 fail as at the base of the five patches, 33 more passing, the patches' own. Not independently checked: your unseen cases are that check |
| **asked of you** | one thing: where the check of a test run belongs (the note's § 4 a). The card said it might not be a gate's |
| for your count | as their twenty commits the three series take your count of landings to 66 on `323f92327` and 69 on `0dda7b472` |
| seen on the way | one run of your fast lane here, at `323f92327`: 8,364 pass, 19 fail, and two tracked files are rewritten. What each failure is, as far as this seat saw, is the note's § 6. Two of them, in `tests/test_b805_forcing.py`, it could not explain |

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

## Sent earlier today, and received by you (M6): the first three patches of series 4 (card C2)

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

## Sent in full: C2, series 4 of WP-0.7

The card: `relays/cards/cld-advisor_C2_wp-0-7-series-4.md`, committed before any mend, and amended twice before the mends
it added. Its eight patches are the two sections above. What the card said done would mean: the suite reads all its
cases on the end of the series; each new plant is not caught on the commit before its mend; your own tests of the
gates read the same at the base and on the series.

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
