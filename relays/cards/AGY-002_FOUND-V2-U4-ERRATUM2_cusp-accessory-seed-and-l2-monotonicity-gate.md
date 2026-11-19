# Erratum `2` to Card `AGY-002_FOUND-V2-U4` — Cusp Accessory Seed & `L_2` Monotonicity Gate (`0 of 19`)

## 1. Cold-Room Referee Defect Catch on Immutable `v1`

- Immutable `v1` (`43bdf65b0` / `0ee4fd3a1`, `verify_found_v2_u4.py`) and Cold-Room Referee (`f94990176` / `a044f145f`, `referee_found_v2_u4.py`) remain untouched in git history.
- Cross-checking `0ee4fd3a1` against `a044f145f` uncovered a numerical branch-jumping defect in `v1`'s `float64` Chebyshev `L_2(tau)` solver: seeding `c_val = 0` caused Gauss–Newton to jump onto an excited non-uniformization root on `y in {5/2, 3, 4, 5}` (`giving 946/100 instead of 229/100 at -1/2 + 4 i`, shifting `m3_tilde_S` `R_ed_min` from `1274/100` to `1577/100`, and shifting `W-P1c` `Clocks A, B, C` by ~`1/100`).
- Wait-scope verification confirmed `Gate F-U2`'s moduli (`-21/100 + 13/10 i`, `13/100 + 17/10 i`, `13/100 + 6 i`, `i`, `rho`) match Referee `RK4` to `< 2 * (1/10)^14`, leaving `Gates F-U0..F-U3` `100%` unaffected.

## 2. Companion `v2` Requirements

Companion `v2` (`relays/agy002_found_v2_u4_v2/verify_found_v2_u4_v2.py`) must:
1. Seed accessory Gauss–Newton at the exact cusp asymptote `c_0 = pi^2 / 12` and assert hyperbolic monodromy `|Re Tr(T_a)| > 2` and `|Re Tr(T_b)| > 2` on every `L_2` solve.
2. Enforce strict monotonic cusp decay `L_2(11/10 i) > L_2(2 i) > L_2(3 i) > L_2(4 i) > L_2(5 i) > L_2(6 i) > L_2(8 i) > L_2(10 i) > pi + ln(pi) - 3 ln(2)` with `L_2(10 i) - (pi + ln(pi) - 3 ln(2)) < 1/25` in Section `0`.
3. Verify `22 / 22` committed `*SHA256.txt` manifests (`21` prior + self `SCRIPT_SHA256.txt`), while passing all `AGY-002_FOUND-V2-U4` (`a0f86dc64`) and `ERRATUM 1` (`3ac7c6796`) rational bars (`including m = 3 R_ed_min > 10` across all `16` FD points).

## 3. Firewall

Strict `0 of 19`; `v1` (`43bdf65b0` / `0ee4fd3a1`) and Referee (`f94990176` / `a044f145f`) remain unmodified.
