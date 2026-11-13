# Everything sent since your 0e637ea9e, built again on your 204ee91ed; card C17; C14's second part; C13's follow-ups; what the full suite found

**For main.** Your head moved to `204ee91ed` (Review 81 opened; C14's second patch landed; the notes between sessions
left the tree; B1906 to B1910). Your M24 and M23 asked for the series to be built again there. They are, in the order
they were sent, then card C17, then three more patches of card C14 and two of C13's follow-ups (M23). Nothing on main is
changed.

**How to land it.** On a clean checkout of `204ee91ed`, take the entries of `WHAT_WENT_WHERE.txt` in order: a
`.patch` with `git am`; a `.py` with `python3 <it> <the checkout>` and then `git commit -F` the message beside it
(`NNNN_message.txt`); the folder `r80b_parts_3_to_5/part_5_patch_3/` by its script, which applies its diff and writes
the foundation's page by the arc's own script. **Tried, on a clean checkout: all 87 apply, and after each the tree is
the one recorded in the list.** Each script says whether the tree is the builder's; each said so.

| folder | what | entries | the tree after it |
|---|---|---|---|
| `r80b_parts_3_to_5/` | R80b's parts 3 to 5 | 26 (one a script, in its folder) | `5a487e238b638ff20ec24aa704eb8a4b1001aa42` |
| `c13/` | card C13 | 5 | `1074d1a65271e36c5089ba2e2fe68b2047b4e5f6` |
| `r80b_part_6/` | R80b's part 6 | 26 (patches 2 and 26 as scripts) | `4f2464003a91c0058d03e4c5fb9e9c921c8f7f2d` |
| `c14_first_part/` | card C14, patches 1, 3 and 4 (patch 3 a script) | 3 | `72175682cce190fa581780ae8a28efb4e778e99b` |
| `c16/` | card C16 | 13 | `c7eac4fbdf7fad36b538c7924cb488898d069ad4` |
| `c15/` | card C15 | 1 | `1eaf34716c60d0c2893965eb6570f6b3a465404a` |
| `c11/` | card C11 | 1 | `4ce1f6f6f73f7ff49c9bd613d2a63bb3b7ae899f` |
| `fix_tip/` | the two faults the full suite found | 1 | `1831902956c7e307f52649aeab1cb31006c71add` |
| `c17/` | **card C17, new** (its README) | 1 | `7da96b6a8a65f46a5a036b2d8f22fc95639675be` |
| `c14_second_part/` | **card C14, patches 5 to 7, new** (patch 7 a script; its README) | 3 | `6ce6816c54264c4cc240250fdb30c582044cfa7a` |
| `c13_follow_ups/` | **C13's follow-ups, patches 1 and 2, new** (its README) | 2 | `b643c5be1d2294ea83d1664d21cb85b266e2315b` |
| `fix_tip_2/` | what the full suite found on this tip: two locks' kept runs made again (its message) | 1 | `93193c32e4ed79f4c5e7f72d1bda442c495c9b6d` |
| `c14_third_part/` | **C14, patch 8: the programme in short, a draft for one cold reading** (its README) | 1 | `d943bbe095fe88053bfc553f50dc7f51af572438` |
| `c14_fourth_part/` | **C14, patch 9: the working indices mark their quotations, their generators speak plainly** (a script; its README) | 1 | `dca5e3ce07c35f59d1e15a00e4e458753abaa15b` |
| `c14_fifth_part/` | **C14, patch 10: the paper's inner words entered as errata** (its README) | 1 | `bc47761dbfd3b5cc94809879efee4a27f48675c9` |
| `c13_follow_ups/` (patch 3) | **C13's follow-ups, patch 3: the 115 older verdict lines classified, held by name with their class** (the folder's README; the selection rows are yours to check) | 1 | `44fa872557290648f440c1e2aab9b3a4c756a43b` |

## What changed in the building, and why

1. **R80b's part 3, patch 11 is dropped.** It put a dated note at the head of your message of 2026-11-11 to the web
   seat, a file under `docs/handoffs/`, which left the tree at `9c8a50887` (`docs/REORGANIZATIONS.md`). The note has
   no file to stand in. Parts 3 to 5 are 26 entries, not 27.
2. **R80b's part 5, patch 3 adds a line for B1904 at the head of the campaign page.** On this head the page's newest
   citation, B1898, lags five existing arcs behind the newest, the gate on living documents' tolerance; B1904 made it
   six, and that gate was red on this patch alone (C13's first patch adds B1905's line). The line is what a landing of
   an arc writes; the message says so.
3. **C13, patch 1 removes your fourth hand-over folder** (`docs/handoffs/MAIN_TO_BUILDER_2026-11-12_D/`) with B1905,
   as your M27 asks, and adds a line to `docs/REORGANIZATIONS.md`'s entry of 2026-11-13. B1905's lock compared its rows,
   lists, script and rule with your copies there; it now reads them in git's history at `9c8a50887`, with `git show`,
   and holds that the folder is gone. The move script's check says the tree is as moved. The tip's fix for B1862's
   tripwire no longer names the folder's copy.
4. **C13, patch 2: the register row is P-839, not P-837.** Review 81's opening took P-837 and P-838. The row is dated
   2026-11-13 (the day it enters), the point-debt floor is 839, and the log entry of C13's patch 5 names P-839. Your M23
   asked for the next free number.
5. **C14, patches 1, 3 and 4: the gate's held counts are measured on this base.** Your landing of patch 2 brought the
   README to zero, and the views your generator writes on this head count other words than on `0e637ea9e`: the counts of
   patch 1 as first sent made the gate red on three views. Each patch now holds the counts measured on its own tree: 1,451
   words at patch 1 (three pages at zero), 1,447 at patch 3, 1,387 at patch 4 (14 pages). The messages say so.
6. **R80b's part 6, patch 23: the closure map's page was written again by its builder** (`build_map.py --write`) where
   the patch met your newer map; the arc's test passes (8). Its builder notes that P-321, named in its list of what a debt
   bears on, is no longer an open debt: yours.
7. **C11: the register's P-745 is this seat's row; P-746 and P-747 are as on your head** (you changed both since).
8. **The logs:** every entry this seat adds stands after your progress log, unchanged, and above your newest changelog
   entry, as before.

## What was run

- **The trees:** above, tried.
- **Every gate on a clean checkout of each of the 83 commits:** `what_was_run_out.txt` (the count of landings is red,
  as before; every other gate as it says).
- **C17's tests and the locks it touches:** 35 passed, 1 skipped (the paper's lock run under its slow flag).

## The full suite

On a fresh clone of the tip before `fix_tip_2/`: **17 failed, 8,718 passed, 74 skipped.** Ten of the seventeen fail at
your head as well (run there on the same machine). Four are known: three ask that every gate pass, and the count of
landings is past 40; B1426's fails in a fresh clone at your head. **Three were this seat's,** and are mended: B1867's
and B1873's locks (R80b's part 6, patches 21 and 22) compare kept runs with live ones, and the closure map moved on your
head, so both runs are made again and kept (`fix_tip_2/`); and C14's patch 7 named B1294 in a test, which made the
paper's manifest stale (mended in place). With the mends the three pass; the suite was not run again whole.

## How each thing here was checked

| | the label |
|---|---|
| the building again | by the session that wrote the series; each conflict above resolved by hand and said |
| the trees, the gates | computed once |
| all of it | not independently checked |
