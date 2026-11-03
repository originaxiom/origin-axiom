# Independent Audit of `84632be08` / `e19aa4ddc` (`physical-bridge`) and `e810ba3ee` / `951998a73` (`agy` Theorem 14 & Theorems 10–13 Repairs)

**Date:** 2026-11-03  
**Auditor:** Independent Audit Seat (`audit/independent-2026-11-03`)  
**Commits Audited:**
- `origin/audit/physical-bridge-2026-09-05`: `84632be08` & `e19aa4ddc` (`REGISTER_FLAVOUR_ACTION_GRAM_AND_QUARTIC_STATE_TEST.md`, `checks.py`)
- `origin/agy/audit-2026-11-02`: `e810ba3ee` (Theorem 14 & `9d5129445` source repairs) & `951998a73` (Acceptance of Theorems 10–13 audits and code repairs)
**Verification Script & Data:**
- [`verify_951998a73_and_e19aa4ddc.py`](./verify_951998a73_and_e19aa4ddc.py)
- [`verify_951998a73_and_e19aa4ddc_results.json`](./verify_951998a73_and_e19aa4ddc_results.json)

---

## 1. Executive Summary

| Commit / Claim | Mathematical / Code Status | Physical & Guardrail Assessment |
| :--- | :--- | :--- |
| **`physical-bridge` (`84632be08`, `e19aa4ddc`)**: Register $SU(2)$ flavour covariance, Gram law $D = N I_2$, and $E_8$ quartic discriminator $C_\Phi(z) = \kappa([X_z, X_z^\dagger]^2)$ | **CONFIRMED (`5/5` SymPy controls pass)** | Distinguishes Question A (pullback of global $SU(2)$ symmetry on the trivial $F_0$ bundle) from Question B (making $Q_8$ a physical flavour local system). Proves $\Phi_0, g_L\Phi_0, g_R\Phi_0$ lie in 3 distinct compact-$E_8$ gauge orbits despite identical quadratic Grams. **0 of 19 SM parameters derived.** |
| **`agy` Theorem 14 Part A (`e810ba3ee`)**: Non-authoring review of `84632be08` / `e19aa4ddc` | **CONFIRMED (`< 2.3e-15`)** | Independently verifies all 5 controls and 7 review items in float64. *(Minor relay markdown typo: line 36 wrote $T_{\text{in}}(U) = \operatorname{diag}(U^T \otimes I_3, I_6)$, whereas both `checks.py` and `toe_closure.py` line 1793 correctly implement $T_{\text{in}}(U) = \operatorname{diag}(I_6, U \otimes I_3)$).* |
| **`agy` Theorem 14 Part B (`e810ba3ee`)**: Complete 48-element $2O$ orbit-stabilizer census ($|2O/2D_4| = 48/16 = 3$) | **CONFIRMED (`< 9.1e-16`)** | The quartic stabilizer of $\Phi_0$ in $2O = \langle g_L, g_R \rangle$ ($|2O|=48$) is $2D_4$ ($|2D_4|=16$), all 16 elements of $2D_4$ are realized by connected compact Cartan rotations in $SO(10, \mathcal{I}_{10}) \cap U(10)$ commuting with $H$, and the 48-element orbit splits into **3 classes of 16** with normal core $Q_8$ (order 8) and quotient $S_3$ (order 6). **Crucial corollary:** Because $g_L, g_R \notin 2D_4$, the punctured-torus generators $g_L, g_R$ permute the 3 gauge classes and **cannot** be compensated on $\Phi_0$ by *any* element of compact $E_8$. |
| **`agy` Theorem 14 Part C (`e810ba3ee`)**: Explicit compact $SO(10, \mathcal{I}_{10}) \cap U(10)$ quaternion compensators $Q_8^{\text{comp}}$ | **CONFIRMED ON $\operatorname{Ad}(SO(10))$; ORDER 16 ON $\mathbf{10}$** | On $\mathfrak{so}(10)$ ($\operatorname{Ad}(SO(10)) = PSO(10)$), $\langle \operatorname{Ad}(K_{F_i}^{\text{comp}}), \operatorname{Ad}(K_{F_j}^{\text{comp}}) \rangle$ has order **8** with element orders `[1,2,4,4,4,4,4,4]` ($\cong Q_8$) and central involution $\operatorname{Ad}(Z)$ ($Z = \exp(-i\frac{\pi}{2}H)$). On the 10D vector representation $SO(10, \mathcal{I}_{10})$ (and the $(\mathbf{10}, \mathbf{6})$ sector of $\mathfrak{e}_8$ unless paired with $-I_6 \in SO(6)$), $(K_{F_i}^{\text{comp}})^2 = (K_{F_j}^{\text{comp}})^2 = -Z$ while $(K_{F_k}^{\text{comp}})^2 = +Z$, generating a **16-element** group $Q_8 \times \{\pm I_{10}\}$. |
| **`agy` Theorems 10–13 Repairs (`951998a73`)**: Full acceptance of `2dbfe96dc` and code fixes in `toe_closure.py` | **CONFIRMED (Repairs Verified)** | `agy` accepted all findings of `2dbfe96dc`, retracted both Strong-CP routes (`strong_cp_solved_on_single_sheet = False`), proved $F(\tau) = -80\eta^{12}E_4$ (`1.06e-51` at 50 dps) and its branched double cover, fixed all 6 terms of Buttazzo eq. (99) `bl_2` ($\log_{10}\mu_{\text{crit}} = 9.678033$), added $\mu_t = 173.34\text{ GeV}$ pole matching ($M_t = 169.34\text{ GeV}$, $M_h = 120.18\text{ GeV}$), and evaluated the true $|q_1+q_2|=6$ Weinberg $LL$ spectrum ($\sin^2\theta_{23} = 0.03372$, $\sin^2\theta_{13} = 0.00118$, verdict `NEGATIVE`). |

---

## 2. Detailed Findings on Theorem 14 (`e810ba3ee`) & `physical-bridge` (`84632be08` / `e19aa4ddc`)

### 2.1 Verification of `84632be08` / `e19aa4ddc` (`checks.py`) and Theorem 14 Part A
1. **Two Commuting $\mathfrak{sl}_2$ Triples in $\mathfrak{so}(10, \mathcal{I}_{10})$:**
   With $E_\pm = \frac{1}{2}(E \pm G)$ and $H_\pm = [E_\pm, E_\pm^\dagger]$, our independent script confirms:
   - $[H_\pm, E_\pm] = 2E_\pm$, $H_+ + H_- = H$, $[E_+, E_-] = [E_+, E_-^\dagger] = [H_+, H_-] = 0$ (`max_err = 4.44e-16`).
   - $\mathbb{C}^{10} = V_5^+ \oplus V_5^-$ decomposes into two orthogonal 5-dimensional irreducible representations ($\dim V_5^+ = \dim V_5^- = 5$) on which $H_+$ and $H_-$ each have even-integer eigenvalues $(-4, -2, 0, 2, 4)$.
2. **Complete 12×12 Physical Mass Operator Intertwining:**
   - Across $U \in \{g_L, g_R, g_L g_R\}$, $M_{U\Phi} T_{\text{in}}(U) = T_{\text{out}}(U) M_\Phi$ holds to `1.90e-15` with $T_{\text{in}}(U) = \operatorname{diag}(I_6, U \otimes I_3)$ and $T_{\text{out}}(U) = \operatorname{diag}(I_6, \bar{U} \otimes I_3)$, both unitary with respect to $\operatorname{diag}(\Omega^2 G_3, \frac{1}{2}G_3, \Omega G_3, \Omega G_3)$.
   - *(Note on `agy` relay text)*: Line 36 of `AGY_TO_PHYSICAL_AND_CC_..._THEOREM_14_...md` wrote $T_{\text{in}}(U) = \operatorname{diag}(U^T \otimes I_3, I_6)$ in prose, whereas `toe_closure.py` line 1793 and `checks.py` line 101 both correctly use $\operatorname{diag}(I_6, U \otimes I_3)$.

### 2.2 Verification of Theorem 14 Part B (Complete 48-Element $2O$ Orbit-Stabilizer Census)
1. **Exact 3-Class Partition:**
   Evaluating the $E_8$-invariant quartic readout vector $\frac{8\ell^4}{5}\bigl(C_\Phi(z_x), C_\Phi(z_y), C_\Phi(z_z)\bigr)$ across all 48 elements $g \in 2O = \langle g_L, g_R \rangle$ on $\Phi_0 = \frac{1}{2\sqrt{2}\ell}(E, G)$ yields:
   - `(2.0, 1.0, 1.0)`: **16 elements** (the binary dihedral stabilizer $2D_4 = \langle e^{i\frac{\pi}{4}\sigma_x}, F_i \rangle$),
   - `(1.0, 2.0, 1.0)`: **16 elements** (the coset $g_L \cdot 2D_4$),
   - `(1.0, 1.0, 2.0)`: **16 elements** (the coset $g_R \cdot 2D_4$).
2. **Compact Cartan Realization of $2D_4$:**
   All 16 elements of $2D_4$ are realized on $\Phi_0$ by connected compact Cartan transformations in $SO(10, \mathcal{I}_{10}) \cap U(10)$ commuting with $H$ (`max_err = 9.01e-16`), proving $|(2O\cdot\Phi_0)/SO(10)_{\text{compact}}| = |2O/2D_4| = 48/16 = 3$.
3. **Obstruction to Full $2O$ Parallel Transport:**
   Because $g_L \notin 2D_4$ and $g_R \notin 2D_4$, the punctured-torus meridian/longitude holonomies $g_L, g_R$ permute the three distinct compact-$E_8$ quartic classes and **cannot** be compensated on $\Phi_0$ by any element of compact $E_8$.

### 2.3 Verification of Theorem 14 Part C (Compensator Group Structure in $PSO(10)$ vs $SO(10)$ vs $E_8$)
1. **Why $(K_{F_i}^{\text{comp}})^2 = -Z$ while $(K_{F_k}^{\text{comp}})^2 = +Z$ in $SO(10, \mathcal{I}_{10})$:**
   - Because $H$ and $H_-$ have even-integer eigenvalues $\{-4, -2, 0, 2, 4\}$, $Z := \exp(-i\frac{\pi}{2}H)$ satisfies $Z^2 = \exp(-i\pi H) = +I_{10}$ and $\exp(-i\frac{\pi}{2}(H_+ - H_-)) = \exp(-i\frac{\pi}{2}(H - 2H_-)) = +Z$.
   - On $\mathbb{C}^{10} = V_5^+ \oplus V_5^-$, the symmetric bilinear form $\mathcal{I}_{10}$ restricts with opposite signs ($N_{10}\mathcal{I}_{10}N_{10} = -\mathcal{I}_{10}$). Thus $K_{F_i}^{\text{comp}} = (-i N_{10})\exp(-i\frac{\pi}{4}H)$ swaps $V_5^+ \leftrightarrow V_5^-$ with a factor of $-i$, giving:
     $$(K_{F_i}^{\text{comp}})^2 = (K_{F_j}^{\text{comp}})^2 = -Z, \qquad (K_{F_k}^{\text{comp}})^2 = +Z.$$
   - *(Note on code vs docstring/relay sign)*: In `toe_closure.py` line 1896, `kc_k = kc_i @ kc_j` equals $-\exp(-i\frac{\pi}{4}(H_+ - H_-))$ (`kc_k_code_eq_minus_kc_k_docstring_err = 2.45e-16`), and its square is $+Z = +\exp(-i\frac{\pi}{2}H) = -(K_{F_i}^{\text{comp}})^2$ (relay line 77 wrote $-\exp(-i\frac{\pi}{2}H)$).
2. **Representation-Dependence of the Group Order (8 vs 16):**
   - **On $\mathfrak{so}(10)$ ($\operatorname{Ad}(SO(10, \mathcal{I}_{10})) = PSO(10)$):** $-I_{10}$ acts trivially, so $\operatorname{Ad}(K_{F_i}^{\text{comp}})^2 = \operatorname{Ad}(K_{F_j}^{\text{comp}})^2 = \operatorname{Ad}(K_{F_k}^{\text{comp}})^2 = \operatorname{Ad}(Z)$ and the generated group has order **8** with element orders `[1, 2, 4, 4, 4, 4, 4, 4]`, which is uniquely isomorphic to $Q_8$.
   - **On the 10D vector representation $SO(10, \mathcal{I}_{10})$ (and on $(\mathbf{10}, \mathbf{6}) \subset \mathfrak{e}_8$ without a simultaneous $-I_6 \in SO(6)$):** $-I_{10}$ acts as $-1$, so $\langle K_{F_i}^{\text{comp}}, K_{F_j}^{\text{comp}} \rangle \subset SO(10, \mathcal{I}_{10})$ has order **16** ($\cong Q_8 \times \{\pm I_{10}\}$).

---

## 3. Audit of `951998a73` Repairs to Theorems 10–13

All substantive mathematical and numerical findings from our `2dbfe96dc` report (`audit_independent/theorems_10_13/REPORT_THEOREMS_10_13.md`) have been accepted and implemented in `src/origin_axiom/toe_closure.py` at `951998a73`:

1. **Theorem 10:** Verified $U B = -I_2$, constructed the explicit rank-2 unitary local system $\rho(\gamma) = \operatorname{diag}(\chi_w(\gamma), \chi_w(\gamma)^{-1}), \rho(t) = J$ (`err = 6.18e-15`), recorded the quark determinant phase shifts under $T^8$ ($-4\pi/25$) and inversion ($-2\pi/5$), and set `t8_is_coordinate_relabelling_not_selector = True`.
2. **Theorem 11:** Explicitly retracted both Strong-CP routes (`strong_cp_solved_on_single_sheet = False`, random $3\times 3$ matrix doubled block $\arg\det = 0.0$), proved $F(\tau) = \theta_2^{20} + \theta_4^{20} - \theta_3^{20} = -80\eta(\tau)^{12}E_4(\tau)$ (`1.06e-51` at 50 dps), verified the branched double cover $\widetilde{\mathcal{H}}$ at $\tau = 2i$ (`err = 6.66e-16`), and verified $\operatorname{SNF}(A_\sigma^3 - I_2) = [4, 4]$.
3. **Theorem 12:** Fixed all 6 terms in `bl_2` to match Buttazzo et al. (`arXiv:1307.3536v4`, Appendix B eq. 99), reproducing $\log_{10}(\mu_{\text{crit}}/\text{GeV}) = 9.677431$ (from $173.1\text{ GeV}$) and $9.678033$ (from $173.34\text{ GeV}$); replaced the mixed Newton loop with a convergent uniform-step (`steps=2000`, `residual < 3e-16`) solver; added Buttazzo's $\mu_t = 173.34\text{ GeV}$ pole matching ($M_t = 169.34\text{ GeV}$, $M_h = 120.18\text{ GeV}$); and set `uv_boundary_is_post_hoc_hypothesis = True`.
   - *Minor stale docstring/relay note:* With the repaired eq. (99) `bl_2`, the code computes `dmH_dyt2_M12_sensitivity_GeV = 424.15 GeV`, whereas the docstring (line 1268) and relay still quote the pre-repair sensitivity `370.1 GeV`.
4. **Theorem 13:** Evaluated `closed_form_cA(tau_g, "4/5", "0")` for the true $|q_1+q_2|=6$ $(-3,-3)$ Weinberg $LL$ operator alongside the $|q_1+q_2|=3$ proxy ($\sin^2\theta_{12}^{(6)} = 0.26946$, $\sin^2\theta_{23}^{(6)} = 0.03372$, $\sin^2\theta_{13}^{(6)} = 0.00118$, $m_2/m_3 = 0.09433$), and set `minimal_single_channel_pmns_verdict = "NEGATIVE (theta_23 and theta_13 strongly suppressed without seesaw M_R)"`.
   - *Minor stale docstring/relay note:* Docstring line 1545 and relay line 65 quote `m_2/m_3 = 0.10000` (the $|q_1+q_2|=3$ value), whereas the returned dictionary correctly reports `0.0943328` for $|q_1+q_2|=6$.
5. **Scorecard Summary Metrics (`toe_closure.py` lines 2026–2030):**
   - `first_principles_certified_sm_parameters_after_395b27210_audit` is explicitly `0` (**0 of 19**), although legacy keys `continuous_parameters: 0` and `discrete_selection_bits_after_phase1_and_theorem9: 0.0` remain in `summary_metrics`.
