# R80b — the mends of Review 80 that are not made yet

The second series of main's M14, in five parts. The card is
`relays/cards/cld-advisor_C10_r80b-the-mends-of-review-80-that-are-not-made.md`.

| part | the rows of main's table | state |
|---|---|---|
| 1 | the SM seat's 28 and 29; agy-exp's F10 | **sent:** `part_1/`, with the note `../ADVISOR_TO_CC_2026-11-12_R80B_PART_1_THE_PLANS_PAGE_QUOTES_NOTHING_OF_THE_OWNER.md` |
| 2 | the SM seat's 19 to 25, 30, 31; agy-exp's F1 to F5, F8, F9; the note on the two derivations | being built |
| 3 | the SM seat's 05, 12, 26, 27, 32 to 35, 41; agy-exp's F6 (b), F7, F11, F13, F14; the web seat's W8 and W9 | not started |
| 4 | the SM seat's 36 to 40; agy-exp's F12 | not started |
| 5 | the five things owed from the first 43 | not started; the enforcement package's rows are series 5 and 6 of WP-0.7 |

## Part 1

Built on main's `10fbbc1c2` with the patch of R80a. Patch 1 is a script, because a diff of it would carry the
sentence it takes off the page; patches 2 and 3 are applied by `git am`. How to apply is in the note, § 2.

The planted suite on the last patch gives the same answer for every case as on `c40446392`, the commit the readers
read: 5 of 5 controls; 25 cases caught and 13 not; one of the 25 is not read, because its twin does not pass (it is
written for the move of the old front pages, which is not landed). So 24 of 37.
