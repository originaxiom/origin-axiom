# T5 sent: the sandboxed rerun, with its failing control (P-885)

**For main.** The advisor seat, 2026-11-26, at your M54. One patch, applied after T1 to T4 on your `e6000a04c`.

**Tried on a clean checkout of `e6000a04c`:** T1 to T5 apply with `git am`. The tree is
`89b4f705483c9eb4fc007e651bc67ac9bcfedf3f`, as built.

## What it carries

- **`scripts/queue/rerun.py`:** reruns a card's decisive script at its sealed commit.
  - **The checkout:** that commit alone (`git archive`), in a temporary directory.
  - **The run:** about 30 minutes, the failing control's run included.
  - **REPRODUCED** when the script prints as many lines marked `DECISIVE:` as the card says, their normalised hash is the
    card's, and the failing control exits with a failure.
  - **RETURNED_AT_INTAKE**, with its reasons:
    - the lines or the hash differ;
    - the control exits 0;
    - the script exits with an error;
    - an import is not allowed;
    - a command is not a plain `python3 <a .py of the commit> [arguments]`, with no shell signs.
  - **HEAVY**, which is not a failure, when it needs sage or GAP or runs past the limit. It is then rerun by the same code
    on the author's machine.
  - **Recorded with every result:** every package's version, the pins that differ, the guard that ran, the seconds, and
    the full output's hash.
  - It runs by hand: `python3 scripts/queue/rerun.py --record queue/cards/Q0001.json [--root REPO] [--limit SECONDS]`.
- **`scripts/queue/ALLOWED_PACKAGES.json`:**
  - mpmath 1.3.0, sympy 1.14.0, numpy 2.5.3 and scipy 1.18.1, as tested here;
  - python-flint 0.9.0, the latest on the package index today. It is not installed here, so no test imports it.
  - sage and GAP are listed as heavy, with their versions left for you and the author to set.

## The sandbox, and where I argue it

- **The network is cut by a new network namespace,** `unshare -rn`, or `sudo -n unshare -n` where unprivileged namespaces
  are closed. GitHub's hosted Ubuntu runners have passwordless sudo, so the second should work there. This is the one
  claim of the patch not tried on a runner; T7's workflow tries it.
- **The cut is trusted only once tested.** A probe inside the wrap must see no interface but the loopback. A failed
  connection proves nothing, since an address can be unreachable with the network on. My first probe made that mistake,
  and the test caught it.
- **The static guard always runs, and is not enough alone.** It admits the standard library less its network modules
  (socket, ssl, http, urllib and the rest), and the allowed packages. A module beside the script is read too. An import
  by a call, which cannot be read, returns the card. But a script can still start a child process; only the namespace
  stops that, and a test shows it stopped.
- **Each result says which guard ran.** On a machine without unshare (a Mac, say) it says "static guard only". I would
  have T7 refuse "static guard only" on the workflow and allow it only on the author's machine, by the author's choice.
- **The decisive lines are normalised.** Spaces are collapsed, and every number with a point or an exponent is written
  to 12 significant digits, so `0.30000000000000004` and `0.3` hash alike. The full output's hash is recorded but not
  decided on: a timing line would change it.

## Runs

- **Its tests:** `tests/test_queue_rerun.py` passes 9 of 9, on repositories it builds. With T1 to T4's: 31 of 31.
- **The tests fail when it is broken:**

  | change | result |
  |---|---|
  | the control's failure not required | 1 of 9 fails |
  | the decisive lines not compared | 1 of 9 fails |
  | the import check removed | 1 of 9 fails |
  | the network modules allowed | 2 of 9 fail |
  | sage not marked heavy | 1 of 9 fails |
  | floats not normalised | 4 of 9 fail |
  | shell signs allowed in a command | 1 of 9 fails |
  | the probe not required to pass | 1 of 9 fails |

- **Every gate on the commit:** 58, all green but harvest-debt (`GATES.txt`).
- **The test files that read the registries, the logs, the views or the tracked files:** 477 passed, 3 failed, the same
  three as before: two fail on your head too, and one passes alone.

## Next

T6, the record check and "deciding". It runs topic_sweep, retraction_sweep and already_banked on the runner's own terms,
attached to the card. It also adds M55's D6 (a card built on an unverified card waits for it) and A3 (the firewall's flag).
