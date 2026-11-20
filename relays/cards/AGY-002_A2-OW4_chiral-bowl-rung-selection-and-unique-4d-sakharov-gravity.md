# Pre-Registration Card: `AGY-002_A2-OW4` — Dynamic Chiral-Bowl Selection of `N = 5` and Unique `(D = 4, N = 5, N_gen = 3)` 1-Loop Sakharov Induced Gravity (`0 of 19`)

- **Seat:** `AGY-002` (`agy-002/verify`)
- **Card ID:** `A2-OW4`
- **Empirical Firewall:** Strict `0 of 19` (zero empirical inputs, zero PDG numbers, zero `m004` / `G:SE1` / `G:SE2` selection)
- **Prerequisite Custody:** Builds strictly on `A2-OW1` (`5f41c72de` / `ccc22f6a1`) and `A2-OW2` (`b400fc161` / `a31eb8051`).

## 1. Scientific Objective & Hypotheses Committed Before Run

This card resolves two foundational open-weave questions without any hand-selected hyperbolic thread or empirical tuning:

1. **Dynamic Rung Selection (`OW4-A`, resolving raw `V_min(1) = V_min(3) < V_min(5)` from `A2-OW2`):**
   - On `A2-OW2`, the Berezin 1-loop effective potential `V_N(tau)` on `X_0(N)` is confining if and only if the protected massless fermionic degrees of freedom exceed bosonic degrees of freedom (`n_F^{chiral} > n_B`).
   - We compute the exact gauge-matter spectrum `(d, a, b, n_V, n_s, fock_even, is_chiral, anomalies)` directly from first-principles `Cl(2d)` even-Fock hypercharge weights across all `21` faithful transitive `(N, d <= 12, P)` permutation actions of the finite triangle quotients `Delta(2, 3, N)` (`N in {2, 3, 4, 5}`, matching `A2-OW1`), with `N_gen = 3` (`W:T` triplet).
   - **Pass bar `OW4-A`:**
     - `N = 2, d = 3` (`S_3`, `[1, 2]`) fails 4D gauge anomaly cancellation directly from charge sums (`Tr(Y^3) = -6 != 0`, `2 Tr(SU(2)^2 Y) = +1 != 0`).
     - Every other non-SM action (`19 / 21`, including all `N = 3` `A_4`, all `N = 4` `S_4`, and all `6 <= d <= 12`) is strictly vector-like (`0` protected chiral Weyl zero modes), giving `n_F^{chiral} - n_B < 0` (**bosonic runaway instability**; specifically `-18` / `-22` for `N = 3` and `-20` / `-22` or `-18` / `-22` for `N = 4` in `1H` / `2H` conventions).
     - **`N = 5, d = 5` (`A_5 / A_4`, `[1, 2, 2]`) is the UNIQUE anomaly-free finite-rung action with a confining chiral 1-loop bowl:** `n_F^{chiral} - n_B = 96 - 32 = +64 > 0` (`2H`) and `96 - 28 = +68 > 0` (`1H`).

2. **First-Principles `S^D` & `S^2 x S^2` Spectral Heat Kernel (`OW4-B`):**
   - By direct `40`-digit `mpmath` spectral summation of exact Laplacian/Dirac/Hodge-1-form eigenvalues and degeneracies with exact Vandermonde Richardson extrapolation on unit round spheres `S^4` (`R = 12`), `S^6` (`R = 30`), `S^8` (`R = 56`) AND on the Einstein product manifold `S^2 x S^2` (`R = 4`, `C^2 = 16 / 3`, `E_4 = 8`), derive from first principles (zero hardcoded formulas):
     - Exact 1-loop Sakharov induced Einstein-Hilbert weights `w_s(D) = +1 / 6`, `w_W(D) = +2^(D/2 - 1) / 12`, and `w_V(D) = (D - 8) / 6` for `D in {4, 6, 8}`, matching the published 4D Broda-Szanecki benchmark (`6 C_grav = (1 - 6 xi) n_s + n_W - 4 n_V`) to `< (1 / 10)^8` on both `S^4` and `S^2 x S^2` (Guardrail 4 literature gate).
     - Exact 4D `a_2` Seeley-DeWitt coefficients on BOTH `S^4` (`a2_s = 29 / 15`, `a2_W = -11 / 30`, `a2_V = -62 / 15` including the exact `l = 0` scalar ghost zero-mode `-6`) AND `S^2 x S^2` (`a2_s = 11 / 45`, `a2_W = +1 / 90`, `a2_V = -38 / 45`), independently disentangling the 4D trace-anomaly central charges `c` (Weyl-squared) and `a` (Euler `E_4`) to `< (1 / 10)^7`.

3. **Unique `(D = 4, N = 5, N_gen = 3)` Induced Gravity & Honest `a_0` Cosmological Constant No-Go (`OW4-C`):**
   - Evaluate the induced gravity balance across all `21` actions of `N in {2, 3, 4, 5}`, generation counts `N_gen in {1, 2, 3, 4}`, and even external dimensions `D in {4, 6, 8, 10}`:
     - **Unique `(D = 4, N = 5, N_gen = 3)` cancellation:** Exact fermion-minus-gauge quadratic Planck cancellation `n_W w_W(D) + n_V w_V(D) = 0` on the unique chiral anomaly-free engine (`n_V = 12`, `16` Weyl per generation) has a unique integer solution across all even `D >= 4`: **`D = 4` AND `N_gen = 3`** (`48 - 4 * 12 = 0`). At `D = 6`, cancellation requires `N_gen = 3 / 4` (non-integer, impossible); for all `D >= 8`, `w_V(D) >= 0` (cancellation impossible for any spectrum).
     - **Unique attractive 4D gravity:** Across all anomaly-free actions (`20 / 21`) and `N_gen in {1, 2, 3}`, `(D = 4, N = 5, N_gen = 3)` is the **unique** configuration with attractive induced Newton constant `G_N > 0` for minimal Higgs (`6 C_grav = +8 > 0` for `2H`, `+4 > 0` for `1H` at `xi = 0`) and exact zero quadratic Planck divergence for conformal Higgs (`C_grav = 0` at `xi = 1 / 6`). Every vector-like action (`N = 3, 4`, `d >= 6`) and every lower generation count (`N_gen = 1, 2` at `N = 5`) yields negative `C_grav < 0` (**ghost / repulsive gravity**).
     - **4D trace anomaly (`a_2`):** `c = 37 / 15 > 0`, `a = 127 / 45 > 0` (`2H`); `c = 73 / 30 > 0`, `a = 253 / 90 > 0` (`1H`).
     - **Honest `a_0` Cosmological Constant No-Go:** Quartic vacuum-energy coefficient `a_0 = n_B - n_F = -64` (`2H`) and `-68` (`1H`), both strictly nonzero — certifying honestly that Bose-Fermi quartic cosmological-constant cancellation does **not** occur on the massless spectrum.

4. **Planted-Fault Self-Checks (`OW4-D`, `4 / 4`):**
   - `PF-OW4-1`: Flipping the Dirac Berezin sign (`+a1_D` instead of `-a1_D`) violates the Broda-Szanecki benchmark and destroys `w_W + 4 w_V` balance (`caught`).
   - `PF-OW4-2`: Omitting the `l = 0` scalar ghost zero-mode (`-6`) on `S^4` shifts `a2_V` from `-62 / 15` to `+28 / 15`, failing the `S^4` Duff trace-anomaly check (`caught`).
   - `PF-OW4-3`: Shifting `N_gen = 2` at `N = 5` flips `6 C_grav(xi = 0)` negative (`-8 < 0` for `2H`, `-12 < 0` for `1H` — ghost gravity, `caught`).
   - `PF-OW4-4`: Shifting external dimension to `D = 6` breaks exact fermion-gauge cancellation (`n_W w_W(6) + n_V w_V(6) = +12 != 0`, requiring `N_gen = 3 / 4`, `caught`).

## 2. Guardrails & Cold-Room Protocol

- Strict `0` float/complex AST literals and `0` `frontier/` imports in both producer and cold-room referee scripts.
- `A`-only `SHA-256` manifests (`SCRIPT_SHA256.txt` pre-run, `OUTPUT_SHA256.txt` post-run sealed unread).
- Independent Cold-Room Referee built solely from this card using disjoint mathematical methods (e.g., independent Euler-Maclaurin / Hurwitz-zeta asymptotic expansion or independent `CP^2` / `S^2 x S^2` + `S^D` spectral evaluation, plus independent `Cl(2d)` weight enumeration). `0 of 19.`
