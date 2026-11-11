# Pre-Registration Plan — Phase 4: 1-Loop Vacuum Selection, 4D $dP_9$ Cusp-Cap Gluing & Quark–Lepton PMNS Unification Engine

## 0. Scope, Clean-Room Firewall, and Non-Negotiable Guardrails
- **Clean-Room Isolation:** Phase 4 is built in an isolated directory (`unification_cap_lepton_phase4`) with zero modifications to Phase 1 (`self_consistent_loop_phi`), Phase 2 (`cusped_3d_loop_phase2`), or Phase 3 (`relational_yukawa_phase3`).
- **Empirical Data Firewall (`0 of 19`):** Zero experimental masses, gauge couplings, CKM/PMNS mixing angles, Jarlskog values, or cosmological parameters are imported anywhere in solver, referee, or test code.
- **All 6 Mathematical-Physics Guardrails (`user_global`):**
  1. **Anti-Texas-Sharpshooter (`Guardrail 1`):** Zero target coordinates ($\tau^*$, target mass ratios, target CKM/PMNS angles, or fitted weights) are embedded anywhere. All equations, calibration gates, falsification thresholds, and planted negative controls are locked in this file and sealed in `SEAL_SHA256.txt` before solver code is written.
  2. **No Literal Flag/Zero Proofs (`Guardrail 2`):** Every necklace classification, 3D isometry quotient, Fox/Reidemeister torsion determinant, Casimir sum, $dP_9$ intersection lattice check, trilinear/quartic 3D integral, singular-value hierarchy, and CKM/PMNS observable is computed directly from explicit matrices and hyperbolic simplices.
  3. **Mandatory Haar Unitary Basis-Scrambling (`Guardrail 3`):**
     - Quark sector $(Y_u, Y_d)$: tested under independent random Haar triples $(U_{L,q}, U_{R,u}, U_{R,d}) \in U(3)^3$ acting via $Y_u \to U_{L,q} Y_u U_{R,u}^\dagger,\; Y_d \to U_{L,q} Y_d U_{R,d}^\dagger$ (`< 1e-12`).
     - Lepton Weyl sector $(Y_e, Y_\nu, M_R)$ and Weinberg $M_\nu^{\text{W}}$: tested under independent random Haar triples $(U_{L,\ell}, U_{e^c}, U_N) \in U(3)^3$ acting via $Y_e \to U_{L,\ell} Y_e U_{e^c}^\dagger$, $Y_\nu \to U_{L,\ell} Y_\nu U_N^\dagger$, $M_R \to U_N^* M_R U_N^\dagger$, $M_\nu \to U_{L,\ell} M_\nu U_{L,\ell}^T$ (`< 1e-12`).
     - Physical mixing is never extracted from left-right overlap $V_f^T U_f$ of a single matrix.
  4. **Benchmark Calibration Gate (`Guardrail 4`):** All tetrahedral quadrature rules (covering both degree-3 Yukawa and degree-4 Weinberg P1 integrands), Fox–Wada Reidemeister torsion determinants, and Haar-invariant PMNS/seesaw extractors must pass analytical textbook benchmarks (`< 1e-12`) before evaluating candidate histories.
  5. **Strict Non-Dimensionalization (`Guardrail 5`):** Zero dimensionful scales are imported; all geometric quantities are in $K = -1$ hyperbolic units and all mass/Yukawa outputs are dimensionless ratios.
  6. **Zero-Trust Referee (`Guardrail 6`):** The independent referee script (`referee_phase4.py`) is AST-verified to contain **zero** imports from `phase4_loop`, `relational_loop`, `cusped_loop`, `phi_loop`, or `src`, and independently verifies every gate using distinct quadrature rules, 50-digit `mpmath` Fox/Reidemeister determinants, independent $dP_9$ lattice construction, and 25 fresh adversarial Haar $U(3)^3$ trials on both CKM and PMNS.

---

## 1. Textbook Calibration Gate (`calibration_gate.py`)
Before evaluating candidate histories in Gates 1–3, verify to `< 1e-12`:
1. **Degree-4 Weinberg & Degree-3 Yukawa Simplex Quadrature + Epstein–Penner Volume:**
   - Verify that the positive-weight $S_4$-symmetric 14-point degree-5 tetrahedral quadrature has strictly positive weights summing to $1/6$ and integrates all reference 3-simplex monomials $\lambda_0^a \lambda_1^b \lambda_2^c \lambda_3^d$ ($a+b+c+d \le 5$, covering both cubic P1 Yukawa and quartic P1 Weinberg $(L_L H_u)^2$ integrands) to `< 1e-15`.
   - Verify Epstein–Penner 24-cone volume on `m004` (`b++LR`) and its sister `m003` (`b+-LR`) against exact Mostow volume $2.029883212819307$ (`< 1e-12`).
2. **Exact Textbook Alexander–Wada–Reidemeister Torsion Benchmark:**
   - Implement exact Fox free-differential calculus on $\pi_1(M)$ presentations and verify Wada column-swap invariance (`< 1e-14`).
   - Verify on the figure-eight knot complement `m004` (`b++LR`, $H_1 = \mathbb{Z}$) at $\theta = 2\pi q / 5$ ($q = 1, 2$) that the Fox Alexander numerator $|\Delta_{4_1}(e^{i\theta})|$ matches $|3 - 2\cos\theta| = \frac{7 \mp \sqrt{5}}{2}$ and $\tau_{\text{Reid}}(m004, \rho_\theta) = \frac{|3 - 2\cos\theta|}{2|\sin(\theta/2)|}$ to `< 1e-13`, and on its sister `m003` (`b+-LR`, $H_1 = \mathbb{Z}/5\mathbb{Z} \oplus \mathbb{Z}$) matches $|3 + 2\cos\theta| = \frac{5 \pm \sqrt{5}}{2}$ to `< 1e-13`.
3. **PMNS Seesaw & Weinberg Haar Basis-Scrambling Calibration (`Guardrail 3`):**
   - For two-component Weyl leptons $\mathcal{L}_{\text{lep}} = L^T Y_e e^c H_d + L^T Y_\nu N^c H_u + \frac{1}{2}(N^c)^T M_R N^c$ ($M_\nu = -Y_\nu M_R^{-1} Y_\nu^T$, $H_e = Y_e Y_e^\dagger$, $H_\nu = M_\nu M_\nu^\dagger$), verify across 20 random Haar triples $(U_L, U_{e^c}, U_N) \in U(3)^3$ on both a complex CP-violating benchmark and a real CP-conserving control that charged-lepton and light-neutrino singular-value ratios, $|U_{\text{PMNS}}|$, PDG-convention mixing angles $(\sin^2\theta_{12}^\ell, \sin^2\theta_{23}^\ell, \sin^2\theta_{13}^\ell)$, and $\hat{\mathcal{J}}_{\text{PMNS}} = \operatorname{Im}\det[H_e, H_\nu] / (\|H_e\|_F^3 \|H_\nu\|_F^3)$ are invariant to `< 1e-12`.

---

## 2. Gate 1: Exhaustive Necklace Census ($2 \le |W| \le 12$), 1-Loop Buckling vs. Relational `A-all` Ensemble (`gate1_vacuum_selection.py`)
Resolves the reversible vs. chiral-irreversible vacuum selection test without restricted word prefixes or tuned weights:
1. **Unrestricted Primitive Necklace Census ($2 \le |W| \le 12$):**
   - Enumerate all primitive cyclic words $W \in \{L, R\}^*$ ($2 \le |W| \le 12$, containing both `L` and `R`) admitting a cyclic representative preserving the Golden $\mathbb{Z}/5\mathbb{Z}$ eigenvector line $v_5 = (1, 2)^T$ ($M_W^T v_5 \equiv \pm v_5 \pmod 5$, setting `b++` for $+1$ and `b+-` for $-1$).
   - Group into exact 3D orientation-preserving isometry classes $\mathcal{M}_{\le 12} / \operatorname{Isom}_+$ and relational weak-compass mirror classes $\mathcal{M}_{\le 12} / \operatorname{Isom}_\pm$ (preventing redundant double-counting of isometric presentations such as $W$ vs. $W_{\text{rev}}$), and also track the Golden-departure sub-family (`...LR` non-cover departures).
   - Classify each relational class $[M]$ into `amphicheiral`, `chiral_reversible` ($\operatorname{Sym}(M)$ contains anti-unitary/palindrome involution $\iota_1$), or `chiral_irreversible` ($\operatorname{Sym}(M) \cong \mathbb{Z}/2\mathbb{Z}$ or trivial, no orientation-preserving reflection), identifying the **exact global minimal-volume chiral irreversible 3-manifold** across $|W| \le 12$ (`[b+-LLLLLRLLRR]_rel` in full census, `[b++LLLLLLLRRLLR]_rel` in orientable-fiber `b++`, alongside `[b++LLLLLRLLRRLR]_rel` in `...LR` departures).
2. **Test 1A — `A-one` Classical Volume vs. Unrigged 1-Loop Quantum Contributions:**
   - Compare `k = 0` (cusp-unramified) vs. `k != 0` (cusp-ramified) $\mathbb{Z}/5\mathbb{Z}$ torsion lines via exact Fox–Wada Reidemeister torsion $\tau_{\text{Reid}}(M_W, \rho_k)$ (testing acyclicity $H^*(M_W; \mathbb{C}_{\rho_k}) = 0$ vs. harmonic zero-mode obstruction $\tau_{\text{Reid}} = 0$).
   - Across the minimal reversible vs. minimal chiral irreversible classes, evaluate:
     1. Classical hyperbolic volume $\operatorname{Vol}(M_W)$,
     2. Exact 1-loop Reidemeister free energy $-\ln\tau_{\text{Reid}}(M_W, \rho)$ (both Golden fiber-twisted $\rho_k$ and base-circle character $\rho_{0,q}$),
     3. UV-subtracted twisted 3D Casimir zero-point sum $\Delta E_{\text{Casimir}}^{\text{twist}}(K_{\text{IR}}) = \sum_{n=1}^{K_{\text{IR}}} (\sqrt{\lambda_n^{(q)}} - \sqrt{\lambda_n^{(0)}})$ across $N_{\text{sub}} \in \{3, 4\}$, and
     4. Dimensionless 1-loop Coleman–Weinberg Yukawa quartic trace $-\operatorname{Tr}[(Y_u Y_u^\dagger)^2 + (Y_d Y_d^\dagger)^2]$.
   - **Pre-Registered Falsifier:** Report transparently without fitted couplings whether parameter-free 1-loop terms select `k != 0` over `k = 0` and whether they overturn $\Delta\operatorname{Vol} > 0$ between minimal reversible and minimal chiral irreversible classes in `A-one`.
3. **Test 1B — Deduplicated Relational `A-all` Partition Sum over $\mathcal{M}_{\le 12} / \operatorname{Isom}_\pm$:**
   - Evaluate both pure-volume $w_{[M]} \propto \frac{1}{|\operatorname{Sym}_+(M)|} e^{-\operatorname{Vol}(M)}$ (and unweighted $e^{-\operatorname{Vol}(M)}$) and 1-loop torsion-weighted ensembles across the deduplicated relational classes, extracting $\langle\tau_{\text{cusp,rel}}\rangle$ and net relational Jarlskog $\langle \sigma_P \hat{\mathcal{J}}_{\text{CKM}} \rangle$ over all low-volume classes ($\operatorname{Vol} \le 9.2$) to test whether exponentially suppressed chiral irreversible throats generate non-zero net CP violation in `A-all`.

---

## 3. Gate 2: 4D $dP_9$ Cusp-Cap Gluing & Mod-5 Ramification Audit (`gate2_dp9_cusp_cap.py`)
Tests rigorously what plugging the 3D cusp into a 4D rational elliptic surface cap ($dP_9 = \frac{1}{2}K3$) forces vs. what remains a boundary choice:
1. **Explicit Unimodular $dP_9$ Lattice $\mathbf{I}_{1,9}$ & $E_8(-1)$ Mordell–Weil Verification:**
   - Construct $H_2(dP_9; \mathbb{Z}) = \mathbb{Z} H \oplus \bigoplus_{i=1}^9 \mathbb{Z} E_i$ ($H^2 = 1$, $E_i \cdot E_j = -\delta_{ij}$), fiber $F = 3H - \sum_{i=1}^9 E_i$ ($F^2 = 0$), section $\Sigma_0 = E_9$ ($\Sigma_0^2 = -1, \Sigma_0 \cdot F = 1$), and verify that $\{F, \Sigma_0\}^\perp$ is isometric to $E_8(-1)$ ($\det = 1$, all 240 norm-$-2$ roots).
   - Verify $\chi(dP_9) = c_2(T_{dP_9}) = 12$ and symmetric $E_8 \times E_8$ Bianchi split $c_2(V_{\text{vis}}) = c_2(V_{\text{hid}}) = 6 = \frac{3(3+1)}{2} = k_{\text{inst},\min}(3)$.
2. **Peripheral Holonomy, ’t Hooft Congruence & FMW Spectral-Cover Audit:**
   - Evaluate both:
     1. Non-abelian $PSU(5)_\perp$ ’t Hooft central flux congruence $c_2(V_\perp) \equiv -\frac{k_{\mathfrak{m}} k_{\mathfrak{l}}}{5} \pmod 1$ at $c_2(V_\perp) = 6 \in \mathbb{Z}$ (checking compatibility with single-cycle peripheral holonomy $(0, k)$ for $k \in \{1..4\}$ vs. $(0, 0)$), and
     2. Friedman–Morgan–Witten 5-sheeted spectral curve $C \in |5\Sigma_0 + 6 F|$ on $dP_9$ ($g(C) = 16$, Riemann–Hurwitz ramification degree $R = 40$, reduced 4-sheet intersection $C_4 \cdot \Sigma_0 = 6 - 4 = 2$).
   - **Pre-Registered Falsifier:** State honestly whether integer bulk $c_2(V_\perp) = 6$ alone forbids `k = 0` at a generic smooth boundary fiber $F_\infty$ (it does not if all branch/instanton loci lie inside $dP_9 \setminus D^2_\infty$) vs. what boundary/acyclicity condition (`F_\infty` at a spectral branch/cusp fiber or 3D Reidemeister acyclicity $\tau_{\text{Reid}} \ne 0$) forces `k != 0`.

---

## 4. Gate 3: Parameter-Free Quark-vs.-Lepton Acid Test (`gate3_quark_lepton_unification.py`)
Tests whether the **same** 3D hyperbolic geometry produces **small CKM quark mixing** and **large PMNS lepton mixing** with `0 of 19` empirical inputs:
1. **Unique $\mathbb{Z}/5\mathbb{Z}$ Gauge-Invariant $E_8 \supset \mathfrak{su}(5)_{\text{GUT}} \oplus \mathfrak{su}(5)_\perp$ Lepton Couplings:**
   - With $\mathbf{10}_{\text{GUT}}$ ($Q_L, u_R^c, e_R^c$) in $q = +1$, $\overline{\mathbf{5}}_{\text{GUT}}$ ($d_R^c, L_L$) in $q = +2$, $H_u$ in $q = -2$, and $H_d$ in $q = +2$:
     1. **Charged-Lepton Lopsided Transpose Identity:** $Y_e = Y_d^T$ (left-handed $Q_L$ lives in $q = +1$ aligned with $Y_u = Y_u^T$, whereas left-handed $L_L$ lives in $q = +2$!).
     2. **Unique Right-Handed Neutrino Charge:** Verify exhaustively across $q \in \mathbb{Z}/5\mathbb{Z}$ that $q(N^c) \equiv 0 \pmod 5$ is the **unique** charge satisfying both Dirac invariance $(+2) + q(N^c) + (-2) \equiv 0 \pmod 5$ and Majorana invariance $2 q(N^c) \equiv 0 \pmod 5$.
2. **Dual Parameter-Free Neutrino Mechanisms ($N_{\text{sub}} \in \{3, 4, 5\}$):**
   Evaluate across amphicheiral controls (`b+-LR`, `(5,5)`), reversible classes (`[b++LLLRLL]_rel`, `[(6)]_rel`, `[3,1,3]`), and chiral irreversible classes (`[b+-LLLLLRLLRR]_rel`, `[b++LLLLLLLRRLLR]_rel`, `[[5,1,2,2]]_rel`) under cusp-ramified (`k != 0`, Dirichlet) bundles:
   - **Mechanism N1 (3D KK Singlet Seesaw):** Using the lowest 3 non-constant $q = 0$ Laplace–Beltrami modes $\{\eta_0^{(n)}\}_{n=1}^3$ ($\Delta_0 \eta_0^{(n)} = \lambda_{0,n} \eta_0^{(n)}$):
     $$(Y_\nu)_{an} = \int_{M_H} \sqrt{\det g}\, \chi_{+2}^{(a)}(x)\, \eta_0^{(n)}(x)\, \phi_{-2}^{(0)}(x)\, d^3x,$$
     $$(M_R)_{mn} = \frac{\sqrt{\lambda_{0,m}} + \sqrt{\lambda_{0,n}}}{2} \int_{M_H} \sqrt{\det g}\, \eta_0^{(m)}(x)\, \eta_0^{(n)}(x)\, d^3x, \qquad M_\nu^{\text{KK}} = -Y_\nu M_R^{-1} Y_\nu^T.$$
   - **Mechanism N2 (Exact Degree-4 Contact Weinberg Integral):**
     $$(M_\nu^{\text{W}})_{ab} = \int_{M_H} \sqrt{\det g}\, \chi_{+2}^{(a)}(x)\, \chi_{+2}^{(b)}(x)\, \bigl(\phi_{-2}^{(0)}(x)\bigr)^2\, d^3x.$$
3. **Acid-Test Observable Extraction & Guardrail Verification:**
   - Extract quark and lepton mass ratios, $|V_{\text{CKM}}|$ vs. $|U_{\text{PMNS}}|$, standard PDG-convention $(\sin^2\theta_{12}, \sin^2\theta_{23}, \sin^2\theta_{13})$ in both sectors, and $(\hat{\mathcal{J}}_{\text{CKM}}, \hat{\mathcal{J}}_{\text{PMNS}})$.
   - Verify Haar $U(3)^3$ scrambling invariance (`< 1e-12`), bilinear eigensolver-phase invariance of $M_\nu^{\text{KK}}$ (`< 1e-14`), enantiomer relational collapse (`< 1e-13`), amphicheiral/reversible CP vanishing (`< 1e-12`), and test directly whether $\sin^2\theta_{12}^\ell > \sin^2\theta_{12}^q$ and $\sin^2\theta_{23}^\ell > \sin^2\theta_{23}^q$ without tuning.
