# Re-Run of `agy-002`'s Twenty-Three Planted Errors Against `B1881`'s Lock at `c40446392` (`M10`, Card `A2-R79d`)

- **Seat:** `agy-002` (`origin/agy-002/verify`)
- **Card closed:** `A2-R79d` (`relays/cards/AGY-002_A2-R79d_b1881-23-plants-at-c40446392.md`, committed and pushed at `6fb31fc42` **before** opening any file of `"frontier/B1881_the_whole_and_the_value_verified/"` or `"frontier/B1897_..."` at `c40446392`)
- **Commit of `main` tested:** `c40446392` (`"B1897"`, following `738be0e5f` and `644d5b40f`)
- **Pre-prose script and raw output:** `relays/r79d/run_b1881_23_plants_at_c40446392.py` and `relays/r79d/run_b1881_23_plants_at_c40446392_out.txt`, committed and pushed at `15debae82` ahead of this report (`build_cases()` imported directly from `relays/r79c/run_b1881_planted_errors.py` at `bfb11498c` with **zero** changes to any plant's mutation logic)
- **Method labels (`docs/seats/README.md` § 12):** `expectations committed first` (`6fb31fc42`) and `tested against planted errors` (`15debae82`)
- **Firewall (`docs/seats/README.md` § 9 item one):** `0 of 19`

---

## 1. Headline Answer in Plain Words

**Twenty-three of twenty-three (`all twenty-three`) planted errors are caught, and zero pass.**

1. **Controls (`two` of `two` behaved as required):**
   - **`CTL-CLEAN` (unmodified `c40446392` snapshot):** All **fifteen** lock tests in `"test_b1881_the_whole_and_the_value_verified.py"` passed (`fifteen` passed, `zero` failed).
   - **`CTL-KNOWN-FAIL` (cusp-width corruption in `census`):** Caught (`fourteen` passed, `one` failed: `test_the_two_quotients_recomputed`).
2. **Environment and comparison branch disclosed (`644d5b40f`):**
   - Local versions in `agy-002`'s environment are Python `three point twelve`, `mpmath` `one point three point zero`, and `sympy` `one point fourteen point zero`, matching `"whole_and_value_on_main_made_with.json"` in every field.
   - Accordingly, `test_the_committed_run_is_what_the_script_gives_today` executed the **exact byte-for-byte comparison branch** across both hash seeds (`one` and `two`); live execution under a differing `mpmath` or `sympy` version was not exercised here (`test_what_is_held_under_another_version_can_fail_and_lets_a_last_digit_be` passed its synthetic checks).
3. **`Group A` — Exact pre-existing `5c7f1879d` / `Row R17` plants (`five` of `five` caught, `zero` passed):**
   - `P01a` (`two` tests failed), `P01b` (`four` tests failed), `P02a` (`three` tests failed), `P02b` (`three` tests failed), and `P03` (`one` test failed).
4. **`Group B` — Blind pre-inspection adversarial plants from `41d0b7faa` (`eighteen` of `eighteen` caught, `zero` passed):**
   - All **twelve** previously caught direct reversions (`P04a`, `P04b`, `P05a_b1872`, `P05b`, `P06a`, `P06b`, `P06c`, `P07`, `P09a`, `P09c`, `P11a`, `P12`) remain caught (`one` to `three` failing tests each).
   - All **six** previously passing structural / evasion plants (`six` of `six`) are now caught on our exact unedited mutators:
     - **`P04c`** (separate unbracketed paragraph in `"FINDINGS.md"` using `"transpose"`): caught by `test_the_withdrawn_word_stands_only_where_it_is_taken_back` (`one` test failed; as `M10` and the lock's docstring state, restating a withdrawn claim *without* using the withdrawn word remains the general open class on `P-817`).
     - **`P05a_transpose`** (`keeps_line_main` function docstring calling the letters `"the transpose"`): caught by `test_the_withdrawn_word_stands_only_where_it_is_taken_back` (`one` test failed).
     - **`P08`** (typing the three sequence counts as integer literals in `"whole_and_value_on_main.py"` instead of computing them): caught independently by **both** `test_no_check_of_the_script_is_passed_a_constant` and `test_the_script_computes_what_it_says_it_computes` (`two` tests failed).
     - **`P09b`** (desynchronizing `"whole_and_value_on_main_run.txt"` counts and set formatting while leaving `.py` and `.json` intact): caught independently by **both** `test_the_committed_run_is_what_the_script_gives_today` and `test_what_is_held_under_another_version_can_fail_and_lets_a_last_digit_be` (`two` tests failed).
     - **`P10`** (appending non-literal tautology `or len(box) > zero` to `mirror_ok` and `single_ok` `check(...)` calls in `"whole_and_value_on_main.py"`): caught by `test_the_conditions_of_the_mended_checks_are_the_ones_that_were_mended` (`one` test failed).
     - **`P11b`** (dropping `sorted(v)` back to unsorted `over` on `E5` in `"whole_and_value_on_main.py"`): caught independently by **both** `test_the_committed_run_is_what_the_script_gives_today` and `test_the_conditions_of_the_mended_checks_are_the_ones_that_were_mended` (`two` tests failed).

0 of 19.
