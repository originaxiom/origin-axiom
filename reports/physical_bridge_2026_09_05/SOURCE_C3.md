# R32: three source modes are not three invariant source modes

2026-09-16. Path-local result on the prescribed sourced realization.
Seal **eeedd0e6** was pushed and remote-confirmed before execution.
[Proof](SOURCE_C3_PROOF.md), [design](SOURCE_C3_DESIGN.md),
[prior](SOURCE_C3_PRIOR.md), [receipts](SOURCE_C3_RECEIPTS.json).

**Result:** for either nontrivial source-C3-compatible flat character,
the singular three/zero kernel is the regular C3 representation.
Each of the three scalar lifts therefore retains ONE invariant source
mode. In the distinct resolved-core realization, the honest symmetry
projection retains positive-energy partners together. It does not
turn R31's light Dirac pairs into three unpaired generations.

This is an authored analytic argument with exact finite controls, not
independent proof acceptance or a no-go for every orbifold/source theory.
The earlier unprojected singular three/zero result is preserved.

## 1. The distinction in one table

All rows use the actual nontrivial invariant characters
(zeta,zeta^-1) and its conjugate, not the nonfixed (zeta,1) sample.

| Declared realization | Zero modes in the relevant charged sector | Small-width statement |
|---|---|---|
| Strong singular maximal domain, no quotient | Three/zero, carrying 1 + zeta + zeta^2 | This is not the smooth-core domain |
| Same singular domain, honest C3 invariant sector | One/zero for every scalar lift | No physical quotient choice is derived |
| Resolved compact absolute domain, C3 invariant sector | No zero modes at finite width | At least one positive light Dirac pair for strong shrinking sources |

The third row is an at-least bound, not exactly one massive pair or a
numerical mass calculation. It retains the fixed compact truncation,
extending flat line, invariant metric/source/end data and ordinary bulk
kinetic norm. The complete cusp limit and extra localized sectors are
not determined by this table.

## 2. Why the fixed arcs carry different weights

The actual C3 action fixes each of the three proper source arcs
pointwise. That does NOT force its action on the flat line fibres to
be the same on all three arcs: parallel transport between fixed
components can contain nontrivial holonomy.

R19's Fox complex gives H*(Q;L)=0 at both nontrivial invariant
characters. The fixed-fibre Hopf trace identity then forces
lambda_1+lambda_2+lambda_3=0. With an honest order-three lift, each
lambda is a cube root of unity, so there is exactly one of each.
Possible extra closed fixed circles have Euler zero and do not affect
this conclusion. The equivariant pair sequence identifies these fibre
sections with H1(Q,N;L), hence the actual source mode module.

The [proof](SOURCE_C3_PROOF.md) spells out the finite-cell trace identity,
boundary hypotheses and equivariant singular comparison; it uses the
primary triangulation theorem only at the stated scope. This module
identification is not obtained by naming three modes a triplet.
No ordered weight-to-geometrical-arc assignment is claimed.

The trivial line is an important different control. Its relative
groups carry H1=Reg+1 and H2=1. The three lift phases give projected
counts two/one, one/zero, one/zero. Their net index is one, but they
are not all the same full kernel. All three fixed fibre weights can
coincide there because the base is not acyclic.

## 3. What happened to the core partners

In R30's split relative-plus-core model, the core and relative modules
are both regular. Their nonzero attachment is an equivariant
isomorphism. Projection keeps one on each side before gluing and
keeps the gluing itself. Deleting only the even/core partner fails
the commuting-differential check.

The stronger analytic statement uses the actual domain: when a
grading-preserving unitary U commutes with the self-adjoint D,
D/sqrt(lambda) intertwines the even and odd eigenspaces at every
positive eigenvalue of D^2. A symmetry projection cannot keep only
one of those partners. For the invariant R31 Poisson family, the
three disjoint whole-arc trial functions have the three fibre weights;
min-max in each sector gives one light pair per character and hence
at least one invariant light pair.

This must NOT be widened into "projection never makes chirality".
The exact circle-reflection control projects its zero modes to
one/zero while leaving each positive Fourier level paired. The
zero-eigenvalue and positive-eigenvalue statements have different
hypotheses. New orbifold-localized fields or changed boundary domains
also require their own analysis.

## 4. Evidence and limits of verification

* [Native first run](SOURCE_C3_NATIVE_FIRST.json): 8/8 check groups,
  exit zero, 4.03 s. All 27 ordered fibre triples are tested; precisely
  the six permutations of the regular weights have zero trace.
* [New tests](SOURCE_C3_TESTS_FIRST.txt): **22 passed**, 4.46 s.
  Exact matrices, both C3 generators, all scalar lifts, basis changes,
  trivial-line cone, core attachment, tensor factors and rejecting
  group/domain controls. No float eigenphase threshold is used.
* [Focused run](SOURCE_C3_FOCUSED_FIRST.txt): **96 passed**, 20.11 s,
  one optional-GUI warning. It includes all new tests and the four
  unchanged test files fixed in the design. Not 118 distinct tests:
  the new 22 are included in the 96.

All science files remained unchanged after the seal and the tree was
read-only during execution. Frozen R20 geometry certificates are reused,
not newly rerun or upgraded. The small algebraic chain models are not
PDE meshes. Finite tests check the proof's inputs and consequences;
they are not independent verification of the full analytic proof.

There were no failed R32 scientific runs or test repairs. A pre-seal
metadata attempt to use the system SHA utility failed because of its
locale; Ruby SHA256 supplied the six actual seal hashes before commit.
A syntax issue caught by inspection before sealing was corrected before
any execution. Neither event is a suppressed scientific negative.
All earlier failed science, including the packet alias and original R20
instrument failures, stays unchanged. The historical R31 54-file result
remains 508 pass / 16 fail / 8 error; it was not rerun here and is not
a whole-repository certificate. Reporting checks are recorded separately
in SOURCE_C3_FINAL_CHECKS.txt.

## 5. Mission consequence and the next physical duty

The parent/quotient idea now has a specific source-spectrum calculation.
The unquotiented three-mode result is intact; requiring this particular
quotient changes its count. The simplest honest projection of the
resolved theory does not remove its core partners. Thus merely adding
an order-three group label is insufficient at this step.

This scopes one explicit proposal and leaves constructive alternatives:

1. Keep C3 as a global symmetry and derive a defect/end action realizing
   the singular three/zero domain, or another physically justified
   chiral domain, with its full kinetic norm and gauge transformations.
2. If C3 is gauged, specify the full parent lift and any additional
   localized fields before counting the quotient spectrum. The current
   calculation covers the inherited invariant sector only.
3. If interactions are intended to remove resolved partners, write
   the gauge-invariant couplings and demonstrate the resulting spectrum
   and complete anomaly cancellation in that SAME realization.

These are stated alternatives, not already derived mechanisms. The
existing R21/R22 anomaly and same-source composition checks remain
applicable within their stated ansatz. Neither deleting a cochain nor
renaming an algebraic 27 supplies the missing physical action.
Vacuum/source/end selection, full quantum consistency and empirical
predictions remain unachieved on this lane; the complete TOE goal is
not achieved. This report makes no semantic absence claim about the
whole repository or other theories and allocates no shared B number.
