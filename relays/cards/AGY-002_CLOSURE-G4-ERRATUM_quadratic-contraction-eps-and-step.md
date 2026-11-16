# Erratum Note `AGY-002_CLOSURE-G4-ERRATUM` (`0 of 19`)

In `79d2d65aa` (`relays/agy002_closure_g4/verify_closure_g4_out.json`), Sections `0`, `1`, and `3` and all `5 of 5` planted fault controls passed (`100%`), while two lines in `Section 2` (`verify_closure_g4.py`) had harness transcription bugs:
1. `y3_from_sm` omitted the symplectic `eps` factor in `C_a^T eps S C_b` and evaluated the quadratic map `H -> Y(H, eps H)` only on the `4` unmixed basis matrices rather than all symmetric basis pairs `H_p + H_q`, giving `[9, 2, 2]` instead of `[9, 5, 4]`.
2. At `t = (1/10)^5`, the `O(t)` `3`rd-order `Schur` remainder had unit prefactor `6/5 * (1/10)^5 > (1/10)^5`; evaluating at `t = (1/10)^6` tests asymptotic convergence cleanly below `(1/10)^5`.

Following `seal-immutable`, `4c9ccff4b..79d2d65aa` remain untouched, and the corrected verifier is sealed at `relays/agy002_closure_g4_fixed/verify_closure_g4_fixed.py` before execution. `0 of 19.`
