# Card AGY-C16: Five-Cell Collar Kaplan-Dirac Derivation and Neutrino Untwisting

1. **The package and the question, in a sentence:** Under `AGY-C15`, can the basis-covariant five-sheet charged overlap `Y_f (Y_f^\dagger Y_f)^2 / (tr(Y_f^\dagger Y_f))^2` and the untwisted one-step neutrino see-saw `Y_\nu Y_\nu^T` both be derived simultaneously from one uniform `30 x 30` Weyl Dirac-Majorana operator on the five-cell collar of `X_{4_1}^{(40)} -> X_{4_1}^{(8)}` using Standard Model gauge invariance alone?

2. **What will be delivered, and what done means:** A pre-registered, hashed `0 of 19` script `relays/agy_2026-11-21_c16/c16_five_cell_collar_kaplan_derivation.py`, raw output, a zero-shared-code independent countercheck `c16_countercheck.py` with five planted negative controls, and a mask-clean result relay testing:
   - **Expectation E1 (Pure-Higgs `Z_5` No-Go vs Trace-Normalized Five-Cell Schur Complement):** Prove across all `125` assignments `(q_L, q_R, q_H) in (Z/5Z)^3` that a `Z_5` phase on `(f_L, f_R, H)` gives identical charge `+q_H` to `Y_f (Y_f^\dagger Y_f)^k` for every `k >= 0`, whereas on the open five-cell collar (`Walls 0..5` of `[X_{4_1}^{(40)} : X_{4_1}^{(8)}] = 5`) with Frobenius bulk mass `M_{KK,f}^2 = xi_M^{-2} tr(Y_f^\dagger Y_f)`, the exact `15 x 15` Schur complement yields `xi_M^4 Y_f (Y_f^\dagger Y_f)^2 / (tr(Y_f^\dagger Y_f))^2` with zero `k < 2` leakage and zero finite-`epsilon` `CKM` eigenvector rotation.
   - **Expectation E2 (Uniform `30 x 30` Weyl Unification of Charged `5`-Step and Neutral `1`-Step Sectors):** Put one uniform `G_{SM}`-invariant Majorana mass `M_0` on every `G_{SM}`-neutral `(1, 1)_0` Weyl spinor across all walls (`both N^c_{1,3,5} and N_{1,3,L}`), with `M_0 = 0` on `(u, d, e)` forced by `SU(3)_C x U(1)_Y` conservation; verify symbolically and at `45`-digit precision that the exact `30 x 30` neutral Schur complement gives `(M_0 / (M_{KK}^2 - M_0^2)) v_u^2 Y_\nu(8) Y_\nu(8)^T + O((v_u / M_{KK})^6)`, preserving `U(3)_L x O(3)_{\nu_R}` invariance beyond `10^{-35}` and `O(1)` solar and atmospheric `PMNS` mixing alongside `5-6` decade charged hierarchies.
   - **Expectation E3 (Degree-`1` Scale Homogeneity & Removal of Synthetic `svd` Indexing):** Verify that `Y_f (Y_f^\dagger Y_f)^2 / (tr(Y_f^\dagger Y_f))^2` is strictly homogeneous of degree `1` in `Y_f(8)`, `U(3)_L x U(3)_R`-covariant beyond `10^{-35}`, and yields `UV` `y_{d3} / y_{e3}` inside `(1/2, 4/5)` so `2`-loop `QCD` running lifts `IR` `y_{d3} / y_{e3}` above `3/2` with zero hand-coded `svd` index or `4/5` literal.

3. **How it could come out wrong, written before any run:**
   - **F1:** Interior `KK` mixing at finite `epsilon = v / M_{KK}` could rotate the left singular vectors `U_{L,u}` relative to `U_{L,d}`, distorting `CKM` mixing away from the `m = 8` collar structure.
   - **F2:** Putting `M_0` uniformly on all odd walls (`1, 3, 5`) could trigger an inverse-seesaw cancellation at `O(v_u^2)` and collapse `m_eff(nu_L)` to `O(v_u^{10})`.
   - **F3:** Replacing `AGY-C15`'s sector-by-sector `svd[2]` normalization with the analytic invariant `(tr(Y_f^\dagger Y_f))^2` could drive `UV` `y_{d3} / y_{e3}` too low (`< 1/3`) for `2`-loop `QCD` to recover `y_{d3} > y_{e3}`.

4. **What it rests on, and what it must not touch:** Rests on `AGY-C5`, `AGY-C7`, `AGY-C10`, `AGY-C12`, and `AGY-C15` (`dee7da71a`) on `agy/cusp-action-2026-11-20`, aligned with `origin/main` at `279459977`. Must not touch `main`, `agy/audit-2026-11-02`, or any measured target (`0 of 19`).

5. **Controls that must fail if the work is broken:**
   - **Control 1a (Periodic `0 ~ 5` collar shortcut):** Adding a direct boundary wrap `Wall 0 <-> Wall 5` spoils `k = 2` selection and collapses `5-6` decade charged hierarchies back to `2` decades; must be caught.
   - **Control 1b (Omitting `M_0` on `N_{1,3,L}`):** Setting `M_0 = 0` on left bulk singlets while keeping `M_0 != 0` on `N^c_{1,3,5}` triggers exact inverse-seesaw cancellation to `O(y^{10})`; must be caught.
   - **Control 2 (Un-normalized `M_{KK} = 1` vs trace-normalized `M_{KK,f}^2 ~ tr(Y_f^\dagger Y_f)`):** Omitting the trace kinetic mass collapses `UV` `y_{d3} / y_{e3}` below `1/5`; plus full `35`-digit Haar `U(3)^5 x O(3)_{\nu_R}` scrambling across the `30 x 30` operators (`drift < 10^{-30}`).

6. **What is needed from main or from another seat:** Nothing (`0 of 19`).

0 of 19.
