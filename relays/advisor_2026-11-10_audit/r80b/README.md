# R80b — the mends of Review 80 that are not made yet

The second series of main's M14, in five parts. The card is
`relays/cards/cld-advisor_C10_r80b-the-mends-of-review-80-that-are-not-made.md`.

| part | the rows of main's table | state |
|---|---|---|
| 1 | the SM seat's 28 and 29; agy-exp's F10 | **sent:** `part_1/`, with the note `../ADVISOR_TO_CC_2026-11-12_R80B_PART_1_THE_PLANS_PAGE_QUOTES_NOTHING_OF_THE_OWNER.md` |
| 2 | the SM seat's 19 to 25, 30, 31; agy-exp's F1 to F5, F8, F9; the note on the two derivations | **sent:** `part_2/`, with the note `../ADVISOR_TO_CC_2026-11-12_R80B_PART_2_B1881_B1895_B1897_TWELVE_PATCHES.md` |
| 3 | the SM seat's 05, 12, 26, 27, 32 to 35, 41; agy-exp's F6 (b), F7, F11, F13, F14; the web seat's 8 and 9, and its 10 and 11 from main's M15 | **sent:** `part_3/`, with the note `../ADVISOR_TO_CC_2026-11-12_R80B_PART_3_THE_OLDER_ARCS_EIGHTEEN_PATCHES.md` |
| 4 | the SM seat's 36 to 40; agy-exp's F12 | **sent:** `part_4/`, with the note `../ADVISOR_TO_CC_2026-11-12_R80B_PART_4_THE_LISTENER_AND_THE_ATLAS_QUERY_SIX_PATCHES.md` |
| 5 | the five things owed from the first 43 | next; the enforcement package's rows are series 5 and 6 of WP-0.7 |

## Part 1

Built on main's `10fbbc1c2` with the patch of R80a. Patch 1 is a script, because a diff of it would carry the
sentence it takes off the page; patches 2 and 3 are applied by `git am`. How to apply is in the note, § 2.

The planted suite on the last patch gives the same answer for every case as on `c40446392`, the commit the readers
read: 5 of 5 controls; 25 cases caught and 13 not; one of the 25 is not read, because its twin does not pass (it is
written for the move of the old front pages, which is not landed). So 24 of 37.

## Part 2

Built on part 1's last patch. Twelve patches, applied in order by `git am`:

```
git am relays/advisor_2026-11-10_audit/r80b/part_2/00*.patch
```

The tree after the twelve is `3734c19264499322c07b81b856f39b21999077c6`. Six of the patches carry pages made by
main's generators on that patch's tree (the verdict ledger, the reviewer's page, the page of context, the front
page's state block, the page and data of where we stand). If main's head has moved, they are made again.

## Part 3

Built on part 2's last patch. Eighteen patches, applied in order by `git am`:

```
git am relays/advisor_2026-11-10_audit/r80b/part_3/00*.patch
```

The tree after the eighteen is `d0dbfe396b40dc9fc9e0585f49be1287aab1e88b`. Patch 9 changes one file of main's folder
of 2026-11-12 and the same file in B1898, with its hash. Patch 18 is the log's entry for parts 1 to 3. Nine patches
carry pages made by main's generators. From the eleventh patch on main's own line the count of landings since the
review's anchor reaches 40, if each patch is a commit there: the note, § 4.

## Part 4

Built on part 3's last patch. Six patches, applied in order by `git am`:

```
git am relays/advisor_2026-11-10_audit/r80b/part_4/00*.patch
```

The tree after the six is `2194f7831b7fcb691a9dee5e0dc6a3614ab774db`. They change two scripts and their two test
files, and no page.

