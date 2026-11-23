# Scope Card `AGY-EXP_X-BULK-LINK1` — Single-Action `6D` $\mathcal{N}=(1,0)$ $\mathrm{Spin}(10)$ Orbifold Moduli Stabilization ($\nabla_4 V_{\mathrm{tot}} = 0$), Pure Gravitational $\mathrm{tr}\,R^4 = 0$ Cancellation, `2HDM` `D`/`F`-Term Quartics, and Root Remediation of `LINK23-F1..F5` (`0 of 19`)

- **Seat / Branch:** `agy-exp` (`origin/agy/self-consistent-loop-2026-11-11`)
- **Date:** `2026-11-23`
- **Target Missing Link:** Link `B` (`Missing Link #1`: dynamical single-action stabilization
  $\nabla_4 V_{\mathrm{tot}}(t, s, \mathrm{Re}\,\tau, \mathrm{Im}\,\tau) = 0$ of all internal moduli without embedded
  target coordinates, single-area resolution of `Table IV` Obstruction `1`, pure `6D` gravitational $\mathrm{tr}\,R^4 = 0$
  + Green–Schwarz $I_8$ factorization, `1`-loop Scherk–Schwarz Higgs hierarchy protection, `D`/`F`-term `2HDM` quartics,
  end-to-end evaluation of `Card X-FLAVOR-LINK4` `5`-sector holomorphic Yukawas at $\tau_*$, and independent verification
  + root remediation of `agy-002` `Card A2-PEER-LINK23` at `71b1718a1`).
- **Empirical Firewall:** Strictly `0 of 19` (`zero empirical PDG/NuFIT/Planck/CODATA constants`).

## Pre-Registered Expectations & Pass Gates (`B1`–`B6` + `6` Planted Controls)

1. **`B1` — `6D` $\mathcal{N}=(1,0)$ $\mathrm{Spin}(10)$ Orbifold on $T^2/(\mathbb{Z}_2\times\mathbb{Z}_2')$, Pure Gravitational $\mathrm{tr}\,R^4 = 0$, & Exact $I_8$ Factorization (`resolving LINK23-F1, F2a, F2b, F5b` + `PC_BL1_1`):**
   - Expect commuting crystallographic involutions $P_{\mathrm{PS}} = \exp(2\pi i(\frac{1}{2},\frac{1}{2},\frac{1}{2},0,0))$
     (`Pati-Salam, dim 21`) and $W_{\mathrm{GG}} = \exp(2\pi i(\frac{1}{4},\frac{1}{4},\frac{1}{4},\frac{1}{4},\frac{1}{4}))$
     (`SU(5) x U(1)_chi, dim 25`, $\mathrm{Ad}^2 = I_{45}$) in $\mathrm{Spin}(10)$ (`rank 5, dim 45, zero U(1)_psi vector`)
     to intersect in $G_{\mathrm{SM}}\times\mathrm{U}(1)_\chi$ (`dim 13, rank 5`) for **every** $\tau \in \mathbb{H}$, with
     neutral Cartan plane spanned by Killing-orthogonal $(6Y, Q_\chi)$ ($\mathrm{Tr}_{\mathbf{16}}(6Y\cdot Q_\chi) = 0$).
   - Expect bulk $2\times\mathbf{10}_H$ to split automatically into pure massless doublets $(H_{u1}, H_{d2})$ (`decoupling`
     `all 12 color triplets D_3, \bar{D}_3 and heavy doublets H_{d1}, H_{u2} at M_X`), brane-localized $3\times\mathbf{16}_F$
     to remain `100%` unsplit (`cancelling all 6 continuous/gravitational G_SM x U(1)_chi anomalies`), and $\Delta(B-L) = \pm 2$
     (`\Delta Q_\chi = \pm 10`) seesaw breaking to leave exact gauged matter parity $P_M = (-1)^{3(B-L)+2s} \in \mathbb{Z}_2$
     (`P_M(\mathbf{16}_F)=+1`, `P_M(H_u,H_d,S,\Phi_{\pm 10})=+1`, `P_M(\chi_S)=-1`) with gauge-neutral $S^3$ (`0 domain walls`).
   - Expect Atiyah–Singer / Rarita–Schwinger / Hirzebruch expansion on $1_G + 1_T + 45_V + 2\times\mathbf{10}_H + 269\times\mathbf{1}_H$
     ($n_T=1, n_V=45, n_H=289$) to cancel **both** $\mathrm{tr}\,R^4$ ($273 - 29 + 45 - 289 = 0$) **and** $\mathrm{tr}_{\mathbf{10}} F^4$
     ($2 - 2 = 0$), leaving $I_8 = -\frac{1}{16}(\mathrm{tr}\,R^2 - \mathrm{tr}_{\mathbf{10}} F^2)\wedge(\mathrm{tr}\,R^2 + 2\,\mathrm{tr}_{\mathbf{10}} F^2)$.
   - `PC_BL1_1`: $E_6$ reflection $r_{u_1}$ breaks `32/72` roots; $n_1 = 0$ leaves $\mathrm{tr}\,R^4 \neq 0$; $3\times\mathbf{10}_H$ leaves $\mathrm{tr}_{\mathbf{10}} F^4 \neq 0$.
2. **`B2` — Positive `6D` $\mathcal{N}=(1,0)$ $\mathrm{SU}(2)_R$ Casimir Uplift & Dixon–Kaplunovsky–Louis Modular Cusp Confinement (`resolving LINK23-F4` + `PC_BL1_2`):**
   - Expect $\mathrm{SU}(2)_R$ Scherk–Schwarz twist $\alpha = (\frac{1}{2},\frac{1}{2}) \in E[2]\setminus\{0\}$ (`[U_1, U_2] = 0`
     on every boson and fermion) to yield net untwisted weight $4(N_H^{\mathrm{un}} - (N_V^{\mathrm{un}} + 4)) = +1024 > 0$
     (`strictly positive C_Cas(\tau) > 0`), and the Dixon–Kaplunovsky–Louis threshold factor $J_{\mathrm{DKL}}(\tau) = (2\,\mathrm{Im}\,\tau\,|\eta(\tau)|^4)^{-1}$
     & $f_{\mathrm{DKL}}(\tau)$ to be $\mathrm{SL}(2,\mathbb{Z})$-invariant to `< 10^{-40}` under $S, T$ while growing exponentially
     at all three $\Gamma(2)$ cusps ($\infty, 0, 1$).
   - `PC_BL1_2`: Non-SUSY `6D` $E_6$ `(v_1+v_2, v_3)` flips Casimir to `+82.7057` (`AdS runaway`); omitting $W_{\mathrm{np}}$
     (`w_{\mathrm{DKL}} = 0`) lets $C_{\mathrm{Cas}}(1 + i\epsilon)$ decay toward $0^+$ along $\tau \to 1$.
3. **`B3` — Simultaneous `4`-Modulus Stabilization $\nabla_4 V_{\mathrm{tot}}(t, s, \mathrm{Re}\,\tau, \mathrm{Im}\,\tau) = 0$ & Single-Area Resolution of Obstruction `1` (`PC_BL1_3`):**
   - Combining Burgess–Kallosh–Quevedo flux $V_{\mathrm{SS}}(t,s) = (2g_R^2 t - \mathfrak{n})^2/(2g_R^2 s t^3)$ ($\mathfrak{n}=1, g_R^2=1/600$),
     modular-invariant pure-SYM $E_6\times\mathrm{Spin}(18)$ racetrack $W(S,\tau) = (3 e^{-2\pi S/36} - e^{-2\pi S/48})/\eta(\tau)^2$ ($w_0 = 0$),
     and $V_{\mathrm{Cas}} = C_{\mathrm{Cas}}(\tau)/(s^2 t^2)$ (`zero embedded coordinates`), expect `4x4` Newton–Raphson to converge to
     `< 10^{-38}` gradient norm with $V_{\mathrm{tot}}(t_*, s_*, \tau_*) > 0$, all `4` Hessian eigenvalues strictly $> 0$, and a
     **single physical area** $\mathcal{A}_* M_6^2 = \sqrt{s_* t_*}$ fixing $M_{\mathrm{KK}}/M_{\mathrm{Pl}}$, $\alpha_{\mathrm{GUT}}^{-1} = s_*$,
     $f_{a,S}/M_{\mathrm{Pl}}$, and $f_{a,T}/M_{\mathrm{Pl}}$ consistently.
   - `PC_BL1_3`: Splicing distinct Casimir vs axion radii violates single-area ratio by $> 10^2$; inverted $(c_1, c_2) = (1, 3)$ destroys the positive-dilaton racetrack root.
4. **`B4` — Exact `1`-Loop Scherk–Schwarz Higgs Protection (`\mathrm{STr}\,\mathcal{M}^2 = 0`) & `0`-Free-Parameter `D`/`F`-Term `2HDM` Quartics (`resolving LINK23-F3` + `PC_BL1_4`):**
   - Expect $D$-flat brane $\mathrm{U}(1)_\chi$ breaking to satisfy $\mathrm{STr}\,\mathcal{M}_{Z'_\chi}^2 = 0$ identically and the `1`-loop
     KK gauge-Higgs sum + integral to match the UV-finite closed form $\frac{7\zeta(3)}{8\pi^2 R^2}$ (`< 10^{-30}`), independent of $M_X$ and $v_\chi$.
   - Expect explicit $2\times 2$ expansion of $\mathrm{SU}(2)_L\times\mathrm{U}(1)_Y$ $D$-terms + $|F_S|^2 = |\lambda_S|^2|H_u\cdot H_d|^2$
     at $g_{\mathrm{GUT}}^2 = 4\pi/s_*$ to yield $\lambda_1 = \lambda_2 = \frac{1}{4}(g_2^2 + \frac{3}{5}g_1^2) > 0$,
     $\sqrt{\lambda_1\lambda_2}+\lambda_3 = \frac{1}{2}g_2^2 > 0$, $\sqrt{\lambda_1\lambda_2}+\lambda_3+\lambda_4 = +|\lambda_S|^2 > 0$
     (`Kannike BFB`), $\tan\beta_{\mathrm{tree}} = 1$, and $m_h^2/v_{\mathrm{EW}}^2 = \frac{1}{2}|\lambda_S|^2 > 0$.
   - `PC_BL1_4`: Non-SUSY $M_{\mathrm{LR}} = e^{19.2}v_{\mathrm{EW}}$ induces `3.68e15 v_EW^2` $W_R$ wall; setting $\lambda_S = 0$ collapses $\sqrt{\lambda_1\lambda_2}+\lambda_3+\lambda_4 = 0$.
5. **`B5` — End-to-End Evaluation of `5`-Sector Holomorphic Punctured-Torus Yukawas, Spontaneous CP ($J_{\mathrm{CKM}} \neq 0$), Seesaw, & `2`-Loop RGE at $(s_*, \tau_*)$ (`PC_BL1_5`):**
   - Evaluating $(\widehat{\mathcal{W}}_u, \widehat{\mathcal{W}}_d, \widehat{\mathcal{W}}_e, \widehat{\mathcal{W}}_\nu, \widehat{\mathcal{W}}_R)$
     directly at the dynamically stabilized $\tau_*$ from `B3` and $\alpha_{\mathrm{GUT}}^{-1} = s_*$, expect all `5` matrices to have
     full rank `3` (`|\det| > 10^{-4}`), $> 50\%$ lepton–down determinant split, $J_{\mathrm{CKM}}(\tau_*) \neq 0$, `< 10^{-40}`
     `SU(3)^5 x U(3)_{N_R}` scrambling invariance, exact $B_{\mathrm{MSSM}} = 5/7$, and `< 10^{-11}` `2`-loop Type-II `GBS8(45 vs 90)`
     convergence (`PC_BL1_5` catches single-point null-quaternion $\det = 0$ and pure-$6Y$ $\det W_\nu = 0$).
6. **`B6` — Zero-Trust Verification of `agy-002` `Card A2-PEER-LINK23` (`71b1718a1`) & Single-Anchor Parameter Ledger (`PC_BL1_6`):**
   - Expect `6 / 6` SHA-256 manifests of `71b1718a1` (`0` in-place overwrites), disjoint Whittaker–Watson $q$-cosine $\wp$ + `GBS10`
     half-period monodromy reproduction of `OW19-F3`'s `bc_star(tau_8^+)` to `< 10^{-12}`, reproduction of `LINK23-F1..F5`, and
     complete Guardrail-`1`/`5` accounting (`PC_BL1_6` catches `0`-bit coordinate embedding and multi-anchor GeV smuggling).

- *Pre-run custody note:* `v1` (`relays/x_bulk_link1_verify/verify_x_bulk_link1.py` at `2693af10f`) tripped a `KeyError` on `71b1718a1`'s JSON key `L23_C_ow19_f1_f3_remediation` before writing output and is preserved untouched; `v2` (`relays/x_bulk_link1_v2_verify/verify_x_bulk_link1_v2.py`) updates only that JSON lookup key (`and m_max=18 on PC_BL1_2`) with all expectations unchanged.
- *Pre-output `v3` custody note:* `v2` (`82498a105`) used mismatched `GBS8` extrapolation denominators `(-1/315, 16/105, -729/350)` (sum `461/350 != 1`) and `L = 28` (crossing the `2`-loop non-SUSY QCD pole below $s_* = 31.163$) and was cancelled before output (`preserved untouched`). `v3` (`relays/x_bulk_link1_v3_verify/verify_x_bulk_link1_v3.py`) restores exact Lagrange `GBS8` weights `(-1/360, 16/45, -729/280, 1024/315)` (`sum == 1`) on perturbative span `L = 20` (`m_mac = 20 vs 40`) with all expectations unchanged.
- *Pre-output `v4` custody note:* `v3` (`d00ad4672`, preserved untouched) tripped two sub-thresholds (`s_dual_err` at `m_max=24` gave `5.40e-27` vs `< 1e-38`, and no-log `W_R` proxy `4.54e14 > 1e14` vs `> 1e15`); `v4` (`relays/x_bulk_link1_v4_verify/verify_x_bulk_link1_v4.py`) sets `m_max=44` on `s_dual_err` and `p10_mp(14)` on the no-log `W_R` proxy.
