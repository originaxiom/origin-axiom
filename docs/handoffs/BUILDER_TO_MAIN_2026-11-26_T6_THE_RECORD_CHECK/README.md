# T6 sent: the record check, "deciding", the premise check (D6) and the firewall's flag (A3) (P-885)

**For main.** The advisor seat, 2026-11-26, at your M54 and M55. One patch, applied after T1b on your `ed9660a9d`.

**Tried on a clean checkout of `ed9660a9d`:** T1b, then T6, apply with `git am`. The tree is
`fc24db78f95bb71a4190ca92ce09bf62efc6f625`, as built.

## What it carries

**`scripts/queue/record_check.py`:** for one card, on the record in the checkout, the attachment the runner keeps with the
card:

| key | what |
|---|---|
| `terms` | the sweep's terms, the runner's own. They are the codes, register rows, identifications and arcs the card's `touches` and `premises on main` name, and the title's long words. The card's own sweep line is kept as `producer_sweep` and is not used |
| `topic` | `topic_sweep.py` on those terms: its VERDICT line, and the arcs and rows it names |
| `banked` | `already_banked.py` on the title's words: whether settled or scheduled material exists, and its last lines |
| `retracted` | every premise arc whose verdict is RETRACTED or that a later arc supersedes; every phrase of `RETRACTED_PHRASES.md` the card uses |
| `deciding` | true when the card touches a scoreboard code, an identification row, a register row or one of the 19 by name, and its effect is not none. It is computed, not declared |
| `waits_on` | door rule D6: the queue's cards (`Q<nnnn>`) among the premises that are not VERIFIED, including one the queue does not hold |
| `firewall` | the author's rule A3: words of a comparison with data or of a sealed look (PDG, CODATA, a measured or observed value, compared with or fitted to data, a sealed look, ±). A flag to the author |

It runs by hand: `python3 scripts/queue/record_check.py CARD.md [--queue DIR]` prints the attachment as JSON. On a card
it took about half a second here.

## Decided in the patch, and where I argue it

1. **The firewall is a flag, never a return.** A word list cannot tell a comparison from a mention ("no comparison with
   the PDG value is made" carries the word). Returning on it would return honest cards and teach producers to avoid the
   word, not the act. The plants should measure it: a planted comparison worded without the list's words is the fault
   the list will miss.
2. **An arc on main is not waited on (D6).** It is the record, and its own verdict is read under `retracted`. Only the
   queue's cards are waited on, and only until they are VERIFIED.
3. **"Deciding" reads the card's fields only.** My critique proposed also reading what the card's commit changes; that
   needs the runner's diff of the seat's branch, which belongs with T7. Until then, a card that touches a code without
   naming it is not caught, and a banking seat may re-class it.
4. **The check returns nothing by itself.** It attaches; the runner (T7) reads `retracted`, `waits_on` and `firewall`,
   and decides the move.

## Runs

- **Its tests:** `tests/test_queue_record_check.py` passes 6 of 6. They find a RETRACTED arc, a superseded arc and a
  retracted phrase on the record itself, so the test follows the record as it grows. With the queue's other tests: 41 of 41.
- **Each rule removed, one at a time:** 8 breaks, each caught by one failing test:
  - deciding on none;
  - the 19 by name;
  - D6's VERIFIED;
  - the RETRACTED premise;
  - the superseded premise;
  - the retracted phrase;
  - ± in the firewall's words;
  - the producer's sweep line used for terms.
- **Every gate on the commit:** 58, all green but harvest-debt (`GATES.txt`).
- **The test files that read the registries, the logs, the views or the tracked files:** 487 passed, 3 failed, the same
  three as before.

## Next

T7, the runner and the workflow:
- **`scripts/queue/intake.py`:** discovery, sighting, form, custody, rerun and record check in one command, and the moves
  they decide.
- **`.github/workflows/intake.yml`:** two jobs, the schedule and the manual trigger.
- **A README of the settings the author makes:**
  - the $0 budget;
  - main protected from the runner's token;
  - the queue's branch refusing a force-push (your M58.3);
  - "static guard only" refused on the workflow.
