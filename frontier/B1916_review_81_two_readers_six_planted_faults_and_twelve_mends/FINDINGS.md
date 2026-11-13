# B1916 — Review 81: two readers, six planted faults, twelve findings mended

**Verdict: PROVED** (a process arc: what was read, what was caught, what was mended, each checked by main). cc (main),
2026-11-13 (S306p). **0 of 19.**

## 1. The answer first

- **The window** is `c40446392` to `0e637ea9e` on main. Two sessions that built none of it read it at `7d7ab1dfa`
  (the branch `review-81/read`): `0e637ea9e` with the waiver's line, and with **six faults main planted** to test the
  readers (R80-12, P-824). The plants file's sha256, `7ab2417b…`, was published at the opening (`a45e66fd1`, P-837);
  the file is published here (`verification/plants.py`; `plants_sha256.txt` gives the same hash).
- **The readers:** the web seat (`relays/REVIEW_81_CHAT1.md` @ `df9569fa5`, five findings) and the SM seat
  (`relays/REVIEW_81_SM.md` @ `400259cda`, eleven). The other family of model (agy-002, agy-exp) did not read: at the
  owner's word their sessions had no use left that day, and at his later word (move on) their reading goes to Review
  82's window instead of holding this entry.
- **Quotations, by main's machine** (`verification/quote_check.py`, at `7d7ab1dfa`): the web seat's 11 of 12 verbatim
  and the twelfth found by hand (a quotation nested in a quoted table row); the SM seat's 23 of 24, the one miss a
  paraphrase set in quotation marks in its reading notes, not in a finding.

## 1a. Seen first

`VERDICT topic-sweep /planted fault|reading commit|Review 81|tested against planted/: 3 of 1655 arcs on main match (PROVED 3); 7 register rows match (DONE 4, QUEUED 3)`. Review 80's entry (docs/progress/REVIEWS.md; B1898), whose item R80-12 asked that the readers be tested against planted
faults; Review 79's (B1892), whose readers were not tested; the readers' own files at the commits named. The method of
planting faults in a reading copy is the record's own (P-824). **Literature:** none.

## 2. The planted faults: what each reader caught

| plant | kind | the web seat | the SM seat |
|---|---|---|---|
| P1 B1898 § 4, agy-exp "15 of 15" | a number off its source | caught (its 1) | caught (its 01) |
| P2 B1895 row A1, "proved by main for every sequence" | a stronger label; a wider claim | missed | missed |
| P3 B1895's lock, `<= 1332` | a check that cannot fail | missed | not in its card |
| P4 B1878, "confirmed by agy-002, whose reading settles it" | a session as an authority | missed | seen, not entered |
| P5 B1896, "every test on main's pages" | a wider claim | missed | missed |
| P6 P-670, "5.8 × 10⁻³³" | a number off its source | caught (its 3) | caught (its 10) |

**Each reader caught 2 of 6, the same two, both numbers off their source. Every wording fault was missed.** On main
the two caught plants were never present (main's B1898 gives 14 of 14; P-670 gives 5.8 × 10⁻³¹). The lesson for the
next cards: a wording fault is not caught by reading notes and running locks; a card asks that every changed sentence
be held against its evidence and that a lock's new tests be read line by line.

## 3. The twelve real findings, each reproduced by main and mended

| finding | what | main's check | mend (each marked "CORRECTED 2026-11-13 (Review 81, …)") |
|---|---|---|---|
| web 2 | B1898's STATUS row 18: the probe counted at `896cae025`, not at `e6298271a` as the row says | by git: 1,408 / 1,525 / 1,540 at `896cae025`; 1,407 / 1,522 / 1,537 at `e6298271a` (`verification/recount_row18.txt`) | the row carries both counts and where each was taken |
| web 4 | B1892 § 1 and STATUS row 06 keep 52 after § 5's table was corrected to 53 | § 5's table sums to 53, 43, 9 | both read 53; the conclusion holds |
| web 5, SM 02 | B1898: "80 checked in full, every one held", "the check's output is in checks/" | 29 of the 80 have no file in `checks/` | STATUS's head lists the 29; FINDINGS points there |
| SM 03 | B1898: "no session was given an arc that judges its own work" | its ANSWERS lines 22 to 23 name one: B1884 and B1889 | the sentence carries the case |
| SM 04 | B1898's verdict line keeps the sentence FINDINGS corrects; FINDINGS' pointer to § 5 | § 5 does not list the five owed things | the verdict line leads with the correction; the pointer names where they are listed |
| SM 05 | B1898's quotation re-check: docstring 99, output 111 | its json: 111 | the docstring carries 111 |
| SM 06 | B1898: "all gates pass and the belt is ok", no output kept | the arc's tool output says NOT RUN | the sentence withdrawn as unsupported |
| SM 07 | B1898: "every quotation was found by machine" leaves out W8, W9 | W8, W9 marked not checked | the sentence names the exception |
| SM 08 | B1873's kept output: "(no failure line)", where the script prints the failure line | **the cause found:** the certificate reads its pages relative to the working directory; run from the arc's folder (as main did at `c8298b0ff`) it fails otherwise and the line is lost | the call runs from the root; the kept output regenerated; the lock now asks for the line itself, in the run and in the kept output |
| SM 09 | B1885's verdict scope: "two checks", its claim line "three" | A4, A5 and H5 | the scope carries three |
| SM 11 | the changelog: the retraction-count test "failed since … Review 79's window" | by the test's rule: 79 rows at both ends of Review 79's window, 96 at `738be0e5f` (Review 80's) | the sentence carries the window |

The review's corrections go into the retractions index as one row (its count in the paper is now ninety-nine).

## 4. What this review does not certify

- That nothing else is wrong in the window: two readers of one family each missed every wording fault.
- What main changed in answer to this review has been read by nobody but main (Review 82's window).
- The five items at their third carry are disposed of in the entry: four resolved by arcs (B1907, B1908, B1909, B1910
  with P-747), one declined with its reason (P-745, carried by the builder's card).

## Files

- `verification/plants.py` (the six plants; sha256 in `plants_sha256.txt`, as published at the opening).
- `verification/quote_check.py` → `quote_check_run.txt` (the readers' quotations at `7d7ab1dfa`).
- `verification/recount_row18.txt` (the counts behind the web seat's finding 2).
- The lock: `verification/test_b1916_review_81.py`.
