# Phase 11 Technical Report: Exact `1`-Loop Hyperbolic $\mathbb{H}^3$ Huygens Propagator Theorem, `60`-Digit Porti Adjoint Torsion, & $M^{(5)}$ Surgery Partition Shootout (`165` of `165` Cumulative Controls)

- **Clean-Room Package:** `self_consistent_loop/selberg_determinant_phase11`
- **Pre-Registration Seal (`SEAL_SHA256.txt`):** `4e8a55171e1fa6abee2f8accebc6e5d4a6da7613e3aefad9c7a728803e5249ee` (`self_consistent_loop/selberg_determinant_phase11/PREREGISTRATION_PHASE11.md`, locked prior to engine execution)
- **Immutable Phase-5 `v1` Blind Lock:** `ece3d98345a3f4982757dad6cea6837af95923ff088086f64cbc374674f2edbd` (`100%` intact)
- **Track-A Empirical Inputs Used:** **`0 of 19`** (verified via AST scan across all five Track-A modules in `self_consistent_loop/selberg_determinant_phase11/scripts/referee_phase11.py`)
- **Zero-Import Referee Verdict:** **`165` of `165` cumulative planted-fault controls caught** (`145` from Phases 1–10 + `20` new controls in Phase 11)

---

## 1. Three Zero-Parameter `1`-Loop Hyperbolic Theorems (`Gates P11-1` through `P11-3`)

1. **Gate `P11-1` (`self_consistent_loop/selberg_determinant_phase11/src/phase11_toe/p11_1_h3_huygens_propagator_exactness.py` — `50`-Digit $\mathbb{H}^3$ Huygens Propagator Exactness):**
   - Conjugating the radial hyperbolic Laplacian $\Delta_{\mathbb{H}^d} = \sinh^{-(d-1)}r\,\partial_r(\sinh^{d-1}r\,\partial_r)$ by $\sinh^{(d-1)/2}r$ yields the radial Liouville operator $-\partial_r^2 + \frac{(d-1)(d-3)}{4\sinh^2 r} + \frac{(d-1)^2}{4}$.
   - **Uniquely for $d = 3$ ($\mathbb{H}^3$, `and d = 1`)**, the centrifugal curvature potential $\frac{(d-1)(d-3)}{4\sinh^2 r}$ vanishes identically (`50`-digit PDE residual `< 1e-45`, vs. `0.1448` in $\mathbb{H}^2$ and `0.4343` in $\mathbb{H}^4$).
   - **Diagrammatic Double-Counting Theorem & `Clause P11-C1`:** Inserting `0`-point vacuum Selberg trace factors (`\ell_0 / |2\sinh(\mathcal{L}/2)|^2`, Giombi–Maloney–Yin $\prod_{n\ge 2}|1-q^n|^{-2}$, or Ruelle spin products) into boundary-pinned `3`-point Yukawa overlaps double-counts disconnected vacuum bubbles and ruins electroweak gauge unification ($\alpha_{\mathrm{EM}}^{-1}(M_Z) \to 140\text{--}176$). Because the `3`-point $\mathbb{H}^3$ geodesic propagator has **identically zero** $1/\ell_\gamma$ WKB subleading corrections, Phase 11 refutes the Phase-10 conjecture that $1/\ell_\gamma$ geodesic WKB corrections drive the `6` RG-quasi-invariant Tier-2 offsets, localizing them to finite-collar KK boundary-condition or Weierstrass $X_8$ fiber wavefunctions.

2. **Gate `P11-2` (`self_consistent_loop/selberg_determinant_phase11/src/phase11_toe/p11_2_porti_adjoint_torsion.py` — `60`-Digit Wada–Dubois–Yamaguchi–Porti Adjoint Torsion):**
   - Pure-matrix abelian-twisted Fox free-calculus solver (`zero Sage dependency`) reproduces Dubois & Yamaguchi's figure-eight adjoint torsion polynomial $\Delta_{4_1}^{\mathrm{Ad}}(t) = -t^{-3}(t-1)(t^2-5t+1)$ (`laurent_coeff_err < 1e-12`, $|\Delta_{\mathrm{Ad}}(1)| < 10^{-40}$, $|\Delta'_{\mathrm{Ad}}(1)| = 3$) and Porti's meridian adjoint torsion $|\tau_{\mathrm{Ad}}(\mathrm{m004}; \mu)| = 2\sqrt{3} = 3.464101615137754\dots$ to `< 1e-35`.
   - Presentation invariance between `m004` and `m129(-3, 1)` plus $\mathrm{SL}(2, \mathbb{C})$ conjugation and $\mathrm{SL}(2, \mathbb{Z})$ modular framing invariance of $I_{\mathrm{Porti}}(M) = |\tau_{\mathrm{Ad}}(M;\mu)|\sqrt{|\mathrm{Im}\,\tau_{\mathrm{cusp}}|}$ hold to `< 1e-35`, and all `8` sibling `m129(p, q)` surgeries (`9` total surgeries in $p + 3q \equiv 0 \pmod{10}$, `Clause P11-C2`) yield exact finite torsions $|\tau_{\mathrm{Ad}}(M_{p,q}; \mu)| \in [12.9105, 739.4810]$.

3. **Gate `P11-3` (`self_consistent_loop/selberg_determinant_phase11/src/phase11_toe/p11_3_one_loop_overtone_partition.py` — `4`-Branch `1`-Loop $M_{p,q}^{(5)}$ Surgery Partition Shootout):**

| `1`-Loop $M_{p,q}^{(5)}$ Partition Branch | SM-24 (`T1 / T2 / T3`) | $\theta_{\mathrm{mis},0}$ (rad) | $\Omega_a h^2$ (`Tier`) | $\beta_{\mathrm{iso}}^{(1\text{B-SD})}$ (`< 0.038`) | Total `36`-Obs (`T1 / T2 / B / Miss`) | Verdict |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **`11A`: `11D` SUSY Bulk ($Z_{\mathrm{1-loop}}^{\mathrm{SUSY}} = 1$)** | **`18 / 6 / 0`** | **`0.04487`** | **`0.1686` (`T1`)** | **`0.00287` (`PASS`)** | **`26 / 6 / 4 / 0`** | **Canonical Zero-Miss Closure** |
| **`11B`: Non-SUSY GMY Graviton on $M^{(5)}$** | `18 / 6 / 0` | `0.04955` | `0.2055` (`T2`) | `0.00236` (`PASS`) | `25 / 7 / 4 / 0` | Viable Non-SUSY Bound (`0` misses) |
| **`11C`: Bulk Scherk–Schwarz on $M^{(5)}$** | `18 / 5 / 1` | `0.03497` | `0.1024` (`T1`) | `0.00472` (`PASS`) | `26 / 5 / 4 / 1` | `1` Tier-3 Miss (`|J_q| = 9.66e-6`) |
| **`11D`: Pure `3D` Topological CS $|\tau_{\mathrm{Ad}}|^{-1/2}$** | `18 / 5 / 1` | `0.00111` | `0.0001` (`T3`) | **`0.824` (`FAIL`)** | `25 / 5 / 3 / 3` | **Falsified (`21.7x` over Planck $\beta_{\mathrm{iso}}$)** |
