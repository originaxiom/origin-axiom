# Card AGY-C40: Unbroken `4D` `N = 1` SUSY, `E[2] \ {0} <-> 3` Generations, & `|2T| = 24` Modular-Gauge Scale Transmutation (`0 of 19`)

1. **The package and the question, in a sentence:** Executing Layer `2` of the Top-Down Synthesis, does mapping `E[2] \ {0}` bijectively to `N_{gen} = 3` while keeping `4D` `N = 1` SUSY unbroken at `M_{KK}` lock `tau_*^+ = (2 + i) / 5` as a strict minimum, derive `Lambda_{SU(5)_perp} / M_{GUT} = |q(tau_8^+)| = exp(-16 pi / 5)` at `alpha_{GUT}^{-1} = |2T| = 24`, and satisfy `8 / 8` compatibility gates (`0 of 19`)?

2. **What will be delivered, and what done means:** Pre-registered zero-float producer `relays/agy_2026-11-24_c39/c40_unbroken_susy_e2_3gen_and_native_e8_condensation.py`, `SCRIPT_SHA256.txt`, first-run `c40_out.json` with `OUTPUT_SHA256.txt` (`computed once`, `expectations committed first`), disjoint cold-room `c40_countercheck.py` (`tested against planted errors`), updated `relays/STATUS_AGY.md`, and relay testing:
   - **Expectation E1 (`E[2] \ {0} <-> 3` Generations Fricke Minimum & Elimination of `OW22-F2/F3` & `BL1-F1/F2`):**
     - Prove that assigning the `3` chiral generations `1-to-1` to `E[2] \ {0} = {(1 / 2, 0), (0, 1 / 2), (1 / 2, 1 / 2)}` yields `V_{3gen}^{(5)}(tau) = -sum_{p in E[2] \ {0}} [E_3(tau; p) + E_3(-1 / (5 tau); p)] = +(15 / 16)[E_3(tau) + E_3(-1 / (5 tau))]`, locking `tau_*^+ = (2 + i) / 5` (`tau_8^+ = 8 tau_*^+ = (16 + 8 i) / 5`) as a **strict local minimum** (`||grad_2 V|| < 10^{-38}`, both Hessian eigenvalues `> 50`, zero embedded coordinates per Guardrail `1`), whereas a single Scherk-Schwarz twist `(1 / 2, 0)` breaks `W_5` (`||grad|| > 50`, `Control 1`).
     - Prove unbroken `4D` `N = 1` MSSM on `T^2` sets tree-level `M_{SS} == 0` (`delta m_H^2(M_{KK}) == 0`), preserving `B_{MSSM} = 5 / 7` across `[M_{SUSY}, M_{GUT}]` (`vs r_{SS} = ln(2) / 30` collapsing `B_{eff} < 3 / 5`, `Control 2`).
   - **Expectation E2 (`|2T| = 24` Modular-Gauge Instanton Duality & Exact Rational `1`-Loop Couplings at `M_{SUSY}`):**
     - Prove that at topological `2T`-cover level `alpha_{GUT}^{-1} = |2T| = 24` (`priced honestly as 1 discrete level choice vs k = 40`) with hidden `SU(5)_perp subset E_8^{(2)}` (`b_0 = 3 N_c = 15` from `AGY-C39`), RG dimensional transmutation gives the exact **Modular-Gauge Instanton Identity**:
       `Lambda_{SU(5)_perp} / M_{GUT} = exp(-2 pi * 24 / 15) = exp(-16 pi / 5) == |q(tau_8^+)|` (`< 10^{-45}`), fixing seesaw `M_0 / M_{GUT} = exp(-16 pi / 5)` and soft SUSY-breaking `M_{SUSY} / M_{GUT} = (Lambda_{SU(5)_perp} / M_{GUT})^3 = exp(-48 pi / 5)` (`M_{SUSY}^2 / M_{GUT}^2 = exp(-96 pi / 5) == |q(tau_8^+)|^6`, replacing retracted fractional torons!).
     - Prove that running `1`-loop MSSM over `Delta t / (2 pi) = 24 / 5` from `alpha_{GUT}^{-1} = 24` to `M_{SUSY}` yields pure exact rationals `(alpha_3^{-1}, alpha_2^{-1}, alpha_1^{-1}, alpha_{EM}^{-1}, sin^2 theta_W) = (48 / 5, 144 / 5, 1392 / 25, 608 / 5, 9 / 38)`, and record the native rank-`<= 8` `E_8^{(2)}` `DKL`-dressed `S`-racetrack scan (`honestly disclosing that pure-SYM c_1 = c_2 = 1 has no finite root without unequal integer indices/ranks, `Control 3`).
   - **Expectation E3 (`8 / 8` Single-Origin Compatibility Matrix & `11D` Friedmann-Witten Gravity at `k = |2T| = 24`):**
     - Verify `8 / 8` compatibility gates simultaneously (`B = 5 / 7`, `Str(M^0) = 0`, `MSSM D-term BFB`, `stage-consistent STr a_1(xi = 0) = 39 / 2 > 0 UV & 37 / 2 > 0 IR`, `C_6 > 0 & R_{crit}`, `6D tr R^4 = tr F^4 = 0`, `strict Fricke minimum at tau_*^+`, `conformal S_{+4} N = 60 plateau`) and compute exact `30`-digit `M_{11} / M_{GUT}` and `(M_{Pl} / M_{GUT})_{SD, ISO}` at `k = 24`.

3. **How it could come out wrong, written before any run:**
   - **F1:** `V_{3gen}^{(5)}(tau)` at `tau_*^+ = (2 + i) / 5` could be a saddle (`min Hessian eig <= 0`) rather than a strict minimum.
   - **F2:** `exp(-2 pi * 24 / 15)` could differ from `|q(tau_8^+)|`, or `alpha_3^{-1}(M_{SUSY})` at `k = 24` could hit a Landau pole (`<= 0`).
   - **F3:** Disjoint `2D` Riemann-Mellin & `M_{11}`-free Friedmann-Witten countercheck in `c40_countercheck.py` could disagree with `c40_out.json`.

4. **What it rests on, and what it must not touch:** Rests on `AGY-C37..C39`, `27f5d89fa` (`OW22`), and `639a5d46b` (`DKL`). Must not touch sealed past files, `main`, `agy/audit-2026-11-02`, peer branches, or empirical constants (`0 of 19`).

5. **Controls that must fail if the work is broken:**
   - **Control 1 (Single `(1 / 2, 0)` twist vs `3`-generation `E[2] \ {0}` sum):** A single twist `(1 / 2, 0)` must break Fricke stationarity at `tau_*^+` (`||grad|| > 50`), whereas `E[2] \ {0}` gives `||grad|| < 10^{-38}` and `2 / 2` positive Hessian eigenvalues.
   - **Control 2 (`T^2` Scherk-Schwarz `M_{SS} = M_{KK} / 2` vs unbroken `4D` `N = 1` MSSM down to `M_{SUSY}`):** `r_{SS} = ln(2) / (48 pi / 5)` must collapse `B_{eff} < 3 / 5 != 5 / 7`, whereas unbroken MSSM gives exact `5 / 7`.
   - **Control 3 (`k = 40` fractional toron `Q = 1 / 5 => exp(-16 pi)` vs `k = 24`, `b_0 = 15` gaugino condensation `exp(-16 pi / 5)`):** Retracted `Q = 1 / 5` toron at `k = 40` must miss `|q(tau_8^+)|` by `exp(-64 pi / 5) < 10^{-17}`, whereas `exp(-2 pi * 24 / 15) == |q(tau_8^+)|`.
   - **Control 4 (Non-SUSY `B1` `a_1(xi = 0) = -46 / 3 < 0` & `B = 5 / 9` vs SUSY `39 / 2 > 0` & `5 / 7`):** Non-SUSY `B1` must fail `B = 5 / 7`, `Str(M^0) = 0`, and `a_1(xi = 0) > 0`, whereas Layer-`2` SUSY passes `8 / 8`.
   - **Control 5 (Un-normalized `T_{M2} = M_{11}^3` vs exact `T_{M2} = M_{11}^3 / (2 pi)^2` at `k = 24`):** Omitting `(2 pi)^{-2}` must mis-scale `M_{11} / M_{GUT}` by `(2 pi)^{2/3} > 3`.

6. **What is needed from main or from another seat:** Export `tau_*^+ = (2 + i) / 5`, `tau_8^+ = (16 + 8 i) / 5`, `alpha_{GUT}^{-1} = 24`, `M_0 / M_{GUT} = exp(-16 pi / 5)`, and `M_{SUSY} / M_{GUT} = exp(-48 pi / 5)` directly into Layer `3` (`AGY-C41`) and Layer `4` (`AGY-C42`).

0 of 19.
