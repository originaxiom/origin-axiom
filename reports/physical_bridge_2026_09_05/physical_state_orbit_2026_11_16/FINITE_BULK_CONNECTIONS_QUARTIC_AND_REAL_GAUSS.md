# Finite bulk connections, their actual quartic and real Gauss response

2026-11-16. Author hand continuation of P-C3b. Independent review pending.
No scientific producer, CAS, collection or test ran. Quantifier is pairs
of the specified zero-residual backgrounds in one fixed supplied bulk
field theory after declared smooth bundle identifications. The registering
and spin qualifications below are part of the result.

## 1. Compare actual configurations in the same smooth bundles

Fix the complete finite-area hyperbolic punctured elliptic surface,
its spin line S, flavour bundle F_rho, compact E8 parent and metrics.
At any fixed extending spin eta and central core character epsilon,
the old physical family has the three state-axis backgrounds. Their
gauge transitions are

    L_h^g=P^b_h Zeta^e_h G(g^-1 rho(h)g) W_h,
    eta_h=(-1)^b_h, epsilon_h=(-1)^e_h,

with background pair g Phi0 and the same local spin-induced connection.
Every such background has vanishing holomorphic and moment residuals.
Its core flat holonomy is part of the state, with the supplied Wilson
datum retained. It is not fixed as an immutable external connection
when the full parent connection field is varied.

The flat peripheral gauge holonomy is the same Zeta P for all g. Use
the same spin/cusp frame and the same flat peripheral representative.
Then the actual full tail connection can be chosen common, while the
endpoint spin pairs are parallel and physically bounded there. This
uses the source's literal tail connection, rather than inferring equal
connections from equal peripheral conjugacy classes alone.

These gauge bundles admit smooth unitary identifications agreeing with
that tail framing. A compact truncation is a two-dimensional surface
with boundary. The obstruction to extending a prescribed boundary
identification of principal bundles is in the fundamental group of
the structure group. Compact E8 is connected and simply connected,
so that obstruction vanishes. No extension is required to preserve
the endpoint flat connections, reductions or core holonomies. The
identification is an auxiliary coordinate choice for comparing fields.
The physical connection remains a variable, and the path below is
allowed to leave the flat core and balanced parallel locus.

The three aligned spin/state orbit members have different spin labels.
Direct interpolation between different spin bundles is not defined by
this argument. The preceding spin/core isometries can represent them
at common spin with changed central core labels. Applying the smooth
bundle argument then connects those representatives in the underlying
bulk theory. Their explicit registering defects and central operations
are still retained. A source or measurer that fixes those extra data
can restrict the allowed paths. No connectivity of that enlarged
registered theory follows without its actual source/end law.

## 2. Construct a finite-action bulk path without a new potential

In the fixed smooth bundles write the two endpoints as X0=(A0,q0,r0)
and X1=(A0+a,q0+u,r0+v). Both are zeroes of all parent residuals.
Their connection difference a is compactly supported in the chosen
common-tail frame. On the tail the differences u,v are parallel
bounded orthonormal profiles, with coordinate size O(sqrt(Omega)).

The affine path is

    X_s=(A0+s a,q0+s u,r0+s v), 0<=s<=1.                 (1)

It is globally defined in those bundles. Its tangent norm from the
same chiral metric is

    K0=(1/G) integral { |a|^2/2+Omega(|u|^2+|v|^2)} dxdy.

It is finite by compact support of a and finite area of the tail.
The path and its residuals have the source nonlinear finite-action
regularity. On the tail Dbar_A0 u=Dbar_A0 v=0; all remaining physical
commutator residuals are bounded. They are integrable against finite
area. Complete cutoffs give the same graph/variation realization.
No finite-circle boundary condition is added.

More can be derived exactly. Put a=a_x+i a_y, and define

    p_q=Dbar_0 u+i[q0,a], p_r=Dbar_0 v+i[r0,a],
    t=[q0,v]-[r0,u],
    mu2=-i[a_x,a_y]+Omega([u,u^dagger]+[v,v^dagger]).

The derivative residuals along (1) are s p_q-i s^2[a,u]
and s p_r-i s^2[a,v]. The commutator residual is s t+s^2[u,v].
The moment is s mu1+s^2 mu2, since the initial moment is zero.
Vanishing of the same residuals at s=1 gives

    p_q=i[a,u], p_r=i[a,v], t=-[u,v], mu1=-mu2.

The actual complete parent potential therefore restricts exactly to

    V(X_s)=B s^2(1-s)^2,                                (2)

    B=(1/G) integral kappa{
        Omega^-1(|[a,u]|^2+|[a,v]|^2)
        +2|[u,v]|^2+|mu2|^2/(2 Omega^2)} dxdy >=0.       (3)

B is finite under the just-stated tail conditions. Its coefficients
come from the parent F and moment squares, including their original
relative weights. No phenomenological double-well coefficient is
inserted. B can vanish for a path lying in the vacuum locus. Even when
B>0 for a chosen affine path, this is an upper construction through
configuration space. Relaxing transverse fields can lower or remove
its barrier. The earlier R83 mixing audit already established that
distinction for residual-square functionals and is explicitly reused.

For an optional transparent tail control, suppose the common tail
frames leave the endpoints as Phi1=U Phi0 with U in SU2, while the
tail connection is fixed. Write Tr U=2 cos(theta). Then
(U-I)^dagger(U-I)=2(1-cos(theta))I. The two commuting raising triples
give on that tail

    mu2/Omega^2=2(1-cos(theta)) M0,
    M0=[qhat0,qhat0^dagger]+[rhat0,rhat0^dagger].

For U!=I and M0!=0 this chosen path has a strictly positive tail
contribution to B. This is a conditional check on the path formula.
It does not prove a minimum barrier over other frames or paths.

## 3. Keep the real longitudinal gauge equation

Let s depend on one external coordinate x, and retain its actual
external connection component A_x^ext=s'(x) alpha_s. It has no external
F_mu_nu in this one-coordinate ansatz. Its mixed internal components
are retained by the full affine gauge tangent

    k_s alpha=(Dbar_(A_s) alpha,
                         i[alpha,q_s],i[alpha,r_s]).

For compact-real alpha, the kinetic density on the path is

    K(s,alpha) s'^2=||dot(X_s)-k_s alpha||_c^2 s'^2,      (4)

where || ||_c includes exactly the positive metric and 1/G above.
The real gauge-parameter metric is the vector metric Omega^2/G.
Variation of alpha gives the real Gauss/longitudinal equation

    k_(s,R)^dagger (dot(X_s)-k_s alpha_s)=0,
    L_s alpha_s=b_s,
    L_s=Re(k_s^dagger k_s), b_s=Re(k_s^dagger dot(X_s)).  (5)

The adjoints and Re use these actual metrics and compact real structure.
An arbitrary interior point need not be D-flat. The D-flat complex
identity for P_v cannot be copied there without the Re in (5).

There is a closed-range argument for this gauge operator despite the
separate spin-fermion continuum. On real parameters its quadratic form is

    <alpha,L_s alpha>=(1/G) integral {
          (|D_x alpha|^2+|D_y alpha|^2)/2
          +Omega(|[alpha,q_s]|^2+|[alpha,r_s]|^2)} dxdy.  (6)

Use radial unitary gauge on a cusp, ds^2=ell^2(dx^2+dy^2)/y^2,
and t=log y. A compactly supported radial test function satisfies

    integral e^-t |partial_t alpha|^2 dt
                >=(1/4) integral e^-t |alpha|^2 dt.

This follows by writing alpha=e^(t/2) f and integrating the cross
term. The angular and Higgs terms in (6) are nonnegative. Relative
to the vector metric this proves the tail lower bound

    <alpha,L_s alpha> >= ||alpha||_v^2/(8 ell^2).         (7)

It applies on every sufficiently far exact cusp. Standard compact-core
Rellich compactness then isolates zero from the essential spectrum of
this complete nonnegative gauge realization. Its kernel is finite and
consists of the actual unbroken parallel parameters annihilated by k_s.
Consequently L_s has a bounded inverse on its kernel complement at
each fixed s. There is no assertion of a uniform inverse through gauge
enhancement points. Equation (7) concerns gauge parameters with vector
density Omega^2. It gives no positive threshold for physical spin
fermions with their different density.

For the smooth path above b_s is L2 and is orthogonal to ker L_s,
since <epsilon,b_s>=Re<k_s epsilon,dot(X_s)>=0 for such epsilon.
Thus (5) has a weak solution alpha_s=L_s^+ b_s, unique up to its
unbroken kernel. The exact horizontal coefficient is

    K(s)=K0-<b_s,L_s^+ b_s>_v, 0<=K(s)<=K0.              (8)

It is an output of the original gauge response. Smoothness of alpha
through an enhancement point and a regular full spacetime field
representative require their own analysis. More generally (8) is the
squared distance of dot(X_s) from the closure of real gauge tangents.
The projection and norm remain defined even where a choice of gauge
coordinate is singular.

## 4. Separate a restricted path equation from full stationarity

At this level the same-action restricted energy is

    E_path=integral dx {K(s) s'^2+B s^2(1-s)^2}.          (9)

On a smooth segment with K>0 its Euler equation and zero-energy
first integral are

    2K s''+K' s'^2=partial_s[B s^2(1-s)^2],
    K s'^2=B s^2(1-s)^2.

For monotone interpolation, the restricted tension is bounded below
by 2 sqrt(B) integral_0^1 s(1-s) sqrt(K(s)) ds, with equality only
if that first integral and the required endpoint regularity hold.
All quantities in (9) come from the same bulk action. Solving (9)
would establish stationarity only along this chosen path. A physical
stationary interface must also solve every transverse field equation
and its fermionic/domain response. No such solution is claimed here.

## 5. Consequence for the programme

Flat core holonomy labels alone do not make the tested fixed-spin
backgrounds disconnected in the full smooth finite-action bulk space.
There is an explicit finite path, a derived nonlinear restricted
potential and an actual real gauge constraint. This gives a concrete
same-action starting point for testing interactions between state
regions, instead of assigning a cross-sector matrix by hand.

The chosen affine path, bundle coordinates and its B are calculation
choices, not fundamental constants or a state-selection rule. The
complete registered theory can still distinguish spin/core frames and
source/end data. The endpoint comparison carries its old registering
defect. No preferred aligned orbit, nonzero end unit, three-generation
composition or SM/gravity spectrum is derived by (1)-(9).

Independent review should check the fixed-spin gluing, common-tail
identifications, nonlinear integrability, all residual coefficients,
the real Gauss factor and Hardy constant, range/domain assertions,
and the precise limitation at gauge enhancement. Full stationary
joining and an earned registering/end law remain next physical duties.
