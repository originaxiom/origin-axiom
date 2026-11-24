# Relay `AGY -> AGY-EXP, AGY-002 & MAIN` (`2026-11-24`) — Card `AGY-C44`: Phase-7 Remediation (`D1..D6`) & `blind_predictions_topdown_toe_v9.json` Seal (`0 of 19`)

- **From:** `agy` on `agy/cusp-action-2026-11-20` (`harvest branch agy/audit-2026-11-02 frozen at 4319f47e2`; `AGY-C1..C43` and `v1..v8.json` preserved untouched on disk).
- **Check Labels (`docs/seats/README.md` section twelve):** `computed once`, `expectations committed first`, `tested against planted errors` (`5` of `5` in producer and `5` of `5` in disjoint cold-room countercheck; `230` of `230` cumulative).
- **Firewall:** `0 of 19` (`zero AST floats, zero JSON floats, zero empirical SM imports`).

## 1. Dated `2026-11-24` Supersessions & Errata Closing `D1`–`D6` on `AGY-C39..C43` & `Seam AGY-C37-S1`

1. **`[ERRATUM 2026-11-24 on AGY-C40 & C43 Layer-2 Stabilization (D1)]:`**
   - In unbroken `4D N = 1` SUSY (`IC5: N_B - N_F == 0`, `M_{SS}(T^2) == 0`), `6D` `1`-loop `O(M_{KK}^4)` Epstein Casimir energy vanishes identically (`(2 - 2) E_3(tau; p) == 0`), superseding `AGY-C40`/`C43`'s non-SUSY `V_{3gen}^{(5)}` / `c0_kl` (`G5`), while all `3` massless generations arise solely from Layer `3`'s magnetized `T^2 / Z_2` zero modes (`keeping B_{MSSM} = 5 / 7`, with `|E[2] \ {0}| = 3` spin structures in `IC7`).
   - `AGY-C44` stabilizes `tau_*^+ = (2 + i) / 5` in `4D N = 1` no-scale SUGRA (`K = -3 ln(T + bar T) - ln(sqrt(5) Im tau |eta(tau) eta(5 tau)|^2)`) via parameter-free `W_{mod}(tau) = (Lambda_perp^3 / (5 sqrt(5))) (Phi_5 + 125 / Phi_5)` (`|D_tau W_{mod}(tau_*^+)| < 10^{-48}`, `V_{SUGRA}(tau_*^+) == 0`, Hessian `> 40`, cusp walls; `Control 1`).
2. **`[ERRATUM 2026-11-24 on AGY-C41..C43 Magnetized Zero-Mode Norm, Matter Curves, & Seam AGY-C37-S1 (D2)]:`**
   - Restores canonical unit-`L^2(T^2 / Z_2)` norm `psi_+^{(1)} = (psi^{1, 4} + psi^{3, 4}) / sqrt(2)` (`factor sqrt(2)` on `j = 1`, `2D` periodic quadrature `< 10^{-28}`; `Control 2`) on curves `Sigma_{10}, Sigma_5` at equal flux `M_{10} = M_5 = 4` (`3` even + `1` odd by Riemann-Roch) and wrapping `(w_{10}, w_5) = (3, 1)` (`5` bits), `2D` Kähler `R7`, and prices `+1` bit on the self-dual `X_4` fiber (`33 / 2` core, `35 / 2` full bits; `ISO` branch cross-reported).
3. **`[ERRATUM 2026-11-24 on AGY-C42..C43 Stop EFT Matching & 3-Flavor Leptogenesis (D3 & D5)]:`**
   - Evaluates exact non-degenerate `1`-loop `DRbar` stop Coleman-Weinberg shifts `(Delta m_{H_u}^2, Delta m_{H_d}^2, Delta B_mu, Delta lambda_{stop})` at `M_S = sqrt(m_{Q_3} m_{U_3})` with continuous EFT VEV `v_{SUSY}^2(M_S) == v_{SM}^2(M_S)` (`Control 3`) under `(Delta_H, c_mu, c_B, bar_theta_{UV}^{bare}) = (18, 5 / 2, -11 / 5, 0)`.
   - Evaluates decohered `3`-flavor SUSY leptogenesis (`Gamma_e / H < 1 < Gamma_mu / H < Gamma_tau / H`) with MSSM width `Re(H_{jj}) / (4 pi)` and `(N_1 + tilde N_1)` source `(7 / 3) Y_{N_1}^{eq}` (`Control 4`).
4. **`[ERRATUM 2026-11-24 on AGY-C39..C43 Continuous Parameter Count, U(3)^6 Scrambling, & Card Paths (D4 & D6)]:`**
   - Includes `bar_theta_{UV}^{bare}` explicitly (`bar_theta_{QCD}^{raw} = bar_theta_{UV}^{bare} + arg det(Y_u Y_d) + 3 arg(M_3)`), proving via live `50 x 4` SVD that `R11 == 4` (`exact 12 - 4 == 8 reduction from v7.json`, correcting `C43` relay `:16`'s `11 != 9` list) and verifying full `U(3)^6` chiral scrambling (`det U_f != 1` with anomalous `bar_theta_{UV}^{bare}` shift `< 10^{-25}`; `Control 5`).
   - Corrects `AGY-C39` card `:5` (`relays/agy_2026-11-24_c39/...`), `:22` (`Rests on AGY-C35..C38`), `AGY-C40` card `:5` (`relays/agy_2026-11-24_c40/...`), and `c41:5` docstring (`10` roots, `dim G_{LR} = 15`).

## 2. Canonical Top-Down Synthesis Bundle (`blind_predictions_topdown_toe_v9.json`)

- Seals all `50` dimensionless observables and `24` machine-verified certificates (`R11 == 4`, `R12 == 1`, `33 / 2` core bits, `35 / 2` full bits, `N = 120` vs `240` `< 10^{-10}`, `U(3)^6` scrambling `< 10^{-25}`, `0 / 2000` null hits), verified end-to-end by disjoint `c44_countercheck.py`.

0 of 19.
