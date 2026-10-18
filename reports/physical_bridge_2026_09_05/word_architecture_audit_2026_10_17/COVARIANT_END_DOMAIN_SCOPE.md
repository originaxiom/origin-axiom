# Boundary families depend on the retained state

October 18, 2026. Analytical scope test using the same registered action
as [the matter and boundary proof](MATTER_AND_BOUNDARY_COMMON_REGISTER.md)
and [the coupling transport](REGISTERED_COUPLING_TRANSPORT.md).
[Independent analytical review](MATTER_COUPLING_REVIEW_INTAKE.md) is
recorded separately; no scientific code executed or admission claimed.

A symmetry-preserving law of boundary domains is not necessarily one
domain fixed by every move. The two requirements coincide at a state
fixed by the whole group; elsewhere the relevant constraint is its
stabilizer. In the specified local coefficient model, a field-dependent
rank-three family exists on an open locus, but cannot extend at rank
three to a state fixed by the natural inner lifts, whose local image
is Q8. This proves
both a freedom and a restriction. It does not derive an end law or
declare that every physical state has that stabilizer.

## The state and module being tested

Let W=C^3 tensor C^2 be the raw local boundary module from the
coherent-lift note, with

    A_e(e_p tensor v)=e_(p phi^-1) tensor g v,
    e=(phi,g) in E.

The coordinates used in B1606 are related by the fixed block change
C=diag(j,i,k); a subspace Lambda here is C^-1 Lambda there. The
source parameterizes its chirality-preserving self-adjoint puncture
conditions by subspaces Lambda_+ of this six-dimensional module.
That parametrization and its index formula are supplied analytic inputs;
the producer computes representation data, not an analytic classification
of operator domains. Here the families are candidate coefficient
subspaces under that parametrization, not constructed physical operators.

For the present test, use the specified state base

    X={(tau,S,M): tau in the upper half-plane, S,M in M2(C)},

with the transport

    e(tau,S,M)=(h(e)tau,
               alpha(e) g S g^-1,
               beta(e) g M g^T).

One may take alpha=beta=1 for the tensor transport alone, or
alpha=mu^k, beta=mu^(-2-k), k an integer, for the bilinear compatibility in the
companion note. The latter are unitary characters and are trivial on
every natural J_h. This declares X and its action; it does not derive
X as the complete physical state space. In particular it has no extra
register coordinate on which the natural inner operations act freely.

## The exact orbitwise condition

A covariant domain family satisfies

    Lambda(e x)=A_e Lambda(x).

At a representative x0 of one orbit, this is possible with prescribed
Lambda0 precisely when Lambda0 is invariant under the stabilizer E_x0.
Necessity follows by applying a stabilizer element to x0. For
sufficiency set Lambda(e x0)=A_e Lambda0: two choices e,f differ by
f^-1 e in E_x0, so they give the same subspace.

Thus the classification on an orbit uses the stabilizer of the specified
state, not all of E by default. Continuity between orbits, a differential
operator domain, and a stationary physical background add obligations
that this algebraic classification does not settle.

## An explicit rank three family on an open locus

Use the existing Hermitian metric on the doublet. Define

    H(S)=S S^dagger - (tr(S S^dagger)/2) I2,
    h(S)=sqrt(tr(H(S)^2)/2).

On X_gap, where H(S) is nonzero, it is Hermitian traceless with
eigenvalues +h and -h, h>0. Hence

    P_+(S)=(I2+H(S)/h(S))/2

is a rank-one orthogonal projector. Take

    Lambda_+(tau,S,M)=C^3 tensor image(P_+(S)).      (1)

Its complex dimension is three. For the stated unitary characters,
H(S')=g H(S) g^-1, so P_+(S')=g P_+(S)g^-1.
Permuting the three identical parity factors leaves (1) unchanged.
Consequently

    Lambda_+(e x)=A_e Lambda_+(x)

for every e in E and x in X_gap. This is a real-smooth covariant
family, generally not holomorphic,
not a fixed three-dimensional constituent of the 2+4 representation.
For S=diag(1,0) it selects the first doublet coordinate in each block;
a quaternion rotation carrying that line to the second also changes S,
so it is not required to leave that one domain fixed.

This construction uses S and the supplied metric to make an additional
boundary rule. The rule is not derived from the foundational principle,
a boundary variational problem, or the paper's physical operator. It
is a counterexample to extending the fixed-domain even-rank claim to
every state-dependent covariant family without extra hypotheses. It
does not establish a four-dimensional index for this family, nor may
the source's fixed-domain modular index simply be reused for it.

## A symmetric state obstructs a global rank three extension

At x_*=(tau,I2,epsilon^-1), with any tau, the natural inner lifts
J_a and J_b fix all the specified state data. They fix tau, their
alpha and beta equal one, I2 is fixed by conjugation, and
g epsilon^-1 g^T=epsilon^-1 for g in SL(2,C).

On W these lifts act as

    A_(J_a)=I3 tensor i,    A_(J_b)=I3 tensor j.

Their finite image is Q8. Every invariant complex subspace has even
dimension. One direct proof is that i and j generate the full complex
matrix algebra M2(C) on the second factor. Its submodules in
C^3 tensor C^2 are U tensor C^2 for U a subspace of C^3, of
dimension 2 dim U. Equivalently, the orthogonal projection onto an
invariant subspace commutes with Q8 and has the form P_U tensor I2.

It follows that no E-covariant rank-three family can be defined at x_*
on this X, whether or not it was constructed from H(S). The spectral
gap in (1) closes there; even a discontinuous prescription of another
rank-three subspace would fail the stabilizer condition. A continuous
constant-rank extension to that point is therefore impossible. A
different-rank or singular boundary description would require its own
operator analysis.

This does not exclude a rank-three family on X_gap, extreme domains,
other ranks, or other state spaces. It also does not show that this
symmetric point is selected by any dynamics. The rank-three test and
the even-rank restriction are both conditional on the declared X.

## Why the registering relation still matters

If a further retained coordinate r is acted on by J_a or J_b, those
operations may cease to stabilize the full state (x_*,r), even though
they fix tau,S,M. For example the unreduced E register in the companion
note has a free left action. One cannot apply the Q8 stabilizer proof
to that enlarged state without checking its actual stabilizer. Nor can
one simply add a free coordinate to erase a legitimate physical gauge
constraint. Which data are observable, which are redescription, and
which enter the boundary dynamics must be specified by the programme.

This is the precise connection to the owner's concern. Dropping a
register may strengthen apparent invariance requirements. Retaining it
can remove that particular restriction, but does not by itself choose
a physical domain. The allowed composition law and the physical joining
law remain different duties, now with explicit two-sided controls.

## Source and verification status

At main 2e5716bd9bea013d69f3cd733f083b61a6f59dbd, B1606's complete
verification/puncture_condition.py and the paper's complete
s06_chiral_three.tex were read directly. The existing 2+4 decomposition,
its fixed invariant domains, the separately supplied grading, and the
paper's three distinct uses of an end are preserved. No existing
numerical result is rerun or reclassified by this note.

Independent analytical review is recorded in the linked intake. An executable
successor would need the actual state action, projector identities,
intertwining frames, a deliberately frozen-state negative control,
and the Q8 stabilizer countercontrol. The frozen verification packages
are unchanged. There is no selected extreme domain, cusp unit,
stationary end mechanism, physical chiral spectrum, or input payment.
