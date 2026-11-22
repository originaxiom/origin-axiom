# Pre-Registration Card `AGY-002_A2-PEER-AGY`: Independent Cross-Seat Verification, Guardrail Scrutiny, and Insight Harvest of Peer `agy` (`0e4506d59`)

- **Seat / Branch:** `agy-002` on `agy-002/verify`
- **Target Read (strictly read-only):** `origin/agy/cusp-action-2026-11-20` at `0e4506d59`
  (`149` commits since merge-base `60a52d359`: `AGY-C1` through `AGY-C25` + `blind_predictions_full_toe_v2.json`)
- **Date:** `2026-11-22`
- **Protocol:** `docs/seats/README.md` Sections `8`, `9`, `12`, `13` plus Guardrails `1`–`6`
- **Empirical Inputs:** `0 of 19` (zero PDG, NuFIT, Planck, DESI, or lattice numbers imported or
  compared; any check requiring empirical comparison is recorded as `cannot check`)

## 1. Pre-Registered Verification Tasks & Failure Conditions

### Task `PEER-AGY-1`: Custody, AST, Firewall, & Exact Machine-Quote Audit (`@0e4506d59`)

- Recount from git (`60a52d359..0e4506d59`): commit count (`149`), non-relay edits (`0`),
  `SCRIPT_SHA256.txt` raw-byte matches (`25 / 25`), chronological custody chains (`25 / 25`),
  zero producer imports across all `25 / 25` counterchecks, `0` `frontier/` imports, `0` MD lines
  `> 680` chars, `0` section-12 authority headings, `0` vendor/empirical leaks, and exact canonical
  SHA-256 verification of `blind_predictions_full_toe_v2.json` (`d918700ed6cfc262...`).
- Machine-verify every exact quotation cited in findings `F1`–`F6` directly against commit
  `0e4506d59` (`docs/seats/README.md` Section 13).
- **Failure condition:** Any unverified quote or custody mismatch not reported transparently.

### Task `PEER-AGY-2`: Zero-Shared-Code Re-Derivation of Load-Bearing Pure Math (`AGY-C1`–`AGY-C24`)

Build all computations strictly from scratch (`0` Python `float`/`complex` AST literals, `0` imports
from `agy`'s scripts or `frontier/`, `mp.mp.dps = 55`) and grade each item `the same`, `differs`,
or `cannot check`:

1. **`AGY-C16` (`15 x 15` & `30 x 30` Collar Algebra & Gauge Charges):**
   - Exhaustive `125`-triple `(Z/5Z)^3` pure-Higgs obstruction (`0 / 125`), exact `SymPy` block
     Schur complement `eps^4 Y (Y^H Y)^2 / (tr(Y^H Y))^2`, exact `SU(2)_L x U(1)_Y` gauge
     invariance of all `10` Weyl blocks of the `30 x 30` neutral collar (`doublets {0,3,4,7,8}`,
     `singlets {1,2,5,6,9}`), and symbolic Weinberg reduction `m_eff(nu_L) = (M_0 / (M_KK^2 - M_0^2))
     v_u^2 Y_nu Y_nu^T`.
2. **`AGY-C17` (`6D` `tr R^4` No-Factorization, `Vol(X_{4_1}^{(m)})`, & `D`-Term Quartics):**
   - Verify `SO(6)` Cartan pair `(1, 2, 0)` vs `(sqrt(2), sqrt(3), 0)` (`tr R^2 = -10`, `tr R^4 =
     34 != 26`), `50`-digit `Vol(X_{4_1}^{(m)}) = (3 sqrt(3)/2) m L(chi_{-3}, 2)` at `m in {1, 8, 40}`,
     and exact tree-level `SU(2)_L x U(1)_Y` `D`-term quartics `(2/5, 2/5, 1/10, -1/2) g_0^2`.
3. **`AGY-C19` (`E_8` Unimodularity, `so(12, 4)` Killing Form, & Mayer–Selberg `s = 2`):**
   - Exact ADE Cartan determinants (`det E_8 = 1`, `E_7 = 2`, `E_6 = 3`, `D_r = 4`, `A_r = r + 1`),
     compact `so(10)` Killing eigenvalues inside `so(12, 4)` (`45` negative-definite, zero gauge
     ghosts), and `50`-digit Gauss telescoping `(L_1 f_1)(x) == f_1(x)` for `f_1(x) = 1 / (1 + x)`.
4. **`AGY-C20` (Ray–Singer / Quillen `V_{Gamma_0(5)}` & `CP`-Mirror Symmetry):**
   - Independent `55`-dps Chowla–Selberg / Dedekind-eta `V_{Gamma_0(5)}(tau)` on `E_tau + E_{5 tau}`,
     `grad V((2+i)/5) == 0` (`< 10^{-45}`), `Delta_{H^2} V == +pi`, `det Hess > 0`, and exact
     `V((2+i)/5) == V((-2+i)/5)`.
5. **`AGY-C21` (`Z_8 x Z_5` `k_{min} = 40` & `Q_A = 3/25 < 1/8 = Q_B`):**
   - Exact rational `1/8 - 1/5 = -3/40` (`gcd(3, 40) = 1` -> `k_min = 40`), `Q_A = 3/25 < 1/8 = Q_B`,
     and `exp(-(S_B - S_A)) = exp(-2 pi / 5) == |q((2+i)/5)|` (`< 10^{-48}`).
6. **`AGY-C22` (`[2I : 2T] = 5` McKay `E_8^hat -> E_6^hat`, `M_{11} / M_{GUT}`, & Unitarity):**
   - Exact algebraic-integer quaternion construction of `2T` (`24` elements) inside `2I` (`120`
     elements), `[2I : 2T] = 5`, `M_{11} / M_{GUT} = 3.93863908... > 39 / 10`, self-dual & isotropic
     `M_{Pl} / v_{EW}` benchmarks, and `|a_2| < 1 / 1000` up to `M_{11}`.
7. **`AGY-C23` (`Spin(10)` Matter Parity `P_M`, `7D` Warped `G_{rr}` No-Go, & `eta_V` Steepness):**
   - Exact `P_M = (-1)^{3(B-L) + 2s}` across all `27` Weyl states of `E_6` (`16_F -> +1`,
     `psi_S in 1_F -> -1`, AND `10_F -> -1`, explicitly flagging the `M(psi_S) < M(10_F)` mass-order
     requirement for `1_F * 10_F * 10_H`!).
   - Independent `SymPy` `7D` Christoffel / Einstein tensor computation of `G_{rr}` verifying zero
     `A''` terms (`B980` vacuum-energy no-go).
   - Independent `55`-dps Fricke hilltop `eta_V(i / sqrt(5))` at `n_K = 1` and `n_K = 3` (`|eta_V| > 1`).
8. **`AGY-C24` (Internal JSON Identities):**
   - Verify `1 - (M_W / M_Z)^2 == electroweak_mix_ratio` and `alpha_2 * sin^2(theta_W) == qed_coupling_ir`.

### Task `PEER-AGY-3`: Quantitative Counter-Computations of Guardrail Findings (`F1`–`F6`)

1. **`F1` (`Guardrail 2` Hardcoded `strong_cp_phase = mp.mpf(0)` & Polar-Phase Erasure):**
   - Independently compute exact `arg det(Y_u Y_d)` on `C16`'s raw `p3 = (1/5, 2/5)` and `p4 =
     (1/6, 1/6)` Yukawas at `m = 8, tau = (16 + 8i) / 5` BEFORE `C16:53`'s Hermitian square-root
     projection `sqrt(gj)`, checking whether raw `arg det(Y_u Y_d)` is non-zero (`differs` from
     hardcoded `"0.0"` in `C18:168` / `blind_predictions_full_toe_v2.json`).
2. **`F2` (`C7` `LinearNDInterpolator` `L_2` Precision Floor & Missing `SL_2(Z)` `-ln|z|` Term):**
   - Quantify the exact difference between `C7`'s `LinearNDInterpolator` over `B1927/grid.json` +
     `B1667` at `(1/5, 8/5)` and our `19`-digit `Order-24` exact `L_2 = 2.5151881308899968867`
     (checking whether the interpolation error exceeds `C18`/`C24`'s claimed `< 10^{-7}` `R6` budget),
     and verify the missing `-ln|z|` `S`-inversion offset `+(1/2) ln(5) ~ 0.8047` at `tau_*^+ = (2+i)/5`.
3. **`F3` (`C18` vs `C24` `tan beta` Internal Discrepancy Inside `blind_predictions_full_toe_v2.json`):**
   - Verify exact difference between `C18`'s large-`tan beta` approximation (`10.78694292...` in
     `sm_msbar_at_ew_horizon`) and `C23`/`C24`'s exact Newton minimization (`10.78186085...` in
     `sm_1loop_pole_and_2hdm_bosons`): `|Delta tan beta| ~ 5.08e-3` (`rel ~ 4.7e-4 >> 2.2e-8` `R6`).
4. **`F4` (`Guardrail 4` Three Hybrid-SUSY-in-Non-SUSY-`2HDM` RGE / Matching Leaks):**
   - Independently compare non-SUSY `2HDM` `dM_R/dt` (`factor 1`, Antusch et al. `hep-ph/0501272`)
     against `C23:81`'s MSSM `factor 2` to quantify the shift in `(M_2 - M_1)/M_1`; check `C18:117`
     `dmh2` zero-crossing scale `t_0` vs `t_EW = -48 pi / 5` and omission of non-SUSY `2HDM`
     quartic/gauge homogeneous terms; document `C24:114` MSSM stop-top `delta_22` with `m_{A^0}` and
     `C18:103-106` omitted electroweak/quartic `2`-loop Yukawa terms.
5. **`F5` (`Guardrail 1 & 5` Unpriced Postulates in `C24`'s `11/2`-Bit / `FITTED == 0` Ledger):**
   - Machine-verify exact quotes for `m12_sq = 1/40`, `k_min = 40 -> alpha_GUT = 1/40`, `M_{KK,f}^2 ~
     tr(Y_f^H Y_f)`, `t_EW = -48 pi / 5` / `m_0` scale identification, `Q_1 = 1/25` (`T^4/(Z_5 x Z_5)`
     vs `SU(5)` `T^4` `1/5`), unstabilized `V_hat_perp`, and single-point `p3, p4` selection.
6. **`F6` (`Guardrail 2` Tautological Placeholder Certificate Strings in `C24:325-326`):**
   - Machine-verify `r_rows` and `ic_rows` placeholder comprehension in `C24:325-326`.

### Task `PEER-AGY-4` (`5 / 5` Planted Negative Controls `PF-PA-1..5`)

1. `PF-PA-1`: `1`-char tamper on `blind_predictions_full_toe_v2.json` -> SHA-256 check MUST fail.
2. `PF-PA-2`: Flip `psi_S` `P_M` from `-1` to `+1` -> matter-parity check MUST fail.
3. `PF-PA-3`: Omit `m = 40` factor in `Vol(X_{4_1}^{(40)})` -> `M_{11}/M_{GUT}` lock MUST fail.
4. `PF-PA-4`: Set `S`-inversion offset to `0` at `(2+i)/5` -> `L_2(-1/tau) - L_2(tau) = ln|tau|` check
   MUST fail.
5. `PF-PA-5`: Pass a non-existent quote to the section-13 quote verifier -> quote verifier MUST fail.

## 2. Coding & Firewall Rules

- Strictly `0` Python `float` or `complex` AST literals (`mp.mp.dps = 55`, exact `Fraction` / `SymPy`).
- Zero imports from `agy`'s scripts or `frontier/`; pre-hash script BEFORE running.
- Every line of every card and relay strictly `<= 680` characters; neutral section-12 check labels.

0 of 19.
