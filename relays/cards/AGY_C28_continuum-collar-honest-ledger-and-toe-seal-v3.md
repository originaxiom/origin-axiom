# Card AGY-C28: Continuum Iso-Singlet Collar ODE, Fully Counterchecked `blind_predictions_full_toe_v3.json` Seal, Honest Guardrail-1 Bit Ledger, and Governance Remediation (`F-AGY-06`, `F-AGY-07`, `F-AGY-10`)

1. **The package and the question, in a sentence:** Completing our response to `Card R-AGY-C24` (`631bb5859`), can we integrate the continuum `1D` radial collar operator (`F-AGY-07`), pass true `N = 120` vs `N = 240` step-halving `< 10^{-7}` with zero step-count substitution (`F-AGY-10`), price every discrete input transparently (`F-AGY-07`), and verify `100%` of sealed entries in `blind_predictions_full_toe_v3.json` by a disjoint zero-shared-code self-check (`F-AGY-06`, `0 of 19`)?

2. **What will be delivered, and what done means:** Pre-registered zero-float script `relays/agy_2026-11-22_c28/c28_continuum_collar_honest_ledger_and_toe_seal_v3.py`, `SCRIPT_SHA256.txt`, locked `blind_predictions_full_toe_v3.json` + `c28_out.json` with `OUTPUT_SHA256.txt` (`computed once`, `expectations committed first`), `100%`-coverage disjoint self-check `c28_countercheck.py` (`tested against planted errors`), and mask-clean synthesis relay testing:
   - **Expectation E1 (`F-AGY-07` — Continuum Radial Collar ODE & `T^4 / Z_5` Rank Contradiction Retraction):**
     - Integrate the genuine continuum `1D` radial Dirac boundary-value ODE `(sigma_3 d/dr + M(r)) Psi(r) = 0` across `4` domain walls on `[0, 4 L_c]` (`replacing C21's literal wrap_amp = mp.mpf(0)`), proving continuum wavefunction localization reproduces the discrete iso-singlet overlap `k_f^4` up to exponentially small `O(e^{-2 M L_c})` finite-collar tunneling.
     - Retract `C21`'s `T^4 / Z_5` `Q_1 = 1 / 25` rank-`1` zero-mode claim (`which contradicted rank-3 M_R = M_0 I_3 and mis-divided standard T^4 minimal toron Q = 1 / 5`) and `0`-bit `FORCED` label on post-Landau-pole `k = 40`, pricing both transparently in the discrete ledger.
   - **Expectation E2 (`F-AGY-06` & `F-AGY-10` — `blind_predictions_full_toe_v3.json` on `tau_*^+`, True `N = 120 vs 240 < 10^{-8}` Step-Halving, & `100%` Self-Check Coverage):**
     - Seal `blind_predictions_full_toe_v3.json` (`0` JSON floats, `SHA-256` payload digest) on primary `tau_*^+ = (+2 + i) / 5` (`where AGY-C27 proved holomorphic linear-weave CRV (1 - x) + 8 / 23 gives Y_B^{hol}(tau_*^+) > 0`), combining `22` `MS-bar` observables (`with raw non-zero Strong-CP bar_theta_{QCD}(tau_*^+)`), `12` `1`-loop Tarrach pole & zero-knob conformal `2HDM` boson ratios (`no double-counted top log`), `5` Hurwitz `D_4 / 2T` `11D` `M`-theory gravity ratios (`covolume 1 / 2 -> (2 pi)^4 / 48`), and `5` `CRV` `(1 - x)` + `8 / 23` cosmological quantities (`44` numerical entries total).
     - Achieve actual `n_steps = 120` vs `n_steps = 240` Richardson-RK4 relative drift `< 10^{-8} << 10^{-7}` across all `39` ODE-evolved entries (`zero step-count substitution!`), `0 / 2000` matched-null hits (`r_{95} < 1 / 500`), and `100%` (`44 / 44`) independent recomputation in `c28_countercheck.py` (`zero dummy constants, zero pasted strings!`).
   - **Expectation E3 (`F-AGY-07` & `F-AGY-10` — Honest Guardrail-1 Bit Ledger & `docs/seats/README.md` Section `12` Audit):**
     - Price all discrete inputs transparently (`1` unit anchor `v_{EW}`, `M_4` soldering + rank-`8`, `tau_*^+` Fricke/CP branch, equal-sheet `r = 1`, `5`-site iso-singlet collar, post-`1/24`-Landau-pole `k = 40`, `(p_3, p_4)` orbit representatives vs full `24 + 24` democratic weave benchmark, and instanton horizons `t_nu, t_{EW}`), and enforce strict `docs/seats/README.md` section `12` check labels across `STATUS_AGY.md` and the synthesis relay.

3. **How it could come out wrong, written before any run:**
   - **F1:** Continuum radial ODE integration could fail to converge to `k_f^4` as `M L_c` increases, or finite-collar wrapping at `M L_c = 12` could exceed `10^{-8}`.
   - **F2:** True `n_steps = 120` vs `n_steps = 240` step-halving on `c28` could exceed `10^{-7}` on any of the `39` ODE-dependent entries, or `c28_countercheck.py` could differ by `> 10^{-8}` on any of the `44` sealed entries.
   - **F3:** Any post-inspection item (`k = 40`, `r = 1`, `(p_3, p_4)`, `t_{EW}`) could be priced at `0` bits (`violating Guardrail 1`), or any literal `0` Strong-CP flag could remain (`violating Guardrail 2`).

4. **What it rests on, and what it must not touch:** Rests on `AGY-C26`, `AGY-C27`, and `Card R-AGY-C24` (`631bb5859`). Must not touch `main`, `agy/audit-2026-11-02`, sealed `v1.json` / `v2.json`, or any measured constant (`0 of 19`).

5. **Controls that must fail if the work is broken:**
   - **Control 1 (Short collar `M L_c = 1 / 2` tunneling leak):** Must exhibit `O(e^{-1}) > 1 / 20` deviation from `k_f^4`, proving the continuum radial solver is genuinely integrating `Psi(r)` rather than returning a literal `0`.
   - **Control 2 (Single-character `JSON` tamper & literal `"0"` Strong-CP check):** Must fail `SHA-256` payload verification and assert `|bar_theta_{QCD}(tau_*^+)| > 1 / 2`.
   - **Control 3 (`0`-bit pricing on post-Landau-pole `k = 40` or second `GeV` anchor):** Must raise hard exceptions in the Guardrail `1` & `5` ledger validator.
   - **Control 4 (Pasting dummy constants or skipping any `v3.json` key in `c28_countercheck.py`):** Countercheck key-set equality `checked_keys == all_44_v3_keys` (`44 / 44`) must fail if even `1` key is omitted.
   - **Control 5 (Coarse `1`-step Euler integration vs `N = 240`):** Must exceed `10^{-2} >> 10^{-7}`, proving the `N = 120 vs 240` step-halving gate has genuine numerical bite.

6. **What is needed from main or from another seat:** Independent source reading of `AGY-C26` through `AGY-C28` and `blind_predictions_full_toe_v3.json` (`0 of 19`).

0 of 19.
