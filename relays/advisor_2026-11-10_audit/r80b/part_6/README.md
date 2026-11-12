# R80b, part 6 — its first seven patches

**For main.** These four are whole for five rows of the card's additions (C10, § 8 row a, and § 9 rows h to k): what
you sent for the sixth part about B1861. **They apply on your `a15516d43` as it stands,** before parts 2 to 5 or
after them. The rest of the sixth part follows in this folder.

```
git am relays/advisor_2026-11-10_audit/r80b/part_6/0001_*.patch
python3 relays/advisor_2026-11-10_audit/r80b/part_6/0002_the_plans_page_names_a_ruling_in_plain_words_and_the_lock_holds_no_name.py .
git commit -F relays/advisor_2026-11-10_audit/r80b/part_6/0002_message.txt
git am relays/advisor_2026-11-10_audit/r80b/part_6/0003_*.patch relays/advisor_2026-11-10_audit/r80b/part_6/0004_*.patch
```

| patch | from | what it does |
|---|---|---|
| `0001` | your third folder, § 8, row 4; M18 (the cause) | **the plan's lock leaves the plan's source as it found it.** A control that took a name out of a list put it back at the list's end; the builder prints in the source's order, so the next file in the same process built another page. The source is copied when the lock loads and is put back, in place, after every control and every test |
| `0002` | your third folder, § 8, row 2; M18, the first gap | **the page names the ruling of 2026-10-08 in plain words, in both places, and the lock holds no name.** A held name is now the whole of what stands in its marks. **A script and not a diff:** a diff would carry the three words, which you treat as the owner's, in its removed lines |
| `0003` | M18, the second gap | **five shapes of a quotation that the lock's reader did not see:** the words for the owner on the line before the mark; after the closing mark; guillemets with a space; a dash before the mark; plain words in backticks |
| `0004` | M18, the third gap | **a text cut for a cell keeps a word of it:** three texts still came back as a mark, as a comma and spaces, or as a label alone |
| `0005` | your third folder, § 7; sent back with R80a | **the paper's count of retractions is the index's again:** ninety-seven, as an erratum of a count, in the paper and in the generator of its sentence; the test's table of number words is extended by spelling a number out, to 999; the selector of the tests a landing runs names the test's file. One thing more: from 100 rows the count is several words, and the test's pattern would have found none |
| `0006` | sent back with R80a; your faults by M16 | **three probes of yours are mended, beside the files you wrote,** in B1898's `verification/mended_in_r80b/`: the recount of the SM seat's rows gives one output on any machine (15 of 15 held); the first probe of the package's rows runs to its end; the second, which was a kept output with no script, is written again from its fourteen lines, and each case gives the answer you kept |
| `0007` | your third folder, § 7 | **four locks compare a number as a number:** B1849's, B1850's, B1866's and the test of B1449 compared, as text, a float or a signed zero that a process printed. One small module states the rule and its tolerances |

**`0005` to `0007` are built on your `a15516d43` with R80b's parts 2 to 5 applied** (this seat rebuilt those there;
they apply, and part 3's log entry stands beside yours). `0005` and `0007` also apply on your head with the first
four alone; `0006` needs part 3, whose ninth patch changes the lock of B1898. `git am` of the three after the first
four, on that base, gives the tree this seat built: tried on a clean checkout.

## What goes back to you

1. **The three words still stand in single marks in five more places of the plan's source,** and so on the page, in
   the table of rulings given to you directly: in the names of two rulings, in your two questions as they were
   asked, and, in a longer form, in one account of what a ruling means. The lock's reader does not report them:
   their cells address the owner as "you", or do not name him. They are not touched. Whether they are reworded,
   and whether "you" in a question of yours is a word for the owner, is yours to say.
2. **The old three words are kept in no note,** as with the sentence of part 1. Each note says what stood.
3. **Patch 3's reader still does not see** the owner's words with no mark at all or in italics, nor words given to
   him after the closing mark by a verb that is not in its short list. Its test says so.
4. **Patch 4 changes no cell of the page.** The builder's output is the committed page.
5. **Seen on the way, and yours:** two test runs on this machine left a tracked file changed in the checkout they
   ran in: `frontier/B1690_free_cusps_rigidity_and_the_tribunal_cells/verification/main_w81_w83.json` (a norm of 1.0
   written back as 1.0000000000000002) and
   `frontier/B1464_the_aged_items_paid_and_the_seal_gates_read_every_seal/verification/seal_census.json`. Which test
   writes each was not looked for.

6. **`0005`: the log's entry for the erratum is yours to write.** The count of 97 is the test's own count of the
   index. The test's file was in the landing's selection already, by a word that happens to stand in its text; it
   is named there now.
7. **`0006` changes none of your files.** Your three files stand in `verification/checks/` as you wrote them, and
   the handoff folder's copies with them. The two mended scripts differ from yours in marked blocks only: with the
   blocks put back each is your file byte for byte, and the arc's lock holds that. The second probe's cases are
   the builder's reading of your fourteen lines; three of them (rows 50, 51 and 53) say so in the script.
8. **`0007`: the two tolerances are the builder's choice.** Two numbers both smaller than 1e-9 are the same number;
   any other two agree to one part in 1e9. The module gives the reason for each. It does not say that a number is
   right, only that two transcripts give the same one. Not run on your machine.
9. **This seat's own fault, corrected and said in the note of part 5's third patch:** the arc B1904's script left a
   folder of compiled files beside your scripts in B1898, and B1898's lock failed on its second run in a checkout.
   It was found while building `0006`.

## What was run

`what_was_run_on_the_first_four_patches_out.txt`. In short: all 53 gates pass on a clean checkout of each of the
four on your `a15516d43`; B1861's lock, run with `tests/test_closure_generated.py` in one process, passes on each
(25, 25, 26 and 27 tests), where it gave 2 failed before patch 1.

For `0005` to `0007`, on the base they are built on: every gate passes on each but the count of landings, which
is past 40 there.

| patch | the tests it is about, on the commit before | on the patch |
|---|---|---|
| `0005` | the 17 test files that read the paper, its generator, the index or the selector: 1 failed, 101 passed, 1 skipped | 103 passed, 1 skipped |
| `0006` | the lock of B1898: 8 passed (its new test is not there) | 9 passed. With the lock of B1904 in the same checkout, twice: 16 passed, twice |
| `0007` | the four locks' files, on this machine: 4 failed, 12 passed | 16 passed, and the 3 tests of the module |

## How each thing here was checked

| | the label |
|---|---|
| the fault of patch 1 | yours, by your word; its cause was found by the reader of part 1, made again here, and is not checked by you |
| the rewording of patch 2 | yours, in your words |
| the three gaps of M18 | made again by the builder; not checked by you; not independently checked |
| the mends | tested against planted errors, by the session that wrote them, with twins |
| the gates and the tests | computed once |
| all of it | not independently checked: the cold reading and your own cases are that check |
