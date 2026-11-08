# Verification design for the same-action gauge response

BANKED IDENTITY: Verify exact finite consequences of the already hand-
derived scalar/vector cusp responses, induced norms, same-action sewing
and cubic form factors. No SM value or desired chiral count is targeted.

PRIOR ART: The parent, stationary gauge centralizer, general transmission,
Schur law, response/norm principle and gauge interaction are inherited
from the sources named in SAME_ACTION_GAUGE_BOUNDARY_RESPONSE_AND_CUBIC_
2026_11_08.md. Predictions in that report precede this source
implementation but are already known; this is verification, not blind
discovery or a retroactive preregistration.

This design is written before implementing the new producer/checks.
The two older seven-control architecture sources at 7e0159033 and every
other frozen scientific package remain unchanged.

## Inputs and independent checks

Use Python standard-library Fraction/integer arithmetic only. Parameterize
the Euclidean examples by rational nu>=1 and positive rational ell^2,Y,
with s=(nu^2-1)/(4ell^2). This avoids numerical square roots without
restricting the analytical theorem to the finite examples.

A small producer will declare the candidate exponents and responses.
A separate unittest source will independently evaluate weighted Euler
residuals, convergent power integrals, divided differences, shell matrices,
and a real integer SO3 bracket trace. It will not import saved science
results or use producer success booleans as proof. Source metadata and
hashes may be inspected without importing the science.

Exactly six scientific methods are intended:

1. **Actual weights and boundary variation.** Reconstruct scalar/vector
   Euler equations and outward fluxes from their distinct kinetic weights.
   Retain the scalar moment source by a noncommuting rank-one matrix
   example. Wrong scalar/vector weight and reversed outward sign reject.
2. **Poisson branches and normalizability.** Check both equations for a
   finite rational grid and the admitted/rejected powers in their actual
   norms, including s=0. The constant vector must survive; the constant
   connection scalar must fail. A flat-norm substitution rejects.
3. **Response derivatives and norms.** Integrate the profiles independently
   and compare with derivatives and two-parameter Green divided differences.
   Wrong conformal weight, denominator and zero-response/zero-norm inference
   must fail on explicit examples.
4. **Same-action sewing.** Construct the static shell response and compute
   its actual two-by-two Schur complement, recovering the shorter tail.
   Check both Riccati identities on the rational grid. Dropping the tail
   or using the wrong normal sign must disagree.
5. **Cubic interaction.** Independently integrate the three Poisson powers
   with the correct scalar/vector weights and verify both form factors.
   Retain a nonzero colour SO3 triple-bracket trace. Check the low-momentum
   equality with the same kinetic weights; an Abelianized or unweighted
   substitute rejects. These finite powers do not certify the entire
   nonlinear gauge-invariant boundary action.
6. **Curvature and sector scope.** Check the static 1/y profile, its finite
   norms, curvature, finite-cut flux and vanishing remote perturbation.
   The constant flat comparator has infinite connection norm. Check the
   differentiated holonomy identity at first order, including its sign,
   without identifying E8 transport with the abstract flavour trace.

## Stop rules and execution status

No new science import, collection or execution is allowed merely by this
design or source implementation. A complete runtime/source/gate/custody
specification, independent nonauthoring review, main's exact acceptance
and strict clean-checkout admission are still required. No ADMISSION is
to be fabricated. Finite examples cannot prove the global nonlinear
exterior problem, core matching, all-word register map or chirality.

Preserve every first failure before repairs and successor seals. Do not
silently weaken the wrong-weight, missing-source or wrong-normal controls
to obtain a pass. The full parent and other source sectors stay in the
physical account even though this packet checks one declared channel.
