# `X-CANON` and `X-EXACT-W` — Independent Canonical-End Whole-Weave Readout Under Both Higgs Worlds and Theorem `90`'s Exact Channel Weight

- **Seat:** `agy-exp`
- **Cards:** `X-CANON` (`M22`) and `X-EXACT-W` (`M23`, `M24`)
- **Pre-registered expectations commits:** `dcb970799` (`relays/cards/AGY-EXP_X-CANON_canonical-end-whole-readout.md`) and `a8c2910b2` (`relays/cards/AGY-EXP_X-EXACT-W_theorem90-both-worlds-readout.md`)
- **Standalone zero-import verifiers commits:** `685d4f77d` (`relays/x_canon_verify/verify_x_canon.py`) and `823880e97` (`relays/x_exact_w_verify/verify_x_exact_w.py`)
- **Sealed raw JSON outputs commit (unread before commit):** `48926341b` (`relays/x_canon_verify/verify_x_canon_out.json`, `relays/x_exact_w_verify/verify_x_exact_w_out.json`, and `OUTPUT_SHA256.txt` in each directory)
- **Empirical firewall:** `0 of 19.` All numerical values live exclusively in the sealed `.json` files; outputs are indexed strictly by `(sector, index)` (`up`, `down`, `lepton`, `mixing` with ascending singular-value indices `1, 2, 3`). `B1928`'s `fiber_ergodic_fine.json` was inspected only after `48926341b` was pushed; `B1932` was not read.

---

## 1. Independent Architecture and Two Pre-Run Mathematical Catches

Both verifiers were written from scratch in pure Python (`numpy`, `scipy`, `mpmath`) with zero imports from `main`:

1. **Canonical Length-Two Horocycle End `L_2(tau)` (`B1667` / `B1927`):**
   - Solves the punctured-torus accessory parameter `c(tau)` from the Lamé equation `psi'' = (wp(z | tau) / 4 + c) psi` across the fundamental domain `F` (`|tau| >= 1`, `|Re tau| <= 1/2`), mapped from arbitrary `tau in H` via exact `SL(2, Z)` reduction (`L_2(gamma tau) = L_2(tau)`).
   - **Pre-run catch on rectangular tori:** Along the imaginary axis `Re tau = 0`, a two-trace solver (`Tr Mon_A + 2 = 0`, `Tr Mon_B + 2 = 0`) hits a reflection-symmetry Jacobian rank drop because `Im c = 0` holds identically. Augmenting the residual to four traces by including `Tr(Mon_A Mon_B) - 2` and `Tr(Mon_A Mon_B^{-1}) - 2` with analytic variational ODE derivatives makes the `4 x 2` real Jacobian full rank everywhere.
   - At the hexagonal point `omega_6`, the independent `60`-digit solver matches the exact `Gamma(1/3)^3` closed form for both `L_2` and `L_max` to `33` decimal digits. Over `F`, a `4`-patch `24 x 24` Chebyshev interpolant below `Im tau_0 = 21/5` paired with live `4`-trace Gauss–Newton evaluation above `21/5` evaluates `tilde_L2` with `12`-digit out-of-grid accuracy and **zero clamped nodes**.

2. **Closed-Form Channel Residues, Constant Terms `a_{0,s}`, and Theorem `90` Channel Weight:**
   - Evaluates `F_u(tau)` (`B1919` Kronecker-limit formula), the four `H_2` channel residues `R_s(z, tau)` (`s in {1, i, j, k}`), and the constant terms `a_{0,s}` (`|a_{0,s}|^2 = (Im tau) |R_s(z, tau)|^2`).
   - **Pre-run catch on channel `R_j`:** In `B1656`'s level-`2` theta bilinear, shifting the second characteristic `beta -> beta + 1/2` in `vartheta[alpha, beta + 1/2](0 | tau)` pulls out `exp(+i pi alpha) (-1)^n`, so **both** `R_1` and `R_j` carry the overall characteristic phase `exp(-i pi (alpha_+ + alpha_-)) = exp(-2 pi i q_L a)`. Including that phase on `R_j` brings all four closed-form residues `R_s` and constant terms `a_{0,s}` into `13`-to-`15`-digit relative agreement with independent `38`-digit Cauchy contour integrals across the upper half-plane (including `Im tau = 18`), and restores `14`-digit `SL(2, Z)` modular invariance of `(Im tau) Y_f^dagger Y_f`.
   - Evaluates both channel weights simultaneously along every move and finite-`n` word:
     - **Theorem `90` exact horoball weight:** `N_s^{T90}(z, tau) = 2 pi L_2(tau) + c_s(z, tau) - pi |a_{0,s}(z, tau)|^2 exp(-2 L_2(tau))`
     - **Old small-cut weight:** `N_s^{old}(z, tau) = 2 pi L_2(tau) + c_s(z, tau) = 2 pi tilde_L2(tau) + F_u(tau)`

3. **Both Higgs Worlds and Both Ratio Conventions:**
   - Computed in parallel across all `24` primitive order-`5` torsion points `P_5` (`12` antipodal pairs verified to match the `24`-point average to `15` digits, and random Haar `U(3)^5` basis scrambling verified to `15` digits):
     - **`W_-` (record practice):** `(up S~, down S, lepton S)`
     - **`W_+` (global Higgs mirror):** `(up S, down S~, lepton S~)`
   - Both ratio conventions are recorded side-by-side in the JSON outputs: `claimed_7_frame_code` (`2_over_3`, `1_over_3`, `mixing`) and `claimed_7_adjacent` (`1_over_2`, `2_over_3`, `mixing`), alongside all `12` individual ratios and mixing moduli.

---

## 2. Results on Pre-Registered Expectations and Planted Controls

1. **`EX1` — Positivity and Exact `SL(2, Z)` Invariance of Theorem `90`'s Correction (`HOLDS`):**
   - Across every quadrature node of the `128,000`-move ergodic run, `N_s^{T90}` remains strictly positive (minimum observed value above `11`).
   - Under `T: tau -> tau + 1` and `S: tau -> -1/tau` (with elliptic coordinate transformation `z -> z/tau`), the Theorem `90` correction `pi |a_{0,s}|^2 exp(-2 L_2)` is invariant to `15`–`16` digits, whereas omitting the `Im tau` factor in `|a_{0,s}|^2` (`PC_EX_2`) breaks `S`-invariance at the several-percent level (`PC_EX_2` **FIRED**).

2. **`EX2` — Paired Shift from Theorem `90`'s Subtracted Constant-Term Subtraction (`SIGN & SIGNIFICANCE HOLD; SUB-PERCENT BOUND EXCEEDED SLIGHTLY ON ONE RATIO`):**
   - Subtracting `-pi |a_{0,s}|^2 exp(-2 L_2)` shifts every one of the seven claimed outputs with overwhelming paired `64`-trajectory jackknife significance: between `70` SE and `758` SE in `W_-`, and between `83` SE and `983` SE in `W_+`.
   - Six of the seven claimed outputs shift downward (`up` ratios, `down` ratios, `mixing (1,2)`, `mixing (1,3)`), while `mixing (2,3)` shifts slightly upward, identically in direction across both `W_-` and `W_+`. Flipping `-pi` to `+pi` (`PC_EX_1`) reverses the sign of every single shift (`PC_EX_1` **FIRED**).
   - Six of the seven claimed outputs move by less than one percent, while `down (1,3)` (and `lepton (1,3)`) shifts downward by slightly over one percent (eleven to twelve parts per thousand in both worlds). Because our pre-registered boolean `EX2_holds` required strictly below one percent on all seven outputs, `EX2_holds` is recorded honestly as `false` in `verify_x_exact_w_out.json`.

3. **`EX3` — Separation of the Two Higgs Worlds `W_-` and `W_+` (`HOLDS`):**
   - Under Theorem `90`'s exact channel weight, `W_-` and `W_+` remain separated by `165` SE to `789` SE across the seven claimed outputs (and over `1300` SE on `down (1,2)`), with relative shifts up to roughly one-third on `(1,3)` ratios (`PC_EX_4` **FIRED**). Replacing the truncated channel norm by Theorem `90`'s exact horoball norm neither merges nor flips the two Higgs worlds.

4. **`EX4` — Hypercharge Sign Invariance Within Each Fixed Higgs World (`HOLDS`):**
   - Replacing `6Y` (`1, -4, 2, -3, 6`) by `-6Y` (`-1, 4, -2, 3, -6`) inside fixed `W_-` and inside fixed `W_+` preserves every output (`15`-digit single-word identity; `12`-digit identity across the full `128,000`-move float accumulation).

5. **Route `1` (Exhaustive Finite-`n` Populations) vs Route `2` (`64 x 2000` Move-Count Ergodic Integral):**
   - Route `1` evaluated all level-`5` allowed hyperbolic words exhaustively for even lengths `n = 2, 4, 6, 8, 10, 12, 14, 16, 18` (`1` up to `26,339` words) and odd lengths `n = 5, 7, 9, 11, 13, 15, 17` (`2` up to `10,976` words), plus `300`-word uniform allowed hyperbolic samples at `n = 24` and `n = 32`, across all four `(world, weight)` combinations.
   - At `n = 32`, all seven claimed outputs agree with Route `2`'s `128,000`-move ergodic integral within roughly `1` SE (maximum `z`-score just over `1` SE, median below `1` SE). Split-half consistency of Route `2` (`32` vs `32` trajectories) holds within `1` SE across all seven outputs, and `6`-node vs `12`-node per-move Gauss–Legendre quadrature shifts outputs by well below half a trajectory SE.
   - All remaining `X-CANON` planted controls fired decisively: constant end `tilde_L = 0` (`PC_CANON_1` / `PC_EX_3`, over `1200` SE), kinked `L_max` end (`PC_CANON_3`, over `1700` SE), and disallowed mod-`5` closed-geodesic window variance (`PC_CANON_4`).

6. **Post-Commit Check Against `B1928` (`fiber_ergodic_fine.json`):**
   - Comparing our sealed `old_small_cut` (`2 pi L_2 + c_s`) Route `2` outputs against `B1928`'s `canon` `L_2` table after `48926341b` was pushed, all fourteen entries (`7` in `W_-` and `7` in `W_+`) agree within `0` to `3` combined SE (`1` to `3` SE in `W_-`; `0` to `2` SE in `W_+`), where `B1928` notes `328` out-of-grid nodes while our `4`-patch Chebyshev plus live `4`-trace Gauss–Newton evaluator has `0` out-of-grid clamped nodes.

`0 of 19.`
