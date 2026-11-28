# PRE-REGISTRATION SCOPE CARD — `Card A2-WHOLE-CENSUS-E8-TWO-REGISTER`

**Date:** 2026-11-28  
**Seat:** `agy-002` (`P-885` seat code: `fam3-v1-high-03`, branch `agy-002/verify`)  
**Status:** PRE-REGISTERED BEFORE RUNNING ANY CENSUS COMPUTATION  
**Data Discipline:** **Strictly Blind (`0 of 19`).** Zero empirical values, zero comparisons with data, zero trial arcs (`B2011`–`B2017`), `imports: none`.

---

## 1. Scientific Question ("Play the Whole Instrument, Not Just `m004`")

In `CLAIM_2026-11-27_C8_two_registers.md` (`P-876`, independently verified `SAME` in our `A2-PEER-PHYS-C8`), the figure-eight knot exterior `m004` carries two commuting registers inside a single compact `E_8` connection (`Spin(13) x Spin(3) -> Spin(16) -> Ss(16) subset E_8`):
1. **Register 1 (Geometric `SL(2, F_25)` Holonomy -> `13` of `Spin(13)`):** a surjective cusp-parabolic representation `rho_geo: pi_1(M) ->> SL(2, F_25)` with full 2D `F_25` cusp lattice (`tau_cusp in F_25 \ F_5`) and non-trivial peripheral central spin sign (`Z = -I` on at least one peripheral curve).
2. **Register 2 (Dihedral Sheet Lift `BD_5` -> `3` of `Spin(3)`):** a surjective homomorphism `rho_sh: pi_1(M) ->> BD_5 = <r, j | r^5 = 1, j^2 = -1, j r j^{-1} = r^{-1}>` (order `20`), acting on the peripheral torus `pi_1(partial M)`.

On `m004`, joining these two registers collapses the `248 = 120 + 128` peripheral adjoint spinor kernel from **`8` down to `0`**.

**This card asks the whole instrument instead of assuming `m004`:** across **ALL `1,199` orientable 1-cusped hyperbolic census manifolds (`<= 6` ideal tetrahedra)** plus non-orientable **`m000` (Gieseking)**, what does the coupled `E_8` two-register mechanism actually do, which manifolds support each ingredient, and does the coupled `8 -> 0` lock select a tiny class or a broad family?

---

## 2. Pre-Registered Modules (`Q1`–`Q4`) & Neutral Expectations

### `Q1` — Universal `E_8` (`Ss(16)`) Peripheral Kernel Classification Theorem (Manifold-Independent)
- Directly enumerate all `248 = 120 + 128` weights in exact `Z/20Z` phase arithmetic across ALL `480` ordered `F_5`-bases `(v_1, v_2)` of `F_25`, all `3` non-trivial peripheral central spin signs `(s_1, s_2) in {+1, -1}^2 \ {(+1, +1)}`, and all `150` commuting peripheral pairs `(h_1, h_2)` in `BD_5` (plus the 1D `SL(2, F_5)` control case).
- **Pre-registered theorem to verify:** Across ALL `4` torus spin structures, the joined `128`-spinor peripheral kernel collapses `8 -> 0` **if and only if** `H_per = <h_1, h_2> <= BD_5` is cyclic of order `4` (`C_4 = <r^a j>`). For `H_per in {C_1, C_2}` the total spinor kernel stays **`8`**; for `H_per in {C_5, C_10}` it drops to **`6`** (quadratic residue shift) or **`4`** (non-residue shift) — strictly positive, never `0`.

### `Q2` — Exhaustive Exact `D_5` and `BD_5` Sheet-Register Census (`1,199` Orientable + `m000`)
- Directly from fresh SnapPy `3.3.2` fundamental-group presentations and peripheral curves (`relays/a2_whole_census_e8_two_register/a2_census_1200_presentations_and_gluing.json`, pure integers/strings, zero floats), exhaustively enumerate ALL surjective homomorphisms `pi_1(M) ->> D_5` (`order 10`) and `pi_1(M) ->> BD_5` (`order 20`) across all `1,199` orientable 1-cusped manifolds (`<= 6` tetrahedra) plus `m000`.
- Record exact integer counts for:
  1. `D_5`-surjective manifolds vs `BD_5`-surjective manifolds (identifying the exact `D_5 -> BD_5` homological lifting obstruction set);
  2. Exact partition of all `BD_5`-surjective manifolds by realized peripheral torus subgroup `H_per <= BD_5` (`C_1`, `C_2`, `C_4`, `C_5`, `C_10`);
  3. Exact set **`S_BD5_C4`** of manifolds admitting a `BD_5` surjection with `H_per = C_4` (the exact necessary & sufficient `BD_5` boundary condition for `8 -> 0` from `Q1`), and check `m004`, `m003`, and `m000` explicitly.

### `Q3` — Exact Geometric `SL(2, F_25)` Parabolic Register & Coupled `E_8` (`8 -> 0`) Intersection
- **Method A (Triangulation-Independent Exact Fricke Character Variety over `F_25^3`):** Across ALL 2-generator manifolds in `S_BD5_C4` (plus `m003`, `m004`, `m000`, and all `BD_5`-surjective 2-generator manifolds), exhaustively check all `14,999` irreducible Fricke triples `(x, y, z) in F_25^3` (`D != 0`) by exact `2 x 2` `SL(2, F_25)` matrix reconstruction for genuine cusp-parabolic representations (`tr(m) in {+2, -2}`, `tr(l) in {+2, -2}`, non-central `M, L`):
  * Classify every hit by: (i) full 2D `F_25` cusp lattice (`tau_cusp in F_25 \ F_5`, proving surjectivity onto all of `SL(2, F_25)` of order `15,600` by Dickson's theorem — also directly verified!) vs degenerate 1D `F_5` cusp lattice (`tau_cusp in F_5`); (ii) non-trivial central spin sign `(s_m, s_l) != (+1, +1)` (required for geometric spinor kernel `8` on a non-trivial torus spin structure).
- **Method B (Exact Thurston Gluing Equations over `F_25 \ {0, 1}`):** Across ALL `1,199` orientable manifolds (including all `158` 3-generator manifolds!), solve the exact integer Thurston edge-and-cusp gluing equations over `F_25 \ {0, 1}` (recording both `F_25 \ F_5` solutions and `F_5` solutions) so 3-generator manifolds in `S_BD5_C4` are audited too!
- **Exact Coupled Lock Set `S_E8_LOCK`:** Report the EXACT list and count of manifolds in the `1,199` census (and `m000`) that simultaneously satisfy Register 1 (full-lattice surjective parabolic `SL(2, F_25)` with `(s_m, s_l) != (+1, +1)`) AND Register 2 (`BD_5` with `H_per = C_4`), collapsing the `E_8` peripheral adjoint spinor kernel `8 -> 0`.

### `Q4` — Unsculpted Cross-Tabulation With `2T = SL(2, F_3)` and `H_1(M)`
- Independently compute exact `2T = SL(2, F_3)` surjections on the `S_BD5_C4` / `S_E8_LOCK` sets and cross-tabulate `S_E8_LOCK` against `2T`, `2T == 2`, `H_1(M) = Z`, and tetrahedron count `t in {2, 3, 4, 5, 6}`.
- **Neutrality pledge:** No target count is assumed. Whether `|S_E8_LOCK| = 1` (`m004` unique), small (`2..20`), or large (`> 50`), the exact certified integer counts and manifold lists will be reported transparently.

---

## 3. Verification Gates & Planted Fault Controls (`PF1`–`PF5`)

- **Runtime & Form:** Decisive script uses Python standard library ONLY (`python3 -I`, zero floats in AST or JSON output), accompanied by a 100% self-contained standalone exit-1 control (`0` stderr bytes under `python3 -I`).
- **Five Planted Fault Controls (`PF1`–`PF5`):**
  1. `PF1`: Omitting `BD_5` sheet action restores `m004` periodic kernel to `8` (not `0`).
  2. `PF2`: Replacing `C_4` (`j`) by `C_5` (`r`) or `C_2` (`-1`) leaves `128`-spinor kernel strictly positive (`4`/`6` or `8`, never `0`).
  3. `PF3`: Testing an explicit `D_5 -> BD_5` obstructed manifold (or `Z/2Z` torsion relator `g^2 = 1`) yields `n_BD5 == 0` when `j^2 = -1` cannot hold.
  4. `PF4`: Testing a degenerate `F_5`-only parabolic matrix pair (`tau_cusp in F_5`) fails the full-2D `F_25 \ F_5` lattice gate and has subgroup order `<= 240 < 15,600`.
  5. `PF5`: Corrupting `m004`'s relator breaks both `BD_5` (`0` lifts) and `SL(2, F_25)` (`0` parabolic hits).
- **Cold-Room Referee Gate:** After sealing unread producer outputs, an independent zero-shared-code Cold-Room Referee will re-verify `Q1`–`Q4` (plus independent SnapPy `SL2C` holonomy checks on the `S_E8_LOCK` manifolds) with `0` discrepancies required.

0 of 19.
