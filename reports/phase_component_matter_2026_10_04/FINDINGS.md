# Matter modes in the newly admitted phase families

2026-10-04. Local branch audit/fork-2026-09-20. This report records exact
selected-point calculations in four determinant-one phase families on
marked M6. Each new family has one paired interior fundamental mode at
t=-1. No tested point has a chiral imbalance. The result repairs a gap in
coverage; it does not extend the old all-parameter negative to these families.

## Exact spectrum at the tested points

The two old permutation actions each admit two new nontrivial phase
representatives, constructed by the preceding complete multiplicative
component audit. These four families retain the old meridian and longitude
matrices. The calculations use Q(zeta3) exactly, not floating-point ranks.

For each of the four families the answer is the same:

| Parameter | Interior E modes | Interior actual dual modes | Interior Lambda2 E modes | Interior actual exterior dual modes |
| --- | ---: | ---: | ---: | ---: |
| -1 | 1 | 1 | 0 | 0 |
| 1 | 0 | 0 | 0 | 0 |
| 2 | 0 | 0 | 0 | 0 |

All twelve cases have zero global H0 in both coefficients and their duals.
At t=-1 the fundamental cohomology tuple (a0,a1,t0,t1,r1) is
(0,4,3,6,3). At t=1 and 2 it is (0,3,3,6,3). The exterior-square tuple
is (0,4,4,8,4) at all tested points. The interior count is a1-r1, not
ordinary H1 or the dimension of the coefficient fiber. Actual-dual
tuples agree at these points, so every tested difference is zero.

## Independent controls

The exterior square is built over the five-dimensional complex coefficient
space and independently checked against every two-by-two determinant minor.
It is not the exterior square of the ten-dimensional rational restriction
of scalars. The trace pairing identifies the literal flat dual, with inverse
phase and exponent, with the rational transpose-inverse representation.
In particular, complex conjugation alone is not substituted for the dual
at the nonunitary point t=2.

Every relator and both marked peripheral matrices are checked. A separate
relative-cone computation reproduces each interior count with the global
H0 correction retained. The positive parallel metric is preserved at
t=+/-1 and fails at t=2. The old zero spectrum at t=2 is recovered, and
the new phase is verified to change both actual coefficients.

The native run succeeded, 13 focused tests passed, and all 181 combined
regression tests passed. All fourteen sealed input, source, test and
dependency hashes remained unchanged. There were no failed scientific runs
or repairs in this packet. Exact outputs and command events are preserved
in RESULTS.json and EXECUTION_RECEIPTS.json, with the three execution logs.

## Meaning for the physics mission

The previously missing components do carry matter at a unitary point.
The positive is paired and the exterior sector is absent there; this is
not a complete Standard Model generation. The three-point diagnostic does
not classify all parameters, common hypercharge lines, or other components.
Nor does it by itself establish a physical spectrum on the complete end.

The diagonal adjoint transport is unchanged by the finite diagonal phases.
That makes transfer of the previously authored harmonic construction a
concrete next obligation, rather than permission to reuse its conclusion
without checking the new bundle. The immediate bounded test is whether
the actual paired mode at t=-1 can continue to first order in the known
neutral direction. A nonzero ordinary H2 obstruction could expose a
classical coupling; a relative-only obstruction would not establish that
claim. Neither answer supplies chirality or a normalized observable.

## Custody and remaining scope

Design, inputs, source, tests and hashes were committed before execution
at e315aa6e33ae5c4eec6895e4b20133ad2abba8f0. The execution tree was read-only.
No shared bank entry, architecture-wide exclusion, new source field,
vacuum choice, push or merge is made by this report. The unsealed parent
mirror-matching draft remains outside this calculation.
