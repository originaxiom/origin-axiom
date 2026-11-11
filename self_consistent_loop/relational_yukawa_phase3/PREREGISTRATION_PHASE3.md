# Pre-Registration Plan — Phase 3: Relational Quotient, Spin-Flux Throat, 3D Hyperbolic Yukawa Overlaps & Topological Tadpole Audit

## 0. Scope, Clean-Room Firewall, and Non-Negotiable Guardrails
- **Workspace:** `/Users/dri/.gemini/antigravity/scratch/relational_yukawa_phase3` (clean-room Phase 3 directory; zero modifications to `origin-axiom*`, Phase 1 `self_consistent_loop_phi`, or Phase 2 `cusped_3d_loop_phase2`).
- **Empirical Data Firewall (`0 of 19`):** Zero experimental masses, couplings, CKM/PMNS mixing angles, Jarlskog values, or cosmological parameters are imported anywhere in `src/`, `scripts/`, or `tests/`.
- **All 6 Mathematical-Physics Guardrails (`user_global`):**
  1. **Anti-Texas-Sharpshooter (`Guardrail 1`):** Zero target coordinates ($\tau^*$, target mass ratios, target CKM angles, or rigged tadpole multipliers) are embedded anywhere. Every hypothesis and falsifier is locked by SHA-256 prior to solver implementation.
  2. **No Literal Flag/Zero Proofs (`Guardrail 2`):** Every quotient collapse, harmonic 1-form solve, spin-flux symmetry check, trilinear 3D Yukawa integral, singular-value hierarchy, Jarlskog determinant, and $E_8$ instanton sum is computed directly from explicit matrices/simplices (`< 1e-12` where algebraic/analytic, and multi-grid verified across $N_{\text{sub}} \in \{3, 4\}$).
  3. **Mandatory Haar Unitary Basis-Scrambling (`Guardrail 3`):** Every physical observable extracted from Yukawa pairs $(Y_u, Y_d)$ — dimensionless singular-value ratios $(s_1/s_3, s_2/s_3)$, matrix ranks, CKM mixing magnitudes $|V_{\text{CKM}}|$, and normalized Jarlskog invariant $\hat{\mathcal{J}} = \operatorname{Im}\det[H_u, H_d] / (\|H_u\|_F^3 \|H_d\|_F^3)$ where $H_f = Y_f Y_f^\dagger$ — is tested under independent random Haar unitary transformations $Y_u \to U_L Y_u U_{R,u}^\dagger,\; Y_d \to U_L Y_d U_{R,d}^\dagger$ ($U_L, U_{R,u}, U_{R,d} \in U(3)$) and asserted invariant to `< 1e-12`. Physical mixing is NEVER extracted from left-right overlap $V_f^T U_f$ of a single matrix.
  4. **Benchmark Calibration Gate (`Guardrail 4`):** All 3D trilinear quadrature rules, discrete Hodge harmonic 1-form solvers, $\mathbb{Z}/5\mathbb{Z}$ selection rules, and Haar-invariant CKM/Jarlskog extractors must pass exact analytical/cover benchmarks before evaluating candidate histories.
  5. **Strict Non-Dimensionalization (`Guardrail 5`):** Zero dimensionful scales imported; all volumes/lengths are in $K = -1$ hyperbolic units and all Yukawa outputs are dimensionless ratios.
  6. **Zero-Trust Referee (`Guardrail 6`):** `scripts/referee_relational_phase3.py` is AST-verified to contain **zero** imports from `relational_loop`, `cusped_loop`, `phi_loop`, or `src`, and independently rebuilds 5-fold cyclic cover triangulations, computes trilinear Yukawa overlaps with a distinct quadrature order (5-point degree-3 Keast vs. Producer's positive-weight 14-point degree-5 rule), verifies relational enantiomer collapse, and applies fresh adversarial Haar rotations.

---

## 1. Textbook Calibration Gate (`calibration_gate.py`)
Before evaluating candidate histories in Gates 1–4, verify to `< 1e-12`:
1. **Positive-Weight $S_4$-Symmetric 14-Point Degree-5 Tetrahedral Quadrature:**
   - Verify strictly positive weights summing to $1/6$, exact integration of all reference 3-simplex monomials $\lambda_0^a \lambda_1^b \lambda_2^c \lambda_3^d$ for $a+b+c+d \le 5$ (`< 1e-15`), and `m004` (`b++LR`, `b+-LR`) Epstein–Penner 24-cone volume matching Mostow volume $2.029883212819307$ (`< 1e-12`).
2. **Exact $\mathbb{Z}/5\mathbb{Z}$ Trilinear Charge-Conservation & 5-Fold Cover Equivalence on `b+-LR`:**
   - On SnapPy's 10-tetrahedron 5-cusp cyclic cover of `b+-LR`, verify that trilinear overlap integrals $\int_{\widetilde{M}} \sqrt{\det g}\, \tilde{\psi}_{q_a} \tilde{\psi}_{q_b} \tilde{\phi}_{q_c}\, d^3x$ vanish to `< 1e-13` whenever $q_a + q_b + q_c \not\equiv 0 \pmod 5$, and match $5 \times$ the 2-tetrahedron base-manifold twisted overlap when $q_a + q_b + q_c \equiv 0 \pmod 5$ (`< 1e-12`).
3. **Discrete Harmonic 1-Form Calibration (`\alpha_s = d\theta_s`):**
   - Construct the canonical free cohomology cocycle $n_f \in H^1_{\text{free}}(M; \mathbb{Z}) \cong \mathbb{Z}$ via integer Smith Normal Form, solve the discrete Poisson/Hodge jump equation $\Delta_g \theta_s = 0$ with face jumps $\theta_s^+ - \theta_s^- = n_f$, and verify discrete co-closure $d^\dagger \alpha_s = 0$ (`< 1e-12`) and exact unit loop holonomy $\oint_{S^1} \alpha_s = 1$ (`< 1e-12`).
4. **Analytical CKM & Jarlskog Haar-Invariance Calibration:**
   - On an analytical complex benchmark pair $(Y_u^{(0)}, Y_d^{(0)})$ with known non-zero $\hat{\mathcal{J}} \ne 0$ and on a real CP-conserving control ($\hat{\mathcal{J}} = 0$), verify invariance of singular-value ratios, $|V_{\text{CKM}}|$, and $\hat{\mathcal{J}}$ across $20$ independent random Haar unitary triples $(U_L, U_{R,u}, U_{R,d}) \in U(3)^3$ to `< 1e-12`.

---

## 2. Gate 1: Relational Weak-Compass Quotient (`gate1_relational_quotient.py`)
**Core Hypothesis:** Anchoring observables to the active light weak boson ($\sigma_P(M_W) := -\operatorname{sgn}(\sin 4\pi\operatorname{CS}(M_W))$ when $|\sin 4\pi\operatorname{CS}| > 10^{-10}$, else $0$) collapses the external 1-bit mirror tie $W \leftrightarrow W_{\text{mirror}} = L \overline{W} L^{-1}$ with zero empirical inputs:
$$\tau_{\text{rel}}(M_W) := \bigl(\sigma_P(M_W)\operatorname{Re}\tau_{\mathcal{F}}(M_W)\bigr) + i\operatorname{Im}\tau_{\mathcal{F}}(M_W), \qquad \Delta m^2_{\text{weak,rel}}(M_W) := m^2(W_{\text{heavy}}) - m^2(W_{\text{active}}).$$

**Pre-Registered Tests:**
1. Verify across every chiral enantiomer pair $(W, W_{\text{mirror}})$ in the Fibonacci-mirror closure of `A6` (plus the irreversible pair `[5,1,2,2]` / `[2,2,1,5]` at `sum = 10`) that $|\tau_{\text{cusp,rel}}(M_W) - \tau_{\text{cusp,rel}}(M_{W_{\text{mirror}}})| < 10^{-12}$, $|\tau_{\text{tube,rel}}(M_W) - \tau_{\text{tube,rel}}(M_{W_{\text{mirror}}})| < 10^{-12}$, and $|\Delta m^2_{\text{weak,rel}}(M_W) - \Delta m^2_{\text{weak,rel}}(M_{W_{\text{mirror}}})| < 10^{-12}$.
2. Verify that in the quotient space $\mathcal{M} / \mathbb{Z}_2^{\text{mirror}}$, `A-one` (minimal hyperbolic volume among non-cover departures) has **exact winner count = `1`** (`[(6)]_rel` at $\operatorname{Vol} = 5.58636161$), and `A-all` Boltzmann expectation yields non-zero relational CP phase $\langle \operatorname{Re}\tau_{\text{cusp,rel}} \rangle_{e^{-\operatorname{Vol}}} \ne 0$ and non-zero relational weak splitting.
3. **Planted Amphicheiral Negative Controls (`b+-LR` and `(5, 5)` `b+-LLLLLRRRRRLR`):** Verify $\sigma_P = 0$, $\operatorname{Re}\tau_{\text{cusp,rel}} = 0$, and $\Delta m^2_{\text{weak,rel}} = 0$ (`< 1e-12`).

---

## 3. Gate 2: Coupled Spin-Flux Throat & Klein-Four Palindrome Protection (`gate2_coupled_spin_flux_throat.py`)
**Core Question (Test A):** Does coupling an intrinsic 2-component spinor + harmonic magnetic flux / base-circle connection $\alpha_s = d\theta_s$ to the 3D hyperbolic $\mathbb{Z}/5\mathbb{Z}$-twisted throat break `(6)`'s symmetric two-shoulder profile `[0, 6]`, or does `(6)`'s Klein-four isometry group $\operatorname{Sym}(\text{`b++LLLLLLRLR`}) \cong \mathbb{Z}_2 \times \mathbb{Z}_2 = \{\text{id}, \sigma_{\text{hyp}}, \iota_1, \iota_2\}$ protect $P_t = P_{6-t}$ ($t=0..6$), $P_7 = P_8$ via the anti-unitary involution $\tilde{\iota}_1 = \Theta \circ U_{\text{spin}}(\iota_1)$?

**Pre-Registered Tests:**
1. Solve the discrete harmonic 1-form $\alpha_s = d\theta_s$ (`\oint_{S^1}\alpha_s = 1`) and assemble the coupled 2-component spin-flux operator (combining minimal $U(1)_{\text{base}}$ harmonic connection $-i 2\pi \Phi_{\text{base}} \alpha_s$, flat $\mathbb{Z}/5\mathbb{Z}$ cocycle, and intrinsic Pauli–Zeeman magnetic coupling $-\mu_B (\sigma_3 \|\alpha_s\|_g + \sigma_1 \mathcal{A}_{\text{throat}})$ covariant under local geometry) across:
   - Palindromic minimal-volume `(6)` (`b++LLLLLLRLR`, `Sym = Z/2 x Z/2`),
   - Reversible single-peak `[3, 1, 3]` (`b++LLLRLLLRLR`, `Sym = Z/2 x Z/2`) and `[2, 1, 1, 1, 2]` (`b+-LLRLRLLRLR`, `Sym = D4`),
   - Irreversible chiral pair `[5, 1, 2, 2]` (`b++LLLLLRLLRRLR`, `Sym = Z/2`) and `[2, 2, 1, 5]` (`b++LLRRLRRRRRLR`, `Sym = Z/2`).
2. Test directly from ground-state spinor layer probabilities $P_t = \int_{\Delta_t} \sqrt{\det g}\, (\|\psi_\uparrow\|^2 + \|\psi_\downarrow\|^2)\, d^3x$ whether covariant harmonic-flux + Pauli spin coupling leaves $P_0 = P_6$ and $P_7 = P_8$ exact (`< 1e-12`) on `(6)` (confirming the Klein-Four Palindrome Protection Theorem) while breaking forward/backward reflection on irreversible `[5, 1, 2, 2]`.

---

## 4. Gate 3: 3D Hyperbolic Yukawa Overlaps, Mass Ranks & Jarlskog CP Audit (`gate3_3d_yukawa_overlap.py`)
**Core Question (Tests B & C):** Using the exact $E_8 \supset \mathfrak{su}(5)_{\text{GUT}} \oplus \mathfrak{su}(5)_\perp$ $\mathbb{Z}/5\mathbb{Z}$-invariant trilinear couplings:
$$(Y_u)_{ab} = \int_{M_H} \sqrt{\det g(x)}\, \psi_{+1}^{(a)}(x)\, \psi_{+1}^{(b)}(x)\, \phi_{-2}^{(0)}(x)\, d^3x \quad ((+1)+(+1)+(-2) \equiv 0 \pmod 5),$$
$$(Y_d)_{ab} = \int_{M_H} \sqrt{\det g(x)}\, \psi_{+1}^{(a)}(x)\, \chi_{+2}^{(b)}(x)\, \phi_{+2}^{(0)}(x)\, d^3x \quad ((+1)+(+2)+(+2) \equiv 0 \pmod 5),$$
where $\{\psi_{+1}^{(a)}\}_{a=0}^2$ and $\{\chi_{+2}^{(b)}\}_{b=0}^2$ are the lowest 3 orthonormal 3D hyperbolic eigenstates in charges $q = +1$ and $q = +2$, and $\phi_{\mp 2}^{(0)} = (\phi_{\pm 2}^{(0)})^*$ is the ground-state Higgs conjugate pair:
1. Evaluate **both** the **cusp-unramified** ($k = 0$) and **cusp-ramified** ($k \not\equiv 0 \pmod 5$, Dirichlet cusp BC) $\mathbb{Z}/5\mathbb{Z}$ torsion bundles across:
   - Amphicheiral negative controls `b+-LR` and `(5, 5)` (`b+-LLLLLRRRRRLR`),
   - Minimal-volume palindromic pair `(6)` (`b++LLLLLLRLR`) and `(1, 6)` (`b++LRRRRRRLR`),
   - Single-peak reversible histories `[3, 1, 3]` (`b++LLLRLLLRLR`), `[1, 2, 2, 2]` (`b+-LRRLLRRLR`), and `[2, 1, 1, 1, 2]` (`b+-LLRLRLLRLR`),
   - Minimal-volume chiral irreversible pair `[5, 1, 2, 2]` (`b++LLLLLRLLRRLR`, `Sym = Z/2`) and `[2, 2, 1, 5]` (`b++LLRRLRRRRRLR`, `Sym = Z/2`),
   across mesh resolutions $N_{\text{sub}} \in \{3, 4\}$.
2. Extract strictly basis-invariant observables (verified invariant under random Haar $U(3)^3$ rotations to `< 1e-12` and independent of arbitrary eigensolver phases when $E_0 < E_1 < E_2$):
   - Eigenvalue gap audit $\min((E_1-E_0)/E_0, (E_2-E_1)/E_1)$ in $q=+1, +2$ (checking whether any candidate suffers subspace degeneracy);
   - Dimensionless Yukawa singular-value hierarchies $(s_{u,1}/s_{u,3}, s_{u,2}/s_{u,3})$ and $(s_{d,1}/s_{d,3}, s_{d,2}/s_{d,3})$, testing whether `(6)` has 3 distinct non-zero singular values (`rank = 3`, $s_1 < s_2 < s_3$) or hits a palindromic mass degeneracy ($s_1 = s_2$ or $s_1 = 0$);
   - CKM mixing matrix magnitudes $|V_{\text{CKM}}| = |U_{L,u}^\dagger U_{L,d}|$ and off-diagonal Cabibbo-like hierarchy $|V_{01}|, |V_{12}|, |V_{02}|$;
   - Basis-invariant normalized Jarlskog CP determinant $\hat{\mathcal{J}} = \operatorname{Im}\det[H_u, H_d] / (\|H_u\|_F^3 \|H_d\|_F^3)$, testing our exact **Hyperelliptic vs. Palindromic CP Theorem**:
     - Under cusp-unramified ($k = 0$) pure torsion, $\tilde{\sigma}_{\text{hyp}}$ forces $\hat{\mathcal{J}} = 0$ (`< 1e-12`) across **all** punctured-torus bundles;
     - Under cusp-ramified ($k \ne 0$) torsion + cusp holonomy, reversible histories (`Sym` containing $\iota_1$, including `(6)`, `[3,1,3]`, `[1,2,2,2]`, `[2,1,1,1,2]`) **still** have $\hat{\mathcal{J}} = 0$ protected by $\tilde{\iota}_1$, whereas **irreversible chiral histories (`[5,1,2,2]` and `[2,2,1,5]`, `Sym = Z/2`) break all anti-unitary involutions and generate non-zero $\hat{\mathcal{J}} \ne 0$**, with exact opposite signs on enantiomers ($\hat{\mathcal{J}}([5,1,2,2]) = -\hat{\mathcal{J}}([2,2,1,5])$) and **invariant relational Jarlskog $\sigma_P \cdot \hat{\mathcal{J}}$**!

---

## 5. Gate 4: Unrigged Topological Tadpole & Flux Quantization Audit (`gate4_topological_tadpole_audit.py`)
**Core Question:** Does any standard, unrigged topological anomaly / Bianchi / framing equation on the cusped 3-manifold force the 3-generation $E_8$ flux norm $\|H\|^2 = 12$ ($k_{\text{inst}} = 6$), or does pure 2D/3D topology fall short without a 4D cusp-cap boundary datum?

**Pre-Registered Tests:**
1. Verify directly across all $240$ explicit $E_8$ roots $\Phi(E_8)$ that for every $H \in \Lambda_R(E_8)$, the gauge instanton number $k_{\text{inst}}(H) := \frac{1}{120}\sum_{\alpha \in \Phi(E_8)} \langle\alpha, H\rangle^2 \equiv \frac{1}{2}\|H\|^2 \in \mathbb{Z}$ holds to `< 1e-13`, and determine by exhaustive enumeration up to $\|H\|^2 \le 24$ ($k_{\text{inst}} \le 12$) the exact minimal instanton threshold $k_{\text{inst},\min}(N_{\text{gen}})$ required for an $\mathfrak{su}(5)_{\text{GUT}}$-commuting $E_8$ coroot to achieve $|N_{\text{gen}}(\mathbf{10}_{\text{GUT}})| = N$ in a $\mathbb{Z}/5\mathbb{Z}$ slot for $N \in \{1, 2, 3, 4\}$.
2. Audit three unrigged topological quantization sources with zero adjustable multipliers:
   - **Rule T1 (2D Punctured-Fiber Euler Characteristic):** $k_{\text{inst}} = |\chi(\Sigma_{1,1})| = 1 \implies \max |N_{\text{gen}}|$.
   - **Rule T2 (3D Rademacher–Dedekind Monodromy Framing Defect):** $k_{\text{inst}} = |\Phi_{\text{Dedekind}}(W_H)| = |\#L - \#R|$ across `(6)` (`5`), `[3,1,3]` (`4`), `[5,1,2,2]` (`2`), etc., checking honestly which $|N_{\text{gen}}|$ values arise without multipliers.
   - **Rule T3 (4D Rational Elliptic Surface / Half-$K3$ Cusp-Cap Bianchi Identity):** $\sum_i k_{\text{inst}, i} = c_2(T_{dP_9}) = \chi(dP_9) = 12$ (symmetric visible/hidden or twin-cusp split $6 + 6 = 12$), reporting transparently what is forced by 3D topology alone vs. what requires 4D cusp-cap completion.
