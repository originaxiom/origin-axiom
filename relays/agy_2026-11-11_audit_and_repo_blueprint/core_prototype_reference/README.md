# `origin-axiom-core` — Distilled Zero-Trust Mathematical Verification Prototype

`origin-axiom-core` is a standalone, lightweight (`< 15 MB`), strictly data-free (`0 of 19`) verification package demonstrating how proven pure-mathematics theorems and executable formal guardrails from the Origin Axiom research programme can be packaged cleanly apart from historical exploration logs.

## Architecture & Scope

1. **Zero Empirical Targets (`0 of 19`):** No Standard Model measured masses, mixing angles, `chi2` fit scores, or held-out observables (`D11` / `P-709`) appear anywhere in this repository.
2. **Executable Formal Guardrails (`origin_axiom_core.guardrail_dsl`):**
   - **Guardrail 1 (`@stabilization_potential`, `LedgerContext.select_from`, `@zero_bit_prediction`):** Rejects potentials $V(x)$ that embed target coordinates or constant shifts $(x - x^*)$, verifies $\|\nabla V(x^*)\| < 10^{-8}$ and $\lambda_{\min}(\operatorname{Hess} V(x^*)) > 0$, and prices discrete candidate scans at $+\log_2 N$ bits.
   - **Guardrail 2 (`@theorem`, `@observable`, `@referee`):** Statically AST-scans return trees, local aliases, and constant-folded arithmetic, banning proof by literal boolean or zero assignment.
   - **Guardrail 3 (`FramedMatrix`, `@observable`):** Blocks illegal single-Dirac left-right SVD overlaps and scrambles every flavor/gauge frame across independent Haar-random unitary transformations $M \mapsto U_L M U_R^\dagger$, asserting `< 1e-12` invariance.
   - **Guardrail 4 (`GatedRGEIntegrator`):** Enforces differential-variable scaling ($\ln\mu$ vs $\ln\mu^2$ vs $\frac{1}{2\pi}\ln\mu$) and cryptographically seals `.integrate_model()` behind an HMAC-SHA256 literature benchmark receipt ($\le 10^{-3}$ relative error).
   - **Guardrail 5 (`LedgerContext`, `TrackedValue`):** Enforces at most **one** dimensionful anchor (e.g., $v_{\mathrm{EW}}$) and requires dimensionless ratios before ledger closure.
   - **Guardrail 6 (`@producer`, `@referee`):** Statically and dynamically forbids `@referee` checks from calling, importing, aliasing, reflecting, or echoing `@producer` functions or cached outputs.
3. **Proven Pure-Mathematics Spine (`CLAIMS_PROVEN.md`):**
   - `origin_axiom_core.analytic_theta`: Holomorphic quarter-nome Jacobi theta functions (`analytic_jtheta`) free of the nome branch cut across all $\tau \in \mathbb{H}$, plus the weight-$-\frac{1}{2}$ weave triplet $(\theta_2^2, \theta_3^2, \theta_4^2)/\eta^3$ (`P-670`).
   - `origin_axiom_core.tick_and_settling`: Non-orientable punctured-torus $\mathrm{Pin}^\pm$ obstruction vanishing via Wu's theorem, projective modular group orders under tick exchange across $N = 2..13$, $G_{96} \to G_{192}$ weave commutant reduction (`2 -> 1`), Stern–Brocot Minkowski `S`-duality $C_{1/y}(s) = C_y(s)$, and punctured-torus $\mathrm{SL}_2(\mathbb{C})$ adjoint trace polynomials (`P-769`, `P-770`, `P-775`).
   - `origin_axiom_core.subweave_r10`: Infinite-$\mathrm{PSL}_2(\mathbb{Z})$ Schreier closure of $\pm\Gamma_1(5)$, Mayer–Selberg subweave transfer operators with old-space pullback embeddings $\Omega_1(kM) \twoheadrightarrow \Omega_1(M)$, and holomorphic fractional-nome Ray–Singer analytic torsion on $X_1(N)$ (`B1881`).
   - `origin_axiom_core.maass_p776`: Exact Two-Tick Bijection $\{F, F'\}^{2k} \xrightarrow{\sim} \{L, R\}^{2k}$ (`P-769`, `B1880`) and literature-gated $\mathrm{SL}_2(\mathbb{Z})$ / $(\Gamma_0(5), \chi_5)$ twin-odd hyperbolic Laplacian cusp-form solver proving the $\mathbb{Q}(\sqrt{5})$ golden-regulator ground state $R_1 = \frac{\pi}{2\ln\varphi}$, its Fricke-circle peak $\tau_{\text{Maass}}^*$, and Class B Kramers doublets (`P-776`, `B1881`).

## Quick Verification (`< 30s`)

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -B -m pytest -v
```
