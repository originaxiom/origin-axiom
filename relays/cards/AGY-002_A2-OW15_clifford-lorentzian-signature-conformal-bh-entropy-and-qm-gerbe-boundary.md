# AGY-002 Pre-Registration Card `A2-OW15`: Deep Foundations — Explicit `Cl(t, s)` Lorentzian `(1, 3)` Selection (`X22`), Conformal `xi = 1/6` Induced Black-Hole Entropy (`X2`), and `X1` / `X37` Boundary Ledger (`0 of 19`)

- **Seat:** `AGY-002`
- **Branch:** `agy-002/verify`
- **Card ID:** `A2-OW15`
- **Empirical inputs:** **`0 of 19`** (pure Clifford-algebra representation theory over `Z[i]`, hyperbolic PDE symbol analysis, conical-defect heat-kernel replica calculus, and finite-dimensional unitary / topological boundary audits).
- **Guardrails:** `0` float/complex AST literals in `.py` (exact `Z[i]` `sympy` matrices, `Fraction`, integer-built `mpmath` at `>= 55` dps); `0` `frontier/` imports; zero hardcoded proof flags (Guardrail 2: every Clifford relation, intertwiner `B^* B`, chirality flip `B gamma_*^* B^{-1}`, kinetic norm, conical replica derivative, and `L^p` Haar drift computed directly from explicit matrices); `A`-only `SHA-256` manifests; Cold-Room Referee disjoint methods (`0` discrepancies, `4/4` planted faults).

---

## 1. Scientific Scope & Hypotheses

Card `A2-OW15` executes Phase 5 of Campaign 2: testing the Tier 1 foundational axioms imported by `A2-OW1..A2-OW14` — proving directly from explicit Clifford matrices whether Lorentzian `(1, 3)` (`1` time + `3` space) is uniquely forced (`X22`), proving whether conformal `xi = 1/6` induced gravity at `A2-OW8`'s exact `c_log = +16` spectrum reproduces Bekenstein-Hawking entropy `S_BH = A / (4 G_ind)` via Kabat vector edge modes (`X2`), and establishing an honest theorem-grade boundary ledger for Quantum Mechanics (`X1`) and non-abelian `H^2` gerbes (`X37`).

---

## 2. Frozen Specification & Pass/Fail Acceptance Criteria

### Task `OW15-A`: Explicit `Cl(t, s)` Matrix Construction Across All `11` Signatures in `D = 4, 6, 7` (`X22`)

1. **Explicit `2^{floor(D/2)} x 2^{floor(D/2)}` Matrix Realization over `Z[i]`:**
   - For all `11` unordered signatures `(t, s)` with `eta = diag(-1^t, +1^s)` (`D = 4`: `(0,4), (1,3), (2,2)`; `D = 6`: `(0,6), (1,5), (2,4), (3,3)`; `D = 7`: `(0,7), (1,6), (2,5), (3,4)`):
     - Explicitly construct `Gamma_0, ..., Gamma_{D-1}` and verify `{Gamma_a, Gamma_b} == 2 eta_{ab} I` entry-by-entry (`0` matrix error across all `11` signatures).
     - For even `D`, compute the volume element `G_vol = Gamma_0 ... Gamma_{D-1}`, its exact square `G_vol^2 = (+1 or -1) I`, and normalized chirality `gamma_*` (`gamma_*^2 = +I`).
     - Exhaustively construct the unitary charge/reality intertwiners `B` satisfying `B Gamma_a^* = eps Gamma_a B` (`eps in {+1, -1}`), directly compute Frobenius-Schur `B^* B = (+1 or -1) I` and chirality conjugation `B gamma_*^* B^{-1} = (+1 or -1) gamma_*`, classifying Weyl/Dirac reality (`C` complex chiral `L^* = R`, `R` Majorana-Weyl, `H` Symplectic-Weyl).
     - Directly verify the Dirac kinetic norm positivity `H_norm * (i Gamma^0) == +I` (positive definite iff `t = 1`) and the wave-operator symbol `P(w, k) = eta^{ab} xi_a xi_b = 0` (`t = 0`: elliptic, `0` real roots; `t = 1`: strictly hyperbolic, `2` real distinct roots; `t >= 2`: ultrahyperbolic, complex Hadamard-unstable roots for `|w_2| > |k|`).
2. **Exact `8 x 8` Chirality Factorization `(1, 5) = (1, 3) + (0, 2)`:**
   - Explicitly construct `gamma_5^{(1,3)}` (`4 x 4`) and `gamma_3^{(0,2)}` (`2 x 2`) and verify `Gamma_{(1,5)} == gamma_5^{(1,3)} kron gamma_3^{(0,2)}` (up to global sign `+-1`, exact `0` matrix residual).
3. **Unique Selection Theorem (`X22`):**
   - Certify that `(1, 3)` is the **UNIQUE `D = 4` signature (`1 of 3`)** with complex chiral Weyl spinors (`C: L^* = R`, `vol^2 = -1`, `B gamma_5^* B^{-1} = -gamma_5`) AND the unique `D = 4` signature with positive-definite Dirac kinetic norm and strictly hyperbolic Cauchy evolution.
   - Certify that `(1, 3) -> (1, 5) -> (1, 6)` is the **UNIQUE signature tower across `D = 4, 6, 7`** combining positive-definite kinetic norm, hyperbolic Cauchy well-posedness, Euclidean Riemannian internal spaces (`T^2/Z_2` `(0,2)`, `H^3/Gamma` `(0,3)`), `4D` complex chiral `16_+`, and `6D` self-conjugate symplectic-Weyl (`H`, `vol^2 = +1`) `I_8` anomaly inflow.

---

### Task `OW15-B`: Conformal `xi = 1/6` Induced Black-Hole Entropy (`X2`) & Schwarzschild Logarithmic Correction

1. **Exact Conical-Defect Replica Calculus on `C_alpha x Sigma` (`S_BH = (alpha d/d_alpha - 1) W(alpha)|_{alpha=1}`):**
   - Using Sommerfeld's exact Bernoulli cone coefficients (`B_2(0) = +1/6` periodic boson, `B_2(1/2) = -1/12` antiperiodic fermion), Wald-Noether non-minimal scalar contact term (`-4 pi xi (1 - alpha)`), and Kabat Ricci vector edge contact term (`-4 pi (1 - alpha)`), directly compute via `replica(f) = (alpha d/d_alpha - 1) f|_{alpha=1}` the exact `w_ent`, `w_contact`, and `w_tot = w_ent + w_contact` weights:
     - Real scalar (`xi`): `w_ent = 1/6`, `w_contact = -xi`, `w_tot = 1/6 - xi` (`w_tot(1/6) == 0`).
     - Weyl / Majorana fermion: `w_ent = 1/6`, `w_contact = 0`, `w_tot = 1/6`.
     - Massive Proca vector (`3` polarizations): `w_ent = 1/2`, `w_contact = -1`, `w_tot = -1/2`.
     - Massless gauge vector (`2` polarizations): `w_ent = 1/3`, `w_contact = -1`, `w_tot = -2/3`.
   - Verify exact identity `w_tot == w_bulk(1 / G_ind)` for ALL four field types (`A2-OW4` & `A2-OW8` exact match).
2. **Exact `A2-OW8` `Spin(10)` Spectrum Check (`33` Proca + `3` Majorana `nu^c` + `8` Conformal `xi = 1/6` `2H` Scalars):**
   - With logarithmic weights `c_log = -w`:
     - Certify pure entanglement part alone is strictly NEGATIVE: `c_log_ent = -55/3 < 0`.
     - Certify contact / edge part (`33` Kabat vector edge `+33` + `8` conformal scalar Wald-Noether `+4/3`) is strictly POSITIVE: `c_log_contact = +103/3 > 0`.
     - Certify exact cancellation sum: **`c_log_ent + c_log_contact == +16 == c_log(1 / G_ind)`**, proving `S_ent + S_contact == A / (4 G_ind)` identically!
3. **Exact `4D` Schwarzschild (`chi = 2`, Ricci-flat `C^2 = E_4`) Matter Logarithmic Entropy Coefficient `2 (c - a)`:**
   - Compute `c = (N_S + 3 N_W + 12 N_V) / 120`, `a = (2 N_S + 11 N_W + 124 N_V) / 720`, and `2 (c - a)` (coefficient of `ln(A / l_Pl^2)`):
     - IR `G_SM 2H` (`45` light Weyl): `c = 287/120`, `a = 1999/720`, `2(c - a) = -277/360`.
     - IR `G_SM 2H` (`48` Weyl incl `nu^c`): `c = 37/15`, `a = 127/45`, `2(c - a) = -32/45`.
     - UV `Spin(10) real-10` `(10, 48, 45)`: `c = 347/60`, `a = 383/45`, `2(c - a) = -491/90`.

---

### Task `OW15-C`: Theorem-Grade Boundary Ledger for `X1` (Quantum Mechanics) & `X37` (`H^2` Gerbe Obstruction)

1. **`X1` `L^2` Born-Rule Uniqueness vs External Axioms:**
   - Directly verify on the exact algebraic `3 x 3` unitary DFT matrix `F_3` (`w = (-1 + i sqrt(3))/2`) AND a `10`-trial `U(3)` Haar-random unitary ensemble (`55` dps) that among `L^p` probability sums `sum_i |psi_i|^p` (`p in {1, 2, 3, 4}`):
     - `p = 2` has exact drift `0` (`F_3`) and `< 1/10^45` across `10` Haar trials;
     - Every `p in {1, 3, 4}` violates unitary probability conservation (`|drift(F_3)| > 1/3` and max Haar drift `> 1/5`).
   - Emit an explicit honest `X1` boundary classification: `L^2` Born-norm uniqueness given unitarity is `PROVED`, while complex Hilbert-space linearity, unitary dynamics, and Born measurement ontology remain `EXTERNAL_AXIOM` (not derived from `7D` geometry).
2. **`X37` `H^2` / `H^3` Gerbe Boundary Ledger:**
   - Compute exact `Spin(10)` topological invariants (`dim = 45`, `rank = 5`, `pi_1(SO(10)) = Z_2`, `pi_1(Spin(10)) = 0`, `pi_2(Spin(10)) = 0`, `pi_3(Spin(10)) = Z`, `H^3(Spin(10), Z) = Z`, second Stiefel-Whitney lifting `Spin(10) -> SO(10)`), certifying that `A2-OW5`'s `7D` CS `3`-form `H_3 = d B_2 + omega_3^{CS}` realizes an **abelian `U(1)` `2`-gerbe / string-structure inflow** (`DERIVED`), whereas non-abelian `2`-form gerbe quantization / `6D` `(2,0)`-type UV completion remains `OPEN_UV_BOUNDARY`.

---

### Task `OW15-D`: `4 / 4` Planted Fault Controls (`PF-OW15-1..4`)

- `PF-OW15-1`: Select `D = 4` Kleinian `(2, 2)` signature -> fails BOTH complex chirality (`Weyl = R`, `B gamma_*^* = +gamma_* B`) AND hyperbolicity (ultrahyperbolic complex wave roots).
- `PF-OW15-2`: Omit the Kabat vector edge contact term (`w_contact^{Proca} = 0`) in `OW15-B` -> `c_log_total` plunges from `+16` to `-17 < 0` (breaks `S_BH = A / (4 G_ind)`).
- `PF-OW15-3`: Shift the `8` `2H` scalars from conformal `xi = 1/6` to minimal `xi = 0` -> `c_log_total` shifts from `+16` to `44/3 != 16`.
- `PF-OW15-4`: Replace `L^2` (`p = 2`) with `L^4` (`p = 4`) probability sum under exact `U(3)` DFT `F_3` -> `drift = -2/3 != 0` (violates unitary probability conservation).

---

## 3. Custody & Referee Protocol

1. Commit 1: seal this Card before any producer code exists.
2. Commit 2a / 2b: seal `relays/a2_ow15/verify_a2_ow15.py` pre-run (`A`-only `SCRIPT_SHA256.txt`), run once, seal `a2_ow15_results.json` & `OUTPUT_SHA256.txt` unread.
3. Independent Cold-Room Referee (`relays/a2_ow15_referee/`): reads ONLY this Card prior to Commit 4b, implements disjoint methods (Bott-periodicity / Weyl-chiral block-off-diagonal gamma realization rather than `Z^k X/Y` Pauli chains, explicit linear nullspace solver for `B` rather than bitmask enumeration, direct Sommerfeld zeta-function / Bernoulli integral derivation for `OW15-B`, and disjoint `4 x 4` Householder / Cayley unitary `L^p` test for `OW15-C`), seals Commit 4a/4b unread, and certifies `0` discrepancies + `4/4` planted faults.
4. Relay `relays/AGY002_A2_OW15_RESULTS.md` + `STATUS_AGY-002.md` item `25` + `7`-point audit + fast-forward push to `origin/agy-002/verify`.
