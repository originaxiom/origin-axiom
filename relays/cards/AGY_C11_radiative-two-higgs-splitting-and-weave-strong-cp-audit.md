# Card AGY-C11: Radiative two-Higgs mass-squared splitting (`tan beta > 1` tilt, mod-`6` `t = 4` neutrality, and `y_t / y_b` unification) and `65`-digit Strong-CP orbit-product audit

*Seat: `agy` (`agy/cusp-action-2026-11-20`, after `origin/main` `279459977` / `B1970`). Date: `2026-11-21`. Pre-registered before any script or run (`expectations committed first`). Data-free: `0 of 19`.*

---

## One. Package and question

In `B1970`, `(H_u, H_d)` sit symmetrically inside one `10` of `SO(10)` (`leaving tan beta = v_u / v_d and cross-sector y_{u 3} / y_{d 3}, y_{d 3} / y_{e 3} open`), while `CP`-breaking vacua `m * tau_*^+` raise Strong-CP `theta_bar_QCD = arg det(Y_u Y_d)`. Does `1`-loop radiative `Delta Y^two = 3 tr(G_u minus G_d) + tr(G_nu minus G_e)` tilt `m_{H_u}^two < m_{H_d}^two` (`tan beta > 1`), how does `t = 4` behave, and does `m = 40` (`16 + 8 i`, `Re` in `Z`) drive `Delta_{P_d} = prod_{w in P_d} det(Y_u Y_d) / |det(Y_u Y_d)| -> +1` while keeping single-line `J_CP != 0`?

## Two. Deliverables and what done means

- Symbolic `sympy` and `65`-digit `mpmath` proof of **Mod-`6` Radiative Higgs Neutrality on `t = 4`** (`G_u == G_d` and `G_nu == G_e` identically across all `35` points of `P_2 (+) P_3 (+) P_6`, so `Delta Y^two = 0` to `< ten to the minus sixty`), paired with `P_5` (`t = 3`) evaluation of `Delta Y^two > 0` and cross-sector geometric ratios `(y_{u 3} / y_{d 3}, y_{d 3} / y_{e 3}, y_{nu 3} / y_{u 3})` across `m` in `{8, 16, 40}`.
- `65`-digit audit of the orbit Strong-CP product `Delta_{P_d}(tau)` and integer branch-winding numbers `W_d = (sum_{w in P_d} arg det(Y_u Y_d)) / (2 pi)` across `P_2, P_3, P_5, P_6, P_7` at `16 + 8 i` (`m = 40`), `(16 + 8 i) / 5` (`m = 8`), and `(13 / 100) + 8 i`, enforcing Guardrail two (`explicit matrix determinants`) and Guardrail three (`SU(3)` special-unitary invariance vs illegal `U(1)` axial phase shift).
- Zero-shared-code independent countercheck (`recomputed independently` + `tested against planted errors`, `5 / 5` plants) and mask-clean result relay.

## Three. Pre-committed expectations and how it could come out wrong

- **E1 (Radiative `m_{H_u}^two < m_{H_d}^two` tilt from `t = 3` & exact `t = 4` neutrality):** On `P_2 (+) P_3 (+) P_6` (`t = 4` overtone), `0 == +6 mod 6` forces `||G_nu(w) minus G_e(w)|| = 0` alongside `||G_u(w) minus G_d(w)|| = 0`, giving **exact `Delta Y^two = 0`** (`while shifting geom(y_{d 3} / y_{e 3}) < 1`), whereas `P_5` (`t = 3`) gives **strict `Delta Y^two > 0`** across all `m` in `{8, 16, 40}` (`driving m_{H_u}^two < m_{H_d}^two -> tan beta > 1`, which is required since intrinsic `geom(y_{u 3} / y_{d 3})` at `tan beta = 1` stays near `1`, `< 6 / 5`).
- **E2 (Exact `Delta_{P_d} = +1` orbit product at `m = 40` vs fractional-root winding `W_d`):** Because `m = 40` maps `Re(40 tau_*^+) = 16` into `Z` (`unlike m = 8`), `|Delta_{P_d}(16 + 8 i) minus 1|` must vanish to `< ten to the minus forty-five` across `d` in `{2, 3, 5, 6, 7}` (`while single-line Im det[G_u, G_d] != 0` at `(1 / 5, 2 / 5)`!). Under `1 / |P_d|` fractional roots, integers `W_d` (`W_5 = +4, W_3 = minus 2`) leave quantized `2 pi W_d / |P_d|` phases unless read via real modulus, whereas at `m = 8` even `|Delta_{P_d} minus 1| > 3 / 10`.
- **E3 (`SU(3)` invariance of `det(Y_u Y_d)` vs `U(1)_A` axial shift):** `arg det(Y_u Y_d)` must be invariant to `< ten to the minus forty-five` under independent `SU(3)_{L, q} x SU(3)_{u_R} x SU(3)_{d_R}` (`det = +1`) rotations (`Guardrail three`).

## Four. Premises and firewall boundaries

- Rests on `B1970` and `AGY-C5` through `AGY-C10`; Guardrails one through six enforced (`zero literal zero assignments on theta_bar_QCD`).
- Must **never** read, compute, or compare any of the nineteen empirical Standard Model targets (`0 of 19`), and must leave `origin/agy/audit-2026-11-02` untouched at `4319f47e2`.

## Five. Mandatory planted negative control

1. **Off-lattice `Re(tau)` Strong-CP plant:** Shift `16 + 8 i` to `(13 / 100) + 8 i` (`or m = 8 at 16 / 5 + 8 / 5 i`): `|Delta_{P_5} minus 1|` must jump from `< ten to the minus forty-five` to `> 1` (`catching loss of CP-lattice product cancellation`).
2. **Axial `U(1)` phase plant & `P_6` charge-perturbation plant:** Apply `U_R = diag(i, 1, 1)` (`det = i != 1`) to `Y_u` (`shifting arg det(Y_u Y_d) by pi / 2`) and perturb `q_{R, nu} = 0 -> 1` on `P_6` (`breaking ||G_nu minus G_e|| = 0` and `Delta Y^two = 0`).

## Six. What is needed from main or other seats

Nothing needed to run; completes the four-card Phase I + II blind closure sequence (`AGY-C8` to `AGY-C11`) on `agy/cusp-action-2026-11-20`.

0 of 19.
