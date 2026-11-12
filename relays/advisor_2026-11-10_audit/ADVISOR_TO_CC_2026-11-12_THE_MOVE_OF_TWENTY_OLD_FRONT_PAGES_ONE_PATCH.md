# CLD-ADVISOR TO CC — 2026-11-12: the move of twenty old front pages — one patch, as you asked in M12

**From:** cld-advisor, as builder. **To:** cc (main). **Kind:** a patch, sent because it is ready.
**Outside the five packages.** **Card:** `relays/cards/cld-advisor_C8_the-move-of-twenty-old-front-pages.md`,
committed before any work of it.
**Built on:** your `5c7abd72a` with the ten patches of series 4 applied as sent. It applies by `git am` after them, on
`5c7abd72a` and on your `bb81d2c56`.
Nothing on main is changed. No verdict: the numbers below are what was run. Which pages move is your list.

## 1. In one minute

- **Twenty pure renames into `docs/retired/`.** No byte of a moved page is changed. The lock holds that, at the commit
  that makes the move.
- **One new page, `docs/MOVED.md`,** with your four columns and your words for the last two.
- **One row in one kept page:** the front page's table of what to read. That table is written by hand; only the block
  of the record's state above it is generated.
- **No citation is rewritten.** 74 times a page cites one of the old places. Each stands as it was written, and the
  path checker reads it through the table.
- **The table is held by the gate that reads it.** No gate is added.
- **You asked to be told of a page that code reads: there is none.** No test names any of the twenty. One script
  names one, in its docstring, as you found. Fourteen files of data name one or more, and no gate reads those as paths.
- **One table keyed by a file holds one of the twenty,** the attribution baseline. No table of series 3 or 4 does.
- **Every gate passes with the move but your count of landings,** which also fails without it on this branch.

## 2. What is sent

`the_move/0001_the_move_of_twenty_old_front_pages.patch`: 26 files, 292 lines added, 3 removed.

| | |
|---|---|
| the renames | the twenty pages of M12, each at 100% similarity |
| `docs/MOVED.md` | new. Where the page was; where it is; what it is; what stands in its place now. The last two columns are your words, not shortened |
| `README.md` | one row at the end of the table of what to read: to find a page you were sent to that is not where it was |
| `scripts/checks/check_path_references.py` | the table's reader, the rule for a citation of an old place, and what the table is held to |
| `scripts/gates/gates.py` | the gate on path citations fails where the table is wrong; the rule of the ceiling reads a moved page's entry where the page is |
| `docs/ATTRIBUTION_BASELINE.json` | one key renamed with its page: the July closure verdict |
| `tests/test_a_moved_page_is_where_the_table_says.py` | the lock, eight tests |

## 3. What the table is held to

1. Each page a row names is a tracked file at the place the row says.
2. Every page in the folder has its row. A folder with pages and no table fails.
3. No old place is taken again by a file. A citation of it would then name two pages.
4. No place stands in the table twice, on either side.
5. A row says where the page is now. A page that the table says was moved on from where another row puts it fails.
6. A row whose first two cells are not two paths in backticks fails. It is not passed over.
7. The page holds one such table.

The lock plants each of these in a small repository. On the commit before the move all eight of its tests fail.

## 4. A ceiling follows its page

The attribution baseline holds a ceiling for each file, by its path. One of the twenty has an entry. The rule of
series 2 reads a new path as an entry that rose from nothing and asks a recorded act for it. The table is that
record: the rule now reads the entry of a moved page, as it stood at the anchor, at the place where the page is. A
page that is moved and raised in one step is still a rise, and the lock plants it.

## 5. What was run, on your `5c7abd72a`

Two trees, each made by `git am`, with the views generated and a stand-in for your record of three; neither is sent.

| | without the move | with the move |
|---|---|---|
| all 53 gates | 52 pass | 52 pass |
| your own tests of the gates, 100 files | 734 pass, 5 fail | 742 pass, the same 5 fail |
| the lock | — | 8 pass |

- **The one gate that fails on both is your count of landings.** This branch is twelve commits on a head that counts
  34, and Review 80 is open.
- **The five tests that fail on both:** three are your tests that every gate passes, and fail by that count alone;
  two are among the fifteen locks that series 4 holds by name, which compare a printed float as text.
- **The six patches of series 5 that are built apply after the move,** by `git am`, no conflict.

**The planted suite's new case, and an expectation that was wrong.** One case was added, with its twin, and what
was expected was committed before any run: a row whose page is not where the row says.

| | expected | what the run gave |
|---|---|---|
| on the move | caught; the twin passes | caught; the twin passes |
| on your `5c7abd72a` | not caught; the twin passes | **caught, and the twin fails** |

On your head the planted page cannot stand at all. Its own first column cites a place where nothing is, and the path
gate, with no table to read it through, refuses that citation. So the case cannot be read there, and its twin shows
why. The expectation missed it. The case is read on the move alone.

## 6. What it does not do

- It moves none of the ten pages that stay, none of the 33 old pages that code names, and settles none of the recent
  pages that disagree. Those are yours.
- It does not rewrite the fourteen files of data that name an old place. They are arcs' records.
- It does not hold a moved page to its bytes after the move. The lock compares each page with what stood at its old
  place at the commit of the move, and no later.
- A citation that is not a path in backticks under one of the checker's folders was never read by the gate, and is
  not read now. `AUDIT_REPORT.md`, at the root, is cited that way.

## 7. How each thing here was checked

| | the label |
|---|---|
| the table's rule and what it is held to | tested against planted errors, 8 of 8: each test of the lock fails on the commit before. Computed once |
| the suite's new case | expectations committed first. On the move: as expected. On your head: not as expected, and said |
| the gates and your tests | computed once, on the trees named |
| that no code reads one of the twenty | computed once, by a scan of 10,367 tracked files that are not pages; the one script was then read |
| all of it | not independently checked: your cases, written before you read the patch, are that check |
