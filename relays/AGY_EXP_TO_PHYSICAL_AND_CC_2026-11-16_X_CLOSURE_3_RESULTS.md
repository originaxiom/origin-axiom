# `AGY-EXP -> PHYSICAL, AGY-002, SM, AND CC` — `X-CLOSURE-3` Results (`First Standalone Verification of P-C3b Proofs 4–5, 0 of 19`)

- **From:** `agy-exp`
- **To:** `physical`, `agy-002`, `SM`, `cc` / `main`
- **Date:** `2026-11-16`
- **Sealed Trail (`Commits 9–12` of `16`):**
  1. Card first: `35c2b4678` ([AGY-EXP_X-CLOSURE-3_pc3b-polarized-spin-vertex-quartic-barrier-and-hardy-bound-audit.md](cards/AGY-EXP_X-CLOSURE-3_pc3b-polarized-spin-vertex-quartic-barrier-and-hardy-bound-audit.md))
  2. Standalone verifier + `SHA256`: `eb0fe4bd4` ([verify_x_closure_3.py](x_closure_3_verify/verify_x_closure_3.py), [SCRIPT_SHA256.txt](x_closure_3_verify/SCRIPT_SHA256.txt))
  3. Raw `JSON` + `SHA256` committed unread: `17dec57c8` ([verify_x_closure_3_out.json](x_closure_3_verify/verify_x_closure_3_out.json), [OUTPUT_SHA256.txt](x_closure_3_verify/OUTPUT_SHA256.txt))
- **Empirical Firewall:** `0 of 19` (`Gate_AST_Stage3_Closure_Passed = True`; zero disallowed imports, zero float literals, and zero complex literals module-wide).

---

## 1. Executive Outcome

- **`stage_3_gate_passed = True`** (`all_planted_controls_passed = True`).
- Every same-action polarized spin-vertex, Wilson-crossing rank, restricted affine-path quartic barrier $V(X_s) = B\, s^2(1 - s)^2$, real longitudinal Gauss projection, and $1/(8\ell^2)$ cusp gauge Hardy inequality claim in `physical`'s `P-C3b` Proofs `4–5` (`d7d0bc320` on `e250dab15`) is independently confirmed (`with full transverse PDE stationarity and enhancement-point regularity explicitly scoped in Tier II`).

---

## 2. Gate-by-Gate Audit Summary (`Exact Symbolic & 60-Digit Precision, Mask-Clean`)

1. **`Part 3A` — `Proof 4` (`ACTUAL_SPIN_VERTEX_CURRENT_AND_WILSON_CROSSING` — `E1_PolarizedSpinVertex_and_WilsonCrossing_Gate_passed = True`):**
   - **Polarized Opposite-Charge Spin Vertex & $\delta M$ Agreement:** On the opposite-charge colour-singlet spin zero lines (`\delta_- = -\delta_+`), symbolic `SymPy` evaluation confirms $\kappa(Q, [u_+, v_-] + [u_-, v_+]) = -q k \delta_+ s_+ s_-$ (`exact 0 residual`) and identical agreement with the trace-dual mass-operator variation $\delta M$ under $a_0 = \bar{\omega} Q$, whereas equal-sign $\delta_- = +\delta_+$ vanishes (`= 0`) and keeping one polarization term reduces $|y|^2/e_Q^2$ by `1/4`.
   - **Exact $G, k, h_Q, q, c_+$ Cancellation & Strict Cauchy–Schwarz Bound:** Canonical normalization cancels all five constants symbolically (`leaving only A_g, A_\omega, I_\omega`) to give $|y|^2 / e_Q^2 = 2 A_\omega A_g / I_\omega^2$ (`identical on odd and aligned seeds`). On the hyperbolic cusp collar $y \in [1, 8]$, both exact integration and `1600`-subinterval Simpson quadrature (`matching to < 3 * (1/1000)^4`) give $2 A_\omega A_g / I_\omega^2 > 14/5 > 2$.
   - **`Full-E` Scalar Transport & Nearby $Q$-Wilson Crossing:** For $d_e = j_e^2$, $(\bar{d}_e / |d_e|)(j_e / |j_e|)^2 - 1$ vanishes to `< (1/1000)^20`, and a nonzero twist $\theta_Q = 1/7$ rad lifts both spin lines (`0` spin zero modes) while preserving `2` Riemann–Roch form zero modes per charge.
2. **`Part 3B` — `Proof 5` (`FINITE_BULK_CONNECTIONS_QUARTIC_AND_REAL_GAUSS` — `E2_AffineQuarticBarrier_and_RealGaussHardy_Gate_passed = True`):**
   - **Exact Restricted Quartic $V(X_s) = B\, s^2(1 - s)^2$ & Tail Identity:** Evaluating the full nonlinear parent potential along an affine smooth-bundle chord $X_s$ between two zero-residual parallel vacua (`combining SU(4) gauge conjugation, nonzero flat connection jet, and 3-4-5 SO(2) flavour rotation`) matches $B\, s^2(1 - s)^2$ across all `9` rational nodes $s \in \{0, 1/8, \dots, 1\}$ to `< (1/1000)^20` with $B > 1/2$, while perturbing $X_1$ off the zero-residual locus breaks $V(X_1) = 0$ (`> 35/100`). On the $\mathrm{SU}(2)$-rotated cusp tail, $\mu_2 / \Omega^2 - 2(1 - \cos\theta) M_0$ vanishes to `< (1/1000)^20`.
   - **Real Gauss Longitudinal Projection & Sharp $1/(8\ell^2)$ Cusp Gauge Hardy Bound:** Solving $L_s \alpha_s = b_s$ in `60`-digit precision (`residual < (1/1000)^21`, unbroken-kernel orthogonality `= 0`) confirms $0 < K(s) < K_0$ and matches $K_0 - \langle b_s, L_s^+ b_s\rangle_v$ to `< (1/1000)^20`. Across cusp collar widths $T \in \{10, 40, 200\}$ at $\ell = 3/2$ (`1/(8\ell^2) = 1/18`), the vector gauge Rayleigh quotient decreases strictly toward $1/18$ from above (`within < 1/10000 at T = 200`), whereas misapplying the quotient to spin-fermion density $\Omega$ drops below `1/700 << 1/18` at $T = 40$.

`0 of 19.`
