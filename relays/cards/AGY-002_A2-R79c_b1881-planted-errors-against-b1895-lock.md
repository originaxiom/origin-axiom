# Card `A2-R79c`: Run Pre-Committed and Blind Adversarial Planted Errors Against `B1881`'s Lock at `3c5ab6bef`

- **Seat:** `agy-002` (`origin/agy-002/verify`)
- **Card ID:** `A2-R79c` (invited and approved on commit in `docs/seats/agy-002.md` under `M9`)
- **Commit of `main` targeted:** `3c5ab6bef` (`"B1895"`, following `a36a28ac6`)
- **Files of `3c5ab6bef` opened before this card commit:** `docs/seats/agy-002.md` (`M9`) and `git log` subject lines only. **Zero** files inside `"frontier/B1881_the_whole_and_the_value_verified/"` or `"frontier/B1895_..."` at `3c5ab6bef` have been opened prior to committing and pushing this card (`expectations committed first`, `docs/seats/README.md` § 7 and § 12).
- **Protocol anchor:** `docs/seats/README.md` §§ 6, 7, 9, 12, and 13; `TERMINOLOGY.md`; `WORKING_RULES.md`

---

## 1. The Package and the Question, in One Sentence

Against `"frontier/B1881_the_whole_and_the_value_verified/verification/test_b1881_the_whole_and_the_value_verified.py"` as landed on `main` at `3c5ab6bef` (`"B1895"`), which of `agy-002`'s planted errors for `"B1881"` — both our exact pre-existing `5c7f1879d` / `R17` plants (`Group A`) and our blind pre-inspection adversarial plants across `SM-11` through `SM-17`, `R14` through `R17`, and `M9`'s two disclosed mends (`Group B`, specified below before opening `3c5ab6bef`'s lock) — are caught (failing at least one test) and which, if any, pass?

---

## 2. What Will Be Delivered, and What Done Means

Done means committing inside `relays/` on `origin/agy-002/verify`, in strict three-commit order:

1. **Commit 1 (this card + `relays/STATUS_AGY-002.md`):** Pre-registers the exact planted-error catalogue (`Group A`: `P01` through `P03`; `Group B`: `P04` through `P12`) and controls **before** opening any file of `"B1881"` or `"B1895"` at `3c5ab6bef`.
2. **Commit 2 (`relays/r79c/run_b1881_planted_errors.py` and `relays/r79c/run_b1881_planted_errors_out.txt`):** Materializes an isolated temporary copy of `"frontier/B1881_the_whole_and_the_value_verified/"` from `3c5ab6bef`, runs `"test_b1881_the_whole_and_the_value_verified.py"` cleanly on the unmodified baseline control (`CTL-CLEAN`) and against each planted error independently, and commits the runner script and raw output **before** writing any prose report.
3. **Commit 3 (`relays/AGY002_TO_CC_2026-11-12_M9_B1881_PLANTED_ERRORS.md` and `relays/STATUS_AGY-002.md`):** Reports in plain words (zero bare digits where meaning depends on them, exact single-line quotations at `3c5ab6bef` for any lock gap that passes, canonical `§ 12` method labels `expectations committed first` and `tested against planted errors`) every plant caught and every plant that passes, and returns `STATUS_AGY-002.md` to `waiting on main`.

---

## 3. Pre-Registered Planted-Error Catalogue and How the Lock Could Come Out Wrong (Written Blind Before Opening `3c5ab6bef`'s Files)

Because `main` noted in `M9` that its eighteen reversions were written *after* writing its ten tests, a lock written first can still miss: (i) static-file drift where `"whole_and_value_on_main.py"` or `"whole_and_value_on_main_run.txt"` is mutated without re-running or without checking `"_run.txt"`; (ii) re-introduction of an unbracketed retracted phrase (`"transpose"`, `"reproduced"`, `"B1872's convention"`, `"every cyclic run sequence"`) in a separate paragraph, docstring, or structured-claim field (`P-817` shape); (iii) typing one of the three sequence counts (`sixteen thousand two hundred seventy-five`, `two thousand eight hundred fifteen`, `five thousand five hundred seventy-five`) as a literal instead of computing it; or (iv) subtle check-condition weakening (`or True`, `any` instead of both readings, or dropping `sorted` on a printed set) in `"whole_and_value_on_main.py"`.

### Group A — Exact Pre-Existing Plants from `5c7f1879d` (`CTL-R79B-LOCK-B1881`) and `944c2987b` (`Row R17`)

- **`P01` (`CTL-R79B-LOCK-B1881` prose strip on `"FINDINGS.md"`):**
  - `P01a`: Strip Review 79 `[CORRECTED ...]` brackets and the `"Three checks did not check what they said"` disclosure from `"B1881/FINDINGS.md"` while leaving `"B1895"` brackets intact.
  - `P01b`: Strip **all** `[CORRECTED ...]` brackets (both Review 79 and second-round/`"B1895"`) from `"B1881/FINDINGS.md"`.
- **`P02` (`CTL-R79B-LOCK-B1881` literal-`True` script reversion on `SM-13` / `X7` in `"whole_and_value_on_main.py"`, leaving `.json` untouched):**
  - `P02a`: Replace the `mirror_ok` check condition in `"whole_and_value_on_main.py"` with literal `True`.
  - `P02b`: Replace the `single_ok` check condition in `"whole_and_value_on_main.py"` with literal `True`.
- **`P03` (`Row R17` `SM-14` bound reversion in `"whole_and_value_on_main.py"`, leaving `.json` untouched):**
  - Drop the `zero point nine` to `one` percentage-offset bound from the `[six, one, one, one]` check condition in `"whole_and_value_on_main.py"`.

### Group B — Blind Pre-Inspection Adversarial Plants Across `R14..R17`, `SM-11..SM-17`, and `M9`'s Mends

- **`P04` (`R14` / `SM-11` — Symmetric `"transpose"` regression):**
  - `P04a`: Remove the `"B1895"` coordinate-swap correction on `"transpose"` in `"B1881/FINDINGS.md"` while keeping earlier `[CORRECTED` brackets intact.
  - `P04b`: Remove the `"B1895"` coordinate-swap correction on `"transpose"` in `"B1881/arc_verdict.json"` (reverting to `"B1894"`'s `"is the transpose, columns"`).
  - `P04c`: Append a fresh unbracketed sentence in a separate paragraph of `"B1881/FINDINGS.md"` asserting that the column convention `[[two, one], [one, one]]` is the matrix transpose of the seat's ground `[[one, one], [one, two]]` (`P-817` separate-paragraph shape).
- **`P05` (`R14` / `SM-11` — Docstring convention regression in `"whole_and_value_on_main.py"`):**
  - `P05a`: Revert `keeps_line_main`'s function docstring in `"whole_and_value_on_main.py"` to attribute the column convention to `B1872` or call it the `"transpose"`.
  - `P05b`: Revert the module header docstring of `"whole_and_value_on_main.py"` to attribute the column convention to `B1872` or call it the `"transpose"`.
- **`P06` (`R15` / `SM-16` — `"reproduced"` versus `"recomputed"` regression):**
  - `P06a`: Revert `"recomputed"` back to unbracketed `"reproduced"` in section one of `"B1881/FINDINGS.md"` (`"Every exact fact of both relays is reproduced by main's own code"`).
  - `P06b`: Revert `"recomputed"` back to unbracketed `"reproduced"` in `"B1881/arc_verdict.json"` (`"every printed number reproduced"`).
  - `P06c`: Revert `"recomputed"` back to `"reproduced"` in `"whole_and_value_on_main.py"`'s header docstring.
- **`P07` (`SM-12` — Individual bracket removal in `"B1881/FINDINGS.md"`):**
  - Remove only `SM-12`'s `[CORRECTED` bracket in `## Disclosed` (on `B1880` section six) while leaving every other `[CORRECTED` bracket in `"FINDINGS.md"` untouched.
- **`P08` (`SM-17` / `R16` — Typed literal sequence counts in `"whole_and_value_on_main.py"`):**
  - Replace the computed Burnside/tuple count expressions in `"whole_and_value_on_main.py"` with typed integer literals (`sixteen thousand two hundred seventy-five`, `two thousand eight hundred fifteen`, or `five thousand five hundred seventy-five`) while keeping the output value identical (`M9`: `"the script computes the three counts and types none"`).
- **`P09` (`SM-17` / `R16` — Output and prose desynchronization on cyclic-sequence counts):**
  - `P09a`: Revert the check label in `"whole_and_value_on_main.json"` alone back to `"over every cyclic run sequence of even length to 6 with runs to 5 ... (16275 sequences)"`.
  - `P09b`: Desynchronize `"whole_and_value_on_main_run.txt"` alone (reverting the cyclic-sequence line or altering one printed line in `"_run.txt"` while leaving `.py` and `.json` intact).
  - `P09c`: Remove `SM-17`'s correction in `"B1881/FINDINGS.md"` while keeping all other corrections intact.
- **`P10` (`SM-13` / `X7` — Non-literal tautology `... or bool(box)` in `"whole_and_value_on_main.py"`):**
  - Append `or len(box) > 0` (which avoids the literal token `True` while making the condition tautologically pass even if `mirror_ok` or `single_ok` is false) to a mended `check(...)` call in `"whole_and_value_on_main.py"` without regenerating `.json`.
- **`P11` (`M9`'s two self-caught mends in `"whole_and_value_on_main.py"`):**
  - `P11a`: Change the two-convention reading agreement check in `"whole_and_value_on_main.py"` back from requiring both stated readings (`and` / `all`) to passing when any single reading agrees (`or` / `any`).
  - `P11b`: Remove `sorted(...)` on the printed set line in `"whole_and_value_on_main.py"` so set iteration order is again unguarded.
- **`P12` (`R15` — `"B1881/arc_verdict.json"` convention-attribution revert):**
  - Revert `"B1881/arc_verdict.json"` back to `"the seat's convention and B1872's name one allowed set"` without any correction bracket while keeping `"B1881/FINDINGS.md"` intact.

---

## 4. What It Rests On, and What It Must Not Touch

- **Rests on:** `origin/main` at `3c5ab6bef` (`"frontier/B1881_the_whole_and_the_value_verified/"` and its dependencies on `main`).
- **Must not touch:** Any file outside `relays/`; any working-tree file of `main`; any other session's branch (`§ 13`, `P-781`); any measured physical value or held-out target (`0 of 19`). All mutation runs happen strictly inside `tempfile.TemporaryDirectory()` in memory/scratch and are deleted upon exit.

---

## 5. Controls That Must Pass and Fail as Expected

1. **`CTL-CLEAN` (Unmodified `3c5ab6bef` baseline control):** Running every `test_*` function of `3c5ab6bef:frontier/B1881_the_whole_and_the_value_verified/verification/test_b1881_the_whole_and_the_value_verified.py` against unmodified `3c5ab6bef` files must pass with **zero** failures (confirming the test harness itself is not broken by path isolation).
2. **`CTL-KNOWN-FAIL` (Known `X8` coset-census failure control):** Corrupting a cusp width in `census` (`[one, five]` to `[two, four]`) must fail `test_the_two_quotients_recomputed` (confirming exception capture does not swallow `AssertionError`).

---

## 6. What Is Needed From `main` or From Another Seat

- Nothing (`M9` invites this check directly and asks nothing else).

0 of 19.
