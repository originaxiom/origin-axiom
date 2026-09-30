# Charged cone radial modes and separate differential domains

September 30, 2026. R63 pre-execution design and authored argument.
Continue PHYSICS_MISSION by resolving the next local admission question
in R62's SAME supplied action, not by counting another algebraic index.

## Scope and declared prior

Use a flat torus link, the incomplete cone g=dr^2+r^2 h, and a constant
normal parent coefficient X with C=wX, initially B=0. In a simultaneous
unitary eigenframe a root/weight line sees C_a=w a, a=alpha(X).
This is an admitted R62 background. The eigenframe is a computation
frame, not a selected physical Cartan, vacuum or parent. Coordinates on
the torus have period one. Test the full eight-component form operator
Q_a=d_a+d_a^dagger and both summands separately. No global kernel,
compact gauge quotient, full supercharge closure or anomaly is inferred.

Prior: nonzero but sufficiently small a has no link cohomology but has
critical conical radial modes. Among its four critical homogeneous
solutions, two pass the separate differential/adjoint norm test and two
only pass their sum by cancellation. The former are decaying candidates,
not particles. Their nonlinear extension and gauge status remain open.
The exact symbolic controls may falsify any formula or sign below.

## Reuse and literature scope

All remote heads were fetched from own HEAD dead2cc9 with no update.
R61, R62, their producers, and R16's CHARGED_DOMAIN design/report and
MetricForms implementation were read. R16 already distinguishes D_min
from d_min+delta_max and derives an indicial operator for a LINE defect;
that different metric/measure and threshold are not imported here.
Reuse its metric exterior calculus, not another invented Hodge engine.
The ladder, framework, campaign and PB-BOUNDARY identify this duty.

The epoch-limited atlas and already-banked query 'cone indicial charged
Hodge graph' were run; 78 hits, no settled match on three of five terms.
Targeted body/code and old kill-graph searches were checked. A broad
search output was truncated and is not an absence certificate. No
whole-corpus absence or novelty claim follows. Identification audit
still has nine unearned entries, with unchanged baseline.

Personally read Albin et al. 1307.5473v3, section 3.1, especially the
unitary radial normalization and Lemma 3.1's link spectral-gap condition.
Its reduction to harmonic-link traces requires that gap. The present
constant flat charged extension is derived below; the reference does
not certify our complete physical domain. Accessed September 30:
https://arxiv.org/html/1307.5473v3
Braun 1812.06072v2 equations 2.9--2.15, 2.34--2.44 supply the adopted
twisted differential and its relation to fermions, already used in R61.
No whole-paper rereading, empirical value or new physical identification.

## Full normalized radial operator

Write link p-forms in an orthonormal link frame and use the isometry

    U(alpha,beta) = sum_p r^(p-1) alpha_p
                         + dr wedge sum_p r^(p-1) beta_p

to radial L2(dr). Here alpha_p is a total p-form and beta_p a total
(p+1)-form. Forgetting this distinction changes the degree test.
On Fourier momentum k=2 pi m, put z=i k+C_a in that frame and
lambda=z^dagger z. Let e(z) be wedge by z, a(zbar)=e(z)^dagger,
L=e(z)+a(zbar), and P=diag(0,1,1,2). Then

    Q = gamma (partial_r + A/r),
    gamma = [[0,-1],[1,0]],
    A = [[P-1,-L],[-L,1-P]],
    r U^-1 d_a U on r^sigma = [[e(z),0],[sigma+P-1,-e(z)]],
    r U^-1 d_a^dagger U on r^sigma
                            = [[a(zbar),-sigma+P-1],[0,-a(zbar)]].

The unit matrices in these block expressions have size four. Check all
entries independently using R16's coordinate exterior derivative and
metric Hodge star for lengths (1,r,r), with a genuinely complex C and
generic Fourier momentum. Its old real dH convenience is not reused as
a complex adjoint: the contraction MUST use conjugate(C). Check d^2
with the shifted radial exponent and a wrong-adjoint countercontrol.

Since L^2=lambda and wedge by z is a degree-preserving unitary transform
of wedge by (sqrt(lambda),0), A has eigenvalues

    +/- (sqrt(lambda+1/4)-1/2),
    +/- (sqrt(lambda+1/4)+1/2), each with multiplicity two.

At lambda=0 this is (-1,-1,0,0,0,0,1,1). Use both the characteristic
polynomial and an explicit complex unitary transform, not a sampled
numeric diagonalization. For 0<lambda<3/4 there are four eigenvalues
in (-1/2,1/2). Above and at 3/4 there are none in the OPEN interval.
At the endpoint the slow r^-1/2 norm diverges logarithmically; the
fast r^1/2 branch has vanishing logarithmic cutoff capacity. This is
a local radial statement, not a global essential-self-adjoint theorem.

## The Fourier population and the moving gap

For the two R61 link metrics H=h^-1, let v=Im(w a), u=Re(w a).
Helicity implies |u|_H^2=|v|_H^2=c|a|^2/2, so

    lambda_m(a)=|2 pi m+v|_H^2+|u|_H^2
               =2|v+pi m|_H^2+2 pi^2 m^T H m.

For nonzero integer m, m^T H m >=1 on the unit-area square link and
>=2/sqrt(3) on the unit-area hexagonal link, using m1^2+m2^2-m1*m2>=1.
Thus every nonzero Fourier mode lies above 3/4, for EVERY a; no finite
Fourier cutoff is used to prove completeness. At m=0,
lambda_0=c|a|^2. For a!=0 the flat-line torus cohomology vanishes:
both periods cannot be integral multiples of 2 pi i since w1/w2 is
nonreal. Equivalently each Fourier Koszul complex has contracting
homotopy a(zbar)/lambda. This does not remove its small radial modes.

Scaling the link metric to ell^2 h divides lambda by ell^2. No fixed
finite scale removes all small charged eigenvalues uniformly as a
varies towards zero through nonzero values. Metric/vev selection must
be earned or stated. These dimensionless thresholds are not measured
couplings or a Higgs mass prediction.

## Separate norms distinguish the critical modes

Put eta=sqrt(lambda+1/4)-1/2, s=sqrt(eta(eta+1)), so 0<eta<1/2 in
the nonzero critical range. Work in the unitary link frame z=(s,0),
ordered (alpha0,alpha1,alpha2,alpha12,beta0,beta1,beta2,beta12).
Four vectors, with unlisted entries zero, are

    fast1: alpha1=s, beta0=eta;                 radial r^eta,
    fast2: alpha12=eta, beta2=s;                radial r^eta,
    slowEven: alpha0=s, beta1=-(eta+1);         radial r^-eta,
    slowOdd: alpha2=eta+1, beta12=-s;           radial r^-eta.

All solve Q u=0 and are L2 near the tip. Both fast modes separately
solve d_a u=0=d_a^dagger u. For each slow vector, d_a u is the negative
of d_a^dagger u, with nonzero squared coefficient
eta(eta+1)^2(2eta+1) and radial density r^(-2eta-2); the separate
norms diverge. Fast1 has total degree one, fast2 total degree two.
The slow vectors mix degrees 0/2 and 1/3 respectively. The fast
two-plane is maximal isotropic for the critical Green pairing; fast
and slow pair nondegenerately. This is an admission condition on these
homogeneous modes, not a complete interacting supersymmetry theorem.

The first fast mode is locally d_a of the scalar r^eta in this frame.
Exhibit that primitive. Local complex exactness does not decide its
physical compact-gauge quotient or global gluing. Its tangential
coordinate trace vanishes, so R62's constant-trace constraint must not
be used to discard it. Finite separate LINEAR residuals do not yet
certify its nonlinear extension; eta can be below R62's generic
sufficient remainder threshold. No physical state is counted here.

## The radial gauge distinction

For a commuting anti-Hermitian B, the map g(r)=exp(B log r) removes
C_r=B/r on the punctured cone under C^g=g C g^-1-dg g^-1. It is unitary
on L2 but generally has no limit at r=0. A concrete diagonal imaginary
B checks the differential and norm identities. This is a unitary
transport of domains, not permission to change the gauge group: an
apex-continuous gauge convention excludes such g. The primary spectral
calculation is B=0, not an assertion that every allowed B is gauge-zero.

## Execution and acceptance

Freeze design, input pins, producer and tests, then commit/push and
confirm remote before science execution. Require the metric-derived
operator, complex adjoint countercontrol, generic polynomial, explicit
unitary reduction, shifted nilpotency, two-sided threshold and endpoint
controls, full Fourier inequality, Koszul homotopy, exact fast/slow
residuals and Green pairing, local primitive and radial gauge scope.
Run ten new tests with R62's ten and R61's eight, a fixed 28-test set.
Keep original stdout/exits and any failures; do not edit sealed science.
Any correction requires its own new seal. No full-suite, independently
accepted proof, physical end-law completion or chirality claim.
