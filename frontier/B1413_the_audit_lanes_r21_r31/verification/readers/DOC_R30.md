# R30: what happens to the chiral sector when its cores are resolved?

## VERDICT AS THE SEAT STATES IT

"The added R29 source model now has an explicit quadratic fermion
extension with positive bulk kinetic norm, a self-adjoint compact operator
domain, and full transmission through artificial core interfaces. In this
specified smooth, flat/exact, absolute-boundary class, its finite-width
zero modes are ordinary twisted cohomology. The two nontrivial
source-C3-compatible m202 characters have no zero modes at finite width...
There is also a conditional low-energy result: sufficiently strong
shrinking logarithmic wells produce light opposite-chirality pairs, not a
proof that unwanted partners become heavy."

## DECLARED INPUTS AND HYPOTHESES

- Prescribed: R29's finite-width charged tube source, flat/exact stationary
  point h=dF_epsilon, unitary coefficient line L; R23's single charged
  representative 16_(1) with its "parent conjugate is not counted as a
  second determinant."
- Boundary hypothesis: "absolute" condition iota_n psi=0 at the compact
  truncation boundary, explicitly flagged as "an input compact regulator,
  not the object's selected physical cusp condition."
- Sourced Hilbert-complex machinery: Wen Lu's Thom-Smale-Witten theorem for
  manifolds with boundary (MRL 24, 2017, section 4) and Anne-Takahashi on
  whole-form transmission (Analysis & PDE 8, 2015) — both flagged as used
  only for their specific stated equations, not their headline spectral
  theorems.
- The frozen m202 Fox complex data (dimensions 1,2,1,0; polynomial
  P=x^2y+x^2+xy^2+xy+x+y^2+y) reused directly from R19/R20, "not a newly
  discovered cohomology engine."
- Light-mode implication conditions 1-3 (uniform cutoff away from arcs,
  |F_epsilon - beta_j log r| <= C on an interior subsegment, a_j=q beta_j>=1)
  stated as explicit additional hypotheses distinct from the finite-width
  theorem.
- Self-correction: the design's original claim that (zeta,1),(zeta^-1,1)
  is "a C3 pair" is retracted in-report — "not fixed by the source's C3
  action" — replaced by an independently rebuilt action from R20's word
  maps giving fixed points (0,0),(1/3,2/3),(2/3,1/3).

## CONTROLS

- "The original assertions were valid generic-character checks; their
  passing result did not verify that source-compatibility claim" — the
  seat marks its own C3-pair error rather than silently patching it, and
  preserves the original run.
- Euler-characteristic control: "any extending flat rank-r coefficient on a
  compact oriented three-manifold with torus boundary has twisted Euler
  characteristic r*chi(Q)=0. This constrains this absolute graded kernel,
  not every physical defect theory."
- Chain-homotopy control on the core-attachment mapping cone: exact
  contraction exhibited for generic t != 0; "A singular matrix can retain
  pairs" — the attachment result is not claimed for all t.
- Axial-cutoff trap control: "A cutoff along only an interior arc segment
  would be invalid for the light-mode conclusion... The explicit
  sin(pi*z/L) comparator retains pi^2/L^2."
- Overlap-transfer control: the R25 normalized-coupling identity "does not
  apply unchanged to R29's nonconstant massive extra-U1 mode."

## TESTS ON THIS BENCH

`python3 -m pytest tests/test_physical_bridge_resolved_fermion*.py -q --no-header -p no:cacheprovider`

`33 passed in 12.64s`

No failures (this includes the C3-control test file). The seat's own
report separately records an original native run (18/18 checks, 105 exact
rows), original new tests (30 passed), a focused six-file run (110 passed),
a 52-file broad regression (458 passed/16 failed/8 errors, "all 24
failed/error IDs equal R29's"), and a separate 5/5-check C3 control run —
not independently re-run here beyond the test files matched by the glob.

## CLAIMS FOR MAIN

1. In the added finite-width quadratic-fermion extension with absolute
   boundary data, the two nontrivial source-C3-compatible m202 characters
   have zero kernel (no zero modes) at every finite core width. —
   PROVED-BY-SEAT (conditional on the stated smooth/flat/absolute-boundary
   class; explicitly not a retraction of R19's singular three/zero result
   on its own different domain).
2. Under additional quantitative well conditions (uniform log-behavior on
   an interior arc, a_j >= 1), resolving k source cores produces at least
   k light opposite-chirality Dirac pairs as width shrinks, not heavy
   partners. — CONDITIONAL ("this is not a certified global Poisson
   asymptotic for the actual m202 solution").
3. (zeta,1),(zeta^-1,1) is not the source's actual C3-fixed character pair;
   the correct fixed points are (0,0),(1/3,2/3),(2/3,1/3) via the rebuilt
   action A=[[-1,-1],[1,0]]. — PROVED-BY-SEAT (self-correction of the
   round's own earlier design/test naming).
4. Full-form transmission through an artificial core-cutting interface
   requires matching both normal and tangential Green-form data; tangential
   matching alone fails. — PROVED-BY-SEAT.

## CONFLICTS WITH MAIN

Searched `git -C <repo> grep -l -F "<phrase>" -- docs frontier`
for "light opposite-chirality" and "no zero modes at finite width": no hits.
Also checked "zeta,1" and "C3-compatible": the only hits are
docs/views/VERDICT_LEDGER.md and frontier/B1304_the_audit_seats_4d_model/
(arc_verdict.json, DESIGN.md, FINDINGS.md), which independently describe
"the trivial character and a conjugate pair of order 3" from B1302's
order-3 H1 matrix — consistent with, not contradicting, R30's corrected C3
locus. NONE found that contradicts R30's stated result or scope.

## WHAT MAIN WOULD HAVE TO VERIFY

Independently reconstruct the R20 word-map action A=[[-1,-1],[1,0]] and its
three fixed torus points to confirm the corrected C3 locus; verify the
chain-homotopy attachment argument at t=0 vs. t!=0 for the k=3 case
directly against the frozen R19 Fox complex.
