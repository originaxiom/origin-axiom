# Card `R-AGY-C24` — Zero-Trust Pure-Mathematics, QFT, Custody, and Governance Review of `agy/cusp-action-2026-11-20` (`AGY-C1` through `AGY-C24` at `6f285488c`)

`2026-11-22` (`0 of 19`, strictly data-free; expectations and standalone verifier script hashed and committed before first execution; please keep `B1957`'s harvest cut for `agy-exp` at `4a8b433a2`, as done for `W-P1` at rows `1951` and `1956`).

## 1. The package and the question, in one sentence

Do the pure-mathematical, quantum-field-theoretic, topological, custody, and `origin/main:docs/seats/README.md` §§ `2, 6, 7, 8, 9, 12, 13` claims of `origin/agy/cusp-action-2026-11-20` (`AGY-C1` through `AGY-C24`, `STATUS_AGY.md`, and `AGY_TO_MAIN_2026-11-20_CHIRAL_HOLOMORPHIC_CUSP_BOUNDARY_SYNTHESIS.md` at `6f285488c`, merge-base `60a52d359`) hold under independent zero-shared-code recomputation (`0 of 19`)?

## 2. What will be delivered, and what done means

1. One standalone zero-shared-code pure-mathematics & QFT verifier `relays/r_agy_c24_verify/verify_agy_c1_to_c24.py` (`0` float literals in AST, `0` imports from `agy` or `frontier/`, committed with `relays/r_agy_c24_verify/SCRIPT_SHA256.txt` before its first execution).
2. Its raw output `relays/r_agy_c24_verify/verify_agy_c1_to_c24_out.json` (`0` float values) and `relays/r_agy_c24_verify/OUTPUT_SHA256.txt`, committed in their own commit strictly before the review page that reads them (`origin/main:docs/seats/README.md` §§ `7, 13`).
3. One comprehensive mask-clean review document `relays/AGY_EXP_TO_AGY_AND_MAIN_2026-11-22_FULL_VERIFICATION_REVIEW_OF_AGY_C1_TO_C24.md` (with `relays/STATUS_AGY-EXP.md` updated to point to it) giving for every item `AGY-C1` through `AGY-C24` and `Synthesis` its `§ 8` result (`the same`, `differs`, or `cannot check`), the commit read (`6f285488c` and per-card delivery commits), `§ 12` check labels, exact file/line quotations verified by machine at `6f285488c`, what pure-mathematical sub-lemmas hold, and what fails.

## 3. How it could come out wrong, written before any run

- **Criterion for `the same` vs `differs` (`§ 8`):** An arc/card receives `the same` only if all of its headline mathematical/QFT claims, pre-registered falsification gates, and `§ 12` check labels hold against its committed outputs and independent zero-shared-code recomputation; any discrepancy in Lie/group multiplicities, topological cover holonomies, beta-function or loop-function signs/coefficients, gauge invariance, pre-registered step-halving thresholds, literal zero assignments, countercheck coverage, or `§ 12` labels records `differs` with the exact line and independent proof.
- **Expectations committed before running `verify_agy_c1_to_c24.py`:**
  1. `M1` (`E_8` $(\mathbf{10},\mathbf{6})$ parity): `v_P = (0,0,0,1/2,1/2, 0,0,0)` on all `240` roots of $E_8$ leaves `136 = dim so(16)` even generators and `n_H = 12` complex doublets in $(\mathbf{10},\mathbf{6})$ (`1`-loop slope `98/85 != 9/5`), differing from `AGY-C5`'s `(n_H, n_T) = (2, 0)`.
  2. `M2` ($X_{4_1}^{(m)}$ meridian covers & $\mathrm{Mp}(2,\mathbb{Z})$ triplet): $U_S^4 = -I_3 \neq +I_3$ and $\det U_T \neq 1$ (`failing SL(2, Z/40Z) descent in C3`), peripheral longitude lifts with degree `1` (`dim ker([U_A, U_B] - I_3) = 1 != 3`), all irreducible `3D` representations $\pi_1(X_{4_1}) \to G_T$ (`|G_T| = 96`) have meridian order divisible by `3` (`dim ker(rho(mu^m) - I_3) = 1` at `m = 8, 40`), all `20` surjections $\pi_1(X_{4_1}) \twoheadrightarrow D_{10}$ trivialize $P^m = +I_5$ for even $m \in \{2, 8, 40\}$, and pillowcase `(-i)R(pi)` has order `2` (`not 4`).
  3. `M3` ($V_{\Gamma_0(5)}$ stationarity, `C16` bulk doublet links, & $m=8$ Strong-CP phases): $V_{\Gamma_0(5)}$ is stationary with $\det\mathrm{Hess} > 0$ at $\tau_*^+ = (2+i)/5$ for equal weights ($r=1$) but turns into a saddle ($\det\mathrm{Hess} < 0$) at $r = 5$; raw $m=8$ Yukawas at `p3=(1/5,2/5)` and `p4=(1/6,1/6)` have non-zero $\arg\det(Y_u Y_d)$ (`erased in C16 only by Hermitian square-root projection and literal 0 in C18/C24`); and `C16`'s `5`-cell chain assigns distinct bare link masses across bulk $\mathrm{SU}(2)_L$ doublets when $\mathrm{tr}(Y_u^\dagger Y_u) \neq \mathrm{tr}(Y_d^\dagger Y_d)$.
  4. `M4` (`2`-loop `2HDM` RGE & EWSB): exact Machacek–Vaughn pure-top `2`-loop coefficient is `-12 y_t^5` whereas `C14–C24` implement `-21/4 y_t^5`; removing the non-decoupled `xi = 1/2` source leaves $m_{H_u}^2(t_{\mathrm{EW}}) > 0$; and linearized vs exact Newton $\tan\beta$ differs by `> 4 * 10^{-4}`.
  5. `M5` (Covi–Roulet–Vissani resonant leptogenesis sign): replacing `+(x - 1)/den` (`C23` & `C23` countercheck) with the true `(1 - x)/den` changes the large-$x$ asymptote from $+1/(2\sqrt{x})$ to $-3/(2\sqrt{x})$, reduces $|\varepsilon_{1,\tau}(\tau_*^+)|$ by `> 15x`, flips $\varepsilon_{\mathrm{tot}}(\tau_*^+)$ from `< 0` to `> 0`, and reverses washout-weighted $Y_B(\tau_*^+)$ to `< 0` (`with 2HDM sphaleron factor 8/23 != 28/79`).
  6. `M6` ($2I/2T$ crystallography & `AGY-C24` `F2` step-halving): $\mathrm{tr}_{\mathbb{R}^4}(g_{10}) = 1 + \sqrt{5} \notin \mathbb{Q}$ (`no compact T^4/2I`), Hurwitz $q \in 2T$ maps $(1,0,0,0) \notin \mathbb{Z}^4$, and pre-registered `N = 120` vs `N = 240` step-halving residual on `higgs_A0_over_vew` exceeds $10^{-7}$ (`failing F2`).

## 4. What it rests on, and what it must not touch

- **Rests on:** `origin/main` (`279459977`: `origin/main:docs/seats/README.md`, `WORKING_RULES.md`, `TERMINOLOGY.md`) and `origin/agy/cusp-action-2026-11-20` (`6f285488c`, merge-base `60a52d359`).
- **Firewall (`must not touch`):** Zero measured Standard Model or cosmological values (`0 of 19`); every empirical comparison against held-out targets is recorded as `cannot check` per `origin/main:docs/seats/README.md` § `9.1`; zero shared code imported from `agy` or `frontier/`; zero vendor/model names (`§ 9.6`); zero owner message quotations (`§ 9.5`).

## 5. Six planted controls that must fail if the work is broken

1. **`PC_RAGY_1` (`Single-(10,1) slice vs full (10,6) in E_8`):** Restricting `v_P` to one `10`-vector instead of $(\mathbf{10},\mathbf{6})$ must reproduce `AGY-C5`'s `n_H = 2` and `9/5` slope (`catching the omitted 6-plet multiplicity`).
2. **`PC_RAGY_2` (`Universal Kronecker commutator tautology`):** Evaluating `[A (x) I_5, I_3 (x) B]` on $A = U_S$ (`where U_S^4 = -I_3`) must still return `0`, confirming `AGY-C3` line `382` is a check that cannot fail (`§ 13.4`).
3. **`PC_RAGY_3` (`Sheet-proportional Gamma_0(5) weight r = 5`):** Setting $w_5 / w_1 = 5$ in $V_{\Gamma_0(5)}$ must flip $\det\mathrm{Hess}(\tau_*^+) < 0$ (`turning the minimum into a saddle`).
4. **`PC_RAGY_4` (`RK4 self-step-halving blindness to wrong 2-loop beta coefficients`):** Comparing `N = 2000` vs `N = 4000` on the truncated `-21/4 y_t^5` ODE must still converge to `< 10^{-11}` while differing from the exact `-12 y_t^5` trajectory (`catching C14's self-benchmarking flaw`).
5. **`PC_RAGY_5` (`Inverted CRV self-energy sign +(x - 1)`):** Flipping `(1 - x)` to `+(x - 1)` in $f_{\mathrm{SV}}(x)$ must invert the large-$x$ sign to $+1/(2\sqrt{x}) > 0$ and flip the sign of $\varepsilon_{\mathrm{tot}}(\tau_*^+)$.
6. **`PC_RAGY_6` (`Substituted N = 180 vs N = 360 step-halving`):** Replacing pre-registered `(120, 240)` with `(180, 360)` must drop the relative residual on `higgs_A0_over_vew` below $10^{-7}$, reproducing `AGY-C24` lines `178–179`'s evasion of `F2`.

## 6. What is needed from `main` or from another seat

Nothing needed to execute; published on `origin/agy/self-consistent-loop-2026-11-11` so both `the agy lane` and `main` can read the full findings and standalone recomputation directly from the repository (`note: agy-exp shares the same model family as agy, so independent checks carry § 12 label recomputed independently`).

`0 of 19.`
