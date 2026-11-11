# Pre-Registered Specification: Self-Consistent Fixed-Point Loop Engine (`Φ(X*) = X*`)

**Status:** SEALED PRIOR TO EXECUTION (`0 of 19` Data-Free Firewall)
**Project Root:** `/Users/dri/.gemini/antigravity/scratch/self_consistent_loop_phi`

---

## 0. Governing Rules & Zero-Cheat Guardrails

1. **Zero Empirical Data (`0 of 19`):** No measured physical constant ($18$ dimensionless SM parameters, neutrino masses, cosmological densities, or unit anchor) appears anywhere in the codebase, tests, or referee scripts.
2. **Guardrail 1 (No Post-Inspection Selection / No Embedded Targets):** No candidate coordinate ($\tau^*$, $N=5$, departure `(6)`, rank $r=8$) is embedded into a potential or filter by hand. Every output must emerge from solving equations defined uniformly over the declared candidate domain.
3. **Guardrail 2 (Ban Literal Flag/Zero Assignment):** Every structural boolean or residual (`is_self_dual`, `extends_bundle`, `is_unique_ground_state`, `mod_invariance_err`) is computed dynamically from explicit matrices/series and verified to `< 1e-12`.
4. **Guardrail 3 (Mandatory Unitary Basis-Scrambling Test):** Every physical observable extracted from mass/Yukawa or gauge-covariant blocks in Sector 4 must be invariant to `< 1e-12` under independent random Haar unitary transformations $U \in \operatorname{U}(d)$.
5. **Guardrail 5 (Non-Dimensionalization):** All spectra, potentials, and masses are expressed in dimensionless form (fixing at most 1 reference length/area scale where explicitly tracked as an open parameter).
6. **Guardrail 6 (Zero-Trust Independent Referee):** `scripts/referee_phi_loop.py` is AST-verified to import **zero** symbols from `src/phi_loop/`, independently constructing all root systems, Smith normal forms, ODE integrators, modular sums, and Lie-algebra commutants.

---

## 1. Declared Candidate Domains & Pre-Registered Thresholds

### Sector 1 (`BE-1`): Cusp Modular Sewing & Parent Algebra Closure (`X:PARENT` / `WP-1.8`)
- **Domain:** All irreducible crystallographic root systems across ranks $1 \le r \le 24$:
  - Classical families: $A_r$ ($1 \le r \le 24$), $B_r$ ($2 \le r \le 24$), $C_r$ ($3 \le r \le 24$), $D_r$ ($4 \le r \le 24$);
  - Exceptional families: $G_2$, $F_4$, $E_6$, $E_7$, $E_8$.
- **Metric Convention:** Symmetric Euclidean inner-product Gram matrix $G_{ij} = \langle \alpha_i, \alpha_j \rangle$ normalized so the shortest roots have minimal even norm $\langle \alpha_{\text{short}}, \alpha_{\text{short}} \rangle = 2$. (Explicitly contrasted against the asymmetric Cartan matrix $C_{ij} = 2\langle \alpha_i, \alpha_j\rangle / \langle \alpha_j, \alpha_j\rangle$.)
- **Closure Criterion (`(T, S)` Single-Channel Sewing):**
  1. $T$-invariance ($\tau \mapsto \tau + 1$ up to vacuum phase $e^{2\pi i r/24}$): evenness $G_{ii} \in 2\mathbb{Z}$ for all $i$, $G_{ij} \in \mathbb{Z}$;
  2. $S$-invariance ($\tau \mapsto -1/\tau$ without non-trivial discriminant channels $\Lambda_R^* / \Lambda_R$): $|\Lambda_R^* / \Lambda_R| = \det G = 1$, verified both algebraically via exact integer/rational determinant and analytically via numerical Poisson transformation of $\Theta_{\Lambda_R}(\tau)$ at generic $\tau \in \mathbb{H}$ to `< 1e-12`.
- **Downstream Consistency Check (`H1.2`):** On the selected algebra's explicit root system, construct the $D_5 \oplus A_3$ grading, verify the $h_4 = \frac{1}{2}(1,1,1,1,1; -1,-1,-1)$ filter and $X(-h_4) = \zeta_{\operatorname{Spin}(10)} X(+h_4)$ to `< 1e-12`, and verify the 3-branch $\langle L, R \rangle$ weave orbit $\{B_{(1,0)}, B_{(0,1)}, B_{(1,1)}\}$.

### Sector 2 (`BE-2`): Bundle-Extension & Twisted Eigenstate Loop (`P-761` / `P-744` Tests `A0`–`A6`, `T0`–`T4`)
- **Geometric Scope Statement (Explicit Non-Overclaiming):**
  - Exact 3-manifold topology & hyperbolic invariants (`H_1(M_W; \mathbb{Z})`, hyperbolic volume $\operatorname{Vol}_{\text{hyp}}(M_W)$, and systole length) are computed directly via `SnapPy` (`b++<word>`) on the true cusped hyperbolic 3-manifold $M_W^{\text{hyp}}$.
  - The eigenvalue/localization back-edge (`A1`–`A5`) is solved **analytically and spectrally to `< 1e-12`** on the unwrapped **Teichmüller/Sol geodesic flat-fibre bundle** $M_W^{\text{Sol}}$ (`ds^2 = dt^2 + A g_{\tau(t)}`, extending `B1857` from untwisted `(S1)` to the twisted fractional bundle `(T)`), plus a **punctured-fibre perturbation test** breaking continuous $\mathbb{T}^2$ translation invariance to the hyperelliptic involution $x \mapsto -x$. Solving the twisted Maass/Laplace–Beltrami PDE directly on the 3D cusped hyperbolic triangulation without $A$ remains explicitly tagged as open (`P-744`).
- **Declared Backgrounds (`T4` / `A5`):** Metallic words $W_0(m) = L^m R^m$ for $m \in \{1, 2, 3, 4\}$ (golden $m=1$, silver $m=2$, bronze $m=3$, McKay door $m=4$).
- **Declared History Family (Golden Thread, $k \in \{1, 2, 3\}$):**
  1. `(6)`: departure `LLLLLLR` ($L^6 R (LR)^k$);
  2. `(2,1,2,1,2)`: departure `LLRLLRLLR` ($L^2 R L^2 R L^2 R (LR)^k$);
  3. `(2,1,1,1,2)` (Planted mirror-degenerate negative control `A4`/`T3`): departure `LLRLRLLR` ($L^2 R L R L^2 R (LR)^k$);
  4. `(2,2,2)`: departure `LLRRLL` ($L^2 R^2 L^2 (LR)^k$);
  5. `(2,1^8,2)`: departure $L^2 (RL)^4 R L^2 R (LR)^k$;
  6. `golden_bg`: bare $(LR)^{k+1}$;
  7. `neg_ctrl_L2RLR` (Planted bundle-extension failure control `T3`): $L^2 R L R$.
  8. **Bounded Exhaustive Family (`A6` / `T2`):** All palindrome-free and general run departures $(r_1, \dots, r_d)$ with $1 \le d \le 5$, $\sum r_i \le 8$, closed with $(LR)^k$ ($k \in \{1, 2\}$).
- **Declared Fibre Area Scan:** $A \in \{0.01, 0.1, 1.0, 2\pi\}$ (default comparison at $A = 1.0$, sensitivity tracked across all four).
- **Pre-Registered Thresholds:**
  - Bundle extension (`A0`): exact modular integer congruence $W_H^T v \equiv \pm v \pmod{\mathbb{Z}^2}$ (`0` tolerance).
  - Orbital/Spectral Uniqueness (`A3`): Two distinct $W_H^T$-orbits $[k_1], [k_2]$ (modulo orientation $\pm k$ for real untwisted `(S1)`, or directly in $\mathcal{E}_v$ for complex twisted `(T)` modulo the bundle's rank-2 $\chi_v \leftrightarrow \chi_{-v}$ swap at $-v$ parity) are resolved as non-degenerate iff $|E_0([k_2]) - E_0([k_1])| / E_0([k_1]) > 10^{-7}$.
  - Loop Sensitivity (`T0` / `A2`): `Read` depends non-tautologically on `Data` iff $|s^*_{(T)} - s^*_{(S1)}|_{\mathbb{R}/\mathbb{Z}} > 10^{-4}$ (or $|\tau_{\text{Sol}}(s^*_{(T)}) - \tau_{\text{Sol}}(s^*_{(S1)})| > 10^{-4}$).

### Sector 3 (`BE-3`): Weave & Torsion-Coupled 1-Loop Potential $V_{\text{eff}}(\tau, w)$ (`P-629` / `X:TAU`)
- **Declared Functional Candidates (Zero Fitted Parameters):**
  1. `C0_four_2D` & `C0_four_6D`: The weave's endomorphism module $\operatorname{End}\rho_Q = \mathbf{1} \oplus \operatorname{ad}$ (trivial + three non-trivial 2-torsion parity lines);
  2. `E8_248_weave_6D`: The 248-dimensional $\mathfrak{e}_8$ root/spinor content $\mathbf{120}_+ \text{ (bosonic, periodic)} \oplus \mathbf{128}_- \text{ (fermionic, anti-periodic)}$ summed democratically over the 3-branch weave orbit;
  3. `Torsion_1loop_6D(N)`: Bosonic and supertrace 1-loop shifted-lattice Casimir potentials coupled to torsion Wilson lines $w = \frac{a\tau + b}{N}$ of exact orders $N \in \{1, 2, 3, 4, 5, 6\}$ on domain $\operatorname{Im}\tau \in [0.5, 8.0]$, $\operatorname{Re}\tau \in [-0.5, 0.5]$.
- **Pre-Registered Checks:**
  - Verify $\operatorname{SL}(2,\mathbb{Z})$ invariance at $w=0$ and $\pm\Gamma_1(N)$ invariance on the torsion orbit to `< 1e-12`;
  - Verify vanishing gradient $|\nabla_\tau V| < 10^{-12}$ at elliptic orbifold points $\tau = i$ and $\tau = \omega = e^{2\pi i/3}$ for all $\operatorname{SL}(2,\mathbb{Z})$-invariant potentials;
  - Determine whether unconstrained minimization over $(\tau, N)$ stabilizes any interior finite-height point off $\{i, \omega\}$ with $N > 1$, or lands on $\{i, \omega\}$, trivial $w = 0$ ($N=1$), or runs to the cusp ($\operatorname{Im}\tau \to \infty$).

### Sector 4 (`BE-4`): Exhaustive 46D $\mathfrak{u}(3)_{c,\text{EM}}$-Neutral Core & Chirality Back-Edge (`WP-3.3` / `X:HAND`)
- **Declared Algebra & Subspace:** Full $248$-dimensional $\mathfrak{e}_8$ Lie algebra constructed explicitly from its root/Chevalley basis (no shortcuts), identifying $\mathfrak{u}(3)_{c,\text{EM}} \subset A_3 \oplus D_5 \subset \mathfrak{e}_8$ and computing $Z_{\mathfrak{e}_8}(\mathfrak{u}(3)_{c,\text{EM}}) = \{X \in \mathfrak{e}_8 : [X, \mathfrak{u}(3)_{c,\text{EM}}] = 0\}$ by exact numerical singular-value nullspace (`tol = 1e-12`).
- **Pre-Registered Tests:**
  1. Prove $\dim Z_{\mathfrak{e}_8}(\mathfrak{u}(3)_{c,\text{EM}}) = 46 = 45\,(D_5) + 1$ and decompose $D_5 = (1,0)_3 \oplus (0,1)_3 \oplus (3,0)_7 \oplus (0,3)_7 \oplus (2,2)_{25}$.
  2. Evaluate the gauge-boson mass-squared matrix $M^2_W(\Phi) = -\operatorname{Tr}_{\mathfrak{e}_8}([T_a, \Phi][T_b, \Phi])$ on the left-right weak sector $(w_L, w_R)$ across general backgrounds $\Phi$ in the 46D neutral space (comparing the $\Omega_{16}$-self-dual 20D locus against generic $(2,2)_{25}$ coset backgrounds, both unrestricted and subject to the hyperKähler/F-D flatness condition $[\Phi, \Phi^\dagger] = 0$), with **mandatory random Haar unitary basis-scrambling (`Guardrail 3`)** verified to `< 1e-12`.
  3. Compute the finite/elliptic chiral antisymmetry index on conjugate matter sectors $(\mathbf{R} \oplus \overline{\mathbf{R}})$ under arbitrary Hermitian/skew-Hermitian deformations in the 46D neutral core, testing whether any static 4D internal operator can generate $\operatorname{ind}(\mathbf{R}) - \operatorname{ind}(\overline{\mathbf{R}}) \neq 0$ without chiral boundary conditions or 6D topological flux.
