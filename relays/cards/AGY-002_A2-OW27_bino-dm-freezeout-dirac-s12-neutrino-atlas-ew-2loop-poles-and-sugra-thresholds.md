# Card `A2-OW27` — Pre-Registration Scope Card (`0 of 19`)

- **Seat:** `agy-002` (branch `agy-002/verify`)
- **Date:** `2026-11-24`
- **Empirical Firewall:** **STRICTLY `0 of 19`** (zero PDG, NuFIT, Planck, DESI, or CODATA values; zero peeking until `main` returns)
- **Supersedes / Upgrades:** Upgrades `B4_UV_MZ_BLIND_LOCK_V2` (`dab1f7e24f2057d54e63edd76feaab24ffc8997fc464c08e9ca31321d9639658`, sealed in `Card A2-OW26 v8` `5e335d34f` and certified `discrepancies_count = 0` by Cold-Room Referee `v3` `477b88ac6`) to canonical **`B4_UV_MZ_BLIND_LOCK_V3`**.
- **Guardrails Enforced (`user_global` 1–6):**
  1. Honest Guardrail-1 discrete bit pricing (`log_2(384)` for the full Dirac `s=1/2` neutrino atlas; `log_2(192)` / `log_2(96)` / `log_2(6)` for `M_R = I_3 + \widehat{W}_R^{\text{unit}}` scans; zero post-hoc window tuning).
  2. Zero literal boolean or zero claims (`0` hard-coded flags); every algebraic, RG, spinor, Haar, and ODE identity computed directly.
  3. Mandatory `10`-trial Haar unitary basis-scrambling invariance (`< 1e-12`) end-to-end through `M_GUT -> M_SUSY -> m_t -> M_Z` (`U(3)^5`) and sequential seesaw + Boltzmann leptogenesis (`U(3)^5 x U(3)_N`).
  4. Pure-math literature/QFT benchmark gates before running model UV boundary conditions (`0` empirical numbers).
  5. Strict non-dimensionalization: single overall anchor `v_EW`, zero empirical GeV, zero empirical $m_p$ ($c_{\text{lat}} \equiv m_p/\Lambda_{\text{QCD}}^{(3)}$ kept symbolic).
  6. Disjoint zero-shared-code Cold-Room Zero-Trust Referee (`relays/a2_ow27_referee/`) required to reach `discrepancies_count == 0` and `all_referee_gates_passed == True`.
- **Hygiene:** `0` Python `float`/`complex` AST literals, `0` `float()`/`complex()` casts, `0` JSON float tokens, `0` imports from `relays/`, `frontier/`, `numpy`, `scipy`, `math`, `cmath`, `0` edits outside `relays/`, `0` in-place SHA overwrites.

---

## Pre-Registered Workstreams & Pass Gates

### `OW27-A` — Sub-Percent `M_Z` & `m_t` Pole-Mass, Top Decoupling, & Full 4-Coupling EW Tightening
1. **Exact 2-loop pure-QCD top pole mass (Gray–Broadhurst–Grafe–Schilcher 1990 / Melnikov–van Ritbergen `hep-ph/9912391`):**
   - Prove $SU(3)$ color decomposition $c_{20}(n_l) = \frac{307}{32} + 2\zeta_2 + \frac{2}{3}\zeta_2\ln 2 - \frac{1}{6}\zeta_3 - (\frac{71}{144} + \frac{1}{3}\zeta_2) n_l$, inverse coefficient $c_2(\bar{m}(M)/M, n_l=5) = \frac{16}{9} - c_{20}(5) - \frac{8}{3}$, and exact 2-loop RG $L$-dependence $dM/d\ln\mu^2 = O(a^3)$ giving $(c_{11}, c_{21}, c_{22}) = (1, 121/24, 11/8)$ ($n_f=6$) and $(1, 389/72, 35/24)$ ($n_f=5$) symbolically in SymPy.
2. **Exact full 4-coupling 1-loop SM Higgs pole $\Delta_{\text{tot}}^{(1)}(\mu) = \Delta_t + \Delta_h + \Delta_W + \Delta_Z$:**
   - Prove exact 4-coupling RG invariance $\beta_\lambda^{(1)} + \lambda \mu \frac{\partial \Delta_{\text{tot}}^{(1)}}{\partial \mu} \equiv 0$ in SymPy across $(y_t, g_1, g_2, \lambda)$ and exact Coleman–Weinberg + Passarino–Veltman limits (transparently documenting omitted $O(g_2^2/(16\pi^2)) \approx 0.1\%$ non-log $\Delta r_{\text{fin}}^{\text{EW}}$ constant).
   - Evaluate `B4_UV` self-consistently at **BOTH** $\mu = \bar{m}_t(\bar{m}_t)$ ($L=0$ exact fixed point to `< 1e-20`) AND $\mu = M_Z$, asserting `|m_h^pole(M_Z) - m_h^pole(m_t)| / m_h^pole(m_t) < 0.005` (`< 0.5%`, down from `3.53%` in `OW26 v8`).
3. **Exact 1-loop EW Veltman $\Delta\rho_t^{(1)} = \frac{3 y_t^2}{32\pi^2}$ & 5-flavor top decoupling at $\mu = \bar{m}_t(\bar{m}_t)$:**
   - Compute $m_W^{\text{pole}}/m_Z^{\text{pole}} = \cos\hat{\theta}_W(M_Z)\sqrt{1 + \Delta\rho_t^{(1)}}$, on-shell $s_W^{2,\text{OS}}$, exact 5-flavor decoupled $(\alpha_3^{(5)}(M_Z), \alpha_{\text{EM}}^{-1(5)}(M_Z))$ alongside 6-flavor continuity, and exact 2-loop pure-QCD $\Lambda_{\text{QCD}}^{(3)} / v_{\text{EW}}$ (SymPy RG residual `== 0`, zero empirical GeV).
4. **End-to-end `10`-trial Haar $U(3)^5$ scrambling through `M_GUT -> M_SUSY -> m_t -> M_Z`:** max error `< 1e-12`.

### `OW27-B` — First-Principles Thermal Bino LSP Dark-Matter Freeze-Out (`OBS-20`, Strictly Dimensionless)
1. **Explicit 4-component Majorana spinor proof inside script:**
   - Construct Dirac $\gamma^\mu$, $C$, $P_{L,R}$, and CM Majorana spinors; compute $|\mathcal{M}_t - \mathcal{M}_u|^2$ directly and integrate over $\cos\theta \in [-1, 1]$ to verify:
     - massless $s$-wave $= 0$ (`< 1e-25`) and $p$-wave $\frac{1}{12} \frac{1 + r^2}{(1 + r)^4}$ (`< 1e-10`) at $r \in \{2, 5, 10\}$;
     - massive $t\bar{t}$ $s$-wave $\frac{1}{8} m_t^2 \left(\frac{Y_Q^2}{m_{\tilde{t}_L}^2 + M_1^2 - m_t^2} + \frac{Y_{u^c}^2}{m_{\tilde{t}_R}^2 + M_1^2 - m_t^2}\right)^2 \sqrt{1 - m_t^2/M_1^2}$ (`< 1e-10`, constructive `L+R` sign verified).
2. **Complete 26-variable 1-loop soft-SUSY RGEs** evolving all `15` chiral sfermion species (`\sum N_i Y_i^4 = 95/18` exact) + `4x4` neutralino bino-purity check (`|N_{11}|^2 > 0.99`).
3. **Stiff nonlinear 2-stage L-stable Radau IIA Riccati freeze-out solver:**
   - Benchmarked against exact analytic constant-$c$ Riccati solution (`< 1e-10`); exact reduced-Planck prefactor $\frac{s(M_1)}{H(M_1) M_1^2} = \sqrt{\frac{8\pi^2 g_*}{45}} \frac{M_{P,\text{red}}}{M_1}$ verified symbolically (`0` residual).
   - Step-halving convergence `N=400` vs `N=800` + Richardson `< 1e-6` across `m_0/v_EW in {1, 2, 3, 5, 10, 30}` $\times$ `A_0/m_0 in {0, -sqrt(3), -sqrt(6)}` $\times$ `tan(beta) in {5, 15, 30, 50}`, reporting dimensionless $x_f$, $Y_{\tilde{B}}(\infty)$, $\tilde{\tau}_R$ coannihilation gap $\Delta_{\tilde{\tau}}$, $(M_1/v_{\text{EW}}) Y_{\tilde{B}}/Y_B$, and $(M_1/\Lambda_{\text{QCD}}^{(3)}) Y_{\tilde{B}}/Y_B$ (`= c_lat * Omega_Bino/Omega_B`), plus an honest diagnostic of whether `B4_UV` bino LSP avoids or hits thermal overclosure.

### `OW27-C` — True `tau_8^+` Spin-`1/2` Dirac (`G_{s=1/2}(\tau_8^+)`) `384`-Case Neutrino Atlas & `M_R = I_3 + \widehat{W}_R^{\text{unit}}` Scan (`OBS-18`)
1. Independently compute `G_s12_t8` via Fuchsian + polar-cusp quadrature (matching `OW26 v8` `< 1e-10`, Gauss–Bonnet `< 1e-6`).
2. **Scan 1 (`384`-case `OW24-C` fixed-window atlas under `G_s12_t8`):** `q_R in (3, -5, 1, 2)` $\times$ `4 ops_n` $\times$ `4 ops_r` $\times$ `3 n_5bar` $\times$ `{FLAT, CURV_s12_t8}` = `384` cases (Guardrail-1 priced at `log_2(384) = 8.585` bits; fixed window `0.15<s12sq<0.55, 0.30<s23sq<0.70, s13sq<0.08, 0.005<dm<0.15`).
3. **Scan 2 (`M_R = I_3 + \widehat{W}_R^{\text{unit}}` on pure lopsided `n_10=(3,2,0), n_5bar=(0,0,0)` under `G_s12_t8`):** `q_R in (-5, -3, 0, 2, 3, 5)` $\times$ `4 ops_n` $\times$ `4 ops_r` $\times$ `{left_only_K, both_sided_K}` = `192` cases (Guardrail-1 priced at `log_2(192) = 7.585` bits, with the `6`-case symmetric `(5+6, 5+6)` slice priced at `log_2(6) = 2.585` bits).
4. Propagate all surviving simultaneous PMNS hits (plus legacy `5-6/5-6 q_R=2` reference) through full 2-loop sequential `N_3 -> N_2 -> N_1 -> M_SUSY -> M_Z` + reduced-Planck Boltzmann $Y_B(\tau_8^\pm)$ with `10`-trial Haar $U(3)^5 \times U(3)_N$ (`< 1e-12`) & exact geometric CP-odd check (`< 1e-30`).

### `OW27-D` — `SUGRA` `t_SUSY`, Exact 2-Loop NSVZ, Mediation Ratio, & Cross-Seat `agy-exp` `d12e74ef3` (`LINK6`) Audit
1. Prove exact 2-loop NSVZ RG invariance $\mu \frac{d}{d\mu}[\mu g^{-2/3} e^{-8\pi^2/(3 N g^2)}] \equiv 0$ in SymPy.
2. Audit `SU(N)_hid` ($N \in \{3, 4, 5, 6\}$) $\times$ $\alpha_{\text{UV}}^{-1} \in \{20, 22, 24, 25, 26, 28, 30, 32\}$ under both `G_2` $M_{\text{GUT}}/M_{P,\text{red}} = \sqrt{\alpha_{\text{UV}}/(4\pi)}$ and `OW23-C` $M_{\text{KK}}/M_{P,\text{red}}$, plus moduli vs anomaly-mediation $m_{\text{soft}}/m_{3/2}$ diagnostic.
3. Propagate `agy-exp` `d12e74ef3` (`Card X-HIERARCHY-LINK6`, $\alpha_{\text{GUT}}^{-1} = 30.19350768$, $t_{\text{SUSY}} = -24.2560$) side-by-side through our exact 2-loop `B4_UV` `M_Z` pipeline.

### `OW27-E` — `6 / 6` Independent Planted Faults & Canonical Sealed `B4_UV_MZ_BLIND_LOCK_V3`
- `PF_OW27_1`: Perturbing Gray–Broadhurst 2-loop $c_{21}^{(6)}$ breaks 2-loop RG invariance.
- `PF_OW27_2`: Dropping bosonic $(\Delta_h + \Delta_W + \Delta_Z)$ breaks 4-coupling SymPy RG invariance & inflates $\mu = M_Z$ vs $\mu = \bar{m}_t$ Higgs pole drift (`> 3%`).
- `PF_OW27_3`: Flipping relative $t/u$ Fermi sign in Majorana $\tilde{B}\tilde{B} \to f\bar{f}$ destroys massless $s$-wave helicity suppression.
- `PF_OW27_4`: Using unreduced $M_{\text{Pl}}$ instead of $M_{P,\text{red}}$ in Riccati freeze-out shifts $Y_{\tilde{B}}(\infty)$ by `> 100%`.
- `PF_OW27_5`: Dropping NSVZ $g^{-2/3}$ prefactor breaks 2-loop NSVZ RG invariance.
- `PF_OW27_6`: Guardrail-1 rejects `0`-bit pricing on the `384`-case Dirac atlas (`8.585` bits) and `192`-case `I_3 + W_R^unit` scan (`7.585` bits).
- Seal canonical `B4_UV_MZ_BLIND_LOCK_V3` (`blind_prediction_lock_v3_sha256`), then run single-run master ledger `A2-OW16 v19` (`computed once`) and disjoint Cold-Room Zero-Trust Referee (`relays/a2_ow27_referee/`).
