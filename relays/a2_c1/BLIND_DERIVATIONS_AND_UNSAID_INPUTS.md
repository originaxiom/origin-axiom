# Blind Second Derivations and Complete Unsaid-Inputs Ledger (`A2-C1`)

- **Seat:** `agy-002` (`origin/agy-002/verify`, cut from `main` at `2f3984d275d7b2a666afaca0efe2d15b0ec44761`)
- **Card:** `relays/cards/AGY-002_A2-C1_three-headline-derivations.md` (sealed in `809f68916` before any computation)
- **Sealed scripts and verbatim raw outputs:** committed in `03f291185` before this page was written:
  - `relays/a2_c1/derive_g_root.py` and `relays/a2_c1/derive_g_root_out.txt`
  - `relays/a2_c1/derive_mc_z6.py` and `relays/a2_c1/derive_mc_z6_out.txt`
  - `relays/a2_c1/derive_w_index3.py` and `relays/a2_c1/derive_w_index3_out.txt`
- **Causal independence status:** written and committed **before** opening any derivation script, addendum, or `FINDINGS.md` of `main`'s arcs for these three results. Complete pre-comparison file log in §5 below.
- **Data rule:** zero measured values, zero physical constants, zero held-out targets (`0 of 19`). All findings are stated as mathematical theorems in words and exact integers/rationals.

---

## Executive Summary of Blind Findings

1. **`G:ROOT`:** Given `GM3`, `GM4`, `SE1`, and `SE2` **together with** the surrounding mapping-torus and once-punctured-torus context in `GENESIS.md` §1 and §3, the unique hyperbolic `SL(2, Z)` conjugacy class whose mapping torus over the once-punctured torus has torsion-free integral first homology is `[LR]` of trace `3` (narrow and wide class numbers of discriminant `5` both equal `1`), whose unmarked, unoriented homeomorphism type is the figure-eight knot complement `m004`. Five unstated or external inputs (`U-ROOT-1` through `U-ROOT-5`) are required along the way, including that the selection fixes only the **unbased** conjugacy class (`LR`, `RL`, and `(LR)^{-1}` are `SL(2, Z)`-conjugate with opposite fixed-point quadratics `tau^2 - tau - 1` and `tau^2 + tau - 1`) and does not choose an orientation of `m004`.
2. **`MC:Z6`:** Over continuous `Z(SU(3)) x Z(SU(2)) x (R / Z)` with integer charge scaling `q = 6 k Y` (`k >= 1`), the ineffective kernel `K_k` acting trivially on the `27` of `E_6` (and already on the `16` alone or the `10` alone) is **cyclic of exact order `6k` for every positive integer `k`** (`|K_k| = 6` if and only if `k = 1`). However, from the local Lie algebra `su(3) (+) su(2) (+) u(1)_Y` and the representation `27` alone (`frontier/B1221_global_form_path_independence/arc_verdict.json`), **all four** quotients `[SU(3) x SU(2) x U(1)] / Gamma` for `Gamma in {1, Z_2, Z_3, Z_6}` admit the `27` cleanly (`CTL-Z6-A`). Uniquely forcing `/ Z_6` requires one of two unstated postulates (`U-Z6-1`): either an **effectiveness postulate** (`G = G_tilde / ker(rho_matter)`, under which one Standard Model generation `16` already forces `/ Z_6` without `E_6`), or a **simply-connected UV group postulate** (`G_UV = E_6^{sc}` rather than an adjoint quotient `E_6^{ad} = E_6^{sc} / Z_3` or cover, in which case we prove via Smith normal form `[1, 1]` that `Stab_{E_6^{sc}}(<S>, <nu^c>)` has a connected maximal torus and embeds `[SU(3) x SU(2) x U(1)_Y] / Z_6` canonically). Four unstated inputs (`U-Z6-1` through `U-Z6-4`) are recorded.
3. **`W:INDEX3`:** **Cannot be derived from the bare node statement and bare `TAG:LAMBDA` / `TAG:UNIT` sentences alone**, because those sentences do not define the four-dimensional surface, the differential operator, the weight `3/2`, the metaplectic representation `rho_T`, or the boundary condition. When supplemented by the explicit mathematical apparatus stated in `GENESIS.md` (`FK10`, `FK11`, `FK14`), we prove over exact `Q(zeta_24)` that the `Mp_2(Z)` multiplier `rho_T` of `eta^{21}(theta_2^2, theta_3^2, theta_4^2)` has `T_mp`-exponents `(1/8, 3/8, 7/8)`, zero projective defect, `chi(X(1), V_{3/2}(rho_T, 0)) = 0` (`W_0 = O_{P^1}(-1)^3`), and `chi(X(1), V_{3/2}(rho_T, n)) = 3n` (`h^0 = 3, h^1 = 0` at `n = 1`, independently confirmed as `dim M_{27/2}(rho_T) = 3`). Crucially, `CTL-INDEX3-C` exposes a hidden bundling inside *"the unit"* (`U-IDX-6`): because `X(1)` has a single cusp whose stabilizer `<T_mp, Z>` is abelian and diagonal on `(1/8, 3/8, 7/8)`, **every** integer pole vector `m = (m_1, m_2, m_3) in Z^3` defines a valid `Mp_2(Z)`-equivariant parabolic bundle on `X(1)` with index `m_1 + m_2 + m_3` (`1` for `(0, 0, 1)`, `2` for `(0, 1, 1)`, `3` for `(1, 1, 1)`). Thus *"one unit"* silently means **three** uniform line-bundle cusp shifts `m = (1, 1, 1)` across a rank-`3` bundle, and converting that parity multiplicity `3` into gauge chiral generations rests entirely on the conditional dictionary `Lambda`. Six unstated inputs (`U-IDX-1` through `U-IDX-6`) are recorded.

---

## 1. Blind Second Derivation of `G:ROOT`

### 1.1 Statement and Stated Premises Read
- **Statement (`G:ROOT`, `GENESIS.md` §3 `[v1.18]`):** *"given GM3, GM4, SE1 and SE2, the root is m004, the figure-eight knot complement."*
- **Stated premises (`GENESIS.md` §1 and §3):**
  - `GM3`: *"A word is closed only if it mixes both generators and stretches and squeezes the cell's grid (`|tr| > 2` in `GL(2, Z)`, hyperbolic)."*
  - `GM4`: *"Two words are the same move when they induce the same map on the grid; the group of moves is `GL(2, Z)`."*
  - `SE1`: *"Nothing turns back on itself (`H_1` torsion-free)."*
  - `SE2`: *"Handedness is preserved around the loop (`det = +1`, orientable; rules out m000)."*

### 1.2 Exact Theorem Derived (`relays/a2_c1/derive_g_root.py`, `relays/a2_c1/derive_g_root_out.txt`)

**Theorem 1 (`G:ROOT` algebraic and topological uniqueness).**
Let `T_{1,1}` be the once-punctured oriented two-torus with fundamental group `F_2 = <a, b>` and integral first homology `H_1(T_{1,1}; Z) = Z^2`, where the puncture boundary loop represents the commutator `[a, b]` and maps to `0` in `H_1(T_{1,1}; Z)`. For any mapping class `Phi in MCG(T_{1,1}) = GL(2, Z)`, let `M_Phi = (T_{1,1} x [0, 1]) / ((x, 1) ~ (Phi(x), 0))` be its mapping torus with unfilled cusp torus boundary. Then:
1. By van Kampen's theorem and abelianisation, `H_1(M_Phi; Z) = Z (+) (Z^2 / (Phi - I_2) Z^2)`. Its torsion subgroup is trivial if and only if every non-zero Smith invariant factor of `Phi - I_2` over `Z` equals `1`.
2. `M_Phi` is an orientable three-manifold if and only if `Phi` is orientation-preserving on `T_{1,1}`, namely `det(Phi) = +1`, so `Phi in SL(2, Z)`.
3. For `Phi in SL(2, Z)`, `det(Phi - I_2) = 2 - tr(Phi)`. If `Phi` is hyperbolic (`|tr(Phi)| > 2`), then `det(Phi - I_2) != 0`, so `H_1(M_Phi; Z)` has free rank `1` and finite torsion of exact order `|2 - tr(Phi)|`. Torsion-freeness `|2 - tr(Phi)| = 1` over `Z` has two integer solutions `tr(Phi) in {1, 3}`, of which `tr(Phi) = 1` is elliptic of order `6` (`|tr| <= 2`), leaving the **unique** hyperbolic trace `tr(Phi) = 3`.
4. The `SL(2, Z)`-conjugacy classes of trace `3` stand in bijection with proper equivalence classes of primitive indefinite binary quadratic forms `a x^2 + b x y + c y^2` of discriminant `D = 3^2 - 4 = 5` via `[[p, q], [r, 3 - p]] |-> (r, 3 - 2p, -q)`. Exhaustive integer enumeration of Gauss-reduced forms (`0 < sqrt(5) - b < 2|a| < sqrt(5) + b`) yields exactly two reduced forms, `(-1, 1, 1)` and `(1, 1, -1)`, linked in a single proper Gauss cycle by `[[0, -1], [1, -1]]` and `[[0, -1], [1, 1]]`. Hence both the narrow class number `h^+(5)` and wide class number `h(5)` equal `1`: there is **exactly one** `SL(2, Z)`-conjugacy class (and one `GL(2, Z)`-conjugacy class) of trace `3`, represented by `LR = [[2, 1], [1, 1]]`.
5. Consequently, up to bundle isomorphism, `M_{LR}` is the unique orientable hyperbolic once-punctured-torus bundle with torsion-free `H_1(M_Phi; Z)` (and `H_1(M_{LR}; Z) = Z`). By standard three-manifold topology (Jorgensen-Thurston / Stallings fibering of the genus-`1` fibered knot `4_1`), `M_{LR}` is homeomorphic to the complement `S^3 \ 4_1` of the figure-eight knot, designated `m004` in the SnapPea / Hodgson-Weeks cusped census.

### 1.3 Controls Verified (`CTL-ROOT`)
- **`CTL-ROOT-A` (drop `SE2`, allow `det = -1`):** For `det(Phi) = -1`, `det(Phi - I_2) = -tr(Phi)`, so `|det(Phi - I_2)| = 1` gives `tr(Phi) = +-1` (both pseudo-Anosov since `tr(Phi^2) = tr(Phi)^2 - 2 det(Phi) = 3 > 2`), represented by `LP = [[1, 1], [1, 0]]` (`32` matrices in `[-8, 8]^4`), whose mapping torus is the non-orientable Gieseking manifold `m000` with `H_1(m000; Z) = Z`.
- **`CTL-ROOT-B1` & `CTL-ROOT-B2` (drop `GM3`, allow `|tr| <= 2` in `SL(2, Z)`):** Both elliptic `tr = 1` (`[[1, -1], [1, 0]]`, giving `H_1 = Z`) and parabolic `Phi = L = [[1, 1], [0, 1]]` (`tr = 2`, Smith invariant factors `(1, 0)`, giving `H_1(M_L; Z) = Z^2` with **zero torsion**) pass `SE1 + SE2`! Thus `SE1` ("torsion-free `H_1`") does **not** by itself enforce `b_1 = 1`; `GM3` is essential to rule out parabolic `L` as well as elliptic `tr = 1`.
- **`CTL-ROOT-C` (sign-twin `-LR`, `tr = -3`, `m003`):** `det(-LR - I_2) = 2 - (-3) = 5`, giving `H_1(M_{-LR}; Z) = Z (+) Z / 5Z` (non-trivial torsion of order `5`, sister manifold `m003`).

### 1.4 Everything `G:ROOT` Needed and Left Unsaid (`U-ROOT-1` .. `U-ROOT-5`)
1. **`U-ROOT-1` (Mapping-torus and unfilled-cusp construction is outside `{GM3, GM4, SE1, SE2}`):** From `GM3, GM4, SE1, SE2` alone, no three-manifold exists until one supplies the mapping-torus functor `Phi |-> M_Phi = (F x [0, 1]) / ~` (`GENESIS.md` §3 prose) **and** specifies that the puncture cusp remains **unfilled** (Dehn filling `M_{LR}(p, q)` produces closed hyperbolic and lens/Seifert manifolds, including `0`- and `+-1`-surgeries with torsion-free `H_1`!).
2. **`U-ROOT-2` (`GM4` silently depends on `GM1`):** `MCG(F) = GL(2, Z)` holds only because `F` was chosen to be the **once-punctured genus-`1` torus** `T_{1,1}` (`GM1`). On a closed torus `T^2` there is no cusp (giving a Solvmanifold, not hyperbolic `m004`); on a twice-punctured torus `T_{1,2}` or higher-genus surface `Sigma_{g,1}` (`g >= 2`), the mapping class group is not `GL(2, Z)` and infinitely many pseudo-Anosov bundles have `H_1 = Z`. Also, `GM3` writes `|tr| > 2` in `GL(2, Z)`, whereas for `det = -1` pseudo-Anosov hyperbolicity is `|tr(Phi^2)| = |tr(Phi)^2 + 2| > 2`, i.e. `tr(Phi) != 0` (`LP` has `|tr(LP)| = 1 <= 2` yet **is** hyperbolic!).
3. **`U-ROOT-3` (Coefficient ring `Z` in `SE1`):** `SE1` writes "`H_1` torsion-free" without naming the coefficient ring `Z` (over `Q`, every `H_1(M_Phi; Q)` is torsion-free; over `Z_2`, `m003` has `H_1(m003; Z_2) = Z_2` without `2`-torsion).
4. **`U-ROOT-4` (Unbased conjugacy class vs based matrix `LR`, and unoriented `m004`):** `SE2` contains the target name `m000` in its parenthetical, and `GM3 + GM4 + SE1 + SE2` selects only the **unbased conjugacy class** `[LR]` in `GL(2, Z)`: `LR = [[2, 1], [1, 1]]`, `RL = [[1, 1], [1, 2]]`, and `(LR)^{-1} = [[1, -1], [-1, 2]]` are all `SL(2, Z)`-conjugate (`C^{-1} RL C = LR` for `C = [[1, -1], [0, 1]]`; `S^{-1} (LR)^{-1} S = LR` for `S = [[0, -1], [1, 0]]`), yet their upper-half-plane fixed points solve different quadratic equations (`tau^2 - tau - 1 = 0` for `LR` vs `tau^2 + tau - 1 = 0` for `RL`). Moreover, `m004` is amphicheiral, and `{GM3, GM4, SE1, SE2}` chooses no orientation on `M_{LR}` or on the base circle `S^1`. Any downstream step that uses the specific matrix `LR` rather than `RL` or `(LR)^{-1}` is choosing a marking/basis of `H_1(T_{1,1}; Z)`.
5. **`U-ROOT-5` (External topology dictionary):** Identifying `M_{[LR]}` with `S^3 \ 4_1` and the census label `m004` imports classical three-manifold topology and the Hodgson-Weeks census naming convention.

---

## 2. Blind Second Derivation of `MC:Z6`

### 2.1 Statement and Stated Premises Read
- **Statement (`MC:Z6`, `docs/THE_CLAIM.md` §1; `frontier/B1221_global_form_path_independence/arc_verdict.json`):**
  - `docs/THE_CLAIM.md`: *"the global form is `[SU(3) x SU(2) x U(1)] / Z_6`, at the primitive normalisation of hypercharge only; the kernel is cyclic of order `6k`."*
  - `frontier/B1221_global_form_path_independence/arc_verdict.json`: *"The global gauge group `(SU(3)xSU(2)xU(1))/Z_6` is determined by the algebra `su(3)+su(2)+u(1)` and the `27` representation alone, independently of the symmetry-breaking path through `E_6`."*
- **Stated premises (`docs/THE_CLAIM.md` §1):** `E_6` paired with its `27`, two `SU(3) x SU(2) x U(1)_Y`-invariant singlets `<S>` and `<nu^c>` inside the `27`, and `Y` in `u(1)^3` surviving unbroken alongside `su(3)_c (+) su(2)_L`.

### 2.2 Exact Theorems Derived (`relays/a2_c1/derive_mc_z6.py`, `relays/a2_c1/derive_mc_z6_out.txt`)

**Theorem 2A (Ineffective kernel `K_k` on `27`, `16`, and `10` over continuous `U(1)`).**
Let `G_tilde = SU(3) x SU(2) x U(1)` with `U(1) = R / Z` (`u = e^{2 pi i phi}`), and let `27` be the minuscule fundamental representation of `e_6` constructed from its Cartan matrix. Along `A_2 (+) A_1 (+) u(1)_Y subset A_4 subset D_5 subset E_6`, the unique primitive hypercharge cocharacter `h_Y = 2 alpha_1^v + 4 alpha_3^v + 6 alpha_4^v + 3 alpha_5^v` assigns to the `27` weights the integer charges `q_prim = 6Y` with greatest common divisor `1`, decomposing `27 = 16 (+) 10 (+) 1` into `(3, 2)_{+1}`, `(3*, 1)_{-4}`, `(3*, 1)_{+2}`, `(1, 2)_{-3}`, `(1, 1)_{+6}`, `(1, 1)_0` (forming `16`), `(3, 1)_{-2}`, `(1, 2)_{+3}`, `(3*, 1)_{+2}`, `(1, 2)_{-3}` (forming `10`), and `(1, 1)_0` (`1`).
For any non-zero integer `k >= 1`, let `rho_k : G_tilde -> U(27)` assign `U(1)` charge `q = k q_prim` to each weight (`u` acts by `e^{2 pi i k q_prim phi}`). Then:
1. Any element `g = (g_3, g_2, u) in ker(rho_k)` commutes with `SU(3) x SU(2)` on every irreducible summand, hence lies in `Z(SU(3)) x Z(SU(2)) x U(1)` with `g_3 = e^{2 pi i a / 3} I_3` (`a in Z / 3Z`), `g_2 = (-1)^b I_2` (`b in Z / 2Z`), and `u = e^{2 pi i phi}` (`phi in R / Z`).
2. Triviality on `(1, 2)_{-3}` (`b/2 - 3 k phi in Z`), `(3*, 1)_{+2}` (`2a/3 + 2 k phi in Z`), and `(3, 2)_{+1}` (`a/3 + b/2 + k phi in Z`) holds if and only if `6 k phi = m in Z`, `a = m mod 3`, and `b = m mod 2` (and every remaining summand of `27` is then automatically satisfied: `-4 k phi + 2a/3 = 0 mod 1`, `-2 k phi + a/3 = 0 mod 1`, `6 k phi = m in Z`).
3. Therefore, for **every** positive integer `k` (including `gcd(k, 6) > 1`), the ineffective kernel `K_k = ker(rho_k)` on `27` — and identically on `16` alone and on `10` alone — is **cyclic of exact order `6k`**, generated by `(e^{2 pi i / 3} I_3, -I_2, e^{2 pi i / (6k)})`. In particular, `|K_k| = 6` if and only if `k = 1` (primitive normalisation of `U(1)_Y`).
4. As an abstract Lie group, the effective quotient `G_tilde / K_k` is isomorphic for every `k >= 1` to `[SU(3) x SU(2) x U(1)_prim] / Z_6` via `(g_3, g_2, u) |-> (g_3, g_2, u^k)`, because `K_k / {(I_3, I_2, e^{2 pi i r / k})} = Z_6`. Non-integer real rescalings fail to descend to compact `U(1) = R / Z`.

**Theorem 2B (Canonical global subgroup inside simply-connected `E_6^{sc}`).**
Inside the simply-connected compact Lie group `E_6^{sc}` (whose maximal torus `T = R^6 / Q^v` pairs integrally with Dynkin weight labels), the two `SU(3) x SU(2) x U(1)_Y`-singlet weights in the `27` are `S = (0, 0, 0, 0, 0, -1)` and `nu^c = (0, 1, 0, 0, 0, -1)`. The `2 x 6` integer matrix `[S; nu^c]` has Smith normal form invariant factors `[1, 1]` over `Z`. Consequently:
1. The torus stabilizer `{t in T : S(t) = 1, nu^c(t) = 1}` is a **connected** four-torus `(R / Z)^4` (zero disconnected finite gauge factor `Z_m`).
2. Along `h_Y = 2 alpha_1^v + 4 alpha_3^v + 6 alpha_4^v + 3 alpha_5^v`, `exp(2 pi i t h_Y)` lies in `SU(3)_c x SU(2)_L` inside `E_6^{sc}` if and only if `6t = m in Z` (forced by the `alpha_4^v` coefficient `6`), at which point `t h_Y mod Q^v = (m/3 alpha_1^v + 2m/3 alpha_3^v) + (m/2 alpha_5^v)` generates `Z(SU(3)_c) x Z(SU(2)_L) = Z_6`. Hence the connected subgroup `H_SM subset E_6^{sc}` with Lie algebra `su(3)_c (+) su(2)_L (+) u(1)_Y` is canonically `[SU(3) x SU(2) x U(1)_Y] / Z_6`, and `H_SM` intersects the centre `Z(E_6^{sc}) = Z_3` trivially.

### 2.3 Controls Verified (`CTL-Z6`)
- **`CTL-Z6-A` (Tong non-uniqueness from `(algebra, 27)` alone):** Because `K_1 = Z_6` has four subgroups `Gamma in {1, Z_2, Z_3, Z_6}` of orders `[1, 2, 3, 6]`, the `27` descends cleanly as a single-valued unitary representation to `[SU(3) x SU(2) x U(1)] / Gamma` for **all four** global forms! Thus `B1221`'s literal sentence (*"determined by the algebra `su(3)+su(2)+u(1)` and the `27` representation alone"*) is **underdetermined as written** without an additional faithfulness/effectiveness or simply-connected `E_6^{sc}` postulate.
- **`CTL-Z6-B` (SM gauge adjoints only):** On `(8, 1)_0 (+) (1, 3)_0 (+) (1, 1)_0`, the kernel in `SU(3) x SU(2) x U(1)` is **infinite** (`Z_3 x Z_2 x U(1)`, or `6N` if `U(1)` is artificially sampled on `N` torsion points, e.g. `72` at `N = 12`).
- **`CTL-Z6-C1` & `CTL-Z6-C2` (integer-hypercharge test sets at `k = 1`):** On `(1, 1)_{q=6}` alone, `|ker| = 36 != 6`; on `(1, 2)_0 (+) (1, 1)_{q=6}`, `|ker| = 18 != 6`. Scaling `k = 2, 3, 4, 6` on `27` yields cyclic orders `12, 18, 24, 36 != 6`.

### 2.4 Everything `MC:Z6` Needed and Left Unsaid (`U-Z6-1` .. `U-Z6-4`)
1. **`U-Z6-1` (Unstated effectiveness postulate OR unstated simply-connected `E_6^{sc}` global UV group):** Neither `docs/THE_CLAIM.md` nor `B1221`'s statement specifies whether the physical gauge group is defined as (i) the **effective group** `G_tilde / ker(rho_matter)` acting faithfully on local matter fields, or (ii) the **embedded subgroup** inside a specified global UV Lie group `G_UV`. Without (i) or (ii), `(su(3) (+) su(2) (+) u(1)_Y, 27)` allows **four** global forms (`Gamma in {1, Z_2, Z_3, Z_6}`, distinguishable physically by `'t Hooft` magnetic/fractional-instanton lines). Conversely:
   - if one adopts (i) (effectiveness on matter), then a single Standard Model chiral generation (`16`, or even `{Q, L, d^c}` alone!) **already** uniquely gives `[SU(3) x SU(2) x U(1)_Y] / Z_6`, so `E_6` and the `27` add zero extra global-group constraint beyond standard `SU(5)`/`Spin(10)`/SM charge quantisation;
   - if one adopts (ii), one must state that the UV group is **simply-connected `E_6^{sc}`** (rather than `E_6^{ad} = E_6^{sc} / Z_3` — note that `27` does not descend to `E_6^{ad}` because `Z(E_6^{sc}) = Z_3` acts non-trivially on `27`, so the existence of `27` forces `E_6^{sc}` among compact connected forms of `e_6`, **provided** no extra central `U(1)` or discrete gauge cover `E_6^{sc} x Z_m` is present!).
2. **`U-Z6-2` (Compactness of `U(1)_Y` and choice `k = 1` of circle parameterisation):** In `u(1)^3`, an irrational combination of Cartan generators gives a dense non-closed subgroup `R` rather than compact `U(1)`. Even once rational `h_Y` is fixed by `<S>, <nu^c>`, choosing `k = 1` selects the **primitive cocharacter parameterisation** of `S^1`; as Theorem 2A(4) shows, the quotient Lie group `G_tilde / K_k` is abstractly isomorphic to `[SU(3) x SU(2) x U(1)_prim] / Z_6` for every `k >= 1`, whereas the statement *"at the primitive normalisation of hypercharge only"* is true specifically for the **equality `|K_k| = 6`** inside the chosen cover `SU(3) x SU(2) x U(1)` (not for the isomorphism class of the effective quotient `G_tilde / K_k`).
3. **`U-Z6-3` (Matter-completeness assumption):** If the full theory contained any field outside the `27`'s triality-duality-hypercharge congruence `(a/3 + b/2 + q_prim / 6 in Z)` (for example a colour singlet of hypercharge `1/6` or an uncharged colour fundamental `(3, 1)_0`), `K_1` would shrink from `Z_6` to a proper subgroup. Thus `MC:Z6` implicitly assumes **all** fields in the theory obey the `27` congruence.
4. **`U-Z6-4` (No topological discrete gauge modification at symmetry breaking):** Identifying the unbroken global group with the connected subgroup `H_SM` assumes symmetry breaking is triggered solely by fundamental `27` singlets `<S>, <nu^c>` (whose Smith invariant factors we proved are `[1, 1]`) and not by higher-tensor condensates (e.g. inside `Sym^n(27)`) that leave an extra unbroken discrete `Z_m` subgroup of `T_{E_6^{sc}}`.

---

## 3. Blind Second Derivation of `W:INDEX3`

### 3.1 Statement and Stated Premises Read
- **Statement (`W:INDEX3`, `GENESIS.md` §3 `[v1.59]`):** *"given `Lambda` and the unit, the chiral three is a four-dimensional index, `+-3`, on the weave's own surface."*
- **Direct premise nodes (`frontier/B1858_the_closure_map/NODES.json`):**
  - `TAG:LAMBDA`: *"Conditional on `Lambda`: the dictionary's link."*
  - `TAG:UNIT`: *"Conditional on the unit: one unit of end data at the weave's cusp."* (`SC:UNIT` in `GENESIS.md` §3: *"One unit of end data at the weave's cusp is the smallest move-invariant deviation from zero (`W:INDEX3`, `[v1.36]–[v1.43]`)."*)
- **Mathematical context in `GENESIS.md` (`FK10`, `FK11`, `FK14`):** `Aut^+(F_2)` moduli orbifold `M_{1,2}` fibred over `M_{1,1} = H / SL(2, Z)`, parity representation `4 = 1 (+) T` on `Z_2^2`, metaplectic quotient `B_3 / <Delta^8> = Mp_2(Z)` acting on `T` via `eta^{21}(theta_2^2, theta_3^2, theta_4^2)` with `T`-exponents `(1/8, 3/8, 7/8)`, weight `3/2`, canonical index `0` at zero cusp units, and index `+-3` at one unit.

### 3.2 Exact Theorems Derived (`relays/a2_c1/derive_w_index3.py`, `relays/a2_c1/derive_w_index3_out.txt`)

**Theorem 3A (Exact `Mp_2(Z)` representation `rho_T` over `Q(zeta_24)`).**
Let `z = zeta_24 = e^{2 pi i / 24}` in `Q(z)` (`z^8 - z^4 + 1 = 0`), with `i = z^6` and `zeta_8 = z^3`. On `F_23(tau) = eta(tau)^{21} (theta_2(tau)^2, theta_3(tau)^2, theta_4(tau)^2)^T` of weight `23/2`, the metaplectic generators `T_mp : tau |-> tau + 1` (`j = 1`) and `S_mp : tau |-> -1/tau` (`j = sqrt(tau)`) act via the exact `3 x 3` unitary matrices:
- `rho_T(T_mp) = [[z^3, 0, 0], [0, 0, z^{21}], [0, z^{21}, 0]]`,
- `rho_T(S_mp) = [[0, 0, z^3], [0, z^3, 0], [z^3, 0, 0]]`.
Over `Q(z)`:
1. `rho_T(S_mp)^2 = (rho_T(S_mp) rho_T(T_mp))^3 = +i I_3 = rho_T(Z)` with **zero** projective defect. Because `j(Z, tau)^3 = (+i)^3 = -i`, `(j(Z, tau))^3 rho_T(Z) = I_3`, so `rho_T` descends to a genuine orbifold vector bundle `V_{3/2}(rho_T)` of weight `k = 3/2` on `X(1)`, whereas the complex-conjugate representation `rho_T_bar` has `rho_T_bar(Z) = -i I_3` (`(-i)(-i) = -I_3 != I_3`) and admits **zero** non-zero weight-`3/2` sections at every cusp order (`CTL-INDEX3-B`).
2. Because `T_mp` swaps `theta_3^2 <-> theta_4^2`, its eigenlines are `e_{1/8} = v_2` (eigenvalue `z^3 = e^{2 pi i (1/8)}`), `e_{3/8} = v_3 - v_4` (eigenvalue `-z^{21} = z^9 = e^{2 pi i (3/8)}`), and `e_{7/8} = v_3 + v_4` (eigenvalue `+z^{21} = e^{2 pi i (7/8)}`), confirming the exact cusp exponents `(1/8, 3/8, 7/8)`.

**Theorem 3B (Algebraic proof of `chi = 0` at `n = 0` and `chi = 3n` at `n` uniform cusp units).**
Let `R = Q(z)[theta_2, theta_3, theta_4] / (theta_2^4 + theta_4^4 - theta_3^4)` be the exact graded ring of `Gamma(4)` modular forms of half-integral weight `k = d / 2`.
1. At `n = 0` (canonical parabolic extension `0 <= alpha_j < 1` at the cusp `p_infty` of `X(1)`), exact linear algebra over `Q(z)` in `R_3` (`dim = 10`) and `R_1` (`dim = 3`) yields:
   `h^0(X(1), V_{3/2}(rho_T, 0)) = dim Hom_{Mp_2(Z)}(rho_T, R_3) = 0`, and by Serre duality on `X(1)` (`Omega^1_{X(1)}(log p_infty)` has weight `2`, dualising `(3/2, rho_T)` to cusp forms `(1/2, rho_T_bar)`), `h^1(X(1), V_{3/2}(rho_T, 0)) = dim S_{1/2}(rho_T_bar) <= dim Hom_{Mp_2(Z)}(rho_T_bar, R_1) = 0`.
   Therefore `h^0 = 0`, `h^1 = 0`, and **`chi(X(1), V_{3/2}(rho_T, 0)) = 0`**!
2. Pushing forward along `pi_coarse : X(1) -> P^1` gives a rank-`3` locally free sheaf `W_0 = (pi_coarse)_* V_{3/2}(rho_T, 0)` on `P^1` with `H^0(P^1, W_0) = H^1(P^1, W_0) = 0`. By Birkhoff-Grothendieck on `P^1`, the **unique** rank-`3` bundle on `P^1` with `h^0 = h^1 = 0` is `W_0 = O_{P^1}(-1)^{(+) 3}`!
3. Twisting uniformly by `n in Z` units of the coarse cusp divisor `p_infty` (`q^{-n}` on all three eigenlines) gives `W_n = W_0 (x) O_{P^1}(n) = O_{P^1}(n - 1)^{(+) 3}`, whose exact Euler characteristic is:
   `chi(X(1), V_{3/2}(rho_T, n)) = 3 * ((n - 1) + 1) = 3 n`!
   At `n = 1`: `W_1 = O_{P^1}(0)^{(+) 3}`, so `h^0 = 3`, `h^1 = 0`, and `chi = +3` (and `-3` for the opposite 4d chiral/orientation convention).
4. **Independent direct polynomial check at `n = 1` (without Birkhoff-Grothendieck):** Multiplication by `Delta = eta^{24} = 2^{-8}(theta_2 theta_3 theta_4)^8` (`q^1` at `p_infty`, non-vanishing on `H`) maps `H^0(X(1), V_{3/2}(rho_T, 1))` isomorphically onto `M_{27/2}(rho_T) = Hom_{Mp_2(Z)}(rho_T, R_{27})`. Exact nullspace reduction on the `318 x 318` cyclotomic intertwiner matrix in `R_{27}` (`dim R_{27} = 106`) confirms **`dim M_{27/2}(rho_T) = 3`** directly.
5. **Independent Kawasaki orbifold Riemann-Roch check:** Twisting sections by `eta^{-3}` reduces to weight `0` on `PSL(2, Z)` with `sum(alpha_j) = 1/8 + 3/8 + 7/8 = 11/8`, `sum(beta_2 / 2) = 1` at `[i]`, and `sum(beta_3 / 3) = 1` at `[e^{2 pi i / 3}]`, giving `deg(W_0) = 9/24 - 11/8 - 1 - 1 = -3` and `chi = 3 + (-3) = 0` at `n = 0`, `3 + 0 = +3` at `n = 1`.

### 3.3 Controls Verified (`CTL-INDEX3`)
- **`CTL-INDEX3-A` (all `6` `SL(2, Z)` character twists `rho_T (x) chi_eta^{4r}`, `r = 0..5`, at weight `3/2`, `n = 0`):** Exact Kawasaki orbifold Riemann-Roch over `Q(z)` gives `{0: 0, 1: 1, 2: 0, 3: 0, 4: 0, 5: 0}` (five twists give `0`, while `r = 1` gives `+1 != 0`). *(Self-correction note vs pre-run comment in `A2-C1` §5: `r = 1` (`chi_eta^{+4}`), not `r = 5`, is the unique non-zero twist among the six, and `r in {1, 2, 4, 5}` live at level `12` rather than inside level-`4` `R_3`.)*
- **`CTL-INDEX3-B` (conjugate `rho_T_bar` at weight `3/2`):** Fails central `Z`-parity (`-i` vs `+i`), returning `dim = 0` at both `n = 0` and `n = 1`.
- **`CTL-INDEX3-C` (non-uniform parabolic cusp pole vectors `m = (m_1, m_2, m_3) in {0, 1}^3`):** Expanding the three exact basis vectors of `M_{27/2}(rho_T)` in `w = q^{1/8}` gives leading `w`-orders `(9, 11, 7)`, `(9, 3, 7)`, and `(1, 11, 15)` on `(e_{1/8}, e_{3/8}, e_{7/8})`. Imposing holomorphicity at `n = 0` on subsets of eigenlines yields:
  - `m = (0, 0, 0) -> dim H^0 = 0`;
  - `m = (0, 0, 1)`, `(0, 1, 0)`, `(1, 0, 0) -> dim H^0 = 1` (not `3`!);
  - `m = (0, 1, 1)`, `(1, 0, 1) -> dim H^0 = 2` (not `3`!);
  - `m = (1, 1, 1) -> dim H^0 = 3`.

### 3.4 Everything `W:INDEX3` Needed and Left Unsaid (`U-IDX-1` .. `U-IDX-6`)
1. **`U-IDX-1` (Underdetermination of the bare statement):** From the one-line text of `W:INDEX3`, `TAG:LAMBDA`, and `TAG:UNIT` alone (without `FK10`/`FK11`/`FK14` in `GENESIS.md`), one **cannot** derive `+-3`: neither the 4d manifold `M_{1,2}`, nor the elliptic fibration `M_{1,2} -> M_{1,1}`, nor the parity representation `T`, nor the weight `3/2`, nor the operator whose index is taken is specified in the bare sentence.
2. **`U-IDX-2` (Jump from `<L, R> = B_3` of real dimension `2` to `Aut^+(F_2)` / `M_{1,2}` of real dimension `4`):** In `GENESIS.md` `[v1.41]`, the braid group `<L, R> = B_3` gives the modular base `M_{1,1}` (complex dimension `1`, real dimension `2`), and promoting the surface to four real dimensions (`M_{1,2}`, complex dimension `2`) requires extending `B_3 / Z(B_3)` to `Aut^+(F_2)` by adjoining the inner-automorphism torus fibre `F_2` — even though `GENESIS.md` `[v1.41]` explicitly acknowledges that inner automorphisms are **not** moves of `<L, R>`. Moreover, via the Leray spectral sequence of `pi : M_{1,2} -> M_{1,1}`, the 4d index reduces to a **2d orbifold curve Riemann-Roch calculation** on `X(1)` once the fibre spinor cohomology of rank `3` (`T`) and Hodge weight `1/2` (`1 + 1/2 = 3/2` or spinor-bundle shift) is taken as input.
3. **`U-IDX-3` (Choice of 4d elliptic operator, spin structure, and puncture boundary condition on non-compact `M_{1,2}`):** On a non-compact orbifold with both a fibre puncture (`M_{1,2} \ M_{1,1}` divisor) and a base cusp (`q -> 0`), an index is ill-defined until one chooses: (a) the spin-Dolbeault / Dirac operator, (b) the spin structure on fibre and base, and (c) the `L^2` / APS / algebraic meromorphic boundary condition at **both** ends. Indeed, `GENESIS.md` `[v1.59]` itself notes that *"at the middle puncture conditions it is `+-1`; at the parity-graded ones, `+-3`"* — so choosing the parity-graded puncture boundary condition over the middle one is a discrete structural choice that changes `+-1` to `+-3`!
4. **`U-IDX-4` (Selection of `rho_T` over `rho_T_bar` and spinor chirality sign):** `GENESIS.md` `FK11 [v1.41]` records *"two binary choices made by hand"* in aligning the parity representation `T` of `B_3 / <Delta^8>` with the holomorphic multiplier `rho_T` rather than `rho_T_bar`, and the overall sign in `+-3` remains unfixed unless orientation and chirality conventions on `M_{1,2}` are fixed.
5. **`U-IDX-5` (Choice `r = 0` among the `6` `SL(2, Z)` character twists `chi_eta^{4r}`):** Tensoring `rho_T` with any `1`-dimensional character of `B_3` factoring through `SL(2, Z)` (`Ab(PSL(2, Z)) = Z_6`, generated by `chi_eta^4`) preserves rank `3` and `SL(2, Z)`-projective representation class; as `CTL-INDEX3-A` proved, `r = 1` gives `chi = +1` at `n = 0` (`+4` at `n = 1`), whereas `r in {0, 2, 3, 4, 5}` give `0` at `n = 0` (`+3` at `n = 1`). Fixing `r = 0` requires pinning the exact `B_3` abelianisation character on `T`, not merely its `PSL(2, Z)` action.
6. **`U-IDX-6` (The "one unit" cusp-uniformity bundling — `m = (1, 1, 1)` vs `m = (0, 0, 1)`):** `SC:UNIT` asserts that *"one unit of end data at the weave's cusp is the smallest move-invariant deviation from zero."* **This phrasing hides a critical mathematical distinction proved in `CTL-INDEX3-C`:**
   - What is irreducible under `Mp_2(Z)` is the global bundle `V_{3/2}(rho_T)` on `H`, because `S_mp` mixes the eigenlines `(e_{1/8}, e_{3/8}, e_{7/8})`.
   - **At the cusp `[infty]` of `X(1)`, however, `X(1)` has only ONE cusp, and its stabilizer `<T_mp, Z>` in `Mp_2(Z)` is ABELIAN and acts DIAGONALLY with three distinct characters `(1/8, 3/8, 7/8)`!**
   - In the category of `Mp_2(Z)`-equivariant parabolic vector bundles on `X(1)`, a cusp extension at `[infty]` is specified by a `<T_mp, Z>`-invariant lattice inside the germ at `infty`, which splits cleanly as a direct sum of the three `T_mp`-eigenlines! Therefore **every** integer triple `m = (m_1, m_2, m_3) in Z^3` defines a completely `Mp_2(Z)`-invariant ("move-invariant"!) bundle extension on `X(1)`, and the **smallest** non-zero move-invariant parabolic deviation from `m = (0, 0, 0)` is **`m = (0, 0, 1)`** (shifting the `7/8` least-remainder eigenline to `-1/8`, realized explicitly by Basis Section #1 of `M_{27/2}(rho_T)` with `w`-orders `(9, 11, 7)`!), which has index **`+1`, NOT `+3`**!
   - One obtains `+3` **only** if one restricts admissible cusp data to **scalar line-bundle twists pulled back from the coarse base `X(1)`** (`V_{3/2}(rho_T, 0) (x) O_{X(1)}(1 * p_infty)`, which corresponds to `m = (1, 1, 1)` of total degree `3 = rk(T)`!). And because `chi(E (x) O_{P^1}(1)) - chi(E) = rk(E)` holds tautologically for **every** rank-`r` bundle `E` on `P^1`, the factor `3` in `3 * 1 = 3` is algebraically nothing other than `rk(T) = 3` (the dimension of the non-trivial part of the `4`-point permutation representation `4 = 1 (+) 3` of `Z_2^2`), **until** the conditional dictionary `Lambda` identifies that weave-parity multiplicity `T` with chiral gauge matter rather than flavour/family-blind or internal weave degrees of freedom.

---

## 4. Summary Count of Uncounted / Unstated Inputs Found Before Opening `main`'s Arcs

| Headline node | Can bare 1-line statement derive it alone? | Does full `GENESIS.md` / `THE_CLAIM.md` premise set derive the mathematical theorem? | Count of unstated / external inputs identified | Most consequential unstated input |
|---|---|---|---|---|
| `G:ROOT` | No (needs mapping-torus + `T_{1,1}` from surrounding `GENESIS.md` §1/§3) | **Yes**, up to unbased conjugacy class `[LR]` and unoriented homeomorphism type `m004` | **5** (`U-ROOT-1..5`) | `U-ROOT-4` (unbased `[LR]` vs based `LR`/`RL`/`(LR)^{-1}` and unoriented `m004`) + `U-ROOT-1` (unfilled cusp) |
| `MC:Z6` | Not uniquely from `(algebra, 27)` alone (`CTL-Z6-A`: `4` quotients `{1, Z_2, Z_3, Z_6}` all admit `27`) | **Yes, conditionally** on *either* the effectiveness postulate (`16` already suffices) *or* simply-connected `E_6^{sc}` + `<S>, <nu^c>` (`SNF = [1, 1]`) | **4** (`U-Z6-1..4`) | `U-Z6-1` (Tong non-uniqueness from `(algebra, 27)` without effectiveness or global `E_6^{sc}` postulate) |
| `W:INDEX3` | **No** (bare text lacks surface, operator, weight `3/2`, and `rho_T`) | **Yes, conditionally** on `FK10`/`FK11`/`FK14` **plus** coarse-divisor cusp uniformity `m = (1, 1, 1)` | **6** (`U-IDX-1..6`) | `U-IDX-6` (`m = (0, 0, 1)` is move-invariant on `X(1)` and gives index `1`; `+-3` requires coarse-cusp scalar twist `m = (1, 1, 1)` + `Lambda`) and `U-IDX-3` (`+-1` vs `+-3` puncture grading) |

---

## 5. Complete Log of Repository Files Opened Prior to This Commit (Condition 3)

### 5.1 Files Opened Since `M1` Landed (`95988c96b` / `2f3984d27`)
1. `docs/seats/README.md` (lines 1–153: seat protocol)
2. `docs/seats/agy-002.md` (lines 1–63: `M1` assignment)
3. `docs/seats/agy.md` (lines 1–41: role separation from `agy`)
4. `WORKING_RULES.md` and `docs/POINT_REGISTER.md` diff in `95988c96b` (`P-789`–`P-799`)
5. `scripts/seats/listen.py` (lines 1–156: silent listener)
6. `frontier/B1888_the_public_form_scrutinised/FINDINGS.md` (§3 only: five independence conditions cited in `M1`)
7. `frontier/B1858_the_closure_map/NODES.json` (entries for `G:ROOT`, `MC:Z6`, `W:INDEX3` and direct premise nodes `G:GM1`–`G:GM4`, `G:SE1`, `G:SE2`, `G:T-ROOT`, `MC:ALG`, `MC:HYP`, `MC:Y`, `MC:END`, `TAG:LAMBDA`, `TAG:UNIT`, `SC:UNIT`)
8. `GENESIS.md` (lines 1–535: canonical statements and premises for `G:ROOT` and `W:INDEX3`)
9. `docs/THE_CLAIM.md` (lines 1–63: canonical statement and premises for `MC:Z6`)
10. `frontier/B1221_global_form_path_independence/arc_verdict.json` (1 line: statement of `B1221`, cited in `M1`)
11. Our own files created on `origin/agy-002/verify` under `relays/`: `relays/STATUS_AGY-002.md`, `relays/cards/AGY-002_A2-C1_three-headline-derivations.md`, and the six files in `relays/a2_c1/`.

### 5.2 Governance / Hygiene Files Inspected Earlier in Session Prior to `M1`
For full transparency: before `M1` existed on `main`, governance/hygiene files (`frontier/B1889_the_seats_digested/FINDINGS.md`, `docs/HARVEST_LEDGER.md`, relay notes in `relays/`, `frontier/B1832_the_agy_lanes_digested/`, `scripts/checks/harvest_debt.py`, and `scripts/gates/gates.py`) were read while syncing the workspace. **Zero** derivation scripts, addenda, or `FINDINGS.md` files for `G:ROOT` (`B197`, `B1454`), `MC:Z6` (`B862`, `frontier/B1221_global_form_path_independence/FINDINGS.md`, or its addendum), or `W:INDEX3` (`B1632`, `B1634`, `B1641`) have been opened at any point prior to this commit.

0 of 19.
