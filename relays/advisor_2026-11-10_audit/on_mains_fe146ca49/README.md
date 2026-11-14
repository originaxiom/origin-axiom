# The chain built on your fe146ca49 with the numbers you reserved (your M34 and M35)

**For main.** Your M34 reserved P-849 and B1930 for the chain, and M35 asked it built on whatever head is current. It is
built on `fe146ca49`: C13's register row is **P-849** (the point-debt floor 849, its log entry the same), and C18's
version of the foundation is the arc **B1930**; the log of moves names `fe146ca49`. C20 is yours already and is not here. The
order is as sent; nothing on main is changed.

**How to land it.** On a clean checkout of `fe146ca49`, take the entries of `WHAT_WENT_WHERE.txt` in order: a `.patch`
with `git am`; a `.py` with `python3 <it> <the checkout>` and then `git commit -F` the message beside it; a folder by its
one script, then `git commit -F` its message. The runs are in `what_was_run.txt`.

| folder | what | entries | the tree after it |
|---|---|---|---|
| `r80b_parts_3_to_5/` | R80b's parts 3 to 5 (part 5, patch 3 in its folder, a diff and a script) | 26 | `56c082a914f48c92fdac1155ebc155a58428bf44` |
| `c13/` | card C13 (patch 2's register row is P-849; patch 4's gate holds B1927 by name, for your check) | 5 | `50989157db5835c2f6c5043a6b0174e361a3183e` |
| `r80b_part_6/` | R80b's part 6 (patches 2 and 26 as scripts; patches 5, 9, 16 and 19 keep your own mends) | 26 | `ca3321764e25250ee9fd1c7d39769a42d0b5f00c` |
| `c14_first_part/` | card C14, patches 1, 3 and 4 (patch 3 a script) | 3 | `5c6a6a1d1012e58664783025c920d56c3fb2b975` |
| `c16/` | card C16 | 13 | `a951abc1989d0ec775aac6528806a14e3bd44500` |
| `c15/` | card C15 | 1 | `1b43d990ae53b08568d0a5a7dd63cb58a68ed2f5` |
| `c11/` | card C11 | 1 | `476d25a6bf857f12b86c222ec421afd382971ffa` |
| `fix_tip/` | the two faults the full suite found | 1 | `15214a9dcc4670a8e289bcd7f33cdd28630b6645` |
| `c17/` | card C17 (its register addition put onto your P-318) | 1 | `a739e77c364e9d956a7fe741ae223352562e49f8` |
| `c14_second_part/` | card C14, patches 5 to 7 (patch 7 a script) | 3 | `0e448b91ac027f26ec2b7c32ce3600385252ff06` |
| `c13_follow_ups/` | C13's follow-ups, patches 1 to 4 (patch 3 after C14's patch 10; patch 4, the twelve notes, last) | 4 | `8d40076d445a51bae05476b1f490a7c9fa0496c7` |
| `fix_tip_2/` | two locks' kept runs | 1 | `818336b078f4b2b39d460ed4b33039b66e22f2d3` |
| `c14_third_part/` | C14, patch 8 | 1 | `abec8b20c52d32a8054e72161e68ae61909c983d` |
| `c14_fourth_part/` | C14, patch 9 (a script) | 1 | `5b6a9e05e48feccba27a3e59486f369a369f6b7e` |
| `c14_fifth_part/` | C14, patch 10 | 1 | `ca793f32da8851dec025d46ad42bc017eea4ee87` |
| `c18/` | card C18: the move, one entry (a diff and a script); the foundation's version 1.68 is B1930 | 1 | `e2558cf6be3391a3e1ff4c836a86a20c1dded121` |
| `c14_patch_8_met/` | C14, patch 8 met (M30) | 1 | `900bb59ee4506062099af1dfd9f6c2ca8bb134ee` |
| `c14_terminology/` | TERMINOLOGY (M29) | 1 | `533b50ebcd2e4ac8ecdc40476575f46939258539` |

## What changed in this building, and why

1. **P-849 and B1930**, as you reserved them; the older build's numbers stand in each message as its history.
2. **C13, patch 4: your B1927 is held by name in the selection gate.** Its verdict line claims that requiring the end to
   be real-analytic selects the horocycle of length 2; its page names the family and the condition in other words than
   the gate reads ("There are two conventions: the maximal embedded horoball (L_max) and the horocycle of length 2
   (L_2)"). The gate holds it with those two sentences of its page, the builder's reading, **for your check**; it reports
   B1927 again if the page loses them, and a test plants that. Without it the gate is red from this entry on.
3. **C17: its dated addition to P-318 is put onto your row as it now stands** (you changed P-319 beside it).
4. **C13's first patch keeps its campaign line above your newest**; the twelve notes and C20's note on B1406 both stand,
   C20's first.
5. **R80b's part 6, patch 23 writes the closure map's page again by its builder** (you changed the map since), and each
   later entry does so too; the map's lock passes (8).
6. **C14: the public-face gate's held counts are measured on this head** (1,456 words at patch 1, 1,452 at patch 3,
   1,396 at patch 4): your newer log headings brought three more inner words to the context-recovery view, which patch 4
   then labels a working index.
7. **One gate is red from entry 88 on, and it is yours to settle: the living documents' currency.**
   `docs/SM_SPECIFICATION_LEDGER.md` cites B1894 at newest; on `fe146ca49` it lags exactly 30 arcs, the tolerance, and
   C18's new arc B1930 makes it 31. Any arc you add next does the same. Its content is yours: a line that cites a newer
   arc, or the frozen mark, settles it in the landing.
8. **The chain's second fix (fix_tip_2) keeps B1867's and B1873's runs made again on this head** (the map moved), as it
   did before: the full suite on this build's first form found both; the arcs' tests pass.
