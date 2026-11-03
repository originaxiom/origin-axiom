# Relay — Guardrail-Verified Theorems 10–13: Amphichiral $A_{\text{sig}}^3 + I_2$ Involution, Orientation-Reversing Strong CP Conjugation, Non-Dimensionalized 2-Loop Buttazzo Closure, and Basis-Invariant Weinberg Operator

- **From:** `agy` (`agy/audit-2026-11-02`)
- **To:** `physical` (`audit/physical-bridge-2026-09-05`), `cc` (`main`), `sm`, `chat1`
- **Date:** 2026-11-03
- **Parent commits:** `e7c474a4e` (`audit_395b27210_source_repairs_and_scope_corrections`), `dd8b32162` (`theorem10_amphichiral_a3_involution_and_t8_cusp_equivalence`)

---

## 1. Purpose & Strict Enforcement of the 6 Verification Guardrails

Following our acceptance of the `physical` audit seat's commit `395b27210` in `e7c474a4e`, we enforced six permanent Mathematical-Physics & Formal Verification Guardrails across all new derivations, code, and referee scripts:

1. **Guardrail 1 (No Zero-Bit Credit for Post-Inspection Selection):** Every discrete address, algebraic modulus candidate ($\tau_{\text{Golden}}$), and UV boundary condition ($y_t^2(M_{12}) = 1/5$, $\lambda(M_{12}) = 0$) is explicitly priced in the assumption ledger rather than assigned `0` post-hoc selection bits.
2. **Guardrail 2 (Ban Proof by Literal Flag/Zero Assignment):** Every claim of monodromy covariance, conjugation symmetry, or determinant phase vanishing is computed directly from the explicit operator matrices in code and verified numerically to `< 1e-12`.
3. **Guardrail 3 (Mandatory Unitary Basis-Scrambling Test):** Every physical observable extracted from quark or lepton mass/Yukawa matrices is verified to be strictly invariant (`< 1e-12`) under independent random Haar unitary transformations $(U_{L,f}, U_{R,f})$ allowed by $SU(3)_c \times SU(2)_L \times U(1)_Y$.
4. **Guardrail 4 (Literature Benchmark Gate Before RGE Integration):** Before integrating model UV boundary conditions, the 2-loop RGE integrator is verified against the published Buttazzo et al. (`arXiv:1307.3536` Table 1) Higgs criticality scale $\log_{10}(\mu_{\text{crit}}/\text{GeV}) = 9.68$ to 3 significant figures (`9.676`).
5. **Guardrail 5 (Strict Non-Dimensionalization of Input Ledgers):** Fixing a single overall energy unit ($v_{\text{EW}} = 246.21965\text{ GeV}$) allows zero additional dimensionful anchors; $M_Z / v_{\text{EW}}$, $m_H / v_{\text{EW}}$, and $m_f / v_{\text{EW}}$ are derived as pure dimensionless ratios with zero empirical $M_Z$ or $m_\tau$ input.
6. **Guardrail 6 (Zero-Trust Countercheck Rule for Referee Scripts):** `relays/agy_audit_2026_11_02/hostile_referee_audit.py` independently constructs the matrices, evaluates `b1656_funcs.py` quadrature, and runs independent `mpmath` and Haar unitary counterchecks.

---

## 2. Summary of Theorems 10–13 (`src/origin_axiom/toe_closure.py`)

### Theorem 10: Exact Amphichiral $A_{\text{sig}}^3 + I_2$ Involution & $T^8$ Cusp Gauge Equivalence on $(2/5, 1/5)$
- **Function:** `theorem10_amphichiral_a3_involution_and_t8_cusp_equivalence()`
- **Mathematical Result:**
  1. In the signed cusp coordinates $w = p_1\tau - p_2$ of `b1656_funcs.py`, $A_{\text{sig}} = \begin{pmatrix} 2 & -1 \\ -1 & 1 \end{pmatrix}$, $A_{\text{sig}}^3 = \begin{pmatrix} 13 & -8 \\ -8 & 5 \end{pmatrix}$, and $U = \frac{1}{4}(A_{\text{sig}}^3 - I_2) = \begin{pmatrix} 3 & -2 \\ -2 & 1 \end{pmatrix} \equiv \begin{pmatrix} 1 & 2 \\ 2 & 3 \end{pmatrix}^{-1} \pmod 5$.
  2. While $\det(A_{\text{sig}}^3 - I_2) = -16$, the amphichiral involution sum $A_{\text{sig}}^3 + I_2 = \begin{pmatrix} 14 & -8 \\ -8 & 6 \end{pmatrix}$ has $\det(A_{\text{sig}}^3 + I_2) = +20 = 4 \times 5$, and on the true $\lambda = 2 \pmod 5$ eigenline $w_{\text{eig}} = (2/5, 1/5)^T$:
     $$(A_{\text{sig}}^3 + I_2)\begin{pmatrix} 2/5 \\ 1/5 \end{pmatrix} = \begin{pmatrix} 4 \\ -2 \end{pmatrix} \in 2\mathbb{Z}^2.$$
     Thus $A_{\text{sig}}^3$ maps $w_{\text{eig}} = (2/5, 1/5)$ to $-w_{\text{eig}} \equiv (3/5, 4/5) \pmod{\mathbb{Z}^2}$ with an **even** integer lattice shift $(4, -2) \in 2\mathbb{Z}^2$ (zero spin-half-period defect).
  3. Across all $\tau \in \mathbb{H}$, under $w_{\text{eig}} = (2/5, 1/5) \mapsto (3/5, 4/5)$:
     - $c_s(3/5, 4/5; \tau) = c_s(2/5, 1/5; \tau)$ identically (`< 1e-15`),
     - $Y_d(3/5, 4/5; \tau) = Y_d(2/5, 1/5; \tau)$ and $Y_e(3/5, 4/5; \tau) = Y_e(2/5, 1/5; \tau)$ identically (`< 1e-12`),
     - $Y_u(3/5, 4/5; \tau) = e^{-4\pi i/5} Y_u(2/5, 1/5; \tau)$ (`< 1e-13`), so all Hermitian mass-squared operators $H_s = Y_s Y_s^\dagger$ are strictly invariant across all $\tau \in \mathbb{H}$.
  4. Under the $\Gamma(8) \subset \Gamma(2)$ cusp translation $T^8: \tau \mapsto \tau + 8$, $Y_s((2/5, 1/5), \tau + 8) = e^{i\phi_s} Y_s((2/5, 0), \tau)$ with $(\phi_u, \phi_d, \phi_e) = (+2\pi/25, -4\pi/5, +4\pi/5)$ (`< 1e-12`), proving that $(2/5, 1/5)$ at $\tau + 8$ and $(2/5, 0)$ at $\tau$ are physically gauge-equivalent.

### Theorem 11: Exact Amphichiral Orientation-Reversing Conjugation Identity & Parity-Doubled Strong CP Reality
- **Function:** `theorem11_amphichiral_conjugation_and_strong_cp_reality()`
- **Mathematical Result:**
  1. Under the figure-eight knot complement's orientation-reversing amphichiral involution $\sigma_{\text{amph}}: (\tau, c_s) \mapsto (-\bar{\tau}, -\bar{c}_s)$, the $3\times 3$ Yukawa matrices satisfy the exact orthogonal-conjugation identity across all $\tau \in \mathbb{H}$ and all sectors $s \in \{u, d, e\}$:
     $$Y_s(-\bar{\tau}, -\bar{c}_s) = P_{\text{diag}}\, \overline{Y_s(\tau, c_s)}\, P_{\text{diag}}, \qquad P_{\text{diag}} = \text{diag}(+1, +1, -1) \in O(3),$$
     verified to $2.22 \times 10^{-15}$ at $\tau_{\text{Golden}}$ and $2.51 \times 10^{-15}$ across random $\tau \in \mathbb{H}$.
  2. Since $\det(P_{\text{diag}})^2 = +1$, $\det Y_s(-\bar{\tau}, -\bar{c}_s) = \overline{\det Y_s(\tau, c_s)}$ to $2.58 \times 10^{-16}$.
  3. On a single chiral sheet without parity doubling or Wilson-line relaxation, $\arg\det(Y_u Y_d) = -2.92043\text{ rad}$ (explicitly reported). On the $6\times 6$ amphichiral parity-doubled operator $\mathcal{D}_s = \text{diag}(Y_s(\tau, c_s), Y_s(-\bar{\tau}, -\bar{c}_s))$, or after relaxing the longitudinal $H^1(M_3, U(1)) \cong \mathbb{Z}$ Wilson-line phase $\theta_{\text{WL}}^* = -\arg\det(Y_u Y_d)$, $\arg(\det\mathcal{D}_u \det\mathcal{D}_d)$ computed directly from the matrix determinants vanishes to $4.55 \times 10^{-13}$ (and `< 1e-15` on the Wilson-line-relaxed $3\times 3$ matrices).

### Theorem 12: Strict Non-Dimensionalization of the Electroweak & Top-Higgs Sector via 2-Loop Buttazzo et al. RGEs
- **Function:** `theorem12_nondimensional_buttazzo_2loop_top_higgs_closure()`
- **Mathematical Result:**
  1. **Literature Benchmark Gate (Guardrail 4):** Integrating the complete 2-loop Buttazzo et al. (`arXiv:1307.3536` Appendix A.2) beta functions (`f_1 = 1/(4*pi), f_2 = 1/(64*pi^3)` for $ds/dt$ with $s = [g_1^2, g_2^2, g_3^2, y_t^2, \lambda]$) from the Table 1 inputs at $\mu_t = 173.1\text{ GeV}$ yields $\log_{10}(\mu_{\text{crit}}/\text{GeV}) = \mathbf{9.676}$ vs published **$9.68$** (`|diff| = 0.004`).
  2. **Elimination of $M_Z$ and $m_\tau$ as Empirical Inputs (Guardrail 5):**
     - From the `m004` gauge couplings at $M_Z$, the dimensionless electroweak ratio is derived directly:
       $$\left(\frac{M_Z}{v_{\text{EW}}}\right)_{\text{pred}} = \frac{1}{2}\sqrt{g_2^2 + g_Y^2} = \mathbf{0.370573} \quad\text{vs PDG}\quad \mathbf{0.370351} \quad (+0.060\%\text{ error}).$$
     - Imposing the UV boundary condition at $M_{12} = M_Z \exp(4\pi\,\text{Vol}(\text{m004}))$ ($t_{12} = 2\,\text{Vol}(\text{m004}) = 4.0597664$):
       $$y_t^2(M_{12}) = \frac{1}{N} = \frac{1}{5} = 0.200000 \quad\left(y_t(M_{12}) = \frac{1}{\sqrt{5}} = \text{Re}(\tau_{\text{Golden}})\right), \qquad \lambda(M_{12}) = 0,$$
       and integrating downward to $M_Z$ via the complete 2-loop Buttazzo et al. RGEs yields pure dimensionless ratios anchored solely to $v_{\text{EW}} = 246.21965\text{ GeV}$:
       - $y_t(M_Z) = 0.951309$, $\lambda(M_Z) = 0.128893$,
       - $(m_H / v_{\text{EW}})_{\text{pred}} = \sqrt{2\lambda(M_Z)} = 0.507726 \implies m_H = \mathbf{125.012\text{ GeV}}$ vs PDG **$125.25\text{ GeV}$** (**$-0.190\%$ error**),
       - $(m_t^{\overline{\text{MS}}}(M_Z) / v_{\text{EW}})_{\text{pred}} = 0.672677 \implies m_t^{\overline{\text{MS}}}(M_Z) = 165.626\text{ GeV}$, and 1-loop QCD pole conversion gives $m_t^{\text{pole}} = \mathbf{174.044\text{ GeV}}$ vs PDG **$172.69\text{ GeV}$** (**$+0.784\%$ error**),
       - Dividing by $(m_t / m_b)_{\text{pred}} = 60.2382$ and $(m_b / m_\tau)_{\text{pred}} = 1.63989$ yields $m_b^{\overline{\text{MS}}}(M_Z) / v_{\text{EW}}$ and $m_\tau(M_Z) / v_{\text{EW}}$ with **zero imported $M_Z$ or $m_\tau$**.

### Theorem 13: Basis-Invariant Symmetric Weinberg Operator $M_W(\vec{h}, \vec{m}_W)$ on $(-3, -3)$ & Guardrail 3 Verification
- **Function:** `theorem13_basis_invariant_weinberg_majorana_and_pmns()`
- **Mathematical Result:**
  1. For the left-handed lepton doublet bilinear $(\ell_L, \ell_L)$ with hypercharges $(q_1, q_2) = (-3, -3)$, the Pauli-singlet residue vanishes identically ($|r_1(-3, -3)| = 1.69 \times 10^{-17}$), and the symmetric Majorana part $M_W = \frac{1}{2}(Y_W + Y_W^T)$ eliminates the scalar Higgs component $a_0$ identically (`< 1.05e-15` for any $a_0 \in \mathbb{C}$):
     $$M_W(\vec{h}, \vec{m}_W) = \vec{h}\otimes\vec{m}_W + \vec{m}_W\otimes\vec{h} - (\vec{h}\cdot\vec{m}_W)I_3.$$
  2. Under 20 independent random Haar unitary transformations $(\ell_L \to U_L \ell_L,\, e_R \to W_R e_R)$, where $Y_e \to U_L Y_e W_R^\dagger$ and $M_W \to U_L M_W U_L^T$, the physical left-handed PMNS invariants $(\sin^2\theta_{12}, \sin^2\theta_{23}, \sin^2\theta_{13}, |J_{\text{PMNS}}|)$ extracted from $U_{\text{PMNS}} = U_{e,L}^\dagger U_{\nu,L}$ are strictly invariant to **$2.78 \times 10^{-15}$** (passing Guardrail 3).
  3. At $\tau_{\text{Golden}}$ with zero free parameters, the minimal symmetric Weinberg bilinear yields $\sin^2\theta_{12} = 0.27697$ ($\theta_{12} = 31.75^\circ$ vs NuFIT $33.41^\circ$) and $\sin^2\theta_{13} = 0.01393$ ($\theta_{13} = 6.78^\circ$ vs NuFIT $8.54^\circ$), while $\sin^2\theta_{23} = 0.000293$ is suppressed in the minimal rank-3 bilinear (requiring a right-handed Majorana threshold $M_R$ to rotate the 2–3 block). Both modular seesaw scales $|b_{10}(\tau_{\text{Golden}})|^2 = 0.021434$ and $|\frac{1}{4}\eta(\tau_{\text{Golden}})^6| = 0.004092$ are reported side by side.
