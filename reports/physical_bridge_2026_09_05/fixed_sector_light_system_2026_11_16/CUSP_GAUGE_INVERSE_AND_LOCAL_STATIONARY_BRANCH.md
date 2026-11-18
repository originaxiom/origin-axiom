# Cusp gauge response and a local family of stationary backgrounds

2026-11-16. P-C3e author analytical proof pending independent review.
No scientific producer, CAS, collection, test or numerical integration
ran. The claims below use the literal parallel coherent background,
exact complete cusp, physical source metrics and common fixed sector
already specified. The analytic estimates and their domains are
load-bearing parts of the independent review requested here.

2026-11-18 author clarification: the linear angular drift below has a
bounded weight coefficient, but its radial value grows as exp(t).
It is dominated by the quadratic exp(2t) term, not a bounded radial
perturbation. The literal operator, uniform estimate, kernel/source
premises and lifted-chart argument are written out in
`../harvest_source_support_2026_11_18/CUSP_INVERSE_SOURCE_SUPPORT.md`.
This is existing-proof support pending independent review; no scientific
execution or independent acceptance is implied.

## 1. Use spaces carrying the actual unbroken asymptote

The real gauge operator P_v has its complete nonnegative realization
and finite kernel spanned by the actual parallel Q parameter. Its
inverse off Q exists in the physical vector Hilbert space. To solve
a nonlinear moment equation, a further inverse estimate on regular
bounded fields is required.

Fix k>=2 and 0<alpha<1. C_delta^(k,alpha) denotes real gauge sections
whose exp(delta t)-weighted coefficients and derivatives have bounded
C^(k,alpha) norms in the hyperbolic cusp geometry. One may define
these norms on fixed-radius balls in its local universal cover, with
the prescribed angular transition imposed on the sections. This
keeps the shrinking cusp circle in the estimates. Compact-core norms
use a finite smooth cover. The choices of cut and norm give equivalent
spaces and carry no new physical boundary coefficient.

In an orthonormal gauge frame the background is parallel, so the
finite Higgs potential is parallel and Hermitian. It commutes with
total H and the actual angular transition. On the zero-angular
coefficients P_v therefore reduces to finitely many scalar operators

    ell^-2(-partial_t^2+partial_t)+c, c>=0.              (1)

The only c=0 coefficient is Q. The nonnegative gauge energy requires
every other zero-c coefficient to commute with both triples, their
adjoints and the connection, whose E6 centralizer is precisely Q.
The nonzero angular operators additionally contain their growing
quadratic term, linear angular drift with a bounded weight coefficient
and the same finite parallel Hermitian potential.

The real gauge normalization makes this explicit. Its source form is

    <psi,P_v psi>_v=(1/G) integral {
       |D_x psi|^2+|D_y psi|^2
                +2Omega(|[q0,psi]|^2+|[r0,psi]|^2)} dxdy.

At the D-flat background its compact-real-preserving complex extension
can be written

    P_v=-Omega^-2(D_x^2+D_y^2)+M_g,
    M_g=sum_(z=qhat0,rhat0)
                       (ad_z^dagger ad_z+ad_z ad_z^dagger).

The sum is positive and parallel. Its kernel is the common compact
centralizer Q. For zero angular frequency the squared connection term
adds w^2/(4ell^2) to its eigenvalue. This derives the nonnegative c
and the unique zero coefficient used in (1), with the physical vector
metric and the original factor two retained.

For each c>0 let

    beta_c=(sqrt(1+4ell^2 c)-1)/2>0.

Choose 0<delta<min(1,beta_c over the finite positive list). Define
the gauge domain space

    X_delta={psi=a chi_tail Q+psi_delta,
                   a real, psi_delta in C_delta^(k+2,alpha)},

where chi_tail is one on the far cusp and zero on the compact core.
Restrict to the positive reflection sector. Fix the global gauge kernel
by <v_Q,psi>_v=0. The residual space is

    Y_delta,0={f in C_delta^(k,alpha), <v_Q,f>_v=0}.     (2)

The physical vector inner product is still Omega^2 kappa/G. These
spaces are used to prove regularity of the same operator and its
nonlinear response. The unbroken constant at infinity is included
in X_delta. Its coefficient will be fixed by the global solution.

## 2. The actual gauge inverse maps these spaces

P_v maps X_delta to decaying Y_delta fields. Integration against
the global Q zero mode gives zero. The boundary term vanishes for
the allowed constant Q asymptote and decaying derivatives. Its kernel
in X_delta is the old Q kernel, removed by (2).

For f in Y_delta,0 the physical complete L2 inverse gives a unique
Q-perpendicular psi. It has local elliptic regularity. On the cusp,
the zero-angular homogeneous solutions of (1) have exponents -beta_c
and 1+beta_c. The growing solution is excluded by the actual vector
measure exp(-t)dt. For c=0 only a constant Q term remains, with a
decaying particular solution for the given decaying source.
For c>0 the source variation-of-constants integral and the admitted
decaying homogeneous solution belong to C_delta. The strict choice
of delta avoids resonance with every such homogeneous exponent.

For nonzero angular frequency, the quadratic angular term dominates
the linear exp(t) drift sufficiently far out. The physical L2
solution uses its decaying fundamental solution. The usual scalar
variation-of-constants formula then preserves exp(-delta t) decay
for a source in Y_delta. The finite commuting matrix projections
retain that estimate. A smooth trace at a finite collar controls
the homogeneous coefficients. Derivatives along the shrinking circle
are estimated with the same hyperbolic derivatives used in (2).
Interior Schauder estimates on lifted fixed-radius balls give the
two derivative gain and Hölder control uniformly on the tail. The
compact-core estimates control the trace and the remaining derivatives.

This proves that the physical L2 solution belongs to X_delta. Each
step uses the actual complete realization and angular transition.
The reverse inclusion in its physical domain follows from the finite
area, bounded Q asymptote and decaying derivatives. Thus

    P_v:X_delta intersect Q-perp -> Y_delta,0           (3)

is a continuous linear bijection of Banach spaces. Its inverse is
bounded by the bounded inverse theorem. In particular the asymptotic
constant a is controlled by f and the chosen zero-kernel convention.
It is not supplied as an additional end parameter.

The decay estimate in this argument is a substantive analytic duty.
It requires the source's exact parallel cusp operator and the complete
L2 inverse. A vertical gap or a finite matrix computation alone would
not establish (3).

## 3. Solve the regular nonlinear moment equation

Choose any unit actual form mode p in the charge +1 two-space and
any unit mode r in its charge -1 two-space. Their unit norms use the
original physical chiral metric. They remain explicit state directions.
For real small t and rho near one let

    X_raw(t,rho)=(A0+t(p+rho r),q0,r0).                 (4)

The preceding proof established that this is exactly F-flat. The
profiles in (4) and all fixed-order physical derivatives decay faster
than exp(-delta t_cusp). Here t is an amplitude, while t_cusp denotes
the radial coordinate in the estimates above.

Act on the holomorphic fields by the complexified gauge transformation
g=exp(-psi), with psi in X_delta intersect Q-perp. The physical unitary
connection is reconstructed from its transformed (0,1) coefficient
and its Hermitian conjugate. The spin adjoints and metric are those
of the original action. This changes the physical field configuration.
It is the usual Hermitian-gauge response of the moment equation.
Holomorphic gauge covariance preserves all F equations.

Write m(t,rho,psi)=Omega^-2 mu(g.X_raw) as a real gauge section.
The constant tail aQ commutes with the unperturbed connection and
spin pair. Its action on the decaying charged forms is bounded.
The remaining psi part and its derivatives decay in X_delta. Products,
finite matrix exponentials and the two-derivative moment expression
therefore give a real-analytic map into Y_delta=C_delta^(k,alpha)
near the origin. It has finite physical residual and kinetic norms.

Choose a compactly supported positive bump and form a real section
phi proportional to that bump times v_Q, normalized by
<v_Q,phi>_v=1. Define the bounded projection

    Pi f=f-phi<v_Q,f>_v.                                (5)

Its use preserves decay of the residual. Subtracting a nondecaying
global Q field instead would leave the stated residual space.
At t=0,psi=0, m=0 and

    D_psi(Pi m)=-P_v.                                  (6)

By (3), the real analytic implicit-function theorem gives a unique
small solution psi(t,rho) of Pi m=0 in this kernel convention.
Its first amplitude derivative is zero because p,r are physical
zero modes. Thus psi(t,rho)=O(t^2), and its second coefficient
recovers the actual inverse response of the preceding proof.

## 4. Solve the remaining finite Q moment

The remaining moment is the scalar

    h(t,rho)=<v_Q,m(t,rho,psi(t,rho))>_v.

Both its constant and linear amplitude terms vanish identically
for rho near one. Analyticity therefore permits a removable division
by t^2. The actual normalized charge current fixes its leading term,

    h(t,rho)/t^2=e_Q(1-rho^2)+O(t).                     (7)

Any second-order psi contribution is annihilated by the global Q
moment derivative. Hence the coefficient in (7) includes every
regular field response. Its rho derivative at t=0,rho=1 is -2e_Q,
which is nonzero. A second real analytic implicit-function theorem
gives rho(t)>0 with rho(0)=1 and h(t,rho(t))=0.

Together Pi m=0 and h=0 give the complete moment m=0. Thus

    X(t)=exp[-psi(t,rho(t))].X_raw(t,rho(t))             (8)

is a local convergent family satisfying all the original F and
moment equations in this supplied complete-cusp theory, subject to
the analytic estimate (3). Its global transitions, end frame and
reflection symmetry are the original ones. Every element has bounded
physical profiles and finite energy, with the same complete variation
law. The asymptotic response and norm-balance correction are outputs
of that equation for the specified p,r,t.

Changing the compact bump or kernel convention changes intermediate
coordinates. The physical family is characterized by F=mu=0 and
the chosen state directions. No bump coefficient enters the action.

## 5. Stationarity and physical symmetry of this family

The full internal potential is a sum of residual squares. Equation
(8) makes it zero. Its first variation vanishes for every admitted
variation, including fields outside the consistent reflection and
E6 background sectors. The static external derivatives vanish.
It therefore supplies classical stationary backgrounds of the same
full supplied E8 action at fixed geometry. Its bosonic internal
Hessian is nonnegative, with gauge and moduli directions retained.

The electromagnetic Q gauge generator acts on the first-order form
pair and is Higgsed at generic nonzero amplitude. In the source
canonical convention its vector mass has leading coefficient

    m_Q^2(t)=4 e_Q^2 t^2+O(t^3).                        (9)

Indeed the norm of k_Q on the first-order fields is
e_Q^2 t^2(1+rho(0)^2). The physical vector mass is twice this norm.
That tangent lies in the original harmonic chiral kernel, orthogonal
to real gauge images, so no massive-vector response cancels this
leading coefficient. The neutral gauge profiles and all other
fields must still be transported at higher order. The preserved
colour gauge algebra commutes with the entire construction.

The amplitude, mode directions and their physical realization remain
unselected. These stationary backgrounds change the original connected
U3 phase. They supply an actual permitted charged route for investigating
the common joining problem. A path reaching the specified distant
axis endpoints, its external stationary equations, and the physical
family/reference interpretation require further work.

Independent review must inspect the inverse lemma on the exact cusp,
all angular and constant-tail estimates, analytic mapping spaces,
the two moment projections, both implicit-function uses, global
complete-domain admission and the physical mass normalization.
These are author analytical results with no fresh scientific test pass.
Foundational inputs counted removed remain zero.
