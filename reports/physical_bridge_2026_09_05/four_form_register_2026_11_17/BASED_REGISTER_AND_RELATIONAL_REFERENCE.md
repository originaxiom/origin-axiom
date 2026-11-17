# An explicit register map and its measuring-reference duty

2026-11-17. PHYSICAL-C7 continuation scoped at 76c167a31. Author hand
derivation pending independent review. No scientific code, CAS or test
ran. The native register comparator is the previously constructed
based family Hom(F(a,b),SU2)=SU2 x SU2. Choosing SU2 as a physical
coefficient category remains a premise of that comparator.

## 1. Test the direct identification before using it

Choose ordered orthonormal frames in the two form coefficient spaces
and a matrix convention for the native SU2 target. These frame choices
are part of this proposed dictionary. A unit sphere is an SU2 torsor;
identifying it with the group requires an origin. No native choice of
those origins is inferred from the Hermitian norm alone.

For a unit vector u=(u_1,u_2) in the chosen frame define

    U(u)=[[u_1,-bar u_2],[u_2,bar u_1]] in SU2.

This is a bijection S^3->SU2. With D_phi=diag(exp(i phi),exp(-i phi)),

    U(exp(i phi)u)=U(u) D_phi.                         (1)

Thus the total space of the four-form direction bundle has the same
underlying manifold as the native based unitary representation family.
Under the actual effective Q gauge action it transforms as

    (A,B)=(U(u),U(v))
            ->(A D_phi,B D_phi^-1).                  (2)

This is not simultaneous conjugation of the native generator matrices.
It need not preserve their commutator trace.

For an explicit hand discriminator use the unit quaternions A=i,
B=j and D_phi=cos(phi)+i sin(phi). The transformed matrices represent

    A_phi=-sin(phi)+i cos(phi),
    B_phi=j cos(phi)+k sin(phi).

Their imaginary axes are orthogonal, and quaternion multiplication gives

    tr[A_phi,B_phi]=2-4 cos^2(phi).                    (3)

At phi=0 it is -2. At phi=pi/2 the first generator is -1, the second
is k, and the commutator trace is 2. All those pairs are the same
four-form coefficient quotient point because their matrix Z=u v^t
is unchanged. In the native based register they have different
conjugacy-invariant data. Here kappa always means the free-generator
fibre commutator trace, with no identification to a knot-meridian trace.

Consequently the direct matrix assignment (A,B) cannot descend to a
native-register map on the gauge quotient while preserving that datum.
This is a counterexample to one explicit map. Other maps, larger field
families and a register retaining its reference remain open.

## 2. A charged reference restores the based pair kinematically

Retain a unit phase zeta transforming with effective charge +1,

    zeta -> exp(i phi) zeta,
    D(zeta)=diag(zeta,zeta^-1).

Define the relational matrices

    A_reg=A D(zeta)^-1,
    B_reg=B D(zeta).                                  (4)

Equations (1)-(2) show that both matrices are gauge invariant when
the reference is carried with them. In vector coordinates they are
the matrices of zeta^-1 u and zeta v. In fact

    [(S^3 x S^3) x U1]/U1 -> SU2 x SU2,
    [(u,v,zeta)] -> (A_reg,B_reg)                     (5)

is a bijection with smooth inverse, obtained by the representative
zeta=1. The action in the quotient of (5) transforms all three entries.
Every word w(a,b) can be evaluated on (4), with its order retained.
This is an explicit kinematic field/reference map for the based pair.
It supplies no action for the reference or realization of every
additional central lift in the full registering group.

The reference enlarges the relational state space. At fixed nonzero
amplitude its quotient has six real dimensions; the coefficient
quotient without that reference has five. The additional relative
information is precisely what the direct assignment had lost.

## 3. A global fixed phase is obstructed by the derived curvature

An equivariant function zeta from the original principal circle
bundle to U1 would choose such a reference over every coefficient
quotient point. It would trivialize that bundle. C7's primitive sphere
has c_1=1, so no such global fixed phase exists over it.

A reference can be kept as part of the joint state, described in
patches, or carried by a charged section with zeros. Those possibilities
need the corresponding physical source and variation law. A physical
charged section that is nowhere zero on that entire sphere would
contradict the nonzero first Chern class. This topological observation
does not forbid local measuring states or a full relational bundle.

A larger reference is a compatible alternative. Over this sphere the
associated doublet L direct-sum L^-1 has trivial determinant and
transition diag(exp(i varphi),exp(-i varphi)). That loop is contractible
in SU2, so the doublet admits a global unitary frame there. This removes
the particular single-phase obstruction on that sphere. It leaves
the choice of frame, its action and its relation to the existing
flavour/measuring fields to be derived. The existing quaternion flavour
doublet is Q-neutral; assigning it these opposite Q characters would
be an additional identification requiring a map. No extension of this
local topological observation to the whole parameter family is assumed.

## 4. Keeping the reference also requires its kinetic response

For a simple local comparator let zeta=exp(i chi) be a physical phase
with positive kinetic weight nu^2. Add its covariant kinetic term to
the original four-mode term

    nu^2 (d chi-b)^2.

If J and N denote the original Gauss numerator and denominator, the
combined real Gauss equation now fixes

    b=[J+nu^2 d chi]/[N+nu^2].                        (6)

Completing that same quadratic yields the exact reduced kinetic term
in this comparator

    g_quot + [N nu^2/(N+nu^2)] (d chi-A)^2.            (6a)

The relative register direction is positive when N and nu^2 are
positive. Its weight approaches zero as the reference amplitude goes
to zero and approaches N in the stiff-reference limit. On the balanced
branch N=2t^2, so the ratio nu^2/(2t^2) remains an actual dimensionless
state datum until a common field/source law determines it.

Its response depends on the measuring-sector weight. If that phase
is merely adjoined with zero kinetic term, varying only its relative
value costs zero energy in the joint-state quotient. The resulting
metric is degenerate in the restored direction. A positive dynamical
register needs its actual response, or an explicitly external source
law with restricted variations. Calling the phase a reference does
not determine nu or its action.

Equation (6) is a diagnostic for a possible completion. It is not an
extra field inserted into the current physical model. A proposed
completion should identify an existing source or derive the reference
sector before using its metric to fix physical transport.

## 5. The existing charged spin mode has a nontrivial compatibility test

The odd/aligned source already contains a charge +1 spin mode S.
Its canonical kinetic metric would supply a phase weight |S|^2 if it
were used locally as a measuring reference. The actual complete light
cubic, however, is

    W_3=y A S T+lambda_+ N_c P_c T
                                  +lambda_- N_d R_c S,
    lambda_+ != 0, lambda_- != 0.                     (7)

Its projected F_Nd equation includes lambda_- R_c S. For a small
family whose R_c and S both have nonzero coefficients at first order,
that term is a nonzero quadratic zero-mode projection. A second-order
heavy correction cannot cancel it, by the original dual-zero-mode
argument. Thus such a reference cannot be added with arbitrary first-
order value over the generic R_c direction while keeping the tested
F-flat branch. The charge -1 spin mode T has the counterpart P_c T.

Special form directions, higher-order induced values and larger
coupled stationary families retain their own equations. This test
does not exclude those alternatives. It shows why using an already
present field as a reference requires the real interaction tensor,
rather than its charge and dimension alone. The topological patch
and zero requirements above still accompany any global use.

## 6. Native word moves require the geometry and metric to travel

In the relational pair coordinates, consider the Nielsen shear

    (A_reg,B_reg)->(A_reg,A_reg B_reg).

At the trivial representation (I,I), its derivative is

    (X,Y)->(X,X+Y), X,Y in su2.                       (8)

It preserves no positive-definite metric on this entire tangent
space. Its n-th power sends (X,0) to (X,nX), whose norm in any
positive-definite metric grows without bound for X!=0. An isometry
at a fixed point would preserve that norm under every power. In
particular it does not preserve the product round metric inherited
by the two coefficient vectors with a fixed reference.

This scopes a limitation of a fixed-background identification. The
original physical construction already carries a marked surface,
its conformal parameter, spin/core data and kinetic Grams under
word-induced geometric changes. Moving those data can give covariance
without an invariant metric on one fixed coefficient fibre. They
must be included in any proposed map of the full registering action.
The two-quaternion manifold and its Haar measure alone do not supply
that physical kinetic construction.

There is an existing positive recovery control. Section 4 of
WILSON_FAMILY_KERNEL_AND_LEVEL_FOUR_REGISTER_MAP.md already proves
covariance of the period metric |dq-tau dp|^2/Im(tau). Tensoring the
same quadratic form with the positive su2 norm gives at the linear
register level

    G_tau(X,Y)=||Y-tau X||^2/Im(tau).

Under tau'=tau+1 and (X',Y')=(X,X+Y), its numerator and denominator
are unchanged. The moving geometry resolves the fixed-point metric
obstruction for this linear comparator. This reuses the earlier Hodge
geometry; it does not fix tau or establish the nonlinear four-form
operator map. The fixed-peripheral complete-cusp admissibility must
also accompany any physical variation of those native holonomies.

## 7. The next earning condition is now explicit

The full charged-form construction gives a source-derived connection
and an explicit candidate register map when a reference is retained.
For that reference completion, derive how the reference is represented
by the existing registering architecture, what metric
and interactions it carries, how its centre is lifted, and how native
word moves transport the geometry, field operator and measuring data.
The coefficient-to-group frame assignment must be transported or
derived as part of that dictionary.

The local kinematic map (4)-(5), its global phase obstruction and the
interaction test (7) give concrete compatibility questions. They leave
the register present throughout the physical construction. They do
not derive a preferred history, a physical end unit or a three-family
chiral spectrum by matching the two S^3 factors.

The companion INTERNAL_COMPOSITE_REGISTER_AND_WORD_ACTION.md supplies
a different lossless angular map using the existing fields. It
demonstrates that an added reference field is not a necessary
consequence of the failed direct pair dictionary. That alternative
has its own explicit group relation, native-action, radial-angle and
vertex duties. The full registering architecture can test both routes.
