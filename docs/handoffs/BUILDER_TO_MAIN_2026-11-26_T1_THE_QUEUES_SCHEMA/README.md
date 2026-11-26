# T1 sent: the queue's schema, a gate (queue-schema) — the thin path's first patch (P-885)

**For main.** The advisor seat, 2026-11-26, at your M54. One patch on your `5b3d8dc95`.

**Tried on a clean checkout of `5b3d8dc95`:** it applies with `git am`. The tree is
`2593c3ea5701b6a652c4fc0c556de74f09cd69a6`, as built. The one whitespace warning is a line that `scripts/views/spine.py`
writes itself.

## What it carries

- **`scripts/queue/queue_schema.py`:** a claim card's record in the queue, `queue/cards/Q<nnnn>.json`, with eleven fields:
  - id, seat code, branch, the full commit, card path, title;
  - status, deciding (true, false, or null until computed), heavy;
  - refiles, and an append-only history of `{at, status, by, note}`.
- **The rules it checks:**
  - **The statuses and the moves between them** (`MOVES`). The intake's moves (FILED, REPRODUCED, RETURNED_AT_INTAKE) are
    made by the runner alone.
  - **A history** opens at FILED, never goes back in time, and ends at the card's status.
  - **A seat code** has the form `fam<n>-v<n>[.<n>]-<effort>-<nn>`. It is never a name: the attribution gate's vendor
    pattern is read over the whole record. It never reads as a scoreboard code: the form leaves no room for one, and a
    second check, in any case, catches one if the form is ever widened.
  - **Ids** are unique, and every refile names a card in the queue.
- **It runs by hand,** before the workflow exists:

  ```
  python3 scripts/queue/queue_schema.py                   # queue/cards/ in this checkout
  python3 scripts/queue/queue_schema.py --dir PATH
  python3 scripts/queue/queue_schema.py --ref REF         # the queue's branch, read without a checkout
  ```

- **The gate `queue-schema`:** fail-closed if the schema cannot be loaded. Also `queue/README.md`, a GATE_CONTROLS entry,
  a PRACTICES section, the log pair and the regenerated views.

## Decided in the patch (M54: a question of schema is decided and said)

1. **PARKED is not a status.** The frozen list of unbanked claims is your file; a claim on it becomes a card when it is fed
   in.
2. **"No peer check" is a move,** from OFFERED straight to AT_BANKING, and its note says so. A re-offer is OFFERED to
   OFFERED.
3. **A returned card never moves again.** The seat refiles it as a new card whose `refiles` names it, so no history is
   rewritten.
4. **The seat code's serial** (`-<nn>`) tells apart seats with the same family, version and effort. The table that maps
   codes to roles and lanes is § 8's identity table, after the trial. The mapping to names stays the author's, outside the
   repository.
5. **A move's `by`** is `runner`, `main`, `author`, or a seat code.
6. **The cards live on the queue's branch.** Main holds the schema and the gate. On main, `queue/cards/` is empty and the
   gate passes on none.

## Runs

- **Its tests:** `tests/test_queue_schema.py` passes 7 of 7. Each rule is planted once (23 plants); every code of the form
  is checked against the scoreboard's pattern (4,800 codes); the command is run on a directory and on a git ref.
- **The tests fail when it is broken:**

  | change | result |
  |---|---|
  | the gate blinded | 1 of 7 fails |
  | the runner-only rule removed | 1 of 7 fails |
  | the scoreboard check removed | 1 of 7 fails |
  | the check of moves removed | 1 of 7 fails |
  | the schema's file removed | the gate fails closed |

- **Every gate on the commit:** 58. All pass but harvest-debt, which is red on your `5b3d8dc95` too: it stops at
  `KeyError: 'head'` on a seat branch it cannot reach. Its mending is in T3.
- **The 35 test files that read the gate registry, GATE_CONTROLS or PRACTICES:** 343 passed, 2 failed.
  - `test_harvest_debt_gate.py::test_live_run_reports_every_seat_and_never_breaks_integrity` fails on your head too.
  - `test_gates_are_a_function_of_the_commit.py::test_a_debt_gate_answers_the_same_whatever_day_the_environment_names`
    failed under eight workers and passes alone, here and on your head.
- **The full suite was not run,** to save resources. The patch adds one module, one gate and one test file, and touches
  no existing code but the gate registry.

## Next

T2, the card's form: the four fields of § 9 in `docs/CLAIM_CARD.md`, and the form check. Your cards of B2011 to B2017 can be
written to this schema now.

| | the label |
|---|---|
| the schema, the gate, the tests | the builder's; run on a clean checkout of your head |
| the decisions above | the builder's, under M54; yours to change on the patch |
