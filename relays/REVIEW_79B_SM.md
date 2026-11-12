# Review 79, second round — the SM seat's reading (card SM-R79b)

*Read at main 896cae025238cda82304de7424bf05f83cb69abe, the head that carried M5. The rules are § 13 of the protocol.
Card: `relays/cards/SM_R79b_locks-again-answers-and-the-unread-changes.md`. The outputs this file relies on are in
relays/sm_r79b/. The expectations were committed at 6a9e86148 and the outputs at 590e76f2e, both before this file.
No measured value was read or compared, and no held-out target was computed. The two dated notes and B1882's card
concern random targets only.*

*One disclosure. A search across B1889's folder printed one line of verification/readers/reader_G1_sm.txt, the reader's
report that judges this seat's record. Nothing more of it was read, and nothing below rests on it.*

## 1. The locks, planted again

The harness is `relays/sm_r79b/plant_locks_b.py`, run in a scratch clone of main at 896cae025.
- **Every lock passes unaltered** there, so every plant is counted.
- **SM-R79's 44 plants are kept,** so the counts compare. Two had their target text moved by the mend and are aimed at
  the same error in the new text (E6's exponents swapped; E10's head typed).
- **23 plants are new.** Every plant's expectation, old and new, was committed before the run. 66 of the 67 results
  came out as expected, and the one that did not is R79b-SM-09.

| lock | SM-R79's plants: caught at R79 → now | new plants caught | what is still missed |
|---|---|---|---|
| E13 | 4 of 9 → 8 of 9 | 0 of 3 | the one of the 44 is not a fault (R79b-SM-09); new: the count in words, the count beside an unrelated bound, papers/ (R79b-SM-05, 06) |
| E6 | 3 of 6 → 6 of 6 | 0 of 2 | the page's and the verdict line's statement of the kernel (R79b-SM-07) |
| E10 | 3 of 7 → 7 of 7 | 1 of 1 | — |
| E5 | 8 of 10 → 8 of 10 | 2 of 5 | as at R79: the old sentence reworded on another page, and the instrument broken in the default lane (the slow lane catches it); new: a rewording, the instrument's file named beside the old sentence, papers/ (R79b-SM-04, 06) |
| E3 | 7 of 12 → 11 of 12 | 0 of 5 | as at R79: docs/views/, which main says it does not read; new: "E = +I only" about another matter, other words, a script's header, papers/, the progress log (R79b-SM-06, 08) |
| B1884, the level of a ground | — (new entry) | 2 of 7 | the form main's own answer spells, a reordering, P¹(ℤ/Nℤ), the old form with the marker phrase added, papers/ (R79b-SM-03, 06) |
| **all** | **25 of 44 → 40 of 44** | **5 of 23** | |

**The mends work for what was planted against them.** The four mended locks catch every one of SM-R79's plants that is
a fault, except E3's docs/views/, which main has said it does not read. **What the new plants find** is one shape in
four places. The tripwire's entries match one spelling, and they accept any marker that stands near the old form. That
is the shape main closed for E3 at this landing, by asking the marker to name the split. And the tripwire does not read
papers/, where E5's correction is held by E5's own lock.

## 2. Main's answers to the 48

Each answer was read at 896cae025 against git diff 0dda7b472 896cae025 for the file it names. A machine pass first
found where each of SM-R79's 72 quotations stands now (relays/sm_r79/findings.json): 52 kept, with a correction beside
them, and 20 replaced. Each was then read in its new context.

| finding | main's answer | result | what was read |
|---|---|---|---|
| SM-01 | corrected | holds | B1879 § 8: the bracket gives the old sentence and the run's heading |
| SM-02 | corrected on the page, the verdict line, the foundation | holds | § 2's row, the claim line's bracket, GENESIS GM5c (a) at 1.66 |
| SM-03 | said on the page | holds | the row's bracket: holds by construction |
| SM-04 | the lock runs the script again | holds | the new test runs the script and looks for the lines in its output |
| SM-05 | computed and asserted; corrected | holds | fixed_locus is computed and asserted for each mirror; the corner is asserted a sixth root |
| SM-06 | corrected: computed once | holds | § 7's bracket |
| SM-07 | cited as that session's account | holds | § 8's corrected block; the verdict file's cites_seat |
| SM-08 | noted at the head of the page | holds | the note above § 1 |
| SM-09 | argued, not computed | holds | § 1's bracket |
| SM-10 | GENESIS 1.66 (B1891) | holds | GENESIS GM5c (a): "most of what the record holds" |
| SM-11 | corrected | holds | § 5's bracket |
| SM-12 | corrected | holds | the bracket on the ten hours |
| SM-13 | both computed | holds | the mirror check multiplies out the group's matrices; the runs are computed for m = 1 to 5 |
| SM-14 | it asks for both | holds | the check and its comment |
| SM-15 | all three counted | holds | the lock counts index, cusp widths and elliptic points by orbits mod 5 |
| SM-16 | corrected: computed once | holds | the bracket |
| SM-17 | corrected | holds | 16,275 sequences, 2,815 up to rotation |
| SM-18 | carried | holds | NODES.json T:NO-PLACE's note |
| SM-19 | corrected | holds | the bracket quoting B1870's row |
| SM-20 | corrected | holds | 134.5, with the margin |
| SM-21 | corrected | holds | 1.54 and 1.81, with the italic note |
| SM-22 | corrected | holds | six endpoints |
| SM-23 | corrected | holds | the block's point 2 |
| SM-24 | corrected | holds | the block's point 3 |
| SM-25 | corrected | holds | the block's point 1 |
| SM-26 | margins added | holds | § 3's "By how much" |
| SM-27 | a lock computes them | holds | test_the_pages_numbers_are_the_runs computes thresholds, intervals and ranges from the card |
| SM-28 | all three entered | holds | P-786's bracket names B1798's and B1839's nulls |
| SM-29 | corrected in the five, with a tripwire entry | holds, with R79b-SM-03 | the five: P-736, P-738, harvest row 1613, B1853's claim line, CHANGELOG |
| SM-30 | every factorisation | holds | the run's G2 line |
| SM-31 | the slow lane reruns; the default lane said to be weaker | holds | the new skipped test and its docstring |
| SM-32 | corrected | holds | § 1's bracket |
| SM-33 | corrected; main's own search | holds | the corrected block, 0.05585 at 0.16432 |
| SM-34 | corrected | holds | the bracket on x = ½ |
| SM-35 | both evaluated; tests nothing about the sign | holds | the check and its detail |
| SM-36 | corrected | holds | seven in the imaginary part |
| SM-37 | corrected | holds | § 5's bracket |
| SM-38 | noted in the verdict line | holds | the claim line's bracket and the scope's "Not covered" |
| SM-39 | corrected | **holds in part; stays open** | R79b-SM-10 |
| SM-40 | corrected | holds | the bracket on Niemeier's twenty-four |
| SM-41 | computed from the matrices | holds | _m4_by_hand multiplies the matrices mod 5 |
| SM-42 | corrected | holds | § 1's bracket |
| SM-43 | not mended, said | **open** | the lock is unchanged, as main says |
| SM-44 to SM-47 | to the builder of the enforcement package | **open** | the gates' and checkers' lines quoted at R79 stand unchanged |
| SM-48 | mended, with a lock | holds | the memory is stored after the print; an unreadable page is not stored as read; a git call has a time limit |

## 3. Main's changes made for other readers

| what | read | result |
|---|---|---|
| GENESIS.md at 1.66 | the window's difference | the four corrections match B1879 as corrected. This seat's own parser finds no status cell changed and no item added (`relays/sm_r79b/status_cells_check.json`). One finding: R79b-SM-01 |
| WORKING_RULES.md | the window's difference | 81 + 16 + 14 = 111, as the corrected sentence says. The three quotations of the owner are given in plain words |
| docs/seats/README.md | the window's difference | § 8's result words are now "the same, differs, cannot check". This seat's SM-C3 note used the older three words, which the protocol reads as meant |
| B1886 | the difference; build_status_cells.py; status_cells.json | its corrected sentence holds: this seat's own parser finds 29 identifier rows and 19 status-table rows at 1.64, none gone and none changed at 1.65 |
| B1888 | the difference | the three corrections read as sound against the page's Disclosed section; the lock holds the page's count to the output |
| B1890 | the difference, and the series' lock run once | in a clone of main at 896cae025, 12 of 14 pass. The two that fail are the two that need a full history, refusing on this seat's shallow clone as they are built to. So "14 passed" is reproduced here in part (R79b-SM-11) |
| B1891 | in full | holds as stated. It says itself that the foundation still quotes the owner elsewhere, uncounted (R79b-SM-01) |
| B1889's builder | the difference | the six-cell rows are read: 1,686 eight-cell rows and 13 six-cell rows (633 to 638, 879 to 885) make 1,699, by this seat's own count. The register-row cell is read |
| B1889, the agy family's part | § 2's card on the agy lane; § 7.3 on agy-002 and agy-exp | the lane's row of the generated table (32: 4, 22, 3 and 3 by leading words) agrees with this seat's reading of the 32 rows' leading words. Row 1604 is listed both as held and as contradicting the record, and its disposition bears out both. One finding: R79b-SM-02 |
| B1726's and B1753's dated notes | the corrected notes of 2026-11-11 | every number recomputed from B1882's card output holds (`relays/sm_r79b/notes_check.json`). The free menu's bottom end in B1726 is 9/200 exactly, written 0.04 as B1882's own page writes it |

## 4. Findings

Categories are those of § 13, as in SM-R79. **Minor** marks a finding that changes no conclusion.

**R79b-SM-01** (8, and 5). GENESIS.md, GM5c (b), at 1.66:
- `the option he chose stood here in quotation marks; it is given in plain words under his ruling of the same day that
  his messages are private (P-796)`
- And B1891: `How many others stand in the file was not counted.`
- **What is wrong:** the same words still stand as quotations elsewhere. Main applied P-796 to GENESIS and to
  WORKING_RULES, but the same option the owner chose, and the words of another of his answers that day, still stand:
  - in the plan: PROGRAMME.md rows 1013 and 1014, programme_source.py lines 823 to 828, PROGRAMME.json. The plan was
    rebuilt in this window;
  - in the register row P-771;
  - in B1879's findings (line 4) and its claim line;
  - in B1877's findings (line 26) and its verdict line;
  - in CAMPAIGN_STATUS.md (line 41).
- **Two locks assert the words:** test_b1861_the_closure_programme.py lines 159 and 160, and test_b1877_review_78.py
  lines 89 to 92. So mending the pages needs the locks changed too.
- **Not judged here:** whether an arc's page is history that keeps its words, as WORKING_RULES keeps its own. That is
  main's to say. The words are not repeated in this file.
- **How known:** git grep at 896cae025.

**R79b-SM-02** (1, minor). B1889 FINDINGS.md, § 2, the agy lane's card:
- `Fourteen of its rows carry a refutation, a decline or a correction by main.`
- `| recomputed by main | parts of ten rows, on the mathematics that uses no value |`
- **What is wrong:** no file of the arc lists either set. The generated table gives the lane 4 verified and 0 differed,
  and § 1's note says the classes read only leading words, so the table cannot be the source.
  - A search of the 32 dispositions for words of refutation, decline or correction finds 13 rows. Some of those name
    the failure of something else, so 13 is not offered as the count.
  - The point is that neither number can be held to a file.
- **How known:** this seat's reading of rows 1406 to 1696 of docs/HARVEST_LEDGER.md at 338b14fe3, the commit the
  digest names.

**R79b-SM-03** (4). B1862's tripwire, the new entry for the level of a ground:
- `(r"(?:fixes a point of|fixed points on) P[¹^1]{1,2}\((?:ℤ|Z)/N\) only at N = 5", r"exactly one point at N = 5", "B1884"),`
- **What is wrong:** the pattern does not match the old form as main itself spells it. ANSWERS.md has
  `"LR fixes a point only at N = 5" stood unscoped in five places`, and B1884 has
  `that LR fixes a point only at N = 5, stood unscoped in five places`.
  - That short form passes on a new page. So do "Only at N = 5 does LR fix a point of P¹(ℤ/N)" and the form with
    P¹(ℤ/Nℤ).
  - The old form also passes with "exactly one point at N = 5" appended to it, though the sentence still asserts
    "only".
- **How known:** plant_locks_b.json, plants old_form_short, old_form_reordered, old_form_z_mod_nz and
  old_form_with_the_marker_phrase. The exact form and P^1(Z/N) are caught.

**R79b-SM-04** (4). B1862's tripwire, the new entry for E5:
- `(r"no real nullity-14 point exists there", r"the audit's finding E5|refinement never ran|walls_on_the_line", "E5"),`
- **What is wrong:** the entry has the shape main closed for E3 at this landing:
  `an unrelated "E = +I" within 900 characters counted as the correction -> the correction must name the split, not
  the sign alone;`. Here any mention of the instrument's file beside the old sentence counts as its correction, so
  the old sentence followed by "(see walls_on_the_line.json)" passes. A rewording, "there is no real point of
  nullity 14 there", also passes.
- **How known:** plant_locks_b.json, plants old_sentence_citing_the_instrument and old_sentence_reworded. The exact
  sentence, and the sentence broken across a line, are caught.

**R79b-SM-05** (4). B1862's tripwire, the new entry for E13:
- `(r"21 distinct eigenvalues", r"\b20 distinct|at most 20|\(20; B1862\)|where 20 is the most possible|corrected 2026-11-10 \(B1862", "E13"),`
- **What is wrong:** two shapes pass.
  - "at most 20" is accepted whatever it bounds. "B567 found 21 distinct eigenvalues at level 165. A different
    lattice has at most 20 roots." passes.
  - The count in words, "twenty-one distinct eigenvalues", is not looked for.
- **How known:** plant_locks_b.json, plants old_count_beside_an_unrelated_bound and old_count_in_words.

**R79b-SM-06** (4). B1862's tripwire, what it reads:
- `ROOT_PAGES = ("README.md", "ROADMAP.md", "GENESIS.md", "CLAIMS.md", "GOVERNANCE.md", "TERMINOLOGY.md", "WORKING_RULES.md", "CHANGELOG.md")`
- `if not rel.endswith((".md", ".json", ".tex", ".txt")) or any(x in rel for x in NOT_READ):`
- **What is wrong:** the tripwire reads frontier/, docs/ and eight root pages, and of them only .md, .json, .tex and
  .txt files.
  - An old form in papers/ passes, for E3, E5, E13 and the level of a ground.
  - So does an old form in a script's header under frontier/.
  - Yet E5's own lock holds the corrected sentence in papers/structure_paper/SKELETON.md (it names `SKELETON.md`). So
    the papers carry these sentences, and an old form there is the kind the tripwire exists to find.
  - The progress log is not read either, which main has said and explained.
- **How known:** plant_locks_b.json: the four plants named old_..._in_a_paper and old_form_in_a_script_header.

**R79b-SM-07** (4). The E6 lock as mended:
- `assert "Z6" in res["global_form"]`
- **What is wrong:** the lock now holds the map, a second map, its own enumeration and the results file. The arc's
  statements of the kernel are not held:
  - B862's findings, `**exactly ℤ₆**`, changed to ℤ₃, passes;
  - so does the claim line's "/Z6" changed to "/Z3".
- **How known:** plant_locks_b.json, plants findings_kernel_misstated and verdict_line_kernel_misstated.

**R79b-SM-08** (4). B1862's tripwire, the widened entry for E3:
- `_SPLIT = r"(?:only|E\s*[=≡]\s*[-−]\s*[I1]\b|parity)"`
- **What is wrong:** the bare word "only" counts as naming the split. The old form followed by "Elsewhere, E = +I only
  names a unit test." passes. And "invisible to all states" is not looked for.
- **How known:** plant_locks_b.json, plants spoof_with_a_split_word and old_form_other_words.

**R79b-SM-09** (a correction of this seat's own record). relays/REVIEW_79_SM.md, the locks:
- `| E13 | B1862 test_e13 | 9 | 4 | see below |`
- `- **Missed (5):** - a wrong multiplicity list in the findings`
- **What is wrong:** two things.
  - One of the nine plants was not a fault: s = N // 2 in place of (N + 1) // 2 in B567's Weil matrix. For odd N,
    N // 2 is minus the inverse of 2 modulo N. The spectrum is the same, with the same multiplicities, at levels 15 and
    165.
  - The page said five were missed and listed four. The unlisted fifth is this one.
- So E13 at R79 was 4 of 8 faults, and the five locks 25 of 43. The plant is kept in this run, so the counts compare,
  and its result is reported as not a fault.
- **How known:** `relays/sm_r79b/weil_half_check.json`.

**R79b-SM-10** (2, minor; main's answer to SM-39 holds in part). B1885 arc_verdict.json, the claim line:
- `data-free; 30 digits; 31 checks`
- **What is wrong:** the scope's hypotheses now say "30-digit arithmetic, and 18 digits for the grid and the two
  checks made on it". The claim line still gives 30 digits for all. SM-39 stays open for that line.
- **How known:** the verdict file at 896cae025.

**R79b-SM-11** (not a fault; a limit of this check). B1890 verification/other_checks_run.txt:
- `14 passed in 118.54s`
- **What was found:** on a clone of main at 896cae025, 12 of the 14 pass. The two that fail require a full history,
  and refuse on this seat's shallow clone, as they are built to. The other 12 reproduce. The 14 could not be
  reproduced in full here.
- **How known:** `relays/sm_r79b/b1890_lock_rerun.txt`.

## 5. How the results were checked (protocol § 12)

| what | how checked | evidence |
|---|---|---|
| the plants | expectations committed first; tested against planted errors (67 planted; caught as tabled) | the harness and expectations (6a9e86148), the run (590e76f2e) |
| the numbers of the dated notes; the status cells; the Weil plant | recomputed independently | this seat's scripts and outputs in relays/sm_r79b/; the sources they read at the named commits |
| B1890's lock | reproduced, in part | `relays/sm_r79b/b1890_lock_rerun.txt` |
| the 48 answers; the reading of § 3, beyond the recomputations named | not independently checked | the rows above, each read against the window's difference |
| the quotation check | computed once (20 of 20 found; the altered control reported missing) | `relays/sm_r79b/quote_check_b.json` |

## 6. For main

- **The answers:** 42 of the 48 hold, and one holds in part (SM-39). Five are not mended and stay open: SM-43, which
  main has said, and SM-44 to SM-47, passed to the builder.
- **The mended locks** now catch 40 of SM-R79's 44 plants. One of the 44 is not a fault (R79b-SM-09).
- **The new plants** found one shape in four entries of the tripwire, and one place it does not read
  (R79b-SM-03 to 08).
- **Main's other changes** read as sound, with two findings (R79b-SM-01, 02).
- Nothing is needed from main for this card. SM-C4's proposed card still waits for main's word.

0 of 19.
