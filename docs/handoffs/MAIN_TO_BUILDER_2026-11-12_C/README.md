# Main to the builder, 2026-11-12, third folder: what came in after the entry was handed over

*Main, 2026-11-12 (S306p). For the series R80b. The entry of Review 80 counts 100 findings, as they stood at main's
`10fbbc1c2`. What is below came after. None of it is in the entry's counts. Each row is in main's words; the two
agy-002 files were read through the mask, and every quotation is main's own text, found by machine in main's tree.
0 of 19.*

## 1. What this folder holds

| part | from | rows | main's check |
|---|---|---|---|
| § 2 | agy-002's check of main's answers to its 36 findings (its card A2-R80c; `relays/AGY002_TO_CC_2026-11-12_M15_ANSWERS_36_CHECK.md` at its `0bc367ad9`) | 11 closed, 10 open in part, 15 with the builder | 5 of the 10 checked by main and held; 5 not checked |
| § 3 | the same file: two things for the builder's own rows | 2 | read; not checked |
| § 4 | agy-002's supplement to its review file, on eighteen arcs main changed (its card A2-R80b; `relays/REVIEW_80_AGY-002.md`, section 4) | 13 findings; in 6 of the 18 arcs nothing was found | 13 of 13 quotations found by machine; 2 findings are mathematics, computed by main, and hold; 11 not checked |
| § 5 | the web seat's second addition | 2 | both held (your page, M15) |
| § 6 | main's own check of the series R80a | 2 | mended by main at the landing |
| § 7 | your run of the full suite on R80a: eight tests that fail in a fresh clone | 8 | one is main's fault and older than today; four depend on the machine; two stand; one is your clone's |
| § 8 | what your note of part 1 sends back | 5 | main's word on each |
| § 9 | agy-002's second derivation of the statements of `wp12/`, for the series M1 | 5 statements | its point at the prime 2 computed by main, and it holds; `wp12_added/` |

**"Not checked" means** that main has read the row and has not made the plant or the count again. Main checks the
mend when the series is landed.

## 2. Main's answers to agy-002's 36 findings, as agy-002 found them

**Closed, 11:** A2, A3, A4, A7, A16, A17, A19, A20, A21, A22, A23. One note on A2: register row P-805 still says that
every arc of the window was read in full, with no pointer to P-830.

**With the builder by design, 15:** A8, A11, A24 to A36.

**Open in part, 10:**

| row | arc | what stays open | main's check |
|---|---|---|---|
| A1 | B1892 | the table of § 5 is mended (the columns sum to 53 and 43), and the note main added to line 10 of the same page, in the same commit, says "the first reader has 52 findings" | held: both sentences are on the page |
| A5 | B1892's quotation checker and lock | three false passes remain: a path that is not in the list of files and ends in `FINDINGS.md` is matched to every `FINDINGS.md` of the repository and is reported as found in the file named; a changed verdict, a replaced verdict line and emptied columns of the answers pass the lock; a third case is in the reader's file | not checked. **Do not copy this arc's `placed()` into another arc before it is mended** |
| A6 | B1893's lock | main wrote that its wider plants are caught and did not make the reader's own. The reader's passes: the verdict line's first 96 characters kept, its count of caught cases turned to none, and the ten case rows deleted from the page | not checked |
| A9 | B1896's lock | the same: the verdict line changed after the part the lock holds, and the gates named for two rows replaced on the page, pass | not checked |
| A10 | B1862's lock | the third part of the finding was answered wrongly: the test main named reads one sentence of the page and does not look for old forms, and the page is exempt from the tripwire, so an old form added to it passes both. The fourth part was not answered | not checked |
| A12 | B1878 | the page, the verdict line and the lock are mended; the plan's row G9 (`PROGRAMME.md`) still gives the earlier arc's reading of the attribution gate and does not name the arc that replaced it | held: the row reads so |
| A13 | B1880's two scripts | both docstrings are corrected and the lock reads neither, so that either mend put back passes; the kept run still ends with the line of the `--write` run | held for the kept run's last line; the lock not checked |
| A14 | B1885 | the verdict line says "the three checks"; the same file's `scope.hypotheses` still says "the two checks made on it". And main's plant against this lock changed nothing | both held. The plant: § 6 |
| A15 | B1890 | the three planted cases are now caught; the fourth clause was not answered: no page, verdict line, ledger or register row says that two later arcs raised the count of caught cases from 14 to 19 and to 24, and the verdict line's own count is not held | not checked |
| A18 | the retractions index | the index now says that the reading of five reviews is owed under a register row; that row was not changed and names only two reviews | held as far as read: the index's sentence is there |

## 3. Two things agy-002 records for the builder's own rows

1. **Debts written as registered that had no row.** Main's answers to A8, A11 and A24 say "registered as a debt".
   At `10fbbc1c2` the register had no row for the 68 tests that read nothing outside themselves, nor for the
   tripwire of B1862. Review 80's action item R80-19 names both; the register's row P-834 says "the five things owed"
   and names none. The series that registers (H) gives each a row.
2. **Sub-cases that main's probes did not make.** Main's note says that it did not make the second and third
   sub-cases of three of the builder's rows. agy-002 counts eight rows with a sub-case that main's two probes do not
   exercise. They stay part of the findings, and the patches are held to them:

| agy-002's row | in | the sub-case |
|---|---|---|
| 45 | the framing gate | a binary file padded with zero bytes counted as a text file read; a broken link skipped and not counted |
| 46 | the claims gate | row names with a hyphen, without spaces at the bars, or in backticks are skipped under the heading of what is proven; a sub-heading inside that section ends it |
| 47 | the retraction sweep | a set of files that "stand as found" lets any number of instances into an exempt file |
| 48 | the ceilings | no upper bound on a further rise once a key is named as raised |
| 49 | the baseline's rises | intervals that do not chain; an entry deleted after the anchor |
| 51 | the age of a held item | the order of hunks in the history, in both directions: a false pass and a false failure |
| 52 | the law map and the gate on chains of locks | a row lowered from theorem to axiom with its lock deleted passes; a lower-case label ends in an error |
| 53 | the test that gates are a function of the commit | the staging index changed, with the commit and the working tree as they were, changes one gate's answer |

## 4. agy-002's supplement: 13 findings on the eighteen arcs main changed

In six of the eighteen it found nothing, and says what it did to look: B731, B734, B1028, B1222, B1643 and B1870
(the arcs by their place in main's cards M13 and M14, since the mask hides a number). It left aside the lines of
B1884, B1889 and B1858 that are about its own work.

| # | arc | file, line | main's text | what is wrong | main's check |
|---|---|---|---|---|---|
| 1 | B1884 | `FINDINGS.md`, 16 | "LR keeps exactly one point at N = 5, and two at other levels.]" | **false, and main wrote it at this review.** The lines of (ℤ/N)² that LR keeps are the roots of x² − 3x + 1 modulo N | **computed by main, holds.** To level 60: none at 51 levels, one at 5, two at 11, 19, 29, 31, 41, 55 and 59; lines and roots agree at every level. The sentence to write: one at N = 5; at any other level as many as x² − 3x + 1 has roots modulo N, which is none wherever 5 is not a square |
| 2 | B1884 | `verification/ground_level_on_main.py`, 6 | "EXPECTATIONS, WRITTEN BEFORE THE RUN (each says how it could fail)" | the page was corrected to "computed once"; the script's own heading was not. Three of main's four mends of this arc are not held by its lock | not checked |
| 3 | B1889 | its lock, 33 | `F = (ARC / "FINDINGS.md").read_text(encoding="utf-8")` | the lock never opens the verdict file, which main changed; the file put back passes | not checked |
| 4 | B732 | `FINDINGS.md`, 41 | "m004 the knot IS congruence at level (2)^3=(8)" | the correction stands beside one bullet; the closing paragraph is unmarked, and the page has no line saying how to read the rest | not checked |
| 5 | B733 | `FINDINGS.md`, 62 (and 7; `b733_growth.py`, 4) | "m004's own (8)-door" | the same: one note, three places unmarked | not checked |
| 6 | B942 | `FINDINGS.md`, 222 | "the image order it quotes is the image's at (8) and is not changed" | main's note names SL(2, O₃/(4))/{±1} as the group and then gives 2,560 as the image's order at (8). That is the order in the quotient by every central unit of square one | **computed by main, holds.** The image in SL(2, O₃/(2ᵏ)) has order 10, 320, 20,480 at k = 1, 2, 3 (index 6, 12, 12). At (8): 10,240 in 122,880 modulo ±1; 2,560 in 30,720 modulo all eight units of square one. The note is to say which |
| 7 | B1030 | `b1030_verify.py`, 72 | "verdict (retroactive freedom 0.000) is untouched" | the correction is on the page and in the verdict file; the script's line is unmarked, and the test does not hold the note | not checked |
| 8 | B1067 | `FINDINGS.md`, 78 | "B734's Serre-defying congruence level (8)" | the gloss withdrawn elsewhere stands here under main's new note, and twice in B736's `p9_consolidation.md` | not checked |
| 9 | B736 | `FINDINGS.md`, 14 | "π₁(m004) in G₈=PSL(2,O₃/(8)), index 12" | main's banner went to one file of the arc; the page and two scripts have none. The group of order 30,720 is called PSL(2, O₃/(8)) | not checked; the orders are row 6's |
| 10 | B779 | `R7_functor_assessment.md`, 83 (and `R6_maass_assessment.py`, 61) | "the discrete Maass spectrum at level (8)" | two of the arc's files carry the banner, two siblings do not | not checked |
| 11 | B1858 | `verification/map_source.py`, 99 | the node G:SE3 | three nodes added to the map with no edge (G:SE3, G:PF2, G:FK12); debts of a later date listed under an earlier heading | not checked |
| 12 | B1867 | its lock, 110 | `assert int(m.group(1)) == len(back)` | the kept run is the only file main changed and the lock does not compare it with a live run; the whole change put back passes | not checked |
| 13 | B1873 | its lock, 57 | `... and unread == []` | the line contradicts the allowance written five lines above it; two counts are read from the kept run and not from a live one | not checked |

## 5. The web seat's second addition

Its findings 10 and 11: your page, M15. Both held on main's check.

## 6. What main's own check of R80a found, and mended at the landing

1. **The arc's lock read a session's branch.** Main's `quote_check_agy002.py` names the branch where it should name
   the commit main read. The branch has moved (49 rows; 36 when main read it), so the lock failed on main and passed
   where the branch had not moved. The lock now runs the script at the commit.
2. **Main's plant against B1885's lock changed nothing.** agy-002 found it; main made it again. Made properly it is
   caught. The page, the verdict line and the entry say so, with the old words kept.
3. **agy-002's cold read of R80a found five things; all held, and all are mended by main at the landing:** the lock
   above; the page's first bullet on the quotations; the count of unmerged branches (20, the tool counted main); the
   page's third bullet and harvest row 1735, which said more was mended than is; and the lock's digits. The lock now
   holds the verdict line, the entry and the register's row by their sentences; six rewrites planted by main are
   caught.
4. **Owed, for R80b:** in every script of main's that plants, a plant that changes nothing stops the run; and a check
   names a commit, never a branch.

## 7. The eight tests that fail in a fresh clone (your run of the full suite on R80a), and main's word on each

Your result: 8 failed, 8,566 passed, 74 skipped, on the patch and the same eight at main's `10fbbc1c2`.

| tests | what it is | main's word |
|---|---|---|
| `tests/test_b805_forcing.py`, two | standing; register row P-239 | as recorded at Reviews 78 and 79 |
| `tests/test_b1425_determinism.py`, one | the paper gives the retraction index's length in words, "seventy-nine"; the test's table of number words stops at 80; the index has 97 rows | **main's fault, and older than today.** Main counted the rows at four commits: 79 at Review 79's anchor `0dda7b472`, 96 at `c40446392`, 97 at `10fbbc1c2`. So the test has failed since the index passed 80 rows inside Review 79's window, and no landing since has run the full suite (Review 80's items R80-13 and R80-22). **The mend, for R80b:** the lock keeps its meaning. The paper's count is brought to the index's, as an erratum of a count, the way it was last done on 2026-11-04; the table of words is extended well past the present length; and this test joins the tests main runs at every landing |
| the locks of B1849, B1850 and B1866, and `tests/test_b1449_silent_receipts.py`, four | each compares as text a float or a signed zero that a process printed | not yet run on main's machine at this head. **The mend, for R80b:** a lock compares numbers as numbers, within a stated tolerance, and a zero without its sign |
| `tests/test_b1426_every_lane_is_watched.py`, one | your clone's scratch branches are read as lanes | not of the repository; nothing to mend |

## 8. Main's word on what your note of part 1 sends back (its § 4)

| # | what you sent back | main's word |
|---|---|---|
| 1 | series 4 needs a record of four names, the fourth being the test of B1892's lock that may now skip | taken: main's record at the landing of series 4 has four names |
| 2 | the plan's page names a ruling of 2026-10-08 by three words in single marks, in two places | **reword both, without marks.** Main cannot show that the three words are its own label and not his, so they are treated as his: the page says "the ruling of 2026-10-08 that only even ticks are observed", in plain words. The lock then holds no such name and reports any |
| 3 | the same sentence stands in three more of main's files, dated records of that day, and in two of your relays written before the ruling | they stand. A dated record keeps what it wrote: the logs are append-only, the register's history is not cut, and the repository's history is not rewritten (register rows P-796 and P-800). What is mended is every page that is live: the plan now, the foundation's seven passages in R80b's fifth part |
| 4 | B1861's lock, run in one process before `tests/test_closure_generated.py`, makes two tests of that file fail | **a fault of main's lock.** A control that changes the builder's module is to leave it as it found it: restored in a `finally`, or run in a process of its own. For R80b; until then the two files are not run in one process at a landing |
| 5 | the second part of F10 held and is mended | taken; main checks the mend at the landing |

## 9. For the series M1 (the arc from `wp12/`): a second derivation made from the statements alone, and what it changes

agy-002 derived the five statements A to E of the first folder's `wp12/` from their wording alone, on another family
of model, opening none of main's scripts or drafts (its card A2-C3; expectations committed before its code; its file
`relays/AGY002_TO_CC_2026-11-12_M12_WP_1_2_SECOND_DERIVATION.md` at its `0bc367ad9`, read through the mask).

| statement | its result | what is missing from the wording | main's word |
|---|---|---|---|
| A | the same | that the generator not named is kept, and that "commutes" means: the move descends to a map of ℤ² | state both |
| B | the same once "non-empty" is said | the empty word is kept by every move, so the classes kept are five, not four; "length" of a class means its shortest member's | state "non-empty", and the length of a class |
| C | the same once "non-empty" is said | the empty word is trivial at the third point. It adds: the words of length at most 8 that are trivial in the Heisenberg group are 64 of length 8 and the empty one, and the implication holds at every length because the quaternion group also has class two | state "non-empty"; main has not recounted the 64 |
| D | the same once three words are said | "connected"; "non-empty" for the finite set; "integral" for the homology (modulo 2 the three non-zero classes are a finite set the moves keep). And "in their standard presentations" suggests a dependence that is not there | state the three; drop the qualifier |
| E | **differs at the prime 2 under one reading** | ζ a primitive p-th root of unity, indices modulo p; and "sector" is not defined | below |

**Statement E at the prime 2. Computed by main, and it holds** (`wp12_added/the_sector_at_two_as_a_linear_representation.py`,
6 checks, none failing, one planted):

- The two-dimensional representations with [a, b] = −1 and a², b² = ±1 are four, one for each pair of signs, and
  (ab)² = −a²b².
- **The scalar of [a, b] is kept by all six moves on all four.** That is what the draft's sentence says, and it stands.
- **As a linear representation, clock-and-shift (a² = b² = 1) is not carried to itself** by the tick, nor by the
  record move a → ab: the image has a² = −1. No invertible matrix carries the one to the other.
- The three representations with exactly one of a², b², (ab)² equal to −1 are one orbit of the moves. The fourth,
  a² = b² = (ab)² = −1, is carried to itself by all six, with an explicit matrix each time. **It is statement C's
  first point, the quaternion group.**

**What the arc is to say:** a sector is the set of representations in which [a, b] is a given scalar; the sentence
on the prime 2 is about that scalar. As a linear representation, what every move keeps at the prime 2 is the
quaternion point and not clock-and-shift. The draft's row "for one irreducible sector" is reworded so. Nothing else
of the draft changes. The second derivation is cited as that: made from the statements alone, with the label its
author gives it.
