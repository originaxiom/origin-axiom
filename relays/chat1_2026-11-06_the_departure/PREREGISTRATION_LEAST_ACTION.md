# THE LEAST-ACTION DEPARTURE — pre-registration (the web seat, 2026-11-06)

**For:** the owner's goal, narrowed by the owner to τ and the line (the scale part dropped; A12 stays open), and the
named choices left in relays/CHAT1_TO_CC_2026-11-06_THE_DEPARTURE_THE_LINE_CANNOT_SEE.md § 6:
- "isolated departures, each invisible to the line by itself, and minimal";
- "one departure", as main framed it in P-717.

**Kind:** data-free. SL(2, ℤ) arithmetic mod 5 and geodesic lengths only: no frame value, no data, no held-out
quantity.
**Written before** `least_action_check.py` is run.

## The principle stated

**(A) The history departs from its golden ground path along the least-action route its own line cannot see.**
- The action of a geodesic history is its hyperbolic length. The cost of a finite defect is its excess length over
  the golden path it modifies.
- A defect is any finite modification of the golden run sequence ⋯1, 1, 1⋯ that replaces m consecutive golden runs by
  m runs (r₁, …, r_m), not all 1.
  - It starts with an L-run at a period boundary. The R-start cases are the mirror, by P-336's covariance.
- **Excess length:** ΔS = lim_k [ℓ(D_S X (LR)^k) − ℓ(D_g X (LR)^k)].
  - D_S and D_g are the matrices of the defect's and the golden m runs.
  - X = R if m is odd and X = I if m is even, so that the closed word stays alternating.
  - ℓ = 2 arccosh(tr/2).
  - For one run of n this is 2 log((n − 1 + √5)/√5) (departure_check.py, part F).
- **The line is not changed by the defect** (L), when E = D_S D_g⁻¹ fixes each line of the golden pair up to sign
  (own(LR), in the period-boundary marking). This is the condition under which the history returns to the golden lift
  it left, in the line's own curve.

## The hypothesis, before computing

**H:** among all defects with m ≤ 6 runs and every run ≤ 6, and m = 7 or 8 runs with every run ≤ 3, the line-invisible
defect of least excess length is the single run of 6, (6) with m = 1: ΔS = 2 log(1 + √5) = 2.348718…
- It is unique up to the defects equivalent to it. (An equivalent defect is (6, 1, …) padded with golden runs, which is
  excluded by requiring the first and last runs to be ≥ 2.)

**Why it is expected:** ΔS of one run is concave (logarithmic) in n. So five extra letters packed into one run cost
less than spread over several.

**Refuted by** any line-invisible defect in the range with ΔS ≤ 2.348718 other than (6).

## What follows either way

- **If H holds,** (A) replaces "one departure" and "minimal" by a single principle, least action under (L).
  - The apex read-out follows if the frame is read at one point fixed by the history alone (A11's one address). The
    history's only symmetry, the palindrome's reflection, fixes exactly that point (Curie).
  - Left would be the bit, a nonzero line, and the premise that the history departs at all.
- **If H fails,** the cheaper defect is reported, and "one departure" stays a choice.

The check also reports, for each defect class met, its highest apex (continued fractions on the closed approximant at
k = 20). That is reported only, not used as a criterion.

0 of 19.
