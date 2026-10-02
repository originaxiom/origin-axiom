# B1451 PREREGISTRATION — THE COMPLETE POINTS ON OTHER LEVELS: what the frame's sectors and couplings carry where a periodic curve reaches κ = −2, on the sixteen levels of B1445

**Sealed 2026-10-02, before any coupling is computed on any level but the control. Seat: cc (main). Occasion: leads
L236 and L237 — B1446 computed the boundary-parabolic points on one level, the root's three-fold cover, and found
there (i) every sector of a background with one torsion, (ii) the up-type coupling at 8 and the others at 16, (iii)
class index zero at all 288 doubly parabolic points. "Other levels" was left open.**

## 0. The quantifier (P0)

For every level of the population and every item selected in §2: the κ = −2 point of the periodic curve of the
character (B1444), reached by continuation; the torsion of a doublet sector there; and for a coupling (ℓ, η, A₁) of
B1445's frame, the bidoublet with the Higgs character η at its κ = −2 point and the extension ℓ at its reducible end,
and with both at their κ = −2 points. The scope sentence names no level.

## 1. The objects

- A κ = −2 point is **parabolic** when the meridian has trace ±2 there (the peripheral group is parabolic or trivial
  in PSL(2)), **elliptic** otherwise; only parabolic points are counted, elliptic ones and failures to reach are
  reported.
- **With the extension at its end the bidoublet splits** into two doublets on the Higgs character's curve, of
  characters (α, β) = (A₁, A₁/η) and (A₁/ℓ, A₁/(ℓη)), so its torsion is the product of two sector torsions at the
  Higgs character's point. The instrument computes it that way and checks the rank-four module once per level.
- With both characters at their κ = −2 points: the class index of the rank-four module (B1446's `index_num.py`).

## 2. The population (fixed before the run)

B1445's sixteen frame levels, `mass_term.FRAME`: −LR 3, +LLR 3, +LRR 3, −LLRLR 1, −LRLRR 1, −LLLRLR 1, −LRLRRR 1,
+LLLRR 2, −LLLRR 2, +LLRRR 2, −LLRRR 2, +LLLLLR 2, −LLLLLR 2, +LRRRRR 2, −LRRRRR 2, +LR 4. On each: up to eight
extension characters of generation-shaped backgrounds and up to twelve couplings of B1445's list, spread evenly over
the sorted lists. Instrument `verification/complete_points.py` (on the sealed engines of B1444, B1445, B1446), driver
`population.py`, reader `read_complete.py` (run twice on the control, identical output).

## 3. What has been seen before the seal (disclosed in full; outputs in `exploration/`)

- **The control**, the root's three-fold cover through the sealed instrument and reader (`control/`,
  `reader_control.txt`): 15 of 15 points parabolic; every sector of all 48 backgrounds at 2√2; up 8, down = lepton =
  neutrino 16; class index 0 at 24 of 24 doubly parabolic points. B1446 reproduced.
- **Sector torsions at the background's own point on two population levels**, by a scratch script:
  **+LLR 3** — the ten and the five-bar differ: |torsion| 2.1028 (Q, u^c, e^c), 3.2870 (d^c, L), 3.4831 (ν^c) on 24
  backgrounds and 8.2503, 3.1392, 1.0302 on the other 24; the points have a coordinate of degree 16
  (x¹⁶ − 5x¹⁴ + 8x¹² − 3x¹⁰ + x⁸ − 13x⁶ + 14x⁴ + 1 and x¹⁶ − 9x¹⁴ + 32x¹² − 50x¹⁰ + 12x⁸ + 63x⁶ − 52x⁴ − 48x² + 64);
  one character of order two there has an elliptic κ = −2 point (meridian trace √2).
  **−LR 3** — the five charged sectors share 2 + 2√5 or 2 − 2√5, ν^c has (2 ∓ 3√5) ∓ 5√−3; the points have the
  coordinates of the root's three-fold cover.
- **+LR 4, unlabelled:** generation-type sectors at six characters took the moduli 4 (slope ±1, a point with
  X = (1 ∓ √−7)/2 or 1), five values between 3.11 and 5.19 (slope ±0.382) and five between 9.11 and 16.41 (slope
  2.618); which sector carries which was not computed (the run was stopped).
- +LR 2 (not in the population): the κ = −2 point is elliptic (meridian trace 1).
- **Not seen:** any coupling, or any class index, on any level but the control; any sector on the other thirteen.

## 4. Sealed predictions (each can come out either way)

| | prediction | prior |
|---|---|---|
| C1 | The class index is zero at every doubly parabolic point computed. | 85% |
| C2 | No coupling has torsion zero with the Higgs character at a parabolic point. | 85% |
| C3 | On at least three quarters of the levels with both, the up-type and the down-type moduli differ. | 80% |
| C4 | On no level but the control is every up-type modulus half of every down-type modulus. | 90% |
| C5 | On every level, on every background, the ten's three sectors share a torsion and the five-bar's two share one. | 55% |
| C6 | On at least half the levels with a table, the ten and the five-bar differ on some background. | 60% |
| C7 | A parabolic point is reached for at least 80% of the characters attempted. | 55% |

## 5. What each outcome would mean (written before the data)

- **C1 NO** would be the first non-zero index at a pinned point: a place where chirality could live, and a
  counterexample to the vanishing statement of B1329–B1332 in a setting where it is not known to apply (the module
  is not self-dual). **C1 YES** adds instances to that unproved statement and closes this door on these levels.
- **C3, C6 YES:** the equalities of the control (one torsion for every sector; a single ratio between the coupling
  types) are accidents of its small exponent; in general a background's complete point carries several algebraic
  numbers, different for the ten and the five-bar and for up-type and down-type couplings.
- None of the outcomes is a value of the Standard Model: a torsion is not a mass, the members of a deck orbit are
  not told apart at these points, and nothing computed selects the complete point. 0 of 19.

## 6. Hashes at seal

See `ARTIFACT_HASHES.txt`.
