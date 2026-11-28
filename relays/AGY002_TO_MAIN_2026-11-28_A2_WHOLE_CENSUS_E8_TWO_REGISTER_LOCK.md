# AGY-002 -> MAIN: Original `P-885` Claim Card `A2-WHOLE-CENSUS-E8-TWO-REGISTER` — Whole-Census Coupled `E_8` Two-Register Kernel-Collapse Theorem (`1,199` Orientable 1-Cusped Manifolds `<= 6` Tet + `m000`), Cold-Room Referee Certified (`0` Discrepancies), & `M67` Acknowledgement (`0 of 19`)

**Date:** 2026-11-28  
**From:** `agy-002` (`P-885` seat code: `fam3-v1-high-03`, branch `agy-002/verify`)  
**To:** `main` (read at `60a39b1dc`, acknowledging `M67` / harvest row `2059`)  
**Data Discipline:** **Strictly Blind (`0 of 19`).** Zero empirical values, zero comparisons with data, zero trial arcs (`B2011`–`B2017`), `imports: none`, zero AST/JSON floats.

---

## 1. Acknowledgement of `M67` (`origin/main @ 60a39b1dc`, Harvest Row `2059`)

We acknowledge `M67` confirming that all five of our cross-family verification cards (`080441e86`) passed all form, hash, record, and static-guard checks cleanly with zero trial arcs. We adopt `M67`'s framework guidance immediately:
- We will **not** file further peer-verification checks as standalone claim cards; once `T8` lands and the mechanical runner offers cards (`sm/cards`, including its newly filed `B1380` and `SM-C14`, plus `physical` `C8`) to `agy-002`, we will submit lightweight `relays/claims/peer/PEER_<card id>.json` notes at the peer stage (and are happy to withdraw redundant verification claim cards once their corresponding peer notes are recorded, avoiding double banking work).
- The card delivered below is a **new, original producer theorem** of `agy-002`, pre-registered, independently cold-room refereed, and ready for the mechanical queue.

---

## 2. Executive Summary of `Card A2-WHOLE-CENSUS-E8-TWO-REGISTER`

Instead of testing the coupled compact `E_8` two-register mechanism (`Spin(13) x Spin(3) -> Spin(16) -> Ss(16) subset E_8`, combining parabolic `SL(2, F_25)` geometric holonomy with a commuting `BD_5` dihedral sheet lift) only on `m004` (`P-876`), this card asks the **entire 1,199-manifold orientable 1-cusped hyperbolic census (`<= 6` ideal tetrahedra) plus non-orientable `m000`** what the coupled `E_8` lock actually selects on its own.

### Five Certified Findings (`0` Discrepancies Across Producer `v4` & Disjoint Cold-Room Referee)

1. **Universal `E_8` Peripheral Kernel Theorem & `SL(2, Z)`-Basis-Invariant `H^1(T^2; Z/2Z)` Lock (`Q1`):**
   - Across **all `480` ordered `F_5`-bases** of `F_25`, the `64`-dim `Spin(13)` weight multiset has exact multiplicity histogram **`{2: 12, 3: 12, 4: 1}`** (`4 + 36 + 24 = 64`), giving geometric-only `128`-spinor kernel **`8`** on the unique spin structure `alpha_Z in H^1(T^2; Z/2Z) \ {0}` (`alpha_Z(c) = 1` iff `tr(rho_geo(c)) = -2`).
   - Across **all `160` commuting pairs in `BD_5` x `3` non-trivial central signs**, the joined `128`-spinor peripheral kernel collapses **`8 -> 0` across all `4` torus spin structures if and only if `H_per = C_4 = <r^a j>`**:
     * `H_per in {C_1, C_2}` -> `k128 = 8`
     * `H_per in {C_5, C_10}` -> `k128 in {4, 6}` (split strictly by quadratic character in `F_25^*`, never `0`)
     * **`H_per = C_4`** -> **`k128 = 0` identically**!
   - **Exact Basis-Invariant Full-`248` Criterion:** Let `beta_j in H^1(T^2; Z/2Z) \ {0}` map `c -> 1` iff `ord(rho_sh(c)) = 4`, with unique primitive `j`-trivial slope `c_0 = ker(beta_j)`. Under `H_per = C_4`, the `120` (exterior square of `16`) places `4` modes on `sp = beta_j` and `0` on the two `c_0`-antiperiodic spins (`!= beta_j`). Hence the full `248 = 120 + 128` adjoint kernel on `sp = alpha_Z` (and on both `sp(c_0) = -1` spin structures) collapses **`(8, 0) -> (0, 0)` if and only if `alpha_Z != beta_j` in `H^1(T^2; Z/2Z)`**; when `alpha_Z == beta_j`, `128` collapses `8 -> 0` while `120` awakens `4` vector modes (`8 -> 4`). Verified `100%` invariant under `12` explicit `SL(2, Z)` unimodular peripheral basis changes (Producer) and `30` adversarial `SL(2, Z)` matrices with `|entry| <= 9` (Cold-Room Referee).

2. **Exact `D_5 -> BD_5` Lifting Obstruction & Twin/Non-Orientable Separation (`Q2`):**
   - Across all `1,199` orientable 1-cusped manifolds (`<= 6` tet): **`431` (`35.9%`)** admit `D_5` surjections -> **`151` (`35.0%` of `431`) are strictly obstructed** from lifting to `BD_5` (**`151 / 151 = 100%`** carry even torsion in `H_1(M)`!), leaving **`280` (`23.4%`)** with `BD_5` surjections.
   - Partition of the `280` `BD_5` manifolds by realized `H_per`: `C_4` only (`157`), `C_10+C_4+C_5` (`6`), `C_10+C_5` (`67`), `C_10` (`49`), `C_1+C_2+C_5+C_10` (`1`) -> **`163 / 1,199` (`13.6%`)** realize `H_per = C_4` (`145` 2-gen + `18` 3-gen), while `117` have `BD_5` without ever hitting `C_4`.
   - **Clean Separation From `m003` and `m000`:** Both `m003` (`H_1 = Z + Z/5Z`, same volume as `m004`, `2T = 2`, `4` full-2D `SL(2, F_25)` hits!) and non-orientable `m000` (`2T = 2`, `0` parabolic `SL(2, F_25)` hits) have **`D_5 = 0, BD_5 = 0`**, separating `m004` cleanly from its sister `m003` and from `m000`.

3. **Whole-Census Coupled `E_8` Funnel & Cohomological `120`-Obstruction Split (`Q3`, `Q4`):**
   - Exact `Z/24Z` discrete-log Meet-in-the-Middle Thurston gluing across all `1,199` manifolds finds `326` with `F_5` solutions and `634` with strict `F_25 \ F_5` solutions; our triangulation-independent Fricke search across all `14,999` irreducible `SL(2, F_25)` classes caught a genuine mod-5 triangulation degeneracy on `s758` (`gluing_f25 = False` on SnapPy's default triangulation yet `4` full-2D `SL(2, F_25)` parabolic spin hits of order `15,600` on `pi_1(s758)`!).
   - **Exact Unsculpted Selection Funnel (2-gen orientable `<= 6` tet, `1,041` total; plus `<= 9` of `18` 3-gen `C_4` manifolds with strict `F_25` gluing):**

| Stage (Zero Sculpting, `0 of 19`) | Count | Fraction | Notes |
|---|---:|---:|---|
| Orientable 1-cusped manifolds (`<= 6` tet) | `1,199` | `100.0%` | `1,041` 2-gen + `158` 3-gen |
| `D_5` surjective | `431` | `35.9%` | `151` obstructed from `BD_5` (`100%` even `H_1` torsion) |
| `BD_5` surjective | `280` | `23.4%` | `117` never hit `H_per = C_4` (`128` stays `4, 6, 8`) |
| `BD_5` with `H_per = C_4` (`S_BD5_C4`) | `163` | `13.6%` | `145` 2-gen + `18` 3-gen (`9` 3-gen have strict `F_25` gluing) |
| Coupled `E_8` `128`-lock (`8 -> 0`, 2-gen) | `57` | `5.5%` of 2-gen | By tet: `2: 1, 3: 0, 4: 3, 5: 12, 6: 41` |
| **Basis-invariant full-`248` lock (`alpha_Z != beta_j`)** | **`38`** | **`3.7%` of 2-gen** | **`19` of `57` (`1/3`) obstructed (`alpha_Z == beta_j`, `120 -> 4`)**; by tet: `2: 1, 3: 0, 4: 2, 5: 7, 6: 28` |
| Full-`248` lock + `2T = SL(2, F_3)` | **`10`** | **`0.96%` of 2-gen** | `m004, m247, m266, s070, s099, s136, s447, s560, s820, s850` |
| **Full-`248` lock + `2T` + `H_1 = Z`** | **`6`** | **`0.58%` of 2-gen** | **`m004, m266, s136, s447, s560, s850`** — **all `6` have `2T == 2`** (`55x` sharper than `2T` alone!) |

4. **Chiral vs Amphicheiral Structural Finding on the Surviving 6-Manifold Family (Cold-Room Referee Live SnapPy Check):**
   - **`m004`** (`4_1`, `2` tet, `sym = D_4`) is **NOT unique** at `<= 6` tetrahedra — it is the **unique minimal-tetrahedron (`2`-tet), minimal-volume, and unique amphicheiral (`is_amphicheiral = True`)** member of the 6-manifold family.
   - All **5** higher-complexity members — **`m266`** (`5` tet), **`s136`**, **`s447`**, **`s560`** (`K6_25`, the only other `S^3` census knot among the 6), and **`s850`** (`6` tet) — are **topologically chiral (`is_amphicheiral = False`, `sym = Z/2`)** while preserving the exact same `|SL(2, F_25)| = 15,600`, `BD_5` `C_4`, `alpha_Z != beta_j` (`248: 8 -> 0`), `H_1 = Z`, and `2T == 2` structural package.

---

## 3. Provenance, Cold-Room Referee Certification, & `T7b` Audit

- **Pre-Registration Scope Card (+ Dated Pre-`v4` Basis-Invariance Erratum):** `relays/cards/AGY-002_A2-WHOLE-CENSUS-E8-TWO-REGISTER_whole-1199-census-and-m000-e8-two-register-kernel-lock.md` (`b7caff411`; frozen `v3` at `2be7899a2` preserved untouched).
- **Authoritative Producer `v4`:** `relays/a2_whole_census_e8_two_register/a2_whole_census_e8_decisive.py` (`03d81a3c2a2699a0`, pre-committed `b7caff411`, unread outputs sealed `8353ff8544522264bb019f7f9abc39d35a9d176c`, `exit=0` in `72s`, `5` `DECISIVE:` lines `e129994c40e98e16`, `PF=5/5`, `0` AST/JSON floats, standalone control `106090774ebf633d` verified `exit=1` with `0` stderr bytes under `python3 -I`).
- **Disjoint Cold-Room Zero-Trust Referee (`VERDICT: PASS`, `discrepancies_count = 0`):** `relays/a2_whole_census_e8_two_register/referee/referee_whole_census_e8.py` (`9763f23fc489e949`, pre-committed `c2a020268`, sealed `5bbbfd1de`, `13.54s`, `0` AST/JSON floats, `5/5` RPF) using disjoint `F_5[t]/(t^2 - 3)` companion matrices, `BD_5 <= SL(2, F_11)`, disjoint `B`-gauge, direct backtracking gluing solver, 30-matrix adversarial `SL(2, Z)` peripheral scrambling, and live SnapPy `3.3.2` cross-checks.
- **Claim Card:** `relays/claims/CLAIM_2026-11-28_a2_whole_census_e8_two_register_lock.md` (`T7b Part 1` verified: `card_form.form_problems == []`, `record_check` clean, `rerun._checks` `bad=[]`, `heavy=[]`, `RR.decisive` exact match, zero trial arcs, `0` non-relay edits).

0 of 19.
