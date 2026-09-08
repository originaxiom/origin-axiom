# R21 action-level control, separately sealed after the original success

2026-09-08. This adds tests; it does not replace the successful R21
source or alter its assertions. Original seal 6a08d343 is unchanged.

BANKED IDENTITY: R21's actual weight-pulled H representation and its
anomaly factorization, computed in anomaly_completion.py. Reuse the
full polynomial and scalar charge, not just the displayed mass formula.
R19/R20 supply the unchanged source and character conditions.

PRIOR ART: the same convention/source basis as the original R21
design, including the local descent of the anomaly polynomial and
the global bundle caveat. Pantev--Wijnholt section 3.4,
https://arxiv.org/pdf/0905.1968, does not derive these new fields on
our geometry. This is a direct symbolic action test, not new empirical
input or a claim to reproduce a geometric anomaly-inflow action.

Scope: R21's declared four-dimensional H effective action, ordinary
spin spacetime, charge-four complex scalar and added V/N fields.
PB-BOUNDARY remains the parent open duty. Positive prior for all
gauge/mass identities; wrong charges and a missing counterterm must
fail. These tests can verify an action with specified coefficients,
not select those coefficients, Higgs profile or scales physically.

1. Derive |D Phi|^2 from Cartesian real fields with D=d-i*q*A, then
   substitute Phi=(f+rho)*exp(i theta)/sqrt(2). Require the complete
   expression (d rho)^2/2+(f+rho)^2*(d theta-q*A)^2/2.
   Verify finite local gauge covariance algebraically, including
   d epsilon and the derivative of the phase. A derivative lacking
   its connection term must fail.
2. Differentiate that derived kinetic expression at rho=0,theta=0
   after A=g*A_can to obtain m_A^2=16*g^2*f^2 at q=4. Differentiate
   the quartic to obtain m_rho^2=2*lambda*f^2 and its zero phase mode
   before gauging. Do not set a mass formula as the test's input.
3. Derive spectator masses from the actual monomial substitutions;
   track both the field phase and charged Weyl bilinears. Wrong
   conjugation/power must fail. The original spinor sector has no
   same-chirality D5 singlet mass: directly check that no pair of
   its D5 weights sums to zero. This is a sufficient obstruction,
   not a claim that weights alone always prove singlet existence.
4. Differentiate the local Wess--Zumino term under theta->theta+4e
   and compare with i*e times the independent full light anomaly
   divided by its U1 curvature c=t/4. Retain the missing-counterterm
   and charge-three mutants; distinguish consistent from covariant
   cubic anomaly conventions in the report.
5. Reuse t and the nontrivial holonomy element u/3 to compute phases
   for all original spinor weights. Establish its order three and
   nonzero t image; the Z3 is an actual gauge subgroup and is NOT
   identified with the geometric source-isometry C3.

Seal design/source/tests and generated digests before execution.
First execute native JSON and 5 direct tests, then the expanded
40-file regression. Capture each run with its actual exit status;
the latter is not relabeled the old 39-file first run. No worktree
edits while a scientific/certifying run is live. Preserve failures
and the existing banking debts; independent review remains unpaid.
