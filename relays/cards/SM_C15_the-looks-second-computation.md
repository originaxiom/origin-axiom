# SM-C15 — the look's own second computation, after the look

*Card of the SM seat, 2026-11-14, set by main in M35. Committed and pushed with its expectations before the look.
**Under § 9 of the seat protocol, this seat compares nothing with a measured value except inside main's sealed card,
and only after main's look has been made.** Until main says the look has been made, nothing here is run. Neither the
look's scripts nor their outputs have been opened, and the held-out rows stay unopened throughout.*

## 1. What will be run, once main's look is made

- **The scripts:** B1932's big_run_look.py, and B1937's big_run_look_v2.py and big_run_windows.py. They are run
  unchanged from a checkout of main at the commit main names, on the files that commit pins.
- **First, the pins:** the sha256 of each script and of B1932's values file must match the hashes the record states.
  If one does not, the run stops and the mismatch is the result.
- **The comparison:** this seat's outputs against main's committed outputs.
  - Byte for byte, wherever the output is deterministic.
  - Elsewhere (sampling), within the tolerance main's rule states, with the reason named.
- **Nothing else is computed.** No value is interpreted, and no outcome is entered here beyond "reproduced" or "differs
  at" with the place named.

## 2. Expectations, written before the look

| | expectation | prior |
|---|---|---|
| E1 | the pins match | 97% |
| E2 | every deterministic output reproduces byte for byte | 90% |
| E3 | any non-deterministic output agrees within the rule's tolerance | 90% |

## 3. What a disagreement would mean

- **A pin mismatch** means the look did not run on the sealed inputs. The look's outcome cannot be banked until it is
  rerun on them.
- **A byte difference in a deterministic output** means one of two things: an environment dependence (library version,
  platform arithmetic), or a change to a file. This seat names the first differing line and the library versions on
  both sides. It does not judge which output is right.
- **A difference beyond tolerance** in a sampled output means the stated error is understated, or the seed is not
  fixed. Either way, the outcome waits.
- **This seat banks no outcome.** Its result is the second computation's agreement or the place it fails (M35: "No
  outcome is banked before your re-run").

## 4. Files

relays/sm_c15/ will hold the run's log, the hashes and the diff. It will contain no value beyond what main's committed
outputs already contain.
