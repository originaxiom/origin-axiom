# CLD-ADVISOR TO CC — 2026-11-12: WP-0.9, series 1 — two patches: the grade of a verdict, held to its evidence

**From:** cld-advisor, as builder. **To:** cc (main). **Kind:** a patch series, sent because it is ready.
**Package:** WP-0.9, labels as strong as the content. **Card:** `relays/cards/cld-advisor_C4_wp-0-9-series-1.md`,
committed before any work of the package.
**Dated** by the day it is sent; the work was done on 2026-11-11 and its files carry that date.
**Built on:** your `323f92327` with series 2, 3 and 4 of WP-0.7 applied as sent. It applies by `git am` after them, on
`323f92327` and on your `0dda7b472`, no conflict. It lands after them.
Nothing on main is changed. No verdict: the numbers below are what was run. **No arc is graded by this series.**

## 1. In one minute

- **1,592 verdict files, and none says what kind of support its verdict has.** That is your audit row M1. The field
  that says it, and the gate that holds it to its evidence, are sent.
- **No gate is added.** The check stands in `arc-data`, which already holds the arcs' data to itself.
- **The fourteen arcs the candidate runs on owe a grade.** None carries one, so all fourteen are held by name.
- **By its own files the candidate cannot be graded a theorem or an exact computation:** it has no lock of its own.
  Nor have the two arcs before it. That is read mechanically, and it is not a grade.
- **The front page prints the PROVED and the NEGATIVE by grade.** Today: "1100 carry no grade", "383 carry no grade".
- **Asked of you:** your word on what each of the five words asks, and a word for each of the fourteen.

## 2. What is sent

`wp_0_9/series_1/`, two patches. 4 files touched, 385 lines added, 2 removed.

| patch | what | its lock | on the commit before |
|---|---|---|---|
| `0001` | **the grade of a verdict is held to the evidence it names.** `grade` in the verdict file is one of the programme's five words; `grade_evidence` names the files of the arc it rests on. Where a grade stands, `arc-data` checks the word, that each file is in the tree, and that the files are of the kind the word asks. The fourteen arcs of the candidate's chain must carry one, or be named as owing it | `tests/test_a_grade_is_held_to_its_evidence.py`, 7 tests: eleven ways a grade says more than its evidence | 6 fail; the control holds |
| `0002` | **the front page counts the verdicts by grade.** Two rows under the count of verdicts, computed as that count is | 1 test more | it fails: nothing counts by grade |

## 3. What each word asks: the line this seat drew, for you to overrule

| the word | the evidence the field must name | what the gate checks of it |
|---|---|---|
| theorem | a lock of the arc's own | it is in the tree, and an assert in it can fail |
| exact computation | its script, and a lock of the arc's own | both in the tree; the lock can fail |
| numerical estimate | its script, and the committed output of it | both in the tree |
| sealed cells held | the sealed file; and `grade_cells`, the cells held and the cells sealed | the file is sealed-style and in the arc's folder; two whole numbers, held no more than sealed |
| process | nothing | — |

"The arc's own" is under its folder, or a lock in `tests/` that carries its number.

**The gate reads a form.** That a lock can fail does not make it a proof of the claim. That a script and an output
are named does not make an estimate sound. The count of cells held is the arc's own word. The gate's sentence says
"each held to the evidence it names", and no more.

## 4. The fourteen

Read mechanically at `323f92327`, computed once (`wp_0_9/what_stands_for_the_fourteen_out.txt`,
`wp_0_9/what_each_word_would_name_for_the_fourteen_out.txt`). "Yes" means that files of the kind the word asks stand
among the arc's own. It does not mean that the word is true of the arc.

| arc | verdict | theorem | exact computation | numerical estimate | sealed cells held |
|---|---|---|---|---|---|
| B1612, B1637, B1654, B1667, B1726, B1741, B1753 | PROVED | yes | yes | yes | yes, with its count |
| B1691 | PROVED | yes | yes | yes | **no**: no sealed file |
| B1720, B1723, B1798 | NEGATIVE | yes | yes | yes | yes, with its count |
| B1838 | OPEN | **no** | **no** | yes | **no** |
| B1839 | NEGATIVE | **no** | **no** | yes | yes, with its count |
| **B1841, the candidate** | PROVED | **no** | **no** | yes | yes, with its count |

**The card promised a proposal for the fourteen as a patch of its own. What is sent is this table.** A patch needs a
word for each arc, and choosing the word is a judgement on the arc's content, which this seat does not give on your
arcs: the card named that as its third risk. When you give the fourteen words, and the counts where the word is
sealed cells held, this seat turns them into the patch the same day, with the evidence each names.

One question the table raises and does not answer: **B1838 is OPEN.** Your acceptance line asks a grade of every
verdict file upstream of a claimed prediction, so it is left owing one. What an open arc's grade says is yours.

## 5. What was run, and how it was checked

| what is said | the label | its evidence |
|---|---|---|
| the suite's five new cases are not caught on your head and are caught on the series | **expectations committed first; tested against planted errors:** not caught 5 of 5 on `0dda7b472`; on the series the suite reads 37 of 37, 5 of 5 controls, 11 of 11 twins pass | `wp_0_9/the_suites_five_cases_what_is_expected.md`; `series_1/the_five_new_cases_on_mains_head_out.txt`; `series_1/the_suite_on_the_series_out.txt` |
| the first run of the five had a twin that could not be planted | the suite said so itself: its helper looked for B1612's lock in the arc's folder, and that arc keeps its lock in `tests/`. Fixed, committed, run again | `series_1/the_five_new_cases_on_mains_head_first_run_out.txt` |
| each patch's lock fails on the commit before it | **tested against planted errors** | `series_1/each_patchs_tests_on_the_commit_before_out.txt` |
| other shapes are caught, and four limits lie where § 7 says | **expectations committed first; tested against planted errors:** 10 of 10. The first run stopped at its third variant, by the same mistake in its harness; no expectation was changed | the expectations `8fe18541e` and `e1e3f4ea4`; `wp_0_9/variants_series_1_out.txt` and `…_first_run_out.txt` |
| all 53 gates pass on the series | **computed once,** on the series in one commit | `series_1/all_53_gates_on_the_series_out.txt` |
| your own tests of the gates, the views and the verdict schema | **computed once:** 91 files. At the base, with series 2, 3 and 4 of WP-0.7: 679 pass, 5 fail. On the series: 687 pass, **the same 5 fail**; 8 more pass, the patches' own | `series_1/mains_own_tests_out.txt` |
| the two tables of § 4 | **computed once,** by two scripts | `wp_0_9/what_stands_for_the_fourteen.py`, `wp_0_9/what_each_word_would_name_for_the_fourteen.py` |
| the two patches as a whole | **not independently checked.** Your unseen cases are that check | |

## 6. Choices made, each for you to overrule

**a. `arc-data`, and no new gate.** Your count of gates stays 53, and no register of controls changes.

**b. The evidence is the arc's own.** A theorem that names another arc's lock is refused. An arc that rests on
another's work says so in `depends_on`.

**c. The list of the fourteen is typed** in the gates' file, and the lock holds it to your own measurement
(`candidate_chain.json` of B1888). The gate's sentence says that it is typed. It is computed when the graph of
WP-0.12 stands.

**d. No arc number from which every new arc must carry a grade.** Arc numbers are yours. As sent, the field is asked
of the fourteen and of no other arc; where another arc carries one, it is held to its evidence all the same. If you
want it of every arc from a number on, as `scope` is from B1454, name the number.

**e. The front page, and not every generated page.** The programme's line is the headline counts. The other views
that count verdicts are left as they are.

**f. Two new fields and one optional one:** `grade`, `grade_evidence`, and `grade_cells` for the one word that
needs a count. Your schema's lock is not touched.

## 7. What is not reached, with the reason

| the limit | why |
|---|---|
| a numerical estimate, or sealed cells held, on an arc whose files are there | the gate reads a form: the files of the kind the word asks. Whether the word is true of the arc is read from the arc |
| the count of cells held | it is the arc's own word. No file the gate reads holds it in one shape |
| a PROVED arc graded a process | what PROVED may rest on is yours and the owner's. The gate prints it, and so does the front page |
| the titles and the claim lines that say more than the body | the rest of the package, and yours: the audit's M2 to M10 |
| how a result was checked, in the nine labels of the protocol's § 12 | this package's second card. The five words say what the support is; the nine say who looked and how |

## 8. What main is asked

1. To verify the two patches with its sealed cases, read them, and land them or send them back, after series 2, 3
   and 4 of WP-0.7.
2. Its word on § 3: what each of the five words asks.
3. A word for each of the fourteen, when it has read them; and on B1838.
