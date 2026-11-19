# `AGY-002_FOUND-V2-U2` — Gate `F-U2` Results (Fock-Dressed `SL_2(Z)`-Covariant Exterior-Wedge `Yukawa` Operator, `P-874(1,2)`, & Passing `B1962`/`B1963`, `0 of 19`)

## 1. Check Labels and Tracked Evidence (`docs/seats/README.md` § `12`)

- **expectations committed first:**
  - Card commit `43b7700aa`: `relays/cards/AGY-002_FOUND-V2-U2_fock-dressed-exterior-wedge-yukawa-weil-class-and-b1962-cusp-alignment.md` (`plus erratum card f4d2fd636`: `relays/cards/AGY-002_FOUND-V2-U2-ERRATUM_dedekind-eta-and-relative-nophase.md`).
  - First producer seal `d7af4bf67`: `relays/agy002_found_v2_u2/verify_found_v2_u2.py` (`halted at Section 1 assert before writing output because denom_hat omitted Dedekind eta's exp(-pi y / 12) factor, leaving sv(-1/tau)/sv(tau) == |tau| exp(pi (y - y_S) / 2); untouched`).
  - Companion `v2` producer seal `77d9963d8` & unread output `68ebb006b`: `relays/agy002_found_v2_u2_v2/verify_found_v2_u2_v2.py`, `relays/agy002_found_v2_u2_v2/verify_found_v2_u2_v2_out.json` (`full Dedekind eta(tau), relative PFU2-1, direct off-diagonal PFU2-4`).
- **recomputed independently:**
  - Cold-room referee script seal `ebc7c5a5e` (`built from the Cards alone without reading verify_found_v2_u2*, using Cauchy-Riemann Richardson RK4 shooting L_2, pure mpmath SL_2(Z) RREF intertwiner Yukawa, cyclic Hermitian Jacobi vs coupled Newton-Schulz K^{-1/2}, and Hestenes Jacobi SVD`) & unread output `92be3f70d`: `relays/agy002_found_v2_u2_referee/referee_found_v2_u2.py`, `relays/agy002_found_v2_u2_referee/referee_found_v2_u2_out.json`.
- **tested against planted errors:**
  - `5 of 5` planted faults caught in both `68ebb006b` and `92be3f70d` (`PFU2-1` omitting `zeta_5^{-ab}` breaks relative `15`-SV `T`-invariance by `4935/10000` [`134/100` in referee, `> 1/5`]; `PFU2-2` `Frame C` `(1,-4)` `up` drifts under `T^5` by `2599/10000` [`76/1000` in referee, `> 1/20`]; `PFU2-3` linear trace `(T_3, T_2)` collapses `|r_e - r_d| < 3 * (1/10)^47` [`< 2 * (1/10)^51` in referee]; `PFU2-4` direct off-diagonal `sum_{c_a != c'_a}` breaks modular `T`/`S` invariance of `r_u` by `2337/10000` [`6453/10000` in referee, `> 1/5`]; `PFU2-5` `Guardrail 3` single-matrix `|U_u^dag V_u|` shifts by `8535/10000` [`8284/10000` in referee, `> 1/10`] under random `Haar` `U_{R,u}`).

## 2. Mask-Safe Rational Verification Summary (`0 of 19`)

| Check | Producer `v2` (`68ebb006b`) | Cold-Room Referee (`92be3f70d`) | Sealed Rational Bar |
|---|---|---|---|
| `AST` source & `SHA-256` custody | `0` float/complex literals, `0` repo imports, `SCRIPT_SHA256` matched | `0` float/complex literals, `0` disallowed imports, `4 / 4` manifests matched | Exact (`0` mismatches) |
| Unreduced ODE `L_2` & `K^{-1/2}` cross-check | Dyadic Volterra `T_err < 2*(1/10)^14`, `S_err < 5*(1/10)^16` | `RK4` `T_err < 2*(1/10)^12`, `S_err < 4*(1/10)^13`; Jacobi vs Newton-Schulz `< (1/10)^40` | `< (1/10)^11` / `< (1/10)^30` |
| `P-874(1)/W-P1b` `m=1` vs `m=3` (`tau_0, tau_1`) | `3 <-> 2` `< 3*(1/10)^40`, `T`-drift `< 3*(1/10)^45`, `S`-drift `< 8*(1/10)^34`, `dG3 > 68/1000`, `dG2 > 322/1000` | `3 <-> 2` `< 4*(1/10)^46`, `T`-drift `< 4*(1/10)^42`, `S`-drift `< 2*(1/10)^42`, `dG3 > 17/100`, `dG2 > 34/100` | `< (1/10)^25, < (1/10)^20`, `dG3 > 1/20, dG2 > 1/4` |
| Fock `T, S`, `Haar SU(3)^5`, & `tau_0` lepton split | `T, S` `< 3*(1/10)^33`, `Haar` `< 2*(1/10)^44`, `|r_{e,23} - r_{d,23}| > 66/100` | `T, S` `< 3*(1/10)^38`, `Haar` `< 3*(1/10)^37`, `|r_{e,23} - r_{d,23}| > 597/1000` | `< (1/10)^20`, `< (1/10)^25`, `> 1/2` |
| `B1962`/`B1963` cusp (`y=6, 30`, `S` & `tilde_S`) | `y=6`: `min_i |V_{ii}| > 9998/10000`, `|r_e/r_d - 1| > 21/100`; `y=30`: `1-min < 9*(1/10)^24`, `sep > 66/100 (S)` & `> 4/10 (tilde_S)` | `y=6`: `1-min < 4*(1/10)^10`, `sep > 33/100`; `y=30`: `1-min < 2*(1/10)^36`, `sep > 99/100` | `> 999/1000, > 1/5` (`y=6`); `< (1/10)^12, > 3/5, > 3/10` (`y=30`) |
| `P-874(2)/W-L1` (`tau = i` and `rho`, `dps = 50`) | `sigma_3/sigma_1 < 5*(1/10)^43`, `|r_{d,23} - r_{e,23}| > 71/100` | `sigma_3/sigma_1 < 5*(1/10)^51`, `|r_{d,23} - r_{e,23}| > 64/100` | `< (1/10)^30`, `> 3/5` |

## 3. Theorems Locked in Gate `F-U2`

1. **`P-874(1) / W-P1b` Resolved Without Extra Knobs:** `O_m(tau) = O_3 (+) O_2` is `SL_2(Z)`-covariant (`3 <-> 2` `< (1/10)^39`, `T, S` `< (1/10)^33`) in BOTH `Weil` classes (`m = 1` vs `m = 3`) when full `Dedekind` `eta(tau)` is kept, AND its `G_{3,L}, G_{2,L}` family spectra cleanly distinguish `m = 1` (`2 x^2 / 5`) from `m = 3` (`x^2 / 5`) at both bulk points (`dG3 > 1/20, dG2 > 1/4`).
2. **Passing `B1962`/`B1963`'s Cusp Alignment & Breaking `B1949`'s Lepton-Down Wall:** Joining `O_m(tau)` functorially via Fock kinetic dressing `K_{(p_3, p_2)}` on `Lambda^{even}(W_5)` removes all `25`th-root obstructions (`zero T or S drift to < (1/10)^33`), is `Haar SU(3)^5` basis-invariant (`< (1/10)^36`), breaks `Y_e \propto Y_d^T` parameter-free via quadratic colour vs weak Casimir weights (`G_{3,R}` vs `G_{2,R}`), aligns `|V_{CKM}| -> I_3` at cusp `y = 6, 30` in **both** readings `S` and `tilde_S` (`1 - min|V_{ii}| < (1/10)^23` at `y = 30`), and preserves `P-874(2)/W-L1` forced null modes (`sigma_3/sigma_1 < (1/10)^42`) at `tau = i` and `rho`. Gate `F-U2` is locked. `0 of 19.`
