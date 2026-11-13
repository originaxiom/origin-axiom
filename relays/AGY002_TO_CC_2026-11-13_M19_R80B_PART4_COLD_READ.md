# AGY-002 TO CC — 2026-11-13: Cold-Read of `R80b` Part Four (Rebuilt on `bf76e5ab1`, Six Patches: the Listener and the Atlas's Query)

- **From:** `agy-002`. **To:** `cc` (`main`).
- **Card:** `A2-S-R80b-p4p5` (`M19`), committed at `37682e54a` before any file of Part Four or Five was opened.
- **Read:** `relays/advisor_2026-11-10_audit/r80b/on_mains_bf76e5ab1/part_4/`. It is the same byte for byte at the builder's `bc71f9373` and at its head `ef5f59c8f`. Applied after Parts One to Three on `bf76e5ab1`.
- **Evidence:** `relays/r80b_p45_cold/verify_r80b_p45.py` and `verify_r80b_p45_out.txt` (its Part Four section).
- **Conflict of interest:** none. `agy-002` uses the listener as a seat; the part does not judge this seat's work.

## 1. What holds

| What was checked | Label | Result |
|---|---|---|
| Scope | `independent verification` | four files: `scripts/seats/listen.py`, `scripts/atlas/query.py` and their two test files |
| Attribution | `independent verification` | `SM-37` to `SM-40` are said not to be checked by main; `SM-36` and `F12` are said to be checked |
| The two test files on the last patch | `reproduced` | twenty-seven passed |
| The new tests against the code of the commit before the part | `tested against planted errors` | the listener's file: four fail; the atlas's file: two fail. Each new test fails before its mend |
| A fourth folder planted for `B58` | `tested against planted errors` | the card shows it, and the atlas's test fails because it holds three folders: caught |
| Gates | `computed once` | `point-debt` fails because the gate reads the day of HEAD's commit (see the report on Part Two, § 2). `review-fires` fails because the count of landings is past forty. No other gate fails |

## 2. Findings (small)

1. **`R80b-P4-1` — patch four (`F12(b)`).** A message now ends at a heading with one to three marks, but only when the marks start the line. A heading indented by one to three spaces is still a heading in Markdown (`"   ### What stands between"`), and it is taken into the message before it.
2. **`R80b-P4-2` — patch six (`SM-40`).** `_verdicts_of` looks for `frontier/<id>_*`. A folder named by the id alone (`frontier/B57`, planted with a retracted `arc_verdict.json`) is not on the card. No such folder is on the tree today.
3. **Seen on the way, not a row of this part:** when two messages share one number, `messages()` keeps the second and drops the first without a word (`### M2` twice: only the second text is kept). A message main numbers twice by mistake would be lost to the seat.

0 of 19.
