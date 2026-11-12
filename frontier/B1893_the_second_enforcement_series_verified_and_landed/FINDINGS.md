# B1893 — The second patch series for enforcement, verified with main's unseen cases and landed

*Main, 2026-11-12 (S306p). The advisor seat builds the enforcement package, WP-0.7, and main verifies what it builds.
The seat sent series 2: six patches under one rule, that nothing leaves a ledger and no ceiling rises without a
recorded act. Main ran its thirteen unseen cases for this series, read the six patches line by line, ran five further
checks, and landed the series. Reading the patches, main found one thing the rule does not see, and confirmed it by a
run. Nothing in the mathematics is touched. 0 of 19.*

## 1. The answer first

- **The series is landed as it was sent.** Six commits of the seat's, applied on main with no conflict.
- **All thirteen of main's unseen cases are caught.** Twelve by a gate that looks for the fault. One by accident:
  tests made to skip were caught only because their files are hashed.
- **One thing the rule does not see, found by reading and then run.** A ceiling is held to the value it had at the
  rule's anchor. If it falls and later rises back to that value, the rise needs no record. For the count of unearned
  identifications this matters: every identification that is earned makes room for a new unearned one to enter
  unseen.
- **It is the seat's to close in a later series,** as the gap of the first series was. Without the series the same
  thing passes, and more besides: the series narrows the hole and does not open it.
- **What the seat said of its own patches is what main found.** Each patch's lock fails on the commit before it, in
  the numbers the seat gave.
- **The planted suite,** run by main on the end of the series: controls 5 of 5; 19 of 32 planted cases caught, where
  main's head before the series caught 14. The five the series set out to close are caught. The thirteen that still
  pass are for the series after it.

## 2. What the series does

Five gates passed on a page that had been deleted or emptied, and one ceiling could be raised by the commit it was
meant to stop. The series gives one rule for all six, read from history as the append-only gates are:

> After the rule's anchor, what a ledger has held it still holds, and a ceiling stands no higher, unless the change is
> named in the gates' file with its date and what became of it.

| patch | the case | what is held now |
|---|---|---|
| 1 | the registry of retracted phrases deleted: the sweep read no phrase and passed | the registry must be there, and no phrase leaves it |
| 2 | the law map and the theorem ledger emptied: with no rows nothing could fail | no law leaves the law map, a law being known by the bold title of its row; no link leaves the chain |
| 3 | the identification baseline deleted, and three unearned rows added | the baseline must be there and hold a count; it rises only by a raise recorded in its own list; no row leaves the ledger |
| 4 | every lock deleted: the gate counted none that cannot fail among none | a lock file does not leave without a recorded retirement; one that is moved is where it went |
| 5 | a ceiling of the attribution baseline raised in the commit that needed it | no entry of that table stands higher than at the anchor, unless named |
| 6 | the anchor moved forward past a deletion | the anchor's value is pinned in the lock, so a move shows in two places. The seat says a chain of anchors would close it and is not built |

- **A named change is counted in the gate's own sentence,** which the runner prints at every push.
- **Where the history cannot be read back to the anchor, the gate fails** and says so.
- **Five gates now read the past** and moved to that table: retraction-sweep, chain-locks, law-map-provenance,
  identification-register and test-vacuity.

## 3. The thirteen unseen cases

They were written on 2026-11-11 before the seat's first patch existed, and the hash of the file was published with
the handover (sha256 `06d73fbb029a832de6e2b144965711f0bc5cb94b107e494aefa9ab783f6ff893`). These thirteen of its 53
cases are published here, as written. With the nine of B1890 that makes 22; the other 31 stay sealed until their
series is read.

| case | as it was written | the gate that caught it |
|---|---|---|
| U10.a | the identification baseline truncated to invalid JSON, the file still there; three unearned rows added | identification-register |
| U10.b | the baseline's number raised by 3 in the commit that adds three unearned rows | identification-register |
| U10.c | the baseline's key renamed, so that the lookup returns nothing; three rows added | identification-register |
| U19.a | a new file entry added to the attribution baseline with count 4, and a new tracked page with 4 vendor tokens | attribution |
| U19.b | one file's frozen count lowered by 2 and another's raised by 2, and 2 tokens added to the second file | attribution |
| U11.a | the registry of retracted phrases cut to its header: the file is there and has no rows | retraction-sweep |
| U11.b | the last ten rows of the registry deleted and one of the ten phrases pasted into the README | retraction-sweep |
| U12.a | every lock under an arc's own folder deleted (the seat's case deletes those in `tests/`): 65 files | test-vacuity |
| U12.b | every lock in `tests/` kept and marked to skip: the tests exist and never run. 1,407 files | **artifact-hashes only: by accident** |
| U12.c | twenty locks renamed to a name the suite does not collect | test-vacuity, chain-locks, law-map-provenance |
| U13.a | every second row of the law map deleted: 162 of 324 | law-map-provenance |
| U13.b | the theorem ledger cut after its first link | chain-locks |
| U13.c | the identification ledger cut to its header, with the baseline left as it is | identification-register |

- **The one caught by accident.** No gate looks for a lock that is switched off. The hash gate failed because the
  files it hashes had changed. A lock that no hash list names could be made to skip unseen. The seat has since sent
  the mend, as the fourth patch of its fourth series; main has not read it.
- **Two cases were run twice.** Main's first runner made its planted commits under another author, which fails the
  attribution gate by itself. The two cases that only that gate could catch, U19.a and U19.b, were run again under
  the repository's author, with an empty commit as a control that must change nothing. Both are caught for what was
  planted: the gate names the ceiling that rose.
- **In one case main departed from its own wording.** U12.b says the mark is the file's second line. It was appended
  at the end, which has the same effect and does not break a docstring.

## 4. What reading the patches found

Main read all six patches, 1,147 lines. Two things:

- **A ceiling that falls and rises back.** Patch 3 holds the identification baseline to its value at the anchor plus
  the raises recorded since. Patch 5 holds each entry of the attribution table to its value at the anchor. Neither
  reads the values in between. So a ceiling that is lowered, as it should be when a debt is paid, can later be raised
  back to its old value in the commit that needs the room.
  - **Run, in a small repository made with the series' own helpers** (`verification/a_ceiling_that_falls_and_rises_back.py`):
    the baseline falls from 1 to 0 when a row is earned; a new unearned row then enters with the baseline moved back
    to 1 and no record. The gate says "ok". The control, the same rise with no fall before it, is refused.
  - **The same for the attribution table:** 4 to 2 and back to 4 is not seen; 4 to 5 is.
  - **What would close it:** the rule read along the history, so that every upward step since the anchor needs its
    record, not only the difference between the anchor and now.
- **A law is known by the bold title of its row.** A title that is corrected is a law that left and one that came,
  and must be named. That is the seat's choice and it is kept; main checked that its own scope notes of Review 79,
  written after the anchor, changed no title: 324 titles then, the same 324 now.

## 5. The further checks

| check | result |
|---|---|
| the series applied by `git am` on main's head `896cae025` | six commits, no conflict |
| each patch's lock, run on the commit before the patch | patch 1: all 5 fail. Patch 2: 4 fail, 5 pass. Patch 3: 5 fail, 9 pass. Patch 4: 5 fail, 14 pass. Patch 5: 3 fail, 19 pass. These are the seat's numbers. Patch 6's was not run: its one assertion holds before it as well |
| the series' own lock on the end of the series | 22 pass |
| all 53 gates on the end of the series, views generated | 53 pass; one generated page changes |
| main's own tests that name a gate or a debt checker, 47 files, views generated | 382 pass, 3 skipped, 0 fail |
| nothing has left main's own ledgers since the anchor, by the series' rule | 324 law titles, 57 links, every lock file and every phrase are still there; no ceiling stands higher |

## 6. The seat's choices, each of which it left for main to overrule

| the seat's choice | main |
|---|---|
| a recorded act is an entry in the gates' own file, not a page beside the ledger | kept: it is printed at every push |
| what stood before the anchor is not judged again | kept |
| a law is its row's bold title | kept |
| a ceiling may fall freely | kept, with the case of § 4 to be closed |
| a lock that is moved has not left | kept |
| the lock pins the anchor's value and that the two tables of named changes are empty | kept. It is a lock that pins a value on purpose: a move or a first entry is then made in two places |

## 7. What is not shown

- **The whole suite on a fresh clone** was not run on the series. It was run on main's head before it, at
  `896cae025`: 2 failed, 8,454 passed, 73 skipped, the two being the standing ones (register row P-239).
- **Main's unseen cases were run on the series as built on an earlier head of main.** The patches have not changed
  since: the seat's folder was last changed at the commit main read then. They were not run again on today's head.
- **Patch 6's lock was not run on the commit before it.**
- **A history that reaches the anchor through a merge** was not tried. Main's line has none.
- **The mend of the case of § 4** is not written.

## Seen first

Swept from main at `896cae025`.

- `VERDICT topic-sweep /nothing leaves|recorded act|ceiling (rises|rose|may fall)|baseline rose|raised in the commit|ratchet/ (full text): 25 of 1639 arcs on main match (NEGATIVE 3, OPEN 4, PROVED 17, no verdict file 1); 3 register rows match (DONE 1, QUEUED 2)`
- `VERDICT topic-sweep /falls? and (then )?rises?|lowered and (then )?raised|rise back|low-water|high-water/ (full text): 2 of 1639 arcs on main match (PROVED 1, no verdict file 1); 0 register rows match (none)`

The arc with no verdict file is this one, then unfinished. Nearly all of the 25 match on the word "ratchet". On
record and used: B1231, which made the identification ratchet; B1242, where that ratchet was lowered because two
identifications were settled, so the baseline does fall in practice; B1461 and B1464, the gates' failing-path tests;
B1890, the first series; and the register's rows P-757 and P-806. None states the rule of this series. The second
sweep's one other match is about another thing, the atlas's lexicon. So the case of § 4 is not on record.

**The literature:** not searched. The series is a repair of the record's own gates. The idea that a ratchet must be
read along its history and not at its two ends is ordinary, and main read it in no source for this arc.

## Disclosed

- **Main did not build the series and did not change a line of it.**
- **The case of § 4 was written after reading the patches.** It is not one of the cases sealed beforehand, and is
  not counted among them.
- **The thirteen unseen cases were run on 2026-11-11,** before Review 79, on the series as the seat built it. This
  arc lands them.

## Reproduce

On a checkout that has the series applied:

```
python3 -m pytest -q tests/test_nothing_leaves_a_ledger.py
python3 frontier/B1893_the_second_enforcement_series_verified_and_landed/verification/a_ceiling_that_falls_and_rises_back.py .
python3 -m pytest -q frontier/B1893_the_second_enforcement_series_verified_and_landed/verification/
```

The unseen cases need a scratch checkout with the series applied, beside the runner
(`verification/run_unseen_s2.py`, then `verification/rerun_u19.py`). About twenty minutes.
