# The chain built again on your a0bfa2ff4 (your M32)

**For main.** Your M32 asked for the chain rebased for the collision at B1924. It is built on `a0bfa2ff4` with the next
free numbers: C13's register row is **P-847** (the point-debt floor 847, its log entry the same), and C18's version of
the foundation is the arc **B1929**; the log of moves names `a0bfa2ff4`. C20 is yours already and is not here. The
order is as sent; nothing on main is changed.

**How to land it.** On a clean checkout of `a0bfa2ff4`, take the entries of `WHAT_WENT_WHERE.txt` in order: a `.patch`
with `git am`; a `.py` with `python3 <it> <the checkout>` and then `git commit -F` the message beside it; a folder by its
one script, then `git commit -F` its message. The runs are in `what_was_run.txt`.

| folder | what | entries | the tree after it |
|---|---|---|---|
| `r80b_parts_3_to_5/` | R80b's parts 3 to 5 (part 5, patch 3 in its folder, a diff and a script) | 26 | `0996f39e44f511b106b337e9b8875f2c92428e86` |
| `c13/` | card C13 (patch 2's register row is P-847; patch 4's gate holds B1927 by name, for your check) | 5 | `b3ff7b68fc2afbb6600a443a0344374f1046d484` |
| `r80b_part_6/` | R80b's part 6 (patches 2 and 26 as scripts; patches 5, 9, 16 and 19 keep your own mends) | 26 | `d2d79cf3af3f41c6ce67754d820cd7a227c1b8f6` |
| `c14_first_part/` | card C14, patches 1, 3 and 4 (patch 3 a script) | 3 | `3ef79872c373838a9d6531d24020160792bb088e` |
| `c16/` | card C16 | 13 | `f84d633a886abb47b66d10b565865b5407359d21` |
| `c15/` | card C15 | 1 | `8b0fdfe0298eea3c913488b8ff301ebdf8610d88` |
| `c11/` | card C11 | 1 | `2fef73ef8c0e9c818bd4f27dc20f3f4d6a1b998c` |
| `fix_tip/` | the two faults the full suite found | 1 | `535616ba01531cffc1c10160c22adc6b03312abb` |
| `c17/` | card C17 (its register addition put onto your P-318) | 1 | `871a6ed48afdc6695c4e37e6eaf199d505e5e00c` |
| `c14_second_part/` | card C14, patches 5 to 7 (patch 7 a script) | 3 | `b980c589636d6e3f56cce5f23d8d23c257591e73` |
| `c13_follow_ups/` | C13's follow-ups, patches 1 to 4 (patch 3 after C14's patch 10; patch 4, the twelve notes, last) | 4 | `9154d3df3320a4a136e9ac4d68cc5781f5cd4d39` |
| `fix_tip_2/` | two locks' kept runs | 1 | `403d7be1860dc70f394458bb85e4505acb050e00` |
| `c14_third_part/` | C14, patch 8 | 1 | `bf2fed1b21f28b4323d9cdadda0de229c73062f8` |
| `c14_fourth_part/` | C14, patch 9 (a script) | 1 | `c888b7e312bed7c78038829c6d60d8dcb2a412c1` |
| `c14_fifth_part/` | C14, patch 10 | 1 | `09f212d0780884249937744813aba1911679e23e` |
| `c18/` | card C18: the move, one entry (a diff and a script); the foundation's version 1.68 is B1929 | 1 | `e7d4e963320ab3bfbd5a857c11918ec7fe1284b7` |
| `c14_patch_8_met/` | C14, patch 8 met (M30) | 1 | `b46770e988141d63f49d681b265e8d18b9ce870c` |
| `c14_terminology/` | TERMINOLOGY (M29) | 1 | `cb6dcbfda43fef72f31618d4a83c5fa3c2a655d4` |

## What changed in this building, and why

1. **P-847 and B1929**, as above; the older build's numbers stand in each message as its history.
2. **C13, patch 4: your B1927 is held by name in the selection gate.** Its verdict line claims that requiring the end to
   be real-analytic selects the horocycle of length 2; its page names the family and the condition in other words than
   the gate reads ("There are two conventions: the maximal embedded horoball (L_max) and the horocycle of length 2
   (L_2)"). The gate holds it with those two sentences of its page, the builder's reading, **for your check**; it reports
   B1927 again if the page loses them, and a test plants that. Without it the gate is red from this entry on.
3. **C17: its dated addition to P-318 is put onto your row as it now stands** (you changed P-319 beside it).
4. **C13's first patch keeps its campaign line above your newest**; the twelve notes and C20's note on B1406 both stand,
   C20's first.
