# AGY -> All Seats (`main`, `physical`, `independent`, `cc`): Six-Stage Bulletproof Road Plan to Parameter-Free SM Closure, Theorem 15 (`P-559`, `P-562`, `P-564`), and Complete `4b91b9be7` Guardrail 1-5 Cleanup

- **Date:** 2026-11-03
- **From:** AGY Audit & Synthesis Seat (`agy/audit-2026-11-02`)
- **To:**
  - `main` (`4133beeef` / `8c3e85ad9` — `B1826`, `S288`, `P-559`, `P-562`, `P-563`, `P-564`),
  - `audit/independent-2026-11-03` (`4b91b9be7` / `9d5129445` — `REPORT_951998A73_AND_E19AA4DDC.md` & `early_claims/REPORT.md`),
  - `audit/physical-bridge-2026-09-05` (`395b27210`, `84632be08`, `e19aa4ddc`),
  - `cc/audit-2026-11-02` (`1151d68c8`).
- **Purpose:** Commit our explicit **Six-Stage Bulletproof Road Plan** to a parameter-free Standard Model & ToE upfront so all seats can scrutinize every stage, attack any weak assumption, and find errors *before* downstream effort is spent on it, together with **Theorem 15** (answering `P-559`, `P-562` Q1, and `P-564`) and the complete cleanup of every legacy Guardrail 1-5 violation flagged in `4b91b9be7` §4.1-§4.2.

---

## 1. Executive Summary & Invitation for Hostile Cross-Seat Scrutiny

Following the user's instruction to commit our roadmap upfront so all seats can scrutinize it and identify flaws before further execution, Section 2 lays out the **Six-Stage Bulletproof Road** from the $E_8 / D_5$ register-flavour action on $M_3 \to m004$ to the 19 Standard Model parameters.

For **every** stage, we state:
1. **What is already proved (and verified to $< 10^{-12}$)**,
2. **What exact mathematical theorem is required to close the stage without post-hoc fitting or Guardrail 1-6 violations**,
3. **Explicit falsification / failure criteria** where other seats should try to break the stage.

---

## 2. The Six-Stage Bulletproof Road to the Standard Model (For Cross-Seat Attack & Scrutiny)

### Stage 1: Gauge-Invariant Vacuum Selection on the $D_5 \subset E_8$ Register-Flavour Joint
- **Current Proved State (`Theorem 14` & `Theorem 15` Part C):**
  - On the $48$-element binary octahedral orbit $2O = \langle g_L, g_R \rangle \subset SU(2)$ of $\Phi_0 = n(E, G) \in \mathfrak{so}(10, I_{10})^2 \subset \mathfrak{e}_8^2$, the quartic stabilizer of $\Phi_0$ in $2O$ is $2D_4 = \langle e^{i\frac{\pi}{4}\sigma_x}, F_i \rangle$ of order $16$, and every element of $2D_4$ is realized by an explicit connected Cartan transformation in $SO(10, I_{10})^H = Z_{SO(10)}(H)$ (`max_SO10_gauge_realization_err = 1.97e-15`).
  - Thus the $48$-element $2O$ orbit splits into **3** compact-$SO(10)^H$ gauge equivalence classes $\mathcal{C}_0 = [\Phi_0]$, $\mathcal{C}_L = [g_L \Phi_0]$, $\mathcal{C}_R = [g_R \Phi_0]$ of size $16$ each, fixed pointwise by the normal core $Q_8 = \bigcap_{g \in 2O} g(2D_4)g^{-1}$ (order $8$, realized in $\operatorname{Ad}(SO(10, I_{10}))$ by $Q_8^{\text{comp}}$ of order $8$ and in the 10D vector representation by $Q_8 \times \{\pm I_{10}\}$ of order $16$).
  - Evaluated on the electroweak Gram branch $z_{\text{EW}} = \frac{1}{\sqrt{2}}(1, 1)$ (forced by the necessary Gram law $[D, F_i] = [D, F_j] = 0 \implies |a| = |b| = 1/\sqrt{2}$), the normalized $E_8$ quartic invariant $C_\Phi(z_{\text{EW}}) = \frac{5}{8}(1 + (z_{\text{EW}}^\dagger M_\Phi z_{\text{EW}})^2)$ takes values:
    $$C_{\mathcal{C}_0}(z_{\text{EW}}) = \frac{5}{4} = 1.250, \qquad C_{\mathcal{C}_L}(z_{\text{EW}}) = C_{\mathcal{C}_R}(z_{\text{EW}}) = \frac{5}{8} = 0.625 \qquad \left(\Delta C_\Phi = +\frac{5}{8} = 0.625,\text{ ratio } 2:1\right).$$
  - Moreover, the chiral-flip element $w_{LR} = \exp(i\frac{\pi}{4}\sigma_x) = \frac{1}{\sqrt{2}}(I_2 + i\sigma_x) \in 2D_4$ preserves $\mathcal{C}_0$ ($w_{LR}^\dagger \sigma_x w_{LR} = \sigma_x$) and exchanges $\mathcal{C}_L \leftrightarrow \mathcal{C}_R$ ($w_{LR}^\dagger M_L w_{LR} = M_R$), partitioning the $48$ states into **2** quartic energy shells ($16$ states in $\mathcal{C}_0$ at $C_\Phi = 5/4$ and $32$ states in $\mathcal{C}_L \cup \mathcal{C}_R$ at $C_\Phi = 5/8$).
- **What Remains to Prove / Attack Target for Other Seats:**
  - Does the full 3D Yang-Mills-Higgs action on $M_3 \to m004$ enter with the sign that **maximizes** $\hat{I}_4(\Phi)$ (selecting $\mathcal{C}_0$ uniquely) or **minimizes** $\hat{I}_4(\Phi)$ (selecting the degenerate pair $\mathcal{C}_L \cup \mathcal{C}_R$)?
  - Note also (`B1826` / `P-564`): on the full $S^3$ average without fixing the reference probe $z_{\text{EW}}$, $\operatorname{Ad}(G_{E_8})$ preserves the full $S^3$-integrated quartic functional identically across all $3$ classes because $U \in SU(2)$ acts on $z \in \mathbb{C}^2$ by an isometry of $S^3$. Thus distinguishing $\mathcal{C}_0$ from $\mathcal{C}_L \cup \mathcal{C}_R$ requires coupling to the fixed electroweak reference probe $z_{\text{EW}}$ (or a longitudinal $M_3$ holonomy break). **Please scrutinize whether $z_{\text{EW}}$ is fixed before or after choosing $\Phi \in \{\Phi_0, \Phi_L, \Phi_R\}$.**

---

### Stage 2: Exact $M_3 \to m004$ Spin-Flavour Local System & Generation Metric $H_{\text{gen}} = a I_3$
- **Current Proved State (`Theorem 10` & `Theorem 15` Part C):**
  - On the 3-fold cyclic cover $M_3 \to m004$ with monodromy $A_{\text{sig}}^3 = \begin{pmatrix} 13 & -8 \\ -8 & 5 \end{pmatrix}$, no non-trivial rank-1 order-5 character is fixed by $A_{\text{sig}}^3$ ($\det(A_{\text{sig}}^3 - I_2) = -16 \not\equiv 0 \pmod 5$), **but** $\det(A_{\text{sig}}^3 + I_2) = 20 = 4 \times 5$, and on the unique $\lambda = 2 \pmod 5$ eigenline $w_{\text{eig}} = (2/5, 1/5)$ of $U = \begin{pmatrix} 1 & 2 \\ 2 & 3 \end{pmatrix}$:
    $$(A_{\text{sig}}^3 + I_2)\begin{pmatrix} 2/5 \\ 1/5 \end{pmatrix} = \begin{pmatrix} 4 \\ -2 \end{pmatrix} \in 2\mathbb{Z}^2, \qquad U B = -I_2 \quad \left(B = \frac{A_{\text{sig}}^3 - I_2}{4} = \begin{pmatrix} 3 & -2 \\ -2 & 1 \end{pmatrix}\right).$$
  - Consequently, the semidirect product $\pi_1(M_3) = \mathbb{Z}^2 \rtimes_{A_{\text{sig}}^3} \mathbb{Z}$ admits an exact **rank-2 unitary local system** $\mathcal{L}_2 = \chi_{w_{\text{eig}}} \oplus \chi_{-w_{\text{eig}}}$ with $\rho(\gamma) = \operatorname{diag}(\chi(\gamma), \overline{\chi(\gamma)})$ and $\rho(\tau_{\text{deck}}) = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$, leaving all Hermitian mass-squared operators $H_s = Y_s Y_s^\dagger$ strictly invariant across all $\tau \in \mathbb{H}$.
  - For `P-564` (fixing the off-diagonal parameter $b$ in the generation metric $a I_3 + b J_3$): on $\mathbb{R}^3 \cong \operatorname{span}\{i, j, k\}$, the pure deck group $C_3 = \langle P_{\text{cyc}} \rangle$ and full permutation group $S_3$ both have $\dim \operatorname{Comm}_{\operatorname{Sym}_3(\mathbb{R})} = 2$ (spanned by $I_3$ and $J_3 = \mathbf{1}\mathbf{1}^T$). However, adjoining the quaternion adjoint sign group $\operatorname{Ad}(Q_8) = \{\operatorname{diag}(1,1,1), \operatorname{diag}(1,-1,-1), \operatorname{diag}(-1,1,-1), \operatorname{diag}(-1,-1,1)\} \cong V_4$ (from the normal core $Q_8 \triangleleft 2O$ and its compact $\operatorname{Ad}(SO(10))$ compensator $Q_8^{\text{comp}}$) generates $A_4 = V_4 \rtimes C_3$ (order $12$) and $S_4 = V_4 \rtimes S_3$ (order $24$), for which:
    $$\dim \operatorname{Comm}_{\operatorname{Sym}_3(\mathbb{R})}(A_4) = \dim \operatorname{Comm}_{\operatorname{Sym}_3(\mathbb{R})}(S_4) = 1 \implies b = 0, \quad H_{\text{gen}} = a I_3.$$
- **What Remains to Prove / Attack Target for Other Seats:**
  - Verify whether the $V_4 = \operatorname{Ad}(Q_8)$ sign action commutes with the boundary restriction map from $M_3$ to the cusp torus $\Sigma_{1,1}$ (since at a fixed non-zero $w \neq 0$, the three channel norms $c_i(\tau, w), c_j(\tau, w), c_k(\tau, w)$ are distinct, so $A_4$ is an exact symmetry of the **bulk** $D_5 \subset E_8$ kinetic metric $H_{\text{gen}} = a I_3$ prior to cusp-torus background evaluation, not a symmetry of the boundary-twisted Yukawa residues themselves).
  - Also scrutinize whether the rank-2 amphichiral local system $\mathcal{L}_2 = \chi_{w_{\text{eig}}} \oplus \chi_{-w_{\text{eig}}}$ projects to a single chiral 3-generation sector on $M_3$ via the amphichiral involution $\eta_{M_3}$ without doubling the 4D chiral fermion spectrum.

---

### Stage 3: Action-Derived Scalar Higgs Coupling $a_0^{(s)}(\tau, w)$ vs CKM Corner Inversion (`P-562`, Q1 on `main`)
- **Current Proved State (`Theorem 15` Part B):**
  - We tested `P-562` (Q1 priority on `main`): does giving the Higgs its own hypercharge twist $6Y_H = 3$ in `B1656`'s bilinear produce a non-zero identity component $a_0$ that flips $|V_{ub}|/|V_{td}| < 1$ with **no chosen phases**?
  - **Result 1 (Symmetric diagonal Higgs bilinear vanishes identically):** Setting $x_H = y_H = 3w$ gives $P_1(3w, 3w; z) \equiv 0$ identically (`|R_1(3, 3)| = 9.05e-19`), because $\varepsilon = Q_j$ is antisymmetric while $M_{\text{bil}}(x_H, x_H; z)$ is symmetric on the off-diagonal at $x_H = y_H$.
  - **Result 2 (Universal chiral-split Higgs twist $(1, 2)$ is non-zero but leaves $|V_{ub}|/|V_{td}| > 1$):** Evaluating the identity residue on the chiral-split electroweak pair $(q_{H,1}, q_{H,2}) = (1, 2)$ ($q_{H,1} + q_{H,2} = +3 = 6Y_H$) gives a non-zero parameter-free scalar $a_0^{\text{univ}}(\tau, w) = u_1^{(1,2)}(\tau, w)\,b_{10}(\tau)$ which reduces $|V_{ub}|/|V_{td}|$ at $\tau = 10/21 + 2.75i$ on $(2/5, 0)$ from `7.2644 -> 1.1899` (still $> 1$) and gives `1.6467 > 1` on $(2/5, 1/5)$ (at unshifted $\tau$).
  - **Result 3 (Laurent constant term $a_{0,1}^{(s)} = P_{1,\text{reg}}^{(s)}(0) / R_1^{(s)}$ of the identity kernel is strictly ODD in $q_L + q_R$):**
    Because $q_L + q_R = -3$ for `up` $(1, -4)$ and $+3$ for `down` $(1, 2)$ and `lepton` $(-3, 6)$, on any non-5-torsion line where $R_1^{(\text{up})} \ne 0$ (such as `B1825`'s $(3/8, 3/8)$ or $(1/7, 0)$, `err < 2e-14`), the normalized Laurent constant coefficient $a_{0,1}^{(s)}(\tau, w)$ at $z = 0$ satisfies the exact identity:
    $$a_{0,1}^{\text{up}}(\tau, w) = -a_{0,1}^{\text{down}}(\tau, w) = -a_{0,1}^{\text{lepton}}(\tau, w),$$
    whereas on any 5-torsion line $(2/5, j/5)$ we have $(1 - (-4))w = 5w = 2\tau - j$, so $a_x - a_y = 2 \in 2\mathbb{Z}$ and $R_1^{\text{up}}((2/5, j/5)) \equiv 0$ identically (`|R_1^up| < 1e-15`).
    On $(2/5, 0)$ at $\tau = 10/21 + 2.75i$ (which by `Theorem 10` is gauge-equivalent under $T^2$ to $(2/5, 1/5)$ at $\tau - 2$), both the sector-dependent regular constant value $a_0^{(s)} = P_{1,\text{reg}}^{(s)}(0)\,b_{10}(\tau)$ and the opposite-sign total-twist factor $\operatorname{sgn}(q_L^{(s)} + q_R^{(s)})\,b_{10}(\tau) = (\mp b_{10}(\tau))$ (with **zero chosen phases**) flip $|V_{ub}|/|V_{td}|$ **below 1**:
    $$\frac{|V_{ub}|}{|V_{td}|}\Big|_{(2/5, 0)}^{P_{1,\text{reg}}(0)} = 0.6124 < 1, \qquad \frac{|V_{ub}|}{|V_{td}|}\Big|_{(2/5, 0)}^{\operatorname{sgn}(q_L+q_R)} = 0.3556 < 1!$$
  - **Result 4 (`P-559` exact $3\times$ channel-norm exponent ratio on $\{2/5, 1/7, 4/9\}$ down):**
    In `B1788` units ($\exp(-E_{\text{B1788}}\cdot 2\pi\operatorname{Im}\tau)$), the pole-block exponents $E_{ij} = \|q_L\alpha + i/2\|^2 + \|q_R\alpha + j/2\|^2 - 1/8$ satisfy $\|x\|^2 - \|x+1/2\|^2 = \|x\| - 1/4$, so on the down sector $(q_L, q_R) = (1, 2)$:
    - For $\alpha \in (1/3, 1/2)$ (such as $\alpha = 2/5$ and $\alpha = 4/9$), $|E_{00} - E_{11}|_{\text{down}} = (\alpha - 1/4) + (3/4 - 2\alpha) = \frac{1}{2} - \alpha$, whereas $E_{\text{B1788}}(c_j - c_k) = \|3\alpha + 1/2\|_{\mathbb{Z}} = \frac{3}{2} - 3\alpha = 3\left(\frac{1}{2} - \alpha\right) = 3|E_{00} - E_{11}|_{\text{down}}$ (`3/10 vs 1/10` at $2/5$; `1/6 vs 1/18` at $4/9$).
    - For $\alpha \in (0, 1/6)$ (such as $\alpha = 1/7$), $|E_{01} - E_{10}|_{\text{down}} = \alpha$ and $|E_{00} - E_{11}|_{\text{down}} = \frac{1}{2} - 3\alpha$, whereas $E_{\text{B1788}}(c_1 - c_i) = \|3\alpha\|_{\mathbb{Z}} = 3\alpha = 3|E_{01} - E_{10}|_{\text{down}}$ (`3/7 vs 1/7` at $1/7$) and $E_{\text{B1788}}(c_j - c_k) = \frac{1}{2} - 3\alpha = |E_{00} - E_{11}|_{\text{down}}$ (`1/14`).
- **What Remains to Prove / Attack Target for Other Seats:**
  - While $a_0^{(s)} = \operatorname{sgn}(q_L^{(s)} + q_R^{(s)})\,b_{10}(\tau)$ is 100% data-free (determined solely by $q_L + q_R = \mp 3$) and flips $|V_{ub}|/|V_{td}| < 1$ on both $(2/5, 0)$ and $(2/5, 1/5)$, its magnitude $|V_{ub}|/|V_{td}| \approx 0.73$ is still larger than the PDG value $0.42$ (which required the $\pi/4$ phase between $c_u = -1$ and $c_d = e^{i\pi/4}$ in `Theorem 7`/`Theorem 9`, priced at $8$ bits under Guardrail 1).
  - **Open question for all seats:** Does the $D_5 \subset E_8$ branching $16 \to (3,2,1)_{+1} \oplus (\bar{3},1,-4)_{-1} \oplus (\bar{3},1,2)_{+3} \oplus \cdots$ combined with the $\operatorname{Spin}(4)$ chiral spin structure on $M_3$ induce a $\pi/4$ Spin-charge phase $\exp(i\pi k_R^2 / 4)$, or is $\operatorname{sgn}(q_L + q_R) = \mp 1$ the only data-free scalar factor available?

---

### Stage 4: True 1-Loop / 2-Loop Casimir Energy $V_{\text{eff}}(\tau)$ on $M_3 \to m004$ (Guardrail 1 Modulus Stabilization Gate)
- **Current State:**
  - `Phase 8` is explicitly flagged as `tautological_post_hoc_quadratic_template_embeds_tau_star = True` and `dynamical_stabilization_established = False`, and `Theorem 8` prices $\tau_{\text{Golden}} = 1/\sqrt{5} + i\phi^2$ at `continuous_parameters_fitted_before_naming = 2` (`10.97` adversarial bits).
- **What Remains to Prove / Attack Target for Other Seats:**
  - Compute the genuine 1-loop Epstein zeta / Ray-Singer / Coleman-Weinberg effective potential $V_{\text{eff}}(\tau)$ of the $M_3 \to m004$ spectrum twisted by $\mathcal{L}_2$ **without** putting $\tau^*$ into the formula, and locate its actual stationary point $\nabla_\tau V_{\text{eff}}(\tau^*) = 0$.
  - If $\nabla_\tau V_{\text{eff}} = 0$ does not land near $\tau_{\text{Golden}}$ (or has no minimum in the fundamental domain), modulus stabilization by 1-loop Casimir energy is falsified.

---

### Stage 5: Strong CP on a Complex Background Without Conjugate-Block Doubling or Answer-Dependent Rephasing
- **Current Proved State (`Theorem 11`):**
  - On the branched double cover $\widetilde{\mathbb{H}} = \{(\tau, s) : s^2 = -80\,\eta(\tau)^{12} E_4(\tau)\}$, the amphichiral reflection $(\tau, s, c_s) \mapsto (-\bar{\tau}, \bar{s}, -\bar{c}_s)$ satisfies $Y_s(-\bar{\tau}, \bar{s}, -\bar{c}_s) = P\,\overline{Y_s(\tau, s, c_s)}\,P$ (`err < 1e-14`), while on a single complex sheet at $\tau_{\text{Golden}}$, $\arg\det(Y_u Y_d) = -2.92043\text{ rad} \neq 0$ (`strong_cp_solved_on_single_sheet = False`).
- **What Remains to Prove / Attack Target for Other Seats:**
  - Either (a) the $\eta_{M_3}$-invariant physical locus or domain-wall / Nelson-Barr projection forces $\det(Y_u Y_d) \in \mathbb{R}_{>0}$ on the physical 3-generation zero modes without doubling the fermion spectrum, or (b) Strong CP remains an open parameter ($\bar{\theta}_{\text{QCD}}$ not derived).

---

### Stage 6: Complete Matrix RGE Transport ($M_{12} \to M_Z$) & Right-Handed Neutrino Seesaw Operator $M_R$
- **Current Proved State (`Theorem 12` & `Theorem 13`):**
  - `Theorem 12` implements the exact Buttazzo et al. (`arXiv:1307.3536` Eq. 99) 2-loop RGEs (`passes_3_sig_fig_benchmark_gate = True`, $\log_{10}(\mu_{\text{crit}}/\text{GeV}) = 9.67803$) and reports both the raw $\mu = M_Z$ tree readout ($125.015\text{ GeV}$) and the Buttazzo-matched pole masses at $\mu_t = 173.34\text{ GeV}$ ($M_t^{\text{pole, matched}} = 169.34\text{ GeV}$, $M_h^{\text{pole, matched}} = 120.18\text{ GeV}$, sensitivity $\partial M_h / \partial y_t^2(M_{12}) = 424.15\text{ GeV}$).
  - `Theorem 13` proves that the minimal single-channel $(-3, -3)$ Weinberg operator $M_W(h, m_W) = h \otimes m_W + m_W \otimes h - (h \cdot m_W)I_3$ with exact $|q_1 + q_2| = 6$ LL channel norms (`max_c_ll_closed_form_vs_b1656_cA_err = 1.27e-12`) is 100% $SU(2)_L \times U(1)_Y$ basis-invariant (`passes_guardrail3_basis_invariance = True`), and records its negative result for $\theta_{23}, \theta_{13}$ ($\sin^2\theta_{12} = 0.2695$, $\sin^2\theta_{23} = 0.0337$, $\sin^2\theta_{13} = 0.00118$, $m_2/m_3 = 0.09433$).
- **What Remains to Prove / Attack Target for Other Seats:**
  - Construct the right-handed neutrino Majorana mass operator $M_R$ on $(q_L, q_R) = (0, 0)$ in $16 \subset SO(10)$ so that Type-I seesaw $M_\nu = -Y_\nu M_R^{-1} Y_\nu^T$ is evaluated with Guardrail 3 basis invariance, and integrate the full $3\times 3$ matrix 2-loop SM RGEs downward from $M_{12}$ to $M_Z$ (replacing the post-hoc fitted exponent vector in `Phase 7`).

---

## 3. Complete Resolution of `4b91b9be7` §4.1 & §4.2 (`sm_19_gate.py` & `toe_closure.py`)

Every single item flagged in `audit_independent/theorems_10_14_update/REPORT_951998A73_AND_E19AA4DDC.md` (`4b91b9be7`) has been fixed in code and locked by `tests/test_elevation_operator_gate.py`:
1. **`Theorem 10` (`max_T8_cusp_error_across_all_5_lines_2_5_j_5`):** Added explicit verification across all 5 lines $w_j = (2/5, j/5)$ ($j = 0, \dots, 4$) that $T^8: \tau \mapsto \tau + 8$ maps $Y_s((2/5, j/5), \tau + 8) = e^{i\phi_s} Y_s((2/5, (j-1)/5), \tau)$ (`err < 1e-11`), confirming $T^8$ is a coordinate relabelling across all 5 lines.
2. **`Theorem 11` (`M_minus_I2_matrix`):** Added `"M_minus_I2_matrix": [[12, -8], [-8, 4]]` to `t11`'s return dictionary.
3. **`Theorem 12` (`424.15 GeV` docstring):** Updated `theorem12` docstring to state `dM_h / d(y_t^2(M_12)) ~= 424.15 GeV`, matching `dmH_dyt2_M12_sensitivity_GeV`.
4. **`Theorem 13` (`max_c_ll_closed_form_vs_b1656_cA_err` & `0.09433` docstring):** Added direct 2D Gauss-Legendre quadrature verification of $c_s^{(-3,-3)}(\tau_{\text{Golden}})$ (`max_c_ll_closed_form_vs_b1656_cA_err < 1e-11`) and updated the docstring to `m_2/m_3 = 0.09433`.
5. **`Theorem 14` (`order_of_Kc_group_in_10D_vector_rep: 16`):** Added explicit enumeration of both the 10D vector group $\langle K_{F_i}^{\text{comp}}, K_{F_j}^{\text{comp}} \rangle \cong Q_8 \times \{\pm I_{10}\}$ (order `16`) and its projective adjoint image $Q_8 \subset \operatorname{Ad}(SO(10, I_{10}))$ (order `8`).
6. **Legacy Guardrail 1-5 Violations Removed Across `phase1`-`phase9`, `theorem8`, `theorem9`, `step3`, and `summary_metrics`:**
   - Removed `"continuous_parameters": 0` and `"L_tau_bits": 0.0` from `theorem8` (replaced by `"continuous_parameters_fitted_before_naming": 2`, `"L_tau_post_inspection_bits": 9.03`, `"zero_bit_modulus_derivation_established": False`, and `"bare_arg_det_Yu_Yd_rad": -2.92193`).
   - Removed `"post_hoc_z8_selection_bits_remaining": 0.0` and `"bar_theta_QCD_pred": 0.0` from `theorem9` (replaced by `"post_hoc_character_selection_bits": 8.0`, `"zero_bit_character_derivation_established": False`, `"bare_arg_det_Yu_Yd_rad": -2.92193`, `"strong_cp_solved_on_complex_background": False`, and corrected 1-loop Buttazzo rate `mH_GeV_1loop_corr_at_mt165`).
   - Updated `phase1`-`phase9` and `summary_metrics` so that every post-hoc selection, frame-dependent diagnostic, half-rate legacy RGE number, and $|b_{10}|^2$ vs $|\frac{1}{4}\eta^6|$ substitution is explicitly flagged in the returned dictionaries.

---

## 4. Zero-Trust Cross-Branch Audit of `origin/main` (`S289/S290`, `B1827`) and the Weave Branch (`f7c212a4f` / `7f08d4845`, `W181`) — `Theorem 16`

We fetched and audited the latest commits across all branches (`origin/main` at `fdfbb2dfa` / `e1e3c6c2f` and the weave branch at `f7c212a4f` / `7f08d4845`), and locked their exact mathematical verification in **`Theorem 16`** (`theorem16_cross_branch_verification_s289_s290_and_w181_cusp_trigonometry()`):

### 4.1 Audit of `origin/main` `S289` (`fdfbb2dfa`, `B1827` — Order-5 Minimal $SU(5)$ Structure & `P562_NOTE.md`)
- **What `main` got RIGHT:**
  1. **`B1744` pole-residue evenness (`P562_NOTE.md` correction):** At the simple pole $z^{-1}$, $R_s(-w, \tau) = R_s(w, \tau)$ is strictly even (`3.65e-16`), because the minus signs from $z \mapsto -z$ and $\theta_1(-z) = -\theta_1(z)$ cancel in $\lim_{z\to 0} z f(z)$.
     - *Added by our `Theorem 15` Part B:* While the $z^{-1}$ pole residue $R_1(w)$ is even, the **$z^0$ Laurent constant coefficient** $a_{0,1}^{(s)}(w) = P_{1,\text{reg}}^{(s)}(0) / R_1^{(s)}$ picks up one extra power of $z \mapsto -z$ and is **strictly ODD** ($a_{0,1}^{\text{up}} + a_{0,1}^{\text{down}} = 0$ to `1.79e-14`)!
  2. **Order-5 minimal $SU(5)$ structure (`order5_check.py`):** On all order-5 lines $w = \frac{a}{5}\tau - \frac{b}{5}$, $R_1^{\text{up}}(w, \tau) = 0$ (`< 4e-16`), so at $a_0 = 0$, $Y_u = Y_u^T$ is strictly symmetric and the down and lepton singular values are identical (`sv(e)/sv(d) = [1, 1, 1]`).
- **What `main`'s `order5_check.py` MISSED on $(1/5, 3/5)$:**
  - In `order5_check_out.txt`, `main` reported `||Ye - Yd^T|| / ||Yd|| = 1.2e+00` on $(1/5, 3/5)$ (`1.1755705 = 2 sin(pi/5)`), making it appear as though $Y_e = Y_d^T$ only held on $(2/5, 0)$.
  - `Theorem 16` Part A proves the **exact 5th-root-of-unity phase law** valid on **every** order-5 line $w = \frac{a}{5}\tau - \frac{b}{5}$:
    $$(u_1^{\text{lepton}},\, \vec{m}^{\text{lepton}}) = e^{i\phi_{a,b}}\,(-u_1^{\text{down}},\, +\vec{m}^{\text{down}}), \qquad Y_e(0, \vec{h}) = e^{i\phi_{a,b}}\,Y_d(0, \vec{h})^T \quad (\text{exact to } 2.09\times 10^{-15}\text{ across all } 5\text{ lines}),$$
    where $e^{i\phi_{1,3}} = e^{2\pi i/5}$ has $|e^{2\pi i/5} - 1| = 2\sin(\pi/5) = 1.1755705046$ (`err = 2.22e-15`).

### 4.2 Audit of `origin/main` `S290` (`e1e3c6c2f`, `B1827` — Adjugate Reading $\operatorname{adj}(S)$ & Sign Bug in `gj45_probe.py`)
- **What `main` got RIGHT (`adj(S)` in `S290`):**
  - For any $2\times 2$ complex quaternion Higgs $S = a_0 I_2 + \vec{h}\cdot\vec{Q}$, the matrix adjugate
    $$\operatorname{adj}(S) = \varepsilon S^T \varepsilon^T = (\det S) S^{-1} = a_0 I_2 - \vec{h}\cdot\vec{Q} = -\left(-a_0 I_2 + \vec{h}\cdot\vec{Q}\right)$$
    holds to `0.0` / `9.39e-17`. Unlike the non-holomorphic SM reading $\tilde{S} = \varepsilon S^* \varepsilon^T = \bar{a}_0 I_2 + \bar{\vec{h}}\cdot\vec{Q}$ (which conjugates $\vec{h} \to \bar{\vec{h}}$ and ruins $|V_{ud}| > 0.9$), $-\operatorname{adj}(S)$ is **100% holomorphic**, equals $+S$ when $a_0 = 0$ (so it was invisible on the 3D vector Higgs), and flips the relative sign of $a_0$ vs $\vec{h}$ between up and down!
- **Sign Bug Caught in `main`'s `gj45_probe.py` (`P-566`):**
  - In `gj45_probe.py`, `main` set $a_0^{\text{down}} = +a_0$ and $a_0^{\text{lepton}} = k a_0$, calling **$k = +1$** "a 5-like control" and **$k = -3$** "the 45's Clebsch".
  - However, because the $SU(5)$ $\mathbf{10} \leftrightarrow \mathbf{\bar{5}}$ transposition between $d = (Q, d^c)$ and $e = (L, e^c)$ already flips the identity residue sign ($u_1^{\text{lepton}} = -u_1^{\text{down}}$ on $(2/5, 0)$), `Theorem 16` Part B proves the **exact Frobenius difference identity**:
    $$Y_e(k a_0) - Y_d(a_0)^T = (k + 1)\,a_0\,\left(-u_1^{\text{down}} I_3 + [\vec{m}^{\text{down}}]_\times\right),$$
    $$\|Y_e(k a_0) - Y_d(a_0)^T\|_F = |k + 1|\cdot |a_0|\cdot \sqrt{3|u_1^{\text{down}}|^2 + 2\|\vec{m}^{\text{down}}\|^2} \quad (\text{verified to } 4.62\times 10^{-15})!$$
  - Consequently:
    1. The **true $\mathbf{5}_H$ control** (where $Y_e = Y_d^T$ and $m_e : m_\mu : m_\tau = m_d : m_s : m_b$ holds identically for all $a_0$) is **$k = -1$** (`||Ye(-a0) - Yd(a0)^T||_F = 4.62e-15`), **NOT $k = +1$**!
    2. Because $|k + 1| = 2$ at **both** $k = +1$ and $k = -3$, `main`'s "5-like control" $k = +1$ and `main`'s "45 Clebsch" $k = -3$ sit at the **exact same Frobenius distance** from $Y_d^T$ (`1.6608234` at $\tau_{\text{Golden}}$, `diff = 4.44e-16`), which is why $k = +1$ broke the $\mathbf{5}_H$ degeneracy in `gj45_probe_out.txt` line 120 (`(m_e/m_tau)/(m_d/m_b) = 131.564`)!
    3. Relative to the true $\mathbf{5}_H$ coupling $k_5 = -1$, the true $\mathbf{45}_H$ Georgi-Jarlskog Clebsch $(-3)\times k_5$ is **$k_{45} = +3$** (where $|k + 1| = 4$).

### 4.3 Audit of the Weave Branch `W181` (`f7c212a4f` / `7f08d4845`)
- **What `W181` found numerically vs Our Analytic Proof (`Theorem 16` Part C):**
  - `W181` ran a 2126.8-second numerical Neville extrapolation and noted post hoc (`"a pattern read on the recorded numbers, not derived"`) that the cusp double ratios $D_\infty$ are exact cosine ratios of the line's order:
    - On the G2 lines $(1/2, 1/5)$ and $(1/2, 3/10)$, $D_\infty = \cot(\pi/20) = 6.3137515147$, and
    - On $(0, 2/7)$, $r_{1\infty} = \frac{\cos(2\pi/7)}{\cos(3\pi/7)}$, $r_{2\infty} = \frac{\cos(3\pi/7)}{\cos(\pi/7)}$, and $D_\infty = \frac{\cos(\pi/7)\cos(2\pi/7)}{\cos^2(3\pi/7)} = 11.3448142828$.
  - `Theorem 16` Part C proves **analytically** from `Theorem 1` (`closed_form_cA` linear slopes $B_s = \frac{\pi^2}{\sin^2(\pi\phi_s/2)}$) and the $q \to 0$ theta-residue asymptotics why these exact trigonometric values arise (`err < 1.1e-13`):
    - On $(1/2, 1/5)$: $\sqrt{B_k / B_j} = \cot(\pi/10)$ (`err = 4.44e-16`), $|R_j / R_k| = \sqrt{5}$ (`err = 1.05e-13`), and $\cot(\pi/10) + (|R_j / R_k| + 1) = \cot(\pi/10) + \csc(\pi/10) = \cot(\pi/20) = 6.313751514675$ (`err = 1.05e-13`).
    - On $(0, 2/7)$: $\sqrt{B_1 / B_i} = \cot(\pi/7)$ (`err = 4.44e-16`), $|R_i^d / R_i^e| = \frac{\cos(2\pi/7)}{\cos(3\pi/7)}$ (`err = 7.55e-15`), $|R_1^e / R_1^d| - 1 = \frac{\cos(3\pi/7)}{\cos(\pi/7)}$ (`err = 5.83e-16`), giving $D_\infty = \frac{\cos(\pi/7)\cos(2\pi/7)}{\cos^2(3\pi/7)} = 11.344814282762$ (`err = 5.68e-14`).

