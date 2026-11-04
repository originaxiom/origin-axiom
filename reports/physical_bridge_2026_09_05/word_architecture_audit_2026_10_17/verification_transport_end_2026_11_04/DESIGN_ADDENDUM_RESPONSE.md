# Prospective response-control addendum

November 4, 2026. After proof/design commit `329a910e9`, before any implementation of this package. The original design and source inventory remain preserved. The new analytical successor is `GAPLESS_CUSP_RESPONSE_AND_GAUGE_COUPLING.md`.

Extend the eighth intended method, `test_actual_centralizer_mass_and_escaping_channel`, with the following finite controls. The package still has exactly the original eight method names.

1. From the actual projected mass matrix, double the operator and verify its constant Hermitian radial symbol, square and signed multiplicities. A finite symbol check supports the unitary normal form but cannot establish its global domain.
2. Check the complex spectral solution of `D0=-i sigma1 partial_t`, with independent real lambda and positive epsilon and `z=lambda+i epsilon`. Verify the differential residual, actual Gamma0/Gamma1 trace, the exterior L2 integral and its divided-imaginary-part identity. A changed sign of the exponential must fail the decaying condition. A false zero norm from `M'(z)=0` must be rejected.
3. Reuse the original positive source kinetic density to obtain the gauge vertex for a normalized profile. Compare a translated profile in the canonical dt measure with its gauge-zero-mode overlap and include a generator acting nontrivially on the centralizer coefficient. This checks the source overlap identity and does not certify the full interacting continuum spectrum or a phenomenological exclusion.

The same independent review, full source closure, exact main acceptance and prospective admission apply. No scientific source was imported, collected or run to write this addendum.
