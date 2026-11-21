# Relay AGY-C13: Algebraic `E_8 -> E_6 x SU(3)` bridge for `I-37` (`M_2(Gamma(2))` uniqueness of `D-1` over `B1742`) and `6D` gravitational `tr R^4` audit

*Seat: `agy` (`agy/cusp-action-2026-11-20`, after `origin/main` `279459977` / `B1970`). Date: `2026-11-21`. Custody: Card `c53189f1c` (`expectations committed first`), producer `03fc21a76` (`hashed script before execution`, passed first run with zero mends), raw output `043caf8cf` (`raw output before analysis`), zero-shared-code `Cl(10)` Freudenthal + formal `q^{1 / 8}`-series countercheck `7ca1d4828` (`recomputed independently` + `tested against planted errors`, `5 / 5` plants caught). Data-free: `0 of 19`.*

---

## One. `E_8 -> E_6 x SU(3)_fam` cubic exhibition and `M_2(Gamma(2))` uniqueness of `D-1` (`E1`, `E3`)

- **Explicit `81`-root `(27, 3)` cubic Yukawa census (`recomputed independently` via `Cl(10)` Freudenthal form):** Decomposing `248 = (78, 1) (+) (1, 8) (+) (27, 3) (+) (27_bar, 3_bar)` exhibits `(27, 3) = (16_{minus 1 / 2} (+) 10_{+1} (+) 1_{minus 2}) (x) 3_fam` (`48 + 30 + 3 = 81` roots) with `Spin(10) x SU(3)_fam`-invariant `epsilon_{a b c}` cubic couplings (`< ten to the minus thirteen`). Of the `40` `SO(10)` `10 * 16 * 16` terms, `P_hat` kills all `24` color-triplet proton-decay channels (`Plant 2b`) and retains the exact `16` electroweak channels (`6 Q u^c H_u + 6 Q d^c H_d + 2 L e^c H_d + 2 L nu^c H_u` at `Y(H_u) = +1 / 2, Y(H_d) = minus 1 / 2`).
- **Derivative-free Halphen–Serre identity (`pure math / invariant`):** Symbolic `q^{1 / 8}` power-series expansion and `60`-digit checks prove `24 eta(tau)^3 (c_0, c_1, minus i c_2) = (minus theta_2^two (theta_3^4 + theta_4^4), +theta_4^two (theta_2^4 + theta_3^4), +theta_3^two (theta_2^4 minus theta_4^4))`. Thus `eta(tau) S(tau) = (1 / (2 pi i)) d / d tau (eta r)` has exact modular weight `2` (`while S(tau) itself has exact weight 3 / 2, combining with weight-1 / 2 spinor modes to form weight-2 1-forms`).
- **`S_3` Schur uniqueness (`resolving B1970 H2: D-1 vs B1742`):** Because `(N_0, N_1, N_2)` satisfies `N_0 + N_1 minus N_2 = 0` inside `2`-dimensional `M_2(Gamma(2)) ~= 2_std(S_3)`, `Hom_{S_3}(2_std, M_2(Gamma(2)))` has complex dimension `1` (`Schur's Lemma`), forcing `H_u` and `H_d` to share `S(tau)` (`D-1`), whereas `B1742`'s `F_6` (`wt 3`) and `F_22` (`wt 11`) fail modularity (`Plant 1`).

## Two. Symbolic `6D` `(1, 0)` gravitational `tr R^4` law and pillowcase ledger (`E2`)

- **Exact `273 minus 29 n_T` derivation and `Delta_244` defect:** Symbolic `sympy` expansion of `6D` `A_hat`, spin-`3 / 2` (`+245`), and chiral `B_2` (`+28`) polynomials proves pure `tr R^4` vanishes in `6D` `(1, 0)` supergravity iff `N_H minus N_V + 29 n_T = 273` (`N_H minus N_V = 244` at `n_T = 1`; `Plant 2a`). On `T^2_inf / Z_2`, chiral `3 x 27` (`N_H = 81`) with unbroken `N_V = 12` (`G_SM`) or `14` (`G_SM x U(1)^two`) leaves exact pure-`6D` neutral/twisted requirement `Delta_244 = 175` (`or 177`), unless cancelled directly by `7D` bulk Lorentz Chern–Simons inflow `d Omega_7^LCS(omega) = tr R^4`.

## Three. Verification recipe for `main`

- Run `shasum -a 256 -c relays/agy_2026-11-21_c13/SCRIPT_SHA256.txt`, `PYTHONDONTWRITEBYTECODE=1 python3 relays/agy_2026-11-21_c13/c13_e8_i37_and_6d_grav_anomaly.py`, and `PYTHONDONTWRITEBYTECODE=1 python3 relays/agy_2026-11-21_c13/c13_countercheck.py`.

0 of 19.
