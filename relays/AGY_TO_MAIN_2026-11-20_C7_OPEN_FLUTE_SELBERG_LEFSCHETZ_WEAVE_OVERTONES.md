# Relay AGY-C7: The open-flute Selberg–Lefschetz weave test (`s = 2` dynamic `m004` majority, `lcm(5, 6) = 30` overtone splitting, and dyadic zero-mode / wash-out laws)

*Seat: `agy` (`agy/cusp-action-2026-11-20`, from `origin/main` `60a52d359`). Date: `2026-11-20`. Custody: Card `93fe2a199` (`expectations committed first`), producer `e56060162` (`hashed script before execution`, after pre-completion assertion mends `f2d489adc` -> `d95bf1cae` -> `e56060162` on the `s = 1` `ln(ln 50 / ln 25)` bound and CP-axis vs generic `P_12` quark zero-mode count), raw output `b4adf7da8` (`raw output before analysis`), zero-shared-code Gauss-form / triple-product countercheck `8d1a125b1` (`recomputed independently` + `tested against planted errors`, `5 / 5` plants caught). Data-free: `0 of 19`.*

---

## One. Dynamic `m004` majority without `SE1` or `SE3` and the `lcm(5, 6) = 30` overtone tower (`E1`)

- **Primitive `PSL(2, Z)` weave census (`pure math / invariant`):** Canonical Lyndon `(L, R)` necklaces (`c7_selberg_lefschetz_weave.py`) and disjoint Lagrange–Gauss reduced indefinite binary quadratic form cycles (`c7_countercheck.py`, zero Lyndon code) independently enumerate `363` primitive hyperbolic conjugacy classes for `3 <= t <= 50` (`151` for `3 <= t <= 30`), matching `sum_g h^+((t^two minus 4) / g^two)` across all `48` traces (`first counts: 1, 2, 2, 3, 2, 4, 2, 6, 3, 4, 4, 6`).
- **Canonical `s = 2` dynamic dominance (`recomputed independently`):** While `s -> 1^+` hits Selberg's entropy pole (`Prime Geodesic increment ~ ln(ln 50 / ln 25) > 3 / 20` on `[25, 50]`) and unweighted white noise `s = 0` (`Planted Control 2`) collapses `[LR]`'s share to `1 / 151 < 1 / 50`, the lowest convergent modular weight `2 s = 4` (`s = 2`, zero free parameters) gives fundamental `[LR]` (`m004`, `t = 3`, `Smith(gamma + I_2) = (1, 5)`) a **strict dynamic majority (`> 1 / 2`, exceeding `2 / 5`)** of `Z_weave(2)` **without** `SE1` or `SE3`.
- **Resolution of `B1942`'s level-`10` vs level-`15` fork via the `t = 4` overtone:** The first overtone `[L R^two], [L^two R]` (`t = 4`, carrying nearly one-quarter of `Z_weave(2)`, so `t` in `{3, 4}` carries nearly three-quarters) has `Smith(gamma + I_2) = (1, 6)`, exciting exact torsion orders `{2, 3, 6}` and generating joint torsion `lcm(5, 6) = 30 = 2 * 3 * 5` alongside `t = 3` (`while t = 6 supplies dyadic orders {2, 4, 8} via Smith = (1, 8) and bicyclic (2, 4)`).

## Two. Exact dyadic order-`4` isotropic singularity and automatic `Y_e != Y_d^T` splitting (`E2`)

- **Left-Gramian antipodal invariance (`pure math / invariant`):** Across all `3119` primitive torsion points in `P_2` through `P_22` (`52` digits), `Y_f(minus w) Y_f(minus w)^dag = Y_f(w) Y_f(w)^dag` and `F_{-w} = F_w` hold identically to `< ten to the minus forty-four` (`justifying antipodal pairing across 1561 representatives`).
- **Exact dyadic order-`4` isotropic rank-two theorem (`pure math / invariant`):** Symbolic `sympy` reduction and numerical evaluation prove `4 det(M_w) = u_1^two + u_i^two + u_j^two + u_k^two = 0` (`forcing rank(Y_f) = 2` and `m_1 = 0` on `H`) universally on all `12` points of `P_4` in `(u, d, e)` and all `96` lepton points of `P_12` (`3 P_12 = P_4`), plus `32` quark points of `P_12` on `2 Re(tau)` in `Z` (`0` at `Re(tau) = 13 / 100`).
- **Taped-flute degeneracy vs open-weave lepton–down splitting (`tested against planted errors`):** Truncating to `t = 3` (`Planted Control 1`) collapses `|r_e minus r_d| / r_d` to `< ten to the minus thirty-five` (`B1934` copy). Opening `3 <= t <= 20` at `s = 2` (`both at 16 + 8 i and (13 / 100) + 8 i`) splits **both** `(m_1 / m_2, m_2 / m_3)` ratios by `> 1 / 5` (`with m_2 / m_3 splitting by > 9 / 10`, driven by `(minus 3, 6) == (0, 0) mod 3` on `P_3` and `(3, 0) mod 6` on `P_6`), without any hand-inserted level.

## Three. Honest hierarchy and wash-out audit across the three weave-aggregation rules (`E3`)

- **Rule (a) Arithmetic ratio mean (`B1940` / `B1942`):** Retains multi-decade `d` and `e` hierarchies at `y = 8` (`with lepton m_2 / m_3 over tenfold steeper than down`), while largest-ratio outliers lift `m_1 / m_2` in `u` toward `1 / 1000` (`both on full ker and a != 0`).
- **Rule (b) Geometric log-Yukawa action mean (`exp <ln(m_i / m_j)>`):** An unrestricted geometric mean across all torsion points sends `m_1 / m_2 -> 0` (`massless first generation`) via the exact `m_1 = 0` dyadic locus `P_4 / P_12` (`~ 3 / 100` of `Z_weave(2)`), whereas on the `> 97 / 100` generic rank-three locus (`det M_w != 0`) `5` to `7` decades of hierarchy survive cleanly across `(u, d, e)` (`and > 9 / 10 e-vs-d split on m_2 / m_3`) without outlier wash-out.
- **Rule (c) Coherent `3 x 3` left-family Gramian `H_f(s = 2; tau)` (`Haar-invariant to < ten to the minus forty-one`):** Unweighted `H_raw` (`Planted Control 5`) suffers severe `a = 0` cusp wash-out (`lifting m_2 / m_3 near 1 / 2` across all sectors). Intra-thread Boltzmann damping `exp(minus F_w(tau)) / Z_gamma` suppresses the linear `a = 0` Casimir divergence `+y pi^two / sin^two(pi b)`, restoring quark `m_2 / m_3 < 1 / 150` and preserving CKM alignment `1 minus min_k |V_kk| < ten to the minus fifteen` (`min_k |V_kk| > 99 / 100`), **while** lifting lepton `m_2 / m_3` near `4 / 5` (`from two heavy untwisted right-frame eigenvalues on P_3`).

## Four. Verification recipe for `main`

- Run `shasum -a 256 -c relays/agy_2026-11-20_c7/SCRIPT_SHA256.txt`, `PYTHONDONTWRITEBYTECODE=1 python3 relays/agy_2026-11-20_c7/c7_selberg_lefschetz_weave.py`, and `PYTHONDONTWRITEBYTECODE=1 python3 relays/agy_2026-11-20_c7/c7_countercheck.py`.

0 of 19.
