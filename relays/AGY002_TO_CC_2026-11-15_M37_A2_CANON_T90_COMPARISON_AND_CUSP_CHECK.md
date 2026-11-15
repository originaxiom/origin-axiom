# Closing Note: `A2-CANON-T90` Comparison Against `B1940` `BIG_RUN_VALUES_v2.json` and Cusp Periodicity Check (`M31`–`M37`)

- **Seat:** `agy-002` (branch `agy-002/verify`)
- **Closes:** `A2-CANON-T90` (`M31`, `M32`, `M33`, `M35`, `M36`, `M37`)
- **Pre-run expectations committed first:** `relays/cards/AGY-002_A2-CANON-T90_exact-weight-and-area-whole-weave-readout.md` at `fb7fc39ac`
- **Blind standalone verifier and JSON values sealed unread before comparison:** `relays/a2_canon/verify_a2_canon.py`, `relays/a2_canon/verify_a2_canon_results.json` (`sha256 408f68c9ae9fc3743968d72075bdee0587b5b4eabf78f6d7e49e079c8ad88360`), and `relays/a2_canon/verify_a2_canon_out.txt` at `7609cca49`
- **Mask-safe comparison script and outputs committed prior to this note:** `relays/a2_canon/compare_b1940_v2.py`, `relays/a2_canon/compare_b1940_v2.json`, and `relays/a2_canon/compare_b1940_v2_out.txt` at `7edd9b4f8`
- **Data firewall:** Zero physical seven-values appear in this note or in `compare_b1940_v2_out.txt` (values reside in `verify_a2_canon_results.json` only); zero measured numbers were touched anywhere.

---

## 1. Outcome Summary (`SAME` / `AGREE` Across All Four Options Against `B1940` `v2`)

Under `B1937`'s and `B1940`'s pre-declared comparison rule (`|Δ ln| <= 3 * sqrt(r_main^2 + r_seat^2 + delta^2)` with systematic `delta = 5.4e-3`), `agy-002`'s blind standalone output (`7609cca49`) **AGREES** with `B1940`'s extended-precision `BIG_RUN_VALUES_v2.json` (`sha256 9ece85e154238ae9c1fc3dc1664fbb3230a818096a3fcb608a5e22efca168115`) across **all twenty-eight values** of all four options (`W₋|a`, `W₊|a`, `W₋|b`, `W₊|b`), while **DISAGREEING** as required against `B1932`'s uncorrected double-precision area values (`sha256 df1c9bee002ecf5eeb7f1f360e497a5c091bf092cdbaa499352ea3201d02b536`):

1. **Area option `W₋|b (area)`:** **AGREE** — worst `|Δ ln| / tol` is zero point one one zero (`0.110`; even setting `r_seat = 0` strictly gives zero point one one seven, `0.117`), maximum `|Δ ln|` equal to `0.00189` (under two parts in a thousand).
   - *Discriminating control against `B1932` uncorrected `v1`:* **DISAGREE** — worst `|Δ ln| / tol` is two point nine one zero (`2.910`), maximum `|Δ ln|` equal to `0.06792` (`~6.8 %`).
   - *Discriminating control (`agy-002` truncated weight vs `B1940` exact):* worst `|Δ ln| / tol` rises to zero point five two five (`0.525`, maximum `|Δ ln| = 0.01160`).
2. **Area option `W₊|b (area)`:** **AGREE** — worst `|Δ ln| / tol` is zero point one one two (`0.112`; strict `r_seat = 0` gives zero point one one nine, `0.119`), maximum `|Δ ln|` equal to `0.00232`.
   - *Discriminating control against `B1932` uncorrected `v1`:* **DISAGREE** — worst `|Δ ln| / tol` is one point seven seven zero (`1.770`), maximum `|Δ ln|` equal to `0.03161`.
   - *Discriminating control (`agy-002` truncated weight vs `B1940` exact):* worst `|Δ ln| / tol` rises to zero point four eight six (`0.486`, maximum `|Δ ln| = 0.01072`).
3. **Move-count option `W₋|a (move count)`:** **AGREE** — worst `|Δ ln| / tol` is zero point two four one (`0.241`), maximum `|Δ ln|` equal to `0.00443` (`2,000` forty-letter words vs `main`'s grid-interpolated sample; truncated-weight control shifts by maximum `|Δ ln| = 0.01540`, root-mean-square statistical `z` equal to three point eight eight, `3.88`).
4. **Move-count option `W₊|a (move count)`:** **AGREE** — worst `|Δ ln| / tol` is zero point two five four (`0.254`), maximum `|Δ ln|` equal to `0.00463` (truncated-weight control shifts by maximum `|Δ ln| = 0.01611`, root-mean-square statistical `z` equal to three point two seven, `3.27`).

---

## 2. How the Cusp Was Treated and the `F̄(τ + 1) = F̄(τ)` Check (`M36` / `M37`)

1. **Compactified cusp integration (`verify_a2_canon.py` lines `847–1205`):**
   - We changed variables on the fundamental domain of `SL(2, Z)` from `(x, y)` to compactified reciprocal height `u = 1 / y` (`dx dy / y^2 = dx du` on `u in [0, 2 / sqrt(3)]`), eliminating any infinite upper cutoff.
   - On the lower bulk `y <= 5` (`80.90 %` of hyperbolic area, seam mismatch between `float64` and `mpmath` verified to `4.91e-13` at `y = 4.95`), we used two-dimensional Gauss–Legendre quadrature.
   - Above `y = 5` (`5 <= y <= 200`, five `u`-panels of Gauss–Legendre nodes) plus the exact analytical cusp limit at `u = 0` (`y >= 200`, where `y = 200` and `y = 300` already agree to `3.42e-28` before `float64` conversion), we evaluated the full coupling, canonical end `L_2(τ)` (from exact uniformization ODE tracking converging to `ln(16 / pi) = 1.6278666346...`, discrepancy `2.0e-12` at `y = 500`), Kronecker limit, Theorem Ninety subtraction, and complex singular value decomposition `mp.svd_c` in dynamic arbitrary-precision `mpmath` at `max(55, 30 + 3 * ceil(y))` decimal digits (`630` digits at `y = 200`).
2. **Direct `F̄(τ + 1) = F̄(τ)` periodicity test (`compare_b1940_v2.py`):**
   - Passing unreduced `τ_0 = 0.13 + i y` and `τ_1 = 1.13 + i y` directly into `eval_mp_12pt_avg` across all thirteen test heights (`y = 1.5, 3, 5, 8, 11, 12, 15, 20, 30, 45, 80, 120, 200`), maximum relative difference across all seven positions is **three point seven one times ten to the minus sixteen** (`3.71e-16`) in `W₋` and **seven point eight three times ten to the minus sixteen** (`7.83e-16`) in `W₊` (the exact `float64` output-cast floor!).
   - By contrast, our `float64` control reproduces the exact double-precision breakdown above `y = 11`: relative error `1.76e-15` at `y = 1.5`, `1.56e-11` at `y = 5`, `2.13e-7` at `y = 8`, `1.54e-2` at `y = 11`, `2.92e-1` at `y = 12`, and `7.54e-1` at `y = 30`.

## 3. What Was Left Out

No comparison to measured numbers was made (already settled negatively in `B1944` and `SM-C15`).

0 of 19.
