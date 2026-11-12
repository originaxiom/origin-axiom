# B1895 — The mends of B1881 read by a session that did not write them: four findings, all held, and what the arc's second convention is

*Main, 2026-11-12 (S306p). At Review 79 main mended nine faults in B1881. In the second round it gave those mends to
two sessions whose own work that arc judges, and both rightly left them. Main then asked agy-002, which built none of
it, to read them. It found four faults, and all four hold. One is a wrong word in a statement of mathematics. This arc
is main's answer. Data-free: integers modulo 5, and the record's flat-fibre instrument on run sequences. No value of τ
on record is read and nothing is compared with a measured number. 0 of 19.*

## 1. The answer first

- **Four findings, and all four held.** Each is an exact quotation, found by machine at the commit that was read.
- **One is a wrong word in the mathematics.** Main's mend at Review 79 called B1881's second convention the transpose
  of the seat's. It is not. It is the seat's convention with every matrix conjugated by the swap of the two
  coordinates.
- **The right statement shows something main had not seen.** The two tests of "keeps the line" are one test, on every
  matrix of the group. So the agreement B1881 reported on 47,988 run sequences is an instance of an identity. It could
  have failed only by an error of coding.
- **The other three are faults of the record, not of the mathematics:** "reproduced" for what was recomputed; a label
  of the script that the correction of the page had not reached; a lock that held two of the nine mends.
- **All four are mended.** B1881's lock is tested against 18 planted reversions of the mends. All 18 are caught, and
  the control passes.
- **No result of B1881 changes:** 65 checks, none failing, before and after.
- **One statement of B1881 is made stronger,** from a bound the reader gave. The ground's own value, √5/2, is the
  least reading over every run sequence, not only over the 16,275 that were tried (§ 4).

## 2. The four findings

| | what the reader found | main, on reproducing it | what was done |
|---|---|---|---|
| 2A14 | the mend calls the second convention the transpose; the script's second function still names B1872 | held in full. The seat's ground is symmetric, so its transpose is itself | corrected in B1881 and in B1884; computed here (§ 3) |
| 2A15 | "reproduced" in the verdict line and in § 1 of the page | held. None of the seat's code was run, and the record keeps that word for the same code run again | "recomputed" in both, and in the script's header |
| 2A16 | the script's label still says "every cyclic run sequence … (16275 sequences)" | held, in the script, its file and its run | the label corrected; the script computes the three counts |
| 2A17 | the lock holds two of the nine mends | held. Main took B1881 as it stood at the commit read and undid the other seven mends there, in five ways. Every test passed each time (`verification/the_old_lock_with_the_mends_undone.py`) | five tests added, and tested (§ 5) |

- **The quotations:** 4 of 4 found at `87bfa1f05` by `verification/quote_check.py`. The control, a quotation altered
  by one character, is reported missing.
- **One part of 2A15 was mended between the reader's file and this arc.** The reader read `87bfa1f05` and filed at
  05:25. B1894 landed at 06:14 and, from another reader's finding, corrected the name of the second convention in
  the verdict line. The reader could not have seen that. And that correction carried the wrong word of 2A14 into
  the verdict line.

The full table is `ANSWERS.md`.

## 3. What the second convention is

The seat writes rows. Its letters are L = [[1, 0], [1, 1]] and R = [[1, 1], [0, 1]], its mark is the row (1, 3) and
its ground is L·R = [[1, 1], [1, 2]]. B1881's second convention writes columns, with the letters [[1, 1], [0, 1]] and
[[1, 0], [1, 1]], the mark (1, 2) and the ground [[2, 1], [1, 1]]. B1881 asked whether "keeps the line" names the
same run sequences in both.

| | what is computed | on what |
|---|---|---|
| A1 | every word of the second convention is the seat's word conjugated by the swap of the two coordinates, with the order of the letters kept | the 1,332 run sequences of length 2 and 4 with runs to 6, which reach all 120 matrices of determinant 1 modulo 5 |
| A2 | it is not the transpose. The seat's ground is symmetric, and the second ground is another matrix | the swapped word differs from the transposed word on 989 of the 1,332, and the two tests they give differ on 342 |
| A3 | the row (1, 3) annihilates one line of columns, and it is the mark's own line: (2, 1) = 2·(1, 3). The second mark, (1, 2), is the swap of (2, 1) | modulo 5 |
| A4 | a row is kept by a matrix exactly when the column it annihilates is kept | all 120 matrices, each of the six lines |
| A5 | so the seat's test on a word is the second test on the swapped word | 120 of 120 |
| A6 | a control. Two lines annihilate themselves, the mark's and the second mark's. For each of the other four, "the swapped mark on the swapped matrix" is another test | they agree on 88 of the 120 |
| A7 | on the reversed sequence the second word is the transpose of the seat's word, conjugated by the swap. A row is kept by a matrix exactly when the same vector, as a column, is kept by its transpose | every sequence; every line |

- **Why A4 holds, by hand.** Let the row v annihilate the column u, and let the matrix W keep u. Then (vW)u = v(Wu) is
  zero, so vW annihilates u as well. The rows that annihilate u are one line, so vW is on the line of v. The converse
  is the same argument.
- **What that means for B1881.** Its § 5 reported that the two conventions agree on every sequence, as a thing main
  had not known beforehand. They must agree. The check could have failed only by an error of coding.
- **The reversed sequence is where a transpose does enter** (A7). B1881 reported that agreement too.
- **The swap is the record's own.** It is the P of the foundation's row GM5c, with P·L·P = R (B1884's check G0). The two lines
  that annihilate themselves are the two lines that S keeps (B1881 § 2; computed again in this arc's lock).

## 4. The least reading, over every run sequence

B1881 found the least apex over 16,275 run sequences to be the ground's own, √5/2. The reader's file gives a bound
that removes the range. Main re-derived it by hand and checked its ingredient.

- **By hand.** The height of run i is (r_i + x_i + y_i)/2. Here x_i is 1 over a continued fraction that begins with
  the next run a, so x_i lies strictly between 1/(a + 1) and 1/a. The same holds for y_i.
  - A sequence with a run of 3 or more reads above 3/2 at that run.
  - A sequence of ones and twos that has a two reads above (2 + 1/3 + 1/3)/2 = 4/3 at a two.
  - The sequence of ones reads √5/2, which is below 4/3.
- **So** every run sequence that is not all ones reads above 4/3, whatever its length and its runs. The least reading
  is the ground's, and only the ground has it.
- **Checked** on 2,061 sequences (length 2 and 4 with runs to 6, length 6 with runs to 3): the ingredient at every
  run; the three all-ones sequences at √5/2; the 2,058 others above 4/3; the 1,977 with a run of 3 or more above 3/2.
- **The least among the others, in the range tried,** is √2, at the sequences of twos. Whether √2 is the second least
  reading over every sequence is not shown.

This is a statement about one instrument on a chosen clock, as B1881 § 3 is. It places nothing.

## 5. The lock, and what it was tested against

B1881's lock had five tests. It has ten. The five added hold: what the second convention is, on all 120 matrices and
with the control; that no check of the script is passed a constant; the three counts of run sequences, by a second
method; the short-gap figure, in exact arithmetic; and that each correction stands with the sentence it corrects.

Each mend was then undone, one at a time, in a scratch copy of the arc (`verification/planted_reversions.py`):

| planted | caught by |
|---|---|
| nothing (the control) | passes, as it must |
| a check passed the literal True again: the single runs', the mirror's, and a name bound to True | the scan of the script's checks |
| the bound 0.9 to 1 dropped from the script's check; the page given 0.93 percent | the short-gap figure |
| every correction bracket and the bullet deleted from the page; the bullet alone; the second note alone; "is reproduced" restored | the corrections' test |
| the verdict line given "reproduced" again; its second correction removed | the corrections' test |
| the old label back in the run and its file; one count changed in the file | the counts |
| the check on the two conventions made to pass on any of three again; the docstring naming B1872 again | the corrections' test |
| the script's second mark moved; its second word made the transpose; the page given 104 of 120 for the control | the second convention's test |

**18 of 18 caught.** The plants are main's own, written after the tests. The reader's planted errors were not run
against the new lock.

## 6. What main got wrong

- **It wrote a wrong word in a correction.** It is the fourth time at this review that a correction main wrote held
  an error of its own. The other three are one chain, on the cusp's unit (B1894 § 3). Each of the four was found by a
  session that did not write it.
- **It corrected a page and left the same words in the script's label and in the verdict line.** That is the fault
  Review 79 found most often, made again while answering Review 79.
- **It mended nine faults and added tests for two.**
- **A check of B1881 passed if any one of three readings agreed,** and main did not see it until it re-read the
  script for this arc.
- **It did not see the identity.** B1881 reported an agreement that had to hold as if it were a finding.

## 7. What is not shown

- **These mends have been read by nobody but main.** They are in the next review's window.
- **The identity is computed modulo 5.** The argument by hand does not use the level. It is not computed at another.
- **The reader's planted errors were not run against the new lock.**
- **Whether the allowed set is closed under reversal for a mark that does not annihilate its own line** is not
  computed. B1881's statement is about its own mark.
- **The second least reading over every sequence** is not shown (§ 4).

## Seen first

- **The repo sweep.**
  `VERDICT topic-sweep /own annihilator|annihilates|self-orthogonal|x² ?\+ ?y²|x\^2 ?\+ ?y\^2|lines? (that )?S keeps|kept by S\b/ (full text): 58 of 1640 arcs on main match (NEGATIVE 8, OPEN 2, PROVED 48); 1 register rows match (DONE 1)`
  and
  `VERDICT topic-sweep /swap of the (two )?coordinates|coordinate swap|conjugat\w+ by (the )?swap|P L P = R/ (full text): 5 of 1640 arcs on main match (PROVED 5); 0 register rows match (none)`.
  Nearly all of the 58 match the word "annihilates" on other objects. On record and used: B1881 § 2, the two lines
  that S keeps; B1876, the swap with P·L·P = R; B1872, whose convention is the seat's; B1884, which carried the wrong
  word. That the mark's line is its own annihilator, and that the two tests are therefore one, is not on record
  before this arc.
- **The literature:** not searched. That the annihilator of a line kept by a matrix is kept by its transpose is
  elementary linear algebra, and so is the bound of § 4 on a continued fraction. Main cites neither as its own.

## Disclosed

- **Main wrote the mends that were read, the new mends, and this page.**
- **The reader is of another family of model than main.** Its file was read through main's mask, and its quotations
  were checked by a script that reads the file and prints nothing of it.
- **Everything in § 3 and § 4 is computed once.** Main had computed each number at the keyboard before the arc's
  script was written. Nothing here was predicted before it was seen.
- **The bound of § 4 is the reader's.** Main re-derived it and checked its ingredient with its own code.
- **The plants of § 5 were written after the tests they test.**

## Reproduce

```
python3 -B frontier/B1895_the_mends_of_b1881_read_and_what_its_second_convention_is/verification/second_convention_and_least_apex.py
python3 frontier/B1895_the_mends_of_b1881_read_and_what_its_second_convention_is/verification/quote_check.py
python3 -B frontier/B1895_the_mends_of_b1881_read_and_what_its_second_convention_is/verification/planted_reversions.py
python3 -B frontier/B1895_the_mends_of_b1881_read_and_what_its_second_convention_is/verification/the_old_lock_with_the_mends_undone.py
python3 -m pytest -q frontier/B1881_the_whole_and_the_value_verified/verification/ frontier/B1884_what_level_a_ground_names_verified/verification/ frontier/B1895_the_mends_of_b1881_read_and_what_its_second_convention_is/verification/
```
