# P-C3 exact algebra and normalization controls

2026-11-16. Expectations recorded before writing the checker. This extends
the committed P-C3 hand derivation at 924f679b2 into a reviewable verification
package. Scientific implementation is being prepared for the independent
proof/code review and separate execution admission required by P-C3's card
and the physical harmonic-transport acceptance. Execution is unreleased.

## Question and deliverable

Check the finite algebra behind the residual section action, constant
interaction-lift classification, cubic vertex, canonical current and
second-order complementary mass response. Start from the displayed parent
action, kinetic weights and literal root matrices. Use exact arithmetic.
Every test must name the finite claim it actually checks.

The checker is separately written from the producer calculations, by the
author of the new proofs. Its output will therefore be an author check.
Independent proof/code review and independent recomputation are distinct
evidence duties. No held-out data or observed parameter is loaded.

## Fixed check population

The twelve methods in EXPECTED.json cover the following claims.

1. Quaternion relations and conjugation on a basis. Include noncommuting
   quaternion generators and an axis quarter-turn. Compare unsigned
   permutation and signed axis actions on their stated monomial family.
2. Rank of the actual bilinear contraction's image span, including all
   traceless S basis inputs paired independently with rank-one M units.
3. Full coupling covariance on basis inputs, plus the explicit traceless
   rejecting witness for unsigned matter transport.
4. Residual inner action after deck cancellation on all eight quaternion
   elements. Carry the declared epsilon and vertical-spin factors.
5. Constant left/right stabilizer equations for the full matrix family
   and the five-slot family. Linearize only by replacing the inverse
   right action with a new unknown matrix. This is an exact equivalent
   linear system, with invertibility imposed in the accompanying proof.
6. Expand the antisymmetric source superpotential and independently
   extract its polarized cubic coefficient on noncommuting fields.
7. Compute the literal SU5 root bracket, projected cubic and variation
   of the displayed physical mass-operator row with its target density.
8. Compute the normalized coupling and gauge current from raw action
   coefficients. Check their ratio and simultaneous action, trace,
   mode-frame and scale changes.
9. Integrate a flat positive metric and a smooth nonconstant periodic
   positive metric exactly. Check equality and strict inequality in
   the normalization formula on these algebraic controls.
10. Test the polynomial slot zero, generic leading rank two and the
    effect of adding an illicit form-form entry.
11. Eliminate an actual noncommuting light/heavy block exactly. Retain
    the explicit second-order background term and both reconstructed
    norms. Compare the leading small singular value with the independently
    computed characteristic polynomial.
12. Check the complex-bilinear Gram conversion with a genuinely complex
    positive Hermitian square root. Derive the current by expanding the
    same kinetic term, and retain its norm under a nonorthogonal frame.

## Deliberate defects

The source must contain explicit rejecting comparisons for an incorrect
quaternion sign, unsigned interaction transport, an omitted deck factor,
an omitted vertical-spin factor, a nonscalar stabilizer, a cubic factor
or sign error, an omitted target density, a doubled connection metric,
an unnormalized current, frozen mode-frame factors, an illicit slot
entry, omitted heavy response, omitted second-order background response,
a Hermitian transpose substituted into a complex bilinear and an
untransported current metric. The checks must compute the discrepancy.
A boolean naming an error without evaluating that error is insufficient.

## Scope and failure handling

The finite controls depend on the declared action and backgrounds. They
cannot establish the full physical mode/domain theorem, a global
register-to-field map, a physical three-family spectrum, an actual
nonzero higher-order coefficient in the curved model or an input reduction.
The periodic metric controls make no claim to solve the curved stationary
background equations. The five-slot span remains an unearned physical
premise even if its algebraic stabilizer is checked.

The exact test population, dependencies, all proof inputs and the runner
will be hash-pinned before a scientific import or collection. Reuse the
existing prospective admission runner. Add isolated-runtime and full
untracked/ignored-file checks requested in main's M5. Execute only in a
clean isolated checkout after the required review and admission, preserve
the first failure, use fail-fast and retain the exact output. No previously
refused physical packet is executed by this package.

Completion of this preparation means a source-complete sealed package and
a relay identifying the review duties. A successful future finite run will
add bounded computational evidence to these claims. The active physical
goal continues through the actual field/domain and interaction map.
