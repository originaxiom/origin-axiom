# B1958 — Review 84 entered: three cold readers caught all seven plants and found twenty faults in main's own arcs

**Verdict: PROVED (a process arc).** Main, 2026-11-18. Register row P-867. 0 of 19.

## Seen first

- **Swept:** `VERDICT topic-sweep /Review 84|plant|reading copy|cold reader/: 45 of 1698 arcs on main match (NEGATIVE 1, OPEN 2, PROVED 41, RETRACTED 1); 62 register rows match (DECLINED 1, DONE 23, QUEUED 38)` — the earlier reviews' entries (B1898, B1916, B1931, B1950) and their planted readings.
- **The literature:** none applies; this is a review of the record's own window.

## Why this review ran when it did

- **The gate fired.** Main's landing of 2026-11-18 (harvest rows 1902 and 1903) was the fortieth commit since Review
  83's anchor, and the push was refused. Main had not counted the commits since the anchor before landing, which is
  its own rule (written after Review 81).
- **No waiver was asked.** Governance gives two ways through: the review, or the author's waiver. Main ran the review.
- **What it cost:** the web seat could not see main's answer to its ten items (M50) until this entry landed.

## What was read

- **The window:** main's work from c8cece9be to 1fc1e224e: 40 commits, the thirteen arcs B1945 to B1957, harvest rows
  1828 to 1903, register rows P-859 to P-866.
- **The sample, drawn by the tool from the anchor:** B1945, B1950, B1955, B1956, B1957, each read in full.
- **The reading copy:** main's head 1fc1e224e with seven planted faults (`verification/plants.json`; its sha256,
  2358bd21…, was fixed before the readers started). A plain folder, not a branch: the push was blocked.
- **The readers:** three sessions of main's own model family, each started cold with the same brief and none of main's
  conclusions. None built any of the window. Reader A took B1945 and B1950, reader B took B1955 and B1956, reader C
  took B1957. Their reports are `verification/READING_A.md`, `READING_B.md` and `READING_C.md`, as delivered.
- **This is weaker than Reviews 82 and 83,** whose readers were sessions of the other model family. That reading of
  this window is owed (R84-2).
- **Quotations** (`verification/quote_check.py`, run file beside it): all 27 are in the file their finding cites; 23 are
  within two lines of the line cited, and four of reader C's are further *[added 2026-11-19 at Review 85, finding A5: the
  run file gives both counts, and the page gave only the first]*.
  Review 83's check had searched the whole window's text; this one holds each quotation at its cited path.

## The plants

**All seven were caught**, each by the reader whose arcs held it.

| plant | where | what was planted | kind |
|---|---|---|---|
| P1 | B1945 | the 14 points with a = 0 or ±1/5 → 16 | number |
| P2 | B1945 | "the lock checks five points" → "all 24 points" | wording about a lock |
| P3 | B1955 | least distance 0.553 → 0.535 | number |
| P4 | B1956 | 162 coloured roots → 164 | number |
| P5 | B1957 | 13 + 9 + 5 → 15 + 7 + 5 | number |
| P6 | B1950 | agy-exp reports 20 → 21 | number |
| P7 | B1957 | "main has not yet harvested" → "has harvested in full" | wording |

Both wording plants were caught. No plant sat in lines a reader was bound to skip (R82-4).

## The findings

Twenty-seven: seven are the plants. Main checked each of the other twenty on its own tree, and **each is right**.

### In main's mathematics pages

| finding | what was wrong | the mend |
|---|---|---|
| A3 | B1945 said a planted charge breaks the closed form "in all 20 cells". No committed output gave that. It breaks 40 cells, on 20 points | the page; a lock test holds the planted case |
| A4 | B1945 said the summed coupling's ratios differ between τ and τ + 1 "by up to 80 %". The run shows 99 % in one row | the page |
| A5 | B1945's verdict line said every cell of both generations equals the closed form. The closed form covers the 96 second-generation cells; the tropical rule covers all 192 | the page and the verdict file |
| A6 | B1945 stated four closed forms for the coupling's pieces as measured. No script of the arc computed them | measured now (`piece_exponents.py`): they hold, to 0.008; a lock test |
| B4 | B1955's "+1/5 on the frame's 25 lines" is a count of fixed lines with the phase assumed | the page says so |
| B5 | B1955 called floating-point identities "exact group theory" and a grid search "never" | the page and the verdict file |
| B6 | B1956: "a line bundle of degree k has ∣k∣ sections". False for negative degree | the page and the script |

### In what main's pages say main checked

| finding | what was wrong | the mend |
|---|---|---|
| A8 | Review 83's entry said eight mends were each recomputed in one script. The script holds four. The reversal near τ = i had no committed output | the page; the output is committed now (B1941's `near_i.py`: −0.392 and −0.120 at 1.05i) |
| A9 | Review 83's quotation counts had no committed output, and "exact" meant present somewhere in the window | the run file is committed; the page says what "exact" meant |
| A10 | Review 83's "the two frames agree" holds for three moduli at one point; the double frame fails its own check there | the page, scoped |
| B3 | B1956 listed a statement under "main's exact check" that its script only printed, and said it agreed with two arcs that say something narrower | the page |
| C3 | B1957's verdict file carried the opening day's counts (275 files, 14,878 statements) against 406 and 20,863 | the verdict file carries no count now; a lock test |
| C5 | B1957's lock had one assertion that could not fail and one that compared a length with itself | both replaced by assertions that can fail |
| C7 | B1957's page said "15 of 24 points orthogonal". The run gives 10 orthogonal and 5 of another kind | the page and the record |
| C9 | B1957's page said "every computed figure of the seat's reproduces" over cards with parts main did not recompute | the page |

### In the register's records

| finding | what was wrong | the mend |
|---|---|---|
| C6 | a record said a singular value is "never below 0.67 at either height". The check takes the larger of two heights and its least value is 0.669 | the record |
| C8 | a record put the Hessian of log(y∣η∣⁴) on y∣η∣⁴ | the record |
| C10 | a record marked verified cited three coefficients; its check computed one | a lock test computes all three |
| C11 | a record marked verified says of itself that it is empty | partial now |
| C4 | the page states the rule "no VERIFIED over a note that says not recomputed"; no lock reads the records' text, and a scan finds a caveat word in 92 of 238 verified records | two records split here (one statement the note said was not recomputed; four the seat itself marks as readings). **The record-by-record pass is R84-1** |

## What it teaches

- **The same fault as the web seat's ten items, found by a second kind of reader.** A statement on a page, or a
  verdict in a record, that says more than the committed output behind it. Eleven of the twenty findings are of
  this kind.
- **Four statements were true and had no output behind them** (A3 apart, which was also wrong): the piece exponents,
  the reversal near i, the quotation counts, and a record's three coefficients (C10). *[The fourth added 2026-11-19 at
  Review 85, finding A3: the line named three.]* A true figure with no committed output reads the same as a wrong one.
- **Review 83's own entry had three faults** in how it described its checks. A review's entry is read like any arc.
- **Main's own family read main's arcs cold and found faults in every arc of the sample.** The plants show the
  readers read with care; they do not show what a reader of another family would add.

## The loop

Nineteen items were open. One is closed here (R82-4); the rest are carried *[corrected 2026-11-19 at Review 85, finding A2: this line said 'Four are closed here', against the entry's own 'One is closed' and its eighteen carried items]*, and ten of those are past their third carry
with no disposition, which the entry in `docs/progress/REVIEWS.md` states line by line.
