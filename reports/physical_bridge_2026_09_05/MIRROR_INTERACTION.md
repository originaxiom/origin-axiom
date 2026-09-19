# R33: an allowed interacting route, not yet mirror removal

2026-09-19. Path-local source/physical-bridge work; no shared B number,
main acceptance, independent proof review or completed TOE.

**Outcome:** the actual subgroup H of the quotient parent admits a
mirror Yukawa and a charge-four phase-locking term. The construction
connects the real-vector Spin(10) mass mechanism to the charge-four
scalar already used in the added source model. It goes beyond R32's
free-operator projection, without pretending that an allowed interaction
has already produced the required quantum phase.

The [authored argument](MIRROR_INTERACTION_PROOF.md) and
[pre-execution design](MIRROR_INTERACTION_DESIGN.md) were pushed at
`c75647aa5a02401b635f340f0db9d37d7f8ee5a0` before execution.
The producer passes nine exact check groups. Original tests: 18 pass /
2 fail; fixed five-file run: 104 pass / the same 2 fail. Those failures
are independently diagnosed below, not erased. No full-green claim.

## 1. What is positive, exactly

The actual charged adjoint spinor is psi=16_1. Its opposite-chirality
partner, written as a left-Weyl field, is chi=conjugate(16)_-1.
Add S=10_2 and retain Phi=1_4. All are genuine H representations;
this does not import the forbidden fundamental 27 of E6/Z3.
An explicit D5 weight map matches the actual parent roots, not just
the familiar representation dimensions. The full 900 generator
identities, on both chiralities, establish the two Yukawa intertwiners.

The allowed terms include

    y_m S_a chi^t epsilon Y_a chi + h.c.,
    -kappa (Phi^dagger S dot S + h.c.).

For nonzero Phi, J_Phi(S)=(Phi/|Phi|) conjugate(S) is a gauge-covariant
real structure. Its fixed bundle is real rank ten. This is a global
bundle statement after the Phi reduction, not a globally chosen square
root of its phase. R21 identifies the surviving group as Spin(10).

For real n, the Yukawa mass satisfies

    Delta(n)^dagger Delta(n) = |n|^2 I_16.

The Clifford coefficient identities prove this for every real n,
not only sampled directions. These are singular-value masses; a
Yukawa matrix here need not be Hermitian. This useful algebraic
ingredient is now checked in the actual charge convention.

## 2. What the controls prevent us from claiming

**A complex scalar is not automatically enough.** A nonzero S can
still leave massless fermions. S=e1+i e2 has norm squared two but
rank-eight Yukawa, with squared singular values 0 and 4, eight each.
In general they are rho +/- sqrt(rho^2-|S dot S|^2), rho=S^dagger S.
The phase-locking step matters; simply citing a real Spin(10) vector
would have missed this issue in the charged model.

**An ordered scalar is not a symmetric quantum gap.** At fixed Phi=f,
the tested potential has an ordered real-vector minimum with one
radial, nine tangent and ten massive imaginary directions. That
vacuum breaks Spin(10) to Spin(9). A symmetry-restored interacting
phase requires a separate quantum demonstration. S9 topology is
not a substitute for its spectrum or correlators.

**Gauge symmetry does not select the mirrors.** S^dagger psi psi is
also allowed. Suppression of the unwanted physical-sector coupling
must come from derived localization/form couplings or another stated
input; choosing y_p=0 is not a consequence of these charges.

**Ordinary mass mixing is not the desired solution.** With a fixed
mirror Majorana block and nonzero Dirac mixing, the exact 32-state
control has no zero mode. At mu=2,M=3 its singular masses are 1 and 4,
each sixteenfold. A small seesaw-like eigenvalue is not an unpaired
chiral mode in an unbroken Spin(10) theory.

**Anomaly matching remains necessary.** The full vectorlike H theory
has vanishing anomaly; the light spinors alone do not. Pure D5 trace
anomalies vanish, but this finite calculation is not a new global
anomaly or full-determinant proof. Higgsing H does not authorize
dropping its matching terms or its defects.

**C3 invariance has a price.** Under R32's inherited single-line lifts,
an invariant charge-four scalar can be nonzero at only one of the
three fixed arcs. Activation on all three requires symmetry breaking
or separately supplied compensating flavour lifts. This is not a
universal ban on three sources or a C3-invariant action.

Finally, the fixed-Phi potential calculation is NOT a new coupled
stationary solution: nonzero S and its quantum fluctuations can
backreact on Phi, the source density, gauge field and geometry.
R29's old stationary construction cannot be transferred unchanged.

## 3. Literature read, with the competing claims retained

Four primary papers, 41 pages including appendices, were personally
read. [Reading record and version hashes](MIRROR_INTERACTION_PRIOR.md).
The real-vector proposal motivates an interacting mechanism; the
conditional doubling critique requires composite-channel and gauge-
current tests. Neither is treated as a universal success or failure.
The recent domain-wall simulation is a two-dimensional FK benchmark,
not a four-dimensional Spin(10) or geometric-source completion.

This is a change of question from "can a projection delete one
positive-energy partner?" to "does a specified interacting source
theory have the required asymmetric low-energy phase?" The former
has R32's answer; the latter now has explicit globally allowed
couplings and concrete checks, not yet an answer.

## 4. Failures, successor controls and exact evidence

| run | result | what it covers |
|---|---|---|
| [original native](MIRROR_INTERACTION_NATIVE_FIRST.json) | 9/9 groups, exit 0 | exact weights, intertwiners, masses, potential and phase action |
| [original tests](MIRROR_INTERACTION_TESTS_FIRST.txt) | 18 pass / 2 fail | 20 instances in the original new file |
| [original focused](MIRROR_INTERACTION_FOCUSED_FIRST.txt) | 104 pass / 2 fail | the five full files fixed before execution |
| [normal-form v1](MIRROR_INTERACTION_NORMAL_FORM_FAILED.txt) | TypeError, no verdict | attempted mutation of an immutable negative fixture |
| [normal-form v2](MIRROR_INTERACTION_NORMAL_FORM_V2_FIRST.json) | both chiralities pass | exact residual and symbolic family, two rejecting controls |
| [v2 tests](MIRROR_INTERACTION_NORMAL_FORM_V2_TESTS.txt) | 6 pass | separate corrective control |
| [expanded focused](MIRROR_INTERACTION_FOCUSED_V2.txt) | 110 pass / same 2 fail | original five files plus v2's test file |

The two original failures compare an expanded matrix against an
unexpanded scalar expression using structural equality. The separate
control obtains exactly zero residual and norm squared ten in both
chiralities, proves the two-parameter collinear family, and still
rejects a changed matrix and the noncollinear null vector. Thus the
failure is diagnosed as test-expression normalization, not physical
gap loss. The original tests and outputs remain unchanged.

The first corrective fixture halted because copying an immutable
SymPy matrix did not make it mutable. V2 changes only that fixture's
construction. Original v1 tests and its planned expanded run are
NOT RUN after the halt, not passing. Control seals `878f6866` and
`a2d52162` were pushed and remote-confirmed before their executions.
Every scientific source remains byte-identical to its respective seal.
[Receipts](MIRROR_INTERACTION_RECEIPTS.json) preserve raw hashes,
commands, populations, failures and narrowly redacted public copies.

No complete-repository run was made. R31's historical 54-file outcome
and its 24 failed/error IDs remain; the halted v1 tests would be
additional failures in an unqualified repository-wide run. R33 does
not hide that debt behind the successful v2 population. Governance
and cumulative custody outcomes are recorded in MIRROR_INTERACTION_FINAL_CHECKS.txt.

## 5. Next work on the same mission

1. Derive an actual local source interaction and normalized overlaps
   for both partners. The allowed physical-sector Yukawa must be
   included, bounded or excluded by an explicit mechanism.
2. Integrate or regulate the charged scalar sector while preserving
   its phase-locking and anomaly data; determine which interactions
   genuinely violate unwanted mirror fermion number. Positive mass
   matrices for frozen scalars do not answer this.
3. Test the interacting phase with physical/mirror cross-correlators,
   fermion and boson gaps, symmetry order parameters, composite
   channels and conserved-current response under cutoff/volume control.
4. Recompute the coupled source/end solution and full quantum matching
   in the same theory, including C3 treatment and the complete cusp.

These are acceptance duties, not a guarantee the candidate works.
The original conditional singular three/zero result, the resolved
light partners and the new class/tower nonsemisimple positives all
remain in their own domains. The overall objective still includes
the physical SM limit, discriminating predictions, common quantum
gravity and cosmology; no part of that is replaced by this checkpoint.
