# Erratum 1 to Card A2-OW19: Frozen v1 Self-Check Catches and Clean v2 Remediation

- **Frozen v1 Commits:** `0d2246ff6` (`verify_a2_ow19.py` + `SCRIPT_SHA256.txt`) and `b9101c210` (`a2_ow19_results.json` + `OUTPUT_SHA256.txt`), preserved untouched.
- **Three Self-Check Catches in `v1` (`all_gates_passed = False`):**
  1. **`OW19-A` (Guardrail 3 conjugate scrambling bug):** `v1` transformed `MR00 -> u_nr @ MR00 @ u_nr.T` instead of the gauge-covariant conjugate law `MR00 -> u_nr.conj() @ MR00 @ u_nr.conj().T` paired with `Ynu -> u_l @ Ynu @ u_nr.conj().T`, giving `haar_10trial_max_drift = 1.688e-5`. Fixed in `v2` (`MR00 -> u_nr.conj() @ MR00 @ u_nr.conj().T`).
  2. **`OW19-B1` (SymPy log-substitution pattern mismatch):** `v1` used `.subs(sp.log(m0_sq / lam**2), -L_sym)` which failed to match `SymPy`'s normalized logarithm representation (`cw_symbolic_identity_zero = False`). Fixed in `v2` by direct algebraic substitution `lam = sp.sqrt(m0_sq) * sp.exp(L_sym / 2)`.
  3. **`OW19-C` (`O(h^2)` finite-difference truncation at `h = 10^{-8}`):** `v1` evaluated `grad F_3(tau_*^+)` with 2nd-order finite differences at `h = 10^{-8}`, leaving `O(f''' h^2) = 2.99e-13 > 10^{-22}`. Fixed in `v2` by evaluating the exact analytic derivatives `(dE_3/dx, dE_3/dy)` and analytic Hessian `(d^2 E_3/dx^2, d^2 E_3/dy^2, d^2 E_3/dx dy)` of the Chowla-Selberg expansion at `35` decimal digits.
- **Zero changes** to any mathematical theorem, expectation, pre-registered gate, or `0 of 19` firewall constraint.
