# Card AGY-C17: 7D Stora-Zumino Gravitational Inflow, 4D Graviton Normalizability, and Zero-Knob Gauge-Higgs EWSB

1. **The package and the question, in a sentence:** Under `AGY-C13`, `AGY-C15`, and `AGY-C16`, does `7D` Lorentz Chern-Simons descent on `M_4 x X_{4_1}^{(m)}` cancel irreducible boundary `tr R^4` anomalies while preserving a finite `L^2`-normalizable `4D` graviton zero mode, and can every continuous `UV` and `IR` threshold placeholder in `AGY-C15` be replaced by exact Gauge-Higgs Unification and cusp-instanton expressions?

2. **What will be delivered, and what done means:** A pre-registered, hashed `0 of 19` script `relays/agy_2026-11-21_c17/c17_7d_grav_inflow_and_zero_knob_ghu.py`, raw output, a zero-shared-code countercheck `c17_countercheck.py` with five planted negative controls, and a mask-clean result relay testing:
   - **Expectation E1a (Non-Abelian `8D` Grassmann Stora-Zumino Descent):** On the `256`-component exterior algebra `Lambda^*(R^8)` with non-commuting quadratic `so(6)` spin connections `omega(x)`, verify analytically (`zero finite differences`) that `d Omega_7^{LCS}(omega) == tr(R^4)` (`coefficients 1, 4/5, 2/3, 4/7`) beyond `10^{-14}`, while `tr(R^4)` is algebraically indivisible by `tr(R^2)` (`blocking pure-6D single-tensor Green-Schwarz factorization without 273-unit matter tuning`).
   - **Expectation E1b (`4D` Einstein-Hilbert Normalizability on Cusped `X_{4_1}^{(m)}`):** Verify to `50` digits that cusped `X_{4_1}^{(m)}` (`m in {1, 8, 40}`) has finite hyperbolic volume `2 m Im Li_2(exp(i pi / 3)) == (3 sqrt(3) / 2) m L(chi_{-3}, 2)`, giving a finite `L^2` `4D` graviton zero mode separated from the continuous cusp Laplacian spectrum at `lambda_ess == 1`.
   - **Expectation E2 (Zero-Knob Gauge-Higgs Quartic & Instanton EWSB Flow):** Verify from `6D` Clifford and `E_8` commutators that Gauge-Higgs Unification fixes unit chiral norm and `D`-term quartics `(2/5, 2/5, 1/10, -1/2) g_0^2` at `alpha_{GUT} = 1/40`. Running to `t_{EW} = -48 pi / 5` (`Majorana threshold -16 pi / 5`, `xi = 1/2`, `m_{12}^2 / m_0^2 = 1/40`) must keep `lambda_1, lambda_2 > 0` and `lambda_3 + lambda_4 + sqrt(lambda_1 lambda_2) > 0`, trigger `m_{H_u}^2 < 0 < m_{H_d}^2` (`tan beta > 5`), and give `m_{u3} / m_{d3} > 10` and `m_{d3} / m_{e3} > 3/2` with zero continuous literals.
   - **Expectation E3 (`35`-Digit `22`-Observable Zero-Knob `UV -> IR` Haar Audit):** Verify simultaneous `35`-digit `U(3)^5 x O(3)_{\nu_R}` invariance (`drift < 10^{-25}`) across all `22` dimensionless `IR` observables (`adding bounded quartic stability margin and electroweak gauge-mixing ratio to AGY-C15's twenty`).

3. **How it could come out wrong, written before any run:**
   - **F1:** Non-abelian ordering of `d omega` and `omega^2` in `Omega_7^{LCS}` could leave a non-vanishing commutator residual `d Omega_7^{LCS} - tr(R^4) != 0` on generic `so(6)` spin connections.
   - **F2:** Starting on the `D`-flat boundary `lambda_3 + lambda_4 + sqrt(lambda_1 lambda_2) == 0` at `t = 0`, `1`-loop running could drive `lambda_1` or `lambda_3 + lambda_4 + sqrt(lambda_1 lambda_2)` negative before `t_{EW} = -48 pi / 5`, destabilizing the vacuum.
   - **F3:** At the exact instanton horizon `-48 pi / 5` (`with zero continuous tuning`), `m_{H_u}^2` could either fail to turn negative or overshoot into `m_{H_d}^2 < 0`.

4. **What it rests on, and what it must not touch:** Rests on `AGY-C4`, `AGY-C13`, `AGY-C14`, `AGY-C15`, and `AGY-C16` (`c48c26c28`) on `agy/cusp-action-2026-11-20`, aligned with `origin/main` at `279459977`. Must not touch `main`, `agy/audit-2026-11-02`, or any measured target (`0 of 19`).

5. **Controls that must fail if the work is broken:**
   - **Control 1a & 1b (Perturbed Chern-Simons coefficient & flat-cylinder divergence):** Perturbing `4/5 -> 1` in `Omega_7^{LCS}` breaks `d Omega_7 == tr(R^4)` at `O(1)`; replacing hyperbolic `dy / y^3` with flat-cylinder `dy` makes the `4D` graviton norm diverge as `y_max -> infty`.
   - **Control 2a & 2b (Flipped top-quartic sign & `xi = 0` no-EWSB control):** Flipping `-12 tr((Y_u Y_u^\dagger)^2) -> +12 tr((Y_u Y_u^\dagger)^2)` drives `lambda_2(t_{EW}) < 0`, while setting `xi = 0` keeps `m_{H_u}^2(-48 pi / 5) > 0`; both must be caught alongside `35`-digit Haar scrambling.

6. **What is needed from main or from another seat:** Nothing (`0 of 19`).

0 of 19.
