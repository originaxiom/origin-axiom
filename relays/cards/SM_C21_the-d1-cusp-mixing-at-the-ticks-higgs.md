# SM-C21 — frame D1's cusp mixing with the tick-fixed Higgs vacuum: aligned or not?

*Card of the SM seat, 2026-11-18, on the author's "go". Committed and pushed before any computation. Data-free:
**no singular value and no mixing modulus is set beside a measured number.** The structure classes and the exponents
below are frame-internal. Main's closed form (`checks/cim_closed.py`) and its gate-5 construction
(`checks/agy002_g5.py`) are imported unchanged.*

## 0. Why

- B1945 found the cusp exponents rational. They are candidates for P-862's parameter-free relations.
- Main rejected reading frame C by them because its cusp mixing is a permutation. B1946 traced that permutation to
  frame C's free choice of Higgs reading.
- Frame D1 has no reading to choose. SM-C18 to SM-C20 showed that its one Higgs bit, the ±π/6 transport pair v±, is the
  tick's orientation.
- Main's gate-5 check tried D1 with a single Higgs mode (a permutation) and with the six modes at the origin (rank one).
  **It never tried the tick-fixed ground states v±.** This card does.

## 1. The construction, inherited, with nothing chosen here

- **The coupling:** a sector's Yukawa matrix is M_s = Σ_k Y_ijk(ξ_s)·v_k, with ξ_s = Δ_s·w/2 and Δ = q_L − q_R = +5
  (up), −1 (down) and −9 (leptons). One Higgs vector v serves every sector, with no conjugation. This is main's
  agy002_g5.py convention, taken as it stands.
- **The Higgs vector:** v₊ or v₋, the unit eigenvectors of main's U_M (level6_higgs.py) with eigenphases ±π/6. Both
  are run, since the sign is not decided.
- **The points:** the 24 points of order 5, at each of the 4 lifts (SM-C18: the coupling is lift-dependent for odd Δ).
- **The heights:** τ = 0.13 + 4i and 0.13 + 8i, with main's Y_mp at extended precision where double precision fails.
  The exponents come from heights 6, 8 and 10.
- **The mixing:** |V| = |U_upᴴ U_down|, from the left singular bases. The classes:
  - **aligned:** |V₃₃| > 0.99 and every diagonal entry > 0.9;
  - **top-aligned:** |V₃₃| > 0.99 only;
  - **permutation:** every row has one entry > 0.99;
  - **other.**

  The top direction is the largest singular value's.

## 2. What is computed

- **K1:** the class counts per Higgs vector, lift and height.
- **K2:** each matrix's rank, with singular values below 1e-12 of the largest treated as zero. A rank-one matrix has no
  mixing beyond the top direction, and is reported as such.
- **K3:** the exponents E = −(1/π)·d log(s_i/s₁)/d Im τ at the mark (2/5, 4/5) for up, down and leptons, from heights
  6 to 10, at both v±. Whether they are close to rationals with denominator ≤ 10 (within 1e-3).
- **K4:** whether lepton ≠ down in the exponents (Δ = −9 against −1).

## 3. Expectations, written before any computation

| | expectation | prior |
|---|---|---|
| K1 | aligned or top-aligned at a majority of points for at least one of v± at height 8 | 35% |
| K1′ | the class depends on the lift at some points (odd Δ) | 70% |
| K2 | full rank 3 for both v± (v± are not the origin's evaluation vector) | 70% |
| K3 | the exponents are rational with denominators ≤ 10, and the same for v₊ and v₋ | 50% |
| K4 | the lepton exponents differ from the down ones | 70% |

## 4. The kill lines

- **If no point is aligned or top-aligned for either v±, at any lift, at height 8:** D1 fails on structure at the cusp
  with its tick-fixed Higgs, and the cusp-exponent route is closed in D1 as well as in frame C.
- **If the mixing is aligned at the cusp and the exponents are rational:** the exponent relations become candidates
  for P-862. Each would still need sealing as a prediction, with main's rule and the author's word before any look.
  None is set beside data here.

## 5. Files

relays/sm_c21/, with its script, output and run. The page will be relays/SM_C21_THE_D1_CUSP_MIXING.md.
