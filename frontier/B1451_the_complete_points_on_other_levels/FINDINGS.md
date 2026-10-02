# B1451 — THE COMPLETE POINTS ON OTHER LEVELS: on sixteen more levels every periodic curve reaches a κ = −2 point, the class index is zero at all 188 doubly parabolic points, and what the root's three-fold cover showed as single numbers splits — the ten and the five-bar of a background carry different torsions, and a coupling's value there is a product of two doublet torsions on the Higgs character's curve

cc, 2026-10-02. B1446 computed the boundary-parabolic points on one level, the root's three-fold cover, and found
single numbers: 2√2 on every sector, 8 for the up coupling and 16 for the others, class index zero. Leads L236 and
L237 left "other levels" open. This arc runs B1445's sixteen frame levels. Preregistration sealed at `5a0ca0c4` on
both remotes before any coupling was computed off the control. **Verdict: PROVED** (computed at 60 digits; six of
seven sealed predictions held, one failed and is explained; **the sealed instrument was found wanting at 40 of
its 188 index computations and those were recomputed at 110 digits, §3a**).

## 1. The objects

On a level, the periodic curve of a character (B1444) is followed from its reducible end round the complex e-plane
to κ = −2. The point is **parabolic** when the meridian has trace ±2 there. For a coupling (ℓ, η, A₁) of the frame:

- **With the extension at its end the bidoublet splits** into two doublets on the Higgs character's curve, of
  characters (α, β) = (A₁, A₁/η) and (A₁/ℓ, A₁/(ℓη)); its torsion is the product of theirs. Checked against the
  rank-four module once on every level: largest relative difference 4·10⁻¹³ (the end is taken at e = 10⁻¹⁴).
- For an up-type coupling the two doublets are dual to each other on every level but one (the ten's three sector
  characters coincide there), so **the up-type value is a square, t²**.
- Every doublet torsion is τ = 2 − (E + 1/E), E the eigenvalue of the monodromy on the fibre's cohomology, and a
  state and its sign twin have E and −E: **τ + τ′ = 4** (B1444). It is visible across the table: −LLRLR 1 has
  t = 5.1075… − 0.7128…i and −LRLRR 1 has 4 − t; the pairs ±LLLLLR 2 likewise.

## 2. The sealed run (`verification/run/`, `run_read.txt`)

| | prediction | prior | outcome |
|---|---|---|---|
| C1 | class index zero at every doubly parabolic point computed | 85% | **YES — 188 of 188**, 40 of them only after the repair of §3a |
| C2 | no coupling has torsion zero with the Higgs character at a parabolic point | 85% | **NO — 6 of 188** (§3) |
| C3 | up-type and down-type moduli differ on ≥ ¾ of the levels with both | 80% | YES, but **only 2 levels have both** in the selection |
| C4 | on no other level is every up-type modulus half of every down-type | 90% | **YES** |
| C5 | the ten's three sectors share a torsion, and the five-bar's two | 55% | YES on 16 of 16 — **forced on 15** (§4) |
| C6 | the ten and the five-bar differ on some background, on ≥ half the levels | 60% | **YES — 11 of 16** |
| C7 | a parabolic point reached for ≥ 80% of the characters | 55% | **YES — 209 of 212**, the other three elliptic |

| level | exponent | \|torsion\| at the background's own point: ten / five-bar / ν^c | up-type | down-type |
|---|---|---|---|---|
| −LR 3 | 10 | 2.4721 / 2.4721 / 12.2814; 6.4721 / 6.4721 / 9.8573 | — | 16 |
| +LLR 3, +LRR 3 | 10 | 2.1028 / 3.2870 / 3.4831; 8.2503 / 3.1392 / 1.0302 | 15.02, 18.74, 110.85, 302.28 | — |
| −LLRLR 1 | 12 | 0 / 0 / 9.7980 | 26.5951 | 0 |
| −LRLRR 1 | 12 | 4 / 4 / 8 | 1.7348 | 16 |
| −LLLRLR 1 | 15 | 0 / 0 / 0 | 38.31, 45.53 | — |
| −LRLRRR 1 | 15 | 4 / 4 / 4 | 5.914, 7.646 | — |
| +LLLRR 2, +LLRRR 2 | 30 | 10.78 / 3.12 / 2.94; 10.78 / 12.87 / 3.61; 13.64 / 3.07 / 7.69; 13.64 / 24.12 / 4.47 | 6.1115, 732.47 | — |
| −LLLRR 2, −LLRRR 2 | 30 | 10.08 / 6.61 / 10.33; 10.08 / 24.95 / 7.75; 10.35 / 5.80 / 2.54; 10.35 / 16.54 / 1.22 | 2.3344, 765.14 | — |
| +LLLLLR 2, +LRRRRR 2 | 45 | 0.60 / 1.81 / 3.43; 0.60 / 7.64 / 26.31; 4.44 / 7.28 / 13.16; 4.44 / 8.06 / 0.37 | 3.830, 12.557 | — |
| −LLLLLR 2, −LRRRRR 2 | 45 | 4.41 / 4.95 / 7.20; 4.41 / 11.48 / 22.31; 7.49 / 6.86 / 3.66; 7.49 / 9.98 / 15.43 | 22.30, 29.90 | — |
| +LR 4 | 15 | 4.26 / 3.11, 5.00 or 5.19 / …; 10.43 / 9.11, 11.12 or 14.52 / … | — | 16.57, 152.35 |

Mirror words (L ↔ R) carry the same numbers. Twenty-five-digit values in the records.

## 3. The prediction that failed: zeros, on curves of filling type

On −LLRLR 1 the six down-type couplings computed have torsion zero, and on −LLRLR 1 and −LLLRLR 1 every charged
sector of every background has torsion zero at the background's own point. These are B1444's curves of **filling
type**: the meridian has trace 2 along the whole curve and the matched doublets' torsion vanishes identically —
checked here at e = 0.01, 0.3 and 1.7 on both Higgs characters concerned, below 10⁻⁵⁹ each time. The zero is not a
property of the complete point. **The prior of 85% was written without recalling B1444's own two types**; the
record of that is this line.

## 3a. A defect in the sealed instrument, found by this arc's own lock, and its repair

The lock asked that the sister's three-fold cover return 2 ± 2√5 to thirty digits. It returned them to fourteen.
At some κ = −2 points κ has a critical point along the curve, so κ = −2 is a double root there (and at others the
continuation's Newton iteration converges slowly): the sealed instrument, whose test is a residual below 10⁻³⁰,
leaves the point 10⁻¹⁵ to 10⁻²⁰ away. The consequences, stated exactly:

- **Torsions** at those points are good to about fourteen digits. The tables above are unaffected.
- **The ranks behind the class index were not resolved at 40 of the 188 couplings** (all twelve of −LR 3, and 28
  on ±LLLRR 2 and ±LLRRR 2): a singular value near 10⁻²¹ was kept as non-zero, where the other 148 have a gap
  from 0.2 down to 10⁻⁵⁸. The sealed record says h¹ = (0, 0) at those forty. **The reader did not look at the gap,
  and reported "all zero" on ranks it had not resolved.**
- **The repair** (`verification/refine_degenerate.py`, `refine/`, `refine_run.txt`; not sealed): all sixty
  couplings of the five levels recomputed at 110 digits, the points polished by a Newton iteration whose step is
  doubled along the degenerate direction (to within 10⁻³³). Every rank then has a gap (smallest kept 0.26, largest
  dropped 10⁻³⁹). **At the forty, h¹ = (2, 2), not (0, 0); no class is interior on either side; the class index is
  zero.** At the other twenty the sealed ranks are confirmed.

So C1 stands on 148 sealed computations and 40 repaired ones, and the statement "the cusp forces the classes that
are there" now holds at all 188. This is the verifier-defect class (ERROR_LEDGER E52): an instrument wrong while
its verdict stood. B1446's 288 points on the root's three-fold cover have gaps from 0.074 down to 10⁻⁵⁹ and are
not affected.

## 4. What is forced and what is not

- **C5 is forced on fifteen levels:** there the sector characters of Q, u^c, e^c are one character and those of
  d^c, L are one character on every background, so the equalities say nothing. On −LR 3 half the backgrounds have
  three distinct characters in the ten, and the torsions agree all the same — but on that level every charged
  sector of a slope has one torsion.
- **C6 is not forced:** the ten and the five-bar are different modules and at the complete point they carry
  different numbers on eleven levels. On +LR 4 the five-bar takes three values (and ν^c three) over the backgrounds
  of one extension character, in the proportion 1 : 2 : 1.

## 5. Exact values (`verification/exact_values.py`, `exact_values_run.txt`; not part of the sealed run)

The point is polished to 300 digits and identified by PARI's `algdep`, accepted only when the polynomial is short
against the precision; the control returns x⁴ − 4x² + 64 for B1446's −√5 − √−3.

| level, Higgs character | a coordinate of the point | the doublet torsion t (up-type value t²) |
|---|---|---|
| −LR 3 | the root's three-fold cover's (x⁴ − 3x³ + 5x² − 6x + 4) | charged sectors 2 ± 2√5; ν^c (2 ∓ 3√5) ∓ 5√−3; down = (2 + 2√5)(2 − 2√5) = −16 |
| −LRLRR 1, (9, 3) | x⁴ − 2x² + 2; Z = −1 + i | x⁴ − 8x³ + 16x² + 64x + 64 |
| −LLRLR 1, (9, 9) | x⁴ + 2x² + 2; Z = 0 | 4 − (the above): x⁴ − 8x³ + 16x² − 64x + 320 |
| +LLLLLR 2, (27, 0) and (36, 0) | sextics, x⁶ ± 2x⁵ − 3x⁴ ∓ 6x³ + 2x² ± 5x + 3 | degree 12, one polynomial for both |
| +LLR 3 | degree 16 (two polynomials, in the preregistration) | not identified |
| −LRLRRR 1 | degree 8 | not identified at degree ≤ 48 |
| +LLLRR 2, (24, 24) | x⁴ − 2x³ − x + 4 | not identified |

"Not identified" is a statement about this search, not about the number.

## 6. What it means, and the fence

- **The single numbers of the root's three-fold cover were accidents of its exponent four.** In general a
  background's complete point carries several algebraic numbers: one for the ten, one or more for the five-bar,
  others for ν^c; and a coupling's value is a product of two doublet torsions on the Higgs character's curve, a
  square for the up type. The 16 of the down type recurs (−LR 3, −LRLRR 1, the control) and is not explained here.
- **The class index is zero at every doubly parabolic point on seventeen levels** (188 here, 288 in B1446). The
  door "an irreducible pinned point carrying the generation's index" is closed on everything computed; chirality
  stays at the reducible end. These modules are twists of a self-dual module by a character, which is the shape
  the unproved vanishing statement of B1329–B1332 concerns. **The preregistration's parenthesis "(the module is
  not self-dual)" was loose**: the module is self-dual exactly when the twisting character has order two.
- **Imported expectation, stated separately:** that other levels would show a ratio between coupling types as
  clean as the control's one half. They do not; the values within one level range over a factor of 300
  (2.33 and 765.14 on −LLLRR 2), between backgrounds, not between members of one orbit.
- **The fence:** a torsion is not a mass; the three members of a deck orbit have the same values at these points
  (the difference is on the branch of B1447); nothing computed selects the complete point; twelve couplings and
  eight extension characters per level; up-type and down-type both occur on only two levels of the selection.
  **0 of 19.**

## 7. Not computed (leads L236, L237)

The values on the branches of B1447 on these levels; the 16; the exact fields of the unidentified torsions; the
levels' remaining couplings; a proof of the vanishing statement.
