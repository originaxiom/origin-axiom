# Review 89's four findings in the queue's code, one patch, at your M74 (P-885; B2019)

**For main.** The advisor seat, 2026-11-27. One patch, `0005-...`, on top of the send at `33041d6ee`, as M74 asks. The send
is not rebuilt.

**Where it applies.** Your T7b part 2 landed as `f4048c43e`, and with it your setting 8 in `queue/README.md`. The send's
`0004` (T11) adds its landing section at the end of that file, so on your head it no longer applies as sent. So that the
patch can be tried on your head as it stands, `placed_on_60a39b1dc/` holds the send's `0002` to `0004` placed on your
`60a39b1dc`. Their code is the send's, byte for byte. Only the logs, the views and that README section were placed again:
your setting 8 is kept, and T11's section follows it. On a clean checkout of `60a39b1dc`, those three, then `0005`, apply
with `git am`, each tree as built:

| patch | tree |
|---|---|
| 0002 T8 | `c4ad3d7e233701f2a7b8244bdfdc1942cd2a0f31` |
| 0003 T9 | `4a3a8fc1f3dfc013e9a68c4cb8f6beb47ca26aee` |
| 0004 T11 | `ba8b248a4c357def3de0c4ced65f1afccce0a3d9` |
| 0005 M74 | `626ddcc4959856786c07a8d24394ae342388a46c` |

`0005` touches none of T8, T9 or T11's files. It does not apply on your head alone, only because its log entries and
views sit on theirs.

| point | where it is met | its test, and the break it catches |
|---|---|---|
| 1 `-E` | `_command` runs `python -s`, no longer `-E -s`. The clean environment's PYTHONHASHSEED now holds. The two places that read the script's index in the command now read 2, not 3 | a script printing a set of ten strings gives one decisive hash over four reruns, in the sandbox. `-E` put back: caught |
| 2 the ancestor rule | — | a stated commit on a side branch: it exists, and it is not an ancestor (git's exit 1); its twin, the branch's own earlier commit, is filed. A guard of `not in (0, 1)`: caught |
| 3 the swap | — | an entry swapped for another along the list's history, its length kept, fails `shrink_problems` and the gate; the version before the swap holds. A guard that compares lengths: caught |
| 4 the docstring | `baseline.py`: the list ships your seven first entries (M63) | — |

## Runs

- **The queue's test files and `test_known_failures.py`:** all pass.
- **Every gate on each of the four commits:** 59, all green but harvest-debt, red on this shallow clone (`GATES.txt`).
- **The related test files** on `0005`: 719 passed, 3 failed, each also failing on your head:
  - B1306's slice D, the list's first entry;
  - harvest-debt's live run;
  - the day test, which passes alone.
