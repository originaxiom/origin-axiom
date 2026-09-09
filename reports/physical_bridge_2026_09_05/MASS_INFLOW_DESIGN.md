# R23: the actual mass texture and its anomaly transport

2026-09-09. Pre-execution design. Path-local, no B allocation.

BANKED IDENTITY: R16's actual exterior/adjoint operator, R18's declared
strong maximal complex, R19/R20's charged adjoint sector and R21's
root-derived anomaly polynomial. R22 leaves actual source/inflow as
the next join. Source inputs are not selected by this calculation.

PRIOR ART: Kanno--Sugimoto 2106.01591, sections 2, 3.2, 4.1.3, 4.3;
Choi--Ohmori 2205.02188 (3.21), section 3.3.2; Braun et al. 1812.06072
(2.2), (2.41)--(2.49), appendix A.2; Pantev--Wijnholt 0905.1968 section
3.4. Full relevant sections, old B796/gap2_gs and six flagged findings
read; see MASS_INFLOW_PRIOR.md and the saved eleven-head sweep.

## Quantifier, choices and two outcomes

P0: the specified commuting charge-q Witten operator on the smooth
source complement, local normal charts and compact regulated regions.
Local statements at nondegenerate zeros do NOT assume that the actual
global source has exactly three such zeros. Full singular determinant,
the total Berry flux on the actual ends and a UV completion are not
provided by finite matrices or a generic Callias citation.

P1--P4: PB-BOUNDARY/X33. Follow the same source path, retaining its
R18 domain and R20 parent. Fresh main/SM/physics/outside pins are in
the prior receipt. Do not import the new smooth-cusp negative's
quantifier or triangulation automorphisms as all isometries.

P6: expect a positive local mass/Clifford identification and a unit,
not doubled, local angular response. Expect bulk descent to cancel a
localized anomaly only by retaining an equal boundary obligation.
Do NOT expect a solved three-family quantum theory from this alone.
Expect the whole-torus-to-partition inference in incoming B1351 to
fail on explicit relative cochains. A contrary result is retained.

PASS/FAIL are per claim below, not a single target-fitting score.
Known zero, orientation-reversed, conjugate, nontrivial-regulator,
and boundary-retaining controls are mandatory. Any original failure
is saved with its producer/tests unchanged; repairs need a separate seal.

## A. Exhibit the map, not just a matching dimension

Oriented Euclidean local coframe (dx0,dx1,dx2), standard L2 form basis
ordered by degree as R16. Let e_i be wedge and i_i its adjoint,
c_i=e_i-i_i, h_i=e_i+i_i, J=c0*c1*c2 and parity (-1)^degree.
Recompute the R16 normal-chart D_H on plane-wave test coefficients.
It must equal sum c_i*partial_i+h_i*m_i, m_i=q*partial_i F.

On EVEN forms derive G_i=i*J*c_i and T_i=i*J*h_i. Expected two commuting
Hermitian Clifford triples with products -i and +i respectively.
Construct a unitary U from their joint eigenspaces, then require

  U^dagger G_i U = -sigma_i tensor 1,
  U^dagger T_i U = 1 tensor sigma_i.

Thus i*J*D_even is a 3d kinetic operator with a two-by-two Hermitian
mass texture. Verify the Spin(3) rotation commutators as well as all
symbols/mass matrices. This is a local Clifford-bundle map; global
spin connection and singular domains are not erased by a chart.

For F=sum lambda_i*x_i^2/2 verify the Gaussian wedge in the negative
eigendirections is annihilated by the ACTUAL D, for all eight sign
patterns and traceless saddle controls. Its degree is the Morse index.
Ground-state oscillator energies must select exactly that form.
Odd forms are left Weyl, even right, per the prior convention, so the
local left-minus-right coefficient is -sign det Hess(qF).

Braun's adjoint reality pairs R_q and its conjugate; one member has
an unconstrained Spin(7) spinor times the R doublet, i.e. two Dirac
flavours per R component. Exhibit the off-diagonal antisymmetric
Grassmann form and Pf([[0,D],[-D^T,0]])=(-1)^(n(n-1)/2)*det(D).
The general identity follows by block congruence; finite controls must
reject both double-counting the conjugate and taking another square
root. This does not settle the global Pfaffian sign/torsion anomaly.

## B. Normalization and frame covariance of the mass response

Use Pauli matrices, n=(sin theta cos phi,sin theta sin phi,cos theta),
P=(1+n.sigma)/2. With anti-Hermitian connection Gamma, the induced
line curvature is Tr[P F_Gamma + P(DP)^2]. Define

  K2 = i/(2*pi) Tr[P F_Gamma + P(DP)^2].

In the flat frame this has integral -1 on the outward unit sphere;
it is the first Chern form of the positive eigenline, not an arbitrary
real multiple. Reverse m or orientation to reverse the charge. The
Morse control ties the sign to the declared physical chirality.
Verify a position-dependent frame rotation, and a constant-projector
curved-connection control that detects omission of F_Gamma.

Independently use the ODD superconnection A=i*T*sigma_aux with
T=m.sigma. The graded cubic term has coefficient i*(dT)^3/6.
The normalized trace must give

  rho3 = -exp(-|m|^2)/pi^(3/2) dm0 dm1 dm2.

Check its integral, angular primitive with radial factor
erf(r)-2*r*exp(-r^2)/sqrt(pi), and both endpoint limits. This is an
exact local normalized Thom/descent form, not a heat-kernel certificate
on the full cusp. Numerical anisotropic-sphere quadrature is an
additional control only. The all-invertible-linear-map degree follows
from polar decomposition, not a finite sample.

Same-sign mass eigenvalues have no angular response; opposite signs
do. A positive equal-mass reference contributes a separate degree-eight
regulator term. Compute a nonzero I8 on the actual R weights to keep
that obligation visible. No unique global counterterm choice is claimed.

## C. Local cancellation must retain all outer boundaries

Declare delta Gamma_Weyl=2*pi*i*sum nu_a*I4_a, d CS5=I6 and
delta CS5=d I4. With dK2=sum nu_a*delta_a, proposed bulk descent obeys

  delta[2*pi*i*integral K2 CS5]
      = 2*pi*i*(integral_outer K2 I4-sum nu_a I4_a).

Recompute the integration-by-parts sign and actual weight polynomial.
If the bulk accounts for a nonzero local sum, its retained outer
boundary has that same total flux. For a gauge parameter constant
internally, its variation is ZERO, so it cannot remove the zero-mode
anomaly merely by being called inflow. Test 3 identical left modes,
zero-total opposite defects, a compactly-supported gauge parameter,
and deliberately dropped outer terms. The three-mode example is a
consistency control tied to R19's anomaly, NOT an assertion that all
its modes have already been localized at three critical points.

The actual global mass map, boundary/eta regulator, end sector or a
massive-U1 mechanism remain duties. Restricting gauge transformations
at the boundary is additional physics; do not preserve a constant
massless U1 zero mode while quietly forbidding its gauge parameter.

## D. Receiving control: a whole torus is not its partition

On a solid torus with nontrivial unitary longitude character z,
H*(M;L)=H*(T2;L)=0. A contractible boundary disc has H0=1. Construct
the mapping-cone relative cochain complex using d_M=z-1 and restriction
C0(M)->C0(disc)=1. Expected H*(M,disc;L)=(0,1,0,0), chi=-1.
Use exact z=i and a cube root, the trivial character control and an
essential annulus carrying the same nontrivial character (index zero).
This refutes that algebraic implication, not every analytic complete-
cusp theorem or a claim that such a disc is physically supplied.

## Execution and evidence

Write producer and locks before sealing; no importing them before
the seal. First native JSON, focused R18--R23 tests and a separately
enumerated expanded regression, retaining original failures and full
stdout. The tree is read-only while certifying. All first outputs
are saved before yielding; public captures redact environment prefixes
only. Update reader surfaces, scoped laws, open duties and failure
record. No main merge, external relay, full banking or TOE claim.
