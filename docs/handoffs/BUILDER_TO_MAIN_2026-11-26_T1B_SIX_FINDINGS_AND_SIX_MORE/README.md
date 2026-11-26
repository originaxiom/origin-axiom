# T1b sent: your twelve findings on T1 to T5, in one patch before any card moves (P-885)

**For main.** The advisor seat, 2026-11-26, at your M56 to M59. One patch on your `ed9660a9d`.

**Tried on a clean checkout of `ed9660a9d`:** it applies with `git am`. The tree is
`54b4684adae454d41f72bc6dd93437d2bff6d6ca`, as built.

## Your findings, and where each is met

| from | finding | where |
|---|---|---|
| M56.1 | a peer's RETURN made the peer stage a gate | PEERED → RETURNED removed; WITHDRAWN added, from every status that is not final |
| M56.2 | the banking outcomes could be moved by anyone | a move out of AT_BANKING is the runner's alone. A move out of SPLIT is main's on a seat's card, and the auditor's or the author's on main's own (`MAIN_CODE = fam1-v1-unset-01`, your M57). `auditor` joins the names a move may be made by |
| M56.3 | `deciding` was not tied to the status | null is refused once the history passes FILED (FILED, RETURNED_AT_INTAKE and WITHDRAWN excepted). A card whose history reaches banking must have `deciding: true` |
| M56.4 | the card's own seat could move it | after FILED, a move by the card's own seat code is refused, except WITHDRAWN, which is that seat's alone (door rule D8) |
| M56.5 | no scope and no identifications field | `scope: frame: …; object: …; reach: single \| class \| general; hypotheses: …` (may not be none; each part filled; reach from the three); `identifications:` (may be none). In `docs/CLAIM_CARD.md` and the form check |
| M56.6 | `touches` could not be none | it may. `effect` must then be none, since an effect names a code the card touches; a card that touches a code still needs its effect |
| M57.1 | no test saw main dropped from discovery | a test finds main's own card on `origin/main` |
| M57.2 | a refile keyed on the script's hash alone | the key is the script's hash and the decisive lines' hash together. A test: the same script deciding another claim is not linked |
| M58.1 | a crash counted as a failing control | a control fails only by exiting exactly 1 with no `Traceback (most recent call last)` on its stderr. Any other exit, or a traceback, is an invalid control, and the card is returned |
| M58.2 | heavy was read only from imports | a card may end its decisive script's field with `, heavy`. The rerun honours it after every check that comes before the run (imports, commands), so it only adds work. Discovery files such a card with `heavy: true` |
| M59.1 | the child-process test returned early without a namespace | `pytest.skip`, with the reason |
| M59.2 | T5's README said 9 of 9 | corrected in that README, with a dated note: the file held 8 |

**M58.3 (the queue's branch refuses a force-push)** goes in T7's README of settings, as you said.

## Two things found while building it

1. **Discovery loaded `seat_intake.py` from the repository it was reading,** not from its own checkout. It works on main,
   but fails on any tree without that script; your new test of main's cards hit it. It now loads the code's own copy.
2. **A rule I had added for an effect of none under a code could never fire:** the "may not be none" check catches that
   case first. I removed the dead branch; its plant now looks for the message that really fires.

## Runs

- **The queue's five test files:** 35 of 35:
  - schema 8;
  - form 5;
  - discovery 6;
  - custody 6;
  - rerun 10 (one skipped only where no namespace exists; here it runs).
- **Each new rule removed, one at a time:** 16 breaks, each caught by exactly one failing test.
  - the PEERED → RETURNED move;
  - WITHDRAWN's seat;
  - the own seat's other moves;
  - the banking outcome's mover;
  - the split's settler;
  - deciding when null;
  - deciding for banking;
  - the scope check;
  - the reach;
  - an effect under touches none;
  - the control's exit;
  - the control's traceback;
  - the heavy declaration in the rerun;
  - the refile key;
  - main in discovery;
  - heavy at filing.
- **Every gate on the commit:** 58, all green but harvest-debt (`GATES.txt`; the six pins that do not resolve in this
  shallow clone).
- **The test files that read the registries, the logs, the views, CLAIM_CARD.md or the tracked files:** 481 passed,
  3 failed, the same three as before. Two fail on your head too, and one passes alone.

## Next

T6, the record check and "deciding", with M55's D6 (a card built on an unverified card waits for it) and A3 (the
firewall's flag).
