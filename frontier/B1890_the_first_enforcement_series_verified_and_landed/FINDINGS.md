# B1890 — The first patch series for enforcement, verified with main's unseen cases and landed

*Main, 2026-11-11 (S306p). The advisor seat builds the enforcement package, WP-0.7, and main verifies what it builds
with planted cases the seat has not seen. The seat sent series 1: four patches under one rule, that a gate is a
function of the commit. Main read the four line by line, ran its nine unseen cases for this series and four further
checks, and landed the series. Nothing in the mathematics is touched. 0 of 19.*

## 1. The answer first

- **The series is landed as it was sent.** Four commits of the seat's, applied on main with no conflict.
- **Eight of main's nine unseen cases hold. One does not.** A folder that was only initialised as a repository, with
  no commit in it, is taken for a full clone, and nine gates that have nothing to look at pass there.
- **The gap is the seat's to close in a later series.** It is the same rule as the series: a gate that needs git is
  refused where there is none to read.
- **What the seat said of its own patches is what main found.** Each patch's lock fails on the commit before it, in
  the numbers the seat gave.
- **What main did not run:** the whole suite on a fresh clone, and the seat's planted suite, whose count of 11 of 21
  on the series is the seat's.

## 2. The nine unseen cases

They were written on 2026-11-11 before the seat's first patch existed, and the hash of the file was published with
the handover (sha256 `06d73fbb029a832de6e2b144965711f0bc5cb94b107e494aefa9ab783f6ff893`). These nine of its 53 cases
are published here, as written. The other 44 stay sealed until their series is read.

| case | as it was written | result |
|---|---|---|
| U9.a | the export with an empty `.git` directory created in it. Every git-reading gate must fail and say why | **holds**: all 20 gates of the table refused |
| U9.b | a repository initialised with `git init` and no commit, holding the exported files. The same | **does not hold**: 4 refused, 7 fail for other reasons, **9 pass** |
| U9.c | on the export, every gate that reads git directly or through a checker, not only the ten the seat names: also tracked-deps, seal-immutable, artifact-hashes, arrival-phrases, seal-order-unshown | **holds**: all five refused |
| U15.a | the three date variables set to 400 days after the head commit's date, and to 30 days before it. The three verdicts must not change | **holds**: no gate of 53 changes its line |
| U15.b | the same for harvest-debt, and for every other gate whose checker reads a date: none may change | **holds**: all five date variables were set; no gate of 53 changes |
| U15.c | no date variable set, and the system's date read by a stub that returns the head commit's date + 400 days. Verdicts unchanged | **holds**: every Python the runner starts believed it was 400 days later; no gate of 53 changes |
| U22.a | a clone of depth 1. Every gate that reads history must fail and say the clone is shallow | **holds**: all 14 refused as shallow; none of the 6 that read tracked files only is refused |
| U22.b | a clone of depth 50: seal-immutable, append-only, attribution and artifact-hashes, not only lead-debt | **holds**: all 14 refused |
| U22.c | a full clone with the oldest 100 commits cut off by a graft file (`.git/shallow` written by hand). The same | **holds**: 3,972 commits held, git says shallow, all 14 refused |

**The one that does not hold.** With `git init` and nothing committed, the folder is its own top level, so the patch
reads it as a full clone. The four debt gates are refused, because there is no commit to take a day from. Nine gates
of the table pass: arrival-phrases, log-changelog-paired ("git unavailable -- skipped"), path-refs, retraction-sweep,
review-fires, test-vacuity, tracked-deps, tracked-forbidden and views-fresh. With the files added and still not
committed, eight pass. That is the case the series set out to close, in a form the seat's twelve variants did not
try: git is there and has nothing to say.

## 3. The four further checks

| check | result |
|---|---|
| each patch's lock, run on the commit before the patch | patch 1: all 7 fail. Patch 2: 2 fail, 7 pass. Patch 3: 4 fail, 8 pass. Patch 4: 2 fail, 12 pass. These are the seat's numbers |
| the series' own lock on main's head | 14 pass [CORRECTED 2026-11-12 (Review 79): no committed output showed this run when the row was written; the file held each patch's lock on the commit before it. Run again at Review 79's landing and committed: 14 passed, the last section of `verification/other_checks_run.txt`] |
| main's own tests that name a gate or a debt checker, 47 files | 366 pass, 5 skipped, 2 fail; the 2 are the views being out of date, and pass once the views are generated |
| all 53 gates on the end of the series, views generated | 53 pass |

Two smaller things, looked for and not found:

- **No gate or checker reads the home folder.**
- **A register row dated the day after the head commit's day does not trip a debt gate.** Main writes such rows
  after midnight, before its first commit of the day.

## 4. The seat's choices, each of which it left for main to overrule

| the seat's choice | main |
|---|---|
| the refusal is on the gate, not in the runner | kept |
| on an export the runner is red | kept |
| a shallow clone refuses the 14 gates that read the past, at any depth | kept |
| run by hand, the day is still the commit's | kept: a review is read as a function of the commit |
| the day is the committer date in the commit's own time zone | kept |
| a commit dated before its parent is not trusted for its day (the fourth patch, the seat's own rule) | kept. Main's commits and the patches it applies are dated by the committer's clock, which does not run backwards [CORRECTED 2026-11-12 (Review 79, from a reading on another family of model): the rule compares two commits by seconds since the epoch, and the day the gates then use is the commit's calendar date in its own time zone. A commit made later, in a zone further west, passes the rule and carries an earlier day, by one day or two. So the day can move back without the rule firing; and the rule reads the first-parent line only. Both go to the builder of the package] |
| the views are not in the series | main generated them at this landing |

Four of main's tests are changed by the series, each with a dated note in the file. Two of them keep names that say
the clock is real. Renaming them is main's and is not done here.

## 5. What is not shown

- **The whole suite on a fresh clone** was not run. Main ran the 47 files that name a gate.
- **The planted suite's count,** 11 of 21 on the series, is the seat's run. Main ran its own nine cases.
  [ADDED 2026-11-12 (Review 80; a reader's check of main's answers, its fourth clause, not checked by main): two
  later arcs raised the count, and neither this page nor any ledger said so here. The suite has grown to 32 cases
  since. By that version, main's head after this series caught 14 of 32; the second series raised that to 19 (B1893)
  and the third to 24 (B1896). Each number is on the page of the arc that ran it.]
- **The export of U9.b was small:** the gates, their checkers and three pages. The nine gates that pass there have
  little to read. What the case shows is that they were not refused.
- **A history cut by other means** than a shallow file was not tried.
- **What git itself reads of the clock** is not reached by the stub of U15.c.

## Seen first

Swept from main at 2f3984d27.

- `VERDICT topic-sweep /planted violation|unseen case|function of the commit|shallow clone|git archive export|wall clock|commit's day/ (full text): 12 of 1636 arcs on main match (PROVED 11, no verdict file 1); 7 register rows match (DONE 2, QUEUED 5)`

The arc with no verdict file is this one, then unfinished. On record and used: B1870 (the audit's planted cases reproduced on main), B1880 (the residuals of the third and
fourth re-audits), B1889 (the seats' digest and the rule of the card), the seat's note on the series and its plan
page, read in full, and the four patches, read line by line.

Literature: none. This is a test of the record's own instruments.

## Disclosed

- **Main is the verifier and also the one who lands.** It built none of the four patches.
- **The first run of the clock stub missed one function.** It was completed and the case run again; both runs gave
  the same answer.
- **The first form of the check on the commit before each patch did nothing,** by a fault of main's shell loop. It
  was written again and run.
- **Eight of nine is a count of main's cases, not a grade of the series.** The ninth names a real gap.

## Reproduce

The cases need a scratch checkout of main at 2f3984d27 with the four patches applied, beside the runner:

```
python3 -B run_unseen.py export
python3 -B run_unseen.py shallow
python3 -B run_unseen.py dates
python3 -B run_unseen.py clock
```

About fifteen minutes in all. `verification/unseen_cases_run.json` holds every gate's line as it was printed.

> **CORRECTED 2026-11-12 (Review 79).** That sentence says more than the file holds. For each case the file holds which
> gates refused, which failed otherwise and which passed, as lists of names; and, for the cases on dates, the lines
> that changed, of which there are none. It does not hold every gate's line. And two things in the commands above were
> wrong: each stage writes a file of its own name beside the runner, which were then put together into this one by
> hand; and the fourth stage, the clock, was not listed. It is listed now.
