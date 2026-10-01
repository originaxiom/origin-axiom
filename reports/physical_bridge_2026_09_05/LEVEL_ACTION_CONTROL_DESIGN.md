# R69 Gaussian-expression normalization control

October 1, 2026, after the first failed native and 32-test runs at
29cedea77abc07421865b5e6f84afbf570e12923. Those logs and all original
science/test files remain unchanged. The unchanged received part F
passes at its three fixed primes. No exact-index verdict is read yet.

The native run raises CoercionFailed before producing an index:
1+(-1-i)(1+i)+i is not syntactically canonical for the Gaussian-domain
converter, although it is exactly 1-i. Six tests fail at that conversion;
26 pass. This is an instrument defect, not a mathematical negative.

A separate adapter loads the frozen producer in its own module instance
and explicitly replaces its rank entry point with canonical expansion
followed by the original Gaussian/rational rank comparison. It changes
neither matrices, character exponents, cohomology definitions, periphery,
fields, controls nor the received implementation. The original producer
is not repaired on disk and its tests are not overwritten.

Opposite controls: the original converter must reject the unexpanded
known expression, the repaired exact rank must be one, and a separately
held unevaluated zero must have rank zero. These three controls augment
the original 40, for 43 fixed checks. Failure stops acceptance and is
preserved; no further silent repair is allowed.

Seal this adapter, control design and new eight-test file before import
or execution. Run its native producer, then the fixed six-file selection:
original R69 tests, new control tests, and the unchanged R58 transport
and cubic, R59 parent tensors and R68 fermion tests. Expected population
40 tests: 34 passes and the same six original R69 failure IDs, if all
repaired checks pass. Preserve all original failures as defects, not
evidence that the candidate is physically or mathematically excluded.

The original scope, hypotheses and forbidden physics promotions stand.
An exact finite coefficient index does not determine the interacting
fermion domain or the physical interpretation of that index.
