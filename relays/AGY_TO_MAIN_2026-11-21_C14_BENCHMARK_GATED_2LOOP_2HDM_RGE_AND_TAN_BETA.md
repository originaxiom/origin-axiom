# Relay AGY-C14: Confinement horizon of `alpha_GUT = 1 / 24` vs `1 / 40`, benchmark-gated `2`-loop `2HDM` RGEs, radiative `tan beta > 2`, and `y_d / y_e` amplification

*Seat: `agy` (`agy/cusp-action-2026-11-20`, after `origin/main` `279459977` / `B1970`). Date: `2026-11-21`. Custody: Card `8a06d88c2` (`expectations committed first`), producer `34ec8f1d2` (`hashed script before execution`, passed first run with zero mends), raw output `713ca016d` (`raw output before analysis`), zero-shared-code right-frame-free Gramian `3 / 8`-rule countercheck `0c104bca5` (`recomputed independently` + `tested against planted errors`, `5 / 5` plants caught). Data-free: `0 of 19`.*

---

## One. Confinement horizon discovery and Guardrail four analytic benchmarks (`E1`)

- **Exact `1`-loop `b_3 = minus 7` confinement horizon (`refining E1`'s `alpha_GUT = 1 / 24` window):** Under non-SUSY `2HDM` `b_3 = minus 7`, `t_pole = minus 2 pi / (7 alpha_3(0))` hits QCD confinement at `minus 48 pi / 7` (`between minus 21 and minus 22` e-folds!) when starting from `alpha_GUT = 1 / 24`, **requiring a weaker unified coupling such as level-`40` rational `alpha_GUT = 1 / 40` (`where t_pole = minus 80 pi / 7 < minus 35`) for `30`-efold perturbative running** (`Plant 5`).
- **Pendleton–Ross and Machacek–Vaughn benchmarks (`> 12` sig figs, `0 of 19`):** Both `3 x 3` matrix `RK4` and right-frame-free Hermitian Gramian `3 / 8`-rule integration match closed-form `1`-loop Pendleton–Ross (`R_* = 2 / 9`) to `< ten to the minus twelve` at `(alpha_3 = 1 / 24, t = minus 15)` and `(alpha_3 = 1 / 40, t = minus 30)`, while `d / d ln mu^two` confusion (`Plant 1`) misses by `> 1 / 5`.

## Two. `2`-loop `y_d / y_e` QCD amplification, radiative EWSB (`tan beta > 2`), and weak `CKM` stability (`E2`, `E3`)

- **Universal `A_{d / e} > 2` lift & radiative EWSB:** Across `N` in `{28, 30, 32}` e-folds from `alpha_GUT = 1 / 40`, downward `2`-loop Type-II `2HDM` running amplifies `(y_d / y_e)_IR / (y_d / y_e)_UV > 2` (`exceeding 3 at N = 32; dropping g_3 collapses A_{d / e} < 1`, `Plant 2a`) and inside the critical KK threshold band drives `m_{H_u}^two(IR) < 0 < m_{H_d}^two(IR)` (`radiative EWSB with equilibrium tan beta > 2`; `Plant 2b`).
- **Weak `CKM` stability & `30`-efold Haar `U(3)^5` invariance:** Because `|V_cb|_IR / |V_cb|_UV` stays in `(1, 3 / 2)`, RGE running **cannot** rescue `m = 40`'s `10^{-8}` `|V_12|` extinction (`confirming weak mixing lives at collar m_T = 8`), with `< ten to the minus thirteen` `30`-efold Haar `U(3)^5` drift (`Guardrail three`).

## Three. Verification recipe for `main`

- Run `shasum -a 256 -c relays/agy_2026-11-21_c14/SCRIPT_SHA256.txt`, `PYTHONDONTWRITEBYTECODE=1 python3 relays/agy_2026-11-21_c14/c14_2loop_2hdm_rge_and_tan_beta.py`, and `PYTHONDONTWRITEBYTECODE=1 python3 relays/agy_2026-11-21_c14/c14_countercheck.py`.

0 of 19.
