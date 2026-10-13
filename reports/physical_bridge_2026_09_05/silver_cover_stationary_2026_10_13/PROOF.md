# Local stationary branch and charged kernels on one compact cover

Authored before execution. Conditional analytic derivation using the pinned
compact smooth background, positive metric, full E8 action and elliptic
strict trace realization. Exact matrix controls do not independently
certify this global argument. No foundational selection is supplied here.

## 1. Keep the relative line and change fields rather than quotient them

Let phi0 be the admitted small nonzero SM-phase background on the connected
double cover. The compensated odd nil-valued relative form b from the
previous proof obeys D0 b=0, [b,b]=0 and b_t=0 on both tori. Hence
phi(q)=phi0+q b is flat for all complex q and has exactly the old tangential
connection. Its absolute class is nonexact in the WHOLE structure adjoint.
This does not assert that its real moment vanishes.

For a Hermitian traceless structure section lambda set g=exp(-lambda) and

    Phi(lambda,q)=g^-1 phi(q) g-i g^-1 dg.

The connection d+iPhi is g^-1(d+i phi(q))g; therefore curvature transforms
by g^-1 H g and remains zero. At lambda=0 its derivative is i D0 lambda,
not D0 lambda or -i D0 lambda. The first two lambda coefficients are
i d lambda+[lambda,phi] and
([lambda,[lambda,phi]]+i[lambda,d lambda])/2. These provide sign controls.
This is a change of configuration in the fixed Hermitian Hilbert bundle,
not an identification of complex gauge orbits with physical gauge.

## 2. The actual Dirichlet derivative has no kernel

Take lambda=0 on every boundary component. Write A,B for the Hermitian
parts of phi0. The real moment derivative is

    d_lambda mu(Phi)(0,0)=-P_Dir,
    P_Dir=-D_A^i D_A,i+sum_i [B_i,[B_i, .]].

It follows directly by differentiating div_A B, including derivatives of
lambda. At a generic nonharmonic field the same REAL expression occurs;
D*D would additionally contain [mu,lambda] and must not be substituted
without mu=0. The background here is harmonic. For real Hermitian lambda
with Dirichlet value zero, integration by parts gives

    <lambda,P_Dir lambda>=||D_A lambda||^2
                           +sum ||i[B_i,lambda]||^2.

The boundary term vanishes by value, not by frozen normal jets. The
principal symbol is |xi|^2 times the identity. A zero of this form is
parallel with zero boundary value, hence zero on the connected core.
More strongly, the metric connection inequality |d|lambda||<=|D_A lambda|
and scalar Dirichlet Poincare give coercivity on H1_0. The nonnegative
Higgs term does not weaken it. The Friedrichs realization is selfadjoint;
Lax-Milgram solves weak sources uniquely. Standard compact strongly
elliptic Dirichlet regularity upgrades its inverse to
H^(m+2) intersect H1_0 from H^m, for every integer m>=0. No numerical gap,
Green profile or inverse from the complete cusp is borrowed.

## 3. Local implicit solution of the real moment

Choose integer m>=3, and use the real space of Hermitian traceless
structure sections H^(m+2) intersect H1_0. Matrix exponential, products
and inversion near identity are smooth there by Sobolev multiplication
in dimension3. Phi lies in H^(m+1), and its moment in H^m. Thus

    M(lambda,q)=mu(Phi(lambda,q))

is a smooth REAL Banach-space map; M(0,0)=0 and its lambda derivative is
the isomorphism -P_Dir. The implicit-function theorem gives a unique small
lambda(q), lambda(0)=0, solving M=0 for q in a neighborhood of zero in C
(two real coordinates). The quasilinear Dirichlet equation remains strongly
elliptic near zero. Smooth supplied coefficients and the homogeneous smooth
boundary permit elliptic bootstrapping, so every resulting field is smooth.
Uniqueness on overlapping Sobolev neighborhoods makes the constructions
compatible. This is a local existence argument, not a solved numerical
profile or an assertion for every q.

Its tangent is qb plus an exact iD0 lambda term. Since b has nonzero
absolute adjoint cohomology, the two real tangent directions cannot be
deleted by allowed real gauge. There is a genuine local stationary family,
not a proof that every neutral direction integrates or that its coordinate
is a canonically normalized physical modulus. The two-dimensional real
chart is not an additional count of generations.

## 4. The same action and whole response stay admissible

g=I on BOTH boundary tori and d_t g=0 there, so Phi_t=phi0,t exactly.
Normal derivatives of g are free and generally nonzero. This preserves
the full old strict E8 tangential trace, the SM phase and the relative
boundary framings; it does not reset the varying bulk transport record.
The change is entirely in the structure algebra s. Since [s,k]=0 and
Tr(s k)=0, its imaginary normal component has zero projection onto the
ONE globally allowed k under the summed boundary pairing.

All other canonical eliminated static response laws are now zero:
H=mu=0 gives F=D_aux=0 and their normal derivatives zero. The fixed
relative CS primitive still cancels its surface by the SAME cyclic trace
law. Thus V=0 and every admitted first variation vanishes in the original
action. Its Hessian is the same nonnegative residual-square expression.
Positive kinetic forms are unchanged. This earns a conditional smooth
static branch, not nonlinear external evolution, a quantum vacuum or an
isolated/gapped minimum. Background field transformations are not an
authorized quotient of imaginary scalar fluctuations.

## 5. Three charged kernels survive without deck-sector copying

For every charged gauge weight keep the WHOLE cover differential D_q and
Q_q=D_q+D_q*. Structure changes commute with the SM gauge algebra; actual
tensor/dual connections are induced from the same Phi. Tangential D_q is
exactly D_0, so the fixed strict boundary subcomplex, its Green annihilator,
graded trace projector and Hilbert domain are unchanged. On this compact
base Q_q-Q_0 is a symmetric bounded order-zero term tending to zero in
operator norm. The inherited selfadjoint elliptic realization has the same
domain and compact resolvent. Its odd-to-even Fredholm block is a
continuous bounded map from that common graph domain, so its index is
constant. This is not an equality of finite cochains and wavefunctions.

At q=0 the actual W and F charged tuples are(0,3,0,0), and both actual
duals have(0,0,3,0). The compact spectral gap on the zero-free even sector
of W/F gives ||Q_0 u_even||>=delta||u_even||. For a sufficiently small
perturbation the triangle inequality gives the same inequality with
delta-||Q_q-Q_0||>0. Their H0,H2 therefore stay zero. Apply the same
zero-free estimate to degree3 to keep H3 zero. The protected odd-minus-even
index3 then forces H1=3. For both duals the zero-free odd sector and
degree0 estimates give H1,H3,H0=0, and the index-3 forces H2=3. Flatness and
the fixed Hilbert complex identify the zero modes degree by degree.

There are finitely many charged SM weights; intersect their neighborhoods
to obtain ONE small q neighborhood for both slots and their duals. No
numerical radius or mass gap is claimed. The odd b generally destroys deck
parity at q!=0. The old 1+2 bookkeeping is not reused; the total3 is
preserved by the whole operator and its missing-partner gaps. An index
alone, without those gaps, would not exclude new opposite/end modes.

## 6. Interactions and limits

The full E8 bracket is retained and the gauge background sector unchanged.
Small smooth spectral projections give a local continuous frame of the
charged harmonic kernels. In that frame an already nonzero QdcL overlap
at q=0 remains nonzero on a smaller neighborhood by continuity, with
positive finite kinetic normalization. This is not a numerical Yukawa or
a statement that earlier eLL/udd cancellations survive at q!=0. Those
dangerous vertices require a new actual overlap test. Neutral and adjoint
kernel counts, full supersymmetric companions, thresholds and their mass
changes must be checked; no unwanted state is silently removed.

The existence of this local branch cannot choose the supplied charged
planes, phase, carrier, metric, cover or parent from genesis. It also does
not turn the other complete positive-cusp complex into a chiral model.
The full foundational index-bearing field/end/source map, Higgs and mass
sector, quantum/global/boundary consistency, normalized parameters,
gravity and any observer/qualia identification remain separate duties.
Full SM and TOE are unachieved.

Primary boundary passages personally checked: Bär-Ballmann Theorem3.9,
3.11 and Corollary5.6/Remark5.7, https://arxiv.org/html/1307.3021v1.
They support the inherited compact boundary realization and regularity,
not our Dirichlet moment calculation or the foundational physical map.
