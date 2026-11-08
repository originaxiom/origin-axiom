# AGY-00a Common-Model & Alternative-Background Manifest

**Date:** 2026-11-08
**Run ticket / microtask ID:** `AGY-00a` (parent task: `AGY-00`; coordination revision 2)
**Status:** **UNREVIEWED AUTHOR SOURCE-INTAKE CHECKPOINT (`0 of 19`)**
**Scientific execution / imports / collection performed:** `false` (strictly source intake and manifest documentation per `START_HERE.md` at `ee34f60fe1e12ca623f8bd6144fb8a6408e6587f`)

---

## 0. Immutable Baseline Pins

| Branch / Role | Commit SHA | Key Inspected Documents & Blob SHA256 |
|---|---|---|
| `origin/audit/physical-bridge-2026-09-05` (Dispatch Rev. 2) | `ee34f60fe1e12ca623f8bd6144fb8a6408e6587f` | `START_HERE.md` (`b0781e973f406fa036535956405304783565ccafe9e885b0ad2c944ad5334f0b`), `WORK_ORDER.md` (`c1b976b740854aecc16c1d29503209190d57cb3729e118d415cbf354ec19276a`), `TASKS.json` (`422601e1b175798cc6c2254ec489a31b7bb7b6e1ef7cdaed69626158780a6dbc`), `REVIEW_FORM.md` (`16fcd8203457ed116f2c87f92f04a086a30ce3bd7b83f947388f17495b4b812b`) |
| `origin/audit/physical-bridge-2026-09-05` (Physical Base) | `dd7490203c55bae043585f594af5a13afe634fa7` | `SM3_AND_GRAVITY_COMPLETION_CHECKLIST_2026_11_08.md` (`b3a04ab794beab0fce31b4365a011d2c3353f03932d22eef34469fd59b71729f`), `relays/PHYSICAL_TO_AGY_MAIN_AND_SM_2026-11-08_21B_SCOPE_AND_SM3_COMPLETION.md` (`769aaadb8cd6614da9f44d39529f8ca0b0dd3c8902d34221fb12c95142dc6a4b`), `weave_curved_action_2026_10_08/PROOF.md` (`c505823ce2b934b9737780acf3d6bbbeeb8482613b7ecc76a2ece58b1c2ebc4f`), `weave_physical_mass_2026_10_08/PROOF.md` (`04fbb6b7ddc23fe2ae56aa24f3df6e9a710f6278363213b8a509b06ace83ef8d`), `DISCRIMINANT_COVER_PERIPHERAL_AND_ORDER_THREE_WILSON_2026_11_08.md` (`5c056ae0d1a4cbc6ead0a9c1efa9f32719a1d013a290894fa70d5f31f2c66d46`) |
| `origin/agy/audit-2026-11-02` (AGY Pinned Base) | `21b293e87ff09fd64911267e9b4aa447fbfab2b9` | `src/origin_axiom/weave_unification_bridge.py` (`73bb65f3c09a6511b9bbcfd3666c7e945ffd39aeab61fe23f589b91113d759c6`), `src/origin_axiom/p000_pure_logic_bridge.py` (`76bd14f3488d1413969da367ee98ef6c2408a4a5f1800ebed5e1cd64f23c4ce5`), `relays/AGY_TO_PHYSICAL_AND_MAIN_2026-11-07_SUCCESSOR_REPAIRS_AND_WEAVE_CRYSTALLIZATION.md` (`771274740ee480e74d767fb6c2f2125111c37cdb84bd00cd2dd161ae0dd6fe08`) |
| `origin/main` (Canonical Genesis) | `217e37c4f37bd80998f3c3e10cad358023f58114` | `GENESIS.md` (`ec8c3dba05a5c947416a18952bc40f99a32af5135c87987c6f7e6236bc34bad4`), `docs/THE_TAU_READOUT_RULE.md` (`461ead931f039e8924c6922e803434529445b8a2cf9296d531ecf99487773fcd`) |

---

## 1. Carrier, Marking, Spin Line, and Supplied Geometry

### 1.1 Base Carrier $\Sigma_{1,1}$ and Canonical `GENESIS.md` Premise Status
- **Topological carrier and marking (`GM1`, `GM2`, `GM4`):** Once-punctured oriented torus $\Sigma_{1,1}$ with marked fundamental group $\pi_1(\Sigma_{1,1}, x_0) \cong F_2 = \langle a, b \rangle$ and oriented peripheral puncture loop $c = [a, b] = a b a^{-1} b^{-1}$.
  - In `GENESIS.md` (`v1.62` at `217e37c4f37bd80998f3c3e10cad358023f58114`), `GM1` (two records / rank-2 invariance of `[a,b]`) is **POSTULATED, in an equivalent form [v1.50]**, `GM2` (elementary shears $L, R$) is **POSTULATED**, `GM3` (aperiodicity) is **POSTULATED**, `GM4` (realization on $\Sigma_{1,1}$) is **POSTULATED, the puncture CONDITIONAL** (`FK5` OPEN: faithful $F_2$ vs. abelian quotient), `GM5b` (inverse moves legal, generating $-I = (L R^{-1} L)^2$) is **ADOPTED [v1.48]**, and `GM5c` (swap $P$) is **OPEN / even ticks observed [v1.33]**.
  - In `docs/THE_TAU_READOUT_RULE.md` (`217e37c4f`) and `GENESIS.md` (`GM5c` [v1.35], `FK9` [v1.45]), geometric level-surface $\tau$ readout (`B1847`/`B1854`/`B1857`) is distinct from state/vacuum selection; no fibre modulus $\tau$ is forced by the weave alone (`FK9` OPEN).
- **Supplied Riemannian metric and conformal factor (`weave_curved_action_2026_10_08/PROOF.md` §1–§2):**
  - Complete finite-area Riemannian metric $g = \Omega^2(dx^2 + dy^2)$, orientation $dx \wedge dy$, complex coordinate $z = x + i y$.
  - On the hyperbolic cusp end $y \ge Y$, $\Omega(y) = \ell / y$, $d\text{vol} = (\ell^2 / y^2)\,dx\,dy$, and Gaussian / scalar curvature is constant negative ($K = -1/\ell^2$, $R_{\text{scalar}} = -2/\ell^2$).
  - Setting $\sigma = \log \Omega$, the unitary spin connection in coordinate directions is $s_x = \frac{1}{2}\partial_y \sigma$, $s_y = -\frac{1}{2}\partial_x \sigma$ with curvature $ds = -\frac{1}{2}\Delta \sigma\,dx \wedge dy = \frac{\Omega^2}{4} R_{\text{scalar}}\,dx \wedge dy$.
- **Spin line $S$ (`weave_curved_action_2026_10_08/PROOF.md` §1; `COUPLED_HALF_ROOT_KERNEL_AND_CORE_LIFT_SENSITIVITY.md` §2, §4–§6):**
  - Holomorphic spin line $S$ satisfying $S^2 = K_\Sigma$, with extending cusp peripheral sign $-1$ (antiperiodic on odd powers $S^a$ in the trivialized puncture frame).
  - Extending $S$ to the compactified elliptic curve defines a flat order-2 spin line $\eta$ (`eta(a), eta(b) in {+1, -1}`). Identifying $\eta$ with the odd spin structure $\eta = \mathcal{O}$ (`eta(a) = eta(b) = +1` in the chosen marking) is a **conditional geometric hypothesis**, not yet an earned physical map (`COUPLED_HALF_ROOT_KERNEL_AND_CORE_LIFT_SENSITIVITY.md` §5–§6).

### 1.2 Distinct Covers (Never Conflated Without an Explicit Pullback Map)
From `DISCRIMINANT_COVER_PERIPHERAL_AND_ORDER_THREE_WILSON_2026_11_08.md` (`1704f9e41`):
1. **Carrier `C0` (Base $\Sigma_{1,1}$, degree 1):** $\pi_1 = F_2$, compact genus $g = 1$, $1$ puncture ($\chi = -1$).
2. **Carrier `C1` (Quaternion cover $\Sigma_{Q_8}$, degree 8):** $N = \ker(\rho: F_2 \to Q_8)$ where $\rho(a) = A$, $\rho(b) = B$ in $Q_8$. $N$ is free of rank $9$; $\Sigma_{Q_8}$ has compact genus $g = 3$ and $4$ punctures ($\chi = -8$), with spatial cusp loops conjugate to $c^2$.
3. **Carrier `C2` (Discriminant cover $\Sigma_K$, degree 32 over $\Sigma_{1,1}$, degree 4 over $\Sigma_{Q_8}$):**
   - With $P_{uv} = P_u + \rho(u) P_v$, $P_a = 0$, $P_b = I$, the restriction $P|_N : N \to L = D_4 \subset \mathbb{Z}^4$ is a surjective additive homomorphism onto the even-sum lattice $L = D_4$, whose dual is $L^* = \mathbb{Z}^4 \cup (\mathbb{Z} + \frac{1}{2})^4$.
   - The four half-lattice characters $k_{00}, k_{10}, k_{01}, k_{11} \in (\frac{1}{2}L)/L^*$ annihilate $2L^* = 2\mathbb{Z}^4 \cup (2\mathbb{Z}+1)^4 \subset L$, defining the order-4 quotient $A_{\text{disc}} = L / (2L^*) \cong (\mathbb{Z}/2)^2$ (distinct from $L/2L$ of order $16$ and $N^{\text{ab}}/2N^{\text{ab}}$ of order $2^9$).
   - The normal subgroup $K = (P|_N)^{-1}(2L^*) \triangleleft F_2$ has $[N:K] = 4$ and $[F_2:K] = 32$.
   - Because $\rho(c) = -I$, $P_c = I + A$, and $P_{c^2} = P_c + \rho(c)P_c = 0$, every spatial puncture loop $h c^2 h^{-1}$ of $\Sigma_{Q_8}$ lies in $\ker P|_N \subset K$. Thus all four $A_{\text{disc}}$ characters are **trivial on the spatial cusps**, and $\Sigma_K \to \Sigma_{Q_8}$ is an unbranched 4-sheeted cover of compact genus $g = 1 + 4(3-1) = 9$ with $16$ punctures ($\chi = 2 - 2(9) - 16 = -32$).

---

## 2. Supplied Gauge Algebra, Field Bundles, Kinetic Weights, and Common Action

### 2.1 Supplied Parent Lie Algebra and Complete 248 Branching
- **Parent gauge algebra (`weave_curved_action_2026_10_08/PROOF.md` §1; `WEAK_CURRENT_GRADING_AND_DISCRETE_CHARGED_VECTORS.md` §1):**
  - Supplied compact real form $\mathfrak{e}_8$ ($\dim_\mathbb{R} = 248$) equipped with positive-definite invariant trace form $\kappa$ on Hermitian generators and 6D gauge coupling $g_6^2 > 0$.
  - **Premise status:** Explicitly **SUPPLIED** (`e8_remains_supplied_premise_not_earned_from_single_register = True`; `FK15` OPEN). The two-register lattice glue $D_4 \oplus D_4 \to D_8 \to E_8$ in `p000_pure_logic_bridge.py` (`verify_wall2_d4_to_e8_glue_and_cover_family_functor`) is a conditional lattice construction that leaves the second register, orthogonal sum, unimodular completion, and field map to be earned.
- **Complete $\mathfrak{so}(10) \oplus \mathfrak{su}(4)$ branching and $\mathrm{Zeta}$-grading (`WORK_ORDER.md` §AGY-02; `WEAK_CURRENT_GRADING_AND_DISCRETE_CHARGED_VECTORS.md` §1):**
  $$\mathfrak{e}_8 = \underbrace{(45, 1) \oplus (1, 15) \oplus (10, 6)}_{\mathfrak{g}_{120}^{(+1)}\text{ (even under }\mathrm{Zeta},\text{ integer }D_8\text{ roots)}} \;\oplus\; \underbrace{(16, 4) \oplus (\overline{16}, \overline{4})}_{\mathfrak{g}_{128}^{(-1)}\text{ (odd under }\mathrm{Zeta},\text{ half-integer spinor roots)}},$$
  where $\mathrm{Zeta} = \exp(3\pi i Q)$ fixes $\mathfrak{g}_{120}^{(+1)}$ ($Q \in \{0, \pm 2/3, \pm 4/3\}$) and negates $\mathfrak{g}_{128}^{(-1)}$ ($Q \in \{\pm 1/3, \pm 1\}$).
  - Under the two principal $\mathfrak{so}(5) \subset \mathfrak{so}(10)$ triples $(E_+, E_-)$, thecentralizer in $\mathfrak{e}_8$ is $A_3 = (1, 15) \cong \mathfrak{su}(4)$.
  - The unbroken colour-plus-electromagnetic subalgebra is $\mathfrak{u}(3) = \mathfrak{su}(3)_c \oplus \mathfrak{u}(1)_Q \subset (1, 15)$ (dimension 9), under which the fundamental $4$ of $\mathfrak{su}(4)$ branches as $1_{(+1)} \oplus 3_{(-1/3)}$, $\bar{4}$ branches as $1_{(-1)} \oplus \bar{3}_{(+1/3)}$, and the antisymmetric $6 = \Lambda^2 4$ in $(10, 6)$ branches as $3_{(+2/3)} \oplus \bar{3}_{(-2/3)}$ (carrying the colour-up quark charges $\pm 2/3$ absent from $\mathfrak{g}_{128}^{(-1)}$).

### 2.2 Bosonic and Fermionic Field Bundles and Actual Kinetic Weights
From `weave_curved_action_2026_10_08/PROOF.md` §1–§2 and `weave_physical_mass_2026_10_08/PROOF.md` §1–§2:
- **Bosonic fields:**
  1. 4D vector multiplet connection $V_\mu$ with internal 6D kinetic density $\Omega^2 \kappa$ under $dx\,dy$;
  2. Internal affine connection chiral field $A = A_x + i A_y$ (where $F = \partial_x A_y - \partial_y A_x - i[A_x, A_y]$ is Hermitian), kinetic density $\frac{1}{2}\kappa(\delta A^\dagger \delta A)\,dx\,dy$;
  3. Two adjoint spin chiral fields $(q, r) \in \Gamma(\operatorname{ad}(P) \otimes S \otimes F)$ with physical orthonormal coefficients $(\hat{q}, \hat{r}) = \Omega^{-1/2}(q, r)$, kinetic density $\Omega\,\kappa(\delta q^\dagger \delta q + \delta r^\dagger \delta r)\,dx\,dy$.
- **Four independent left-handed Weyl fermion slots $(\lambda, a, u, v)$:**

| Slot | Physical Origin | Rotational Charge under $z' = e^{i\theta}z$ | Bundle Identification | Coordinate Kinetic Density $h_i(x,y)\,dx\,dy$ |
|---|---|:---:|---|---|
| $\lambda$ | Vector-multiplet scalar gaugino | $0$ | $\operatorname{ad}(P)$ (mapped via $i\Omega^2\lambda/\sqrt{2}$ to $C_3 = E \otimes K_\Sigma \otimes \bar{K}_\Sigma$) | $h_0 = \Omega^2$ |
| $a$ | Chiral connection / $(0,1)$-form fermion | $+2$ | $\operatorname{ad}(P) \otimes \bar{K}_\Sigma$ | $h_1^{(a)} = \frac{1}{2}$ |
| $u$ | First spin chiral fermion ($q$ superpartner) | $-1$ | $\operatorname{ad}(P) \otimes S$ | $h_1^{(u)} = \Omega$ |
| $v$ | Second spin chiral fermion ($r$ superpartner) | $-1$ | $\operatorname{ad}(P) \otimes S$ | $h_1^{(v)} = \Omega$ |

- **Right-handed Weyl fields:** Hermitian conjugates $(\bar{\lambda}, \bar{a}, \bar{u}, \bar{v})$ in the trace-dual conjugate bundle; never four additional independent left slots.

### 2.3 Common Curved Action, Moment Map, and Stationary Vacuum Equations
From `weave_curved_action_2026_10_08/PROOF.md` §2–§4:
- **Kähler moment map (derived from $G(\delta,\delta)$ without integration by parts on $q,r$):**
  $$\mu = F + \Omega([q, q^\dagger] + [r, r^\dagger]) = \Omega^2\!\left(\frac{F}{\Omega^2} + [\hat{q}, \hat{q}^\dagger] + [\hat{r}, \hat{r}^\dagger]\right),$$
  fixing the D-term potential energy to
  $$V_D = \int dx\,dy\,\frac{\kappa(\mu^2)}{2\Omega^2} = \frac{1}{2}\int d\text{vol}\,\kappa\!\left(\left|\frac{F}{\Omega^2} + [\hat{q}, \hat{q}^\dagger] + [\hat{r}, \hat{r}^\dagger]\right|^2\right).$$
- **Holomorphic superpotential (from 10D $\mathcal{N}=1$ AHGW Eq. 35 keeping total derivatives):**
  $$W = \frac{1}{2}\int \kappa(q\bar{\partial}_A r - r\bar{\partial}_A q)\,dx\,dy, \qquad \bar{\partial}_A = \partial_x + i\partial_y - i\operatorname{ad}_A,$$
  whose first variation retains both the bulk F-terms and the exact antisymmetric boundary pairing:
  $$\delta W = \int dx\,dy\,\kappa(\delta q\,\bar{\partial}_A r - \delta r\,\bar{\partial}_A q - i\delta A\,[r, q]) - \frac{i}{2}\oint_{\partial\Sigma} \kappa(q\,\delta r - r\,\delta q)\,dz.$$
- **Coupled classical stationary background equations:**
  $$\bar{\partial}_A q = 0, \qquad \bar{\partial}_A r = 0, \qquad [q, r] = 0, \qquad \frac{F}{\Omega^2} + [\hat{q}, \hat{q}^\dagger] + [\hat{r}, \hat{r}^\dagger] = 0.$$
  At the balanced two-triple background (`COUPLED_QUATERNION_STATIONARY_BUNDLE_AND_CUSP_LAW.md` §2), the spin-induced gauge connection is $A_{\text{spin}} = \frac{1}{2}s H$ with $F_{\text{spin}} = -\frac{H}{4\ell^2}\,d\text{vol}$ and local orthonormal spin condensates
  $$\hat{q} = \frac{E}{2\sqrt{2}\ell}, \qquad \hat{r} = \frac{G}{2\sqrt{2}\ell}, \qquad [E, G] = 0, \qquad [\hat{q}, \hat{q}^\dagger] + [\hat{r}, \hat{r}^\dagger] = \frac{H}{4\ell^2},$$
  cancelling $F_{\text{spin}}/d\text{vol}$ identically across every patch.

---

## 3. Physical 4-Slot Fermion Operator $M = U_{\text{out}} T U_{\text{in}}$ and Complete Domain

From `weave_physical_mass_2026_10_08/PROOF.md` §2–§4:
- **Quadratic fermion superpotential Hessian and gauge Killing coupling:**
  For $x = (a, u, v)$, define
  $$p_1 = \bar{\partial}_A u + i[q, a], \qquad p_2 = \bar{\partial}_A v + i[r, a], \qquad t = [q, v] - [r, u],$$
  $$D_0 \epsilon = \sqrt{2}(\bar{\partial}_A \epsilon, -i[q, \epsilon], -i[r, \epsilon]), \qquad D_0^\dagger x = -\frac{\partial_z a - 2i\Omega([q^\dagger, u] + [r^\dagger, v])}{\sqrt{2}\Omega^2},$$
  where $\partial_z = \partial_x - i\partial_y - i\operatorname{ad}_{A^\dagger}$.
- **Explicit 4-slot physical mass operator $M(\lambda, a, u, v)$:**
  $$M(\lambda, a, u, v) = \begin{pmatrix} D_0^\dagger x \\ 2i t + \sqrt{2}\partial_z \lambda \\ p_2 / \Omega - \sqrt{2}i[q^\dagger, \lambda] \\ -p_1 / \Omega - \sqrt{2}i[r^\dagger, \lambda] \end{pmatrix} = U_{\text{out}} T U_{\text{in}},$$
  where $T(x, \sigma) = (D_0^\dagger x,\, D_1 x + D_2^\dagger \sigma)$ acts on the Koszul-Dolbeault complex $(C_1 \oplus C_3) \to (C_0 \oplus C_2)$ with metrics
  $$h_0 = \Omega^2, \qquad h_1 = \operatorname{diag}\!\left(\frac{1}{2}, \Omega, \Omega\right), \qquad h_2 = \operatorname{diag}(\Omega^{-1}, \Omega^{-1}, 2), \qquad h_3 = 2\Omega^{-2},$$
  and the explicit unitary bundle isometries are
  $$U_{\text{in}}(\lambda, a, u, v) = \left((a, u, v),\, \frac{i\Omega^2\lambda}{\sqrt{2}}\right), \qquad U_{\text{out}}(g, p_1, p_2, t) = \left(g,\, 2i t,\, \frac{p_2}{\Omega},\, -\frac{p_1}{\Omega}\right).$$
- **Complete operator domain:**
  - Graph closure of compactly supported smooth sections on the complete cusp surface $\Sigma$ (`weave_curved_action_2026_10_08/PROOF.md` §4; `weave_physical_mass_2026_10_08/PROOF.md` §4).
  - In a local puncture coordinate $w$ ($r = |w|$), a meromorphic section of $S^a$ with pole order $n$ has radial norm $\int r^{a - 1 - 2n}(\log(1/r))^{a-2}\,dr$, which is $L^2$-integrable if and only if $n < a/2$, or $n \le a/2$ when $a < 1$ (`COUPLED_HALF_ROOT_KERNEL_AND_CORE_LIFT_SENSITIVITY.md` §4).
  - For the surviving half-root Koszul cohomology lines $S^{-3}, S^1 \oplus S^1, S^5$, the strict cusp pole bounds give divisor degrees $(-2, 0, 2)$ on the compactified genus-1 curve.

---

## 4. Spin / Flavour / Gauge Transitions and Explicit Separation of Candidate Background Models

In the balanced flavour frame $(q', r') = ((q+r)/\sqrt{2}, (q-r)/\sqrt{2})$ proportional to $(E_+, E_-)$ (`COUPLED_HALF_ROOT_KERNEL_AND_CORE_LIFT_SENSITIVITY.md` §2):
- Flavour holonomy acts by $\rho(F_i) = i\sigma_x$, $\rho(F_k) = \operatorname{diag}(i, -i)$ ($\det = -1$).
- Gauge compensators $A, D \in \operatorname{Spin}(10)$ (with $B = D A$) obey
  $$\operatorname{Ad}_A E_+ = -i E_-, \quad \operatorname{Ad}_A E_- = -i E_+, \quad \operatorname{Ad}_D E_+ = -i E_+, \quad \operatorname{Ad}_D E_- = +i E_-,$$
  so $\rho(\gamma)\operatorname{Ad}_{K(\gamma)}(E, G) = (E, G)$ preserves the background pair globally.
- On the $(j, j) = (3/2, 3/2)$ spinor module of each $16 \subset \operatorname{Spin}(10)$, if $A$ has eigenvalue $\alpha$ on the highest weight vector $v_{\text{top}} = |3/2, 3/2\rangle$, the induced actions on the surviving Koszul cohomology lines $(S^{-3}, S^1 \oplus S^1, S^5)$ are:
  - Degree 0 ($S^{-3}$): $A \mapsto \alpha$, $D \mapsto 1$, $B \mapsto \alpha$;
  - Degree 1 ($S^1 \oplus S^1$): $A \mapsto \alpha\sigma_x$, $D \mapsto I_2$, $B \mapsto \alpha\sigma_x$;
  - Degree 2 ($S^5$): $A \mapsto -\alpha$, $D \mapsto 1$, $B \mapsto -\alpha$.

To prevent silent cross-model combination (`WORK_ORDER.md` Guardrail 1 & §AGY-00), the table below separates the **five distinct candidate models** present across the physical and AGY branches:

| Model ID | Carrier | Core Gauge Lift $K(\gamma)$ | Extra Order-3 Wilson $\chi_3$ | $A_3 = (1,15)$ Unbroken Gauge Reduction | Half-Root $(16,4)\oplus(\overline{16},\overline{4})$ Kernel at $\eta = \mathcal{O}$ | Integer-Root $(10,6)\oplus(45,1)$ & Global Status |
|---|---|---|---|---|---|---|
| **M1 (Bare $\operatorname{Spin}(10)$ Lift)** | `C0` ($\Sigma_{1,1}$, $g=1$, $1$ cusp) | Bare $A_{\text{bare}} \in \operatorname{Spin}(10)$, $A_{\text{bare}}^4 = \mathrm{Zeta}$, $\alpha^4 = -1$ | Retained: $\chi_3$ of order 3 on $3_{(-1/3)}, \bar{3}_{(+1/3)}$ | Reduced to $\mathfrak{u}(3)$ ($9$ generators) by $\chi_3$ | $\alpha\chi_R \neq \pm 1$ on all records $\implies 2$ modes per record ($8 \times 2 = 16$ total) | **OPEN** (full $(10,6)$ and $(45,1)$ roster under bare lift not yet tabulated in one common table) |
| **M2a / M2b (Coherent $\operatorname{Pin}_2$ Lift + $\chi_3$, $\pm\mathrm{Zeta}$)** | `C0` ($\Sigma_{1,1}$, $g=1$, $1$ cusp) | $\tilde{A} = A_{\text{bare}} h_4$ (or $\pm\mathrm{Zeta}\tilde{A}$), $\tilde{A}^2 = K_\pi = \exp[-i\pi(H_+-H_-)/2]$, $\alpha^2 = 1$ ($\alpha = +1$ vs $-1$ exchanges $L_+, L_-$) | Retained: $\chi_3 \neq 1$ of order 3 on colour triplets; $1$ on colour singlets | Reduced to $\mathfrak{u}(3)$ ($9$ generators) by both $h_{15} = \operatorname{Ad}_{h_4}$ and $\chi_3$ | Singlets $1_{(\pm 1)}$: $3$ modes each ($2\times 3 = 6$); Triplets $3_{(-1/3)}, \bar{3}_{(+1/3)}$: $2$ modes each ($6\times 2 = 12$); Total $= 18$ | **OPEN** (integer-root $(10,6)$ up-quark $Q=\pm 2/3$ kernel and continuum threshold duty assigned to `AGY-02`) |
| **M3a / M3b (Pure-$h_4$ Coherent Lift, $\chi = (0,0)$, $\pm\mathrm{Zeta}$)** | `C0` ($\Sigma_{1,1}$, $g=1$, $1$ cusp) | $\tilde{A} = A_{\text{bare}} h_4$ (or $\pm\mathrm{Zeta}\tilde{A}$) with $h_4 = \exp(2\pi i \cdot \frac{3}{8}Q)$, $\alpha^2 = 1$ | **Omitted** ($\chi = (0,0)$, trivial on all sectors — an explicit change of flat background, NOT a pullback of M2) | $h_{15} = \operatorname{Ad}_{h_4}$ acts as $-1 \neq +1$ on the $6$ leptoquark roots ($Q=\pm 4/3$) and $+1$ on $\mathfrak{u}(3)$ ($9$ generators) without $\chi_3$ | All $8$ half-root records have cohomology `(0,3,3,0)` $\implies 3$ modes per record ($8 \times 3 = 24$ charged half-root coefficients) | **OPEN (`AGY-01` & `AGY-02`):** Must verify global stationarity, real structure, peripheral/core coherence, and full $(10,6)$ + $(45,1)$ roster without $\chi_3$ |
| **M4 (Pullback of M2 to Degree-32 Cover $\Sigma_K$)** | `C2` ($\Sigma_K$, $g=9$, $16$ cusps, $[F_2:K]=32$) | Pullback of M2a/M2b along $K = (P|_N)^{-1}(2D_4^*) \hookrightarrow F_2$ | **Survives nontrivial** on $K$ since $\gcd(32, 3) = 1$ (`1704f9e41` §5) | Pullback of $\mathfrak{u}(3)$ bundle to $\Sigma_K$ | Under the base fixed-column comparator, $\mathbb{Z}_2$ deck signs $\pm 1$ cannot cancel $\omega_3 = e^{2\pi i/3}$ ($\ker(\pm\omega_3\sigma_x - I_2) = \{0\}$); full genus-9 spectrum is **OPEN** | **OPEN (`AGY-05`):** Requires genuine genus-9 / 16-cusp operator pullback and physical end/source law to select the 3D augmentation module $W$ (irreducible under $A_{\text{disc}} \rtimes S_3$ of order 24) |
| **M5 (Pullback of M3 to Degree-32 Cover $\Sigma_K$)** | `C2` ($\Sigma_K$, $g=9$, $16$ cusps) | Pullback of M3a/M3b ($\chi = (0,0)$) along $K \hookrightarrow F_2$ | Absent ($\chi = (0,0)$) | Pullback of $h_{15}$-reduced $\mathfrak{u}(3)$ bundle to $\Sigma_K$ | Base `(0,3,3,0)` modes vs. cover $A_{\text{disc}}$ triplet $W$ are distinct dimension-3 spaces (`WORK_ORDER.md` §AGY-05); genus-9 spectrum is **OPEN** | **OPEN (`AGY-05`):** Equality of dimension ($3$) does not identify base pure-$h_4$ cohomology modes with the $A_{\text{disc}} \rtimes S_3$ cover triplet |

---

## 5. Disclosed `21b293e87` Source Limits and Preserved Standalone Controls

Per `WORK_ORDER.md` §AGY-00 and `PHYSICAL_TO_AGY_MAIN_AND_SM_2026-11-08_21B_SCOPE_AND_SM3_COMPLETION.md` (`dd7490203`), the following three source limitations in `src/origin_axiom/weave_unification_bridge.py` and `src/origin_axiom/p000_pure_logic_bridge.py` at `21b293e87ff09fd64911267e9b4aa447fbfab2b9` are explicitly recorded and quarantined from physical claim promotion:

1. **Imposed finite-interval radial profiles and `tau_plus` tensor product (`weave_unification_bridge.py` lines 4697–4723 and 5227–5262):**
   - *What the code computes:* Solves an interior Dirichlet Chebyshev matrix for $-d_t^2 + V(t)$ on the truncated interval $t \in [0, 4]$ with $V(t) = \frac{1}{4} + \pi^2 e^{2t} + 1$, assigns radial profiles $e^{-t/2}$ and $e^{-3t/2}$ (Gram-Schmidt orthogonalized on $[0,4]$), computes their $3 \times 3$ Hermitian overlap matrix `g_mat_3` against the radial vector mode $w_0(t)$, and forms `v_weak_6x6 = np.kron(tau_plus, g_mat_3)`.
   - *Why it is not yet the physical weak vertex:* The assigned profiles $e^{-t/2}, e^{-3t/2}$ are not verified to solve the coupled 4-slot differential equation $M\psi = 0$ with global core/cusp matching on $\Sigma_{1,1}$, and tensoring $\tau_+$ onto a single half-root spinor record does not evaluate the actual $\mathfrak{g}_{128}^{(-1)} \leftrightarrow \mathfrak{g}_{120}^{(+1)}$ weak root generator $[w_{\text{root}}, \cdot]$ between solved $(16,4)$ down-type ($Q = -1/3$) and $(10,6)$ up-type ($Q = +2/3$) zero modes.
   - *Preserved standalone status:* Retained strictly as a **conditional finite-interval quadrature and $SU(2)_L \times U(3)$ SVD-invariance software control**, not a physical SM3 weak-current derivation.
2. **Cubic-overlap-to-negative-quadratic-mass substitution in `Wall1` (`weave_unification_bridge.py` lines 4001–4025):**
   - *What the code computes:* Sets `c_a_coeff = I_L(1, 3) = 3/4` and `lambda_4_coeff = (||[L_i, L_j]||^2 / 2) * I_G(1; 4, 4) = 9/16`, then minimizes the polynomial $V(x) = -c_a x^2 + \frac{1}{2}\lambda_4 x^4$ at $x_*^2 = 45/32$.
   - *Why it is a type mismatch:* In `SAME_ACTION_GAUGE_BOUNDARY_RESPONSE_AND_CUBIC_2026_11_08.md` (`7e401a2f3b`), $I_L(p, q) = \frac{2Y}{\nu_p + \nu_q}$ is a **longitudinal cubic $vbb$ vertex overlap** carrying external momentum factors $(p^2 - q^2)$, not a negative quadratic mass term $-c_a x^2$. Furthermore, in `FOUR_CONNECTION_TAIL_VERTEX_WITH_GAUSS_EXCHANGE_2026_11_08.md` (`9bb2f1ef75`), integrating out the massive / Gauss radial mode produces a **negative Schur-complement exchange contribution** $-\frac{1}{2}\langle J_2, H_\perp^{-1} J_2\rangle$ subtracting from the direct quartic, rather than a standalone positive stabilizing quartic `lambda_4_coeff`.
   - *Preserved standalone status:* The rational values $I_L(1,3) = 3/4$ and $I_G(1;4,4) = 9/64$ remain valid standalone cusp overlap integrals; $x_*^2 = 45/32$ is only the minimum of an assumed polynomial, not a derived stationary core+tail amplitude.
3. **Discriminant cover quotient, spatial periphery, and $S_3$ vs. $A_{\text{disc}} \rtimes S_3$ wording in `Wall2` (`p000_pure_logic_bridge.py` lines 2970–3046):**
   - *What must be distinguished:* The order-4 quotient annihilated by the four characters is $A_{\text{disc}} = D_4 / (2D_4^*) \cong (\mathbb{Z}/2)^2$ (with $K = (P|_N)^{-1}(2D_4^*)$ of index $32$ in $F_2$), not $D_4/2D_4$ (order 16) or $N/2N$. Because $P_{c^2} = 0$, the spatial cusp loops of $\Sigma_{Q_8}$ have trivial $A_{\text{disc}}$ holonomy; the nontrivial signs on $Q_8$ presentation relators $r_2, r_3, r_2 r_3$ are core data, not automatic spatial cusp signs. Finally, pure $S_3$ permutations split the 3D augmentation module $W$ as $1 \oplus 2$ (commutant $a I_3 + b J_3$); irreducibility on $W$ (with scalar commutant $\mathbb{C} I_3$) requires the **order-24 combined action $A_{\text{disc}} \rtimes S_3$** retaining deck signs $D_2 = \operatorname{diag}(-1,+1,-1)$ and $D_3 = \operatorname{diag}(+1,-1,-1)$.

---

## 6. Open & Conflicting Manifest Entries (`OPEN` Registry for Subsequent Subtasks)

Each item below is marked **OPEN** for intake and mapped to its exact source files and downstream campaign task (`START_HERE.md` §Current assignment):

| Open Item ID | Question / Conflict Identified at Intake | Authoritative Source Locations Needed to Settle It | Target Downstream Task |
|---|---|---|---|
| **`OPEN-01`** | **Global coherence and input status of pure-$h_4$ ($\chi = (0,0)$) vs. $h_4 \cdot \mathrm{Zeta}$ vs. bare lift vs. legacy $\chi_3 = (1,0)$:** Does pure $h_4 = \exp(2\pi i \cdot \frac{3}{8}Q)$ define a globally stationary bundle across all sectors (including periphery, superpotential, real structure, and norms), and is the continuous-$\operatorname{Pin}_2$ relation $\tilde{A}^2 = K_\pi$ derived from registration or an added coherence premise? | `FULL_E8_COMPENSATOR_LIFT_AND_REGISTER_TRANSPORT.md` (`60128166`), `PIN2_COMPENSATOR_COHERENCE_AND_ELECTROMAGNETIC_PHASE.md` (`fc67d444`), `COUPLED_QUATERNION_STATIONARY_BUNDLE_AND_CUSP_LAW.md` (`221a7cd2`), `COUPLED_HALF_ROOT_KERNEL_AND_CORE_LIFT_SENSITIVITY.md` (`789adf75`) | `AGY-00b` (Reuse & Input Ledger) and `AGY-01` (`LIFT_AND_DOMAIN.md`) |
| **`OPEN-02`** | **Missing integer-root $(10,6)$ up-type quark sector ($Q = \pm 2/3$) and full 248 roster:** What are the exact kernel and cokernel counts, Koszul retractions, cusp pole bounds, and continuum thresholds of the physical 4-slot operator $M = U_{\text{out}} T U_{\text{in}}$ on $(10,6)$, $(45,1)$, and $(1,15)$ under both M2 ($\chi_3 \neq 1$) and M3 ($\chi = (0,0)$)? | `ELECTROWEAK_TWO_TRIPLE_PHYSICAL_KERNEL.md` (`871529dd`), `CONFINED_HALF_ROOT_SECTOR_AND_SURVIVING_CONTINUUM.md` (`8436811a`), `weave_physical_mass_2026_10_08/PROOF.md` (`04fbb6b7`), `WEAK_CURRENT_GRADING_AND_DISCRETE_CHARGED_VECTORS.md` (`7ac2e6cc`) | `AGY-02` (`ROSTER_PROOF.md`, `FULL_ROSTER.md`) |
| **`OPEN-03`** | **Common-action nonlinear boundary response and Schur-complement sign:** What is the exact quadratic Hessian, cubic $vbb$ response, direct quartic, and $-\frac{1}{2}\langle J_2, H_\perp^{-1} J_2\rangle$ Schur-complement Gauss/massive exchange on the joined core + tail (including all 4 fermion slots and cut-location sewing independence)? | `weave_curved_action_2026_10_08/PROOF.md` (`c505823c`), `SAME_ACTION_GAUGE_BOUNDARY_RESPONSE_AND_CUBIC_2026_11_08.md` (`7e401a2f`), `ACTUAL_CORE_MEAN_RESPONSE_AND_FLUX_SEWING_2026_11_08.md` (`4e8be593`), `FREQUENCY_CORE_ANGULAR_TAIL_AND_GAUGE_WARD_RESPONSE_2026_11_08.md` (`ea5bc025`), `FLAT_PERIOD_QUARTIC_AND_HANDLE_SCOPE_2026_11_08.md` (`a4f27a29`), `FOUR_CONNECTION_TAIL_VERTEX_WITH_GAUSS_EXCHANGE_2026_11_08.md` (`9bb2f1ef`) | `AGY-03` (`BOUNDARY_VARIATION.md`, `STATIONARITY_AND_RESPONSE.md`) |
| **`OPEN-04`** | **Global zero-mode wavefunctions and 128-to-120 cross-grading weak current:** Do actual global solutions of $M\psi = 0$ in $(16,4)$ and $(10,6)$ and the global charged-vector eigenmode $w$ of $P_v$ exist on the uncut domain, and what is the resulting matrix $g_{mn}(w) = g_6 \sum_i \int h_i\,\kappa(\psi_{i,m}^\dagger [w, \psi_{i,n}])$ without hand-assigned radial profiles or $\tau_+$ tensoring? | `WEAK_CURRENT_GRADING_AND_DISCRETE_CHARGED_VECTORS.md` (`7ac2e6cc`), `SAME_ACTION_REAL_GAUGE_FIXING_AND_ONE_LOOP_WEIGHTS.md` (`18a7f136`), plus outputs of `AGY-02` and `AGY-03` | `AGY-04` (`GLOBAL_MODES.md`, `WEAK_CURRENT.md`) |
| **`OPEN-05`** | **Base pure-$h_4$ 3-mode cohomology vs. degree-32 cover $A_{\text{disc}} \rtimes S_3$ triplet $W$:** Are the 3 base cohomology modes of `(0,3,3,0)` in Model M3 intertwined with the native registering triplet, or does family multiplicity require pulling back the full operator to the genus-9, 16-cusp cover $\Sigma_K$ ($K = (P|_N)^{-1}(2D_4^*)$) and earning deletion of the trivial character $k_{00}$ from an actual end/source law? | `DISCRIMINANT_COVER_PERIPHERAL_AND_ORDER_THREE_WILSON_2026_11_08.md` (`5c056ae0`), `AFFINE_DOUBLET_KERNEL_D4_AND_PARITY_2026_11_08.md` (`2e598aac`), `JOINT_FIRST_ORDER_REGISTER_AND_OLD_QUATERNION_COVER_2026_11_08.md` (`a147e103`), `GENESIS.md` (`FK7`, `FK8`, `FK12`, `FK13`) | `AGY-05` (`REGISTER_TO_FIELD_MAP.md`) |
| **`OPEN-06`** | **Dynamical 3+1 gravity and full anomaly / mode completion:** How does the 2+1 hyperbolic/CS construction (`THE_FRAMEWORK.md` L174) or spin-2 representation slot (`B1140`) connect to a dynamical 3+1 spacetime metric $g_{\mu\nu}$ with universal stress-energy coupling, and do full noncompact parent + boundary inflow anomalies cancel? | `SM3_AND_GRAVITY_COMPLETION_CHECKLIST_2026_11_08.md` (`b3a04ab7`) §3–§4, `weave_physical_mass_2026_10_08/PROOF.md` (`04fbb6b7`) §6 | `AGY-06` (`JOINED_VERDICT.md`, `INPUT_LEDGER.md`) |
