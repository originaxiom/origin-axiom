# Symmetric state boundary responses and the grading assumption

October 24, 2026. Authored analytical response to P-210, pending
independent review. No scientific producer, test or numerical experiment
was executed. The mathematical classification below concerns the
specified fixed-fibre critical Green quotient, not a complete physical
boundary theory or a claim about every generated carrier.

At the stated symmetric state, Q8 covariance permits only even-dimensional
PLUS subspaces if the domain preserves the chirality grading. But the
same Green quotient admits a continuous U3 family of Q8-invariant
self-adjoint boundary planes when that restriction is not imposed.
The paper's coupling at that state does not by itself specify which
plane is the exterior response. This sharpens the missing physical law
instead of selecting a domain by its desired index.

## Source and fixed frame

Main's October 20 and 21 relays assign P-210 to this lane. B1678 at
fetched main `2bd171386` verifies the earlier state-dependent rank-three
example and its Q8 obstruction, while retaining the finite-distance
Fredholm application's analytic qualification. Its findings and
`verification/main_check/s3_commutant.py` were read, not rerun here.

Reuse [the state and boundary scope](COVARIANT_END_DOMAIN_SCOPE.md),
[the actual connecting map](ACTUAL_PUNCTURE_CONNECTING_MAP_AND_TRACE.md),
[coupling transport](REGISTERED_COUPLING_TRANSPORT.md),
[normal-frame transport](REGISTERED_PRINCIPAL_PARTS_AND_GREEN_TRANSPORT.md)
and [the exterior response argument](EXTERIOR_RESPONSE_AND_JOINING.md).
The source puncture proof explicitly restricts its Lambda classification
to grading-invariant domains. That qualifier is material, not a defect
in that proof. The present calculation uses its full two-slot quotient.

Fix one puncture, its actual coordinate/spin/coefficient frame, and the
source's positive coefficient metric. In the normalized local t frame,
write the two critical traces as u,v in W=C3 tensor C2, with Green form

    G((u,v),(u',v'))=u dagger v'+v dagger u'.             (1)

The omitted overall normal/orientation constant does not change null
planes. In the root frame, the d_y factors from the normal-frame note
must be restored; they are not assumed to vanish or be universally one.
The following fixed-state algebra uses the specified stabilizer acting
diagonally on the two slots by I3 tensor rho(h), h in Q8. It must not
be transferred to another geometric stabilizer or full E8 field without
the actual intertwiner, reality and slot actions.

## All maximal null planes and the Q8 constraint

Put a=(u+v)/sqrt(2), b=(u-v)/sqrt(2). Equation (1) becomes

    G=a dagger a'-b dagger b'.                          (2)

Every maximal complex null plane L of dimension six is the graph

    b=U a,  U in U(6).                                 (3)

Indeed projection to a is injective: if a=0, nullness gives ||b||^2=0.
Equal dimensions make that projection surjective. Nullness then says
U dagger U=I. Conversely a unitary graph is maximal null. This proof
does not use a numerical eigenvalue tolerance or a generic graph chart.

The Q8 action preserves a and b in the same way. Invariance of (3)
is therefore equivalent to U commuting with I3 tensor i and I3 tensor j.
These generate the matrix algebra on C2. Consequently

    U=C tensor I2,  C in U(3).                          (4)

This is a continuous family, not just the four possible even ranks.
It is a classification of coefficient-level candidate planes. Applying
the source's cone-domain correspondence, full physical reality law and
nonlinear action still requires their stated analytic/type hypotheses.
No abstract null plane alone proves a complete admissible physical end.

## Grading reduces that family to the familiar even ranks

The source chirality grading is Gamma(u,v)=(u,-v). It exchanges a,b.
Applying Gamma to (3) gives a=U b. Thus L is grading-invariant exactly
when U^2=I, or equivalently when U is Hermitian as well as unitary.
For (4), C is then a Hermitian involution. If its +1 eigenspace has
dimension r, the plus trace subspace is

    Lambda=ker(C-I) tensor C2,  d=2r, r=0,1,2,3.        (5)

The minus trace is Lambda_perp. Under the SOURCE'S finite-distance
ordinary-spin index formula, this gives

    index=d-3=2r-3 in {-3,-1,+1,+3}.                   (6)

So main's odd-index restriction stands WITH its grading premise.
For a general C in U3 that premise fails: the total self-adjoint Dirac
domain is not Gamma-stable, so restricting it to a separate chiral
Fredholm map and assigning (6) would change the operator problem.
This does not establish a physical zero index, or a way to evade all
chirality requirements. It exposes which requirement needs justification.

If the entire local registering action, rather than this state's Q8
stabilizer, is imposed on a fixed domain, the existing 2+4 commutant
gives another classification. If a full continuous family symmetry is
imposed, it supplies still another constraint. Neither is automatically
the symmetry of this particular state. No extra symmetry is adopted here
to manufacture extremes.

## A regular response can pass where a spectral projector fails

Within the u chart, every Hermitian H on W defines the maximal null plane

    v=i H u,   U=(I-iH)(I+iH)^-1.                      (7)

Substitution into (1) gives i u dagger H u'-i u dagger H u'=0.
The inverse exists because H has real eigenvalues. Q8 covariance at
the symmetric state requires H=A tensor I2 with A Hermitian; H=h I6
already provides a one-real-parameter fixed-state control. For h=0,
v=0 is the plus extreme. The other extreme u=0 is present in (3) as
U=-I, outside this finite-H chart, not a missing plane.

On the earlier supplied state space, use its own traceless Hermitian
field H2(S)=S S dagger-tr(S S dagger)I2/2. The algebraic state-dependent
planes

    v=i eta (I3 tensor H2(S))u,
    u=i eta (I3 tensor H2(S))v                         (8)

are smooth through S=I2, for any declared real eta. Under that note's
raw unitary coefficient action the same equivariance calculation for
H2 gives covariance of both planes. At S=I2 the first gives v=0,
the second u=0. Away from it they generally MIX the grading. These
are two candidate response laws, not two derived exterior theories.
Their eta, dimensions/units and physical interpretation remain supplied.
Actual geometric/spin transport has different scalar factors in the
two slots; covariance of (8) over that full family additionally needs
the corresponding response-line factor. No such factor is discarded.

For comparison, take any unit vector n in R3 and the Pauli matrix
n.sigma. For 0<t<1 choose the positive square root S_t of I2+t n.sigma.
Then H2(S_t)=t n.sigma, and the earlier rank-three PLUS projector is
I3 tensor (I2+n.sigma)/2, independent of t. Opposite n give orthogonal
projectors with operator-norm distance one although S_t tends to I2
along both paths. There is no continuous projector limit. In contrast
(8) tends to its stated extreme continuously, by losing Gamma-invariance
off the symmetric locus, not by contradicting (5). The singularity of
the chosen spectral projector is not alone a singularity of every
possible full response plane.

## The actual paper coupling supplies no boundary normal map

At the earlier symmetric state S=I2, M=epsilon^-1, the actual contraction
is

    Y_ab=sum_mn (C_a^T epsilon C_b)_mn (epsilon^-1)_mn,
    (C1,C2,C3)=(j,i,k).

Since C_a^T epsilon=-epsilon C_a and (epsilon^-1)^T=epsilon,

    Y_ab=tr(C_a^T epsilon C_b epsilon)
        =tr(C_a C_b)=-2 delta_ab.                      (9)

The sign and transpose follow the supplied bilinear convention, not a
Hermitian replacement. Its common singular value does not identify Y,
which pairs triplet matter, with a map between the local PLUS and MINUS
critical traces. That requires a field map, the correct scalar lines,
the action's boundary variation and a physical exterior or end state.
Likewise a scalar value of Y dagger Y does not prove the entire
interacting state has a new U3 gauge symmetry.

The earlier exterior argument already derives propagation of a supplied
Cauchy plane and its response equation. It does not supply its remote
state. Equations (4), (7) and (8) show explicitly why symmetry and the
coupling value (9) cannot be substituted for that missing boundary
normal map in THIS quotient model. They do not prove logical independence
from every possible foundational formulation or from a future complete
generated action. A specified exterior could select a plane and its
compatible grading; no such computation is claimed here.

## Next verification and physical duties

The bounded successor should check the actual fixed-state action,
intertwining frames, all-null-plane/Cayley identities, the Gamma test,
Q8 commutants, projector-path countercontrol and contraction (9).
Those are post-derivation verification duties, not blind predictions.
Their finite checks cannot prove global cone Fredholmness, full E8
reality, supersymmetry closure, or selection of an exterior state.
The frozen eighteen-test proposal predates this result and is unchanged.

P-210 is not closed: what is derived here is the precise candidate
response space and the qualification on its possible chiral indices.
The actual same-action boundary response, its lift/line transport,
stationary background and full charged spectrum remain to be supplied
by derivation and independently verified. No physical-input row is paid.
