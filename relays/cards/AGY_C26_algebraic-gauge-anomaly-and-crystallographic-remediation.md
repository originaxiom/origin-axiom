# Card AGY-C26: Root-Cause Algebraic, Gauge-Invariance, Anomaly-Inflow, and Crystallographic Remediation of Findings F-AGY-02, F-AGY-03, F-AGY-05, F-AGY-08, and F-AGY-09

1. **The package and the question, in a sentence:** Following `agy-exp`'s peer reading `Card R-AGY-C24` (`631bb5859` on `origin/agy/self-consistent-loop-2026-11-11`), can we record complete non-destructive retractions and scopings for `F-AGY-02`, `F-AGY-03`, `F-AGY-05`, `F-AGY-08`, and `F-AGY-09` while proving zero-float, gauge-invariant, phase-preserving, and crystallographically exact replacements (`0 of 19`)?

2. **What will be delivered, and what done means:** Pre-registered zero-float script `relays/agy_2026-11-22_c26/c26_algebraic_gauge_anomaly_and_crystallographic_remediation.py`, `SCRIPT_SHA256.txt`, sealed `c26_out.json` with `OUTPUT_SHA256.txt` (`computed once`, `expectations committed first`), disjoint self-check `c26_countercheck.py` (`tested against planted errors`), and mask-clean relay testing:
   - **Expectation E1 (`F-AGY-03` — Full `E_8` `(10, 6)` Holonomy Projection, `Mp(2, Z)` Spin Lift, & Cover Obstructions):**
     - Verify on all `240` roots plus `8` Cartans of `E_8` that `v_P` alone leaves `so(16)` (`dim = 136`) and `n_H = 12` doublets (`slope 98 / 85`), whereas adding a commuting `SU(4)` family-holonomy shift plus `Spin(10)` hypercharge shift projects `(10, 6)` cleanly to `G_{SM}` (`dim = 12`) and `n_H = 2` (`slope 9 / 5`, explicitly priced in the discrete holonomy ledger).
     - Record exact negative/scoping theorems (`retracting C3/C6 overclaims`): `U_S^4 == -I_3` lifts `rho_T` to `Mp(2, Z)`, cyclic meridian covers `X_{4_1}^{(m)}` at `m in {8, 40}` retain peripheral longitude degree `1` and meridian kernel `dim = 1` across all `384` `G_T` homomorphisms while trivializing `P^m == +I_5`, and pillowcase `(-i) R(pi)` has exact order `2`.
   - **Expectation E2 (`F-AGY-02` & `F-AGY-05` — `G_{SM}`-Invariant Dim-`4` Holomorphic Iso-Singlet Overlap & Raw Non-Zero Strong-CP):**
     - Replace `C16`'s `SU(2)_L`-breaking, anti-holomorphic, dim-`8` chain with a `5`-site right-handed iso-singlet Kaplan/Clockwork operator on inequivalent `G_{SM}` irreps `u^c`, `d^c`, `e^c`: only Wall `0` couples linearly to `H_{u/d}` (`exact operator dimension 4`, `0` `(v_{EW} / M_{KK})^4` suppression, `0` `H^dag` insertions), while walls `1..4` carry `SU(2)_L`-trivial heavy links whose `M_{KK}` cancels identically above EWSB.
     - Compute `bar_theta_{QCD} = arg det(Y_u Y_d)` directly from complex holomorphic weave amplitudes without Hermitian phase stripping or literal zero assignment (`Guardrail 2`), proving `arg det(Y_f^{eff}) == arg det(Y_f^{(0)}) mod 2 pi`, verifying `SU(3)` invariance `< 10^{-35}`, and disclosing the honest non-zero tree-level `bar_theta_{QCD}(tau_*^{+-})` (`marking Strong-CP OPEN without a 7D CS axion`).
   - **Expectation E3 (`F-AGY-08` & `F-AGY-09` — `2D` vs `6D` Casimir Scaling, Chiral `I_8(3 x 16_+)`, & Hurwitz `D_4 / 2T` Lattice Volume):**
     - Scope `V_{Gamma_0(5)}` strictly to the `2D` worldsheet Ray-Singer determinant at priced equal-sheet weight `r = 1` (`confirming sheet-proportional r = 5 has det Hess < 0 and 6D -> 4D bulk modes scale as E(tau, 3) ~ y^3`).
     - Recompute exact rational `I_8(3 x 16_+)` with scalar `10` contributing `0` and `-1 / 24 tr(R^2)` sign (`c(F_3^3 F_Y) = 1 / 3`, `c(R^4) = 1 / 120`); prove `tr_{R^4}(g_{10}) = 1 + sqrt(5)` rules out compact `T^4 / 2I` while `24 / 24` Hurwitz units preserve `Lambda_{D_4}` of covolume `1 / 2` (`fixing the 2x volume factor to (2 pi R)^4 / 48`); and fix `27 = 16_{+1} + 10_{-2} + 1_{+4}` vs `(-1)^{3(B-L)}` and `(-1)^{3(B-L)+2s}`.

3. **How it could come out wrong, written before any run:**
   - **F1:** Commuting `(Spin(10), SU(4))` holonomy shifts in `E_8` could fail to isolate `n_H = 2` without breaking `G_{SM}`, or the iso-singlet Schur complement could retain `M_{KK}` suppression above EWSB.
   - **F2:** Removing Hermitian phase stripping could destroy `CKM` alignment at `m = 8` or violate `SU(3)` special-unitary invariance of `arg det(Y_u Y_d)`.
   - **F3:** Any of the `24` Hurwitz `2T` units could fail to map `Lambda_{D_4}` into itself, or `I_8(3 x 16_+)` could fail `4D` anomaly cancellation.

4. **What it rests on, and what it must not touch:** Rests on `AGY-C1` through `AGY-C25` on `agy/cusp-action-2026-11-20` (`preserving all sealed historical files untouched per WORKING_RULES.md Rule 3`) and peer review `Card R-AGY-C24` (`631bb5859`). Must not touch `main`, `agy/audit-2026-11-02`, or any measured Standard Model / cosmological value (`0 of 19`).

5. **Controls that must fail if the work is broken:**
   - **Control 1 (`v_P` alone without `SU(4)` family holonomy):** Must yield `n_H = 12` doublets (`slope 98 / 85 != 9 / 5`) and `dim = 136 != 12`.
   - **Control 2 (`C16` odd-wall `H^dag` doublet chain with `M_{KK,u} != M_{KK,d}`):** Must break `SU(2)_L` (`mass ratio != 1`) whereas the iso-singlet chain preserves `SU(2)_L` identically.
   - **Control 3 (Anomalous chiral `U(1)_A` phase rotation `det U != 1` / Hermitian `sqrt(Y Y^H)`):** Must shift `arg det(Y_u Y_d)` away from its true non-zero value (`catching F-AGY-05 phase stripping`).
   - **Control 4 (Sheet-proportional `r = 5` weight in `2D` `V_{Gamma_0(5)}`):** Must flip `det Hess(V)` negative (`< 0`, saddle instability).
   - **Control 5 (Cubic `Z^4` lattice under Hurwitz `q = (1+i+j+k)/2 in 2T` & scalar `10` inserted as chiral fermion in `I_8`):** Must fail `Z^4` integrality (`1/2 not in Z`) and corrupt `I_8` coefficients.

6. **What is needed from main or from another seat:** Independent source reading of `AGY-C26` through `AGY-C28` alongside `Card R-AGY-C24` (`0 of 19`).

0 of 19.
