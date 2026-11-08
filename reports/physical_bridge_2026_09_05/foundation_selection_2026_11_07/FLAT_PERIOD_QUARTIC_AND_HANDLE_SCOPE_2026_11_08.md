# What the inherited action does to the surviving flat periods

2026-11-08. **Author hand derivation, UNREVIEWED.** No scientific
import, collection, CAS or numerical run. This is a conditional,
leading-order calculation within the existing residual-zero classical
gauge sector. It does not select the parent, the surface or a vacuum.

## 1. Reuse the old kernels, metric and nonlinear obstruction

The finite-norm form extension at the cusp is already in
[the form-parent proof](../weave_form_parent_2026_10_08/PROOF.md).
The harmonic representatives, their admissible gauge equivalence to
compactly supported representatives and the actual period kinetic metric
are already in
[the full flat family](../word_architecture_audit_2026_10_17/FULL_FLAT_FAMILY_METRIC_AND_DISCONNECTED_CENTRALIZER.md).
The general harmonic-curvature/Kuranishi obstruction is already in
[the silver transfer proof](../silver_analytic_transfer_2026_10_09/PROOF.md).
Those are credited prior results with their original qualifications.
The silver coefficient complex and its metric are NOT substituted for
the physical bulk geometry here.

The new duty is narrower: minimize the first nonlinear curvature energy
of the surviving complete-surface connection periods, including the
nonharmonic second-order response. This tests whether the apparently
unfixed linear periods are independent nonlinear flat directions.

Use the same connected, finite-area complete cusp surface Sigma, fixed
metric, supplied physical parent and residual-zero background as
[the gauge proof](SAME_ACTION_GAUGE_BOUNDARY_RESPONSE_AND_CUBIC_2026_11_08.md).
Let g0 be its globally parallel unbroken compact gauge algebra. Every
element commutes with the retained q0,r0 and their adjoints. The source
already proves that g0-valued connections form a consistent classical
bosonic sector. Other fields remain in the physical model and in its
stability/spectrum obligations.

Use the source's Hermitian convention. Thus

    F(a)=d a-i a wedge a,
    V(a)=1/(2 g6^2) integral_Sigma |F(a)|^2 dvol.       (1)

In (1), |F| means the orthonormal curvature coefficient and the positive
source trace kappa is understood. Let A=Area(Sigma). No boundary amplitude
or boundary metric is added.

## 2. Retain all harmonic periods before varying them

On a genus-g compactification choose real harmonic forms h_i,k_i
with symplectic periods and

    integral h_i wedge k_j=delta_ij,
    integral h_i wedge h_j=integral k_i wedge k_j=0.

These forms extend across the filled punctures. Their one-form norm is
conformally invariant, finite on the complete cusp, and equals the norm
on the compact conformal surface. Conversely, the local Laurent/L2
argument from the form-parent proof prevents extra pole forms. Here the
g0 coefficient bundle is parallel and trivial on this channel; twisted
coefficient kernels are a different problem.

Take independent small Hermitian coefficient periods U_i,V_i in g0,
and write

    a=epsilon a1+epsilon^2 a2+O(epsilon^3),
    a1=sum_i (h_i U_i+k_i V_i).

Do not identify the two relative harmonic modes on a truncated genus-one
core with two already matched global particles. This calculation uses
the actual COMPLETE-surface harmonic representatives. Their metric is
the already derived Hodge metric, not a new flavour matrix.

At second order the curvature is

    F2=d a2+S,  S=-i a1 wedge a1,
    C=integral_Sigma S=-i sum_i [U_i,V_i].             (2)

C is a Hermitian Lie-algebra coefficient. It is a quadratic obstruction
in the small periods, not a supplied integral cocharacter flux. The
earlier quantized Abelian Phi sector must not be identified with C.

## 3. Eliminate the nonharmonic response, not the obstruction

Work in the complete finite-energy domain, fixing the harmonic part of
a2 to zero as a coordinate choice. For the corrections constructed below
the remote circulation vanishes, so integral d a2=0. The fixed harmonic
periods have already been retained in a1; no physical period is removed
by this coordinate convention.

Cauchy--Schwarz gives the lower bound

    integral |F2|^2 dvol >= kappa(C^2)/A.              (3)

It is attained at this order. Put f=*S, and solve

    Delta chi=f-C/A, integral chi dvol=0,
    a2=*d chi.                                       (4)

The source has the positive scalar Laplacian Delta. In two dimensions
d*d chi=-(Delta chi)dvol, so (4) makes

    F2=(C/A)dvol.                                    (5)

Existence here concerns the actual fixed complete cusp, not a formal
finite matrix inverse. Its scalar zero eigenfunctions are constants.
On the orthogonal complement there is a positive spectral gap for this
fixed finite-area surface: outside a compact set the zero-angular
unitary scalar reduction is -partial_t^2+1/(4 ell^2), and nonzero angular
modes have the increasing cusp potential. The compact part and standard
Rellich/Fredholm argument isolate the constant zero eigenspace. This is
the same scalar cusp reduction already recorded in the form-parent
proof; no gap uniform in surface degeneration is asserted.

The right side of (4) is mean zero and L2. In a puncture coordinate the
smooth h_i,k_i make f decay exponentially relative to the cusp volume
density. Subtracting the constant C/A remains L2 because total area is
finite. The mean-zero inverse gives chi and d chi in L2. For its cusp
mean, a constant right side produces a logarithmic chi and a 1/y
tangential a2; its circulation tends to zero. Nonzero angular solutions
decay. Green's identity then gives the required complete-domain solution
and integral d a2=0 without a finite-cut boundary source. No arbitrary
Robin condition has been chosen.

The second-order solution is unique modulo closed zero-mode and gauge
data; these are fixed only for constructing the response at given
harmonic coordinates. Equations (3)--(5) do not prove all-order nonlinear
existence or a positive Hessian in every other parent sector.

Therefore the tree-level reduced leading potential is

    V_eff(epsilon U,epsilon V)
       =epsilon^4/(2 g6^2 A)
          kappa((-i sum_i[U_i,V_i])^2)+O(epsilon^5).  (6)

The coefficient follows from the inherited action and actual volume.
Keeping only the bare source S would give a shape-dependent integral
of |S|^2 and omit the relaxation (4). The bare quartic and the minimized
quartic are not the same calculation.

## 4. A genus-one restriction cannot exclude the larger architecture

For the present one-handle candidate, (6) vanishes iff [U,V]=0. Thus the
two sets of linear periods cannot be treated as arbitrary independent
non-Abelian flat directions. Near the identity the actual flat solutions
with trivial cusp holonomy have commuting unitary cycle holonomies;
their Cartan/Weyl family and its kinetic metric were already derived in
the full-flat-family note. The quartic is a same-action recovery of that
obstruction, not discovery of a unique vacuum or a preferred SM stratum.

Compact trace positivity also shows that a critical point of the leading
one-handle quartic cannot have a nonzero commutator: its scaling derivative
would be four times its positive value. This is a local leading-order
statement, not a no-go for flux sectors, other backgrounds or the full
nonlinear parent.

For g>=2 the zero condition is instead

    sum_i[U_i,V_i]=0.                                (7)

Individual commutators need not vanish. Two handles with (U1,V1)=(X,Y)
and (U2,V2)=(Y,X) have cancelling terms even when [X,Y]!=0. There is
also an exact group-level flat control: assign holonomies (G,H) to the
first handle and (H,G) to the second. Their surface relation is
[G,H][H,G]=1, with trivial puncture holonomy. This is not a proof that
this different carrier is generated or physically selected by OA. It
does prove why the one-handle commutativity conclusion cannot be silently
promoted to every carrier of the larger allowed architecture.

## 5. What has and has not been reduced

Within this specified gauge sector the first nonlinear period response
and the leading quartic coefficient are not additional input data.
They are inherited consequences of the same action, domain and metric.
The calculation carries the nonharmonic response rather than keeping
only a finite linear kernel or imposing a desired flat subset.

The classical flat minima still form a family; no measure, state,
nonzero period, genus, metric modulus or SM gauge stratum is selected.
Other spin, charged and fermion fluctuations remain. Their equations,
normalizations, quantum corrections and possible additional stationary
branches are not settled by the nonnegative quartic of this subsector.
The earlier gauge-free spin continuum is not gapped by this argument.

This proof needs independent analytic scrutiny, particularly the
complete-domain inverse in (4). Finite rational/quaternion controls can
check coefficients and opposite examples, but cannot certify that PDE.
All earlier six scientific checks remain unrun and unadmitted.
