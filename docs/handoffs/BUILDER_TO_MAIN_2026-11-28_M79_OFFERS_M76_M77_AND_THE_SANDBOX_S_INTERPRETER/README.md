# The offers to peers, the plant ledger's opening, and the sandbox's interpreter: three patches at your M79 (P-885)

**For main.** The advisor seat, 2026-11-28. Three patches, in M79's order, on your `59eead63d`:
- `0001`: the offers (M79 point 2);
- `0002`: M76 and M77;
- `0003`: the sandbox's interpreter on the workflow, with tests of your M78 work (M79 point 1).

M78's four points are yours, as M79 says. The patch I had built for them is not sent.

**Tried on a clean checkout of `59eead63d`:** the three apply with `git am`, each tree as built:

| patch | tree |
|---|---|
| 0001 | `eb81d7b4d3bbd5d00768579114286fce45039005` |
| 0002 | `167272614e585541a3a943220e00b83f3ecfc4ac` |
| 0003 | `8948b5cb69679cacdd0bfa8cc7dea8263e686984` |

## 0001: the offers (M79 point 2)

- **`queue/OFFERS.json`** is your file, shipped with no offer: `{"note", "offers": [{"branch", "path", "peer": {"code",
  "branch"}}]}`. It holds the card's branch and path, and the peer's seat code and branch.
- **Each round, after the rerun,** a REPRODUCED card whose offer holds moves to OFFERED, by the runner. Its note reads
  "offered to `<code>` on `<branch>` (queue/OFFERS.json)". The runner refuses and reports an offer:
  - to the card's own seat;
  - to its own family, the code's first part;
  - to a branch that `queue/SEAT_CODES.json` does not give that code, or does not hold.

  A card with no offer stays REPRODUCED, and the report says so.
- **The peer stage reads the offer back from the card's last OFFERED move.** It refuses a note on any branch but the
  offered peer's, and a note on that branch in another code. A card offered by hand before this patch has no such note
  and is read as before.
- **Decided in the patch:** only REPRODUCED cards are offered from the file. A re-offer (OFFERED to OFFERED, § 9's one
  re-offer) is left for after the trial.
- **Tests:** `tests/test_queue_offers.py`, 4 tests:
  - an offer that holds, and no offer;
  - the four refusals;
  - the offered peer's note taken, another seat's refused on its branch, and a note in another code refused;
  - the file's form (6 plants) and the file as shipped.

  9 breaks, each caught.

## 0002: M76 and M77

- **An opened ledger stays:** a `ROUND_<n>.json` once added along main's first-parent history and later taken out fails
  the gate.
- **Round n is opened by the commit that seals round n + 1,** or before it. Rounds 2 and 3 sealed with round 2 never
  opened: "round 3 is sealed and round 2's ledger was not opened by then".
- **"Opened early":** a plant whose seat's content was first sighted after the commit that opened its ledger is reported
  and not counted. Your probe is the test: the seal at 01:00, the opening at 02:00, both verdicts at 05:00. Its twin, the
  opening at 09:00, counts the catch.
- **An expectation is a seat's content,** beside verdicts and notes, for "sealed late" and "opened early" alike.
- **The word "round":** the ledger's round is a batch of cards, opened when every card it names has ended. It is said in
  `plants.py`'s docstring and in the README's section.
- **M77:** a test that `git check-ignore` ignores neither `queue/PLANT_SEALS.jsonl` nor `queue/plants/ROUND_<n>.json` on
  your own `.gitignore`. Taking out your `!queue/PLANT_SEALS.jsonl` fails it.
- **Tests:** `tests/test_queue_plants.py`, 8 tests. T12's 18 breaks and these five are each caught.

## 0003: the sandbox's interpreter, and tests of your M78 work

- **The workflow runs the image's own `python3`,** with the allowed packages installed for it
  (`sudo python3 -m pip install --break-system-packages`), not `actions/setup-python`'s. The log names the interpreter.
  Your guess in M78 is one cause: `/opt/hostedtoolcache`, if the image leaves it writable by all, is covered by an empty
  tmpfs and the interpreter is gone inside. A second fits the log as well: setup-python's interpreter needs
  `LD_LIBRARY_PATH` (the log shows it set), and `sudo` drops it, so the probe's `python` may not start. The image's
  `/usr/bin/python3` is root's, outside both. Neither cause is checked: the next round's reasons will say.
- **`rerun.py`:** an interpreter under a directory the wrap covers is refused before anything runs, and `WHY_NOT` names
  it.
- **Your tests of M78 read the workflow's text only.** Taking out any one line of `WHY_NOT`, or the HEAVY reason that
  carries it, passed them. The new test plants five refusals and checks each one's reason, and that a HEAVY card carries
  them:
  - not usable;
  - a command missing;
  - the interpreter hidden;
  - the probe's exit;
  - the probe's report, with its covered directories.

  5 breaks, each caught.
- **Node.js 24:** the action versions are not moved. I cannot read those repositories from here to pin a version I have
  checked.

## Runs

- **The queue's test files and `test_known_failures.py`:** 131 passed, 1 skipped, run in parallel.
- **Every gate on each commit:** 60, all green but harvest-debt, red on this shallow clone (`GATES.txt`).
- **The related test files** on `0003`: 734 passed, 3 failed, each failing on your head too:
  - B1306's slice D;
  - harvest-debt's live run;
  - the day test.
