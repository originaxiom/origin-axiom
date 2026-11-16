# A source-operator test for the actual affine joining path

2026-11-16. PHYSICAL-C5 author continuation of SAME_ACTION_END_RESPONSE.md,
pending independent review. No scientific script or test ran. This gives
an explicit operator target for the full bosonic joining problem in the
supplied physical parent.

## 1. Keep the original four residual slots and both metrics

Use the same fixed internal geometry, compact-real fields and smooth
bundle identifications as P-C3b. Package the parent potential as

    V(X)=||R(X)||_res^2,

    R(X)=(Omega^-1/2 Dbar_A q,
          Omega^-1/2 Dbar_A r,
          sqrt(2) [q,r],
          mu/(sqrt(2) Omega)),
    mu=F_A+Omega([q,q^dagger]+[r,r^dagger]).            (1)

The first two complex derivative residuals, the complex commutator and
the real moment are the source residuals with their original weights.
The residual norm integrates kappa/G against dxdy. The field norm used
for gradients, real Gauss and orthogonality is the physical chiral norm,
with its connection factor 1/2 and spin factor Omega. Confusing these
two metrics changes the adjoint below.

Write Y=(a_x,a_y,u,v), a=a_x+i a_y. At X=(A,q,r) the real derivative is

    D R_X Y=(
       Omega^-1/2 (Dbar_A u-i[a,q]),
       Omega^-1/2 (Dbar_A v-i[a,r]),
       sqrt(2) ([u,r]+[q,v]),
       [D_x a_y-D_y a_x
          +Omega([u,q^dagger]+[q,u^dagger]
                         +[v,r^dagger]+[r,v^dagger])]
                                             /(sqrt(2) Omega)).     (2)

All dagger terms are retained because the full physical variation is
real. Define (D R_X)^* using the real part of the residual pairing and
the physical field metric on the admitted complete domains. Then

    grad V(X)=2 (D R_X)^* R(X).                        (3)

Boundary contributions in (3) must vanish under the existing complete
variation law or be retained in the actual source/end response. No
finite-radius boundary condition is added by writing this adjoint.

## 2. Reduce the full stationary test to an identity along the curve

The old affine proof gives a fixed residual vector C such that

    R(X_s)=s(1-s) C, B=||C||_res^2,
    V(X_s)=B s^2(1-s)^2.                              (4)

This fixed C uses the old common bundle frame. An s-dependent unitary
frame change must transport R, C, the derivative, adjoints and measuring
metric together. The quotient statement below uses their common frame.

Let v_s be the real horizontal tangent after solving the old Gauss
equation. Put K(s)=||v_s||_c^2 and
II_s=P_perp nabla_s v_s on a smooth regular segment. The exact normal
bosonic equation from SAME_ACTION_END_RESPONSE.md becomes

    P_perp (D R_(X_s))^* C
          =[B s(1-s)/K(s)] II_s, 0<s<1.              (5)

To derive it, substitute (3)–(4) and the scalar first integral
K(s)(s')^2=B s^2(1-s)^2 into the full normal residual, then divide
by 2s(1-s). Thus (5) is independent of the wall position coordinate.
It compares two actual functions of s on the internal carrier.

If the scalar wall exists, the curve stays in one regular gauge slice,
its endpoint data are allowed, and (5) holds in the actual dual domains,
then the full bosonic Euler equation along that curve holds. The real
Gauss equation is already included. If (5) fails, this affine path needs
a transverse deformation or different endpoint/source dynamics. Such
a failure is scoped to that path. It does not exclude the parent theory
or another stationary joining.

At gauge enhancement the smooth-quotient derivation requires its own
continuation. At B=0 one uses the unreduced normal equation directly.
Neither division by K nor the positive-barrier wall argument applies
at a vanishing horizontal tangent.

## 3. A small rejecting example checks what the test detects

Consider a two-real-field comparator with flat kinetic metric and

    R(x,y)=(sqrt(b) x(1-x), y-c x(1-x)), b>0, c!=0.

Both endpoints (0,0) and (1,0) have zero potential. The straight path
y=0 has K=1 and V=(b+c^2)x^2(1-x)^2. Its scalar equation has the usual
logistic wall and a finite positive tension. But its normal curvature
II is zero, whereas

    partial_y V at y=0=-2c x(1-x).

Therefore its full normal residual is nonzero throughout the interior.
This hand comparator demonstrates exactly how a correct scalar wall
can fail the parent field equations, even for a positive residual-square
action with correct zero-potential endpoints. A full stationary solution
may leave the straight path. The comparison preserves that possibility.

## 4. What a concrete completion must now supply

Choose and state one actual smooth core bundle identification and the
two allowed endpoint field configurations. This fixes a,u,v and hence
C in (4), including the tail and core. Solve L_s alpha_s=b_s with the
physical vector metric and its kernel convention. Compute the two
sides of (5) with the complete source adjoints. Keep a failed residual
before trying a transverse correction.

The former existence argument for a smooth identification does not
select one or calculate these source profiles. The resulting path
choice is an explicit construction datum. A justified source law may
ultimately select or restrict it. That law still needs its foundational
and physical derivation.

Equation (5) turns the next task into a specific same-action operator
calculation. It removes the need to guess a wall potential for that
chosen path. Independent source/domain review and a controlled solution
remain necessary before a physical joining result can be banked.
