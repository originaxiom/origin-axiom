# Card AGY-C27: Exact Lamé Horocycle Solver, Complete 2-Loop Type-II 2HDM RGEs with Zero-Knob Conformal Instanton EWSB, and Exact Covi-Roulet-Vissani Leptogenesis (`F-AGY-01`, `F-AGY-04`, `F-AGY-06`)

1. **The package and the question, in a sentence:** Can we eliminate `grid.json` interpolation (`F-AGY-06`), restore the complete `2`-loop Type-II `2HDM` Yukawa and homogeneous soft-mass RGEs with `two_loop=True` literature benchmarks and zero-knob conformal instanton EWSB (`F-AGY-04`), and fix the `(1 - x)` resonant leptogenesis loop sign plus `8 / 23` `2HDM` sphaleron conversion (`F-AGY-01`) in a zero-float `0 of 19` script?

2. **What will be delivered, and what done means:** Pre-registered zero-float script `relays/agy_2026-11-22_c27/c27_lame_2loop_2hdm_rge_and_crv_leptogenesis.py`, `SCRIPT_SHA256.txt`, sealed `c27_out.json` with `OUTPUT_SHA256.txt` (`computed once`, `expectations committed first`), disjoint self-check `c27_countercheck.py` (`tested against planted errors`), and mask-clean relay testing:
   - **Expectation E1 (`F-AGY-06` — `frontier/`-Free Richardson-RK4 `mpmath` Lamé Solver for `L_2(tau)`):**
     - Compute canonical horocycle log-radius `L_2(tau)` directly from `y'' + (wp(z; tau)/4 + c(tau)) y = 0` on `E_tau \ {0}` with zero `frontier/` imports, zero binary64 interpolation, and zero `ymax = 6` clamping.
     - Match `B1667`'s closed-form `eta(exp(i pi / 3))^4` period integral to `< 10^{-9}` and verify mirror symmetry `|L_2((+16 + 8i)/5) - L_2((-16 + 8i)/5)| < 10^{-9}`.
   - **Expectation E2 (`F-AGY-04` — Complete `2`-Loop Type-II `2HDM` RGEs, Guardrail 4 Benchmarks, & Zero-Knob Conformal Instanton EWSB):**
     - Restore the complete `2`-loop Type-II `2HDM` gauge and Yukawa beta functions (`Machacek-Vaughn 1983/1984`, including `-9/4 (3 tr G_u^2 + tr G_nu^2) Y_u` so pure-top `2`-loop coefficient equals `-12`, plus `2`-loop EW/QCD/Yukawa terms) and `Buttazzo et al.` Appendix A `2`-loop `SM` quartic check at a synthetic rational UV point (`Guardrail 4`), plus `Pendleton-Ross` `1`-loop exact Bernoulli and `2`-loop quasi-fixed-point checks (`two_loop=True`).
     - Replace the un-decoupled `xi = 1/2` soft source with exact homogeneous `2HDM` soft-mass RGEs (`xi = 0`): prove symmetric positive `m_0^2 = (1, 1)` leaves `m_{H_u}^2(t_{EW}) > 0` (`honest No-Go`), whereas zero-knob conformal instanton EWSB (`m_{H_u}^2 = m_{H_d}^2 = 0`, `m_{12}^2 > 0` at `t_{EW} = -48 pi / 5`) eliminates `m_{12}^2 / m_0^2 = 1 / 40` completely, yields exact Newton-identical `tan(beta) = (lam_1 / lam_2)^{1/4}`, and gives four strictly positive scale-invariant `2HDM` boson ratios without top-loop double counting.
   - **Expectation E3 (`F-AGY-01` — Exact Covi-Roulet-Vissani `(1 - x)` Loop Sign & `8 / 23` `2HDM` Sphaleron Yield on `tau_*^-`):**
     - Prove symbolically in `sympy` that CRV `(1 - x)` gives `lim_{x -> inf} sqrt(x) f_{SV}(x) = -3 / 2` (`catching C23's +1/2 bug`), solve the `Harvey-Turner` chemical-potential system symbolically for `B / (B - L) = 4 (N_H + 2 N_g) / (13 N_H + 22 N_g) = 8 / 23` at `(N_g, N_H) = (3, 2)`, and compute `3`-flavor washout-weighted `Y_B` across both CP hands: proving `Y_B(tau_*^+) < 0` (`antimatter`) while `tau_*^- = (-2 + i) / 5` gives `Y_B(tau_*^-) = -Y_B(tau_*^+) > 0` (`matter`) with identical CP-even observables (`< 10^{-35}`).

3. **How it could come out wrong, written before any run:**
   - **F1:** The standalone Lamé solver could miss the closed-form `eta^4` period benchmark at `exp(i pi / 3)` by `> 10^{-8}` or break mirror symmetry on `tau_8^{+-}`.
   - **F2:** Under complete `-12 y_t^5` `2`-loop Type-II `2HDM` running to `t_{EW} = -48 pi / 5`, boundedness-from-below `lam_3 + lam_4 + sqrt(lam_1 lam_2) > 0` or any of the four conformal-instanton `2HDM` boson eigenvalues could turn negative.
   - **F3:** Under exact CRV `(1 - x)` and `3`-flavor Boltzmann washout weighting, `Y_B(tau_*^-)` could fail to flip positive or fail Haar `U(3)_L x U(3)_{e_R} x U(3)_{nu_R}` invariance (`< 10^{-30}`).

4. **What it rests on, and what it must not touch:** Rests on `AGY-C26` (`iso-singlet holomorphic Yukawa construction`) and `Card R-AGY-C24` (`631bb5859`). Must not touch `main`, `agy/audit-2026-11-02`, `frontier/` data/grid files, or any measured constant (`0 of 19`).

5. **Controls that must fail if the work is broken:**
   - **Control 1 (Linearly interpolated `grid.json` `L_2` vs exact Lamé `L_2`):** Must detect chord-interpolation offset `> 10^{-3}` at `tau_8`.
   - **Control 2 (Truncated `-21 / 4` pure-top `2`-loop Yukawa coefficient & `d/d ln(mu^2)` factor-of-`2` error):** Must miss exact `-12` (`9 / 16` missing fraction) and fail `Pendleton-Ross` (`> 1 / 10`).
   - **Control 3 (Symmetric positive `m_0^2 = (1, 1)` homogeneous `2HDM` running at `xi = 0`):** Must leave `det M_Phi^2(t_{EW}) > 0` (`no EWSB`), confirming `F-AGY-04` item two.
   - **Control 4 (Buggy `(x - 1)` self-energy numerator & `1HDM` `28 / 79` sphaleron factor):** Must give wrong asymptotic sign `+1 / 2 != -3 / 2`, flip `Y_B` sign on `tau_*^+`, and differ from `8 / 23`.
   - **Control 5 (Perturbing `m_{12}^2` by `100x` in Conformal Instanton EWSB):** Must leave `tan(beta)` and all four `m_H / v_{EW}` ratios invariant to `< 10^{-35}`, whereas dropping `l_4` corrupts `m_{H^{+-}} / v_{EW}`.

6. **What is needed from main or from another seat:** Independent source reading alongside `AGY-C26` and `AGY-C28` (`0 of 19`).

0 of 19.
