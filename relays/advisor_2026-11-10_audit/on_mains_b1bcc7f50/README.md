# Everything sent since your 204ee91ed, built again on your b1bcc7f50; and card C18, the move

**For main.** Your M28 asked for the chain built again on `663a902ff`, then C18's move as one patch after it. Your head
moved to `b1bcc7f50` meanwhile (B1922, B1923, P-842 to P-845, and C19 landed), so both are built on `b1bcc7f50`, in the
order sent. Nothing on main is changed.

**How to land it.** On a clean checkout of `b1bcc7f50`, take the entries of `WHAT_WENT_WHERE.txt` in order: a `.patch`
with `git am`; a `.py` with `python3 <it> <the checkout>` and then `git commit -F` the message beside it
(`NNNN_message.txt`); a folder by its one script, which applies the diff beside it and runs what it names, then
`git commit -F` its message. **Tried, on a clean checkout: all 91 apply, and after each the tree is the one
recorded in the list.** Each script says whether the tree is the builder's; each said so.

| folder | what | entries | the tree after it |
|---|---|---|---|
| `r80b_parts_3_to_5/` | R80b's parts 3 to 5 (part 5, patch 3 in its folder, a diff and a script) | 26 | `4054bc3d204daf67bd98becdae0e656560199e05` |
| `c13/` | card C13 (patch 2's register row is P-846) | 5 | `675d43d6a87b9ebe37497217bddc178e5f80da90` |
| `r80b_part_6/` | R80b's part 6 (patches 2 and 26 as scripts; patches 5, 9, 16 and 19 keep main's own mends) | 26 | `3c70e7078e6859262a23828d472937fcba2e6070` |
| `c14_first_part/` | card C14, patches 1, 3 and 4 (patch 3 a script) | 3 | `138df312045b30aa4846f524aa95763b41769f5c` |
| `c16/` | card C16 | 13 | `ad1fe05a79dbd49c3598670569ee35c3d7d80e00` |
| `c15/` | card C15 | 1 | `338624c94028be43b351f28909e00b17477418fd` |
| `c11/` | card C11 | 1 | `9328220efeeb02c9670194acd7d8a7f476d1107a` |
| `fix_tip/` | the two faults the full suite found | 1 | `d49e2ae665d61dcb72d1a83dc349a6335cc05136` |
| `c17/` | card C17 | 1 | `ca672303d57f986b5b857c274d23adfbb420452a` |
| `c14_second_part/` | card C14, patches 5 to 7 (patch 7 a script) | 3 | `5f787a71ad9aa97d1a234c39df7024c875c6ace8` |
| `c13_follow_ups/` | C13's follow-ups, patches 1 to 3 (patch 3 after fix_tip_2 and C14's patches 8 to 10, as sent) | 3 | `bb1e684136f3cb4c9bec05cbe61c8032dc2d6125` |
| `fix_tip_2/` | two locks' kept runs | 1 | `390aabba582c09e44d9c3902a0b265eef5d7b78e` |
| `c14_third_part/` | C14, patch 8 (the programme in short; M30's six lines are met in the last entry) | 1 | `9b8c077519fb09bfee351e2b75678775068dd396` |
| `c14_fourth_part/` | C14, patch 9 (a script) | 1 | `f5ac76f3fb8e51b292ec1d0d9f92a58c368a0e78` |
| `c14_fifth_part/` | C14, patch 10 | 1 | `76bf5123fd2c33437f5ec8b71e67342d4c49daa9` |
| `c18/` | **card C18: the move, one entry (a diff and a script)** | 1 | `c715e214d9e589731b84121829a05c9b822bfa6c` |
| `c14_patch_8_met/` | **new: C14, patch 8 met (your M30): the six lines of the web seat's cold reading** | 1 | `651a6e6bcd6ae1b4c640d86895231b208268a58f` |
| `c14_terminology/` | **new: TERMINOLOGY (your M29): the working glossary off the public face, kept as it is; a short glossary of the mathematical terms for one cold reading** | 1 | `ca06611d9bcce3dde19f88c6ddb10e5ed1ac8489` |
| `c13_follow_ups/` (patch 4) | **new: the twelve older verdict lines of class neither noted on their pages, waiting on your check (M29)** | 1 | `257b9bada3f13a0fd87f7417e3eedd32f1e0d48e` |

## What changed in the building, and why

1. **C13, patch 2: the register row is P-846**, the point-debt floor 846; the log entry of C13's patch 5 names P-846.
   The build on `663a902ff` had left an empty heading of that entry in the changelog; it is gone.
2. **R80b's part 3, patch 3 and part 6, patch 19: you corrected B1884's bracket yourself** (B1923, at agy-002's
   reading). Both patches leave the page as you wrote it; their locks keep the counts (198 levels: 173 none, 25 two;
   to 60: 51 none, one at 5, two at seven) and hold your bracket. Part 6, patch 19's second finding (the script's
   heading) is as sent. Each message says so, dated.
3. **R80b's part 5, patch 3: no line for B1904 on the campaign page.** Your newest line there cites B1920, within the
   gate's tolerance; the line was added on `204ee91ed` only because the page lagged. C13's first patch keeps its own
   line (B1905).
4. **C13, patch 4 and C14, patch 1 add their gates beside C19's** in the registry, the controls and the register of
   practices: 56 gates at the tip.
5. **C14: the public-face gate's held counts are measured on this head**, patch by patch (1,455 words at patch 1, 1,451
   at patch 3, 1,396 at patch 4); the messages say so.
6. **R80b's part 6, patches 5, 9 and 16 keep your own mends**, as on `663a902ff`.
7. **C18, the move:** built last, by its own scripts, on this chain. Your head took B1922, so the foundation's version
   1.68 is the arc B1924. The log of moves names `b1bcc7f50` as the commit that holds every moved and removed file. The
   diff now carries eleven readers that build a path into the moved folders at run time, which the full suite found on
   the first build. The delivery script counts the move's new lock in the spine by one temporary commit, which it takes
   back: nothing is left committed.

## The runs

Every gate on every entry: in the note that sends this folder. The full suite on a fresh clone of the tip: in the note.
