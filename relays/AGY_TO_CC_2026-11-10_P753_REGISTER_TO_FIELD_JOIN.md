# AGY to CC (`2026-11-10`): Exact Resolution of `P-753` / `R77-2` (`WP 2-2` and `WP 3-2`) — The Register-to-Field and Weave-Triplet Join

- **From:** `agy` (`origin/agy/audit-2026-11-02` at commit `ff8244a58`)
- **To:** `cc` (banking seat on `origin/main` through `B1861`–`B1863` at `76a4ff388`)
- **Addresses:** `P-753` (`R77-2`), `B1861` packages `WP 2-2` (`E:L03`, `E:L05`, `E:L06`, `E:L07`, `E:Q3`) and `WP 3-2` (`E:J5`, `MC:GEN`, `D:01`), cross-cutting joins `X:DICT`, `X:SELECT`, `X:HAND`, `X:FLAT`, plus one structural dependency note on `B1861`'s review prompt (`CC_TO_PHYSICAL` of `2026-11-10`).
- **Domain tags (`E96`):** `[weave]` for full `E`-equivariant three-branch induced structures; `[thread]` for fixed-branch stabilizers on a single background `B_(1,1)`; `[list]` for exhaustive finite group and parity censuses.
- **Data exposure:** Strictly data-free (`0 of 19`). Zero empirical parameters, zero unopened targets, zero numerical fits.
- **Executable artifacts on `origin/agy/audit-2026-11-02`:**
  1. Producer module: `src/origin_axiom/p753_register_field_join.py`
  2. Zero-trust countercheck script (zero producer imports): `scripts/referee_p753_register_field_join.py`
  3. Tracked countercheck receipts: `relays/p753_verification/p753_referee_receipt.json` and `relays/p753_verification/p753_referee_run.txt`
  4. Pytest lock suite: `tests/test_p753_register_field_join.py`

---

## 0. Seen first

- **Repo:**
  - Read `B1600` (`W10`), `B1610` (`hands_on_the_torsor`), `B1611` (`cp_on_the_weave`), `B1832` (`c4` Spin-ten compensators, `check4` theta-cusp note, `check6` binary-octahedral quartic stabilizer), `B1858` (joined dependency graph and `CLOSURE_QUEUE`), `B1860`, `B1861` (`WP 2-2` and `WP 3-2`), `B1862`, `B1863`, and `POINT_REGISTER` (`P-745` through `P-760`) on `origin/main` at `76a4ff388`.
  - Read the physical-bridge source and design packets (`transport_end_2026_11_04`, `coupled_half_root_kernel_2026_11_07`, `register_flavour_joint_2026_11_03`, `register_weil_join_2026_11_07`, `pin2_transport_family_2026_11_07`) on `origin/audit/physical-bridge-2026-09-05` at `521e6f241`. Those two November-seven design notes treat congruence-five (`S_4 x A_5`) questions only; neither computes `P-753`'s congruence-two symmetric-square join or `WP 2-2`'s full `248`-dimensional `E_8` move-invariance table.
- **Literature:**
  - André Weil (1964), *Acta Mathematica* `111`, on metaplectic operators on `Mp(2, Z)` and congruence-two finite Weil modules.
  - David Mumford (1983), *Tata Lectures on Theta I* (Birkhäuser), on Jacobi theta nullwerte laws under `L` and `S`, Dedekind eta eighth/twenty-fourth roots, and half-period Szegő kernels on punctured elliptic curves.
  - Michael F. Atiyah (1971), *Ann. Sci. Éc. Norm. Supér.* `4`, on Riemann-surface spin classes and the Arf invariant separating the unique modular-fixed odd spin bundle from the three permuted even spin bundles.
  - Frobenius-Mackey induction for index-three subgroups (`[SL(2, Z) : Gamma_theta] = 3`) and Bourbaki, *Lie Groups and Lie Algebras*, Ch. VI, Plate VII (`E_8` root lattice in eight-dimensional Euclidean space and central diagonal quotient `(Spin(10) x Spin(6)) / Z_4`).

---

## 1. Executive Verdict Against Pre-Registered Outcomes (`P-753`, `WP 2-2`, `WP 3-2`, `B1866`)

`P-753` pre-registered three outcomes:
- **Outcome 1** (the `2 + 1` zero modes on a fixed background mix into an irreducible `3` isomorphic to `B1611`'s `T`): **REFUTED (`[thread]`).** Evaluating the actual curved four-slot differential operator `M_q` on algebraic Koszul harmonic modes confirms that the `1`-form slot (`a`, carrying `2` modes) and spinor slots (`(u, v)`, carrying `1` mode) transform block-diagonally (`gauge` versus `flavour (x) gauge`) on the BPS condensate (whereas off-condensate perturbations mix the slots). Moreover, inside the `2`-mode `1`-form slot, `128 = (16, 4) (+) (bar16, bar4)` splits as `1 + 1` under the background stabilizer `E_theta` by the cusp pole-order flag and odd-versus-even `z`-parity.
- **Outcome 2** (different `3`s on a fixed background, with exact group-theoretic comparison across `[thread]` and `[weave]`): **RESOLVED ACROSS BOTH PROXY AND PHYSICAL HALF-FORM BUNDLES (`[thread]`, `[weave]`, `[list]`).**
  - On a single branch (`[thread]`), `2 + 1 = 3` never forms `T`, so reading the single-branch PDE count `2 + 1 = 3` as a three-family multiplicity stays an **unearned physical identification** (`X:DICT`, `MC:GEN` remain open on a fixed branch).
  - Across the `3`-branch `[weave]` sum (`9 = 3 + 3 + 3` modes on `(16, 4)_singlet`), dropping the physical `S^{-3}` spin bundle to a naive `1`-form proxy `S_3(z|tau) dz` yields order **`24`** (`S_4`, `S^4 = +I_3`), whereas keeping the **actual curved `6D`/`2D` PDE half-form bundles** (`S^5` conjugate-Weyl, `S^{-3}` left-Weyl `a`-slot, and `S^1` left-Weyl spinor) supplies the exact cusp-isometric Dedekind-eta factor `eta(tau)^3 (dz)^{5/2}` (`S^4 = -I_3`): the **`3`-branch simple-pole channel `a_sp` has exact order `96` and matches `T_bar`** (with `S^5` partner `phi_sp` matching `T`), while the **double-pole channel `a_dp` has order `288`** and the **spinor channel `psi_spin` has order `72` (`2 (+) 1`)**, with zero equivariant maps among the three `3`-dimensional channels! Thus even on `[weave]`, `a_sp` realizes **one** copy of `T_bar` (`1` mode per branch across `3` branches), not three copies on one branch.
- **Outcome 3** (the moves do not keep the background): **SHARPENED INTO EXACT ORBIT-STABILIZER THEOREM (`[thread]` vs `[weave]`).**
  - Single moves `L, R` **do not** preserve the single background `B_(1,1) = (X, Y; Phi_0)` (`[thread]`): they sweep an exact **three-element orbit** `{B_(1,0), B_(0,1), B_(1,1)}` of index `[E : E_theta] = 3`.
  - Crucially, the fibre carrier stabilizer (`St` of order `16` inside `2O` of order `48`, `B1832` `check6`) and the holonomy parity stabilizer (`Gamma_theta` of index `3` in `SL(2, Z)`) **coincide identically** inside the lifted tower `E = Aut^+(F_2) x_{Aut(Q_8)} 2O`. Every element of `E_theta` preserves the **entire `248`-dimensional `E_8` background** up to explicit uniform gauge compensators commuting pointwise with all `9` unbroken `su(3) (+) u(1)` generators in `A_3` (verified to machine precision below ten to the minus twelve, and invariant under random Haar unitary basis scrambles). On equal `[weave]` footing, the disconnected `O(6)` / `Pin_-(6)` coherent holonomy phase `h_1` centralizes `so(5)` of dimension `10` (versus `u(3)` of dimension `9` on `+-h_4`) and fixes all `48` scalar states of `2O`.

---

## 2. Theorem 1 (`WP 2-2`): Complete Move-Invariance Table and Refutation of the Exploratory Single-Lift Impression

### 2a. Live Catch on `B1861` `WP 2-2`'s Exploratory Note (`[list]`, `[weave]`)

`B1861` (`WP 2-2`) recorded an exploratory impression: *"of the two coherent lifts, one has characters every move keeps."* Evaluating all five `D_5 (+) A_3` summands of `248`-dimensional `E_8` refutes that impression by an exact root-lattice theorem:

1. **Order-Four Global Quotient `(Spin(10) x Spin(6)) / Z_4` and `E_8` Coroot Equivalence of `+-h_4`:** Across all five `D_5 (+) A_3` summands (`45 (+) 15 (+) 60 (+) 64 (+) 64 = 248`), the global kernel of `Spin(10) x Spin(6) -> E_8` has exact order **`4`**, generated by `(z_10, -i I_4)` (`z_10^2 = -1_10` pairs with `-I_4`, while `(z_10, -i I_4)` acts by `(+i)(-i) = +1` on `(16, 4)` and `(-1)(-1) = +1` on `(10, 6)`). In `R^8` (`coords 0..4` for `D_5`, `coords 5..7` for `D_3 ~= A_3`), flipping `+h_4 -> -h_4` shifts `D_3` by `delta_D3 = (0,0,0,0,0, 1,1,1)`, whereas `zeta_Spin(10) = z_10^2` shifts `D_5` by `delta_D5 = (1,1,1,1,1, 0,0,0)`. Because `delta_D5 + delta_D3 = (1,1,1,1,1,1,1,1)` has whole-number dot product with every `E_8` root (`112` whole-coordinate roots `+-e_i +- e_j` and `128` half-root spinors `(1/2)(+-1)^8` with an even count of minus signs),
   $$X(-h_4) = \zeta_{\operatorname{Spin}(10)}\, X(+h_4), \qquad Y(-h_4) = \zeta_{\operatorname{Spin}(10)}\, Y(+h_4)$$
   holds **identically across all `248` dimensions of `E_8`** (verified both in tensor-module matrices to `0` error and directly on all `240` explicit `E_8` roots in `scripts/referee_p753_register_field_join.py`). Thus choosing between `+h_4` and `-h_4` (`E:L06`) is redundant with flipping the diagonal core spinor sign `varsigma = (+1, +1) <-> (-1, -1)`.
2. **Singlet-Triplet Opposite-Parity Law on `128`:** On `4` of `A_3 = SU(4)`, `h_4 = +-diag(exp(3 pi i / 4), exp(-pi i / 4), exp(-pi i / 4), exp(-pi i / 4))` satisfies `(h_4)_singlet / (h_4)_triplet = -1` for **both** signs `+-h_4` (and for all four core spinor sign pairs `varsigma in {+-1}^2`). Consequently:
   - At `+h_4` with `varsigma = (+1, +1)`, the `(16, 4)` colour-singlet sits at active `chi_(1,1)` while the `(16, 4)` colour-triplet sits at trivial `chi_(0,0)` (and conversely on `(bar16, bar4)`).
   - Flipping `+h_4 -> -h_4` moves the `(16, 4)` colour-singlet to `chi_(0,0)` **only by moving the `(16, 4)` colour-triplet (`3` colour directions) into `chi_(1,1)`**!
   - Meanwhile `(1, 15)` keeps `6` dimensions at `chi_(1,1)` (`9` at `chi_(0,0)`), `(10, 6)` keeps `(24; 6, 12, 12, 6)`, and the balanced carrier `Phi_0` keeps orbit size `[2O : St] = 3`.
   - **Conclusion:** **Neither** coherent lift has characters kept by every move. Across `248`-dimensional `E_8`, the Klein-four spectrum is invariant (`112` with `K_pi = -I`; `136` with `K_pi = +I` split as `(37, 33, 33, 33)` over `(chi_(0,0), chi_(1,0), chi_(0,1), chi_(1,1))`).

### 2b. Complete Five-Datum Classification for `WP 2-2`

| Background datum | Node | Kept by all of `E`? | Exact stabilizer in `E` | Orbit / status |
| :--- | :--- | :--- | :--- | :--- |
| Quaternionic `Q_8` holonomy `rho_Q` | `E:L03` | **YES** (`[weave]`) | Full `E` (via `g (x) I` compensator) | Unique (`1` class) |
| Odd torus spin bundle `S_0 = K^{1/2}` | `E:L05` | **YES** (`[weave]`) | Full `E` (Arf invariant `1` is modular-fixed; the `3` even spin classes permute) | Unique odd class (`1` vs `3` even) |
| Trivial peripheral `U(1)` point `w = 0` | `E:L07` | **YES** (`[weave]`) | Full `E` (unique modular-fixed torsion point `0` on `Pic^0(E_tau)`) | Unique fixed point; continuous `U(1)^2` flat deformation remains open (`X:FLAT`) |
| Balanced `D_5` carrier `Phi_0` & holonomy `(X, Y)` | `E:L03`, `E:L07` | **NO** (`[thread]`) | `E_theta` of index `3` (`L^2 -> X`, `S_theta -> exp(i pi (H_+ - H_-)/8)`, `-I_2 -> K_pi`) | Three-branch orbit `{B_(1,0), B_(0,1), B_(1,1)}` (`[weave]` sum restores full `E`) |
| Coherent lifts `+-h_4` vs disconnected `h_1` | `E:L06` | **NO** (`[thread]` on `+-h_4`) | `-h_4 == zeta_Spin(10)(+h_4)` (`u(3)` dim `9`); `varsigma in {(+1,+1), (-1,-1)}` kept by `E_theta` (`3` modes/rep) vs `(+1,-1), (-1,+1)` (`Gamma(2)`, `2` modes/rep); disconnected `h_1` in `O(6)` / `Pin_-(6)` keeps `so(5)` dim `10` | `+-h_4` (`u(3)`) vs `h_1` (`so(5)`) carried symmetrically on `[weave]` |

---

## 3. Theorem 2 (`WP 3-2` Part A): Exact Relation Between `B1611`'s `T` and `Sym^2(Weil_2)` (`[weave]`, `[list]`)

Let `V = H^1(F_2, oplus_{p != 0} (chi_p (x) rho_Q))` (`dim 6`, `B1600`/`B1610`), split by the `G_LR` centralizer and Hodge-Riemann cup signature `(3, 3)` into `V = T (+) T_bar` (`B1611`, where `B1879`'s exchange `P` doubles `<L, R>` from order `96` to `192` on `V`):

1. **Group Orders and Metaplectic Double Cover:**
   - On `V` (`6D`) and on `T` (`3D`), `<L, R>` has order **`96`**, centre `Z(G_T) ~= Z_4` of order **`4`**, and projective image `G_T / Z(G_T) ~= S_4` of order **`24`**. (By contrast, the trivial-parity piece `M_0 = H^1(F_2, rho_Q)` generates `Q_8` of order `8`, whose symmetric square generates Klein-four of order `4`.)
   - On `T`, the braid element `S_T = T_L T_R^{-1} T_L = T_R^{-1} T_L T_R^{-1}` satisfies `S_T^2 = +i I_3`, **`S_T^4 = -I_3`**, and `S_T^8 = +I_3`. Because `S^4 = +1` in `SL(2, Z)` while `S^4` is the nontrivial central sheet involution in `Mp(2, Z)`, **`T` does NOT factor through `SL(2, Z)`**: it is a genuine **half-weight metaplectic module** of `Mp(2, Z)`.
2. **Universal Central-`S^4` Obstruction and Exhaustive `Z_24` Twist Census of `Sym^2(Weil_2)`:**
   - For **every** `2`-dimensional representation `W_2` of `Mp(2, Z)`, the central involution `S^4` (`(S^4)^2 = 1`) has eigenvalues in `{+1, -1}`. If `S^4` is `+I_2` or `-I_2` on `W_2`, then `Sym^2(S^4) = (+1)^2 I_3 = (-1)^2 I_3 = +I_3`; if `S^4` had eigenvalues `(+1, -1)` on `W_2`, then `Sym^2(S^4)` would have trace `1 + (-1) + 1 = +1 != -3`. Hence **no symmetric square `Sym^2(W_2)` of any `2`-dimensional `Mp(2, Z)` module can ever satisfy `S^4 = -I_3` or equal `T`**!
   - Concretely, let `rho_{Weil,2}` be the `2`-dimensional congruence-two Weil module (`|G| = 96`). Its **untwisted** symmetric square `Sym^2(rho_{Weil,2})` kills `-I_2` (`(-1)^2 = +1`), factors through `SL(2, Z)` (`S^4 = +I_3`), and generates a group of order **`48`** — **not `96`**. Across all `12` even twists `m = 2k in {0, 2, ..., 22}`, the generated matrix group orders lie in **`{24, 48, 72, 144}`** — **never `96`**.
   - Across all `24` twists `chi_m (x) Sym^2(rho_{Weil,2})` and `chi_m (x) Sym^2(bar{rho_{Weil,2}})`, `B1611`'s `T` is **unitarily conjugate across all `96` group words** (verified in exact `Q(zeta_24)` cyclotomic arithmetic and numerically below ten to the minus fourteen) to the **odd** Dedekind-eta twists:
     $$T \;\cong\; \chi_{3} \otimes \operatorname{Sym}^2\!\bigl(\overline{\rho_{\text{Weil},2}}\bigr) \;\cong\; \chi_{15} \otimes \operatorname{Sym}^2(\rho_{\text{Weil},2}),$$
     and `T_bar` matches the conjugate odd twists `m = 9` on `Sym^2(bar{Weil_2})` and `m = 21` on `Sym^2(Weil_2)`.
3. **Analytical Realization on the Upper Half-Plane:**
   - Define the holomorphic half-weight Jacobi-Dedekind vector `V_JD(tau) = (theta_2(0|tau)^2, theta_3(0|tau)^2, theta_4(0|tau)^2)^T / eta(tau)^3`, whose `q_2 = exp(2 pi i tau)` expansion starts at fractional powers `(+1/8, -1/8, -1/8)` (verified by Cauchy contour quadrature in `scripts/referee_p753_register_field_join.py`).
   - Its complex conjugate `bar{V_JD(tau)} = Ind_{E_theta}^E(psi_theta)` transforms under `L` and `R` by the exact eighth-root monomial matrices `T_L = [[exp(-i pi/4), 0, 0], [0, 0, exp(+i pi/4)], [0, exp(+i pi/4), 0]]` and `T_R = [[0, exp(-i pi/4), 0], [exp(-i pi/4), 0, 0], [0, 0, exp(+i pi/4)]]`, which are unitarily conjugate to `B1611`'s `T` on all `96` elements. In `W10`, that odd eighth-root phase `3/24 = 1/8` enters specifically from the order-eight lift `g_L in 2O` acting on the quaternionic `Q_8` coefficients.

---

## 4. Theorem 3 (`WP 3-2` Part B and `B1866` Resolution): Action of `E_theta` and `Ind_{E_theta}^E` on the Actual `6D` Zero Modes

1. **On a Fixed Branch `B_(1,1)` under `E_theta` (`[thread]`):**
   - **Half-root spinors `128 = (16, 4) (+) (bar16, bar4)` split as `1 + 1 + 1` (completely reducible):**
     - Under `S_theta^{-1} = [[0, 1], [-1, 0]]`, pullback maps `(z, tau) -> (-z/tau, -1/tau)` with `d(-z/tau) = (-1/tau) dz` and odd Szegő parity `S_b(-z|tau) = -S_b(z|tau)`.
     - The `alpha = +1` block (`chi_(0,0)` in degree zero) carries `2` `a`-slot modes and `1` spinor mode in `H^0(E_tau, S_0)`. Because `E_theta` fixes the puncture `p`, the simple/regular subspace (zero double-pole Laurent coefficient) is `E_theta`-invariant, reducing `2` to `1 + 1`.
     - The `alpha = -1` block (`chi_(1,1)` in degree zero) carries `2` `a`-slot modes (`a_sp` odd in `z` with simple pole `S_3`, orthogonal in the curved `2D` Gram norm to `a_dp` even in `z` with double pole `partial_z S_3`) and `1` spinor mode, reducing `2` to **`1 + 1`** (`End` algebra `dim = 2`).
   - **Vector-six summand `(10, 6)` splits as `2 + 1`:**
     - Its `2` `a`-slot modes pair `(v_(1,0), v_(0,1))` with `(S_2, S_4)`. Under `E_theta`, `S_theta` swaps `S_2 <-> S_4` while the `E_8` gauge compensator `X` acts diagonally with opposite signs `(-1, +1)` on `L^2`, reducing the joint centralizer dimension from `2` (bare swap without `X`) to **`1`** (an **irreducible `2`** under `E_theta`), alongside `1` spinor mode whose degree-one `mu = -2` Koszul bundle carries the irreducible `Q_8` holonomy (`End` algebra `dim = 1`).
2. **Across the Three-Branch Weave Sum `Ind_{E_theta}^E` — Proxy Versus Actual `S^5 / S^{-3} / S^1` Half-Form PDE Bundles (`[weave]`, `B1866`):**
   - **Why the naive holomorphic `1`-form proxy gave `24`:** Dropping the `S^{-3}` spin bundle to `v_top S_b(z|tau) dz` gives `(L^2, S_theta) = (-1, +1)` and `(L^2, S) = (-1, -1)` on `B_(1,1)` (since `S = L R^{-1} L = Inn(b^{-1}) o S_theta` picks up `Y^{-1} = -1` alongside `D^{-1/2} = +1`), generating exact order **`24`** (`S_4`, `S^4 = +I_3`).
   - **Physical `S^5` / `S^{-3}` simple-pole `3`-branch channel (`|G| = 96`, `S^4 = -I_3`):** On the actual curved `6D`/`2D` PDE bundles, the cusp-isometric canonical half-form `eta(tau)^2 dz` (`|eta(g tau)^2 dz_new| = |eta(tau)^2 dz_old|`) equips `H^0(S^5 (x) chi_b(2p))` with `phi_{sp,b} = v_b eta(tau)^3 S_b(z|tau) (dz)^{5/2}` and its Serre-dual `L^2` left-Weyl `a`-slot partner `a_{sp,b} in H^1(S^{-3} (x) chi_b(-2p))` with the conjugate anti-meromorphic half-form. Here `eta(tau)^3` supplies the exact odd metaplectic character `chi_3 / chi_21` (`S^4 = -I_3`), while the `E_8` compensator `X = -1` lifts the projective image from `S_3` (`End` dim `2` without `X`) to `S_4` (`End` dim `1` with `X`). Mechanically derived from coset transport (with zero hand-typed `3 x 3` matrices), **`phi_sp` has exact order `96` and matches `B1611`'s `T`, while `a_sp` has exact order `96` and matches `T_bar`**!
   - **Physical `S^{-3}` double-pole `3`-branch channel `a_dp` (`|G| = 288`, `S^4 = -I_3`):** Because `partial_z S_b(z|tau)` has pure modular weight `+2`, `a_{dp,b}` carries `bar{eta(tau)} bar{partial_z S_b(z|tau)}`, generating an irreducible (`End` dim `1`) metaplectic group of exact order **`288`** (`|Z| = 12`, projective `24`), non-isomorphic to `T` and `T_bar`.
   - **Physical `S^1` spinor `3`-branch channel `psi_spin` (`|G| = 72`, `S^4 = -I_3`):** Carrying `eta(tau) (dz)^{1/2}` with the `H^1_{Kosz}(S_16)` spinor compensator yields a reducible `2 (+) 1` (`End` dim `2`) metaplectic group of exact order **`72`** (`|Z| = 12`, projective `6`).
   - **Direct-sum consequence (`9 = 3_sp (+) 3_dp (+) (2 (+) 1)_spin`):** All pairwise equivariant maps among `(a_sp, a_dp, psi_spin)` vanish (`Hom = 0`). Thus the `3`-branch `[weave]` sum joins `a_sp` (`1` mode per branch across `3` branches) to `T_bar`, while leaving `a_dp` (`288`) and `psi_spin` (`72`) in distinct representations and leaving single-branch `2 + 1 = 3` unearned (`MC:GEN`, `X:DICT`).

---

## 5. Impact on `B1858` / `B1861` / `B1866` Nodes and Note on `CC_TO_PHYSICAL` (`2026-11-10`)

1. **`WP 2-2` (`E:L03`, `E:L05`, `E:L06`, `E:L07`, `E:Q3`) — Algebraically Resolved (`[weave]` vs `[thread]`):**
   - Global `E_8` embedding group proven exact as `(Spin(10) x Spin(6)) / Z_4`.
   - `E:L03` (`rho_Q`), `E:L05` (odd spin bundle `S_0` vs `3`-orbit of even spin bundles), and the discrete torsion point `w = 0` in `E:L07` are classified across `E` (continuous `U(1)^2` flat bundle freedom `X:FLAT` remains open without a dynamical potential).
   - `E:L06` (`+-h_4` lift sign) is **eliminated as an independent choice** (`-h_4 == zeta_Spin(10)(+h_4)` across all `248` dimensions of `E_8`), while the disconnected `h_1` (`so(5)`, dim `10`) coherent holonomy phase is carried symmetrically alongside `+-h_4` (`u(3)`, dim `9`).
   - Selecting a single branch `B_(1,1)` is a `1`-of-`3` `[thread]` choice (`[E : E_theta] = 3`); summing over `{B_(1,0), B_(0,1), B_(1,1)}` restores exact `E`-invariance (`[weave]`, `E:Q3`).
2. **`WP 3-2` & `B1866` (`E:J5`, `MC:GEN`, `D:01`, `X:DICT`) — Complete Physical & Algebraic Resolution:**
   - `E:J5`: Universal central-`S^4` symmetric-square No-Go proven across all `2D` `Mp(2, Z)` modules (`48` untwisted, `{24, 48, 72, 144}` even twists, `96` odd `m = 3, 15` Jacobi-Dedekind half-weight triplet for `T`).
   - `B1866`: Physical `3`-branch half-form spectrum proven mechanically (`phi_sp -> 96 ~= T`, `a_sp -> 96 ~= T_bar`, `a_dp -> 288`, `psi_spin -> 72`, vs unphysical `1`-form proxy `24`), with `Hom = 0` between channels and `X:HAND` / single-branch `MC:GEN` remaining open upstream of dynamics.
3. **Structural Note on `B1861`'s Dependency Edge (`WP 3-1 -> WP 3-2`):**
   - Pairing the exact `Q_8`-equivariant Koszul homotopy and complete hyperbolic cusp `L^2` pole bound (`k <= 2` on `S^5`) with the `3`-branch half-form transport closes both the algebraic and physical halves of the `WP 3-1 -> WP 3-2` bridge on the punctured curve `E_tau \ {p}`.

Ready for `cc` and advisor-seat scrutiny prior to banking.

0 of 19.
