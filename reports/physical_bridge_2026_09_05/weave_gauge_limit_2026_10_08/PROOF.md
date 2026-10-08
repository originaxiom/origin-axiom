# Classical gauge convergence does not control the end current

Conditional analytic result for the supplied parent, fixed complete
domain and stationary family. This diagnoses the old covariant inverse
current, already shown not integrable; it does not construct a local
fermion phase or prove that every quantum completion is discontinuous.

## Local coefficient of the actual operator

The physical kinetic metric is diag(Omega^2,1/2,Omega,Omega).
At an orthonormal point set Omega=1 after retaining the metric
connection. Normalize the fields with H=diag(1,1/sqrt(2),1,1).
Reorder the metric-normalized target as (row1,-row0,-row3,row2).
With Fourier Dbar=p=i*kx-ky, Dz=-conjugate(p), the actual mass formula
becomes diagonal in its principal part:

    M0=diag(Dz,Dz,Dbar,Dbar)=partial_x+J partial_y,
    J=diag(-i,-i,i,i), Jdagger=-J, J^2=-1.

All Q/R terms join the first two slots to the last two. Thus in this
frame their zero-order matrix Phi has diagonal two-by-two blocks zero;
tr(Phi)=tr(J Phi)=0, including their covariant first derivatives.
This remains true for matrix-valued Q/R and both neutral condensates.
No diagonal soft bosonic mass is imported into M.

Here is a local calculation which checks the effect of these potentials
rather than assuming all Dirac-type potentials have the same density.
Write M=partial_x+J partial_y+B and C=Bdagger. In flat normal frames,
its adjoint is -partial_x+J partial_y+C. For Hplus=Mdagger M and
Hminus=M Mdagger, write H=-Delta+a_i partial_i+b. Direct composition gives

    ax_plus=ax_minus=C-B,
    ay_plus=J B+C J, ay_minus=B J+J C,
    b_plus=-Bx+J By+C B,
    b_minus=Cx+J Cy+B C.

Completing the connection square gives omega_i=-a_i/2 and

    E=-b+(partial_i a_i)/2-sum_i a_i^2/4,
    H=-(nabla^2+E).

Cyclicity and J^2=-1 give tr(ay_plus^2-ay_minus^2)=0 and equal
traces of the connection divergences. Consequently

    tr(Eplus-Eminus)=tr(Bx+Cx-J By+J Cy).             (1)

This is an arbitrary-matrix identity, not a commuting-mass assumption.
Adding the actual off-block Phi and Phidagger changes its right side
by zero. Curved normal-frame terms give the old zero-potential local
Dolbeault density; metric curvature terms proportional to rank cancel.
The potential calculation is tensorial at a point, so choosing normal
frames here does not discard curvature or the spin connection.

At zero potential the virtual twisting bundle is

    E_internal tensor (2S-1-S^2).

Its rank and degree-two Chern character vanish identically:
2-1-1=0 and 2s-0-2s=0; tensoring E_internal and including the Todd
factor does not change that degree-two zero. Equivalently, each weight
beta gives 2(1-beta)-(-beta)-(2-beta)=0 with zero rank. This is pointwise
curvature cancellation, not the generally nonzero complete cusp index.

The ordinary compactly smeared heat expansion has a0 proportional to
rank and a2 proportional to tr(E+scalar_curvature/6). These are the
standard formulas in Vassilevich,
https://arxiv.org/html/hep-th/0306138, equations2.1--2.4,4.26--4.27
and the matrix-insertion explanation at7.30. On each fixed compact
support, (1) and the bundle identity imply

    Str_internal(eta_R exp(-epsilon Dint^2))=O(epsilon). (2)

The complete manifold has no physical boundary at the transition of a
smooth smearing function; this is not a truncated-domain heat problem.
Local elliptic heat asymptotics on fixed compact supports are analytic
inputs. No uniformity in R is asserted or required in (2).

## The two cutoffs have different jobs

Let alpha(x) be one of the prior smooth four-dimensional color parameters,
internally parallel. Take a smooth eta_R(t), equal to1 before cusp
height R and0 after R+1. Its derivative is bounded independently of R.
Set alpha_R=eta_R alpha. The background still has product form;
only the gauge variation has acquired an internal component.

The prior finite-cutoff Ward identity holds also for this parameter:

    B_e,T(alpha_R)
      =Str(chi_T alpha_R exp(-e D^2))
       +1/2 Str([D,chi_T] D^-1 exp(-e D^2) alpha_R).

B is Omega(delta_alpha D)/i with the same physical charge-counting
convention. For T>R+1, chi_T=1 on the parameter support. Moreover
[D,chi_T] is Clifford multiplication by d chi_T; on the diagonal of
the trace its product with alpha_R is identically zero. The second
term therefore vanishes EXACTLY, not by discarding a small tail.
All traces are legitimate smoothing traces with compact insertions
and the prior external gap.

The first term factors into the bounded external chiral heat insertion
and (2), separately in every unbroken representation. Hence for every
finite R,

    B(alpha_R):=lim_e->0 lim_T->infinity B_e,T(alpha_R)=0. (3)

For the uncut alpha, the earlier result instead is

    B(alpha)=sum_Rrep integral_0^infinity
                        a_Rrep(s) S_Rrep'(s) ds.        (4)

The representation label Rrep is not the cutoff height R. On the
previous gapped torus probes, the slow-field limit of (4) has nonzero
color coefficient for every nonzero n: -1 at n=1, -3 at n>=2, reversed
for negative flux. Thus there are sufficiently large FINITE external
metric scales with B(alpha)!=0. No numeric threshold scale is claimed.
The finite-cutoff local and global limits do not commute:

    lim_R->infinity B(alpha_R)=0 != B(alpha).

This does not refute the older continuum heat result or establish a
consistent anomaly from a covariant current. It identifies a second
defect of this particular current as a candidate quantum variation.

## Why classical admission did not settle this

Cusp area is ell*exp(-t)dt. For any smooth unit-width transition with
derivative bounded by C, the lost scalar norm and derivative norm obey

    ||1-eta_R||^2 <= ell exp(-R),
    ||d eta_R||^2 <= ell C^2(1-exp(-1)) exp(-R).

External alpha and its derivatives have finite norms. Since the
unbroken generator commutes with the internal background, these
bounds prove alpha_R->alpha in the classical scalar graph norm,
and the corresponding classical gauge-field variations converge in
their kinetic norm. Smooth approximation preserves these bounds.

Equations(3)--(4) prove B is NOT continuous in that topology.
There is no bounded linear extension agreeing with these values:
if |B(f)|<=K||f||_graph, then B(alpha-alpha_R)->0, contradicting
B(alpha)!=0. The end evaluation f->lim_t->infinity f, on parameters
where the limit exists, is another explicit discontinuous functional
in this norm: it is0 on every eta_R and1 on the constant.

Thus the classical Hilbert-space completion does not itself retain
the end data needed to infer quantum gauge continuity. This is an
operator/topology distinction, not an observer or qualia derivation.
It does not authorize forbidding the normalizable gauge transformation.

## Consequence for the actual local completion task

A genuine local regulated Gaussian must specify its end/reference
state and its gauge transformation, or prove an appropriate continuity
and cancellation statement. Compactly supported gauge invariance alone
cannot be extended to the normalizable constant gauge mode using only
the classical graph bound above.

Witten--Yonekura, https://arxiv.org/html/1909.08775, section2.1,
keeps the bulk state and boundary-state pairing in its partition
function. That is a methodological example, not an identified end
state for this complete cusp. Likewise the previous nonlocal paired
phase was defined only for parallel fields; it supplies no result
about alpha_R gauge directions without an extension of its prescription.

An end-sensitive topology or an additional compensating response may
alter the conclusion for a different completed action. Neither has
been selected here. The existing stationary saddles, zero-flux minima,
source/silver alternatives and full foundational SM/TOE duties remain.
