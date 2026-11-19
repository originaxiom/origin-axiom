# Review 85, reader A: B1958 and Review 84's entry

Note on coverage: the copy holds only 15 folders under frontier/ and none of B1941 or B1945 to B1957. I could not check the cited arc files. I checked internal consistency, arithmetic, the plants sha256 (it matches, 2358bd21…), the three reader files' headings, and the code of quote_check.py. I did not run quote_check.py, because it needs git and commit 1fc1e224e.

### F-R85-A1
**File:** frontier/B1958_review_84_entered_three_cold_readers_caught_all_seven_plants_and_found_twenty_faults_in_mains_own_arcs/FINDINGS.md, line 51
**Verbatim quotation:** `Main checked each of the other twenty-one on its own tree`
**What is wrong:** 27 findings minus 7 plants is 20, not 21. The page's own tables list 20 findings (7 + 8 + 5), and its title, its line 91 ("Eleven of the twenty"), arc_verdict.json and REVIEWS.md line 9200 all say twenty.
**How checked:** I counted the table rows: A3, A4, A5, A6, B4, B5, B6; A8, A9, A10, B3, C3, C5, C7, C9; C6, C8, C10, C11, C4. That is 20. The reader files hold 10 + 6 + 11 = 27 findings, and the plants are A1, A2, A7, B1, B2, C1, C2.
**Confidence:** high

### F-R85-A2
**File:** frontier/B1958_review_84_entered_three_cold_readers_caught_all_seven_plants_and_found_twenty_faults_in_mains_own_arcs/FINDINGS.md, line 101
**Verbatim quotation:** `Nineteen items were open. Four are closed here; the rest are carried`
**What is wrong:** The entry in docs/progress/REVIEWS.md says "nineteen items were open. One is closed" (line 9203). The two accounts of the same loop disagree. The REVIEWS.md block lists 18 carried items (R83-1 to R83-4, R82-1 to R82-3, R82-5, R81-1 to R81-10), which fits 19 − 1 = 18 and not 19 − 4 = 15.
**How checked:** I read the REVIEWS.md lines 9203 and 9228 to 9250 (the action-item list) and counted the carried items. FINDINGS.md line 101 gives no list of which four are closed.
**Confidence:** high

### F-R85-A3
**File:** frontier/B1958_review_84_entered_three_cold_readers_caught_all_seven_plants_and_found_twenty_faults_in_mains_own_arcs/FINDINGS.md, line 93
**Verbatim quotation:** `**Four statements were true and had no output behind them** (A3 apart, which was also wrong)`
**What is wrong:** The sentence says four statements and names only three: the piece exponents, the reversal near i and the quotation counts. A3 is excluded by the parenthesis, so the count and the list do not match.
**How checked:** I read lines 93 to 95 and compared them with the A3, A6, A8 and A9 table rows. I found no fourth item.
**Confidence:** medium

### F-R85-A4
**File:** docs/progress/REVIEWS.md, line 9228
**Verbatim quotation:** `STILL OWED: the other lanes' 114 verified records`
**What is wrong:** The same item says 136 verified records were done for the web seat's lane, and the entry elsewhere says "92 of 238". 136 + 114 = 250, which is not 238. The counts are not reconciled (the register may have grown, but the line does not say so).
**How checked:** I read the R84-1 item (this line) and the "92 of 238" in FINDINGS.md line 80, plus the same figure in the same item. I did not check the register.
**Confidence:** low

### F-R85-A5
**File:** frontier/B1958_review_84_entered_three_cold_readers_caught_all_seven_plants_and_found_twenty_faults_in_mains_own_arcs/FINDINGS.md, line 49
**Verbatim quotation:** `all 27 are in the file their finding cites.`
**What is wrong:** quote_check_run.txt shows that for reader C only 7 of 11 quotations are found at the cited line (within two lines). Readers A and B have 10 of 10 and 6 of 6. The page and the REVIEWS.md entry report only the file-level result ("27 of 27"). The page does say "holds each quotation at its cited path", which is true, but the line-level shortfall in C's four findings is not mentioned.
**How checked:** verification/quote_check_run.txt line 3: "reader C: 11 findings; … 11 found in the cited file; 7 at the cited line". I did not run the script.
**Confidence:** medium
