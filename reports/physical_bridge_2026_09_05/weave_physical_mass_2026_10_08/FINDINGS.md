# Physical charged chirality and the anomaly completion duty

October 8, research checkpoint. In the SAME supplied curved E8 action,
the actual four-Weyl mass operator has nonzero net charged chirality on
the admitted magnetic stationary family. This is a conditional physical
operator result, not merely an index of a bosonic deformation complex.
The backgrounds remain saddles. The full charged zero-mode index is not
three Standard Model generations, and its perturbative anomaly traces
are nonzero. A stable, anomaly-completed physical vacuum is not derived.

Scope: the fixed complete curvature-minus-one punctured elliptic surface,
trivial extending spin, principal embedding, action and complete graph
domain, with A=A_n, Q=Q_principal+c*psi*Z, R=d*psi*Z for integer n and
finite complex c,d. These inputs are supplied, not selected by genesis.
Other parents, end data, sources and the full generated architecture are
not excluded. No empirical parameter comparison or shared B/I allocation.

## The physical identification is explicit

The four independent left Weyl fields are the gaugino lambda and the
three chiral coefficients a,u,v. Their kinetic densities are
(Omega^2,1/2,Omega,Omega). The quadratic superpotential is

    W2 = integral kappa(u Dbar v + i a([q,v]-[r,u])).

Together with the kinetic-metric dual of the actual gauge Killing
vector, this fixes every entry of the mass operator. No diagonal
bosonic D-term mass is inserted into the fermion bilinear. The neutral
parallel gaugino remains a physical, finite-norm zero mode, not a ghost.

The previous Hodge map T and this physical mass map M obey

    M = Uout T Uin,
    Uin(lambda,a,u,v) = ((a,u,v), i*Omega^2*lambda/sqrt(2)),
    Uout(g,p1,p2,t) = (g,2i*t,p2/Omega,-p1/Omega).

Both maps are isometries between the actual weighted bundles. The
previous auxiliary C3 slot is identified with the EXISTING physical
gaugino by the volume form; no new field is added. The output lies in
the conjugate Hilbert space of the opposite-charge left coefficients,
using the E8 trace pairing. The variable-metric derivative cancels
inside the volume-form substitution, not by treating Omega as constant.

The charge-dual bilinear transpose, including integration by parts,
identifies the adjoint kernel with the conjugate-charge left kernel.
Consequently ind(M_R) counts left R minus left conjugate(R), without
counting right antiparticles again or equating independent left fields
by adjoint reality. The maps preserve compact-support cores and graph
norms, hence the complete closures. The prior complete-domain Fredholm
proof retains both shifted end blocks and their extremes. Finite c,d
are graph-compact perturbations. These global analytic steps are the
authored proof in PROOF.md; finite matrix tests do not replace them.

The component W-Hessian and gauge-coupling structure uses Martin,
[A Supersymmetry Primer, sections 3.4 and 7.1](https://arxiv.org/html/hep-ph/9709356v7).
The curved bundle maps and domain argument are our calculation, not a
theorem borrowed from that finite-dimensional example. The complete
paper is not claimed read.

## Net physical charged multiplicities

The full E8 root population, including eight Cartans and all conjugate
charges, agrees exactly with a separate SU5 tensor reconstruction.
The connected gauge group is S(U3 x U2); Z is the integer cocharacter.
Conventional Y=Z/6 remains a supplied normalization label.

| Z | Representation | Internal module | Net for n=1 | Net for n>=2 |
|---|---|---|---:|---:|
| 1 | (3,2) | V2 | 0 | -1 |
| 2 | (bar3,1) | V1+V3 | 2 | 2 |
| 3 | (1,2) | V1+V3 | 2 | 2 |
| 4 | (3,1) | V2 | -1 | -1 |
| 5 | (bar3,2) | V0 | -1 | -1 |
| 6 | (1,1) | V2 | -1 | -1 |

A negative entry means net left-handed conjugates of that row. All
entries reverse for negative n and vanish for n=0. The charge-five
exotic from the gauge 24 is retained. These are multiplicities, not
representation dimensions or complete kernel counts. Additional
vector-like zero pairs are not determined by the index.

For beta=m+2nq the contribution per internal weight is
I(beta)=2J(1-beta)-J(-beta)-J(2-beta), equal to zero at beta=0 and
-sign(beta)*(-1)^beta otherwise. J is the complete-cusp spin-power
index, not the closed-surface degree. Actual weight bounds and parity
prove the all-integer statement; the finite flux grid only checks it.
In particular the first-flux charge-one endpoint is not erased.

## Anomalies distinguish this positive from a consistent chiral vacuum

With A(3)=1 and T(fund)=1/2, the coefficient order is
(SU3^3, SU3^2 Z, SU2^2 Z, Z^3, gravity^2 Z):

| Flux | Coefficients |
|---|---|
| n=1 | (-1,-5,-9/2,-1002,-24) |
| n>=2 | (-3,-6,-6,-1008,-30) |
| n=0 | (0,0,0,0,0) |

Negative flux reverses the signs. Full root traces use the required
half factor when both members of a conjugate pair are included; the
separate tensor route uses one signed representative. They agree.
Known anomaly-free SM-generation and vector-pair controls pass; dropping
the exotic or double-counting conjugates changes the answer and fails
the controls. Unknown vector-like pairs cannot cancel these traces.

These symmetric traces diagnose local perturbative gauge anomalies;
opposite-chirality pairs cancel, as in Bilal,
[Lectures on Anomalies, sections 7.1 and 7.2](https://arxiv.org/html/0802.0634v1).
The finite zero-mode spectrum therefore cannot be gauged as a standalone
four-dimensional quantum theory without compensation. This is NOT a
calculation of the complete noncompact determinant, regulated end
response or inflow. Their cancellation cannot be presumed or excluded
by this result. No global anomaly is calculated. The older R23 local
inflow calculation retains an outer-end anomaly for internally constant
gauge transformations and is in a different parent; it is not a free
completion of this model.

The separate bosonic result also stands: every nonzero-flux member of
the finite two-neutral-field family is unstable. At n=0, nonzero neutral
condensates still give a nonnegative SM-gauge minimum with flat moduli
and zero net charged index. Stability, anomaly completion and selection
are three distinct duties; none is discharged by naming the index.

## Verification and custody

Pre-execution commit 05c63c15a7804dde53b660e6ace20184d626b7d2 was
pushed and server-confirmed before scientific execution. Seven science
files and twelve pinned AND working sources remain byte-identical.

| Check | First result | Captured elapsed seconds |
|---|---|---:|
| Native exact predicates | 33 PASS, exit 0 | 9.601671 |
| Separate tensor and coefficient predicates | 15 PASS, exit 0 | 1.290737 |
| Focused tests | 22 PASS, exit 0 | 10.548847 |
| Fourteen-packet regression | 238 PASS, exit 0 | 49.661584 |

Pytest reports 9.72 seconds focused and 48.65 seconds regression; the
table includes invocation overhead. The tree stayed unchanged during
regression. Literal outputs and hashes are in NATIVE.json, REFERENCE.json,
FOCUSED.txt, REGRESSION.txt and RECEIPTS.json. No failed science attempt,
source repair or criterion change occurred. A misplaced, unexecuted test
draft was moved to its proper path before the seal; it is not a rerun.

Both implementations have the same author. Their agreement is not
nonauthor analytic acceptance. The complete graph-domain argument and
physical dictionary require outside review. This is not a full-suite
certificate or a main-bank merge. Preseal governance is 26 PASS with
four inherited FAIL categories, not all green. The first publication
gate also caught a new attribution token in the intake's branch name;
that unsealed prose was corrected, retaining the first gate output.
No scientific source changed. Final governance returns26 PASS with the
four inherited FAIL categories only (attribution, test-vacuity,
seal-provenance, relay-debt), review379 due, exit1. It ran on the unchanged
staged content tree2aa810d10ad471884a476446ee199a52ccc52a02 before these
literal capture files and receipt were added. GOVERNANCE_FIRST_PUBLICATION.txt
preserves the initial failure; GOVERNANCE_FINAL.txt the repaired result.
No all-green or full SM/TOE completion claim.

## What changes next

Stage2S is executed. Stage2T is the actual parent/end anomaly-compensation
test, before a costly charged-condensate search. The nonzero SU3 cubic
coefficient means addressing only an abelian normalization or U1 mass
does not by itself discharge the computed diagnostic. A regulated
parent mechanism, additional admitted sector or changed end/domain
must be explicit and derived, not attached by desired cancellation.
NEXT_TEST.md defines the unexecuted investigation.

INTAKE_AFTER_RUN.md records main through 760499985 and SM through
5af9a3bf6. Their new exact conditional fixed-space work answers our
earlier sampling question, but its numerical representation recognition
is distinguished from exact symbolic identities. None of those incoming
results is a premise of the sealed physical calculation. The sender
relay preserves the update and review questions on this branch.

The source and silver constructions remain separate alternatives.
The foundational derivation of this action, metric, spin, embedding,
flux and end law remains open in this work. Act/register and lift data
must survive that derivation; neither these operators nor their modes
identify an observer or qualia. Parameter-free SM and full TOE remain
the active, unachieved objective.
