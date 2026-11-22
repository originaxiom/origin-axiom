# `AGY-002_A2-OW10` — 4D Asymptotic Safety FRG Double-Pincer Selection (`0 < N_S + N_W - 4 N_V < 14`), Stelle Spin-2 Pole & `a`-Theorem Flow, and Master Open-Weave ToE Scorecard Results (`0 of 19`)

## 1. Check Labels and Tracked Custody (`docs/seats/README.md` § `12`)

- **expectations committed first:**
  - Card commit `09b9c55f1`: `relays/cards/AGY-002_A2-OW10_asymptotic-safety-double-pincer-stelle-pole-and-master-scorecard.md`.
  - Early `v1` script `7f23a4235` (`relays/a2_ow10/verify_a2_ow10.py`, `SCRIPT_SHA256.txt`) caught a generator typo in `N = 5` `b` at the pre-run group-order assert and never produced an output; preserved untouched for strict `A`-only manifest custody.
  - Authoritative Producer `v2` script seal `4de06843e` (`relays/a2_ow10_v2/verify_a2_ow10_v2.py`, `SCRIPT_SHA256.txt`) & unread output seal `7fe067647` (`relays/a2_ow10_v2/verify_a2_ow10_v2_out.json`, `OUTPUT_SHA256.txt`, `all_gates_passed = true`, `0` errata).
- **recomputed independently:**
  - Independent Cold-Room Referee built from Card `09b9c55f1` alone (zero access to `relays/a2_ow10/` or
    `relays/a2_ow10_v2/` prior to `Commit 4b`), using strictly disjoint `sympy` symbolic cubic derivation +
    manual Sturm-sequence root counts + direct `55`-dps bracketed bisection & `2D` Newton-Raphson directly on
    `(beta_g, beta_lam)` (zero `polyroots`) + 4th-order Richardson finite-difference Jacobian (`jac_conv < 2 /
    10^40`), disjoint matrix-group realizations (`GL(2, F_2)`, `PSL(2, F_3)`, `SO(3, Z)`, `PSL(2, F_5)`) +
    direct `0 .. 2^d - 1` bitmask Fock-space enumeration, and symbolic `sympy.apart` / `sympy.residue`: script
    seal `bb1569319` (`relays/a2_ow10_referee/referee_a2_ow10.py`, `SCRIPT_SHA256.txt`) & unread output seal
    `42157ca60` (`relays/a2_ow10_referee/referee_a2_ow10_out.json`, `OUTPUT_SHA256.txt`, **`0` discrepancies
    across all `51 / 51` numerical fields (`0 / 51` printed-digit rounding mismatches), all `21 / 21` action
    rows, all `6 / 6` `a`-theorem stages, all `12` scorecard rows, and `4 / 4` planted faults**; on the `19`
    non-chiral even-`d` rows producer sets decoupled `n_W_chiral = 0` while referee retains raw `3 * 2^(d-1)`,
    both identically yielding `is_chiral = false` and `all_four_gates_pass = false`).
- **tested against planted errors:**
  - `4 of 4` planted faults caught identically in both `7fe067647` and `42157ca60` (`PF-OW10-1` flipping fermion sign in `B_1` shifts `M_g` from `+8` to `-88`, collapsing `g_*` by `> 18x` to `< 1 / 2` and shifting `lam_*` from `< -10` to `> -1`; `PF-OW10-2` `N_gen = 4` gives `M_g = +24 > 14` with `0` UV FPs; `PF-OW10-3` switching to Type-I cutoff gives `M_g = +56 > 14` with `0` UV FPs; `PF-OW10-4` reversed `a_IR - a_UV = -125 / 48 < 0` and non-conformal `xi = 0` `(0 - 1/6)^2 = 1/36 != 0`).

## 2. Mask-Safe Verification Summary (`0 of 19`)

| Task / Metric | Producer `v2` (`7fe067647`) | Cold-Room Referee (`42157ca60`) | Agreement |
|---|---|---|---|
| `AST` source & `SHA-256` custody | `0` float/complex literals, `0` `frontier/` imports, `A`-only manifests `OK` | `0` float/complex literals, `0` `frontier/` imports, `0` `polyroots`, `A`-only manifests `OK` | Exact (`0` mismatches) |
| `OW10-A`: Guardrail 4 Litim 2004 & DEP `1311-2898` benchmarks | Pure gravity `g_* ~ 70732 / 10^5`, `lam_* ~ 19320 / 10^5`, `theta ~ (14753 +- 30432 i) / 10^4`; pure Dirac fermion survival `N_D <= 6` (Type-II) vs `N_D <= 3` (Type-I) | Direct `55`-dps 2D Newton + Sturm + 4th-order Richardson FD (`res = 0`, `jac_conv < 5 / 10^41`): `0` printed-digit mismatches, identical `N_D` collapse walls (`7` vs `4`) | Exact (`0` discrepancies) |
| `OW10-A`: Exact Double-Pincer `0 < N_S + N_W - 4 N_V < 14` | At `N = 5, 2H`: `5 / 2 < N_gen < 27 / 8` uniquely selects `N_gen = 3` (`N_gen = 1, 2` violate `M_g > 0`; `N_gen = 4` has `0` UV FPs); at `N_gen = 3`: `n_H in {1, 2, 3}` (`n_H = 4` gives `0` UV FPs) | Exact Sturm + 2D Newton reproduction across all `N_gen = 1..4` and `n_H = 1..4` | Exact (`0` discrepancies) |
| `OW10-A`: Open-Weave `(8, 48, 12)` Type-II FP, `21` Actions, & Caveats | `N = 5, d = 5` (`A_5 / A_4`, `M_g = +8`) unique `1 of 21` survivor; Type-II UV-attractive FP (`7 < g_* < 71/10`, `-101/10 < lam_* < -10`, `theta` real `> 2`, `res < 1 / 10^30`); Type-I gives `0` FPs (`M_g = +56` `2H`, `+46` SM `1H`); strong-coupling caveat flagged | Matrix groups (`GL(2,F_2)`, `PSL(2,F_3)`, `SO(3,Z)`, `PSL(2,F_5)`) + bitmask Fock `0 .. 2^d - 1`: identical unique `1 of 21` winner, `0 / 51` numerical digit mismatches, `res < 7 / 10^55`, Type-I destruction & strong-coupling caveat identically confirmed | Exact (`0` discrepancies) |
| `OW10-B`: Stelle Spin-2 Ghost Pole & `6`-Stage `a`-Theorem Ladder | `(c, a) = (37/15, 127/45)` (`2H`), `(73/30, 253/90)` (`1H`); `b_R(xi = 1/6) = 0`; Stelle `1/(x(1+x)) = 1/x - 1/(x+1)` exact at `x in {1/3, 1, 5}` (residue `-1` ghost); `5 / 5` positive drops summing to `125 / 48` | Symbolic `sympy.apart` & `sympy.residue` (`+1` at `0`, `-1` at `-1`) + `sympy.Rational` `6`-stage ladder: identical exact rationals (`1/90, 11/240, 223/360, 17/9, 7/180`, total `125/48`) | Exact (`0` discrepancies) |
| `OW10-C`: Master Open-Weave ToE Scorecard (`A2-OW1..A2-OW10`) | `12` rows: `5 PROVED`, `3 PARTIAL / CONDITIONAL`, `2 NO-GO / IMPOSSIBLE-BY-THEOREM`, `2 STILL OPEN` (`0` unclassified) | Identical `12`-row exact partition `5 + 3 + 2 + 2 = 12` | Exact (`0` discrepancies) |
| `OW10-D`: Planted faults (`PF-OW10-1..4`) | `4 / 4` caught | `4 / 4` caught | Exact (`4 / 4`) |

## 3. Core Foundational Findings (`0 of 19`)

1. **Exact Double-Pincer Selection of `N_gen = 3` (`A2-OW4` + `A2-OW10`):** Combining `A2-OW4`'s lower bound
   for attractive 1-loop Sakharov gravity (`M_g = N_S + N_W - 4 N_V > 0`) with `A2-OW10`'s upper bound for a
   covariant Type-II Lichnerowicz Asymptotic Safety UV fixed point (`M_g < 14` in the fermion-dominated `M_l <
   0` sector, proved via the exact integer cubic `2(M_g - 14) u^3 + (82 - 2 M_g - 6 M_l) u^2 - 118 u + 48 =
   0`) yields the exact double-pincer `0 < N_S + N_W - 4 N_V < 14`. At `N = 5, 2H` (`N_S = 8, N_V = 12, N_W =
   16 N_gen`), this reduces to `5 / 2 < N_gen < 27 / 8`, **uniquely selecting `N_gen = 3` generations** (and
   restricting Higgs doublets at `N_gen = 3` to `n_H in {1, 2, 3}`), while selecting **`N = 5, d = 5` (`A_5 /
   A_4`, `M_g = +8`) uniquely (`1 of 21`)** across all faithful transitive actions of `Delta(2, 3, N)` (`N =
   2..5, d <= 12`).
2. **Quantum-Gravity Check Result & Master Scorecard (`A2-OW1..A2-OW10`):**
   - **Positive survival:** Open-weave `2H` `(8, 48, 12)` possesses a unique UV-attractive Type-II fixed point (`7 < g_* < 71 / 10`, `-101 / 10 < lam_* < -10`, both real critical exponents `> 2`), zero 1-loop induced `R^2` scalaron at conformal `xi = 1 / 6`, and strict Komargodski-Schwimmer `a`-theorem monotonicity (`Delta a_total = 125 / 48 > 0` across all `5` consecutive EFT thresholds down to `gamma + 3 nu_L`).
   - **Honest limitations:** Perturbative 4D induced quadratic gravity has a massive spin-2 Stelle ghost (residue `-1` from `c = 37 / 15 > 0`), Type-I non-Lichnerowicz FRG destroys the UV fixed point completely (`M_g = +56 > 14`, `0` UV FPs), and the surviving Type-II fixed point sits at strong single-metric coupling (`g_* > 7`, `lam_* < -10`), so higher-order/bi-metric FRG or `7D` bulk UV completion remains open alongside the `10^(-120)` cosmological constant value, `4` continuous dimensionless scale ratios (`g_UV, lam_0, tan(beta), M_R / M_X`), and early-universe dynamics (`5 PROVED, 3 PARTIAL / CONDITIONAL, 2 NO-GO, 2 STILL OPEN`). `0 of 19.`
