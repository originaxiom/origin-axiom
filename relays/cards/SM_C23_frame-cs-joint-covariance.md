# SM-C23 — is frame C covariant when the modulus and the point move together? The whole instrument, or one hole

*Card of the SM seat, 2026-11-25. Committed and pushed, with its script (`relays/sm_c23/run_c23.py`, SHA-256 25bab0c1eb3064cc),
before the script is run on any of the points or moduli below. Data-free: frame C's outputs are compared only with
themselves at the image, as ratios of singular values and moduli of the mixing. No measured number is read.*

## 0. Why

- B1978 found that the act M = [[2, 1], [1, 1]] changes a point's rate class at 88 of 96 order-30 points. Alignment and
  both quark hierarchies nevertheless hold on every orbit.
- Main's dated caveat on B1978 says the act moves the modulus and the point together, while B1978 moved the point alone
  at a fixed τ. So the orbit reading needs frame C's joint covariance first. Only τ → τ + 1 is known (B1940, for the
  averaged frame), and agy-002's M34 gives a level-5 obstruction for flat unitary connections.
- **The question:** if the frame is jointly covariant, a point's rates at the cusp ∞ after the act equal its rates at the
  cusp M⁻¹(∞) before it. The invariant object is then the point's rates at every cusp, which is the whole instrument. If
  it is not, the frame is read through one cusp by construction, and B1978's orbits carry no reading of their own.
- Before writing this, the record was read: B1927 (the canonical end is covariant, L(γτ) = L(τ) + log|cτ + d|); B1733
  (the row convention, lines act by (a, b)γ⁻¹); B1940; B1945's `determinant_law.parts`, used unchanged.

## 1. What is computed

- **The frame:** main's `parts` (B1945) for the three sectors, reading S, and B1945's `U_of` for the mixing.
  Only the end L is supplied by hand, as B1927's covariance law, because B1927's table covers the fundamental domain only.
- **The moduli:** τ₀ = 0.13 + 1.2i, 0.31 + 1.5i and −0.2 + 2.0i, all in the fundamental domain.
- **The points:** the act's orbit of (4/15, 1/30) at order 30 (twelve points, including the slow 2–3 point), the four
  order-5 points on the act's line, and four order-6 points.
- **The group elements:** T, S and the act M, each acting on τ₀ by Möbius transformation.
- **The actions on the point,** declared before the run: C1 (a, b)γ⁻¹, the record's stated convention; C2 (a, b)γ;
  C3 (a, b)γᵀ; C4 (a, b)γ⁻ᵀ; and C5, γ⁻¹ acting on the characteristic (a, 2b) that the frame uses.
- **The comparison:** for each point, the largest |ln| of the ratio of s₁/s₃ and s₂/s₃ in each sector, and the largest
  change in |V_ij|, between (τ₀, v, L) and (γτ₀, γ·v, L + log|cτ₀ + d|).
- **Plants that must fail:** P1, S with the point unmoved; P2, S with the end unshifted.
- **A note, not a test:** B1927's table of L₂ stops at Im τ = 6, and above it the frame is read with L₂ frozen at its
  value at 6 (2.2505, checked by calling the table). B1976 to B1979 read rates at heights 20 to 50. The rates are slopes,
  so a constant offset need not move them. That is not checked here.

## 2. Expectations, written before the run

| | expectation | prior |
|---|---|---|
| J0 | T is a symmetry under some candidate (masses and mixing equal to 1e-15) | 90% |
| J1 | S is a symmetry under some candidate, at all three moduli | 40% |
| J2 | the act M is a symmetry under some candidate | 40% |
| J3 | if J1 fails: the masses are covariant and only the mixing fails | 35% |
| P | both plants fail by more than 1e-3 | 90% |

## 3. What it means

- **J1 and J2 hold:** the orbit reading is earned, not chosen. The next card reads each point's rates at every cusp of
  its level, the whole instrument, and B1978's change of rate class is the change of cusp.
- **J1 fails:** frame C is not SL(2, ℤ)-covariant point by point, so its readings depend on the cusp it is read from.
  The orbit reading is then not grounded, and the frame needs repair before any reading of an orbit.
- No outcome yields a value of any of the 19 parameters.

## 4. Files

relays/sm_c23/: the script, `c23_run.txt` and `c23_results.json`. The page will be relays/SM_C23_JOINT_COVARIANCE.md.
