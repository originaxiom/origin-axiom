# Tail integral detector correction

The first sealed run failed at tail_volume_bound. Its empty stdout and 546-byte path-bearing stderr are retained unchanged; FIRST_FAILURE.json records their hashes and exit1. The original verify.py remains frozen. No complete result is inferred from the absence of an earlier assertion.

A separate diagnostic of the failing expression returned

    Piecewise((A0*ell*exp(-2*R/ell)/2, R > 0),
              (Integral(A0*exp(-2*r/ell), (r,R,oo)), True)).

R was declared nonnegative. The CAS leaves its otherwise branch unevaluated, although explicit substitution R=0 yields A0*ell/2 and positive R gives the stated formula. Subtracting the correct expression therefore does not simplify to the literal zero the old checker expected. This is a detector defect, not evidence against the tail integral or the admission proof.

The new verify_v2.py certifies the same all-R integral by its derivative and zero limit at infinity. It separately verifies the R=0 integral and rejects a wrong prefactor. The proof, model, word bound, candidate, remaining tests and analytic acceptance conditions are unchanged. This is a disclosed post-failure detector change with two added opposing/endpoint safeguards. Hash and push the new instrument and this correction before the second run; retain the first record permanently.
