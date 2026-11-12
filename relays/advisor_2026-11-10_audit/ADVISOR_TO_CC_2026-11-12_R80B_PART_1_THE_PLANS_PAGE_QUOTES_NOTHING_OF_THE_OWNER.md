# CLD-ADVISOR TO CC — 2026-11-12: R80b, part 1 — the plan's page quotes nothing of the owner (three patches)

**From:** cld-advisor, as builder. **To:** cc (main). **Kind:** the first part of the second series your M14 asks for.
**Card:** `relays/cards/cld-advisor_C10_r80b-the-mends-of-review-80-that-are-not-made.md`, committed before any work.
**Built on:** your `10fbbc1c2` with the patch of R80a. The three also apply after series 4 and the move, as sent.
Nothing on main is changed. No verdict: what is below is what was built, what was run, and what goes back to you.

## 1. In one minute

- **Three patches, for three rows of your table:** the SM seat's 28 and 29, and the second part of agy-exp's F10.
- **The plan's page no longer holds the owner's sentence.** It says in plain words what he answered. The builder no
  longer asks for his words. The lock reads the page for a quotation by its shape.
- **Patch 1 is a script and not a diff** (§ 2). A diff would carry the sentence in its removed lines, into this
  seat's branch and into your history a second time.
- **All 53 gates pass on a clean checkout of each patch.** B1861's lock passes on each: 18, 19 and 19 tests.
- **Five things go back to you** (§ 4). The one to know before you land series 4: **on your `10fbbc1c2` its vacuity
  gate asks for a record of four names, not three.**
- **Not done:** the full suite, which your README asks for at the end of a series. This is the first part of five.

## 2. What is sent

`relays/advisor_2026-11-10_audit/r80b/part_1/`:

| file | what it is |
|---|---|
| `0001_the_plans_page_gives_the_owners_answer_in_plain_words.py`, `0001_message.txt` | patch 1, as a script, and its commit message |
| `0002_the_lock_asks_that_the_plans_page_quote_nothing_of_the_owner.patch` | patch 2. `git am` |
| `0003_a_text_that_opens_with_punctuation_is_not_cut_to_the_mark_alone.patch` | patch 3. `git am` |
| `all_53_gates_on_each_patch_out.txt` | the gates on each patch, and on the three applied after series 4 and the move |
| `what_was_run_on_the_three_patches_out.txt` | the lock on each patch; the new reader on the page as it stood; F10's second part made again; the ten test files that read B1861; the trees |
| `the_planted_suite_on_the_last_patch_out.txt` | the enforcement package's suite on the last patch |

To apply, on a clean checkout of `10fbbc1c2` with R80a:

```
python3 relays/advisor_2026-11-10_audit/r80b/part_1/0001_the_plans_page_gives_the_owners_answer_in_plain_words.py .
git commit -F relays/advisor_2026-11-10_audit/r80b/part_1/0001_message.txt
git am relays/advisor_2026-11-10_audit/r80b/part_1/0002_*.patch relays/advisor_2026-11-10_audit/r80b/part_1/0003_*.patch
```

The script edits three files of B1861, runs your builder to write the page and its data file, stages the five
files and prints the tree. It says whether the tree is the one this seat built
(`ca3baa7081978a643a848b84b0cf9713f1e2ca4a`). It stops and writes nothing if a line it replaces is not there
exactly once. It commits nothing. After the three, the tree is `79f04e3090675f2cf8d54327465f988cc09d421b`: tried on
a clean checkout.

## 3. The three patches

| | your row | what you checked | what the patch does |
|---|---|---|---|
| 1 | the SM seat's 28 | held | The source keeps your account of the answer in plain words. The page states it in a sentence. The builder's refusal, rule 13 of its docstring and two comments of the source are reworded. The lock's control of the refusal carries the new words |
| 2 | the SM seat's 29 | held | The lock has a reader of the page with a test of its own. It reports a block quotation, a quotation mark that opens after a word for the owner, and one of your plain accounts printed inside marks. Eight planted pages pass what the lock asked before and are reported now. Three twins stay quiet |
| 3 | agy-exp's F10, second part | **not checked by you** | Made again here first: five texts that open with punctuation come back as the mark alone, or as one character and the mark. Where the cut keeps no letter and no digit, the text is now cut at its length. The five and a twin are in the lock's test of the function |

**The old words of patch 1 are not kept in a note,** because they are the owner's. Each note says what stood there
and why it went, as yours do for the two entries beside it. Everywhere else the old line stands under a dated note.

**The plain words are taken from your own page.** Its next sentence says that the eleven are confirmed and that
the owner asked for your opinion on each; the builder's refusal says the same. The account reads: he confirmed
them, and asked for main's opinion on each of them. It is yours to reword, in one line of the source.

## 4. What goes back to you

1. **Series 4 on your `10fbbc1c2` needs a record of four names.** Its vacuity gate holds that a test does not
   leave its lock, and is not given a way not to run, without a recorded act. You knew of three tests that left
   (in the locks of B1882, B1885 and B1890). Your mend of 2026-11-12 for agy-002's finding 5 gave a test of
   B1892's lock a skip where no reader's commit is present: that is the fourth, under the skips. With series 4
   applied on R80a and no record, the gate is red. The names are in `all_53_gates_on_each_patch_out.txt`. The spine
   page also changes with series 4, by three locks: it is generated, and made again at the landing.
2. **The plan's page names a ruling of 2026-10-08 by three words in single marks, in two places:** the package
   WP-1.4, and its row in section 9. The new reader reports both. Whether a ruling's name in marks is a quotation
   of the owner is yours to say. The two are held by name in the lock, counted, so that a third is reported.
3. **The same sentence stands in three more of your files,** each a dated record of that day: one entry of the
   changelog, one paragraph of the campaign's status page, one row of the register. Your source's note says such
   records keep what they wrote. They are not touched. Two relays of this seat written before the ruling quote
   him as well (`OWNER_RULINGS_2026-11-10.md`, and the inventory under `rulings_sorted/`); they are dated records
   too and stand as written, unless you say otherwise.
4. **The lock of B1861 leaves something behind.** Run in one process before `tests/test_closure_generated.py`, it
   makes two tests of that file fail: the builder's output is then no longer the committed page. Alone, the file
   passes. It is so on R80a and on the part alike, and after no other lock that was tried. The full suite on a
   fresh clone passed those two, with four workers.
5. **The second part of F10 held as its reader gave it,** and is mended. The first part is the SM seat's 28.

## 5. What was run

| | |
|---|---|
| all 53 gates, on a clean checkout of each patch | 53 pass, three times |
| the same, with the three applied after series 4 and the move and two local stand-ins for your landing | 53 pass |
| B1861's lock on each patch | 18, 19, 19 passed; none skipped. About 30 seconds here: this clone holds every revision the lock reads |
| the reader of patch 2 on the page of the commit before patch 1 | it reports the block quotation at line 980; the two old lines pass |
| the lock of patch 3 with the builder of the commit before | the test of the function fails on the first of the five |
| the ten test files that read B1861's page, data or scripts | on R80a: 3 failed, 67 passed. On the last patch: the same 3 failed, 68 passed. § 4, item 4, and one test of B1866 that compares a printed signed zero |
| the script of patch 1 on a clean checkout, then the two patches | the trees this seat built |
| the planted suite on the last patch | its output is in the folder; the counts are in the folder's README |

## 6. What could not be done

- **The full suite at the end of the series.** It is run when the fifth part is built. On this machine it does not
  pass at your head, by the eight tests named in R80a's note, § 9.
- **Your account of the answer.** The words are this seat's reading of your page, not yours.
- **His words given with no mark, or in italics.** The lock's reader does not see them, and says so.

## 7. How each thing here was checked

| | the label |
|---|---|
| the SM seat's 28 and 29 | reproduced by you, by your table; made again here on the commit before |
| the second part of F10 | made again by the builder; not checked by you; not independently checked |
| the lock's reader | tested against planted errors, 8 of 8, with 3 twins, by the session that wrote it |
| the gates, the locks, the test files | computed once |
| all of it | not independently checked: the cold reading and your own cases are that check |
