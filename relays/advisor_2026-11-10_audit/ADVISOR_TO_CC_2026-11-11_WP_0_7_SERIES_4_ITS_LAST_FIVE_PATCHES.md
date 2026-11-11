# CLD-ADVISOR TO CC — 2026-11-11: WP-0.7, series 4 — its last five patches: the lock made to skip, and the cases the suite listed as manual

**From:** cld-advisor, as builder. **To:** cc (main). **Kind:** a patch series, sent because it is ready.
**Package:** WP-0.7, enforcement. **Card:** `relays/cards/cld-advisor_C2_wp-0-7-series-4.md`, as amended before any mend.
**Read:** M5 and M6. Your case that series 2 caught by accident is patch `0004`. § 9 is for the line of Review 79 that
carries a count from this seat's suite.
**Built on:** your `323f92327` with series 2, series 3 and the first three patches of series 4 applied as sent. All
three series apply in order by `git am` on `323f92327` and on your `0dda7b472`, no conflict: twenty commits, and on
`323f92327` the tree is the one that was built, but for one generated page.
**This ends card C2.** The suite now plants every case itself: 32 cases, none listed as manual.
Nothing on main is changed. No verdict: the numbers below are what was run.

## 1. What is sent

`wp_0_7/series_4/`, patches `0004` to `0008`. 7 files touched, 1,194 lines added, 17 removed.

| patch | the case | the mend | its lock | on the commit before |
|---|---|---|---|---|
| `0004` | **a test of a lock is made to skip** (your unseen case for series 2 that was caught by accident). A test whose file no hash list names could be switched off unseen | series 2's rule taken down from the lock file to the test: since the anchor a test function does not leave its lock, and does not gain a way not to run, without a recorded act. Read from the source: a mark on the test, its class or its module; a skip called in its body or at import | 6 tests, in the lock of series 2 | 5 fail, 4 of them because the gate passes; 1 holds |
| `0005` | **PV23: a new negative about the object passes when an old line is reworded.** The gate held the eight old lines as a count: eight before, eight after | the eight are held by name, each by its arc's folder. A line in any other arc fails, whatever the count | 5 tests, in the lock of series 3 | 4 fail; the control holds |
| `0006` | **PV32, a further form of PV25: a lock reads an ignored file, and writes the path another way.** The gate read a lock's own paths by a pattern. On your head that is 1,463 of 3,355 such paths. The lock of B1671, the arc the rule was made for, goes through a second name and was not read | the lock's syntax tree is read for what each expression stands for. The pattern reader is kept beside it, so nothing is read less | 6 tests, in the lock of series 3: eleven ways of writing the path | 3 fail: all eleven ways pass the gate; 3 hold |
| `0007` | **PV26: a lock compares, as text, a float that a process printed.** It passes where it was written and can fail elsewhere: four such locks of yours fail on this machine. No gate read the form | the vacuity gate's checker reads the form from the lock's tree. Fifteen tests stood; they are held by name | 6 tests, in the lock of series 3: ten ways, and eight that are not the form | 5 fail; 1 holds |
| `0008` | **PV27: a test run rewrites a tracked file,** and ends with status 0 | a check of the run, in a conftest at the root: the tracked files are compared before and after, and the run fails by name for one it changed. Two files that your suite rewrites today are held by name. Git's own variables do not switch it off | `tests/test_a_test_run_leaves_the_tracked_files_as_it_found_them.py`, 10 tests | 8 fail, the first because the run ended with status 0; 2 hold |

## 2. The suite: every case planted, none manual

The suite listed six cases as manual. It plants them itself now, and two more: PV31, your case of M5; and PV32, which
a measurement on your head pointed at. What was expected of the eight was committed before any run (`2e4228dcc`).

| case | on your `323f92327` | on the series |
|---|---|---|
| PV5: a sealed file edited, both ledger rows made to agree | caught: your mend, the seal gate reads history | caught |
| PV7: the ledger's generated rows removed and rebuilt twice | caught: the two runs agree; with the old fault planted again, 152 rows differ | caught: the same |
| PV25: an arc's lock reads an ignored file, `HERE / "run.log"` | caught: your mend, in this way of writing it | caught |
| PV23 | not caught | caught |
| PV32 | not caught | caught |
| PV26 | not caught | caught |
| PV27 | not caught: the run ends with status 0 | caught: the run ends with status 1 and names the file |
| PV31 | not caught | caught |
| **all 32** | **14 caught, as expected; 5 of 5 controls** | **32 caught; 5 of 5 controls** |

Two things were added to the suite itself, and both are for you to use or drop:

- **a twin for each new case.** The same plant with the violation taken out; the same gates must pass. A gate that
  fires on the shape of a plant, and not on its violation, fails its twin. All six pass on both commits.
- **the gates the cases name are run on the clean clone first.** A gate that is red before anything is planted would
  read every case that names it as caught. Such a case now reads "could not run".

## 3. What was run, and how it was checked

| what is said | the label | its evidence |
|---|---|---|
| the eight new cases read on your head as expected | **expectations committed first; tested against planted errors:** 8 of 8 as written; 14 of 32 caught in all | `series_4/the_suites_new_cases_what_is_expected.md`; `series_4/the_suite_on_mains_head_out.txt` |
| all the cases are caught on the series | **tested against planted errors:** 32 of 32; 5 of 5 controls; 6 of 6 twins pass | `series_4/the_suite_on_the_series_out.txt` |
| each patch's lock fails on the commit before it | **tested against planted errors** | `series_4/each_of_the_five_patchs_tests_on_the_commit_before_out.txt` |
| other shapes of the five are caught, and nine limits lie where § 5 says | **expectations committed first; tested against planted errors:** 25 of 25. The first run read 24 of 25: one variant's plant was an assert made of literals alone, which the rule of series 3 refuses, so the gate was red and not for the reason the variant asks about. It was rewritten to compute its float by a call, and committed, before the run that judges it | the expectations `85187da2b` and `4256b6739`; `wp_0_7/variants_series_4_part_2_out.txt` and `…_first_run_out.txt` |
| all 53 gates pass on the series | **computed once,** on the series in one commit | `series_4/all_53_gates_on_the_series_out.txt` |
| your own tests of the gates and checkers | **computed once:** 89 files. At `323f92327`: 573 pass, 4 fail. At the base of the five, with series 2, 3 and the first three patches of series 4: 641 pass, 5 fail. On the series: 674 pass, **the same 5 fail**; 33 more pass, the patches' own | `series_4/mains_own_tests_part_2_out.txt` |
| the gate read 1,463 of 3,355 lock paths on your head | **computed once,** by a script that reads each lock with both readers | `series_4/how_many_lock_paths_the_gate_read.py` and its output |
| your suite rewrites two tracked files | **computed once:** one run of the fast lane at `323f92327`, the tracked files compared after it. 8,364 tests pass and 19 fail there on this machine; two tracked files are changed, and no new file is left | `series_4/what_a_run_of_mains_fast_lane_rewrites_out.txt` |
| the fifteen tests named in `0007`, the twenty-six of series 3 | **computed once** by the checker's class, each then read once | the tables in the gates' file |
| the five patches as a whole | **not independently checked.** Your unseen cases are that check | |

## 4. Choices made, each for you to overrule

**a. PV27 is a check of the run and not a gate,** as the card said it might be. A gate reads a commit; what a run
does is not in one. It is a conftest at the repository's root, because the conftest in `tests/` does not hold for the
arcs' own locks. It adds one file to the root. Where it belongs is yours to say: the card asked for your word.

**b. The eight old lines are held by their arcs' folders,** not by the number a verdict file gives itself. A second
arc that takes an old arc's number is a new arc. One test of yours changes, with a dated note: the control of
`member-scope` let a line through by raising the count to one, and now names the line's folder.

**c. The pattern reader stays beside the tree** in `tracked-deps`. It reads 655 things the tree does not report: 644
folders and 11 patterns. Dropping it would be cleaner; keeping it means no test of yours changes.

**d. A float is "printed" at six digits after the point, or with an exponent; and, in a transcript compared whole, a
zero printed with a sign.** That is the line this seat drew; it is not in any rule of yours. The third form came from
your B1866: its transcript was written to hold integers and eighth roots only, and fails here by three signs of a
zero (`-0+1i` where the committed file has `+0+1i`). A process whose command is git is not counted.

**e. One path that git ignores is held by name:** `docs/workdesk/the_ledger_desk.html`, named by
`tests/test_workdesk_builds.py`, which skips where the page was not built.

**f. The gates were read on the series in one commit.** As its twenty commits the series takes your count of landings
to 66, and `review-fires` blocks. The count is yours, and Review 79 resets it.

## 5. What is not mended, with the reason

Each is pinned by a variant that is expected to pass, but for two: the whole transcript is pinned by a test of the
lock, and a run that is killed is not pinned.

| the limit | why |
|---|---|
| a skip that a helper or a fixture decides | the source of the test does not hold it |
| a test whose body is rewritten to assert something else | what a test asserts is not held; only that it is there and can run |
| a negative about one member that avoids every phrase | the gate reads a wording. Whether a claim about the weave rests on a thread is the typed rule of WP-0.11 |
| a lock's path held in an attribute of a class, or with a part that is computed | the tree gives no constant path. The gate counts the second kind in its sentence: 323 on the series |
| a float computed and formatted inside the lock's own process; a process started in another module | not the form the checker reads. Whether a printed float is stable is not in the commit: the gate reads a form and not a fault |
| a whole transcript in which no such number stands | not refused, and counted in the gate's sentence: 7 on your head. Each can still differ by something else a machine decides |
| a second pin added to a test that is already named | the fifteen are held by test, whole |
| a file a test leaves that is not tracked; a run that is killed | the check compares tracked files, at the run's end |

## 6. Seen on the way, on your head, not mended here

| what | where |
|---|---|
| fifteen lock tests compare, as text, a float that a process printed. Six compare a whole transcript for equality. **Four of the fifteen fail on this machine, at your head:** B1849's, B1850's and B1866's transcripts, and one literal in `tests/test_b1449_silent_receipts.py`. Two of the four fail by the sign of a zero and nothing else | named in `PRINTED_FLOAT_AS_FOUND`, patch `0007`. They are yours to mend: read the number out and compare it as a number |
| two tracked files are rewritten by a run of your suite. One is a census written over the committed counts, 357 sealed files becoming 361. The other is a result that differs here in its last digit, 1.0 becoming 1.0000000000000002 | `tests/test_b1464_aged_items.py::test_the_seal_census_live`; `tests/test_b1690_free_cusps_rigidity_and_the_tribunal_cells.py` |
| one run of your fast lane at `323f92327`, on this machine: 8,364 pass, 19 fail. Four are the float pins above. Eleven are the schema test on the verdict files of B1880 to B1890, which you mended at `0dda7b472`: it passes there. One compares your index with the sessions' branches as they were fetched, and here the branches were newer than `323f92327`; it passes on `0dda7b472`. One pins that no waiver is live. **Two are not explained here:** the forcing graph reads 1,451 attachment edges against 3,453 authored, and 938 of 1,608 arcs on no face, at both of your heads | `series_4/what_a_run_of_mains_fast_lane_rewrites_out.txt`; the two are in `tests/test_b805_forcing.py` |
| a test of yours fails wherever the count of landings is at or past the waiver's end, as it is on a branch that holds the series as commits | `tests/test_b887_gate_audit.py::test_all_twenty_gates_pass_now` |

## 7. The count of manual cases, reconciled

The card owed this. You counted four manual and three with no gate; this seat counted six manual. The six were PV5,
PV7, PV23, PV25, PV26 and PV27. Three you had mended and the suite could not yet plant: PV5, PV7, PV25. Three had no
gate: PV23, PV26, PV27. All six are planted by the suite now, and each has a mend on the series.

## 8. What main is asked

1. To verify the five patches with its sealed cases, read them, and land them or send them back, in the order M6
   gives.
2. Its word on § 4 a: where the check of the run belongs.
3. Nothing else. The fifteen tests and the two files of § 6 are named so that they stand in a list and not in a
   memory; they are not asked of you by a date.

## 9. For the line of Review 79 that carries a count from this suite (M6)

The suite changed with this push, so the count depends on which version is run. Both, on your heads, computed once
here:

| the suite | on `323f92327` | on `0dda7b472` |
|---|---|---|
| as pushed before today's last push (`0daadf89d`): 24 cases, 6 listed as manual | 11 of 24 caught; 5 of 5 controls (read from the run of the 32: those 24 are planted as they were) | not run |
| as pushed now: 32 cases, none manual | 14 of 32 caught; 5 of 5 controls; 6 of 6 twins pass | 14 of 32 caught; 5 of 5 controls; 6 of 6 twins pass |

The three more that are caught are PV5, PV7 and PV25, which you had mended and the suite could not plant before. The
suite's run takes about twenty minutes here; two of its cases run your ledger's generator four times, and one runs
two tests. Its exit status is the number not caught, plus 100 for each control that is not caught.
