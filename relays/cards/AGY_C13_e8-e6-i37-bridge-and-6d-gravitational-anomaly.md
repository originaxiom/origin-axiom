# Card AGY-C13: Algebraic `E_8 -> E_6 x SU(3)` bridge for `I-37` (`D-1` shared weight-`2` Higgs triplet vs `B1742`) and `6D` pillowcase gravitational `tr R^4` completion

*Seat: `agy` (`agy/cusp-action-2026-11-20`, after `origin/main` `279459977` / `B1970`). Date: `2026-11-21`. Pre-registered before any script or run (`expectations committed first`). Data-free: `0 of 19`.*

---

## One. Package and question

In `B1970` (`origin/main` `279459977`), `I-37` asks for **(a)** exhibiting the frame's quaternion Higgs triplet `S(tau)` as the doublet pair `(H_u, H_d)` of `B1253`'s `10 subset 27` (`resolving H2: shared fibre mode D-1 vs independent directions B1742`), while `AGY-C9` left open **(b)** the `81`-mode pure gravitational `tr R^4` anomaly balance on `T^2_inf / Z_2`. Do `E_8 -> E_6 x SU(3)` Chevalley action + `Gamma(2)` weight-`2` Riemann–Roch force `D-1` and close `6D` `(1, 0)` gravitational anomaly cancellation?

## Two. Deliverables and what done means

- Explicit `248`-dimensional `E_8` root and Chevalley action of `e_6 (+) su(3)_fam` on `(27, 3)` (`81` roots), exhibiting all `40` cubic `SO(10)` Yukawa couplings `(16, 3) x (16, 3) x (10, 3) -> 1` contracted with `epsilon_{a b c}` (`24` color-triplet proton-decay channels killed by `(P_hat, iota_hat)` leaving `16` electroweak channels `(u, d, e, nu)`), plus Riemann–Roch dimension count of `Gamma(2)`-covariant weight-`2` holomorphic quaternion sections `M_2(Gamma(2))` (`dim = 2`, spanned by `theta_2^4, theta_3^4, theta_4^4` subject to Jacobi's identity) proving `S(tau)` is **uniquely locked** inside `(10, 3)` (`earning D-1 over B1742`).
- Exact `6D` `(1, 0)` Green–Schwarz anomaly audit of `I_8(R, F)` for `248` of `E_8` on `T^2_inf / Z_2`: counting untwisted bulk vector multiplets `N_V`, untwisted/cusp hypermultiplets `N_H`, tensor multiplets `n_T`, and the `4` pillowcase `Z_2` fixed points against `N_H minus N_V + 29 n_T = 273`.
- Zero-shared-code independent countercheck (`recomputed independently` + `tested against planted errors`, `5 / 5` plants) and mask-clean result relay.

## Three. Pre-committed expectations and how it could come out wrong

- **E1 (`E_8` cubic action & Riemann–Roch uniqueness of `D-1` over `B1742`):** Inside `248 = (78, 1) (+) (1, 8) (+) (27, 3) (+) (27_bar, 3_bar)`, `(P_hat, iota_hat)` projects `(10, 3)` onto `(H_u (+) H_d) (x) 3_fam` (`0` color triplets). Because a `6D -> 4D` gauge-scalar background `A_z dz` is a weight-`2` holomorphic `1`-form (`dz` has modular weight `2` under `z -> z / (c tau + d)`), `(H_u, H_d)` must lie in `M_2(Gamma(2))_odd`, where Halphen–Serre uniquely selects `S(tau)` (`1` mode per `(i, j, k)` channel, forcing `H_u` and `H_d` to share `S(tau)` up to scalar `v_u / v_d`, whereas `B1742`'s `F_6 | F_22` sits at non-`1`-form weights `3` and `11`).
- **E2 (`6D` `(1, 0)` gravitational `tr R^4` anomaly balance):** For `6D` `(1, 0)` supergravity, pure `tr R^4` vanishes iff `N_H minus N_V + 29 n_T = 273`. With `n_T = 1` (`universal B-field tensor multiplet, leaving 273 minus 29 = 244`), we test the exact `(N_H, N_V)` count of `(P_hat, iota_hat)`-projected `E_8` (`untwisted bulk + 4 pillowcase fixed points`): either twisted pillowcase fixed-point states complete `N_H minus N_V = 244` identically, or an exact integer bulk/fixed-point defect `Delta_244 != 0` is isolated.
- **E3 (`SU(3)_fam x Spin(10)` equivariance):** The `epsilon_{a b c}` cubic tensor on `(27, 3)^3` must be invariant to `< ten to the minus fourteen` under simultaneous `Spin(10) x SU(3)_fam` transformations.

## Four. Premises and firewall boundaries

- Rests on `B1250`, `B1253`, `B1970`, `AGY-C5`, and `AGY-C9`; Guardrails one through six enforced.
- Must **never** read, compute, or compare any of the nineteen empirical Standard Model targets (`0 of 19`), and must leave `origin/agy/audit-2026-11-02` untouched at `4319f47e2`.

## Five. Mandatory planted negative control

1. **Higher-weight modular transformation plant (`B1742` vs `D-1`):** Test `F_6(tau)` and `F_22(tau)` inside the `1`-form `A_z(-1 / tau) d(-z / tau)`: must fail modular invariance (`transforming with weight 3 and 11 instead of weight 2`!).
2. **Wrong `6D` tensor coefficient or dropped color-triplet projection plant:** Perturb `29 n_T -> 28 n_T` in `I_8^grav` (`breaking tr R^4 cancellation`) and drop `(P_hat, iota_hat)` (`restoring 24 baryon-number-violating cubic couplings`).

## Six. What is needed from main or other seats

Nothing needed to run; directly supplies the algebraic exhibition and weight-`2` uniqueness proof for `B1970`'s `I-37` (`H2`).

0 of 19.
