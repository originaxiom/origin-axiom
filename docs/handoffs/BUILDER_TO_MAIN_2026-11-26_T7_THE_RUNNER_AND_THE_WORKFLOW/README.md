# T7 sent: the intake runner and its workflow (P-885)

**For main.** The advisor seat, 2026-11-26, at your M54 and § 9. One patch, applied after T1b and T6 on your `ed9660a9d`.

**[REBUILT 2026-11-26 on your `6f0f8fe45` (M60's head)]:** T1b, T6, T7, T8 and T9 apply in that order on a clean checkout of `6f0f8fe45`; this patch's tree is `4ef5b86652f109ea42d41d79036aadd1988153f0`, as built. The patch file is replaced; what follows was written on `ed9660a9d`, and its runs stand for the code that did not change. Its test cards carry the new `definitions:` line.

**Tried on a clean checkout of `ed9660a9d`:** T1b, T6 and T7 apply with `git am`. The tree is `1b12d47f4f66d174717b4374c6cca324883ff8d0`, as built.

## First, a rule this patch changes: yours to accept or refuse

`.gitignore` ignores `.github/` whole, and the gate tracked-forbidden refuses any tracked path under it. The ignore file's
comment says GOVERNANCE forbids tracking a CI workflow, but GOVERNANCE.md holds no such rule (a search for `.github`, CI,
workflow and Actions finds none); the ban stands in the comment and the gate.

§ 9, agreed by the author, puts the intake on GitHub Actions, and a workflow file must be tracked to run there. So this
patch allows exactly one path, `.github/workflows/intake.yml`:
- in `.gitignore`, by negations;
- in the gate, by `GITHUB_ALLOWED`.

Every other path under `.github/` is still ignored and refused, and a test shows both: the exemption removed fails it, and
the exemption widened to every workflow fails it. If you refuse the change, the workflow file stays out of the tree, and
the runner still runs by hand.

## What it carries

- **`scripts/queue/intake.py`:** one round of the intake, in this order:
  1. **Discovery and sighting:** new cards are filed FILED, and their card and decisive script are sighted at the same
     moment.
  2. **The form:** a refile the card does not declare is returned, as T3's note said it would be.
  3. **Custody.**
  4. **The record check,** attached under `queue/checks/Q<nnnn>.json`:
     - a retracted or superseded premise returns the card;
     - a premise card not VERIFIED keeps it FILED (D6);
     - the firewall's words are flagged in the round's report (A3).
  5. **The rerun:**
     - REPRODUCED, with `deciding` set from the record check;
     - RETURNED_AT_INTAKE, with its reasons;
     - or heavy, which keeps the card FILED for the author's machine.
  - **At most three reruns a round** (`--max-cards`), so a round stays inside the job's two hours.
  - **Nothing is written** unless the queue holds its schema and the log its form.
  - **A round that cannot cut the network stops** (exit 2). It runs only with `--allow-static-guard`, which the workflow
    never passes.
  - **By hand:** `python3 scripts/queue/intake.py --queue-dir <the queue/ folder of the queue's branch> [--write]`.
- **`.github/workflows/intake.yml`:**
  - **Triggers:** a schedule (every three hours, at minute 17) and the manual trigger. There is no pull-request trigger.
  - **Runners:** `ubuntu-latest` only. Top-level permissions: `contents: read`.
  - **Job `round`:** runs seat code, with read permission and no secret. Its checkout keeps no credentials. It fetches
    every seat branch, installs the allowed packages at their pins, runs one round, and uploads the queue's folder.
  - **Job `record`:** runs no seat code, and alone has `contents: write`. It checks the round's cards against the schema
    and the log's form, refuses a log that does not begin with the old one, commits to `queue`, checks the queue's history
    along that branch (`custody.py --history HEAD --root .`), and pushes to `queue` only.
- **`queue/README.md`:** the runner, and the six settings the author makes:
  1. the budget for Actions at $0;
  2. workflow permissions read-only by default;
  3. a ruleset on `main` that keeps the runner's token out (admin bypass only);
  4. a ruleset on `queue` blocking force-pushes and deletion (your M58.3);
  5. no pull-request trigger;
  6. reading "the network guard" in the first run's log.

  Main relays them, as you said.
- **`custody.py --root DIR`** reads another checkout's history; the record job needs it.

## What is not tried, said plainly

- **The workflow has not run.** I cannot run Actions from here, and a workflow on a branch other than the default one
  does not run on a schedule. Its first run will be on main, after you land it and the author makes the settings.
  - Its shape is tested as text (the repository has no YAML reader among its dependencies).
  - Its two scripts are tested by hand: the round on a repository built for it, the record job's checks in T1 and T4.
- **The namespace on hosted runners:** `unshare -rn` may be closed there and `sudo -n unshare -n` should work. The first
  run's log will say which, or the round stops by itself.
- **Action versions** are pinned by major tag (`actions/checkout@v4`, `setup-python@v5`, `upload-artifact@v4`,
  `download-artifact@v4`), not by commit hash. I did not want to write hashes I cannot check from here; pinning them is a
  later step worth taking.

## Runs

- **Its tests:** `tests/test_queue_intake.py` passes 5 of 5:
  - seven cards through one round, each moved as its checks decide;
  - a second round that changes nothing and sights nothing again;
  - a round that cannot cut the network;
  - the workflow's shape;
  - the one tracked workflow.

  With the queue's other tests: 46 of 46. The test files that read the registries, the logs, the views, the tracked files or `.github`: 641 passed, 3 failed, the same three as before.
- **Each rule removed, one at a time:** 12 breaks, each caught by one failing test:
  - custody;
  - D6's wait;
  - the A3 flag;
  - deciding;
  - the network refusal;
  - the heavy hold;
  - the sighting;
  - the workflow's top permission;
  - its credentials;
  - its triggers;
  - the exemption removed;
  - the exemption widened.
- **While building it, the test cards first all shared one script and one decisive line.** Discovery linked them as
  refiles of one another, which is your M57 key working as asked; the test now gives each card its own script.
- **Every gate on the commit:** 58, all green but harvest-debt (`GATES.txt`).
