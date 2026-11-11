# Pre-Registration Plan — Phase 2: The 3D Cusped Hyperbolic & Chiral-Boundary Loop Engine

## 0. Scope, Firewall, and Non-Negotiable Guardrails
- **Workspace:** `/Users/dri/.gemini/antigravity/scratch/cusped_3d_loop_phase2` (clean-room Phase 2 workspace; zero edits to Phase 1 or upstream repositories).
- **Empirical Data Firewall (`0 of 19`):** Zero experimental masses, couplings, CKM/PMNS angles, or cosmological scales are imported anywhere in `src/`, `scripts/`, or `tests/`.
- **All 6 Mathematical-Physics Guardrails (`user_global`):**
  1. **Anti-Texas-Sharpshooter (`Guardrail 1`):** Zero target coordinates ($\tau^*$, target eigenvalues, or target generation counts) are embedded in any potential, selection rule, or mesh construction.
  2. **No Literal Flag/Zero Proofs (`Guardrail 2`):** Every homology group, bundle-extension check, volume integral, Laplace eigenvalue, Chern–Simons parity flip, and 2D Dirac topological index is computed directly from explicit matrices/simplices and verified numerically (`< 1e-12` where algebraic/analytic, and multi-grid convergence verified for 3D PDE eigenvalues).
  3. **Mandatory Haar Unitary Basis-Scrambling (`Guardrail 3`):** Every physical observable extracted from $E_8$ gauge/Dirac operators (weak boson mass spectra and 2D chiral Dirac zero-mode indices) is tested under independent random Haar unitary transformations and verified invariant to `< 1e-12`.
  4. **Benchmark Calibration Gate (`Guardrail 4`):** All 3D hyperbolic geometric/spectral tools and 2D topological Dirac solvers must pass exact analytical/literature calibration benchmarks before evaluating candidate histories.
  5. **Strict Non-Dimensionalization (`Guardrail 5`):** All hyperbolic lengths, volumes, eigenvalues, cusp shapes, and indices are strictly dimensionless geometric/topological invariants ($K = -1$ curvature units).
  6. **Zero-Trust Referee (`Guardrail 6`):** `scripts/referee_cusped_phase2.py` is AST-verified to contain **zero** imports from `cusped_loop` / `src` and independently rebuilds hyperbolic geometry, 3D spectral discretization, Mostow invariants, and lattice Wilson–Dirac / Clifford $E_8$ chirality checks.

---

## 1. Textbook Calibration Gate (`calibration_gate.py`)
Before evaluating `(6)` or scanning `A6`, verify:
1. **3D Hyperbolic Volume & Cusp Calibration on `m004` (`b++LR` and `b+-LR`):**
   - Extract exact Penner $\lambda$-lengths $\lambda_{ab}$ from horotriangle cross-sections of SnapPy's quad-precision (`SnapPyHP`) ideal triangulations and assemble the $4\times 4$ Minkowski Gram matrices $G^{(t)}_{ab} = -2\lambda_{ab}^2$.
   - Verify intra-tetrahedron Penner consistency (`< 1e-12`), inter-tetrahedron face-gluing isometry (`< 1e-12`), and 24-cone cusp-desingularized Riemannian metric quadrature $\int_{\Delta_t} \sqrt{\det g(w)}\, d^3w$ matching exact Bloch–Wigner dilogarithm volumes $D(z_t)$ and `m004` Mostow volume $2.029883212819307$ to `< 1e-12`.
2. **3D Simplicial P1 Finite-Element Cover Equivalence Calibration on `b+-LR`:**
   - Construct the $100\%$ $S_4$-permutation-symmetric Eulerian tetrahedral subdivision ($\binom{n+2}{3}$ upward simplices, $\binom{n+1}{3}$ interior-split octahedra, $\binom{n}{3}$ downward simplices; total volume units $= n^3$).
   - Verify that:
     - The untwisted Neumann P1 Laplacian has exact constant zero mode $\lambda_0 = 0$ (`< 1e-12`) and assembled total mass $\mathbf{1}^T M \mathbf{1}$ converging smoothly to $\operatorname{Vol}_{\text{trunc}}(M)$.
     - The $\mathbb{Z}/5\mathbb{Z}$-twisted P1 Laplacian on the 2-tetrahedron base manifold `b+-LR` reproduces the charge-$q \in \{\pm 1, \pm 2\}$ sector of the untwisted P1 Laplacian on SnapPy's 10-tetrahedron 5-fold cyclic cover to `< 1e-12`.
3. **2D Topological Dirac Index Calibration (`Atiyah–Singer` & `Haar` Gate):**
   - Construct an explicit 2D staggered / overlap / covariant Fourier–Landau–Wilson Dirac operator on a magnetized 2-torus with integer first Chern number $c_1 \in \{-3, -2, -1, 0, +1, +2, +3\}$ and verify directly from singular-value kernels (`sval < 1e-10`) that $\dim\ker D_+ - \dim\ker D_- \equiv c_1$, invariant under random Haar unitary basis rotations (`< 1e-12`).

---

## 2. Gate 1: True 3D Pinched Throat vs. Uniform-Area Sol Mirror Split (`gate1_3d_twisted_throat.py`)
**Core Question:** In Phase 1, the uniform-area `Sol` torus-bundle model split `(6)` (`LLLLLLRLR`) at charge $q = \pm 1 \pmod 5$ into a 2-peak mirror pair around the $L^6$ stretch (`s* = [0.3009, 0.6991]`) and put $q = \pm 2$ at the anti-apex (`s* = 0.5`). On the **true cusped 3D hyperbolic manifold** $M_H$, where `b++LLLLLLRLR` develops a unique ultra-short Margulis geodesic ($\ell_1 \approx 0.18487$, `mult = 1`), does the $\mathbb{Z}/5\mathbb{Z}$-twisted 3D ground state localize into a **single unique peak** or remain **mirror-split**?

**Pre-Registered Tests:**
1. Evaluate both punctured-torus sign conventions `b++W_H` (monodromy $+W_H$) and `b+-W_H` (monodromy $-W_H$) across:
   - `(6)` (`LLLLLLRLR`), its enantiomer `(1, 6)` (`LRRRRRRLR`), `(2, 1, 2, 1, 2)` (`LLRLLRLLRLR`), `(2, 1, 1, 1, 2)` (`LLRLRLLRLR`), `(2, 1^8, 2)`, golden background `LR`, planted non-extending negative control `L^2 R L R` (`LLRLR`), and all $18$ bundle-extending histories of the bounded family `A6` ($\le 5$ runs, $\sum r_i \le 8$, $k=1$).
2. For each manifold admitting the golden $\mathbb{Z}/5\mathbb{Z}$ bundle (either directly as a rank-1 torsion character in $H^1(M_H; \mathbb{Z}/5\mathbb{Z})$ when $5 \mid |H_1(M_H)_{\text{tors}}|$, or via its canonical rank-2 unitary $D_5$-bundle / base-circle 2-fold cover when $W_H^T v \equiv -v$ on `b++` or $+v$ on `b+-`), test:
   - Both the unique **cusp-unramified** torsion character (`5 cusps` in 5-fold cover, zero peripheral cusp holonomy) and the **cusp-ramified** torsion characters (`1 cusp` in 5-fold cover), at charges $q = \pm 1$ and $q = \pm 2 \pmod 5$, across mesh resolutions $N_{\text{sub}} \in \{3, 4, 5\}$.
   - Compute:
     - Ground eigenvalue $E_0$, next distinct eigenvalue $E_1$, relative spectral gap $(E_1 - E_0)/E_0$, and ground-eigenspace multiplicity;
     - Layer-by-layer 3D probability distribution $P_t = \int_{\Delta_t} \sqrt{\det g}\, |\psi_0|^2 d^3w$ across the $N_{\text{let}}$ ideal tetrahedra ($t = 0, \dots, N_{\text{let}}-1$) along $S^1$, identifying the number of distinct circular probability peaks, peak location $t^* / N_{\text{let}}$, and overlap with the thin Margulis-hinge tetrahedra vs. thick anti-apex tetrahedra;
     - Exact closed-geodesic holonomy check: whether the shortest Margulis geodesic $\gamma_{\min} \subset M_H$ lifts in the 5-fold torsion cover to `1` closed geodesic of length $5\ell(\gamma_{\min})$ (charged core) or `5` disjoint geodesics of length $\ell(\gamma_{\min})$ (uncharged core).

---

## 3. Gate 2: Mostow Topological Rigidity Readout (`gate2_mostow_rigidity_readout.py`)
**Core Question:** Since 1-loop homogeneous torus potentials (`BE-3`) cannot stabilize an interior $\tau$ off $\{i, \omega\}$, what exact dimensionless geometric invariants are **topologically locked with zero continuous parameters** by Mostow–Prasad rigidity on the cusped 3-manifolds $M_H$ across all $18$ bundle-extending histories in `A6`?

**Pre-Registered Tests:**
1. Extract in quad precision (`SnapPyHP`) for every extending history $H \in A_6$ (under both `b++` and `b+-`):
   - Hyperbolic volume $\operatorname{Vol}(M_H)$ and Chern–Simons invariant $\operatorname{CS}(M_H) \in [-1/4, 1/4)$ (with complex volume $\operatorname{Vol}(M_H) + i\, 2\pi^2 \operatorname{CS}(M_H)$);
   - Canonical shortest-meridian cusp conformal modulus $\tau_{\text{cusp}}(M_H) \in \mathbb{H}$ and its $\operatorname{PSL}(2,\mathbb{Z})$ fundamental-domain image $\tau_{\text{cusp},\mathcal{F}}(M_H)$;
   - Shortest closed geodesic (Margulis throat) complex length $\lambda_1(M_H) = \ell_1 + i\theta_1$ and associated complex tube modulus $\tau_{\text{tube}}(M_H) := \frac{\theta_1 + i\ell_1}{2\pi}$ (and dual $\frac{2\pi i}{\ell_1 - i\theta_1}$);
   - Ground-state expectation readout $\langle \tau_{\text{pleated}} \rangle_{\psi_0} = \sum_{t=0}^{N_{\text{let}}-1} P_t\, \tau_{\mathcal{F}}(\Delta_t)$ weighted by the 3D twisted ground state $P_t$ from Gate 1.
2. Evaluate **Selection (`A-one`)** (minimum hyperbolic volume $\operatorname{Vol}(M_H)$ and minimum word length) and **Aggregation (`A-all`)** (volume-weighted $\sum_H e^{-\operatorname{Vol}(M_H)} (\cdot)$ and complex-volume / Chern–Simons weighted $\sum_H e^{-\operatorname{Vol}(M_H) - 2\pi i \operatorname{CS}(M_H)} (\cdot)$), reporting honestly whether `A-one` uniquely isolates a history or an enantiomeric pair $\{(6), (1,6)\}$, and what exact numbers emerge without comparing against or fitting any empirical target.

---

## 4. Gate 3: Topological Handedness & 4D Chiral Matter Index (`gate3_topological_chirality.py`)
**Core Question:** Phase 1 (`BE-4`) proved that across the entire 46D $\mathfrak{u}(3)_c$-neutral core of $\mathfrak{e}_8$, every static algebraic background gives `0` net 4D conjugate chiral index on $(\mathbf{16},\mathbf{4}) \oplus (\overline{\mathbf{16}},\overline{\mathbf{4}})$, and leaves $w_L$ vs. $w_R$ in an exact $\mathbb{Z}_2$ parity tie. What **minimal topological ingredients** break both ties?

**Pre-Registered Tests:**
1. **Explicit 2D Gauged Dirac / Atiyah–Singer Flux Theorem on $\mathfrak{e}_8$ (`248`):**
   - Enforce global $E_8$ bundle integrality (`<alpha, H_flux> in Z` for all $240$ explicit $E_8$ roots $\alpha \in \Phi(E_8)$, i.e. $H_{\text{flux}} \in \Lambda_R(E_8)$).
   - Construct the explicit 2D gauged Dirac operator on $T^2$ coupled to $H_{\text{flux}}$ across all 128 spinor states $(\mathbf{16},\mathbf{4}) \oplus (\overline{\mathbf{16}},\overline{\mathbf{4}})$ and compute the net 4D chiral zero-mode index directly from matrix singular values (`sval < 1e-10`), verified invariant under random Haar unitary rotations (`< 1e-12`).
   - Exhaustively classify all $E_8$-integral coroots $H_{\text{flux}} \in \Lambda_R(E_8)$ commuting with:
     - **(a) Full $\mathfrak{so}(10) \oplus \mathfrak{su}(3)_c$:** Test whether a smooth $T^2$ $\mathfrak{u}(1)_{B-L}$ coroot can yield family-universal $\mathbf{16}$ multiplicities (`N_gen(quark) == N_gen(lepton)`), or hits an exact `1 : 3` quark-to-lepton lattice obstruction!
     - **(b) $\mathfrak{su}(5)_{\text{GUT}} \oplus \mathfrak{su}(3)_c$ / Standard Model gauge algebra $\mathfrak{su}(3)_c \oplus \mathfrak{su}(2)_L \oplus \mathfrak{u}(1)_Y$:** Determine the exact minimal family-universal chiral index achievable by a globally valid $E_8$ coroot flux on $T^2$ vs. punctured/orbifold holonomy.
2. **Atiyah–Patodi–Singer (APS) Chiral Boundary / Domain-Wall Defect Test on $[0, L] \times S^1$:**
   - Construct the explicit 1D/2D cusp-throat Dirac operator with chiral boundary / Callan–Rubakov mass-step profile coupled to the $E_8$ spinor block and compute its explicit spectral kernel asymmetry (`dim ker D_+ - dim ker D_-`), comparing sealed periodic boundary (`must = 0`) vs. chiral APS boundary (`!= 0`).
3. **3D Spatial Handedness vs. Weak $w_L / w_R$ Parity Test (`M_H` vs. Mirror `-M_H`):**
   - Prove numerically on the explicit 3D hyperbolic triangulation that pure parity-even 3D Yang–Mills–Higgs kinetic + potential energy $\int_{M_H} \sqrt{\det g}\, (\dots)$ leaves $\mathfrak{so}(5)_+$ ($w_L$ broken) and $\mathfrak{so}(5)_-$ ($w_R$ broken) degenerate (`diff < 1e-12`), even on chiral `b++LLLLLLRLR`.
   - Test parity-odd 3D topological Chern–Simons coupling $\operatorname{CS}(M_H)$ across `LR` (amphicheiral negative control: $\sin(4\pi\operatorname{CS}) = 0$, tie unbroken), `(6)` (`b++LLLLLLRLR`: $\sin(4\pi\operatorname{CS}) < 0$), and mirror `(1, 6)` (`b++LRRRRRRLR`: $\sin(4\pi\operatorname{CS}) > 0$, exact opposite sign to `< 1e-12`), establishing whether weak handedness reduces to the 1-bit orientation choice between enantiomers `(6)` and `(1, 6)`.
