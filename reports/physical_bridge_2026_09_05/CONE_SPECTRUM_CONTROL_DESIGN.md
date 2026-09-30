# Polynomial generator identity repair

September 30, 2026. R63 separately sealed instrument repair. Preserve
the original four scientific files at seal a7b9167149cb69db12411fd99a76016921dc47e3.
The original native run passes 68 of 69 checks; the fixed 28-test run
has 26 passes and two failures, both due to the polynomial comparison.
Their raw logs, commands and exits remain unchanged.

## Diagnosis and unchanged mathematical target

The native polynomial is (lambda-t^2-t)^2(lambda-t^2+t)^2, the expected
((t^2-lambda)^2-t^2)^2. However, the requested t has real=True and the
polynomial engine returns a generator without that assumption. These
same-printed symbols are unequal. A separately captured identity-matrix
diagnostic reproduces the false comparison and verifies equality when
the returned generator is used. It tests the instrument, not the cone.

The old wrong-density-shift check also compared mismatched generators
and must be recomputed, not merely counted as an unaffected pass.
No operator entry, metric, eigenvalue, threshold, physical hypothesis or
scientific criterion changes. Neither original test is deleted, rebound
or made to pass. No change to the other 67 native criteria is proposed.

## Correction and two sided acceptance

A new producer imports the original unchanged source and preserves its
full failed check dictionary. Recompute the characteristic polynomial
using its returned generator throughout and compare polynomial
coefficients. Require equality with the original polynomial object,
the same generic expected formula, rejection of the wrong density
shift and of a deliberately changed coefficient, and reproduction of
both outcomes in the identity-matrix diagnostic.

The effective dictionary has the original 69 entries with these TWO
comparisons explicitly recomputed, plus four instrument safeguards.
It must pass 73 of 73. Six repair checks (two replacements and four
safeguards) are separately visible. Four new tests must pass. Rerun
the original 28 tests unchanged together with the four new tests:
the expected disposition is 30 passes and the same two original failed
IDs. Do not report that fixed combined population as green.

Seal this design, new producer and tests, commit/push and confirm the
remote before execution. First-run failures stay preserved. This
repairs comparison mechanics, not a complete physical end law or a
nonlinear/global mode admission argument.
