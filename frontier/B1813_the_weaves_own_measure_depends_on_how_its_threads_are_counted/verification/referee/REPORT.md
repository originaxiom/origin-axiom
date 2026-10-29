# B1813 (the weave's measure and its clock) — hostile referee report (read-only, 2026-10-29)

Saved by main from the referee's hand-back. Its scripts (refcore, check1–check7) and outputs are beside this file.

**Verdict: PASS WITH CORRECTIONS.** Every number reproduces from independent code. The four required corrections are
framing, scope and Seen first.

## Verified

- **The sampling.**
  - The axis from the fixed points and the unit-speed parametrisation are correct.
  - c ≥ 1 for every positive word with both letters.
  - The reduction terminates.
  - Each thread gets mass ℓ.
  - Re-implemented two ways (an independent axis method; Series' run-segment method, to 6 × 10⁻¹⁵).
  - The move tables at n = 10 and 12 match.
  - The float sampler fails near ℓ ≈ 40 (check 7); the draft's sizes are safe.
- **The move-count limit is real (check 2).**
  - Its runs are i.i.d. Geometric(½) with their roof: P = 0.3829, 0.1676, 0.03462, 0.00754 at Y = 1.5, 2, 3, 4, and
    0.00039 at Y = 6, where the draft is 10% low.
  - Monte Carlo at n = 20, 40, 80 agrees.
  - The tail is P ≈ 3.9·4^(−Y)/√Y; the local slope falls toward 2 ln 2.
- **The measure is known.** It is Minkowski's question-mark measure (the Farey coding's maximal-entropy measure), lifted
  with the roof.
  - The mean length per move is 0.79239, twice B1663's escape rate.
  - log 2/0.7924 = 0.8748, Kinney's dimension (a pointer).
- **The trace set is complete (check 3).** An independent enumeration gives 29, 60, 96, 151. Extended to T = 50–400, it
  approaches area monotonically from below: 0.315 and 0.155 at T = 400.

## Required corrections

- **R1. Seen first omits B1663,** which found the move clock's measure (Minkowski's) and averaged one τ-function under
  it; also B852. Its sweep: 109 arcs and 5 rows.
- **R2. "P-107's non-uniqueness is this choice of clock" overclaims.** The rule is a continuum: e^(−sℓ) gives distinct
  limits (0.0346, 0.0539, 0.0859 at s = 0, 0.25, 0.5; check 6). P-107 is relocated, not settled.
- **R3. The lines tally is Burnside's lemma:** 2 per order for any family equidistributed mod N (check 4). No
  information.
- **R4.** The card named the apex rule, but the run used the arclength measure: disclose it. The headline's hierarchy
  claim is a reading, conditional on H-cov and on end data on v₊. Add labels.

## Recommended

- The tail's form, and the hierarchy exponent x^0.44 asymptotically.
- The walk identification, computed (B1662's walk and free-group words give the same; check 5).
- "Orders" rather than "weights".
- The T = 400 values.
- For the cusped surface, cite Pollicott (1986), Sarnak or Roblin (2003), not Bowen–Margulis.

## Main's verification

- The referee's checks 1, 2, 4 and 6 regenerated on main (main_rerun/).
- The s-family matches main's own stage 1c.
- All corrections applied in B1813's FINDINGS.
