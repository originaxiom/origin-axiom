# F15: what the finite linear tests mean

All statements below are algebraic implications, conditional on the
explicit identities/ranks being checked. No rank has yet been observed.

For rho_t(g)=(I+t u_g+O(t^2))rho(g), differentiating a product gives
u_gh=u_g+Ad(rho_g)u_h. Thus a two-generator cocycle is in the kernel
of the adjoint Fox matrix d1. Infinitesimal conjugation has image of
B=(Ad(rho_m)-I,Ad(rho_n)-I)^T (the sign of its parameter is immaterial).
The quotient ker(d1)/im(B) is the infinitesimal deformation space
modulo infinitesimal conjugation. No smoothness or integrability is
inferred from this definition.

Set F(rho)(g)=J^-1 rho(theta(g))^-T J, with J fixed and symmetric.
This is an involution of representations: theta is an automorphism,
contragredient is a homomorphism, and the two commute. At each generator
theta(g)=g^-1, so F(rho)_g=J^-1 rho_g^T J. F14 gives F(rho)=rho.
Differentiating with LEFT logarithmic variations gives

    T(u)_g=Ad(rho_g)(J^-1 u_g^T J).

It is important not to omit Ad(rho_g), or the quotient grading changes.
If C(X)=J^-1 X^T J, direct substitution gives T B = B(-C).
Both involutions square to one. In characteristic zero every invariant
subspace splits into +/- eigenspaces, so

    dim H1_+/- = dim(ker d1 intersect ker(T-/+I))
                - rank(B(I-/+C)).

Explicit quotient columns also certify independence/non-boundaries.
When q varies, J varies. Differentiating F_{J(q)}(rho(q))=rho(q)
introduces an infinitesimal conjugation from J'; consequently the q
tangent is even in the quotient, not necessarily in this fixed gauge.

For a coefficient complex d0(t),d1(t) and a closed class alpha at zero,
alpha+t beta is closed to first order exactly when

    d1(0) beta = -d1'(0) alpha.

Thus its obstruction is d1' alpha in coker(d1). Replacing alpha by a
boundary changes this by an element of im(d1), because differentiation
of d1(t)d0(t)=0 gives d1' d0=-d1 d0'. Conjugating the representation
also produces an isomorphic complex, hence zero obstruction for gauge
directions. These identities are independently checked in the actual
complex. A row computed with a chosen alpha and cokernel basis is only
defined up to nonzero scalars; its kernel and joint ranks are invariant.

For the actual dual family, differentiate rho^-T: delta(rho^-T)=
-rho^-T delta(rho)^T rho^-T. This is not obtained by merely changing
the central phase. The same adjoint deformation coordinate is used for
both sectors. Comparing their obstruction kernels is therefore meaningful.

A nonzero first-order obstruction forbids continuation of that specific
nonzero class to a first-order family. Vanishing does NOT supply a
nonlinear family, constant cohomology, normalizable physical deformation
or a mirror-selective gap. In particular ordinary adjoint H1 is not the
normalizable defining-four matter H1. End asymptotics and F12's global
harmonic existence have not been extended by this calculation.
