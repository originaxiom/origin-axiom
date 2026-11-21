# Card AGY-C18: Pre-Registered Zero-Knob Blind Prediction Seal, Matched-Null Power Audit, and Comparator Card Proposal

1. **The package and the question, in a sentence:** Under `AGY-C16`, `AGY-C17`, `THE_BAR`, `CROSSING_REQUIREMENTS` (`R1-R12`), and `INPUT_COMPLETENESS_LEDGER` (`Items 1-13`), can the zero-continuous-knob `22`-observable `UV -> IR` pipeline be sealed at `40`-digit precision with certified data-free matched-null specificity (`< 1/100`), location-free `5%`-noise power (`> 1/10`), zero `FITTED` continuous parameters, and a complete `P-406` Frame & Comparator Card ready for separated-seat evaluation?

2. **What will be delivered, and what done means:** A pre-registered, hashed `0 of 19` script `relays/agy_2026-11-21_c18/c18_blind_prediction_seal_and_matched_null.py`, locked `JSON` artifact `blind_predictions_zero_knob_v1.json`, raw output, a zero-shared-code countercheck `c18_countercheck.py` with five planted negative controls, and a mask-clean Frame & Comparator Card relay testing:
   - **Expectation E1 (`40`-Digit Zero-Knob `2`-Arm Blind Prediction Seal & Step-Halving Precision Budget `R6`):** Evaluate Primary Arm `A` (`t_{EW} = -48 pi / 5`) and Sensitivity Arm `B` (`t_{EW} = -10 pi`) at `40` digits (`with step-halving ODE discretization residual < 10^{-8}` across all `22` dimensionless `IR` observables, far tighter than any `1%` theoretical/experimental band), emit `blind_predictions_zero_knob_v1.json` with embedded `SHA-256` seal, and verify `0` `FITTED` continuous inputs (`every constant in the RHS and boundary conditions is an exact rational or rational multiple of pi`).
   - **Expectation E2 (Data-Free `2,000`-World Matched-Null Specificity `X2` & Location-Free Power Screen):** Across `2,000` synthetic Haar-mixing and log-uniform hierarchy null worlds (`strictly 0 of 19, taking the best-of-two-arms minimum distance per null world per THE_BAR`), verify that the `2`-arm menu's joint `20%`-band false-positive rate satisfies `p_{null} < 1/1000 < 1/100` (`passing X2 specificity`), while `500` synthetic `5%`-perturbed signal worlds achieve location-free joint recovery power `> 9/10 > 1/10` (`passing THE_BAR's unspent-target power floor`).
   - **Expectation E3 (Mechanical `P-406` Frame Card, `R1-R12` + `13`-Item Input-Completeness Validator, & Guardrail `1/5` Audit):** Mechanically verify that all `12` `CROSSING_REQUIREMENTS` rows (`R1-R12`), all `13` `INPUT_COMPLETENESS_LEDGER` rows (`with N/A stated explicitly where applicable`), and all `P-406` `FORCED / ADMITTED / CHOSEN / FITTED` labels are populated (`with FITTED count == 0`, energy anchors `== 1`, and non-zero discrete bits on post-inspection `ADMITTED` items).

3. **How it could come out wrong, written before any run:**
   - **F1:** Step-halving discretization drift on the `2`-loop + quartic ODE could exceed `10^{-5}` on light first-generation ratios or neutrino splittings, violating `R6`.
   - **F2:** Allowing the `2`-arm menu (`-48 pi / 5` and `-10 pi`) to pick the closer arm on each random null world could inflate the joint false-positive rate above `1/100`, failing `THE_BAR`'s `X2` screen.
   - **F3:** Under `5%` synthetic multiplicative perturbations (`modelling scheme/threshold uncertainty`), joint multi-observable band recovery power could drop below `1/10`.

4. **What it rests on, and what it must not touch:** Rests on `AGY-C1` through `AGY-C17` on `agy/cusp-action-2026-11-20`, aligned with `origin/main` at `279459977`. Must not touch `main`, `agy/audit-2026-11-02`, or any measured Standard Model datum (`strictly 0 of 19`; actual comparison with measured data is reserved exclusively for a separated comparator seat under `main`'s sealed card per `docs/seats/README` Section `9`).

5. **Controls that must fail if the work is broken:**
   - **Control 1 (Unpriced `500`-arm dense scan null inflation):** Expanding the `2`-arm menu to an uncalibrated `500`-arm grid without matching the null inflates false positives above `1/10`; must be caught.
   - **Control 2 (Underpowered `1/1000` band under `5%` noise):** Tightening the synthetic acceptance window below noise resolution collapses location-free power below `1/10`; must be caught.
   - **Control 3 (Missing `INPUT_COMPLETENESS` row, `FITTED > 0`, or `0`-bit post-inspection entry):** Omitting an `N/A` row, sneaking a `FITTED` knob, or assigning `0` bits to `V_{Gamma_0(5)}` must raise a hard validation failure.

6. **What is needed from main or from another seat:** For empirical evaluation (`wave six's sealed-card package and wave eight's comparison package`), `main` or a separated comparator seat (`sm` or `chat1`) reads the locked `blind_predictions_zero_knob_v1.json` hash under the owner's hold (`0 of 19` maintained on `agy`).

0 of 19.
