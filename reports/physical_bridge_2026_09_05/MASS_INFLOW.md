# R23: the source operator supplies normalized anomaly transport, not a boundary completion

2026-09-09. Path-local research. Original seal a726252a; separate
bundle-control seal 2684623c. Original sources and tests unchanged.

**Movement.** The existing charged differential is explicitly mapped
to the two-flavour mass operator used in anomaly-inflow calculations.
Its mass direction supplies an integrally normalized angular form,
with the local chirality sign and fermion reality factor checked.
A separate control retains the full eigenbundle characteristic class;
its extension ambiguity is integral on admissible closed spin fillings.

This constructs a specific local anomaly-transport candidate from the
same operator, not another appended list of fields. It does NOT yet
construct the global singular determinant or its boundary sector.
Even granting perfect local inflow, dropping the outer-boundary term
would fake cancellation of the three-spinor gauge-zero-mode anomaly.
The source/cusp completion remains the physical next duty.

## 1. The operator map actually acts

Use R16's differential and adjoint in an oriented orthonormal chart.
Write e_i for wedge, a_i for contraction, c_i=e_i-a_i and h_i=e_i+a_i.
On all eight forms the actual operator is

    D_H = sum_i c_i partial_i + h_i m_i,  m_i=q partial_i F.

It is not enough that eight equals a spinor dimension. Put J=c0 c1 c2.
J is odd, Hermitian and unitary. On even forms G_i=iJc_i and T_i=iJh_i
are commuting Hermitian Clifford triples, with products -i and +i.
Their joint eigenspaces construct an explicit unitary U satisfying

    U* G_i U = -sigma_i tensor 1,
    U* T_i U = 1 tensor sigma_i.

Thus iJ D_even has the actual kinetic symbol -sigma.partial and
Hermitian mass m.sigma on the second two-dimensional factor. Every
matrix is checked against the original exterior/adjoint operator.
The natural form-rotation generators also agree with the combined
two spin actions. Consequently the map respects the local twisted
connection, not only constant matrices in an unrelated representation.

For F=sum lambda_i x_i^2/2, the actual Gaussian form is
exp(-sum abs(lambda_i)x_i^2/2) wedged in the negative eigendirections.
Direct substitution annihilates it. All eight occupation energies
give exactly one zero state, of degree equal to the Morse index.
The traceless saddle controls are compatible with a locally harmonic
F. Under the declared odd-left/even-right dictionary, its contribution
is nu=-sign det Hess(qF). The other sign patterns are instrument
controls, not extrema asserted for the actual harmonic source.

The adjoint's reality condition pairs R_q and its conjugate. One
representative has an unconstrained Spin(7) spinor times the R doublet:
two Dirac flavours, not one and not a second copy for its conjugate.
The off-diagonal Grassmann matrix has
Pf([[0,D],[-D^T,0]])=(-1)^(n(n-1)/2) det D. Block congruence proves
the general identity; exact controls reject doubling and an extra
square root. This fixes the local counting factor, not a global
Pfaffian sign on the singular space.
Prior action and chirality dictionary: [Braun et al., (2.2),
(2.41)--(2.49), appendix A.2](https://arxiv.org/pdf/1812.06072).

## 2. A unit angular response, with the frame retained

Where m is nonzero, n=m/|m| and P=(1+n.sigma)/2 define the positive
eigenline L+. Its induced connection is P nabla. For anti-Hermitian
connection Gamma the first Chern form is

    K = i/(2*pi) Tr(P F_Gamma + P(DP)^2).

In a flat frame on an outward mass-direction sphere,
K=-sin(theta) dtheta dphi/(4*pi), with integral -1. Under any invertible
linear mass map its flux is -sign(det map), by polar decomposition
and degree; anisotropic numerical quadrature is a separate check,
not that proof. This is precisely the Gaussian chirality coefficient.

The connection terms are essential. A position-dependent unitary
frame change preserves K when Gamma is transformed too; omitting it
reverses the displayed local sphere density in the control. A constant
projector with a curved diagonal connection has nonzero K from F_Gamma.
The flat n.dn.dn expression cannot be copied onto a curved frame alone.

An independent odd-superconnection calculation uses T=m.sigma.
The graded cubic term is i(dT)^3/6 and Tr(dT)^3=12i dm0 dm1 dm2.
With the odd-supertrace normalization it gives

    rho3 = -pi^(-3/2) exp(-|m|^2) dm0 dm1 dm2,
    integral rho3 = -1.

Its angular primitive has radial factor
f(r)=erf(r)-2r exp(-r^2)/sqrt(pi), with f(0)=0 and f(infinity)=1.
The two endpoints are explicitly checked; losing the second loses
the flux. Regulator-scaled mass coordinates are used here. This is a
normalized local mass-space form, not evaluation of a heat-kernel
trace over the actual cusp. The noncompact/discrete-spectrum hypotheses
in the literature have not thereby been proved for our operator.
[Kanno--Sugimoto, sections 2, 3.2, 4.1.3 and 4.3](https://arxiv.org/pdf/2106.01591).

## 3. The global characteristic expression is more than K I6

Let I_(2j)=[Ahat(T) ch(R)]_(2j), with the actual H spinor weights
from R21, and use the positive equal-mass reference on the SAME
rank-two R bundle. With one positive and one negative eigenvalue,
the signed half-sum minus this reference is -ch(L-), where L-=L+ dual.
The degree-eight class is therefore

    B8 = -I8 + K I6 - K^2 I4/2 + K^3 I2/6 - K^4 I0/24.

Independent substitution ell->ell-K in the root-derived -I8 gives
exactly this polynomial. When K is pulled back from a flat mass sphere,
K^2=0 and the local expression reduces to -I8+K I6. That simplification
is not valid on every extension bundle. On the explicit spin product
(S2)^4 with gauge flux (2,3,4,5) in the allowed cocharacter C^-1 e0
and eigenline flux (1,1,1,1), full integration is -384 whereas retaining
only -I8+K I6 gives 544. Independent product integration agrees with
the full polynomial. These are normalization controls, not predictions.

For two ADMISSIBLE smooth spin eight-dimensional fillings, with all
the same boundary bundles extended, their difference is closed and
the integral of B8 is minus the ordinary Dirac index twisted by
R tensor L-. It is integral. Hence the corresponding extension phase
ambiguity is trivial. This uses the ordinary index theorem as an
analytic input; finite examples alone would not establish integrality
on every spin manifold. It neither proves that every configuration
bounds, nor selects a torsion/Pfaffian phase or a boundary eta invariant.
The actual singular/open-end determinant is still not constructed.
[Choi--Ohmori, (3.21), section 3.3.2](https://arxiv.org/pdf/2205.02188).

## 4. What the inflow cancels, and what it leaves

Declare d CS5=I6 and delta CS5=d I4. If K accounts for local charges
nu_a, its distributional derivative is sum nu_a delta_a. Then

    delta[2*pi*i integral K CS5]
      = 2*pi*i (integral_outer K I4 - sum_a nu_a I4_a).

The integration-by-parts sign is checked in exterior algebra. Local
Weyl anomalies cancel the second term, leaving the first. All cusp,
source-tube and corner pieces of the outer boundary belong in it.

For a gauge parameter constant internally, Stokes gives total outer
flux=sum nu_a, so this bulk term's gauge variation is ZERO. In the
three-positive-mode control the local, outer and bulk coefficients
are 3, 3 and 0. Multiplication by the actual root anomaly reproduces
R19's nonzero three-spinor I6, not zero. A compactly-supported gauge
parameter does have its local anomaly cancelled. Opposite defects with
zero total charge also pass the cancellation control. The full bundle
normalization in section 3 does not waive this boundary balance.

This does NOT assert that the actual global F has three nondegenerate
critical points or that its complete end flux has been computed. It
tests what a proposed local inflow completion must do IF it accounts
for those charged modes. The finite kernel in R18 is not a license
to import a global Callias/determinant theorem with unchecked hypotheses.
Forbidding the constant gauge parameter at the boundary would change
the gauge theory; it cannot silently coexist with the unchanged
massless U1 gauge-zero-mode claim. Actual end matter, an eta/relative
sector, a massive-U1 mechanism or different physical boundary dynamics
remains necessary in this construction.
[Pantev--Wijnholt, section 3.4](https://arxiv.org/pdf/0905.1968).

## 5. A new incoming negative has a narrower valid scope

SM B1351 at ce5ca412 states that acyclicity of the full cusp torus
forces zero index for every Morse partition. That implication fails
as a relative-cohomology statement. On a solid torus with nontrivial
unitary longitude character, both the solid torus and its whole
boundary torus are acyclic. But a boundary disc is contractible and
has H0=1. The actual restriction mapping cone has

    C0=C, C1=C^(1+k), d0=(z-1,1,...,1)^T

for k disjoint boundary discs, hence H*=(0,k,0,0) and chi=-k.
The full torus complex has ranks 1,1 and zero cohomology for z!=1.
Exact i and cube-root characters verify both calculations. Replacing
the discs by an essential annulus gives an acyclic relative cone,
including the trivial-character control.

Thus cohomology of a whole torus cannot replace the cohomology of
its partition. This preserves a mathematical opening, not a physically
selected disc boundary or a new complete-cusp harmonic vacuum. It
does not contradict the correctly scoped closed-space pairing theorem
or reproduce the later V10 computations.

## 6. Status and next duty

Closing sentence:

> The existing commuting charged operator has an explicit local mass
> map and unit anomaly-transport form, with a conditional integral
> eigenbundle response; bulk descent alone retains the outer-boundary
> anomaly of an internally constant gauge mode.

PB-BOUNDARY remains OPEN. Next determine the actual global mass map,
its source/cusp end response and admissible regulator/domain, then
construct the end sector or massive-U1 dynamics in that same theory.
Do not append another abstract counterterm, discard a boundary, or
forget R22's mode-supply restriction. Source/global-form selection,
Spin(10)-to-SM breaking, the neutral 4D limit, common gravity and
empirical tests remain separate duties. No new B ID or full TOE.

## 7. Verification and incoming-work boundary

Both first native runs succeeded: 3.978 seconds for the original
operator/transport calculation and 1.744 seconds for the separately
sealed full-bundle control. Their complete JSON outputs were captured
immediately. The first focused selection passed 87 tests; the expanded
focused selection passed 93 tests in 40.60 seconds. There are 24 new
tests in the two sealed modules.

The quiescent 43-file regression finished with 309 passed, 13 failed,
8 errors and one warning in 306.45 seconds. Its 21 failed/error IDs
are EXACTLY R22's: none added or missing. This is neither full-repository
green nor independent proof review. No original scientific source,
assertion, tolerance or failed receipt was rewritten.

Receipts: [original focused](MASS_INFLOW_CHECKS.txt),
[bundle focused](MASS_INFLOW_BUNDLE_CHECKS.txt),
[expanded regression](MASS_INFLOW_REGRESSION.txt),
[original native JSON](mass_inflow_first_run.json),
[bundle native JSON](mass_inflow_bundle_first_run.json).

The calculation's incoming sweep was pinned to main abb16e85 and
SM ce5ca412. A subsequent all-head fetch reached main b94ed03a and
SM 1703c0d8, including new B1355. That received curved-cone construction
is a distinct route, not tested or excluded by this calculation.
Its cross-seat assessment will be recorded separately. Main's earlier
harvest through R20 is not independent review of R21--R23.

Reporting-gate and artifact-check receipts are tracked in
[BANKING_RECEIPT.md](BANKING_RECEIPT.md). No B number is allocated.
