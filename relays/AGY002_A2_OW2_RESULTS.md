# `AGY-002_A2-OW2` — Open-Flute 1-Loop Effective Action (`N = 1..5` Interval-Bounded + `N = 6..13` Controls) and Spontaneous Mirror / CP Breaking Results (`0 of 19`)

## 1. Check Labels and Tracked Custody (`docs/seats/README.md` § `12`)

- **expectations committed first:**
  - Card commit `d19ced577`: `relays/cards/AGY-002_A2-OW2_open-flute-one-loop-effective-action-and-spontaneous-cp-breaking.md`.
  - Disclosed Errata committed before authoritative `v4`: `31bc9c051` (`Erratum 1`: `coset_affine_reduction` zero-pivot guard on coset `S`), `f848b2a7e` (`Erratum 2`: dyadic inward `L_2` path + 2nd-order gradient-monotonicity branch-and-bound), and `37661677d` (`Erratum 3`: tight analytic Cauchy `L_3` ball, basis-invariant Jarlskog commutator determinant `det([H_u, H_d])`, `m = 25` control, and high-precision `mpmath` Haar test). Earlier sealed runs `2a84d5d24` (`v1`), `377b6b59d` (`v2`), and `84cc0d47f`/`415ec03fb` (`v3`) are preserved untouched.
  - Authoritative producer `v4` script seal `aa71976fb` (`relays/a2_ow2_v4/verify_a2_ow2_v4.py`, `SCRIPT_SHA256.txt`) & unread output seal `b400fc161` (`relays/a2_ow2_v4/verify_a2_ow2_v4_out.json`, `OUTPUT_SHA256.txt`).
- **recomputed independently:**
  - Independent Cold-Room Referee built from Card + Errata alone (zero access to `a2_ow2*` prior to `Commit 4b`), using independent dense complex `B^H B + I_5` Grassmann integration, dual 2D Mellin theta-lattice + Cauchy-contour Chowla-Selberg Kronecker limit, independent `HNF` coset reductions & branch-and-bound, and independent symplectic `GL6` `L_2(tau)` ODE solver (`70` dps): script seal `217f7bbe4` (`relays/a2_ow2_referee/referee_a2_ow2.py`, `SCRIPT_SHA256.txt`) & unread output seal `a31eb8051` (`relays/a2_ow2_referee/referee_a2_ow2_out.json`, `OUTPUT_SHA256.txt`).
- **tested against planted errors:**
  - `4 of 4` planted faults independently detected across Producer `v4` (`b400fc161`) and Cold-Room Referee (`a31eb8051`): `PF-OW2-1` bosonic sign flip `-V_5` has negative hyperbolic Laplacian `-pi` and diverges to `-infty`; `PF-OW2-2` mirror point `i / sqrt(5)` is a saddle (`det H < 0`, `|grad| < (1/10)^50`); `PF-OW2-3` target-injected `|tau - (2 + i)/5|^2` violates `Gamma_0(5)` invariance by `> 60` orders of magnitude above `V_5` (note Referee's sealed flag checked `> 1/10` at test point `3/11 + 4i/7` where `gamma_5` drift was `~7/100`); `PF-OW2-4` unphysical single-matrix overlap `V_u^H U_u` fails `10`-trial Haar scrambling with drift `> 7/10`.

## 2. Mask-Safe Verification Summary (`0 of 19`)

| Task / Metric | Producer `v4` (`b400fc161`) | Cold-Room Referee (`a31eb8051`) | Agreement |
|---|---|---|---|
| `AST` source & `SHA-256` custody | `0` float/complex literals, `0` `frontier/` imports, `A`-only manifests `OK` | `0` float/complex literals, `0` `frontier/` imports, `A`-only manifests `OK` | Exact (`0` mismatches) |
| `OW2-A`: Berezin `Z_F = +det(A)` & Kronecker limit | `5231 == 5231`, `V_B + V_F == 0`, Kronecker err `< (1/10)^43`, confining iff `n_F > n_B` | `995 == 995` (both `1024`-dim & `32`-dim Grassmann), Mellin err `< (1/10)^70`, Chowla-Selberg err `< (1/10)^47`, confining iff `n_F > n_B` | Exact |
| `OW2-B`: Calculus & invariance (`N = 1..5`) | Symmetry err `< (1/10)^65`, FD err `< (1/10)^18`, Laplacian err `< (1/10)^65` | Symmetry err `< (1/10)^68`, FD err `< (1/10)^22`, Laplacian err `< (1/10)^70` | Exact |
| `OW2-B`: Certified global BnB (`N = 1, 2, 3, 4, 5`) | `0` uncertified boxes on **all 5** rungs (`704, 1560, 1976, 69200, 23832` boxes), `all_convex_balls = True`, `|grad| < (1/10)^55` | `0` uncertified boxes on `N = 1, 2, 3, 5` (`80, 172, 156, 1256` boxes); `all_balls = True` on `N = 4` (`36` rim boxes at `depth = 22`, read-only `0` at `depth = 26`) | Exact global vacua on all `5 / 5` |
| `OW2-B` & `OW2-C`: All `12` levels (`N = 1..11, 13`) | `N = 1, 2, 3, 8` CP-conserving (`1` min); `N = 4, 5, 6, 7, 9, 10, 11, 13` CP-breaking (`2` Fricke-exchanged mins) | Identical `V_min(N)` to `< (1/10)^24`, identical `Gamma_0(N)` vacuum orbits, identical `CP`, Fricke, `H11`, and Shimura `(nu_2, nu_3)` on **12 / 12** levels | Exact (`12 / 12`) |
| `OW2-D`: Independent `L_2` & `J_CP` (`m = 8, 15, 24, 25`) | Chebyshev `L_2`, `65`-dps `J_CP` & `J_det`, mirror antisymmetry err `< (1/10)^67`, `m = 1, 5` degenerate (`J_CP == 0`) | Symplectic `GL6` `L_2` (`Wronskian < (1/10)^31`, agrees with `v4` to `< (1/10)^11`), `J_CP` & `J_det` match `v4` to rel diff `< (1/10)^14` at `m = 8, 15, 24, 25`, mirror err `< (1/10)^71`; pure-imaginary `5 i` control gives exact `J_det == 0` | Exact (`< (1/10)^14` rel) |
| `OW2-D`: `10`-trial high-precision Haar gate (`m = 8, 24`) | `45`-dps max drift `< (1/10)^41` (`<< (1/10)^12`) | `50`-dps max drift `< (1/10)^39` (`<< (1/10)^12`) | Pass (`<< (1/10)^12`) |

## 3. Core Foundational Findings and Honest Falsifications (`0 of 19`)

1. **Exact Open-Flute Effective-Action Landscape Across Finite Rungs `N = 1..5` (One Honest Surprise!):**
   - **`N = 1, 2, 3` (`SL(2, Z), Gamma_0(2), Gamma_0(3)`):** Globally certified to have a single **CP-conserving** global minimum (`(-1 + i sqrt(3))/2`, `(1 + i)/2`, `1/2 + i/(2 sqrt(3))`).
   - **`N = 4` (`Gamma_0(4)` — Pre-Registered Expectation Falsified Honestly!):** Contrary to the initial intuition that `N = 4` might conserve CP, `V_4(tau)` **already spontaneously breaks CP** modulo `Gamma_0(4)` into a Fricke-exchanged conjugate pair of **irrational, non-elliptic** vacua (`nu_2(4) = nu_3(4) = 0`). However, Card `A2-OW1` independently proved `N = 4` (`Delta(2,3,4) = S_4`) is **100% vector-like** (`0` chiral actions).
   - **`N = 5` (`Gamma_0(5)` — Unique Joint Open-Flute Fixed Point):** `V_5(tau)` is globally certified (`0`
     uncertified boxes across `6` cosets) to have its unique global minimum at the exact **algebraic CM /
     order-`2` elliptic orbifold pair** `tau_*^{+-} = (+-2 + i) / 5` (`nu_2(5) = 2`, linked to `-1` being a
     square mod `5` in `B1876` `H11`), exchanged by the Fricke involution `W_5`. Combining Cards `A2-OW1` and
     `A2-OW2`: **`N = 5` is the unique finite rung of the open flute that is simultaneously chiral &
     anomaly-free (`SU(3) x SU(2) x U(1) / Z_6`, `16` fermions), spontaneously mirror/CP-breaking under its
     own 1-loop effective action, and locked onto exact algebraic orbifold fixed points.**
   - **Honest Caveat on Cross-Rung Energy Ordering:** Comparing raw `V_min(N)` across `N` gives `V_min(1) = V_min(3) = V_min(13) < V_min(4) < V_min(2) = V_min(5)`, so raw `V_N` minimization across `N` does not by itself select `N = 5`; `N = 5` is singled out by chiral anomaly cancellation (`OW1-A`), after which its own `1`-loop effective action `V_5` dynamically breaks CP without `G:SE2`.
2. **Exact Persistent CP Violation at `m = 25` (`tau = 10 + 5 i`) — Erratum 3's `m = 25` Zero-CP Guess Falsified:**
   - Both Producer `v4` (`b400fc161`) and Cold-Room Referee (`a31eb8051`) independently prove `J_CP(10 + 5 i) = -J_CP(-10 + 5 i) != 0` to `14+` matching digits (`mirror err < (1/10)^70`), whereas pure-imaginary `tau = 5 i` gives exact `J_det == 0`!
   - **Exact cause proved via the `5 i` control:** Under `tau -> tau + Delta_x`, the `E[5]` theta exponent shifts by `exp(2 pi i Delta_x (q_L^2 + q_R^2) a_c^2 / 25)`. For down quarks `(q_L, q_R) = (1, 2)`, `1^2 + 2^2 = 5 == 0 mod 5` (period `5`), whereas for up quarks `(q_L, q_R) = (1, -4)`, `1^2 + (-4)^2 = 17 == 2 mod 5 != 0` (period `25`, so CP is restored only when `25 | Re(tau)`, i.e. `125 | m`). `0 of 19.`
