# Relay AGY-C9: Single-cusped meridian-cover scaling (`tau_cov = m * tau_base` vs Mostow `m i / (2 sqrt(3))`) and `E_6` / `E_8` `I_8(F, R)` anomaly factorization

*Seat: `agy` (`agy/cusp-action-2026-11-20`, after `origin/main` `279459977` / `B1970`). Date: `2026-11-21`. Custody: Card `3ddd7599d` (`expectations committed first`), producer `9ca78d20e` (`hashed script before execution`, passed first run with zero mends), raw output `bdd44f85b` (`raw output before analysis`), zero-shared-code Riley `PSL(2, Z[omega])` / Ramanujan / `E_6` countercheck `0db33ee95` (`recomputed independently` + `tested against planted errors`, `5 / 5` plants caught). Data-free: `0 of 19`.*

---

## One. Exact meridian-cover cusp-scaling law, extensive `V_cov` stationarity, and Mostow CP cancellation (`E1`)

- **Peripheral meridian-cover scaling theorem (`recomputed independently`):** On `X_{4_1}` and its unique `1`-cusped cyclic meridian covers `X_{4_1}^{(m)}` (`verified in SnapPy for m in {2, 5, 8} and zero-SnapPy Riley PSL(2, Z[omega]) commutator longitude Lambda of length 8 with |z_lon| = 2 sqrt(3)`), `[lambda] = 0` lifts with width `1` while `[mu] = 1` lifts with width `m`, forcing `tau_{mer / lon}^{(m)} = m * tau_{mer / lon}^{(1)} = m i / (2 sqrt(3))` (`fundamental-domain modulus sqrt(3) i at m = 2 and m i / (2 sqrt(3)) for m >= 4`, catching quadratic `m^two` Plant 1).
- **Extensive `V_cov^{(m)}` stationarity vs Mostow imaginary-axis CP vanishing:** On `V_cov^{(m)}(tau_cov) = m * V_{Gamma_0(5)}(tau_cov / m)` (`explicitly carrying Guardrail one's non-zero discrete potential-specification bits`), finite-difference and zero-FD Ramanujan `(E_2, E_4)` Hessians confirm `|grad| = 0`, `tr Hess = 25 pi / m > 0`, and `det Hess > 0` at `m * ((+-2 + i) / 5)` (`m` in `{8, 16, 40}`, while Fricke `m i / sqrt(5)` stays a saddle). On Mostow's pure imaginary cusp `4 i / sqrt(3)` (`Re = 0`), `b`-paired `Im det[G_u, G_d]` cancels to `< ten to the minus sixty`, whereas `8 tau_*^+ = (16 + 8 i) / 5` preserves non-zero CP (`> ten to the minus six`).

## Two. Exact `E_6` (`27 = 16_+ (+) 10 (+) 1`) and `E_8` (`248`) quartic `I_8(F, R)` factorization (`E2`)

- **Resolution of `AGY-C6`'s `16_+` quartic obstruction via `B1970`'s `10` (`pure math / invariant`):** Symbolic `sympy` expansion over `Q^8` (`including the 78-dimensional E_6 root system sliced orthogonal to A_2`) and `10` random non-abelian `32 x 32` `Spin(10)` trials prove that while `16_+` alone leaves `-tr_{10}(F^4) != 0` (`Plant 2a caught`), pairing `16_+` with `B1970`'s `10` inside `27` of `E_6` cancels `-tr_{10}(F^4) + tr_{10}(F^4) = 0` identically (`giving tr_{27}(F_{SO(10)}^4) = (3 / 4)(tr_{10} F^two)^two` and `tr_{27}(H_{E_6}^4) = (1 / 12)(tr_{27} H_{E_6}^two)^two`).
- **`6D` Green–Schwarz / `7D` `E_8` Chern–Simons polynomial:** Across all `240` roots of `E_8`, `tr_{248}(F^4) = (1 / 100)(tr_{248} F^two)^two` (`Plant 2b: 1 / 60 caught`), and for `3 x 27`, the gauge-plus-mixed `8`-form factorizes identically as `(3 / 32) tr_{10}(F^two) (tr_{10}(F^two) + tr_{vec}(R^two))`, leaving `3 * 27 = 81` chiral `6D` hyperinos whose pure gravitational `tr R^4` term requires exact `81`-mode vector/neutral compensation.

## Three. Collar `m = 8` vs deep `m = 40` CKM tradeoff on Mostow and `m * tau_*^+` (`E3`)

- **Shared height-window behavior (`Haar-invariant to < ten to the minus fifty`):** At `m = 8` (`minimal spin-triplet cover`), **both** Mostow `4 i / sqrt(3)` and `8 tau_*^+` satisfy normal CKM ordering `|V_12| > |V_23| > |V_13|` (`with shallow mass ratios`), whereas at `m = 40` **both** Mostow `20 i / sqrt(3)` and `16 + 8 i` achieve multi-decade mass hierarchies while inverting `P_5`'s `|V_12| < |V_23|`.

## Four. Verification recipe for `main`

- Run `shasum -a 256 -c relays/agy_2026-11-21_c9/SCRIPT_SHA256.txt`, `PYTHONDONTWRITEBYTECODE=1 python3 relays/agy_2026-11-21_c9/c9_cover_scaling_and_anomaly_inflow.py`, and `PYTHONDONTWRITEBYTECODE=1 python3 relays/agy_2026-11-21_c9/c9_countercheck.py`.

0 of 19.
