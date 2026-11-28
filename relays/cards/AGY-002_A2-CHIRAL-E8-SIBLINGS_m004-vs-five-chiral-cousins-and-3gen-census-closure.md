# PRE-REGISTRATION SCOPE CARD — `Card A2-CHIRAL-E8-SIBLINGS` (Phase 1 of Listening Masterplan)

**Date:** 2026-11-28  
**Seat:** `agy-002` (`P-885` seat code: `fam3-v1-high-03`, branch `agy-002/verify`)  
**Status:** PRE-REGISTERED BEFORE RUNNING ANY PHASE-1 COMPUTATION  
**Methodology:** `docs/LISTENING_PROTOCOL.md` (Rungs 1–3 ONLY: Field/Reality, Galois Torsor, Forced Form/Relation), **Strictly Blind (`0 of 19`)**, zero trial arcs (`B2011`–`B2017`), `imports: none`.

---

## 1. Scientific Question (Listening at the `B2008` Chirality Seam)

In `A2-WHOLE-CENSUS-E8-TWO-REGISTER` (`M68` clean, harvest row `2064`), running the coupled compact `E_8` two-register kernel-collapse test (`SL(2, F_25)` + `BD_5` `C_4` + basis-invariant `alpha_Z != beta_j`, collapsing `248 = 120 + 128` cleanly `8 -> 0`) across all `1,041` 2-generator orientable 1-cusped manifolds (`<= 6` tetrahedra) narrowed the census to **`38` full-`248` locks**, **`10` with `2T = SL(2, F_3)`**, and **exactly `6` integer-homology (`H_1 = Z`) `2T` manifolds**:
- `m004` (`2` tet, amphicheiral, `2T == 2`)
- `m266` (`5` tet), `s136`, `s447`, `s560` (`K6_25`), `s850` (`6` tet) — all `5` topologically chiral, all `2T == 2`.

Separately, `B2008` identified **sourced handedness** (breaking the mirror lock without choosing an orientation by hand) as the central open question of the Listening Campaign.

This card tests **both** halves of the chirality seam without sculpting:
1. Does any of the `5` chiral siblings share `m004`'s **arithmeticity** (`Rung 1`: degree-2 imaginary quadratic invariant trace field + integral traces) and **`2T` parabolic rigidity** (`SM-R635`-style Fox calculus) while natively breaking mirror symmetry — OR does arithmeticity/rigidity force `m004` uniquely, proving an **exact Arithmeticity-vs-Chirality Dilemma** at `<= 6` tetrahedra?
2. Do any of the remaining **`18` 3-generator `BD_5 C_4` manifolds** (`m201, m207, m235, m261, s051, s426, s556, s573, s640, s733, s754, s788, s837, s854, s882, s890, s942, s961`) achieve the full `248: 8 -> 0` lock + `2T` + `H_1 = Z`, closing **100% of all `1,199` orientable 1-cusped manifolds (`<= 6` tetrahedra)**?

---

## 2. Pre-Registered Modules (`C1`–`C4`) & Neutral Expectations

### `C1` — Exact Invariant Trace Field, Arithmeticity, & Mod-5 Splitting (`Rung 1`)
- Across all `10` `lock_248_2T` manifolds (`6` `H_1 = Z`: `m004, m266, s136, s447, s560, s850`; `4` torsion: `m247, s070, s099, s820`) plus `m003`:
  1. Discover exact irreducible integer minimal polynomials `P_M(X) in Z[X]` of the geometric shape field `k(M) = Q(z_1, ..., z_t)` via `sympy` `DomainMatrix.lll` from `64`-digit SnapPy shape strings, express every `z_j = Q_j(X) in Q[X]/(P_M(X))`, and **symbolically certify `gluing_rect == 0 mod P_M(X)` in exact rational arithmetic** (zero reliance on floating-point approximations!).
  2. Certify exact field degree `[k(M) : Q]`, signature `(r_1, r_2)`, trace integrality of `pi_1(M)^{(2)}` (`tr(a^2), tr(b^2), tr((ab)^2), tr([a,b])`), and exact Maclachlan–Reid Theorem 8.2.3 arithmeticity verdict (`1`-cusped manifold is arithmetic iff `k(M)` is imaginary quadratic of degree `2` with integral traces).
  3. Compute exact factorization of `P_M(X) mod 5` over `F_5`, verifying directly whether the geometric shape field itself splits off a degree-2 factor (`F_25`) mod `5`.

### `C2` — Exact Rational Fox-Calculus `Ad(2T)` Cohomology & Rigidity (`Rung 3`)
- Generalizing `SM-R635`: across all `10` `lock_248_2T` manifolds plus `m003` and `m000`, build exact integer `3 x 3` signed-permutation matrices for `Ad(2T) = A_4 subset SO(3)` and compute via exact `sympy` `QQ` Fox calculus on every `Aut(2T)`-orbit of surjections `pi_1(M) ->> 2T`:
  * `dim H^0(pi_1(M); ad rho_2T)`, `dim H^1(pi_1(M); ad rho_2T)`, and `dim H^1_par = dim ker(H^1(M) -> H^1(partial M))`.
  * Verify `SL(3, Z)` basis-scrambling invariance (`Guardrail 3`, `10` unimodular matrices `det = +1`) of all cohomology dimensions.

### `C3` — Native Orientation / Mirror-Breaking Audit (`B2008` Open Seam)
- Across all `6` `H_1 = Z` survivors (`m004, m266, s136, s447, s560, s850`):
  * Record exact symmetry group, `is_amphicheiral`, Chern–Simons invariant `CS(M) mod 1/2` (nonzero `!= 0, 1/4` certifies orientation-reversing obstruction), complex cusp shape mirror-asymmetry (`Re(tau_cusp) mod 1/2 != 0`), AND exact mod-5 cusp-shape spectrum `{tau_cusp in F_25 \ F_5}` across all `SL(2, F_25)` parabolic representations (checking symmetry under `tau -> -tau` and Frobenius `tau -> tau^5`).

### `C4` — 100% Census Closure on All `18` 3-Generator `BD_5 C_4` Manifolds
- Across all `18` 3-generator manifolds in `S_BD5_C4`:
  1. Compute exact `H_1(M)`, exact `2T = SL(2, F_3)` surjection orbit counts, exact `F_25` Thurston gluing status, and exact `F_25` Ptolemy variety solutions (`obstruction_class='all'`).
  2. For every 3-generator manifold with `F_25` gluing solutions (and any with `2T > 0` or `H_1 = Z`), verify explicitly whether it admits a full-2D parabolic `SL(2, F_25)` representation (`|H| > 240`, `R_i == I_2` verified on exact `SL(2, F_25)` matrices) with basis-invariant `alpha_Z != beta_j` (`248: 8 -> 0`), closing `100%` of all `1,199` orientable 1-cusped manifolds at `<= 6` tetrahedra.

---

## 3. Neutral Expectations & Falsifiers (`PF1`–`PF5`)

- **Neutrality:** We do not predict in advance whether any of the `5` chiral siblings is arithmetic or `H^1_par == 0` rigid, nor whether any 3-generator manifold enters the `H_1 = Z` + `2T` + `248`-lock set. Both outcomes (chiral arithmetic survivor vs Arithmeticity-vs-Chirality Dilemma) are reported strictly as computed.
- **Five Planted Fault Controls (`PF1`–`PF5`):**
  1. `PF1`: Perturbing `m004`'s minimal polynomial `X^2 - X + 1 -> X^2 - X + 2` fails exact symbolic gluing certification (`!= 0 mod P`).
  2. `PF2`: Replacing `Ad(2T) = A_4` by the reducible trivial representation `I_3` increases `dim H^0` from `0` to `3` and breaks `H^1` rigidity.
  3. `PF3`: Testing a non-integral (non-monic) degree-2 polynomial fails the trace-integrality / arithmeticity gate.
  4. `PF4`: Checking `m004`'s amphicheiral symmetry vs a genuinely chiral manifold separates `is_amphicheiral` and `CS mod 1/2` cleanly.
  5. `PF5`: Corrupting a 3-generator relator breaks its `2T` / Ptolemy / `SL(2, F_25)` verification.
- **Cold-Room Referee Gate:** Disjoint zero-shared-code `self` subagent referee certifying `VERDICT: PASS` and `discrepancies_count = 0`.

0 of 19.
