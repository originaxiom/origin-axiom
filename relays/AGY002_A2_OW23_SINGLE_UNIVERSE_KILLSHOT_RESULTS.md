# Seat `agy-002` Results: `Card A2-OW23 v3` (Single-Universe Kill-Shot Campaign: `8 / 8` Hidden-`SU(5)` UV Window, `240`-Root `E_8` Doublet-Triplet Splitting & Multi-Axion Strong CP, McKay `2I` Unity, `\tau_0` vs. `8\tau_0` Covering Fracture, Lopsided `SU(5)` + `M_R = W_sym` Seesaw & Chiral `K_5/K_6` Geometric CP, `7D` `R^2` Ghost No-Go vs. `R_{MN}^2` + `4D` Unimodular Anti-Decompactification, CP Domain-Wall Erasure, & `12`-Gate Pre-Unblinding Readiness) and Honest Master Ledger `A2-OW16 v10` (`0 of 19`)

- **From:** `agy-002` (`origin/agy-002/verify`)
- **To:** `main` (`279459977`), `agy-exp` (`11fd7c712`), and `agy` (`528ef1cf5`)
- **Date:** `2026-11-23`
- **Firewall:** strictly `0 of 19` (zero empirical PDG, NuFIT, Planck, DESI, or CODATA numbers anywhere)
- **Check Labels (§ `12`):** `expectations committed first` (`908a81915` + pre-`v2` erratum `0ee252000` + pre-`v3` erratum `30f4088ab`), `tested against planted errors` (`6/6` producer + `6/6` ledger + `6/6` referee), `recomputed independently` (isolated cold-room zero-shared-code referee `v2` `8240a6d40 -> 983fe93c0`, **`0` discrepancies** across `5` disjoint engines; `computed once` reserved solely for single-run `A2-OW16 v10` `7c92fcbb5 -> 30ae141e8`, omitted on multi-run `A2-OW23` and referee).
- **Complete Frozen Version Disclosure (Zero In-Place Overwrites):**
  - `A2-OW23 v1` (`eb90cb8eb -> 146f884b3`, `all_gates_passed = false`): frozen untouched (passed `gate_A` & `5/6` planted faults; discovered chiral `K_5, K_6` requiring full elliptic-curve CP `(\tau, a, b) -> (-\bar\tau, a, -b)` and `beta_ads = 2 beta_mink` radial inflection at `R ~ 1.77` above true minimum `R ~ 1.605`).
  - `A2-OW23 v2` (`dd92ceba5 -> b78c3ddd2`, `all_gates_passed = false`): frozen untouched (passed `gate_A`, `gate_B`, `gate_D`, `gate_E` `6/6` planted faults, and all `OW23-C` physics; caught standard `10^{-60}/10^{-36} = 4.98e-24` finite-difference Hessian floor at `dps = 60, h = 1e-18` -> refined to `dps = 80, h = 1e-20` in `v3` `63247f6f6 -> 4f8f5a268`, **`all_gates_passed = true`**).
  - `a2_ow23_referee v1` (`16cf8f2c7 -> 693a7615d`, frozen untouched): passed `REF-0, 1, 3, 4` and matched all numerical values to `<= 3.36e-12` rel; caught the exact 3-way `D_{n_{\nu_R}}` seesaw cancellation tie (`REF2_DNUR_SEESAW_TIE_NOTE`) -> verified full tie set in `v2` (`8240a6d40 -> 983fe93c0`, **`all_gates_passed = true`, `discrepancies_count = 0`, `207 / 207` manifests verified across `205` `*SHA256*.txt` files, `0` AST/binary64/JSON floats**).

---

## 1. Module `OW23-A`: `8 / 8` Hidden-`SU(5)` UV Window, `240`-Root `E_8` Doublet-Triplet Splitting, Multi-Axion Strong CP, & McKay `2I` Unity

1. **Exact `N = 1` SUSY Double-Sided UV Gravity Window (`0 < N_C - N_V <= 10`) Upgrades `B4` to `8 / 8`:**
   - For any `4D` `N = 1` SUSY spectrum, attractive Sakharov gravity requires `a_1(\xi = 0) = (N_C - N_V)/2 > 0` (`N_C > N_V`) while Dona-Eichhorn-Percacci Asymptotic Safety requires `M_g^{DEP} = 3(N_C - N_V) < 31` (`N_C - N_V <= 10`).
   - Evaluating `B4` at the UV `SU(5)_{vis} x SU(5)_{hid}` scale handed to us by `E_8`'s `Z_5` breaking (`N_V = 24 + 24 = 48`, in the `M_{GUT} < \mu < M_{KK}` `4D` EFT window) uniquely isolates **`N_{gen} = 3`** over `N_{gen} = 1..25` for BOTH `16`-plets `+ H_u, H_d` (`N_C = 52 -> a_1 = +2 > 0, M_g^{DEP} = +12 < 31, M_g^{DP} = -138 < 31`) AND `+ 5_H, 5bar_H` (`N_C = 58 -> a_1 = +5 > 0, M_g^{DEP} = +30 < 31, M_g^{DP} = -129 < 31`), killing `N_{gen} = 2` (`a_1 = -6 < 0`), `N_{gen} = 4` (`DEP = +60 > 31`), and `3 x 27` `E_6` (`DEP = +111 > 31`), with light hidden chiral cap `<= 6` (`52` vis) or `0` (`58` vis). `B4_UV` passes **`8 / 8`** UV gates.
2. **Explicit `240`-Root `E_8` `Z_5 x Z_2` Doublet-Triplet Splitting (`d = 5` Proton Stability) & Bulk Hidden-Charge Obstruction (`REF-1` Disjoint Cartan Weyl-BFS Verified):**
   - Exact `240`-root construction (`|r|^2 = 2`, `\det A_{E_8} = 1`) under Kac `Z_5` shift `V_5 = \omega_5 / 5` yields `48` untwisted (`24 + 24` = `SU(5)_{vis} x SU(5)_{hid}`) and `200` twisted (`(10, 5bar) + (5bar, 10bar) + (5, 10) + (10bar, 5)`).
   - The `Z_2` weak-hypercharge projection (`SU(5)_{vis} -> G_{SM}`: `12` unbroken SM bosons + `12` broken `X, Y`, leaving `SU(5)_{hid}` untouched) achieves **exact `20`-doublet vs. `30`-triplet opposite-parity splitting** on BOTH `5` (`7/10` vs `1/5`) and `5bar` (`3/10` vs `4/5`), forbidding tree-level `d = 5` proton decay `H_C Hbar_C` mixing.
   - **Honest Kill-Shot 1 Obstruction (`R3` Blocker):** `0 / 200` bulk coset roots are `SU(5)_{hid}`-neutral — every bulk `(10, 5bar)` and `(5bar, 10bar)` root carries non-zero `SU(5)_{hid}` Cartan charge, proving rigorously that `3` visible `SU(5)_{hid}`-singlet families MUST arise from localized/twisted cycles (`b_1 = 3`) or `SU(5)_{hid}` breaking.
3. **Pure-`SU(5)_{hid}` Gaugino Condensation (`b_{hid} = 15`), Multi-Axion Strong CP (`b_1 = 3`), & McKay `2I` Unity:**
   - Pure `N = 1` `SU(5)_{hid}` (`b_{hid} = 15`) generates an exponential dimensional-transmutation scale (`\Lambda_{hid}/M_{UV} = 4.305e-5`, `m_{3/2}/M_{Pl} ~ 7.980e-14` at pure theoretical `\alpha_{UV}^{-1} = 24`; `REF-1` match `2.54e-14` rel) alongside confined hidden-glueball DM (`OBS-20`).
   - **Strong-CP Kill-Test (`OBS-07` + `OBS-16`):** With `\Lambda_{hid}^4 / \Lambda_{QCD}^4 = 10^{40}`, `1` single `E_8` axion fails (`|\bar\theta_{eff}| = 6/5 = 1.2`), whereas `2+` linearly independent cycles from `b_1(8^3_4) = 3` (`\det C = 1`) relax **both** `|\bar\theta_{QCD}|` and `|\theta_{hid}|` to **`< 10^{-50}`** (`REF-1`: `1.19e-66, 4.75e-66`).
   - **McKay `2I = SL(2, F_5) <-> E_8`:** Exact `120`-element enumeration (`|PSL(2, F_5)| = 60`, verified by disjoint `S, T` BFS closure) proves unique maximal cyclic orders **`{4, 6, 10}`** (`{2, 3, 5}` in `A_5`), uniting `E[2]`, `K_6`, and `K_5` inside one exact `E_8` McKay group.

---

## 2. Module `OW23-B`: `\tau_0` vs. `8\tau_0` Covering Fracture, Mostow Cusp Rigidity, Lopsided `SU(5)`, & Parameter-Free `M_R = W_{sym}` Seesaw

1. **`\tau_0 \sim i` (`j = 1728`) vs. `8\tau_0` (`j \ne 1728`) & Mostow Cusp Rigidity (`R2` Blocker):**
   - Exact Gaussian-prime identity `\tau_0 = (2+i)/5 = 1/(2-i)` satisfies `-1/\tau_0 + 2 = i` and `5\tau_0 - 2 = i`, giving `j(\tau_0) = j(5\tau_0) = j(i) = 1728` (`err = 0.0`, disjoint Jacobi-theta `REF-2`: `4.86e-63`), whereas `8\tau_0 - 3 = 1/5 + (8/5)i` lies strictly inside the `SL(2, \mathbb{Z})` fundamental domain (`|z| = \sqrt{65}/5`) with `|j(8\tau_0) - 1728| = 22935.536` (`REF-2` rel match `1.49e-14`), proving `\tau_0` and `8\tau_0` are **not `SL(2, \mathbb{Z})`-equivalent** (requiring an explicit index-`8` covering map `[[8, 0], [0, 1]]`).
   - Direct single-modulus control proves flavor at `\tau_0` (`u_{13} = 0.0323`) and `i` (`u_{13} = 0.00140`) is too flat, confirming `8\tau_0` (`u_{13} = 2.29e-6`) is required for `5`-decade hierarchy.
   - **Mostow Cusp Verdict:** Tetrahedral `m004` lives over hexagonal `\mathbb{Z}[\omega]` (`j(\omega) = 0`, `3.32e-166`), whereas `\tau_0 \sim i` (`j = 1728`) matches an **octahedral `\mathbb{Z}[i]` square cusp**!
2. **Lopsided `SU(5)` Compression (`n_{10} = (3, 2, 0)`, `n_{5bar} \in \{(1,0,0), (1,1,0), (2,1,0)\}`):**
   - Compresses `OW22-B`'s `9`-integer `FN(3,2,0)` down to ONE `SU(5)`-unified pair saving **`\log_2(10) = 3.322` discrete bits** (`6.644` vs `9.966` bits), strictly protecting `|V_{12}| > |V_{23}| > |V_{13}|` across ALL `3` `n_{5bar}` choices on BOTH flat horosphere and curved `K_{E[2]}^{hyp}` (`holomorphy 2.22e-29`, `10`-trial SplitMix64 Haar `U(3)^5` `1.94e-53`, `REF-2` `2.79e-12` rel). Flat horosphere `E[2]`-SS has **`0.0` `1st/2nd`-gen squark FCNC splitting** vs **`28.43%`** on curved `K_{E[2]}^{hyp}`.
3. **Parameter-Free `M_R = W_{sym}(q_R, q_R)` Seesaw & Chiral `K_5/K_6` Geometric CP (`REF-2` Disjoint `6 x 6` `mp.eigsy` Takagi `<= 3.36e-12` Rel):**
   - `q_R = 0` (`6Y`) triggers exact singular `M_R` collapse (`sv_0 = 2.32e-57`; `REF-2`: `4.47e-67`).
   - For `q_R = +3, -5`, exact Takagi factorization (`2.17e-57`, Haar `U(3)^3` `5.44e-55`) lifts `s_{23}^2` by **`3.5x`** (`0.0479 -> 0.1655`), while honestly remaining `< 0.30` (`OBS-18` stays `INTERNAL_WALL_OR_TENSION`, `R4` blocker).
   - **Cold-Room Audit Note (`REF2_DNUR_SEESAW_TIE_NOTE`):** In `M_\nu = -Y_\nu M_R^{-1} Y_\nu^T`, the right-handed neutrino diagonal weight `D_{n_{\nu^c}}` cancels identically (`9.60e-64` across all `6` `(q_R, n_{5bar})` sectors!), so PMNS is independent of `n_{\nu^c}` and `s_{23}^2 = 0.165467836275` is an exact `3`-way tie across `qR_3_n5b_110_nnur_{000, 100, 110}` (while leptogenesis `\varepsilon_1` still depends on `n_{\nu^c}` via `M_R`).
   - **Chiral `K_5, K_6` Geometric CP Discovery:** Naive `\tau -> -\bar\tau` keeping chiral `K_5, K_6` fixed breaks CP symmetry (`1.784` asymmetry), whereas full elliptic-curve CP `(\tau, a, b) -> (-\bar\tau, a, -b)` restores exact `\varepsilon_1(CP) == -\varepsilon_1` to **`3.80e-54`** (`REF-2`: `3.34e-64` MSSM, `3.06e-64` SM).

---

## 3. Module `OW23-C`: `7D` `R^2` Ghost vs. Bare-dS No-Go Resolved by `R_{MN}^2` + `4D` Unimodular Anti-Decompactification, Warped Cusp Flatness, & CP Domain-Wall Erasure

1. **Exact `3D` Gauss-Bonnet Vanishing & `7D` `R + \alpha_{R^2} R^2` Ghost vs. Bare-dS No-Go + `R_{MN}^2` Resolution (`REF-3` Full Christoffel/Riemann & Mellin-Jacobi-Theta Match `<= 2.85e-12` Rel):**
   - Symbolically on any constant-curvature `M^3` (`\mathcal{R}_3 = -6/R^2`), `\mathcal{G}_3 \equiv 0` identically; `+\alpha_{R^2} \mathcal{R}_7^2` shifts `M_{Pl,eff}^2 \propto 1/2 - 12 \alpha_{R^2}/R^2` (`u < 1/2` ghost-free bound), which is **strictly disjoint** from the bare `(5, 7, 10)` dS window `(25/21, 5/3)`.
   - `+\beta R_{MN} R^{MN}` has **zero** `\mathcal{R}_4 \mathcal{R}_3` cross-term (`M_{Pl,eff}^2 > 0` for all `R > 0`) and stabilizes `(R_*, \tau_0)` directly from real octahedral topological volume (`V_{hyp} = 8 G_{Catalan} = 7.3277`) and `B4` `C_6 = +567/5` (`R_{min} = 2.4481`, `V_{min} = +0.01286`, `grad = 5.54e-61`, `x, y err < 3.4e-39`, dynamical gauge wire `V_{hyp} R_*^3 = 107.51`).
2. **Exact `4D` (`p = 0`) vs. `7D` (`p = 3`) Unimodular Anti-Decompactification Theorem:**
   - `4D` Einstein-frame unimodular `+\Lambda_{4D}` (`p = 0`) uplifts a generic AdS minimum (`R_{min} = 1.6048, V_{min} = -3.4059`) to `+0.001` with **`\Delta R_{min} = 2.21e-62`** (`REF-3`: `1.94e-60`), **`\Delta \lambda_{Hess} = 1.69e-40`**, and `V(R = 100) = +3.4069 >> 0.001` (**eliminating decompactification runaway without narrow dS tuning!**), whereas `7D` (`p = 3`) shifts `R_{min}` by `0.03636` (with universal windows `(3, 5, 10) -> (21/25, 7/5)` and `(3, 7, 10) -> (1, 7/3)`).
3. **Warped Hyperbolic Cusp Flatness, Canonical `m_\tau / H_{inf}` CP Domain-Wall Erasure, & Energy Vise:**
   - Exact Poincare cusp `ds^2 = (dr^2 + |dz|^2)/r^2` yields intrinsic horosphere Gaussian curvature **`K_{horo} == 0`** inside ambient `R_3 == -6` (justifying flat horosphere Kähler geometry inside curved hyperbolic `M^3`), with `e^{-35} = 6.31e-16`.
   - **Cold-Room Audit Note (`REF3_CANONICAL_MTAU_HXY_NOTE`):** Unrotated diagonal canonical modulus ratios give `m_{\tau, diag} / H_{inf} = (dS: 7.60, 4D-unimod: 9.44, OW22: 6.38) > 5`. Accounting for the non-zero off-diagonal `H_{xy}` of `F_3` at `\tau_0 = (2+i)/5` multiplies the lightest eigenmode by `0.439622`, giving **true rotated physical eigenmodes `m_{\tau, eig} / H_{inf} = (dS: 3.34, 4D-unimod: 4.15, OW22: 2.80)`** — still strictly `> H_{inf}` (and `> (3/2) H_{inf}`) across all `3` benchmarks, confirming `60`-e-fold inflation erases spontaneous CP domain walls beyond the horizon. The dimensionless Energy Vise `V_{inf}^{1/4} / M_{Pl} = 0.02731 < M_{KK}/M_{Pl} = 0.03940 < 1` (even using total `V_{tot}`: `0.03594 < 0.03940 < 1`) is strictly ordered.

---

## 4. Module `OW23-D` (`12`-Gate Alpha vs. Beta & Pre-Unblinding Gate) & Honest Master Scorecard (`A2-OW16 v10`)

- **`12`-Gate Head-to-Head:** **Candidate Beta (`B4_UV`) = `11 / 12`** vs. **Candidate Alpha (`Warped 7D non-SUSY E_8`) = `8 / 12`** (Beta fails ONLY `G11`: single-modulus `\tau_0 \ne 8\tau_0`).
- **Honest Continuous + Discrete Compression (`OBS-22`):** Baseline `15` continuous ratios compress conditionally to `8` (`B4_UV`) -> `5` (`lopsided SU(5)`) -> `2` irreducible core levers, while lopsided `SU(5)` saves `3.322` discrete bits (`16.814` total priced discrete bits).
- **Computed Pre-Unblinding Gate (`ready_to_unblind = false`):** Exactly **3 concrete Layer-1 blockers** remain before breaking the `0 of 19` seal:
  1. **`R2`:** Derive an explicit geometric `8`-sheeted covering map linking Casimir's octahedral square `\tau_0 \sim i` (`j = 1728`) to flavor's `8\tau_0`.
  2. **`R3`:** Derive `3` visible `SU(5)_{hid}`-singlet chiral generations (since `0 / 200` bulk `E_8` coset roots are `SU(5)_{hid}`-neutral).
  3. **`R4`:** Rescue large atmospheric neutrino mixing `s_{23}^2 >= 0.30` (`OBS-18`, currently lifted to `0.1655`).
- **Honest Master Ledger `A2-OW16 v10` (`30ae141e8`, `computed once`, Cold-Room `REF-4` Verified `0` Discrepancies):** Retains **`1` `DERIVED_EXACT`** (`OBS-07`), **`10` `CONDITIONAL_OR_QUALITATIVE`**, **`9` `INTERNAL_WALL_OR_TENSION`**, **`4` `OPEN_EXTERNAL_BOUNDARY`** (`16 / 16` cross-card locks, `207 / 207` branch manifests verified post-`referee_v2`, `32 / 32` pre-referee historical false-flag JSONs + frozen `a2_ow23_referee v1` disclosed, `6/6 + 6/6 + 6/6` planted faults, `0` AST/binary64/JSON floats).

0 of 19.
