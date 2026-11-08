# The actual core's static circulation response and its flux matching

2026-11-08. **Author hand derivation, UNREVIEWED.** No scientific
import, collection or execution. This is an analytical step toward the
actual core problem while the earlier six-control packet is being prepared
for independent review. It is outside those six controls and does not
claim completion of the full core response or the physical mission.

## 1. Fix one actual channel and its retained data

Use the same supplied complete punctured surface, metric, residual-zero
stationary background (A0,q0,r0) and gauge parent as
[the gauge-response derivation](SAME_ACTION_GAUGE_BOUNDARY_RESPONSE_AND_CUBIC_2026_11_08.md).
Take one globally parallel Hermitian generator H in its unbroken gauge
algebra, commuting with both spin fields and their adjoints. Let
c_H=kappa(H^2)>0. This compact/gauge/physical identification remains an
input, not a derivation from the registering principle.

Cut the actual surface at the cusp circle y=Y, x mod 1. Write C for
its connected compact core, T for the complete tail, and

    A_c=Area(C)>0, A_t=ell^2/Y, A=A_c+A_t.

Orient the surface by dx wedge dy. The induced core boundary orientation
is -dx; the induced lower-tail boundary orientation is +dx. The finite-cut
perturbation has circulation b: in the tail frame a_x=b H on that circle.
Here b is the real circulation in the retained frame and flux history,
not a principal logarithm recovered from an isolated Wilson-loop trace.
In this STATIC commuting channel the action for the perturbation is

    E_region = c_H/(2g6^2) integral_region f^2 dvol,
    da = H f dvol,                                     (1)

with q0,r0 retained. It follows directly from the old residual-zero
parent: the new moment is fH and all spin residuals remain zero.
The original background curvature is not set to zero or counted again.

The analysis below allows every smooth core one-form variation with the
specified tangential trace. It is not a restriction to a one-dimensional
radial model inside the core. It retains gauge equivalence and flat
core periods rather than assigning an inverse to their zero modes.

## 2. The fixed-framing, zero-added-flux core response is exact

First keep the same connection bundle/end framing, so the perturbation
is a globally defined H-valued one-form. Stokes gives

    integral_C f dvol = -b.                           (2)

Cauchy--Schwarz, in the actual core metric, gives

    integral_C f^2 dvol >= b^2/A_c.                    (3)

Equality requires and is attained by constant f=-b/A_c. To check that
attainment is compatible with the FULL specified boundary one-form,
observe that C has nonempty boundary and retracts onto a graph. Hence
H^2_dR(C)=0, so the two-form (-b/A_c)dvol has a smooth primitive a_*.
Its boundary integral is the required -b. The difference between its
tangential trace and the prescribed boundary trace is therefore an exact
one-form on the circle. Extend its scalar primitive smoothly into C and
subtract its differential from a_*. This corrects the trace without
changing curvature. A further gauge function zero on the boundary can
put the result in a Coulomb slice if needed. No extra curvature energy
or geometric approximation is introduced by these exact adjustments.

Thus the actual static core on-shell functional and outward response are

    Gamma_c(b)=c_H b^2/(2g6^2 A_c),
    pi_c=c_H b/(g6^2 A_c).                            (4)

The coefficient 1/A_c is independent of detailed core shape in this one
static circulation channel. It is not the full angular or finite-frequency
Dirichlet-to-Neumann operator.

The core minimizer is NOT unique as a field. Closed relative one-forms
with zero tangential boundary trace, modulo gauge functions zero at the
boundary, remain. Their classes form H^1(C,boundary C); for a genus-one
core with one boundary this has real rank two per H direction. The
curvature, energy and response (4) do not depend on those flat periods.
Their kinetic norms and charged probes can depend on them. This preserves
the physical zero-mode duty rather than eliminating it by notation.

## 3. The tail fixes the seam circulation in this sector

The earlier actual tail calculation gives

    Gamma_t(b)=c_H b^2/(2g6^2 A_t),
    a_x(y)=H b Y/y,  f_t=b/A_t.                       (5)

These are an on-shell exterior and its actual positive norm, not a
source-free global zero mode. Summing (4) and (5) and varying the common
trace gives

    (1/A_c+1/A_t)b=0.                                (6)

Both areas are positive, so b=0. This resolves the old open amplitude
question in THIS source-free, fixed-framing, static commuting channel:
the nonzero 1/y tail cannot be assigned arbitrarily and declared a
global stationary solution. Its required core momentum has the wrong
value unless the joined problem changes.

Equation (6) does not remove the flat relative core classes, nonzero
angular fields, time dependence, non-Abelian branches or matter sources.
It is not an exclusion of the larger registering architecture or of
the full parent. The field configuration with b!=0 remains finite-energy;
it simply does not satisfy the joined stationary equation under these
particular constraints.

## 4. Retain the global flux/gluing datum instead of silently discarding it

There is a distinct allowed problem with fixed additional flux Phi along
H. When H is a cocharacter, exp(2pi i H)=1, take Phi=2pi n, n integer,
and retain the circle transition

    U(x)=exp(-i Phi x H).

The actual inhomogeneous gauge law gives a_core=a_tail-Phi H dx in
these two frames. The fields are identified by U; they are not two
unrelated boundary values. Stokes now gives

    integral_C f dvol=Phi-b.                          (7)

This is a changed relative gluing/flux datum, not a contradiction of
(2) or a gauge choice that permits forgetting the marking. The same
core argument gives the exact reduced static action

    Gamma(b;Phi)=c_H/(2g6^2) [ (Phi-b)^2/A_c+b^2/A_t ]. (8)

Its common-trace stationary equation has the unique solution

    b_*=Phi A_t/A,
    f_c=f_t=Phi/A,
    Gamma_on-shell=c_H Phi^2/(2g6^2 A).              (9)

The second derivative in the seam circulation is positive. All the flat
core periods remain; this is not full Hessian stability. Moving the
artificial cut changes b_* but leaves the uniform physical curvature
and total energy in (9) unchanged. In particular

    a_x(y)=H Phi ell^2/(A y).                        (10)

The exterior amplitude is therefore forced once the ACTUAL flux sector,
metric and action are fixed. Phi is still independent discrete global
data. Calling (10) a fully parameter-free vacuum would hide that input.

For smooth matching, use the same constant curvature in a collar on both
sides. The difference of their local connection primitives is closed;
the retained transition and a smooth gauge function make the primitives
and jets agree. All fields commuting with H retain their gluing. This
provides a full static solution of the commuting gauge equation, rather
than only a boundary energy estimate.

## 5. Relationship to actual magnetic stationary solutions

The parent variation supplies a further conditional check. At (9) its
orthonormal moment is the parallel constant (Phi/A)H. Its covariant
derivative vanishes and it commutes with q0,r0 and their adjoints.
Thus connection and scalar first variations vanish in every E8 direction,
with the same complete finite-energy variation class and vanishing cutoff
errors. The kinetic signs and interactions are the old parent ones.
This does not prove stability, a gravitational metric equation or a
selected physical state.

The global flux sector can be realized using the already supplied spin
line and a commuting cocharacter. Its spin connection satisfies
ds=-dvol/(2ell^2). Twisting the gauge bundle by the circle connection
2nH s gives added curvature -nH dvol/ell^2. For the once-punctured
torus A=2pi ell^2 this is Phi=-2pi n, and (10) becomes a_x=-nH/y
in the source cusp gauge. It preserves the original limiting peripheral
because exp(2pi i nH)=1, while changing full connection and charged
operator data. Its full transitions must be retained on all 248 fields.

At ell=1, H=Z, the old principal source's energy is recovered:

    E=pi n^2 kappa(Z^2)/g6^2.

This is the already owned
[magnetic stationarity result](../weave_magnetic_stationarity_2026_10_08/PROOF.md),
now reconstructed through core/tail response. Its global cocharacter
realization, nonzero-moment stationarity and charged instability are
prior work, not new discoveries. The source's principal-background
negative directions do not automatically classify a different coupled
two-spin background; its full Hessian needs its own calculation.

The new response around the residual-zero seed likewise must not be
used unchanged as the full fluctuation operator about a nonzero-moment
solution. Retain its moment times quadratic-curvature term. A positive
seam Hessian in (8) cannot conceal negative charged directions elsewhere.

## 6. What this closes and what it leaves open

This closes the actual zero-frequency mean-circulation core response and
stationary seam-amplitude duty in one physical commuting sector. There
is no new adjustable Robin coefficient or free boundary amplitude once
the geometry, flux sector and parent are fixed. The result recovers,+rather than erases, the old magnetic examples and their costs.

It leaves the actual finite-frequency/angular core matrix, flat-period
state selection, non-Abelian/matter response, full fermion operator,
charged stability and weak-current spectrum open. The foundational map
to the supplied parent/metric/flux data is not earned by this solution.
No chiral SM3, observed parameter or gravitational result is claimed.

The proof requires independent source review and future discriminating
controls for orientations, zero modes, flux gluing, actual area dependence
and cut-independent stationary energy. It is outside the original six
unrun controls; do not count their future execution as verification of
these new core claims.
