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
| `c13_follow_ups/` | C13's follow-ups, patches 1 to 4 (patch 3 after C14's patch 10; patch 4, the twelve notes, last) | 4 | `a150805a955c4e80cd45543c92a9f64cdd778815` |
| `fix_tip_2/` | two locks' kept runs | 1 | `6e52f98a1056c4021a1c3053d4efef87feee363b` |
| `c14_third_part/` | C14, patch 8 | 1 | `cbe307611551ffeb574d1bd4dcb05dfb9a7a5ebb` |
| `c14_fourth_part/` | C14, patch 9 (a script) | 1 | `4b3e43d406037d8e8613ca953e2a13dc7c582bba` |
| `c14_fifth_part/` | C14, patch 10 | 1 | `f9178361160288017c34d842d724914ab70b25d0` |
| `c18/` | card C18: the move, one entry (a diff and a script); the foundation's version 1.68 is B1930 | 1 | `e7ae142e8342bc875f4b7ddd05ceb330ab73bb79` |
| `c14_patch_8_met/` | C14, patch 8 met (M30) | 1 | `7cb5d5956976dea2bc948908308d0ff4d8cc97d0` |
| `c14_terminology/` | TERMINOLOGY (M29) | 1 | `08db97b7ade6ee0b205527b63961103495d7e1b2` |

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
