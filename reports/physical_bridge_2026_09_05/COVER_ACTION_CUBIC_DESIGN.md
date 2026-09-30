# Nonzero cubic control for the finite cover action test

September 30, 2026. Separately sealed R58 follow-on, before its execution.
The first 28 controls and 23 tests passed, but author review found a
non-discriminating cubic fixture: each original rank-two A and B is
traceless, so tr(A B A)=tr(A^2 B)=0. The general block-algebra proof is
not affected, but that channel alone does not guard a nonzero cubic.
The original producer, tests and outputs must remain unchanged.

Use three sheets and H=diag(1,-1), E=E_01, F=E_10. Let A_i=(i+1)H,
B_i=E, C_i=F. The predicted sum tr(A_i[B_i,C_i]) is 12. Direct image
retains 12; merging the sheet fields before forming the bracket gives
108 and must be detected as a different operation. Antisymmetrizing
the three matrix coefficients in the form wedge product gives three
times the bracket trace, predicted 36, a nonzero cubic-form control.

Check the old zero explicitly, the nonzero sheet sum, faithful transport,
wrong-merge opposite, and nonzero antisymmetrized wedge coefficient.
The numbers are comparator values, not couplings or measurements.
No new physical action, manifold, generation, normalization or boundary
claim is permitted. This supplements the first controls, not their logs.

Seal this design, producer and two tests; push/server-confirm before
importing the new producer. Run it and the fixed previous three test
files plus its new file. Freeze HEAD/tree during both runs. The inherited
cover_action.py remains at 3adce05c and is imported only for the old
fixture/equality helpers; the new H,E,F tensor is constructed separately.
Report failed outputs if any, with no after-the-fact criterion repair.
