# B1436 — THE FIRST BIRKHOFF COEFFICIENT: the object's monodromy trace map has a = 16√−3/63 at its fixed character, derived here

cc, 2026-10-01. A web research seat reported this number in its September checkpoints; the audit lane received it
unverified (its intake of 2026-09-26: "deferred … absent a faithful same-action map"); main registered it as lead
L230 (a). Derived here **from scratch, with code written on this bench and no computer algebra system**.
**Verdict: PROVED.**

## The statement

The monodromy of m004 acts on the character variety of its fibre by the trace map

    F(X, Y, Z) = (Z, YZ − X, Z(YZ − X) − Y),

which preserves κ = X² + Y² + Z² − XYZ − 2 and, on each leaf, the area form Ω = dX ∧ dY / (2Z − XY). On the object's
own leaf κ = −2 it fixes the two conjugate characters ((3 ± √−3)/2, (3 ∓ √−3)/2, (3 ± √−3)/2), with multipliers
λ^{±1}, λ = (5 + √21)/2 (banked: B520, B581, B622). Near a hyperbolic fixed point an area-preserving map is
conjugate to

    (q, p) ↦ (q·L(qp), p / L(qp)),    L(s) = λ(1 + a·s + …),    dq ∧ dp = Ω.

**a = 16√−3/63 at the first fixed character and −16√−3/63 at its conjugate.** It is the first datum of the object's
own dynamics beyond the linear one. Main had the multipliers and no cubic term.

## Why no Darboux chart is needed

In linear eigen-coordinates the quadratic terms are removed by a unique near-identity change, because no quadratic
monomial is resonant. The coefficient of x²y in the first component is then unchanged by any cubic change, because
x²y is resonant. So it depends on the coordinates only through the linear frame, and on the frame only through
dx ∧ dy at the fixed point. With the frame normalised to Ω(e₊, e₋) = 1, a is that coefficient divided by λ.

## Computed (`verification/birkhoff.py`, record `birkhoff.json`, `birkhoff_run.txt`; under a second)

Exact arithmetic in ℚ(√−3, √21) on rational 4-tuples; truncated bivariate polynomials; the leaf as an implicit
series, asserted to solve the leaf equation to the truncation degree.

| check | result |
|---|---|
| chart (X, Y), Z implicit | a = 16√−3/63 |
| chart (X, Z), Y implicit, Ω = −dX ∧ dZ / κ_Y | the same |
| the conjugate fixed character | −a |
| F ∘ F, multiplier λ² | 2a |
| Ω → (7/3)Ω | a / (7/3) |
| a linear map with the same multipliers | 0 |
| **bite:** the leaf's curvature dropped (Z linear in the chart) | −11/18 + (55/54)√−3 + (1/42)√21 − (5/126)√−3√21 ≠ a |

Asserted inside: det DF = 1 and tr DF = 5 at the fixed point; the eigenvectors; the quadratic terms vanish after the
change.

## What it is, and the fence

- **A number of the object, with one normalisation.** a scales as 1/c under Ω → cΩ, so the invariant content is
  a·Ω, not a number: any other normalisation of the leaf's area form rescales a by the same constant. The sign
  is the choice of fixed character; the two are exchanged by complex conjugation.
- **Purely imaginary on a complex leaf.** The fixed characters are not real, so this is not the twist of a real
  area-preserving map, and no stability statement follows.
- **Not a coupling.** Nothing here inserts the number into an action. The audit lane's fence stands: no physical
  use absent a same-action map.
- **The fixed character is isolated on the leaf:** det(DF − 1) = det DF − tr DF + 1 = 1 − 5 + 1 = −3 ≠ 0.

## Not verified here

The web seat's real four-dimensional realisation (its H = log λ·U − γUV), its balanced-representation transfer
negative, and its magnitude-only readout. Read, not re-derived.

## Registered

L230 (a) is closed by this arc. Higher coefficients (the next is the coefficient of s² in log L) are not computed.
