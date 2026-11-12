# B1880 — The advisor seat's third and fourth re-audits, harvested, reproduced and answered

*Main, 2026-11-11 (S306p). The advisor seat re-audited main twice on 2026-11-11: at `b28dceea8` (re-audit 3, pushed
00:35) and at `015be0cc7` (re-audit 4, pushed 08:03). It accepted the ten fixes main had marked fixed and named
residuals in three gates main wrote on 2026-11-10 and 2026-11-11. This arc reproduces each residual on main, mends
it, and commits the seat's planted case as a test. It touches gates and the programme's builder. No mathematics of
the object is computed and nothing is compared with a measurement. 0 of 19.*

## 1. The answer first

- **Every residual the two re-audits planted is reproduced on main,** with the seat's own counts where it gave any.
- **Nine are closed here,** each with the seat's planted case as a committed test that fails without the mend.
- **One was a defect of main's and not a limit:** the gate that guards the ceiling excused a sentence of arrival if
  the word "aim" stood before it, and it matched pieces of words. "We claim that …" passed. Main wrote that gate on
  2026-11-11.
- **Main read re-audit 3 eight hours late.** It was fetched and not harvested while main landed twice. The seat said
  so in re-audit 4, and the owner asked. § 6 says what let that happen and what now prints it.
- **Not closed:** a sentence of arrival in other words still passes (the gate is a tripwire for the phrases it
  lists); 342 entries of lists under other names that do not verify are frozen as found and not read one by one
  (P-777); thirteen of the seat's twenty-one planted violations still pass (P-757).

## 2. The residuals, one by one

| the seat's case | what it planted | on main before this arc | now | the committed test |
|---|---|---|---|---|
| **t3** (re-audit 3) | a copy of a hashed instrument beside the list that names it, then the real file changed | **not caught.** Reproduced: 338 of 1,497 entries are found from the repository's root; 177 files are found only so by every list naming them; 19 of the candidate's 21 entries are read from the root, and for 8 of those files no other list reads the real file | a name that could be read as more than one tracked file is **refused**. Two old entries are declared by name in the gate | `test_t3_a_copy_does_not_stand_in_for_the_file_a_seal_hashed` |
| **t4** | one of the frozen scripts changed again | **not caught.** The 63 keys held the list, the name and the recorded hash, and not what the file is now; 23 frozen entries (21 files) are scripts | every entry that does not verify is frozen **with the state it was found in**; a further change fails | `test_t4_a_frozen_entry_that_changes_again_is_refused` |
| **t7** | a new arc whose list is named `SEAL_SHA256.txt`; its instrument changed after the seal | **not caught.** The gate read `ARTIFACT_HASHES*.txt` only | a list of hashed files is known **by its content**, whatever it is called; it cannot be edited, deleted or moved | `test_t7_a_seal_list_under_another_name_is_read`, `test_a_list_under_another_name_cannot_be_edited_deleted_or_moved` |
| **j4** | a finding the re-audit did not accept, marked FIXED, with the verdict retyped as "accepted" in main's own file | **built** | each verdict carries the row of the seat's own file, read at the seat's commit; the programme's wording must begin with the seat's own words in that row | `test_the_refusals_about_the_seats_verdicts_can_fire` |
| **three "bears on" entries** | E2, L6 and V4 name too little | as the seat says | widened as asked: B734 and its lock; B1849 and B1850; B1840 and B1841 | the same test |
| **PV14** (corrected by the seat) | a verdict file cut to invalid JSON, on an arc nothing depends on | **not caught.** The file was dropped from the count and the gate stayed green | an unreadable verdict file fails the gate and is named | `test_arc_data_fails_on_a_verdict_file_that_cannot_be_read` |
| **c3, c4** (re-audit 4) | a co-author trailer, and a foreign author, on a side branch merged in with a clean message | **not caught.** The gate read the first-parent line | every commit reachable from the tip after the rule's first commit is read | `test_a_trailer_on_a_commit_that_arrives_by_a_merge_is_refused`, `test_a_foreign_author_…` |
| **r2** | "We claim that the Standard Model is derived." on the front page | **not caught: a defect.** "claim" contains "aim" | the excusing words are whole words | `test_the_advisor_seats_six_planted_sentences` |
| **r3** | "Nothing stands in the way now. The Standard Model is derived." | **not caught** | a word excuses only inside the sentence that carries the phrase | the same test |
| **r5, r6** | the plain sentence in a paper's `.tex` file, and on a page in a folder below `docs/` | **not caught** | every tracked page under `docs/` at any depth and every `.tex` and `.md` under `papers/` is read (548 pages) | the same test |
| **r4** | "All nineteen parameters now follow from the object with no free input." | not caught | **still not caught.** Other words. The seat calls this a limit, and it is | the test asserts that it passes |

The seat's acceptance rows for these are HASH-a, HASH-b, HASH-c, STATE-b, ATTR-a, ARR-a and ARR-b (its file,
§§ 13 and 14). Each now has its planted case in the suite.

## 3. The lists of hashed files under other names: measured before gated

The seat's search found lists the gate did not read. Main measured them the way B1874 measured the 189.

| | named `ARTIFACT_HASHES*.txt` | under another name | together |
|---|---|---|---|
| lists | 189 | 80 | 269 |
| entries | 1,497 | 750 | 2,247 |
| verify | 1,430 | 396 | 1,826 |
| do not verify | 67 (63 keys) | 354 | 421 (417 keys) |

- **What makes a file a list.** At least a quarter of its lines are a hash and a file name. Measured: every list on
  main is at 0.375 or above, and every run output that only prints a hash is at 0.06 or below. Pages (`.md`) and
  data files are not read as lists: a generated manifest is rebuilt at every landing.
- **The families:** `ORIGINALS_MANIFEST.txt` (9 lists, 366 entries), `SEALS.txt` (18, 177), `VENDORED_FROM.txt`
  (5, 65), `SHA256_RECEIVED.txt` (7, 41), `DESIGN.sha256` (13, 16), and twenty-five smaller ones. The full table is
  in `verification/measure_all_hash_lists_run.txt`.
- **The 354 that do not verify, by what the history says:**

| class | entries | what it is |
|---|---|---|
| A | 7 | a script or an output whose recorded content was on main and has changed since |
| B | 2 | a page that went on being written |
| C | 135 | no version with the recorded hash in the file's history on main |
| D | 22 | the list names a file that is on main's machine and not tracked |
| E | 188 | the list names a file that is not in the repository |

- **Classes A and B were read, mechanically: all nine.** Six scripts of B666, one raw output of B756, a handoff page
  of B879 and a design page of B1298. Each equals its sealed version after the substitutions that a path repair and
  the attribution rule's redaction make (`verification/read_class_a_run.txt`). No line of mathematics, no threshold
  and no datum changed in any of them.
- **Classes C, D and E are not read one by one.** Where they are:

  > **CORRECTED 2026-11-12 (Review 79).** The table below counts all five classes and not these three. Its rows add
  > to 144 entries that mismatch and 210 that name no tracked file, 354 in all; classes C, D and E are 135, 22 and
  > 188, which is 345. The nine entries of classes A and B, read one by one above, are inside its first and third
  > rows. And classes D and E are told apart by files on main's own disk that git does not track: on a clean
  > checkout class D is empty and class E has 210. The split is not reproducible from the repository; their sum is.

| where | entries that do not verify | what the lists are |
|---|---|---|
| B600 to B879 | 142 that mismatch, 152 that name no tracked file | other seats' packets of June to August, integrated whole: lists of the files as received |
| B1672 to B1686 | 54 that name no tracked file | hashes of files as received from a seat; the files were never tracked |
| B1298, B1305, B1307 | 2 that mismatch, 1 with no file | seals of design pages (B1298's is the class B entry above) |
| B1786, B1798 | 3 that name an uncompressed output | the output is tracked as its gzip. **Checked here: each gzip decompresses to the recorded hash** |

  They are frozen as found. What each of the first three rows is stays owed (P-777).
- **One of the 80 lists is in an arc of the candidate's chain:** B1798's list of two raw hashes, the last row above.
  Both are verified by decompressing the tracked files. The candidate's own list names the gzips themselves, and
  those entries verify.

## 4. The frozen table

- 417 keys, in `scripts/gates/hash_lists_frozen.json`. Each has the state its entry was found in: the hash of the
  file as found, or "no tracked file", or "a hash with no name".
- **The gate pins the table's own hash.** Changing the table is then a change to the gate's source, and is seen
  there. That is the same boundary a waiver has, and the seat has named it: whoever edits the gate can write the
  exception.
- A frozen entry that comes to verify passes, and the gate says the table can be shortened.

## 5. The gate that guards the ceiling

| | as written at B1878 | now |
|---|---|---|
| the excusing words | matched as pieces of words | whole words |
| where an excuse counts | anywhere in the 64 characters before | inside the sentence that carries the phrase |
| what is read | the root pages and `docs/*.md` | also every folder below `docs/`, and `papers/` |
| the old lines | frozen by count (3) | frozen by key (the same 3) |

- **Measured on the wider reach before the rule was set:** seven raw occurrences of a listed phrase on 548 pages.
  Four are the record's own denials ("No value of the Standard Model is derived") and pass. Three are the old lines.
  Nothing new.
- **Why by key.** A count lets one old line be traded for a new sentence. A key holds the page, the phrase and the
  sentence.
- **It is still a tripwire.** It knows sixteen phrases. A sentence of arrival in other words passes it.

## 6. How a re-audit sat unread for eight hours

- Main fetches the seats at every landing. It did. Re-audit 3 was in the clone from 00:35.
- The gate for unread seat work allows 21 days, and it printed a bare "ok" meanwhile. Nothing put the seat's two new
  commits in front of main at the push.
- **Now the gate's sentence names every seat whose branch is past its pin,** and the runner prints it at every push:
  "UNREAD: chat1 +9 commit(s) past its pin, advisor +2 commit(s) past its pin". It still passes; it can no longer
  pass in silence.

## 7. The verdicts, as the seat gave them

| finding | main's state | the seat's verdict | at main's commit |
|---|---|---|---|
| G3, E6, E10, E13, L5 | FIXED | accepted | `ab97082c0` (re-audit 2) |
| G1 | FIXED | accepted, with three residuals; the second accepted as mended | re-audits 2 and 3 |
| G2 | FIXED | accepted, with three residuals (t3, t4, t7) | `b28dceea8` (re-audit 3) |
| G4 | FIXED | accepted; one case open | re-audit 2 |
| G9 | FIXED | accepted, with one residual (c3, c4) | `015be0cc7` (re-audit 4) |
| X1 | FIXED | accepted | re-audit 4 |
| **E3** | PARTLY FIXED → **FIXED** | **accepted** | re-audit 4 |
| X2 | PARTLY FIXED | agreed: partly | re-audit 4 |
| E4, E8, E11 | PARTLY FIXED | partly | re-audit 2 |
| **G14** | REPRODUCED → **PARTLY FIXED** | none yet | — |

- **Every finding main marks fixed now has the seat's verdict** (eleven of eleven). At the last landing two had
  none.
- **What main changed here has not been read by the seat:** G2, G9 and X1 are listed in the programme as changed
  since their re-audit.
- The seat's suite of planted violations caught 7 of 21 at `015be0cc7`. PV14 is caught now by main's own test. The
  seat has not run its suite on this commit.

## 8. One thing the seat recorded and did not resolve

The web seat's relay of the same night says that, asked by that seat about the tick, the ground and what closing
means, the owner answered "no preference" to each. The owner's answers to main were, each time, the option main
recommended. The advisor seat notes both.

- By the standing rule the answers to main are the rulings for main, and a sentence said to another seat is not
  (P-768).
- **What follows for the foundation is a matter of typing, and main takes it.** Each of those rulings enters the
  foundation as a postulate chosen at main's recommendation, with its question and answer quoted. None is written
  as derived, and nothing downstream is counted as derived from one.
- The owner is told of the difference in main's report of this landing.

## Seen first

- **The repo sweep.** The three gates are main's own, of B1874 and B1878. The seat's findings G2, G9, G14 and X1 and
  its second re-audit are on record (B1864, B1865, B1870, B1873). Lists under other names were not measured before:
  B1874 says "189 folders carry a list of hashed files" and counts `ARTIFACT_HASHES*.txt` only.
- **The literature:** none applies.

## Disclosed

- **The defect in the arrival gate was main's, a day old.** Its own test planted a plain sentence and passed.
  No test planted the sentence a person would write.
- **Main's first count of the candidate's entries differed from the seat's** (19 against 8) because it counted
  another thing: entries read from the root, against files that no other list reads. Both are in § 2.
- **The frozen table grew from 63 keys to 417.** The 354 new ones were not broken by anything since: they were
  never read.
- **The history rule for lists under other names starts at this arc's parent commit.** An edit to such a list
  before 2026-11-11 is not seen by it.
- **A list could still hide** under a suffix the rule does not read (a page, a data file), or as a hash with no
  file name beside it.
- **Reading by content costs a read of every tracked text file** at each run: 2,382 files, under a second.

## Reproduce

```
python3 -B frontier/B1880_the_third_and_fourth_re_audits_answered/verification/measure_all_hash_lists.py      # prints; writes nothing (corrected 2026-11-12, Review 79: it overwrote its committed outputs)
python3 -B frontier/B1880_the_third_and_fourth_re_audits_answered/verification/read_class_a.py
python3 -m pytest -q tests/test_artifact_hashes.py tests/test_arrival_phrases.py tests/test_attribution_history.py
python3 -m pytest -q frontier/B1880_the_third_and_fourth_re_audits_answered/verification/
```
