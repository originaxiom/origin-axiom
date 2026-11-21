# Relay AGY-C11: Radiative two-Higgs splitting (`tan beta > 1` tilt, mod-`6` `t = 4` neutrality, and `y_t / y_b` unification) and `65`-digit Strong-CP orbit-product audit

*Seat: `agy` (`agy/cusp-action-2026-11-20`, after `origin/main` `279459977` / `B1970`). Date: `2026-11-21`. Custody: Card `684063bfe` (`expectations committed first`), producer `8d085b8fb` (`hashed script before execution`, passed first run with zero mends), raw output `be705f944` (`raw output before analysis`), zero-shared-code `B1945` scalar-determinant / triple-product countercheck `b297d1dff` (`recomputed independently` + `tested against planted errors`, `5 / 5` plants caught). Data-free: `0 of 19`.*

---

## One. Mod-`6` radiative Higgs neutrality on `t = 4` vs strict `m_{H_u}^two < m_{H_d}^two` tilt on `t = 3` (`E1`)

- **Exact `G_nu == G_e` and `Delta Y^two = 0` on the `t = 4` overtone (`pure math / invariant`):** Symbolic `sympy` expansion and `65`-digit evaluation across all `35` points of `P_2 (+) P_3 (+) P_6` prove `q_{R, nu} = 0 == +6 = q_{R, e} mod 6` forces `M_{w, nu} M_{w, nu}^dag = M_{w, e} M_{w, e}^dag` and `||G_nu(w) minus G_e(w)|| / ||G_e(w)|| < ten to the minus sixty` alongside `G_u(w) = G_d(w)` (`AGY-C8`), driving `1`-loop radiative Higgs splitting `Delta Y^two = 3 tr(G_u minus G_d) + tr(G_nu minus G_e) = 0` identically on `t = 4` (`while shifting geom(y_{d 3} / y_{e 3}) < 3 / 5` off `P_5`'s exact `b`-`tau` equality `y_{d 3} / y_{e 3} = 1`).
- **Strict `t = 3` radiative `tan beta > 1` tilt and `y_t / y_b` constraint:** Across all `m` in `{8, 16, 40}`, `P_5` (`t = 3`) satisfies `mean_{a != 0} Delta Y^two > 0` (`driving m_{H_u}^two < m_{H_d}^two -> radiative EWSB with tan beta = v_u / v_d > 1`). However, because intrinsic `tan beta = 1` geometric `y_{u 3} / y_{d 3}` on `P_5` stays near `1` (`between 1 and 6 / 5`), generating a large `m_t / m_b = tan beta * (y_{u 3} / y_{d 3})` hierarchy strictly requires a large radiative `tan beta >> 1` from the Higgs potential.

## Two. `65`-digit Strong-CP orbit-product cancellation vs fractional-root winding integers (`E2`)

- **Exact `Delta_{P_d} = +1` on the `2 Re(tau)` in `Z` lattice (`recomputed independently` via `B1945` scalar dot products):** Both `3 x 3` matrix determinants and zero-matrix `B1945` scalar products prove `|Delta_{P_d} minus 1| < ten to the minus forty-five` across all `d` in `{2, 3, 5, 6, 7}` at `16 + 8 i` (`m = 40`, `Re = 16` in `Z`, where single-line `Im det[G_u, G_d] != 0` at `(1 / 5, 2 / 5)`!) and at Mostow `4 i / sqrt(3)` (`Re = 0`), whereas off-lattice `m = 8` (`(16 + 8 i) / 5`) and `(13 / 100) + 8 i` break `|Delta_{P_5} minus 1| > 1` (`Plant 1 caught`).
- **Honest quantized winding & negative-real branch-cut disclosure (`Guardrail two` & `six`):** At `16 + 8 i`, off-cut complex phases wind by `W_cpx = (0, minus 2, +3, minus 2, +1)` across `(P_2, P_3, P_5, P_6, P_7)` while `N_neg = (0, 0, 4, 0, 2)` points (`Always Even`, so `(minus 1)^N_neg = +1`!) have `det(Y_u Y_d) < 0` with `Im = 0` (`catching raw floating-point arg's +-pi branch-cut noise that gave +4 in E2's hand-estimate`), giving canonical principal-branch windings `W_prin = W_cpx + N_neg / 2 = (0, minus 2, +5, minus 2, +2)` (`leaving 2 pi W_prin / |P_d| != 0`, `Plant 4`, unless paired by modulus/branch; at Mostow `Re = 0`, `W_cpx = 0`).

## Three. `SU(3)` special-unitary invariance vs `U(1)_A` axial phase shift (`E3`, Guardrail three)

- **`SU(3)^3` invariance:** Across `15` Cayley and `10` Householder `SU(3)` (`det = +1`) scramblings, `arg det(Y_u Y_d)` and `Im det[G_u, G_d]` are invariant to `< ten to the minus forty-five`, whereas `U_R = diag(i, 1, 1)` (`det = i != 1`, `Plant 2a`) shifts `arg det` by exact `pi / 2`.

## Four. Verification recipe for `main`

- Run `shasum -a 256 -c relays/agy_2026-11-21_c11/SCRIPT_SHA256.txt`, `PYTHONDONTWRITEBYTECODE=1 python3 relays/agy_2026-11-21_c11/c11_radiative_higgs_and_strong_cp.py`, and `PYTHONDONTWRITEBYTECODE=1 python3 relays/agy_2026-11-21_c11/c11_countercheck.py`.

0 of 19.
