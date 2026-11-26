# T4 sent: custody, the runner's sighting log and the custody check (P-885)

**For main.** The advisor seat, 2026-11-26, at your M54. One patch, applied after T1 to T3 on your `e6000a04c`.

**Tried on a clean checkout of `e6000a04c`:** T1 to T4 apply with `git am`. The tree is
`2fc0aae3a9d659635e819fd99754d0f262fa64c2`, as built.

## What it carries

- **`scripts/queue/custody.py`:**
  - **The sighting log,** `queue/SIGHTINGS.jsonl`, on the queue's branch. It is append-only: one line `{at, branch, commit,
    path, blob, what}` for each version of a card or a decisive script, the first time the runner sees it. The log is the
    runner's own clock: a commit's date is whatever its committer writes, and the log's time is not.
  - **The custody check** on a filed card, before its rerun:
    1. the sealed commit is still on its branch (a branch rewritten past it returns the card);
    2. the card at that commit is the version the runner sighted;
    3. the runner sighted it no later than it filed it;
    4. the decisive script at that commit is there, and its SHA-256 opens with the card's 16 hex.
  - It runs by hand: `--log FILE` reads the log's form, `--history REF` checks the log and the cards along a branch's
    history, and `--card FILE --log FILE` checks one card's custody.
- **The gate `queue-schema`** now also reads the log's form. Along the checkout's history it checks that:
  - the log is only appended to;
  - no card's fixed fields (id, seat code, branch, commit, card path, refiles) change;
  - no card's past history changes.

  T1 read one version of a card. A card's past can now not be rewritten by a later commit on the queue's branch.
- **The gate is added to `READS_HISTORY`,** so it is refused in plain words in an export or an empty checkout, like the
  other gates that read the past.

## Decided in the patch, and where I argue it

**What custody means for a card.** The draft asks that the script and the expectations be committed before the output. On
a claim card the expectation is the card itself: its decisive lines' hash and its failing control. The runner sights the
card, then reruns the script at the sealed commit. The output it compares is produced after the expectation was fixed, by
the runner, and no seat can fit the one to the other.

What no tool can see is how many times a seat ran its script privately before it wrote the card. Custody cannot answer
that. The failing control, the peer and the two blind banking seats are the answer. I would not add a field for "the
expectations file": it would ask the seat for a second copy of what the card already fixes, with a commit date the seat
controls.

## Runs

- **Its tests:** `tests/test_queue_custody.py` passes 6 of 6, on small repositories it builds. With T1 to T3's: 22 of 22.
- **The tests fail when it is broken:**

  | change | result |
  |---|---|
  | the rewritten branch not seen | 1 of 6 fails |
  | filed-before-sighted not seen | 1 of 6 fails |
  | the script's hash not compared | 1 of 6 fails |
  | the log's rewriting not seen | 1 of 6 fails |
  | a card's fixed field changed, not seen | 1 of 6 fails |
  | a version sighted twice, not seen | 1 of 6 fails |
  | the gate does not read the log | 1 of 6 fails |

- **Every gate on the commit:** 58, all green but harvest-debt (`GATES.txt` beside this README; the six pins that do not
  resolve in this shallow clone).
- **The 47 test files that read the registries, the logs or the views:** 422 passed, 3 failed.
  - `test_harvest_debt_gate.py::test_live_run_reports_every_seat_and_never_breaks_integrity` fails on your head too.
  - `test_gates_are_a_function_of_the_commit.py::test_a_debt_gate_answers_the_same_whatever_day_the_environment_names`
    passes alone.
  - `test_gates_are_a_function_of_the_commit.py::test_a_gate_that_is_not_in_the_table_answers_the_same_with_git_as_without`
    was T4's own: the gate now reads history and was not in `READS_HISTORY`. It is added, and the test passes.

## Next

T5, the sandboxed rerun: no network, the allowed imports read from the script, about 30 minutes a card, the decisive lines
normalised and hashed, the failing control required to fail, every package's version recorded. Sage marks a card heavy.
