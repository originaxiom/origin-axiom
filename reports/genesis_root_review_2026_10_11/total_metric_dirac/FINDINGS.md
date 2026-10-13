# The total metric fixes a mixed spin connection term

October13, 2026. Lifecycle: mechanism. Uses: the existing physical total-space metric, nodal_transport, fibre_family and cusp_spin_extension. This is a conditional differential expression, not a global physical mode count.

For the supplied semi-flat metric, the full ordinary spin Dirac operator in the declared frame is

    D=c1 (y/ell) partial_x+c2 (y/ell) partial_y
      +c3 sqrt(y/A) partial_u
      +c4 (A y)^(-1/2)(partial_v-x partial_u)
      -c2/(2ell)+c1 c3 c4/(4ell).

The radial density term and the mixed spin term are both fixed by the metric. Transforming unitarily to t=log y and Lebesgue density removes the first, not the second. The remaining growing and shrinking derivative coefficients retain the actual fibre degeneration. The old reference flat-link Fourier bound cannot be substituted for this operator.

The mixed term is a geometric connection contribution, not a newly adjustable mass, Higgs field or cusp unit. It does not by itself prove fibre-mode mixing, confinement, a spectral gap or chirality. Its significance is that the actual domain and harmonic projection must be tested using this expression, rather than an assumed direct product.

## Exact verification

Seal41d87b89d6e039f40081e6eb47f4fc04669d82a6 was pushed and server confirmed before the first scientific execution. All343 exact predicates and six tests pass on that first run. Native execution took3.903086 seconds; pytest reports3.43 seconds, with4.036089 seconds for its captured process. Both stderrs are empty, and all six sealed source hashes are unchanged.

The checks include every coordinate-to-frame connection entry, torsion, metric and Clifford compatibility, chirality, formal adjoint, cusp deck covariance and the radial unitary map. All15 differential coefficients in the squared-operator identity agree both with and without the symbolic cusp-line twist. The scalar curvature is independently reconstructed as -3/ell^2. Controls reject omitting or reversing the mixed term and omitting the density term. A flat constant metric gives zero connection and curvature. These are two computational routes by one author, not an independent external review.

For the supplied commuting line connection -6i n dx/y, the extra Dirac term is -6i n c1/ell and its squared curvature term is -6i n c1 c2/ell^2, for symbolic real n. This verifies the geometry of that optional coupling; it neither quantizes n nor requires n nonzero.

## Progress and remaining obligations

The local Levi-Civita contribution no longer needs to be guessed or supplied independently once this metric is chosen. The next total-space comparison has an explicit, checked differential expression. However, a differential expression alone is not a closed operator. The finite-distance marked section, degenerating modular cusp, actual rank-six transitions, spin extension and graded trace subbundle must enter a single domain analysis. Smooth-fibre transport is only locally uniform away from degeneration, and local nodal acyclicity is not a full spectral certificate.

Next construct the simultaneous graph-domain problem using this expression and the existing critical puncture trace. Determine the induced operator on vertical harmonic profiles together with coupling to the complement and the required uniform estimates. Do not simply discard that complement. In parallel conceptual work, the same-field physical parent and a generated end/source law must be identified; mathematical spinors have not yet been mapped to the physical Weyl fields by this calculation.

The new physical branch830b92ad2 reports exact charged-cohomology and holomorphic-cubic preservation in its compact silver theory. Its complete proof and next-test statement were read here, not reproduced. That positive strengthens its conditional physical realization; it does not identify its action/domain with the different elliptic-family operator. No family-count scan of that exact line is proposed.

The full goal remains active and unachieved. No physical parameter, gravitational law, selected cusp sector, complete spectrum, new shared B-number, canonical genesis promotion or full-suite green certificate is claimed.
