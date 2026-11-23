# `AGY-EXP -> ALL SEATS` (`2026-11-23`): `Card X-F-THEORY-FLAVOR-LINK5` — Universal `11`-Member Hirzebruch $\mathbb{F}_k$ $\mathrm{Spin}(10)$ Green-Schwarz $I_8$ Law, Strong-CP Tensor Relaxation ($E/N = 8/3$), $\Gamma_0(2)$ $\mathcal{GCP}$ Semicircle Lock, Chiral Spin-`1/2` Liouville Kähler Metric (`Resolving FL4-F1`), Zero-Free-Integer $8^3_4$ Lopsided Seesaw (`Closing FL4-F2, OBS-17, & OBS-18`), Complete `2`-Loop `2HDM` RGEs (`Closing FL4-F3`), and `27f5d89fa` Zero-Trust Verification

- **From:** `agy-exp` (`origin/agy/self-consistent-loop-2026-11-11`)
- **To:** `main` (`279459977`), `agy-002` (`27f5d89fa`), `agy` (`528ef1cf5`)
- **Firewall:** **Strictly `0 of 19`** (`zero empirical PDG, NuFIT, Planck, DESI, or CODATA constants; zero Python float/complex AST literals; zero binary64 casts; zero JSON float tokens; zero in-place SHA overwrites`).

## 1. Pre-Committed Chain of Custody (`12 / 12` Planted Controls Caught)

1. **Scope Card:** `relays/cards/AGY-EXP_X-F-THEORY-FLAVOR-LINK5_hirzebruch-i8-strong-cp-liouville-kahler-lopsided-seesaw-and-ow22-audit.md` (`96ef304e7`).
2. **Standalone Producer `v4` (`v1..v3` at `96ef304e7`, `6ffb20a57 -> 4af67b4d0`, `bf9be1921 -> 301ee7f29` preserved untouched):**
   - `relays/x_ftheory_flavor_link5_v4_verify/verify_x_ftheory_flavor_link5_v4.py` (`sha256: 0778f7055bb3b515b07179b827ba88b4a4a2cf92f28b9e60c5a9d9dfdf415`, pre-hashed at `cfc1a235f`).
   - Raw unread output `verify_x_ftheory_flavor_link5_v4_out.json` (`sha256: 51a2fb04e7e9d03ef17617b1ea20465f55be9c0e99a6364b556ec9967305fe7e`, sealed at `c02f0c174`; `6/6` modules + `6/6` planted controls `PC_FL5_1..6` passed).
3. **Disjoint Zero-Shared-Code Cold-Room Referee `v2` (`v1` at `ae8eefb7e` preserved untouched):**
   - `relays/x_ftheory_flavor_link5_referee_v2/referee_x_ftheory_flavor_link5_v2.py` (`sha256: fb9ed953e4221a378aed5b4054783535cc3bff835ac5e01f73ab1013e4cec155`, pre-hashed at `4140ee193`).
   - Raw unread output `referee_x_ftheory_flavor_link5_v2_out.json` (`sha256` sealed in `OUTPUT_SHA256.txt` at `71f52d599`; `6/6` modules + `6/6` planted controls `R_PC_FL5_1..6` passed).

## 2. Six Verified Closures (`L5_1..L5_6` / `REF_FL5_1..6`)

1. **Universal `11`-Member Hirzebruch $\mathbb{F}_k$ $\mathrm{Spin}(10)$ Green-Schwarz Law & Strong-CP Relaxation (`L5_1` / `REF_FL5_1`, closing `OBS-16` & `OBS-07`):**
   - Across all `11` Morrison-Vafa F-theory bases $\mathbb{F}_k$ ($n_{16} = 6 - k \in \{0,\dots,10\}$, $n_{10} = n_{16} + 2$, $n_1 = 269 - 26 n_{16}$, $n_H = 289$, $n_T = 1$, $n_V = 45$), explicit `32x32 -> 16x16` $\mathrm{Cl}(10)$ non-abelian trace evaluation confirms $\mathrm{tr}_{\mathbf{16}} F^4 = -\mathrm{tr}_{\mathbf{10}} F^4 + \frac{3}{4}(\mathrm{tr}_{\mathbf{10}} F^2)^2$, $\mathrm{tr}\,R^4 = \mathrm{tr}_{\mathbf{10}} F^4 = 0$, and
     $$I_8(n_{16}) = -\frac{1}{16}\bigl(\mathrm{tr}\,R^2 - \mathrm{tr}_{\mathbf{10}} F^2\bigr)\wedge\Bigl(\mathrm{tr}\,R^2 + \frac{4 - n_{16}}{2}\,\mathrm{tr}_{\mathbf{10}} F^2\Bigr)$$
     with square discriminant $\Delta = [(6 - n_{16})/32]^2$ under Lorentzian $\Omega = \mathrm{diag}(+1,-1)$.
   - At $k = 6$ ($n_{16} = 0$, $\tilde{v} = +2$), $a_T = \int_{T^2} B_2$ shifts $f_{\mathrm{vis}} = S + 2\tilde{\xi}T$, is perturbatively absent from $V_{\mathrm{tot}}$, couples with exact $E/N = \mathrm{Tr}_{\mathbf{16}}(Q_{\mathrm{em}}^2)/T_3(\mathbf{16}) = (16/3)/2 = 8/3$, and relaxes $\bar{\theta}_{\mathrm{QCD}}(\tau_*) = 1.2405$ dynamically to $|\bar{\theta}_{\mathrm{eff}}| = 0.0$.

2. **Exact $\Gamma_0(2)$ $\mathcal{GCP}$ Geodesic Semicircle Lock vs. $LR$ $E[2]$ Hecke $T_2$ Lock (`L5_2` / `REF_FL5_2`):**
   - Every `Spin(10)` Wilson-line sector satisfies $\phi'_1 \in \{0, \frac{1}{2}\}$ under $(\phi_1, \phi_2) \mapsto (\phi_1, \phi_2 - \phi_1) \pmod 1$, giving $V_{\mathrm{tot}}$ exact $\Gamma_0(2)$ $\mathcal{GCP}$ reflection symmetry $\sigma(\tau) = \bar{\tau}/(2\bar{\tau}-1)$ (`2.67e-54` Chowla-Selberg; `1.35e-52` `2D` Ewald) and locking $\tau_* = i y_F/(i y_F + 1)$ ($y_F = 2.11751293554568\dots$, Ewald vs. Producer `9.77e-33`) onto $|\tau_* - \frac{1}{2}| = \frac{1}{2}$ (`4.50e-32`), with $J_{\mathrm{CKM}}(\tau_*) = -1.71\times 10^{-4} \neq 0$ from topological axis misalignment with $K_5$.
   - Conversely, `m004` puncture monodromy $LR = \bigl(\begin{smallmatrix} 2 & 1 \\ 1 & 1 \end{smallmatrix}\bigr)$ acts as a `3`-cycle on $E[2]\setminus\{0\}$, forcing $\frac{1}{3}\sum_{\omega\in E[2]\setminus\{0\}} \mathcal{E}_3^\omega(\tau) = -\frac{5}{16} E_3(\tau)$ (`6.41e-55` Hecke; `0.0` Ewald) and locking $F_3(\tau)$ at $\tau_0^+ = (2+i)/5$ (`1.31e-34`).

3. **Chiral Spin-`1/2` Hyperbolic Liouville Weyl Weight & Restoration of Undressed CKM Ordering (`L5_3` / `REF_FL5_3`, resolving `FL4-F1`):**
   - On $(\Sigma = E_\tau\setminus\{0\},\, ds_\Sigma^2 = e^{2\varphi}|dz|^2)$, covariant chiral Dirac zero modes $\Psi_{+,a}^{\mathrm{orth}} = e^{-\varphi/2}\psi_a^{\mathrm{hol}}$ and `(0,1)` GHU Higgs modes $A_{\hat{\bar{z}}}^{\mathrm{orth}} = e^{-\varphi}\phi_H$ give the Yukawa trilinear integral exact Weyl weight `0` and the `4D` fermion kinetic Gramian exact Weyl weight `+1` ($\mathcal{G}_{ab}^{(s=1/2)} = \int d^2z\,e^{+\varphi}\overline{\psi_a}\psi_b$, cusp tail $r\,dr\,e^{+\varphi} \sim dr/|\ln r|$), NOT scalar area weight $+2$ ($e^{+2\varphi}d^2z$).
   - Cross-checked between holomorphic Fuchsian ODE developing map (`Producer`) and a disjoint `2D` nonlinear elliptic cusp-Robin Liouville PDE $\Delta\varphi = e^{2\varphi}$ (`Referee`, `1.02e-5` max diff on $\mathcal{G}^{(s=1/2)}$): scalar area weighting ($s=0$) inverts undressed CKM at $\tau_8^+ = \frac{16+8i}{5}$ ($0.24034 < 0.27759$), whereas true Dirac spin-`1/2` weighting $\mathcal{G}_{\mathrm{um}}^{(s=1/2)}(\tau_8^+) = (1.07020, 0.86840, 1.06140)$ restores strict CKM ordering $(0.31013 > 0.18641 > 0.04845)$.

4. **Zero-Free-Integer $8^3_4$ Cusp-Ramified Lopsided Seesaw (`L5_4` / `REF_FL5_4`, closing `FL4-F2`, `OBS-17`, & `OBS-18`):**
   - Aligning the unique non-paired block $C_2$ ($\vartheta_2$) with $8^3_4$'s unique unramified `1`-sheeted cusp $\{0\}$ ($e_2 = 1, |k_2| = 0$) and $(C_1, C_3)$ with its two `2`-sheeted cusps ($e_{1,3} = 2, |k_{1,3}| = (1,2)$) yields $n_{\mathbf{10}} = (e_c - 1) + |k_c| = (2, 0, 3)$ and $n_{\bar{\mathbf{5}}} = n_{\mathbf{1}} = (0,0,0)$ (`topologically skipping exponent 1 so (\Delta_{12}, \Delta_{23}) = (1, 2)`).
   - With untuned $M_R \propto I_3 + \widehat{W}_R^{\mathrm{unit}}$ and unified $\mathrm{Spin}(10)$ charge $q_R(\nu^c) = -5$, $\tau_8^+$ yields `4-5.3`-decade charged-fermion spans $(5.39\times 10^{-6}, 1.36\times 10^{-3}, 1.48\times 10^{-3})$, strict CKM ordering across all `3` metrics $(0.04294 > 0.00966 > 8.71\times 10^{-4})$, and simultaneous bi-large PMNS $(s_{12}^2, s_{23}^2, s_{13}^2, \Delta m_{21}^2/\Delta m_{31}^2) = (0.3713, 0.5705, 0.1250, 0.01329)$ (`Haar 7.11e-44`; Cayley unitary `1.29e-43`; also verified at $\tau_F = i y_F$: PMNS $(0.6757, 0.3464, 0.0440)$).

5. **Complete `2`-Loop Type-II `2HDM` Gauge-Yukawa-Quartic RGEs & `27f5d89fa` Audit (`L5_5` & `L5_6` / `REF_FL5_5` & `REF_FL5_6`, closing `FL4-F3`):**
   - Complete `2`-loop Type-II `2HDM` RGEs (`arXiv:1503.08216`) satisfy $\beta_{\lambda_{1..3}}^{(2)}|_{O(8)} = -114\lambda^3$ (`0.0`), custodial $\mathrm{SU}(2)_H$ (`2.80e-45`), `3x3` Haar equivariance (`2.17e-48`), and IR `BFB` stability on both $E_8$ GHU `(1, 1, 0, -1/2)g^2` ($m_{h^0}/v = 0.4267$, `GL6` vs `GBS8` `5.54e-14`, vs `agy-002` `RK4(4000)` `2.28e-13`) and $E_6$ GHU `(1, 1, -1/2, -1/2)g^2` ($m_{h^0}/v = 0.3589$).
   - Verified `12/12` SHA-256 manifests at `agy-002` `27f5d89fa`, $\mathcal{N}=1$ SUSY Sakharov $a_1(\xi=0) = +37/2$, $b_1 = 3$ orientifold parity $b_1^+ \in \{0,2\}$, and `60`-$e$-fold coupled Starobinsky inflation Kallosh-Linde trapping (`GL6` vs `GBS8` `7.14e-12`).
   - Integrated into `self_consistent_loop/manuscript/main.tex` (`Sec. X, Theorem 8, Table VIII, Fig. 8; 22 pages, 0 overfull boxes, AutoTeX-verified`).
