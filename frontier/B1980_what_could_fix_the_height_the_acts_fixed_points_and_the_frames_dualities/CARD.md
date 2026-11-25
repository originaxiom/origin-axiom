# B1980 card — what could fix the height: the act's fixed points on the level-30 curve, and frame C's dualities

Written 2026-11-25 before any run, at the author's word: "can we for real find a principle, derived rather than
chosen, that fixes ε (equivalently, the height Im τ)? think thoroughly". Data-free. 0 of 19.

## Why

- **The record has closed every route it tried** (B1791, the magnitude ledger, B1868, B1923, P-380, P-631). Main's
  reading of why:
  - **The frame has no preferred depth.** High in the cusp the outputs are C·ε^E. A condition on the exponents alone
    cannot fix ε; something must set ε^ΔE equal to an order-one number the object supplies.
  - **The object's own geometric numbers are of order one.** The cusp shape is 3.46, the act's geodesic peaks at 1.1,
    and the level surfaces sit at 1 to 6. A depth of tens needs a large derived number, and the level is the only one in
    sight.
- **One kind of principle needs no chosen functional: a symmetry of the frame whose fixed point sets the height.** This
  is how T-duality fixes a radius. This card tests whether frame C at order 30 has one.
- **It also records the act's own fixed points on the level-30 curve,** computed exactly.

## The run

### Part A — the act on the level-30 curve (`verification/act_level30.py`; exact integer arithmetic)

- **The act's order.** M = [[2,1],[1,1]] in SL(2, ℤ/30) and in PSL(2, ℤ/30).
- **Interior fixed points.** For each k, M^k has a fixed point on X(30) = Γ(30)\H off the cusps iff some element of
  M^k Γ(30) is elliptic or ±I, that is, iff tr M^k ≡ 0 or ±1 (mod 30), or M^k ≡ ±I.
- **Cusps.** The cusps of X(30) are the vectors of order 30 in (ℤ/30)² up to sign. The run counts them, and gives the act's
  orbits on them and the cusps each power M^k fixes.

### Part B — dualities of frame C (`verification/duality.py`)

- **The outputs O(τ, p).** Nine logs: m₂/m₃ and m₁/m₃ for up, down and lepton, and |V₁₂|, |V₂₃|, |V₁₃|. They come from
  frame C, every sector reading S (B1945's `determinant_law.parts`, `cusp_mixing.U_of`), on the imaginary axis
  (Re τ = 0), which every map below carries to itself.
- **Source:** B1976's 96 points at height y.
- **Partner:** all 899 nonzero points of E[30] at the image height.
- **A duality τ ↦ −K/τ** carries iy to i K/y. It is a symmetry of the outputs if every source point has a partner point
  with the same nine outputs.
  - The distance of a source point is d(p) = min over partner points q of the largest relative difference of the nine
    logs. An exact zero matches only an exact zero.
  - **Pass:** the largest d(p) is below 1e-8 at both source heights.
- **The declared K:** 1 (the S move itself), 2, 3, 5, 6, 10, 15, 30, 60 and 900. Each is tested at source heights
  1.5√K and 2.5√K, so the partners sit at √K/1.5 and √K/2.5.
- **Controls:**
  - **C0:** source and partner at the same height (2.0), which must match at distance 0;
  - **C1:** the T move, height 2.0 at Re τ = 0 against Re τ = 1 (B1940: the frame is covariant under τ ↦ τ + 1).

## Expectations, with priors

| id | expectation | prior |
|---|---|---|
| A1 | no power M^k, 1 ≤ k < 60, has a fixed point off the cusps of X(30); M^k ≡ ±I first at k = 60 | 0.97 (computed in a sketch before this card: the traces of M^k mod 30) |
| A2 | M itself fixes no cusp; M^12 fixes some cusps | 0.85 |
| C0 | the identity control matches at every point, distance 0 | 0.99 |
| C1 | the T control matches at every point (d < 1e-8) | 0.85 |
| D1 | K = 1 (S) passes | 0.35 |
| D900 | K = 900 passes | 0.02 (high in the cusp the outputs fall exponentially on both sides, so y ↦ 900/y cannot preserve them) |
| DK | each other K passes | 0.05 each; some K other than 1 passes, 0.15 |

## What each outcome means

- **A1 and A2:** the object's act singles out only cusps on the level-30 curve. That is a derived reason the frame lives in
  the cusp, but a cusp has no depth.
- **A K other than 1 passes:** frame C has a duality beyond the moves. Its self-dual height √K is the first height
  derived from a symmetry, and it would be tested next, with no data.
- **Only K = 1 passes, or none does:** no duality of this family fixes the height. What remains is a frame-computed
  racetrack (P-629's missing effective action) or a self-consistent loop. Failing those, ε stays one counted input, and
  the scale-free test of route (d) does not need it.
- **Nothing here is compared with data.**
