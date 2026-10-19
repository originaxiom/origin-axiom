# Which coefficient-metric freedom survives the actual flat structure?

October 19, 2026. Analytical continuation of
[the full 2+4 calculation](FULL_DOUBLET_QUARTET_AND_NORMALIZATION.md).
It qualifies that note's move-invariant metric freedom by imposing
the coefficient's actual holonomies. This removes a relative weight
in a stated conditional class, without adding a continuous gauge group
or claiming to have derived the physical kinetic theory.
No scientific producer or mathematical test was run; separate review
and scientific admission remain outstanding.

## Keep the coefficient and its local action in one frame

The existing [registered embedding](../weave_registered_embedding_2026_10_13/PROOF.md)
gives the unitary fixed change C=diag(j,i,k) from the parity-twisted
coefficient to three equivalent quaternion doublets. Its underlying
flat holonomies in the common coefficient frame are

    R_a=I3 tensor i, R_b=I3 tensor j.              (1)

The [theta repair](THETA_SEQUENCE_REPAIR_AND_MONODROMY_DUTY.md)
puts the local moves in that SAME frame as

    F_e=O_g tensor g.

Their inner lifts are not (1): F_(J_a)=O_i tensor i and
F_(J_b)=O_j tensor j. A flat fibre holonomy and a registering
operation can have different actions even though they involve
the same quaternion unit. Neither may silently replace the other.

For example, in the original parity frame the holonomies are
C(I3 tensor i)C^-1 and C(I3 tensor j)C^-1; transforming only
the moves and not these matrices would create another false price.
The finite-distance puncture operator's source explicitly assumes
a unitary flat coefficient. Its unitarity and physical interpretation
are hypotheses, not consequences established by this note.

## Constant, fibre-parallel and move-invariant: only one scale

The preceding note finds every constant move-invariant Hermitian
matrix H=h2 P2+h4 P4, with h2,h4>0. Fibre-parallel unitarity
adds the independently required compatibility equations

    R_a^dagger H R_a=H, R_b^dagger H R_b=H.        (2)

Since (1) is unitary in the reference metric, these say H commutes
with the two holonomies. Their quaternion algebra generates M2(C),
so any such H is M tensor I2. Move invariance then requires
M to commute with every O_g. The signed quaternion axis rotations
force M to be diagonal, and the quarter rotations permute the
axes transitively, forcing equal diagonal entries. Therefore

    H=h I6, h>0, hence h2=h4=h.                  (3)

There is also a direct bite check without an irreducibility slogan.
The (j,i) block of P2 is k/3. Its commutator with I3 tensor i
has that block [k,i]/3=2j/3, nonzero. Consequently
[H,R_a]=(h2-h4)[P2,R_a] cannot vanish unless h2=h4.
Unequal sector weights violate (2) in this constant class.

This is a conditional input reduction: an independent doublet/quartet
coefficient ratio is NOT available when both the specified flat
unitarity and constant move invariance are required. No extra SU(6)
invariance, E8 embedding or fitted relation was added to obtain (3).
The scale h remains; it cannot be discarded from normalized
interactions without checking every field and coupling slot.

For the preceding theta injection I_v, the same-class pullback is

    I_v^dagger H I_v=h ||v||^2 I3.               (4)

There is no three-eigenvalue coefficient hierarchy in (4). This
does not determine the integrated profile Gram of a physical field,
which also uses geometry, differential equations and an operator domain.

## This does not make every boundary domain holonomy invariant

Equations (2) follow when a metric is required to be parallel for
the given flat coefficient. They do NOT imply that an arbitrarily
chosen puncture boundary subspace is fixed by R_a,R_b. A domain
at a marked puncture may transform under basepoint transport; being
globally parallel around all fibre loops is an additional property
that must be justified if used.

One could combine the holonomy matrices with the local registering
matrices to produce bare parity operations on the common vector
space. Treating all these as fixed-domain symmetries would change
the boundary classification. The metric calculation does not grant
that authorization. It therefore does not restore the received
report's forced-extreme-domain or three-generation argument.
Unique compatible coefficient norm is not a unique physical domain.

The same commutator also proves that the move-invariant W2,W4
splitting is not a parallel splitting of the original flat fibre
coefficient: its projectors do not commute with R_a. In particular
a constant projector discarding W4 is not a globally parallel
bulk truncation justified by the original connection.

The cubic Psi(f) in the preceding note obeys O_g tensor g when
the doublet f obeys g. For period continuation with g=i this
is O_i tensor i, not the original I3 tensor i in (1). Therefore
the constructive quartet cannot be promoted to a field in that
original bulk coefficient without an additional transition/map
argument. Agreement of their central commutator sign is necessary
but does not identify all holonomies. A different associated
quartet bundle is allowed mathematically; it is not automatically
the same physical field. The source's full-roster quaternion
calculation already keeps quartet-derived multiplicities, and
must not be replaced by an isolated four-dimensional count.

## Allowing modulus dependence changes the question

Keep only fibre-parallelity, and let H(tau) transform covariantly
under the registered moves, rather than require one fixed H for
all tau. From (2), H(tau)=M(tau) tensor I2. Natural inner lifts
fix tau and force M(tau) to commute with O_i and O_j, hence

    H(tau)=diag(h_j(tau),h_i(tau),h_k(tau)) tensor I2,
    h_p(tau)>0.                                 (5)

The move law is

    H(gamma_e tau)=F_e H(tau) F_e^dagger.

Thus the three functions in (5) are permuted under the modular
generators. This does not force them to be equal at a generic tau.
A metric parallel on the entire universal family is a stronger
condition than fibre-parallelity and would require its actual
connection in the tau directions as well.

At tau=i, s fixes tau and exchanges the i,j axes, so h_i=h_j.
At omega=(-1+i sqrt(3))/2, s l fixes tau and cycles all three
axes; thus all h_p agree there. These are stabilizer constraints,
not a derivation that the physical background sits at omega.

For an explicit positive nonconstant family, use the scalar theta
laws read directly in [DLMF 20.7.27--33](https://dlmf.nist.gov/20.7#viii).
In axis order (j,i,k), with y=Im(tau), put

    a_j=y |theta_4(0|tau)|^4,
    a_i=y |theta_2(0|tau)|^4,
    a_k=y |theta_3(0|tau)|^4,
    b_p=3 a_p/(a_j+a_i+a_k).

The theta constants have no zeros on the upper half-plane by
their products, so b_p>0 and their sum is three. Under l they
exchange j,k; under s they exchange i,j: y's transformation
cancels the theta constants' absolute modular factor. Thus

    h_p^(t)(tau)=h [(1-t)+t b_p(tau)], 0<=t<1,    (6)

obeys the full move covariance and fibre-parallelity assumptions,
and is uniformly bounded below by h(1-t). Natural inner actions
are diagonal on the axis factor, so impose no further condition.
These are the same coefficient and operation matrices, not a
different representation introduced to evade (3).

For t>0 the tensor is not constant: as y tends to infinity,
b_i tends to zero and b_j,b_k to 3/2. This proves that the
weaker family conditions do not force (3) globally. The parameter
t is an example of residual freedom, not a selected physical coupling.

## Do not mistake frame freedom for a new physical parameter

Distinct tensors in the displayed frame are not automatically
physically inequivalent theories. A field redefinition by H^(1/2)
can make the coefficient metric the identity. But derivatives in
tau then acquire the corresponding connection term, and physical
interaction tensors and operator domains must be transformed too.
For an operator D=d+A and field psi'=G psi, its expression is

    D'=G D G^-1=d+G A G^-1-(dG)G^-1.

If all those data are transported, this may be an equivalent
description. If a claimed fixed parent forbids the new connection
or changes the normalized interactions, it may instead be a
genuine change of model. This note does not decide equivalence
without that parent. Moving a metric choice into a connection
is not by itself earning or adding a physical-input ledger row.

## Input verdict and next physical duty

Forced in the constant fibre-parallel, move-invariant class:
the coefficient metric is scalar; no independent h2/h4 survives.
Allowed under weaker fibre-parallel family covariance:
nonconstant positive metrics such as (6), with stabilizer constraints.
Not established: a physical choice between those conditions,
the profile integrals, an end response or a boundary-domain selection.

The next same-parent audit must identify what connection and
coefficient metric its action actually uses, and whether its
end response inherits a parallel coefficient norm or a profile
Gram. Only then can a physical normalization input be removed
rather than renamed or double-counted. The compact silver
rank-five and weave rank-six coefficient maps remain distinct.

This is analytical progress toward reducing supplied inputs,
not a completed physical ledger payment or an SM prediction.
Separate review is pending. Frozen v2/v3 are unchanged; no new
scientific execution or publication pass is asserted.
