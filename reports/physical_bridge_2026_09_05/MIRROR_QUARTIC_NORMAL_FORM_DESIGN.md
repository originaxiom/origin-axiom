# R34 rational normal-form control — separately sealed before execution

2026-09-19. Original seal 77fdcc15c3fdbe9962d7d970b780f6d8ea9e5dfd
and all its files remain unchanged. Native nine groups pass; the new
test file returns 16 pass / 1 fail, and the fixed seven-file run
126 pass / 3 fail: the new failure plus R33's two retained comparisons.
The new failing ID is test_mirror_only_limit_and_breaking_requires_locking.
The original numerator expanded a rational expression without cancelling
its common determinant. Structural == then differs from rational equality.

This proposed diagnosis is not accepted on inspection alone. Check the
mirror-only and full ten-channel numerators with cancel(together(lhs-rhs));
check kappa=0 and Phi=0 limits, and reject a deliberately missing
number-changing coefficient. A simple known rational identity and a
one-unit error test the diagnostic itself. Inputs must be exact.

Cancellation is algebraic on D != 0, not permission to integrate out a
massless or unstable field. An independent exact numerical domain helper
requires r>2 abs(kappa Phi), tests three stable inputs, and rejects a pole,
an indefinite Hessian and a negative-definite Hessian (D>0 alone fails).

Declared prior: all exact residuals zero and all negative controls reject.
No new physical prediction, quantum gap or universal claim. Seal these
three files, commit, push and remote-confirm before native and nine-test
execution. Then run the original seven full files PLUS this new test file;
do not deselect any original failure. Preserve every first output.
This repeated expression-normalization error is an instrument-design
failure, not something to hide by calling the entire suite green.
