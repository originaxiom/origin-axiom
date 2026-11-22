# AGY-002 Results Relay: Card `A2-OW14` — Unfreezing `7D` Spacetime (`M_4 x M_3` Hyperbolic Radion & Townsend-Wohlfarth Acceleration) and Unimodular / Kaloper-Padilla Vacuum Sequestering (`0 of 19`)

- **Seat / Branch:** `AGY-002` on `agy-002/verify`
- **Empirical Inputs:** **`0 of 19`** (zero PDG or cosmological-parameter inputs; pure `7D -> 4D` differential geometry, Friedmann-radion dynamics, Litim unimodular FRG, and variational sequestering algebra).
- **Custody Chain:**
  - Pre-Registration Card: `relays/cards/AGY-002_A2-OW14_7d-hyperbolic-radion-acceleration-and-unimodular-sequestering.md` (`9b6a76ae9`)
  - Preserved `v1` Producer (untouched): `relays/a2_ow14/` (`81309c1fd` / `4a0f1fc98`, `ow14_a/c = True`, `ow14_b = False` due to an `A_5` generator typo fixing index `4`)
  - Authoritative `v2` Producer (`all_gates_passed = true`): `relays/a2_ow14_v2/verify_a2_ow14_v2.py` (`c4b1f5560`, `SCRIPT_SHA256 = ebdf1389797bbe312a9b1a13411ee913890727897b9443010790cf603afff8b3`) and `relays/a2_ow14_v2/a2_ow14_v2_results.json` (`d6ee2c158`, `OUTPUT_SHA256 = 8ee32689f299f47f221088770f36415632b3e5df3cc2b5ba6e5d1193cf16cf9c`)
  - Independent Cold-Room Zero-Trust Referee (strictly cold-room sealed unread): `relays/a2_ow14_referee/referee_a2_ow14.py` (`baf83287d`, `SCRIPT_SHA256 = 2b88727df9a2cc162983f99a4849ae05f9d9b0c9b5fb36671bd5edf480c3f11b`) and `relays/a2_ow14_referee/a2_ow14_referee_results.json` (`43fd95262`, `OUTPUT_SHA256 = c7cf995001f6590f7d70532601ec21756314e535d812086810c9e512bf3c2ea0`)
  - **Cross-Check Result:** **`0` producer defects across all `112` compared fields** plus `4 / 4` planted
    faults (`PF-OW14-1..4`) detected identically. Disjoint referee methods: general `D = d + n` Weyl conformal
    / `(1 + 6)` ADM extrinsic-curvature reduction (disjoint from `7^3` Christoffel loop), Heaviside partial
    fractions + `sympy.integrate` + `70`-dps Gauss-Legendre / tanh-sinh quadrature + `scipy` `Radau` `1D`
    autonomous & `4D` cosmic-time ODEs (disjoint from `DOP853`), manual exact-`QQ` Sturm sequence + `60`-dps
    bisection/Halley, general `10`-parameter non-diagonal `L D L^T` unimodular metric tensor, and
    `sympy.combinatorics` `PermutationGroup` census. Max non-ODE discrepancy `<= 5 / 10^18` (JSON
    serialization floor); `1D Radau` vs `DOP853` `N_accel` matches to `< 2 / 10^15`; `4D Radau` vs `DOP853`
    `w_min` matches to `0` and `w_late(t = 200)` to `< 5 / 10^12`. *(Cold-room transparency notes: (i) in
    `referee_a2_ow14.py`, the referee's own `4D` event surface accidentally coded `3 v^2 - 2 V = 0` (`w =
    -1/2`) rather than `v^2 - V = 0` (`w = -1/3`), causing its sealed `OW14-A.2` flag to trip even though its
    `1D Radau`, `4D Radau` trajectory, and `70`-dps quadratures all reproduced every `v2` number to `< 5 /
    10^12`; the cold-room seal `baf83287d`/`43fd95262` is preserved untouched; (ii) the referee caught a Card
    line `58` prose arithmetic typo stating `theta_g = 14/6 = 7/3` for traceless `cap = 22, N_gen = 3` whereas
    BOTH Producer `v2` and Referee compute the exact value `2*(22 - 8)/(21 - 8) = 28/13`; (iii) the referee
    noted Card line `59` omitted the `A2-OW10` `(max_index <= 12, involution-class)` pairing convention (`21`
    actions vs `20` unconstrained transitive cosets), while BOTH conventions uniquely select `N = 5, d = 5`
    (`M_g = 8`) for both caps.)*

---

## 1. Task `OW14-A`: `7D -> 4D` Hyperbolic Radion, Townsend-Wohlfarth Acceleration, & Volume Stabilization

1. **First-Principles `7D` Einstein-Frame Reduction (`M_4 x M_3`):**
   - Direct `7^3` Christoffel / `7 x 7` Ricci reduction (producer) and `(1 + 6)` ADM / Weyl conformal reduction (referee) agree identically: `4D` Einstein frame fixes `a = -(3/2) b`, integration by parts gives `L_kin = (15/4) b^2 (sig')^2`, yielding canonical `b = sqrt(2/15) = sqrt(30)/15` and `a = -sqrt(3/10) = -sqrt(30)/10`.
   - Exact Einstein-frame potential slopes (`V_i proportional to e^{-gamma_i phi}`):
     - Bulk `Lambda_7` (`L^-3`): `gamma_Lam = sqrt(6/5) < sqrt(2)`, `eps_V = 3/5 < 1`, `w_attr = -3/5 < -1/3` (accelerates).
     - Hyperbolic curvature `R(H^3) = -6 / L^2` (`L^-5`): `gamma_curv = sqrt(10/3) > sqrt(2)`, `eps_V = 5/3 > 1`, `w_attr = +1/9` (no-go).
     - `7D` CS `3`-form flux (`L^-9`): `gamma_flux = 3 sqrt(6/5) > sqrt(2)`, `eps_V = 27/5`, `w_attr = +13/5` (no-go).
     - `1`-loop `n_F > n_B` Casimir (`L^-10`): `gamma_Cas = 2 sqrt(10/3) > sqrt(2)`, `eps_V = 20/3`, `w_attr = +31/9` (no-go).
   - **Single-Term Slow-Roll No-Go:** Hyperbolic curvature, `3`-form flux, and Casimir energy ALL strictly violate `gamma < sqrt(2)` and cannot drive permanent slow-roll inflation.

2. **Exact Closed-Form Townsend-Wohlfarth Hyperbolic Acceleration Theorem (`H^3`):**
   - Exact `1D` autonomous Friedmann-radion flow `dx/dN = (1 - x^2)(sqrt(5) - 3 x)` (`w = 2 x^2 - 1`, accelerating band `|x| < 1/sqrt(3)`) yields the exact closed-form supremum of transient acceleration `e`-folds for ANY roll-up-and-bounce trajectory on `M_4 x H^3 / Gamma`:
     `N_accel_max(H^3) = (3/4) ln((sqrt(5) + sqrt(3)) / (sqrt(5) - sqrt(3))) - (sqrt(5)/4) ln((sqrt(3) + 1) / (sqrt(3) - 1))` (`~ 8114 / 10^4` `e`-folds).
   - Verified `3` ways: exact closed form, `55`/`70`-dps quadrature (`< 6 / 10^56`), and direct cosmic-time `DOP853` / `1D Radau` Friedmann ODEs (`w_min = -1` exact de Sitter bounce to `< 5 / 10^34`, `N_accel` matches closed form to `< 2 / 10^14`, late-time `w(t = 200) ~ 1097/10^4 -> 1/9`).
   - Dimension scan across hyperbolic `H^n`: `N_accel_max(H^2) ~ 687/1000 < N_accel_max(H^3) ~ 811/1000 < N_accel_max(H^4) ~ 907/1000 < N_accel_max(H^6) ~ 1054/1000 < 2` — **proving genuine transient de Sitter bounce (`w -> -1`) AND a sharp quantitative no-go against single-radion `60`-`e`-fold CMB inflation (`N_accel_max < 1 << 60`)!**

3. **Exact `7D` Hyperbolic Volume Stabilization Theorem (Guardrail 1 Zero-Pinning):**
   - For `V(L) = c_3 L^-3 + c_5 L^-5 + c_9 L^-9 + c_10 L^-10` (`c_5, c_9, c_10 > 0`):
     - `Lambda_7 >= 0` (`c_3 >= 0`): **`0` positive extrema** (strict runaway decompactification no-go).
     - `Lambda_7 < 0` (`c_3 = -|c_3| < 0`, AdS bulk): **unique strictly stable local minimum `L_* > 0`** (benchmark `(|c_3|, c_5, c_9, c_10) = (1, 1, 1, 1)` gives `L_* ~ 1578/1000`, `V'(L_*) < 2 / 10^55`, `V''(L_*) ~ +1060/1000 > 0`, `V(L_*) ~ -125/1000 < 0`), with general symbolic proof `V''(L_*) = 2 (5 c_5 L_*^5 + 27 c_9 L_* + 35 c_10) / L_*^12 > 0` AND strictly negative `AdS_4` energy `V(L_*) = -(2 c_5 L_*^5 + 6 c_9 L_* + 7 c_10) / (3 L_*^10) < 0`.
     - Lifting to a stable **Minkowski minimum (`V = V' = 0, V'' > 0`)** without unimodular gravity requires a negative intermediate term (`-c_6 L^-6`, exact `c_6 = (4/3) c_5 L_*`, `c_9 = (1/3) c_5 L_*^4`, `V''(L_*) = 4 c_5 / L_*^7 > 0`).

---

## 2. Task `OW14-B`: Unimodular Gravity (`det g = -1`, `lam = 0`) & Kaloper-Padilla Sequestering

1. **Exact Vacuum-Energy Decoupling & Moduli Preservation:**
   - Verified on `4 x 4` diagonal (producer) and `10`-parameter non-diagonal `L D L^T` unimodular metrics (referee) that `T_{ab} -> T_{ab} - rho_vac g_{ab}` shifts the trace-free tensor `T_{ab} - (1/4) g_{ab} T` by identically `0`, decoupling `a_0 = -64`, `6D` bulk `-6/-2/-1`, and `V(L_*) < 0` (`AdS_4` radion minimum), while covariant conservation `nabla^a T_{ab} = 0` leaves the Klein-Gordon equation `Box phi - V'(phi) = 0` (`A2-OW9` `tau_*` and `OW14-A` `L_*`) `100%` intact.

2. **Unimodular Asymptotic Safety FRG (`lam = 0`) — `N_gen = 3` Double Pincer Preserved!**
   - Exact closed forms: `g_* = 12 pi / (cap - M_g)`, `theta_g = 2 (cap - M_g) / (cap - 1 - M_g) > 2` for `M_g < cap`:
     - **Full `lam = 0` slice (`cap = 23`):** `0 < 16 N_gen - 40 < 23 <=> 5/2 < N_gen < 63/16` -> **unique integer `N_gen = 3`** (`g_*(G_SM 2H) = 4 pi / 5 ~ 251/100`, `theta_g = 15/7`; `N_gen = 4` has `M_g = 24 >= 23`, excluded!).
     - **Traceless unimodular (`cap = 22`):** `0 < 16 N_gen - 40 < 22 <=> 5/2 < N_gen < 31/8` -> **unique integer `N_gen = 3`** (`g_*(G_SM 2H) = 6 pi / 7 ~ 269/100`, `theta_g = 28/13`; `N_gen = 4` excluded!).
   - **`Delta(2,3,N)` Action Census:** **`N = 5, d = 5` (`A_5 / A_4`, `M_g = +8`) remains the UNIQUE chiral, anomaly-free survivor (`1 of 21` `(H, involution)` pairs, `1 of 20` unconstrained transitive cosets) for BOTH `cap = 23` and `cap = 22`!**
   - **UV `Spin(10) real-10`:** survives BOTH Type-II (`M_g = -122`, `g_* = 12 pi / 145 ~ 26/100` full, `pi / 12 ~ 26/100` traceless) and Type-I (`M_g = -74`, `g_* = 12 pi / 97 ~ 39/100` full, `pi / 8 ~ 39/100` traceless).
   - **`A2-OW13` Bridges at `lam = 0`:** (i) `f_xi^{bg}(lam = 0) = 0` identically (conformal `xi = 1/6` protected from gravitational breaking!), and (ii) bare `G_SM 2H` gets `f_lam^{(dD)}(lam = 0) = 16/3 > 5 >> f_crit ~ 404/10^4`, curing even bare `G_SM 2H`'s `lam_1` collision wall!

3. **Kaloper-Padilla (`arXiv:1309-6562`) Global Sequestering:**
   - Exact global variation of `(Lam_bare, lam_s)` gives `Lam_bare = (1/4) <T^{phys}>`, `Lam_res = Lam_bare + lam_s^4 rho_vac = lam_s^4 (L_0 - K_sym / 2)`, and **`d(Lam_res) / d(rho_vac) == 0` identically** (exact sequestering of `a_0 = -64` and `V(L_*) < 0`, contingent on finite `4D` spacetime volume `0 < V_4 < infty`).

---

## 3. Task `OW14-C`: `4 / 4` Planted Faults (`PF-OW14-1..4`)

- `PF-OW14-1` (corrupt `a = -(3/2) b` to `a = -b`): **CAUGHT** — `2 a + 3 b != 0`, non-Einstein frame, `b` shifts from `sqrt(30)/15` to `sqrt(6)/6`.
- `PF-OW14-2` (flip AdS bulk `c_3 = -1` to dS `c_3 = +1`): **CAUGHT** — positive extrema drop from `1` to `0` (runaway).
- `PF-OW14-3` (`N_gen = 4`, `M_g = +24` in unimodular FRG): **CAUGHT** — `g_* = -12 pi < 0` (`cap = 23`) and `-6 pi < 0` (`cap = 22`), no physical UV FP.
- `PF-OW14-4` (omit `lam_s^4` scaling in Kaloper-Padilla): **CAUGHT** — `d(Lam_res) / d(rho_vac) = 1 != 0`.
---

## 4. Dated Correction (`2026-11-22`, `AGY-C25` Findings `S5` & `S6`)

- **`S5` (Unimodular / KP Status Downgraded to `CONDITIONAL`):** While the algebraic identities
  `g_* = 4 pi / 5` and `d(Lam_res)/d(rho_vac) = 0` are exact given `det g = -1` or global
  Kaloper-Padilla variables (`0 < V_4 < infty`), that modified-gravity postulate is imported rather
  than derived from `A2-OW4`/`A2-OW8`'s general-covariant induced gravity. `A2-OW16 v4` moves
  `OBS-11` from `DERIVED_EXACT` to `CONDITIONAL_OR_QUALITATIVE` (`CONDITIONAL_GRAVITY_POSTULATE`).
- **`S6` (Formal Card Erratum Logged):** Sealed card line 58 typo (`7 / 3` instead of exact
  `2 * (22 - 8) / (21 - 8) = 28 / 13`) is now closed by formal dated card erratum
  `relays/cards/AGY-002_A2-OW14-ERRATUM-1_traceless-cap22-theta-g-28-13.md` (`71581e83a`).

---

### Dated Correction (`2026-11-22`, `R-AGY002-V1`)

**2026-11-22 (`R-AGY002-V1` Erratum, `F-A2-05` / `F-A2-12`):** Retracts `verify_a2_ow14_v2.py:537`'s minimal-scalar `0 < 16n - 40` lower bound at conformal `xi = 1/6` (`where 6 C_{grav}(N_gen=3) = 0` for `48` Weyl and `-3` for `45` Weyl; `A2-OW18 v3` `c4b79467c`), and discloses `relays/a2_ow14_referee/a2_ow14_referee_results.json` `all_gates_passed: false` (cataloged in `A2-OW16 v5` `7320b5f19`). The exact `7D -> 4D` radion bound `N_{accel,max} = 0.811376 < 1` stands (`Bridge B-3S-06`).
