# `AGY-002_A2-OW4` — Dynamic Chiral-Bowl Selection of `N = 5` and Unique `(D = 4, N = 5, N_gen = 3)` 1-Loop Sakharov Induced Gravity Results (`0 of 19`)

## 1. Check Labels and Tracked Custody (`docs/seats/README.md` § `12`)

- **expectations committed first:**
  - Card commit `def63a893`: `relays/cards/AGY-002_A2-OW4_chiral-bowl-rung-selection-and-unique-4d-sakharov-gravity.md`.
  - Disclosed Erratum committed before authoritative `v2`: `7b0d3372c` (`Erratum 1`: fixing `A_5` triangle generator `b` at `N = 5` to `(0, 2, 4, 3, 1)` so `ord(ab) = 5`; earlier sealed `v1` `9ca94f852` is preserved untouched).
  - Authoritative producer `v2` script seal `285100ebd` (`relays/a2_ow4_v2/verify_a2_ow4_v2.py`, `SCRIPT_SHA256.txt`) & unread output seal `08315469d` (`relays/a2_ow4_v2/verify_a2_ow4_v2_out.json`, `OUTPUT_SHA256.txt`, `all_gates_passed = true`).
- **recomputed independently:**
  - Independent Cold-Room Referee built from Card + Erratum 1 alone (zero access to `a2_ow4*` prior to `Commit
    4b`), using disjoint matrix realizations (`PSL(2, F_2)`, `PSL(2, F_3)`, `SO(3, Z)` cube rotations, `PSL(2,
    F_5)`), direct bitmask `0 .. 2^d - 1` even-Fock weight enumeration, exact rational Bernoulli /
    Hurwitz-zeta Euler-Maclaurin heat-kernel expansion on `S^4, S^6, S^8, S^10` and `S^2 x S^2` (zero
    Vandermonde finite-`t` fitting), and `50`-digit Mellin / spectral cross-checks (matching direct spectral
    sums at `t = 1 / 200` to `< (1 / 10)^31`): script seal `ec901028d`
    (`relays/a2_ow4_referee/referee_a2_ow4.py`, `SCRIPT_SHA256.txt`) & unread output seal `1192ed854`
    (`relays/a2_ow4_referee/referee_a2_ow4_out.json`, `OUTPUT_SHA256.txt`, **`0` discrepancies across all
    fields**).
- **tested against planted errors:**
  - `4 of 4` planted faults caught identically in both `08315469d` and `1192ed854` (`PF-OW4-1` Dirac Berezin sign flip violates Broda-Szanecki by `2`; `PF-OW4-2` omitting `l = 0` scalar ghost zero-mode `-6` on `S^4` shifts `a2_V` from `-62 / 15` to `+28 / 15`; `PF-OW4-3` shifting `N_gen = 2` flips `6 C_grav` negative `-8` / `-12` ghost gravity; `PF-OW4-4` shifting to `D = 6` breaks exact cancellation to `+12 != 0`).

## 2. Mask-Safe Verification Summary (`0 of 19`)

| Task / Metric | Producer `v2` (`08315469d`) | Cold-Room Referee (`1192ed854`) | Agreement |
|---|---|---|---|
| `AST` source & `SHA-256` custody | `0` float/complex literals, `0` `frontier/` imports, `A`-only manifests `OK` | `0` float/complex literals, `0` `frontier/` imports, `A`-only manifests `OK` | Exact (`0` mismatches) |
| `OW4-A`: All `21` faithful actions `Delta(2,3,N)` (`d <= 12`) | `1` anomalous (`N = 2, d = 3`, `Tr Y^3 = -6`), `19` vector-like bosonic runaways (`n_F^{chiral} - n_B < 0`), unique confining chiral bowl `N = 5, d = 5` (`+64` `2H`, `+68` `1H`) | Independent matrix-group + bitmask `0 .. 2^d - 1` enumeration: identical `21 / 21` classification (`+64` `2H`, `+68` `1H`) | Exact (`0` discrepancies) |
| `OW4-B`: `S^4, S^6, S^8` & `S^2 x S^2` Sakharov weights | Direct `45`-dps Vandermonde spectral fit: `w_s = 1 / 6`, `w_W = 2^(D/2 - 1) / 12`, `w_V = (D - 8) / 6`, max err `< (1 / 10)^8`, Broda-Szanecki err `< (1 / 10)^9` | Exact rational Bernoulli / Hurwitz-zeta Euler-Maclaurin (`0` exact err, `S^10` included, spectral check `< (1 / 10)^31`); max offset vs `v2` `< 4 / 10^9` | Exact |
| `OW4-B`: 4D `a_2` & disentangled `(c, a)` (`S^4` + `S^2 x S^2`) | `S^4`: `(29/15, -11/30, -62/15)`; `S^2 x S^2`: `(11/45, 1/90, -38/45)`; `(c, a)` max err `< (1 / 10)^7` | Exact rational inversion (`det = 128`): `(c_s, a_s) = (1/120, 1/360)`, `(c_W, a_W) = (1/40, 11/720)`, `(c_V, a_V) = (1/10, 31/180)`; max offset vs `v2` `< 5 / 10^8` | Exact |
| `OW4-C`: Unique `(D = 4, N = 5, N_gen = 3)` induced gravity | Exact cancellation `n_W w_W(D) + n_V w_V(D) = 0` holds uniquely at `(D = 4, N_gen = 3)` (`48 - 4*12 = 0`); unique attractive `6 C_grav = +8` (`2H`) / `+4` (`1H`), conformal `= 0` | Identical across all `16` `(D, N_gen)` pairs and all `21` actions; `N_gen = 1, 2` and all `19` vector-like actions give ghost gravity (`< 0`); `D = 6` needs `N_gen = 3 / 4`; `D >= 8` impossible (`w_V >= 0`) | Exact (`0` discrepancies) |
| `OW4-C`: 4D trace anomaly `(c, a)` & honest `a_0` CC no-go | `c = 37 / 15, a = 127 / 45` (`2H`), `c = 73 / 30, a = 253 / 90` (`1H`); `a_0 = n_B - n_F = -64` (`2H`) / `-68` (`1H`) `!= 0` | Identical exact rationals; `quartic_cc_cancellation_occurs = false` | Exact |
| `OW4-D`: Planted faults (`PF-OW4-1..4`) | `4 / 4` caught | `4 / 4` caught | Exact (`4 / 4`) |

## 3. Core Foundational Findings (`0 of 19`)

1. **Dynamic Chiral-Bowl Selection of `N = 5` (Resolving `A2-OW2`'s Raw Rung Ranking):** Combining `A2-OW1`'s
   chirality/anomaly census with `A2-OW2`'s Berezin confining sign (`n_F > n_B`) eliminates every rival finite
   rung dynamically: `N = 2` (`S_3`) is gauge-anomalous (`Tr Y^3 = -6`), while all `19` anomaly-free non-SM
   actions (including `N = 3` `A_4`, `N = 4` `S_4`, and every higher degree `6 <= d <= 12`) are strictly
   vector-like with `0` protected chiral Weyl zero modes, yielding negative `n_F^{chiral} - n_B < 0` (bosonic
   runaway instability). The top finite rung `N = 5` (`A_5 / A_4`, `d = 5`, `[1, 2, 2]`) is the **unique**
   dynamically confining chiral bowl (`n_F^{chiral} - n_B = +64` for `2H`, `+68` for `1H`).
2. **Unique `(D = 4, N = 5, N_gen = 3)` 1-Loop Induced Gravity:** First-principles spectral heat-kernel
   evaluation on `S^4, S^6, S^8` and `S^2 x S^2` proves `w_s(D) = 1 / 6`, `w_W(D) = 2^(D/2 - 1) / 12`, and
   `w_V(D) = (D - 8) / 6`. For the open-weave `A_5 / A_4` gauge-matter engine (`n_V = 12`, `16` Weyl per
   generation), exact fermion-minus-gauge quadratic Planck cancellation `n_W w_W(D) + n_V w_V(D) = 0` selects
   **both `D = 4` (uniquely among all even external dimensions `D >= 4`) and `N_gen = 3` (`48 - 4 * 12 = 0`,
   matching `W:T`)**. Minimal Higgs (`xi = 0`) tips `6 C_grav = +8 > 0` (`2H`) / `+4 > 0` (`1H`) — unique
   attractive 4D gravity (`G_N > 0`) — while conformal Higgs (`xi = 1 / 6`) gives exact zero quadratic Planck
   divergence (`C_grav = 0`), with positive trace-anomaly central charges `c = 37 / 15` and `a = 127 / 45`.
3. **Honest Remaining Cosmological Constant Wall (`a_0 != 0`):** Because `n_B - n_F = -64` (`2H`) / `-68` (`1H`) is strictly nonzero (the exact same fermionic excess required for the confining 1-loop chiral bowl), the quartic vacuum-energy coefficient `a_0` does **not** vanish on the massless spectrum. `0 of 19.`
