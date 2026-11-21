# Pre-Registration Card: `AGY-002_A2-OW10` — 4D Asymptotic Safety FRG Double-Pincer Selection (`0 < N_S + N_W - 4 N_V < 14`), Stelle Spin-2 Pole & `a`-Theorem Flow, and Master Open-Weave ToE Scorecard (`0 of 19`)

- **Seat:** `AGY-002` (`agy-002/verify`)
- **Card ID:** `A2-OW10`
- **Empirical Firewall:** Strict `0 of 19` (literature benchmarks of Litim 2004 `PRL 92 201301` and Dona-Eichhorn-Percacci `arXiv 1311-2898` isolated strictly inside Guardrail 4 verification gates; zero empirical PDG inputs).
- **Prerequisite Custody:** Builds on `A2-OW1..A2-OW9` (`f1f876162` on `origin/agy-002/verify`), completing the four-wall Open-Weave Endgame Campaign.

## 1. Scientific Objective & Hypotheses Committed Before Run

This card settles Hard Wall 4 (4D UV quantum gravity completion of the open-weave `(8, 48, 12)` `2H` spectrum via Functional Renormalization Group Asymptotic Safety, perturbative Stelle spin-2 pole & `a`-theorem unitarity diagnostics) and synthesizes the final honest Master Open-Weave ToE Scorecard across `A2-OW1..A2-OW10`:

1. **Guardrail 4 FRG Benchmark Gate & Exact Double-Pincer Selection Theorem (`OW10-A`):**
   - Implement the exact `d = 4` harmonic-gauge Litim-regulated Einstein-Hilbert + minimally coupled matter FRG beta-function system (`Litim 2004 PRL 92 201301`, `Dona-Eichhorn-Percacci arXiv 1311-2898`):
     - `u = 1 - 2 lam`, `M_g = N_S + f_W N_W - 4 N_V` (`f_W = 1` for covariant Type-II Lichnerowicz `D_slash^2 = -nabla^2 + R / 4`, matching `A2-OW4`'s exact `S^4` heat kernel; `f_W = 2` for Type-I `-nabla^2`), `M_l = (N_S - 2 N_W + 2 N_V) / 2`.
     - `B_1(lam) = (1 / (6 pi)) * [ 10 / u - 18 / u^2 - 14 + M_g ]`, `B_2(lam) = (1 / (6 pi)) * [ -5 / (2 u) + 3 / u^2 ]`, `eta_N = g B_1 / (1 - g B_2)`.
     - `beta_g = (2 + eta_N) g`, `beta_lam = (eta_N - 2) lam + (g / (2 pi)) * [ 5 (1 - eta_N / 6) / u - 4 + M_l ]`.
   - Derive and verify the exact integer cubic polynomial reduction of the `eta_N = -2` UV fixed-point locus in `u = 1 - 2 lam_* > 0`:
     - `2 (M_g - 14) u^3 + (82 - 2 M_g - 6 M_l) u^2 - 118 u + 48 = 0`, with `g_* = -12 pi u^2 / ((M_g - 14) u^2 + 15 u - 24) > 0`.
   - **Pass bar `OW10-A`:**
     - **Guardrail 4 Pure-Gravity Benchmark (`N_S = N_W = N_V = 0`):** Unique UV-attractive fixed point reproducing `Litim 2004 PRL 92 201301` to `>= 5` significant figures: `|g_* - 70732 / 10^5| < 1 / 10^5`, `|lam_* - 19320 / 10^5| < 1 / 10^5`, complex critical exponents `|Re(theta) - 14753 / 10^4| < 1 / 10^4`, `|Im(theta) - 30432 / 10^4| < 1 / 10^4`, and `max(|beta_g|, |beta_lam|) < 1 / 10^30`.
     - **Guardrail 4 Pure-Fermion Bound (`N_S = N_V = 0, N_W = 2 N_D`):** Reproduces `Dona-Eichhorn-Percacci arXiv 1311-2898` cutoff dependence: Type-II (`f_W = 1`) survives through `N_D = 6` (`M_g = 12`) and collapses at `N_D = 7` (`M_g = 14`, `0` UV FPs); Type-I (`f_W = 2`) survives through `N_D = 3` (`M_g = 12`) and collapses at `N_D = 4` (`M_g = 16`, `0` UV FPs).
     - **Exact Double-Pincer Selection Theorem (`A2-OW4` + `A2-OW10`):**
       - Lower bound (`A2-OW4` attractive 1-loop Sakharov gravity `C_grav > 0` for `xi < 1/6`): `M_g = N_S + N_W - 4 N_V > 0`.
       - Upper bound (`A2-OW10` Type-II Asymptotic Safety existence for fermion-dominated `M_l < 0`): `M_g = N_S + N_W - 4 N_V < 14`.
       - At `N = 5, 2H` (`N_S = 8, N_V = 12, N_W = 16 N_gen`): `0 < 8 + 16 N_gen - 48 < 14 <=> 5 / 2 < N_gen < 27 / 8` **uniquely selects `N_gen = 3`** (`N_gen = 1, 2` violate `M_g > 0`; `N_gen = 4` violates `M_g < 14` with `0` UV FPs).
       - At `N = 5, N_gen = 3` (`N_W = 48, N_V = 12, N_S = 4 n_H`): `0 < 4 n_H < 14` restricts Higgs doublets to `n_H in {1, 2, 3}` (`n_H = 4` has `M_g = 16 > 14` and `0` UV FPs).
       - Across all `21` faithful transitive actions of `Delta(2, 3, N)` (`N = 2..5, d <= 12`, reconstructed directly from `A2-OW4`'s permutation groups), **`N = 5, d = 5` (`A_5 / A_4`, `(8, 48, 12)`, `M_g = +8`) is the UNIQUE action (`1 of 21`) simultaneously chiral, anomaly-free, Sakharov-attractive (`M_g > 0`), and Type-II asymptotically safe (`M_g < 14`)**.
       - For open-weave `N = 5, 2H` `(8, 48, 12)` in Type-II (`f_W = 1`): unique UV-attractive fixed point `7 < g_* < 71 / 10`, `-101 / 10 < lam_* < -10`, both stability exponents real and positive (`Re(theta_1), Re(theta_2) > 2`, specifically `21 / 10 < theta_2 < 22 / 10`, `39 / 10 < theta_1 < 4`), residual `< 1 / 10^30`.
       - **Honest Caveats Certified:** In Type-I (`f_W = 2`), both `(8, 48, 12)` (`M_g = +56`) and SM `1H` `(4, 45, 12)` (`M_g = +46`) yield `0` UV FPs (proving covariant Lichnerowicz `D_slash^2` is mandatory); and even in Type-II, `g_* > 7` and `lam_* < -10` sit in the strong single-metric coupling regime, so higher-order/bi-metric truncation stability remains open.

2. **Stelle Quadratic-Gravity Spin-2 Ghost Pole & Komargodski-Schwimmer `a`-Theorem Flow (`OW10-B`):**
   - Using `A2-OW4`'s exact trace-anomaly formulas `c = N_S / 120 + N_W / 40 + N_V / 10`, `a = N_S / 360 + 11 N_W / 720 + 62 N_V / 360`, and scalar `R^2` coefficient `b_R ~ N_S (xi - 1 / 6)^2`:
   - **Pass bar `OW10-B`:**
     - Exact `(c, a) = (37 / 15, 127 / 45)` for `2H` `(8, 48, 12)` and `(73 / 30, 253 / 90)` for `1H` `(4, 48, 12)`.
     - At conformal coupling `xi = 1 / 6`, `b_R = 0` identically (zero 1-loop induced `R^2` scalaron); because `c = 37 / 15 > 0`, the 1-loop induced `C^2` coupling `alpha_W > 0` produces the exact Stelle partial-fraction identity `1 / (x (1 + x)) = 1 / x - 1 / (x + 1)` verified in exact `Fraction` arithmetic at `x in {1 / 3, 1, 5}` -> **strictly negative residue `-1` massive spin-2 ghost pole at `M_2^2 = M_Pl^2 / (2 alpha_W)`** in perturbative 4D quadratic gravity (requiring non-perturbative FRG or `7D` bulk UV completion).
     - Exact Komargodski-Schwimmer `a`-theorem ladder across `6` EFT decoupling stages from `N = 5, 2H` down to deep IR (`gamma + 3 nu_L`):
       1. `UV (8, 48, 12)`: `c = 37 / 15`, `a = 127 / 45`
       2. `SM 1H + 3 nu^c (4, 48, 12)`: `c = 73 / 30`, `a = 253 / 90`, `Delta a = +1 / 90 > 0`
       3. `SM 1H below M_R (4, 45, 12)`: `c = 283 / 120`, `a = 1991 / 720`, `Delta a = +11 / 240 > 0`
       4. `Below EW (QCD + QED, 39 W, 9 V)`: `c = 15 / 8`, `a = 103 / 48`, `Delta a = +223 / 360 > 0`
       5. `Below QCD (QED + 3 pions + e + 3 nu: 3 S, 5 W, 1 V)`: `c = 1 / 4`, `a = 37 / 144`, `Delta a = +17 / 9 > 0`
       6. `Deep IR (gamma + 3 nu_L: 0, 3, 1)`: `c = 7 / 40`, `a = 157 / 720`, `Delta a = +7 / 180 > 0`
       - Verify `5 / 5` consecutive positive drops and total `Delta a_total = 125 / 48 > 0`.

3. **Master Open-Weave ToE Scorecard (`OW10-C`, `A2-OW1..A2-OW10`):**
   - Assemble a machine-verified `12`-row Master Open-Weave ToE Scorecard classifying every sector of SM + Gravity + Cosmology across `A2-OW1..A2-OW10` into exact disjoint statuses: `PROVED` (`5` rows: Gauge/Chiral/Anomaly Engine `A2-OW1/A2-OW4`; `N = 5` & `N_gen = 3` Double-Pincer Selection `A2-OW4/A2-OW10`; `6D -> 7D` Chirality & Inflow `A2-OW5`; `X_0(5)` Dynamical Casimir Stabilization of `tau_*^{+-}` & Positive dS Sign `A2-OW2/A2-OW9`; Conformal `xi = 1/6` Attractive Finite Gravity & `2H` Radiative EWSB Mechanism `A2-OW3/A2-OW8`), `PARTIAL / CONDITIONAL` (`3` rows: Flavor Hierarchies/CKM/CP via `7D` QR-Decoupling with `log_2(6)` Perm Cost `A2-OW6/A2-OW7`; Dark Matter LKP Conditional on `E[2]` Democracy with Zero-Mode `nu^c` Ruled Out `A2-OW9`; 4D Asymptotic Safety Conditional on Type-II Cutoff & Strong-Coupling Truncation `A2-OW10`), `NO-GO / IMPOSSIBLE-BY-THEOREM` (`2` rows: Pure-Volume/Untwisted `Im(tau) > 1` & Raabe `-36` Selection + `1H` Conformal EWSB + Perturbative 4D Stelle Ghost `A2-OW3/A2-OW6/A2-OW8/A2-OW10`; `T^2 / Z_2` KK-Tower `a_0` Cosmological Constant Cancellation & `4D` Zero-Mode `nu^c` Stabilizer `A2-OW4/A2-OW9`), and `STILL OPEN` (`2` rows: Observed `10^(-120)` Cosmological Constant Value & `4` Continuous Scale Inputs `g_UV, lam_0, tan(beta), M_R/M_X` `A2-OW8/A2-OW9`; Early-Universe Dynamics — Inflation, Baryogenesis Rate, CMB Spectrum, Structure Formation & Non-Perturbative `7D`/FRG Quantum Gravity `A2-OW10`). Verify exact partition `5 + 3 + 2 + 2 = 12` with zero unclassified or conflicting rows.

4. **Planted-Fault Self-Checks (`OW10-D`, `4 / 4`):**
   - `PF-OW10-1`: Flipping fermion sign in `B_1` (`-f_W N_W`) shifts `M_g(2H)` from `+8` to `-88`, collapsing `g_*` by `> 18x` (`> 7` down to `< 1 / 2`) and shifting `lam_*` from `< -10` to `> -1` (`caught`).
   - `PF-OW10-2`: Increasing generations from `N_gen = 3` to `N_gen = 4` (`M_g = +24 > 14`) destroys the Type-II UV fixed point (`0` UV FPs, `caught`).
   - `PF-OW10-3`: Switching Type-II (`f_W = 1`) to Type-I (`f_W = 2`) shifts `M_g(2H)` from `+8` to `+56 > 14` and destroys the UV fixed point (`0` UV FPs, `caught`).
   - `PF-OW10-4`: Reversing UV/IR in `a`-theorem (`a_IR - a_UV = -125 / 48 < 0`) and setting non-conformal `xi = 0` (`(xi - 1/6)^2 = 1/36 != 0`) both fail monotonic `Delta a > 0` and conformal zero-scalaron checks (`caught`).

## 2. Guardrails & Cold-Room Protocol

- Strict `0` float/complex AST literals and `0` `frontier/` imports; `A`-only `SHA-256` manifests; zero hardcoded proof flags; independent Cold-Room Referee built solely from this card using disjoint methods (`2D` Newton-Raphson directly on `(beta_g, beta_lam) = (0, 0)` without cubic reduction + numerical finite-difference Jacobian stability matrix + disjoint `Delta(2, 3, N)` matrix-group `21`-action reconstruction + symbolic `sympy` Stelle partial-fraction & `a`-theorem verification). `0 of 19.`
