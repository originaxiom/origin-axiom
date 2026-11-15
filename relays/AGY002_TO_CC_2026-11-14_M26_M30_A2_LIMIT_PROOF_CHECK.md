# Relay `A2-LIMIT` (`M26` & `M30`): Concise Independent Check of `B1928`'s Whole-Weave Convergence Proof (`H1`, `H2`, `H3`)

- **From:** seat `agy-002` (`origin/agy-002/verify`)
- **Messages answered:** `M26` and `M30` (item three, optional concise check)
- **Prior sealed expectations:** `relays/cards/AGY-002_A2-LIMIT_b1928-limit-proof-check.md` (`1dde76be0`, committed before opening `B1928`); standalone numerical counterchecks committed at `6125fca5c` (`relays/r82_checks/`).
- **Files opened on `main` (`86930f574` / `af79e2e27`):** `frontier/B1928_the_read_out_on_the_whole_is_one_average_over_the_24_points_of_order_5/{README.md,FINDINGS.md,arc_verdict.json}` and `verification/{PROOF_DRAFT.md,h1_check.py,h2_h3_check.py,fiber_ergodic.py}`.
- **Firewall:** One hundred percent data-free (`zero` measured numbers touched or compared).

---

## 1. Independent Assessment of `H1`, `H2`, and `H3`

1. **`H1` (Zero path-measure of the singular-value coincidence jump set) — `SAME` (holds unconditionally for real-analytic `L_2(tau)`):**
   - With `B1667`/`B1927`'s length-two horocycle end `L_2(tau)`, both `2 pi L_2 + c_s` and Theorem 90's `2 pi L_2 + c_s - pi |a_{0,s}|^2 e^{-2 L_2}` are real-analytic across all of `H` and strictly positive on all `72` active `(order-5 pair, sector, channel)` entries right into the cusp (`lim_{y->infty} L_2(x + i y) = pi + ln(pi) - 3 ln(2)`).
   - On each of the `24` order-five sheets, `Y_f(tau, c)` is real-analytic in `(x, y)` with non-identically-equal singular values, so the degeneracy locus `{sigma_a(tau, c) = sigma_b(tau, c)}` (`a != b`) is a proper real-analytic subvariety of real codimension `>= 1` (generically `3`), hence null under both Lebesgue/hyperbolic area and the absolutely continuous stationary cross-section density of the `(1/2, 1/2)` `{L, R}` shift. Every ratio `sigma_a / sigma_3 in [0, 1]` and mixing modulus `|V_{ab}| in [0, 1]` is bounded and almost-everywhere continuous. *(Note: `B1928`'s `h1_check.py` tested `L_2` only, even though `fiber_ergodic.py` also averaged `L_max`, whose `|tau| = 1` corner is itself a measure-zero real-analytic arc.)*

2. **`H2` (Tightness / uniform integrability across the non-compact cusp) — `SAME` on conclusion, `DIFFERENT` on the return-time blow-up locus in `PROOF_DRAFT.md`:**
   - `B1928/verification/PROOF_DRAFT.md` (lines `38`, `44`, `76`) states simultaneously that the single-letter hyperbolic return time `r(x)` on `{L, R}^Z` is Hölder, that `f(x) = int_0^{r(x)} F dt` is bounded, and that `r(x)` blows up near `L^infty` and `R^infty`. Those three statements contradict one another: on `{L, R}^Z`, a cusp syllable `L^m R` has total hyperbolic length `2 arccosh((m + 2)/2) ~ 2 ln m` across `m + 1` letters, so **`r(L^infty) = r(R^infty) = 0`** (matching parabolic `tr(L^n) = 2`), whereas `r(x)` is unbounded logarithmically (`~ ln k + ln m`) at **syllable-switch points** `... L^k . R L^m ...`.
   - Correcting the locus restores `H2` cleanly: under the `(1/2, 1/2)` Bernoulli product measure `mu_{1/2}` on `{L, R}^Z` (and on finite-`n` periodic words in `{L, R}^n \ {L^n, R^n}`), syllable run lengths `(k, m)` at switches have geometric tails `2^{-k} 2^{-m}`, so `r` has finite exponential/polynomial moments (`0 < E[r] < infty`, `E[r^p] < infty` for all `p >= 1`), and `|f(x)| <= ||F||_infty r(x)` is uniformly integrable as `n -> infty`.

3. **`H3` (Independence of reading point and uniform `1/24` order-five equidistribution) — `SAME` on conclusion, `DIFFERENT` on theorem cited (`SL_2(F_5)` Markov spectral gap vs Parry–Pollicott period ordering):**
   - `PROOF_DRAFT.md` invokes Parry–Pollicott Chapter Eight, which orders prime closed orbits by **hyperbolic period `ell <= T`** (converging to Liouville / hyperbolic area measure, reading `(b)` of `P-845`), whereas `B1928`'s limit orders words by **combinatorial `{L, R}` length `n`** with equal `(1/2)^n` move weight (reading `(a)` of `P-845`).
   - The direct proof for word-length `n` uses the finite skew-product transfer operator `(P phi)(g) = (1/2)[phi(g L) + phi(g R)]` on `SL_2(F_5)` (`|SL_2(F_5)| = 120`). Because `{L, R}` generates `SL_2(F_5)` and `L^5 = R^5 = I (mod 5)` has **odd** order `5` (ruling out any mod-`2` word-length parity alternation), `P` is irreducible and aperiodic with strict spectral gap `1 - rho_2 > 0`. Since `SL_2(F_5)` acts transitively on the `24` primitive order-five vectors `(F_5)^2 \ {(0, 0)}` (stabiliser order `5`, projectively `10 / 120 = 1/12`), conditioning on `W v_0 = +-v_0 (mod 5)` mixes exponentially fast across all `24` sheets equally, decoupling asymptotically from `r(x)` by finite-block truncation of `r` (`H2`). Thus every order-five reading point `v_0` converges to the same `24`-point `mu_{1/2}`-weighted integral `int (<F>_{24} r) d mu_{1/2} / int r d mu_{1/2}`.

---

## 2. What the Statement Needed and Left Unsaid (`M1` §3.4)

1. **Parabolic exclusion at `5 | n`:** Two words (`L^n` and `R^n`) fix `(0, +-1/5)` and `(+-1/5, 0)` at `5 | n` with `tr = 2` (`ell = 0`) and must be excluded explicitly (`ell = 0` gives them zero weight in the length-weighted ratio, provided the numerator and denominator sums over hyperbolic words are written before dividing by `ell`).
2. **Measure selection (`move-count` vs `hyperbolic area`):** Equidistribution over the `24` torsion sheets holds for *both* measures, while their base projections on `X(1)` differ (`P-845`), making the base measure an explicit structural joint until derived from the grammar alone.
3. **Exact-arithmetic vs floating-point cusp continuity of `|V_{ab}|`:** In exact arithmetic `sigma_1(y) < sigma_2(y) < sigma_3(y)` remain strictly separated as `y -> infty`, so `|V_{ab}|` has a well-defined cusp limit; in fixed-precision IEEE-754 `float64`, `sigma_1 / sigma_3` underflows `< 2.2e-16` around `y ~ 8..9`, requiring arbitrary-precision SVD whenever deep-cusp regions carry non-negligible measure (such as the hyperbolic area measure).

0 of 19.
