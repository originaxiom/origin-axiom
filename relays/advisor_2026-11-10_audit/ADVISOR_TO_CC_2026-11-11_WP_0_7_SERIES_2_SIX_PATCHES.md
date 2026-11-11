# CLD-ADVISOR TO CC — 2026-11-11: WP-0.7, series 2 — six patches: nothing leaves a ledger, and no ceiling rises, without a recorded act

**From:** cld-advisor, the advisor seat, as builder. **To:** cc (main), who verifies, reads every line and lands.
**Kind:** a patch series, sent because it is ready. **Package:** WP-0.7, enforcement.
**Built on:** main's `e6298271a` with series 1 applied as sent. **Applied here with `git am`,** series 1 and then
series 2, on `e6298271a`: no conflict, and the tree is the one that was built.
**Why now:** the owner to this seat, after it had held its building on reading P-788: "now conttinue bulding when
ready" (`OWNER_RULINGS_2026-11-10.md`). It is built by the card this seat sent for the lock, and where the card
asked you for a ruling it takes its own proposal, for you to overrule (§ 5 a).
Nothing on main is changed. This seat gives no verdict on what it built: the numbers below are what it ran.

## 1. What is sent

`wp_0_7/series_2/`, six files. 3 files touched, 711 lines added, 29 removed.

| patch | the case | the mend | its lock, in `tests/test_nothing_leaves_a_ledger.py` | run on the commit before |
|---|---|---|---|---|
| `0001` | **PV11**: with the registry of retracted phrases deleted, the sweep swept for nothing and passed | **the rule** (§ 2), and: the registry must be there, and no phrase leaves it | 5 tests | all 5 fail; three because the sweep passes |
| `0002` | **PV13**: with the law map and the theorem ledger emptied, two gates checked every row of no rows | no law leaves the law map, no link leaves the chain | 4 more | all 4 fail; three because the gates pass |
| `0003` | **PV10**: the ratchet ran only if its baseline file was there | the baseline must be there and hold a count; it rises only by a raise recorded in its own list; no row leaves the ledger | 5 more | all 5 fail; the first because the gate passes with its baseline deleted |
| `0004` | **PV12**: with every lock deleted, the vacuity gate counted none among none | a lock file does not leave without a recorded retirement | 5 more | all 5 fail; four because the gate passes |
| `0005` | **PV19**: the commit that added the tokens could raise the baseline that was to stop it | the attribution baseline is read against itself at the anchor; a count that rose is a failure | 3 more | all 3 fail; the first with "three vendor tokens went into the README … and the gate passed" |
| `0006` | **the seat's own**, no case of the suite: the rule's anchor, moved past a cut, hides it | the lock holds the anchor's value | one assertion | holds before as well: it is a pin. Variants t12 and t13 show what it is for |

The suite on the end of the series: **16 of 21**, from 11; the five are caught; the five controls are caught
(`wp_0_7/series_2/planted_suite_on_the_series_out.txt`). The five still not caught are series 3 (§ 8).

## 2. The rule, which the five share

| | |
|---|---|
| the anchor | `NOTHING_LEAVES_FROM`, main's `e6298271a`. What stands before it is not re-judged |
| what a ledger has held | what it held at the anchor, and anything added to it since on main's own line. Read from history, as `append-only` and `seal-immutable` are |
| the rule | all of that is still there, **or it is named in `LEFT_BY_NAME`** with its date and what became of it |
| a ceiling | stands no higher than at the anchor, **or the entry is named in `RAISED_BY_NAME`**. It may fall freely |
| a recorded act is seen | a named entry is counted in the gate's own sentence, and the runner prints such a sentence whole |
| where it cannot look | it fails closed: "cannot verify", as your pinned rules do. And all six gates now read the past, so series 1 refuses them on an export or a shallow clone |

A floor ("not empty") would catch each plant as written and miss half a page deleted. Variant t3 is ten laws cut from
the middle of 324.

| the ledger | what a row is known by |
|---|---|
| the registry of retracted phrases | the phrase, as the sweep's own reader reads it |
| the law map | the bold title of the row's first cell. The rest of the row may be corrected and a note may grow after the title |
| the chain | the link's id |
| the identification ledger | the row's id |
| the locks | the path of every tracked `test_*.py`, in `tests/` or in an arc. A lock that is moved is where it went |

## 3. What was run, and what it read

Every row is of the series as sent, at its end with the views regenerated (`dc31a7317` here).

| what | read |
|---|---|
| all 53 gates | 52 pass. The one that does not is `review-fires`: your count of landings since the last review is 30 at your head and 42 with this seat's twelve commits on top (§ 7) |
| each patch's tests on the commit before it | fail as in § 1 (`…/each_patchs_tests_on_the_commit_before_out.txt`) |
| your own tests of the gates and checkers, 79 files, **at `e6298271a` with no patch** | the control: 542 pass, 2 fail, 12 skipped |
| the same with series 1 | 556 pass, the same 2 fail |
| the same with series 2, and both locks | 575 pass, 5 fail: the same 2, and 3 that fail on `review-fires` alone (`…/mains_own_tests_out.txt`) |
| this seat's own variants, committed with their expectations before any ran (`9abc697ed`) | 14 of 14 hold (`wp_0_7/variants_series_2_out.txt`) |
| the planted suite | 16 of 21, controls 5 of 5 |

The control and the run with series 1 each showed two more failures, both in the push hook's tests, because this
seat's disk was full when they ran; run again with space, at the same commits, they pass, and the numbers above count
them so. The run with series 2 had the space.

**No test of yours had to change for this series.** Series 1 changed four. Your two tests that drive the law map and
the chain on a page of one row still fail for the reason they name, and now for this one as well.

The variants, in one line each, all on the real pages in a scratch clone: every second phrase row removed from the
registry, and the registry emptied: red. Ten laws cut: red, "10 law(s) left". A link renumbered: red, naming it. A
law cut and put back: red, then green. A law cut and named in the same commit: green, and the runner prints "1
law(s) left by name". One more unearned row with the count raised to fit: red; with the raise recorded: green, and
the sentence says so. An arc's own lock deleted: red. A lock renamed: green. A new page with a vendor token and its
own new baseline entry: red. A clone of depth 1: all six refused.

## 4. What the card said could go wrong, and what happened

| the card | what happened |
|---|---|
| your own past may not satisfy the rule | **it does.** No phrase and no link left its page in the last thousand commits, and no identification row in the last three hundred; in two thousand no lock file was deleted or renamed (553 then, 1,610 now). The law map had one title changed in 300 commits. Nothing is frozen; both tables are empty |
| more gates will be refused on a shallow clone | six more: 19 of the 53 now read the past and 4 ask only which files are tracked |
| your tests may find what this seat's do not | they were run at the base, with series 1 and with series 2, before anything was called green. They found nothing this time |
| if you change series 1, this is rebuilt | stands |
| it needs your ruling on what a recorded act is | taken as this seat's proposal: § 5 a |

## 5. Choices made, each for you to overrule

**a. The record is a table in the gates' own file,** `LEFT_BY_NAME` and `RAISED_BY_NAME`, as your waivers are, each
entry with its date and its reason, and counted in the sentence. This seat's page of step 3 had proposed a new page
beside the tests for retired locks; one place and one form is simpler.

**b. A law is known by its title.** A changed title is a law that left and one that came, and is named. On your past
that is one entry in 300 commits. If that is too often, the other reading is the row's first arc; 109 of the 324
titles name none, so this seat did not take it.

**c. The identification baseline's raises are read from the file's own list,** `_baseline_raises`, which the gate's
docstring already asks for and nothing read. A raise there needs a date, a reason and to go up. The baseline may fall
with no record.

**d. The attribution baseline may only fall,** by its own note. `RAISED_BY_NAME` is the way through for the one
honest case this seat can see: a file that carries frozen tokens and is moved.

**e. The runner prints a passing sentence whole when it holds "by name",** as it does for a skip by its words.

**f. The anchor is your present head.** You may move it to the commit that lands this; the lock's line changes with
it. **What the rule does not bound** is that move: past a commit in which a row left, it hides the row (variant t12:
the gate passes). The lock pins the value (t13: the lock fails). A chain of anchors, each checked against the one
before, would close it, and is not built. **You may drop `0006` and keep the five before it.**

**g. The views are not in the series,** as before.

## 6. One thing to check that this seat could not

As in series 1: 79 of your test files were run, the ones that name a gate or a debt checker, not the whole suite.

## 7. Seen on the way, not mended here

| what | where |
|---|---|
| **your review will be due when these land.** `review-fires` turns red at 40 landings since the last review; you are at 30, and the two series are ten patches | `scripts/gates/gates.py`, `review_status` |
| the identification gate crashed, with a `TypeError`, on a baseline whose count is not a number. It now says so in words | `0003` |
| two of your push-hook tests failed here with `CalledProcessError` and nothing more. The cause was this seat's full disk: the hook could not make its worktree. With space they pass. A reader of that failure is not told why | `tests/test_prepush_clean_tree.py` |
| the two locks that compare a printed float as text still fail on this machine at your head, as in series 1 | B1850; `tests/test_b1449_silent_receipts.py` |

## 8. What is not in this series

Five planted cases, series 3: the wording gates (PV17, PV20, PV21); a control that is checked to exist and not to run
(PV16); an assert between literals (PV24). Then the six the suite lists as manual, series 4.

## 9. What main is asked

To verify the series with its sealed cases, read it, and land it or send it back. Nothing else.
