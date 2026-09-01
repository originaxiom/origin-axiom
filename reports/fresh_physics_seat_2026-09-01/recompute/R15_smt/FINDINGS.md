# R15 — B892, the Second Measurement Theorem: RECOMPUTED. Verdict: MATCH

R2 recomputation cell, fresh physics seat, 2026-09-01. Blind-first discipline observed.

## Blind ledger (read BEFORE writing my code vs AFTER)

**Before (claim + committed data only):** `B892_second_measurement/FINDINGS.md` (claim,
banked numbers, amendment scope), `wall_results.json`, `B877_fmt_review/FINDINGS.md` +
`REVIEWED_DOCUMENT.md` (setting, mu(rho), x_i = g8 + rho_i g16), `B874_measurement_ladder/results.json`
+ `joint_results.json` (censuses), `tests/test_b892_smt.py`, and the docstring header
(first 80 lines, definitions only) of `B1102.../e6_bracket_vendored.py` — the committed
DATA defining the charges: t = x^5 y − x y^5, W = x^8 + 14 x^4 y^4 + y^8, x8 = W, x14 = tW,
x16 = W^2, x22 = tW^2, embedded by x^{n−k}y^k ↦ ((n−k)!/n!) f^k·v in the principal-sl2 blocks.
**After (post-blind diff only):** `wall_search.py`, `B854.../e6_centralizer.py`,
`B874/FINDINGS.md` (2026-08-18 addendum), `B992/FINDINGS.md` (headline).

## My route (all code in this dir, written blind)

`r15_build_e6.py`: my own e6 Chevalley basis from the Cartan matrix (reflection closure,
Frenkel–Kac epsilon; Jacobi verified exactly on 400 random triples), my own principal sl2,
Sym^{2m} blocks for m in {1,4,5,7,8,11}, my own charge embeddings. Charges commute exactly /Q.
`r15_exact.py`: root-evaluation method, made exact — the charpoly of each measurement
pencil is interpolated EXACTLY over Q (flint) and its lowest lambda-coefficient factored
over Z; since the pencils are semisimple, the order of vanishing at a point equals the
extra nullity there, so every stratum dimension below is exact over the algebraic closure,
both directions (this is *stronger* than the banked mod-p squeeze).
`r15_types_modp.py` + `r15_second_prime.py`: type data (derived/center) certified mod p
at 40123 (the banked prime) AND 40039.

## Results, diffed against the bank

| quantity | banked | mine (method) | verdict |
|---|---|---|---|
| censuses z(x8),z(x14),z(x16),z(x22), core, Cent(C) | 30,12,30,12,30,12 | same (exact /Q ranks) | MATCH |
| enhancement cubic | mu(rho) = 500716339200 rho^3 − 2075673600 rho^2 − 4769856 rho + 2197 | 500716339200 x^3 − 159667200 x^2 − 28224 x + 1, multiplicity 16 | MATCH — mu(13x) ∝ mine; the 13 is the arc's own convention (`wall_search.py` line 54 applies `13*root` explicitly). E23 resolved. |
| dim z(x1) | 46 (so(10)+u(1)) | 46 exact /F (restriction of scalars: Q-nullity 138 = 3·46); derived 45, center 1 at both primes ⟹ D5 + u(1) | MATCH |
| dim z(x1, y*) | **14** | **14 exact over the closure**: slope polynomial on z(x1) factors as (even sextic)^2 · (even sextic)^6; each multiplicity-2 root adds exactly one antipodal weight-line pair to the kernel-12 | MATCH |
| decomposition | 11 + 3 = su(3)+su(2)+u(1)^3 | derived 11, center 3 at both primes; center >= 3 a priori (C ∩ ker lambda); reductivity ⟹ 14 = 11 ⊕ 3 exactly; 11-dim semisimple = A2+A1 uniquely | MATCH (14 = 8+3+3) |
| gamma_q = 13410, a_q = 2675 at p = 40123 | banked digits | −a_q/(13 gamma_q) ≡ 6167 mod p **is a root of my sextic** (and the mu-root × sextic-root grid gives nullity 14 on exactly the 6 matched pairs, 12 on the 12 unmatched) | MATCH, digit-level |
| wall is complex ("a imaginary") | numeric sign of det14 | exact: both sextics have even powers and all-positive coefficients ⟹ NO real roots; the u = s^2 cubic has three negative real roots ⟹ all six SM-wall slopes pure imaginary | MATCH (stronger: exact proof) |
| real-line scan (wall_results.json: only jump (pi/2, 30)) | numeric SVD scan | exact: no real slope wall exists; slope-infinity endpoint z(x1, g16) = z(Pi) = 30 | MATCH |
| within-C ladder {18, 14} | banked | multiplicity-6 sextic roots give dim 18 (derived 15, center 3), both primes; full line inventory over the closure: {12, 14, 18, 30} | MATCH |
| the skip (no su(5)) | 26 not reached; over the closure four non-real A4 points *elsewhere* | neither centralizer is 26 (46 and 14); NO 26-point anywhere on the (x14,x16) second-measurement line even over the closure (only mults 2 and 6 occur). The B874-addendum 26/A4 points live in P(C/<x1>) directions involving x22 — outside this family, consistent | MATCH |
| B992 completion (u(1)^3 = span(Y,chi,psi)) | banked elsewhere | compatible fact verified: the 3-dim center lies INSIDE the charge torus C (both primes) | consistent (B992's identification not re-derived here — out of cell scope) |

**Planted-positive control (exclusion discipline):** an A4-annihilating Cartan element
(Bourbaki nodes 2,6 charged, 1-3-4-5 killed) fed through the same pipeline returns
dim z = 26 exact /Q, derived 24 = A4 — i.e. su(5)+u(1)^2. The su(5)-exclusion check
could have fired and did not.

**Convention diff, fully closed:** my independently constructed charge vectors are
EXACTLY EQUAL (not merely proportional) to the committed instrument's `INV[8,14,16,22]`
(`r15_diff_vectors.py`), and my exact cubic equals the arc's hard-coded `CUBIC` verbatim.

## Notes

1. **Lock vacuity note (not a defect of the theorem):** `tests/test_b892_smt.py` asserts
   FINDINGS phrasing and the real-scan JSON only — it cannot fail if the mathematics
   were wrong. This cell supplies the recomputation the lock does not.
2. One banked digit not independently reproduced: "det14 = +2.79e9" is an internal,
   normalization-dependent tower quantity; the FACT it certifies (a imaginary, wall
   complex) is proved exactly here instead.
3. B950's language correction stands and is respected: the landing is 14-dimensional
   (su(3)+su(2)+u(1)^3 as complex type A2+A1+ab^3), two abelian factors above the 12-dim
   SM algebra. Nothing here touches Gate 5; no measured SM value used anywhere.
4. `smt_verified: false` in `wall_results.json` records only that the REAL-line scan
   found no wall — exactly as my exact no-real-root proof requires; not a failed check.

**VERDICT: MATCH** — every banked number (14 = 11+3, 46, the cubic, the {18,14} ladder,
the skip, gamma_q/a_q at 40123, the complex-wall fact) reproduces from an independent
construction, most upgraded from mod-p/numeric to exact-over-the-closure certificates.

Files: `r15_build_e6.py`, `r15_exact.py` (+ `r15_exact_out.json`), `r15_types_modp.py`,
`r15_second_prime.py`, `r15_center_in_C.py`, `r15_diff_vectors.py`, `r15_e6_data.pkl`.
(`r15_spectrum.py` was a first numeric draft, superseded by the exact route; kept for the record.)
