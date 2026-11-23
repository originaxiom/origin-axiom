# Pre-Registration Card A2-OW25 & A2-OW16 v13: Final `0 of 19` Pre-Lock IR Pipeline (`B4_UV` `2`-Loop MSSM + Weinberg Operator + Radiative EWSB & Gluino FCNC Dilution), Arithmetic `\mathbb{Z}[i]` Octahedral `b_1 = 3` Unification (`U2`: Borromean Rings `6^3_2` vs. Whitehead Link `5^2_1` vs. `m004`), `T^2 / Z_N` Twisted-Sector Anomaly-vs-Gravity Obstruction (`U3`), & SHA-256 Sealed `B4_UV` IR Blind-Prediction Lock (`0 of 19`)

- **Seat / Branch:** `agy-002` on `origin/agy-002/verify` (base `88de12cc9`)
- **Date:** `2026-11-23`
- **Firewall:** strictly `0 of 19` (zero empirical PDG, NuFIT, Planck, DESI, or CODATA numbers anywhere; all predictions are purely dimensionless ratios).
- **Coding & Custody Standard:** `0` Python `float`/`complex` AST literals, `0` binary64 `float()`/`complex()` casts, `0` JSON float tokens (`assert_no_json_floats`), `0` peer/`frontier/` imports, `0` hardcoded proof booleans (Guardrail `2`), pre-hashed `SCRIPT_SHA256.txt` committed before execution, raw unread `OUTPUT_SHA256.txt` committed before analysis, zero in-place overwrites, single-run `A2-OW16 v13` (`computed once`), followed by an isolated cold-room zero-shared-code referee (`relays/a2_ow25_referee/referee_a2_ow25.py`).
- **Hard Stop-Rule:** Once `Card A2-OW25` + `A2-OW16 v13` + Cold-Room Referee pass with `discrepancies_count = 0`, we stop blind UV iteration, freeze the conditional SHA-256 blind-prediction lock, push/sync with peer seats, and proceed to pre-registered staged unblinding.

---

## 1. Pre-Registered Modules & Acceptance Gates (`A2-OW25`)

### Module `OW25-A`: The `B4_UV` `2`-Loop MSSM + Weinberg-Operator + Pure-`SU(5)_{hid}` Soft-SUSY IR Pipeline (Attacking `U4` & Computing Genuine `M_Z` Ratios)
1. **Guardrail-4 Literature Benchmark Gate (Strictly `0 of 19`, Zero Binary64 Casts):**
   - Derive all `1`-loop and `2`-loop MSSM gauge beta coefficients (`b_i = (33/5, 1, -3)`, `B_{ij}`, `C_{ik}`) and all `7` chiral superfield anomalous dimensions `(\gamma_Q, \gamma_{u^c}, \gamma_{d^c}, \gamma_L, \gamma_{e^c}, \gamma_{H_u}, \gamma_{H_d})` directly from `SU(3)_c x SU(2)_L x U(1)_Y` Casimirs (`C_2, S_2`) via Martin–Vaughn (`PRD 50 (1994) 2282`, `hep-ph/9311340`) master formulas.
   - Verify to `< 10^{-40}` on non-commuting complex `3 x 3` Yukawa matrices that both `1`-loop and `2`-loop superpotential beta functions satisfy the exact **NSVZ / SUSY non-renormalization theorem** (`\beta_{Y_f} \equiv \gamma_L Y_f + Y_f \gamma_R + \gamma_H Y_f`) and the exact Antusch–Kersten–Lindner–Ratz (`hep-ph/0305273`) `2`-loop dimension-`5` Weinberg operator identity (`\beta_\kappa \equiv (\gamma_L + \gamma_{H_u} I_3)\kappa + \kappa (\gamma_L + \gamma_{H_u} I_3)^T`).
   - Verify the exact `d / d\ln\mu` (`1/(16\pi^2)`, `1/(16\pi^2)^2`) integrator (`45`-dps `mpmath` RK4 with step-halving `N` vs `2N` agreement `< 10^{-11}`) against:
     - Exact closed-form `1`-loop MSSM gauge running (`< 10^{-13}`),
     - Exact closed-form `1`-loop Bernoulli Pendleton–Ross top-Yukawa analytic solution in the `(g_3, y_t)` limit (`< 10^{-13}`),
     - Exact Antusch et al. downward RG running direction (`M_{GUT} \to M_{SUSY}`) on a pure synthetic normal-ordered neutrino benchmark (`\Delta s_{12}^2 > 0, \Delta s_{23}^2 > 0` for large `y_\tau`).
2. **Dimensionless `B4_UV` UV Boundary Conditions & Full `2`-Loop Evolution (`M_{GUT} \to M_{SUSY}`):**
   - Pure theoretical unified gauge grid `\alpha_{UV}^{-1} \in \{23, 24, 25\}` (`g_{UV} = \sqrt{4\pi \alpha_{UV}}`).
   - Dynamically derived SUSY-breaking hierarchy from pure-`SU(5)_{hid}` gaugino condensation (`b_{hid} = 15`, `OW23-A`):
     $$\frac{\Lambda_{hid}}{M_{GUT}} = \exp\!\left(-\frac{2\pi}{15\,\alpha_{UV}}\right), \qquad t_{GUT \to SUSY} = \ln\!\left(\frac{M_{GUT}}{M_{SUSY}}\right) = \frac{2\pi}{5\,\alpha_{UV}} \in \{28.90, 30.16, 31.42\}.$$
   - Pure theoretical Higgs VEV angle grid `\tan\beta \in \{5, 15, 30, 50\}` and `E_8` GHU / `O(1)` UV Yukawa normalization `y_0 \in \{g_{UV}, 1\}` (normalizing `3`-rd-generation pure lopsided `SU(5)` `Y_u` at `M_{GUT}` by `y_0` and `Y_d, Y_e` by `y_0` / `y_0 \cdot r_{b/t}` where `Y_u = y_0 \hat Y_u / \sigma_3(\hat Y_u)` and `Y_d, Y_e` share unified `y_b(M_{GUT}) = y_0 / \tan\beta` or unified `y_0` for `t-b-\tau` unification at large `\tan\beta`; specifically, test both unified `y_0 = g_{UV}` across `\tan\beta \in \{5, 15, 30, 50\}` with `Y_{d,e}` scaled by `y_0 / \tan\beta` so `m_b/m_t = (\sigma_3(Y_d)/\sigma_3(Y_u))/\tan\beta` cleanly captures `O(1)` vs `1/\tan\beta` Yukawa normalization without importing any empirical mass!).
   - Evolve full non-commuting `3 x 3` complex `(g_1, g_2, g_3, Y_u, Y_d, Y_e, \kappa)` at `2`-loop MSSM from `t = 0` (`M_{GUT}`) to `t = -t_{SUSY}` (`M_{SUSY}`), extracting strictly dimensionless IR observables:
     - `(\alpha_1, \alpha_2, \alpha_3)`, `\sin^2\theta_W = \frac{3\alpha_1}{3\alpha_1 + 5\alpha_2}`, `\alpha_3 / \alpha_2`, `\alpha_{EM}^{-1} = \frac{5}{3}\alpha_1^{-1} + \alpha_2^{-1}` (at `M_{SUSY}` and `1`-loop SM-matched down to `M_{EW}` via `t_{SUSY \to EW} = \ln(M_{SUSY}/M_{EW})` parameterized by theoretical `m_{3/2}/v_{EW}` ratio benchmarks `\{10, 30, 100\}` — zero GeV!).
     - Pure lopsided `SU(5)` (`n_{10} = (3, 2, 0), n_{5bar} = (0, 0, 0)`) IR quark/lepton mass ratios (`m_u/m_t, m_c/m_t, m_d/m_b, m_s/m_b, m_e/m_\tau, m_\mu/m_\tau, m_b/m_\tau`) and CKM (`|V_{12}|, |V_{23}|, |V_{13}|, J_{CKM}`) on both flat horosphere and curved `K_{E[2]}^{hyp}`.
   - **Guardrail-3 Mandatory `10`-Trial Haar `U(3)^5` Scrambling Through the Full `2`-Loop ODE:** Scramble `(Y_u, Y_d, Y_e, \kappa)` at `M_{GUT}` by `10` independent SplitMix64 Haar-random `U(3)^5` unitaries, run each scrambled system through the entire `2`-loop MSSM + Weinberg ODE to `M_{SUSY}`, and verify EVERY extracted IR observable is invariant to `< 10^{-12}`.
3. **Radiative EWSB, Dimensionless Higgs Mass Ratio (`m_h / M_Z`, `m_h / v_{EW}`), & Direct Attack on `U4`:**
   - Integrate `1`-loop Martin–Vaughn soft-SUSY RGEs (`M_1, M_2, M_3, m_{H_u}^2, m_{H_d}^2, m_{Q_3}^2, m_{u_3}^2, m_{Q_1}^2, m_{Q_2}^2, A_t`) from universal gravity mediation (`m_0 = M_{1/2} = m_{3/2}`, moduli-mediation `A_0 / m_0 \in \{0, -\sqrt{3}, -\sqrt{6}\}`), verifying dynamical radiative EWSB (`m_{H_u}^2(M_{SUSY}) < 0` with `m_{H_d}^2, m_{Q_3}^2, m_{u_3}^2 > 0`) and computing exact dimensionless `1`-loop stop-corrected `m_h / M_Z` and `m_h / v_{EW}`.
   - **Test 4a (Flat-Horosphere RG Rescue of `U4`):** Evolve flat-horosphere `q_R = +3` seesaw branches (`OW23-B` `K_5+K_6` and `OW24-C` `H_u(K_5)`) across `\tan\beta \in \{5, 15, 30, 50\}` (with `y_b = y_\tau = y_t` unified vs `1/\tan\beta` scaling) to determine definitively whether `2`-loop Weinberg RG running lifts flat-horosphere mixing into `(0.15 < s_{12}^2 < 0.55, 0.30 < s_{23}^2 < 0.70, s_{13}^2 < 0.08, 0.005 < dm < 0.15)` without paying `8.585` discrete bits, or proves an exact flat-horosphere RG obstruction.
   - **Test 4b (Curved `1/384` Hit RG Stability + Gluino Dilution of Curved `28.43%` Squark FCNC Split):** Evolve `CURV_5-6_over_5-6_qR_2_n5b_000` down to `M_{SUSY}` (verifying IR stability of all `5` PMNS observables) and compute the exact `SU(3)_c` gluino RG dilution ratio `(\Delta m_{\tilde q,12}^2 / \bar m_{\tilde q,12}^2)_{M_{SUSY}} / (\Delta m_{\tilde q,12}^2 / \bar m_{\tilde q,12}^2)_{M_{GUT}}` from the Martin–Vaughn soft-mass ODE!

### Module `OW25-B`: Resolving `U2` — Arithmetic `\mathbb{Z}[i]` Octahedral `b_1 = 3` Hyperbolic `3`-Manifold (`Borromean Rings 6^3_2` vs. `Whitehead Link 5^2_1` vs. `m004`)
1. **Exact First-Principles `SL(2, \mathbb{Z}[i])` & `SL(2, \mathbb{Z}[\omega])` Holonomy Construction:**
   - **Borromean rings `S^3 \setminus 6^3_2`:** `a = [[1, 2], [0, 1]], b = [[1, 0], [i, 1]], c = [[2 - i, 2], [i, i]]` — verify `\det = 1`, parabolic `\operatorname{tr} = 2`, exact Borromean Wirtinger commutator relations `[a, [b^{-1}, c]] = [b, [c^{-1}, a]] = [c, [a^{-1}, b]] = I`, non-abelian irreducibility, and exact peripheral cusp modulus **`\tau_{cusp} = 2i`** on ALL THREE cusps (`j(2i) = 66^3 = 287496`, exact index `2` sublattice of `\mathbb{Z}[i]` commensurable with `\tau_0 = (2+i)/5 \sim i` via `GL^+(2, \mathbb{Q})` index `2`, and `4 \cdot \tau_{cusp} = 8i`).
   - **Whitehead link `S^3 \setminus 5^2_1`:** `a = [[1, 1], [0, 1]], b = [[1, 0], [-1 - i, 1]]` — verify exact Wirtinger longitude commutators and exact cusp modulus **`\tau_{cusp} = -1 + 2i \sim 2i`** on BOTH cusps (`b_1 = 2`).
   - **Figure-eight knot `m004` (`S^3 \setminus 4_1`):** `a = [[1, 1], [0, 1]], b = [[1, 0], [-\omega, 1]]` over `\mathbb{Z}[\omega]` — verify exact Wirtinger relation `W a = b W` (`W = a b^{-1} a^{-1} b`), exact canonical longitude `l_a = b a^{-1} b^{-1} a^2 b^{-1} a^{-1} b = [[-1, -2\sqrt{3} i], [0, -1]]`, and cusp modulus **`\tau_{m004} = 2\sqrt{3} i`** living in `\mathbb{Q}(\sqrt{-3})` (**incommensurable** with `\mathbb{Q}(i)`!).
2. **Exact Lobachevsky Volumes (`55`-dps Quadrature) & Abelianization `b_1` + `6`-Gate Manifold Comparison:**
   - Verify `V(6^3_2) = 16 \Lambda(\pi/4) = 8 G_{Catalan} = 7.3277247534...` (exact match to `OW23-C` `R_{MN}^2` stabilization volume!), `V(5^2_1) = 8 \Lambda(\pi/4) = 4 G_{Catalan}`, `V(m004) = 6 \Lambda(\pi/3) = 2.0298832128...`.
   - Compute exact link-group abelianization Smith Normal Forms proving `b_1(6^3_2) = 3`, `b_1(5^2_1) = 2`, `b_1(m004) = 1`.
   - Compute the **`6`-gate `3`-manifold consistency matrix** (`G1`: `b_1 >= 2` Strong CP, `G2`: `b_1 = 3` cycles, `G3`: `\mathbb{Q}(i)` trace field, `G4`: cusp commensurable with `\tau_0 \sim i`, `G5`: volume `= 8 G_{Catalan}` matching `OW23-C`, `G6`: orientation-reversing `Z_2` involution with `b_1^+ \in \{0, 2\}`): prove **`6^3_2` passes `6 / 6`**, `5^2_1` passes `4 / 6`, and **`m004` fails `5 / 6` (passes only `1 / 6`)** — replacing `m004` with the Borromean rings `6^3_2` while honestly pricing `M = 8` flux selection (and noting `6^3_2` consists of `8` regular `(\pi/2, \pi/4, \pi/4)` ideal tetrahedra without claiming zero-bit dynamical derivation of `M = 8` per Guardrail 1!).

### Module `OW25-C`: Closing `U3` (`T^2 / Z_N` Twisted Fixed-Point Anomaly-vs-Gravity Obstruction) & Canonical SHA-256-Sealed `B4_UV` IR Blind-Prediction Lock Table
1. **Exact Diophantine Twisted-Sector Anomaly-vs-Gravity Obstruction Across All `9 / 9` `OW24-B` Orbifolds:**
   - For all `9` bulk magnetized `E_8` orbifolds (`7` `T^2 / Z_4` + `2` `T^2 / Z_2` imported from `A2-OW24 v2` and verified from exact `240`-root data), compute:
     - Exact remaining Asymptotic Safety chiral headroom `H = 10 - (N_C^{bulk, post-DT} - N_V)` (`M_g^{DEP} = 3(N_C - N_V) < 31 \iff N_C - N_V \le 10`),
     - Exact minimum twisted chiral degrees of freedom `\Delta N_C^{twist, min}` required to cancel BOTH `SU(2)_{hid}` Witten anomaly (`\equiv 0 \pmod 2`) AND `4D` `U(1)_a \times G^2` GS non-universality under (a) physical `E_8`-bounded Cartan charges (`|q_a| \le 2`), and (b) unrestricted arbitrary integer charges (`|q_a| \in \mathbb{Z}`!).
   - Prove sharply:
     - Under physical `E_8`-bounded charges (`|q_a| \le 2`), **`0 / 9`** twisted-completed magnetized `E_8` orbifolds survive `N_C - N_V \le 10` (`M_g^{DEP} < 31`)!
     - Even allowing completely unrestricted non-`E_8` integer charges, **`7 / 9`** STILL fail strictly on headroom + Witten parity (`H < 2` for `Witten = 1` or `H < 4` for `Witten = 0`), while the sole `2` remaining models (`T^2/Z_4 (-4,-4,4,4)` and `T^2/Z_2 (-2,-2,0,4)`) require exotic unphysical charges `|q| = 14, 15` (`7x` the maximum `E_8` root charge) — AND `(-4,-4,4,4)` fails headroom anyway (`N_C = 78 > 60`) once `A_{\bar z}` zero-flux `(10, 2)` is included (`REF2_ZERO_FLUX_CHIRAL_DZ_TWIST_NOTE`)!
   - Conclude cleanly that **`G_2` codimension-`7` conical-locus `SU(5)_{vis} x SU(5)_{hid}` (`N_V = 48, N_C = 52`, `0` hidden matter, `8 / 8`)** is uniquely forced as `B4_UV`'s anomaly-free UV completion!
2. **Canonical SHA-256-Sealed Conditional `B4_UV` IR Blind-Prediction Lock Manifest:**
   - Emit `blind_prediction_lock_B4_UV` combining all `2`-loop MSSM IR dimensionless ratios (`\sin^2\theta_W`, `\alpha_3/\alpha_2`, `\alpha_{EM}^{-1}`, `m_h / M_Z`, `m_h / v_{EW}`, quark/lepton mass ratios, `m_b/m_\tau`, CKM, PMNS, `\varepsilon_1`, `E/N = 8/3`, `|\bar\theta_{QCD}| < 10^{-50}`, Starobinsky `60`-e-fold `(n_s, r)`, Borromean `6^3_2` `V = 8 G_{Cat}`, `b_1 = 3`), with explicit Guardrail-1 discrete bit costs and Guardrail-5 continuous UV lever pricing, and compute its canonical SHA-256 lock digest!

### Module `OW25-D`: `6 / 6` Planted Fault Controls
1. **`PF_OW25_1`:** Corrupt `2`-loop `\gamma_{H_u}` `g_3^2 \operatorname{Tr}(H_u)` coefficient `16 -> 12` -> caught by NSVZ / SUSY non-renormalization identity (`err >> 10^{-40}`).
2. **`PF_OW25_2`:** Inject `2x` `d/d\ln\mu^2` factor error -> caught by Guardrail-4 Pendleton–Ross analytic trajectory gate.
3. **`PF_OW25_3`:** Flip sign of `y_t^2` in `m_{H_u}^2` soft RGE -> caught by radiative EWSB gate (`m_{H_u}^2(M_{SUSY}) > 0`).
4. **`PF_OW25_4`:** Perturb Borromean `c` matrix entry `c_{0,1}: 2 -> 3` -> caught by exact Wirtinger commutator & determinant check.
5. **`PF_OW25_5`:** Claim `m004` passes `b_1 >= 2` or `\mathbb{Q}(i)` cusp commensurability -> caught by `6`-gate manifold matrix.
6. **`PF_OW25_6`:** Claim zero Guardrail-1 discrete bits for the curved `384`-case atlas hit -> caught by bit-pricing gate.

---

## 2. Updated Single-Run Honest Master Scorecard (`A2-OW16 v13`, `computed once`)
- Retains honest `1` `DERIVED_EXACT` (`OBS-07`), `10` `CONDITIONAL_OR_QUALITATIVE`, `9` `INTERNAL_WALL_OR_TENSION`, `4` `OPEN_EXTERNAL_BOUNDARY` (updating `OBS-03, OBS-06, OBS-08, OBS-09, OBS-12, OBS-13, OBS-17, OBS-18, OBS-22` strictly from `A2-OW25` without any premature promotion!), adds `LOCK_18_ow25_b4uv_2loop_mssm_ir_pipeline_borromean_and_blind_lock`, verifies `100%` of branch `*SHA256*.txt` manifests, `0` AST/binary64/JSON floats, and `6 / 6` planted faults.

0 of 19.
