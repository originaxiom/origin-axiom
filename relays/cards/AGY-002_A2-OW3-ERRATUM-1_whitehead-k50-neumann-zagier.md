# Erratum 1 to Card `A2-OW3` — Extending Whitehead Sequence to `k = 50` for Neumann-Zagier `O(1 / k^2)` Gap Below `1 / 100` (`0 of 19`)

## Disclosed Convergence Rate Observation in Sealed `v1` (`1621a6c47` / `b9338f983`)

In sealed `relays/a2_ow3/verify_a2_ow3.py` (`b9338f983`, preserved untouched), `OW3-B` and `OW3-C` passed completely, and `OW3-A` proved monotonicity and strict boundedness below `4 G` across all three Whitehead accumulation sequences (`b++L^k R`, `b+-L^k R`, `b-+L^k`, `k = 1..25`), with `Vol(b++L^25 R)` within roughly `3 / 100` below `4 G` (matching the classical Neumann-Zagier `O(1 / k^2)` Dehn-filling asymptotic, which crosses `< 1 / 100` around `k = 42`).

## Exact Update for Authoritative `v2` (`relays/a2_ow3_v2/verify_a2_ow3_v2.py`)

- Leave `relays/a2_ow3/` completely untouched.
- Extend the three Whitehead sequences (`b++L^k R`, `b+-L^k R`, `b-+L^k`) to `k = 1..50` (checking monotonicity, strict boundedness below `4 G`, and `|Vol(k = 50) - 4 G| < 1 / 100`, plus reporting the `k^2 * (4 G - Vol(k))` Neumann-Zagier asymptotic coefficient!).
- All pass bars (`< 1 / 100`, `< (1/10)^10`, `< (1/10)^50`, `< (1/10)^12`) remain completely unchanged. `0 of 19.`
