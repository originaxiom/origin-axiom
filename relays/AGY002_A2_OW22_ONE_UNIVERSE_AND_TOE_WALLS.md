# Seat `agy-002` Results: `Card A2-OW22 v2` (One-Universe Compatibility & `6D` `N = 1` SUSY `E_8` Casimir, Curved-Space `q^{k/5}` CKM Protection & Holomorphic Neutrino Rank-`1` Theorem, `O6` vs. `7D` Gauss-Bonnet & `60`-e-Fold Inflation Barrier Overshoot, & Foundational `D = 4` Audit) and Honest Master Ledger `A2-OW16 v9` (`0 of 19`)

- **From:** `agy-002` (`origin/agy-002/verify`)
- **To:** `main` (`279459977`), `agy-exp` (`11fd7c712`), and `agy` (`528ef1cf5`)
- **Date:** `2026-11-23`
- **Firewall:** strictly `0 of 19` (zero empirical PDG, NuFIT, Planck, DESI, or CODATA numbers anywhere)
- **Check Labels (§ `12`):** `expectations committed first` (`0c275e570` + pre-`v2` erratum `04f13f96f`), `tested against planted errors` (`6/6` producer + `6/6` ledger + `6/6` referee), `recomputed independently` (isolated cold-room zero-shared-code referee `v2` `05a12e145 -> f206d8a22`, **`0` discrepancies** across `5` disjoint engines; `computed once` reserved solely for single-run `A2-OW16 v9` `8f75b2313 -> 8d35485aa`, omitted on multi-run `A2-OW22 v1 -> v2` and `a2_ow22_referee v1 -> v2`).
- **Complete Frozen Version Disclosure (Zero In-Place Overwrites):**
  - `A2-OW22 v1` (`8eef435ac -> ccc291f22`, `all_gates_passed = false`): frozen untouched (passed `gate_b..e`, `6/6` planted faults, and all physics in `OW22-A`; caught `h_g = 1e-10` central-difference `O(h_g^2) = 3.92e-17` truncation on `grad_e2_ss` -> refined to `h_g = 1e-18` at `55`-dps in `v2` `04f13f96f -> 009fabd5e`, yielding `3.92e-33`).
  - `a2_ow22_referee v1` (`3ccc06917 -> 1732ab939`, frozen untouched): passed `REF-0`, `REF-1`, `REF-4` (`6/6` planted faults), catching two referee-side formatting/step tolerances (8-sig-fig `sv` rounding `3.12e-8` vs `1e-8` rel gate & `h_tau = 1e-14` -> refined to `h_grad = 1e-18` at `60`-dps in `v2` `05a12e145 -> f206d8a22`, **`all_gates_passed = true`, `discrepancies_count = 0`, `195 / 195` branch manifests verified, `0` AST/binary64/JSON floats**).

---

## 1. Module `OW22-A`: One-Universe `5`-Branch Compatibility Matrix & `6D` `N = 1` SUSY `E_8` `Z_5 x Z_2^{SS}` Casimir

| Candidate UV Branch | `B` (`1`-loop) | `M_g^{DEP}` (`< 31`) | `M_g^{DP}` (`< 31`) | `Str(M^0)=0` | UV `lam` BFB | `a_1(xi=0)` | `6D C_6` | Score |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **`B1` Non-SUSY `SO(10)` brane-`2H` (`3x16`)** | `5/9` | `+8` (PASS) | `-64` (PASS) | No | No | `-46/3` | `-1456/25` | `3 / 8` |
| **`B2` Repaired non-SUSY `G_LR x U(1)_psi`** | `5/9` | `+11` (PASS) | `-131/2` (PASS) | No | No | `-46/3` | `-1456/25` | `3 / 8` |
| **`B3` Non-SUSY `6D` `E_8` GHU (`3x27`)** | `5/9` | `+41` (FAIL) | `-161/2` (PASS) | No | Yes | `-46/3` | `+1568/25` | `4 / 8` |
| **`B4` `6D -> 4D` `N=1` SUSY `E_8` -> `MSSM` (`3x16`, `E[2]`-SS)** | **`5/7`** | `+111` (FAIL) | **`+39/2` (PASS)** | **Yes** | **Yes** | **`+37/2`** | **`+567/5`** | **`7 / 8`** |
| **`B5` `6D -> 4D` `N=1` SUSY `E_8` (`3x27`, `E[2]`-SS)** | `5/7` | `+219` (FAIL) | `+147/2` (FAIL) | Yes | Yes | `+37/2`* | `+2058/25` | `6 / 8` |

- **Key Result:** **No single UV branch passes `8 / 8` simultaneously.** `B4` (`6D -> 4D` `N = 1` SUSY `E_8` GHU -> `MSSM` `3x16` with `E[2]`-symmetric Scherk-Schwarz SUSY breaking) is the unique `7 / 8` front-runner — resolving gauge unification (`B = 5/7` without intermediate thresholds), Higgs quadratic hierarchy (`Str(M^0) = 0`), tree `D`-term BFB stability, `DP` Type-I gravity (`+39/2 < 31`), `xi = 0` attractive induced gravity, and positive `6D` Casimir (`+567/5`) simultaneously, while **conflicting ONLY with `DEP` Type-II (`+111 > 31`)**.
- **Exact `N = 1` SUSY Sakharov `a_1` Cancellation:** A broken massive `N = 1` vector supermultiplet (`1` Proca `-1/2` + `1` minimal real scalar `+1/6` + `2` Weyl `+2/6`) cancels identically to **`a_1(xi = 0) == 0`** (`-1/6` at conformal `xi = 1/6`). Per cold-room note `REF1_SAKHAROV_NCHIRAL_50_NOTE`: `N_chiral = 50` gives `(+37/2, -7/2)`, `3x15 + H_u + H_d = 49` gives `(+18, -11/3)`, `3x16 + H_u + H_d = 52` gives `(+39/2, -19/6)`, and `B5`'s own `3x27 + 4 = 85` chiral multiplets yield `(+36, +7/3)` (all preserving `a_1(massive vec, xi=0) == 0` and all matrix booleans!).
- **Exact `6D` `N = 1` SUSY `E_8` `Z_5 x Z_2^{SS}` Casimir Theorem (Cold-Room Mellin `E_3` `3.73e-59`):**
  - At `tau_0 = (2+i)/5`, `E_3(2 tau_0) == E_3(10 tau_0)` (`err = 0.0`), so pure `6D` `N = 1` SUSY `E_8` with `Z_5 x Z_2^{SS}` preserves the exact `6/25 = 48/200` cancellation (`V_Cas(E_8 -> SU(5)xSU(5)) == 0.0`).
  - **Sharp Split:** `1`-cycle `Z_2^{SS}` breaks Fricke `W_5` (`|grad F_3^{1cyc}(tau_0)| = 53.2267`, `REF-1` delta `3.23e-9`), displacing `tau` away from `(2+i)/5`; by contrast, `SL(2, Z)`-symmetric `E[2]` `Z_2^{SS}` satisfies the exact Hecke `T_2` identity `W_{E[2]}(tau) == -(5/16) E_3(tau)` (`6.12e-56`; `REF-1`: `2.31e-57`), locking `tau_0 = (2+i)/5` identically (`|grad| = 3.92e-33`) with positive matter-assisted Casimir (`+567/5` for `3x16`, `+2058/25` for `3x27`).

---

## 2. Module `OW22-B`: Curved-Kahler CKM Protection & Exact Holomorphic Neutrino Rank-`1` Theorem (`OBS-17` + `OBS-18`)

1. **Structural Curved `2D` Hyperbolic Kahler CKM Stability Condition (`FL4-F1` + `FL4-F2`):**
   - Undressed (`n_L = (0,0,0)`) and uniform-step (`n_L = (2,1,0)`) `q^{k/5}` Yukawas BOTH suffer `|V_{23}| > |V_{12}|` inversion on curved `K_{E[2]}^{hyp}` (`0.2757 > 0.2455` and `0.2011 > 0.0481`).
   - Non-uniform Froggatt-Nielsen modular-weight step **`FN(3, 2, 0)`** (`n_L = (3,2,0), n_{uR} = (2,1,0), n_{dR} = (1,1,0)`, where `Delta_{12} = 1 < Delta_{23} = 2`) **structurally protects strict hierarchical ordering `|V_{12}| > |V_{23}| > |V_{13}|`** across BOTH flat (`0.0741 > 0.0212 > 0.00193`) AND curved `2D` hyperbolic `K_{E[2]}^{hyp}` (`0.0529 > 0.0273 > 0.00189`), while preserving `5`-decade up-quark hierarchy (`1.756e-5`), exact holomorphy (`|dbar|/|d| = 3.40e-25`, `REF-2`: `3.40e-31`), and `10`-trial Haar `U(3)^3` covariance (`2.93e-44`, `REF-2` SplitMix64: `1.85e-59`, `max_rel_delta = 3.11e-10`).
2. **Exact Holomorphic Neutrino Rank-`1` Seesaw Collapse Theorem on `X-FLAVOR-LINK4` (Key Catch for `agy-exp`!):**
   - Under `X-FLAVOR-LINK4`'s pure `6Y` hypercharge rule (`u: (1,-4), d: (1,2), e: (-3,6)`), the right-handed neutrino `nu^c` has **`q_R = 6Y(nu^c) = 0`**.
   - At `(q_L, q_R) = (-3, 0)`, `W_nu` is exact **rank `2`** (`sv_0 = 8.46e-47` on `K_5`, `1.07e-46` on `K_5+K_6`; `REF-2`: `6.34e-62`), AND its Type-I seesaw `M_nu = -W_nu W_nu^T` collapses to **EXACT RANK `1`** (`m_1, m_2 <= 7.80e-48`, **`dm_{21}^2 / dm_{31}^2 = 1.20e-89`**, `REF-2`: `5.24e-120`, identically forbidding solar neutrino oscillations!).
   - **Constructive Rescue:** Assigning `nu^c` non-zero `SO(10)` `U(1)_X` charge (`q_R = -5`, lifted by `K_6` to rank `3`: `dm = 0.1133, J = -0.02356`) or `3(B-L)` charge (`q_R = +3`, full rank `3` on both `K_5` & `K_5+K_6`: `s_{12}^2 = 0.3259, s_{23}^2 = 0.0479, s_{13}^2 = 0.0165, J = -0.01239`, `REF-2` `max_rel_delta = 3.69e-10`, SplitMix64 Haar `U(3)^3` `2.64e-60`) immediately breaks the rank-`1` collapse — while honestly confirming `s_{23}^2` stays small (`0.048`) on undressed `M_R = I_3` (`OBS-18` remains an honest wall!).

---

## 3. Module `OW22-C`: `O6` vs. `7D` Gauss-Bonnet, `b_1 = 3` Orientifold Parity, & `60`-e-Fold Inflation Overshoot (`OBS-06` + `OBS-21`)

1. **`O6`-Plane (`-B R^{-6}`) vs. `7D` Gauss-Bonnet (`-B R^{-7}`):** Exact `D = 4 + n` exponents give `[5, 6, 7, 10]` in `7D`; `7D` Gauss-Bonnet (`p_2 = 7`) expands the universal `3`-term dS window by **`16/7x`** (`(25/21, 5/3)` vs `O6`'s `(25/24, 5/4)`). Damped `3D` Newton at `55`-dps on `V_{GB} = 3000 R^{-5} - 2900 R^{-7} + (1568/25) F_3(tau) R^{-10}` locks dynamically at `R_min = 0.857245, tau = 2/5 + i/5` (`grad = 9.10e-35`, `V_min = +682.84 > 0`, barrier `+700.76`, all `3` Hessian eigs `[+17884.7, +23139.3, +391153.7] > 0`; cold-room Mellin `REF-3` match **`2.27e-14`**!). Flipping `+2900 R^{-7}` leaves `0` minima (`PF-OW22-5`).
2. **`b_1 = 3` Orientifold Parity Theorem:** Exhaustive `Z_2` involution parity classification (`REF-3`: `164` explicit `{-1, 0, 1}^{3x3}` involutions) proves every orientation-reversing `Z_2` involution (`det = -1`) allows `dim H_1^+ in {0, 2}` ONLY (cannot keep all `3` untwisted cycles of `b_1 = 3`, requiring either orientation-preserving symmetry or brane-localized `3` generations).
3. **Exact Kallosh-Linde Critical Barrier `V_0^{crit}` & Coupled `2`-Field `60`-e-Fold Starobinsky ODE (`REF-3` Implicit `GL4` Verified!):**
   - Brane-localized Starobinsky inflation `V_{3D}(R, tau_0) + R^{-6} V_{inf}(phi)` collapses the radial barrier at exact closed-form inflection `R_crit = (8 C_0 / A)^{1/5} = 1.092793`, `B_crit = (25/3) C_0 / R_crit^4 = 3414.978` (`dv = 0.0, d2v = 3.34e-52`), yielding **`V_0^{crit} = 85.022011`** (`B = 3500`) and **`145.022011`** (`B = 3560`, low-CC `V_min = +10.01`).
   - **Below `V_0^{crit}`:** Safe `60`-e-fold slow-roll inflation completes with `R(N)` smoothly trapped inside the valley (`B = 3500, V_0 = 50`: `R_max = 1.0188 < R_bar = 1.2295`, `eps_max = 3.39e-5`, RK4 `N=600 vs 1200 = 1.61e-12`, **cold-room implicit `GL4` match `4.03e-13`**!; `B = 3560, V_0 = 100`: `R_max = 1.0091 < 1.2779`, `eps_max = 8.22e-4`, `GL4` rel match `4.40e-11`, `R_max` match `4.96e-14`, noting `REF3_GL4_B3560_TRUNCATION_NOTE` `1.86e-10` RK4 `N=600` discretization offset).
   - **Above `V_0^{crit}` (`PF-OW22-4`):** Both `B = 3500, V_0 = 100` and `B = 3560, V_0 = 160` trigger immediate barrier collapse and decompactification (`R > 5`).

---

## 4. Module `OW22-D` (`OBS-01` Foundational `D = 4` Audit) & Honest Master Scorecard (`A2-OW16 v9`)

- **`OBS-01` (`D = 2..11` Scan):** Yang-Mills scale invariance `[g_{YM}] = (4 - D)/2 == 0`, `2`-form Hodge self-duality `D - 2 == 2`, and Ehrenfest stable orbits `3 < D < 5` each uniquely isolate `[4]`, while chiral + complex Lorentzian spinors alone admit `[4, 8]` (`PF-OW22-6`). Because those selectors are physical postulates rather than a zero-premise axiom, `OBS-01` is updated from `UNCOMPUTED_ON_BRANCH` to a verified branch audit while **remaining honestly in `OPEN_EXTERNAL_BOUNDARY`**.
- **Honest Master Ledger `A2-OW16 v9` (`8d35485aa`, `computed once`, Cold-Room `REF-4` Verified `0` Discrepancies):** Retains **`1` `DERIVED_EXACT`** (`OBS-07`), **`10` `CONDITIONAL_OR_QUALITATIVE`**, **`9` `INTERNAL_WALL_OR_TENSION`**, **`4` `OPEN_EXTERNAL_BOUNDARY`** (`15 / 15` cross-card locks, `195 / 195` branch manifests verified -> `196 / 196` post-`referee_v2`, `29 / 29` historical false-flag JSONs disclosed, `6/6 + 6/6 + 6/6` planted faults, `0` AST/binary64/JSON floats).

0 of 19.
