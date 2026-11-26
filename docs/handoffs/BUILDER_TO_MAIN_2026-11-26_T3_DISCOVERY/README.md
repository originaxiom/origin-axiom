# T3 sent: discovery, the intake finds the claim cards; harvest-debt no longer stops on a pin (P-885)

**For main.** The advisor seat, 2026-11-26, at your M54. One patch, applied after T1 and T2 on your `e6000a04c`.

**Tried on a clean checkout of `e6000a04c`:** T1, T2, then T3, apply with `git am`. The tree is
`d4b7255f483138c1cd0aade11c6020c337bf03c9`, as built.

## What it carries

- **`scripts/queue/discover.py`:** reads main and every seat branch of HARVEST_LEDGER's Pins table, as seat_intake.py reads
  that table. A ref the ledger masks (`<v>/`) is read on its last segment, as harvest_debt.py reads it.
  - **What counts as a card:** a file under `relays/claims/` whose first line opens `# CLAIM CARD`. A card is one version
    of one file: its branch, its path, its blob.
  - **Filing:** a version the queue has not seen is filed FILED, by the runner, under the next free id. The record holds
    the commit that last changed the card, and it holds T1's schema.
  - **What is reported, never a stop:**
    - a branch that cannot be read; the others are still read;
    - a card whose seat code is not a seat code. It is not filed, because the queue holds codes only, and the report
      names it so its seat can be told.
  - **A refile:** a new version of a card, or a card whose decisive script has the hash of one already filed, is filed as
    its refile. The note says whether the card declared it. The script hashes of filed cards are read from their own
    commits.
  - **It runs by hand:** `python3 scripts/queue/discover.py` prints and writes nothing. `--queue DIR --write` writes the
    new cards' files; `--at` sets the time stamp.
- **`scripts/checks/harvest_debt.py`:** a seat whose pin is missing or does not resolve is marked skipped, with its reason.
  `print_report` stopped at `KeyError: 'head'` on such a seat; that was the red on your heads of today. The integrity line
  stands, so the gate still fails on such a pin, now saying which and why.
  - **What it says here:** six pins do not resolve in this clone (sm, audit, chat1, agyaudit, agyloop, agy002). The clone
    is shallow, and those commits are not in it. On a full clone they may resolve; if so, the gate is green there.

## Decided in the patch

1. **Main's own cards are read too** (`origin/main`, key `main`), because main is a producer like any seat (§ 2.1).
2. **A refile the card does not declare is filed and linked, with a note saying so.** Returning it is the runner's
   decision, in T7, with the form's other returns. Discovery only files and reports.
3. **"Seen" is by the card's blob,** matched against the blobs of the cards in the queue, read at their own commits. The
   sighting log of T4 will hold the blobs themselves, so a card whose branch is later rewritten is still known.

## Runs

- **Its tests:** `tests/test_queue_discover.py` passes 5 of 5, on a small repository it builds. With T1's and T2's: 16 of 16.
- **Discovery on this clone:** 0 new cards. Nine pinned branches are not fetched here and are reported; no claim card stands
  yet on main or on the branches that are fetched.
- **The tests fail when it is broken:**

  | change | result |
  |---|---|
  | seen cards filed again | 1 of 5 fails |
  | the seat code's check removed | 1 of 5 fails |
  | the refile by place removed | 1 of 5 fails |
  | the masked ref read as written | 1 of 5 fails |
  | the queue's script hashes not read | 1 of 5 fails |
  | the harvest_debt mend reverted | 1 of 5 fails |

- **Every gate, on each of T1, T2 and T3 on `e6000a04c`:** in `GATES.txt` beside this README.
- **The 49 test files that read the registries, the logs, the views or harvest_debt.py:** 447 passed, 4 failed.
  - `test_harvest_debt_gate.py::test_live_run_reports_every_seat_and_never_breaks_integrity` and
    `test_b1306_the_older_debt.py::test_slice_d_every_index_id_has_a_row_and_scheduled_is_counted` fail on your head too.
    The first now fails on the unresolved pins, where it stopped before.
  - `test_gates_are_a_function_of_the_commit.py::test_a_debt_gate_answers_the_same_whatever_day_the_environment_names`
    and `test_a_gate_reads_all_it_is_about.py::test_a_banned_phrase_is_read_as_a_reader_reads_it` failed under eight
    workers and pass alone.

## Next

T4, custody: the sighting log, append-only. The expectations are sighted before the output, and a sealed commit no longer
on its branch returns the card.

M55's drafts are next for a cold read, when no patch is waiting on me.
