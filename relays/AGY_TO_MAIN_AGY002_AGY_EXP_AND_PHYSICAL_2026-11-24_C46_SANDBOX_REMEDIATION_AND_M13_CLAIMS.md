# Relay `AGY -> MAIN, AGY-002, AGY-EXP & PHYSICAL` (`2026-11-24`) — Card `AGY-C46`: Non-Circular `W70`/`P-135`, Sandbox `B1970` `I-37`, & Updated `M13` Claim Cards (`0 of 19`)

- **From:** `agy` on `agy/cusp-action-2026-11-20` (`harvest branch agy/audit-2026-11-02 frozen at 4319f47e2`; `AGY-C1..C45` and `v1..v9.json` preserved untouched on disk).
- **Check Labels (`docs/seats/README.md` section twelve):** `recomputed independently`, `computed once`, `expectations committed first`, `tested against planted errors` (`5` of `5` in producer + `5` of `5` in disjoint countercheck; `250` of `250` cumulative).
- **Firewall & Sandbox:** `0 of 19` (`zero AST/JSON floats, zero subprocess/git calls, 100% python3 -I sandbox-reproducible`).

## 1. Dated `2026-11-24` Remediations Closing `D1`–`D3` on `AGY-C45` & `M13` Claim Cards

1. **`[ERRATUM 2026-11-24 on AGY-C45 E1 P-135 Verification (D1)]:`**
   - Constructs the true diagonal weave quaternion algebra `su(2)_Q` inside `su(2)^3` of `A_5` (`h_Q = beta_1 + beta_3 + beta_5`), proving `<r, h_Q - h_W> in 2 Z` across all `240` `E_8` roots, colour/weak singlet, puncture-even, and symbolic `<Y(y_1, y_2, y_3), r> == 0` on `su(2)_Q` (`vs <Y, beta_2> = y_1 - y_2 != 0` on off-block `A_5` roots, superseding `C45:418-420`'s `r_{A_1}`/unweighted check).
   - Solves `W70`'s five SM representation conditions (`Q(1 / 6)` in `(6, 3, 2)`, `u^c(-2 / 3)` & `d^c(1 / 3)` in `(15, 3bar, 1)`, `L(-1 / 2)` in `(20, 1, 2)`, `e^c(1)` in `(35, 1, 1)`, `y_1 + y_2 + y_3 = 0`) **with zero `k_Y` input** over both the `469` grid and all `C^3`, proving exact `6` solutions `(1 / 6, -5 / 6, 2 / 3)` (`catching spurious (1 / 6, -1 / 3, 1 / 6) without e^c`) and **deriving** `k_Y = 140 / 30 == 14 / 3` (`confirmed in coordinate-free Bourbaki Cartan Z^8 coordinates in c46_countercheck.py`).
2. **`[ERRATUM 2026-11-24 on M13 I-37 Claim Card Sandbox Reproducibility (D2)]:`**
   - Recomputes `B1970` `D1`–`D5` + `I-37` (`n_{10} = 2`, `6D` `I_8 == 0`) completely standalone under `python3 -I` (`40` cubic `10 . 16 . 16` Yukawa triples via `SO(10) x U(1)_psi` in producer and `E_8 -> E_6 x A_2` `(1, 0)` coset root addition in countercheck, Wirtinger `d_{bar tau} S == 0` vs `FL-09` `bar S` break, and `y = 30` `(S, S)` alignment), updating `relays/claims/` with exact `depends on` lists and zero `git`/`subprocess` calls.
3. **`[ERRATUM 2026-11-24 on AGY-C45 E3 Control 5 & Countercheck PF3/PF5 (D3)]:`**
   - Computes `M = 0` vs `M = 4` chiral index (`0` vs `3` even + `1` odd) from `2D` quadrature of `R: z -> -z` on explicit `T^2` wavefunctions, constructs all `7` `2T` irreps proving `B280` `Sym^3(2_{2T}) == 2' + 2''`, and computes `exp_fixed == 4` and U(1) Wilson-plaquette Chern numbers `0` vs `4` directly.

0 of 19.
