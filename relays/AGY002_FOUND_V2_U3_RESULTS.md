# `AGY-002_FOUND-V2-U3` — Gate `F-U3` Results (`P-873 Q1/Q2`, Radiative Box vs `CW`/`Berezin` Dichotomy, & `CIM` `[R_*, G] = 0` No-Go, `0 of 19`)

## 1. Check Labels and Tracked Evidence (`docs/seats/README.md` § `12`)

- **expectations committed first:**
  - Card commit `2a7447548`: `relays/cards/AGY-002_FOUND-V2-U3_p873-q1-coleman-weinberg-higgs-plane-stabilization-and-cim-nogo.md` (`plus erratum cards f8d66057b and ab096d771`).
  - Immutable `v1` (`53d240cbc`) halted on `Section 1` `len(rays) == 12` (`6 projective rays in CP^5 vs 12 signed unit vectors in S^3 subset E` because `U_M^6|_E = -I_E`); immutable `v2` (`e56653dc7`) halted on Clarified Assumption `orbit_6_spread_box < (1/10)^10` (`because V_box at fixed tau radiatively lifts the 6-ray U_M orbit by > 22 at y = 17/10 and > 266 at y = 6`). Both remain untouched in git history.
  - Companion `v3` producer seal `33dc586ed` & unread output `061557807`: `relays/agy002_found_v2_u3_v3/verify_found_v2_u3_v3.py`, `relays/agy002_found_v2_u3_v3/verify_found_v2_u3_v3_out.json` (`2D torus cell quadrature`).
- **recomputed independently:**
  - Cold-room referee script seal `241bfe632` (`built from the three Cards alone without reading verify_found_v2_u3*, using 1D unfolded Gauss-Legendre / trapezoidal integrals vs Jacobi Theta_c(6 tau, 6 xi), 25 x 25 shifted Gauss-Legendre V_4^{frozen}, 55-digit mp.det V_det, and exact Q(zeta_24) cyclotomic algebra`) & unread output `17bda48ef`: `relays/agy002_found_v2_u3_referee/referee_found_v2_u3.py`, `relays/agy002_found_v2_u3_referee/referee_found_v2_u3_out.json`.
- **tested against planted errors:**
  - `5 of 5` planted faults caught in both `061557807` and `17bda48ef` (`PFU3-1` target-embedded `V_{fake}(h) = 1 - |<h_* | h>|^2` spread `1` `> 1/2` across `{U_M^k h_*}`; `PFU3-2` frozen tree overlap `B_{frozen}^{P873} < -11/10 < -1` at all `3` moduli; `PFU3-3` `V_{det}` puts `h_*` `> +72` [`> +60`] above circle minimum at `y = 17/10`; `PFU3-4` `1`-pt `(1/5, 1/5)` quadratic mass breaks `(v_+, v_-)` isotropy by `> 37/100` [`> 1/5`]; `PFU3-5` `10`-trial `Haar SU(3)` SV ratio invariance `< 4 * (1/10)^51` [`< (1/10)^30`] vs raw `|M_{00}/M_{22}|` shift `> 2` in producer and `> 14` in referee [`> 1/5`]).

## 2. Mask-Safe Rational Verification Summary (`0 of 19`)

| Check | Producer `v3` (`061557807`) | Cold-Room Referee (`17bda48ef`) | Sealed Rational Bar |
|---|---|---|---|
| `AST` source & `SHA-256` custody | `0` float/complex literals, `0` repo imports, `SCRIPT_SHA256` matched (`2D calib < 3*(1/10)^39`) | `0` float/complex literals, `0` disallowed imports, `16 / 16` manifests matched (`1D GL vs Theta < 3*(1/10)^55`) | Exact (`0` mismatches) |
| `Q2` ratios & `12`-vec / `6`-ray `U_M` orbit | `Q(zeta_24)` exact, `mp55 < 3*(1/10)^54`, `12` vecs / `6` rays, `U_M^12 < 8*(1/10)^55`, `inv_quad_dim = 1` | `Q(zeta_24)` exact, `mp55 < 9*(1/10)^56`, `12` vecs / `6` rays, `U_M^12 < 3*(1/10)^55`, `inv_quad_dim = 1` | Exact `== 0`, `< (1/10)^50`, `12 vecs / 6 rays`, `dim = 1` |
| Frozen tree `B_{frozen}^{P873}` (`3` moduli) | `<-134/100`, `<-129/100`, `<-110/100` (`mean < -29/100`) | `<-134/100`, `<-129/100`, `<-110/100` (`mean < -29/100`) | `< -1`, `mean < -1/5` |
| `P-873 Q1` Box vs `CW`/`det` (`y = 17/10`) | `B_p > 19`, `B_m > 17`, `orbit6 > 22`, `barrier > 19/10`, `min = [4, 0]` (`idx=0`), `CW_muE < -54`, `det_ex > 72` | `B_p > 19`, `B_m > 17`, `orbit6 > 22`, `barrier > 19/10`, `min = [4, 0]` (`idx=0`), `CW_muE < -54`, `det_ex > 72` | `> 15, > 15, > 20, > 1, (4,0)/0, < -40, > 60` |
| `P-873 Q1` Box vs `CW`/`det` (`y = 6`) | `B_p > 115`, `B_m > 32`, `orbit6 > 266`, `barrier > 48`, `idx = 0`, `CW_mu1 > 212` (`idx=0`), `CW_muE < -295`, `det_ex > 310` | `B_p > 115`, `B_m > 32`, `orbit6 > 266`, `barrier > 48`, `idx = 0`, `CW_mu1 > 212` (`idx=0`), `CW_muE < -295`, `det_ex > 284` | `> 100, > 15, > 200, > 40, idx=0, > 150/0, < -200, > 250` |
| `CIM [R_*, G] == 0` No-Go Theorem | `SymPy` exact, `24`-pt `< 2*(1/10)^53`, `mark err < 14/100`, `(0,0,0) < 4*(1/10)^53`, `exp in (-1/1000, 1334/1000)` | `SymPy` exact, `24`-pt `< 5*(1/10)^55`, `mark err < 14/100`, `(0,0,0) < 5*(1/10)^55`, `exp in (-1/1000, 1334/1000)` | Exact, `< (1/10)^40`, `< 1/5`, `< 2/1000` from `(0, 4/3)` |

## 3. Theorems Locked in Gate `F-U3`

1. **`P-873 Q2` & Cartan Scalar Relaxation (`Pure e_0 Spectral Algebra`):** Projecting $e_0$ onto the $\pm \pi/6$ eigenspaces of $U_M = T_6 S_6 T_6^\dagger S_6^\dagger$ derives the `3` zero-entry directions (`2 - sqrt(3)`, `2 + sqrt(3)`, `+1`) in exact $\mathbb{Q}(\zeta_{24})$ arithmetic without any target embedding (`Guardrail 1`), yields `12` signed unit vectors on `6` projective rays `{U_M^k h_*}`, gives `B_{tree, relaxed} == 0`, and makes frozen `2D` overlap $B_{\text{frozen}} < -1$ prefer $v_\pm$.
2. **`P-873 Q1` Scale/Functional Dichotomy & Radiative `U_M`-Orbit Lifting:** The scale-free `1`-loop UV box trace $V_{\text{box}}(h)$ (`coefficient of ln Lambda_{UV}^2`) radiatively lifts the `6`-ray `U_M` orbit degeneracy (`> 22` at `y = 17/10`, `> 266` at `y = 6`) and **uniquely stabilizes $h_*$ (`idx = 0` on the equal-magnitude circle at both moduli and `[4, 0]` global minimum on the `216`-pt `S^3` at `y = 17/10`)**, whereas at the canonical Frobenius scale $\mu_E^2$ (`where ln(H_f / mu_E^2) < 0`) `V_{CW}(h; mu_E)` flips sign (`< -54` at `y = 17/10`, `< -295` at `y = 6`) alongside Berezin `V_{det}` (`> +72`, `> +284`).
3. **Analytical `CIM [R_*, G] == 0` No-Go Theorem:** Both `24`-point shifted `Frame D1` and unshifted `CIM(0,0,0)` satisfy `[R_*, G_u(h_*)] == 0` identically (`< 2 * (1/10)^53`), proving why `Gate F-U2`'s Fock–Weil join is structurally indispensable even once $h_*$ is radiatively stabilized. Gate `F-U3` is locked. `0 of 19.`
