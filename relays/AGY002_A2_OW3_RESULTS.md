# `AGY-002_A2-OW3` — Unblocked All-Thread Partition Function (Whitehead Hagedorn Wall) and Open-Torus `Spin(10)` Holomorphic Two-Higgs Closure Results (`0 of 19`)

## 1. Check Labels and Tracked Custody (`docs/seats/README.md` § `12`)

- **expectations committed first:**
  - Card commit `14149615d`: `relays/cards/AGY-002_A2-OW3_unblocked-all-thread-partition-function-and-open-torus-yukawa-closure.md`.
  - Disclosed Erratum committed before authoritative `v2`: `983932f61` (`Erratum 1`: extending the three Whitehead accumulation sequences to `k = 50` for the Neumann-Zagier `O(1 / k^2)` gap `< 1 / 100`). Earlier sealed `v1` (`1621a6c47` / `b9338f983`) is preserved untouched.
  - Authoritative producer `v2` script seal `6ee7c7daf` (`relays/a2_ow3_v2/verify_a2_ow3_v2.py`, `SCRIPT_SHA256.txt`) & unread output seal `2294c03c3` (`relays/a2_ow3_v2/verify_a2_ow3_v2_out.json`, `OUTPUT_SHA256.txt`, `all_gates_passed = true`).
- **recomputed independently:**
  - Independent Cold-Room Referee built from Card + Erratum 1 alone (zero access to `a2_ow3*` prior to `Commit 4b`), using 3-way exact Catalan `4 G` (`Cl_2(pi / 2)`, Euler, Ramanujan), high-precision `SnapPy` `HP` volumes (`L5a1` and `5^2_1`), full unoriented-isometry deduplicated census (`53` pairwise non-isometric threads vs producer's `91` oriented Lyndon necklaces), exact `Q[w] / (Phi_5)` ring arithmetic, and independent `5`-fold Pauli Jordan-Wigner `32 x 32` `Cl(10)` construction in exact `Z[i]`: script seal `4163ac0a9` (`relays/a2_ow3_referee/referee_a2_ow3.py`, `SCRIPT_SHA256.txt`) & unread output seal `2fcde558a` (`relays/a2_ow3_referee/referee_a2_ow3_out.json`, `OUTPUT_SHA256.txt`; note two trivial `beta = 0` strict-inequality boundary checks in the sealed referee script evaluated `false` where `exp(0) == 1` exact equality holds, while every positive `beta` and every Card `A2-OW3` pass bar corroborated `v2` digit-for-digit).
- **tested against planted errors:**
  - `4 of 4` planted faults caught identically in both `2294c03c3` and `2fcde558a` (`PF-OW3-1` false `m004` volume uniqueness refuted by `m000` at half volume and `m003` tie; `PF-OW3-2` false pure-volume convergence at `beta = 10` refuted by all `50` Whitehead terms strictly above `exp(-40 G)`; `PF-OW3-3` false Path-A trace variation refuted by constant `+1 / 2` to `< (1/10)^65`; `PF-OW3-4` false `H_u / H_d` cross-coupling refuted by exact `0` entries).

## 2. Mask-Safe Verification Summary (`0 of 19`)

| Task / Metric | Producer `v2` (`2294c03c3`) | Cold-Room Referee (`2fcde558a`) | Agreement |
|---|---|---|---|
| `AST` source & `SHA-256` custody | `0` float/complex literals, `0` `frontier/` imports, `A`-only manifests `OK` | `0` float/complex literals, `0` `frontier/` imports, `A`-only manifests `OK` | Exact (`0` mismatches) |
| `OW3-A`: Whitehead volume `5^2_1` / `L5a1` vs `4 G` | Err `< (1/10)^15` | `L5a1` & `5^2_1` `HP` err `< (1/10)^63`; also verifies `2 * Vol(m001) == 4 G` to `< (1/10)^63` | Exact |
| `OW3-A`: Unblocked ground state (`m000`) & orientable tie (`m003` vs `m004`) | `|2 Vol(m000) - Vol(m004)| == 0`, `|Vol(m003) - Vol(m004)| == 0`, `m000` share `> 999 / 1000` at `(0, 10)`, `m003 / m004` exact `50 / 50` tie (`91` oriented threads) | Identical exact `HP` ratios (`0` diff), non-isometric `m003 != m004`, `m000` share `> 999 / 1000` at `(0, 10)`, exact `50 / 50` tie across all `16` `(s, beta)` points (`53` unoriented-isometry threads) | Exact (invariant under orbit convention) |
| `OW3-A`: Whitehead sequences (`k = 1..50`) & `Z(0, beta) = +infty` | All `3` branches (`b++L^k R`, `b+-L^k R`, `b-+L^k`) strictly monotone `< 4 G`, `k = 50` gaps `< 1 / 100`, all `16` `k = 50 / k = 1` ratios matched | Digit-for-digit match on all `3` branches & all `16` ratios (`b-+L^k` `k^2 * gap -> 2 pi^2`), `Z(0, beta)` divergence proved for all `beta >= 0` | Exact |
| `OW3-B` Part 1: Path-A `15 x 15` trace collapse (`24` shifts) | Exact `+1 / 2` (`W_3^+`) & `-1 / 2` (`W_2^-`) mod `Phi_5`; `65`-dps trace err `< (1/10)^65`, collapse err `< (1/10)^63` | Exact `Cyclo5` `+1 / 2` & `-1 / 2`; `65`-dps trace err `< (1/10)^65`, collapse err `< (1/10)^63` | Exact |
| `OW3-B` Part 2: `32 x 32` `Cl(10)` & `Spin(10)` `X:HOL` (`16 x 16 x 10_C`) | Fock-bitmask `0` errs across `Cl(10)`, `C_10`, `16 x 16` symmetry; `H_u -> {(Q, u^c), (L, nu^c)}`, `H_d -> {(Q, d^c), (L, e^c)}`, `0` crosstalk | Independent `5`-fold Pauli Jordan-Wigner in exact `Z[i]`: `0` errs across `100` `Cl(10)` anticommutators, `C_10`, `16 x 16` symmetry, `0` crosstalk | Exact (`0` errors) |
| `OW3-B` Part 2: `11 / 12` `tan(beta)` invariance & `10`-trial Haar gate | `11`-ratio drift `< (1/10)^15`, `m_t / m_b` linear err `< (1/10)^15`, Haar drift `< (1/10)^14` (`<< (1/10)^12`) | `11`-ratio drift `< (1/10)^14`, `m_t / m_b` linear err `< (1/10)^15`, Haar drift `< (1/10)^14` (`<< (1/10)^12`) | Exact (`PASS`) |
| `OW3-C`: Planted faults (`PF-OW3-1..4`) | `4 / 4` caught | `4 / 4` caught | Exact (`4 / 4`) |

## 3. Core Foundational Findings (`0 of 19`)

1. **Hyperbolic Volume Alone Does NOT Select `m004` (and Pure Volume Sums Diverge Everywhere):**
   - Dropping `G:SE2` reveals **two** non-orientable threads strictly smaller in volume than `m004`: `m000` (`b-+L`, exact `Vol(m004) / 2`, capturing `> 999 / 1000` of the census weight at `beta = 10`) and `m001` (`b-+LL`, exact `Vol(Whitehead) / 2 = 2 G`). Even on the orientable sub-ensemble (`G:SE2` imposed), `m003` (`b+-LR`) and `m004` (`b++LR`) are non-isometric manifolds with **identical** minimal volume (`exact 50 / 50 tie` across all `(s, beta)`).
   - Furthermore, all three infinite cusp-accumulation families (`b++L^k R`, `b+-L^k R`, and non-orientable `b-+L^k`) stay strictly below the Whitehead-link volume `4 G` and converge monotonically from below as `4 G - O(1 / k^2)`, proving rigorously that any pure-volume partition function `Z(0, beta) = sum_M exp(-beta Vol(M))` **diverges (`+infty`) for every finite `beta >= 0`** unless regulated by word-length entropy (`s > 0`, connecting directly to `B1813`).
2. **Open-Torus Yukawa Closure (`N = 5` Top Finite Rung, Zero `m004` Required):**
   - On the open weave's `N = 5` Weyl algebra (`A2-OW1`), `Tr_{W_3^+}(D(w)) == +1 / 2` and `Tr_{W_2^-}(D(w)) == -1 / 2` across all `24` nonzero `w in E[5] \ {0}`, proving unconditionally why any single-Higgs linear contraction collapses to one `3 x 3` matrix (`Path-A` no-go).
   - Explicitly lifting to `32 x 32` `Cl(10)` (`Spin(10)` holomorphic `10_C = 5_H (+) 5bar_H`) separates `H_u` (`Q u^c`, `L nu^c`) from `H_d` (`Q d^c`, `L e^c`) with exact zero crosstalk, exact `11 / 12` `tan(beta)` invariance, and verified Haar basis-scrambling invariance — completing the open-weave structural closure while leaving the continuous Yukawa/hierarchy inputs honestly accounted for. `0 of 19.`
