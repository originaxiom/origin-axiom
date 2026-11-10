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
  - Frobenius-Mackey induction for index-three subgroups (`[SL(2, Z) : Gamma_theta] = 3`) and Bourbaki, *Lie Groups and Lie Algebras*, Ch. VI, Plate VII (`E_8` root lattice in eight-dimensional Euclidean space and central diagonal gluing `(Spin(10) x Spin(6)) / Z_2`).

---

## 1. Executive Verdict Against Pre-Registered Outcomes (`P-753`, `WP 2-2`, `WP 3-2`)

`P-753` pre-registered three outcomes:
- **Outcome 1** (the `2 + 1` zero modes on a fixed background mix into an irreducible `3` isomorphic to `B1611`'s `T`): **REFUTED (`[thread]`).** The `1`-form slot (`a`, carrying `2` modes) and spinor slots (`(u, v)`, carrying `1` mode) transform diagonally (`gauge` versus `flavour (x) gauge`) with exact zero off-block coupling (`norm = 0`). Moreover, even inside the `2`-mode `1`-form slot, `128 = (16, 4) (+) (bar16, bar4)` is reducible (`1 + 1`) under the background stabilizer `E_theta` by the cusp pole-order flag.
- **Outcome 2** (different `3`s on a fixed background, with exact group-theoretic comparison): **HOLDS ON FIXED BACKGROUND (`[thread]`, `[list]`), AND EXTENDS TO THE THREE-BRANCH ORBIT (`[weave]`).** Neither `2 + 1 = 3` on a single branch nor the `3`-branch induced spaces on `128` equal `B1611`'s `96`-element weave triplet `T`. Consequently, reading the per-branch PDE index `2 + 1 = 3` as a three-family count stays an **unearned physical identification** (`X:DICT`, `MC:GEN` remain open unless a dynamical coupling maps the slot multiplicity to a physical observable).
- **Outcome 3** (the moves do not keep the background): **SHARPENED INTO EXACT ORBIT-STABILIZER THEOREM (`[thread]` vs `[weave]`).**
  - Single moves `L, R` **do not** preserve the single background `B_(1,1) = (X, Y; Phi_0)` (`[thread]`): they sweep an exact **three-element orbit** `{B_(1,0), B_(0,1), B_(1,1)}` of index `[E : E_theta] = 3`.
  - Crucially, the fibre carrier stabilizer (`St` of order `16` inside `2O` of order `48`, `B1832` `check6`) and the holonomy parity stabilizer (`Gamma_theta` of index `3` in `SL(2, Z)`) **coincide identically** inside the lifted tower `E = Aut^+(F_2) x_{Aut(Q_8)} 2O`. Every element of `E_theta` preserves the **entire `248`-dimensional `E_8` background** up to explicit uniform gauge compensators commuting pointwise with all `9` unbroken `su(3) (+) u(1)` generators in `A_3` (verified to machine precision below ten to the minus twelve, and invariant under random Haar unitary basis rotations).

---

## 2. Theorem 1 (`WP 2-2`): Complete Move-Invariance Table and Refutation of the Exploratory Single-Lift Impression

### 2a. Live Catch on `B1861` `WP 2-2`'s Exploratory Note (`[list]`, `[weave]`)

`B1861` (`WP 2-2`) recorded an exploratory impression: *"of the two coherent lifts, one has characters every move keeps."* Evaluating all five `D_5 (+) A_3` summands of `248`-dimensional `E_8` refutes that impression by an exact root-lattice theorem:

1. **`E_8` Coroot Equivalence of `+-h_4` and `zeta_Spin(10)`:** In `R^8` (`coords 0..4` for `D_5`, `coords 5..7` for `D_3 ~= A_3`), flipping `+h_4 -> -h_4` shifts the `D_3` maximal-torus angle by `delta_D3 = (0,0,0,0,0, 1,1,1)`, whereas the `Spin(10)` centre `zeta_Spin(10)` shifts `D_5` by `delta_D5 = (1,1,1,1,1, 0,0,0)`. Because `delta_D5 + delta_D3 = (1,1,1,1,1,1,1,1)` has whole-number dot product with every `E_8` root (`112` whole-coordinate roots `+-e_i +- e_j` and `128` half-root spinors `(1/2)(+-1)^8` with an even count of minus signs),
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
| Coherent lifts `+-h_4` & core spinor signs `varsigma` | `E:L06` | **NO** (`[thread]`) | `-h_4 == zeta_Spin(10)(+h_4)`; `varsigma in {(+1,+1), (-1,-1)}` kept by `E_theta` (`3` modes/rep), whereas `(+1,-1), (-1,+1)` break `S_theta` to index-six `Gamma(2)` (`2` modes/rep) | `2` diagonal `E_theta`-compatible sign classes vs `2` `S_theta`-broken classes |

---

## 3. Theorem 2 (`WP 3-2` Part A): Exact Relation Between `B1611`'s `T` and `Sym^2(Weil_2)` (`[weave]`, `[list]`)

Let `V = H^1(F_2, oplus_{p != 0} (chi_p (x) rho_Q))` (`dim 6`, `B1600`/`B1610`), split by the `G_LR` centralizer and Hodge-Riemann cup signature `(3, 3)` into `V = T (+) T_bar` (`B1611`):

1. **Group Orders and Metaplectic Double Cover:**
   - On `V` (`6D`) and on `T` (`3D`), `<L, R>` has order **`96`**, centre `Z(G_T) ~= Z_4` of order **`4`**, and projective image `G_T / Z(G_T) ~= S_4` of order **`24`**. (By contrast, the trivial-parity piece `M_0 = H^1(F_2, rho_Q)` generates `Q_8` of order `8`, whose symmetric square generates Klein-four of order `4`.)
   - On `T`, the braid element `S_T = T_L T_R^{-1} T_L = T_R^{-1} T_L T_R^{-1}` satisfies `S_T^2 = +i I_3`, **`S_T^4 = -I_3`**, and `S_T^8 = +I_3`. Because `S^4 = +1` in `SL(2, Z)` while `S^4` is the nontrivial central sheet involution in `Mp(2, Z)`, **`T` does NOT factor through `SL(2, Z)`**: it is a genuine **half-weight metaplectic module** of `Mp(2, Z)`.
2. **Exhaustive `Z_24` Twist Census of `Sym^2(Weil_2)`:**
   - Let `rho_{Weil,2}` be the `2`-dimensional congruence-two Weil module (`|G| = 96`). Its **untwisted** symmetric square `Sym^2(rho_{Weil,2})` kills `-I_2` (`(-1)^2 = +1`), factors through `SL(2, Z)` (`S^4 = +I_3`), and generates a group of order **`48`** — **not `96`**.
   - More generally, for **every** `2`-dimensional module `chi_k (x) rho_{Weil,2}` of `Mp(2, Z)` (`k in Z_24`), its symmetric square `chi_{2k} (x) Sym^2(rho_{Weil,2})` carries an **even** `Z_24` twist `m = 2k`. Across all `12` even twists `m in {0, 2, ..., 22}`, the generated matrix group orders lie in **`{24, 48, 72, 144}`** — **never `96`**. Thus `T` is **not** the symmetric square of *any* `2`-dimensional representation of `Mp(2, Z)`!
   - Across all `24` twists `chi_m (x) Sym^2(rho_{Weil,2})` and `chi_m (x) Sym^2(bar{rho_{Weil,2}})`, `B1611`'s `T` is **unitarily equivalent across all `96` group words** (conjugacy error below ten to the minus fourteen) to the **odd** Dedekind-eta twists:
     $$T \;\cong\; \chi_{3} \otimes \operatorname{Sym}^2\!\bigl(\overline{\rho_{\text{Weil},2}}\bigr) \;\cong\; \chi_{15} \otimes \operatorname{Sym}^2(\rho_{\text{Weil},2}),$$
     and `T_bar` matches the conjugate odd twists `m = 9` on `Sym^2(bar{Weil_2})` and `m = 21` on `Sym^2(Weil_2)`.
3. **Analytical Realization on the Upper Half-Plane:**
   - Define the holomorphic half-weight Jacobi-Dedekind vector `V_JD(tau) = (theta_2(0|tau)^2, theta_3(0|tau)^2, theta_4(0|tau)^2)^T / eta(tau)^3`, whose `q_2 = exp(2 pi i tau)` expansion starts at fractional powers `(+1/8, -1/8, -1/8)` (verified by Cauchy contour quadrature in `scripts/referee_p753_register_field_join.py`).
   - Its complex conjugate `bar{V_JD(tau)} = Ind_{E_theta}^E(psi_theta)` transforms under `L` and `R` by the exact eighth-root monomial matrices `T_L = [[exp(-i pi/4), 0, 0], [0, 0, exp(+i pi/4)], [0, exp(+i pi/4), 0]]` and `T_R = [[0, exp(-i pi/4), 0], [exp(-i pi/4), 0, 0], [0, 0, exp(+i pi/4)]]`, which are unitarily conjugate to `B1611`'s `T` on all `96` elements. In `W10`, that odd eighth-root phase `3/24 = 1/8` enters specifically from the order-eight lift `g_L in 2O` acting on the quaternionic `Q_8` coefficients.

---

## 4. Theorem 3 (`WP 3-2` Part B): Action of `E_theta` and `Ind_{E_theta}^E` on the Actual `6D` Zero Modes

1. **On a Fixed Branch `B_(1,1)` under `E_theta` (`[thread]`):**
   - **Half-root spinors `128 = (16, 4) (+) (bar16, bar4)` split as `1 + 1 + 1` (completely reducible):**
     - The `alpha = +1` block (`chi_(0,0)` in degree zero) carries `2` `1`-form modes in `H^0(E_tau, O(2p)) * dz = span{dz, wp(z|tau) dz}` and `1` spinor mode in `H^0(E_tau, S_0)`. Because `E_theta` fixes the puncture `p`, the holomorphic line `C * dz` (zero double-pole Laurent coefficient) is `E_theta`-invariant, reducing `2` to `1 + 1`.
     - The `alpha = -1` block (`chi_(1,1)` in degree zero) carries `2` `1`-form modes in `H^0(E_tau, chi_(1,1)(2p)) * dz = span{S_3(z|tau) dz, S_3'(z|tau) dz}` and `1` spinor mode. Because `Gamma_theta` fixes `chi_(1,1)` and `p`, the simple-pole Szegő line `C * S_3(z|tau) dz` is `E_theta`-invariant (verified by Cauchy residue quadrature to ten to the minus thirty-two), again reducing `2` to **`1 + 1`**.
   - **Vector-six summand `(10, 6)` splits as `2 + 1`:**
     - Its `2` `1`-form modes sit in `H^0(E_tau, (chi_(1,0)(p) (+) chi_(0,1)(p))) * dz = span{S_2(z|tau) dz, S_4(z|tau) dz}`. Under `S_theta in E_theta`, `S_2` and `S_4` swap off-diagonally while `L^2` acts diagonally with opposite signs, forming an **irreducible `2`** under `E_theta`, alongside `1` spinor mode whose degree-one Koszul bundle carries the `Q_8` holonomy `chi_(1,1) (x) rho_Q` (the exact local system of `W10` on the `B_(1,1)` branch!).
2. **Across the Three-Branch Weave Sum `Ind_{E_theta}^E` (`[weave]`):**
   - Inducing a single `128` spinor zero-mode across the `3` branches gives a `3`-dimensional fiber representation (`L^2 -> +1, S_theta -> -1`) of order **`6`** (`S_3`) whose **projective image in `PGL(3, C)` has order `6`** — never `24` (`S_4`). Because multiplying by any scalar modular-weight bundle (`eta(tau)^k`) leaves the `PGL(3, C)` image invariant, **no scalar modular twist can ever carry the `3`-branch `128` spinor zero-mode into `B1611`'s `T`**.
   - Inducing the `128` active simple-pole Szegő `1`-form `S_3 dz` across the `3` branches (`L^2 -> -1` via `U_{L^2} = X`, `S_theta -> +1`) gives a `3`-dimensional representation of order **`24`** (`S_4`, projective order `24`), because Slot `1` (`a`) carries `gauge` (`X^4 = +I`, order `4`) without `flavour` (`g_L in 2O`, order `8`), and `dz` carries whole-number modular weight `+1` (an **even** `Z_24` twist, factoring through `SL(2, Z)` with `S^4 = +I_3` and order in `{24, 48, 72, 144}`, never `96`).
   - Only the `(10, 6)` degree-one quaternionic `Q_8` bundle summed over the `3` branches (`oplus_{p != 0} (chi_p (x) rho_Q)`) carries both the active parities and the order-eight `2O` lift `g_L` whose group cohomology `H^1(F_2, -)` yields `V = T (+) T_bar` (`|G_T| = 96`).

---

## 5. Impact on `B1858` / `B1861` Nodes and Note on `CC_TO_PHYSICAL` (`2026-11-10`)

1. **`WP 2-2` (`E:L03`, `E:L05`, `E:L06`, `E:L07`, `E:Q3`) — Algebraically Resolved (`[weave]` vs `[thread]`):**
   - `E:L03` (`rho_Q`), `E:L05` (odd spin bundle `S_0`), and the discrete torsion point `w = 0` in `E:L07` are uniquely fixed by **all** moves in `E` (`0` discrete selection bits once flatness/spin-type are declared; continuous `U(1)^2` deformation `X:FLAT` remains open without a dynamical potential).
   - `E:L06` (`+-h_4` lift sign) is **eliminated as an independent choice** (`-h_4 == zeta_Spin(10)(+h_4)` across all `248` dimensions of `E_8`); only the `S_theta`-invariance split on `varsigma` (`{(+1,+1), (-1,-1)}` vs `{(+1,-1), (-1,+1)}`) distinguishes `3` versus `2` zero modes per chiral spinor block.
   - Selecting a single branch `B_(1,1)` is a `1`-of-`3` `[thread]` choice (`[E : E_theta] = 3`); summing over the three-element orbit `{B_(1,0), B_(0,1), B_(1,1)}` restores exact `E`-invariance (`[weave]`, `E:Q3` structural orbit step).
2. **`WP 3-2` (`E:J5`, `MC:GEN`, `D:01`, `X:DICT`) — Algebraically Resolved:**
   - `E:J5` (`Sym^2(Weil_2)` vs `B1611` `T` vs `2 + 1` PDE modes) is settled with exact group orders (`48` untwisted, `{24, 48, 72, 144}` all even twists, `96` odd `m = 3, 15` Jacobi-Dedekind half-weight triplet for `T`; `1 + 1 + 1` on `128` vs `2 + 1` on `(10, 6)` under `E_theta`).
   - `MC:GEN` / `D:01` / `X:DICT`: the `2 + 1 = 3` per-branch zero-mode sum is **not** `main`'s `T`, and `X:HAND` (`D:01` chiral selection from `V = T (+) T_bar`) is not discharged by the `6D` elliptic index alone.
3. **Structural Note on `B1861`'s Dependency Edge (`WP 3-1 -> WP 3-2`):**
   - In `B1861`, `WP 3-2` lists `Needs: WP 3-1` (`E:P01`, complete Fredholm domain). All group, root-lattice, bundle-cohomology, and Szegő/Weierstrass pole-flag proofs in `src/origin_axiom/p753_register_field_join.py` and `scripts/referee_p753_register_field_join.py` are purely algebraic and complex-analytic on the punctured curve `E_tau \ {p}`, so `WP 3-2`'s module-theoretic comparison holds unconditionally on the declared carrier without waiting on `WP 3-1`'s Sobolev/Fredholm domain completion (`E:P01` remains needed for the self-adjoint `6D` PDE index theorem itself).

Ready for `cc` and advisor-seat scrutiny prior to banking.

0 of 19.
