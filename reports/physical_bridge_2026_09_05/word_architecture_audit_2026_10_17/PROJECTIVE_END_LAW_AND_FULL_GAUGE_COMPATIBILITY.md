# Projective end laws and the full gauge coefficient

October 20, 2026. Authored conditional analytical audit, pending
independent review. No scientific producer or test was executed.

The candidate projective regularity condition is meaningful for the
specified rank-six coefficient. Applying it to the full interacting
theory requires another step: its puncture element is NOT scalar on
the full E8 adjoint. The existing bosonic action at its flat origin
does not distinguish the extension lattices by their potential value.
A weak-factor compensation can remove the full puncture transport,
but changes the charged coefficient and its gauge background. None
of these facts is a no-go for other coupled backgrounds or end laws.

## Reused source results and scope

The sources read directly for this audit are the complete
[curved action](../weave_curved_action_2026_10_08/PROOF.md), the
[registered embedding](../weave_registered_embedding_2026_10_13/PROOF.md),
the [complete coefficient map](../weave_field_map_2026_10_14/PROOF.md),
and [geometric loop gluing](../surface_geometric_loops_2026_10_14/PROOF.md),
including its inverse-word correction. The coefficient-map producers
and the registered embedding's root/branching construction were read
without importing them. The central equality and the need to retain
weak compensation are PRIOR RESULTS, not discoveries of this note.
The earlier stationary two-field completion also retains an explicit
central quotient and compensator; it is not identified with this flat
control or used to claim its gauge algebra here.

The [projective regularity argument](PROJECTIVE_REGULARITY_AND_RETAINED_LIFT.md)
has residue R=(1/2)I6-P_Lambda and degree d-3. It concerns the actual
extension of a specified flat rank-six connection on a punctured
elliptic fibre. The following audit checks its compatibility with the
retained A5+A2+A1 coefficient and the same supplied classical action.
It neither classifies every generated carrier nor supplies the physical
dictionary to the total higher-dimensional family.

## The zero of the potential does not select the lattice

The source's bosonic potential is the positive residual sum

    g6^2 V = integral dxdy kappa(
      Omega^-1 (|Dbar q|^2+|Dbar r|^2) + 2|[q,r]|^2
      + |F+Omega([q,q dagger]+[r,r dagger])|^2/(2 Omega^2)).

At the original flat connection and q=r=0 every residual vanishes.
The extension lattices E_Lambda change the behaviour admitted at the
missing point, not this flat connection or its potential density on
the punctured region. Thus evaluating V at this origin cannot distinguish
their ranks or derive the projective condition d=0 or 6. The first
variation of a differentiable squared-residual norm also vanishes there.

This does NOT assert that every rank is an admitted domain of the
complete interacting theory. A supersymmetric field space, a physical
end, a nonzero background, an exterior response or quantum effects can
impose additional restrictions. Those restrictions must be derived in
their own terms. Nor is the spectrum independent of the domain: the
fermion Hessian and its closed realization still need that choice.
The zero background is a countercontrol to selection by its classical
potential value, not to all possible selection mechanisms.

## The actual central quotient follows from all charged blocks

Use the source's regular compact subgroup map from
SU6 times SU3_colour times SU2_weak to E8. Its Lie algebra map is
injective; any group kernel is discrete and central. The full branching is

    (35,1,1)+(1,8,1)+(1,1,3)+(20,1,2)
      +(15,bar3,1)+(bar15,3,1)+(6,3,2)+(bar6,bar3,2).

Write a central tuple as (z6^a I6,z3^b I3,(-1)^c I2), where
z6=exp(2 pi i/6) and z3=exp(2 pi i/3). The adjoint blocks impose
no condition. On (20,1,2), the character is (-1)^(a+c), so
c=a modulo 2. On (15,bar3,1), it is z3^(a-b), so b=a modulo 3.
With those conditions the remaining mixed character is

    z6^a z3^b (-1)^c = exp(2 pi i (a+2b+3c)/6)=1.

The conjugate blocks obey the same condition. Faithfulness of the E8
adjoint therefore gives the exact kernel

    K = <(z6 I6,z3 I3,-I2)> = Z6.                  (1)

In particular (-I6,I3,-I2) is trivial in E8, but (-I6,I3,I2)
is not: it acts negatively on (6,3,2) and (20,1,2), positively on
the other blocks. The latter has the same full adjoint action as the
weak centre, as the earlier all-root calculation already established.

Consequently discarding scalar transport in PGL6 does not give a
regular flat full E8 connection over a filled puncture with the original
holonomies. A flat connection on a disc has identity holonomy in its
actual gauge group. Here the original full puncture holonomy is nontrivial.
Curvature, a defect, a retained puncture or a changed full transport
must account for it. The earlier traceless local curvature control is
preserved; this is not a claim that all completions require trace flux.

## An explicit compensation changes the charged coefficient

Let i=diag(i,-i), j=(0,1;-1,0), so i^2=j^2=-I2 and [i,j]=-I2.
In the common source frame set

    U_a = image(I3 tensor i, I3_colour, i_weak),
    U_b = image(I3 tensor j, I3_colour, j_weak).          (2)

The factors commute with each other before taking the quotient.
Their commutator in the product group is (-I6,I3,-I2), which is in
K by (1). Their squares have the same value. Thus U_a,U_b commute
and square to identity in E8. They give a flat E8 representation of
the closed torus group. This is a concrete allowed transport, not a
derivation that the generated architecture chooses it.

The compensation is not a gauge change of the original punctured
representation: it changes its full commutator from nonidentity to
identity. On the mixed block (6,3,2), the old quaternion coefficient
rho times a trivial weak multiplicity becomes rho tensor rho. The
two commuting involutions i tensor i and j tensor j have the four
joint sign characters, each once: each generator and their product
have trace zero on the four-dimensional tensor, and their squares
are identity. In particular its puncture sign is now even. The same
change must be tracked on (20,1,2) and on the weak adjoint itself.

The original weak su2 is not unbroken by (2): a weak generator would
need to commute with both i and j, whose common matrix commutant is
scalar, leaving no weak su2 Lie generator. This statement concerns
THAT weak factor. It does not classify the full common E8 centralizer
or rule out another weak embedding. No algebra is named from a
dimension count.

It is therefore inconsistent to use (2) to remove the full obstruction
and simultaneously retain the old bare-rho theta profile, weak vacuum
and critical mode count without a new field/operator map. The source's
frame-loop compensation is a separate geometric relation: it does not
already impose the new fibre transports in (2).

## What the same action does admit in this control

On a separately specified smooth compact elliptic surface, the flat E8
bundle from (2) and q=r=0 make all the source's residuals vanish.
For admitted differentiable finite-energy variations this is a stationary
zero-potential background, with nonnegative bosonic Hessian and the
source's interactions retained away from the origin. Geometry and this
gauge background are still supplied. No mass gap or unique vacuum is
inferred from positivity.

For its ordinary degree-zero spin problem every unitary flat charged
bundle on that compact elliptic curve has degree zero, hence Dolbeault
Euler characteristic zero. This preserves the closed flat control's
paired index, not the puncture-extension +/-3 result. It is a different
background and domain. It neither negates the noncompact one-form
positive nor supplies a four-dimensional chiral spectrum.

## The next physical derivation is now more specific

A viable end law must state which fields it makes regular and in which
bundle, retain their actual central transitions, and arise from the
same action's admissible variations or an actual exterior response.
Three different operations must remain distinct:

- regularizing the projective connection while retaining a vector lift;
- changing the connection in a smooth cap with its full determinant;
- compensating transport with another physical gauge or spin factor.

The first leaves an integer/sign lift duty, the second requires a
stationary join, and the third changes other fields and their operator.
These are concrete compatibility constraints, not reasons to abandon
the projective route. Deriving a compatible spin/gauge end response
that carries all compensating fields is the remaining task. No complete
physical-input row is paid, no independent acceptance is supplied, and
none of the frozen scientific tests verifies this new analysis.
