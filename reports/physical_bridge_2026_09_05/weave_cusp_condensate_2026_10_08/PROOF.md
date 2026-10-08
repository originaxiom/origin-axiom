# Local end solution and a changed asymptotic operator

Conditional on the supplied curved action at bb6c80767. This is an
authored analytic construction with finite exact checks, not an external
existence theorem for a global compactification. All fields and Yukawas
of that action are retained; only the background is changed.

## 1. A nonzero solution of all local vacuum equations

Use the cusp w=x+iy, x in R/(2pi Z), y>Y>0, metric
ds^2=(dx^2+dy^2)/y^2. Its scalar curvature is -2. Let E,F=E dagger,H
be a compact root sl2 triple: [H,E]=2E, [E,F]=H. Normalize the positive
invariant trace by n=Tr(E dagger E), so Tr(H^2)=2n. Set

    A_x=-H/(4y), A_y=0, q=E/(2sqrt(y)), r=0.
    qhat=Omega^(-1/2)q=E/2, Omega=1/y.

For the more general real-amplitude ansatz A_x=hH/y,q=cE/sqrt(y),
the exact residuals of the preceding action are

    Dbar_A q=-i c(1/2+2h)E/y^(3/2),
    F_xy=hH/y^2,
    F_xy/Omega^2+[qhat,qhat dagger]=(h+c^2)H,
    Dbar_A r=[q,r]=0.

Thus the nonzero branch has h=-1/4,c^2=1/4; an arbitrary constant
phase is removable in this local sl2 ansatz. The zero branch has h=c=0.
The nonzero solution is not normal: its Higgs commutator is H/4, canceled
by actual nonzero curvature. Removing A is not a gauge change and fails
both equations. The value c is in units of the SUPPLIED curvature radius;
this has not determined a measured Higgs scale.

Every residual of the nonnegative local potential is zero. For smooth
compactly supported variations on this end the first variation vanishes
and its full bosonic quadratic form is the sum of the linearized residual
norms. This is local stationarity and nonnegative Hessian, not a choice
of boundary condition at y=Y or a proof of existence on the core.

The unitary spin connection is s_x=-1/(2y),s_y=0, with
nabla=partial+i s-i ad A. It makes qhat covariantly parallel. The
expanded physical energy densities balance as

    (1/2)|F_xy/Omega^2|^2 = n/16,
    (1/2)|[qhat,qhat dagger]|^2 = n/16,
    (R_scalar/4)|qhat|^2 = -n/8.

Their sum is zero; the rough covariant gradient and its associated
surface current vanish for this parallel profile. No negative term
alone is used as a stability test.

## 2. The same end domain, not the same flat connection

Let p be the old quaternion peripheral element. For a p-odd root,
Ad(p)E=-E and Ad(p)H=H. Bounding spin contributes the other minus sign,
so the displayed spin coefficient is periodic in the combined bundle.
A_x also descends. The adjoint holonomy on a finite horizontal circle
is p exp(-i pi H/(2y)); it tends to p but is generally not equal to p.
The background is a curved connection on the same local bundle, not a
new flat representation with all old a,b Wilson matrices unchanged.

With the preceding kinetic metric, its end norms are

    ||q||^2 = integral Omega Tr(q dagger q) dxdy = n pi/(2Y),
    ||A-A0||^2 = (1/2)integral Tr(A_x^2) dxdy = n pi/(8Y),

in the flat-end trivialization A0=0 with transition p. Baseline Dirac
derivatives of q and exterior derivatives of A are also square-integrable:
their orthonormal coefficients are bounded and cusp volume is finite.
Commutator residuals separately have finite norms. Smooth cutoffs with
bounded gradient, moved to t=log(y) going to infinity, have errors
bounded by a constant times the L2 tail; hence this profile belongs to
the graph closure AT THE END. This argument makes no assertion about
the finite interface y=Y or a global nonlinear weak-solution theorem.

Under z=exp(iw), the holomorphic-frame coefficient transforms as
q_z=constant*z^(-1/2)(log(1/|z|))^(-1/2)E. The flat critical solution
z^(-1/2) has divergent norm integral dy/y. The present coefficient has
norm integral dy/y^2. The extra logarithm follows from the nonflat
coupled equations, not from changing the kinetic measure. An exclusion
for a flat holomorphic coefficient does not exclude this new solution.

## 3. An exact block of the actual bosonic Hessian

At r=0 the R fluctuation has no linear contribution to the moment map.
It therefore decouples from delta q and delta A at quadratic order:

    V_R^(2)=integral dxdy [Omega^(-1)|Dbar_A delta r|^2
                             +2|[q,delta r]|^2].

All other blocks and interactions remain in the theory. This block alone
is not the full fermion mass matrix. For a root sl2 irreducible spin j,
write H weight2m and physical spin coefficient phi=sqrt(y)delta r.
The zero-angular channel has kinetic measure e^(-t)dt, t=log y.
The unitary radial transformation is phi=e^(t/2)u. Direct substitution
gives

    V_R^(2)=integral dt [|u'+(m/2)u|^2+(1/2)|E u|^2],
    E dagger E=(j-m)(j+m+1).

For compactly supported u the derivative cross term integrates to zero.
The half-line essential spectrum of this constant-coefficient channel
begins at

    mu^2(j,m)=m^2/4+(j-m)(j+m+1)/2.

This statement concerns the Friedrichs realization of the quadratic form;
any regular self-adjoint change at the finite end leaves the essential
threshold unchanged, but can change discrete bound states. A normalized
escaping bump has Rayleigh quotient mu^2+10/L^2; smoothing the piecewise
polynomial bump gives form-domain Weyl sequences. This is a form quotient,
not a mislabeled norm of a second-order operator residual. The constant
coefficient half-line calculation also gives the full interval
[mu^2,infinity). Nonzero angular frequency contributes a growing n^2 y^2
term (with lower-order y terms), so those channels are confining at this end.

For j=1/2, m=+/-1/2 the thresholds are1/16 and9/16; for j=1 they
are1/4,1,5/4 in descending m order. Spin0 retains zero. The coefficient
1/2 is inherited from the same action, not a inserted adjustable mass.

## 4. The actual E8 peripheral element, not a dimension match

In R91's Euclidean E8 root coordinates the A5 simple roots are
e7-e8,e6-e7,e7+e8,-(e1+...+e8)/2,e4+e5. Color is generated by
e1-e2,e2-e3 and weak SU2 by v=e4-e5. The SU6 central minus identity
is p=exp(i pi h), where

    h=a1+2a2+3a3+4a4+5a5=(-2,-2,-2,3,3,0,0,0).

For every E8 root beta, beta.(h-v) is even: (h-v)/2 is the integer
E8-lattice vector(-1,-1,-1,1,2,0,0,0). Thus p and exp(i pi v) act
identically on every root and the Cartan. The E8 adjoint is faithful,
so these are the SAME group element. The implementation also checks
the A5 Cartan matrix and commuting color/weak factors. It does not
identify the full SU6 action with the weak SU2 action.

The explicit alpha=e4+e6 is p-odd, commutes with color, and has weak
weight1. Its condensate breaks the original weak SU2. No physical
hypercharge is assigned: the old SU5 generator does not automatically
commute with the full quaternion background. Calling this the measured
electroweak Higgs would require the actual global gauge and charge map.

For each of the112 p-odd root choices the adjoint sl2 decomposition is
133 spin0 copies,56 spin1/2 copies and one spin1 copy. Its sl2 centralizer
has126 root spaces and7 Cartans;54 of its root spaces are p-odd. Within
the112 odd root spaces,54 have(j,m)=(0,0),28 have(1/2,1/2),28 have
(1/2,-1/2), and one each has(1,1),(1,-1). Hence the R zero-angular
channel histogram of squared thresholds is

    0:54; 1/16:28; 9/16:28; 1/4:1; 5/4:1.

This lifts58 of112 R channels. They are NOT58 massive particles. Both
spin fermion slots have free asymptotic operator on the54 odd sl2
centralizer directions: all background Yukawa commutators vanish there,
and the spin/p transition is periodic. Thus108 spin-slot channels
remain gapless; an escaping sequence needs only this end, not knowledge
of a global kernel. Any global extension with these exact asymptotics
still has this continuum. No full gap is claimed for this ROOT class.

## 5. What has and has not advanced

The positive is a local nonlinear end solution in one already specified
interacting action, with finite kinetic/graph norms and a calculated
change in part of its actual spectrum. This is stronger than inserting
a mass comparator, and weaker than a global physical chiral construction.
Core matching and bundle extension, full coupled fermion spectrum,
retained gauge symmetry/charges, anomaly accounting and generated
selection are subsequent obligations. Higher nilpotent embeddings,
simultaneous Q/R backgrounds and other end laws are NOT excluded.
The observer/registering relation and qualia have not been derived by
interpreting this condensate; those foundational obligations remain.

Literature context: Hitchin, Spinor-valued Higgs fields,
https://arxiv.org/abs/2404.12981v1, studies adjoint spinor Higgs fields,
including compact-bundle Dirac kernels and nilpotent extensions. Its
compact index statements do not establish this complete-cusp result.
Xie--Yonekura, https://arxiv.org/abs/1310.0467v2, equation2.1, displays
the generalized Hitchin system with L1 tensor L2=K. Their M5/(2,0)
physical parent is not the (1,1) Yang--Mills parent used here. Neither
source is credited with the authored construction or an OA-to-SM theorem.
