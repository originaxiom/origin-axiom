# Post-Commitment Comparison With `main`'s Arcs (`A2-C1`, Condition 5)

- **Seat:** `agy-002` (`origin/agy-002/verify`, cut from `main` at `2f3984d275d7b2a666afaca0efe2d15b0ec44761`)
- **Causal order:**
  1. `809f68916` — pre-registered card `relays/cards/AGY-002_A2-C1_three-headline-derivations.md` committed before any computation;
  2. `03f291185` — three zero-float exact-arithmetic scripts and verbatim outputs committed before prose and before opening any of `main`'s arcs;
  3. `d003e482b` — blind theorems and unsaid-inputs ledger `relays/a2_c1/BLIND_DERIVATIONS_AND_UNSAID_INPUTS.md` committed before opening any of `main`'s arcs;
  4. **This file** — written after `d003e482b` was pushed to `origin/agy-002/verify`, upon opening `main`'s seven arc pages listed in §4 below.
- **Data rule:** zero measured values, zero physical quantities, zero decimals (`0 of 19`).

---

## Summary Classification Table (`M1` Condition 5)

`M1` asks, for each of the three headline results: **`the same`**, **`different`**, or **`cannot be derived from what is stated`**. Because two of the three statements behave differently depending on whether one evaluates the literal stated hypothesis sentence vs the mathematical calculation once the unstated premises from `relays/a2_c1/BLIND_DERIVATIONS_AND_UNSAID_INPUTS.md` are supplied, we report both levels explicitly:

| Result | From literal stated sentence & direct premises alone | When unstated premises in `relays/a2_c1/BLIND_DERIVATIONS_AND_UNSAID_INPUTS.md` are supplied | Specific finding against `main`'s arcs |
|---|---|---|---|
| `G:ROOT` | **`the same`** (using `GENESIS.md` §1/§3's `T_{1,1}` mapping-torus & unfilled-cusp context `U-ROOT-1..3`) | **`the same`** (unmarked, unoriented homeomorphism class `m004` via `[LR]` of trace `3`) | Global proof across all of `SL(2, Z)` via discriminant-`5` Gauss reduction (`h^+(5) = h(5) = 1`) replaces `B1454`'s bounded-box search; `U-ROOT-4` flags based `LR` vs `RL` vs `(LR)^{-1}` and unfixed orientation. |
| `MC:Z6` | **`cannot be derived from what is stated`** in `B1221`'s literal sentence (`(algebra, 27)` admits all four quotients `{1, Z_2, Z_3, Z_6}`) | **`the same`** on cyclic order `6k` (`|K_k| = 6 <=> k = 1`) and `/ Z_6` once `U-Z6-1` is added; **`different`** on `B1221`'s adjoint control row | (1) Catches **uncorrected 12-point `U(1)` grid bug** in `frontier/B1221_global_form_path_independence/FINDINGS.md` (`adjoint-only content = 72`, true kernel on continuous `U(1)` is **infinite** `Z_3 x Z_2 x U(1)`); (2) proves `[S; nu^c]` has Smith invariant factors `[1, 1]` in `E_6^{sc}` (`Theorem 2B`), supplying the missing global-group bridge between `B862` and `B1221`; (3) notes `[SU(3) x SU(2) x U(1)] / K_k` is abstractly isomorphic to `/ Z_6` for every `k >= 1`. |
| `W:INDEX3` | **`cannot be derived from what is stated`** in bare `W:INDEX3` + `TAG:LAMBDA` + `TAG:UNIT` (`SC:UNIT`), and **`different`** on `SC:UNIT`'s "smallest move-invariant deviation" claim | **`the same`** on all exact integers (`0` at `n = 0`, `{0, 1, 0, 0, 0, 0}` on the `6` twists, `+-3` at `m = (1, 1, 1)`) once `FK10`/`FK11`/`FK14` **and** coarse-divisor cusp uniformity `m = (1, 1, 1)` are imposed | **`U-IDX-6` (`CTL-INDEX3-C`) refutes `SC:UNIT` as worded:** none of `B1632`, `B1634`, or `B1641` tested non-uniform cusp shifts `m = (m_1, m_2, m_3) in Z^3`. Because `X(1)` has one cusp with abelian diagonal stabilizer `<T_mp, Z>`, `m = (0, 0, 1)` is `Mp_2(Z)`-invariant ("move-invariant") and gives global index **`+-1`, not `+-3`**. Getting `+-3` requires an uncounted coarse-cusp scalar uniformity hypothesis `m = (1, 1, 1)`. |

---

## 1. Detailed Comparison for `G:ROOT` (`B197` and `B1454`)

- **Arcs opened on `main`:**
  - `frontier/B197_figure_eight_volume_torsionfree/FINDINGS.md`
  - `frontier/B1454_genesis_v1_verified_and_adopted/FINDINGS.md`
- **What is `the same`:**
  1. Both `main` (`B1454` §2 `G2`, `G8`) and our blind `derive_g_root.py` establish that on the once-punctured torus `T_{1,1}`, `H_1(M_Phi; Z)` has torsion order `|2 - tr(Phi)|` for `det(Phi) = +1` and `|-tr(Phi)|` for `det(Phi) = -1` whenever `Phi - I_2` is non-singular.
  2. Every counter-witness in `B1454` `G8` matches our blind controls in `CTL-ROOT`:
     - dropping `SE2` admits `LP` (`det = -1, tr = +-1`, Gieseking manifold `m000`, `16` matrices per trace sign in `[-8, 8]^4`, `32` total — matching `B1454` `G2`'s `16 + 16 = 32`!);
     - dropping `GM3` admits both the order-`6` elliptic class of trace `1` and the **parabolic shear `L`** (`H_1(M_L; Z) = Z^2`, torsion-free — matching `B1454` `G8`!);
     - flipping trace `+3` to `-3` (`-LR`, sister manifold `m003`, `B197`) gives `Z / 5Z` torsion of order `5`;
     - `L^{-1} (LR) L = RL` conjugates `LR` to `RL` in `SL(2, Z)` while flipping the fixed-point quadratic between `tau^2 - tau - 1` and `tau^2 + tau - 1` (`B1454` `G3`).
- **Methodological sharpening over `B1454`:**
  - `B1454` verified trace-`3` conjugacy inside a finite matrix box (`[-8, 8]^4` / bounded word length). Our `derive_g_root.py` proves uniqueness across **all infinitely many matrices in `SL(2, Z)`** by exact Gauss reduction of binary quadratic forms of discriminant `D = 5` (`h^+(5) = h(5) = 1`).
- **Unsaid inputs confirmed as uncounted in the headline `G:ROOT`:**
  - `B1454` `G7` tests Dehn fillings `(1, 0)` and `(0, 1)` (where `(0, 1)` also has `H_1 = Z`!), confirming `U-ROOT-1`: `G:ROOT` requires the unstated premise that the puncture torus cusp remains **unfilled**.
  - `GM4` silently imports `GM1` (`T_{1,1}`); `GM3`'s parenthetical `|tr| > 2 in GL(2, Z)` is inaccurate for `det = -1` (`|tr(LP)| = 1` is pseudo-Anosov because `tr(LP^2) = 3 > 2`); and `{GM3, GM4, SE1, SE2}` selects only the **unbased** conjugacy class `[LR]` and **unoriented** manifold `m004` (`U-ROOT-2`, `U-ROOT-4`).

---

## 2. Detailed Comparison for `MC:Z6` (`B862`, `B1221`, and `B1221` Addendum)

- **Arcs opened on `main`:**
  - `frontier/B862_global_form/FINDINGS.md`
  - `frontier/B1221_global_form_path_independence/FINDINGS.md`
  - `frontier/B1221_global_form_path_independence/ADDENDUM_2026-08-31_the_Z6_needs_primitivity.md`
- **What is `the same`:**
  1. At integer scaling `q = 6 k Y` (`k >= 1`), our blind `derive_mc_z6.py` over continuous `Z(SU(3)) x Z(SU(2)) x (R / Z)` proves `K_k` is **cyclic of exact order `6k` for every positive integer `k`**, identical on `27`, `16` alone, and `10` alone, so `|K_k| = 6` holds if and only if `k = 1`. This independently reproduces `main`'s `2026-11-10` correction (`S306n`, `P-604`) in `B1221`'s addendum.
- **Three concrete findings where `main`'s arcs are incomplete or `different`:**
  1. **Uncorrected 12-point `U(1)` grid bug in `frontier/B1221_global_form_path_independence/FINDINGS.md` (`different`):**
     In `frontier/B1221_global_form_path_independence/FINDINGS.md` (line 35), the main table still reports `adjoint-only content | 72`. On the actual group `Z(SU(3)) x Z(SU(2)) x U(1)`, every `U(1)` angle acts trivially on `(8, 1)_0 (+) (1, 3)_0 (+) (1, 1)_0`, so the kernel is **infinite** (`Z_3 x Z_2 x U(1)`), as our blind `CTL-Z6-B` proved before opening `B1221`! The number `72` is `6 * 12` — the exact same finite-grid discretisation artefact on `U(1)` that `S306n` (`P-604`) corrected in `B1221`'s addendum, left standing in `frontier/B1221_global_form_path_independence/FINDINGS.md` itself.
  2. **Logical tension between `B862` and `B1221` (`cannot be derived from what is stated` without `U-Z6-1`):**
     - `B862` cites Tong (`arXiv:1705.01853`) to note that the Standard Model's local algebra and matter representations leave all four global quotients `Gamma in {1, Z_2, Z_3, Z_6}` open, and resolves that ambiguity by exponentiating inside `SU(5)`.
     - `B1221` then drops the global group embedding, computes `ker(rho_27) = Z_6` from `(su(3) (+) su(2) (+) u(1)_Y, 27)` alone, and concludes (`frontier/B1221_global_form_path_independence/arc_verdict.json`) that `(SU(3) x SU(2) x U(1)) / Z_6` is determined by `(algebra, 27)` alone!
     - **Why those two statements cannot simultaneously stand as written (`CTL-Z6-A`):** In the bare Standard Model, `ker(rho_16)` is **already** `Z_6` (`B1221`'s own row `the 16 alone | 6`). Knowing `ker(rho) = Z_6` only proves that `27` (or `16`) descends to `[SU(3) x SU(2) x U(1)] / Gamma` for **every subgroup `Gamma subseteq Z_6`**, namely **all four** `Gamma in {1, Z_2, Z_3, Z_6}`!
     - To select `Gamma = Z_6` uniquely, one must add an unstated postulate (`U-Z6-1`):
       - **Route A (Effectiveness postulate `G = G_tilde / ker(rho_matter)`):** Forces `/ Z_6` from `(algebra, 27)`, **but** also forces `/ Z_6` from `(algebra, 16)` in the bare SM alone (so `E_6` resolves nothing that effectiveness on the SM did not already resolve).
       - **Route B (Global simply-connected UV Lie group `G_UV = E_6^{sc}`):** Because `Z(E_6^{sc}) = Z_3` acts faithfully on `27`, `E_6^{sc}` (rather than `E_6^{ad} = E_6^{sc} / Z_3`) is required among compact connected forms of `e_6` (assuming no extra central cover). Then **path-independent global `/ Z_6` inside `E_6^{sc}`** requires proving that breaking `E_6^{sc}` by `<S>, <nu^c>` leaves a **connected** stabilizer torus and intersects `SU(3)_c x SU(2)_L` in `Z_6` — which `B1221` did not check, and which our blind **Theorem 2B** proved via the Smith normal form `[1, 1]` of `[S; nu^c]`!
  3. **Distinction between kernel order `|K_k| = 6k` and quotient Lie group isomorphism (`U-Z6-2`):**
     `B1221`'s addendum writes *"The global form is `Z_6` given the primitive integral normalisation of hypercharge."* Precisely stated (`Theorem 2A(4)`): what requires `k = 1` is `|K_k| = 6` inside the parameterised cover `SU(3) x SU(2) x U(1)`; for every positive integer `k`, the quotient Lie group `[SU(3) x SU(2) x U(1)] / K_k` is still isomorphic as a Lie group to `[SU(3) x SU(2) x U(1)_prim] / Z_6` via `(g_3, g_2, u) |-> (g_3, g_2, u^k)`.

---

## 3. Detailed Comparison for `W:INDEX3` (`B1632`, `B1634`, and `B1641`)

- **Arcs opened on `main`:**
  - `frontier/B1632_w45_verified_on_main/FINDINGS.md`
  - `frontier/B1634_w50_on_main/FINDINGS.md`
  - `frontier/B1641_w46_on_main_and_the_two_objects/FINDINGS.md`
- **What is `the same` (once `FK10`/`FK11`/`FK14` and uniform `m = (1, 1, 1)` are assumed):**
  1. Exact `Mp_2(Z)` closure `rho_T(S_mp)^2 = (rho_T(S_mp) rho_T(T_mp))^3 = +i I_3` with zero projective defect (`B1634` P5/P6), `T_mp`-exponents `(1/8, 3/8, 7/8)`, and incompatibility of `rho_T_bar` at weight `3/2` (`B1634` P5, `B1641` §2b).
  2. Canonical `n = 0` Euler characteristic `chi_{3/2}(rho_T, 0) = 0` (`h^0 = h^1 = 0`) and `dim M_{23/2}(rho_T) = 3`, `dim M_{27/2}(rho_T) = 3` (`B1634` V4/P4 — notably, `B1634` §4 discloses that its numerical rank spot-check became ill-conditioned beyond degree `d = 5`, whereas our `derive_w_index3.py` works over exact cyclotomic `Q(zeta_24)` with zero floats all the way through `d = 27`!).
  3. Across all `6` genuine `SL(2, Z)` character twists `rho_T (x) chi_eta^{4r}` (`r = 0..5`) allowed at weight `3/2`, five give `chi_{3/2} = 0` and exactly one (`r = 1`, i.e. `chi_eta^{+4}`, `j = 4`) gives `chi_{3/2} = 1` (`B1632` §2 and `B1634` P5!).
  4. Puncture boundary condition dependence (`U-IDX-3`): `B1641` W3 explicitly computes `index(Lambda_+, n) = n (|Lambda_+| - 3)`, giving `+-3` for `Lambda_+ = 0` or `L_6` and `+-1` for `V_2` or `V_4` (`GENESIS.md` `[v1.59]`).
- **What `cannot be derived from what is stated` and what is `different` (`U-IDX-1`, `U-IDX-6`):**
  1. **Bare statement underdetermination (`U-IDX-1`):** `W:INDEX3` + `TAG:LAMBDA` + `TAG:UNIT` alone cannot derive `+-3` without importing the surface `M_{1,2}` (which `B1634` §3 itself shows requires point-pushing inner automorphisms **not** present in the ruled braid group `<L, R>`!), the spin-Dolbeault operator, the parity-graded puncture condition `Lambda_+ = 0` (`+-3` vs `+-1`), weight `3/2`, and `rho_T`.
  2. **The uncounted cusp-uniformity gap (`U-IDX-6` / `CTL-INDEX3-C` — NOT tested in `B1632`, `B1634`, or `B1641`):**
     - `GENESIS.md` `SC:UNIT` defines *"the unit"* as *"the smallest move-invariant deviation from zero"*, and `B1641` W3 writes `index(Lambda_+, n) = n (|Lambda_+| - 3)` with a **single** integer `n` at the cusp.
     - **Our blind `CTL-INDEX3-C` disproves `SC:UNIT`'s claim that `n = 1` (`m = (1, 1, 1)`) is the smallest move-invariant cusp deviation:** on `X(1)` there is a single cusp `[infty]`, and its stabilizer in `Mp_2(Z)` is `<T_mp, Z>`, which is abelian and diagonal on the three distinct eigenlines `(e_{1/8}, e_{3/8}, e_{7/8})`. Therefore **every** integer pole vector `m = (m_1, m_2, m_3) in Z^3` defines a strictly `Mp_2(Z)`-equivariant ("move-invariant") parabolic bundle on `X(1)` of index `m_1 + m_2 + m_3`!
     - Explicitly, Basis Section #1 of `M_{27/2}(rho_T)` in `relays/a2_c1/derive_w_index3_out.txt` has leading `q^{1/8}`-orders `(9, 11, 7)` (dividing by `Delta = q^1 + ...` gives `q^{9/8}` and `q^{11/8}` holomorphic on the `1/8` and `3/8` lines and `q^{-1/8}` solely on the `7/8` line), spanning the `1`-dimensional global space for `m = (0, 0, 1)` of **index `+1`, not `+3`**!
     - Obtaining `+-3` therefore requires an **additional uncounted hypothesis** beyond move-invariance: restricting cusp boundary data to **parity-blind / coarse-divisor scalar twists `m = (n, n, n)`** pulled back from `X(1)`, which bundles `3 = rk(T)` elementary cusp shifts into "one unit".

---

## 4. Complete Log of Repository Files Opened in Commit 3 (Condition 3)

In addition to the pre-comparison files logged in `relays/a2_c1/BLIND_DERIVATIONS_AND_UNSAID_INPUTS.md` §5, **exactly seven** repository files on `main` were opened after `d003e482b` was pushed:
1. `frontier/B197_figure_eight_volume_torsionfree/FINDINGS.md` (lines 1–77)
2. `frontier/B1454_genesis_v1_verified_and_adopted/FINDINGS.md` (lines 1–158)
3. `frontier/B862_global_form/FINDINGS.md` (lines 1–49)
4. `frontier/B1221_global_form_path_independence/FINDINGS.md` (lines 1–83)
5. `frontier/B1221_global_form_path_independence/ADDENDUM_2026-08-31_the_Z6_needs_primitivity.md` (lines 1–63)
6. `frontier/B1632_w45_verified_on_main/FINDINGS.md` (lines 1–65)
7. `frontier/B1634_w50_on_main/FINDINGS.md` (lines 1–124)
8. `frontier/B1641_w46_on_main_and_the_two_objects/FINDINGS.md` (lines 1–93)

*(Correction to count in sentence above: **eight** files — the seven arc `FINDINGS.md` pages plus `B1221`'s addendum.)* Zero `.py` scripts of `main`'s arcs were opened or run, and zero empirical or held-out files were touched anywhere (`0 of 19`).

0 of 19.
