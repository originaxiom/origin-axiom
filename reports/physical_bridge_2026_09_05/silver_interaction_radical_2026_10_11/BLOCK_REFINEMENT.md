# Four-plane diagnosis: post-first-run, before explicit refinement checks

At pushed 9339effac the first complete native/reference runs pass 46/23
predicates. Their original outputs are preserved as FIRST_SUCCESS logs.
Every e5-incidence hypothesis is FALSE. All four charged channels instead
vanish term by term. No physical result is recovered by the e5 hypothesis.

The native exact polynomial bases reveal a different common flag, whose
constant-envelope hashes agree with the separately reconstructed Fraction
envelopes: Q,u,e have fifth coordinate zero; d and both weak modes have no
two-form coordinate containing 4; Hu has only dual coordinates containing4.
Indices are zero-based. This motivates the following POST-FIRST-RUN
refinement. Explicit block tests and two-sided detector controls are added
to both methods and hashed/pushed BEFORE they execute. No field or boundary
is replaced, no outcome is overwritten and the original seal is retained.

## Proposed algebraic explanation to verify

Let V=span(e0,e1,e2,e3) in W, the actual proper invariant submodule of the
affine rank-five coefficient. The fifth-coordinate quotient does not split
globally: e4 is boundary-parallel but not a bulk invariant section. At the
specified cusp A and B split V plus span(e4). Charged primitives satisfy

    f_Q,f_u,f_e in V;
    f_d,f_weak in wedge2 V;
    f_Hu in ann(wedge2 V) inside (wedge2 W)*.

The same statements hold after A or B acts; the scalar charge twist
preserves every listed subspace. Explicit tests check these statements on
the ENTIRE primitive pencils, or equivalent degree-certified envelopes,
not merely at the constant term or one selected phase.

Both up terms evaluate the Hu dual on a wedge of two V vectors, hence zero.
Each down/lepton/udd term is a degree-five exterior product entirely in
the four-dimensional V, hence zero. The two Stokes terms vanish separately;
there is no fitted cancellation. The earlier repeated-family exchange
zero is also retained, not counted as a separate physical prediction.

This is an algebraic sufficient mechanism for THIS same-domain tensor.
It is NOT a global splitting of the affine bundle or a statement that all
interactions of the complete E8 parent vanish. Neutral background response,
massive-mode transfer, other admitted phases/metrics/end laws and quantum
effects were not computed. A derived upstream map must preserve the
interacting data and explain its selected domain; choosing a favorable
replacement plane would not derive that map or solve the full SM/TOE.
