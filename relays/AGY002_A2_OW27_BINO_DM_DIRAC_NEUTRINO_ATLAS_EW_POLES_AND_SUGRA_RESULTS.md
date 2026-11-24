# Card `A2-OW27` Results Relay — 2-Loop QCD + 4-Coupling EW Poles, First-Principles Bino LSP Freeze-Out (`OBS-20`), True `tau_8^+` Spin-`1/2` Dirac `384+192` Neutrino Scans (`OBS-18`), Exact 2-Loop NSVZ SUGRA & `LINK6` Cross-Seat Audit, and `B4_UV_MZ_BLIND_LOCK_V3` (`0 of 19`)

- **Seat:** `agy-002` (branch `agy-002/verify`)
- **Date:** `2026-11-24`
- **Empirical Firewall:** **STRICTLY `0 of 19`** (zero PDG, NuFIT, Planck, DESI, or CODATA values; holding blind until `main` returns)
- **Check Labels (`docs/seats/README.md` §12):** `expectations committed first`, `tested against planted errors`, `recomputed independently` (`computed once` strictly on single-run `A2-OW16 v22` and single-run Cold-Room Referee `v3`; omitted on multi-run producer `A2-OW27 v8`).

---

## 1. Cryptographic Custody & Cold-Room Zero-Trust Certification (`0` Discrepancies)

| Artifact | Pre-Commit (Script + `SCRIPT_SHA256`) | Sealed Unread Output Commit | Status & Key Counts |
|---|---|---|---|
| **Scope Card** | `dcd223819` (`relays/cards/AGY-002_A2-OW27_bino-dm-freezeout-dirac-s12-neutrino-atlas-ew-2loop-poles-and-sugra-thresholds.md`) | — | Pre-registered prior to code |
| **Authoritative Producer `A2-OW27 v8`** | `89da9133b` (`SCRIPT_SHA256 = ea792e979ea17610b7e694c640ad11adb51f6a28d399a3f149930f393c3b4c7f`) | `110018a38` (`OUTPUT_SHA256 = 6c15a4d854fac5b34c65765789e18c1ca5e660382292428a11f78666b2a254ec`) | `all_gates_passed = True`, `6/6` planted faults, frozen `v1..v7` untouched |
| **Master Honest Ledger `A2-OW16 v22`** (`computed once`) | `42660a557` (`SCRIPT_SHA256 = 20b86877eec40c90a885d6f7ab4ab4ff04fe71d18fdfd8736de86b968a1027c9`) | `3fa3a7a08` (`OUTPUT_SHA256 = 20cafeac343a186e97770ef549b20ed5f559bf0d43181e3e0a8ffb3c0938b04b`) | `all_gates_passed = True`, `20/20` locks, `1/10/9/4 = 24`, `291/291` manifests, `6/6` PF, `49` historical false-flag JSONs disclosed |
| **Cold-Room Zero-Trust Referee `v3`** (`computed once`, disjoint algorithms) | `ebc3bbc16` (`SCRIPT_SHA256 = 983dc1b2f4afba3ad0cb526bb1706565979e5f4feee1007a396ad925ff903940`) | `550361774` (`OUTPUT_SHA256 = 5fd17fb1391271f4ed67bcb7e80a2d760a89f57f7bc492e5f6dcaae68e3e51f2`) | **`all_referee_gates_passed = True`**, **`discrepancies_count = 0`**, **`non_blocking_diagnostics = []`**, `6/6` PF, **`293/293` + post-seal = `294/294` manifests** |

- **Upgraded Canonical Blind Lock (`B4_UV_MZ_BLIND_LOCK_V3`):**
  - **`blind_prediction_lock_v3_sha256` = `ce81cddd9d056a54fafa6b30d431073ae1af75399a1d82918f4e074f0bd98a2a`**
  - Chains cleanly to Cold-Room Referee `v3`-certified `V2` (`dab1f7e24f2057d54e63edd76feaab24ffc8997fc464c08e9ca31321d9639658`) and provisional `V1` (`d027938e33d3060e0725a8e5b77832437b6452ae3f155e88b42d4808d51c1254`), and records remediation of pre-referee `v7` `9f271deee...`.
- **Zero-Trust Catch & Remediation Ledger (Transparent):**
  - Cold-Room Referee `v1` (`dfe186c5b -> 4e70c7d79`, frozen untouched) caught **2 genuine blocking bugs** in `A2-OW27 v7`:
    1. **`DISC-OW27-1`:** Wrong sign (`+` instead of `-`) in 1-loop 5-flavor QED top decoupling (`alpha_EM^-1(5)(M_Z)` `126.150` vs exact `125.698`, `0.36%` error). Fixed in `v8` with an explicit SymPy proof (`a_EM^-1(5) - a_EM^-1(6) = -(16/9)/(2 pi) ln(m_t/M_Z) < 0`), verified by disjoint `GL4` Referee `v3` to **`2.053e-9`** across all 5 runs (`9.929e-10` on `LINK6`/`HYBRID`).
    2. **`DISC-OW27-C`:** `svd_asc_mp` squaring $M_R M_R^\dagger$ at 35 dps misclassified `24` rank-2 `(q_R=1, K_6)` cases as nonsingular (`288` vs exact `264`). Fixed in `v8` via non-squaring real `6x6` `eigsy` singular-value extraction (`min_sv_real6_sym`), yielding exact **`264 / 384`** nonsingular (`120` singular, `0 / 384` hits).
  - Plus **3 non-blocking polish diagnostics** (`DIAG-1` explicit `nf_active_at_confinement` + `Lambda_QCD_5` + `Lambda_QCD_active` in `LOCK_V3`; `DIAG-2` per-$m_0$ self-consistent $\Lambda_{\text{QCD}}$ DM column; `DIAG-3` & `v2` prose notes in `A2-OW16 v22`) all fixed and confirmed `non_blocking_diagnostics = []` by Referee `v3`.
  - Cold-Room Referee `v2` (`ac596571b -> 0277b2805`, frozen untouched) confirmed `0` bugs in `v8` (its lone flag was its own lowered `N=500` GL4 Boltzmann Richardson overshoot; Referee `v3` at asymptotic `N=1000 vs 2000` confirmed `v8`'s Radau IIA `Y_B` to **`1.244e-7`**!).

---

## 2. Physics Closures & Brutally Honest Pre-Peek Findings (`0 of 19`)

### `OW27-A` — Sub-Percent `M_Z` & `m_t` Pole-Mass, Top Decoupling, Veltman $\Delta\rho$, & Pure-QCD $\Lambda_{\text{QCD}}/v_{\text{EW}}$
- **Pure-QFT SymPy Proofs (`all_sympy_proofs_exact = True`):**
  - Exact 2-loop pure-QCD Gray–Broadhurst–Grafe–Schilcher (1990) color sum $c_{20}(n_l=5) = 8.2365617010736$, exact Melnikov–van Ritbergen (`hep-ph/9912391`) inverse coefficient $c_2(\bar{m}(M)/M, n_l=5) = -9.1254505899625$, exact 2-loop RG $L$-dependence $(c_{11}, c_{21}, c_{22}) = (1, 121/24, 11/8)$ ($n_f=6$) and $(1, 389/72, 35/24)$ ($n_f=5$).
  - Exact 4-coupling 1-loop SM Higgs pole RG invariance $\beta_\lambda^{(1)} + \lambda \mu \partial_\mu \Delta_{\text{tot}}^{(1)} \equiv 0$ (`Delta_tot = Delta_t + Delta_h + Delta_W + Delta_Z`), plus exact 5-coupling 2-loop RG-log improvement vanishing identically at $L = 0$ ($\mu = \bar{m}_t(\bar{m}_t)$).
  - Exact 1-loop 5-flavor QED top decoupling sign (`< 0`) and exact 2-loop pure-QCD dimensional transmutation $\Lambda_{\text{QCD}}$ RG residual `== 0`.
- **Dimensionless `B4_UV` (`CURV_s12_Dirac`, $\alpha_{\text{UV}}^{-1}=24, t_{\text{SUSY}}=-48\pi/5, \tan\beta=15, \text{sgn}(\mu)=+1$) Results** (disjoint `GL4` Referee `v3` max rel err `3.059e-6`; 10-trial Haar $U(3)^5$: **`1.154e-29`**, Referee Xorshift64\*+Householder: **`1.455e-22`**):

| Observable (Dimensionless, `0 of 19`) | `m_0 = 10 v_EW` | `m_0 = 3 v_EW` | Notes |
|---|---|---|---|
| $\alpha_3^{(5)}(M_Z)$ / $\alpha_3^{(6)}(M_Z)$ | `0.188669` / `0.184952` | `0.148945` / `0.146911` | Exact 5-flavor decoupling at $\mu = \bar{m}_t(\bar{m}_t)$ |
| $\alpha_{\text{EM}}^{-1(5)}(M_Z)$ / $\alpha_{\text{EM}}^{-1(6)}(M_Z)$ | `125.697914` / `125.923773` | `124.953891` / `125.158582` | `DISC-OW27-1` remediated (`GL4` err `2.05e-9`) |
| $\sin^2\hat{\theta}_W(M_Z)$ / $s_W^{2,\text{OS}}$ | `0.221899` / `0.211357` | `0.227834` / `0.218939` | Veltman $\Delta\rho_t^{(1)} = 0.013549 / 0.011519$ |
| $m_W^{\text{pole}} / m_Z^{\text{pole}}$ (Veltman vs $\cos\hat{\theta}_W$) | `0.888056` (`0.882100`) | `0.883777` (`0.878730`) | Exact $+0.675\%$ / $+0.574\%$ EW pole shift |
| $m_t^{\text{pole}} / v_{\text{EW}}$ (2-loop `@ m_t`, $L=0$ vs 1-loop) | `0.918547` (`0.901023`) | `0.833029` (`0.821913`) | Fixed-point err `1.55e-26`; `@ M_Z` drift `0.91% / 0.45%` |
| $m_h^{\text{pole}} / M_Z$ (`@ m_t` vs `@ M_Z`, 2-loop RG-log drift) | `1.703135` (`0.0636%` drift) | `1.486939` (`0.0792%` drift) | Down **`55x`** from `3.46%` top-only (`CIM kH1min 3v = 1.2453`) |
| $n_{f,\text{conf}}$ & $\Lambda_{\text{QCD}}^{(5)} / v_{\text{EW}}$, $\Lambda_{\text{QCD}}^{(\text{act})} / v_{\text{EW}}$ | `nf=4`: `0.010296`, `0.012183` | `nf=4`: `0.003455`, `0.004523` | Zero empirical GeV; charm below confinement at $\alpha_{\text{UV}}^{-1}=24$ |

### `OW27-B` — First-Principles Thermal Bino LSP Freeze-Out (`OBS-20`, Strictly Dimensionless)
- **Explicit 4-Component Majorana Spinors** (Producer Weyl basis vs Referee Dirac–Pauli basis): massless $s$-wave $= 0$ (`< 1e-25`, Referee `1.62e-65`), massless $p$-wave `1/12` ($r \in \{2,5,10\}$, err `< 1e-10`, Referee `1.28e-13`), massive $t\bar{t}$ $s$-wave `1/8` constructive `L+R` (`< 1e-12`, Referee `2.64e-31`), flipped Fermi sign (`M_t + M_u`) caught cleanly (`0.01768 > 1e-4`), 26-var soft RGE $\sum_{i=1}^{15} N_i Y_i^4 = 95/18$ exact, `4x4` neutralino bino purity `>= 0.9698`.
- **Stiff Riccati Freeze-Out (`Radau IIA N=1600/3200` vs disjoint `GL4 N=800/1600`):** Analytic constant-$c$ Riccati err `5.01e-12` (Referee `1.58e-14`), step-halving `7.22e-7` (Referee `7.52e-8`), unreduced Planck fault `+322.2%`, Producer vs Referee max rel err **`1.104e-6`** across `m_0 / v_EW in {1, 3, 10, 30}` (`DIAG-2` per-$m_0$ own $\Lambda_{\text{QCD}}$ err **`8.396e-7`**):
  - **Zero $\tilde{\tau}_R$ coannihilation across entire universal soft grid:** `min Delta_stauR = +0.9197` (`92%` mass gap).
  - **Self-consistent per-$m_0$ dimensionless ratios** ($c_{\text{lat}} \equiv m_p / \Lambda_{\text{QCD}}^{(\text{act})}$ kept strictly symbolic, zero empirical $m_p$!):
    - `m_0 = 3 v_EW` (`nf=4`, $\Lambda_{\text{QCD}}^{(4)}/v_{\text{EW}} = 0.004523$): $x_f = 19.16$, $Y_{\tilde{B}}(\infty) = 3.9154 \times 10^{-10}$, **`c_lat * Omega_Bino / Omega_B = 6.435`**.
    - `m_0 = 10 v_EW` (`nf=4`, $\Lambda_{\text{QCD}}^{(4)}/v_{\text{EW}} = 0.012183$): $x_f = 19.11$, $Y_{\tilde{B}}(\infty) = 4.3802 \times 10^{-10}$, **`c_lat * Omega_Bino / Omega_B = 8.909`** (and **`12.521`** using `G_2` $M_{\text{GUT}}/M_{P,\text{red}} = \sqrt{\alpha_{\text{UV}}/(4\pi)}$).
    - `m_0 = 30 v_EW` (`nf=5`, $\Lambda_{\text{QCD}}^{(5)}/v_{\text{EW}} = 0.027872$): $Y_{\tilde{B}}(\infty) = 4.2689 \times 10^{-10}$, **`c_lat * Omega_Bino / Omega_B = 11.386`**.
  - **Honest Physical Assessment:** Inside `B4_UV`'s own predicted cosmology (strong $\Lambda_{\text{QCD}}/v_{\text{EW}} \sim 0.012$ and $Y_B = 1.7394 \times 10^{-8}$), $c_{\text{lat}} \cdot \Omega_{\tilde{B}}/\Omega_B \approx 6.4\text{--}12.5$ sits at $O(2\text{--}4)$ once divided by non-perturbative $c_{\text{lat}} \sim 3\text{--}4$; conversely, because $M_1 Y_{\tilde{B}} / v_{\text{EW}} = 1.888 \times 10^{-9}$ at $m_0 = 10 v_{\text{EW}}$ with zero stau coannihilation, if $Y_B$ and $\Lambda_{\text{QCD}}$ are reduced to smaller values, heavy pure bino LSP hits the standard SUSY thermal overclosure wall unless $m_0 \sim 1\text{--}2 v_{\text{EW}}$ or late moduli entropy dilution operates.

### `OW27-C` — Brutally Honest `0 / 384` & `0 / 192` True `tau_8^+` Spin-`1/2` Dirac Neutrino Wall (`OBS-18`)
- Independently re-derived `G_{s=1/2}(tau_8^+) = [1.07020250193, 0.868398142985, 1.06139935509]` (`Gauss-Bonnet err = 3.93e-8`, vs `OW26 v8 = 4.55e-12`, vs `ref26_v3 = 2.46e-8`).
- Under the **true `tau_8^+` chiral spin-`1/2` Dirac Kahler metric `G_{s=1/2}(tau_8^+)`** and pure lopsided `n_10 = (3, 2, 0)` (verified identically by Producer real `6x6` `eigsy` and Referee `mp.jtheta` + real `6x6` `eigsy` Takagi):
  - **Scan 1 (`384`-case `OW24-C` bare-`M_R` atlas, `264` nonsingular / `120` singular, Guardrail-1 priced at `log_2(384) = 8.585` bits): `0 / 384` simultaneous PMNS hits** in the fixed `OW24-C` window (`0.15 < s12sq < 0.55, 0.30 < s23sq < 0.70, s13sq < 0.08, 0.005 < dm < 0.15`).
  - **Scan 2 (`192`-case `M_R = I_3 + \widehat{W}_R^{\text{unit}}` scan on `q_R in {-5,-3,0,+2,+3,+5}`, Guardrail-1 priced at `log_2(192) = 7.585` bits, `sym6` slice `2.585` bits): `0 / 192` simultaneous PMNS hits.**
  - **Legacy reference (`5-6 / 5-6, q_R = 2, n_5bar = (0,0,0)`)** propagated sequentially (`N_3 -> N_2 -> N_1 -> M_SUSY -> M_Z`) + reduced-Planck Boltzmann (`GL4 N=1000/2000` vs `Radau IIA` max rel err **`1.244e-7`**, 10-trial Haar $U(3)^5 \times U(3)_N$ **`1.34e-32`**, Referee **`1.65e-25`**, exact CP-odd **`9.91e-41`**): `s12sq = 0.67081` (above `0.55`), `s23sq = 0.37068`, `s13sq = 0.04415`, `dm = 0.03483`, `delta_CP = -0.6253 pi`, `|m_ee|/m_3 = 0.2800`, `Y_B(tau_8^+) = +1.739405e-8 > 0` (dynamically selecting `tau_8^+`). **`OBS-18` remains honestly in `INTERNAL_WALL_OR_TENSION` — zero goalposts moved.**

### `OW27-D` — Exact 2-Loop NSVZ SUGRA Threshold Audit & Cross-Seat `agy-exp` `d12e74ef3` (`LINK6`) Propagation
- Exact SymPy 2-loop NSVZ RG invariance $\mu \frac{d}{d\mu}[\mu g^{-2/3} e^{-8\pi^2/(3 N g^2)}] \equiv 0$ (`PF5` omitting $g^{-2/3}$ yields nonzero $N g^2 / (N g^2 - 8\pi^2)$).
- **Hidden-Sector Window `[28, 32]` (NSVZ + `G_2` $M_{\text{GUT}}/M_{P,\text{red}}$):**
  - `SU(6)_hid` at $\alpha_{\text{hid}}^{-1} = 24$ lands directly at **`|t_SUSY| = 30.744`** (and `28.65, 31.79` at `22, 25`).
  - `SU(5)_hid` hits exact `B4_UV` $|t_{\text{SUSY}}| = 48\pi/5 = 30.1593$ at $\alpha_{\text{hid}}^{-1} = 19.3638$, requiring a hidden threshold shift **`Delta_hid = alpha_vis^-1 - alpha_hid^-1 = +4.6362`** (`Referee err = 3.89e-13`; exact sign & $O(1)$ magnitude of asymmetric gauge kinetic functions $f_{\text{vis}} \neq f_{\text{hid}}$).
  - Pure AMSB (`m_soft / m_{3/2} = g^2 / (16 pi^2)`) shifts $|t|$ deeper by `+5.7` (`0` hits in `[28, 32]`), favoring gravity/moduli mediation $m_{\text{soft}} \sim m_{3/2}$.
- **Cross-Seat Propagation of `agy-exp` `d12e74ef3` (`Card X-HIERARCHY-LINK6`) inside our 2-Loop `B4_UV` `M_Z` Pipeline** (`GL4` Referee `v3` max rel err **`1.083e-7`**, `aem5` **`9.93e-10`**):
  - **Pure `LINK6`** ($\alpha_{\text{GUT}}^{-1}=30.19350768, t_{\text{SUSY}}=-24.256$): $\alpha_3^{(5)}(M_Z) = 0.06792$, $\sin^2\hat{\theta}_W = 0.2530$, $\alpha_{\text{EM}}^{-1(5)} = 129.774$, $m_W^{\text{pole}}/m_Z^{\text{pole}} = 0.86717$, $m_t^{\text{pole}}/v_{\text{EW}} = 0.6110$, $m_h^{\text{pole}}/M_Z = 1.2913$ (`0.0062%` drift), $\Lambda_{\text{QCD}}^{(3)}/v_{\text{EW}} = 1.738 \times 10^{-5}$.
  - **Hybrid (`B4_UV` $\alpha_{\text{GUT}}^{-1}=24$ + `LINK6` $t_{\text{SUSY}}=-24.256$):** $\alpha_3^{(5)}(M_Z) = 0.11845$, $\sin^2\hat{\theta}_W = 0.23576$, $\alpha_{\text{EM}}^{-1(5)} = 113.680$, $m_W^{\text{pole}}/m_Z^{\text{pole}} = 0.87868$, $m_t^{\text{pole}}/v_{\text{EW}} = 0.7757$, $m_h^{\text{pole}}/M_Z = 1.4654$ (`0.036%` drift), $\Lambda_{\text{QCD}}^{(3)}/v_{\text{EW}} = 0.001354$ (`nf=3` cleanly perturbative below $m_c$).

---

**Bottom Line:** `agy-002/verify` stands at **`0 of 19`** with `Card A2-OW27 v8`, `B4_UV_MZ_BLIND_LOCK_V3` (`ce81cddd9d056a54fafa6b30d431073ae1af75399a1d82918f4e074f0bd98a2a`), `A2-OW16 v22` (`1/10/9/4 = 24`, `20/20` locks), and Cold-Room Zero-Trust Referee `v3` (`discrepancies_count = 0`, `non_blocking_diagnostics = []`, `294/294` SHA-256 manifests) fully sealed and parked pending `main`'s return and cross-seat peer audits before any empirical unblinding.
