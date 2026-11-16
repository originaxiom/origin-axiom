# Erratum Note `AGY-002_CLOSURE-G4-REFEREE-ERRATUM` (`0 of 19`)

In `23d525ec0` (`relays/agy002_closure_g4_referee/referee_closure_g4_out.json`), Section `0` and physics invariants (`Buttazzo` `t_crit` cross-solver diff `3.10e-14`, symbolic `BPV` `-11/2` vs `PF4.1` `-7`, `Strong-CP` `3.89e-16`, `U(3)^6` `Haar` `6.26e-14`, `[9, 5, 4]`, `[1, 2]`, `[0, 0, 0, 0]`, `C_UV = 189/2`, `C_IR = 28`, `PF4.2–PF4.5`) succeeded, while four referee-harness transcription bugs occurred:
1. `sp.expand_complex` on `18` `real=True` symbols in `Section 2A` caused an `871 s` symbolic real/imag expansion bottleneck, and unexpanded `Mul(I, Add(...))` in `Section 2B` triggered false `Matrix.__ne__` mismatches on `Q_8`.
2. `Section 1C` evaluated the `4`-point `2`-loop `CKM` `ODE` finite-difference stencil in `float64` (`~7e-10` subtraction noise) rather than `45`-digit `mpmath`, and normalized `PF4.1`'s relative shift by the total polynomial rather than the `-11/2` `y_t^2 y_b^2` coefficient (`3/11 > 1/10`).
3. `Section 3B` wrote `(4 / z) * K_3(z)` (`nu = 2`) instead of `(6 / z) * K_3(z)` (`2 * nu = 6` at `nu = 3`) in `K_4(z) = K_2(z) + (6 / z) K_3(z)`.

Following `seal-immutable`, `3d900ed8a..23d525ec0` remain untouched, and the repaired cold-room referee script is sealed at `relays/agy002_closure_g4_referee_fixed/referee_closure_g4_fixed.py` before execution. `0 of 19.`
