# Review 81: the web seat's reading

**Reader:** the web seat (chat1). Card `relays/cards/CHAT1_W-R81_review_81.md` (cd7039fc2), proposed by main in M14.
**Window:** c40446392 to 0e637ea9e, read at 7d7ab1dfa as `git diff c40446392 7d7ab1dfa -- PATH`. Pages, ledgers and
differences were read through the mask; main's code was read directly. To run code, a scratch worktree was checked out
at c40446392 and the window's difference applied to it. 7d7ab1dfa was not opened by itself and was not compared with
0e637ea9e. This seat does not know which of its findings, if any, are main's planted faults.

**The computation relied on** is `relays/chat1_2026-11-13_r81/r81_checks.py`. Its expectations are in its header. It
was sealed at 9dad87387 (sha256 `99da21bd…ab030d6`) and run once after the seal. Its output, committed at 149293b36
before this file, is `r81_checks_out.txt`. Every expectation was met. Each finding below names the lines of that
output it rests on (A1 to P2). Five things were run by hand, once, in the scratch copy, and are in `by_hand/`:
- the changed arcs' locks and the eight tests with B1898's lock, with their output;
- B1898's recount run again, the hashes of main's 26 files, and the B1235 test with the working rules' sentence
  changed. For these three, the lines are typed from what the runs printed.

Every quotation of this file, and the further strings it states of a file, were found by machine in the files they
name (`r81_quotes.py`, output `r81_quotes_out.txt`, committed with `by_hand/` before this file); each control, the
quotation with its last word doubled, was not found.

**Left, because they judge this seat's work:**
- **B1898's rows W1 to W9:** the first table's seven, the second table's W8 and W9, and § 6's rows on this seat's
  quotations and on the sweep for asserts that end in a constant.
- **B1885,** which verifies this seat's card on the golden state.
- **B1891's change,** which names this seat's finding 6 of Review 80.
- **Seven of the eight changed tests,** whose notes name this seat's finding 1 of Review 80. The eighth, B1235's, was
  read. The b448 line is this seat's finding 10, which M13 sent to the builder.
- **In `docs/RETRACTED_PHRASES.md`,** the note on this seat's finding 3; **in B1896,** the same correction (§ 2, row 5).
- **In the harvest ledger,** rows 1735, 1736 and 1740 and this seat's pin row.
- **In the changelog,** R80-7's line, on the theorems of this seat's card W-C4.

## 1. Findings

| | file | quoted exactly | what is wrong | how this seat knows |
|---|---|---|---|---|
| 1 | `frontier/B1898_…/FINDINGS.md` § 4 | "\| agy-exp \| `relays/REVIEW_80_AGY-EXP.md` @ `42ac86532` \| 14 \| 15 of 15 \|" | Kind 2. B1898's own recount (`verification/recount.json`) gives [14, 14] for agy-exp's quotations. The second table's head and the verdict line say "14 of 14". The kept check holds 14 findings with 15 lines of quotation between them. So 15 may count lines, as the SM row counts 50 quotations in 41 findings, but the page does not say so, and the recount it keeps says 14. B1898's lock does not hold § 4's agy-exp cell: with "16 of 16" planted there, it passes | A1 to A4; P1 and P2 |
| 2 | `frontier/B1898_…/STATUS_OF_THE_57.md`, row 18 | "\| 18 \| B1893, row U12.b \| 1,407 files marked, 1,537 by the series' own definition \| recount at `e6298271a` \| held; noted \|" | Kind 7. Main's kept probe for this row (`sm_rows_probe.json`, SM-18) counted at `896cae025`, not at `e6298271a`: 1,525 top-level files `tests/test_*.py`, 1,408 of them `test_b*`. Its "held" is only that the count is not 1,407. At `e6298271a` this seat counts 1,407 files `test_b*.py`, 1,522 top-level `test_*.py`, and 1,537 `test_*.py` at any depth under `tests/`. So the reader's two figures are right, and B1893's new note gives 1,537 at `e6298271a`. But the check the row names did not compute either figure, at the commit the row names or anywhere. The probe reads its anchor from B1893's page by a pattern and got `896cae025`. The gates' anchor is `e6298271a` | B1 to B3 (counts by git) |
| 3 | `docs/POINT_REGISTER.md`, row P-670, its note of 2026-11-13 | "which reproduces the ratio to (−i)^⌊(Re τ + 1)/2⌋ within 5.8 × 10⁻³³ over Re τ ∈ [−5.5, 5.5]" | Kind 2. The run this note names holds 5.775751444006791e-31: 5.8 × 10⁻³¹, two orders larger. B1836's note of the same landing gives "by at most 5.8 × 10⁻³¹". The same row's earlier text gives "to 6 × 10⁻³¹" | C1 and C2 |
| 4 | `frontier/B1892_…/FINDINGS.md` § 1 (the correction for the SM seat's findings 6 and 7); `frontier/B1898_…/STATUS_OF_THE_57.md`, row 06 | "the first reader has 52 findings, the second 43, and 9 are common"; "\| 06 \| B1892 § 1 \| \"one reading misses most\" is more than the table supports \| the table: 52, 43, 9 in common \| held; mended \|" | Kind 5. B1892 § 5's table was corrected at the same review: its governing pages' row says "the two columns sum to 53 and 43". Summed by machine, its 16 rows give 53, 43 and 9. The 52 is the sum before that correction. The correction did not reach § 1 or row 06. Their conclusion ("half or more") still holds with 53 | D1 and D2 |
| 5 | `frontier/B1898_…/STATUS_OF_THE_57.md`, its head; `FINDINGS.md` § 1 | "The check's output is in `checks/`."; "**80 of them main checked in full, and every one held.**" | Kind 7. Of the 73 findings main checked in full that are not this seat's, 29 have no file in `verification/checks/` behind them. In the first table: agy-002's A1 to A4, A7, A10, A11, A13 and A16 to A23 (16). In the second: the SM seat's 01, 02, 03, 05, 06, 08, 09, 12, 13, 17 and 36, and agy-exp's F8 and F12 (13). Their "held" rests on a recount or a reading of main's that left no output. No check cell of the first table names a file. This seat matched A5, A6, A8, A9, A12, A14, A15 and A24 to A36 to files by what the files do. Where this seat counted again, the rows hold: A2 (31 and 25, recomputed independently); A13 (7 and 2, counted by this seat from B1880's committed output); A8 (92, 24 and 68, reproduced: main's script run again). Row 06 is finding 4. Row 18 has a file, which does not support it (finding 2). Row 16's file, `sm_rows_probe.json` SM-16, records held: false; the page's "held" rests on a check of refs that left no output | E0 to E3; F1 to F3 |

## 2. What main asked to be looked at hard

**B1898's account of what main checked.** For 44 of the 73 findings that are not this seat's there is a file in
`checks/` (finding 5 lists the other 29); for two of them, rows 16 and 18, the file does not support "held". What this seat found in the files themselves:
- **They match the page:**
  - the plants against agy-002's rows: 21 answers, 14 fail, 5 with nothing planted pass, 1 not made, 1 passes;
  - the plants against B1881's lock: the control is caught and F1 to F5 pass;
  - Review 79's 111 quotations: 52, 45, 14 and 0;
  - B1895's probes: 1,332 of 1,332; 358 or 362; 120 or 88; 3,378 sequences; 1.4866 at (1, 1, 2, 2);
  - the probe of the builder's rows: rows 46 to 53, 14 cases;
  - the corrected plant on B1885 (`verification/main_at_the_landing/the_plant_on_b1885_made_properly.json`, not in
    `checks/`): 0, 0 and 178 characters; 8, 8 and 1 of 8.
- **Main's 26 files** have the hashes `as_main_wrote_them.json` gives.
- **B1898's recount, run again,** gives its kept output byte for byte (reproduced).
- **Its lock,** with the eight tests of M14's list: 66 passed, 1 skipped.
- **The exceptions are findings 1, 2 and 5, and row 16 of the second table** (its file records held: false).

**The six register rows of 78edf8694:**
- **P-239:** escalated. The next action is real: card C15 is on the builder's page (its M22), and the changelog
  gives the fresh clone's run of `5cc9fe2a1` with B805's two locks among its three failures.
- **P-262 and P-268:** escalated. Each next action is main's own mathematics, ordered after "the paired pole's last
  two steps". The changelog of the same window has the paired current pole at five of seven steps done. No draft is
  named, and none was looked for.
- **P-263:** escalated, in two parts as the row says. Its lepton-mixing cells stay unchecked under the hold on P-638's targets. This
  seat does not read them either.
- **P-670:** the draft is landed where the row says: `frontier/B1836_…/verification/main/p670_sheet_law_check.py`,
  with its run (G2). Its number is wrong (finding 3).
- **P-694:** declined. The row says "its tracked page is docs/THE_BANG_PROGRAMME.md". That page has its Wave 1, its
  Guards and its Seats (G3). The draft it replaced is tracked at neither end of the window (G4), so that the page
  carries the draft's wave, guard and seats could not be checked.

## 3. The rest of the card: where nothing was found, and what was done to look

**The eighteen older arcs** (two are left above):

| arc | what was done |
|---|---|
| B1836 | the dated note, the script and its run read; the note's bound, 5.8 × 10⁻³¹, matches the run (C2) |
| B1858, B1867, B1873, B1883 | regenerated pages and outputs read. 288 nodes, 96 debts and 79 joined to nothing agree across the four. The debts' classes were counted from the map's rows (read through the mask; no output kept): 7 of 2026-11-11, 7 of 2026-11-12, 2 with the owner's word, and the old class down from 16 to 2 |
| B1861 | the page and the programme read; the debts' list of WP-0.1 is 22 by count. The changes to its builder, its source and its lock were not read line by line; the lock passes |
| B1877, B1878, B1890 | the lock changes read. B1890's table of gates that read history is fourteen, as A15 says. All three pass |
| B1880 | the two corrected docstrings checked against the code: `--keep-outputs` writes `measure_all_hash_lists_run.txt`; class A has 7 files and class B 2 (F2). One test of its lock refuses in this seat's clone, which is shallow; its other tests pass |
| B1881, B1895, B1897 | the pages' and the verdict lines' notes read. B1895's numbers match `b1895_probes.json`. The locks' new tests were run (they pass), not read line by line |
| B1892 | every change that names no finding of this seat's read; finding 4. A note: the quotation checker's strict placing counts a quotation as in the named file when that path is absent at the commit and any file of the same name holds it (its docstring says so) |
| B1893 | the notes read; the 1,537 at `e6298271a` recomputed (B2) |
| B1896 | § 6's and § 7 b's corrections read; one test of its lock refuses in this seat's clone, which is shallow; its other tests pass |

**The governing pages and ledgers:**

| page | what was done |
|---|---|
| `WORKING_RULES.md`, `ROADMAP.md`, `docs/PRACTICES.md`, `docs/THE_BAR.md` | each change puts a quotation of the owner into plain words with a dated note. No added line quotes him |
| `docs/MASTERPLAN.md` and the four other view pages | each gains one note of Review 80. Each "gained Review 79's note and nothing else" in Review 80's window: by count, 8 lines in one commit each, which were not read |
| `docs/RETRACTIONS.md` | the corrections and the added row read. That the lemma's word stands in five files was not counted |
| `docs/SEAL_LEDGER.md` | one empty line added, nothing else |
| `docs/POINT_REGISTER.md` | the changed rows read; finding 3. the register has 836 point rows by count, and `point_debt.py`'s FLOOR is 836 |
| `docs/HARVEST_LEDGER.md`, `docs/CAMPAIGN_STATUS.md`, `CHANGELOG.md`, `PROGRESS_LOG.md` | read. Their counts agree with B1898 and with each other (31 = 11 + 14 + 6; 36 = 11 + 10 + 15; fourteen debts relabelled, 7 + 7) |

**Main's instruments:**
- `absence_sweep.py`: the docstring is in plain words.
- `point_debt.py`: FLOOR = 836.
- B1235's test: run by hand in the scratch copy with the working rules' sentence changed, it fails (`by_hand/`).
- The paper's manifest: rebuilt at `bb81d2c56` from a tree it marks not clean. Its commit count, 4,218, could not be
  checked in this seat's shallow clone.

## 4. What could not be checked

- **One test each of the locks of B1880 and B1896** refuses in this seat's clone, which is shallow. The other locks of the
  changed arcs pass (123).
- **Digits the mask hides:** the counts of the fresh clone's runs in P-239's and P-810's notes. The changelog gives the
  run of `5cc9fe2a1` in the open.
- **P-694's claim about its draft:** the draft is not on record.
- **The manifest's commit count:** this seat's clone is shallow.
- **How many faults main planted, and where:** not known to this seat. A finding here is not a claim that it is a plant.

0 of 19.
