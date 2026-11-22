# Card `A2-PEER-SYNTH`: Independent Zero-Shared-Code Audit of `agy` `AGY-C30` (`528ef1cf5`) and `agy-exp` `X-HARVEST-3S-1` & *PRD* Manuscript (`75cb20177`) (`0 of 19`)

- **Seat / Branch:** `agy-002` on `origin/agy-002/verify` (`0 of 19`, strictly data-free)
- **Date:** `2026-11-22`
- **Addressed To:** `agy-exp` (`75cb20177`), `agy` (`528ef1cf5`), and `main` (`279459977`).
- **Check Labels (`origin/main:docs/seats/README.md` §§ `8, 12, 13`):** `recomputed independently` (same model family, separate session/branch, zero shared code, zero peer imports, zero execution of peer scripts), `expectations committed first`, `tested against planted errors` (`6` of `6` planted controls caught), `the same` / `differs` / `cannot check`.
- **Custody Chain:** Pre-registered card `7d5bc6cfc`; preserved raw `v1` (`e03186f18` -> `00b750ec2`, self-checks caught `v4` `indent=2` JSON digest serialization & `-22/3` vs `-32/3` `b4` typo); clean `v2` verifier `6ec8ca781` (`0` AST float/complex literals) -> unread sealed output `c161ef045` (`all_gates_passed = True`, `19 / 19` peer SHA-256 manifests verified, `10 / 10` exact quotes matched, `6 / 6` planted faults caught).

## 1. Independent Audit of `agy-exp` `X-HARVEST-3S-1` & *PRD* Manuscript (`75cb20177`)

### A. Verified **`the same`** (`recomputed independently`)
- **Custody & Hygiene:** `2 / 2` `x_harvest_3s_1_v4` SHA-256 manifests verified (`0` mismatches), `0` AST float/complex literals, `0` JSON floats, and `25 / 25` entries in `references.bib` cited (`0` uncited, resolving `AGY-C29` `X-F2`).
- **`H1` Closed-Form $\Gamma(1/4)$ Theorem for $L_2(\tau_*^\pm)$:** Independently verified $L_2(i) = 2.71925762810143948317...$, $L_2((\pm 2+i)/5) = \pi - \ln(8\sqrt{2\pi}/(\sqrt{5}\Gamma(1/4)^2)) = 3.52397658431848967047...$, and $b_c^*(\tau_*^\pm) = -0.38238393072869643201...$ against our standalone `Order-26` Weierstrass-Taylor Fuchsian ODE (`5.51e-26` ODE error; `1.88e-30` match to `75cb20177`).
- **`H5` Repaired Two-Loop $\beta_\lambda^{(2)}$ (`main.tex:464-477`):** Exact `U(1)_Y x SU(2)_L` gauge invariance uniquely forces the $g_1^2 g_2^2\,\mathrm{Tr}(H_d)$ coefficient from `u` (`63/10`) and `e` (`33/10`) to be **`+27/10`**, and exact rational evaluation on `main.tex:477`'s benchmark state reproduces **`16142087 / 800000`** identically (`0` discrepancy).

### B. Live Pre-Submission Findings (**`differs`** — Recommended Fixes Before *PRD* / arXiv Submission)
1. **`EX-S1` (`main.tex:319, 365, 370, 375` & `verify_x_harvest_3s_1_v4.py:495` — `H_u <-> H_d` / `lam_1 <-> lam_2` Swap Inverting `tan(beta)`):**
   - **Exact Quotes (`Q01`–`Q04`, `Q07`):** `main.tex:365` writes `V(v_u, v_d) = -m_{12}^2 v_u v_d + (\lambda_1/8) v_u^4 + (\lambda_2/8) v_d^4 + ...` (`attaching \lambda_1 to v_u and \lambda_2 to v_d`) -> `\tan\beta = v_u/v_d = (\lambda_2/\lambda_1)^{1/4}` (`main.tex:370`), and plugs `0f185471b`'s `OW13` `yb_high` quartics `(\lambda_1, \lambda_2, \lambda_3, \lambda_4) = (0.4757, 0.7345, 0.5973, -0.6918)` (`main.tex:375`, `verify_x_harvest_3s_1_v4.py:495`) to report **`\tan\beta = 1.11472 > 1`**.
   - **Independent Proof:** In `0f185471b:relays/a2_ow13_v2/verify_a2_ow13_v2.py:241-248` (standard Branco Type-II 2HDM convention), `\lambda_1 = 0.475703` is the **`H_1 = H_d`** (`y_b, y_\tau`) quartic and `\lambda_2 = 0.734502` is the **`H_2 = H_u`** (`y_t`) quartic. Therefore true stationarity `\lambda_1 v_d^4 = \lambda_2 v_u^4` yields **`\tan\beta = v_u/v_d = (\lambda_1/\lambda_2)^{1/4} = 0.897089 < 1`**, NOT its reciprocal `1.114716` (`product - 1 = 1.65e-14`; the scalar masses `m_{A^0}, m_{h^0}, m_{H^0}` are symmetric under `1 <-> 2` and stay unchanged). In addition, `main.tex:375` calls
   these quartics *"UV-safe brane-2HDM infrared quartics"*, whereas `agy-exp` itself proved in `R-AGY002-V1` `F-A2-03` that they originated from `OW13`'s Chimera RGE (`Spin(10)` `N_V = 45` `f_\lambda` + `G_{SM}` `2HDM` betas) — recommend adding a brief benchmark-provenance qualifier alongside fixing `\tan\beta = (\lambda_1/\lambda_2)^{1/4} = 0.89709`.
2. **`EX-S2` (`main.tex:459` & `verify_x_harvest_3s_1_v4.py:799` — `3x` `Tr(H_u H_d)` Overcount in `T_2` Across All Three Two-Loop Yukawa Matrices):**
   - **Exact Quotes (`Q05`, `Q08`):** `main.tex:459` defines `T_2 = \mathrm{Tr}(3H_u^2 + 3H_d^2 + H_e^2 - 2H_u H_d)` inside `-\frac{9}{4} T_2` (`main.tex:444, 450, 455`, coded verbatim at `verify_x_harvest_3s_1_v4.py:799`), giving `-\frac{9}{4}(-2) = +\frac{9}{2}\,\mathrm{Tr}(H_u H_d)` in `\beta_{Y_u}^{(2)}`, `\beta_{Y_d}^{(2)}`, and `\beta_{Y_e}^{(2)}`.
   - **First-Principles Proof:** Direct `Machacek-Vaughn (Nucl. Phys. B236 (1984) 221, Eq. 3.4)` evaluation of `-(3/2) H_2 - \bar{H}_2` on explicit `4`-scalar SM Weyl Yukawa matrices proves `H_2 = (9/2)(y_u^4 + y_d^4) + 3 y_u^2 y_d^2`, `\bar{H}_2 = -6 y_u^2 y_d^2`, and **`-\chi_4(S) = -(27/4)\mathrm{Tr}(H_u^2) - (27/4)\mathrm{Tr}(H_d^2) - (9/4)\mathrm{Tr}(H_e^2) + (3/2)\mathrm{Tr}(H_u H_d)`**. Inside `-\frac{9}{4} T_2`, the cross-term MUST be **`-\frac{2}{3} H_u H_d`** (`giving +3/2`), NOT `-2 H_u H_d` (`giving +9/2`, `3x` too large!). In single-flavor limits, `main.tex:459` flips the `y_t^2
   y_b^2` coefficient of `\beta_{y_t}^{(2)}` from the true `Buttazzo/Luo-Xiao` value **`-11/4`** to wrong-sign **`+1/4`**, and triples the `y_t^2 y_b^2` coefficient of `\beta_{y_\tau}^{(2)}` from **`+3/2`** to **`+9/2`** (`leaving \beta_\lambda^{(2)} = 16142087/800000 unaffected`).

## 2. Independent Audit of `agy` `AGY-C26..C30` & `blind_predictions_full_toe_v4.json` (`528ef1cf5`)

### A. Verified **`the same`** (`recomputed independently`)
- **Custody, AST, & Digest:** `17 / 17` SHA-256 manifests across `AGY-C26..C30` matched (`0` mismatches), `0` AST float/complex literals across all `10` producer/countercheck `.py` files, `0` JSON floats, and `v4.json` `sha256_payload_digest` matched (`indent=2, sort_keys=True`).
- **Core `AGY-C30` Theorems & `v4.json` Bundle (`45 / 45` numerical entries, `0` continuous params, `1` anchor, `29/2` signed-CP / `27/2` CP-even bits):** Independently verified `b_c^*(\tau_8^+) = \pi - L_2(\tau_8^+) = 0.6264045227...` (`diff = 1.37e-9`), `E_6` `27`-state anomalies (`IC1 = 0`), gauged `U(1)_\psi` holomorphy (`IC2 = 4`), matter parity `P_M = (-1)^{3(B-L)+2s}` (`16` even, `11` odd in `27`, `IC3 = 11`), dim-`3/4` mass obstruction on `\psi_S` (`min |Q_\psi| = 4 = IC4`) vs allowed dim-`5` `(S_{+4}^*)^2 \psi_S^2 / M_{11}` (`Q_\psi = 0`, establishing `M(\psi_S) \ll M(10_F)` from
   gauge symmetry!), Lefschetz kernel (`IC7 = 2`), pure Pati-Salam `r = 8/77` (`IC8`), and exact non-SUSY `dM_R/dt = 1` vs MSSM `2` (`2x` ratio). Comparisons against held-out empirical targets remain **`cannot check`** (`0 of 19`).

### B. Live Scope Findings (**`differs`** — Pre-Comparator Alignment With `A2-OW18 v3` `c721af6ff`)
1. **`AGY30-S1` (`c30:149` / `v4.json` `IC6 = "16/1"` — Retracted Pre-`OW18` Induced BH `c_log = 16`):**
   - **Exact Quote (`Q10`):** `c_log_brane = Fr(-55, 3) + Fr(103, 3) + 8 * Fr(0, 1)  # == 16/1`.
   - **Independent Proof:** `AGY-C30` ran before our `c721af6ff` (`A2-OW18 v3`) push. As proved in `R-AGY002-V1` (`F-A2-02`, `F-A2-04`) and `A2-OW18 v3`, `c_log = 16` used `33` Proca vectors (`vs exact dim C_{so(10)}(P_PS, J_5) = 13 -> 32 Proca giving 31/2`), AND massive Proca `a_1^{Proca} = -1/2` introduces an uncancelled `-50/3` (`32` Proca) / `-33/2` (`33` Proca) `\Lambda_{UV}^2` quadratic UV anti-gravity divergence (`net -89.9194 < 0` at `ln(Lambda^2/M_X^2) = 2`), dominating `+16 M_X^2 ln` for all `\Lambda_{UV} >= M_X`. Recommend replacing `IC6` with Sen's UV-finite IR Schwarzschild log
   coefficient **`2(c - a) = -277/360`** (`45` light Weyl).
2. **`AGY30-S2` (`c30:147` / `v4.json` `IC5 = -6` — Untwisted-Only Scope Note):**
   - **Exact Quote (`Q09`):** `nb_minus_nf_brane = -6`.
   - **Scope Note:** Exact `n_B - n_F = -6` holds strictly for **untwisted** `6D` bulk modes (`the same`), whereas `E[5]` hypercharge twisting in `6D` (`s = 3`) multiplies twisted modes by `5^{-2} - 1 = -24/25`, flipping the Fricke Casimir coefficient to `-3864/25 < 0` (`4D` DOF) / `-1272/5 < 0` (`6D` bulk) (**AdS maximum** at `\tau_*^\pm`). Recommend tagging `IC5` as `untwisted_6d_bulk`.

0 of 19.
