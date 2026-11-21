# Pre-Registration Card: `AGY-002_A2-OW12` — Strong CP (`bar_theta_Q` & `7D` CS Axion `E / N = 8 / 3`), Zero-Parameter `eps_nu = 1` Neutrino Seesaw PMNS, Fukugita-Yanagida Leptogenesis `epsilon_1`, & `7D` `(T_{3R}, B - L)` Bulk Inter-Sector Audit (`0 of 19`)

- **Seat:** `AGY-002` (`agy-002/verify`)
- **Card ID:** `A2-OW12`
- **Empirical Firewall:** Strict `0 of 19` (zero empirical PDG inputs used as model inputs; all observables computed strictly from the open-weave `m_L = 8` Regime-4b `E[5] + E[6]` Yukawa & Majorana operators).
- **Prerequisite Custody:** Builds on `A2-OW6` (`b57f20422` / `e078dd365`), `A2-OW7` (`57a8539b2` / `19d2facbe`), `A2-OW9` (`c33fc2a72` / `f9f8be537`), and `A2-OW11` (`1680fd50c` / `a9d82818b` @ `590a85bcb`), attacking Limp 5 and `THE_LADDER.md` rows `X6` (Strong CP), `X7` (Neutrinos), and `COSMOLOGY_LEDGER` Row 6 (Baryogenesis Play).

## 1. Exact Open-Weave Operator Specification (Self-Contained From `A2-OW6` & `A2-OW7`)

Using the exact Regime-4b `E[5] + E[6]` punctured-torus Yukawa construction of `A2-OW6` / `A2-OW7` at `tau = m * (+-2 + i) / 5` (`m_L = 8`, Selberg weights `w_3 = ((3 + sqrt(5)) / 2)^(-4)` and `w_4 = 4 * (2 + sqrt(3))^(-4)`, `Y = w_3 Y_5 / 24 + w_4 Y_6 / 35`, with quaternion `Q_8` couplings on `(Q_J, Q_I, Q_K)` and `6 Y` hypercharge twists `w_{Q_L} = +1`, `w_{u^c} = -4`, `w_{d^c} = +2`, `w_{L_L} = -3`, `w_{e^c} = +6`, `w_{nu^c} = 0`):
- **Dirac neutrino Yukawa:** `Y_nu` is evaluated with exact lepton-doublet twist `w_L = (-3 a, -3 b)` and right-handed neutrino twist `w_R = (0, 0)` (zero hypercharge `6 Y(nu^c) = 0`), with zero-parameter `7D` bulk localization `eps_nu = phi^(-2 |6 Y_R(nu^c)|) = phi^0 = 1`.
- **Canonical Majorana mass operators on `nu^c`:**
  1. `M_R^{(1)} = M_0 I_3` (unique `A_5`-invariant symmetric singlet on the `3`-dim irrep).
  2. `M_R^{(00)} = Y_{eval}(tau, L_2(tau), (0, 0), (0, 0))` (canonical zero-parameter `(0, 0)-(0, 0)` punctured-torus Majorana overlap — exact complex symmetric `3 x 3` matrix!).

## 2. Scientific Objective & Hypotheses Committed Before Run

1. **Strong CP Audit (`bar_theta_Q = arg det(Y_u Y_d)`) & `7D` Chern-Simons Axion Escape (`OW12-A`):**
   - Compute `bar_theta_Q = arg det(Y_u Y_d)` directly from `A2-OW7`'s exact complex Yukawa matrices at `tau_*^+` (`m_L = 8` and `m = 24`), at mirror `tau_*^-`, on `E[5]` and `E[6]` separately, and at the CP-conserving point `tau_CP = 8 i / sqrt(5)`.
   - Verify Guardrail 3 invariance under `10` random Haar `SU(3)_Q x SU(3)_u x SU(3)_d` (`det U = 1`) basis rotations (`max drift < 1 / 10^30`) and invariance under positive diagonal right-handed `eps_f` scaling and all `6` permutations.
   - **Pass bar `OW12-A`:**
     - At CP-conserving `tau_CP = 8 i / sqrt(5)`: `|bar_theta_Q| < 1 / 10^30` (exact CP conservation before spontaneous breaking).
     - At `tau_*^+` (`m_L = 8`): `E[5]` alone gives `arg det > 9 / 10`, `E[6]` alone gives `arg det < -6 / 10`, and `E[5] + E[6]` gives partial cancellation to **`15 / 1000 < bar_theta_Q < 16 / 1000`** (`~156 / 10^4 rad`, strictly nonzero — exposing an unavoidable Strong CP wall absent a Peccei-Quinn mechanism, since `Re(tau)` is Casimir-heavy `e_1 > 61` from `A2-OW9`!). At `m = 24`, `|bar_theta_Q| > 9 / 10`.
     - Exact `Z_2` CP conjugation: `|bar_theta_Q(tau_*^+) + bar_theta_Q(tau_*^-)| < 1 / 10^30`.
     - Exact `7D` Chern-Simons Peccei-Quinn axion anomaly ratio from `A2-OW5` / `A2-OW11` (`Spin(10)` `3 x 16_+` uniform PQ charge): `E_gen = 16 / 3`, `N_gen = 2`, **`E / N = 8 / 3`** exact over `Q` (certifying that `A2-OW5`/`OW11`'s forced `7D` CS inflow provides a canonical GUT axion candidate).

2. **Zero-Parameter `eps_nu = 1` Type-I Seesaw PMNS Mixing & Exact Fukugita-Yanagida Leptogenesis `epsilon_1` (`OW12-B`):**
   - Compute `U_PMNS = U_e^dagger U_nu` (from `Y_e * D_R(eps_e^2, eps_e, 1)` with `eps_e = phi^(-12)` and Type-I seesaw `M_nu = Y_nu M_R^(-1) Y_nu^T`, singular values sorted ascending `m_1 <= m_2 <= m_3`) across all `6` permutations for BOTH `M_R^{(1)} = I_3` and canonical `M_R^{(00)}`, verifying `10`-trial `45`-dps Haar `U(3)_L x U(3)_e x U(3)_nu` basis-scrambling invariance (`< 1 / 10^25` for PMNS angles, `J_PMNS`, and `epsilon_1`).
   - Compute exact Takagi factorization `U_R^T M_R^{(00)} U_R = diag(M_1, M_2, M_3 > 0)` (`residual < 1 / 10^30`) and exact 1-loop Fukugita-Yanagida CP asymmetry `epsilon_1 = (1 / (8 pi)) sum_{j=2,3} Im((H_hat)_{1j}^2) / (H_hat)_{11} * f(M_j^2 / M_1^2)` with `H_hat = U_R^dagger Y_nu^dagger Y_nu U_R` and `f(x) = sqrt(x) * [1 / (1 - x) + 1 - (1 + x) ln((1 + x) / x)]`, normalized at unit third-generation Yukawa (`epsilon_1^{norm} = epsilon_1 / sigma_{max}(Y_nu)^2`).
   - **Pass bar `OW12-B`:**
     - `||M_R^{(00)} - (M_R^{(00)})^T|| < 1 / 10^35` (exact complex symmetry), hierarchical positive Takagi spectrum `M_1 < M_2 < M_3`.
     - For `M_R^{(1)} = I_3`: normal hierarchy `5 / 1000 < Delta m^2_21 / Delta m^2_31 < 7 / 1000`; on the two `Q_I`-heaviest perms `(0, 2, 1)` and `(2, 0, 1)`, `28 / 100 < sin^2(theta_12) < 33 / 100`, `51 / 100 < sin^2(theta_23) < 53 / 100`, `5 / 100 < sin^2(theta_13) < 7 / 100`, and `|J_PMNS| > 4 / 100` (while honestly logging the `4 / 6` CKM-strict subset gives smaller `sin^2(theta_23) < 2 / 10`).
     - For canonical `M_R^{(00)}`: **`26 / 1000 < Delta m^2_21 / Delta m^2_31 < 28 / 1000`** (mild normal hierarchy `~269 / 10^4`!), AND across **ALL `6 / 6` permutations** `sin^2(theta_23) > 55 / 100` (universal large atmospheric mixing, while honestly logging `sin^2(theta_12) in (1 / 100, 12 / 100)` and `sin^2(theta_13) in (5 / 100, 11 / 100)`).
     - Exact Fukugita-Yanagida leptogenesis: **`5 / 10^6 < epsilon_1^{norm}(tau_*^+) < 6 / 10^6`** (`~545 / 10^8`, strictly positive at `tau_*^+`), AND exact mirror flip `|epsilon_1^{norm}(tau_*^+) + epsilon_1^{norm}(tau_*^-)| < 1 / 10^25` (certifying `tau_*^+` vs `tau_*^-` as the literal `Z_2` matter-vs-antimatter sign!).

3. **`7D` `(T_{3R}, B - L)` Bulk Zero-Mode Decomposition & Honest Inter-Sector Mass Ratio Audit (`OW12-C`):**
   - Verify exact `Spin(10)` identity `6 Y = 6 T_{3R} + 3 (B - L)` across all `6` species `(Q_L, u^c, d^c, L_L, e^c, nu^c)`, confirming `T_{3R} == 0` identically on left-handed doublets `(Q_L, L_L)` and `T_{3R} = +-1 / 2` exclusively on right-handed singlets `(u^c, d^c, e^c, nu^c)`.
   - Verify explicitly that multiplying left-handed doublets uniformly by `phi^(-2 |6 Y_L|)` (`Q_L -> phi^(-2)`, `L_L -> phi^(-6)`) leaves all `6` permutations' intra-sector mass ratios, CKM angles, PMNS angles, `J_CP`, `J_PMNS`, `bar_theta_Q`, and `epsilon_1^{norm}` invariant to `< 1 / 10^30`, while shifting overall `y_tau / y_b` by exact factor `phi^(-4)`.
   - Compute and transparently report exact `tan(beta) = 1` inter-sector Yukawa ratios `(y_t / y_b, y_tau / y_b, y_mu / y_s, y_e / y_d)` on all `6` permutations at `m_L = 8` (`|6 Y_R| = (4, 2, 6)`): certify `9 / 10 < y_tau / y_b < 14 / 10` (`b-tau` proximity on `4 / 6` perms, e.g. `~93 / 100` on `(1, 2, 0)` and `(2, 1, 0)`), while honestly certifying the quantitative **`e / mu` over-steepness tension** (`y_mu / y_s < 2 / 100` and `y_e / y_d < 1 / 1000` from `eps_e = phi^(-12)` vs `eps_d = phi^(-4)`).

4. **Planted-Fault Self-Checks (`OW12-D`, `4 / 4`):**
   - `PF-OW12-1`: Applying an anomalous `U(1)_A` chiral phase `exp(i / 2) I_3` to `Y_u` shifts `arg det(Y_u Y_d)` by `+3 / 2` (NOT `0` like `SU(3)`), confirming basis-scrambling distinguishes `SU(3)` from anomalous `U(1)_A` (`caught`).
   - `PF-OW12-2`: Replacing `M_R^{(00)}` by a purely real symmetric matrix `Re(M_R^{(00)})` with purely real `Re(Y_nu)` drives `epsilon_1^{norm} == 0` (`< 1 / 10^30`), proving spontaneous CP breaking at `tau_*` is strictly necessary for leptogenesis (`caught`).
   - `PF-OW12-3`: Using wrong quark twist `w_L = +1` (`Y_u`) instead of lepton twist `w_L = -3` (`Y_nu`) shifts `Delta m^2_21 / Delta m^2_31` under `M_R = I_3` from `~6 / 1000` to `> 3 / 10` (`caught`).
   - `PF-OW12-4`: Omitting `e^c` from `16_+` shifts the `7D` CS axion anomaly ratio `E / N` from `8 / 3` to `13 / 6` (`caught`).

## 3. Guardrails & Cold-Room Protocol

- Strict `0` float/complex AST literals and `0` `frontier/` imports; `A`-only `SHA-256` manifests; zero hardcoded proof flags; `10`-trial Haar basis-scrambling (`< 1 / 10^25`) on every physical observable; independent Cold-Room Referee built solely from this card (plus `A2-OW6`/`A2-OW7` card specs) using disjoint GL6 Fuchsian `L_2` + `mpmath.jtheta`, disjoint `mp.svd_c` / `mp.eigh` Takagi solver, and disjoint `sympy.Rational` `E / N` & `T_{3R}` checks. `0 of 19.`
