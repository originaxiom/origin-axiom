# Pre-Registration Card: `AGY-002_A2-OW5` — Open-Weave `6D -> 7D` Chirality & Triple-Locked `I_8` Inflow Theorem and Five-Regime Open-Flute Selberg `s = 2` Audit (`0 of 19`)

- **Seat:** `AGY-002` (`agy-002/verify`)
- **Card ID:** `A2-OW5`
- **Empirical Firewall:** Strict `0 of 19` (zero empirical inputs, zero PDG numbers, zero `m004` / `G:SE1` / `G:SE2` selection)
- **Prerequisite Custody:** Builds on `A2-OW1` (`5f41c72de` / `ccc22f6a1`), `A2-OW3` (`2294c03c3` / `2fcde558a`), and `A2-OW4` (`08315469d` / `1192ed854`). Audits peer-seat `AGY-C7`'s `s = 2` Selberg claim on the truly unblocked open flute (`GL(2, Z)` including `det = -1`).

## 1. Scientific Objective & Hypotheses Committed Before Run

This card resolves Hard Wall 3 (full 4D chirality and 6D/7D anomaly inflow without `m004`) and Hard Wall 5 (open-flute dynamical thread weighting when `det = -1` and `+-gamma` signs are unblocked):

1. **Universal Open-Weave `T^2 / Z_2` Pillowcase Involution & Explicit `8 x 8` `Cl(6)` Chirality Projection (`OW5-A`):**
   - Verify algebraically across all `547` primitive hyperbolic conjugacy classes (`363` in `PSL(2, Z)` with `3 <= tr <= 50` plus `184` `det = -1` classes with `1 <= tr <= 50`) that the hyperelliptic involution `iota = -I_2` commutes identically with every monodromy `M` (`(-I_2) M == M (-I_2)`, `0` exceptions — requiring zero `m004` selection), fixes the cusp puncture `0 in E[2]`, and permutes the `3` non-trivial `W:T` parities `E[2] \ {0}` via `M mod 2 in S_3` (reporting the exact orbit-type census across all `363` `PSL(2, Z)` and `184` `det = -1` classes, verifying `(3,)` for both `m000` and `m004`, and `(1, 2)` for both `t = 4` overtones).
   - Construct explicit `8 x 8` `Cl(6)` gamma matrices `Gamma_1 .. Gamma_6` in exact Gaussian integer `Z[i]` arithmetic (zero float/complex literals): verify all `36` anticommutators `{Gamma_a, Gamma_b} = 2 delta_{ab} I_8`, exact factorization `Gamma_7 = gamma_5 * gamma_int`, and spin-lift `hat_iota = (-i) R(pi) = -i Gamma_5 Gamma_6 = gamma_int` satisfying `hat_iota^2 = +I_8`, `[hat_iota, Gamma_7] = 0`, `[hat_iota, gamma_5] = 0`.
   - **Pass bar `OW5-A`:** Explicit eigenspace projection proves that `hat_iota = +1` projects a `6D` chiral Weyl spinor (`Gamma_7 = +1`, `dim = 4`: `2_L + 2_R` in 4D) strictly onto `(2_L, 0_R)` — hence `3 x 16_+` projects cleanly to pure 4D chiral `(48_L, 0_R)` — while free unorbifolded `Tr(gamma_int) = 0` confirms `index = 0` (`48_L, 48_R`) without `T^2 / Z_2`.

2. **Triple-Locked `6D` `G_SM` `I_8` Impossibility & Forced `7D` Chern-Simons Inflow (`OW5-B`):**
   - From the `6` `G_SM = SU(3) x SU(2) x U(1)_Y` multiplets of `16_+` in exact `Fraction` arithmetic (first verifying all `4D` anomalies vanish identically: `Tr(Y) = Tr(Y^3) = 2 Tr(SU(3)^2 Y) = 2 Tr(SU(2)^2 Y) = A(SU(3)^3) = 0`, plus verifying `tr(H^4) == (1 / 2) (tr H^2)^2` for `SU(2)` and `SU(3)` on `10` random traceless Hermitian matrices to `< (1 / 10)^13`), compute the exact `6D` 8-form anomaly polynomial `I_8(16_+) = [ch(F) A_hat(R)]_8`:
   - **Pass bar `OW5-B`:** Prove all three independent obstructions to `6D` Green-Schwarz cancellation:
     1. **Irreducible mixed gauge 6-form `^` 2-form anomaly:** `c(tr_3(F_3^3) F_Y) = +1 / 9` per generation (`+1 / 3` for `3 x 16_+`) — strictly nonzero, un-cancellable by **any** number of `6D` 2-form Green-Schwarz tensors `B_2`.
     2. **Irreducible pure gravitational anomaly:** `c(tr(R^4)) = +1 / 360` per generation (`+1 / 120` for `3 x 16_+`) — strictly nonzero, un-cancellable by **any** `6D` 2-form tensor.
     3. **Quadratic 4-form `^` 4-form matrix `Q`** in basis `(tr F_3^2, tr F_2^2, F_Y^2, tr R^2)` has exact rational nonzero determinants `det(Q_3) != 0` (`rank = 3 > 2`) and `det(Q_4) != 0` (`rank = 4 > 2`), proved by exact rational Bareiss elimination — ruling out single-tensor `6D` Green-Schwarz even on the quadratic block alone.
     4. **Explicit `7D` Chern-Simons Inflow Closure:** Verify term-by-term that every monomial of `I_8(3 x 16_+)` (`tr(F_3^3) F_Y`, `tr(R^4)`, and all `10` independent quadratic entries of `x^T Q x`) is matched identically by `d omega_7^{CS}` on the `7D` bulk `M_4 x X_3`.

3. **Exact Five-Regime Open-Flute Selberg `s = 2` Audit (`OW5-C`):**
   - Independently enumerate all `363` primitive `PSL(2, Z)` hyperbolic conjugacy classes (`3 <= tr <= 50`) and all `184` primitive `det = -1` classes (`1 <= tr <= 50`), matching `AGY-C7`'s exact first `12` trace counts `[1, 2, 2, 3, 2, 4, 2, 6, 3, 4, 4, 6]` and exact `7` odd-square `PSL(2, Z)` classes (including `m004 = m000^2`).
   - **Pass bar `OW5-C` (`50`-dps `mpmath`):** Certify all five `s = 2` Selberg weight regimes:
     - `(R1)` `PSL(2, Z)` only (`AGY-C7`): `m004 > 1 / 2` (`t = 4` pair `> 24 / 100`).
     - `(R2)` `SL(2, Z)` orientable (`+M` vs `-M`): exact `50 / 50` tie `m004 == m003` (`> 1 / 4` each).
     - `(R3)` Unblocked open flute (`PSL + det = -1`): `m000` (`> 62 / 100`) crushes `m004` (`< 1 / 10`) by exact `phi^4 = (7 + 3 sqrt(5)) / 2 > 685 / 100`, and `m004 = m000^2` is not primitive in `PGL(2, Z)`.
     - `(R4a)` Unblocked `GL(2, Z)` (`+-M`, `det = +-1`) + non-trivial spinor torsion `|det(M + I)| > 1`: `m000` and `m003` drop out automatically (`|det| = 1`), but non-orientable `t = 2, det = -1` (`lambda = 1 + sqrt(2)`) still beats `m004` by exact `(phi^2 / (1 + sqrt(2)))^4 > 138 / 100`.
     - `(R4b)` Orientable `SL(2, Z)` (required for 4D chirality) + non-trivial spinor torsion `|det(M + I)| > 1`: `m000` is excluded by orientability, `m003` drops out via `|det(-LR + I)| = 1`, and **`m004` (`+LR`, `Smith(M + I) = (1, 5)`) emerges as the unique `#1` thread (`> 1 / 3`, `> 4` times any single `t = 4` thread), paired almost `1 : 1` (`96 / 100 < w4_tot / w3 < 98 / 100`) with the `4` signed `t = 4` (`Smith = (1, 6)`) overtones (`combined share > 66 / 100`)**.

4. **Planted-Fault Self-Checks (`OW5-D`, `4 / 4`):**
   - `PF-OW5-1`: Omitting `-i` in `hat_iota` gives `R(pi)^2 = -I_8 != +I_8` (`caught`).
   - `PF-OW5-2`: Dropping `u^c` from `16_+` breaks 4D `Tr(Y)`, `Tr(Y^3)`, and `A(SU(3)^3)` (`caught`).
   - `PF-OW5-3`: Dropping the `7` odd-square `PSL(2, Z)` classes reduces the census from `363` to `356` (`caught`).
   - `PF-OW5-4`: Evaluating `SL(2, Z)` without `|det(M + I)| > 1` collapses `m004` into an exact tie with `m003` (`caught`).

## 2. Guardrails & Cold-Room Protocol

- Strict `0` float/complex AST literals and `0` `frontier/` imports; `A`-only `SHA-256` manifests; independent Cold-Room Referee built solely from this card using disjoint methods (e.g., independent `Cl(6)` representation, direct `16`-state weight-by-weight `I_8` evaluation, and disjoint Lagrange-Gauss indefinite binary quadratic form enumeration for `PSL(2, Z)` and `det = -1`). `0 of 19.`
