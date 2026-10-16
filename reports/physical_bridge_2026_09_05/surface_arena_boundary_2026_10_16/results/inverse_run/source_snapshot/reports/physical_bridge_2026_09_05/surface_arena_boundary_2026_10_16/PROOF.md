# Normal boundary geometry and the physical source dictionary

Authored conditional application of the credited primary results and
actual source geometry. No new generic moduli-space theorem claimed.

## 1 The map is a normal bundle map

Hain Prop1.1/Cor1.2 identify the normal line of the universal elliptic
curve's zero section with L^-1, via z'=(c tau+d)^-1 z. Removing the
section and retaining the direction of approach gives its real oriented
normal blowup boundary, the unit circle bundle of L^-1. This is NOT
replacing the whole four-real-dimensional surface by a three-manifold.
Write tau=x+iy and w=z/sqrt(y)=r exp(i phi), area factor omitted here.
The normalized normal transforms w'=exp(-i theta)w, theta=arg(c tau+d).

Put g_tau=[[sqrt(y),x/sqrt(y)],[0,1/sqrt(y)]] and
k(t)=[[cos(t),-sin(t)],[sin(t),cos(t)]]. The map

    (tau,phi) -> SL2Z g_tau k(-phi)

is equivariant: gamma g_tau=g_(gamma tau) k(theta). It is a smooth
bijection on quotient frames. Its unit tangent direction on the
hyperbolic base has angle2phi. The generic -I sends phi to phi-pi,
so it is NOT legitimate to erase that central action before defining
the normal circle. Inversion gives the opposite left/right quotient
convention. Ghys Section3.1 identifies this homogeneous space with
the trefoil complement via Weierstrass invariants, not just pi1.

The same result is visible from nonzero tangent vectors: Hain Remark1.6
gives their B3 group and the trefoil discriminant complement. Positive
radial normalization retracts that C* normal bundle to this boundary.
These are published facts connected to our actual normal/source chart.

## 2 The two different meridians and the based register

Keep c=abAB, our positive puncture circle in the ELLIPTIC FIBRE.
The previously corrected free-word dictionary gives c=(ZY)^-6 as
an inner action. The regular Seifert fibre h=(ZY)^-3 projects to-I
and h^2 acts by Inner(c). The full normal rotation2pi is h^2; a
regular orbit in the coarse boundary closes at phi+pi via-I.
Hain's natural tangential-basepoint map identifies that full circle
with c. It fixes c and retains point-pushing rather than abelianizing it.

Under a tangent rescaling v, the Weierstrass invariants have degrees
4,6 and their discriminant degree12. Therefore full2pi normal rotation
has linking12 with the missing trefoil; the regular phi+pi fibre has
linking6. The ordinary TREFOIL knot meridian has linking1. It is a
different loop, not c merely because both are called a meridian.
This does not identify a physical charge or quantum winding with12.

The actual gauge h has SU6 part(Z6Y6)^-3 and weak part D^-6.
Its square is(I6,-I2), equal in the stated E8 quotient to(-I6,I2),
the puncture involution. The code checks all248 via the complete
branching in each of the six weak classes. All coefficient sectors
are kept; no preferred angle, family or zero mode is selected.

## 3 A smooth globally embedded tube

For q_mn=y^2/((m+n x)^2+n^2 y^2)^2 define

    E2(tau)=sum_(m,n)not(0,0) q_mn, sigma=E2^-1/4.

The series and all derivatives converge locally normally on H. For
each compact set the summands are bounded by a constant times
(m^2+n^2)^-2; every derivative has the same order with a compact-set
constant. T and S reindex(m,n) by(m+n,n) and(-n,m), bijections of
the nonzero integer pairs. Thus E2 and sigma are smooth, positive,
modular invariant. This uses the full infinite lattice, not a truncation.

The shortest unit-area period is l1=min |m+n tau|/sqrt(y). The term
attaining it gives E2>=l1^-4, hence sigma<=l1. Including its negative
makes the inequality strict. In the standard fundamental domain
l1=1/sqrt(y): n=0 is immediate, |n|>=2 uses y>=sqrt(3)/2, and
|n|=1 uses |tau|>=1, |x|<=1/2 and the nearest m=0,+/-1.

In the actual fibre metric the shortest period is sqrt(A)l1. A disc
of radius less than half this period is embedded. Consequently

    r=epsilon sqrt(A)sigma(tau), 0<epsilon<1/2,

defines a smooth invariant embedded tube over the ENTIRE modular base.
The value epsilon remains a regulator, not a derived physical scale.
All base stabilizers rotate a nonzero normal vector nontrivially, so
the normal boundary itself is a smooth three-manifold. No claim that
all bulk orbifold singularities were thereby removed.

## 4 Actual contact form and strictness

The actual coframe and radius gradient in the preceding tube packet
give eta/(2r^2)=alpha=dphi+dx/(2y), eta=(J grad r^2)^flat.
For a variable tube use f=log r-log(sqrt(A)sigma). With
d^c f=-df composed with J, its characteristic form is

    beta=d^c f=alpha-d^c log sigma
         =dphi+[1/(2y)+partial_y log sigma]dx
                   -partial_x log sigma dy.

This is derived using the actual total complex structure, not a
vertical-normal approximation. On the three-dimensional tube,

    d beta=L dx wedge dy,
    L=1/(2y^2)-Delta_Euclidean log sigma
     =(4-|grad_hyp log E2|^2)/(4y^2).

Each summand obeys y^2 Delta q=2q and
|grad_hyp log q|=2. With weights w=q/E2, their average gradient has
norm strictly less than2: the (1,0) and(0,1) summands have different
gradients and positive weight at every tau. Explicitly

 4-|sum w v|^2=(1/2)sum_(a,b) w_a w_b |v_a-v_b|^2>0.

Thus beta wedge d beta=L dx wedge dy wedge dphi is strictly positive
EVERYWHERE, not just in a finite numerical sample. One explicit lower
bound is L>=4y^4/((x^2+y^2)^3 E2^2)>0 from those two summands.
The strict infinite-series argument is authored analysis, not proven
by the number of finite tests. Convergence permits the weighted identity.

The exact cusp's x-constant term follows by integrating the n!=0
summands over one x period and then the real line:

    E2=2 zeta(4)y^2+pi zeta(3)/y+exponentially small Fourier terms.

The rational kernel's Fourier transform, obtained by differentiating
that of1/(u^2+a^2), is proportional to(1+2pi a|k|)exp(-2pi a|k|).
This justifies exponential derivative bounds and the displayed
asymptotic. For E=a y^2+b/y, exact differentiation gives

    L=3b(4a y^3+b)/(4y^2(a y^3+b)^2)
      ~3(b/a)y^-5.

Hence the hyperbolically normalized coefficient y^2 L tends to0.
The global strict contact tube does NOT have uniform positive Levi
constant at the cusp. Using exactly sigma=y^-1/2 gives L=0, a
rejecting control, not the actual E2 tube. Fixed-radius local contact
and failure of fixed-radius global fit both remain true.

## 5 Three forms cannot be identified by their shared manifold

The Hilbert form of the modular geodesic flow is

    lambda=cos(2phi)dx/y+sin(2phi)dy/y,
    G=y cos(2phi)partial_x+y sin(2phi)partial_y
                                  -(cos(2phi)/2)partial_phi.

Direct differentiation gives lambda(G)=1, i_G d lambda=0,
lambda wedge d lambda=-2 dx wedge dy wedge dphi/y^2.
For alpha, the Reeb vector is partial_phi and alpha(G)=0,
but L_G alpha=i_G d alpha is nonzero. The strict beta has positive
contact orientation like alpha, not lambda. Since beta(partial_phi)=1
and i_partial_phi d beta=0, its Reeb is also exactly partial_phi.
Thus the identity of underlying manifolds does not identify their
contact dynamics. The modular flow is not thereby source boundary
Reeb evolution, physical time, or an interacting physical force.
The roles of alpha (normal-line connection), beta (actual CR tube)
and lambda (geodesic flow) must remain separate. Other derived
boundary actions/dynamics are not excluded.

## 6 The actual source field connection travels with the map

The freshly replayed source dictionary gives the16x16 transition
generator W=i diag(m), m=(0,2,1,-3) on the four left flavours, twice
for external spin, and opposite m on their actual conjugates. Its
complete source connection at r->0, tangent to a constant-r circle,
has Omega0=-W/(2ell), Omega1=0. The remaining coframes are O(r)
on compact base sets, not erased from the full finite-radius operator.
In the tautological invariant frame f=exp(W phi)psi, this becomes

    Omega_boundary=-W alpha.

In particular the anti-canonical scalar's connection is3i alpha,
with NONZERO curvature3i dx wedge dy/(2y^2). It is not zero when
the pullback line is trivialized, and it is NOT3i beta just because
the globally embedded tube's CR form is beta. Gauge transport remains
a separate full tensor factor, with h^2=puncture as above. No separate
spin half-line is postulated where the product spin/R bundle suffices.

This is a leading geometric/tensor connection map, not the whole
singular source operator, full radial Green law or a stationary Higgs.
The noncommuting half-pole, mass kernels and full scalar/gauge source
terms still travel with any such operator. No old gap/count is copied.

## 7 Meaning for the mission

Post-interruption implementation certificate: the coordinate coframe's
structured inverse is multiplied on BOTH sides to check identity before
computing the same gradient and J. This replaces generic trigonometric
matrix inversion only. The original interrupted source/manifest is kept
in first_run and POST_HOC_REPAIR; no original success is claimed.

The proposed common arena is the actual normal boundary of the
already-supplied surface, with an explicit globally embedded shrinking
realization and actual field/connection/based-gauge map. It is not a
new unrelated space inferred from the group name B3. The map is a
whole modular-architecture statement, not a model on m004 alone.

This does not force M1,2 as physical spacetime/internal space, choose
epsilon, supply a true end state/action, derive the canonical E8 parent
or identify its dynamics with geodesic linking. Full global stationary
Higgs/connection, charged singular/cusp domains, spectrum/conjugates/
boundary states/norms/vertices/anomalies, physical three generations,
observed parameters and gravity remain. Qualia is not identified with
a normal phase or a contact flow. Full physical goal stays ACTIVE.
