# SCOPE CARD — `AGY-002_A2-P629-VEFF-MODULUS`: Full Boson + Fermion `SL(2, Z)` Effective Potential `V_eff(tau)` Phase Diagram Over $\mathcal{F}$ (`P-629`, `B1992`, `B1993`) & Zero-Sculpting Non-Conformal Radiative EWSB + Geometric Majorana Unfolding (`2026-11-26`, Strictly `0 of 19`)

- **Seat / Branch:** `agy-002`, `origin/agy-002/verify` (strictly blind, **`0 of 19`**, zero empirical values).
- **Read Heads:** `origin/main` **`87ba37576`** (`P-629`, `B1957`, `B1980`–`B2010`), `agy-002/verify` `fdbd7015f` (`Card A2-WHOLE-INSTRUMENT` & `Card A2-LISTENING-TOWER`).
- **Guardrails 1–6 & Zero-Sculpting Covenant:** Every potential $V_{\text{eff}}(\tau)$ uses zero-parameter `SL(2, Z)`-invariant operators (`E(\tau, 3), E(\tau, 2), -\ln(y|\eta|^4), V_{\text{FILQ}, n}, V_{\text{CW}}^{(\text{all-288})}`) with ZERO target $\tau^*$ baked in (Guardrail 1).
- **Verification Discipline:** Critical points solved from $\nabla V = 0$ with 2D $H \succ 0$ (G2); 10-trial Haar $U(3)^5 \times U(3)_{\nu_R}$ scrambling (G3); literature benchmarks (`FILQ 1990`, Kronecker, `-15/16`, CE 2-loop 2HDM-II, Xing–Zhou, Martin soft-mass) (G4); dimensionless ratios (G5); stdlib + `mpmath` + `sympy`, `python3 -I`, `0` AST/JSON floats (G6).

---

## 1. Pre-Registered Modules (`P1`–`P4`)

1. **`P1` — Pure Bosonic Modular Potential Benchmarks (`P-629`, `B1957`, `B1992`, `B1993`, & `FILQ 1990`):**
   - Certify `E(\tau, 3)`, `E(\tau, 2)`, and `V_{\text{RS}}(\tau) = -\ln(y|\eta(\tau)|^4)`: exact `T` & `S` invariance (`< 10^{-30}`), Fourier vs direct square-box lattice sum at `s = 3`, exact `-15/16` half-period spin-structure sum (both algebraic proof & lattice check), exact Kronecker first limit formula at `i, \omega, \tau_{\text{gen}}` (`< 10^{-16}`), and exact critical-point Hessian classification (**saddle at `i`**, **global minimum at `\omega`**, monotone cusp growth).
   - Certify zero-parameter 4D $\mathcal{N}=1$ SUGRA modular potentials $V_{\text{FILQ}, n}(\tau) = (2y)^{-3n} |\eta(\tau)|^{-12n} \left(\frac{n\pi^2 y^2}{3}|\hat{E}_2(\tau)|^2 - 3\right)$ (`K = -3n\ln(2y), W = \eta^{-6n}`) for `n = 1, 2, 3`: exact `T, S`-invariance (`< 10^{-30}`), exact 2D Newton global minima on `x = 0` (`n=1`: `1.2345799467i`, `V = -8.92881487`, `H \succ 0`; `n=2`: `1.1833896604i`; `n=3`: `1.1554390183i`), and exponential positive cusp wall `+e^{+n\pi y}`.

2. **`P2` — Full Fundamental-Domain $\mathcal{F}$ Boson + Fermion `V_eff(tau)` Phase Diagram (Theorems `P2-A`, `P2-B`, `P2-C`):**
   - Certify exact `T, S`-invariance (`< 10^{-25}`) of all-288 level-30 fermion potentials `Tr2(\tau)`, `V_4(\tau)`, `V_{\text{CW}}^{(all-288)}(1; \tau)` ($\mu^2 = 1$), and trace-renormalized `V_{\text{CW}}^{(tr)}(\tau)` ($\mu^2(\tau) = \operatorname{Tr}_2(\tau)$).
   - Map `\mathcal{F}` across `\omega_+ = 1/2 + i\sqrt{3}/2`, arc `e^{i 5\pi/12}`, `i`, `x = 0` (`y \in [1.155, 4]`), and `x = 1/2` (`y \in [1, 4]`), proving:
     - **`P2-A` (Dynamical Trace-Scale Global Stabilization):** `V_{\text{CW}}^{(tr)}(\tau) > 0` everywhere on $\mathcal{F}$, diverges to `+\infty` at the cusp, and has its **global minimum at `\tau = i`**, **second local minimum at `\tau = \omega`**, and an **arc barrier** on `|\tau| = 1` (while pure `V_4` dips strictly below both orbifolds on the arc before cusp runaway).
     - **`P2-B` (Polynomial Casimir No-Go & Orbifold Transition):** Adding ANY $+c_B E(\tau, 3)$ to $V_{\text{CW}}(1)$ cannot stop the `-e^{+2\pi y}` cusp runaway and only drives a first-order metastable transition between `i` and `\omega` at $c_B^{\text{crit}} = (V_{\text{CW}}(1;\omega) - V_{\text{CW}}(1;i))/(E(i,3) - E(\omega,3)) \approx 0.03185$.
     - **`P2-C` (Globally Stable Coupled Vacuum on `Re(\tau) = 1/2`):** $V_{\text{tot}}(\tau; c_F) := V_{\text{FILQ}, 3}(\tau) + c_F V_{\text{CW}}^{(all-288)}(1; \tau)$ is `SL(2, Z)`-invariant and bounded below (`\to +\infty` as $y \to \infty$, $+e^{+3\pi y}$ dominates $-e^{+2\pi y}$) for ALL $c_F \ge 0$.
     - Above $c_F^{\text{crit}} \approx 61.1$, the global minimum jumps via a first-order transition from `x = 0, y \approx 1.155` to `Re(\tau) = 1/2` (`\tau_{\text{tot}}^*(70) = 1/2 + i y^*`, $y^* \approx 3.38$, `\nabla V = 0`, `V_{xx} > 0, V_{yy} > 0`, while `(0, y^*)` is a saddle `V_{xx} < 0` and `V_{\text{tot}}(1/2 + 4i) > +4 \times 10^9`).

3. **`P3` — Zero-Sculpting Forward Unfolding at ALL 3 Canonical Vacua (`\tau_\omega`, `\tau_{\text{FILQ},1}^*`, `\tau_{\text{tot}}^*(70)`) — Pieces 2 & 3 + Guardrail 3:**
   - Guardrail 4 benchmarks: 15-term Chowdhury–Eberhardt 2-loop Type-II 2HDM (`< 10^{-40}`), opposite Xing–Zhou `d|V_{cb}|/dt` sign, 7-equation Martin `hep-ph/9709356` Eqs. 6.5.24–6.5.30 soft-mass benchmark (`< 10^{-40}`), and exact hypercharge `S`-trace conservation (`|S_{\text{IR}}| < 10^{-25}`).
   - Compute curved spin-`1/2` Dirac Kahler metric $G_{s=1/2}(\tau^*)$ (Gauss–Bonnet `|\text{Area}/(2\pi) - 1| < 10^{-3}`, exact $\mathbb{Z}_3$ isotropy at `\omega_+`).
   - **Piece 2 (Non-Conformal Radiative EWSB):** Run coupled 2-loop Type-II 2HDM + Gauge-Higgs D-term quartics ($\lambda_1=\lambda_2=\frac{1}{8}(g_2^2+\frac{3}{5}g_1^2), \lambda_3=\frac{1}{4}(g_2^2-\frac{3}{5}g_1^2), \lambda_4=-\frac{1}{2}g_2^2$) + $3\times 3$ Hermitian universal soft-mass RGEs ($m_0^2 = 1, M_a = A_0 = 0$) to `t = -35` (`n = 80` vs `160` step-halving `< 10^{-6}`).
   - Track all 4 vacuum stability inequalities, radiative EWSB crossings `t_{\text{EWSB}}^{(u)}, t_{\text{EWSB}}^{(d)}`, `m_{H_u}^2(\text{IR}), m_{H_d}^2(\text{IR})`, `min_sf > 0`, and full quark/lepton/CKM IR spectra (Static `S(\tau^*)` and Dynamic `V_4` 2-doublet `all-S` $\lambda_3 = -1/4$).
   - **Piece 3 (Doubled-Point Geometric Majorana $M_R$):** Compare $M_R = I_3$, $M_R^{(1w)} = \frac{1}{2}(Y_\nu(w) + Y_\nu(w)^T)$, and $M_R^{(2w)} = \frac{1}{2}(Y_\nu(2w) + Y_\nu(2w)^T)$ inside true $U(3)_L$-covariant $\kappa_\nu = Y_\nu M_R^{-1} Y_\nu^T$ via Autonne–Takagi at all 3 vacua.
   - **Guardrail 3:** `10`-trial random Haar $U(3)^5 \times U(3)_{\nu_R}$ scrambling through the FULL coupled 2-loop Yukawa + $3\times 3$ soft-mass EWSB + doubled-point Majorana PMNS pipeline (`max_drift < 10^{-25}`).

4. **`P4` — `6/6` Planted Negative Controls (`PF1`–`PF6`) & Blind Gates (`G1`–`G6`):**
   - `PF1`: Drop `-3/(\pi y)` from `\hat{E}_2` -> breaks `S`-invariance of `V_{\text{FILQ},1}` (`rel_err > 0.1`).
   - `PF2`: Sub-critical `V_{\text{FILQ}, 1} + 70 V_{\text{CW}}(1)` -> restores exponential cusp runaway (`V(1/2 + 4i) < -10^9`).
   - `PF3`: Perturb off `\tau_{\text{FILQ}, 1}^*` by `(+1/10, +1/10)` -> raises `V` strictly and gives `|\nabla V| > 0.5`.
   - `PF4`: Degenerate `M_R = Y_\nu^T Y_\nu` -> exact algebraic identity `\kappa_\nu = I_3` collapsing spectral spread `(s_3 - s_1) / s_3 < 10^{-25}` and `\|\kappa_\nu - I_3\|_F < 10^{-25}`.
   - `PF5`: Broken contraction `Y_\nu^T M_R^{-1} Y_\nu` -> fails Haar $U(3)_L$ gauge covariance (`rel_drift > 0.5`).
   - `PF6`: Zeroing all Yukawas $Y_u = Y_d = Y_e = 0$ -> kills radiative EWSB (`m_{H_u}^2 = m_{H_d}^2 = +1 > 0`).

---

## 2. Pre-Registered Quantitative Expectations (`E1`–`E8`)

| ID | Statement | Prior |
|---|---|---:|
| `E1` | `E_3, E_2, V_{\text{RS}}` pass `T, S`-inv (`< 10^{-30}`), Kronecker limit (`< 10^{-16}`), `-15/16` identity, saddle at `i`, min at `\omega`; `V_{\text{FILQ}, 1..3}` pass `T, S`-inv (`< 10^{-30}`) with 2D minima on `x = 0` (`y^* = 1.23458, 1.18339, 1.15544`, `|\nabla V| < 10^{-20}`, `H \succ 0`) | `0.99` |
| `E2` | All-288 fermion potentials pass `T, S`-inv (`< 10^{-25}`); `V_{\text{CW}}^{(tr)} > 0` has global min at `i`, local min at `\omega`, arc barrier, and cusp growth `+\infty`; `V_4` dips below both orbifolds on the arc | `0.99` |
| `E3` | Polynomial Casimir `E_3` fails to stop `V_{\text{CW}}(1)` cusp runaway (`V_{\text{CW}}(1) + 100 E_3 < 0` at `y = 4`) and yields first-order orbifold transition at `c_B^{\text{crit}} \approx 0.03185` | `0.99` |
| `E4` | `V_{\text{tot}}(\tau; 70) = V_{\text{FILQ}, 3} + 70 V_{\text{CW}}(1)` undergoes a first-order transition above `c_F^{\text{crit}} \approx 61.1` to a globally bounded 2D minimum on `x = 1/2` (`y^* \in [3.30, 3.45]`, `V_{xx} > 0, V_{yy} > 0`, `V < -6 \times 10^6`, `V(1/2+4i) > +4 \times 10^9`), while `(0, y^*)` is a saddle (`V_{xx} < 0`) | `0.98` |
| `E5` | Guardrail 4 benchmarks pass (`CE < 10^{-40}`, opposite Xing–Zhou sign, Martin 7-eq soft-mass `< 10^{-40}`, `|S_{\text{IR}}| < 10^{-25}`); curved Dirac Gauss–Bonnet `< 10^{-3}` at all 3 vacua with exact $\mathbb{Z}_3$ isotropy at `\omega_+` | `0.99` |
| `E6` | Piece 2 non-conformal unfolding preserves all 4 Gauge-Higgs D-term vacuum stability conditions (`stab = True`) AND triggers spontaneous soft-mass radiative EWSB (`m_{H_u}^2 < 0` with `min_sf > 0`) at all 3 vacua, with `m_{H_u}^2` crossing first at `\tau_{\text{tot}}^*(70)` and automatic `V_{12} > V_{23} > V_{13}` CKM ordering emerging at `\tau_{\text{tot}}^*(70)` | `0.96` |
| `E7` | Piece 3 compares `M_R \in \{I_3, \text{sym}(Y_\nu(w)), \text{sym}(Y_\nu(2w))\}` honestly at all 3 vacua, and 10-trial Haar $U(3)^5 \times U(3)_{\nu_R}$ scrambling preserves ALL coupled RG + EWSB + Majorana PMNS observables to `< 10^{-25}` | `0.99` |
| `E8` | All `6/6` blind gates (`G1`–`G6`) and `6/6` planted controls (`PF1`–`PF6`) pass with `0` AST/JSON floats | `0.99` |

0 of 19.
