# BLIND COLD-ROOM ZERO-TRUST REFEREE VERDICT — Card `A2-WEIL-CHIRAL-LATTICE-BRIDGE`

- **VERDICT:** **`PASS`**
- **Card ID:** `A2-WEIL-CHIRAL-LATTICE-BRIDGE`
- **Seat Code:** `fam3-v1-high-03`
- **Blindness:** strictly `0 of 19` (pure mathematics; zero empirical data)
- **Branch:** `agy-002/verify` (base commit `873836a0c`)
- **Cross-Diff Summary:** **`322 / 322` matched checks (`0` discrepancies)** across `GLOBAL` (`7`), `W1` (`147`), `W2` (`50`), `W3` (`75`), and `W4` (`43`)
- **All Referee Gates Passed:** `true` (`W1=true`, `W2=true`, `W3=true`, `W4=true`, `RPF=5/5`, `ast_floats=0`, `json_floats=0`, `T7b Part 1=clean`)
- **Manifest Integrity:** `9 / 9` sealed files verified (`OK`) across both Producer and Referee SHA-256 manifests (`0` edits outside `relays/`)

---

## 1. Blind Cold-Room Protocol & Provenance Audit

1. **Phase 1 (Blind Script Sealing — Prior to Execution & Prior to Reading Producer Artifacts):**
   - Read only the Scope Card (`relays/cards/AGY-002_A2-WEIL-CHIRAL-LATTICE-BRIDGE_all-odd-n-chiral-index-leg5-intertwiner-l15-stabilization-and-genus-duality.md`). Zero Producer scripts, JSON outputs, or stdout logs were opened prior to Phase 2 sealing.
   - Initial blind commit `a2e0ca679` ran with all four mathematical modules (`W1..W4`) and hygiene passing to `< 1e-46`, while planted fault control `RPF2` detected `4/5` because its `v1`-character BFS included only `(L->3, R->3)` (which alone coincides with the valid order-2 character `rho^3`) without `(C->2, Sig->3)`. Before committing any outputs and still strictly blind to all Producer artifacts, `RPF2` was corrected to include all four generators `((pL,3), (pR,3), (pC,2), (pSig,3))`, re-audited statically (`0` AST float literals, `0` warnings, `T7b Part 1` clean), re-sealed, and committed as Phase 1 v2 (`9011a5f26`).
2. **Phase 2 (Unread Execution & Sealing):**
   - Executed `python3 -I relays/a2_weil_chiral_lattice_bridge_referee/referee_a2_weil_chiral_lattice_bridge.py` once (`EXIT_CODE=0`, runtime `141.94s`), sealed `OUTPUT_SHA256.txt`, and committed unread outputs (`905883933`) prior to opening Producer JSON.
3. **Phase 3 (Post-Seal Cross-Diff & Verdict):**
   - Executed `compare_referee_vs_producer.py` (`0` AST float literals, `0` JSON float literals) against the sealed Producer and Referee JSONs, achieving `322 / 322` matches with `0` discrepancies, sealed `CROSS_DIFF_SHA256.txt`, and verified all SHA-256 manifests in both directories.

### Cryptographic Seal Table (16-hex prefixes)

| Artifact | Manifest | SHA-256 Prefix (16 hex) | Status |
| :--- | :--- | :--- | :---: |
| `referee_a2_weil_chiral_lattice_bridge.py` | Referee `SCRIPT_SHA256.txt` | `720de274d74b9099` | `OK` |
| `referee_a2_weil_chiral_lattice_bridge_out.json` | Referee `OUTPUT_SHA256.txt` | `4547948835979f46` | `OK` |
| `referee_a2_weil_chiral_lattice_bridge_stdout.txt` | Referee `OUTPUT_SHA256.txt` | `cf1a8609f3edee5d` | `OK` |
| `compare_referee_vs_producer.py` | Referee `CROSS_DIFF_SHA256.txt` | `e573e008d25ca330` | `OK` |
| `referee_vs_producer_diff.json` | Referee `CROSS_DIFF_SHA256.txt` | `823b94d05c5819cf` | `OK` |
| `a2_weil_chiral_lattice_bridge_decisive.py` | Producer `SCRIPT_SHA256.txt` | `8f04ea23e2b0a7e5` | `OK` |
| `a2_weil_chiral_lattice_bridge_control.py` | Producer `SCRIPT_SHA256.txt` | `2696317dc554f1b6` | `OK` |
| `a2_weil_chiral_lattice_bridge_out.json` | Producer `OUTPUT_SHA256.txt` | `e1624cf0ea4a1049` | `OK` |
| `a2_weil_chiral_lattice_bridge_stdout.txt` | Producer `OUTPUT_SHA256.txt` | `d3a8ef4748420938` | `OK` |

---

## 2. Module-by-Module Independent Disjoint Verification

### Module W1 (`147 / 147` cross-checks matched)
- **Disjoint methods:** (i) Exact algebraic arithmetic over cyclotomic quotient rings `Q[x] / (Phi_N(x))` via `sympy.Poly` for `(N, r) in {(3,1),(3,2),(5,1),(5,2),(7,1),(9,1),(15,1),(15,4)}` plus exact algebraic CRT `rho_{15,1} ~= rho_{3,2} (x) rho_{5,2}` and `rho_{15,4} ~= rho_{15,1}` (zero floating-point error); (ii) 50-digit `mpmath` Fourier-dual (momentum) Weil basis (`L_hat = F L F^H`, `Sinv_hat = F Sinv F^H`, verified unitarily equivalent to `1.34e-49`) across all `220` `(N, r)` pairs (`N in 3..49` odd) and all `17` odd `N in 3..35`.
- **Key referee residuals:** `max_tr_c3_err = 3.37e-49`, `max_flip_trace_err = 1.70e-49`, `max_full_spinor_err = 8.78e-50`, `max_c3_order3_err = 1.44e-49`, `parity_dim_mismatches = 0`, `mod4_mismatches = 0`, `max_mirror_c3_err = 6.90e-50`, `max_crt_err = 2.14e-50`.
- **Cross-diff:** Exact match on `pairs = 220`, iso-spectral list `[5, 13, 17, 25, 29]`, chirally split list `[3, 7, 9, 11, 15, 19, 21, 23, 27, 31, 33, 35]`, and all `17 x 6 = 102` chiral/parity dimensions (`dim_H1, dim_H2, dim_H1_even, dim_H2_even, dim_H1_odd, dim_H2_odd`).

### Module W2 (`50 / 50` cross-checks matched)
- **Disjoint methods:**
  - `Leg(5)` constructed via 12-ray involution projection (`iota: v -> 2v`, `-1` eigenspace residual `0.0`) on `Rays(5) = (F_5^2 \ {0}) / {+-1}`; `K_5` built via explicit 60-element `PSL(2, F_5)` conjugation (`|[L]| = 12`, eigenvalue error `3.21e-50`); unitary intertwiner `U` built via simultaneous `(W_6, W_ch, C_3)` diagonalization (disjoint from `L`-eigenprojectors), confirming `U^H {L, S, R, C_3, W_6, -W_ch} U` to `<= 1.65e-49` and `Leg(5)` spectra to `5.35e-50`.
  - `Phi^wp` computed via `-d^2/dz^2 ln jtheta(1, pi*z, q)` (no `E_2` series): `R_5^wp(omega_+) = 1/4` (err `3.34e-51`), `R_5^wp(i) = 7/23` (err `2.00e-51`), `SL(2, Z)` ratio invariance `2.67e-51`.
  - `Phi^Siegel` computed via `jtheta(1, ...)` and Euler-pentagonal Dedekind `eta(tau)` (no `B_2` q-products): `R_5^Siegel(omega_+) = 0.0034232996167354906...`, `fb_siegel(omega_+) = 0.0034116206171842369...`, `R_5^Siegel(i) = 0.0142848218747545619...`, `SL(2, Z)` ratio invariance `7.52e-52` — matching every printed Producer digit (`< 1e-16`).
  - `O_27^{(3,3,3)}` constructed as the `<C_tr, Sig_tr>`-orbit of `(3,3,3) mod 27` (`|O_27| = 72`), `Q_6` extracted via direct Union-Find partition refinement (unique 6-block system, block sizes `[12]*6`, `|Fix(C)| = 3`), `|G_3| = 216`, `rho: (L, R, C, Sig) -> (1, 5, 2, 3) mod 6` (`0` homomorphism defects, `0/216` character-defect mismatches for both `rho` and `rho_3 = rho^4`).
  - `O_27 - Q_6` chiral moments `m = 0..4` verified via exact `G_3` group-algebra DP for `N in {3, 5, 7, 15}` (`max_diff = 7.46e-47`), and `Q_6 x Weil_N` moments `m = 0..6` verified independently via direct `(6N) x (6N)` matrix powers and non-Hermitian `mp.eig` on `H_1, H_2` (`max_exact_err = 6.13e-46`, `eig_vs_direct = 9.63e-46`, `dp_vs_direct = 2.53e-47`), matching all `28` Producer moments (`N in {3, 5, 7, 9}`, `m = 0..6`).

### Module W3 (`75 / 75` cross-checks matched)
- **Disjoint methods:** Branch-free completed-square 1D Jacobi-theta sums (`jtheta(3, pi*tau, q)` and `jtheta(3, pi*tau*s, q^2)` with derivatives, explicitly evaluating both real and imaginary linear harmonic pieces and verifying the real piece vanishes to `1.39e-52` on `L_N`). Zero-parameter 2D stabilization via coarse fundamental-domain scan + golden-section search + secant root-finding on 4-point central `dV/dy` + 5-point Richardson-extrapolated 2D Hessians.
- **Key referee residuals:** `max_sl2z_equiv_err = 1.77e-50`, `L_3` odd norm `6.63e-52`, `max_omega_plus_leak = 1.28e-100` (`even -> q=2`, `odd -> q=1` across all lattices), boundary global maximum at `omega_+` confirmed for `L_7` and `L'_15`, and strict 2D interior global maxima at `x = 0` (`V_xx < 0, V_yy < 0`) with strict saddles at `x = 1/2` (`V_xx > 0, V_yy < 0`) confirmed for `L_11`, `L_15` (`y_* = 2.2677896617356798665...`), and `L_19`.
- **Precision Diagnostic (Finite-Difference Order):** Producer and Referee agree to `16/16` printed digits on all `V_omega_plus`, `V_tau_i`, `V_star`, `V_half`, to `12/12` digits on `V_yy`, and to `12–14` digits on `y_star` (`|dy| <= 3.3e-13`). On `V_xx`, Producer values are systematically smaller in magnitude by a relative factor of `3.28e-8` (`L_11`), `3.29e-8` (`L_15`), and `3.29e-8` (`L_19`), matching the exact `O(h^2)` truncation term `(2*pi*h)^2 / 12 = 3.28987e-8` of a 3-point finite difference at `h = 10^{-4}` acting on the `cos(2*pi*x)` mode (versus Referee's `O(h^6)` 5-point Richardson extrapolation). All signs and concavity/saddle classifications match identically.

### Module W4 (`43 / 43` cross-checks matched)
- **Disjoint methods:** Exact `Q[[q^{1/15}]]` identities `A*D + B*C == 0`, `B*theta_{A2,0} - D*theta_{A2,1} == 0`, `A*theta_{A2,0} + C*theta_{A2,1} == 0` proved through `t^60` (`q^{60/15}`) using `sympy.Poly(..., t, domain="QQ")`; `L'_15` swap isometry `j -> -4j == (-1,+1) = P_flip^{(3)}` verified (`6.95e-51`, `H_3^odd (x) H_5^odd` block norm `3.79e-51`); CRT `3 x 5` SVD and left-singular mixing `|V_{3x3}|` computed via non-squaring `8 x 8` Hermitian Jordan-Wielandt block `[[0, M], [M^H, 0]]` at `tau0`, `tau0+1`, `-1/tau0`, and dynamically computed `L_15` `tau_* = i y_*`.
- **Key referee residuals:** `all_rank_duality_ok = true` (non-squaring Jordan-Wielandt resolves rank-2 zero singular-value ratios to `1.18e-51` / `9.98e-54` for `L_15` `M_odd` and `3.35e-51` for `L'_15` `M_even`, improving on the `~1e-24` floor expected from squaring `M M^H`), `max_sl2z_sv_ratio_err = 9.35e-51`, `max_sl2z_mix_err = 3.56e-50`, `max_pflip3_comm_err = 7.26e-51`, `max_block_2plus1_leak = 3.59e-49`, `max_jarlskog = 2.53e-101`.
- **Guardrail 3 (10-trial LCG128 Householder-reflection Haar `U(3) x U(5)` scrambling):** `unitary_err = 2.73e-50`, `max_sv_err = 1.34e-50`, `max_mix_err = 1.52e-49` across both `L_15` and `L'_15`. All singular-value ratios and all `18` `|V_{3x3}|` entries at `tau0` plus `tau_*` match Producer to every printed digit (`<= 1e-10`).

---

## 3. Planted Fault Controls & Hygiene

| Control | Fault Planted | Observed Signal | Detected |
| :--- | :--- | :--- | :---: |
| `RPF1` | `N=15, r=2` tested vs `r=1` trace + false mirror check on `N=35` | `tr_err = 3.4641`, `N=35` has no `sqrt(-1)` | `true` |
| `RPF2` | Perturb `omega_+` by `+i/100` in `R_5^wp` + faulty `v1` character `(3,3,2,3) mod 6` | `wp_ratio_err = 7.12e-5`, `441` homomorphism defects | `true` |
| `RPF3` | Wrong equianharmonic `omega_- = -1/2 + i*sqrt(3)/2` + `x=1/2` saddle `V_xx` | `q=1` leak `0.5591`, `V_xx = +1.063e-5 > 0` | `true` |
| `RPF4` | Wrong sign `A*D - B*C` + `1e-5` swap-breaking perturbation on `L'_15` `M_even` | `AD-BC != 0`, `s_3/s_1 = 4.82e-6` | `true` |
| `RPF5` | Unphysical gauge-breaking `U_{3,e} != U_{3,o}` (Guardrail 3) | `sv_err = 5.35e-51`, `mix_shift = 0.7758` | `true` |

- **Hygiene:** `ast_float_literal_count = 0` (`referee_a2_weil_chiral_lattice_bridge.py` and `compare_referee_vs_producer.py`), `json_float_literal_count = 0` (`referee_a2_weil_chiral_lattice_bridge_out.json` and `referee_vs_producer_diff.json`), `T7b Part 1` refused imports/calls/sys.path mutations = `0`.

---

## 4. Final Certification

All pre-registered expectations in the Scope Card for **`Card A2-WEIL-CHIRAL-LATTICE-BRIDGE`** (`W1`, `W2`, `W3`, `W4`, controls, and hygiene) are independently verified by completely disjoint methods at 50-digit precision and exact algebraic arithmetic, with **`322 / 322`** cross-diff checks matched and **`0`** discrepancies.

**VERDICT: `PASS`**
