# Card `AGY-002_ENDGAME-V2-G3` — Radiative `EWSB` Scale Closure, `Picard-Lindelof` / `Coleman-Weinberg` / `Vissani` Threshold Theorems, and Dimensionless `v_EW` Ledger (`0 of 19`)

## 1. Package and Question

Testing dynamic IR termination via radiative `mu_H^2(mu) = 0` zero-crossing with `v_EW` as sole dimensionful unit (`Guardrail 5`, strict `0 of 19`, zero rescue factors):
1. Does pure `MSbar` `2`-loop Standard Model evolution (`Buttazzo et al. 2013 Appendix A`) below heavy thresholds ever cross `mu_H^2(mu) = 0` from `mu_H^2 > 0`, or close scale-invariantly via `Coleman-Weinberg` (`mu_H^2 = 0, lambda(mu_CW) = 0`) when the top Yukawa dominates?
2. Above heavy seesaw (`M_R`) and `Pati-Salam` (`M_PS`) thresholds, what are the exact `MSbar` signs of `1`-loop heavy Majorana neutrino (`Vissani 1998`) vs heavy portal-scalar radiative shifts to `mu_H^2(mu)`, and does `v_EW / M_PS` close parameter-free or require an explicit UV tuning parameter?

## 2. Deliverables and Definition of Done

1. **Exact `Buttazzo et al. (2013)` `2`-Loop `gamma_{mu_H^2}` Polynomial & `Picard-Lindelof` Integral Lock:**
   - Verify in exact `Fraction` arithmetic that the `3 x 3` matrix `2`-loop Higgs mass-squared anomalous dimension `gamma_{mu_H^2} = d ln(mu_H^2) / d ln(mu)` equals `2 * (1/m^2) dm^2 / d ln(mu^2)` of `Buttazzo et al. (2013) Appendix A`, and verify numerical `ODE` integration of `d mu_H^2 / d ln(mu) = gamma_{mu_H^2} mu_H^2` against `mu_H^2(0) exp(int gamma)` to `< 1e-11`.
2. **Exact Pure-`SM` Homogeneous Non-Crossing & Top-Dominated `Coleman-Weinberg` Obstruction Theorems:**
   - Prove and verify numerically that in homogeneous `MSbar` evolution below heavy thresholds, `sgn(mu_H^2(mu)) = sgn(mu_H^2(mu_0))` for all finite `ln(mu)` (`zero crossing strictly impossible without negative input or active threshold source`).
   - Prove and verify that at `mu_H^2 = 0` and `lambda(mu_CW) = 0`, `d^2 V_CW / dH^2|_{H=v} = 4 beta_lambda(mu_CW) v^2` is positive (`Gildener-Weinberg` IR minimum) in the gauge-only limit (`Y_f = 0`), **but strictly negative (`local maximum / UV instability, NOT an EWSB minimum`) whenever top Yukawa dominates (`e.g. y_t = 9/10`)**.
3. **Heavy-Threshold Radiative `EWSB` Sign Theorem (`Vissani 1998` vs Scalar Portal) & `Guardrail 5` Dimensionless Ledger:**
   - Verify `mu d/d(mu) V_eff^{(N_R)} = 0` (`to < 1e-12`) for `1`-loop heavy Majorana neutrinos, proving `d mu_H^2 / d ln(mu)|_{N_R} = -Tr(Y_nu^dag Y_nu M_R^2) / (4 pi^2) < 0` in `MSbar`, which shifts `Delta mu_H^2 > 0` during **downward** flow `M_PS -> M_R` (`stabilizing unbroken symmetry rather than triggering EWSB`).
   - Verify that heavy `Pati-Salam` scalar portals (`lambda_{HS} > 0`) have `d mu_H^2 / d ln(mu)|_S = +d_S lambda_{HS} M_S^2 / (16 pi^2) > 0`, driving a genuine downward radiative zero-crossing `mu_H^2(t_cross) = 0` from `mu_H^2(M_U) > 0`, while proving in `45`-digit `mpmath` that achieving `v_EW^2 / M_PS^2 = exp(-2 Delta_SM)` at `Delta_SM = 28` requires `Barbieri-Giudice` tuning sensitivity `> 1e20` (`so v_EW / M_PS does NOT close parameter-free; v_EW remains the sole dimensionful anchor, with all 12 fermion/boson masses expressed as dimensionless ratios m_i / v_EW invariant under U(3)^6 Haar scrambling to < 1e-12`).

## 3. How It Could Come Out Wrong (Falsification Conditions Sealed Before Execution)

- Any polynomial mismatch with `Buttazzo et al. (2013)` `gamma_{m^2}` or `Picard-Lindelof` integral discrepancy `>= 1e-11`.
- Any violation of `mu d/d(mu) V_eff^{(N_R)} = 0` (`>= 1e-12`), failure of scalar-portal downward zero-crossing, or `U(3)^6` Haar drift `>= 1e-12` on `m_i / v_EW`.
- Claiming parameter-free `v_EW / M_PS` closure despite `> 1e20` threshold sensitivity (`Guardrail 1`), or importing `> 1` dimensionful anchor (`Guardrail 5`).
- Failure to catch any of the `5` planted fault controls below.

## 4. Five Planted Fault Controls That Must Fail When Broken

1. **`PF3.1` (`d/d ln mu^2` vs `d/d ln mu` Half-Slope Error in `gamma_{mu_H^2}`):** Dividing `gamma_{mu_H^2}` by `2` must break `mu_H^2(IR)` by `> 0.1` relative error.
2. **`PF3.2` (`Homogeneous Positivity Guard`):** Asserts `min mu_H^2(mu) > 0.1` along pure-`SM` homogeneous flow from `mu_H^2(0) = 1`, catching any literal zero-crossing flag (`Guardrail 2`).
3. **`PF3.3` (`Inverted Vissani Fermion-Loop MSbar Sign`):** Flipping `-1/(4 pi^2)` to `+1/(4 pi^2)` must violate `mu d/d(mu) V_eff = 0` `RG` invariance by `> 0.01`.
4. **`PF3.4` (`Unstable Top-Dominated Coleman-Weinberg Curvature`):** Evaluating `d^2 V_CW / dH^2` at `lambda = 0, y_t = 9/10` must catch negative curvature `< -0.01`.
5. **`PF3.5` (`Unpriced Second Dimensionful Anchor, Guardrail 5`):** Supplying a second independent dimensionful scale alongside `v_EW` must return anchor count `2 > 1`.

## 5. Dependencies and Firewall Boundaries

Rests on `Buttazzo et al. (2013)`, `Gildener-Weinberg (1976)`, and `Vissani (1998)`. Strict `0 of 19` firewall; touches only files under `relays`. Expectations committed first (`0 of 19`).
