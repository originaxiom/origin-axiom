# Pre-Registration Erratum 1: `AGY-002_A2-OW11-ERRATUM-1` — Pati-Salam `(1, 2, 2) + (10, 1, 3)` Unification Slope Clarification (`0 of 19`)

- **Parent Card:** `AGY-002_A2-OW11` (`93246dcb0`)
- **Preserved `v1` Custody:** `6438776d5` (`relays/a2_ow11/verify_a2_ow11.py`) & `320f31dfd` (`verify_a2_ow11_out.json`, `all_gates_passed = false` solely on the overly narrow `b1_eff < b2L` sub-flag for `PS_122_1013`).
- **Exact Clarification:**
  - All three Pati-Salam scalar sets close exact `1`-loop gauge unification `B_reconstructed == 5 / 7` at the exact pre-registered intermediate scale ratios `r in (0, 1)` (`67 / 75`, `61 / 69`, and `25 / 33`).
  - The two `(4, 1, 2)` models close `5 / 7` by flipping `b_1_eff < b_2L` (`-16 / 3 < -8 / 3` and `-76 / 15 < -8 / 3`), whereas `(1, 2, 2) + (10, 1, 3)` has `b_1_eff = -2 / 3 > b_2L = -8 / 3` and closes `5 / 7` via positive slope ratio `B_PS = (b_2L - b_4) / (b_1_eff - b_2L) = 5 / 2 > 5 / 7`.
  - In authoritative `v2` (`relays/a2_ow11_v2/`), exact closure is checked by `0 < r < 1`, `B_reconstructed == 5 / 7`, and exact per-model mechanism (`b_1_eff < b_2L` for the two `(4, 1, 2)` models; `B_PS == 5 / 2 > 5 / 7` for `(10, 1, 3)`). `0 of 19.`
