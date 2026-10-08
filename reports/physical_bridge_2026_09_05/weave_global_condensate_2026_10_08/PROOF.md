# Global stationary condensate with its actual unbroken algebra

This is an authored conditional construction on the same fixed-metric
classical action as the preceding cusp result. It does not solve Einstein
equations, derive spacetime, or invoke an unproved existence theorem for
nonlinear fields. The fields are built explicitly from bundle connections.

## Spin line and a global nonzero field

Let Sigma be a complete curvature -1 once-punctured elliptic curve, with
finite area2pi. The two ideal triangles in an ideal triangulation each
have area pi. This is also the cusped Gauss--Bonnet limit. Fix an extending
spin line S, S^2=K. In a unitary spin frame write nabla_S=d+i s; the
preceding convention gives ds=-dvol/2. Locally with g=Omega^2|dw|^2,
s_x=partial_y(log Omega)/2, s_y=-partial_x(log Omega)/2.

Sigma retracts to a wedge of two circles. A smooth unitary line bundle
over it is therefore trivial, and S^-1 has a square root L with a
connection whose square is the inverse spin connection. One explicit
construction chooses a unitary trivialization of S, halves the negative
connection one-form, then allows the four flat Z2 choices on the two
circles. These choices are priced; no preferred root follows. This is
a statement on the OPEN surface, not a fourth root of a compactified
log-canonical bundle with an unmentioned integral degree condition.

The SU2 bundle L plus L^-1 has determinant1. In its adjoint the E root
line is Hom(L^-1,L)=L^2=S^-1. Hence the spin-valued field

    qhat=(1/2) identity in S tensor L^2,  rhat=0

is globally defined and covariantly parallel. In local frames it is E/2.
Its Hermitian gauge connection is A_spin=sH/2, with [H,E]=2E. Thus

    F_spin=-H dvol/4,
    [qhat,qhat dagger]=H/4.

Any flat connection C in the compact centralizer of this root SU2 can
be added: A=A_spin+C. It commutes with H,E,F, has zero curvature and
does not change q's covariant parallelism. In every holomorphic spin
frame q=Omega^(1/2)E/2. Substituting the actual local s components gives
Dbar_A q=0; the moment residual is -H/4+H/4=0; r=0 kills the other
two residuals. No field equation is solved only at the puncture.

## The peripheral quarter phase must be compensated

Take x periodic2pi, y>Y at the cusp and orientation dx wedge dy. The
positive x circle is OPPOSITE the oriented boundary of the compact core.
For the line connection Stokes therefore gives the spin-root holonomy

    U_spin(y)=exp(i H Area(core_y)/4)
             =exp(i*pi*H/2) exp(-i*pi*H/(2y)).

Here Area(core_y)=2pi-2pi/y. Its limiting quarter phase is
p0=exp(i*pi*H/2). The spin-line holonomy itself is
exp(-i Area(core_y)/2)=-exp(i*pi/y), agreeing with bounding spin and
the local s_x=-1/(2y). Flat root choices on a,b have trivial commutator
and do not change these limits. Reversing the peripheral circle inverts
EVERY holonomy simultaneously, not just this factor.

The old quaternion p is exp(i*pi*v), where v=e4-e5 in the established
Euclidean E8 root coordinates. The chosen condensate root is
alpha=e4+e6, with alpha.v=1. Their compensating torus logarithm is

    t=v/2-alpha/4,    alpha.t=0,
    p0 exp(2pi i t)=exp(i*pi*v)=p.

This equality is in E8, checked on every root and the Cartan. The adjoint
is faithful. Omitting the quarter phase or giving it the wrong sign fails.
The finite-circle total remains p exp(-i*pi*H/(2y)), exactly the prior
local end; the global construction has not altered that asymptotic operator.

## An explicit color-preserving flat compensator

Let delta=e5+e6 and reflect the entire R91 regular A5+A2+A1 frame in
delta. This Weyl map takes old weak v to alpha and fixes color A2.
The transported A5 commutes with both alpha's root SU2 and color.
The vector t lies in this A5 Cartan. On its defining six weights it
has eigenvalues (+1/4,+1/4,+1/4,-1/4,-1/4,-1/4), after a supplied
Weyl ordering. The fundamental-weight metric and all root differences
are checked to identify this matrix frame faithfully inside E8.

Set zeta8=exp(i*pi/4) and use the following actual SU6 matrices:

    A=diag(zeta8^-1,zeta8,zeta8^3,zeta8,zeta8^-1,zeta8^-3),
    B e_j=e_(j+1) for j=0,...,4;  B e_5=-e_0.

Both are unitary with determinant1. The signs in B are necessary:
the unsigned six-cycle has determinant-1. Conjugation by B cycles the
diagonal of A; its commutator is

    A B A^-1 B^-1=diag(i,i,i,-i,-i,-i)=exp(2pi i t).

Choose the marking of the punctured surface with positive x peripheral
c=[a,b]. Sending a to A and b to B defines a flat SU6 bundle because
pi1(Sigma) is free on these generators. If the inverse peripheral marking
is used, invert the corresponding commutator prescription consistently.
This is an explicit representation, not an invocation of the assertion
that every compact-group element is some commutator.

The commuting root SU2 and SU6 bundles induce an E8 bundle through the
same regular embedding, including its central quotient. No faithful
direct-product identification is assumed. Their separate central minus
identities coincide inside E8, as checked on the whole root system. The
total peripheral is the required p of order2 even though each compensating
factor has order4. A principal E8 bundle over this open surface is trivial;
the relative identification with the old bundle at the end also extends
over the core since pi1(E8)=0. This admits both connections in one bundle,
NOT a gauge equivalence between a curved and a flat connection. Their
a,b holonomies are not asserted equal to the old quaternion matrices.

## Finite norms and stationarity on the complete surface

Use the SAME trace and coupling as before, with n=Tr(E dagger E).
The global Higgs norm is n Area(Sigma)/4=n*pi/2. Curvature, quartic
and curvature-coupling densities are respectively n/16,n/16,-n/8,
times the area density, so each is integrable and their sum vanishes.
The combined covariant gradient is zero. The flat compensator is smooth
on the core and can be locally gauged to zero at the end with its fixed
transition. After the total transition is identified with p, A-A0 is
-H dx/(4y) on the tail and has finite affine kinetic norm. Everything
on the compact core is smooth and has finite norm.

Exhausting cutoffs have derivative bounded and supported in tails of
vanishing L2 mass. They approximate these fields and their first-order
derivatives in the prior graph norms. Products in the residuals are
bounded in orthonormal frames and square-integrable. Thus the constructed
smooth background is in the stated finite-energy configuration class.
All auxiliary residuals vanish globally. For every differentiable finite-
energy variation the first derivative of their norm squares vanishes;
the full bosonic Hessian is their nonnegative linearized norm sum, with
gauge and possible moduli zero directions. This proves classical
stationarity on that specified domain, not quantum stability or a theorem
about arbitrary weak solutions. The metric and R twist remain supplied.

## The actual unbroken compact algebra

A massless four-dimensional gauge generator must be parallel and commute
with q and q dagger. The second condition removes every nontrivial root
SU2 module, leaving its E7 centralizer. Rebuilding the entire248 in the
transported A5+color A2+root A1 frame gives

    (35,1,1)+(1,8,1)+(1,1,3)+(20,1,2)
      +(15,bar3,1)+(bar15,3,1)+(6,3,2)+(bar6,bar3,2).

The required remaining invariant dimensions under A,B are

    6:0,  exterior^2(6):1,  exterior^3(6):0,  su6:0.

The actual matrices, not just their commutator, determine these kernels.
For example B^3 is a nondegenerate skew form preserved by A and B.
The one exterior-square invariant accounts for it; an irreducible six
does not imply an empty exterior-square kernel. The separate reference
follows each monomial basis orbit and accumulates its exact eighth-root
phase, without floating eigenvalues or a random generic element.

Consequently the full unbroken algebra has color weights
8+3+bar3. Its zero-weight space is the two color Cartans. The twelve
nonzero weights are six color roots of norm2 and six fundamental or
antifundamental weights of norm2/3. They form the rank2 G2 root system,
with off-diagonal Cartan entries -1,-3. This is not a dimension14 guess.
Compactness follows from the positive unitary parent. The connected
unbroken compact algebra is g2, not su3 plus su2 plus u1. The global
group's possible disconnected normalizer is not enumerated here.

These parallel generators have finite kinetic integral Area(Sigma)*Tr(X^2)
and nonzero inherited gauge interactions; they are genuine admitted
classical gauge zero directions. The old weak generator does not remain
unbroken. This PARTICULAR holonomy completion is not an SM vacuum.
Other compensators and condensates are not excluded by its algebra.

## What global admission does not repair

The completed background has the same cusp limit as the preceding root
solution. The54 odd root-SU2-centralizer directions still provide escaping
zero-energy channels in each spin slot; compact-core holonomy cannot
remove essential spectrum localized arbitrarily far along the end.
No global finite zero-mode count or anomaly-free chiral spectrum has
been inferred from those channels. The fully coupled fermion operator
and any isolated charged sector require a new computation on this very
background, not the old flat roster or a different branch's index.

The conditional existence advances a supplied classical theory. It
does not select its metric, root, line-root lift or SU6 matrices from
genesis, select three generations, normalize observed parameters,
derive gravity, or establish an observer/qualia mechanism. R39's earlier
global construction is credited rather than rediscovered; this is its
methodological joint with the new spin-valued action and exact p.

Primary geometry context, read directly: Ralph Howard,
https://ralphhoward.github.io/Classes/Spring2020/551/Lecture3/ (Gauss--Bonnet
with oriented boundary terms); Glasgow,
https://www.maths.gla.ac.uk/wws/cabripages/hyperbolic/harea.html (polygon area).
The explicit bundle, holonomy and field-theory argument above is authored,
not attributed to those elementary geometric sources.
