# B1892 — Review 79: everything landed since the last review, read in full by sessions that did not build it

*Main, 2026-11-12 (S306p). A process arc: no mathematics of the object is computed and no measured number is read.
The review's entry is in `docs/progress/REVIEWS.md`; this arc holds its evidence. 0 of 19.*

## 1. The answer first

- **99 findings, and all 99 held.** Four sessions read main's work of two days. Main reproduced every finding at its
  source before changing a word. One finding held in all but one detail.
- **One reading misses most of what is there.** The 99 are 88 distinct faults. Ten were found by two readers. [CORRECTED 2026-11-12 (Review 80, the SM seat's finding 6 and 7): the heading says more than § 5's table supports. In the arcs two readers read, the first reader has 52 findings, the second 43, and 9 are common, so each reading found half or more of what the two found together; how much no reader found is not estimated. And by the rule written in advance, which does not count A9 with X13, the 99 are 89 distinct faults, of which nine were found twice; 88 and ten count that pair.]
- **Every fault main could mend is mended,** each with the old words kept and, where a check had been too weak, with a
  lock that can fail. Eleven are in files of the enforcement package and are sent to its builder.
- **Main's own instruments catch 14 of 32 planted faults** on the reviewed commit, by the advisor seat's suite, run by
  main. The repairs for most of the rest are written and are not yet verified by main.
- **The full suite on a fresh clone failed 15 of about 8,500 tests,** and 12 of the 15 were main's own, of this window.
- **The review's own gate can be switched off in two ways.** Neither was used. The repair is not landed.

## 2. How this review was run

The owner ruled that the choices about the review are settled by what best protects the project's integrity (register
row P-805). Main settled them so:

| | before | this review |
|---|---|---|
| what is read in full | one arc in six, drawn by seed | every arc of the window: the 13 added, the 11 whose verdict file changed, the 14 whose findings changed; the governing pages; main's changes to its instruments [CORRECTED 2026-11-12 (Review 80; register row P-830): not every arc. Of the 25 changed arcs the readers' cards named fifteen; ten were on no card, and six more changed in other files only] |
| who reads | main, with readers of its own family | sessions that built none of it, two for each piece where two could be had; no session reads an arc about its own work |
| who decides | main | main reproduces each finding, then mends it or answers it; a reader closes nothing |
| what a finding is | a reader's sentence | an exact quotation, looked for by machine in the file at the commit read |
| the block | waived when it fired | not waived further; nothing was landed between the last message to the readers and this entry [CORRECTED 2026-11-12 (Review 80, the SM seat's finding 4): one landing came between. The last message to the readers is `f8b5e6769`, of 00:11 on 2026-11-12; `c66c8ccae`, of 00:20, changed the changelog, the progress log, the campaign status, the register and the seal ledger; this entry is `84baf38fb`, of 03:04] |

The rules a reader worked under are § 13 of `docs/seats/README.md`.

## 3. The window

`38d2a36dc` to `0dda7b472`: 49 commits. The readers read `323f92327` and, for what was added to their cards,
`0dda7b472`. What main mended in answer is after the window and belongs to the next review's. [NOTED 2026-11-12 (Review 80, the SM seat's finding 8): the two agy sessions read at `0dda7b472` only, as their delivery commits and this arc's own quotation check say; the SM seat and the web seat read `323f92327` and then `0dda7b472`. That no reader's findings were mended before the second reader delivered is not touched.]

## 4. Who read what, and what came back

| reader | what it read | findings | held |
|---|---|---|---|
| the web seat | B1878, B1880, B1882, B1883, B1886, B1888; the governing pages; fifteen changed arcs as the window's difference | 10, and three notes | 10 |
| the SM seat | B1879, B1881, B1882, B1884, B1885, B1887; main's changes to its instruments; five locks, with errors it planted | 48 | 48 |
| agy-002 | B1878, B1880, B1883, B1884, B1886, B1887, B1889, B1890; two corrections made from its own findings; the governing pages; main's changes to its instruments | 26 | 26, one in all but one detail |
| agy-exp | B1879, B1881, B1885, B1888, B1890; the two corrections main made from another reader's findings, with their locks; fifteen changed arcs as the window's difference | 15 | 15 |

- **Every quotation was found:** 111 of 111, by `verification/quote_check.py`. Its control, a quotation altered by one
  character, is reported missing.
- **The fourth reader delivered last,** three hours after the first. Main had by then mended, in its working tree, what
  the first reader found in the same arcs. None of it had been pushed or written on any page, so the fourth reading was
  made on the commit the others read and without sight of their findings.
- **False alarms: none.** No finding was set aside. One detail of one finding did not hold: it counted five rows as
  status rows that have no status cell.
- **B1889 was left by two readers,** rightly: it describes their own work. One reader read it, leaving the part on
  its own family. It was not on the fourth reader's card.

The full table, finding by finding, is `ANSWERS.md`.

## 5. What two readers found in common

Where two sessions read the same thing. The rule for "the same finding" was written before a second reader's file was
opened: the same arc, the same file, quotations that overlap.

| what | first reader | second reader | found by both |
|---|---|---|---|
| B1879 | 10 | 0 | 0 |
| B1881 | 8 | 2 | 1 |
| B1882 | 1 | 10 | 0 |
| B1884 | 4 | 1 | 0 |
| B1885 | 7 | 2 | 1 |
| B1886 | 2 | 1 | 2 (one finding of the second covers both of the first) |
| B1887 | 4 | 2 | 1 |
| B1888 | 2 | 1 | 0 |
| B1890 | 2 | 2 | 0 by the rule; one fault is the same, quoted at other lines |
| B1878 | 0 | 1 | 0 |
| B1880 | 0 | 3 | 0 |
| B1883 | 0 | 0 | 0 |
| the two corrections of 2026-11-11 (B1221, B1641) | 3 | 6 | 2 |
| the fifteen arcs changed and not added | 2 | 2 | 0 |
| main's changes to its instruments | 5 | 7 | 2 |
| the governing pages | 3 [CORRECTED 2026-11-12 (Review 80; found by a reading on another family of model and reproduced by main): this read 2. The web seat's findings on governing pages are three, W2, W9 and W10; with it the two columns sum to 53 and 43, and with B1889's three to 99] | 3 | 0, and two things the first wrote as notes are findings of the second |

- **What it shows.** Of the faults found in what two sessions read, most were found by one of them alone. In B1879
  one reader found ten faults and the other none.
- **What it does not show.** A rate. The counts are small, and a fault that is easy to find is found by both, so any
  rate from them would flatter the readers. Main prints the counts and no estimate.
- **Read once only:** B1889 (3 findings). It describes the work of every reader. Two left it; one read it, leaving
  the part on its own family's sessions, which no reader has read.
- **Not read by the second reader of the fifteen changed arcs:** B1726 and B1753. Their notes are about the nulls of a
  comparison with measured values, and the reader left them under the firewall. The first reader's two findings are
  in B1726.

## 6. The kinds of fault

| kind | examples |
|---|---|
| a check that could not fail, or a lock weaker than its sentence | a check passed the literal value true; one built from typed integers; one that passed over an empty list; an index that was the sum by definition; locks that looked for a printed line; a test of a central claim that skipped; a gate excused by any earlier word of denial |
| a statement wider than what was computed | "the walk's measure" where run lengths were computed; "two ... and on" that fails nine levels past the range; "never touches the measured values" from a static chain; ranges given for one menu of three |
| a number that differs from its source | 26 lattices where the page said two; 1,699 rows where the digest counted 1,686; a greatest place that was the nearest grid point; interval ends, a threshold, a count of digits |
| a label stronger than its evidence | "expectations written before" where everything entered in one commit; "reproduced" for a recomputation; another session's check stated as fact; a row "14 pass" with no committed run behind it |
| a correction that did not travel | main's two corrections of 2026-11-11 missed two verdict lines and two tables; a sentence true of four levels stood unscoped in five places; a verdict line of August still called a ladder complete that its own page had amended twice; a note promised for the map was not carried through four changes |

## 7. The instruments

- **The locks on five corrections,** tested by the SM seat with errors it planted: 25 of 43 caught [CORRECTED 2026-11-12 (Review 80; found by a reading on another family of model and reproduced by main): this read 25 of 44. One of the 44 was not a fault, by the SM seat's own correction at the second round (register row P-811), and the old count had stayed here, in the verdict line and in the register's ranked list]. Mended: both
  spellings and line breaks in the tripwire, entries for two more corrections, the kernel computed for another map,
  the lookup held to four arcs' own files, the page's list compared with the computed one.
- **The lookup of one arc at the front door** printed a guess from words as the arc's status: 218 proved arcs were
  shown as dead. It prints the verdict now. The guess itself is register row P-322.
- **The web seat ran its planted errors again** against the two locks main mended on 2026-11-11: 10 of 11 and 11 of
  13 caught, where each had caught 5.
- **The gates,** by the advisor seat's suite run by main on a scratch clone of `0dda7b472`
  (`verification/planted_suite_on_main_0dda7b472_out.txt`): controls 5 of 5; **14 of 32 planted cases caught.**
- **The full suite on a fresh clone,** at `323f92327`: 15 failed, 8,422 passed, 72 skipped. Eleven were verdict
  files of this window whose scope broke the schema; the schema's test is not a gate and no landing ran it
  (register row P-810). One was a ledger row. One fails by construction while a waiver is live. Two are standing. [NOTED 2026-11-12 (Review 80, the SM seat's finding 9): no output of that run was committed. The figure stands as typed text, here and in the logs: computed once and not kept, which § 6 of this page counts as a fault in another row.]
- **The environment.** No variable of the project was set in any run of main's.

## 8. What skips the review still

- **Two ways to switch its block off** (register row P-806): a variable of the environment, and a sentence on the
  reviews' page. The repair is in the advisor seat's fourth series, which main has not verified.
- **The schema's test is not a gate.** Main runs it by hand at every landing until it is.
- **The trigger counts commits.** Of this window's 49, twenty touched nothing but generated pages [CORRECTED 2026-11-12 (Review 80; found by a reading on another family of model and reproduced by main): this read
  "eighteen touched nothing but generated pages or a session's page". By git twenty touch nothing but generated
  pages, and none touches a session's page alone].
- **No reader was tested against planted faults.** No way exists yet to give a reader a planted copy that it cannot
  compare with main.

## 9. What main got wrong in running this review

- **It entered a reader's finding as new without sweeping the foundation,** and wrote that the foundation lacked what
  it has said since version 1.59 (register row P-802). The session whose finding it was caught it within the hour.
- **It mended two findings and left three places uncorrected** (A11 to A13). The same reader caught those.
- **The correction it wrote for that error held an error of its own.** It gave a dimension as a sum, without the
  maximum the foundation's row has, so that it was negative on ten of the 64 vectors computed (X3). The fourth reader
  caught it.
- **It answered one finding and left the fault standing.** Asked why a lock did not count what it promised, main added
  the count and kept the line of typed fractions beside it (SM-15, then X8).
- **A check it had just made real failed on a threshold main had typed,** not on the mathematics. The threshold was
  corrected and the check kept.
- **Its first reader had been silent for hours** and main did not notice until the others had answered.

## Seen first

A review of this form has not been run here before. The sweep that matters is the readers' own. Main looked for
each old form before correcting it and found, with the readers, eleven places a correction had to reach.

**The literature:** not searched for this arc. It counts findings on the record's own pages and states nothing of the
mathematics. Two ideas of method are used and were read in no source for it: that what two readers find in common
bounds what one reading misses, and that a reader is tested by faults planted on purpose. The first is used only to
print counts; the second was not done.

## Disclosed

- **Main wrote every arc that was read, and the instruments, and this page.** It did not read its own work as a
  reviewer; it answered.
- **Two of the four readers are of main's family of model and two are not.** The two that are not found 41 of the 99.
- **Two readers of the agy family are read by main through a mask that hides numbers.** Their quotations were checked
  by a script that reads their files; main did not. Each number main needed it took from its own files.
- **What main mended is not yet read by anyone but main.** It is the next review's window.

## Reproduce

```
python3 frontier/B1892_review_79_read_by_those_who_did_not_build_it/verification/quote_check.py
python3 -m pytest -q frontier/B1892_review_79_read_by_those_who_did_not_build_it/verification/
```
