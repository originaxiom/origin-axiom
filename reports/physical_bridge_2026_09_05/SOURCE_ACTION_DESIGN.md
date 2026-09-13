# R28 — fixed-source stationarity, source cost and action scope

2026-09-13. Pre-execution design. No empirical target or new B number.

BANKED IDENTITY: R15 has a commuting global phi=u dF, harmonic off
prescribed geodesic sources, with F=V+exp(2s)(bs+c) plus a bounded
harmonic cusp corrector. R19's charged kernel and R26's index stability
are conditional on their fixed strong-source domain and flat character.

PRIOR ART: SOURCE_ACTION_PRIOR.md. The twisted 7d SYM action is
standard, specifically Braun et al. (2.13); R23 already used its
fermionic part. No new action for the originating object is claimed.
SOURCE_ACTION_PROOF.md contains the all-class argument to be checked.

## P0--P6

P0: over the prescribed commuting compact-gauge, fixed-metric source
class on complete finite-volume hyperbolic three-manifolds, distinguish
static BPS potential on the excised space, 4d kinetic norms of changes
in source data, and the bare potential cost of a resolved abelian core.
The tube bound assumes a straight embedded segment with fixed radial
flux and zero end-cap flux; it is not a theorem about every defect.
The separate discrete-action controls have their own real finite-
dimensional quantifier and no physical field-theory identification.

P1--P4: same PB-BOUNDARY/X33 duty; no value rung is skipped. Retrieved
history, live leads and incoming scopes are recorded in the prior file.
Both rows and all members are included when the analytic hypotheses
hold; no special count, source activation or topology is selected here.

P6: expected outcome is a POSITIVE static fixed-background result and
a distinction, not a universal infinite-action kill: the BPS residuals
vanish off sources, but promoting residues/through-flux to 4d fields
has divergent kinetic norm in the fixed metric/action. A finite core
at fixed flux should have a sharp nonzero bare D-term cost. If any
identity/control fails, preserve the first run and narrow that module.

Seal and commit this design, proof, source and tests BEFORE first
scientific import or execution. Keep the tree read-only during runs.
Capture first stdout and exit status durably; corrections get new seals.

## A. Correct field, action and stationarity

Take a positive invariant inner product on the compact gauge algebra,
a covariantly constant Cartan u and flat commuting W. With form norms
including the conventional 1/p!, (2.13)'s commuting static potential
is (2/g7^2) times integral(|d phi|^2+|delta phi|^2+|d W|^2).
The 4d scalar kinetic coefficient is (1/g7^2) integral |delta phi|^2.
No measured g7 or derived normalization is asserted.

Verify the two-form/component contraction and I=2 div(phi) factors.
At a zero-residual background all first variations vanish and the
potential is minimal among admissible nonnegative-residual fields.
This is proved on compactly supported regular variations, not by an
unchecked integration by parts across a source. It neither derives
the fermion self-adjoint extension nor includes a dynamical defect.

Use a periodic smooth 1-form control with positive potential and finite
kinetic norm, and a harmonic constant torus control with zero potential
and finite kinetic norm. The action need not punish every deformation,
and zero potential alone must not imply nonnormalizability.

## B. Exact hyperbolic tube and sharp smooth-core cost

Metric: dr^2+sinh(r)^2 dtheta^2+cosh(r)^2 dell^2, curvature length one,
theta period 2*pi, central-axis segment length L. Let w=sinh(r)cosh(r)
and F=beta log(tanh r). Compute phi_r=F', div(phi)=(w F')'/w and
kinetic norm on epsilon<r<R. Recover the coefficient 2*pi*L*beta^2
of log(1/epsilon). beta=0 must remove it.

Compute all three orthonormal Hessian entries directly, including
coth(r)F' and tanh(r)F'. Check the Bochner boundary identity for
Hess(F)^2-2|dF|^2. This is a control against discarding the curvature
and boundary terms and replacing the Hodge potential by rough energy.

For a smooth commuting core 0<r<epsilon with total outward flux
2*pi*L*beta and zero axial cap flux, apply Cauchy--Schwarz to div(phi).
Volume is pi*L*sinh(epsilon)^2. The D-residual norm must be at least
4*pi*L*beta^2/sinh(epsilon)^2. Exhibit the attaining axially invariant
core phi_r=beta*tanh(r)/sinh(epsilon)^2 and check regularity, boundary
matching, uniform divergence and its exact integral. The joined field
is piecewise smooth, continuous at the side, with no delta jump there;
do not call it globally C-infinity. A strictly larger nonuniform-core
control tests sharpness. Also check that a DECLARED external moment-map
source shifts the residual to zero: this changes the action and does
not derive that source. Nonabelian cores and end leakage are excluded
from the bound, not silently killed.

## C. Cusp norm and gauge compensation

Metric ds^2+exp(-2s)g_T, torus area A. Verify the Laplacian cancellation
between Delta_T V=-2b off punctures and H=exp(2s)(bs+c). Include the
constant harmonic corrector and zero-mean Fourier correctors in the
mean argument; no computed global corrector is asserted.

For a parameter variation (delta_b,delta_c), check the exact radial
norm antiderivative A*exp(2s)*(4*(delta_b*s+delta_c)^2+delta_b^2)/2.
Jensen's inequality gives this as a lower bound for the full norm.
Test b=0,c nonzero separately: through-flux alone is still nonnormalizable.
For b=c=0 the radial lower bound is zero, NOT a certificate that every
other variation is normalizable. Any nonzero individual residue has
the separate local tube obstruction, even if endpoint sums cancel.

Gauge compensation cannot remove the Cartan component: prove
<u,[epsilon,u]>=0 by invariance, and check with explicit Hermitian
2-by-2 matrices. The metric and source embedding are fixed; no claim
about gravitational compensation, new boundary kinetic terms or UV
renormalization is allowed. Compactly supported regular fluctuations
are the positive finite-norm control, not changes to the end data.

## D. The received action negative: verify its actual quantifier

Recompute the trace-map invariant and anti-Poisson identity and retain
the exact matrix conjugacy of the two half-step conventions. For a
regular autonomous one-coordinate discrete Lagrangian on a connected
real invariant domain, preserve its nonvanishing area density; this
forbids orientation reversal there, not all stationary actions.

Check L(a,b)=exp(a)*b: its DEL map preserves exp(a) da wedge db but
has Jacobian exp(a-b), not identically one. Check the time-dependent
regular L_n(a,b)=(-1)^n*(a*b-a^2/2): its DEL equation is proportional
to c-b-a and gives the actual Fibonacci half-step. Removing the time
alternation must fail. For the full nonlinear trace map, the enlarged
multiplier action sum p_(n+1).(x_(n+1)-T(x_n)) gives the map by its
p-equation and the cotangent recurrence by its x-equation; p=0 is
admissible on every orbit. These are stationary-action counterexamples,
NOT minima, autonomous same-state actions or derived physical dynamics.

## Outcomes and scope

Report separately: zero-residual bulk stationarity; nonnormalizable
source parameters; sharp specified-core cost; incoming action-scope
correction. Do not infer a full physical action, source selection,
anomaly cancellation, three generations, neutral-sector gap or gravity.
R18/R19's conditional spectrum stays on its original domain. Run focused
tests and the exact prior broad population plus the new test file;
compare failure IDs without altering old assertions or tolerances.
Record gates honestly, commit/push this branch and leave the TOE goal
unfinished. Independent bank/main acceptance is not this checkpoint.
