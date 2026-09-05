# R6 post-result derivative and verifier controls

BANKED IDENTITY: R6's first output is successful, with full kernel-force,
stationarity, SM-action and weak-coupling checks. Its design/code/tests were
sealed in 44a52ec4. The reference scalar displacement is 14.9%, not assumed
small. R5's positive angular result is protected by numerical regression.

PRIOR ART: R6's staged governance run newly flags the vector/Weyl derivative
test as NO-ASSERT. Inspection of `scripts/checks/check_test_vacuity.py` shows
that it recognizes Python assert nodes and six pytest-style method names,
but not `np.testing.assert_allclose`. This is a static-screen verdict, not
yet a demonstrated unconditionally passing test. The original test and
checker are not edited or exempted. The failure remains visible.

P0: verify the R6 derivative test's ability to fail, and independently
contract its full gradient and solve its SM-singlet normal equation. This
is a post-result instrument check, not blind evidence for the known result.
No measured input or additional physical action is involved.

Before execution, seal the new test file. It must (1) execute the original
derivative test successfully, then require AssertionError after an additive
perturbation breaks linearity of the vector orbit; (2) do the same for the
Weyl mass map; (3) contract explicit full scalar Hessian derivatives with
the matrix-function derivative in every one of 186 directions and compare
with the independently rearranged R6 gradient formula; (4) solve the reduced
13-dimensional SM-singlet equation, verify nine positive modes, and recover
the full-space normal displacement. These controls can fail. The direct
gradient check reuses the quadratic-constraint primitives but not the fast
gradient contraction; it is not a wholly independent action derivation.

Prior: the static gate is missing a legitimate assertion vocabulary. If
either mutation is not detected, record an actual test defect and diagnose
it without changing an old sealed file. No gate is weakened here.
