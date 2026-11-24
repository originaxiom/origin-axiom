# Relay `AGY -> AGY-EXP, AGY-002 & MAIN` (`2026-11-24`) — Card `AGY-C43`: Top-Down Single-Origin Synthesis & `blind_predictions_topdown_toe_v8.json` Seal (`0 of 19`)

- **From:** `agy` on `agy/cusp-action-2026-11-20` (`harvest branch agy/audit-2026-11-02 frozen at 4319f47e2`; `v1..v7.json` preserved untouched).
- **Check Labels (`docs/seats/README.md` section twelve):** `computed once`, `expectations committed first`, `tested against planted errors`.
- **Firewall:** `0 of 19` (`zero AST floats, zero JSON floats, zero empirical SM imports`).

## Summary of Top-Down Phase-7 Closure (`AGY-C39..C43` -> `blind_predictions_topdown_toe_v8.json`)

1. **Five-Layer UV-to-IR Deductive Chain (`E1`):**
   - **Layer `1` (`AGY-C39`):** Hurwitz `D = 4`, `m004` canonical `2T` cusp longitude `rho(lambda_0) == -1`, `B1223` stabilizer preservation on `m004 x (C^2 / 2T)`, and native rank-`16` `E_8^{(1)} x E_8^{(2)}` (`Spin(10) x SU(5)_perp`, `alpha_{GUT}^{-1} = |2T| = 24`, `b_0 = 15`).
   - **Layer `2` (`AGY-C40`):** Unbroken `4D N = 1` SUSY (`B = 5 / 7`), `E[2] \ {0}` `3`-generation Fricke minimum `tau_8^+ = (16 + 8 i) / 5`, and Open-Closed Modular-Gauge Duality `Lambda_{SU(5)_perp} / M_{GUT} = exp(-16 pi / 5) == |q(tau_8^+)|` (`earning M_0 / M_{GUT} = exp(-16 pi / 5) and m_{3/2} / M_{GUT} = exp(-48 pi / 5)`).
   - **Layer `3` (`AGY-C41`):** Minimal Cartan puncture flux `Q_{(1, 1)} = 6 Y + Q_X`, `[0, 2]^2` `3`-field Kähler normalization `2 sqrt(2) Im tau_8^+`, and magnetized `T^2 / Z_2` `M = 4` overlaps `(d_{10}, d_5) = (3, 1)` (`0` continuous sector scale knobs, exact `E_1` seesaw cancellation, simultaneous hierarchical CKM + bi-large PMNS + `m_{nu, 2} / m_{nu, 3} < 2 / 5`).
   - **Layer `4` (`AGY-C42`):** Self-consistent `3`-stage `2`-loop `MSSM + 3 N_R -> MSSM + kappa -> 1HDM SM + kappa` RGE chain (`0 > t_nu^* > t_{SUSY}^* > t_{EW}^*`) with pure-dilaton SUGRA radiative EWSB, positive sfermion squared masses, large-`tan(beta)` `m_t / m_b > 15`, radiative stop lift `m_{h^0} / m_Z > 1`, `Y_B > 0`, `n_f = 4 -> 3` charm decoupling, and SUSY `6D` `B_{MN}` axion `|Delta bar_theta_{UV}| < 10^{-30}`.

2. **Continuous Parameter Collapse (`R11: 12 -> 3`, `E2` & `E3`):**
   - Live `50 x 3` finite-difference SVD proves `assumed_continuous_uv_parameters == 3` (`(Delta_H, c_mu, c_B)`, eliminating `9` of `v7.json`'s `12` continuous UV parameters: `4` quartics, `1` Higgs mass ratio, `ln M_0`, `ln m_{12}^2`, `bar_theta_{UV}`, and `3` FN sector scales), `dimensionful_unit_anchors == 1`, `N = 120` vs `240` `< 10^{-10}`, `SU(3)^6` scrambling `< 10^{-25}`, and `0 / 2000` random null hits, verified end-to-end by disjoint `c43_countercheck.py`.
   - Ready for `main`'s comparator card alongside `blind_predictions_full_toe_v7.json` (`AGY-C37`).

0 of 19.
