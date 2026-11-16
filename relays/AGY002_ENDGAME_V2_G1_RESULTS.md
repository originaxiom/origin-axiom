# `AGY-002_ENDGAME-V2-G1` — Gate 1 Results (`0 of 19`)

## 1. Check Labels and Tracked Evidence (`docs/seats/README.md` § 12)

- **expectations committed first:**
  - Card commit `65c6f2e41`: `relays/cards/AGY-002_ENDGAME-V2-G1_e6-pati-salam-dparity-gauge-and-strong-cp.md`
  - Erratum card commit `4707fd827` (prior to any output file): `relays/cards/AGY-002_ENDGAME-V2-G1-ERRATUM_perturbative-uv-grid.md`
  - First script seal `6951d2e46`: `relays/agy002_endgame_v2_g1_fixed/verify_endgame_v2_g1_fixed.py`, `relays/agy002_endgame_v2_g1_fixed/SCRIPT_SHA256.txt` (unmodified prior script at `57001ce15`: `relays/agy002_endgame_v2_g1/verify_endgame_v2_g1.py`, `relays/agy002_endgame_v2_g1/SCRIPT_SHA256.txt`)
  - First output seal `b4639e929` (committed unread): `relays/agy002_endgame_v2_g1_fixed/verify_endgame_v2_g1_fixed_out.json`, `relays/agy002_endgame_v2_g1_fixed/OUTPUT_SHA256.txt`
- **recomputed independently:**
  - Second script seal `612475c36` (built from the card and published literature alone without reading or importing the first script): `relays/agy002_endgame_v2_g1_referee/referee_endgame_v2_g1.py`, `relays/agy002_endgame_v2_g1_referee/SCRIPT_SHA256.txt`
  - Second output seal `dcf42f19e` (committed unread): `relays/agy002_endgame_v2_g1_referee/referee_endgame_v2_g1_out.json`, `relays/agy002_endgame_v2_g1_referee/OUTPUT_SHA256.txt`
- **tested against planted errors:**
  - `5 of 5` planted cases caught in `relays/agy002_endgame_v2_g1_fixed/verify_endgame_v2_g1_fixed_out.json` (`PF1.1` `0.9682 > 0.05`, `PF1.2` `3.1416 > 3.0`, `PF1.3` `4.0 > 1.0`, `PF1.4` `0.0496 > 0.01`, `PF1.5` `1.0 > 0.5`);
  - `5 of 5` planted cases caught in `relays/agy002_endgame_v2_g1_referee/referee_endgame_v2_g1_out.json` (`PF1.1` `0.9423`, `PF1.2` `3.1416`, `PF1.3` `4.0`, `PF1.4` `0.0422`, `PF1.5` `1.0`).

## 2. Numerical Summary (`0 of 19`)

| Check | First Computation (`verify_endgame_v2_g1_fixed_out.json`) | Second Computation (`referee_endgame_v2_g1_out.json`) | Bound |
|---|---|---|---|
| AST zero float literals & allowed imports | `0` floats, `True` | `0` floats, `0` complex, `True` | `0` floats |
| Exact `Z[zeta_6]` Riley cusp & `E_6` `27` branching | `2 Re(tau_cusp) = 0`, `|tau_cusp|^2 = 12`, `t_tan = 1`, `A_max = 2 sqrt(3)`, `Vol(m004) = 2.0298832128193074`, `T_4 = T_{2L} = T_{2R} = 3`, `N_g = 3 => b_3 = -7` | Verified across `4,372` reduced words (`len <= 7`), `polylog` vs `quad` `0.0`, Lobachevsky `4.22e-81`, `27` minuscule Weyl weights | Exact |
| `3`-Family `D`-parity `Strong-CP` vanishing (`tree + 1-loop + 2-loop SM RGE`) | Tree `5.83e-16`, `2`-loop Jacobi `Im Tr = 2.60e-18`, IR `|bar_theta| = 1.28e-14` (`|J_CKM| >= 0.0160`) | `45`-digit Jacobi `Im Tr = 5.49e-53`, `DOP853` IR `|bar_theta| = 5.55e-16`, `mpmath` IR `1.00e-28` (`|J_CKM| >= 0.0311`) | `< 1e-13` |
| Haar `U(3)^6` post-`RGE` `Strong-CP` & observable invariance | `|bar_theta| <= 7.02e-14`, observable drift `7.85e-14` (`8` trials) | `|bar_theta| <= 5.42e-15`, observable drift `4.66e-15` (`10` trials) | `< 1e-12` |
| `P-862` `1`-loop `Pati-Salam` closed-form law `(23/134, 109/201, 506/201)` vs ODE (`96` histories) | `max_err = 3.25e-15`, positive slope `506 / (201 pi) = +0.801317` | `max_err < 1e-13` (`DOP853`), exact `0.0` `1`-loop table diff vs first computation; `2`-loop Yukawa sensitivity `<= 1.32e-5` | `< 1e-13` |
| `4D` collar scale-fixing test (`Guardrail 1` obstruction) | `3D` boundary Mostow-rigid; `alpha_U^{-1}` & `Delta_PS` scale linearly with `(L_4, kappa_warp)` (`parameter-free 3D closure = False`) | Independently confirmed (`alpha_U^{-1}` ratio `2.0` at `lambda_4 = 2`; `Delta_PS` unfixed without `4D` bulk potential) | Honest obstruction |

## 3. Result for Gate 1

1. **Exact `3`-Family `Strong-CP` Law (`B1948` Row `19` Rehabilitated on `X_4`):** On `X_4 = m000 x~ [-1, 1]` bounded by amphicheiral `partial X_4 = m004` (`Re(tau_cusp) = 0`), `E_6 -> SU(4)_c x SU(2)_L x SU(2)_R x| Z_2^D` preserves `N_g = 3` chiral families without `6`-family mirror doubling and enforces `bar_theta_QCD = 0` (`given positive determinant sign parity sgn det(Y_u Y_d) = +1`, `1` discrete sign bit, `0` continuous parameters) across tree level, `1`-loop, and `2`-loop non-commuting `SM RGE` evolution while maintaining `|J_CKM| > 1e-2`.
2. **Exact `P-862` `Pati-Salam x| Z_2^D` Gauge Corridor (`B1948` Row `4` Generalized):** Eliminating `(alpha_U^{-1}, ln(M_PS / mu_IR))` yields the universal `1`-parameter corridor `sin^2 theta_W = 23/134 + (109/201)(alpha_EM / alpha_3) + (506 / (201 pi)) alpha_EM Delta_PS + delta_{2-loop}` with strictly positive slope `+506 / (201 pi)` lifting the minimal `SU(5)` desert (`Delta_PS = 0`), with `2`-loop Yukawa sensitivity `~ 1.3e-5`.
3. **Exact `4D` Collar Scale Obstruction:** `3D` hyperbolic rigidity of `m004` uniquely fixes `tau_cusp = 2 sqrt(3) i`, `A_max = 2 sqrt(3)`, and `Vol(m004) = 2 Cl_2(pi/3)`, but leaves transverse interval length `L_4` and collar warp `Delta_PS = ln(M_U / M_PS)` unfixed unless a `4D` bulk gravitational/Casimir potential is supplied. Gate 1 is locked. `0 of 19.`
