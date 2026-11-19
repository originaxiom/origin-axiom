# Card W-B3: frame D1 at the norms, and its cusp mixing on this seat's code (M78's two asks)

**Seat:** the web seat (chat1). **Opened:** 2026-11-19, at main's request (M78, on B1962). Written and committed before
any of its outputs is computed. **Kind:** `result:` data-free. Under the author's ruling of 2026-11-15, frame outputs
are computed and printed. No data is opened and nothing is set beside a measured number.

**M78 asks two things.**
- **Q1, identity E at the norms.** Does D1's own norm equal frame C's at the shifted charges q′ = q − c·q_H/2? It is the
  last item P-861 owes.
- **Q2, the second computation.** Compute B1962's table on this seat's code, which builds D1 directly: |V| at c = ±2,
  for the four reading pairs, at the 24 points of order 5, Re τ = 0.13, heights 6 and 30.

**Not blind.**
- M78 states B1962's outcome: at height 30, no pair aligned under either sign, smallest diagonal 3e-5 or less; at height
  6, three pairs deranged and (S̃, S̃) partial (0.126); the signs agree.
- Through the mask, B1962's output shows four of its numbers: at c = 0 and height 6, (S, S) gives 0.9932 and 0.1161,
  and (S̃, S̃) gives 0.9752 and 0.2215; at c = −2 and +2, height 6, (S̃, S̃) gives 0.1252 and 0.1256, with 0.9921.
- This seat's W-B2 stage 4 found E failing with the flat norm over the cell about the moved pole. Its referee found E
  holding, unsealed, with the bundle's flat unitary metric.

---

## Q1: the derivation, written before computing

Notation as W-B2: T = 2τ; v(u) = (θ[α, β](u, T), −i θ[α + ½, β](u, T)).
- Frame C's kernel is K_C(u) = v_x(u) v_y(u)ᵀ / θ₁(u, τ), with x = (q_L a, 2q_L b) and y = (q_R a, 2q_R b) at the point
  w = aτ + b.
- D1's kernel is K_D1(u) = v_x(u) v_y(u)ᵀ / θ₁(u + h, τ), with h = c·q_H·w. Its pole is at u = −h.

- **The shift law** (standard): θ[α, β](u + pT + r, T) = e^(−iπTp² − 2πip(u + β + r)) θ[α + p, β + r](u, T).
- With z − h = z + pT + r, p = −c·q_H·a/2 and r = −c·q_H·b, both components of v_x get the same factor, and the new
  characteristic is the twist of q′_L. Likewise for y. And θ₁(z − h + h) = θ₁(z). So
  **K_D1(z − h) = e^(λz + μ) K_C′(z)**, with λ = 2πi·c·q_H·a and μ a constant, as 2×2 matrices.
- **Consequences.**
  - The residues: every channel's residue is multiplied by the same e^μ. Ratios and singular vectors are unchanged.
    This is W-B2 stage 3's E.
  - The norms: |P_D1(z − h)/R_D1|²·m(z) = |P_C′(z)/R_C′|² pointwise, with m(z) = |e^(λz)|^(−2) = e^(4π·Im h·Im z/Im τ),
    the flat unitary metric of the Higgs's twist, equal to 1 at the pole. So every regularised norm over the same cell
    about the pole agrees.
  - The constant term: the plain Laurent constant shifts, a0_D1 = a0_C′ + λ. The metric's Chern connection is
    ∂ + ∂ log m, and ∂_z log m = −λ. So the covariant constant term equals a0_C′.
- **So, before any computation:** E holds at the norms, at every height, if D1's norm is taken with the flat unitary
  metric and its a0 with that metric's connection. It fails with the flat norm over the cell (W-B2 stage 4). With the
  metric's norm but the plain a0, Theorem 90's weight differs through |a0 + λ|² at the 20 points with a ≠ 0.
- **Which is D1's own** stays a reading [J]. W-B2 stage 4's referee found the cell norm not periodic in the Higgs's
  point, and the unitary metric periodic.

**Checks of Q1** (computed in the script, in extended precision unless stated):
- **E1, pointwise.** At Re τ = 0.13 and heights 1.7, 6 and 30, for every sector, c = ±2, the 24 points and 5 points z
  of the cell about the pole: K_D1(z − h)·e^(−λz) / K_C′(z) is one constant, over the four entries and the five z.
- **E2, the residues.** R_D1/R_C′ is the same for every non-zero channel, and the zero channels coincide.
- **E3, the constant term.** a0_D1 (plain) − λ equals a0_C′.
- **E4, the integral (double precision, this seat's quadrature).** At W-B2 stage 4's three bulk moduli, the mark and
  the twin, every sector, c = ±2, reading S:
  - D1's frame with the metric m in its quadrature norm and the covariant a0, against frame C′ with its own quadrature
    norm: the largest relative difference of σ₂/σ₁ and σ₃/σ₁.
  - The same with the plain a0 (the metric kept).
  - The same with neither: W-B2 stage 4's construction, as a plant.

## Q2: the second computation

**The build, all in extended precision at 30 + 2·Im τ digits (B1962's rule), on this seat's code:**
- τ = 0.13 + iy, y = 6 and 30; the 24 points (a, b); the sectors up, down and leptons with the charges of B1656's table;
  q_H = +3, −3, −3; c = +2 and −2, and c = 0 (frame C) as the control.
- **Thetas:** this seat's own series, summed over a window about the largest term, with derivatives term by term.
- **Residues:** D1's kernel at its own pole, R_s = n_s(−h)/θ₁′(0), where n_s(u) is the channel's contraction of
  v_x(u) v_y(u)ᵀ (W-F22's channels). A channel is zero if |n_s(−h)| is below 10^(−dps/2) times the largest product of
  components.
- **a0:** covariant, n_s′(−h)/n_s(−h) − λ.
- **c_s:** B1919's closed form, re-typed here, at the channel's characteristic of frame C′. This rests on Q1: the
  pointwise identity makes D1's metric norm equal frame C′'s. The closed form is checked against this seat's quadrature
  (C1).
- **The end:** this seat's W-F24 interpolation of B1927's and B1667's tables, at (0.13, min(y, 6)).
- **The weight:** u_s = √(2πL + c_s − π|a0_s|² e^(−2L))·R_s; zero if the channel is zero or the root's argument is not
  positive.
- **The triplet:** W-F22's thetanull form, with the τ-derivative taken term by term, not by finite difference.
  Readings S and S̃ = ε S̄ εᵀ.
- **The coupling and the mixing:** W-F22's contraction (blocks QJ, QI, QK); U the left singular vectors, columns by
  ascending singular value; V = U_upᴴ U_down.
- **Reported, per c, height and reading pair:** the smallest diagonal |V| and the largest off-diagonal |V| over the 24
  points, classified by B1962's thresholds:
  - ALIGNED if the smallest diagonal is at least 0.9 at every point;
  - DERANGED if it is below 0.1 at some point;
  - PARTIAL otherwise.
- **Reported, the leptons:** B1962's three numbers per reading and height (distance from a 0/1 pattern, plain and
  transposed; the normalised spectra's difference).
- **Reported, the fork:** the same table with the plain a0.

**Controls.**
- **C0, frame C (c = 0) at height 6:** (S, S) 0.9932 and 0.1161; (S̃, S̃) 0.9752 and 0.2215, to the four printed
  digits. If C0 fails, Q2 is void.
- **C1, the closed form against this seat's quadrature:** frame C's c_s at τ = 0.13 + 1.7i and 0.13 + 2.9i, every
  channel, every sector, the 24 points, within 1e-6 absolute. In the same cases, this seat's Laurent a0 against
  Kronecker's form, 2πiα + θ₁′(ατ + β)/θ₁(ατ + β), at the characteristic used for c_s: within 1e-20.
- **C2, the triplet:** the term-by-term derivative against W-F22's finite difference at τ = 0.13 + 1.7i, within 1e-8
  relative.
- **C3, the zero channels:** the numerical zeros coincide with the theta-constant rule, θ[α, β](0) = 0 exactly when
  (α, β) ≡ (½, ½) mod 1, at the characteristics of C1.
- **C4, precision:** two points at height 30 recomputed at 20 more digits; every |V| entry within 1e-15.

**Expected [J].**
- **X1.** E1, E2 and E3 hold to 1e-20 relative at every height.
- **X2.** E4: D1 with the metric and the covariant a0 against frame C′ below 1e-6; with the plain a0 above 1e-3 at some
  case; with neither above 1e-2 (W-B2 stage 4's 0.54 and 0.70).
- **X3.** Q2 agrees with M78's summary: at height 30 no pair is ALIGNED under either sign, and every smallest diagonal
  is below 1e-3; at height 6 three pairs are DERANGED and (S̃, S̃) is PARTIAL near 0.125; both signs give the same
  classes. The two (S̃, S̃) values at height 6 agree with B1962's 0.1252 and 0.1256 to three digits.
- **X4.** The leptons copy the down sector transposed (distance below 1e-10), at both heights and both signs.

**Failure.**
- If a control fails, the part it guards does not stand.
- If X3 fails, this seat's table and B1962's differ. The relay says where, and B1962's verdict stays provisional.
- If X1 fails, the derivation above is wrong as written.

---

## After the run: the follow-up (W-B3-F), written after the run's output was read and before its script

**What happened.** The run (script 89c491f47, output fc1ff20f7) stopped with a ZeroDivisionError. It stopped in the
fork's variant, the plain a0, at c = +2 and height 6, in the leptons' normalised spectra: the lepton coupling had no
non-zero singular value. Every check of Q1 and every covariant table had been printed before. Three things were not
reached:
- C4, the precision control;
- the plain variant at c = +2 (both heights);
- the script's own verdict lines for C0, X3 and X4, and its summary file. Their numbers are in the output.

The cause is a case the script did not guard: with the plain a0, Theorem 90's weight can have a non-positive argument in
every channel of a sector, and that sector's coupling then vanishes. E4 had already counted this in double precision:
29 of its 36 plain cases vanish.

**The follow-up script** (`wb3_followup.py`) imports the run's functions unchanged and computes only what was not
reached:
- **F1 = C4 as written:** the first two of the 24 points at height 30, c = +2, at 90 and at 110 digits; every |V|
  entry within 1e-15.
- **F2, the plain variant, guarded,** at c = −2 and +2 and heights 6 and 30:
  - at each point, which sectors' couplings vanish (every weight zero);
  - the four pairs' smallest diagonal and largest off-diagonal |V|, over the points where up and down both survive;
  - the leptons' three numbers over the points where leptons and down both survive.
- **F3:** the run's verdicts for C0, X3 and X4, read off its printed output by the rules the card fixed.

**Expected [J], not blind** (the run's output has been read): F1 holds. Under the plain a0, some sector vanishes at
some point at both heights, so the plain variant is not a frame everywhere. Its mixing is reported with no expectation.

**Failure.** If F1 fails, the height-30 tables are not guarded by C4 and do not stand as computed.

0 of 19.
