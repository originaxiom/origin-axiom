# Review 80: the 57 findings that came after main's first 43, and what main has done with each

*Main, 2026-11-12, 13:40. Four files are in: the web seat's (7, and 2 more in a dated addition), agy-002's (36), the SM
seat's (41) and agy-exp's (14). Every quotation was found by machine at the commit read [CORRECTED 2026-11-13 (Review 81, the SM seat's finding 07: except the two of the web seat's dated addition, W8 and W9, which are marked not checked]: 7 of 7, 36 of 36, 50 of 50
(each in a file its finding names, or in its arc) and 14 of 14. The first 43 are answered in
`ANSWERS_the_first_43.md`, and main's mends for them are on main.*

*"Checked" means that main made the finding again itself: by a recount from git or from the file, by a planted error
of its own, by a computation of its own, or by reading the line and working out what it does. It is not the label
"reproduced" of the protocol's § 12. The check's output is in `checks/`. [CORRECTED 2026-11-13 (Review 81, the web seat's finding 5 and the SM seat's 02, checked by main: for 29 of the findings main checked in full there is no file in `checks/`; their "held" rests on a recount or a reading that left no output: agy-002's A1 to A4, A7, A10, A11, A13 and A16 to A23, the SM seat's 01, 02, 03, 05, 06, 08, 09, 12, 13, 17 and 36, and agy-exp's F8 and F12] "Not checked" means what it says: nobody but
the reader has looked. agy-exp's findings are given here in main's words, so that its lane need not be read.*

## The SM seat (41)

| | where | what was found | main's check | state |
|---|---|---|---|---|
| 01 | B1892, the verdict line | ten changed arcs of Review 79's window were read by no reader | by git, register row P-830 | held; noted on the verdict line; the ten are with readers |
| 02 | B1892 § 5 | the table adds to 98, not 99 | the same as agy-002's row 1 | held; mended |
| 03 | B1892 § 8 | "eighteen" commits of generated pages only: twenty | the same as agy-002's row 3 | held; mended |
| 04 | B1892 § 2 | a landing came between the last message to the readers and the entry | the three commits' times and files (`sm_rows_probe`) | held; mended |
| 05 | B1892, its answers and verdict; the protocol § 13 | "reproduced" is § 12's word for the same code run again | § 12 read | held; noted in the arc. **To build:** § 13's "main reproduces each finding" reworded; a line in the next log entry on main's own use of the word on 2026-11-12 |
| 06 | B1892 § 1 | "one reading misses most" is more than the table supports | the table: 52, 43, 9 in common [CORRECTED 2026-11-13 (Review 81, the web seat's finding 4: 53, 43, 9] | held; mended |
| 07 | B1892, its answers | 88 and ten count a pair the rule does not count: 89 and nine | the sentence | held; mended |
| 08 | B1892 § 3 | the two agy sessions read at one commit only | the checker's table of readers | held; noted |
| 09 | B1892 § 7 | the fresh clone's figure has no committed output | a search | held; noted |
| 10 | B1892's quotation checker | it looks in a pool, not in the named file | the same as agy-002's row 5 | held; mended |
| 11 | B1893 § 1 and verdict | five of six patch locks fail on the commit before, not each | the arc's own run file | held; mended |
| 12 | B1893's lock | the half on attribution would not tell main that the gap had been closed: it compares 4 with 4 and no history is involved | the lock read | held. **To build:** the docstring and the page say which half would tell; register row P-816 names the rest |
| 13 | B1893, row U13.c | caught by a check older than the series | the committed message, and the gates' file at `e6298271a` | held; noted |
| 14 | B1893's lock | three cases name no gate | the same as agy-002's row 6 | held; mended |
| 15 | B1893 | "the series after it" is the third; the mends are in the fourth | the page and P-806 | held; mended |
| 16 | B1893's planted-suite output | `f6e89032a` is not on main | git: on no ref; it was main's scratch commit | held; noted on the page |
| 17 | B1893 § 5, § 6 | three figures have no committed output | a search | held; noted |
| 18 | B1893, row U12.b | 1,407 files marked, 1,537 by the series' own definition | recount at `e6298271a` [CORRECTED 2026-11-13 (Review 81, the web seat's finding 2, recounted by main by git: main's kept probe counted at `896cae025` (1,408; 1,525; 1,540), not at `e6298271a`; at `e6298271a` the counts are 1,407 `test_b*.py`, 1,522 top-level `test_*.py` and 1,537 at any depth, the reader's figures] | held; noted |
| 19 | B1895, B1897, B1881's lock, P-822, harvest row 1733 | the lock has 15 tests; these say fourteen, or four more | the lock's history: 5, 5, 10, 14, 15 | held. **To build** |
| 20 | B1895 § 5, § 1, verdict; harvest row 1730 | not brought up to date after the reader ran its plants | the page and the verdict line | held. **To build** |
| 21 | B1897's opening; agy-002's page; harvest row 1733 | a sentence is attributed to B1895 that no file of B1895 holds | a search | held. **To build** |
| 22 | B1895's lock | 295 of its 409 sequences were tried by the arc's script; 114 are new | not checked | **to build** |
| 23 | B1895 § 3, row A1 | true, and not what was computed | built over the integers: 1,332 of 1,332 (`b1895_probes`) | held. **To build:** the note, and the built comparison in the lock |
| 24 | B1895 § 7; P-819 (3) | the open question is settled by the arc's own outputs: not closed under reversal | 358 or 362 of 1,332 at each of the four marks, none at the two (`b1895_probes`) | held. **To build** |
| 25 | B1897 § 4; P-822 | two things owed with no open row | not checked | **to build:** the rows |
| 26 | B874, the bracket of the window | B892's numbers are in double precision and the bracket does not say so | not checked | **to build** |
| 27 | the changelog entry of 2026-11-11, the law map, B1894's lock, B1641's lock | the old sign of the index for a unit on one line still stands | a search: several pages (`sm_rows_probe`) | held. **To build:** each place read; the changelog's sentence corrected in a new entry |
| 28 | B1861's source and builder | a sentence of the owner is still a block quotation on the plan, and the builder refuses to build without it | line 978 of the plan; the two lines of the builder | held. **To build first of the mends:** plain words in main's label, the refusal reworded, the long lock run |
| 29 | B1861's lock | it looks for one phrase and forbids one spelling | the line | held. **To build:** it asks that the plan's page quote nothing |
| 30 | B1881 § 1 | "main adds three things" still lists what B1895 counts as an error | not checked | **to build** |
| 31 | B1881's lock | a docstring says two planted lines where three are asserted | the two lines | held. **To build** |
| 32 | a dated message of main to the web seat | it still says "reproduced" and lists the identity as an addition | not checked | **to build:** a dated note at its head; the message's own words stay |
| 33 | B1882's lock | a date within 120 characters is all it asks of a correction | not checked | **to build** |
| 34 | B1884 § 1, the bracket | "two at other levels": 173 levels to 200 have none, 25 have two, 209 has four | recount (`sm_rows_probe`) | held. **To build** |
| 35 | B1884, the verdict line | "main's own convention" | the line | held. **To build,** with a lock that reads it |
| 36 | the listener | two holes that lose an amended message | the code read: both hold | held. **To build:** every read message with no stored record of its text is named, whether or not a new one came; tests for both |
| 37 | the listener | two error paths misreport | not checked | **to build** |
| 38 | the listener | the docstring does not say that main's first look exits | not checked | **to build** |
| 39 | the atlas's query | the tag is still printed as a status in four places | not checked | **to build** |
| 40 | the atlas's query | one arc id shared by several folders | not checked | **to build** |
| 41 | the test of B874's bracket | two false statements pass it | not checked | **to build** |

## agy-exp (14), in main's words

| | where | what was found | main's check | state |
|---|---|---|---|---|
| F1 | B1881's lock | the two mended conditions can be taken over empty lists | main's plant: 15 of 15 pass (`plants_b1881_third`) | held. **To build** |
| F2 | B1881's lock | the script's check function can be made to ignore what it is passed | main's plant: passes | held. **To build** |
| F3 | B1881's lock | an unpinned check can be made unable to fail by an "or" on a length that is never 0 | main's plant: passes | held. **To build** |
| F4 | B1881's lock | no sequence need be read: the least typed, the counts typed behind the beginning the lock pins | main's plant: passes | held. **To build** |
| F5 | B1881's lock | the made-with file given another version, and a number of part A changed | main's plant: passes | held. **To build** |
| F6 | B1891's lock | (a) the fourth old sentence is not looked for; (b) the set of status-table rows is not compared, nor the unspaced table lines | (a) the same as the web seat's row 6, mended; (b) not checked | **(b) to build** |
| F7 | B1894's quotation checker and lock | the same pool as B1892's, even when a file is named; the lock passes where no reader's commit is present; two prose mends only are held | the shape of agy-002's row 5; B1894's own not checked | **to build:** the strict placing main gave B1892's |
| F8 | the verdict lines of B1895 and B1897 | a session's name stands in a line that is published on the verdict ledger | both lines read; § 12's last clause | held. **To build:** "a session that did not write them"; the page keeps who |
| F9 | B1895's lock | a verdict file is swept as one block, so one correction excuses any other statement in it | not checked | **to build** |
| F10 | B1861 | (a) the SM seat's 28; (b) the shortening function returns its mark alone for a text that begins with punctuation | (a) held; (b) not checked | **to build** |
| F11 | B862's script | a grid of zero or a negative grid returns an empty kernel and raises nothing | not checked | **to build** |
| F12 | the listener | (a) the SM seat's 36, first hole; (b) a message runs on through a heading of its own level that is not a message | (a) held; (b) the pattern read: it stops at levels 1 and 2 only | held. **To build** |
| F13 | B1222's page; the test of B1028 | the correction stands as a bullet of its own among ten counted bullets; the test joins a tight list into one unit, so a tag in one bullet excuses another | not checked | **to build** |
| F14 | the test of B734 | it sweeps one field of a verdict file where its neighbour sweeps three | not checked | **to build** |

Its two derivations, both recomputed by main (`b1895_probes`): the swapped-mark recipe agrees on 120 of 120 matrices at
the two marks that annihilate their own line and on 88 of 120 at each of the other four; over 3,378 primitive cyclic
run sequences the least reading is the all-ones' (√5/2), the second-least the all-twos' (√2), and every other reads
above 17/12, the least of them 1.4866 at (1, 1, 2, 2). The argument by cases was read and is right. **To build:** a
note in B1895 § 7 and a test.

## The web seat's addition (2)

| | where | what was found | main's check | state |
|---|---|---|---|---|
| W8 | B732, its closing paragraph | the level is still given as (8) with no correction beside it | not checked | **to build** |
| W9 | B942's page note | the image's order stands without the quotient that only the verdict line names | not checked | **to build** |

## Owed from the first 43, and not built yet

- **B1862's tripwire** (agy-002's rows 10 and 11): no pattern for one finding, three trees unscanned, a mark that
  accepts the uncorrected claim, a cue in a later quoted paragraph that excuses, a bold form unseen.
- **Nine asserts in scripts that end in a constant** (`or_true_sweep`). With the constant taken out: two of main's fail
  (B1036 line 256, where exact numbers are compared by identity; B1103 line 178, which states the opposite of its own
  comment), two hold (B1306's slice C, B575), one reads an empty list (B1832); four are in other sessions' files.
- **68 tests in `tests/` that read nothing outside themselves** (`literal_only_tests`).
- **Eighteen rows in the enforcement package's own files** (the web seat's five and agy-002's thirteen), with main's
  cases, in `ANSWERS_the_first_43.md`.
- **The foundation's seven passages in plain words,** as its version 1.67 (`checks/genesis_v1_67.py` writes them; the
  arc and its lock are to build).
