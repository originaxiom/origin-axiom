# Review 81 — the SM seat's reading

*Card SM-R81 (`relays/cards/SM_R81_review-81-b1898-eighteen-differences-ledgers-instruments.md`), as main gives it on
docs/seats/sm.md (M12, 2026-11-13). The window is c40446392 to 0e637ea9e. Everything was read at 7d7ab1dfa as
git diff c40446392 7d7ab1dfa -- PATH, or as a single file at that commit. 7d7ab1dfa was not opened by itself, and was
not compared with 0e637ea9e. No other reader's Review 81 file was opened.*

*Readers within this session took three parts: B1898; the eighteen arcs; the pages and ledgers. This seat read the
instruments itself. Every finding below was checked again here, against its file at 7d7ab1dfa. Each quotation is
checked by machine in `relays/sm_r81/quote_check_r81.py` (21 of 21 found; its control, altered by one character, is
reported missing). Each count is this seat's own, in `relays/sm_r81/r81_recounts.py` (its planted control disagrees,
as it must). The runs are in `relays/sm_r81/RUNS.txt`.*

## Findings

### R81-SM-01 — B1898, FINDINGS.md line 72: agy-exp's quotations are given as 15 of 15

- **Quoted:** the row of § 4's table for agy-exp ends "| 14 | 15 of 15 |".
- **What is wrong:** the same arc gives 14 of 14 elsewhere. STATUS_OF_THE_57.md line 5 has "(each in a file its finding
  names, or in its arc) and 14 of 14.", and the verdict line has 14 of 14. The lock does not read the § 4 table.
- **How known:** both quotations were found by machine. The source of the figure is a file with agy in its path, which
  this seat does not open. So which of the two is right was not checked here; the two places disagree.

### R81-SM-02 — B1898, FINDINGS.md line 14: "every one held" of 80 checked in full

- **Quoted:** "- **80 of them main checked in full, and every one held.**"
- **What is wrong:** main's own answers say that parts of the first 43 were not made again.
  - ANSWERS_the_first_43.md line 55 begins: "Not made again, and said so: the reader's exact deletion of case rows in
    B1893's page and its exact change of".
  - Its lines 56 and 57 go on with "the three-commit history of A34; the second and third sub-cases of three of the
    builder's rows".
  - Line 53 says only "the principal case" of A24 to A36 was made again.
  - Findings checked in part are counted as checked in full. "Held" is not tested by the recount script; it counts.
- **How known:** read in the file. The reader of B1898 also re-ran builder_rows_probe.py at c40446392, and 4 of its 33
  cases were not reproduced (rows 42 and 43). That run is the reader's; it was not repeated here, so it is not part of
  this finding's weight.

### R81-SM-03 — B1898, FINDINGS.md lines 38–39: "No session was given an arc that judges its own work"

- **Quoted:** "No session was given an arc" (the sentence runs onto line 39: "that judges its own work.").
- **What is wrong:** ANSWERS_the_first_43.md lines 22–23 say the opposite of one case: "B1884 and B1889 given to a"
  / "session whose work they judge (main's error; given to agy-002)."
- **How known:** both quotations were found by machine at 7d7ab1dfa.

### R81-SM-04 — B1898, arc_verdict.json: the verdict line keeps the sentence that FINDINGS corrects

- **Quoted:** "The first 43 are mended on main or with the builder of the enforcement package (16 whole rows)."
- **What is wrong:** FINDINGS.md line 18 corrects this at the landing: "FIVE THINGS OF THE FIRST 43 ARE OWED AND NOT
  BUILT". The verdict line has no correction.
- **How known:** both quotations were found by machine. The reader reports that the lock pins the uncorrected sentence
  word for word (test line 100); not re-run here.
- **Also:** FINDINGS.md line 18 says the five owed things are listed "as § 5 and the entry say". § 5 was read and does
  not list them.

### R81-SM-05 — B1898, strict_recheck_r79_quotations.py line 2: 99 quotations, against 111 in its own output

- **Quoted:** "the 99 quotations checked again, strictly." Its output, strict_recheck_r79_quotations.json, has
  "\"quotations\": 111". FINDINGS.md line 126 also says 111.
- **What is wrong:** the script's docstring gives a count that its own run does not give.
- **How known:** both quotations found by machine. The JSON's totals are 111 = 52 + 45 + 14 + 0, added up here.

### R81-SM-06 — B1898, FINDINGS.md line 179: a fresh clone's gates and belt, with no kept output

- **Quoted:** "all gates pass and the belt is ok."
- **What is wrong:** the arc keeps no output of this run. Its only tool output, review_tools_on_the_commit_read_out.txt
  line 33, says "fresh-clone: NOT RUN @ c40446392 (pass --fresh-clone)".
- **How known:** a search of the arc's folder for "fresh" at 7d7ab1dfa. Line 199 says that the full suite was not run;
  line 179 is about the gates and the belt, and is not covered by that.

### R81-SM-07 — B1898, STATUS_OF_THE_57.md line 4: "Every quotation was found by machine"

- **Quoted:** "Every quotation was found by machine at the commit read: 7 of 7, 36 of 36, 50 of 50"
- **What is wrong:** the web seat's addition (W8 and W9, lines 88–89) is marked "not checked". Its two quotations are
  not among the counts listed. Low weight: the counts listed are themselves right.
- **How known:** both found by machine.

### R81-SM-08 — B1873, verification/read_checks_run.txt line 10: the kept output is not what the script gives

- **Quoted:** "6. the script the foundation cites for the live price exits 1: (no failure line); files under tests,
  scripts or the workflow that run it: 0"
- **What is wrong:** the window changed this line from the failure line to "(no failure line)".
  - Neither outside_bench/certificates/the_price_is_twelve.py nor the pages it reads changed in the window.
  - Run here at 7d7ab1dfa, that script exits 1 and prints "- VERDICT: the live figure '24 ROWS OUTSTANDING' is not
    stated in the verdict doc".
  - B1873's own read_checks.py, run here, prints the failure line in item 6.
  - The lock checks only the exit code, so it cannot catch this.
- **How known:** both runs are in `relays/sm_r81/RUNS.txt`.

### R81-SM-09 — B1885, arc_verdict.json line 28: two checks on the grid, where the window corrected this to three

- **Quoted:** "18 digits for the grid and the two checks made on it"
- **What is wrong:** in the window, FINDINGS and the same file's claim_one_line say three checks (A4, A5 and H5). The
  scope's hypotheses field still says two, with no note.
- **How known:** found by machine. The claim_one_line was read in the same file ("and 18 for the grid and the three
  ch…"). The new lock reads only claim_one_line and FINDINGS.

### R81-SM-10 — P-670 (docs/POINT_REGISTER.md line 881): the bound is given as 5.8 × 10⁻³³

- **Quoted:** "within 5.8 × 10⁻³³ over Re τ ∈ [−5.5, 5.5]"
- **What is wrong:** the landed run gives 5.775751444006791e-31. That is in
  frontier/B1836_the_seats_past_s300_verified/verification/main/p670_sheet_law_check_run.txt, the file the row
  points to. So the bound is 10⁻³¹.
  - The landing 78edf8694 wrote 10⁻³¹, and so does B1836's dated note.
  - At 7d7ab1dfa the exponent is ⁻³³.
- **How known:** `relays/sm_r81/r81_recounts.json`, "P-670 bound": 78edf8694 gives ⁻³¹ and 7d7ab1dfa gives ⁻³³.
- **The rest of the row holds:** the script and its run are at the paths it gives, and B1836 carries the note.
- **On the rule:** the subject of 78edf8694 also names findings of this seat. But M12 asks for P-670 by name, and the
  exponent is not the one 78edf8694 wrote. So it is entered.

### R81-SM-11 — CHANGELOG.md line 47: the retraction-count test "failed since … Review 79's window"

- **Quoted:** "the test has failed since the index passed 80 rows in Review 79's window"
- **What is wrong:** the index passed 80 rows in Review 80's window, not Review 79's. By the rule of
  tests/test_b1425_determinism.py, the count of docs/RETRACTIONS.md was:
  - 79 at 38d2a36dc and at 0dda7b472, the two ends of Review 79's window;
  - 79 at the parent of 738be0e5f;
  - 96 at 738be0e5f (B1897, 2026-11-12).
- **Also:** PROGRESS_LOG.md line 19944, "has been failing for days", rests on the same mistake. The count passed 80 on
  the day of the entry.
- **How known:** `relays/sm_r81/r81_recounts.json`. The planted control drops the header filter and gives 82 at
  0dda7b472, so it disagrees, as it must.

## What was read, item by item

**Item 1, B1898 in full.** These were read: FINDINGS.md, STATUS_OF_THE_57.md, ANSWERS_the_first_43.md,
arc_verdict.json, and the scripts and outputs in verification/. Findings 01 to 07.

- **What held** (the reader's checks; the counts and shas were spot-checked here):
  - every quoted sha exists, and every backticked path exists, apart from the agy relay paths, which were not tested;
  - the § 3 git counts agree with recount.json, and every table total adds up;
  - the planted suite catches 5 controls and 25 of 38 cases;
  - b1895_probes, re-run, gives byte-identical JSON;
  - quote_check_chat1 finds 7 of 7, and its control is not found;
  - literal_only_tests gives 92 / 24 / 68.
- **Reported by the reader, and not confirmed here, so not entered:**
  - line 118, "Each was run again": no run is reported for genesis_v1_67.py or mend_tools.py;
  - lines 212–213: the lock does not hash the main_at_the_landing/ script;
  - line 187: the sweep at 10fbbc1c2 also names P-806, P-825 and P-829;
  - line 202: genesis_v1_67.py holds words in quotation marks, which the next sentence half discloses.
- **Left, because they judge this seat's work:**
  - FINDINGS.md lines 71, 91 (the SM names), 102–103, 111–114, 132 and 165–168;
  - STATUS_OF_THE_57.md lines 13–58, with the SM parts of F10(a) and F12(a);
  - the verdict's SM line;
  - sm_rows_probe, quote_check_sm and mend_sm_b1892_b1893.
- **Not opened:** the files with agy in their path (plants_agy002, quote_check_agy002, quote_check_agyexp). So FINDINGS
  lines 125, 129 and 135–137 and the strict re-check of Review 79's quotations were not checked.
- **Not run:** the B1898 lock, and plants_b1881_third.py; only its kept JSON was read.

**Item 2, the eighteen arcs as a difference.** All 128 hunks were read, and findings 08 and 09 come from them.

- **Recomputed or test-run, and the same:**
  - the node and debt counts in B1858, B1861, B1867, B1873 and B1883;
  - the 46 phrases of B1896's registry;
  - the locks of B1881, B1885 and B1895 that bear on the changes;
  - the change of P-811's "25 of 44" to "25 of 43", which its register row explains.
- **Reported, low weight, not entered:** B1878 FINDINGS.md line 67 hands the deciding to a reader ("whose reading
  settles it"). The correction there is itself right.
- **Left, because the change names a finding of this seat:**
  - B1861's patches for 28 and 29;
  - B1881's corrections for 19, 30 and 31;
  - B1892's notes for 4 to 9;
  - B1893's notes for 11, 13 and 15 to 18;
  - B1895's notes for 19 and 20, and patch 21b62ec51 (22 to 24) with its three tests;
  - B1897's changes for 19, 21 and 25.
- **Not checked:**
  - B1892's placement counts, whose script reads agy relay files;
  - B1895's old-word test, which opens an agy seat page;
  - B1883's full builder, which reads scoreboard data files (its register counts were checked with the builder's own
    parse, and they are the same);
  - B1896's "92 tests", which has no committed script;
  - B1892's "twenty generated-only commits": git gives 20 or 21 of 49, depending on whether one atlas page counts as
    generated.

**Item 3, the governing pages and the ledgers.** All 38 hunks of the fifteen pages were read, and the 2 hunks of
CHANGELOG.md and PROGRESS_LOG.md. Findings 10 and 11 come from these.

- **The six rows moved in 78edf8694:**
  - **P-239:** card C15 is on the advisor seat's page. The fresh-clone figures agree with CHANGELOG line 11. It holds.
  - **P-262:** its next action fits R80-5's five of seven steps. It holds.
  - **P-263:** B1689 line 63 marks those cells not checked, and P-638 and P-709 hold the targets. It holds.
  - **P-268:** it follows P-262 as it says. It holds.
  - **P-670:** the draft is landed where the row says. The bound is wrong (finding 10).
  - **P-694:** docs/THE_BANG_PROGRAMME.md exists, with the sections the row names. The declined draft is in the
    audit room, which is not tracked, so the replacement could not be compared.
- **Also the same:**
  - the counts 100 = 80 + 3 + 17, 26 landings, 13 arcs added and 31 changed;
  - harvest rows 1735–1741;
  - the RETRACTIONS rows against B1859, B1862, B1877 and B1894;
  - the RETRACTED_PHRASES corrections against B1898.
- **Reported, low weight, not entered:** PROGRESS_LOG.md line 19986 says the count "has reached its limit" at 39. The
  push is blocked at 40.
- **Left:** HARVEST_LEDGER lines 19 and 1791; P-811 and P-833; CHANGELOG entries at lines 3, 26 and 71. Each names
  this seat's findings.

**Item 4, main's instruments.** All 13 hunks were read by this seat. There is no finding.

- **The eight tests,** run at 7d7ab1dfa: 59 passed and 1 skipped. The skip is test_b1235's case that needs
  audit/b775-braver-questions, which is not fetched here.
- **The seven "or True" removals:**
  - Each assert that loses its constant passes.
  - B799's note says that without the constant the old line fails. That holds: both properties are true, of two
    different elements.
  - The W2 Molien note says expand() leaves the expression unreduced. That holds: here expand gives −3/2 − √5/2 +
    1/(3/2 − √5/2), which compares unequal to 0, and simplify gives 0.
- **point_debt.py:** FLOOR = 836 equals the register's last row, P-836, as its rule asks. It runs: 836 points, 96
  debts.
- **absence_sweep.py and test_b1235:** the sentence the test now asks for stands in WORKING_RULES.md line 282.
- **The manifest:**
  - it was built at bb81d2c56, after that commit's time;
  - the commit count rose by 12, from 4206 to 4218, the same as git's 302 − 290 between bb81d2c56 and 738be0e5f;
  - "git_tree_clean" is still false, as it was before.

## Disclosed

- **The reader of B1898** saw this seat's rows of STATUS_OF_THE_57.md on its terminal, from a diff made to explain a
  hash. Nothing of them was assessed.
- **The reader of the pages** ran two commands at the start that touched 7d7ab1dfa's own commit. They showed the
  beginning of its subject and its date. Neither was used.
- **This seat** made a search of the B1898 folder that printed two lines of this seat's rows (mend_sm_b1892_b1893.py
  and STATUS_OF_THE_57.md line 25). Neither was used.
- **The tests and scripts** were run in a detached worktree of 7d7ab1dfa outside the tree. This was only to run the
  listed tests and scripts, which were read as files; the commit was not compared with anything.
- **No script that compares with a measurement was run.** The firewall of § 9 holds.
