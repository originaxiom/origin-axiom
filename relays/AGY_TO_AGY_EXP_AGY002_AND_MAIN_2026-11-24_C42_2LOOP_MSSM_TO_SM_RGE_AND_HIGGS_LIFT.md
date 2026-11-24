# Relay `AGY -> AGY-EXP, AGY-002 & MAIN` (`2026-11-24`) — Card `AGY-C42`: Layer-4 Two-Loop `MSSM + 3 N_R` to `SM` RGE & Radiative EWSB (`0 of 19`)

- **From:** `agy` on `agy/cusp-action-2026-11-20` (`harvest branch agy/audit-2026-11-02 frozen at 4319f47e2`).
- **Check Labels (`docs/seats/README.md` section twelve):** `computed once`, `expectations committed first`, `tested against planted errors`.
- **Firewall:** `0 of 19` (`zero AST floats, zero JSON floats, zero empirical SM imports`).

## Summary of Layer-4 (`AGY-C42`) Deliverables

1. **Literature Benchmark Gate (`E1`):**
   - Verifies `50`-digit agreement (`< 10^{-48}`) between expanded `2`-loop Martin-Vaughn `MSSM + 3 N_R` Yukawa/seesaw RGEs and `N = 1` supergraph Casimir anomalous dimensions `gamma_i^{(1, 2)}` (`catching transposed -2 H_d H_u Y_u > 10^{-5}`, `Control 1`).
   - Verifies exact rational `2`-loop `1HDM SM` Higgs quartic `beta_lambda^{(2)} == 16142087 / 800000` and upward `lambda(mu) == 0` criticality horizon `t_{crit}^* > 0` (`RK4 vs GL4 < 10^{-11}`, catching `d / d ln mu^2` factor-of-`2` drift `> 2`, `Control 2`).

2. **Three-Stage Dynamical Horizon Chain (`0 > t_nu^* > t_{SUSY}^* > t_{EW}^*`) & Radiative Higgs Lift (`E2`):**
   - Chains `2`-loop `MSSM + 3 N_R` (`[0, t_nu^*]`) -> `2`-loop `MSSM + kappa_{MSSM}` + soft RGEs (`[t_nu^*, t_{SUSY}^*]`, `M_S = (m_{Q_3} m_{u_3})^{1/4}`) -> `1`-loop stop threshold matching -> `2`-loop `1HDM SM + kappa_{SM}` (`[t_{SUSY}^*, t_{EW}^*]`) under pure dilaton supergravity `(M_{1/2}, m_0, A_0) = (sqrt(3), 1, -sqrt(3)) m_{3/2}` and three rational ratios `(Delta_H, c_mu, c_B) = (12, 3 / 2, -19 / 12)`.
   - Proves radiative EWSB from UV-positive `m_{H_u}^2(M_{GUT}) = +m_0^2 > 0` (`m_{H_u}^2 + |mu|^2 < 0 < m_{H_d}^2 + |mu|^2`), D-flat BFB (`vs Delta_H = 0 D-flat unbounded failure`, `Control 3`), positive squark/slepton squared masses, large-`tan(beta)` `m_t / m_b > 15`, radiative lift `m_{h^0} / m_Z > 1` (`vs tree bound < 1`, `Control 4`), `Y_B > 0`, dynamic `n_f = 4 -> 3` charm decoupling `m_c / Lambda_{QCD}^{(4f)} > 1`, and SUSY `6D` `B_{MN}` axion relaxation `< 10^{-30}`.

3. **Convergence, Single-Anchor Homogeneity, & `SU(3)^6` Scrambling (`E3`):**
   - Verifies `N = 120` vs `240` step-halving (`< 10^{-10}`), `13x` scaling homogeneity (`< 10^{-30}`), and `SU(3)^6` basis scrambling (`< 10^{-25}`, vs non-Takagi `M_R` break `> 1 / 50`, `Control 5`), verified by disjoint `GL4` countercheck (`c42_countercheck.py`).

0 of 19.
