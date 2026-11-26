# REFEREE VERDICT — `AGY-002_A2-P629-VEFF-MODULUS` (`2026-11-26`, Strictly `0 of 19`)

**`VERDICT: FAIL`** *(Producer `v3` fails certification on two concrete mathematical/Guardrail-4 bugs in `P3` — `BUG-1` UV D-term quartic convention mismatch causing `t = 0` vacuum instability, and `BUG-2` two-loop Type-II 2HDM hypercharge transcription error masked by a self-copied benchmark — while ALL core `P1` and `P2` modular-potential theorems, `P3` curved Dirac `G_{s=1/2}`, `P3` `Static` qualitative/quantitative spectra outside `l1, l2`, `10`-trial Haar invariance, and `P4` `6/6` planted controls are independently confirmed. Remediation requires a clean Producer `v4`.)*

---

## 1. Cold-Room Custody, Commit SHAs & Manifest Audit

- **Seat / Branch:** `agy-002`, `agy-002/verify`, strictly **`0 of 19`** (zero empirical PDG/NuFIT/Planck/DESI/CODATA inputs).
- **Cold-Room Protocol:** Zero producer files (`v1/v2/v3` or any other `verify_a2_*`) were read, listed, grepped, or imported prior to sealing `referee_a2_p629_veff_modulus.py` (`SCRIPT_SHA256.txt`), committing pre-execution, executing once via `python3 -I`, verifying `0` JSON floats, and committing unread output JSON + `OUTPUT_SHA256.txt`.
- **Static & Output Hygiene (Referee):** `0` AST float/complex literals, `0` float/complex names/casts, `0` forbidden imports (`numpy/scipy/frontier/sage/gap`), `py_compile` clean, `0` JSON floats in both Referee output and cross-diff JSON.

| Artifact | Git Commit SHA | SHA256 |
|---|---|---|
| Producer `v3` script (`verify_a2_p629_veff_modulus_v3.py`) | `1b9f9d0e7` | `94d76a8782f3ace499e6776380c7eb06e0f84cac14d5db658b63f6487875ae89` |
| Producer `v3` output (`verify_a2_p629_veff_modulus_v3_out.json`) | `c4c3177f3` | `47bd2abf22b46a85506c65c36956bfbc9b2ed6c834d766f3b3118109b2151367` |
| Referee script (`referee_a2_p629_veff_modulus.py`, pre-exec) | `6f165e0a0` | `e1736025590a11ae323c8282fed217bf0e30e9cd8dd9477222db8755a674b106` |
| Referee output (`referee_a2_p629_veff_modulus_out.json`, unread) | `fbe13c8bf` | `90d33213735e6fb020053029112b514bccff33a31e5d93b45fc055a3fe9db72d` |
| Cross-diff script (`compare_referee_vs_producer_v3.py`) | *(this commit)* | `3996e39707c4354163417ba63a0a24bbf54bb284c6ebc92d7b49028da7b33b28` |
| Cross-diff JSON (`referee_vs_producer_v3_diff.json`) | *(this commit)* | `0311a4fce154bd4e94490fd84cafec92f9d4658263b453e4e0f54b16ec935f29` |

- **Manifest Verification:** **`373 / 373` `*SHA256*.txt` manifests across `relays/` OK (`0` failures)** (including newly sealed `CROSS_DIFF_SHA256.txt`; `372/372` pre-existing).
- **Branch Isolation:** **`0` non-relay edits** (`git diff --name-only origin/main...HEAD | grep -v '^relays/'` = `0` files).

---

## 2. Disjoint Referee Algorithms (Guardrail 6)

| Module | Disjoint Numerical Algorithm (Pure stdlib + `mpmath` + `sympy`) |
|---|---|
| `RP1` $\eta, E_2$ | Euler pentagonal number theorem $\eta(\tau) = e^{i\pi\tau/12}\sum (-1)^k q^{k(3k-1)/2}$; $E_2 = 1 + 24 q P'/P$ (exact log-derivative, no divisor-sum loop) |
| `RP1` $E(\tau, s)$ | Chowla–Selberg expansion cross-checked against direct square-box lattice sum ($N = 40$) & exact `Fraction(-15, 16)` proof |
| `RP2` $\wp(z)/4$ | Exact Jacobi $\theta_1$ logarithmic derivative $-\partial_z^2 \ln\theta_1(\pi z, \tau) - \frac{\pi^2}{3} E_2(\tau)$ (no Lambert series) |
| `RP2` Fuchsian $L_2$ | Hybrid explicit 6th-order Yoshida Solution A (derived from exact BCH polynomial equations) + implicit 5-stage `GL10` / 6-stage `GL12` symplectic polish (`det = 1` exact) + graded-ray Frobenius extraction |
| `RP2`/`RP3` Linalg | Real-split $6\times 6$ symmetric `mp.eigsy` for Hermitian $H = Y^\dagger Y$ AND complex-symmetric Autonne–Takagi $\begin{pmatrix}A & B \\ B & -A\end{pmatrix}$ |
| `RP3` Curved $G_{s=1/2}$ | Corner-split Clenshaw–Curtis polar quadrature + Forest–Ruth symplectic radial ray propagation + exact analytic inner cusp disk |
| `RP3` RGE & `V4` | Implicit 2-stage 4th-order Gauss–Legendre (`GL4`) with cubic Hermite EWSB crossings (not RK4); multi-start Riemannian Armijo descent on $S^5 \times S^5$ |
| `RP3` Haar `G3` | 10-trial Cayley-transform $U = (I - i A)(I + i A)^{-1}$ over $U(3)^5 \times U(3)_{\nu_R}$ (not Box–Muller QR) |

---

## 3. Critical & Moderate Audit Findings (`discrepancies_count = 91 / 439`)

Automated cross-diff (`compare_referee_vs_producer_v3.py`) compared **`439`** shared quantitative & boolean observables across `P1`–`P4`: **`348` matched**, **`91` discrepancies**, **`0` unexplained**. Every single discrepancy maps cleanly to 3 root causes, plus 1 code-level Guardrail 4 literature bug:

1. **`BUG-1` (CRITICAL — `18` discrepancies: `l1, l2` across all `9` vacuum $\times$ branch runs; UV instability at `t = 0`):**
   - In `verify_a2_p629_veff_modulus_v3.py`, lines `1306`–`1309` (`dl1, dl2, dl3, dl4`) and lines `1941`–`1942` (`l3 + l4 + sqrt(l1*l2) > 0`) use the **Branco / Chowdhury–Eberhardt** potential $V = \frac{1}{2}\tilde\lambda_1|\Phi_1|^4 + \frac{1}{2}\tilde\lambda_2|\Phi_2|^4 + \lambda_3|\Phi_1|^2|\Phi_2|^2 + \lambda_4|\Phi_1^\dagger\Phi_2|^2$.
   - However, lines `1851`–`1854` initialize `l1_D = l2_D = (g2^2 + (3/5)g1^2)/8 = 0.05` (the **no-`1/2`** convention) instead of `/4 = 0.10`, while keeping `l3_D = +0.025`, `l4_D = -0.125`.
   - **Consequence:** At `t = 0`, `v3`'s own stability criterion evaluates to `l3_D + l4_D + sqrt(l1_D * l2_D) = 0.025 - 0.125 + 0.05 = -0.05 < 0` (**unbounded below at the UV scale**), masked only because `v3` checks stability solely at `t = -35` after `dl1, dl2` grow by `~2x`. In the Referee's consistent convention ($\tilde\lambda_{1,2} = 2\lambda_{1,2}$ inside $\beta$ and `l3 + l4 + 2*sqrt(l1*l2) >= 0`), `t = 0` exactly saturates the MSSM D-flat direction (`0.025 - 0.125 + 2*0.05 = 0`) and remains strictly positive for all `t in (-35, 0)`.

2. **`BUG-2` (CRITICAL — Code-Level Guardrail 4 Literature Transcription Error in 2-Loop Type-II 2HDM $\beta_{Y_u}^{(2)}, \beta_{Y_d}^{(2)}$):**
   - Verified directly against the primary published arXiv TeX sources of **Chowdhury & Eberhardt (`arXiv:1503.08216`, Appendix A)** and **Luo–Wang–Xiao (`hep-ph/0211440`, Eq. 35)**:
     - Coefficient of $g_1^2 H_d$ in $\beta_{Y_u}^{(2)}$ is $-\frac{41}{144}\cdot\frac{3}{5} = \mathbf{-\frac{41}{240}}$ (NOT `v3` line `1269`: `-29/240`, off by `+1/20`).
     - Coefficient of $g_1^2 H_u$ in $\beta_{Y_d}^{(2)}$ is $-\frac{53}{144}\cdot\frac{3}{5} = \mathbf{-\frac{53}{240}}$ (NOT `v3` line `1284`: `-65/240`, off by `-1/20`).
   - Crucially, `v3` copied its own typo `-29/240` into its Guardrail 4 benchmark formula `b2_yt_ex` at line `1790`, rendering its `< 10^{-40}` Chowdhury–Eberhardt benchmark a self-consistent tautology. (While its numerical IR effect at 2-loop is small, `~10^{-5}`, it is a clear Guardrail 4 failure.)

3. **`CONV-3` (MODERATE — `73` discrepancies on `DynamicV4_ferro_CURVED_s12` only: `37` UV/IR + `36` PMNS):**
   - **Order of $G_{s=1/2}$ vs $V_4$ minimization (`37` diffs):** `v3` lines `1884`–`1892` minimize $V_4(h_u, h_d)$ in the **flat** basis before applying $G_{s=1/2}$, whereas the Referee applies $G_{s=1/2}^{-1/2} Y G_{s=1/2}^{-1/2}$ first so the 1-loop Coleman–Weinberg quartic is evaluated on canonical kinetic Yukawas. At $\omega_+$ ($G = I_3$) both match to `5+` digits; at `FILQ1_star` and `tot_star_70` ($G \neq I_3$) the UV/IR Higgs alignment differs (e.g. `tot_star_70` IR `V12 = 0.1355` vs `0.3086`, `V23 = 0.0565` vs `0.2792`, `V13 = 0.0159` vs `0.0361`, though both yield `std_ckm = True` and radiative EWSB).
   - **Piece 3 $Y_\nu$ Higgs vector (`36` diffs):** `v3` lines `1904`–`1905` keep static $S(\tau)$ for $Y_\nu$ on the `DynamicV4` branch, whereas the Referee couples $Y_\nu$ to the dynamic up-type vector $h_u^*$. On `Static_FLAT` and `Static_CURVED_s12`, ALL 3 vacua $\times$ 3 `M_R` PMNS entries match `v3` to `< 1.6e-4`!

4. **Transparent Referee Self-Gate Note (`RG2 = False`, `5/6` Referee gates passed):**
   - Referee gates `RG1, RG3, RG4, RG5, RG6` all passed (`True`). `RG2` flagged `False` solely because Referee's `GL12` Fuchsian solver at `Im(-1/tau_mod) = 0.799` reached `T_rel_err = 2.64e-24` and `S_rel_err = 6.89e-19` vs the strict `< 1e-25` threshold (`18.2` digits of `SL(2,Z)` invariance confirmed; `P2_A = True`, `P2_B = True`, and all `P2` observables matched `v3` to `7`–`12` digits).

---

## 4. Full Side-by-Side Comparison Tables (`P1`–`P4`)

### 4.1 Modules `P1`, `P2` (`P2-A`, `P2-B`, `P2-C`), and `P4` (`0` Discrepancies on `52/52` Shared Observables)

| Category | Observable | Referee (Disjoint) | Producer `v3` | Rel. Diff | Status |
|---|---|---:|---:|---:|---|
| `P1` | `FILQ n=1` `y_star`, `V_star` | `1.23457994670`, `-8.92881487086` | `1.23457994670`, `-8.92881487086` | `< 1e-11` | MATCH |
| `P1` | `FILQ n=2` `y_star`, `V_star` | `1.18338966039`, `-26.4595897531` | `1.18338966039`, `-26.4595897531` | `< 1e-11` | MATCH |
| `P1` | `FILQ n=3` `y_star`, `V_star` | `1.15543901831`, `-78.3405090283` | `1.15543901831`, `-78.3405090283` | `< 1e-11` | MATCH |
| `P1` | Half-period sum (`s = 3`) | `-15/16` (`lat err 1.4e-7`) | `-15/16` (`lat err 1.4e-7`) | `exact` | MATCH |
| `P1` | Kronecker first limit max err | `< 1e-22` (3 pts) | `3.31e-18` (3 pts) | `< 1e-16` | MATCH |
| `P2` | `VCW_tr(i)`, `VCW_tr(omega)`, `VCW_tr(arc)` | `4.53508959234`, `4.60938688241`, `4.71400641191` | `4.53508959234`, `4.60938688241`, `4.71400641191` | `< 1e-11` | MATCH |
| `P2-B` | `c_B^crit (E_3)` | `0.0318659172106` | `0.03186591721` | `1.8e-11` | MATCH |
| `P2-B` | `VCW1 + 100 E_3` at `4i` | `-158731585.367` | `-158731585.4` | `2.1e-10` | MATCH |
| `P2-C` | `y_star` (`c_F = 70`, `x = 1/2`) | `3.38045110573` | `3.380451106` | `7.9e-11` | MATCH |
| `P2-C` | `V_star` (`c_F = 70`, `x = 1/2`) | `-7043393.75844` | `-7043393.76198` | `5.0e-10` | MATCH |
| `P2-C` | `V(0, y_star)` (`c_F = 70`) | `-7043366.25441` | `-7043366.25917` | `6.8e-10` | MATCH |
| `P2-C` | `V_xx(1/2, y_star)` (`h_x = 1/50`) | `+542.1938116` | `+542.0459565` | `2.7e-4` | MATCH |
| `P2-C` | `V_xx(0, y_star)` (saddle) | `-542.1936737` | `-541.8150515` | `7.0e-4` | MATCH |
| `P2-C` | `V_yy(1/2, y_star)` | `+501742225.51` | `+501742224.3` | `2.4e-9` | MATCH |
| `P2-C` | `V_tot(tau_FILQ3*; 70)` | `+28.3124306273` | `+28.31243063` | `9.4e-11` | MATCH |
| `P2-C` | `V_tot(1/2 + 4i; 70)` | `+4437698613.71` | `+4437698612.36` | `3.0e-10` | MATCH |
| `P2-C` | `V_tot(1/2 + 4i; 100)`, `V_tot(1/2 + 5i; 100)` | `-3.24640086e8`, `+3.022537522e13` | `-3.24640088e8`, `+3.022537521e13` | `< 6e-9` | MATCH |
| `P4` | Planted controls `PF1`–`PF6` | `6 / 6` triggered (`PF2 = -1.111210823e10`) | `6 / 6` triggered (`PF2 = -1.111210823e10`) | `< 1e-9` | MATCH |

### 4.2 Module `P3` — Curved Spin-`1/2` Dirac `G_{s=1/2}`, `Static`, & `DynamicV4` Across All 3 Vacua

| Vacuum | Metric `G_{s=1/2}` (`[QJ, QI, QK]`) — Referee vs `v3` | GB Err (Ref / `v3`) | Max `G` Rel. Diff |
|---|---|---:|---:|
| `omega_+` | `[0.99999999, 0.99999999, 1.00000001]` vs `[1.00000003, 0.99999994, 1.00000002]` | `1.14e-5` / `5.33e-7` | `5.1e-8` |
| `FILQ1_star` | `[1.01724200, 0.93244048, 1.05031752]` vs `[1.01724018, 0.93244899, 1.05031082]` | `1.37e-5` / `1.24e-6` | `9.1e-6` |
| `tot_star_70` | `[1.17538746, 0.64922587, 1.17538667]` vs `[1.17539381, 0.64921235, 1.17539384]` | `5.63e-5` / `1.24e-6` | `2.1e-5` |

| Vacuum / Branch | `yt/g3` (Ref / `v3`) | `mHu2_IR` (Ref / `v3`) | `l1_IR` (Ref / `v3`) | `V12, V23, V13` IR (Ref / `v3`) | `Hu1st` / `std_ckm` | Status |
|---|---|---|---|---|---|---|
| `omega` / `Static_FLAT` | `0.89422` / `0.89421` | `-0.60751` / `-0.60749` | `0.2409` / `0.4812` | `0.1866, 0.7027, 0.0609` / identical | `F/F` (exact) | `BUG-1` (`l1,l2`) |
| `omega` / `Static_CURVED` | `0.89422` / `0.89421` | `-0.60751` / `-0.60749` | `0.2409` / `0.4812` | `0.1866, 0.7027, 0.0609` / identical | `F/F` (exact) | `BUG-1` (`l1,l2`) |
| `omega` / `DynamicV4` | `1.01561` / `1.01561` | `-0.21762` / `-0.21760` | `0.2911` / `0.5814` | `0.6891, 0.1516, 0.0774` / identical | `F/T` (exact) | `BUG-1`+`CONV-3` |
| `FILQ1*` / `Static_FLAT` | `0.93944` / `0.93944` | `-0.60255` / `-0.60253` | `0.2141` / `0.4275` | `0.2647, 0.6498, 0.0972` / identical | `F/F` (exact) | `BUG-1` (`l1,l2`) |
| `FILQ1*` / `Static_CURVED` | `0.93259` / `0.93259` | `-0.60660` / `-0.60657` | `0.2127` / `0.4246` | `0.2738, 0.6540, 0.1041` / identical | `F/F` (exact) | `BUG-1` (`l1,l2`) |
| `FILQ1*` / `DynamicV4` | `1.02350` / `1.02685` | `-0.22447` / `-0.22782` | `0.2918` / `0.5850` | `0.654, 0.223, 0.159` / `0.692, 0.241, 0.205` | `F/T` (exact) | `BUG-1`+`CONV-3` |
| `tot*(70)` / `Static_FLAT` | `1.02944` / `1.02943` | `-0.25582` / `-0.25579` | `0.2362` / `0.4701` | `0.1219, 0.1715, 0.0241` / identical | `T/F` (exact) | `BUG-1` (`l1,l2`) |
| `tot*(70)` / `Static_CURVED` | `1.01686` / `1.01684` | `-0.22042` / `-0.22039` | `0.2738` / `0.5466` | `0.1112, 0.1650, 0.0209` / identical | `F/F` (exact) | `BUG-1` (`l1,l2`) |
| `tot*(70)` / `DynamicV4` | `1.01858` / `1.02457` | `-0.21508` / `-0.23227` | `0.2876` / `0.5787` | `0.1355, 0.0565, 0.0159` / `0.3086, 0.2792, 0.0361` | `F/T` (exact) | `BUG-1`+`CONV-3` |

- **`Static_FLAT` & `Static_CURVED_s12` Summary (all 3 vacua, outside `l1, l2`):** `max UV diff = 1.81e-5`, `max IR diff = 1.41e-3`, `max Piece 3 PMNS diff = 1.53e-4` across all 3 `M_R` (`I_3, sym(1w), sym(2w)`).
- **Guardrail 3 (10-trial Cayley-Haar $U(3)^5 \times U(3)_{\nu_R}$):** Referee `max_observable_drift = 9.88e-35` (`max_unitarity_err = 1.25e-39`); `v3` `9.58e-40` — BOTH strictly `< 1e-25`.
- **Guardrail 4 Benchmarks:** Referee CE `y_t, y_b, y_tau` err `< 5.5e-48` (against exact `arXiv:1503.08216` `-41/240, -53/240`), Martin 7-eq err `3.28e-47`, Xing–Zhou opposite sign `True`, `|S_IR| < 1e-33`.

---

## 5. Exact Remediation Required for Producer `v4`

1. **Fix `BUG-1` (Quartic D-term convention):** Either initialize `l1_D = l2_D = (g2^2 + (3/5)g1^2)/4` at `v3` lines `1851`–`1852` (consistent with Branco/CE `dl1..dl4` and `l3 + l4 + sqrt(l1*l2) >= 0`), OR rescale `l1_ce = 2*l1, l2_ce = 2*l2` in `rhs_coupled_2hdm_soft` and check `l3 + l4 + 2*sqrt(l1*l2) >= 0` at **every** step including `t = 0`.
2. **Fix `BUG-2` (Guardrail 4 CE 2-loop hypercharge coefficients):** Replace `-mp_rat(29, 240)` with `-mp_rat(41, 240)` at lines `1269` & `1790`, and `-mp_rat(65, 240)` with `-mp_rat(53, 240)` at line `1284`, and benchmark all three (`y_t, y_b, y_tau`) directly against `arXiv:1503.08216` Appendix A.
3. **Clarify `CONV-3` (`DynamicV4_ferro_CURVED_s12`):** State explicitly (and ideally adopt the canonical-kinetic basis ordering) whether $V_4(h_u, h_d)$ is minimized after applying $G_{s=1/2}$ and whether Piece 3 $Y_\nu$ couples to $h_u^*$ on the `DynamicV4` branch.

0 of 19.
