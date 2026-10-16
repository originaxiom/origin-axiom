# Intrinsic cutoff plane and its compact gauge stabilizer

Authored before execution, in the supplied metric and real parent.
Standard Clifford isotropy and contact bracket reasoning are credited;
the task is their SAME-source actual tube application, not a new
general theorem. Finite embedded tube/base truncation only.

## Radius normal and contact plane

Set f=A|u+tau v|^2/y=alpha^2+beta^2. Actual frame derivatives of
(alpha,beta) are(beta/ell,0),(-alpha,beta)/(2ell),(1,0),(0,1).
Thus N=grad f=(2alpha beta/ell,(beta^2-alpha^2)/ell,2alpha,2beta).
Its horizontal fraction of norm squared is r^2/(4ell^2+r^2),
nonzero for r>0. The true tube normal is not exactly vertical.

J is the supplied parallel complex structure, eta=(JN)^flat and
P_H=I-(N N^T+JN(JN)^T)/normN^2. Let T=P_H E0. It has
norm(T)^2=4ell^2/(4ell^2+r^2)>0; JT=P_H E1.
Computing d eta with the actual frame brackets gives

 d eta(T,JT)=16ell^2 r^2/(4ell^2+r^2)^2>0.

T,JT annihilate f and eta. Hence their bracket is tangent to the
tube and eta([T,JT])=-d eta(T,JT)!=0. They and their bracket span
the real three-dimensional tangent space. This proves the required
contact/bracket-generating assertion directly, with no appeal to a
snippet about CR manifolds. For the flat product metric the analogous
horizontal T,JT have zero Levi value; that control keeps scope honest.

The scalar radius is invariant under modular S/T in the local zero-
section chart. It is not a periodic distance function on a whole fibre:
use only the embedded local tube. At the cusp a fibre cycle has length
sqrt(A/y), so no fixed positive radius fits below its half length for
all y. A varying tube needs another normal/contact calculation.

## Actual real principal boundary plane

Use the previously computed physical velocities v_a and scalar Noether
charge R_s=-i v4v5 in the actual source frame. The inherited vertical
minus-plane is Q0=(I+i R_s v2v3)/2. Its intrinsic extension is

 Q(N)=(I+i R_s v(N)v(JN)/normN^2)/2.

Clifford relations, J compatibility and actual Majorana reality make
this a C-real Hermitian rank-eight projector. Both Q v(N) Q and
Q v(JN) Q vanish. For a real tangent orthogonal to N,JN its symbol
commutes with Q. The complementary plane also has these properties;
no physical hand is selected. The actual coordinate/matrix calculation
tests these statements and detects the unchanged vertical-plane error.

Let Omega_i be the actual spin/R connection and H_i=E_i N+Gamma_i N.
Its faithful Clifford action gives

 nabla_i Q=(i R_s/2)[(v(H_i)v(JN)+v(N)v(JH_i))/normN^2
                         -v(N)v(JN) E_i(normN^2)/normN^4].

Thus the moving plane contributes connection/second fundamental terms.
Principal Green isotropy alone does not prove closure of the full
operator, on-shell supersymmetry or an elliptic/singular domain.

## Restricted compact gauges not all complex CR fields

Impose the candidate adapted version of A_t=0: the connection's
complex CR-tangent component vanishes. In that frame its compact
infinitesimal stabilizer satisfies(T-iJT)alpha_g=0. Both T alpha_g
and JT alpha_g are anti-Hermitian. Taking dagger separates them:
T alpha_g=JT alpha_g=0. Applying the commutator shows
[T,JT]alpha_g=0 as well; the preceding span proves all tangential
derivatives vanish on each connected cut patch. A finite unitary
gauge transformation has anti-Hermitian g^-1 dg and obeys the same
argument. Global bundle compatibility can further restrict constants.
External V=0 retains its previously declared external gauge cost.

This implication is FALSE for arbitrary complex fields. The local
antiholomorphic coordinate bar(tau) is nonconstant and annihilated
by T-iJT. The exact real Lie-algebra jet-norm test and complex control
keep a gauge restriction from becoming a false matter-spectrum kill.

The prior Kähler field-space cocycle -4 integral_boundary omega
B(alpha_g,d beta_g) vanishes on this internally constant stabilizer.
Locally d(theta)=eta/(2r^2)-e0/(2ell), hence

 T theta=-2ell/(4ell^2+r^2), JT theta=0.

The cos/sin angular pair used in the previous collar example fails
the adapted tangent condition. Its nonzero unconstrained cocycle
was valid, but not an admitted charge of this boundary class.

This is conditional on the proposed adapted whole-superfield trace,
not a derivation of that trace from the action. Actual curvature/normal
jets, full curved SUSY variation, nonlinear boundary source/response,
singular limit, gauge-vector recovery and SAME global charged physics
remain. No basis for a programme-wide no-go, index/three or gravity.
