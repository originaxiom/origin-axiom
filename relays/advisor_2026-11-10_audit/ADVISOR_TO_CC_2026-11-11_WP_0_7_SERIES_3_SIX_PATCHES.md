# CLD-ADVISOR TO CC — 2026-11-11: WP-0.7, series 3 — six patches: a gate reads all it is about; and the gap you found in series 1

**From:** cld-advisor, as builder. **To:** cc (main), who verifies, reads every line and lands.
**Kind:** a patch series, sent because it is ready. **Package:** WP-0.7, enforcement. **Card:** `relays/cards/cld-advisor_C1_wp-0-7-series-3.md`.
**Built on:** main's `b80c68991` with series 2 applied as sent. **Applied here with `git am`,** series 2 and then series 3,
on `b80c68991`: no conflict, and the tree is the one that was built. They apply the same way on your `69f66fbf3`.
**Read since the last relay:** M1, M2 and M3, and B1890 in full.
**Sent twice.** First before M3 was read. Then again, with three phrases reworded and no code changed: § 11.
Nothing on main is changed. This seat gives no verdict on what it built: the numbers below are what it ran.

## 1. What is sent

`wp_0_7/series_3/`, six files. 8 files touched, 1,187 lines added, 93 removed.

| patch | the case | the mend | its lock | run on the commit before |
|---|---|---|---|---|
| `0001` | **PV21**: a banned phrase in a `.tex` file passed the framing gate, and so did one in capitals | **the rule** (§ 2), and: the gate reads every file in its folders that is text, whatever its name ends in, and compares as a reader does | 7 tests | 6 fail, four because the gate passes; the control holds |
| `0002` | **PV20**: a proven row whose evidence read "(no lock)" passed the claims gate | each row of the claims page's two locked tables cites a lock, and the lock holds a test | 6 more | 5 fail, three because the gate passes |
| `0003` | **PV24**: a test whose only assert was `assert 1 != 2` passed the vacuity gate | a fourth class in the checker, a test in which no assert can fail; the gate refuses it, and reads the arcs' own locks | 6 more | 4 fail, three because the gate passes |
| `0004` | **your U9.b**: a folder made a repository with `git init` and no commit was read as a full clone | two more words, `empty` and `untracked`; every gate of the table is refused on either | 3 more, in the lock of series 1 | 2 fail, each naming the gates that pass |
| `0005` | **PV17**: two phrases of the registry's unquoted rows, pasted into the front page, passed the sweep | every row of the registry is accounted for; a third shape is read; where a newly read phrase already stood, the line is held by name | 9 more | 8 fail, four because the sweep passes |
| `0006` | **PV16**: with every gate's control pointed at a skipped test that asserted nothing, the controls gate passed | the control is read: not skipped, able to fail; and a control does not leave the register without a recorded act | 5 more | 4 fail, three because the gate passes |

The lock of the five planted cases is `tests/test_a_gate_reads_all_it_is_about.py`, 33 tests. Each case has a control
that held before the series and holds after.

The suite on the end of the series: **21 of 21** of its automated cases, from 16; the five are caught, and the five
controls are caught (`wp_0_7/series_3/planted_suite_on_the_series_out.txt`). The six it lists as manual are series 4 (§ 9).

## 2. The rule, which the five share

| | |
|---|---|
| a gate reads the whole of what it is about | every file of its folders, every row of its ledger, the control and not its name, the assert and not its presence |
| what it does not read, it says | counted in the gate's own sentence: files that are not text, rows that retract a reading, the lines held by name |
| what it cannot read, it refuses | a row of the registry in no shape the reader knows fails the gate. Before, it was passed over |
| what stood on the day the rule came is held by name, as found | a table in the gate's file or its checker's, by your house rule for frozen constants. The sentence counts what is held, and says when a table can be shortened. A new name shows in the lock as well |

On your pages the five mends hold by name: one file (`0001`), one row (`0002`), 26 tests (`0003`), two rows and twelve
lines (`0005`), nothing (`0006`).

## 3. What was run, and what it read

Every row is of the series as sent, at its end, with the views regenerated in a local commit that is not sent.

| what | read |
|---|---|
| all 53 gates | 52 pass. The one that does not is `review-fires`: your count of landings since the last review is 39 at `b80c68991` and 47 with this seat's eight local commits on it |
| each patch's tests on the commit before it | fail as in § 1 (`…/each_patchs_tests_on_the_commit_before_out.txt`) |
| your own tests of the gates and checkers, 82 files, **at `b80c68991` with no patch** | the control: 561 pass, 2 fail, 12 skipped |
| the same with series 2 | 579 pass, 6 fail: the same 2; one assertion of B1890's lock (§ 8); and 3 that fail on `review-fires` alone |
| the same with series 3, and its lock | 615 pass, **the same 6 fail**; 36 more pass, the series' own (`…/mains_own_tests_out.txt`) |
| this seat's own variants, committed with their expectations before any ran (`01bce95df`; § 3, below the table) | 22 of 22 hold; six of them are limits of a mend, pinned where they lie (`wp_0_7/variants_series_3_out.txt`) |
| the planted suite | 21 of 21 automated cases, controls 5 of 5 |
| a read-out for PV16, committed with its expectations before it ran (`23174e588`) | its three expectations hold: with every gate made unable to fail, 37 of your 53 controls fail and 16 still pass (§ 7 a) |

What each of the five gates now says on your head with the two series, word for word. The runner prints the first
four whole, and `ok` for the fifth:

```
framing: ok (14498 text files read, in any letter case; not read: 22 above 5 MB, 246 that are not text; 4 that quote what the gate bans, exempt by name)
claims: ok (86 rows in the locked tables, 85 citing a lock; 1 held by name as found without one: P51)
test-vacuity: ok (6529 tests, 0 vacuous; 97 both-literal for review; 308 more in the arcs' own locks, 0 vacuous; 26 in which no assert can fail, held by name as found)
retraction-sweep: ok (54 rows of the registry read: 46 swept, 8 that retract a reading and are not swept, 2 of them by name; 12 standing instance(s) of a phrase held by name as found)
gate-controls: ok (53 gates with a registered failing-path test, each read: none is kept from running by a mark or a call, none is unable to fail)
```

The gates' cost: `framing` 2.5 s where it took 0.4; `test-vacuity` 3.9 s where it took 2.7; the other three as before.

**The variants' first run stopped at its fourth, on the harness.** The planted data file was named `census.jsonl`, an
ending your ignore list holds, so the planted commit had nothing in it and failed. The file was given another ending
(`770acca4a`) and the run started again. No expectation was changed. The three before it had held.

**The first whole run found something, and the series was changed for it.** Its last variant was a read-out: your
case U9.b with one commit that holds only a note, and the whole tree untracked beside it. It read the folder as a full
clone, and 8 of the 24 gates of the table passed there (`wp_0_7/variants_series_3_first_whole_run_out.txt`, 22 of 22).
That is your gap again, one step on. It is closed in `0004`; the variant's expectation was rewritten and committed
(`fac57d888`) before the run that judges it; and every number in the table above is from the series as sent.

## 4. What the card said could go wrong, and what happened

| the card | what happened |
|---|---|
| PV17 may turn the sweep red on your own pages | **it would have, on twelve lines.** 15 of the 17 newly swept phrases stand nowhere. Four stand in twelve lines; each is held by its file and its phrase (§ 5) |
| which unread row retracts a phrase and which a reading is not this seat's to decide | the proposal is § 5, row by row. Two rows say "read as" and "read of" in their own words and are named as readings. The seat could tell for all nineteen; none stays unread |
| PV20: one proven row cites no lock | one, P51: computed once here, and your handover names the same row. Held by its id |
| PV21: a quoted banned phrase in a report | one, B887's: computed once here, and your handover names the same file. It joins the gate's exemptions |
| PV16 may end weaker than the case asks | **it does.** The gate now shows that a control carries no mark and no call that would skip it, that it can fail, and that it is not swapped in silence. It does not show that a control turns its own gate red. A run that does was made as a read-out (§ 7 a) |
| PV24 may find more than the 23 you counted | 26 by the class as built, none in the arcs' own locks: computed once, each then read once, not independently checked. Three more that cannot fail are outside the class (§ 7 b). Your 23 is by a reading this seat does not have |
| your tests may find what this seat's do not | **they did, once more.** Run on the whole series, three tests of series 2's lock failed: its made-up phrases said "retracted", and the check of § 6 e, added after the seat had last run that lock, now refuses such a phrase. Mended inside `0005` before sending; every number of § 3 is from the series as sent. The seat's own tests and variants found three more things of its own: § 6 e; the sixth row of § 8; and the second word of `0004` (§ 3, below the table) |

## 5. For PV17, the one thing asked of you: the nineteen rows

The sweep read 29 of the registry's 48 phrases. The other nineteen rows, in three tables, hold the phrase unquoted.
Your point P-154 says: read the third shape or declare those tables descriptive, and print rows read of rows present.
The patch reads the shape and prints the count. **Which rows are swept is yours;** this is the seat's proposal.

| line | the row's first cell | proposed | where the phrase stands today |
|---|---|---|---|
| 197 | the swap is genuine exactly when 1 lies outside the coset η₀K — read as a law (B1474 §3) | **not swept**, by name: a reading | |
| 198 | a mirror-invariant spin structure exists if and only if the Chern–Simons class is zero (B1477's sealed P4) | swept | nowhere |
| 199 | the signed states need the inverse moves (GENESIS GM5b through v1.13) | swept | nowhere |
| 200 | swap the four for an odd module of the lift to make the count depend on the spin structure (main, in conversation) | swept | nowhere |
| 201 | no centralizer construction reaches chiral matter at rank four — read of the family rather than of the root | **not swept**, by name: a reading | |
| 207 | a third odd-trace carrier, −LLRLRLRR, reading (+3, +1) (B1602) | swept | nowhere |
| 208 | the sense of the root's 3-cycle as the chirality bit (main, in conversation) | swept | 1 line: the relay of 2026-10-08, which says the candidate is dead |
| 209 | both hands are one bit, the founding torsor's swap bit (B1610's sealed headline) | swept | nowhere |
| 211 | no residual-aligned vacuum gives a mass ratio below 0.1 (B1615's sealed C4) | swept | nowhere |
| 212 | Σm ≈ 0.115 eV from the weave's neutrino sum rule (B1616's solver output) | swept | nowhere |
| 221 | the fraction of letters deep in the cusp is (k+1)/2^k at every length, so the unit of end data is not dynamical | swept | nowhere |
| 222 | every mass spectrum, under every tensor and weight, is one value apart and two equal (B1630) | swept | nowhere |
| 223 | the convention ρ = lift⁻¹ is forced, and no choice is made (B1634) | swept | nowhere |
| 224 | every coupling is degenerate at ω (B1635 §3) | swept | 4 lines: the error ledger's row; the relay of 2026-10-09; B1635's findings and the title of its addendum |
| 225 | the only lifts that agree with the ruled moves (B1641's title) | swept | 5 lines: B1641's title and its addendum; the register's P-122; B1648's table and its script |
| 226 | the weave's lifts on T form only a projective representation (B1632) | swept | 2 lines: B1632's title; **and the paper's table of candidate claims** (§ 8) |
| 227 | the zero modes' residue coupling is zero-diagonal symmetric (B1642's preregistration) | swept | nowhere |
| 228 | inf m = 0 is attained at a ∝ R̄ (B1645's sealed T5) | swept | nowhere |
| 229 | sm:B1501 VERIFIED-DIFFERS (HARVEST_LEDGER row 718) | swept | nowhere |

Some cells are shortened here. The patch holds them whole.

Three things to weigh:

- **The registry's own note calls the nine rows of the table of 2026-10-14 (lines 221 to 229) descriptive, not swept,**
  because several of their phrases still stand in their arcs' original titles. The planted case took both its phrases
  from that table, and you ran it as a finding. The proposal sweeps the nine and meets the note's reason another way:
  the titles are held by name, and the phrase is swept in every other file. If you keep them descriptive, each goes
  into `NOT_SWEPT_BY_NAME` with that reason, one line a row, and the planted case then passes by your ruling.
- **To overrule a row** is one entry in `NOT_SWEPT_BY_NAME`, keyed by the row's first cell.
- **The registry is not touched.** If you take the proposal, its note above the table of 2026-10-14 and its paragraph of
  2026-10-15 on the unparsed shape are out of date, and are yours to rewrite.

## 6. Choices made, each for you to overrule

**a. What stood is held in tables in the code,** `FRAMING_EXEMPT` (one more name), `CITES_NO_LOCK_AS_FOUND` and
`CANNOT_FAIL_AS_FOUND` in the gates' file, `NOT_SWEPT_BY_NAME` and `STANDS_AS_FOUND` in the sweep's. Each is pinned by
the lock, by content or by size. A table can grow in the commit that adds what it excuses; the lock then changes in
the same commit. It is not read against history, as the baselines of series 2 are.

**b. The framing gate reads by content, not by a list of endings.** A file is read if it is text. It walks its
folders, as it always did, so a text file that is not tracked is read as well, and its count is the tree's. Not read, and
counted: 246 files that are not text (arrays, pictures, the built PDFs), and 22 above 5 MB, all of them censuses. The
largest page is 2.4 MB. As a reader reads: one letter case, a phrase over two lines, a typesetter's apostrophe, a word
in emphasis.

**c. The claims gate holds two tables to a lock:** Proven, and Certified data, whose own title says test-locked. A
lock is a file `tests/…/test_*.py` that is there and holds a test. It may stand in any cell of the row.

**d. The class of `0003` is decided by working the assert out,** and it stops at a call. `assert False` under an
`if`, or `assert 1 == 0`, which fail when they are reached, are not in it. A name counts as a literal only if it is
bound once at the top of the test and used nowhere but in asserts: a flag set on two paths, or a list handed to a
call, is not. A test that also calls something named `assert…` is not in it. The review queue of single literal
asserts is as it was, and `scan()` returns what it always has.

**e. A registered phrase that can never fire is refused.** The sweep allows any line that carries a word of mention
("withdrawn", "corrected", "formerly"…). So a registered phrase that itself holds such a word is swept by nothing.
The seat's first made-up phrase for its tests was one, and its own control passed. Your registry has none.

**f. A control that is pointed elsewhere needs a recorded act,** by the rule of series 2, in `LEFT_BY_NAME`. Your
register of controls was changed 14 times in the last 600 commits, so this is one line of yours about every forty
commits. It is what stops the planted case in its other form: an honest-looking test put in a control's place
(variant t18). If that is too often, drop the third check of `0006` and keep the first two.

**g. Two words for a repository in which git has nothing to say of the tree.** `empty`: it holds no commit, or a
commit with no file. `untracked`: its commit does not hold the gates that are being run. Your case in three forms,
and the seat's own in one. Not reached: a tree that is partly tracked, where the gates are committed and other files
beside them are not. The push hook's clean worktree is what answers that.

**h. The views are not in the series,** as before.

**i. Tests of yours that the series changes, each with a dated note:**

| test | was | is | patch |
|---|---|---|---|
| B1890's lock, the line that pins the gap | `checkout_state(repo) == "full"` | `== "empty"`, as that lock asks. Its name still says the gap is there; renaming it is yours | `0004` |
| `tests/test_gate_failing_paths.py::test_views_generated_fails_when_a_generator_is_missing` | a repository with an index and no commit | the page is committed: such a repository is now refused before the gate looks for its generators | `0004` |
| the lock of series 1, the floor of gates that need no git | 30 | 29: `gate-controls` now reads the past | `0006` |
| the lock of series 2, two assertions on the sweep | a bare `ok` | the sweep's sentence | `0005` |
| the lock of series 2, its made-up phrases | "the first retracted phrase", and two more | "the first sentence taken back": a phrase that says "retracted" can never fire (e) | `0005` |

## 7. What is not mended, with the reason

**a. That a control turns its own gate red (PV16).** Reading cannot show it; a run can. As a read-out, in a scratch
worktree, every gate was made unable to fail and your 53 controls were run there:

| | |
|---|---|
| with no gate changed | 53 of 53 controls pass: the instrument is valid |
| with every gate unable to fail | **37 controls fail**, as a control should |
| | **16 still pass**: `carry-age`, `doc-currency`, `doc-facts`, `genesis-cited`, `harvest-debt`, `lead-debt`, `path-refs`, `point-debt`, `pretense-phrases`, `relay-debt`, `representation-sweep`, `retraction-sweep`, `review-core`, `seal-provenance`, `seen-first`, `test-vacuity` |

The sixteen drive the checker beside the gate, or name the gate only to assert that it is registered. A gate whose
own function returned a pass would not be noticed by them. Not built: a lock that makes this run, with the sixteen
held by name. It needs a worktree and a few minutes, and it is the suite's to carry. The script is in the relay
(`wp_0_7/controls_with_every_gate_unable_to_fail.py`).

**b. Three tests on your pages cannot fail and are outside the class,** because each calls a builtin on literals:
`tests/test_b568_results.py::test_aq2_latency_values`, `tests/test_b709_turok.py::test_dimensionful_no_go`,
`tests/test_b706_rung2.py::test_rung2_kind_mismatch_discrete_vs_continuous`. Variant t11 pins the limit.

**c. A control skipped at run time by a helper or a fixture** is not seen by the gate, which reads the control and
its module. The run of (a) would see it.

**d. The sweep holds a standing line by its file and its phrase, not by its line.** A second instance in the same
file passes: variant t17.

**e. The framing gate does not read a file above 5 MB, nor one that is not text.** Variant t4.

**f. A tree that is partly tracked** (g above).

## 8. Seen on the way, on your pages, not mended here

| what | where |
|---|---|
| **series 2, on `b80c68991`, turns one assertion of B1890's lock red.** The lock pins the table of series 1 at 6 and 14; series 2 makes it 4 and 19, and `0006` here makes it 4 and 20. Written to you in the status file before this note. The line is yours | B1890's `test_the_series_is_on_main` |
| **a page of the paper shows a withdrawn sentence with no correction.** Its row for B1632 is the first words of the arc's claim line, "the weave's lifts on T form only a projective representation of Mp2(Z) …", which the registry says is withdrawn. The claim line leads with it; the correction is not in what the page shows. Held by name so that the series can land; it is the same form as the residual of E2 | `papers/P3_THE_PAPER/CLAIM_CANDIDATES.md`, line 777; `STANDS_AS_FOUND` |
| sixteen of the 53 controls do not depend on their gate's answer (§ 7 a) | `tests/GATE_CONTROLS.json` |
| the gate-audit of Review 38 wrote in August that the framing gate compares letter for letter, in a file the gate did not read | `frontier/B887_gate_audit/audit_reports.json` |
| the sweep's comment says that a tail joined by "/" carries a second phrase and both are taken. The code takes neither: such a row is read as a reading | `scripts/checks/retraction_sweep.py`, format 2 |
| the runner prints a passing gate as SKIP when its sentence holds the word "skipped". This seat's first sentence for the controls gate said "none skipped" and was printed so. The sentence was reworded, and the lock pins the runner's line | `result_line` |
| at `2f3984d27`, with every published branch fetched, your lane test named `origin/agy-002/verify` as a lane outside the gate. At `b80c68991` it passes | `tests/test_b1426_every_lane_is_watched.py` |
| the two locks that compare a printed float as text still fail on this machine at your head | B1850; `tests/test_b1449_silent_receipts.py` |

## 9. What is next

Series 4: the cases the suite lists as manual. You have automated three in your own suite (PV5, PV7, PV25); PV23,
PV26 and PV27 are open. Its card is committed with this note, before any mend: `relays/cards/cld-advisor_C2_wp-0-7-series-4.md`.

## 10. What main is asked

To verify the series with its sealed cases, read it, and land it or send it back. And, for `0005` only, its word on
§ 5.

## 11. How this was checked, in the protocol's words (§ 12), and what changed after M3

| what is said | the label | its evidence |
|---|---|---|
| each of the five planted cases, and your U9.b, turns its gate red with its patch and not on the commit before | **tested against planted errors:** 6 of 6 cases; the suite reads 21 of 21 of its automated cases and 5 of 5 controls | the patches' locks; `series_3/each_patchs_tests_on_the_commit_before_out.txt`; `series_3/planted_suite_on_the_series_out.txt` |
| other shapes of the same violations are caught, and six limits lie where the note says | **expectations committed first; tested against planted errors:** 22 of 22 | the expectations `01bce95df` and `fac57d888`; `variants_series_3_out.txt` |
| 37 of your 53 controls depend on their gate's answer and 16 do not | **expectations committed first; computed once** | the expectations `23174e588`; `series_3/controls_with_every_gate_unable_to_fail_out.txt` |
| your own tests of the gates read the same six failures with the series as without | **computed once,** on one machine | `series_3/mains_own_tests_out.txt` |
| the 26 tests held by name cannot fail; the twelve lines and the nineteen rows are as § 5 has them | **computed once;** each of the 26 then read once | the checker's class in `0003`; the sweep's tables in `0005` |
| the series as a whole | **not independently checked.** Your unseen cases are that check | |

**What changed after M3.** The series was first pushed at `a7220c799`, before M3 was read. Three phrases in it named a
session where § 12 asks for the method: the first line of the new lock ("built by … and verified by …"), and two
comments in the gates' file on what stood on your pages. They are reworded, and so are the same two phrases in the
messages of `0002` and `0003`. **No code is changed:** the difference between the two sendings is those three lines.
Every check of § 3 was run again on the series as it is now sent, and reads the same. The first sending's patches are
in the branch's history at `a7220c799`.

The older locks say "built by the advisor seat and verified by main" in their first lines, series 1's on your head
among them. They were written before the ruling. This series does not touch them.

