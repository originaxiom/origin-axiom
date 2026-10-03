# R81 authored application: compact boundary versus complete end

Pre-execution. Uses known mathematics explicitly; original novelty not claimed.

## D1. The published result is already twisted

Wu--Zhang, [arXiv:2109.01776v1](https://arxiv.org/pdf/2109.01776v1),
Proposition3.3 pp12--13 treats a metric on a vector bundle with connection
over a compact Riemannian manifold with smooth boundary. Prescribed
positive boundary data determine a unique harmonic metric. We require
connected X with NONEMPTY boundary, smooth D and smooth compatible data;
no closed component is admitted by the scalar Dirichlet barrier argument.
For our application D is flat. No reductivity assumption is used here.

Their convention D=D_H+psi_H agrees with D=A+Psi; harmonicity is
d_A^*Psi=0, so our I=-2d_A^*Psi vanishes. They evolve the bundle metric,
not an ordinary single-valued map to a target on X. A scalar solution of
Delta u=-|D_K^*psi_K| with zero boundary controls accumulated tension
along the flow. Metric-comparison identities control H and its inverse;
the proof invokes smooth convergence/regularity, not a finite matrix
test. We import that analytic result, rather than claiming our finite
tests establish PDE existence. Independent analytic review still owed.

For SL(n,C), use its parallel determinant trivialization. The trace
equation at a harmonic metric is Delta log det H=0. Determinant-one
boundary data give log det H=0 by the scalar maximum principle, hence
det H=1 throughout X. Positive boundary metrics extend smoothly into X
(the metric fibre is contractible); the theorem may use any such K as
initial metric. Uniqueness concerns THIS fixed boundary value problem,
not a unique vacuum when boundary data are allowed to vary.

The complete noncompact theorems elsewhere in the paper add analytic
stability, bounds and base hypotheses. They are NOT obtained by simply
sending this finite boundary to infinity. No Kahler identification,
pluriharmonicity or Higgs-bundle result is imported onto our 3-manifold.

## D2. Apply to the actual nonsplit W without changing its holonomy

Take a smooth compact truncation X_R of R75's threefold-cyclic cover.
It deformation retracts the cusped manifold, preserving its fundamental
group and the verified flat rank-five representation W. Restriction to
X_R does not kill its nonzero extension class: a flat complementary
subbundle would give a splitting of that SAME representation. Choose
the restricted smooth base metric and ANY smooth positive determinant-one
boundary datum. D1 supplies H_R, with F_D=0 and I(H_R)=0.

R76's supplied static potential is

    V=(2/g7^2) integral (|F_D|^2+|d_A^*Psi|^2), g7^2>0.

Its first derivative vanishes at zero residuals for arbitrary smooth
bulk field/metric variations consistent with the boundary data; varying
norms/volume multiplies zero too. Thus H_R realizes a zero-potential
stationary point of this specified BARE functional, not merely of the
auxiliary harmonic-map energy. Other fields are zero. No additional
boundary action, physical end law or quantum state is thereby selected.
This is existence and stationarity, not an explicit computed H_R for W.

Let P project orthogonally onto the actual invariant four V inside W,
xi=5P-4Id, eta the upper cross-block. R41/R75 give on X_R

    0 = 5 integral_X_R |eta|^2
        +2 integral_boundary tr(xi Psi(n_out)).

Nonsplitting forces eta not identically zero, so the integrated outward
flux is strictly negative. This is a boundary response to K, not an
independently selectable current in addition to the same solution.
The actual W index and exterior-square calculations remain R75's;
no physical chiral fermion count follows from this metric existence.

## D3. Exact global comparator, with an unsplit loop

Use periodic x,y of period1 on T2, Euclidean metric, and
s in[-a,a], a=pi/4. In a GLOBAL smooth frame put

    D=d-N dx, N=E01, J=diag(1,-1), f=-log cos(s),
    H=diag(exp(f),exp(-f)), G=H^(1/2).

Parallel transport for D=d+C0 satisfies v'=-C0 v, so the x holonomy
is L=exp(N)=Id+N, not exp(-N). Its only eigenline is span(e0).
An invariant complement would also be an eigenline and cannot exist.
Thus this is a genuine global nonsplit extension over a periodic loop,
unlike R80's simply connected s-only connection. It is not R75's W.

In the orthonormal frame C=G C0 G^-1-dG G^-1,

    C_s=-f'J/2, C_x=-exp(f)N, C_y=0.

The sign of the radial term matters. [J,N]=2N, so
F_sx=partial_s C_x+[C_s,C_x]=0, and all other F components vanish.
With A=(C-Cdag)/2, Psi=(C+Cdag)/2, the full moment is

    I=sum_i(partial_i(C_i+C_i dag)+[C_i,C_i dag])
     =(-f''+exp(2f))J=0,

because f'=tan(s), f''=sec(s)^2=exp(2f). No off-diagonal equation
or connection term is dropped. At every s, the holonomy is G L G^-1,
so changing metric has not split or changed the flat local system.
Both eigenvalues of H are positive/bounded on this compact interval.

The upper extension has |eta|^2=sec(s)^2. With xi=J,
tr(xi Psi_s)=-tan(s). Unit torus area gives

    integral_X |eta|^2=2tan(a)=2,
    integral_boundary tr(xi Psi(n_out))=-2tan(a)=-2,
    2 integral_X |eta|^2+2 flux=0.

Setting the flux to zero falsely reports4 instead of0. Flipping C_s
while retaining C_x spoils F_sx and I. The supplied identity connection
with H=Id is a split zero-current comparator. This comparator is smooth,
finite energy and stationary for the same positive residual functional.
Its product geometry, boundary data and interval are supplied inputs.

## D4. The limit and gluing do not come for free

For the secant comparator, a approaches pi/2 from below:
2tan(a) diverges, H and its inverse cease to be bounded, and the metric
does not extend smoothly at the pole. Identifying the two s ends as a
circle is also invalid: integrating f''=exp(2f)>0 over a periodic circle
would give0>0. These are failure controls, not proofs about other metrics.

Generally, suppose H_R on an exhaustion had a smooth positive local
limit H_infinity on the COMPLETE finite-volume boundaryless base, still
flat/harmonic, with finite integral |Psi|^2. R41's cutoff argument would
force the invariant subbundle to split, a contradiction for W. Therefore
this whole collection of limiting properties cannot hold simultaneously.
No particular failure (energy growth, degenerating metric, missing smooth
limit, surviving physical boundary/source or loss of global invariance)
is chosen by this argument. Do not replace it with a claimed computed
blow-up rate for W. Compact-boundary existence and the complete-domain
obstruction are compatible statements with different domains.

If two pieces are glued with a smooth matching flat connection/positive
metric, their interface normals are opposite and projector fluxes cancel
when a COMMON invariant subbundle extends across the join. The whole
architecture must still pay its bulk balance. It cannot erase a current
by not counting its partner. A relation that removes that invariant
subbundle, introduces genuine sources/nonflatness, or changes the global
domain escapes this particular proof, but must supply its own coupled
equations and conserved currents. This is where act/register provenance
must be retained; it is not a derivation of an observer or qualia.

## Evidence boundary

The local comparator identities get finite symbolic and independent
rational checks. The general Dirichlet theorem is credited imported
analysis; its W application and complete-limit/gluing scope are authored
arguments awaiting nonauthor review. No whole-repository green, selected
boundary, normalized SM spectrum, anomaly matching, observable, action
from genesis or full TOE follows from this packet.
