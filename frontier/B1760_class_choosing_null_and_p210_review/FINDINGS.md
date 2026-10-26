# B1760 — THE CLASS-CHOOSING & JOINT-LAW NULL CALIBRATION ACROSS THE CENSUSES (P-381 / P-384) AND INDEPENDENT NON-AUTHORING AUDIT OF THE P210 PACKAGE & OCTOBER 24–26 REDUCTIONS (P-386)

**Verdict: PROVED (computed & audited; calibration and independent review, not a new look).**

## 1. Executive Summary

This arc closes three open methodological and review duties in [`docs/POINT_REGISTER.md`](../../docs/POINT_REGISTER.md):
1. **`P-381` & `P-384` (Class-Choosing & Cross-Census Joint-Law Null Calibration):**
   We compute the exact non-parametric class-choosing null
   $$p_{\mathrm{class\text{-}choosing}}(\mathcal{M}; C_0) = \Pr_{y \sim \mathrm{null}}\!\left[\min_{C \in \mathcal{M}} p_C(y) \le p_{C_0}(\mathrm{PDG})\right]$$
   across $80\,000$ random hierarchies (seeds `1820..1839`) on the 266 low-order lines of `B1749` ($1 \le N \le 12$, 125 fresh apexes) and the 396 high-order lines of `B1755` ($N \in \{13, 14, 15, 20\}$, at the same 125 fresh apexes) under three natural class menus: prime divisibility ($\mathcal{M}_{\mathrm{prime}}$), exact order ($\mathcal{M}_{\mathrm{order}}$), and rational slope ($\mathcal{M}_{\mathrm{slope}}$), plus the two-stage (`B1749` train $\to$ `B1755` test) class-selection protocol and cross-census correlation analysis.
2. **`P-386` (Independent Non-Authoring Audit of the `P210` Package and October 24–26 Analytical Reductions on `origin/audit/physical-bridge-2026-09-05`):**
   We verify all 39 artifact SHA-256 bindings in `SPECIFICATION.json` and all 14 source-closure entries in `SOURCE_REVIEW_MANIFEST.json` at sealed commit `39ce620a82e5373d5f07eee91a6a7cbfd4cdd4f7`, inspect the 10 frozen `SymmetricResponseChecks` test methods in `verification_p210/checks.py` via static AST parsing without executing scientific modules (preserving prospective custody), and symbolically certify the Weyl norm derivative, unitary slot-involution grading transport, and Schur-complement mode-elimination kinetic metric identities across the six October 24–26 reduction notes (`65dd3c112`..`a506b1b15`).

---

## 2. Part 1 — Class-Choosing Null Calibration (`P-381`) and Cross-Census Joint Law (`P-384`)

### 2.1 In-Sample Class-Choosing Nulls on `B1749` ($1 \le N \le 12$) and `B1755` ($N \in \{13, 14, 15, 20\}$)

When a small class $C_0 \subset \text{lines}$ (such as $5 \mid N$, $N = 10$, or $\alpha = 2/5$) is selected after observing the census and evaluated against random hierarchies restricted to $C_0$ alone, its single-class null $p_{C_0}(\mathrm{PDG})$ scales down roughly with $|C_0| / |\text{lines}|$. Minimizing the within-class p-value $\min_{C \in \mathcal{M}} p_C(y)$ across the class menu $\mathcal{M}$ restores the look-elsewhere factor ($\mathrm{LEF} = p_{\mathrm{class\text{-}choosing}} / p_{C_0}$):

| Census | Class menu $\mathcal{M}$ | $|\mathcal{M}|$ | Named class $C_0$ ($|C_0|$) | $\min_{C_0}\chi^2_{\mathrm{six}}$ | Single-class null $p_{C_0}$ (hits / 80k) | Class-choosing null $p_{\mathrm{cc}}(C_0)$ (hits / 80k) | Inflation $\mathrm{LEF}$ | Class-choosing at best $C^*$ |
|---|---|---:|---|---:|---|---|---:|---|
| **`B1749`** ($N \le 12$) | `prime_divisibility` ($p \in \{2,3,5,7,11\}$) | 5 | $p = 5$ (48) | $3.5737$ | $0.0050\%$ (4) | **$0.0213\%$ (17)** | $4.25\times$ | $0.0213\%$ ($p=2,5$) |
| **`B1749`** ($N \le 12$) | `exact_order` ($N \in \{2..12\}$) | 11 | $N = 10$ (36) | $3.5737$ | $0.0038\%$ (3) | **$0.0413\%$ (33)** | $11.00\times$ | $0.0413\%$ ($N=10$) |
| **`B1749`** ($N \le 12$) | `slope_alpha` ($\min(a, -a \bmod 1)$) | 24 | $\alpha = 2/5$ (10) | $3.5737$ | $0.0025\%$ (2) | **$0.0600\%$ (48)** | $24.00\times$ | $0.0600\%$ ($\alpha=2/5$) |
| **`B1755`** ($13..20$) | `prime_divisibility` ($p \in \{2,3,5,7,13\}$) | 5 | $p = 5$ (240) | $5.3303$ | $0.1013\%$ (81) | **$0.3575\%$ (286)** | $3.53\times$ | $0.1325\%$ ($p=3$) |
| **`B1755`** ($13..20$) | `exact_order` ($N \in \{13,14,15,20\}$) | 4 | $N = 15$ (96) | $5.3303$ | $0.0363\%$ (29) | **$0.1413\%$ (113)** | $3.90\times$ | $0.1413\%$ ($N=15$) |
| **`B1755`** ($13..20$) | `slope_alpha` ($\min(a, -a \bmod 1)$) | 28 | $\alpha = 2/5$ (20) | $5.3303$ | $0.0163\%$ (13) | **$0.4488\%$ (359)** | $27.62\times$ | $0.4488\%$ ($\alpha=2/5$) |

### 2.2 Two-Stage (`B1749` Train $\to$ `B1755` Test) Null and Cross-Census Correlation (`P-384`)

1. **Two-stage train $\to$ test prime-class selection exceeds $0.1\%$:**
   When each random hierarchy $y$ selects its best prime-divisibility class $p^*(y) = \arg\min_{p \in \{2,3,5,7\}} p_{C_p^{\mathrm{train}}}(y)$ on `B1749` ($N \le 12$) and is then evaluated on the held-out `B1755` lines ($N \in \{13, 14, 15, 20\}$) in that chosen class $C_{p^*(y)}^{\mathrm{test}}$, the two-stage null is
   $$p_{\mathrm{two\text{-}stage}} = \Pr_y\!\left[p_{\mathrm{test}}(p^*_{\mathrm{train}}(y);\, y) \le p_{\mathrm{test}}(p=5;\, \mathrm{PDG})\right] = \frac{125}{80\,000} = 0.1563\% > 0.1\% \quad (\mathrm{LEF} = 1.54\times).$$
   Thus, on `B1755`, **every class-choosing null**—in-sample `prime_divisibility` ($0.3575\%$ at $p=5$, $0.1325\%$ at $p=3$), in-sample `exact_order` ($0.1413\%$), in-sample `slope_alpha` ($0.4488\%$), and two-stage `train -> test` ($0.1563\%$)—moves above the $0.1\%$ threshold.

2. **Strong cross-census correlation along $\alpha = 2/5$ ($r = 0.8953$):**
   Across the $80\,000$ random hierarchies, the minimum $\chi^2_{\mathrm{six}}$ on `B1749` ($N \le 12$) and on `B1755` ($N \in \{13, 14, 15, 20\}$) are strongly correlated because the order-15 and order-20 lines at $\alpha = 2/5$ sit at $|\Delta b| = 1/30$ and $1/20$ from the order-10 $T$-orbit of `B1749`:
   - $\mathrm{Corr}\bigl(\chi^2_{\mathrm{B1749}}[5 \mid N],\, \chi^2_{\mathrm{B1755}}[15+20]\bigr) = 0.7021$;
   - $\mathrm{Corr}\bigl(\chi^2_{\mathrm{B1749}}[N = 10],\, \chi^2_{\mathrm{B1755}}[15+20]\bigr) = 0.7274$;
   - $\mathrm{Corr}\bigl(\chi^2_{\mathrm{B1749}}[\alpha = 2/5],\, \chi^2_{\mathrm{B1755}}[\alpha = 2/5]\bigr) = 0.8953$.
   Consequently, while only $1.25\%$ of random hierarchies achieve $\chi^2_{\mathrm{six}} \le 16.75$ unconditionally on `B1755` (`15+20`), **$39.75\%$ of random hierarchies that achieve $\chi^2_{\mathrm{six}} \le 16.75$ on `B1749` ($5 \mid N$) also achieve $\chi^2_{\mathrm{six}} \le 16.75$ on `B1755` (`15+20`)** — a **$31.7\times$ conditional enhancement**.

3. **Look-ledger evaluation (`docs/LOOK_LEDGER.md`):**
   At look $m = 40$ (decisive) and $m = 71$ (broad), `THE_BAR` ($\alpha = 0.01$ family-wise, $95\%$ upper confidence limit $\le \alpha/m$) requires $\le 11$ hits out of $80\,000$ at $m = 40$ ($\le 5$ hits at $m = 71$). All three fresh-apex censuses exceed this bar (`B1749`: 16 hits; `B1753`: 36 hits; `B1755`: 78 hits) and remain `ungraded` under `THE_BAR`.

---

## 3. Part 2 — Independent Non-Authoring Audit of `P210` & October 24–26 Reductions (`P-386`)

### 3.1 Sealed `P210` Verification Package (`39ce620a82e5373d5f07eee91a6a7cbfd4cdd4f7`)

Following the five duties in `reports/physical_bridge_2026_09_05/word_architecture_audit_2026_10_17/verification_p210/EXECUTION_REVIEW_DUTIES.md`:
1. **Cryptographic Integrity:** Verified `SPECIFICATION.json` (`f33348144c91711b0bcc3a05cf62974aac28a468eb57181f1ea6dfc93077f948`), `DESIGN.md`, `ENVIRONMENT.json`, all **39 artifact SHA-256 digests**, and all **14 local source-closure digests** in `SOURCE_REVIEW_MANIFEST.json` (`6527684c1999398e25e98f59584f03f7e417ad0a4a7f728f8941b8f3052dbf4d`) directly from the git object database at `39ce620a82e5373d5f07eee91a6a7cbfd4cdd4f7`.
2. **Prospective Custody & Static AST Inspection:** Inspected `verification_p210/checks.py` (`70d441f672228f6bbf9bb22e869a3575e6082d3002c7be044ad1c15c642b5a58`) and `run_checks.py` without importing or executing scientific modules. Confirmed that `SymmetricResponseChecks` defines the exact 10 frozen test methods (`test_all_216_registered_states_and_scalar_extremes`, `test_complete_exterior_l2_kernel_and_decay_rate`, `test_covariant_end_domain_conjugation`, `test_joined_fredholm_index_and_kernel_matching`, `test_negative_controls_detect_corruptions`, `test_nonzero_spectral_parameter_gap_response`, `test_principal_part_and_green_transport`, `test_registered_coupling_transport_and_gram_preservation`, `test_symmetric_state_green_response_and_grading`, `test_threshold_gap_closing_and_singular_limits`) with non-vacuous positive and negative controls.
3. **Verdict on `P210` Package:** Concur with `review/INDEPENDENT_REVIEW_2026-10-24.md` (`APPROVE_EXECUTION` scoped strictly to the 10 frozen `SymmetricResponseChecks` methods once prospective admission is granted on a clean worktree).

### 3.2 Audit of the Eight October 24–26 Analytical Reduction Notes (`65dd3c112`..`926a26f59`)

We inspected and symbolically verified the core derivations of all eight analytical notes committed on `origin/audit/physical-bridge-2026-09-05` after the `P210` seal (up to head `926a26f59cf1427f9a1474adc4e938f0d8571eb1`):
1. **`ACTUAL_CUSP_WEYL_RESPONSE_AND_INDUCED_NORM.md` (`65dd3c112`, unreviewed in `REVIEW.json`):**
   - *Verified:* For $D = -i\sigma_1 \partial_t - \sigma_2 \otimes K$ ($K = K^\dagger$ invertible, $H = |K|$, $J = \mathrm{sign}(K)$), the unitary involution $a = P_+ x + P_- v$, $b = P_+ v + P_- x$ conjugates $D \mapsto -i\sigma_1 \partial_t - \sigma_2 \otimes H$ and transports the chirality grading $\Gamma_{\mathrm{old}} = \mathrm{diag}(I, -I) \mapsto \mathrm{diag}(J, -J)$. Thus $a(T)$ cannot be identified with the original $+$ chirality slot whenever $K$ has negative eigenvalues.
   - *Verified:* In the gap $|\lambda| < h_{\min}$, the $L^2([T,\infty))$ Weyl response $M(\lambda) = \lambda(H + Q(\lambda))^{-1}$ ($Q(\lambda) = \sqrt{H^2 - \lambda^2 I}$) obeys the exact Loewner/Weyl identity
     $$M'(\lambda) = \gamma(\lambda)^\dagger \gamma(\lambda) = \frac{I + M(\lambda)^2}{2Q(\lambda)} = \frac{H}{Q(\lambda)(H + Q(\lambda))} > 0, \qquad M(0) = 0, \qquad M'(0) = (2H)^{-1},$$
     diverging at threshold $|\lambda| \to h^-$ and as $h \to 0^+$.
2. **`HODGE_GEOMETRY_REDUCTION_AND_FIBRE_MAP.md` (`ba6e0d943`, Oct 26):**
   - *Verified:* Correctly separates the derived complex-analytic/Hodge structure on $E_\tau$ (where fibre translations shift the flat line holonomy $(\alpha, \beta)$ without altering the base modulus $\tau$ or the $(1,0)\oplus(0,1)$ polarization) from the unpaid physical dictionary (mapping the $U(1)_Y$ hypercharge $6Y$ and $SU(3)_C \times SU(2)_L$ quantum numbers onto the fibre holonomy).
3. **`FULL_MODE_ELIMINATION_AND_INDUCED_KINETIC_METRIC.md` (`9d150df6b`, Oct 26):**
   - *Verified:* For $S(\lambda) = (A_{00} - \lambda G_{00}) - (A_{0\perp} - \lambda G_{0\perp})(A_{\perp\perp} - \lambda G_{\perp\perp})^{-1}(A_{\perp 0} - \lambda G_{\perp 0})$, symbolic differentiation at $\lambda = 0$ yields the exact dressed kinetic metric $-\left.\frac{dS}{d\lambda}\right|_{\lambda=0} = \Pi_0^\dagger G \Pi_0$ with $\Pi_0 = \begin{pmatrix} I \\ -A_{\perp\perp}^{-1} A_{\perp 0} \end{pmatrix}$. Eliminating heavy Kaluza-Klein/end modes therefore modifies the kinetic metric unless $A_{\perp 0} = 0$ and $G_{\perp 0} = 0$.
4. **`INTERACTING_DRESSED_DOMAIN_DEPENDENCE.md` (`e23eb793e`, Oct 26):**
   - *Verified:* While the Fredholm index is invariant under gap-preserving perturbations $V$, the kernel subspace $\ker(D_B + V)$ and its induced physical Yukawa couplings rotate continuously with $V$ whenever $V$ mixes opposite-sign boundary blocks.
5. **`BOUNDARY_REWRITE_VERSUS_FINITE_END_DYNAMICS.md` (`d49730597`, Oct 26) & `REDUCTION_FIRST_MISSION_2026_10_26.md` (`a506b1b15`, Oct 26):**
   - *Verified:* Cleanly distinguishes what discrete move-invariance on the boundary module $L_6$ can fix (invariant subspaces $0, V_2, V_4, L_6$ and topological indices) from what requires a continuous bulk/end operator (the finite regulator scale $L = \ln(1/\varepsilon)$ and finite norm constants $c_s(\tau, w)$).
6. **`END_AMPLITUDE_SELECTION_AND_SEWING.md` (`b43a81f2f`, Oct 26):**
   - *Verified via SymPy:* Endpoint additions $C_{\mathrm{out}} - C_{\mathrm{in}}$ telescope and cancel on artificial seams, whereas at a true end, adding the finite term $\eta I_0$ ($e = \eta \nu R/\pi$) to the leading-divergence-subtracted root energy $E_\eta = (\pi/R^2)\bigl[x(3x-1)/(1-x)^3 + e x\bigr]$ ($x = 4\lambda^2 R \in (0, 1)$) gives
     $$\frac{R^2}{\pi}\frac{dE_\eta}{dx} = g(x) + e, \qquad g(x) = \frac{3x^2 + 4x - 1}{(1-x)^4}, \qquad g'(x) = \frac{6x(x+3)}{(1-x)^5} > 0 \text{ on } (0, 1),$$
     with $g((\sqrt{7}-2)/3) = 0$, $g(1/4) = 16/27$, and $g(1/2) = 28$. Thus any $x_0 \in (0, 1)$ can be made the unique restricted minimum by choosing $e = -g(x_0)$.
7. **`QUATERNION_ORBIFOLD_DOMAIN_AND_METRIC_PRICE.md` & `QUATERNION_ORBIFOLD_SOURCE_CUSTODY_2026_10_26.json` (`926a26f59`, Oct 26):**
   - *Verified via SymPy & SHA-256:* Verified all 9 source-custody hashes and the author-note hash (`d91a77e6...`). Certified that in the upstairs chart $w = x + iy$, $s = 1 - k|w|^2$ ($k = 4\lambda^2$) on the genus-3 $Q_8$ cover $Y \to E_\tau$, the local non-commuting core $A = \frac{ik(-y\,dx + x\,dy)}{s}H$ ($A_{\bar{w}} = -\frac{kw}{2s}H$), $Q_w = \frac{4\lambda}{s}E_+$ satisfies the exact reduced-Yang-Mills BPS equations $\bar{D}_A Q_w = \partial_{\bar{w}}Q_w + [A_{\bar{w}}, Q_w] = 0$ and $F_{xy} - \frac{i}{2}[Q_w, Q_w^\dagger] = \frac{2ik}{s^2}H - \frac{i}{2}\frac{16\lambda^2}{s^2}H = 0$ with smooth fields at $w = 0$, while explicitly pricing the cone-angle-$\pi$ downstairs metric $h(\sqrt{z})|dz|^2/(4|z|)$ and the $\mathrm{Spin}^c$/$R$-charge lift.

## Files

- `verification/class_choosing_and_p210_audit.py` → `verification/class_choosing_and_p210_audit.json`, `verification/class_choosing_and_p210_audit_run.txt`
- `tests/test_b1760_class_choosing_null_and_p210_review.py`
