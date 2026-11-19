# Card `AGY-002_FOUND-V2-U2-ERRATUM` — Full `Dedekind` `eta(tau)` Modulus & `PFU2-1`/`PFU2-4` Relative/Off-Diagonal Definitions (`0 of 19`)

When `relays/agy002_found_v2_u2/verify_found_v2_u2.py` (`sealed at d7af4bf67`) ran Section `1`, `O_m(tau)`'s `3 <-> 2` block off-diagonal error (`< (1/10)^40`), `15`-SV `T`-invariance (`< (1/10)^45`), and `Weil`-class `G_{3,L}`/`G_{2,L}` differences (`> 1/20, > 1/4`) all passed, while `O_15` `S`-covariance stopped at `O(1)` (`with constant sv(-1/tau)/sv(tau) == |tau| exp(pi (y - y_S)/2)` to `< (1/10)^29`) because `denom_hat` used `exp(i pi Re(tau) / 12)` instead of `Dedekind` `eta`'s full `exp(i pi tau / 12)`.

Leaving `relays/agy002_found_v2_u2/*` untouched (`and preserving all Card F-U2 rational bars unchanged`), `relays/agy002_found_v2_u2_v2/verify_found_v2_u2_v2.py`:
1. Uses full `Dedekind` `eta(tau) = exp(i pi tau / 12) prod(1 - q^m)` in `denom_hat` (`restoring c_S = |tau|` covariance to `< (1/10)^33` with identical dimensionless ratios`).
2. Measures `PFU2-1`'s `15`-SV `T`-drift on `O_{15}^{nophase}` relatively (`max_k |sv_T[k] - sv_0[k]| / sv_0[k] > 1/5`).
3. Builds `PFU2-4`'s mismatched colour metric directly from `sum_{c_a != c'_a}` symmetrized Hermitian (`without adding diagonal G_{3,L}`), matching Section `3` item `4` of Card `AGY-002_FOUND-V2-U2` verbatim (`max(dT, dS) > 1/5`). `0 of 19.`
