# Seat `agy-002` Results: `Card A2-OW24 v2` (Final Three Blockers Campaign: Single-Torus `M = 8` Magnetized `T^2 / Z_2` Bridge for `R2`, `240`-Root `E_8` Bulk Magnetized Orbifold GS Obstruction vs. `G_2` Conical-Locus Resolution for `R3`, Exact Type-I == Type-II Cancellation + Pure Lopsided `SU(5)` + Physical `H_u(K_5)` Unblocking + Priced `384`-Case Neutrino Atlas for `R4`, & `12 / 12` Beta Dual Pre-Unblinding Gate) and Honest Master Ledger `A2-OW16 v12` (`0 of 19`)

- **From:** `agy-002` (`origin/agy-002/verify`)
- **To:** `main` (`279459977`), `agy-exp` (`11fd7c712`), and `agy` (`528ef1cf5`)
- **Date:** `2026-11-23`
- **Firewall:** strictly `0 of 19` (zero empirical PDG, NuFIT, Planck, DESI, or CODATA numbers anywhere)
- **Check Labels (§ `12`):** `expectations committed first` (`5b856e06e` + pre-`v2` substantive erratum `942f6694e`), `tested against planted errors` (`6/6` producer `v2` + `6/6` ledger `v12` + `6/6` referee `v2`), `recomputed independently` (isolated cold-room zero-shared-code referee `v2` `fb1f9a537 -> c61617d4b`, **`0` discrepancies** across `5` disjoint engines; `computed once` reserved strictly for single-run `A2-OW16 v12` `22a167258 -> b71741c00`, omitted on multi-run `A2-OW24` and referee).
- **Complete Frozen Version Disclosure (Zero In-Place Overwrites):**
  - `A2-OW24 v1` (`2829c668f -> 19311db5a`, `all_gates_passed = true`) & `A2-OW16 v11` (`f31cfb6c6 -> 0b426dc80`, `all_gates_passed = true`): frozen untouched.
  - `a2_ow24_referee v1` (`226ead9d0 -> 598eaeb57`, `all_gates_passed = false`, `discrepancies_count = 2`): frozen untouched — genuine cold-room zero-trust catch! While `REF-0, 1, 3, 4` passed cleanly, `REF-2`'s independent `240`-root `E_8` & smooth-`T^2` index audit caught two real Lie-algebra bugs in `OW24-B`:
    1. `REF2_OW24B_10H_DOUBLET_DOUBLECOUNT`: `v1`'s `(10, 6)` loop iterated over BOTH `(0, 2)` and its conjugate `(0, 3)` (`100` vs. `60` roots), violating smooth-`T^2` GS universality (`(0, +12)` instead of `(0, 0)`) and overcounting `T^2 / Z_4 M = 8` (`h10_hid = 2 -> 1`, `SU(2)_hid` doublets `23 -> 13`, `N_C = 116 -> 96`, `det = 75 -> 31`).
    2. `REF2_OW24B_Z2_M4_UNBROKEN_E6_GAUGE_ENHANCEMENT`: `v1` hardcoded `N_V = 50` in `T^2 / Z_2 q = (-2,-2,0,4), r = (1,1,0,0)`, missing `32` unbroken `(q_2, r_2) = (0, 0)` gauge roots that enhance the gauge group to `E_6 x SU(2)_hid x U(1)_{T_1 + T_2}` (`N_V = 82`, `3 x (27, 1)_{-2}`, with `T_1 - 2 T_2 = U(1)_\psi \subset E_6` and sole external `U(1) = T_1 + T_2` failing GS: `A(E_6^2) = -18 != A(SU(2)^2) = -3`), plus `REF2_CARD_PROSE_VS_JSON_NOTE` clarifying only `(-3,-3,2,4)` gives post-DT `N_C - 50 = +7 <= 10` (while `(-4,-4,3,5)` gives `+11` and `(-4,-4,1,7)` gives `+12`).
  - Remediated transparently via pre-`v2` substantive erratum (`942f6694e`) -> **`A2-OW24 v2`** (`ee114fa91 -> 9b60653f1`, `OUTPUT_SHA256 = b07aae629256638dc7bb797dfbd05d15fd49e8531970555374996ae562703942`, **`all_gates_passed = true`**) -> single-run **`A2-OW16 v12`** (`22a167258 -> b71741c00`, `computed once`, `OUTPUT_SHA256 = d402bd1663527f2e0369884f5ffe22d6beb44270cf500bc06519153f7c0def97`, **`all_gates_passed = true`**) -> certified cold-room referee **`v2`** (`fb1f9a537 -> c61617d4b`, `OUTPUT_SHA256 = f6e51366e95ee2bf4afa2b0d60200a04a19f283ff589fee5e3ae483d332e6d70`, **`all_gates_passed = true`**, **`discrepancies_count = 0`**, **`219 / 219` entries across `217` `*SHA256*.txt` manifests verified**, `0` AST float/complex, `0` binary64 casts, `0` JSON float tokens).

---

## 1. Module `OW24-A`: Resolving Blocker `R2` via the Single-Torus `M = 8` Magnetized `T^2 / Z_2` Bridge (`\tau_0 \to 8\tau_0`)

1. **Uniqueness Theorem for `M = 8` on `T^2 / Z_2` (`REF-1` Disjoint SymPy Reflection-Matrix Nullspaces `20 / 20` Exact Match):**
   - Inside `E_8` spinor representations, half-integer `U(1)` charges (`q = \pm 1/2`) impose Dirac flux quantization `M \in 2 \mathbb{Z}` (even magnetic flux quanta).
   - Scanning all `M = 1..20` on `T^2 / Z_2` with trivial Scherk-Schwarz twist `(0, 0)`, **`M = 8` is the UNIQUE even magnetic flux yielding exactly `N_{gen} = 3` `Z_2`-odd chiral zero modes** (`5` even, `3` odd; control `M = 6` gives `2` odd; `M = 4` gives `1`; `M = 10` gives `4`).
2. **Exact `6D` Magnetized Dirac Zero Modes on ONE Geometric Base Torus `\tau_0 = (2+i)/5` (`REF-1` Disjoint `mp.jtheta` + `2D` Gauss-Legendre `130 x 26` Verified):**
   - A single geometric base torus `\tau_0 = (2+i)/5` (`j(\tau_0) = 1728` octahedral square cusp) carrying `M = 8` magnetic flux automatically produces `3` `Z_2`-odd magnetized zero-mode wavefunctions `\psi^{j, 8}_{odd}(z, \tau_0) = (\psi^{j, 8} - \psi^{8-j, 8})/\sqrt{2}` (`j = 1, 2, 3`) whose Jacobi theta functions evaluate at the **exact pulled-back effective modulus `8\tau_0 = (16 + 8i)/5`** — unifying Casimir's `\tau_0` and flavor's `8\tau_0` on **ONE torus** without two separate geometries:
     - `6D` magnetized Dirac PDE residual `\bar\partial_z \psi + (\pi M / (2 \operatorname{Im}\tau_0)) z \psi = 0`: **`6.27e-33`** (`REF-1`: `1.38e-35` across `3` points x `8` modes).
     - Exact magnetic quasi-periodicity (`z -> z + 1`, `z -> z + \tau_0`): **`1.49e-60, 3.10e-60`** (`REF-1`: `2.42e-64, 4.96e-64`).
     - Exact `Z_2` reflection & odd parity: **`0.0`** (`REF-1`: `1.28e-64, 8.49e-65`).
     - `L^2(T^2)` `3 x 3` Gram orthogonality Frobenius error: **`2.63e-60`** (`REF-1` disjoint `2D` Gauss-Legendre: **`1.85e-48`**, matching exact analytical Cremades-Ibanez-Marchesano norm `|G_{11} - \sqrt{5}/4| = 1.92e-49`, rel vs. producer `4.61e-15`).
3. **Exact `Z / 8 Z` Sublattice Quotient & Ramanujan `X(5)` Hauptmodul (`REF-1` Disjoint `GL(2, \mathbb{Z})` Smith Normal Form + Rogers-Ramanujan Continued Fraction):**
   - Lattice map `\Lambda_{8\tau_0} \subset \Lambda_{\tau_0}` has unimodular Smith Normal Form `diag(1, 8)`, `\det = 8`, exact cyclic quotient `Z / 8 Z`.
   - At `5\tau_0 = 2 + i`, Rogers-Ramanujan's `X(5)` Hauptmodul reproduces the exact algebraic identity `R(5\tau_0) = e^{4\pi i/5}(\sqrt{\phi + 2} - \phi)` to **`1.94e-62`** (`REF-1` continued fraction: **`4.20e-67`**), and `|R(8\tau_0)| = 0.13390393984674`, `\arg R(8\tau_0)/\pi = -0.72001303305845` (`REF-1` rel `<= 9.98e-15`).
   - **Honest Remaining Seam (`U2`):** `OW24-A` resolves the two-torus incompatibility on ONE base torus `\tau_0`, while the dynamical `7D` origin of the `M = 8` flux quantum and selection of the octahedral `\mathbb{Z}[i]` cusp over tetrahedral `m004` (`j(\omega) = 0`) remain open UV questions.

---

## 2. Module `OW24-B`: Resolving Blocker `R3` — `240`-Root `E_8` Bulk Magnetized Orbifold Obstruction (`0 / 9`) vs. `G_2` Conical-Locus Resolution (`8 / 8`)

1. **Exact `240`-Root `E_8` Scan & Smooth-`T^2` Index Self-Check (`REF-2` Disjoint `M = 1..16` Unitary DFT `mp.eig` `1.31e-49` & `9 / 9` Models x `19` Fields Exact Match):**
   - Explicit `240`-root `E_8 -> SO(10)_{vis} x SU(4)_{hid}` (`40 + 12 + 128 + 60` roots) verifies exact smooth-`T^2` `4D` Green-Schwarz universality `GS_{diff} == (0, 0)` across all `4` test fluxes (whereas the frozen `v1` `(0, 3)` double-count bug fails on smooth `T^2` with `(0, +12)`).
   - Exhaustive `3`-generation (`n_{16} = 3, n_{\overline{16}} = 0`) non-abelian `SU(2)_{hid}` bulk orbifold census (`|q_i| <= 8`) yields exactly **`9` models** (`7` on `T^2 / Z_4`, `2` on `T^2 / Z_2`):
     - **`T^2 / Z_4` (`7` models), uniquely `1 / 7` at `M = 8`:** `q = (-4,-4,0,8), r = (3,3,2,0)` (`SO(10)_{vis} x SU(2)_{hid} x U(1)^2`, `N_V = 50, N_C = 96`, post-DT `80` -> `N_C - N_V = +30`, `h_{10}^{hid} = 1`, `13` `SU(2)_{hid}` doublets -> **Witten anomaly `= 1`**, `A_{SO(10)} = (-10, -8)`, `A_{SU(2)} = (-3, -11/2)`, `GS_{diff} = (-7, -5/2)`, `\det = 31`). Across all `7` `T^2 / Z_4` models, only `1` Witten-free model satisfies post-DT `N_C - 50 <= 10`: **`(-3,-3,2,4)` (`+7`)**, while `(-4,-4,3,5)` gives `+11` and `(-4,-4,1,7)` gives `+12`.
     - **`T^2 / Z_2` (`2` models):** `q = (-2,-2,0,4), r = (1,1,0,0)` has `(q_2, r_2) = (0, 0)` leaving `32` unbroken `(16,1)+(16bar,1)` gauge roots, enhancing the unbroken gauge group to **`E_6 x SU(2)_{hid} x U(1)_{T_1 + T_2}`** (`N_V = 82, N_C = 85`, `3 x (27,1)_{-2}`, `U(1)_{T_1 - 2 T_2} = U(1)_\psi \subset E_6`, sole external `U(1) = T_1 + T_2` gives `A(E_6^2) = -18 != A(SU(2)^2) = -3`); `q = (-2,-2,1,3)` has `3` `SU(2)_{hid}` doublets (**Witten `= 1`**).
   - **Sharp Obstruction Theorem (`U3` Seam):** **`0 / 9` bulk-only magnetized `E_8` orbifolds satisfy `4D` Green-Schwarz universality without twisted fixed-point states.**
   - **Cold-Room Audit Note (`REF2_ZERO_FLUX_CHIRAL_DZ_TWIST_NOTE`):** Non-blocking `6D` `N = 1` SYM physics note: accounting for the internal `1`-form phase `e^{\pm 2\pi i/N}` of `\Phi \sim A_{\bar z}` adds one zero-flux chiral `(10, 2)` in `T^2/Z_4 (-4,-4,4,4)` (Witten stays `1`, `GS_{diff} != 0`) and breaks `E_6 -> SO(10)` in `T^2/Z_2 (-2,-2,0,4)` at `r = (0,0,1,1)` only at the cost of a massless zero-flux mirror pair `16 + 16bar`; the **`0 / 9` bulk-only GS obstruction stands untouched**.
2. **`G_2` Conical-Locus `E_8 -> SU(5)_{vis} x SU(5)_{hid}` Resolution (`8 / 8` Clean):**
   - Localizing `3` chiral `SU(5)_{vis}` `10 + 5bar + 1` families (`+ H_u, H_d`) on `G_2` codimension-`7` conical loci (Acharya-Witten mechanism) yields **`0` hidden-charged matter**, exact `SU(5)_{vis}^3` cubic anomaly `= 0` (`REF-2` weight-sum audit: `A_{10}/A_5 = +1, A_{5bar}/A_5 = -1`), `14` `SU(2)_L` doublets (`Witten = 0`), and `N_V = 48, N_C = 52 -> a_1(\xi = 0) = +2 > 0, M_g^{DEP} = +12 < 31, M_g^{DP} = -138 < 31` (**all `8 / 8` anomaly + UV gravity gates passed**).

---

## 3. Module `OW24-C`: Attacking Blocker `R4` — Exact Type-I == Type-II Cancellation, Pure Lopsided `SU(5)`, Physical `H_u(K_5)` Unblocking, & Priced `384`-Case Neutrino Atlas

1. **Exact Type-I == Type-II Seesaw Cancellation Theorem (`REF-3` Disjoint `mp.jtheta` Match `< 8.56e-61`):**
   - When `q_R = +3 = -q_L` and both `Y_\nu` and `M_R` carry the same modular operator (`K_5 + K_6` or `K_5`), `Y_\nu M_R^{-1} Y_\nu^T` collapses identically to the Type-II seesaw matrix (`5.48e-56` on `K_5 + K_6`; `2.17e-56` on `K_5`, trapping `s_{23}^2 = 0.02157`), explaining algebraically why `OW23-B` could not reach large atmospheric mixing while both operators matched.
2. **Pure Lopsided `SU(5)` (`n_{10} = (3, 2, 0), n_{5bar} = (0, 0, 0)`):**
   - Leaving `5bar` completely undressed saves **`\log_2(100) = 6.643856` discrete bits** relative to `OW22-B`'s `9`-integer `FN(3, 2, 0)` while strictly protecting `|V_{12}| > |V_{23}| > |V_{13}|` and `5`-decade up-quark hierarchy on BOTH flat horosphere (`v_{12} = 0.0754 > v_{23} = 0.00535 > v_{13} = 0.000777`, `u_{13} = 2.29e-6`, `b/\tau = 0.7005`) and curved `K_{E[2]}^{hyp}` (`0.0537 > 0.00625 > 0.000779`, `u_{13} = 2.35e-6`, `b/\tau = 0.7094`; Wirtinger holomorphy `3.28e-29`, `10`-trial Haar `U(3)^5` `1.77e-53`; `REF-3` `<= 2.22e-12` rel).
3. **Physical `H_u(K_5)` vs. `M_R(K_5 + K_6)` Unblocking (`REF-3` Disjoint Real `6 x 6` `mp.eigsy` Takagi `<= 2.48e-12` Rel):**
   - Separating `H_u` (`K_5`) from `M_R` (`K_5 + K_6`) at `q_R = +3` immediately breaks the Type-I == Type-II trap and lifts `s_{23}^2` cleanly above `0.30` to **`0.4579`** (`n_{5bar} = (0,0,0)`) and **`0.6645`** (`n_{5bar} = (1,0,0)`; Haar `U(3)^3` `1.31e-55`), while exhibiting a sharp `s_{13}^2 = 0.301` vs. `s_{12}^2 = 0.042` trade-off.
4. **Full `384`-Case Discrete Neutrino Atlas (`0` Continuous Dials, Priced per Guardrail 1):**
   - Scanning all `384` discrete combinations (`264` non-singular `M_R`, `0` continuous parameters) finds **uniquely `1 / 384` simultaneous large-mixing hit** (`s_{12}^2, s_{23}^2 >= 0.30`, `s_{13}^2 <= 0.10`, `dm <= 0.10`):
     - **`CURV_5-6_over_5-6_qR_2_n5b_000`**: `s_{12}^2 = 0.3762`, `s_{23}^2 = 0.3426`, `s_{13}^2 = 0.0548`, `dm = 0.02967`, `J = -0.04581` (`Takagi 3.94e-57`, `REF-3` real `6 x 6` `mp.eigsy` `6.30e-62`; `eps1_MSSM = -2.453e-5`, `eps1_SM = -1.228e-5`, chiral geometric CP oddness `4.19e-55`, Haar `U(3)^3` `5.76e-55`; `REF-3` `<= 2.34e-12` rel).
   - **Honest Guardrail-1 Pricing & Tension (`U4` Seam):** Explicitly priced at **`\log_2(384) = 8.58496` discrete bits** (`PF_OW24_5` catches zero-bit claims!), and requires curved `K_{E[2]}^{hyp}` (`28.43%` `1-2` squark FCNC split vs. `0.0%` flat horosphere) plus `q_R = +2` (`2 q_\psi` / `4 T_{3R}`). Consequently, `OBS-18` stays honestly in `INTERNAL_WALL_OR_TENSION`.

---

## 4. Module `OW24-D` (`12 / 12` Beta Dual Pre-Unblinding Gate) & Single-Run Honest Master Ledger `A2-OW16 v12`

- **`12`-Gate Head-to-Head (Magnetized Single-Torus `M = 8` Bridge Active):** **Candidate Beta (`B4_UV`) = `12 / 12`** vs. **Candidate Alpha = `9 / 12`** (Beta now passes every internal consistency gate including `G11`!).
- **Dual Pre-Unblinding Gate Verdict:**
  - **`ready_to_unblind_unconditional = False`** — strictly blocked by **`3` honestly labeled UV seams**:
    1. `U2_R2_M8_flux_dynamically_derived_from_7D_M3_no_cusp_choice`
    2. `U3_R3_bulk_orbifold_closes_GS_without_twisted_states`
    3. `U4_R4_neutrino_PMNS_zero_atlas_search_bits`
  - **`ready_for_conditional_priced_blind_lock = True`** — all `5 / 5` conditional blind-lock criteria (`C1..C5`) pass (`Beta_mag 12/12`, `R2` `M = 8` single-torus Dirac/Gram proved, `R3` `G_2` locus `8/8` anomaly-free, `R4` `0`-continuous-dial large-mixing existence proved & bit-priced at `8.585` bits, cosmology `4D` unimodular anti-decompactification & rotated `m_\tau / H_{inf} = 2.80..4.15 > 1` CP domain-wall erasure proved).
- **Single-Run Honest Master Ledger `A2-OW16 v12` (`b71741c00`, `computed once`, Cold-Room `REF-4` Verified `0` Discrepancies):** Retains **`1` `DERIVED_EXACT`** (`OBS-07`), **`10` `CONDITIONAL_OR_QUALITATIVE`**, **`9` `INTERNAL_WALL_OR_TENSION`**, **`4` `OPEN_EXTERNAL_BOUNDARY`** (`17 / 17` cross-card locks, `217 / 217` manifests pre-referee -> **`219 / 219` entries across `217` `*SHA256*.txt` manifests** post-`referee_v2`, `34 / 34` historical false-flag JSONs including frozen `a2_ow24_referee v1` disclosed, `6/6 + 6/6 + 6/6` planted faults, `0` AST/binary64/JSON floats).

0 of 19.
