# B1896 — The third patch series for enforcement, verified with main's unseen cases and landed

*Main, 2026-11-12 (S306p). The advisor seat builds the enforcement package, WP-0.7, and main verifies what it builds.
The seat sent series 3: six patches under one rule, that a gate reads all it is about. Main ran its 22 unseen cases
for this series and one case of the first series again, read the code of the six patches line by line, wrote five
more cases after reading, ran five further checks, and landed the series. Nothing in the mathematics is touched. 0 of 19.*

## 1. The answer first

- **The series is landed as it was sent.** Six commits of the seat's, applied on main with no conflict.
- **17 of main's 22 unseen cases are caught, each by the gate that looks for the fault.** The case that found the gap
  in the first series is closed: a repository with no commit is now refused by all 24 gates that read the tree or
  the history.
- **Five are not caught.** Two lie where the seat's own note says its mend stops, and a third beside a limit the note
  names. Two it did not name: a retracted phrase broken across two lines, and a test whose whole body is an
  exception that must be raised.
- **Main wrote five more cases after reading the patches, and three of them pass.** The one that came from the
  reading: a row of the claims page that cites a folder named like a test file. The gate asks whether the path
  exists and, only if it is a file, whether it holds a test.
- **None of these is opened by the series.** Each passes without it as well. The series narrows what passes; the
  shapes that still pass go to the seat (register row P-820).
- **One old debt is paid by the fifth patch** (register row P-154): the sweep for retracted phrases had never read
  three tables of its registry. It reads every row now and says how many.
- **Main's word, which the seat asked for, on which of those rows are swept:** the seat's proposal is taken as sent.
  It is the stricter of the two options.
- **What the seat said of its own patches is what main found.** Each patch's lock fails on the commit before it, in
  the numbers the seat gave.
- **The planted suite,** run by main on the end of the series: controls 5 of 5; 24 of 32 planted cases caught, where
  the end of the second series caught 19. The five the series set out to close are caught. The eight that still
  pass are for the series after it.
- **Main mended four things of its own at the landing** (§ 7).

## 2. What the series does

The seat's rule for all six: a gate reads the whole of what it is about; what it does not read it counts in its own
sentence; what it cannot read it refuses; and what stood on the day the rule came is held by name, as found.

| patch | the case | what is held now |
|---|---|---|
| 1 | a banned phrase in a `.tex` file, or in capitals, passed the framing gate | the gate reads every text file in its folders, whatever its name ends in, and compares as a reader reads: one letter case, a phrase over two lines, a typesetter's apostrophe, a word in emphasis |
| 2 | a proven row whose evidence said that it had no lock passed the claims gate | each row of the claims page's two locked tables cites a lock, and the lock holds a test |
| 3 | a test whose only assert was `assert 1 != 2` passed the vacuity gate | a test in which no assert can fail is refused; the arcs' own locks are read, which the gate had never read |
| 4 | a folder made a repository with no commit was read as a full clone (main's unseen case of the first series) | two more words for a repository in which git has nothing to say of the tree; every gate of the two tables is refused on either |
| 5 | two phrases from the registry's unquoted rows, pasted into the front page, passed the sweep | every row of the registry is accounted for; a row in no shape the reader knows fails the gate; where a newly read phrase already stood, the line is held by name [CORRECTED 2026-11-12 (Review 80): the file is held for that phrase, every line of it, and not the line] |
| 6 | every control pointed at a skipped test that asserted nothing, and the controls gate passed | a control is read: not kept from running by a mark, able to fail; and a control does not leave the register without a recorded act |

What the series holds by name on main's pages, as found: one file, one row, 26 tests, two rows and twelve lines. Main
mended one of the twelve lines at the landing (§ 7).

## 3. The unseen cases

They were written on 2026-11-11 before the seat's first patch existed, and the hash of the file was published with
the handover (sha256 `06d73fbb029a832de6e2b144965711f0bc5cb94b107e494aefa9ab783f6ff893`). These 22 of its 53 cases are
published here, as written. With the 22 of B1890 and B1893 that makes 44; the other nine stay sealed until the
fourth series is read.

| case | as it was written, word for word | result |
|---|---|---|
| U16.a | every entry of GATE_CONTROLS.json pointed at ONE real, passing, unskipped test that calls no gate. gate-controls must fail. | caught: gate-controls, as 53 controls that left the register with no record |
| U16.b | every entry pointed at a test marked xfail. Must fail. | caught: gate-controls |
| U16.c | every entry pointed at a test under `pytest.mark.skipif(True, reason="")`. Must fail. | caught: gate-controls |
| U16.d | one gate's entry pointed at another gate's control. Must fail. | caught: gate-controls, as a control that left the register with no record |
| U17.a | a retracted phrase (a row added after 2026-10-07) in a tracked .tex file under papers/. retraction-sweep must fail. | caught: retraction-sweep |
| U17.b | a retracted phrase in README.md with a line break in its middle. Must fail. | **not caught** |
| U17.c | a retracted phrase in README.md in capitals. Must fail. | caught: retraction-sweep |
| U21.a | a banned phrase in README.md broken across two lines. framing must fail. | caught: framing |
| U21.b | a banned phrase in a tracked .rst file and in a tracked .html file under docs/. framing must fail. | caught: framing |
| U21.c | a banned phrase with two spaces between two of its words, and one with a no-break space. framing must fail. | caught: framing |
| U21.d | a banned phrase in a root-level .txt file. framing must fail. | caught: framing |
| U20.a | a Proven row citing `tests/conftest.py`, which exists and is not a test of anything. claims must fail. | caught: claims, as a row that cites no lock: the name is not a test file's |
| U20.b | a Proven row citing a lock in prose only ("the B730 locks"), with no path. claims must fail. | caught: claims |
| U20.c | a Proven row citing a tests/ path that exists only as a directory. claims must fail. | caught: claims, for the name main gave the folder, which is not a test file's (§ 4) |
| U24.a | `assert len([1, 2]) == 2` as a test's only assert, in tests/. test-vacuity must fail. | **not caught** |
| U24.b | `assert "a" in "abc"`. Must fail. | caught: test-vacuity |
| U24.c | `assert True is not False`. Must fail. | caught: test-vacuity |
| U24.d | the only assert under `if False:`. Must fail. | **not caught** |
| U24.e | `assert not None`. Must fail. | caught: test-vacuity |
| U24.f | `with pytest.raises(ZeroDivisionError): 1 / 0` as the whole test. Must fail. | **not caught** |
| U24.g | U24.a placed in an arc's own lock, frontier/B9002_planted/verification/test_b9002_planted.py. Must fail. | **not caught** |
| U24.h | `x = 3` then `assert x == 3` (a literal through one name). Must fail. | caught: test-vacuity |

- **Each case was planted and committed** in a scratch checkout of main's head with the series applied, under the
  repository's author, and every gate was run. The control, an empty commit, changed no gate.
- **U16.a and U16.d are caught by the rule of the second series,** which the sixth patch carries to the controls: a
  control does not leave the register without a recorded act. Reading the control would not have caught U16.a, whose
  test is real and passes. The seat says so: that a control turns its own gate red is not shown by reading.
- **The first series' case again** (U9.b: a repository made with `git init` and no commit, holding the gates, their
  checkers and three pages): all 24 gates of the two tables refuse it. None passes.
- **Why each of the five passes:**

| case | why it passes | did the seat's note say so |
|---|---|---|
| U17.b | the sweep flattens the whole file to see which phrases are in it, and then looks for each phrase line by line. A phrase over two lines is seen by the first step and found by the second on no line | no |
| U24.a, U24.g | the class is decided by working the assert out, and it stops at a call | yes: its § 7 b, with three tests on main's pages that are of this shape [CORRECTED 2026-11-12 (Review 80; found by a reading on another family of model and reproduced by main): three is far too few. The reader counts nine by its own shape. Main's scan by the syntax tree finds 92 tests in the tests' folder that read no name from outside themselves but a few pure builtins; 24 of them are held by name as found, and 68 are not] |
| U24.d | an assert that would fail if it were reached is not in the class; this one is never reached | in part: its § 6 d names `assert False` under an `if`, not a condition that is never true |
| U24.f | the test holds no assert, and a block that expects an exception counts as one | no |

## 4. What reading the patches found

Main read all six patches: the gates' and the checkers' code line by line, and the tests by their names and first
lines. One case came from the reading, and four more were written to see where the vacuity class ends. They are not among the cases sealed beforehand and are not counted with them.

| case | written after reading | result |
|---|---|---|
| AR1 | a Proven row citing a path under tests/ whose name is that of a test file and which is a folder holding one empty file | **passes every gate** |
| AR2 | `x, y = 3, 3` then `assert x == y` | **passes every gate** |
| AR3 | `assert (1, 2) == (1, 2)` | caught: test-vacuity |
| AR4 | `assert 2 > 1 and "a" < "b"` | caught: test-vacuity |
| AR5 | `x = 3`, `x = 3` again, then `assert x == 3` | **passes every gate** |

- **AR1.** The claims gate asks three things of a cited lock: that the path exists, that its name is that of a test
  file, and, if it is a file, that it holds a test. A folder with a test file's name passes all three. U20.c, sealed
  beforehand, used a folder whose name is not a test file's, and was caught for the name.
- **AR2 and AR5.** A name counts as a literal only if it is bound once, alone. The seat's note says the second; a
  pair bound in one line it does not name.
- **The tables of what is held by name.** Five tables hold what stood on main's pages when the rule came. The seat
  says that such a table can grow in the commit that adds what it excuses, the lock changing in the same commit.
  Nothing refuses that. By the rule of the second series it would shorten freely and grow only by a recorded act.
  Main asks the seat for that.

## 5. The further checks

| check | result |
|---|---|
| the series applied by `git am` on main's head | six commits, no conflict |
| each patch's lock, run on the commit before the patch | the seat's numbers. Patch 1: 6 fail. Patch 2: 5. Patch 3: 4. Patch 4: 2, and one in B1890's lock. Patch 5: 8, and two in the second series' lock. Patch 6: 4. The three in older locks are assertions the patch changes, as its note says. On each patch itself everything passes, but for one failure that was not seen again (below) |
| the three locks of the enforcement series on the end of the series, views generated | 72 pass |
| all 53 gates on the end of the series, views generated | 53 pass; one generated page changes |
| main's own tests that name a gate or a debt checker, 47 files, views generated | 385 pass, 3 skipped, 0 fail; with the second series it was 382 and 3, and the three more are those the fourth patch adds to the first series' lock |
| the planted suite, the version of 32 cases, run by main on the end of the series | controls 5 of 5; 24 of 32 planted cases caught; its six twins, the honest form of six of the cases, pass |

- **One failure that was not seen again.** When the two lock files that the sixth patch changes were run on the
  patch itself, one test of the fifty failed. Its name was not kept. The same files were then run in the same
  checkout alone (33 pass; 17 pass) and together (50 pass), and with the second series' lock in the other checkout
  (72 pass). At the moment it failed main was adding and removing worktrees of the same repository for another
  landing. Main does not know the cause.
- **What the framing gate says on main's own tree,** which holds files that are not tracked: it reads 14,824 text
  files there and 14,534 in the clean checkout. The gate walks its folders, as the seat's note says, so its sentence
  is the tree's.

## 6. Main's word on the nineteen rows, and the seat's choices

The sweep read 29 of the registry's 46 phrases [CORRECTED 2026-11-12 (Review 80; found by a reading on another family of model and reproduced by main): this read "48 phrases". The registry has 54 rows: 46 phrases, and
8 rows that take back a reading. Of the nineteen unquoted rows seventeen are phrases and two are readings; the other
six readings are in the quoted tables]. Nineteen rows, in three tables, hold their phrase unquoted, and the
registry's own note called nine of them descriptive and not swept. The seat asked main which rows are swept.

- **Main's word: the seat's proposal, as sent.** Seventeen rows are swept. Two say in their own words that they take
  back a reading and not a sentence, and are held by name as not swept.
- **Why.** It is the stricter of the two options. The registry's reason for leaving nine rows unswept was that their
  phrases still stand in the arcs' original titles. That is met another way: those lines are held by name, by file
  and phrase, and the phrase is swept in every other file.
- **The registry's two notes are rewritten,** each keeping what it said.
- **The old debt is paid** (register row P-154, of 2026-10-15): on main the sweep reads 54 rows, 46 swept and 8 that
  take back a reading.

| the seat's choice | main |
|---|---|
| what stood is held in tables in the code, pinned by the lock by content or by size; not read against history | kept for this landing; main asks for the second series' rule on them (§ 4) |
| the framing gate reads by content and walks its folders, so it reads files that are not tracked | kept. The push hook's clean worktree is what a push is judged on |
| the claims gate holds two tables to a lock, which may stand in any cell of the row | kept, with AR1 to be closed |
| the vacuity class is decided by working the assert out and stops at a call | kept, with the shapes of § 3 and § 4 to be closed or declared open |
| a registered phrase that can never fire is refused | kept |
| a control that is pointed elsewhere needs a recorded act | kept. It is one line of main's about every forty commits, by the seat's count |
| two words for a repository in which git has nothing to say of the tree | kept |
| tests of main's that the series changes, each with a dated note | accepted, each of them |

## 7. What main changed of its own at the landing

- **B1632's claim line leads with its correction.** The paper's table of candidate claims shows the first words of
  each arc's claim line, and for B1632 those words were a sentence that B1634 refuted in part. The seat found it when
  its sweep first read that row, and held the line by name so that the series could land. The claim line now leads
  with the correction, and the row of the paper's page carries it (register row P-808, item 3).
- **The seat's table of standing lines is shortened by that one line,** in the sweep and in its lock, as the gate's
  own sentence asked: eleven lines are held.
- **B1890's test is renamed.** Its name said that the gap of the first series was still there.
- **The registry's two notes** (§ 6).

## 8. What is not shown

- **The whole suite on a fresh clone** was not run on the series.
- **The unseen cases were run on main's head before B1895 landed,** with the series applied. The patches have not
  changed since they were read.
- **That a control turns its own gate red** is not shown by reading, as the seat says. Its read-out, in which 16 of
  the 53 controls still pass with every gate made unable to fail, is the seat's run.
- **The mends of the shapes of § 3 and § 4** are not written.
- **The cause of the one failure of § 5** is not known.

## Seen first

Swept from main at `3c5ab6bef`.

- `VERDICT topic-sweep /reads all it is about|held by name|no assert can fail|cannot fail|vacuous|vacuity|retraction sweep|framing gate|controls gate|claims gate/ (full text): 189 of 1642 arcs on main match (NEGATIVE 43, OPEN 14, PROVED 128, RETRACTED 3, no verdict file 1); 15 register rows match (DONE 8, QUEUED 7)`
- `VERDICT topic-sweep /broken (across|over) (two )?lines?|line break in its middle|folder named like|a lock that is a (folder|directory)|pytest\.raises|tuple assignment/ (full text): 1 of 1642 arcs on main match (no verdict file 1); 2 register rows match (DONE 1, QUEUED 1)`

The arc with no verdict file is this one, then unfinished, and the two register rows of the second sweep were written
at this landing. Nearly all of the 189 match the words "vacuous" and "cannot fail" in other senses.

On record and used: B1890 and B1893, the first two series; B887, the gate audit of Review 38, which wrote in August
that the framing gate compares letter for letter; the register's rows P-154, the debt on the sweep's unread tables,
P-808, what the seat saw on main's pages, and P-816, the case the second series does not see. The shapes of § 3 and
§ 4 that still pass are not on record before this arc, but for the limit the seat names in its own note.

**The literature:** not searched. The series is a repair of the record's own gates.

## Disclosed

- **Main did not build the series and did not change a line of it.**
- **The five cases of § 4 were written after reading the patches.**
- **The unseen cases were run on main's head before B1895 landed.** The patches are byte for byte those on the
  seat's branch today.
- **The runner and its output are committed with five changes, four of them marked.** As run, the runner typed two of the framing
  gate's banned phrases, and the gates' messages named the phrases they found. The series' own framing gate reads
  every text file under frontier/, so the committed runner reads the phrases from the gate, and the committed
  output masks them. The six cases those changes touch were run again with the committed runner: each is caught by the same gate as in
  the first run. The two that plant a retracted phrase were run a third time, because the mask had missed an
  apostrophe that a gate's message escapes. The committed output holds the last run of each of the six.
- **U20.c was caught for a reason main had not meant.** Its folder's name was not a test file's. The case main meant
  is AR1, written after reading.
- **The runner for the fourth series' nine sealed cases is written,** before any of its patches was read, and is not
  published until it has been run (sha256 `591e7e85ca300e1354d7902299f0e1a7113ca81de21aa92900371daddc59d573`). Main
  had read the seat's notes on that series in part.

## Reproduce

```
python3 -m pytest -q tests/test_a_gate_reads_all_it_is_about.py tests/test_gates_are_a_function_of_the_commit.py tests/test_nothing_leaves_a_ledger.py
python3 -m pytest -q frontier/B1896_the_third_enforcement_series_verified_and_landed/verification/
```

The unseen cases need a scratch checkout with the series applied, beside the runner
(`verification/run_unseen_s3.py`, then `verification/after_reading_s3.py`). About eighty minutes.
