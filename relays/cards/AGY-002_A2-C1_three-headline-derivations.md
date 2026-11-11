# Card `A2-C1`: Second Derivations of `G:ROOT`, `MC:Z6`, and `W:INDEX3` From Their Statements Alone

- **Seat:** `agy-002` (`origin/agy-002/verify`, branched from `main` at `2f3984d27`)
- **Card ID:** `A2-C1` (pre-approved on `docs/seats/agy-002.md` under `M1`, `2026-11-11`)
- **Mask & data rule:** zero measured values, zero empirical comparisons, zero held-out targets (`0 of 19`); theorems stated in words and exact integers/rationals only.

---

## 1. The Package and the Question, in One Sentence

Under the closure verification programme (`M1`), can the three data-free conditional headline results `G:ROOT` (figure-eight root `m004`), `MC:Z6` (`[SU(3) x SU(2) x U(1)] / Z_6` global form and cyclic kernel of order `6k`), and `W:INDEX3` (four-dimensional index `±3` on the weave's surface given `Λ` and the unit) each be derived independently from their stated text and stated premises alone, and what unstated assumptions, conventions, or hidden inputs does each derivation actually require?

---

## 2. What Will Be Delivered, and What Done Means

Committed in strict causal order across three separate commits on `origin/agy-002/verify`:
1. **Commit 1 (this commit — before any derivation or script):** `relays/STATUS_AGY-002.md` and this pre-work card `relays/cards/AGY-002_A2-C1_three-headline-derivations.md`, sealing expectations, failure criteria, controls, and the pre-derivation file-access log.
2. **Commit 2 (blind second derivations + exact integer scripts + raw outputs + unsaid-inputs list, BEFORE opening any of `main`'s derivation scripts or arc `FINDINGS.md`):**
   - Three standalone Python exact-arithmetic scripts (under "relays/a2_c1/" for G:ROOT, MC:Z6, and W:INDEX3) using only Python standard library / exact rational-integer algebra, plus their verbatim raw output files;
   - One blind derivation and unsaid-premises report (under "relays/a2_c1/") stating each result as an exact theorem (or recording where the stated premises underdetermine the conclusion) and enumerating every unstated premise, representation choice, topological/orbifold convention, or normalisation needed along the way.
3. **Commit 3 (post-derivation comparison against `main`'s arcs + delivery relay):**
   - After Commit 2 is pushed, open `main`'s cited arcs (`B197` / `B1454` for `G:ROOT`; `B862` / `B1221` and its addendum for `MC:Z6`; `B1632` / `B1634` / `B1641` for `W:INDEX3`), compare each derivation and unsaid-inputs list against `main`'s record, classify each of `G:ROOT`, `MC:Z6`, `W:INDEX3` as **`the same`**, **`different`**, or **`cannot be derived from what is stated`**, log every file opened in Commit 3, write the closing delivery note in `relays/`, and update `relays/STATUS_AGY-002.md`.

---

## 3. Pre-Registered Expectations and How Each Result Could Come Out Wrong (Written Before Any Run)

### 3A. `G:ROOT` — *"given GM3, GM4, SE1 and SE2, the root is m004, the figure-eight knot complement"*
- **What we expect before computing:**
  1. For a once-punctured-torus bundle `M_phi` with monodromy `phi in GL(2, Z)` (`GM4`), `H_1(M_phi; Z) ≅ Z ⊕ Z^2 / (phi - I) Z^2` (assuming peripheral/puncture homology does not add free rank because a single puncture on a genus-1 surface bounds the commutator `[a, b]`, which lies in `[F_2, F_2]` and maps to `0` in `H_1(T_{1,1}; Z) = Z^2`).
  2. The torsion subgroup of `H_1(M_phi; Z)` is finite iff `det(phi - I) != 0`, of order `|det(phi - I)| = |1 - tr(phi) + det(phi)|`.
  3. Under `SE2` (orientable total space `M_phi`, meaning `det(phi) = +1`, `phi in SL(2, Z)` — *note: whether orientability of the 3-manifold bundle equals `det(phi) = +1` requires stating that base `S^1` and fibre are oriented compatibly*), `|det(phi - I)| = |2 - tr(phi)|`.
  4. Torsion-free `H_1` (`SE1`) requires `det(phi - I) = ±1`:
     - `2 - tr(phi) = +1  =>  tr(phi) = 1` (elliptic of order `6` in `SL(2, Z)`, excluded by `GM3` hyperbolicity `|tr(phi)| > 2`);
     - `2 - tr(phi) = -1  =>  tr(phi) = 3` (hyperbolic!).
  5. Over `SL(2, Z)`, the number of `SL(2, Z)`-conjugacy classes (and `GL(2, Z)`-conjugacy classes) of trace `3` equals the narrow/wide ideal class count of `Z[(1 + sqrt(5))/2]` (discriminant `3^2 - 4 = 5`), which has class number `1` and fundamental unit `epsilon = (1 + sqrt(5))/2` of norm `-1`! Therefore there is **one** `SL(2, Z)`-conjugacy class of trace `3`, represented by `LR = [[2, 1], [1, 1]]`, whose once-punctured-torus bundle is `m004`.
  6. Without `SE2` (`det(phi) = -1`), `|det(phi - I)| = |-tr(phi)| = 1` gives `tr(phi) = ±1` (hyperbolic since `tr(phi^2) = tr(phi)^2 - 2 det(phi) = 1 + 2 = 3`), represented by `LP = [[1, 1], [1, 0]]` and `-LP`, whose bundle is the non-orientable Gieseking manifold `m000`.
- **What would count as disagreement / coming out wrong:**
  - If `SL(2, Z)` has more than one conjugacy class of trace `3`, or if `det(phi) = +1, tr(phi) = -3` also gives `|2 - tr(phi)| = 1` (expect `|2 - (-3)| = 5 != 1`, giving torsion order `5`, `m003`), or if the puncture contributes an extra homology relation/generator changing `H_1(M_phi; Z)` from `Z ⊕ coker(phi - I)`, or if `GM3 + GM4 + SE1 + SE2` leaves an unstated ambiguity between `m004` as an *unoriented/oriented homeomorphism type* vs *framed/marked bundle* (e.g. `LR` vs `(LR)^{-1}` or `RL`) that `GENESIS.md` needed and left unsaid.

### 3B. `MC:Z6` — *"the global form is `[SU(3) x SU(2) x U(1)] / Z_6`, at the primitive normalisation of hypercharge only; the kernel is cyclic of order `6k`"*
- **What we expect before computing:**
  1. Let `G_tilde = SU(3) x SU(2) x U(1)` with `U(1) = {e^{i theta} : theta in R / 2 pi Z}`, where an element of fractional hypercharge `Y_phys` and integer charge `q = 6 k Y_phys` (for non-zero integer multiple `k >= 1` of the primitive integer hypercharge lattice `q_prim = 6 Y_phys`) transforms by `e^{i q theta}`.
  2. Wait — check carefully what *"the kernel is cyclic of order `6k`"* means!
     - An element `(g_3, g_2, u) in SU(3) x SU(2) x U(1)` acts as a scalar on every irreducible representation `(R_3, R_2)_q` of the Standard Model / `27` of `E_6` only if `(g_3, g_2)` lies in the centre `Z(SU(3)) x Z(SU(2)) = Z_3 x Z_2 ≅ Z_6`!
     - Let `g_3 = omega^a I_3` (`omega = e^{2 pi i / 3}`, `a in Z/3Z`), `g_2 = (-1)^b I_2` (`b in Z/2Z`), and `u = e^{i theta}` (`theta in R / 2 pi Z`).
     - On a Standard Model generation (or on the `27` of `E_6` decomposed under `SU(3)_c x SU(2)_L x U(1)_Y`), the `(3, 2)_{1/6}` quark doublet has integer primitive charge `q_prim = 1` (scaled charge `k`), `(3*, 1)_{-2/3}` has `q_prim = -4` (`-4k`), `(3*, 1)_{1/3}` has `q_prim = +2` (`2k`), `(1, 2)_{-1/2}` has `q_prim = -3` (`-3k`), `(1, 1)_{1}` has `q_prim = +6` (`6k`), plus `E_6` singlets/exotics `(3, 1)_{-1/3}` (`-2k`), `(3*, 1)_{1/3}` (`2k`), `(1, 2)_{1/2}` (`3k`), `(1, 2)_{-1/2}` (`-3k`), `(1, 1)_0` (`0`).
     - Triviality on `(3, 2)_{k}`: `omega^a (-1)^b e^{i k theta} = 1`.
     - Triviality on `(1, 2)_{-3k}`: `(-1)^b e^{-3 i k theta} = 1 => e^{3 i k theta} = (-1)^b`.
     - Triviality on `(3*, 1)_{2k}`: `omega^{-a} e^{2 i k theta} = 1 => e^{2 i k theta} = omega^a`.
     - Multiplying `e^{3 i k theta} = (-1)^b` and `(e^{2 i k theta})^{-1} = omega^{-a}` gives **`e^{i k theta} = (-1)^b omega^{-a}`**, which is ALREADY a `6`-th root of unity (`(e^{i k theta})^6 = 1`) and uniquely fixes `(a mod 3, b mod 2)` FROM `e^{i k theta}` (`a ≡ 2 (3 k theta / pi)...`, specifically `(e^{i k theta})^2 = omega^{-2a} = omega^a` fixes `a mod 3`, and `(e^{i k theta})^3 = (-1)^b` fixes `b mod 2`)!!
     - **BINGO (Predicted Algebraic Mechanism):** For ANY integer `k >= 1`, `e^{i k theta}` can be ANY `6`-th root of unity (`e^{6 i k theta} = 1`), i.e. `theta = 2 pi m / (6k)` for `m in Z / (6k Z)`, and for EVERY such `theta`, `a mod 3` and `b mod 2` are **uniquely determined** (`g_2 = e^{3 i k theta} I_2`, `g_3 = e^{2 i k theta} I_3` — verify signs in script!), so the map `m mod 6k -> (g_3(theta), g_2(theta), e^{i theta})` is an injective homomorphism `Z_{6k} -> Z(SU(3)) x Z(SU(2)) x U(1)` whose image is the EXACT ineffective kernel of order `6k`!
     - WAIT A SECOND! Look at the quotient group `[SU(3) x SU(2) x U(1)] / ker_k`: as a Lie group, `U(1) / Z_k ≅ U(1)` via `u -> u^k`, so `[SU(3) x SU(2) x U(1)] / Z_{6k} ≅ [SU(3) x SU(2) x U(1)_prim] / Z_6`! What changes with `k` is the **order of the kernel inside the parameterised group `SU(3) x SU(2) x U(1)`** (`6k`, equal to `6` iff `k = 1`, i.e. primitive normalisation of the `U(1)` circle!), AND deriving `[SU(3) x SU(2) x U(1)] / Z_6` from `THE_CLAIM.md` requires knowing **what matter representation is faithful** (e.g., that the theory contains the `27` of `E_6` or `16` of `Spin(10)`, AND does NOT contain fields of fractional `q_prim` or faithful `Z_6`-breaking charges, AND that the global group is defined as the **effective action group `G_tilde / ker(rho_matter)`** rather than an abstract cover with topological discrete gauge Wilson lines!).
- **What would count as disagreement / coming out wrong:**
  - If the kernel for general integer scaling `k` were NOT cyclic (e.g. `Z_6 x Z_k` when `gcd(6, k) > 1` — we predict it IS cyclic `Z_{6k}` for **every** `k >= 1` because `theta -> (g_3(theta), g_2(theta), e^{i theta})` projects bijectively onto the `6k`-th roots of unity in `U(1)`!), or if `27` vs `16` vs `10` gave different kernels, or if `THE_CLAIM.md`'s stated hypotheses fail to state the **effectiveness postulate** (`G_phys = G_tilde / ker(rho_matter)` as opposed to `G_tilde` itself or an intermediate quotient `[SU(3) x SU(2) x U(1)] / Z_2` or `/ Z_3`, which have the exact same local algebra and the exact same `27` representation!).

### 3C. `W:INDEX3` — *"given `Λ` and the unit, the chiral three is a four-dimensional index, `±3`, on the weave's own surface"*
- **What we expect before computing:**
  1. Look closely at `GENESIS.md` (`FK10`, `FK11`, `FK14` `[v1.28]`, `[v1.36]–[v1.43]`, `[v1.59]`):
     - The weave's surface is stated as `M_{1,2}` (the moduli orbifold of twice-marked elliptic curves, or equivalently the `Aut^+(F_2)` orbifold surface over the modular curve `M_{1,1} = H / SL(2, Z)` with universal punctured elliptic curve fibre!).
     - Over the modular curve `H / Mp_2(Z)` (or `M_{1,2}`), the triplet `T` (dimension `3`, one line per non-zero parity of `Z_2^2`) carries a rank-`3` vector-valued modular / metaplectic multiplier `rho_T` of `Mp_2(Z)` (`B_3 / <Delta^8>`), stated in `GENESIS.md` (`FK10 [v1.41]`) as isomorphic to the multiplier of `eta^{21} (theta_2^2, theta_3^2, theta_4^2)` with `T`-exponents `(1/8, 3/8, 7/8)` (sum `13/8`, or check mod `1` against `eta^{21}` + `(theta_2^2, theta_3^2, theta_4^2)`!).
     - Wait: let's check BOTH levels of `W:INDEX3`!
       - **First:** Can `W:INDEX3` be derived **solely from the bare one-line statement** (`"given Λ and the unit, the chiral three is a four-dimensional index, ±3, on the weave's own surface"`) + the bare definitions of `Λ` (`TAG:LAMBDA`: *"the dictionary's link"*) and `the unit` (`TAG:UNIT`: *"one unit of end data at the weave's cusp"*)? Or does deriving `±3` require a long chain of mathematical choices and definitions (what 4d operator on the non-compact orbifold `M_{1,2}`, which spin structure, why weight `3/2`, why `chi_{3/2}(rho_T) = 0` at `n = 0` cusp units, how `n = 1` uniform unit on all `3` cusp eigenlines shifts Riemann–Roch–Kawasaki / orbifold Dolbeault–Dirac index from `0` to `3 * 1 = 3`, and why the *uniform* twist `O(1 * delta)` on `T` rather than a rank-1 twist `(1, 0, 0)` giving index `1` is bundled inside "the unit")?
       - **Second:** Using the explicit mathematical ingredients stated in `GENESIS.md` (`Aut^+(F_2)`, `M_{1,2}`, the 3-dimensional parity representation `rho_T` of `B_3 / <Delta^8> = Mp_2(Z)`, weight `3/2`, orbifold elliptic orders `4` and `6` on `H / SL(2, Z)` and fibre cohomology), we expect before computing:
         1. On the modular base curve `X(1)` (with elliptic points `i`, `omega` and one cusp) twisted by a rank-`3` metaplectic bundle `V_{3/2}(rho_T)` at weight `k = 3/2` with cusp exponents `(1/8, 3/8, 7/8)` (at canonical/untwisted cusp condition `n = 0`), the holomorphic Euler characteristic `chi(X(1), V_{3/2}(rho_T) ⊗ O(n * cusp))` satisfies:
            - At `n = 0`: `chi = 0` (`h^0 = h^1 = 0`), matching `W45`'s canonical zero!
            - At `n = 1` ("one uniform unit of end data at the cusp", shifting each of the 3 cusp exponents down by `1`, or tensoring the rank-3 bundle by `O(cusp)`): by Riemann–Roch on the orbifold curve (`chi(E ⊗ O(n * p_infty)) - chi(E) = rk(E) * n = 3 * n`!), shifting by `n` uniform cusp units shifts the index by **`3n`** — so `n = 0` gives **`0`** and `n = 1` gives **`+3`** (and **`-3`** under the opposite orientation / conjugate grading)!
         2. AND from the four-dimensional Leray / fibration perspective `pi : M_{1,2} -> M_{1,1}` (fibre = elliptic curve punctured, or parity-twisted spinor on the fibre whose `H^0` has rank `1` per parity = `T` of Hodge weight generating weight `3/2` on the base): the 4d index reduces by Leray spectral sequence to `chi(M_{1,1}, R^0 pi_* (...) - R^1 pi_* (...))`, which equals `0` at `n = 0` and `±3` at `n = 1` uniform cusp twist!
- **What would count as disagreement / coming out wrong:**
  - If the orbifold Riemann–Roch formula on `(H / SL(2, Z), rho_T, k = 3/2)` at `n = 0` gives `chi != 0` (e.g. `±1` or non-integer due to inconsistent `Mp_2(Z)` central action `Z^2` vs `(-1)^{2k}`), or if the stated multiplier `eta^{21} (theta_2^2, theta_3^2, theta_4^2)` has `T`-exponents DIFFERENT from `(1/8, 3/8, 7/8) mod 1` (WAIT — let's flag this right now before computing: `21 / 24 = 7/8`! And `(theta_2^2, theta_3^2, theta_4^2)` has `T`-eigenvalues `(i, 1, 1)` or exponents `(1/4, 0, 0)` under `tau -> tau + 1`! `7/8 + (1/4, 0, 0) = (9/8, 7/8, 7/8) = (1/8, 7/8, 7/8)`, NOT `(1/8, 3/8, 7/8)` unless `T` is `L` acting on `(theta_2, theta_3, theta_4)` where `L: tau -> tau + 1` swaps `theta_3 <-> theta_4`!! Let's test that exact eigenvalue spectrum in Commit 2 — if `GENESIS.md`'s parenthetical `eta^{21}(theta_2^2, theta_3^2, theta_4^2)` vs `(1/8, 3/8, 7/8)` has a subtle `theta_3^2 ± theta_4^2` diagonalisation or typo, catching or verifying it from first principles will be HUGE!).

---

## 4. What This Card Rests On, and What It Must Not Touch

- **Rests on (files opened before Commit 1, complete list):**
  1. `docs/seats/README.md` (lines 1–156: shared seat protocol)
  2. `docs/seats/agy-002.md` (lines 1–63: `M1` assignment)
  3. `docs/seats/agy.md` (lines 1–41: role boundary between `agy-002` and `agy`)
  4. `WORKING_RULES.md` and `docs/POINT_REGISTER.md` diff in `95988c96b` (`P-789`–`P-799`)
  5. `scripts/seats/listen.py` (lines 1–156: background listener)
  6. `frontier/B1888_the_public_form_scrutinised/FINDINGS.md` (§ 3 only: the five independence conditions cited in `M1`)
  7. `frontier/B1858_the_closure_map/NODES.json` (JSON entries for `G:ROOT`, `MC:Z6`, `W:INDEX3` and their direct premise nodes `G:GM1`–`G:GM4`, `G:SE1`, `G:SE2`, `G:T-ROOT`, `MC:ALG`, `MC:HYP`, `MC:Y`, `MC:END`, `TAG:LAMBDA`, `TAG:UNIT`, `SC:UNIT`)
  8. `GENESIS.md` (lines 1–535: canonical statement & premises for `G:ROOT` and `W:INDEX3`)
  9. `docs/THE_CLAIM.md` (lines 1–63: canonical statement & premises for `MC:Z6`)
  10. `frontier/B1221_global_form_path_independence/arc_verdict.json` (1 line: the statement of `B1221`, cited in `M1`'s table)
- **Must NOT touch before Commit 2 is pushed:**
  - Zero `FINDINGS.md`, addenda, or `.py` scripts inside `frontier/` (including `B197`, `B862`, `B1221/FINDINGS.md`, `B1221/ADDENDUM_...`, `B1422`, `B1454`, `B1632`, `B1634`, `B1641`), zero `src/` library code, zero `tests/` code, and zero empirical/held-out target files anywhere in the repository (`0 of 19`).
  - Zero edits to any file outside `relays/` on `origin/agy-002/verify`.

---

## 5. Controls That Must Fail If the Work Is Broken (One Per Result)

1. **Control for `G:ROOT` (`CTL-ROOT`):**
   - Drop `SE2` (allow `det(phi) = -1`): the torsion-free hyperbolic filter MUST fail to select `m004` uniquely and MUST admit the `det = -1, tr = ±1` class (`LP`, `m000`). Drop `GM3` (allow `|tr(phi)| <= 2` in `SL(2, Z)`): the filter MUST admit elliptic `tr = 1` (order `6`, trefoil complement). Perturb `tr = 3` to `tr = -3` (`-LR`, `m003`): `|det(phi - I)|` MUST evaluate to `5 != 1` (non-trivial torsion `Z_5`).
2. **Control for `MC:Z6` (`CTL-Z6`):**
   - Replace the `27` (or SM chiral generation) by (a) adjoint-only fields (`(8, 1)_0 ⊕ (1, 3)_0 ⊕ (1, 1)_0`) or (b) integer-hypercharge-only fields (`q_prim in 6 Z`), or replace `k = 1` by `k = 2, 3`: the ineffective kernel computation MUST NOT return `Z_6` of order `6`! Specifically, at `k = 2, 3` on the `27` it must return cyclic order `12, 18` (`!= 6`), and at `k = 1` on integer-hypercharge-only quark/lepton test sets it must return a strictly larger kernel (`!= 6`). Also test whether `[SU(3) x SU(2) x U(1)]` itself (without the effectiveness quotient) acts faithfully on `27`: it MUST fail faithfulness with kernel of order `6k`.
3. **Control for `W:INDEX3` (`CTL-INDEX3`):**
   - Evaluate the same orbifold Riemann–Roch / polynomial-space dimension check at (a) `n = 0` cusp units (canonical cusp condition: MUST return `0`, NOT `±3`), (b) the conjugate multiplier `rho_T_bar` at weight `3/2` (MUST fail weight-`3/2` parity compatibility `Z^2 = (-1)^{2k} = -I` or fail holomorphicity at `n = 1`), and (c) a non-uniform single-eigenline cusp unit `m = (1, 0, 0)` (MUST return `1`, NOT `3`, exposing that "one unit" must mean one *uniform* move-invariant unit across all three parity lines!).

---

## 6. What Is Needed From `main` or From Another Seat

Nothing (`A2-C1` is pre-approved on `docs/seats/agy-002.md`; proceeding directly to Commit 2's blind derivations).

0 of 19.
