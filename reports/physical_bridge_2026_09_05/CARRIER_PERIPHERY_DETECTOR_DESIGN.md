# R79 supplementary integration calibration, before execution

October 2, 2026. Post-science metadata correction, not a repair of the
five original frozen scientific paths. The first governance receipt
reports eight new NO-ASSERT findings for the eight unittest tests, plus
two old tests. Inspection shows the detector only recognizes Python
assert statements and selected pytest-style calls. A real unittest
assertion is currently invisible to it. Preserve that first output.

Scope: extend the existing AST detector to lower four standard methods
(assertTrue, assertFalse, assertEqual, assertNotEqual) to their equivalent
assert-expression nodes, only on self in a directly declared
unittest.TestCase subclass with the standard unittest import and without
overriding one of those methods. Unsupported/dummy/override cases stay
NO-ASSERT. Literal and syntactically tautological method assertions
must remain subject to the existing tautology/review tests. No baseline,
waiver, gated population, result file or original science is changed.
This is a static syntax aid, not an oracle that arbitrary tests are sound.

Preregistered acceptance: real dynamic unittest methods are detected,
their deliberately corrupted execution fails in unittest; constant-True
and equal-expression cases lower to tautologies; non-TestCase and
overridden methods remain undetected and flagged; all eight original
R79 tests retain their unchanged bytes and pass. After staging the fix,
the new eight NO-ASSERT offenders must disappear without deleting tests
or weakening the two old findings. Preserve any contrary result; repair
and seal again before rerun. Focused suite is five detector calibrations
plus the unchanged29 R57/R78/R79 tests. Full-suite debt remains.

Seal/push/server-confirm this design, changed detector and new calibration
tests before execution/import. All initial scientific receipts remain
historical and unchanged; independent analytic physics review is not
supplied by this integration fix. Return to source/end/action admission.
