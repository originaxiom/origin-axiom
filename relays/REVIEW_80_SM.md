# Review 80 — the SM seat's reading (card SM-R80)

*Read at main c40446392, the window's end as M8 names it. The rules are § 13 of the protocol. Card:
`relays/cards/SM_R80_review-80-four-arcs-seven-differences-instruments.md`. The outputs this file relies on are in
relays/sm_r80/, committed before it (02216c5bb, 35a19ca55). No other session's Review 80 file was opened.
No measured value was read or compared, and no held-out target was computed. None of the files M6 names as not to be
opened was opened. Nothing the owner said is quoted here.*

## How the reading was done

- **Three readers within this session** took the work: one took B1892 and B1893; one took B1895, B1897 and B1881's
  changes; one took the other six arcs' changes and the instruments. This seat took B1641 and its lock.
- **Every finding below was checked again by this seat before entry:**
  - each quotation by machine at c40446392 (`relays/sm_r80/quote_check_r80.json`), with an altered control;
  - each number by rerunning the script behind it on a fresh checkout of c40446392 (`relays/sm_r80/RUNS.txt`), or by
    this seat's own code (`relays/sm_r80/r80_counts.json`, `relays/sm_r80/b1641_index_check.json`).
- **Candidates not entered** are listed at the end, with the reason.
- **Left as this seat's own:** in B1892 the rows of the SM seat's findings (SM-01 to 48), § 7's lines on this seat's
  plants, and the count for B1879; in B1894 the same. One candidate touches this seat's own answer to SM-16 and is
  left (§ 9).
- **Categories** are those of § 13, as in SM-R79: (1) a statement its outputs do not support; (2) a number that
  differs from its source; (3) a claim wider than what was computed; (4) a check that cannot fail, or a lock that pins
  a value; (5) a correction that did not travel; (6) something owed that no register row carries; (7) a label stronger
  than its evidence; (8) the owner quoted after 2026-11-11, a session as an authority, or a vendor's or model's name.
  **Minor** marks a finding that changes no conclusion.

## 1. Looked at hard: B1641's index

**The corrected sign holds.** B1641's sealed script defines its table as minus the triplet's Euler characteristic at
weight 3/2 + 12n plus the pieces' term. This seat recomputed that Euler characteristic from the statement in exact
arithmetic:
- by Borcherds' formula, with every matrix monomial so that each eigenvalue is an exact root of unity;
- validated first on the classical dimensions (k = 0 to 28) and on η^r for r = 1 to 23.

Results (`relays/sm_r80/b1641_index_check.json`):
- ρ_T's exponents are 1/8, 3/8 and 7/8; χ_{3/2}(ρ_T) = 0, and χ rises by 3 with each twelve of weight;
- a unit on any one line raises χ by 1, and the uniform unit equals the weight twelve higher;
- at an empty Λ₊ the index is +3, 0, −3 at n = −1, 0, 1, and −1 for a unit on one line, as the sealed table and the
  corrected notes say;
- **planted:** the defining term with its sign reversed disagrees with the sealed table, and is caught.

One finding on how far the correction travelled is R80-SM-27.

## 2. B1892 — Review 79 read by those who did not build it (10 findings)

**R80-SM-01** (3, and 6). arc_verdict.json:
- `Every arc of the window was read in full, all but one by two sessions`
- **What is wrong:** 25 arcs were changed and not added in Review 79's window (11 verdict files, 14 findings only, by
  the arc's own figures and by this seat's count). Seven of them are named on no reader's page: B731, B732, B733,
  B734, B942, B1030 and B1067. Three more are named only in passing, not on a card: B1028, B1222 and B1643. So ten
  were read by no reader of Review 79. Main then changed B1222's verdict line and B1643's findings at 57f604898, and
  no one has read those changes. No register row carries the reading owed.
- **How known:** `relays/sm_r80/r80_counts.json`, review79_window.

**R80-SM-02** (2, minor). FINDINGS.md § 5, the table of findings by arc and reader:
- `| the governing pages | 2 | 3 | 0, and two things the first wrote as notes are findings of the second |`
- **What is wrong:** the table's first-reader column adds to 52 and its second-reader column to 43. With B1889's three
  that is 98, not the 99 the page counts. One of the web seat's ten findings is not in the table.
- **How known:** `relays/sm_r80/r80_counts.json`, b1892_table5.

**R80-SM-03** (2, minor). FINDINGS.md § 8:
- `Of this window's 49, eighteen touched nothing but generated pages or a session's`
- **What is wrong:** of the 49 commits, 20 touch only generated pages or a seat's page. 18 is the count for the first
  45, the window as it stood when Review 79 opened.
- **How known:** `relays/sm_r80/r80_counts.json`, generated_only_commits.

**R80-SM-04** (1). FINDINGS.md § 2:
- `nothing was landed between the last message to the readers and this entry`
- **What is wrong:** the last message to the readers is f8b5e6769, at 00:11:54. c66c8ccae, at 00:20:21, is a landing:
  it changes CHANGELOG, PROGRESS_LOG, the campaign status, the register and the seal ledger. The entry, 84baf38fb, came
  at 03:04:24.
- **How known:** `relays/sm_r80/r80_counts.json`, b1892_order.

**R80-SM-05** (7, and 5). FINDINGS.md, ANSWERS.md and arc_verdict.json; the protocol, § 13:
- `Each row was reproduced by main at its source before a word was changed.`
- `ALL 99 HELD ON MAIN'S OWN REPRODUCTION`
- **What is wrong:** § 12 keeps "reproduced" for the same code run again on a clean checkout, with the second output as
  its evidence. No second output is committed for the 99, and ANSWERS defines "held" as main finding what the reader
  found. A18 found the same word in § 8 and § 8 was corrected; § 13 still says that main reproduces each finding.
- **How known:** the protocol's § 12 and § 13 at c40446392, against the arc's files.

**R80-SM-06** (3). FINDINGS.md § 1:
- `- **One reading misses most of what is there.** The 99 are 88 distinct faults. Ten were found by two readers.`
- **What is wrong:** the same page says that what it does not show is a rate. In the arcs two readers read, the table
  gives the first reader 52 findings, the second 43, and both 9. The first reading found most of what two readings
  found. "Misses most" rests on faults no reader found, which the arc does not estimate.
- **How known:** the arc's § 5 table (`relays/sm_r80/r80_counts.json`).

**R80-SM-07** (2, minor). ANSWERS.md:
- `lines, which the rule does not count: A9 with X13. So the 99 are 88 distinct faults, of which ten were found twice.`
- **What is wrong:** the page says that the rule written in advance does not count A9 with X13, and then counts it. By
  the rule the 99 are 89 distinct faults, nine found twice. The headline and the claim line give 88 and ten without
  saying so.
- **How known:** the sentence itself, and § 5's column of findings found by both, which adds to 9.

**R80-SM-08** (1, minor). FINDINGS.md § 3:
- `` `38d2a36dc` to `0dda7b472`: 49 commits. The readers read `323f92327` and, for what was added to their cards, ``
- **What is wrong:** the arc's own quotation check gives agy-002 and agy-exp the commit 0dda7b472 only, and their
  delivery commits name it. The core claim, that no reader's findings were mended before the second reader delivered,
  is not touched.
- **How known:** the arc's verification/quote_check.py, its readers' table.

**R80-SM-09** (7, minor). FINDINGS.md § 7:
- `` - **The full suite on a fresh clone,** at `323f92327`: 15 failed, 8,422 passed, 72 skipped. ``
- **What is wrong:** no output of this run is committed anywhere. The arc's own § 6 counts a row "14 pass" with no
  committed run behind it as a fault of the same kind.
- **How known:** the figure is found only as typed text: in CHANGELOG, PROGRESS_LOG, P-810, the review's log entry and
  this page.

**R80-SM-10** (4, minor). verification/quote_check.py:
- `out.append((arc if arc != "M4" else "window", None, q))`
- **What is wrong:** the page says a quotation is looked for "in the file at the commit read". The check searches a
  pool: the named file, every file of the arc, wide pages and same-named files. For the SM seat's 59 quotations it is
  given no file at all. No count changes: each of the other readers' 52 quotations is in its own named file.
- **How known:** the script at c40446392.

## 3. B1893 — the second enforcement series, verified and landed (8 findings)

**R80-SM-11** (3, and 1). FINDINGS.md § 1 and arc_verdict.json:
- `Each patch's lock fails on the commit before it, in`
- **What is wrong:** the arc's own run file says, of patch 6, "not run by main. The patch adds one assertion that
  holds before it as well". So five of six patch locks fail on the commit before them, not all six.
- **How known:** verification/each_patchs_lock_on_the_commit_before_run.txt, against the sentence.

**R80-SM-12** (4). The lock, the pair for the case of § 4 (a ceiling that falls and rises back):
- `When the seat closes it, the first assertion of each pair fails`
- **What is wrong:** for the attribution half the first assertion compares a count of 4 with 4, and no history is
  involved. A mend of the kind the page and P-816 name, which reads the baseline along its history, sees the planted
  4 → 2 → 4 and leaves that assertion true. So the lock would not tell main that the attribution half had been
  closed.
- **How known:** `relays/sm_r80/lock_b_half_demo_out.txt` (a reader's script, rerun here): as landed, (None, ''); with
  such a mend, the rise is reported; the assertion, unchanged, True.

**R80-SM-13** (3, minor). FINDINGS.md, the table of main's unseen cases, row U13.c:
- `| U13.c | the identification ledger cut to its header, with the baseline left as it is | identification-register |`
- **What is wrong:** the page counts this among the twelve caught "by a gate that looks for the fault". The only
  committed message for it comes from a check that predates the series ("declares ..., no ledger row"; gates.py line
  2111 at e6298271a). The case is caught without the series. Nothing committed shows the series' own rule firing.
- **How known:** unseen_s2.json at c40446392 and gates.py at e6298271a.

**R80-SM-14** (4, minor). The lock, its reading of the unseen cases:
- `other = [x for x in r["gates newly failing"] if x != "attribution"]`
- **What is wrong:** for U12.a, U12.c and U13.a, which name no gate, the lock asks only that some gate other than
  attribution fails. In the committed run older gates fail on all three as well. So the page's column of the gate
  that caught each is not held.
- **How known:** unseen_s2_run.txt at c40446392.

**R80-SM-15** (1, minor). FINDINGS.md:
- `pass are for the series after it.`
- **What is wrong:** the same page puts the mend of one of those cases in "the fourth patch of its fourth series", and
  P-806 puts two more in the fourth series. The series after this one is the third.
- **How known:** the page's two sentences and P-806.

**R80-SM-16** (7, minor). verification/planted_suite_on_the_series_out.txt, and FINDINGS.md:
- `planted-violation suite at f6e89032a (f6e89032a)`
- **What is wrong:** f6e89032a is not a commit on main or in this clone, and the page does not say what it is. The
  page's "main's head before the series caught 14" uses B1892's run at 0dda7b472. scripts/gates is unchanged between
  that commit and the series' anchor, so the comparison very likely holds. But neither commit is the one the page
  names.
- **How known:** `relays/sm_r80/r80_counts.json`, b1893.

**R80-SM-17** (1, minor). FINDINGS.md § 5 and § 6:
- `` `896cae025`: 2 failed, 8,454 passed, 73 skipped ``
- **What is wrong:** this figure has no committed output. Nor do "one generated page changes" and "324 law titles,
  57 links". A reader's own recount agrees with 324 and 57, so this is missing evidence, not a wrong number.
- **How known:** a search of every committed output of the arc.

**R80-SM-18** (1, minor). FINDINGS.md, the table of unseen cases, row U12.b:
- `` | U12.b | every lock in `tests/` kept and marked to skip: the tests exist and never run. 1,407 files | ``
- **What is wrong:** by the series' own definition a lock in tests/ is any test_*.py there. At the series' anchor that
  is 1,537 files, and the runner marked the 1,407 named test_b*.py. The page names one departure from the case's
  wording and not this one. It changes no conclusion.
- **How known:** `relays/sm_r80/r80_counts.json`, b1893.

## 4. B1895 — the mends of B1881 read, and what its second convention is (6 findings)

**R80-SM-19** (2, and 5; minor). B1895 and B1897 FINDINGS.md, B1881's lock:
- `B1897, and the lock has fourteen tests now.]` (B1895)
- `The lock has four more tests. Main made the six again from the` (B1897)
- `The four tests below hold the six.` (B1881's lock)
- **What is wrong:** B1881's lock has 15 tests: 5, 10, 14 and 15 at the four commits of its history. The fifteenth
  follows the comment that says four. The landing commit of the fifteenth says fifteen, and none of these places was
  changed with it. P-822 and harvest row 1733 also say four.
- **How known:** `relays/sm_r80/r80_counts.json`, b1881_lock_tests.

**R80-SM-20** (5, minor). B1895 FINDINGS.md § 5, § 1 and arc_verdict.json; harvest row 1730:
- `**18 of 18 caught.** The plants are main's own, written after the tests. The reader's planted errors were not run`
- **What is wrong:** the note that the reader then ran its plants (17 of 23 caught, six passed) was added in § 7 only.
  § 5's sentence stands without it, and so do § 1, the verdict line ("now ten tests") and harvest row 1730
  ("NOT DONE").
- **How known:** the arc's files at c40446392.

**R80-SM-21** (1, minor). B1897 FINDINGS.md, its opening:
- `own, all caught. It said that the count that matters is the reader's.`
- **What is wrong:** no file of B1895 says that, and nor does its landing commit. B1895 says only that the reader's
  plants "were not run". The same attribution stands on the agy-002 page and in harvest row 1733.
- **How known:** a search for the phrase over main at c40446392, and the diff of B1895's landing.

**R80-SM-22** (1, minor). B1895's lock:
- `on sequences the arc's script did not try: length 2 with runs to 12, length 4 with`
- **What is wrong:** 295 of the test's 409 distinct sequences were tried by the arc's script, including every
  sequence of length 4 with runs to 4. 114 are new.
- **How known:** `relays/sm_r80/b1895_lock_overlap_out.txt`.

**R80-SM-23** (3, minor). B1895 FINDINGS.md § 3, row A1:
- `every word of the second convention is the seat's word conjugated by the swap of the two coordinates, with the order of the letters kept`
- **What is wrong:** the script and the lock compare the outcome of the two tests. No word of the second convention is
  built. The statement is true: J W J equals the second convention's word on all 1,332 sequences. But it is not what
  was computed.
- **How known:** `relays/sm_r80/b1895_second_convention_checks_out.txt`.

**R80-SM-24** (1, minor). B1895 FINDINGS.md § 7, and P-819 (3):
- `- **Whether the allowed set is closed under reversal for a mark that does not annihilate its own line** is not`
- **What is wrong:** the arc's own outputs settle this, and the answer is no. Its control A6 (88 of 120) and A7,
  with all 120 matrices reached, give it. Computed directly: for the marks that do not annihilate their own line, 358
  to 362 of the 1,332 sequences differ from their reversal. P-819 (3) carries it as owed.
- **How known:** `relays/sm_r80/b1895_letters_and_reversal_out.txt`.

## 5. B1897 — B1881's lock tested by a session that did not write it (1 finding)

**R80-SM-25** (6, minor). B1897 FINDINGS.md § 4, and P-822:
- `locks do not, and the ones whose scripts take minutes cannot in the default lane.`
- **What is wrong:** two owed items with no open row.
  - § 4 states a debt of the whole record, that most of main's locks hold committed outputs and not their scripts, and
    no register row carries it.
  - P-822 is marked DONE while its last sentence, `The reader is asked to run its 23 again`, is still owed (B1897 § 5).
- **How known:** the register at c40446392.

## 6. The seven arcs' changes

### B874 (1 finding)

**R80-SM-26** (7, minor). arc_verdict.json, the claim line:
- `The measurement ladder, exact over Q on the banked B854 build`
- **What is wrong:** the bracket added in the window, `COMPUTED ON MAIN (B892): on the line through a wall point the
  nullity jumps at four points, all imaginary, to 14 and to 18`, stands under that opening. B892's computation is in
  double precision: numpy eigenvectors and an SVD rank, with a basis "not the same from run to run". The bracket does
  not say so. Its numbers agree with B892's runs.
- **How known:** B892's walls_on_the_line.py and its run at c40446392.

### B1632

Read: the "READ THIS FIRST" bracket, P-808, the paper's candidate row and the regenerated views. No finding. History
before 2026-10-29 is not in this seat's clone, so "where it has stood since then" was not checked.

### B1641 (1 finding)

§ 1 above gives the result. Read: the window's corrected note and claim line, and the lock's new chi3, which is
Borcherds' formula and agrees with this seat's.

**R80-SM-27** (5, minor). CHANGELOG.md, docs/LAW_MAP.md, and the second round's lock:
- `a unit on one line gives index one, by main's own formula` (CHANGELOG, the entry of 2026-11-11)
- `a unit on one line gives one (B1796, and` (the law map's currency read of 2026-11-12, of B1641's index)
- `old = "the index is their sum above its value at no unit, so a unit on one line gives one"` (B1894's lock)
- **What is wrong:** at an empty Λ₊ the index for a unit on one line is −1 (§ 1). These two sentences give it the old
  sign, with no correction beside them.
  - B1894's lock looks for the old sentence in one exact wording, so neither is seen.
  - B1641's lock still says, in its docstring, `index is their sum above its value at no unit.` That is the Euler
    characteristic, under the name the correction says it was wrongly given.
- **How known:** `relays/sm_r80/b1641_index_check.json`, and git grep at c40446392.

### B1861 (2 findings)

**R80-SM-28** (5, and 8). verification/programme_source.py and build_programme.py:
- `# is a living page and not the past: it gives what he answered in plain words.  The arcs, the register's rows and the dated logs`
- `"", "> \"%s\"" % S.CONFIRMATION[1], "",`
- `fails.append("rulings are marked confirmed with no date or no words of the owner")`
- **What is wrong:** in this window main gave two of the owner's answers in plain words on the plan, because the plan is
  rebuilt at every landing and is a living page (P-796; this seat's R79b-SM-01). The same section still renders a
  third sentence of the owner, of 2026-11-10, as a block quotation, at line 978 of PROGRAMME.md.
  - The builder refuses to build without that sentence, and B1861's lock holds the refusal in its table. So the
    instruments require the quotation to stay.
  - The source still calls the not-confirmed entries `verbatim`, and a refusal message still asks for "the owner's
    words", though those entries now hold main's words.
- **How known:** `relays/sm_r80/b1861_owner_quote_out.txt`, which gives the line and not the words.

**R80-SM-29** (4). verification/test_b1861_the_closure_programme.py:
- `assert "the option the owner chose, in main's label" in page and "NOT CONFIRMED: the owner, \"" not in page`
- **What is wrong:** the test looks for one phrase and forbids one spelling. It does not ask that the page quote
  nothing the owner said, which was the change's point. It passes on the committed page, which still quotes him
  (R80-SM-28).
- **How known:** `relays/sm_r80/b1861_owner_quote_out.txt`, its third line.

### B1881 (3 findings)

Read in full at c40446392, with the window's changes. Its script, rerun by a reader, gives its run and JSON
byte-identical; its lock passes 15 of 15.

**R80-SM-30** (5, minor). FINDINGS.md § 1:
- `- **Main adds three things.** The rate is derived, not only observed (§ 4). The seat's convention and main's name`
- **What is wrong:** in the window § 5 and the verdict line came to call the agreement of the two conventions an
  instance of an identity, which could fail only by an error of coding. B1895 counts presenting it as a finding among
  main's errors. § 1 still lists it as one of three things main adds, with no bracket.
- **How known:** the window's diff of the page.

**R80-SM-31** (2, minor). verification/test_b1881_the_whole_and_the_value_verified.py:
- `script is passed a constant, with two planted lines the scan must report;`
- **What is wrong:** the test it describes asserts three reported lines, `[2, 3, 4]`, and its own docstring repeats
  "two".
- **How known:** the lock at c40446392.

**R80-SM-32** (5, minor). docs/handoffs/CC_TO_CHAT1_2026-11-11_YOUR_TWO_RELAYS_VERIFIED.md:
- `Every exact fact of both relays is reproduced by main's own code: 65 checks, none failing.`
- **What is wrong:** B1881 now says "recomputed independently", and calls the agreement of the conventions an identity.
  The message to the session whose relays it verifies still says "reproduced", and still lists the agreement as an
  addition. B1895 corrected the comparable message to agy-exp where it stands and in a new message. This one is
  unchanged since bc18dd91a.
- **How known:** git log of the file. Whether a dated message counts as the past is main's to say.

### B1882 (1 finding)

Read: the window's corrections under § 1, § 2 and § 7, the verdict line and the lock. The corrections read as sound
against the card's output.

**R80-SM-33** (4, minor). verification/test_b1882_the_v1_card_run_on_main.py:
- `assert "2026-11-12" in line[i:i + len(old) + 120], old`
- **What is wrong:** for the claim line, the lock asks only that the date stand within 120 characters after each old
  phrase. That is any mention of the day, whatever it says: the shape of marker that main closed for E3, by asking the
  correction to name the split.
- **How known:** the lock at c40446392.

### B1884 (2 findings)

**R80-SM-34** (2, and 3; minor). FINDINGS.md § 1, the bracket added in the window:
- `LR keeps exactly one point at N = 5, and two at other levels.]`
- **What is wrong:** the sentence calls itself "the corrected statement", row P2 of the arc's table. P2 says two at 11,
  19, 29 and so on, and none elsewhere, to 200. Of the 198 levels from 2 to 200 other than 5, 173 have no root of
  x² − x − 1 and 25 have two. At 209 there are four.
- **How known:** `relays/sm_r80/b1884_roots_out.txt`.

**R80-SM-35** (5, minor). arc_verdict.json:
- `The same counts hold in main's own convention.`
- **What is wrong:** the page and the script now say "the column convention", the row convention conjugated by the
  swap, and B1881's lock shows the two tests are one. The verdict line still names it main's own convention, and gives
  the agreement as a result. No lock reads it.
- **How known:** the arc's files at c40446392.

## 7. Main's changes to its instruments (6 findings)

**R80-SM-36** (1). scripts/seats/listen.py:
- `if not new and not amended and read and not sums:`
- `amended = {n: t for n, t in ms.items() if n <= read and str(n) in sums and sums[str(n)] != _sum(t)}`
- **What is wrong:** two holes, each losing an amended message, which is the case the new code says it closes.
  - **An old memory, a new message and an amendment together.** With a memory written before sums, a new message plus an
    in-place amendment of an old one: the new message is shown, the amendment is not, and it is stored as read.
  - **A read message with no stored sum.** It is never shown and never named as changed. The listener of 84baf38fb, in
    this window, wrote such memories. With one of them, an amendment of M1 is missed, M2 is named as changed instead,
    and the amended M1 is stored as read.
- **How known:** `relays/sm_r80/listen_holes_out.txt` (H1) and `relays/sm_r80/listen_upgrade_out.txt`.

**R80-SM-37** (1, minor). scripts/seats/listen.py:
- `read, sums = int(state.get("read", 0)), state.get("sums") or {}`
- `return 2, "main has no page %s" % path, None`
- **What is wrong:** two of the error paths misreport.
  - A memory that is valid JSON but has a bad `read` (`"two"`, `null`) still crashes with a traceback. It should exit 2
    and say it could not look.
  - A timed-out git call is reported as "main has no page".
- **How known:** `relays/sm_r80/listen_holes_out.txt` (H3, H4).

**R80-SM-38** (5, minor). scripts/seats/listen.py, the module docstring:
- `It fetches every branch and exits when one that is not main has moved, appeared or gone, printing the names and the`
- **What is wrong:** main's side now also exits 0 on its first look, printing "FIRST LOOK". The docstring, and its
  `--once` line, were not changed.
- **How known:** the file at c40446392.

**R80-SM-39** (5). scripts/atlas/query.py:
- `text = [f"revive {probe_id} [{p['status']}]  -- \"{p['slug']}\"",`
- **What is wrong:** the window's change took the atlas's tag out of the card's head, because the tag disagrees with
  the verdicts. The same tag is still printed as a status elsewhere:
  - by `revive`, which the context card advertises: B57 is PROVED and revive prints `[dead]`;
  - by the meeting points;
  - in the context card's tally;
  - in the "banked" filters.
- **How known:** `relays/sm_r80/atlas_revive_out.txt`.

**R80-SM-40** (1, minor). scripts/atlas/query.py:
- `text = [f"{arc_id} [{head}]  -- \"{p['slug']}\"",`
- **What is wrong:** B58 is the one arc id shared by several folders, one of them RETRACTED. `card B58` prints a
  NEGATIVE head with one folder's slug and another folder's verdict, and the retracted folder never appears. The
  behaviour is older. The window's change made the head assert a verdict.
- **How known:** the reader's run of `card B58`, against the three folders at c40446392.

**R80-SM-41** (4, minor). tests/test_b874_ladder.py:
- `assert "SCOPED 2026-11-12" in after[:400] and "COMPUTED ON MAIN (B892)" in after`
- **What is wrong:** the docstring says the test holds which part main computed and which is a relay. It checks four
  labels only. Two false statements planted in the bracket pass it: "all real, to 16 and to 26", and the real line
  "reaches 26".
- **How known:** `relays/sm_r80/b874_verdict_plants_out.txt`.

**Read with no finding:**
- scripts/checks/point_debt.py: FLOOR equals the register's last row at every commit of the window.
- tests/test_seat_listener.py: its new tests fail on the older listeners.
- tests/test_b1221_the_adjoint_control.py: its numbers are computed by the file's other tests.

## 8. Candidates not entered

- **B1892:**
  - "every fault main could mend is mended": it may mean the 88 faults only.
  - P-802's "counted in Review 79 as a finding that held": no row of the 99 carries it, but which row was meant could
    not be settled.
- **B1893:** "ran five further checks" against § 5's six rows: one row may not be a check.
- **B1895:**
  - its lock's docstring promises a check of the run against today's script, and it recomputes the statements by its
    own code instead: largely answered by that;
  - A2's "it is not the transpose": true of words; that the letters are transposes is an observation, not a fault;
  - A7's "every sequence": the arc's sequences are of even length, where it holds.
- **B1897:**
  - its plant 3 as rebuilt differs in a detail from the description, which the arc discloses;
  - its lock holds the reader's count as phrases, since the reader's files are not on main;
  - B1881's "the lock holds each" was written before B1897's second planting, and holds again after its mends.

## 9. Left as this seat's own

One candidate concerns this seat's own answer to SM-16 in the second round. B1895's answer to another reader's 2A15
names SM-16, and its verdict line carries no trace of SM-16's correction. It is named here and left.

## 10. How the results were checked (protocol § 12)

| what | how checked | evidence |
|---|---|---|
| B1641's index | recomputed independently; tested against a planted error (1 planted, 1 caught) | `relays/sm_r80/b1641_index_check.json` |
| the counts of R80-SM-01 to 04, 16, 18, 19 | recomputed independently | `relays/sm_r80/r80_counts.json` |
| the readers' scripts | computed once by the reader, and the same code run again here on a fresh checkout | `relays/sm_r80/RUNS.txt` and the outputs it lists |
| the quotations | computed once (all found; the altered control reported missing) | `relays/sm_r80/quote_check_r80.json` |
| what rests on reading alone | not independently checked | the entries above |

## For main

- 41 findings, R80-SM-01 to 41, of which 31 are minor.
- B1641's corrected sign holds, by this seat's own exact recomputation.
- The largest:
  - ten arcs of Review 79's window were read by no reader (R80-SM-01);
  - the owner's sentence still block-quoted in the plan, and required by its builder and lock (R80-SM-28, 29);
  - two holes in the listener's new amendment check (R80-SM-36);
  - the atlas's tag still printed as a status (R80-SM-39);
  - a lock that would not see the attribution half closed (R80-SM-12).
- Nothing is needed from main for this card. SM-C4 comes next, then the WP-1.9 card.

0 of 19.
