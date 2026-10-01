# R71 separately sealed polynomial-generator control

October 1, 2026. First scientific seal 1aa3bd5c4eb5414ee246c5f75d6b6c7978a10108.
Original native exit1: 55/56 checks pass; only scalar/independent_scalar_charpoly
fails. Original three-file regression:21 pass,2 fail. All original files
and raw outputs remain frozen; this is a new instrument, not an overwrite.

Local primary implementation read: Sympy matrices/determinant.py _charpoly,
lines332--437, and core/symbol.py uniquely_named_symbol, lines131 onward.
The characteristic polynomial uses its own PurePoly.gen, which need not
equal the requested symbol, including a loss of the requested real
assumption. Prior: normalize the target to the ACTUAL polynomial
generator; the unchanged scalar mathematical formula should pass.
No changed lambda, threshold, count, metric, operator or eigenvalue target.

Two-sided controls: recover the old failed comparison, explicitly check
the requested versus actual generators, aligned exact polynomial equality,
an independent rational-matrix determinant fixture, and a deliberately
shifted mass that must still fail. This does not convert the original
tests into passing tests; they remain two original failures. No new
asymptotic/domain/particle theorem is asserted.

Seal this control design, producer and seven control tests; record actual
digests, commit/push/server-confirm before import/execution. Run native
control then the fixed R68/R70 plus this control file. Expected corrected
three-file result23 pass, while first21 pass/two failures stay recorded.

