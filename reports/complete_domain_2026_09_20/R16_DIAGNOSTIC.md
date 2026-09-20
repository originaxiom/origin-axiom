# Post-failure diagnostic, not a replacement for the failed old test

The unchanged selected antecedent run returned 23 passed and one failure in
24.74 s, exit 1. R16's `test_nonzero_green_form_and_distinct_complex_domains`
passed its Green-pair and cutoff-domain assertions, then failed to simplify
`capacity_energy_identity` to zero. Its expression still contained SymPy
`Integral` and `Piecewise` objects. No scientific file was changed during
that run. The test and producer remain unchanged afterward as well.

This diagnostic is deliberately **post-failure**, not a preregistered success
of that old code. Before running the diagnostic, record the independent
analytic expectation. For L>0 and 0<epsilon<R set

    I=(epsilon^(-2L)-R^(-2L))/(2L),
    w=r^(2L+1), chi'=1/(w I).

The proposed energy primitive is -r^(-2L)/(2L I^2); the normalization
primitive is -r^(-2L)/(2L I). Their derivatives should equal w chi'^2
and chi', and their endpoint differences should be 1/I and 1 respectively.
The Cauchy--Schwarz lower bound for integral w chi'^2 with integral chi'=1
is 1/I; this profile attains it. This does not rely on definite integration
software. A half-sized energy primitive must fail the derivative identity.

`r16_capacity_diagnostic.py` checks precisely these facts and a single exact
rational substitution. It uses no fitted constants or broader scan. Its
source and this note are committed before first diagnostic execution. The
original failed result must remain visible regardless of the diagnostic's
outcome. This check can establish the identity despite a symbolic integration
failure; it cannot retroactively make the old test pass.
