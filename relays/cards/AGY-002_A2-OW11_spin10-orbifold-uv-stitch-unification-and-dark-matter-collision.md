# Pre-Registration Card: `AGY-002_A2-OW11` — `6D / 7D` `Spin(10)` Orbifold UV-IR Stitch, Weak-Coupling Type-I/II FRG, Pati-Salam Unification Closure, & `3 = 4 - 1` Dark-Matter Collision Audit (`0 of 19`)

- **Seat:** `AGY-002` (`agy-002/verify`)
- **Card ID:** `A2-OW11`
- **Empirical Firewall:** Strict `0 of 19` (all unification targets, mass-scale ratios, and proton-lifetime ratios expressed purely dimensionlessly; zero empirical PDG inputs).
- **Prerequisite Custody:** Builds on `A2-OW1..A2-OW10` (`f55d5124a` on `origin/agy-002/verify`), directly closing Internal Limps 1 (`G_SM` vs `Spin(10)` UV-IR seam) and 2 (`3 = 4 - 1` brane-generation vs LKP dark-matter collision).

## 1. Scientific Objective & Hypotheses Committed Before Run

This card stitches `A2-OW1, OW3, OW5, OW8, OW9, OW10` into a single consistent `6D / 7D` `Spin(10) -> Pati-Salam -> G_SM` UV-to-IR hierarchy and settles the `3 = 4 - 1` dark-matter collision discovered in `A2-OW9`:

1. **`6D` Bulk `Spin(10)` Orbifold `[3, 2]` Projection, `6D` `I_8` Anomaly, & Dynamic Casimir Selection of Higgs Localization (`OW11-A`):**
   - Explicitly construct the `45` antisymmetric `10 x 10` basis matrices of `so(10)`, the diagonal Pati-Salam orbifold involution `P_PS = diag(+1^6, -1^4)`, and the commuting `U(5)` complex structure `J_5 = diag([[0, -1], [1, 0]] x 5)` (`P_PS J_5 == J_5 P_PS`, `J_5^2 == -I_10`).
   - Compute exact centralizer dimensions in `so(10)` via exact rational Gaussian elimination (zero hardcoded dimensions):
     - `dim C(P_PS) = 21` (`so(6) + so(4) = su(4)_C + su(2)_L + su(2)_R`, `24` odd `X, Y` coset), and `-P_PS` on the `10` splits `2H` (`4` components, `+1` even) from color triplets (`6` components, `-1` odd) — exact orbifold doublet-triplet splitting.
     - `dim C(J_5) = 25` (`u(5) = su(5) + u(1)_X`).
     - `dim C(P_PS, J_5) = 13` (`G_SM x U(1)_X`), leaving `dim G_SM = 12` and **`45 - 12 = 33` massive Proca gauge vectors (`24 + 8 + 1`)** once `U(1)_X` breaks at `M_R` — directly supplying `A2-OW8`'s exact `33` Proca vectors without an ad-hoc GUT Higgs sector.
   - Directly sum over all `16` Cartan weight states of `16_+` (`s_1 .. s_5 in {-1, +1}` with `prod s_k = +1`) on `4` independent Cartan vectors in exact `Fraction` arithmetic to prove `tr_{16}(F^2) = 2 tr_{10}(F^2)` and `tr_{16}(F^4) = -tr_{10}(F^4) + (3 / 4) (tr_{10} F^2)^2`, yielding for `3 x 16_+` (`48` `6D` Weyl): **`c_{tr_10 F^4} = -1 / 8 != 0`, `c_{tr R^4} = +1 / 120 != 0`, and `0` mixed `U(1)` anomaly** — proving `6D` non-SUSY `Spin(10)` STILL forces `7D` bulk Chern-Simons inflow (`A2-OW5`).
   - Compute exact `6D` `Spin(10)` bulk supertraces per `T^2` lattice point (`45 * 2 = 90` real gauge B vs `48 * 2 = 96` real Weyl F):
     - Brane `2H` (`0`): `-6` -> positive dS Casimir (`+(6 / pi^3) E_3 > 0`, stabilizes `tau_*^{+-}` and slashes bulk imbalance `12x` vs `-72`).
     - Bulk `2H` (`+4`): `-2` -> positive dS Casimir (`+(2 / pi^3) E_3 > 0`, stabilizes `tau_*^{+-}`, slashes `34x` vs `-68`).
     - Bulk real `10` (`+5`): `-1` -> positive dS Casimir (`+(1 / pi^3) E_3 > 0`, stabilizes `tau_*^{+-}`, slashes `68x` vs `-68`).
     - Bulk complex `10` (`+10`): `+4` -> **negative AdS Casimir (`-(4 / pi^3) E_3 < 0`), flipping `tau_*^{+-}` from a global minimum into an unstable local maximum (dynamically excluded!)**.

2. **Weak-Coupling UV `Spin(10)` FRG (Type-I & Type-II), Pati-Salam Unification Closure, & Proton Stability (`OW11-B`):**
   - Solve the exact `A2-OW10` harmonic-gauge Litim FRG cubic (`50`-dps + analytic Jacobian) in BOTH Type-II (`f_W = 1`) and Type-I (`f_W = 2`) for:
     - `Spin(10) + real 10` `(10, 48, 45)`: **survives BOTH Type-II (`2 / 10 < g_* < 3 / 10`, `0 < lam_* < 1 / 10`, UV-attractive) AND Type-I (`3 / 10 < g_* < 4 / 10`, `0 < lam_* < 1 / 10`, UV-attractive)** — curing BOTH strong-coupling (`> 27x` weaker than `g_* = 7058 / 1000`!) and Type-I caveats of `A2-OW10`!
     - `Spin(10) + complex 10` `(20, 48, 45)`: survives BOTH Type-II (`2 / 10 < g_* < 3 / 10`, `1 / 10 < lam_* < 2 / 10`) and Type-I (`3 / 10 < g_* < 4 / 10`, `1 / 10 < lam_* < 2 / 10`).
     - Intermediate Pati-Salam variants `(24, 48, 21)` (`(1,2,2)+(4,1,2)`), `(39, 48, 21)` (`+(15,1,1)`), and `(68, 48, 21)` (`(1,2,2)+(10,1,3)`): verify `(24, 48, 21)` (`M_g = -12, 2 M_l = -30`) and `(39, 48, 21)` (`M_g = +3, 2 M_l = -15`) have Type-II UV FPs (and `0` Type-I FPs), while boson-dominated `(68, 48, 21)` (`2 M_l = +14 > 0`) has weak Type-II and Type-I FPs (`3 / 10 < g_* < 4 / 10`, `3 / 10 < lam_* < 4 / 10`).
   - Compute exact rational `1`-loop gauge unification slope ratios `B = (b_2 - b_3) / (b_1 - b_2)`:
     - `6D` KK bulk `2H` (`-10 / 3 C_2 + 2H`) gives `B = 5 / 8` (halfway from `5 / 9` toward `5 / 7`, still `< 5 / 7`), while `6D` KK brane `2H` gives `B = 1 / 2`.
     - Intermediate `4D` Pati-Salam above `M_PS` flips `b_1_eff < b_2L`, closing exact `B_eff = 5 / 7` unification at exact rational intermediate scale ratios `r = ln(M_PS / M_Z) / ln(M_GUT / M_Z) in (0, 1)`: **`67 / 75`** for `(1,2,2)+(4,1,2)`, **`61 / 69`** for `+(15,1,1)`, and **`25 / 33`** for `(1,2,2)+(10,1,3)`.
   - Verify dimensionless proton-lifetime enhancement from `A2-OW8`'s `M_X / M_Pl = sqrt(pi) / 4` relative to a canonical `M_GUT / M_Pl = 1 / 1000` benchmark: `(M_X / M_GUT)^4 = 250^4 * pi^2 > 3 * 10^10` (over `10` orders of magnitude safer than naive `SU(5)`!).

3. **Exact `3 = 4 - 1` Brane-Generation vs. LKP Dark-Matter Collision Audit (`OW11-C`):**
   - Compute exact `Z_2 x Z_2` Fourier projections `C_S(m, n) = sum_{p in S} (-1)^{m p_1 + n p_2}` across all `4` grades `{(0,0), (1,0), (0,1), (1,1)}` for:
     - Full `E[2]` (`4` points): `(4, 0, 0, 0)` (exact `Z_2 x Z_2` conservation -> `Q = 1` LKP strictly stable).
     - Cusp puncture `{(0,0)}` (`1` point): `(1, 1, 1, 1)`.
     - **`3` non-cusp generation fixed points `E[2] \ {0}` (`3` points): `(3, -1, -1, -1)`** — exact identity `C_3 == C_4 - C_1 == -1 != 0` on EVERY non-trivial `Z_2 x Z_2` grade!
   - Certify the exact **Brane-Generation vs. LKP No-Go Theorem**: localizing `3` chiral generations at `E[2] \ {0}` breaks `Z_2 x Z_2` KK-parity with `O(1)` amplitude `-1`, opening prompt tree-level LKP decay to `(0, 0)` SM zero modes (`Gamma / M_KK ~ g^2 / (16 pi)`) and ruling out strictly stable `Q = 1` LKP dark matter in the brane-localized picture; conversely, if the `3` generations arise as uniform bulk `7D` zero modes (index-theorem / `A_5` `3`-bundle), bulk couplings project as `(4, 0, 0, 0)` and `Q = 1` LKP remains strictly stable across all `547 / 547` `GL(2, Z)` threads.
   - Verify `Spin(10)` `Z_4` center matter parity `P_M = (-1)^{3(B-L)}` equals `+1` on all `33` broken `X, Y` Proca bosons (so `X, Y` decay freely to SM pairs) and `-1` on `16_+` fermions (`== (-1)^F`).

4. **Planted-Fault Self-Checks (`OW11-D`, `4 / 4`):**
   - `PF-OW11-1`: Replacing `P_PS = diag(+1^6, -1^4)` by `diag(+1^8, -1^2)` breaks `so(10)` to `so(8) + so(2)` (`dim = 29 != 21`) instead of Pati-Salam (`caught`).
   - `PF-OW11-2`: Putting bulk complex `10` (`+10 / pt`) into `6D` `Spin(10)` shifts `n_B - n_F` from `< 0` to `+4 > 0`, flipping Casimir energy to AdS (`< 0`) and destabilizing `tau_*^{+-}` (`caught`).
   - `PF-OW11-3`: Omitting the `3 / 4 (tr F^2)^2` double-trace term in `tr_{16}(F^4)` violates the `16_+` Cartan trace identity on `(1, 1, 0, 0, 0)` (`caught`).
   - `PF-OW11-4`: Treating `3` generation sites `E[2] \ {0}` as `Z_2 x Z_2`-conserving (`C_3 == 0`) fails directly against `C_3(1, 0) = C_3(0, 1) = C_3(1, 1) = -1 != 0` (`caught`).

## 2. Guardrails & Cold-Room Protocol

- Strict `0` float/complex AST literals and `0` `frontier/` imports; `A`-only `SHA-256` manifests; zero hardcoded proof flags; independent Cold-Room Referee built solely from this card using disjoint methods (e.g. `sympy` exact `so(10)` Lie-bracket & root-system Cartan decomposition for `45 -> 12 + 33`, disjoint `32 x 32` Clifford matrix `tr_{16}(F^4)` computation, disjoint `55`-dps direct 2D Newton-Raphson FRG solver without `polyroots`, and disjoint exact `Fraction` Pati-Salam & Fourier character audit). `0 of 19.`
