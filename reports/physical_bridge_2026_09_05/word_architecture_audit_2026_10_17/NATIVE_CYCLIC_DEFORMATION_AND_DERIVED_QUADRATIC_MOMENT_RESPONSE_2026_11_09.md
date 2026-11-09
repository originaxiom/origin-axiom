# A small native cyclic stationary family and its moment response

2026-11-09. AUTHOR ANALYTICAL DERIVATION, UNREVIEWED AND UNRUN.
Source baseline be1b2e92e64eb488870ec1b27a3b0841fd026845.
The calculation uses the supplied balanced curved E8 parent, its complete
punctured-elliptic end, physical metrics and two Spin5 factors. The
profile and vacuum-selection questions retain their open evidence grades.

## Scope and inherited data

The paired-current report gives two tree-level charged-vector witnesses
at the same mass. NEXT_PROBE_NATIVE_NEUTRAL_FIELDS_AND_MOMENT_RESPONSE
locates neutral cyclic spin fields among the existing D5 adjoint fields.
Here the concrete task is their actual moment response and the terms
it contributes to the physical vector operator.

Use the curved parent, physical mass proof, real gauge-fixing proof and
two-triple decomposition. TWO_SPIN_FIELD_MOMENT_ORBIT_UNIQUENESS gives
the existing bounded Hermitian-orbit framework. Its uniqueness statement
and the existence problem have separate hypotheses. REDUCTION_CARD_03
already treats native neutral fields in a different stationary family.
Its old state amplitudes and charged counts remain tied to that family.

Write qhat,rhat for orthonormal spin coefficients and

    muhat=F_A/dvol+[qhat,qhat†]+[rhat,rhat†].

The balanced source has muhat=0 and
qhat=E_+/(2ell), rhat=E_-/(2ell) in the unitary flavour coordinates.
All brackets and adjoints below use the source positive trace metric.

## 1. The moment equation combines the scalar and curvature insertions

For a gauge profile epsilon, the action fixes

    Pv=Dbar^{*v}Dbar
            +2 ad_qhat† ad_qhat+2 ad_rhat† ad_rhat.        (1)

The conformal scalar/gauge norm gives

    Dbar^{*v}Dbar=nabla* nabla-ad(F_A/dvol).

At a moment-flat configuration, the Lie identity
ad_[qhat,qhat†]=[ad_qhat,ad_qhat†] therefore yields

    Pv=nabla* nabla
            +{ad_qhat,ad_qhat†}+{ad_rhat,ad_rhat†}.        (2)

This uses precisely the relative coefficient2 in(1). Curvature and
the two orderings of the spin-field insertion are fixed by the common
action. The formula holds on compact-support cores and extends through
the physical closed quadratic forms when their boundedness and domain
conditions hold. It supplies a check on any proposed stationary deformation.

## 2. Explicit local spinor matrices expose the leading terms

In a principal Spin5 spinor four, use orthonormal weights ordered
3/2,1/2,-1/2,-3/2. Let e_ij denote matrix units. The actual principal
raising matrix has the representation

    E=sqrt(3)e_12+2e_23+sqrt(3)e_34,
    H=diag(3,1,-1,-3).

The grade-minus-three adjoint root acts as X=c e_41, for a fixed
nonzero source normalization c. Keeping c explicit suffices for the
following products. A cyclic spin coefficient aE+t fX has

    E†X=X†E=0,
    X†X=|c|^2 e_11,
    XX†=|c|^2 e_44.                                    (3)

The first relation also follows from weight range, since either cross
term would change the principal weight by four. Both chiral Spin10
modules restrict to4 tensor4 under the two Spin5 factors, so the
corresponding first-order Higgs insertion vanishes on each whole
charge-one spinor module. Functions f may vary over the surface.
The vector mass term contains their pointwise products.

For a path with this Higgs tangent and A'(0)=0, the derivative of Pv
on the charge-one blocks is consequently zero. Any stationary branch
with this prescribed tangent requires a second-order mass calculation.
At a fixed connection, its direct quadratic term would instead act
on the highest weight through2|t f c|^2 e_11. Formula(2) shows that
the moment-induced curvature term adds
|t f c|^2(e_44-e_11). Their combined zero-order insertion is

    |t f c|^2(e_11+e_44).                               (4)

The rough connection Laplacian and any further field response also
vary. Equation(4) fixes one part of the calculation. A full mass shift
requires all those terms and the complete degenerate eigenspace.

## 3. State the global deformation hypothesis

Fix actual smooth global holomorphic spin sections u',v' supported
on the lowest grade-minus-three adjoint roots in the plus and minus
Spin5 factors, respectively. Require their source graph and quartic
norms, bounded physical coefficients, and the decaying S^4 cusp
profiles described in the exploratory construction. Their global
transition/section construction remains a separate review duty.

The two factors commute. Their extreme-weight identities imply

    Dbar u'=Dbar v'=0,
    [E_-,u']=[E_+,v']=0,
    [E_+†,u']=[E_-†,v']=0.

For real t, q'_t=q'_0+t u', r'_t=r'_0+t v', at A_0, is exactly
F-flat. Its physical moment is

    muhat_t=t^2 S,
    S=[uhat,uhat†]+[vhat,vhat†].                         (5)

The first-order terms vanish by the displayed identities. S is a
Hermitian D5 section. In the original H direction,

    kappa(H S)=-6(|uhat|^2+|vhat|^2).

Thus the straight curve produces a nonzero moment source for every
nonzero such deformation. Its unrelaxed potential starts at quartic
order with coefficient ||S||^2/(2g6^2).

## 4. The actual D5 gauge inverse has global coercivity

The balanced source vector operator reduces on the D5 adjoint. Its
two-triple modules are

    (1,0),(0,1),(3,0),(0,3),(2,2).

These give45 dimensions and contain no joint trivial module. In(2)
the zero-order endomorphism has eigenvalues

    [j(j+1)+k(k+1)-m^2-n^2]/(2ell^2).

Its minima on the listed modules are respectively
1/(2ell^2),1/(2ell^2),3/(2ell^2),3/(2ell^2),2/ell^2.
The source transitions preserve the positive trace and the Higgs
norm sum. Hence this is a pointwise global bound on the D5 bundle.
The nonnegative connection form gives

    Pv|_D5 >= 1/(2ell^2),
    R5=(Pv|_D5)^-1,       ||R5||_L2 <= 2ell^2.           (6)

This supplies coercivity over the whole core and end. The Green
operator R5 still contains the actual core geometry and holonomies.
Its bound determines estimates while its full kernel determines the
response. The relevant source and response both lie in D5. The A3
spin continuum belongs to a different retained physical sector.

## 5. Derive the second-order response through a Hermitian field path

Use the existing Hermitian-orbit convention with generator xi,

    delta A_x=D_y xi, delta A_y=-D_x xi,
    delta q=[xi,q], delta r=[xi,r].

These are physical field changes at fixed Hermitian kinetic metric.
The associated complex gauge action preserves the holomorphic
equations and the commutator equation. Direct variation of the moment
has connection part nabla* nabla xi and spin parts
{ad_qhat,ad_qhat†}xi+{ad_rhat,ad_rhat†}xi. At the base point,

    delta muhat=Pv xi.                                 (7)

There is an actual global normalization control. The source H is
parallel, Pv H=H/ell^2, and the Hermitian path generated by H changes
each raising field by2 times that field. Direct variation of the
moment gives H/ell^2 as well, fixing the convention in(7).

The full second-order response is therefore determined by

    xi2=-R5 S.                                         (8)

Selfadjointness also fixes its H component explicitly. With
N=integral dvol(|uhat|^2+|vhat|^2),

    projection_H(xi2)=6ell^2 N H/||H||_L2^2.

This follows from R5 H=ell^2 H and the H pairing in section3. It
determines the mean response from the actual source profile and norm.

It is Hermitian because S and the inverse respect compact reality.
The D5 Lie subalgebra is closed, the background is in D5, and the
source S lies there. The response solves an invariant neutral source
equation inside the full action. Charged fluctuations retain their
role in subsequent spectrum and current calculations.

For the proposed S^4 sections, S decays faster than every exponential
in T=log y. Section6 gives a bounded inverse on decaying Holder spaces
as well. It controls xi2, its derivatives and its physical graph norms.

Apply the corresponding Hermitian exponential field path with
generator t^2 xi2 to the F-flat data of section3. Equations(5),(7),(8)
cancel the order-t^2 moment. The holomorphic and commutator equations
remain satisfied. In the source norms,

    muhat_corrected(t)=O(t^3),
    V_corrected(t)=O(t^6).                              (9)

The bounded response and the stipulated bounded profiles justify the
Taylor products in these norms. The effective quartic along this
relaxed path is zero. The positive quartic of the straight fixed-
connection curve measures its unsolved moment source. Section6
extends the response to small finite t.

## 6. A convergent nonlinear response on the full core and cusp

The inverse estimate needed here can be obtained with a scalar barrier.
Put v0=1/(2ell^2). For a smooth solution Pv xi=F, the covariant Kato
inequality and the pointwise endomorphism bound used in(6) give

    (-Delta+v0)|xi| <= |F|.                             (10)

This follows by differentiating |xi| with a positive regularization
at its zeros, using |d|xi||<=|nabla xi|, and then taking the
regularization to zero. The same comparison holds for compact-domain
Dirichlet solutions. Their constant supersolution gives
||xi||_infinity<=||F||_infinity/v0. Energy estimates from(6), core
elliptic estimates and exhaustion identify their unique limit with
the complete-form inverse R5 F.

Choose an auxiliary positive weight rho=e^(-T/4) on the cusp and
extend it smoothly over the compact core. Define C_beta^{k,alpha}
by requiring covariant derivatives through order k and their local
Holder seminorms to be bounded after division by rho. Take0<alpha<1.
The local seminorms use fixed-radius hyperbolic lifts, so the estimate
uses their uniform charts. The weight sets the analytical function
class. The metric and physical fields are the original data.

In the hyperbolic cusp, Delta=(partial_T^2-partial_T)/ell^2 on
radial scalars. Therefore

    (-Delta+v0)rho=3rho/(16ell^2)>0.                    (11)

Compare(10) with a sufficiently large multiple of rho on every
truncated end. The inner circle is controlled by the preceding
global infinity bound, and the outer Dirichlet value is zero.
This gives an exhaustion-independent weighted infinity estimate.
Uniform local Schauder estimates on the hyperbolic lifts then give

    R5 : C_beta^{k,alpha} -> C_beta^{k+2,alpha}

as a bounded inverse. The compact core uses its ordinary finite atlas.
All lifted background coefficients and derivatives are bounded, since
the source curvature and physical Higgs norms are bounded and parallel
in their declared tensor bundles. A bounded decaying section is L2
on the finite-area surface. The uniqueness in(6) identifies the
Holder inverse with the same physical inverse.

In a local bundle frame the principal second-order coefficient is the
scalar metric times the identity. Apply the scalar interior estimate
componentwise and absorb the coupled lower-order derivative terms by
interpolation. Differentiation gives higher k. The scalar estimate,
coefficient-freezing argument and interpolation proof were personally
read in Robert Haslhofer's four-page lecture. The bundle and weighted
cusp application is the argument given here. [PDE II Schauder estimates](https://www.math.utoronto.ca/roberth/pde2/schauder_estimates.pdf)

Let X be the real Hermitian C_beta^{k+2,alpha} space and Y the real
Hermitian C_beta^{k,alpha} space, with k>=2. Products and covariant
derivatives in the moment map are continuous in these spaces.
For small xi in X, its Hermitian exponential has bounded inverse.
Apply that field transformation to the F-flat holomorphic data
parameterized by t. The resulting physical moment is a real analytic
map from(t,xi) to Y, with expansion

    muhat(t,xi)=Pv_0 xi+S2(t)+N(t,xi),
    S2(t)=O(|t|^2),  N(t,0)=0.

The local product and exponential estimates give

    ||N(t,xi)-N(t,eta)||_Y
      <= C(|t|+||xi||_X+||eta||_X)||xi-eta||_X.          (12)

Consequently the map

    xi -> -R5(S2(t)+N(t,xi))                            (13)

is a contraction on a ball of radius K|t|^2 in X for sufficiently
small |t|, with K chosen from the displayed inverse and source bounds.
It maps that ball into itself and has a unique fixed point. This
proves a global bounded decaying response satisfying muhat=0.
Its expansion begins with -R5 S2(t), recovering(8).

The F equations hold exactly by covariance along the Hermitian
exponential field transformation. The resulting family is therefore
globally stationary in the same classical action, with zero residual
potential. The positive physical kinetic metrics are the source
metrics. The Hessian is the sum of the linearized residual squares.

The field differences and their required derivatives are bounded and
decay on the cusp. In orthonormal physical frames the first-order
fermion operator changes by bounded zeroth-order terms. Its complete
graph domain is consequently preserved. The gauge operator retains
its natural closed first-order form domain. The construction uses
the same unitary bundle transitions and source/end law.

## 7. Global native cyclic directions supplying the holomorphic data

The available D5 adjoint pair(3,0)+(0,3) has highest grade3 and
lowest grade-3. The full compensator relation is A^2=P on this
adjoint. On the highest pair P=-I, and A exchanges its two factors.
Unitary constant phase frames therefore give A_top=i sigma_x.
Six lowering steps give A_low=-i sigma_x. D on the lowest pair is
diag(-i,+i). Including the actual flavour factors i sigma_x and
diag(i,-i) gives A_middle=sigma_x, D_middle=I and B_middle=A_middle.

The two core characters of this rank-two middle coefficient are
(++),(--). Its physical spin power is S^4. At the cusp the strict
norm rule for a=4 permits a simple pole. On the compact elliptic
curve each permitted line is therefore L(p), where L is the
corresponding flat unitary character and the extending spin satisfies
eta^4=O. Each line has degree one. Genus-one RR and duality give
one holomorphic section on each line.

Thus the construction retains both available holomorphic directions.
Their physical coefficients behave as r(log(1/r))^2 or faster near
the puncture. Their hyperbolic covariant derivatives have the same
exponential decay up to polynomial factors. They meet the bounded
and decaying hypotheses in section3 and belong to every weighted
class used above. The compact-invariant bracket relations give the
two commuting F-flat data directions directly.

Taking their two complex coefficients as source coordinates gives
a small family near the original background. The contraction argument
applies to the corresponding four real parameters. The uniqueness
asserted here concerns the small Hermitian response for fixed
holomorphic data. Physical equivalences among those state coordinates
require their own gauge and observable analysis.

## Remaining earning conditions

This determines the perturbative response once the holomorphic
deformation is given. Its amplitude, phase and selection remain open.
Sections6-7 give the proposed nonlinear existence argument and its
global native data. Its analytical evidence grade awaits independent
scrutiny. The earlier moment-orbit uniqueness proof has its own full
path and endpoint hypotheses.

The charged-vector masses require the response contributions from
xi2, the varied rough Laplacian and the actual whole same-pole
eigenspace. The cyclic pairing symmetry proposed in the exploratory
notes also needs its complete bundle/operator verification. The
connection directions in(5,5) provide a further native investigation.

Review must verify the exact source matrices and coefficients, the
global neutral sections, the pointwise D5 coercivity, exhaustion/Kato
and weighted Schauder bounds, the Hermitian moment derivative and
the nonlinear contraction and domain estimates. The current
computational design is prospective.
The result's evidence grade is an author hand derivation pending
independent review and admitted checks.
