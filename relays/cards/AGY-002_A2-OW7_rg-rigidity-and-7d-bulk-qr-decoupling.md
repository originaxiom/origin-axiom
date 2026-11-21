# Pre-Registration Card: `AGY-002_A2-OW7` — Resolving the Flavor Hierarchy-vs-CKM/CP Trade-Off: 2-Loop RG Rigidity Theorem and Exact `7D` Bulk QR-Decoupling (`0 of 19`)

- **Seat:** `AGY-002` (`agy-002/verify`)
- **Card ID:** `A2-OW7`
- **Empirical Firewall:** Strict `0 of 19` for all open-weave model predictions (published benchmark numbers from Buttazzo et al. `arXiv 1307-3536` and Xing-Zhou `arXiv 1804-01925` enter **solely** inside the isolated Guardrail 4 RGE integrator verification gate `OW7-A` and never touch any model matrix or parameter).
- **Prerequisite Custody:** Builds on `A2-OW3` (`2294c03c3` / `2fcde558a`), `A2-OW5` (`b47f02450` / `efeabdbc7`), and `A2-OW6` (`b57f20422` / `e078dd365`).

## 1. Scientific Objective & Hypotheses Committed Before Run

This card attacks Hard Wall 1b (the single-modulus exponential Hierarchy-vs-CKM/CP trade-off proved in `A2-OW6`) via two independent mechanisms — perturbative `2`-loop RG running (`SM` vs `Type-II 2HDM`) and `7D` bulk right-handed wavefunction localization (`QR-decoupling`):

1. **Guardrail 4 Published Literature Benchmark Gate (`OW7-A`):**
   - Implement exact `2`-loop SM RGEs (`t = ln(mu / mu_0)`, `dX / dt = beta^{(1)} / (16 pi^2) + beta^{(2)} / (16 pi^2)^2`, Machacek-Vaughn / Luo-Xiao / Buttazzo App. A) and exact `3 x 3` complex matrix `SM` and `Type-II 2HDM` Yukawa RGEs (with left-covariant `(Y Y^dag) Y` ordering verified under `Q_L -> U_L Q_L`).
   - **Pass bar `OW7-A`:**
     - On Buttazzo et al. (`arXiv 1307-3536`, Table 3 NNLO `MS-bar` inputs at `M_t = 17334 / 100 GeV`, evolved to `M_Pl = 12209 * 10^15 GeV`), reproduce `g_Y(M_Pl)` within `1 / 100` of `477 / 1000`, `g_2(M_Pl)` within `1 / 100` of `506 / 1000`, `g_3(M_Pl)` within `1 / 100` of `487 / 1000`, `y_t(M_Pl)` within `1 / 100` of `382 / 1000`, `lam(M_Pl) < 0` (`-2 / 100 < lam(M_Pl) < -1 / 100`), and `9 < log10(Lambda_lam / GeV) < 105 / 10`.
     - On Xing-Zhou (`arXiv 1804-01925`, hierarchical CKM benchmark evolved upward `M_Z -> 10^14 GeV`), reproduce exact opposite running direction between `SM` (`|V_cb|` ratio `> 11 / 10`, `|J_CP|` ratio `> 12 / 10`) and `Type-II 2HDM` (`|V_cb|` ratio `< 98 / 100`, `|J_CP|` ratio `< 95 / 100`) while `|V_us|` stays frozen (`|ratio - 1| < 1 / 1000`).

2. **Exact RG Rigidity Theorem on Open-Weave `A2-OW6` UV Yukawas (`OW7-B`, `0 of 19`):**
   - Evolve the exact `A2-OW6` open-weave UV matrices `(Y_u, Y_d, Y_e)` (`E[5] + E[6]` Regime-4b) at `m = 8` and `m = 24` downward `14` decades (`dt = -14 ln(10)`) from perturbative unified gauge coupling `g_UV = 52 / 100` and top/bottom/tau UV normalizations `y_UV in {7 / 10, 3 / 2}` under both `SM` (`1H`) and `Type-II 2HDM` (`2H`).
   - **Pass bar `OW7-B`:** Prove quantitatively across all `8` trajectories that perturbative RG running changes `m_1 / m_3` by `< 2x`, `|V_us|` by `< 4 / 100`, and `|V_cb|, |J_CP|` by `< 4x` (suppressed in `SM`, modestly enhanced `< 2x` in `Type-II 2HDM`), certifying **RG Rigidity**: perturbative 4D RG running alone cannot break `A2-OW6`'s single-modulus trade-off.

3. **Exact `7D` Bulk Right-Handed QR-Decoupling Theorem Across All `6 / 6` Permutations (`OW7-C`, `0 of 19`):**
   - At the minimal left-handed covering level `m_L = 8` (`tau = 16 / 5 + 8 i / 5`, `E[5] + E[6]` Regime-4b), apply the zero-parameter hypercharge-weighted `3D` hyperbolic geodesic right-handed bulk profile `D_{R,f} = diag(eps_f^2, eps_f, 1)` with `eps_f = exp(-(|6 Y_R| / 2) L_{m004}) = phi^(-2 |6 Y_R|)` (`|6 Y_R| = (4, 2, 6)` for `(u^c, d^c, e^c)`) in the canonical `W:T` `(Q_J, Q_I, Q_K)` orbifold fixed-point basis.
   - Evaluate ALL `6 / 6` permutations `P in S_3` of the three right-handed columns in `45`-dps `mpmath` (zero cherry-picking; Guardrail 1 prices any individual permutation choice at `log_2(6)` bits, while the trade-off breaking itself holds universally across all `6 / 6`!):
   - **Pass bar `OW7-C`:**
     - **Universal trade-off breaking across all `6 / 6` permutations:** Every permutation simultaneously achieves multi-decade hierarchies (`r13_u < 2 / 10000`, `r13_d < 5 / 1000`, `r13_e < 2 / 10^6`, `u` steeper than `d` by `> 20x`, `e != d` `23`-split `> 98 / 100`), sizable Cabibbo mixing (`14 / 100 < |V_us| < 25 / 100`), and non-collapsed Jarlskog CP (`|J_CP| > 5 / 10^5`, over `11` orders of magnitude larger than `m = 24`'s `~ 9 / 10^17`).
     - **Exact QR-Limit Convergence Theorem:** As `eps_f -> 0^+`, `|V_CKM(Y_u D_{R,u}, Y_d D_{R,d})|` and `J_CP` converge strictly to the parameter-free Gram-Schmidt QR limit `V_CKM^{QR} = Q_u^dag Q_d` across all `6 / 6` permutations (`max ||V_abs - V_QR_abs|| < 2 / 100` at finite geodesic `eps_f`, shrinking to `< (1 / 10)^6` at `eps_f / 1000`), completely decoupling mass hierarchies from CKM mixing and CP violation.
     - **Mandatory Guardrail 3 (`10`-trial `45`-dps Haar Gate):** Across all `6 / 6` permutations, independent random Haar `U(3)` basis transformations `(U_L, U_{R,u}, U_{R,d}, U_{R,e}, U_{L,e})` leave all singular-value ratios, `|V_CKM|`, `J_CP`, and `J_det_norm` invariant to `< (1 / 10)^30` (`<< (1 / 10)^12`).
     - Also certify asymmetric covering `(Y_u@8, Y_d@24)` and `(Y_u@24, Y_d@8)`, showing it preserves `|V_us| > 5 / 100` and `|J_CP| > 3 / 10^4` but leaves one quark sector shallow (`r13 > 5 / 100`).

4. **Planted-Fault Self-Checks (`OW7-D`, `4 / 4`):**
   - `PF-OW7-1`: Inserting an erroneous factor `1 / 2` in `d / dt` (`d / d ln mu^2` mistake) pushes Buttazzo's `log10(Lambda_lam / GeV)` above `15` (`caught`).
   - `PF-OW7-2`: Flipping `c_cross` in SM from `-3 / 2` to `+1 / 2` reverses Xing-Zhou's upward `|V_cb|` and `|J_CP|` ratios from `> 1` to `< 1` (`caught`).
   - `PF-OW7-3`: Extracting a gauge-non-invariant left-right overlap `V_u^T U_u` from `Y_u` fails the `10`-trial Haar invariance gate with drift `> 1 / 10` (`caught`).
   - `PF-OW7-4`: Turning off bulk localization (`D_{R,f} = I_3`) at `m = 24` regresses directly back into `A2-OW6`'s collapsed CKM/CP trade-off (`|V_us| < 1 / 10^5`, `|J_CP| < (1 / 10)^15`, `caught`).

## 2. Guardrails & Cold-Room Protocol

- Strict `0` float/complex AST literals and `0` `frontier/` imports; `A`-only `SHA-256` manifests; independent Cold-Room Referee built solely from this card (plus `a2_ow2_referee` `GL6`/`jtheta` Yukawa definition if needed) using disjoint ODE integrator (`Gauss-Legendre` or `Dormand-Prince` / `mpmath` `odefun`) and disjoint Householder QR + `45`-dps SVD. `0 of 19.`
