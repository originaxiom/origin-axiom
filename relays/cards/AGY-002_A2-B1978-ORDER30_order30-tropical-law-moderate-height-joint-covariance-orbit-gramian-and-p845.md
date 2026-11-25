# Pre-Registration Scope Card — `AGY-002_A2-B1978-ORDER30` (`0 of 19`)

**Seat:** `agy-002` (`origin/agy-002/verify`)  
**Target:** `origin/main @ 88a1e9474` (`B1976`, `B1977`, `B1978`, `88a1e9474` Dated Caveat citing `agy-002`'s `M34`, `P-845`, `P-860 (d)`) & cross-seat synthesis with `origin/chat1/web-seat @ 220e3d9ec` (`CHK-1`) and `origin/agy/self-consistent-loop-2026-11-11 @ 0c8debf48` (`E_\tau[6]_{\mathrm{prim}}`).  
**Kind:** Pre-committed standalone pure-`mpmath` + `sympy` derivation, exact tropical theorem, moderate-height & joint-covariance audit, `12`-point `M`-orbit Gramian evaluation, and `P-845` group-theoretic lens census.  
**Firewall:** Strictly **`0 of 19`** — zero empirical, PDG, NuFIT, Planck, DESI, or CODATA numbers appear anywhere in this card, script, or output. Every quantity is a pure dimensionless mathematical output or exact rational exponent of Frame C.  
**Custody Discipline (`docs/seats/README.md` § `12` & Guardrails 1–6):**
1. This Scope Card is committed **before** any Producer execution.
2. Standalone Producer `relays/a2_b1978_order30/verify_a2_b1978_order30.py` uses **only** Python stdlib, `mpmath`, and `sympy` (`0` float/complex AST literals or casts, `0` `numpy`/`scipy`/`frontier/` imports, `0` JSON float tokens), hashed into `SCRIPT_SHA256.txt` and committed **before** execution.
3. Producer executes **once** (`computed once`), sealing its unread output JSON and `OUTPUT_SHA256.txt` before analysis.
4. A disjoint zero-shared-code **Cold-Room Zero-Trust Referee** subagent independently reconstructs all five modules (`O1`–`O5`), planted controls, and Haar invariance from this Scope Card alone.

---

## 1. Exact Mathematical Objects (Frame C, All-`S` Two-Doublet Reading)

- **Torsion set `P_{30}` (`B1976`):** `K_5^* = \{ (k/5, 2k/5) \bmod 1 : k \in \{1, 2, 3, 4\} \}` (`4` primitive points on `B1943`'s act line `LR`), `E[6]_{\mathrm{prim}} = \{ (i/6, j/6) : \operatorname{ord} = 6 \}` (`24` points), and `P_{30} = K_5^* + E[6]_{\mathrm{prim}} \bmod 1` (`96` points of exact order `30`).
- **Act monodromy (`B1943`, `B1978`, `88a1e9474`):** `M = LR = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix} \in \mathrm{SL}(2, \mathbb{Z})`. Because `M = M^T`, `M w` and `w M^{-1}` generate the exact same `8` orbits of size `12` on `P_{30}` (traversed in opposite directions).
- **Frame C Coupling (`B1656`, `B1736`, `B1940`, `B1974`):**
  - Charges `6Y`: `Q = 1, u = -4, d = 2, L = -3, e = 6` (`up = (Q, u)`, `down = (Q, d)`, `lep = (L, e)`).
  - Unique holomorphic Higgs triplet (`B1974` Halphen–Serre identity):
    $$c_0 = \frac{-\theta_2^2(\theta_3^4 + \theta_4^4)}{24\eta^3},\qquad c_1 = \frac{\theta_4^2(\theta_2^4 + \theta_3^4)}{24\eta^3},\qquad c_2 = \frac{i\,\theta_3^2(\theta_2^4 - \theta_4^4)}{24\eta^3},\qquad S(\tau) = c_0 Q_I + c_1 Q_J + c_2 Q_K.$$
  - Channel matrix `M_w(\tau; a, b; q_L, q_R)` built from exact theta residues `R_s`, exact `B1940` digamma `F_u`, exact Jacobi `a_0 = 2\pi i\alpha + \theta_1'(z)/\theta_1(z)`, and exact first-principles Weierstrass Fuchsian canonical end `L_2(\tau)` (also comparing against `B1927`'s `y = 6` clamped `L_2` at high `y = 20, 30, 40`).
  - Coupling `Y_f(\tau, w)_{ab} = \sum_{m, n} (C_a^T \varepsilon S C_b)_{mn} (M_w)_{mn}` with `(C_0, C_1, C_2) = (Q_J, Q_I, Q_K)`, `\varepsilon = Q_J`, and all three sectors reading `S` (`B1970`, `B1976`, `B1977`).
  - Ascending left singular basis `U_f = [u_{1,f}, u_{2,f}, u_{3,f}]` (`m_1 \le m_2 \le m_3`), unitary CKM `V = U_u^\dagger U_d`, and Jarlskog invariant `J_{\text{CP}} = \operatorname{Im}(V_{01} V_{12} \overline{V_{02}} \overline{V_{11}})`.

---

## 2. Five Pre-Committed Verification Modules (`O1`–`O5`) & Explicit Falsifiers (`G1`–`G6`)

### `G1` (`O1`) — Exact Closed-Form Tropical Theorem for the `1/60` Grid, `e(V_{23}) = 2|\operatorname{nd}(a) - 1/4|`, CKM Ordering Classification, & General-Level `N` Anti-Sharpshooting
- **Pre-Committed Expectations:**
  1. **Exact `12`-Value `\operatorname{nd}(a)` Collapse:** Across all `96` points of `P_{30}`, `\operatorname{nd}(a) = \min(a \bmod 1, 1 - (a \bmod 1))` takes exactly **`12`** values `{k/30 : k \in {1,2,3,4,6,7,8,9,11,12,13,14}}` (`0` exact `is_zero` channel cancellations across all `96 \times 3 \times 4` channels). Consequently, the true `y \to \infty` asymptotic mass and mixing rates depend solely on `\operatorname{nd}(a)` and fall into at most **`12`** exact rational rate classes (any extra classes in `B1977`'s `17` at `y = 20..30` arise from finite-`y` `b`-phase drift / `round(..., 2)` splitting).
  2. **Exact `1/60` Lattice & `1/30` `V_{23}` Law:** From exact `SymPy`/`Fraction` tropical min-plus polynomials for `Y_f` and `3 \times 3` Gramian perturbation in the `(e_+, e_1, e_-)` left basis, every one of the `96 \times 9 = 864` exact asymptotic rates in `\varepsilon = e^{-\pi y}` units is an exact rational multiple of **`1/60`**, and **`e(V_{23}) = 2|\operatorname{nd}(a) - 1/4|`** holds identically across all `96/96` points — matching 60-dps numerical Frame C rates between `y = 30` and `y = 40` (`x = 13/100`) to `< 2 \times 10^{-3}` on all `864/864` rates!
  3. **Exact `B1976` `E3`/`E4` Sub-Lattices:** `E3` (`e = d` tie) persists on exactly the **`8`** points with `a \in \{1/5, 2/5, 3/5, 4/5\}` (`a_6 = 0`); `E4` (`|u["1"]|/mx < 10^{-10}` at `y = 30`) occurs on the **`4`** points with `a \in \{2/5, 3/5\}`.
  4. **Structural CKM Ordering Census (Not Prejudged):** Classify all `12` exact `\operatorname{nd}(a)` classes (`96` points) into:
     - `W-STD`: `0 < e(V_{12}) < e(V_{23}) < e(V_{13}) = e(V_{12}) + e(V_{23})` (standard additive Wolfenstein ordering),
     - `W-INV`: `0 < e(V_{23}) < e(V_{12}) < e(V_{13}) = e(V_{12}) + e(V_{23})` (inverted `2-3` vs `1-2` ordering),
     - `W-NONADD`: `e(V_{13}) \neq e(V_{12}) + e(V_{23})` (also recording `e(V_{31})` alongside `e(V_{13})`).
  5. **General-Level `N` Anti-Sharpshooting Law (`B1976` Open #1 & Guardrail 1):** Across `N = 5k` (`k = 1..12`: `5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60`) on `K_5^* + E[k]_{\mathrm{prim}}` plus `N = 6, 12`, verify the exact closed-form minimal `V_{23}` exponent law:
     $$e_{\min}(V_{23}; N) = \begin{cases} 0 & (4 \mid N), \\ 1/N & (N \equiv 2 \pmod 4), \\ 1/(2N) & (N \text{ odd}), \end{cases}$$
     and record which levels `N` simultaneously admit aligned mixing, both quark hierarchies, 2nd-gen `e \neq d` splitting, and slow mixing `e_{\min} < 1/10` (testing specifically whether `N = 20` or `N = 10` already achieves viability!).
- **Falsifier:** Any discrepancy `> 2 \times 10^{-3}` between exact closed-form tropical rates and `y = 30 \to 40` 60-dps Frame C rates across the `864` entries, or any failure of `e(V_{23}) = 2|\operatorname{nd}(a) - 1/4|` on `P_{30}`.

### `G2` (`O2`) — Moderate-Height Survival (`y = 1..40`), `L_2(y)` vs. Clamped `L_2(6)`, Column Sensitivity, & Finite-`y` `O(1)` Prefactors (`Fracture 1`)
- **Measurement Protocol (Not Prejudged on Moderate-`y` Survival):**
  1. Solve exact Fuchsian Weierstrass `L_2(x + i y)` (trace residual `< 10^{-11}`) at `x = 13/100` for `14` heights `y \in \{1, 3/2, 2, 5/2, 3, 4, 5, 6, 8, 10, 15, 20, 30, 40\}` and across `3` extra columns `x \in \{0, 31/100, 1/2\}` at `y \in \{2, 4, 10, 20\}`. Verify `L_2(\tau + 1) = L_2(\tau)` to `< 10^{-11}` and quantify `L_2(y) - L_2(6)` for `y \in \{10, 20, 30, 40\}` and its exact effect on `O(1)` prefactors vs. `1/60` rates.
  2. Evaluate all `12` `\operatorname{nd}(a)` representatives (plus all `5` `B1976` slow points) at all `14` heights and all `96` points at `y \in \{2, 3, 5, 10, 20, 30, 40\}`.
  3. Record without prejudgement: (a) survival counts of alignment (`min diag >= 9/10`), both hierarchies (`m_2/m_3 < 1/2, m_1/m_3 < 1/10`), 2nd-gen `e \neq d` split (`|\ln((m_\mu/m_\tau)/(m_s/m_b))| > 1/10`), and CKM ordering (`|V_{12}|` vs `|V_{23}|` vs `|V_{13}|`) at every moderate height `y = 1..10`; (b) asymptotic `O(1)` prefactors `C_k(x, y) = \operatorname{obs}_k \cdot \varepsilon^{-e_k}` and effective local rates across `(2,3), (3,5), (5,8), (8,10), (20,30), (30,40)`; (c) column spread across `x \in \{0, 13/100, 31/100, 1/2\}`.
- **Falsifier:** Any Fuchsian ODE trace residual `> 10^{-10}`, any `L_2(\tau + 1)` mismatch `> 10^{-10}`, or failure to reproduce `B1977` / `chat1` `y = 20 \to 30` and `y = 30 \to 40` summaries (`G1–G5`).

### `G3` (`O3`) — Exact Joint `SL(2, \mathbb{Z})` & Monodromy `M = [[2,1],[1,1]]` Covariance at Order `30` (`88a1e9474` Caveat)
- **Pre-Committed Expectations:**
  1. Direct Fuchsian ODE verification of `L_2(\gamma\tau) = L_2(\tau) + \ln|c\tau + d|` at `\tau_0 = -9/10 + 6/5 i` (`\operatorname{Im}(T\tau_0) = 6/5`, `\operatorname{Im}(S\tau_0) = 8/15`, `\operatorname{Im}(M\tau_0) = 24/29`) for all three `\gamma \in \{T, S_{\text{mod}}, M\}` to `< 10^{-10}`.
  2. Pointwise joint covariance test of ALL `9` physical observables (`u, d, e` mass ratios, `|V_{\text{CKM}}|`, `|J_{\text{CP}}|`) on order-30 points under `(\tau, w) \mapsto (\gamma\tau, w\gamma^{-1})` with exact `L_2(\gamma\tau) = L_2(\tau) + \ln|c\tau + d|` at both `\tau_0 = -9/10 + 6/5 i` and `\tau_1 = 13/100 + 2 i`:
     - Under `T`: exact pointwise invariance `< 10^{-30}` (`B1940` extended to order `30`).
     - Under `S_{\text{mod}}` and `M = LR`: measure exact pointwise invariance or exact residual (testing both whether `S(\gamma\tau)`'s `S_3` triplet rotation cancels in `|Y_f|` and `|V_{\text{CKM}}|` AND contrasting directly against holding `L_2` fixed [`PF3`] and holding `\tau` fixed [`B1978`'s caveat]).
- **Falsifier:** Failure of direct Fuchsian `L_2(\gamma\tau) = L_2(\tau) + \ln|c\tau + d|` beyond `10^{-10}` or failure of joint `T`-invariance beyond `10^{-30}`.

### `G4` (`O4`) — Exact `8`-Orbit Algebraic Classification (`B1978` Open #2) & `12`-Point `M`-Orbit Gramian `\mathcal{H}_{L,f}^{(O)}(\tau)` vs. Coherent Sum (`B1978` Open #1)
- **Pre-Committed Expectations:**
  1. **Exact Mark–Twin Orbit Dichotomy (`B1978` Open #2):** Pure exact arithmetic proves `P_{30} = K_5^* \times E[2]_{\mathrm{prim}} \times E[3]_{\mathrm{prim}}` decomposes under `M = [[2,1],[1,1]]` into `8` orbits of size `12` (`\operatorname{ord}_5 = 2, \operatorname{ord}_2 = 3, \operatorname{ord}_3 = 4`), where:
     - All `4` MARK orbits (`w_5 \in \{\pm(2/5, 4/5)\}`) carry slow `V_{23} = 1/30` points — `6` slow points on `E[3]` Orbit `A` (`a_3 \neq 0` on `4/4`) and `3` slow points on `E[3]` Orbit `B` (`a_3 = 0` on `2/4`), reproducing `B1978`'s exact `[6, 6, 3, 3]` multiplicities.
     - All `4` TWIN orbits (`w_5 \in \{\pm(1/5, 2/5)\}`) carry **`0`** slow points (`[0, 0, 0, 0]`).
  2. **Orbit-Gramian Evaluation (`B1978` Open #1 — Not Prejudged on Survival vs. Wash-Out):** For all `8` orbits `O_1, \dots, O_8`, evaluate our `M34` exact Hermitian Gramian `\mathcal{H}_{L,f}^{(O)}(\tau) = \frac{1}{12} \sum_{w \in O} Y_f(\tau, w) Y_f(\tau, w)^\dagger` and coherent sum `\bar{Y}_f^{(O)}(\tau) = \frac{1}{12} \sum_{w \in O} Y_f(\tau, w)` at `y \in \{3, 5, 10, 20, 30\}` (`x = 13/100`), verifying exact CKM unitarity (`< 10^{-35}`), exact `M`-invariance on `w` (`< 10^{-35}`), and exact `y = 20 \to 30` Gramian rates — cleanly establishing whether Orbit-Gramians preserve hierarchy + alignment + slow mixing or wash them out (`B1944`-style).
- **Falsifier:** Any failure of the exact `[6, 6, 3, 3, 0, 0, 0, 0]` algebraic orbit theorem, CKM non-unitarity `> 10^{-30}`, or `M`-action non-invariance `> 10^{-30}` on `\mathcal{H}_{L,f}^{(O)}`.

### `G5` (`O5`) — `P-845` Group-Theoretic Audit (`N = 1..60`) & Head-to-Head Comparison with `agy-exp` `E_\tau[6]_{\mathrm{prim}}` Shell
- **Pre-Committed Expectations:**
  1. Exhaustive algebraic census across all `N = 1..60` of (i) unit-lens ties `(\mathbb{Z}/N\mathbb{Z})^\times`, (ii) non-unit `gcd(6Y, N)` order collapses (specifically `3 \mid 6Y(L, e)` collapsing order-`3m` leptons to order-`m` whenever `3 \mid N`!), and (iii) minimal `N` carrying `K_5^*` (`5 \mid N`) with zero sector ties and genuine 2nd-gen `e \neq d` splitting — explicitly comparing `N = 10`, `N = 15`, `N = 20`, and `N = 30` under Guardrail 1!
  2. Head-to-head 45-dps evaluation of the `24`-point `E_\tau[6]_{\mathrm{prim}}` Gramian, the `96`-point `P_{30}` Gramian, and the `4`-point `K_5^*` Gramian at `y \in \{3, 10, 20, 30\}` (plus exact `T` and `S` modular invariance checks on `E_\tau[6]_{\mathrm{prim}}` and `P_{30}` using exact `L_2` law).
- **Falsifier:** Any arithmetic contradiction with `B1976` `E0` at `N \in \{5, 6, 30\}` or failure of `K_5^*` Gramian `e = d` tie (`< 10^{-35}`).

### `G6` — Guardrail-3 Haar `U(3)^3` Basis-Scrambling & `6/6` Planted Fault Controls (`PF1`–`PF6`)
- `10`-trial independent random Haar `U(3)^3` basis scrambles (`Y_f \mapsto U_L Y_f U_{R,f}^\dagger`) leave all pointwise and Orbit-Gramian physical observables (`m_2/m_3, m_1/m_3, |V_{\text{CKM}}|, J_{\text{CP}}`) invariant to `< 10^{-30}`, while catching `PF5` (`|U_u^\dagger V_u|` drift `> 0.1`).
- All `6` planted faults must trigger cleanly:
  - **`PF1`:** `6Y(u) = -4 \to -3` breaks `> 90%` of `96` up-sector tropical rates in `O1`.
  - **`PF2`:** Replacing `1/4` by `1/3` in `2|\operatorname{nd}(a) - 1/4|` breaks `100%` (`96/96`) of `V_{23}` rates in `O1`.
  - **`PF3`:** Holding `L_2(\gamma\tau) = L_2(\tau)` constant under `S_{\text{mod}}` / `M` breaks joint covariance in `O3` by `> 10^{-3}`.
  - **`PF4`:** Using wrong point action `w\gamma` instead of `w\gamma^{-1}` under `T` / `M` breaks joint covariance in `O3` by `> 10^{-1}`.
  - **`PF5`:** Non-physical left-right overlap `|U_u^\dagger V_u|` breaks Haar invariance by `> 0.1`.
  - **`PF6`:** Dropping `E[6]_{\mathrm{prim}}` (`P_{30} \to K_5^*`) collapses `e \neq d` splitting to `< 10^{-35}` (`SM-C13` / `B1976` `E2` control).

0 of 19.
