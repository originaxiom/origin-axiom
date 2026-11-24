# Card `AGY-C42` — Layer 4: Two-Loop `MSSM + 3 N_R` to `SM` RGE, Radiative EWSB, & Higgs Lift (`0 of 19`)

- **Seat / Branch:** `agy` on `agy/cusp-action-2026-11-20` (`origin/agy/audit-2026-11-02` untouched at `4319f47e2`).
- **Empirical Firewall (`docs/seats/README.md` section nine):** `0 of 19` — strictly data-free; zero empirical Standard-Model or experimental constants imported.
- **Section-Twelve Check Labels (`docs/seats/README.md` section twelve):** `computed once`, `expectations committed first`, `tested against planted errors`.

## Purpose & Layer-4 Role in the Top-Down Synthesis

Layers `1`–`3` (`AGY-C39..C41`) derived `D = 4`, `X_7 = m004 x (C^2 / 2T)`, native rank-`16` `E_8 x E_8`, `tau_8^+ = (16 + 8 i) / 5`, `alpha_{GUT}^{-1} = |2T| = 24`, `M_0 / M_{GUT} = exp(-16 pi / 5)`, `m_{3/2} / M_{GUT} = exp(-48 pi / 5)`, and zero-knob `3 x 3` UV Yukawa and Majorana matrices `(Y_u^{UV}, Y_d^{UV}, Y_e^{UV}, Y_nu^{UV}, C_R^{UV})`.

Layer `4` (`AGY-C42`) connects `M_{GUT}` to the electroweak vacuum via a self-consistent three-stage two-loop renormalization-group chain (`Stage I: MSSM + 3 N_R -> Stage II: MSSM + kappa -> Stage III: 1HDM SM + kappa`), replacing all four continuous UV Higgs quartic knobs of `v7.json` with supersymmetric `D`-term + `1`-loop stop threshold matching and radiative electroweak symmetry breaking.

## Pre-Committed Mathematical Expectations (`E1`–`E3`)

1. **`E1` — Literature Benchmark Gate (`2`-Loop Martin-Vaughn `MSSM + 3 N_R` & Luo-Xiao / Buttazzo `1HDM SM`):**
   - Verify `50`-digit agreement (`< 10^{-48}`) across all four non-commuting `3 x 3` Yukawa sectors `(Y_u, Y_d, Y_e, Y_nu)`, `M_R` (`dM_R / dt = 2`), and `kappa_{MSSM}` between expanded `2`-loop polynomials and `N = 1` supergraph Casimir anomalous dimensions `gamma_i^{(1, 2)}` (`catching transposed -2 H_d H_u Y_u > 10^{-5}`, **Control `1`**).
   - Verify exact rational `2`-loop `1HDM SM` Higgs quartic `beta_lambda^{(2)} == 16142087 / 800000` at the canonical rational test point, and reproduce an upward `lambda(mu) == 0` criticality horizon `t_{crit}^* > 0` (`RK4 vs implicit GL4 < 10^{-11}`, catching `d / d ln mu^2` vs `d / d ln mu` factor-of-`2` error `|Delta t_{crit}^*| > 2`, **Control `2`**).

2. **`E2` — Three-Stage Dynamical Horizon Chain (`0 > t_nu^* > t_{SUSY}^* > t_{EW}^*`), Radiative EWSB, & Higgs Lift:**
   - Under pure dilaton-dominated supergravity `(M_{1/2}, m_0, A_0) = (sqrt(3), 1, -sqrt(3)) m_{3/2}` and three rational `2 x 10_H` / Giudice-Masiero boundary ratios `(Delta_H, c_mu, c_B) = (12, 3 / 2, -19 / 12)` (`with UV-positive m_{H_u}^2(M_{GUT}) = +m_0^2 > 0 and m_{H_d}^2(M_{GUT}) = (1 + Delta_H) m_0^2 > 0`):
   - **Stage I (`[0, t_nu^*]`):** Integrate `2`-loop `MSSM + 3 N_R` to `t_nu^* = ln(M_1(t_nu^*) / M_{GUT})`, match `kappa_{MSSM} = -Y_nu M_R^{-1} Y_nu^T`, and verify `Y_B > 0` (`Gamma_tau / H(M_1) > 1`).
   - **Stage II (`[t_nu^*, t_{SUSY}^*]`):** Integrate `2`-loop `MSSM + kappa_{MSSM}` + soft RGEs to stop-decoupling horizon `t_{SUSY}^* = ln(M_S(t_{SUSY}^*) / M_{GUT})` (`M_S = (m_{Q_3} m_{u_3})^{1/4}`), proving radiative EWSB (`m_{H_u}^2 + |mu|^2 < 0 < m_{H_d}^2 + |mu|^2`), D-flat BFB (`m_1^2 + m_2^2 > 2 |B mu|`, vs `Delta_H = 0` `m_1^2 + m_2^2 < 0` failure in **Control `3`**), positive sfermion squared masses (`min m_{sf}^2 > 0`), large-`tan(beta)` `m_t / m_b > 15`, and radiative stop-threshold lift `m_{h^0} / m_Z > 1` (`vs tree-level D-term bound <= |cos 2 beta| < 1` in **Control `4`**).
   - **Stage III (`[t_{SUSY}^*, t_{EW}^*]`):** Integrate `2`-loop `1HDM SM + kappa_{SM}` to `t_{EW}^* = ln(v_{EW}(t_{EW}^*) / M_{GUT})` (`0 > t_nu^* > t_{SUSY}^* > t_{EW}^*`), computing `MSbar` & `1`-loop pole masses, `Lambda_{QCD}^{(5f, 4f)}`, dynamic charm decoupling `m_c / Lambda_{QCD}^{(4f)} > 1 -> Lambda_{QCD}^{(3f)}`, `k = 24` `M_{Pl} / v_{EW}`, and SUSY `6D` `B_{MN}` axion `|Delta bar_theta_{UV}| < 10^{-30}`.

3. **`E3` — `N = 120` vs `240` Step-Halving, `13x` Single-Anchor Homogeneity, & `SU(3)^6` Basis Scrambling:**
   - Verify `N = 120` vs `240` convergence (`< 10^{-10}`), `13x` UV energy-unit scaling homogeneity (`< 10^{-30}`), and `SU(3)^6` basis scrambling (`< 10^{-25}`, vs non-Takagi `M_R` break `> 1 / 50` in **Control `5`**).

## Disjoint Cold-Room Countercheck (`c42_countercheck.py`)

- Re-evaluates all three stages via supergraph Casimir `gamma_i^{(1, 2)}` + `4`-real-scalar `MV84` component tensors + implicit `2`-stage Gauss-Legendre `GL4` (`zero shared polynomial or RK4 lines`) and verifies `5 / 5` planted-fault controls.

0 of 19.
