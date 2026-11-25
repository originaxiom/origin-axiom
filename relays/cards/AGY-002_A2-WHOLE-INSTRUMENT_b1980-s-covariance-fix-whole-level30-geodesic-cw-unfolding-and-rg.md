# Pre-Registration Scope Card: `AGY-002_A2-WHOLE-INSTRUMENT` (`0 of 19`)

**Card ID:** `AGY-002_A2-WHOLE-INSTRUMENT`  
**Seat:** `agy-002` (`origin/agy-002/verify`)  
**Date:** `2026-11-25`  
**Target:** Direct resolution of `origin/main` `B1980` (`d2dd6951c`), `B1981`, `P-882` ("THE WHOLE INSTRUMENT, NOT ONE HOLE"), `P-629`, `P-845`, `SM-C23/C24`, & `chat1` `W-LV1` — plus strict **zero-sculpting forward unfolding** of the whole coupled instrument (`W1`–`W5`).  
**Firewall:** Strictly **`0 of 19`** (zero PDG, NuFIT, Planck, DESI, or CODATA numbers anywhere; zero target-box sculpting!).

---

## 0. Anti-Sculpting Principle & Custody Rules

1. **Forward Unfolding Only (No SM Sculpting):** Modules `W2`, `W3`, and `W4` never search for parameters to match an empirical or structural SM target box. Instead, they start from the geometry's own `SL(2,\mathbb{Z})`-covariant operators, minimize the interactions' own 1-loop effective potential `V_{\text{CW}}`, and run the exact coupled 2-loop RG equations forward from the resulting UV state — reporting honestly whatever spectrum, alignment, hierarchy, EWSB scale, and PMNS mixings unfold naturally.
2. **Standalone Purity:** Pure Python stdlib + `mpmath` + `sympy` ONLY (`0` AST `float`/`complex` literals or casts, `0` `numpy`/`scipy`/`frontier` imports, `0` JSON float tokens, `python3 -I` sandbox-runnable).
3. **Custody:** Pre-commit this Scope Card before writing Producer code; pre-commit Producer script + `SCRIPT_SHA256.txt` before execution; seal unread first-run output + `OUTPUT_SHA256.txt`; then invoke a disjoint Cold-Room Zero-Trust Referee reading ONLY this Scope Card prior to sealing its own unread output.

---

## 1. Exact Mathematical Specifications (`W1`–`W5`)

### Shared Frame C & Weight-`0` Canonical Yukawa Definition (`B1656`/`B1927`/`B1945`/`B1974`/`B1980`)
- Charges `6Y`: `Q = 1, u = -4, d = 2, L = -3, e = 6, \nu^c = 0`; sectors: `up = (Q, u)`, `down = (Q, d)`, `lep = (L, e)`, `nu = (L, \nu^c)`.
- Quaternion basis `Q_I = [[i,0],[0,-i]]`, `Q_J = [[0,1],[-1,0]]`, `Q_K = Q_I Q_J`, `\varepsilon = Q_J`, blocks `B = [Q_J, Q_I, Q_K]`, exact `G^{-1}` dual basis `EDUAL` (`B1656`).
- Branch-cut-free holomorphic modular triplet (`B1974`, weight `+3/2`):
  `c_0 = -\theta_2^2(\theta_3^4 + \theta_4^4)/(24\eta^3)`, `c_1 = \theta_4^2(\theta_2^4 + \theta_3^4)/(24\eta^3)`, `c_2 = i\theta_3^2(\theta_2^4 - \theta_4^4)/(24\eta^3)`, `S(\tau) = c_0 Q_I + c_1 Q_J + c_2 Q_K`.
- Channel factor `R_s(\tau, w) = \kappa_s \theta_{c_s}(0,\tau)\theta_{d_s}(0,\tau)/(2\pi\eta(\tau)^3)` (weight `-1/2`), Fuchsian canonical end `L_2(\tau)` satisfying `L_2(\gamma\tau) = L_2(\tau) + \ln|c\tau + d|` (weight `0` for `2\pi L_2 + c_s`), so `Y_f(\tau, w)` has exact modular weight `+1` (`|Y_f(\gamma\tau, w\gamma^{-1})| = |c\tau + d| |Y_f(\tau, w)|`).
- **Canonical weight-`0` Yukawa:** `Y_f^{\text{inv}}(\tau, w) := (\operatorname{Im}\tau)^{1/2} Y_f(\tau, w)`.
- **General Higgs Yukawa operator `Y_f(h; \tau, w)`:** For unit `h = (h_0, h_1, h_2) \in S^5 \subset \mathbb{C}^3`, let `S_{\text{unit}}(h) = \|c(\tau)\|_2 (h_0 Q_I + h_1 Q_J + h_2 Q_K)` and `\tilde{S}_{\text{unit}}(h) = \varepsilon S_{\text{unit}}(h)^* \varepsilon^T`, scaled by `(\operatorname{Im}\tau)^{1/2}` so that at `h = \hat{c}(\tau) = c(\tau)/\|c(\tau)\|_2`, `Y_f(\hat{c}(\tau); \tau, w) \equiv Y_f^{\text{inv}}(\tau, w)` identically.

### Module `W1` — Surgical `B1980` Part A/B Audit & `P-882 Q1` Resolution
1. **Part A (Exact Algebra in `\mathrm{PSL}(2, \mathbb{Z}/30)`):** Verify independently that `M = [[2,1],[1,1]]` has order `60` in `\mathrm{PSL}(2,\mathbb{Z}/30)`, trace cycle mod `30` `(3,7,18,17,3,22,3,17,18,7,3,2)` avoids `0, \pm 1` (`0` elliptic elements in `M^k \Gamma(30)`), `X(30)` has `288` cusps splitting into `4` orbits of `12` + `4` orbits of `60`, and the `48` cusps fixed by `M^{12}` equal `P_{30}/\{\pm 1\}` (`96` points) identically.
2. **Part B (`B1980` `S`-Move Exact Fix & `P-882 Q1` Closure):** On `B1980`'s exact three axis pairs `(y, 1/y) \in \{(5/4, 4/5), (3/2, 2/3), (5/2, 2/5)\}` across ALL `96` points of `P_{30}` using `B1980`'s exact `9`-log distance `d(u, v) = \max_k |u_k - v_k|/\max(1, |u_k|)` (`6` mass log ratios + `3` CKM logs `|V_{12}|, |V_{23}|, |V_{13}|`):
   - Solve direct Fuchsian ODE for both `L_2(iy)` and `L_2(i/y)`, verifying `|L_2(i/y) - (L_2(iy) + \ln y)| < 10^{-8}`.
   - Evaluate Frame C (`dps = 55`) with the true cocycle `L_2(i/y) = L_2(iy) + \ln y` and exact bijection `w' = w S^{-1}`: verify max `9`-log distance `< 10^{-38}` across all `96/96` points at all `3` pairs (proving **ZERO** `S`-breaker in `F_u`, `a_0`, `(a, 2b)`, or Higgs normalization!).
   - **Full-Norm Modular Weight `+1` Proof:** Verify that ALL `9` **absolute** canonical singular values `s_k^{\text{inv}}(\tau, w) = (\operatorname{Im}\tau)^{1/2} s_k(Y_f(\tau, w))` (`u, d, e`) are invariant under `T`, `S`, and `M` at `\tau_1 = 13/100 + 6/5 i` and `\tau_0 = -9/10 + 6/5 i` (`w = (4/15, 1/30)`) to `< 10^{-38}`.
   - **Corrected `K \neq 1` Duality Audit:** Re-test `K \in \{2, 3, 5, 6, 10, 15, 30\}` at `y = \frac{3}{2}\sqrt{K}, y' = \frac{2}{3}\sqrt{K}` using exact non-clamped, `\ln`-cocycle-correct Fuchsian `L_2` on both sides, matching the `12` exact class representatives of `P_{30}` against all `899` nonzero points of `E[30]` (`451` antipodal representatives) under `B1980`'s `9`-log distance metric.

### Module `W2` — Whole Level-30 Instrument (`576` Points / `288` Pairs) & Closed Geodesic `\gamma_M(t)` Reading
1. **Whole `E[30]_{\text{prim}}` (`288` `\pm`-pairs = `576` points = `100%` of `X(30)` cusps, addressing `SM-C24`):**
   - Run exact symbolic tropical rate classification (`10` rates per point) across all `288` pairs, reporting exact class count, alignment/hierarchy counts, exact channel-zero count, `0 < e(V_{23}) < 1/10` count, and asymptotic standard Wolfenstein count — partitioned into the `48` `M^{12}`-fixed act-line pairs vs `240` off-line pairs.
   - Evaluate Frame C numerically (`dps = 38`, exact Fuchsian `L_2`) at finite physical heights `y = 2` and `y = 3` (`x = 13/100`) across all `288` pairs, counting aligned (`\min|V_{kk}| \ge 9/10`), hierarchical (`u, d` `m_2/m_3 < 1/5`), `e \neq d` split (`|\ln D_2| > 1/10`), and **standard CKM ordering `|V_{12}| > |V_{23}| > |V_{13}|`**, split by act-line (`48`) vs off-line (`240`).
2. **Closed Hyperbolic Geodesic `\gamma_M(u)` of `M = [[2,1],[1,1]]` (Zero Free `y`!):**
   - Exact unit-speed geodesic `\tau(u) = \frac{1}{2} + \frac{\sqrt{5}}{2}(\tanh u + i\,\operatorname{sech} u)`, period `\ell_M = 4\ln\varphi = 2\ln\frac{3+\sqrt{5}}{2}`, satisfying `M(\tau(u)) = \tau(u + \ell_M)` identically (`< 10^{-40}`).
   - Using `16`-node periodic midpoint quadrature on `u \in [-2\ln\varphi, +2\ln\varphi]` (mapping each `\tau(u)` to `\mathcal{F}` for exact Fuchsian `L_2` + exact `\ln|c\tau+d|` cocycle), compute for both a representative MARK orbit (`(4/15, 1/30)`) and TWIN orbit (`(1/30, 1/6)`):
     (a) Exact `SL(2,\mathbb{Z})`-invariant geodesic-averaged canonical observable spectrum (`\langle s_k^{\text{inv}}, m_2/m_3, m_1/m_3, |V_{ij}|, |J_{\text{CP}}| \rangle_{\gamma_M}`), verifying `M`-basepoint shift invariance (`u \mapsto u + \delta`) to `< 10^{-8}`;
     (b) Geodesic-integrated Hermitian Gramian `\mathcal{H}_{L,f}^{(\gamma_M, O)} = \frac{1}{12\ell_M}\int_{-2\ln\varphi}^{+2\ln\varphi}\sum_{w \in O} Y_f^{\text{inv}} Y_f^{\text{inv}\dagger}\,du` and single-point coherent geodesic integral `\bar{Y}_f^{(\gamma_M, w)} = \frac{1}{\ell_M}\int_{-2\ln\varphi}^{+2\ln\varphi} Y_f^{\text{inv}}(\tau(u), w)\,du` — listening honestly to whether geodesic integration preserves or washes out `m_2/m_3` and CKM!
3. **`B1981` & `chat1` `W-LV1` Direct Cross-Check:** Verify `Y_e(w) \propto Y_d(3w)` (`< 10^{-40}`) at `N = 10` and `N = 30`, and confirm `B1981`'s `E[6]_{\text{prim}}` shell `L` (unweighted `\sum Y`) vs `G` (`\sum Y Y^\dagger`) wash-out at `y = 2, 3` and `y = 20 \to 30` (`dps = 110`).

### Module `W3` — Natural Unfolding (I): Un-Sculpted `V_{\text{CW}}(h_u, h_d)` & Modular `V_{\text{CW}}(\tau)` (`P-629`, `P-879`, `P-882 Q3`)
1. **Dynamical Higgs Direction Selection (`V_{\text{CW}}` on `S^5` & `S^5 \times S^5`, Zero Target Filters):**
   - Define the scale-free quartic trace core `V_4 = -\sum_{f \in \{u,d,e\}} N_{c,f}\operatorname{Tr}[(Y_f^\dagger Y_f)^2]` (`N_c = 3, 3, 1`) and full 1-loop `\overline{\text{MS}}` fermion potential `V_{\text{CW}} = -\frac{1}{64\pi^2}\sum_f N_{c,f}\operatorname{Tr}[(Y_f^\dagger Y_f)^2(\ln(Y_f^\dagger Y_f/\mu^2) - 3/2)]` with canonical trace scale `\mu^2 = \frac{1}{3}\sum_f \operatorname{Tr}(Y_f^{\text{inv}\dagger} Y_f^{\text{inv}})`.
   - At `\tau_{\text{apex}} = \frac{1}{2} + i\frac{\sqrt{5}}{2}` and `\tau_2 = 13/100 + 2i` (`w_{\text{mark}} = (4/15, 1/30)` & `w_{\text{twin}} = (1/30, 1/6)`):
     - **1-doublet conjugated (`h \in S^5`, `H_u = S_{\text{unit}}(h), H_d = \tilde{S}_{\text{unit}}(h)`):** Minimize `V_{\text{CW}}` and `V_4` from `8` deterministic multi-starts on `S^5`; record `h^*`, `r(h^*) = |h^{*T} h^*|`, `|\hat{c}(\tau)^\dagger h^*|`, mass ratios, CKM, `|J_{\text{CP}}|`, and verify `M2–M3` compliance.
     - **2-doublet `all-S` (`(h_u, h_d) \in S^5 \times S^5`):** Minimize `V_{\text{CW}}(h_u, h_d) + \lambda_3 V_0 |h_u^\dagger h_d|^2` for `\lambda_3 \in \{-1, -1/4, 0, +1/4, +1\}` (`V_0 = |V_{\text{CW}}(\hat{c}, \hat{c})|`) from `8` multi-starts; record `(h_u^*, h_d^*)`, `|h_u^{*\dagger} h_d^*|`, `r_u, r_d`, overlap with `\hat{c}(\tau)`, mass ratios, CKM ordering, and `|J_{\text{CP}}|`.
2. **Modular Effective Potential `V_{\text{CW}}(\tau)` Across `\mathcal{F}` (Does the Frame's Own Loop Fix `y`?):**
   - Derive exact symbolic cusp exponent `e_{\text{norm}}(w)` of `\|Y_f^{\text{inv}}(\tau, w)\|_F` across all `288` pairs of `E[30]_{\text{prim}}` (proving exact sign: negative = cusp growth / fermion-loop runaway, positive = cusp decay / finite-`y` minimum!).
   - Verify exact `SL(2,\mathbb{Z})` invariance of the full-level potential `V_{\text{CW}}^{(\text{all-288})}(\tau) = \sum_{w \in E[30]_{\text{prim}}/\pm} V_{\text{CW}}(\tau, w)` (and `V_4^{(\text{all-288})}(\tau)`) under `T` and `S` at `\tau = 1/4 + 6/5 i` to `< 10^{-30}`.
   - Evaluate `V_{\text{CW}}^{(\text{all-288})}(\tau)`, `V_4^{(\text{all-288})}(\tau)`, and MARK/TWIN single-point potentials across `y \in \{1, 5/4, 3/2, 2, 5/2, 3, 4, 5, 6, 8\}` (`x = 0` and `x = 1/2`, exact non-clamped Fuchsian `L_2`), checking for finite-`y` stationary points vs cusp runaway (and comparing growth exponent against `E_3(\tau)` Casimir energy `A2-OW9`).

### Module `W4` — Natural Unfolding (II): Curved Dirac `s=1/2` Metric + Coupled 2-Loop `2HDM-II` RG + Canonical Neutrinos
1. **Guardrail 4 Literature Benchmark Gate:** Verify `15/15` Chowdhury–Eberhardt `arXiv:1503.08216` Type-II 2HDM `1\times 1` coefficients (`< 10^{-40}`), Arason/Buttazzo `1HDM` `(-12, -11/4, -1/4)` (`0`), and opposite `1HDM` vs `2HDM-II` Xing–Zhou `|V_{cb}|` running direction.
2. **Curved Spin-`1/2` Dirac Kähler Metric `G_{s=1/2}(\tau)`:** Compute `G_{s=1/2}` directly from the polar Fuchsian developing map `e^{+\varphi}` on `E_\tau \setminus \{0\}` at `\tau_{\text{apex}} = \frac{1}{2} + i\frac{\sqrt{5}}{2}` and `\tau_2 = 13/100 + 2i` (verifying Gauss–Bonnet `|\text{Area}/(2\pi) - 1| < 10^{-3}`).
3. **Un-Sculpted Coupled 2-Loop `2HDM-II` RG Unfolding (`t = 0 \to -35`):** Evolve downward from natural conformal UV initial conditions (`g_1 = g_2 = g_3 = 1/2`, chosen so `1/g_3^2(0) = 4 > (14/16\pi^2)\cdot 35 \approx 3.10` stays above the `b_3 = -7` confinement pole across all `35` `e`-folds; `\lambda_1 = \lambda_2 = \lambda_3 = \lambda_4 = 0`, Yukawas scaled so `\max_f \sigma_3(Y_f) = 1`, zero tuning!) for three un-sculpted UV states:
   - `(U_A)` Frame C at `\tau_2 = 13/100 + 2i`, `w_{\text{mark}} = (4/15, 1/30)` (FLAT and CURVED `G_{s=1/2}`);
   - `(U_B)` Dynamically minimized `W3` vacuum `(h_u^*, h_d^*)` at `\tau_2` (`\lambda_3 = 0`, FLAT and CURVED `G_{s=1/2}`);
   - `(U_C)` Geodesic apex `\tau_{\text{apex}} = \frac{1}{2} + i\frac{\sqrt{5}}{2}`, `w_{\text{mark}}` (zero free `y`, FLAT and CURVED `G_{s=1/2}`).
   Report exact IR ratios (`y_t/g_3`, `m_b/m_\tau`, `m_s/m_\mu`, `u/d/e` hierarchies, CKM ordering, `|J_{\text{CP}}|`), spontaneous radiative EWSB crossover scale `t_{\text{EWSB}}` (`\lambda_1` or `\lambda_2` zero crossing), and step-halving convergence (`80` vs `160` steps `< 10^{-6}`).
4. **Un-Sculpted Canonical Neutrinos & Guardrail 3 Haar Check:** Evaluate canonical Frame C `Y_\nu` (`q_L = -3, q_{\nu^c} = 0`, zero texture scan!) + canonical Weinberg operator `\kappa_\nu = Y_\nu^T Y_\nu` (`M_R = I_3`, FLAT and CURVED `G_{s=1/2}`), compute Autonne–Takagi PMNS `U_{\text{PMNS}} = U_e^\dagger U_\nu` (verifying `10`-trial Haar `U(3)^3`/`U(3)^5` invariance `< 10^{-25}` across curved Kähler + 2-loop RG + Takagi PMNS!), and report all angles & mass-squared ratio honestly.

---

## 2. Pre-Committed Expectations (With Honest Priors) & Blind Gates (`G1`–`G6`, `PF1`–`PF6`)

| ID | Pre-Committed Expectation | Prior |
|---|---|---:|
| `E1` | Restoring `L_2(i/y) = L_2(iy) + \ln y` drops `B1980`'s `(0.12, 0.18, 0.32)` `S`-move errors to `< 10^{-38}` across all `96/96` points, while weight-`0` `s_k^{\text{inv}} = \sqrt{y} s_k` is `T, S, M`-invariant to `< 10^{-38}`; dropping `+\ln y` reproduces `B1980`'s `(0.12, 0.18, 0.32)` | `0.98` |
| `E2` | Corrected `K \neq 1` duality test (`K \in \{2,3,5,6,10,15,30\}`) with true non-clamped Fuchsian `L_2` still finds NO duality (`\min_K d > 0.1`) | `0.90` |
| `E3` | Across all `288` primitive order-30 pairs (`E[30]_{\text{prim}}`), there are `> 12` asymptotic classes (`SM-C24 E3`), `0/288` have standard additive Wolfenstein ordering at `y \to \infty`, while a substantial fraction have standard ordering at finite `y = 2..3` | `0.80` |
| `E4` | Geodesic-integrated Hermitian Gramian along `\gamma_M` washes out `m_2/m_3` (similar to `O4`), whereas pointwise geodesic averages keep non-trivial finite-height hierarchy with basepoint invariance `< 10^{-8}` | `0.75` |
| `E5` | Fermion-loop `V_{\text{CW}}(h)` Schur-convexity spontaneously drives `h^*` toward high hierarchy (`r \to 0` or near-singular) rather than degenerate `r = 1`; for 1 doublet it obeys `M2–M3` strictly | `0.85` |
| `E6` | On `E[30]_{\text{prim}}`, `V_{\text{CW}}^{(\text{all-288})}(\tau)` is strictly `SL(2,\mathbb{Z})`-invariant (`< 10^{-30}`), and because `e_{\text{norm}} < 0` on cusp-dominant points, pure fermion `V_{\text{CW}}(\tau)` runs away to `-\infty` as `y \to \infty` (proving bosonic/racetrack balancing is needed to fix `y`) | `0.80` |
| `E7` | Un-sculpted 2-loop `2HDM-II` RG unfolding from `\tau_2` and `\tau_{\text{apex}}` triggers spontaneous radiative EWSB (first `\lambda_1` or `\lambda_2` crossing zero) while preserving standard CKM ordering where present at UV (`y=2`) | `0.70` |
| `E8` | Un-sculpted canonical `Y_\nu^T Y_\nu` (`M_R = I_3`) produces a clean deterministic PMNS spectrum without tuning (likely differing from flat-ansatz expectations, recorded honestly without filtering) | `0.85` |

### Blind Gates (`G1`–`G6`) & Planted Negative Controls (`PF1`–`PF6`)
- **`G1`:** `B1980` Part A exact algebra PASS; `S`-covariance `< 10^{-38}` on `96/96` points at all `3` pairs; full-norm `s_k^{\text{inv}}` invariance `< 10^{-38}` under `T, S, M`; corrected `K \neq 1` audit completed.
- **`G2`:** All `288/288` pairs (`576` pts) classified symbolically & numerically at `y=2, 3`; geodesic `M(\tau(u)) = \tau(u+\ell_M)` `< 10^{-40}` & basepoint invariance `< 10^{-8}`; `Y_e(w) \propto Y_d(3w)` `< 10^{-40}` & `B1981` confirmed.
- **`G3`:** `V_{\text{CW}}` multi-start optimizations converged, `100%` of 1-doublet minima obey `M2–M3`, `V_{\text{CW}}^{(\text{all-288})}(\tau)` `T, S`-invariant `< 10^{-30}`, exact `288/288` norm-exponent cusp theorem proved.
- **`G4`:** Guardrail 4 benchmarks PASS (`15/15` `< 10^{-40}`, `1HDM` `0`, opposite `|V_{cb}|` sign); polar Gauss–Bonnet `< 10^{-3}`; 2-loop RK4 step-halving (`80` vs `160`) `< 10^{-6}`; `10`-trial Haar `U(3)^3`/`U(3)^5` `< 10^{-25}`.
- **`G5`:** `6/6` planted controls caught: `PF1` (drop `+\ln y` reproduces `B1980` `(0.12, 0.18, 0.32)`), `PF2` (drop `\sqrt{y}` breaks absolute `s_k` invariance by `|c\tau+d|`), `PF3` (flip `V_{\text{CW}} \to -V_{\text{CW}}` destroys hierarchy), `PF4` (wrong action `w\gamma` breaks `S/M`), `PF5` (drop `Y_u` from 2HDM RG breaks benchmark & EWSB), `PF6` (non-unitary basis rotation breaks Haar invariance).
- **`G6`:** `0` AST float/complex literals or casts, `0` numpy/scipy/frontier imports, `0` JSON floats, strictly `0 of 19`.

---

## 3. Dated Pre-`v5` Erratum & Addendum (`2026-11-25`, Disclosing Frozen `v1`–`v4`)

Frozen runs `v1` (`38b820bf0`), `v2` (`7a192f8b6`), `v3` (`aceac1cb7`, all pre-output), and `v4` (`a2221c7ec -> a510dc8c6`, `G1, G3, G6 PASS`, `5/6 PF`, `0` JSON floats) are preserved untouched. Four predicate/convention clarifications plus one discovery-driven extension are registered prior to running Authoritative Producer `v5`:
1. **`PF4` (`W1`):** Since `S^{-1} = -S` and Frame C is antipodally invariant (`Y(-w) \equiv Y(w)`), wrong point action `w\gamma` vs `w\gamma^{-1}` is tested on `T` and `M` (`1.637` and `0.335` in `v4`).
2. **`W2` (`W-LV1` & Geodesic Basepoint):** `chat1` `W-LV1` states `Y_e(w) \propto Y_d^{\text{neg-}q_Q}(3w)` (with doublet charge `q_Q` negated: `(-1, +2)` at `3w`, verified `< 10^{-40}`), whereas un-negated `Y_d(+1, +2)(3w)` splits by `3.85%` via `F_u(a_+)` vs `F_u(a_-)` — `v5` reports both. On `\gamma_M`, smooth `SL(2,\mathbb{Z})`-invariant trace integrals `\langle \operatorname{Tr}(Y^\dagger Y)\rangle_{\gamma_M}` and `\langle \operatorname{Tr}[(Y^\dagger Y)^2]\rangle_{\gamma_M}` verify basepoint invariance to `< 10^{-8}` (`16` nodes), alongside the `16`-node CKM observable average.
3. **`W4` (Xing–Zhou Downward Running Sign):** In `dt < 0` downward running, `1HDM` decreases `|V_{cb}|` (`dvcb_1h_down < 0`) while `Type-II 2HDM` increases `|V_{cb}|` (`dvcb_2h_down > 0`; `v4` already produced `-4.60e-5` vs `+1.65e-5` with an inverted boolean test).
4. **`W3`/`W4` (`V_4` vs `V_{\text{CW}}` Convexity Dichotomy):** `v4` discovered that at `\mu^2 = \frac{1}{3}\sum\operatorname{Tr}(Y^\dagger Y)`, `\ln(\lambda/\mu^2) - 3/2 < 0` flips the 1-loop potential convex (favoring degeneracy `r \approx 0.68`), whereas the Schur-convex quartic core `V_4 = -\sum N_c\operatorname{Tr}[(Y^\dagger Y)^2]` (equivalent to `\mu < e^{-3/4} m_f`) snaps 1-doublet `h^*` onto Frame C's exact modular triplet `S(\tau)` (`|\hat{c}^\dagger h^*| = 0.9855`, `r = 0.025`, `d_m2m3 = 0.0073`). `v5` therefore also runs `two_doublet_allS` (`\lambda_3 \in \{-1, -1/4, 0, +1/4, +1\}`) on `V_4` and propagates its `\lambda_3 = -1/4` dynamic vacuum (`UD_W3_DynamicV4_y2`) through `W4`'s curved `G_{s=1/2}` + 2-loop RG unfolding.

0 of 19.
