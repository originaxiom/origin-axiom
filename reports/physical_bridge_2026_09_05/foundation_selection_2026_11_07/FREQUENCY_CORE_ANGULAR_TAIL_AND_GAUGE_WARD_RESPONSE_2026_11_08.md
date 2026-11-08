# The frequency-dependent core, angular tail and a forced gauge identity

2026-11-08. **Author analytical derivation, UNREVIEWED.** No science
import, collection, CAS or numerical calculation. New claims are outside
the six frozen gauge-response controls. This is a conditional calculation
in the SAME supplied residual-zero gauge-centralizer sector, not a
derivation of its E8 parent, fields, geometry or physical state from OA.

## 1. Retain the actual channel, geometry and gauge constraint

Reuse [the parent and zero-angular response](SAME_ACTION_GAUGE_BOUNDARY_RESPONSE_AND_CUBIC_2026_11_08.md),
[the actual static core](ACTUAL_CORE_MEAN_RESPONSE_AND_FLUX_SEWING_2026_11_08.md)
and the source's [real gauge-fixing distinction](../word_architecture_audit_2026_10_17/SAME_ACTION_REAL_GAUGE_FIXING_AND_ONE_LOOP_WEIGHTS.md).
The core is the actual smooth compact truncation, with its inherited
metric and bundles. The tail has x mod 1, y>=Y and Omega=ell/y.
Work in one globally parallel unbroken gauge coefficient H, with
c_H=kappa(H^2)>0; linearization treats its real coefficients by the
same Maxwell operator. Both spin fields and all other E8 sectors remain
in the parent, though this linear channel decouples from them.

Take Euclidean external momentum p and s=|p|^2>0. Decompose the external
vector into its p-transverse and longitudinal parts. Setting the latter
to zero is a gauge chart. The longitudinal vector Euler equation still
imposes the Gauss condition delta alpha=0 on the internal one-form
alpha. It must not be omitted after gauge fixing. The internal equation is

    delta d alpha+s alpha=0, delta alpha=0.            (1)

Let f=*d alpha, and use the positive scalar Laplacian Delta=delta d.
On an oriented surface delta(f dvol)=-*df, so (1) is equivalent to

    alpha=*df/s,  (Delta+s)f=0.                       (2)

For the upper core boundary, its outward normal points toward +y.
If alpha_x=b(x) there, (2) gives

    partial_n f=-s b(x)/Omega(Y),
    pi_core(x)=-f_boundary(x).                        (3)

The momentum is per coordinate dx. The common prefactor c_H/g6^2
is suppressed until it is restored in the action. The full conformal
factors remain in Delta and its physical normal. For transverse external
vectors, the same parent yields the scalar equation (Delta+s)v=0,
with the ordinary positive scalar gradient/kinetic quadratic form.

## 2. One actual geometric operator determines both core responses

Let D_c(s) map a scalar boundary value u to Omega partial_n v, where
(Delta+s)v=0 in the actual core and v|boundary=u. Its boundary pairing
uses dx. The positive energy identity gives

    <u,D_c(s)u>_boundary=integral_C (|dv|^2+s|v|^2)dvol.

For s>0 this scalar Dirichlet-to-Neumann map is positive and invertible
between the usual smooth/Sobolev trace spaces. Equations (2)--(3) give
the internal connection response

    R_c(s)=s D_c(s)^-1.                               (4)

This is an operator identity, not a scalar inversion of a selected
Fourier mode. No assumption that D_c commutes with a boundary angular
projection is made. It derives the relation between the two boundary
responses from the given action and geometry.

Here are the existence ingredients. The Neumann problem for f has
coercive form integral(|df|^2+s|f|^2) on H1(C), with bounded boundary
source -s integral b f dx. Lax--Milgram and smooth elliptic regularity
give its unique solution for smooth b. The Dirichlet problem is handled
on H1_0 by the same form and a trace lift. These standard elliptic
ingredients are used on the smooth FIXED compact core, not uniformly
over degenerating metrics or over the complete noncompact surface.

## 3. A spectral formula for the actual core and its zero limit

Let phi_j be an orthonormal scalar Neumann eigenbasis in L2(C,dvol):

    Delta_N phi_j=lambda_j phi_j,
    lambda_0=0, phi_0=1/sqrt(A_c), lambda_j>0 for j>=1.

This basis follows from the nonnegative Neumann H1 quadratic form,
compact Sobolev embedding on C and the spectral theorem. Connectedness
makes its scalar zero eigenspace exactly the constants. Define

    B_j[b]=integral_boundary b(x) phi_j(x) dx,
    B[b]=integral_boundary b(x) dx.

Green's identity applied to (2)--(3) gives

    (lambda_j+s)<phi_j,f>=-s B_j[b].                  (5)

Consequently the connection response, in its quadratic-form sense, is

    <a,R_c(s)b>=conj(B[a])B[b]/A_c
       +s sum_(j>=1) conj(B_j[a])B_j[b]/(lambda_j+s). (6)

For smooth traces the expression is understood through the convergent
elliptic solution/energy pairing; boundary eigenfunction series need not
be treated as an absolutely convergent pointwise expansion. The j=0
term has been evaluated BEFORE s tends to zero. Dropping it would
incorrectly predict a vanishing static mean response.

In particular,

    R_c(0)b = B[b]/A_c,                              (7)
    <1,R_c(s)1>=1/A_c
             +s sum_(j>=1) |B_j[1]|^2/(lambda_j+s).

Thus the old 1/A_c is a rank-one STATIC circulation response on the
whole boundary space; it is not 1/A_c times the identity on all angular
data. The frequency-dependent weights and Neumann eigenvalues depend
on the actual core geometry. They are derived once that metric is fixed,
but have not been numerically computed or foundationally selected here.

Differentiating (6) gives

    <a,R_c'(s)b>=sum_(j>=1)
            lambda_j conj(B_j[a])B_j[b]/(lambda_j+s)^2
                =<alpha_a(s),alpha_b(s)>_L2(C).      (8)

The second equality follows independently by reconstructing alpha
from (2) and integrating its gradient expansion. It fixes the actual
core contribution to the connection norm. The common action factor is
c_H/(2g6^2), consistent with the source's real one-form kinetic metric;
no additional boundary kinetic matrix is supplied.

Equivalently, D_c'(s) is the scalar Poisson-solution norm, and

    R_c'(s)=D_c^-1-s D_c^-1 D_c' D_c^-1 >=0.          (9)

The order of the factors in (9) matters. D_c-sD_c' is the positive
gradient energy form. The response/norm principle is old work; (6)--(9)
apply it to the actual compact-core gauge channel and retain its constant
mode rather than substituting a proxy matrix.

## 4. Relative one-form zero modes are not the scalar constant mode

The scalar Neumann constant in (5) and the relative harmonic one-forms
are different objects. At s=0 one may add any h with dh=delta h=0 and
zero tangential trace. Their space is H1(C,boundary C), real rank two
for the genus-one one-boundary core. Formula (2), which divides by s,
must not be used at zero to declare those fields nonexistent.

The coexact solution *df/s at s>0 is orthogonal to those relative
harmonic forms, by Green's identity and their zero tangential trace.
If the forms are retained as core variables z_i h_i, their partially
reduced quadratic action has the block s z_dagger G z, where
G_ij=integral_C <h_i,h_j>dvol. It supplies a metric fixed by the same
core geometry, not a choice of independent flavour weights.

This CORE block is not yet the whole physical kinetic matrix of globally
matched flat modes. Normal traces, longitudinal vector currents and any
angular tail compensators must travel with them. A relative core class
does not by itself establish a normalizable global Weyl particle. Keep
the zero modes until those full-field matching equations are solved.

## 5. The complete angular tail is explicit in this linear channel

Put k_n=2pi n and nu=sqrt(1+4ell^2 s), eta=nu/2. For n!=0 the scalar
equation in (2), or the transverse vector equation, becomes

    u''-[k_n^2+ell^2 s/y^2]u=0.                      (10)

The decaying solution, normalized at Y, is

    P_n(s,y)=sqrt(y/Y) K_eta(|k_n|y)/K_eta(|k_n|Y).

Set

    L_n(s)=|k_n| K_(eta-1)(|k_n|Y)/K_eta(|k_n|Y)
                                      +(eta-1/2)/Y.

Then the two exact outward tail responses are

    D_t,n(s)=L_n(s), R_t,n(s)=s/L_n(s), n!=0.         (11)

Indeed P_n'(Y)=-L_n. The exterior normal is the opposite core normal;
the connection's fixed trace requires f'(Y)=-s b_n, and its outward
momentum is +f(Y), giving the second formula. Scalar/vector response
weights remain different, despite the common differential equation.

For n=0 the correct normalizable power solution instead gives

    D_t,0(s)=(nu-1)/(2Y),
    R_t,0(s)=Y(1+nu)/(2ell^2).                        (12)

Thus R_t(s)D_t(s)=sI for s>0, with a removable zero-mode limit in (12).
At s=0,

    D_t,n(0)=|k_n|, R_t,n(0)=0 for n!=0,
    D_t,0(0)=0, R_t,0(0)=Y/ell^2.

The nonzero-angular connection profile at zero, in its Coulomb chart,
has alpha_x=b_n exp(-|k_n|(y-Y)) and
alpha_y=i sign(k_n)b_n exp(-|k_n|(y-Y)). Its squared one-form norm
per |b_n|^2 is 1/|k_n|, equal to R_t,n'(0). Its static curvature is
zero; the corresponding boundary gauge and longitudinal vector data
must be included before assigning any physical degree of freedom.

The Bessel input is standard, personally checked in NIST DLMF:
[equation 10.25.1](https://dlmf.nist.gov/10.25.E1),
[derivative recurrence 10.29.2](https://dlmf.nist.gov/10.29.E2),
[positive integral 10.32.9](https://dlmf.nist.gov/10.32.E9),
[decaying asymptotics 10.40.2](https://dlmf.nist.gov/10.40.E2), and
[half-integer check 10.39.2](https://dlmf.nist.gov/10.39.E2).
The modified-cylinder notation in 10.29 includes exp(i*pi*eta)K_eta;
it yields K_eta'=-K_(eta-1)-eta K_eta/z. Ignoring that phase would
give the wrong derivative sign. The OA channel reduction is the hand
derivation above, not a theorem attributed to DLMF.

## 6. The boundary gauge variables obey an exact quadratic Ward constraint

For s>0 and a single angular mode write v_mu=v_T,mu+p_mu v_L/sqrt(s),
where p dot v_T=0. Under a boundary gauge parameter epsilon,

    delta b=i k_n epsilon, delta v_mu=i p_mu epsilon.

The invariant scalar source is

    B_n=b_n-(k_n/s) p dot v_n.

The tail quadratic action, with its source prefactor restored, is

    Gamma_t^(2)=c_H/(2g6^2) sum_n [
          D_t,n |v_T,n|^2+R_t,n |B_n|^2 ].           (13)

Its boundary matrix annihilates (k_n,p_mu) exactly. This retains the
longitudinal/Gauss relation and prevents calling b_n an independent
physical scalar in every angular sector. The s=0 chart is singular:
take the full-field/gauge limit, not a division by zero. The core has
the analogous operator formula with D_c and s D_c^-1; tangential
derivatives and D_c need not commute, so keep their actual order.

This is the quadratic functional of the declared linear gauge channel.
It is not the full non-Abelian quartic/ghost/fermion boundary theory or
the response of the 128 charged spinor-product sectors.

## 7. Why a static mean match need not remain a scalar dynamic match

The tail is diagonal in its angular modes; the actual core generally
requires the complete operator D_c. For the mean input b=1, closure
would require the nonconstant part of R_c(s)1 to vanish. From (6) its
matrix element with a zero-mean trace a is

    s sum_(j>=1) conj(B_j[a])B_j[1]/(lambda_j+s).      (14)

Equation (14) is the required discriminator, not a proof that it is
nonzero on every actual metric. Particular symmetries can make elements
vanish. The static rank-one response alone gives no all-frequency
closure. Do not treat a finite spectral surrogate as its evaluation
on this surface.

Full matching must retain R_c+R_t on the actual scalar trace space,
D_c+D_t on transverse vectors, and the remaining gauge/normal/matter
and zero-mode data. Eliminating angular traces uses their ACTUAL inverse
or retains their kernel constraints. A desired scalar Robin coefficient
cannot replace this operator problem. This is geometry-derived coupling
between boundary channels; the core spectral data are still to be earned
or computed from the supplied carrier metric.

## 8. Complete the longitudinal part of the old zero-angular vbb cubic

The earlier cubic overlap I_T=2Y/(nu_p+nu_q+nu_k-1) used the linear
Poisson profile of a TRANSVERSE vector. It must not be assigned unchanged
to a longitudinal gauge leg. At zero angular momentum that leg is a
pure gauge extension constant in y, with its original boundary trace.
The inherited bulk vertex then fixes instead

    I_L(p,q)=integral P_b(p)P_b(q)dy=2Y/(nu_p+nu_q).

The actual scalar response satisfies the exact divided-difference law

    I_L(p,q) (p^2-q^2)=R_t,0(p^2)-R_t,0(q^2).        (15)

For all incoming momenta p+q+k=0, the vbb momentum factor, with its
old Lie/overall normalization retained, is therefore

    V_mu=I_T P_T,mu_nu(k)(p-q)_nu
                   +I_L P_L,mu_nu(k)(p-q)_nu.       (16)

Contraction gives k dot V=-(R_b(p^2)-R_b(q^2)), the gauge Ward relation
required by the quadratic adjoint-scalar action. No independent cubic
boundary coefficient was chosen. When k^2 tends to zero, I_L-I_T is
O(k^2); the apparent projector denominator is removable in the full
vertex. This extends rather than retracts the old transverse overlap.

As an explicit algebraic discriminator take p=0, q=-k, ell^2=2,
q^2=1. Then nu_p=1, nu_q=nu_k=3, I_L=Y/2 while I_T=Y/3. The
longitudinal contraction requires Y/2. Applying the old transverse
formula to every polarization would fail. These are disclosed hand
values, not executed tests or measured physical targets.

The general vvv tensor completion, quartic backreaction, Gauss sources
and fermionic vertices remain separate calculations. No full nonlinear
existence, scattering amplitude, chiral SM3 or anomaly result is inferred
from the necessary Ward relation (15)--(16).

## 9. Reduction grade and next obligation

Once the parent, metric, background and complete end are fixed, the
scalar/vector responses, their norms and the longitudinal vbb coefficient
are mutually constrained; none is an additional independent boundary
input. Core geometry enters through an actual Neumann/Dirichlet operator,
and zero modes and angular data survive in their proper roles.

This is author-unreviewed CONDITIONAL SAME-MODEL derivation. It has not
removed the foundational carrier/field/action/metric/state choices, fixed
the flat periods or selected a stable physical vacuum. The current
commuting static energy depends only on total area and flux, so it does
not select a shape modulus among equal-area core/tail realizations.
The actual geometric spectral evaluation, charged stability, complete
fermion matching and global weak-current spectrum are still owed.

The six earlier scientific methods remain unrun and unadmitted; their
source-complete review is pending. New controls for this proof need
their own design/seal/review, without retroactively expanding that packet.
