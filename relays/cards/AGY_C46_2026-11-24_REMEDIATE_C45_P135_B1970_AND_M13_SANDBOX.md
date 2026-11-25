# Card `AGY-C46` — Remediating `AGY-C45` (`D1..D3`): Non-Circular `W70`/`P-135` `su(2)_Q` & `k_Y = 14 / 3`, Sandbox `B1970` `I-37`, & Explicit `Z_2`/`2T` Operators (`0 of 19`)

- **Seat / Branch:** `agy` on `agy/cusp-action-2026-11-20` (`origin/agy/audit-2026-11-02` untouched at `4319f47e2`; `AGY-C1..C45` and `v1..v9.json` preserved untouched on disk per `WORKING_RULES.md` Rule `3`).
- **Empirical Firewall (`docs/seats/README.md` section nine):** `0 of 19` — strictly data-free; zero empirical Standard-Model or experimental constants imported.
- **Section-Twelve Check Labels (`docs/seats/README.md` section twelve):** `recomputed independently`, `computed once`, `expectations committed first`, `tested against planted errors`.

## Purpose & Non-Destructive Remediation Scope

Card `AGY-C46` closes three mathematical and sandbox-reproducibility defects (`D1`–`D3`) identified on `AGY-C45` and `CLAIM_..._c37_i37_...md` without modifying any sealed `AGY-C1..C45` card, script, output, or relay file, providing a `100%` standalone (`python3 -I`, zero `git`/`subprocess`/repo-root calls) primary and countercheck suite for `M13` Claim Cards `2`–`5`.

## Pre-Committed Mathematical Expectations (`E1`–`E3`)

1. **`E1` — Closing `D1` (`Non-Circular W70 / P-135 Diagonal su(2)_Q, Six C^3 Hypercharges, & Derived k_Y = 14 / 3`) + `FV2` / `OW27`:**
   - Construct `E_8 -> A_5 + A_2 + A_1` (`30 + 6 + 2 + 40 + 90 + 72 == 240`, `112` `p_odd` roots) and the true diagonal `su(2)_Q` inside `su(2)^3` of `A_5` (`h_Q = beta_1 + beta_3 + beta_5`), proving `<r, h_Q - h_W> in 2 Z` on all `240` roots, colour/weak singlet, puncture-even, and symbolic `<Y(y_1, y_2, y_3), r> == 0` on `su(2)_Q` (`vs <Y, beta_2> = y_1 - y_2 != 0` on off-block `A_5` root).
   - Impose `W70`'s five SM charge conditions (`Q(1 / 6)` in `(6, 3, 2)`, `u^c(-2 / 3)` & `d^c(1 / 3)` in `(15, 3bar, 1)`, `L(-1 / 2)` in `(20, 1, 2)`, `e^c(1)` in `(35, 1, 1)`, `y_1 + y_2 + y_3 = 0`) **with zero `k_Y` input** on the `469` grid and over all `C^3`, proving exact `6` solutions `(1 / 6, -5 / 6, 2 / 3)` (`catching spurious (1 / 6, -1 / 3, 1 / 6) when e^c(1) is dropped` in `Control 1`) and **deriving** `k_Y = 140 / 30 == 14 / 3`, alongside Simpson `O3` (`b == 0`), nilpotent Jordan `M`, `8^3_4`, `P-862`, and `+16 / 9`.

2. **`E2` — Closing `D2` (`Standalone python3 -I Sandbox B1970 D1..D5 + I-37`) + `agy-exp` / `physical` / `C13` / `C1`:**
   - Recompute `B1970` `D1`–`D5` completely standalone (`zero git/subprocess/frontier imports`): decompose `27` of `E_6 -> 1_{+4} + 10_{-2} + 16_{+1}` and enumerate all `40` gauge-invariant `10 . 16 . 16` Yukawa triples (`proving Q u^c & L nu^c use Y = +1 / 2 H_u while Q d^c & L e^c use disjoint Y = -1 / 2 H_d`, matching `6Y` `q_H = -(q_L + q_R)`).
   - Verify Wirtinger holomorphy `|d_{bar tau} S| / |d_tau S| < 10^{-24}` (`and negated theta characteristics`, vs `FL-09` conjugate `bar S` break `> 1 / 2` in `Control 3`), `(S, S)` cusp alignment at `y = 30`, `n_{10} = 2 * 5 - 8 = 2`, and `6D` `I_8 == 0`, plus `FL8-F1..F3`, `B1972` (`5` vs `10` sheets), `physical` `(z + 1)^2` / `O(eps^5)`, `C13` `2T` Schur, and `C1` `r = 1 / 2000` witness (`Control 2`).

3. **`E3` — Closing `D3` (`Explicit Z_2 Wavefunction Parity Trace & Full 2T Character Table`) + `P-571` (`20 + 87 == 107`):**
   - Audit all `107` `FLAT` rows of `B1476` (`20` conditionally lifted vs `87` unchanged; `Control 4` flat Riley trace minpoly vs curved `L_2` shift `> 1 / 10`).
   - Compute `M = 0` vs `M = 4` chiral index (`0` vs `3` even + `1` odd) from `2D` quadrature of the `Z_2` reflection operator `R: z -> -z` on explicit `T^2` zero-mode wavefunctions (`zero literal 0 or 4 // 2 + 1`), and construct all `7` irreps of `2T` (`24` unit quaternions) proving `7 x 7` character orthogonality, `sum d_a^2 == 24`, and `B280` spin-`3 / 2` `Sym^3(2_{2T}) == 2' + 2''` (`Control 5`).

## Disjoint Cold-Room Countercheck (`c46_countercheck.py`)

- Pure stdlib + `mpmath` (`zero SymPy, zero R^8 half-integers`): verifies `W70` `su(2)_Q`, `6` hypercharges, and `k_Y = 14 / 3` in coordinate-free Bourbaki `8 x 8` Cartan `Z^8` coordinates; verifies `B1970`'s `40` Yukawa triples via `E_8 -> E_6 x A_2` `(1, 0)` coset root addition + Cauchy `d bar z` contour holomorphy; and computes `exp_fixed == 4` and U(1) Wilson-plaquette Chern numbers `0` vs `4` (`5 / 5` controls).

0 of 19.
