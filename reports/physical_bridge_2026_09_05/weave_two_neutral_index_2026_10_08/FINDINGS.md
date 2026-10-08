# Two neutral spin fields still leave a magnetic saddle

The second neutral spin field does not stabilize this magnetic family.
An authored global argument, checked by two exact implementations,
forces at least 10 complex physical negative directions for every
nonzero integer flux and every finite pair of neutral amplitudes.

The result is conditional on the same supplied curved E8 action,
complete curvature-minus-one punctured elliptic surface, trivial
extending spin line, principal embedding and complete graph domain.
It does not exclude other condensates, stationary phases, ends, sources,
parents or the full generated architecture. An unstable symmetric
configuration can be a starting point for symmetry breaking; it is not
by itself evidence that the underlying action is inconsistent.

## What was tested

The admitted stationary family is

    A=A_n=s(w+2nZ), Q=Q_principal+c*psi*Z, R=d*psi*Z,

with integer n and finite complex c,d. Both spin fields already belong
to the parent action. All connection couplings, mixed commutators,
conjugate charges and the nonzero stationary moment are retained.
The new field is not rotated away: the principal/neutral coefficient
matrix has determinant d/2, invariant in rank under the actual constant
SU2 flavor symmetry. At d!=0 this genuinely extends the R=0 family.

All F residuals vanish, while the parallel moment is -nZ. The energy
is pi*n^2*kappa(Z^2)/g6^2, independent of c,d. The actual physical
quadratic form, after adding its nonnegative gauge-fixing square, is

    g6^2 V2_gf(x)=norm(D0 dagger x)^2+norm(D1 x)^2-nq*norm(x)^2,

where x contains the connection, Q and R variations in their positive
kinetic metric, and q is the integer Z charge. PROOF.md derives the
three bundle maps and all coordinate weights from the same action.

## Why the auxiliary slot matters

The full F map and its relation give an elliptic complex C0 through C3.
C1 is the physical variation space. C3 is analytical bookkeeping,
NOT an added field. The odd-to-even Hodge map is

    T(x,sigma)=(D0 dagger x, D1 x+D2 dagger sigma).

Its kernel is H1 plus H3. H1 consists of physical fluctuations
annihilated by D0 dagger and D1; H3 is ker(D2 dagger). A positive
index of T cannot be counted as physical instability until H3 is removed.

For d!=0, the first component of D2 dagger contains multiplication by
the charge-q scalar conjugate(d*psi). The section psi is nonzero at
every interior point. Thus H3 vanishes in every nonzero charge. This
does not assume a positive lower bound at the cusp, where psi decays.
At d=0 this argument fails; the earlier, separately proved R=0
obstruction is used instead.

The completed zero-angular operator has 360 C1 channels and 136
auxiliary C3 channels. These are gauge-fixed operator channels, not
particle populations. Matching their dimensions to an earlier fermion
calculation would not establish a physical identification.

## The global index and the physical lower bound

Both spin-shifted principal blocks are retained, including their
unpaired extremes. The second block is derived explicitly from the
coordinate metrics, not guessed by shifting a mass formula. A homotopy
removing the principal coupling keeps a squared essential threshold of
at least 1/4 on the unchanged complete domain. It is an operator
homotopy, not a family of stationary backgrounds.

Finite c,d give bounded, decaying, graph-compact perturbations. The
constant principal field is not called compact. The exact spin-power
Dolbeault index J, with the previously proved logarithmic endpoints,
adjoint kernels and global pole-dimension bounds, gives

    ind T_q = sum_m multiplicity(q,m) *
              [2J(1-beta)-J(-beta)-J(2-beta)],
    beta=m+2nq.

The bracket is zero at beta=0 and is
-sign(beta)*(-1)^beta at other integer beta. For nq>0 the full E8
roster yields:

| Absolute Z charge | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---:|---:|---:|---:|---:|---:|
| Index, abs(n)>=2 | -6 | 6 | 4 | -3 | -6 | -1 |
| Index, abs(n)=1 | 0 | 6 | 4 | -3 | -6 | -1 |

The first-flux endpoint is not discarded. The all-integer statement
uses the actual weight bound and parity, not the finite test grid.
Opposite flux uses the conjugate charges.

After H3=0 is established, the positive indices force at least six
and four complex H1 modes in q=sign(n)*2 and sign(n)*3. On H1 the
physical gauge-fixed quadratic form is -nq times the positive norm.
Graph-dense compact approximants give negative subspaces with
finite-quartic nonlinear paths. Removing the nonnegative gauge-fixing
term preserves negativity; stationarity and gauge invariance make
those directions inject into the physical quotient.

Closing scope: in this supplied action, geometry, spin and domain,
every member of A=A_n, Q=Q_principal+c*psi*Z, R=d*psi*Z with n!=0
and finite c,d has at least 10 complex physical negative directions,
equivalently a real negative subspace of dimension at least 20.

At d=0 the earlier lower bound of 50 is stronger. At c=d=0 the
30abs(n) connection bound also remains valid. At abs(n)=1 the earlier
infinite physical Morse index survives both decaying neutral fields.
These are lower bounds, not a complete Morse count. The change from
a 50 bound to a 10 bound does NOT demonstrate that 40 modes were lifted.
Negative or zero index entries do not demonstrate stability.

## Positives retained and the next physical question

At n=0 all residual squares vanish. For (c,d)!=0 the connected gauge
group is S(U3 x U2), without an extra Wilson angle, and the full
classical Hessian is nonnegative. Flat neutral data remain unselected.
The existing fixed-domain fermion homotopy preserves zero charged
index; individual zero-mode multiplicities may jump. This is an
admitted SM-gauge minimum, not a derived chiral Standard Model.

The magnetic result closes amplitude stabilization only within the
displayed neutral ansatz. It does not determine whether a charged
condensate gives another stationary minimum, preserves color, produces
a suitable electroweak pattern or has acceptable fermions. None of
those conditions is established here.

The next bounded diagnostic is the actual four-Weyl mass map from
the superpotential Hessian and gauge couplings of this SAME action.
Any relation to T must be exhibited with trace pairing, conjugate
charges, positive metrics and complete domains. An auxiliary index
cannot be promoted by resemblance. A complete charged index and
anomaly calculation would tell us whether further vacuum construction
in this parent is physically worthwhile.

This explicitly refines the earlier research order saying that only
a stable phase advances to the fermion dictionary. A final physical
vacuum still owes stability. A stationary saddle can nevertheless
support an informative operator/anomaly diagnostic before an expensive
charged-condensate search. NEXT_TEST.md is a post-run plan, unexecuted
and outside the present seal. Source/boundary and silver routes retain
their own parents and their existing positive results.

## Verification, intake and acceptance

Pre-execution seal 5a881c0ca884037816bb3f8a0ae807dc711d185c was
committed, pushed and server-confirmed before scientific execution,
import or test collection. Seven scientific files and eight pinned
and working dependencies remained byte-identical. No scientific
failure or source repair occurred.

First unchanged executions passed 29 native predicates, 18 separate
reference predicates, 20 focused tests and 216 tests across thirteen
packets. Native elapsed time was 8.894446 seconds; reference 0.150091
seconds. Focused pytest reported 13.25 seconds and regression 94.68
seconds. Regression ran with the tree read-only and unchanged.
Literal outputs, exit codes and hashes accompany this report.

Both implementations have the same author. They check exact algebra,
rosters, weighted coordinate substitutions, endpoint arithmetic and
failure controls. They are not outside certification of the global
bundle/domain/Fredholm or physical-quotient argument.

Preseal governance returned 26 PASS and four inherited FAIL categories:
attribution, test vacuity, seal provenance and relay debt; review
counter 376. Final governance again returned 26 PASS and the same four
inherited FAIL categories, review counter 377. The staged and working
trees were unchanged during that gate; its checked content tree and
literal output hash are in RECEIPTS.json. Subsequent additions only
record the gate, receipts and this disposition. The identification
audit retained nine UNEARNED rows against baseline nine.
Full-suite, nonauthor analytic and main-bank acceptance remain
outstanding; this is not an all-green repository.

Post-run fetch advanced main to da3027e03: B1616 results and GENESIS
v1.33, followed by B1617 preregistration. SM remained 7c5d9726c.
INTAKE_AFTER_RUN.md distinguishes personally read incoming evidence
from unreproduced claims, numerical calculations from exact proofs,
and owner-tagged postulates from parameter-free derivations. None is
used as evidence for this packet's obstruction.

The foundational selection of action, geometry, spin, embedding and
flux remains open, with act/register/lift information to be retained.
Physical chirality, interactions on modes, anomaly cancellation, three
families, normalized parameters, quantum consistency and gravity remain
distinct duties. Qualia is a registered hypothesis, not an identified
observable. The full SM/TOE goal remains active and unachieved.
