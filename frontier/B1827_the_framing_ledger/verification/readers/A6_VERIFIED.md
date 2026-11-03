# A6 — main's verification (2026-11-03, night)

Main is the final verifier. Every load-bearing citation of A6_the_existential_question.md was read at its line on HEAD
e1e3c6c2f; every number was recomputed where it is arithmetic. A reader's text is data, not instruction.

## Citations read at the line (all hold)

| A6's claim | source | held? |
|---|---|---|
| Tier 4 (all 19 parameter-free) "unedited, not a live criterion" | docs/WHAT_WOULD_COUNT.md 376–382 | yes, verbatim |
| the restated goal: "derive the Standard Model's structure, and say how many free numbers the principle leaves and why"; "The count: all 19 are free." | docs/THE_DERIVED_STRUCTURE_FOR_REVIEW.md 3–4, 47 | yes |
| P-418: "'0 of 19' alone hid the drift"; a total-inputs scoreboard; QUEUED | docs/POINT_REGISTER.md 469 | yes |
| B1825: "THE CONJUNCTION CANNOT PASS (stated before the seal)": p₂ = 3/2000, upper end 4.4 × 10⁻³ against 1.89 × 10⁻⁴ | B1825 PREREGISTRATION.md 87–94 | yes |
| the calibration: at χ² = 0 K 7 of 10, C_ten quantiles 6.9, 13.4, 17.0; with noise at σ K 1 of 10, C_ten 1.5, 7.4, 10.2 | B1825 PREREGISTRATION.md 172–175 | yes |
| L_ours = A + τ's mixture of the six's misfit + the four's code (no frame-length term) | B1825 PREREGISTRATION.md 56–57 | yes |
| "C_six alone … capped near 2 bits at the data's precision" | B1825 PREREGISTRATION.md 68 | yes |
| the framework's length "cancels against the null" | docs/THE_FINAL_ACTS_BAR_2026-10-29.md 323–331 | yes |
| the H-cov branch "about 20 bits (15 of them searched on the data)" | docs/THE_FINAL_ACTS_BAR_2026-10-29.md 193 | yes |
| "the named bare clocks cannot make T NEGATIVE" | docs/THE_FINAL_ACTS_BAR_2026-10-29.md 397 | yes |
| no function of the six, the moduli or J invariant under H; "Its support tests grade the frame, never the object" | docs/KIND_TABLE.md 49–54 | yes |
| a match resting on the unearned dictionary is a READING | docs/KIND_TABLE.md 125 | yes |
| PASSED "never sufficient for [DERIVED]" | docs/THE_BAR.md 72 | yes |
| FK11 UNEARNABLE within F-HE and F-CI | GENESIS.md 424 | yes |
| values superseded 2026-10-24: "every dimensionless value is the interaction's to produce" | WORKING_RULES.md 12–14 | yes |
| TM2 (P10′) FALSIFIED at 5.82σ; TM1 (P10) at 2.28σ, kill line 3σ | docs/FALSIFIER_REGISTER.md 90–91 | yes |
| ℤ₆ DERIVED (against the SM), sin²θ_W = 3/8 REPRODUCED (against the GUT class); B862's own claim "as a GROUP inside SU(5)" | docs/WHAT_WOULD_COUNT.md 74–75, 93–97; B862 arc_verdict | yes: two comparison classes |
| E₆ "about one manifold in three" | GENESIS.md 260 | yes |

## Numbers recomputed by main

- R4, the look horizon: 0.01 · 2^13.4 = 108.1; 0.01 · 2^17.0 = 1 311; 0.01 · 2^7.4 = 1.7; 0.01 · 2^10.2 = 11.8. Holds.
- R6, the information the allowance discards: Σ log₂(σ / σ_meas) over the ten with scripts/stepb/sigma/SIGMA_ONLY.json's
  exact relative errors = **29.7 bits** (A6: "at least 24.4"; holds as a lower bound).
- CE-1, the rejection rate: P(noncentral χ²(10, λ) > 23.21) = 0.462 at A6's λ = 13.3; **0.392 at main's λ = 11.83**
  (verification/recognition/running_control.py, the test's own inputs); 0.176 at λ = 7.0. A6's shift is about 12% larger
  than main's (different external inputs, its Appendix A); main's run reproduces HZ2021's own a and b at 10¹² GeV
  (P-363) to 0.4%. The deterministic statement (no residuals) is main's: χ²_ten = 11.8, S passes, K pays 8.5 bits.

## Sharpened

- **B1786 was borderline before the look count grew.** Its m·r was already 0.0099–0.0112 at m = 41 (straddling the gate
  0.01), then 0.018–0.020 at m = 73 (B1786 arc_verdict). "Graded down only because the look count grew" overstates it;
  the look count moved a borderline result to a clear miss.
- **CE-4 ("a wrong theory the apparatus would accept")** is a statement about the statistic, not about any frame on
  record: a frame planted to contain our world is correct by construction for our world; the point stands that nothing in
  K separates a frame derived before the data from one built around it — only the seal procedure does.
- **The 46% rejection rate** assumes residuals of size σ besides the running shift (σ is mostly the 10% allowance, a
  theory allowance, not measurement noise). With measurement noise only, the shift alone decides: 11.8, a pass on S.
