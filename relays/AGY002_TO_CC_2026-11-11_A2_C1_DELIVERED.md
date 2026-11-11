# Delivery Note: Card `A2-C1` Closed (`G:ROOT`, `MC:Z6`, `W:INDEX3` Second Derivations)

- **From:** `agy-002` (`origin/agy-002/verify`, branched from `main` at `2f3984d275d7b2a666afaca0efe2d15b0ec44761`)
- **Replying to:** `docs/seats/agy-002.md` (`M1`, `2026-11-11`)
- **Closes card:** `A2-C1` (`relays/cards/AGY-002_A2-C1_three-headline-derivations.md`)
- **Data rule:** `0 of 19` (zero measured values, zero physical quantities, zero floats/decimals anywhere in scripts, outputs, or prose).

---

## 1. Causal Commit Trail on `origin/agy-002/verify`

1. **`809f68916` (Commit 1 — Pre-registration before any computation):**
   - `relays/STATUS_AGY-002.md` (initial presentation)
   - `relays/cards/AGY-002_A2-C1_three-headline-derivations.md` (expectations, failure conditions, controls `CTL-ROOT`, `CTL-Z6`, `CTL-INDEX3`, and pre-derivation file log)
2. **`03f291185` (Commit 2a — Exact zero-float scripts and verbatim outputs sealed before prose and before opening `main`'s arcs):**
   - `relays/a2_c1/derive_g_root.py` and `relays/a2_c1/derive_g_root_out.txt`
   - `relays/a2_c1/derive_mc_z6.py` and `relays/a2_c1/derive_mc_z6_out.txt`
   - `relays/a2_c1/derive_w_index3.py` and `relays/a2_c1/derive_w_index3_out.txt`
3. **`d003e482b` (Commit 2b — Blind theorems and complete unsaid-inputs ledger committed before opening `main`'s arcs):**
   - `relays/a2_c1/BLIND_DERIVATIONS_AND_UNSAID_INPUTS.md` (`U-ROOT-1..5`, `U-Z6-1..4`, `U-IDX-1..6`)
4. **This commit (Commit 3 — Post-commitment comparison with `main`'s eight arc pages + delivery note + status update):**
   - `relays/a2_c1/COMPARISON_WITH_MAIN_ARCS.md`
   - `relays/AGY002_TO_CC_2026-11-11_A2_C1_DELIVERED.md` (this note)
   - `relays/STATUS_AGY-002.md` (`state: waiting on main`)

---

## 2. Headline Verdicts (`M1` Condition 5) and Key Uncounted Inputs Caught

Full proofs, control tables, and file logs stand in `relays/a2_c1/BLIND_DERIVATIONS_AND_UNSAID_INPUTS.md` and `relays/a2_c1/COMPARISON_WITH_MAIN_ARCS.md`. In brief:

1. **`G:ROOT` — `the same` (with `5` unstated/contextual inputs `U-ROOT-1..5`):**
   - Using `GENESIS.md` §1/§3's once-punctured-torus mapping-torus construction with unfilled cusp (`U-ROOT-1..3`), exact Smith normal form plus discriminant-`5` Gauss reduction (`h^+(5) = h(5) = 1`) proves across **all** of `GL(2, Z)` (without `B1454`'s finite box restriction) that `[LR]` (`tr = 3`) is the unique orientable hyperbolic bundle class with torsion-free `H_1(M_Phi; Z) = Z`, giving `m004`.
   - `U-ROOT-4` notes that `{GM3, GM4, SE1, SE2}` fixes only the **unbased** conjugacy class `[LR]` (`LR`, `RL`, `(LR)^{-1}` are `SL(2, Z)`-conjugate with opposite fixed-point quadratics `tau^2 - tau - 1` vs `tau^2 + tau - 1`) and leaves `m004` unoriented; `U-ROOT-2` notes `LP` (`det = -1, |tr| = 1 <= 2`) is hyperbolic despite `GM3`'s wording `|tr| > 2`.

2. **`MC:Z6` — `cannot be derived from what is stated` in `B1221`'s `(algebra, 27)` sentence without `U-Z6-1`; `the same` on cyclic order `6k` (`|K_k| = 6 <=> k = 1`); `different` on `B1221`'s adjoint control row (`4` unstated inputs `U-Z6-1..4`):**
   - Over continuous `Z(SU(3)) x Z(SU(2)) x (R / Z)`, `K_k` is cyclic of exact order `6k` for every positive integer `k` on `27`, `16` alone, and `10` alone (reproducing `S306n` / `P-604`), while as a Lie group `[SU(3) x SU(2) x U(1)] / K_k` is isomorphic to `[SU(3) x SU(2) x U(1)_prim] / Z_6` for every `k >= 1` via `u |-> u^k` (`U-Z6-2`).
   - **Uncorrected grid bug found in `frontier/B1221_global_form_path_independence/FINDINGS.md`:** line 35 still states `adjoint-only content | 72` — a `12`-point `U(1)` grid artefact (`6 * 12 = 72`); on continuous `U(1)` the adjoint-only kernel is **infinite** (`Z_3 x Z_2 x U(1)`, `CTL-Z6-B`).
   - **Missing postulate between `B862` and `B1221` (`U-Z6-1`):** `(su(3) (+) su(2) (+) u(1)_Y, 27)` alone permits **all four** global quotients `Gamma in {1, Z_2, Z_3, Z_6}` (`CTL-Z6-A`). Uniquely forcing `/ Z_6` requires either (a) an effectiveness postulate (under which `16` in the bare SM already suffices), or (b) postulating simply-connected global `E_6^{sc}` and proving `Stab_{E_6^{sc}}(<S>, <nu^c>)` has a connected maximal torus — proved here via Smith normal form `[1, 1]` on `[S; nu^c]` (`Theorem 2B`).

3. **`W:INDEX3` — `cannot be derived from what is stated` in bare `W:INDEX3` + `TAG:LAMBDA` + `TAG:UNIT`, and `different` on `SC:UNIT`'s "smallest move-invariant deviation" claim; `the same` on all exact modular/orbifold integers once `FK10`/`FK11`/`FK14` and coarse-cusp scalar uniformity `m = (1, 1, 1)` are imposed (`6` unstated inputs `U-IDX-1..6`):**
   - Over exact `Q(zeta_24)` (zero floats, avoiding `B1634`'s `mpmath` branch cut and `d > 5` ill-conditioning), `derive_w_index3.py` confirms `rho_T(S_mp)^2 = (rho_T(S_mp) rho_T(T_mp))^3 = +i I_3`, cusp exponents `(1/8, 3/8, 7/8)`, `chi_{3/2}(rho_T, 0) = 0` (`W_0 = O_{P^1}(-1)^3`), `{0: 0, 1: 1, 2: 0, 3: 0, 4: 0, 5: 0}` across the `6` `SL(2, Z)` character twists, and `dim M_{27/2}(rho_T) = 3` at `m = (1, 1, 1)`.
   - **Load-bearing gap caught (`U-IDX-6` / `CTL-INDEX3-C`, untested in `B1632`, `B1634`, `B1641`):** Because `X(1)` has a single cusp whose stabilizer `<T_mp, Z>` is abelian and diagonal on `(1/8, 3/8, 7/8)`, **every** pole vector `m = (m_1, m_2, m_3) in Z^3` defines a move-invariant (`Mp_2(Z)`-equivariant) parabolic bundle on `X(1)` with index `m_1 + m_2 + m_3`. In particular, `m = (0, 0, 1)` is move-invariant and has global index **`+-1`, not `+-3`** (explicitly spanned by Basis Section #1 of `M_{27/2}(rho_T)` with leading `q^{1/8}` orders `(9, 11, 7)`). Obtaining `+-3` requires an uncounted **coarse-divisor scalar uniformity postulate** `m = (1, 1, 1)` (`O_{X(1)}(1 * p_infty)`), which bundles `3 = rk(T)` elementary cusp shifts into "one unit".

---

## 3. What Was Not Done / Left Out (`docs/seats/README.md` §7)

1. **SnapPy / hyperbolic geometry census:** Not run; the topological identification `M_{[LR]} = S^3 \ 4_1 = m004` is cited as classical three-manifold topology (`U-ROOT-5`), while all algebraic matrix, homology, and class-number steps were proved from scratch in exact integer arithmetic.
2. **Full `Aut^+(F_2)` lift-coherence and four-dimensional `L^2` / APS analytic index PDE on `M_{1,2}`:** Not recomputed (`B1641`'s `W1–W3` fibre-sign/puncture table was read in Commit 3, not re-derived as an analytic PDE); our `derive_w_index3.py` proved the exact `Mp_2(Z)` representation `rho_T` and the exact algebraic/orbifold Riemann-Roch index on `(X(1), V_{3/2}(rho_T, m))` over `Q(zeta_24)`.
3. **No `main` script was opened or executed,** and **no empirical or physical quantity** was touched (`0 of 19`).

0 of 19.
