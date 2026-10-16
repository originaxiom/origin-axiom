# Curved residual potential and the retained variational terms

Authored before execution. Positive field metrics, compact gauge parent,
metric, scalar supersymmetry and cut are supplied. Credit earlier
weave_curved_action/R28 for the gauged-Kähler/curvature/end method,
the full real-action Gaussian proof and actual charge/twist map, and
the previous normal nonabelian energy identity. No generic identity
below is claimed as a new literature discovery.

## One field metric and superpotential

On the internal Kähler surface use unit complex coframe zeta0,zeta1.
Its bar-volume wedge hol-volume is dvol. A_unit has chiral metric4,
P02 has metric1/2 and vector D has Gaussian1/2. These follow from
C_i=-2 A_unit,i and P=sqrt2 C2 in the actual prior unit-C metric.
With old derivative_i=sqrt2 unit_derivative_i, F_old=2F_unit.
Thus the reduced W=-Tr(P F_old) has global bulk expression

 W=-2 integral Tr(P02 wedge F20).

The old epsilon reduction differs by its explicit local derivative
primitive. It must remain in boundary/patch comparisons; W above is
not a proof that all affine local primitives glue without descent data.
The positive field metric, W and affine compact gauge action specify
the candidate gauged N=1 field-space construction, as in the credited
lower-dimensional parent. Full curved component/boundary completion is
a separate duty, not borrowed from an unmatched printed action.

Inverse Gaussian metrics give8|F20|^2 from P and|partial_A P|^2 from
the two A components. The moment derived below gives Tr(mu^2)/2.
All norms use the actual tensor metric. There is no independently
chosen scale or relative quartic. The same tensor bundles already give
the credited full curved fermion connection, not an assertion of a
new independent all-component supersymmetry check.

## Full four-dimensional curved energy identity

Let Fij be compact gauge curvature and let U,V be real components of
P=-2(U-iV). With a_P=i q, define

 Di U=Ei U+[Ai,U]+qi V, Di V=Ei V+[Ai,V]-qi U.

Writing Cij^k=[Ei,Ej]^k, exact second-jet commutators are

 [Di,Dj]U=Cij^k DkU+[Fij,U]+fij V,
 [Di,Dj]V=Cij^k DkV+[Fij,V]-fij U,

where f=dq is the real barK curvature. The moment is
mu=2i(Lambda F+[U,V]). The full residual potential is twice the sum
of squares of Lambda F+[U,V], F02-F13, F03+F12, and for each pair
(i,j)=(0,1),(2,3) the two terms DiU-DjV,DiV+DjU.

Let E=sum_i<j B(Fij,Fij)+sum_i(B(DiU,DiU)+B(DiV,DiV))
+B([U,V],[U,V]). For each complex pair define

 Ji=B(U,DjV)-B(V,DjU), Jj=-B(U,DiV)+B(V,DiU).

Use ACTUAL divJ=sum EiJi+(div Ei)Ji. Kähler compatibility and the
frame commutator cancel the first-jet frame terms. Pairing invariance
then gives

 divJ=2sum_pairs[B(DiU,DjV)-B(DiV,DjU)]
       -2B(Lambda F,[U,V])-Lambda(f)(|U|^2+|V|^2).

Set k=B(F wedge F)/dvol=2[B(F01,F23)-B(F02,F13)+B(F03,F12)].
Expanding ALL noncommuting squares gives

 V=2E+2k-2divJ-2Lambda(f)(|U|^2+|V|^2).             (1)

For the supplied total-space metric, a_P=3i dx/(2y),
Lambda f=3/(2ell^2)=-R_scalar/2 and|P|^2=4(|U|^2+|V|^2).
The final term is therefore R_scalar|P|^2/4. It is negative on this
metric, but V itself is the positive complete square sum. It is not
an isolated tachyon verdict or a freely inserted mass. Formula(1)
must retain gauge topology and BOTH boundary currents. On a flat
normal2slice it recovers the prior2E-2divJ identity exactly.

Standard Chern--Weil gives k dvol=d CS_B(A) locally, with
CS_B=-Tr(A dA+2A^3/3), and delta B(F wedge F)=2d B(delta A wedge F).
Both are checked in a genuine graded differential algebra with d^2=0;
form parity is not physical fermion parity. Globally a nontrivial
bundle may need patch terms/characteristic class rather than one CS
form. Neither the gauge topological sector nor the absolute vacuum
energy coupled to gravity is determined by setting residuals to zero.

## Field-space moment with a boundary

This is the KÄHLER FIELD-SPACE form used by N=1 gauging, NOT the
physical-time canonical symplectic form. With real tangent(a,u,v),

 Omega((a,u,v),(b,s,t))=-4 integral[omega wedge B(a wedge b)
                                      +B(u,t)-B(s,v)].

The factor4 follows from the actual chiral metrics and complex
coordinates X-iY. Compact gauge tangent is(Dalpha,[U,alpha],[V,alpha]).
Integration by parts with d omega=0 gives

 i_Xalpha Omega=delta H_bulk -4 integral_boundary omega B(alpha delta A),
 H_bulk=4 integral B(alpha,Lambda F+[U,V])
       =-2i integral B(alpha,mu).

Thus zero-boundary gauge parameters have the bulk moment. For nonzero
boundary values the differentiable FIELD-SPACE Hamiltonian instead is

 H_alpha=H_bulk-4 integral_boundary omega B(alpha,A).

Dropping the boundary term changes the Hamiltonian variation. At fixed
parameters and delta_beta A=D beta, exact cyclic algebra gives

 delta_beta H_alpha+H_[alpha,beta]
               =-4 integral_boundary omega B(alpha,d beta).       (2)

The right side is a Lie-algebra cocycle: skewness is a boundary total
derivative and its Jacobi sum is d B(alpha,[beta,gamma]). A commuting
Cartan cos/sin pair gives a nonzero local circle witness; common traces
on BOTH annulus ends cancel, whereas a parameter cut off at the other
end does not. This is a local collar/cocycle control. Whether such
angular parameters satisfy the actual global boundary and finite-norm
requirements is NOT established. It is not an added physical particle,
quantum affine level, anomaly compensation or 4D chirality.

## Necessary auxiliary boundary jets

For the smooth product-cut class whole V=C_t=0, D=G_t=0 as well.
Gaussian elimination requires mu=0 and the corresponding normal
covariant derivative of P=0. Lowest C_t alone implies neither. Linear
variation of the latter is D_n chi+[psi_n,P], retaining the nonlinear
bracket; it is not just partial_n chi. Its on-shell supersymmetry use
also needs the SAME fermion equations and boundary evolution. These
necessary jet conditions do not prove a closed nonlinear Sobolev
domain, a globally adapted tube, or the singular/gauge limit. The
earlier exact normal BPS family satisfies its normal residuals, not
thereby the complete global horizontal equations.

The actual global cutoff normal and possible high-pole modes of the
finite local chiral trace are further diagnostics to perform, not
verified failures. Full superspace/gauge/WZW and boundary/source
completion, global stationary charged spectrum, anomalies, foundational
selection of observed SM/three/gravity remain the active goal.
