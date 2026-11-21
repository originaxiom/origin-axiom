# Card AGY-C14: Benchmark-gated `2`-loop `2HDM` matrix RGEs, radiative electroweak symmetry breaking, and quantitative `tan beta` / `y_d / y_e` amplification

*Seat: `agy` (`agy/cusp-action-2026-11-20`, after `origin/main` `279459977` / `B1970`). Date: `2026-11-21`. Pre-registered before any script or run (`expectations committed first`). Data-free: `0 of 19`.*

---

## One. Package and question

Cards `AGY-C11` and `AGY-C12` showed that **(a)** intrinsic `tan beta = 1` `y_{u 3} / y_{d 3}` stays near `1` (`< 6 / 5`), requiring quantitative radiative `tan beta = v_u / v_d > 1` from `m_{H_u}^two(\mu)` vs `m_{H_d}^two(\mu)`, and **(b)** uniform `H^3` radial smearing cannot steepen hierarchies beyond `y_eff` (`Ky Fan convexity`), placing downward `2`-loop gauge + Yukawa running squarely at the center of `y_d / y_e` (`Georgi–Jarlskog`) and `|V_cb|` evolution. How do `2`-loop Type-II `2HDM` RGEs transform the UV cusp weave across `N` e-folds?

## Two. Deliverables and what done means

- **Guardrail four synthetic analytic benchmark gate (`0 of 19`):** Verify the `4`-th order Runge–Kutta / Dormand–Prince matrix RGE integrator (`checking d / d ln mu` vs `16 pi^two` and `(16 pi^two)^two` factors) to `< ten to the minus ten` (`> 10` sig figs, exceeding Guardrail four's `3` sig figs) against **(i)** the exact closed-form `1`-loop Pendleton–Ross Bernoulli analytic solution from synthetic rational inputs `(alpha_3(0) = 1 / 24, y_t(0) = 1)` and **(ii)** `2`-loop Machacek–Vaughn pure-gauge Casimir asymptotic integration over `Delta ln mu = minus 30` (`Guardrail five dimensionless log-ratio, zero GeV anchors`).
- Downward `2`-loop Type-II (`holomorphic (S, S, S)`) matrix RGE integration of `(g_1, g_2, g_3, Y_u, Y_d, Y_e, Y_nu, m_{H_u}^two, m_{H_d}^two)` from symmetric UV boundary `(alpha_GUT = 1 / 24, m_{H_u}^two = m_{H_d}^two = m_0^two)` across `N_efolds` in `{25, 30, 35}`, measuring **(a)** radiative `m_{H_u}^two < 0 < m_{H_d}^two` EWSB / equilibrium `tan beta`, **(b)** QCD/EW amplification `(y_{d k} / y_{e k})_IR / (y_{d k} / y_{e k})_UV` (`testing whether factor > 2 lifts b/tau and s/mu`), and **(c)** RGE rescaling of `|V_cb|, |V_ub|` and intra-family ratios.
- Zero-shared-code independent countercheck (`recomputed independently` + `tested against planted errors`, `5 / 5` plants) and mask-clean result relay.

## Three. Pre-committed expectations and how it could come out wrong

- **E1 (Guardrail four analytic benchmark reproduction):** The matrix RGE integrator must match the closed-form `1`-loop Pendleton–Ross analytic ratio `y_t(t)^two / g_3(t)^two` to `< ten to the minus ten` across `Delta ln mu = minus 30`, whereas confusing `d / d ln mu` with `d / d ln mu^two` (`factor of 2 error`) must miss the benchmark by `> 1 / 5`.
- **E2 (Radiative EWSB & `y_d / y_e` QCD amplification vs weak CKM running):** Downward `2`-loop running from `alpha_GUT = 1 / 24` over `30` e-folds amplifies `y_d / y_e` by a universal QCD/hypercharge factor `> 2` (`lifting b/tau and down/lepton scale`), drives `m_{H_u}^two(\mu_IR) < m_{H_d}^two(\mu_IR)` (`triggering radiative m_{H_u}^two < 0 EWSB above critical UV Yukawa normalization and yielding tan beta > 2`), while `|V_cb|_IR / |V_cb|_UV` shifts by only an `O(1)` factor (`< 3 / 2`, proving RGE running **cannot** rescue `m = 40`'s `10^{-8}` `|V_12|` collapse — locking weak mixing to the `m_T = 8` collar!).
- **E3 (Basis-covariant matrix RGE flow):** Scrambling UV `(Y_u, Y_d, Y_e, Y_nu)` by random `U(3)^5` unitaries before `30`-efold `2`-loop integration must leave all IR singular values and CKM moduli invariant to `< ten to the minus twelve`.

## Four. Premises and firewall boundaries

- Rests on `AGY-C2` (`(n_H, n_T) = (2, 0)`), `AGY-C11`, and `AGY-C12`; Guardrails one through six strictly enforced (`synthetic rational UV inputs only`).
- Must **never** read, compute, or compare any of the nineteen empirical Standard Model targets (`0 of 19`), and must leave `origin/agy/audit-2026-11-02` untouched at `4319f47e2`.

## Five. Mandatory planted negative control

1. **`d / d ln mu^two` variable-confusion plant (`Guardrail four`):** Multiply beta functions by `1 / 2`: must fail the closed-form Pendleton–Ross benchmark by `> 1 / 5`.
2. **Dropped `SU(3)_c` anomalous dimension & flipped `2HDM` Higgs-coupling plants:** Set `g_3 -> 0` in `beta_{Y_d}` (`collapsing y_d / y_e amplification below 1`) and swap `H_u <-> H_d` (`reversing m_{H_u}^two > m_{H_d}^two`).

## Six. What is needed from main or other seats

Nothing needed to run; establishes the benchmark-gated `UV -> IR` matrix RGE bridge (`0 of 19`).

0 of 19.
