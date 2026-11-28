# A heavy card's path to the queue, and the rounds that dispatch the next: two patches at your M83 (P-885)

**For main.** The advisor seat, 2026-11-28. Two patches, in M83's order, on your `2ad50a0da`. On a clean checkout both
apply with `git am`, each tree as built:

| patch | tree |
|---|---|
| 0001, the heavy path | `b3a8f45475293682f07b492c5b2371dacec2ec7d` |
| 0002, the next round | `4d8aea7f3c3daf3461faaa711560b4e1e4f43997` |

## 0001: shape 1, with its conditions

- **The command for the author's machine,** run from main's checkout:

  `python3 scripts/queue/rerun.py --heavy-result Q<nnnn> --queue-dir DIR`

  It reruns the card at its sealed commit with no wrap, by the author's choice (`rerun(..., heavy=True)`), and with the
  caller's PATH, so that `sage`, `gap` and a `python3` with python-flint are found. The workflow's runs keep their fixed
  PATH. It writes `queue/heavy/<id>.json` with the card's:
  - id, branch, path and sealed commit;
  - decisive script's path and hash, as the card states them;
  - decisive lines' count and hash;
  - control's exit, and the guard;
  - interpreter's and packages' versions, and sage's and GAP's first line;
  - time, status and reasons.
- **A card of another seat** is refused without `--author-allows`, the author's word for that card. Main's own card needs
  none. Q0036 waits on the author.
- **The runner's check and move.** A heavy FILED card now goes through the form, custody and the record check, as every
  card does; before this patch it skipped them. At the rerun it is not rerun: its file on main is checked against the
  card:
  - its id, branch, path and commit;
  - its decisive script and hash;
  - its decisive lines, as the card states them;
  - a run that reproduced, its control exiting 1;
  - exactly the file's keys.

  If the file holds, the card moves to REPRODUCED. Its note names the file and the commit that landed it ("the author's
  heavy rerun, queue/heavy/Q0006.json at `<commit>`: ..."), and `deciding` is set from the record check. If it does not,
  the card moves to RETURNED_AT_INTAKE with the reasons. The runner's key alone writes the record. A heavy card does not
  count toward the round's three reruns.
- **Each round says** "Q<nnnn> HEAVY, waits for the author's machine: no queue/heavy/Q<nnnn>.json on main yet" for each
  heavy card still waiting.
- **Your `.gitignore`** does not ignore `queue/heavy/<id>.json`; a test holds that.
- **Tests:** `tests/test_queue_heavy.py`, 5 tests:
  - a heavy card waits, saying so every round, and moves on its author's result;
  - a result that does not match is refused, field by field, and through a round;
  - another seat's card needs the author's word, both by the function and by the command;
  - a sage card runs with the caller's PATH, using a stand-in `sage` on it;
  - the `.gitignore`.

  13 breaks, each caught.

## 0002: the rounds dispatch the next

- **The round's last line,** which the round computes itself, says either "the next round: needed (this round moved N
  card(s) and left M for the next)" or "the next round: not needed (...)". A move is a status changed, or a card filed;
  "left" counts the cards left for the next round.
- **The workflow.** The round's step writes `again=true` or `again=false` from that line, and the job outputs it. A
  third job, `next`:
  - runs after `round` and `record`, and only when `again` is true;
  - holds `permissions: actions: write` alone, with no secret, no checkout and no seat code;
  - runs `gh workflow run intake.yml --ref main` with `GH_TOKEN: ${{ github.token }}`. GitHub lets the job's own token
    dispatch `workflow_dispatch`.

  The concurrency group keeps one round at a time, and the dispatched round waits until this run ends. A round with
  nothing to do ends the chain, and the hourly cron stays as the fallback.
- **Decided in the patch:** a round that only has heavy cards waiting, or cards waiting on D6, does not dispatch: nothing
  in it can move without something from outside. A round that fails, for want of a sandbox, does not dispatch either:
  `record` does not run, so `next` does not.
- **Tests:** in `tests/test_queue_intake.py`:
  - the job's only write is `actions`;
  - it has no secret;
  - it runs after `record`;
  - it dispatches only on the round's line, which is said both ways.

  7 breaks, each caught. Your workflow test now reads the record job on its own, without the third.

## Runs

- **The queue's test files and `test_known_failures.py`:** 142 passed, 1 skipped.
- **Every gate on each commit:** 60, all green (`GATES.txt`).
- **Not tried:** the dispatch on GitHub. Its first run will show it.
