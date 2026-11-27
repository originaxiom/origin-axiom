# T10 sent: the known failures may only shrink, a gate (known-failures) (P-885)

**For main.** The advisor seat, 2026-11-26, at your M54 and § 9's sixth decision. One patch, applied after T1b and T6 to
T9 on your `6f0f8fe45`.

**Tried on a clean checkout of `6f0f8fe45`:** T1b, T6 to T9, then T10, apply with `git am`. The tree is `a4f266cf6d392aecc9588862c8d28282e637ae95`, as
built.

**[REBUILT 2026-11-27 TO STAND ALONE on your `0df8d79a6`, at your M63]:** T10 no longer needs T7 to T9. It applies by
itself on a clean checkout of `0df8d79a6`; its tree is `a7fd218107beecf7892a97e2b0964d0490d10ab0`, as built. The patch file
is replaced. **It now carries your seven first entries**, each on P-810, with the reason M63 gives:
- B1306's slice D;
- B1421's partition;
- B1266's selftest;
- B1462's corrections;
- B1957's three.

Neither of the two that passed alone is on the list (B618, B1968); they are debts of their own on P-810. The lock checks
that the list holds seven tests on P-810 and no flake. Every gate on the commit: 59, all green but harvest-debt
(`GATES.txt`). The related test files: 463 passed and 4 failed, each failing on your `0df8d79a6` too: B1306's slice D (the
first entry), harvest-debt's live run, the day test, which passes alone, and `test_point_debt_gate.py`'s stale-point test,
which fails since the date rolled to 2026-11-27.

## What it carries

- **`queue/KNOWN_FAILURES.json`:** `{"tests": [...], "gates": [...]}`, each entry `{id, row, why}`. **It ships empty.**
  Its first entries are yours, from your own full suite on a fresh clone, each with the register row you give it. Here I
  can run only a part of the suite, and this clone is shallow, which turns harvest-debt red for want of six pins; neither
  is a list to bind main by.
- **`scripts/queue/baseline.py`:**
  - `--check`: the list's form, every entry naming a row of `docs/POINT_REGISTER.md`, and the list only shrinking along
    the history;
  - `--compare FAILURES [--gates RED]`: a run against the list. A failure or red gate the list does not hold is NEW, and
    the command exits 1, which is what the landing tool (T11) will refuse on. An entry that now passes is reported for
    taking off;
  - `--draft FAILURES [--gates RED]`: prints a list from a run, with `row` and `why` left as `?` for you. FAILURES is a
    file of test ids, one a line, as `pytest -rf` prints them after `FAILED `.
- **The gate `known-failures`:** fail-closed, in READS_HISTORY (it reads the list's past versions). It has a GATE_CONTROLS
  entry and a PRACTICES section.

## Decided in the patch

1. **A flaky test is not an entry.** The day test of `test_gates_are_a_function_of_the_commit.py` fails under load and
   passes alone. A list of known failures that held it would let a real failure of that test pass unseen. A flake is a
   debt of its own, for the register.
2. **Shrinking is checked along main's first-parent history,** as the append-only gate reads the log. A rebase that
   rewrote main's history would not be seen. Main's ruleset, in T7's README, refuses force-pushes for that reason too.
3. **The entry's row must exist in the register,** but its state is not read. A row closed while its test still fails is
   for the review to see.

## Runs

- **Its tests:** `tests/test_known_failures.py` passes 4 of 4:
  - a list with a row the register does not hold fails the gate, and its twin passes;
  - on a repository built for it, a list that shrinks passes and one that grows fails;
  - the list's form (6 plants);
  - a run compared with the list, both ways;
  - the commands by hand, and the list shipped empty.
- **Each rule removed, one at a time:** 5 breaks, each caught:
  - the shrink check;
  - the register row;
  - the new tests;
  - the new gates;
  - a duplicate entry.
- **Every gate on the commit:** 59 (the new one among them), all green but harvest-debt (`GATES.txt`).
- **The related test files:** 657 passed, 3 failed, the same three as before.

## Next

T11, the landing tool: the single writer of the arc, the lock, the ledger rows and the log pair. It takes the arc's number
at landing, and runs the gates and the suite on a fresh clone against this list, refusing otherwise.
