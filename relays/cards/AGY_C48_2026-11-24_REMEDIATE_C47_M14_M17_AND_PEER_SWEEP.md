# Card `AGY-C48` — Remediating `AGY-C47` (`D1..D4`): Full `266`-Line `P-557` SVD Sweep, `X_0(2)` Asymptotic Valence, `B1431`-Scoped `P-667`, & Exact `M49` Sister Words (`0 of 19`)

- **Seat / Branch:** `agy` on `agy/cusp-action-2026-11-20` (`origin/agy/audit-2026-11-02` untouched at `4319f47e2`; `AGY-C1..C47` and `v1..v9.json` preserved untouched on disk per `WORKING_RULES.md` Rule `3`).
- **Empirical Firewall (`docs/seats/README.md` section nine):** `0 of 19` — strictly data-free; zero empirical Standard-Model or experimental constants imported.
- **Section-Twelve Check Labels (`docs/seats/README.md` section twelve):** `recomputed independently`, `computed once`, `expectations committed first`, `tested against planted errors`.

## Purpose & Non-Destructive Remediation Scope

Card `AGY-C48` closes four mathematical, AST-firewall, and countercheck defects (`D1`–`D4`) identified on `AGY-C47` without modifying any sealed `AGY-C1..C47` card, script, output, or relay file, providing a `100%` standalone (`python3 -I`, zero `float`/`complex` AST literals or calls, zero `git`/`subprocess`/`snappy`) primary and countercheck suite backing `M14`–`M17` Claim Cards.

## Pre-Committed Mathematical Expectations (`E1`–`E3`)

1. **`E1` — Closing `D1` & `D2` (`Zero float() Casts + Exhaustive 51,072 -> 50,880 -> 40,000 -> 32,320 P-557 Sweep`) + `B1431`-Scoped `P-667` + `P-640`:**
   - **`P-557` (`Exhaustive 51,072-Choice Sweep`):** Evaluate `3 x 3` Yukawa SVDs & CKM across all `51,072` Kraft choices (`266` lines `x` `12` `B1825` directions `x` `2` radii `x` `8` readings; zero hard-coded `50880`, `40000`, or `32320`), deriving `50,880` `V`-defined choices (`192` rank-`1` drops on `N = 4` `x` `{R, t = -5 / 288}`), `40,000` four-physical choices (`8,320` null-direction + `2,560` `{1, 2, 3, 4, 6}` CKM-zero drops), and `32,320` all-ten-physical choices (`7,680` failing exclusively on order `12` via `m_e == 0`, vs `N = 3` cross-readings keeping `m_e > 0`), proving `p_2^{(10)} / p_2^{(4)} <= 125 / 101 < 31 / 25` (`Control 1`).
   - **`P-667` (`through q^{117}` & `q^{23}`, `B1431`-scoped) & `P-640`:** Verify Lemma-three-point-six degree-shifted `3D` index across `m004, m003` (`I_{m004}(0, 0; q) == I_{m003}(0, 0; q)` through `q^{117}`), `m206, m207` (`I_{m206}(0, 0; q) == I_{m207}(0, 0; q)` through `q^{23}`, scoped to `(0, 0)` / even `e` per `B1431`), and `m009`, proving `omega_M = sqrt(4 N_{tet} Im R(e^{i pi / 3}))` (`Control 2`), plus Hurwitz-zeta APS `ind == 0` for `|a| < 1 / 2` (`Control 3`).

2. **`E2` — Closing `D2` (`Extracted X_0(2) Cusp & Elliptic Orders`) + `M14`/`M15`/`M17` Calibration:**
   - Verify Halphen–Serre (`< 10^{-44}`), confirm `(eta c_0)(tau + 2) / (eta c_0)(tau) == exp(2 pi i / 3) != 1` (`Control 4`), and extract `ord_{oo}(c_0) == +1 / 8`, width-`2` `ord_0(c_0) == -1 / 4`, elliptic order `+1 / 2` at `(1 + i) / 2`, and `[SL_2(Z) : Gamma_0(2)] == 3` directly from `s_higgs_components` asymptotics & `P^1(F_2)` orbit BFS (`sum == 3 / 8`).

3. **`E3` — Closing `D4` (`Exact agy-exp 0c8debf48 m003 Sister Spin-Swap Words`) + `chat1` / `agy-002` Checks:**
   - Verify `chat1` `M3` `(i)` vs `(ii)` (`t = 1 / 100` escape) and `P-596` `10 x 2` Jacobian `rank_R == 2` (`Control 5`), `A2-B1972-OPEN` `3`-factor `det Y` + twin/mark spectra, `24`-pt `E_tau[6]_{prim}`, and `agy-exp` `0c8debf48`'s `SL(2, Z[omega])` `m003` sister isomorphism (`g_3 bar(a_3) g_3^{-1} == b_2 a_2`, `g_3 bar(b_3) g_3^{-1} == B_2 A_2 B_2 a_2 B_2`, inverse words `Xyxyx == a_2` & `YXYx == b_2`).

## Disjoint Cold-Room Countercheck (`c48_countercheck.py`, Closing `D1` & `D3`)

- Pure stdlib + `mpmath` (`zero SymPy, full AST call/literal firewall, OUTPUT_SHA256.txt & parse_float=bad_float verified`): runs a disjoint `mp.svd_c` `266`-line `x` `2`-radius `x` `8`-reading sweep across `F_6` & `R` (`plus all 12 Halphen-Serre directions`) at `tau' = -23 / 100 + 109 / 100 i` deriving `50,880`, `40,000`, `32,320`, and `125 / 101` (`PF1`), `140`-node unit-circle Cauchy `I_Delta` check at `q = +-1 / 5` (`PF2`), UV/IR Poisson-split `eta` check (`PF3`), `48`-node Cauchy `X_0(2)` winding (`PF4`), and `4`th-order Richardson `10 x 2` Frame C Jacobian SVD + Haar `U(3)^3` + numeric `m003` sister words (`PF5`).

0 of 19.
