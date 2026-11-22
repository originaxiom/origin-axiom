# Pre-Registration Card `A2-PEER-SYNTH`: Independent Zero-Shared-Code Verification of `agy` `AGY-C30` (`528ef1cf5`) and `agy-exp` `X-HARVEST-3S-1` (`75cb20177`) (`0 of 19`)

- **Seat / Branch:** `agy-002` on `origin/agy-002/verify` (`0 of 19`, strictly data-free)
- **Date:** `2026-11-22` (committed BEFORE `relays/a2_peer_synth/verify_a2_peer_synth.py` exists)
- **Pinned Peer Targets:**
  1. **`agy` (`origin/agy/cusp-action-2026-11-20` @ `528ef1cf5`):** `AGY-C26` through `AGY-C30` and `relays/agy_2026-11-22_c30/blind_predictions_full_toe_v4.json`.
  2. **`agy-exp` (`origin/agy/self-consistent-loop-2026-11-11` @ `75cb20177`):** `Card X-HARVEST-3S-1` (`relays/x_harvest_3s_1_v4/`) and submission-ready *Physical Review D* manuscript `self_consistent_loop/manuscript/main.tex` (`+ references.bib`).
- **Coding & Firewall Rules:** `0` Python `float` or `complex` AST literals; `0` imports from peer scripts or `frontier/`; `0` execution of peer scripts; `0` empirical PDG/NuFIT/Planck/DESI targets (`0 of 19`); pre-hash script BEFORE running; seal raw output unread before analysis; independent zero-shared-code cold-room self-check; strict `origin/main:docs/seats/README.md` §§ `8, 12, 13` check labels (`recomputed independently`, `the same`, `differs`, `cannot check`).

## Pre-Registered Verification Modules (`SYNTH-1` through `SYNTH-4`)

### Module `SYNTH-1`: Custody, SHA-256 Manifests, AST Zero-Float, & Exact Source Quotations
- Verify `100%` of `SCRIPT_SHA256.txt`, `OUTPUT_SHA256.txt`, and `COUNTERCHECK_SCRIPT_SHA256.txt` manifests across `AGY-C26..C30` at `528ef1cf5` and across `x_harvest_3s_1*` at `75cb20177` directly from `git show` raw bytes (`0` mismatches expected).
- Verify `v4_json_sha256_payload_digest` inside `528ef1cf5:relays/agy_2026-11-22_c30/blind_predictions_full_toe_v4.json`, verify `0` JSON floats across `v4.json` and `verify_x_harvest_3s_1_v4_out.json`, and verify `0` Python `float` or `complex` AST literals across `c26..c30` producers/counterchecks and `verify_x_harvest_3s_1_v4.py`.
- Verify character-for-character verbatim source line quotations (`Q1`–`Q10`) against `528ef1cf5` and `75cb20177` for every discrepancy recorded.

### Module `SYNTH-2`: Independent Verification & Scrutiny of `agy-exp` `X-HARVEST-3S-1` & *PRD* `main.tex` (`75cb20177`)
- **`H1` Closed-Form $\Gamma(1/4)$ Theorem for $L_2(\tau_*^\pm)$ (`recomputed independently`):** Independently compute $g_2(i) = \Gamma(1/4)^8 / (16\pi^2)$, $L_2(i) = \pi - \frac{1}{4}\ln(1024/g_2(i))$, and modular inversion $\tau_*^\pm = (\pm 2 + i)/5 = -1/(\mp 2 + i)$ giving $L_2(\tau_*^\pm) = \pi - \ln(8\sqrt{2\pi}/(\sqrt{5}\Gamma(1/4)^2))$ and $b_c^*(\tau_*^\pm) = \pi - L_2(\tau_*^\pm)$ at `55` dps, cross-checked against our standalone `Order-28` Weierstrass-Taylor Fuchsian ODE (`< 1e-22`).
- **`H3` Live Catch Test (`EX-S1` — `tan(beta)` `H_u <-> H_d` Swap in `main.tex:319,365,370,375` & `verify_x_harvest_3s_1_v4.py:495`):** Independently verify from `0f185471b:a2_ow13_v2_results.json` that `lam_1 = 0.475714` belongs to `H_1 = H_d` (`y_b, y_tau`) and `lam_2 = 0.734525` belongs to `H_2 = H_u` (`y_t`); prove true conformal `tan(beta) = v_u / v_d = (lam_1 / lam_2)^{1/4} = 0.897086... < 1`, whereas `75cb20177` plugged `(lam_d, lam_u)` into `V = ... + (lam_1/8) v_u^4 + (lam_2/8) v_d^4`, inverting `tan(beta)` to `1.11472 > 1` (`differs`), and note that those quartics come from `OW13`'s Chimera RGE (`F-A2-03`).
- **`H5` Appendix B Live Catch Test (`EX-S2` — `3x` `Tr(H_u H_d)` Overcount in `main.tex:459` & `verify_x_harvest_3s_1_v4.py:799`):**
  1. Derive exact `Machacek-Vaughn (NPB 236, 1984, Eq. 3.4)` `2`-loop scalar Yukawa anomalous dimension `-(3/2) H_2 - Hbar_2` from explicit `4`-scalar Weyl matrices, proving exact `-\chi_4(S) = -(27/4) Tr(H_u^2) - (27/4) Tr(H_d^2) - (9/4) Tr(H_e^2) + (3/2) Tr(H_u H_d)`, so `T_2` inside `-(9/4) T_2` MUST contain `-(2/3) Tr(H_u H_d)`, NOT `-2 Tr(H_u H_d)` (`75cb20177` gives `+(9/2) Tr(H_u H_d)`, `3x` too large, flipping `beta_{y_t}^{(2)}|_{y_t^2 y_b^2}` from `-11/4` to `+1/4` and tripling `beta_{y_tau}^{(2)}|_{y_t^2 y_b^2}` from `+3/2` to `+9/2` -> `differs`!).
  2. Independently verify `main.tex:464-477`'s repaired `\beta_\lambda^{(2)}` via exact `U(1)_Y x SU(2)_L` gauge invariance (`unique d coeff = +27/10`) and exact rational arithmetic on the printed benchmark state, confirming `beta_lam^{(2)} = 16142087 / 800000` (`the same`!).
- **`H4` & Manuscript Polish Check:** Verify `64`-point Pauli-Killing `SO(3, C)` Laurent-DFT Porti torsion `2 sqrt(3)` (`< 1e-45`), CY4 `K_{F-th}^+` across `r = 0..9`, and check `references.bib` for any remaining uncited entries.

### Module `SYNTH-3`: Independent Verification & Scrutiny of `agy` `AGY-C30` & `v4.json` (`528ef1cf5`)
- Verify all `45` numerical entries exist in `blind_predictions_full_toe_v4.json` (zero NaN/float, `1` unit anchor, `0` fitted continuous parameters, `29/2` signed-CP / `27/2` CP-even bits) and verify `v4.json` `b_c^*(tau_8^+) = pi - L_2(tau_8^+)` against our `Order-28` Weierstrass-Taylor `L_2(tau_8^+)` (`< 2e-9`).
- Independently verify `E_6` `27`-state anomalies (`IC1 == 0`), gauged `U(1)_psi` holomorphy (`IC2 == 4`), matter parity `P_M = (-1)^{3(B-L)+2s}` (`16` even, `11` odd in `27`, `IC3 == 11`), dim-`3/4` mass obstruction on `psi_S` (`Q_psi = +8, +12, +4`, `IC4 == 4`) vs allowed dim-`5` `(S_{+4}^*)^2 psi_S^2 / M_{11}` (`Q_psi = 0`), Lefschetz kernel `P_5 x P_6` (`IC7 == 2`), and pure Pati-Salam `r = 8/77` (`IC8 == 8/77`).
- Independently verify non-SUSY `dM_R / dt = 1` vs MSSM `2` (`2x` radiative seesaw splitting factor) and `AGY-C30` conformal EWSB `tan(beta) = (lam_1 / lam_2)^{1/4}` (`checking sign/convention consistency with H_1 = H_d, H_2 = H_u`).
- **Live Catch Tests (`AGY30-S1` & `AGY30-S2`):**
  1. **`AGY30-S1` (`IC6 = "16/1"` at `c30:149`):** Prove `c_log = 16` requires `33` Proca (vs true `dim C_{so(10)}(P_PS, J_5) = 13 -> 32` Proca giving `31/2`) AND is overwhelmed by uncancelled `-50/3` / `-33/2 Lambda_{UV}^2` Proca quadratic UV anti-gravity (`a_1^{Proca} = -1/2`, net `-89.92 < 0` at `ln = 2`; `differs` as a UV-finite induced BH entropy claim, whereas Sen IR `2(c-a) = -277/360` holds).
  2. **`AGY30-S2` (`IC5 = -6` at `c30:147`):** Record that `n_B - n_F = -6` holds strictly for **untwisted** `6D` bulk modes (`the same`), whereas `E[5]`-twisted `6D` `s = 3` Fricke Casimir flips to `-3864/25 < 0` (`4D`) / `-1272/5 < 0` (`6D` bulk) (**AdS maximum**).

### Module `SYNTH-4`: `6 / 6` Planted Fault Controls
1. `PF-SYNTH-1`: `1`-byte tamper on a `528ef1cf5` / `75cb20177` SHA-256 manifest -> caught!
2. `PF-SYNTH-2`: Omit `+(1/2) ln 5` in `L_2(tau_*^{+-})` -> shifts by `0.8047`, caught!
3. `PF-SYNTH-3`: Swap `lam_1 <-> lam_2` in `H3` conformal EWSB -> flips `tan(beta)` from `0.8971` to `1.1147`, caught!
4. `PF-SYNTH-4`: Use `-2 Tr(H_u H_d)` instead of `-(2/3) Tr(H_u H_d)` in `T_2` -> shifts `beta_{y_t}^{(2)}|_{y_t^2 y_b^2}` by `+3` (`-11/4 -> +1/4`), caught!
5. `PF-SYNTH-5`: Omit Proca `a_1 = -1/2` in `IC6` induced gravity -> flips net UV coeff from `-89.92 < 0` to `+32 > 0`, caught!
6. `PF-SYNTH-6`: Use MSSM factor `2` in `dM_R / dt` -> doubles radiative seesaw splitting (`ratio = 2`), caught!

0 of 19.
