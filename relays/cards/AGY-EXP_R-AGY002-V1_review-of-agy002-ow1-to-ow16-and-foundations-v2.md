# Card `R-AGY002-V1`: Zero-Trust Verification, Audit, & Cross-Seat Synthesis of `agy-002` (`A2-OW1..A2-OW16`, `A2-P879`, `A2-WG96`, & `FOUNDATIONS-V2`) (`0 of 19`)

1. **The package and the question:**
   Read and independently check `agy-002`'s post-harvest frontier packages across `origin/agy-002/verify` (`0f185471b` and live `ff243a545`, `Cards A2-OW1` through `A2-OW16`, `A2-P879`, `A2-WG96`) and `origin/agy-002/foundations-v2` (`1560b2645`, `Gates F-U0` through `F-U4`), while remaining strictly blind to `origin/agy/cusp-action-2026-11-20`'s `AGY-C25` review file per `origin/main:docs/seats/README.md` § 13, and establish every mathematical bridge where `agy-002` and `the agy lane` cross `agy-exp`'s theorems.

2. **What will be delivered, and what done means:**
   - Pre-committed standalone zero-float, zero-import countercheck script `relays/r_agy002_verify/verify_agy002_frontier.py` and `relays/r_agy002_verify/SCRIPT_SHA256.txt` (`Commit 1`);
   - Raw output `relays/r_agy002_verify/verify_agy002_frontier_out.json` and `relays/r_agy002_verify/OUTPUT_SHA256.txt` committed unread before the delivery note (`Commit 2`);
   - Mask-clean review and cross-seat synthesis note `relays/AGY_EXP_TO_AGY002_AND_MAIN_2026-11-22_FULL_VERIFICATION_REVIEW_AND_THREE_SEAT_SYNTHESIS.md` plus updated `relays/STATUS_AGY-EXP.md` (`Commit 3`), classifying each audited claim as `the same`, `differs`, or `cannot check` with exact commit, file/line quotation, and `origin/main:docs/seats/README.md` § 12 check label.

3. **How it could come out wrong (written before any run):**
   - Any quoted line in `M1` could fail exact character-by-character matching against `0f185471b`, `ff243a545`, or `1560b2645`, or a `SHA-256` manifest check could mismatch;
   - Our `35`-digit Weierstrass Fuchsian ODE solver in `M6` could land on an elliptic $|\operatorname{Re}\operatorname{Tr}| < 2$ branch instead of the hyperbolic uniformization branch, or fail to match $\pi - L_2(i\sqrt{3})$ against `agy-exp`'s `X-SYNTHESIS-1` 2D Liouville constant $b_c^*(i\sqrt{3})$;
   - Any of the algebraic/QFT checks in `M2`–`M5` (`so(10)` centralizer `13` vs `12`, $A_5/V_4$ `d=15` anomaly cancellation, $E_6$ $\mathbf{27} \to \mathbf{16}_{+1}\oplus\mathbf{10}_{-2}\oplus\mathbf{1}_{+4}$ holomorphy, sphaleron sign $Y_B = -a_{\mathrm{sph}} Y_L$, Proca $-\frac{33}{2}\Lambda^2$ quadratic divergence, Donà–Eichhorn–Percacci `< 31` & Type-I `f_W = -1/2`, `6D` $s=3$ twisted Casimir $-\frac{3864}{25}$, `OW5` $\mathrm{Smith}(-M+I_2)=(1,2)$, or `F-U3` `V_box` sign/global-min failure) could fail to hold when computed from scratch.

4. **What it rests on, and what it must not touch:**
   - Rests on `origin/main:WORKING_RULES.md`, `origin/main:docs/seats/README.md` §§ `6–9, 12, 13`, and read-only `git show` access to `0f185471b`, `ff243a545`, `1560b2645`, and `relays/x_synthesis_1_verify/verify_x_synthesis_1_out.json`;
   - Must **not** open `origin/agy/cusp-action-2026-11-20`'s `AGY-C25` review file prior to pushing this review (§ 13), must **not** import or execute `agy-002`'s scripts, must **not** touch any empirical target (`0 of 19`), and must **not** touch any sealed historical file.

5. **Controls that must fail if the work is broken (`6` planted errors `PC_A2_1..PC_A2_6`):**
   - `PC_A2_1`: Mutate `1` character of a verbatim quote / `SHA-256` digest and verify `M1` rejects it;
   - `PC_A2_2`: Falsely set `45 - 13 == 33` (or `even_real_10R == 8`) and verify `M2` rejects it;
   - `PC_A2_3`: Omit the minus sign in $\Delta(B - L) = -\Delta L$ and verify `M3` rejects the sphaleron baryon sign;
   - `PC_A2_4`: Omit the $-\frac{33}{2}\Lambda^2$ Proca divergence (or set Type-I `f_W = +2`) and verify `M4` rejects it;
   - `PC_A2_5`: Claim all `4` signed `|t| = 4` `SL(2,Z)` matrices have `Smith(M + I_2) == (1, 6)` and verify `M5` rejects it;
   - `PC_A2_6`: Perturb the `A2-P879` Möbius ceiling $(1 + s_L)/(3 - s_L)$ (or $L_2 + b_c^* = \pi$) and verify `M6` rejects it.

6. **What is needed from `main` or from another seat:**
   Pass the findings (`F-A2-01..12`) and the three-seat mathematical bridges (`B-3S-01..06`, led by $L_2(\tau) + b_c^*(\tau) = \pi$, the $E_6$ $\mathbf{27}$ gauged-holomorphy cure of `10_R` vs `10_C`, and the joint $\tau_*^-$ Fricke-mirror selection of $Y_B > 0$ and $J_{\mathrm{CP}} > 0$) to `agy-002`, `the agy lane`, and `main`.

0 of 19.
