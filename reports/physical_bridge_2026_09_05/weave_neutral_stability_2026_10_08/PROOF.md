# Neutral spin fields and the full magnetic fluctuation operator

Conditional authored proof in the pinned curved parent. Metric, E8,
embedding, spin and complete-domain law remain supplied. This is a
classical fixed-metric analysis, not a quantum or gravitational theory.

## The global neutral section and stationary family

On the compact elliptic curve C the canonical line is trivialized by a
nowhere-zero holomorphic differential omega. Of its four extending spin
lines S, only the trivial one has a nonzero holomorphic section: a
nonzero section of a degree-zero line has no zero divisor and trivializes
the line. This is the odd theta characteristic (h0=1), not a derived
choice of spin. Fix psi with psi^2=omega.

In a puncture coordinate u, omega=g(u)du with g(0)!=0. The complete cusp
has h_K comparable to r^2*log(r)^2, r=abs(u). Hence

    abs(psi)^2 is comparable to r*abs(log r).

Its L2 radial norm is comparable to integral dr/abs(log r); its fourth
norm is comparable to integral r dr. Both are finite. A holomorphic
spin section with a pole of order p instead has L2 radial integrand
r^(-2p)/abs(log r), so every p>=1 is forbidden. Angular Laurent
orthogonality excludes essential singularities too: every negative
Laurent coefficient would give a divergent summand. Thus every L2
holomorphic section extends, proving the same uniqueness statement for
the punctured surface. Bounded cusp-metric comparison is enough.

In the cusp coordinate z=x+iy with period ell, u=exp(2*pi*i*z/ell).
The holomorphic spin coefficient is O(exp(-pi*y/ell)); its orthonormal
coefficient Psi is O(sqrt(y)*exp(-pi*y/ell)). Every fixed-order unit-frame
derivative is bounded and tends to zero. The covariant first derivatives
are L2. Complete exhausting cutoffs place psi in the same first-order
graph domain, not an independently imposed boundary condition.

Use the previous principal triple H=2w,E and Z=T/2, with[Z,E]=0.
Let Q_principal have orthonormal coefficient E/2, and set

    A=A_n, Q=Q_principal+c*psi*Z, R=0.

The added section is holomorphic, neutral under A, and commutes with the
entire principal triple. Therefore every F residual is zero and the
orthonormal moment remains mu=-nZ. Its covariant derivative is zero and
it commutes with Q and R. The full first-variation proof from the magnetic
packet applies in every E8 direction. No zero-D assumption was made.
The energy is still pi*n^2*kappa(Z^2)/g6^2 for every finite c.

The background has finite positive kinetic norm. Its c-dependent part
has norm abs(c)^2*kappa(Z^2)*integral abs(psi)^2. Cross terms vanish by
trace orthogonality of E and Z. In particular the amplitude is visible
in a gauge-invariant norm; it is a genuine unfixed modulus, not silently
eliminated by a change of basis.

For n!=0,c=0 the compact group was already SM. For c!=0, any unbroken
gauge section is parallel. Since Q_principal is spin-parallel, its
commutator with such a section has constant norm along the cusp. The
commutator with c*psi*Z tends to zero. Invariance of Q therefore forces
separate commutation with E and its adjoint, hence w, and then with Z.
The previous faithfully embedded SU5_g is reduced to S(U3 x U2), with
the same Z6 global form. This also proves the n=0,c!=0 case. n=c=0
returns SU5; no extra Wilson angle is introduced.

At n=0 all residuals vanish. The entire potential is a positive sum of
squares, so this SM phase has a nonnegative classical Hessian on the
actual gauge quotient. It is a minimum with flat moduli, not an isolated
selected vacuum or proof of nonlinear asymptotic/quantum stability.

## The full quadratic form and the gauge quotient

Use holomorphic spin coefficients q for the background and u,r for its
Q,R variations; a=a_x+i*a_y varies A, with Hermitian a_x,a_y.
Dbar=partial_x+i*partial_y-i*ad A, Dz=partial_x-i*partial_y-i*ad Abar.
Put

    f1=D_x a_y-D_y a_x,
    M1=f1+Omega*([u,q dagger]+[q,u dagger]),
    M2=-i[a_x,a_y]+Omega*([u,u dagger]+[r,r dagger]),
    m0=-nZ*Omega^2.

The exact coefficient of the square of the path amplitude in g6^2 V is

    integral dxdy kappa[
      Omega^-1 (abs(Dbar u+i[q,a])^2+abs(Dbar r)^2)
      +2 abs([q,r])^2
      +(1/(2*Omega^2)) M1^2
      +Omega^-2 m0*M2 ].

This includes both spin fields, all their conjugates, the moment's
quadratic curvature and every mixed A/Q term. It is obtained by
expanding the original squared residuals, whose F backgrounds vanish.
No favorable scalar potential has been appended.

The kinetic form is the parent's positive
integral dxdy kappa[abs(a)^2/2+Omega*(abs(u)^2+abs(r)^2)].
The real background gauge condition, its orthogonal slice, is

    G1=D_x a_x+D_y a_y-i*Omega*([q dagger,u]+[q,u dagger])=0.

Adding integral kappa(G1^2)/(2*Omega^2) is positive gauge fixing, not
a modification of the physical potential on this slice. The connection
and spin parts of the real gauge tangent give precisely this adjoint
condition by integration by parts. Nonnegative vector/vertical sectors
must not be counted as extra matter.

For a charged root pair let v=(u of opposite charge) dagger,
a_bar=(a of opposite charge) dagger, and B=ad q. Set X=Dz a,
Y=Dbar a_bar, P=Omega*B dagger u, U=Omega*B v. Then

    M1=(X-Y)/(2i)-P+U,   G1=(X+Y)/2-i(P+U),
    abs(M1)^2+abs(G1)^2
      =(abs(X-2iP)^2+abs(Y-2iU)^2)/2.

This elementary identity displays the two charged blocks; treating u
and its opposite-charge adjoint as the same independent field would
miscount them. The negative moment contributes -k times the positive
kinetic norm in the a/u/r charge-q block, k=nq; its opposite-charge
variables supply the opposite sign. The full real field is retained.

## Canonical cusp blocks on every E8 summand

Decompose the complex248 by Z charge q and principal spin j, with w
weights m=-j,...,j. The complete profile is

    q=0: 12*V0 + V1+V2+V3+V4;
    q=+/-1: 6*V2;  q=+/-4:3*V2;  q=+/-6:V2;
    q=+/-2:3*(V1+V3); q=+/-3:2*(V1+V3);
    q=+/-5:6*V0.

It is verified from all240 roots plus8 Cartans and separately from
(24,1)+(1,24)+(10,5)+(bar10,bar5)+(bar5,10)+(5,bar10).
No charged or neutral summand is removed.

At c=0, zero angular A channels have even m, while Q/R channels have
odd m: the old gauge peripheral and the extending spin sign BOTH enter.
For t=log y the canonical maps are a=sqrt(2/y)*alpha and u=u_Q,r=u_R
in holomorphic spin coefficients. For even m with -j<=m<=j-1 the
A_m,Q_(m+1) block is

    norm[(partial_t+d)u+b*alpha]^2
      +norm[(-partial_t+d)alpha-b*u]^2
      -k*(norm u^2+norm alpha^2),
    d=k+(m+1)/2, b^2=(j-m)(j+m+1)/2.

Cross terms cancel with the actual adjoints on compact support and then
on the complete graph closure. Each of its two channels has threshold

    d^2+b^2-k
      =1/4+(k+m/2)^2+(j(j+1)-m^2)/2 = V_m.

In particular, these blocks are not inferred just from a proposed square.
For ell_m=sqrt((j-m)(j+m+1)), the coordinate residuals before
normalization are i(u_y+(m+1+2k)u/(2y)+ell_m*a/(2sqrt(y))) and
-i(a_y-(m+2k)a/(2y)+ell_m*u/y^(3/2)). Their weights after dxdy=y dxdt
are y^2 and y^3/2 respectively. Substituting a=sqrt(2/y)*alpha
gives precisely the two rows above and normalizes its kinetic term.
Both substitutions are tested symbolically for all ten coupled blocks.

The upper extreme A_j exists for even j and has the same formula with
b=0. For odd j the lower extreme Q_-j instead has threshold

    E_j(k)=(k-j/2)^2-k.

These extremes cannot be discarded as zero-dimensional blocks.

The full R field decouples at quadratic order since its background is
zero. At odd m its threshold is

    R_jm(k)=(k+m/2)^2+(j-m)(j+m+1)/2-k
      =(k+(m-1)/2)^2+(j(j+1)-m^2)/2-1/4.

The four-dimensional vector fluctuation has a positive gradient/Higgs
operator. Its even-m threshold is V_m above: the gradient gives
1/4+(k+m/2)^2 and the two real Higgs components give
(j(j+1)-m^2)/2. This independently matches the gauge-tangent partner
of the paired A/Q block and never creates a negative physical mode.

The scalar gauge-fixed roster contains248 A/Q and112 R complex
zero-angular channels; the vector roster contains136. These counts
retain gauge-fixed redundancy and are NOT numbers of physical particles.
Nonzero angular modes have a positive leading frequency-square*y^2 term;
bounded principal fields/flux give lower-order O(y) terms. They cannot
supply a further finite essential threshold. Compact-core terms are
relatively compact by local ellipticity and Rellich.

## Exact end verdict for all integer fluxes

V_m>=1/4 for all k because abs(m)<=j. Likewise R_jm>=j/2-1/4>=1/4
on its nonempty odd-m sectors j>=1. Thus only an odd-j Q extreme can
have a negative threshold.

For j=1, E_1(k)=(k-1)^2-3/4. The ACTUAL charges are0,+/-2,+/-3,
so k=nq is never1. Therefore E_1>=1/4 for every integer n.
An artificial q=1,j=1 module would violate this; it is an explicit
opposite control, not a discarded real representation.

For j=3, E_3(k)=(k-2)^2-7/4. Actual charges are0,+/-2,+/-3.
A negative value occurs precisely at abs(n)=1 with k=2 or3:
three complex channels have -7/4 and two have -3/4, by the multiplicities
above. At n=0 or abs(n)>=2 every such threshold is positive (at least9/4).
Their actual color/weak weights identify a color-antitriplet weak-singlet
at q=2 and a color-singlet weak-doublet at q=3 (conjugated at negative
flux). They are SCALAR fluctuations, not fermion generations. The
instability therefore is not merely a desired electroweak Higgs mass:
it contains color-charged directions in this SM-preserving background.
The neutral gauge V0 channel retains1/4, so the bottom of the COMPLETE
essential spectrum is exactly

    -7/4 for abs(n)=1;   1/4 for n=0 or abs(n)>=2.

These are in supplied curvature units. There is no inference from the
positive cases to the discrete eigenvalues or global stability.

At c=0 a lowest Q_-3 variation has [E dagger,u]=0, so both its linear
moment and its gauge divergence vanish. Canonically its quadratic form
is norm(partial_t+(k-3/2))u^2-k*norm u^2.
Normalized long smooth packets supported arbitrarily far down the cusp
have Rayleigh quotients tending to E_3(k). The packets can be chosen on
disjoint supports. Their nonlinear paths have finite energy and all
quartic norms because each support is compact. Negative directions
cannot be pure gauge; the gauge-invariant Hessian vanishes on gauge
tangents at a stationary point. This proves infinite physical Morse
index at the first flux, not merely a finite matrix warning.

One explicit form-domain control is chi(s)=s(1-s) on[0,1], extended by
zero. Its derivative-to-norm ratio is10; dilation to length L gives
10/L^2. Smooth compact approximants converge in H1, so the strict
negative sign persists. Smooth long packets also give the operator Weyl
sequences with arbitrary radial frequency used for the essential set.

## What the neutral deformation can and cannot change

For each fixed finite c, Psi and its unit-frame derivatives decay.
The changes to the gauge-fixed Hessian have bounded decaying first-order
coefficients and potentials, hence are relatively form-compact with
respect to the elliptic graph form. The same follows by compact-core
Rellich plus small tail norms. Essential spectrum is unchanged.

The escaping Q packets therefore remain negative at abs(n)=1 for EVERY
finite c; added neutral terms tend uniformly to zero on their supports.
The gauge condition error also tends to zero, while the vector/vertical
operator is nonnegative. Alternatively the gauge-invariant bare quadratic
form itself is negative on the packets. A profile confined to the core
or decaying at this end cannot cure these essential channels.

At abs(n)>=2 this particular obstruction is absent. The c=0 phase still
has the magnetic packet's at-least30*abs(n) global negative directions.
A positive essential threshold alone says nothing about whether a
finite c removes those and any further discrete negative modes.
No global stability theorem, numerical optimum or stable nonzero-flux
phase is asserted here.

For n=0,c!=0 the positive-square background already proves a nonnegative
classical Hessian and exact SM gauge group. Its complete fermion mass
operator differs from the pinned n=0 phase by decaying bounded
zeroth-order Yukawa/Killing terms. Fixed-domain local ellipticity and
Rellich make the difference graph-compact. The preceding full gap gives
Fredholmness, and every fixed-SM charged index stays zero along c.
Individual kernels can jump; no zero-mode census is inferred.
This phase is an important positive control, NOT the chiral SM.

The proper successor is the higher-flux DISCRETE stability problem with
all mixed modes retained, or another earned end/source construction.
Full fermion index at nonzero n, three physical families, interactions
and anomaly acceptance still require their own calculation. The neutral
amplitude, spin, action and geometry have not been derived from genesis.
No observer/qualia identification or full SM/TOE completion follows.
