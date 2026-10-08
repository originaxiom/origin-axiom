# Magnetic stationarity and an admitted charged instability

Authored conditional proof, not outside acceptance. All action, metric,
spin and embedding inputs are those of the pinned preceding packets.
No first-order vacuum equation is silently substituted for full variation.

## A global stationary family outside the zero residual ansatz

Set Z=T/2=(5,5,5,-3,-3,-3,-3,-3)/2 and
w=(0,0,0,-1,1,-2,0,2). The principal spin-two triple is the old
H=2w,E, with[H,E]=2E,[E,E dagger]=H. Z commutes with the entire
bundle SU5. Both Z and w are E8 cocharacters. For integer n,
w+2nZ therefore induces a global E8 bundle from the SAME spin line S.
Since exp(2*pi*i*nZ)=1, its limiting peripheral is still the old p.
This is not an assertion that its whole connection or all core holonomies
are unchanged. The added even spin power is independent of the flat
sign choices of S.

Let A_n=s(w+2nZ), qhat=E/2, rhat=0, where ds=-dvol/2.
The spin covariant derivative of qhat vanishes because Z commutes with E.
Thus both holomorphic residuals and[Q,R] vanish. The orthonormal moment is

    mu=F/dvol+[qhat,qhat dagger]=-nZ.

It is nonzero for n!=0. Its covariant derivative is zero and it commutes
with qhat and rhat. Variation of the positive residual-square functional
therefore vanishes in EVERY E8 direction: integration by parts turns the
connection variation into D_A mu, and invariant trace turns the matter
variation into[mu,qhat] and[mu,rhat]. No restriction to the displayed
Cartan or to SM-invariant variations is used.

The same complete finite-energy variation class is used. mu is L2 since
area=2*pi. Exhausting cutoffs with uniformly vanishing derivative remove
the boundary pairing by Cauchy--Schwarz with the variation's L2 norm.
This is stationarity for admissible differentiable variations, not an
assertion about arbitrary weak fields or changes of prescribed end data.
The energy is pi*n^2*kappa(Z^2)/g6^2. For the full adjoint trace,
kappa(Z^2)=1800, verified on the full root roster; this is a normalization
in supplied curvature/coupling units, NOT a cosmological prediction.
There is no metric equation here. Positive energy does not establish
a four-dimensional Minkowski vacuum.

The compact Higgs commutant is the preceding faithfully embedded SU5_g.
For n!=0 its curvature additionally enforces commutation with Z.
Z on the defining gauge five is diag(-2,-2,-2,3,3), so the connected
gauge group is exactly S(U3 x U2), with the known Z6 kernel. No separate
Wilson angle is needed in this example. The integer, embedding, spin,
metric and parent remain supplied. At n=0, without a Wilson line, the
group is SU5, an essential opposite control.

This supplies stationary configurations excluded from a classification
that assumes mu=0. The previous zero-residual parallel theorem is not
refuted within its hypotheses; it must not be quoted as all stationarity.

## A negative physical variation in the complete bosonic action

Consider a gauge SU5 root e with[Z,e]=q e, q=sign(n)*5,
Tr(e dagger e)=1. There are six such root directions, transforming
as a complex color triplet or antitriplet weak doublet. They commute
with the WHOLE bundle triple. Let a=f e be the complex connection
variation delta A_x+i delta A_y, and impose

    D_z a=(D_x-iD_y)a=0.

Its real Hermitian components are
a_x=(a+a dagger)/2, a_y=(a-a dagger)/(2i).
D_z a=0 and its conjugate give both linear curvature delta F=0
and background divergence D_x a_x+D_y a_y=0. The second identity is
the physical gauge-fixing condition, not deletion of a matter field.
Such a nonzero charged variation is not pure gauge: a pure gauge's
curvature variation is i[epsilon,F]; in this root sector it can vanish
only when epsilon vanishes, since nq!=0.

The quadratic curvature is NOT zero:

    -i[a_x,a_y]=[a,a dagger]/2.

Every Q/R derivative and commutator residual still vanishes along
A_n+t a, since all gauge-factor generators commute with the Higgs
background. Consequently the FULL action difference is exactly

    g6^2 (V(t)-V(0))
      = -nq*t^2/2 integral dxdy |f|^2
        +t^4/8 integral dxdy Omega^-2 Tr([a,a dagger]^2).

The second term is nonnegative. The kinetic metric is
(1/2)integral dxdy |f|^2. The negative mass squared is therefore
-nq=-5|n| in the supplied units. Overall invariant-trace factors
cancel in this ratio. Omitting the quadratic curvature would falsely
declare the direction flat; merely observing mu!=0 would not prove
stationarity or instability. This gives an actual small-amplitude
energy-lowering path once the following global norms are earned.

## Global negative directions and their actual cusp domain

Let C be the compact elliptic curve and p its removed point. In the
charged gauge-root line the old w acts trivially; the added connection
is d-i*2nq*s. Since S^2=K, its holomorphic Hermitian line is

    L=K^(-k), k=nq=5|n|>0.

No fractional root or spin sign enters L. For a holomorphic local
frame e_L with squared norm h_L, a holomorphic section
b(u) du tensor e_Ldual of K tensor Ldual gives the(0,1) form
h_L^-1 conjugate(b(u)) dbar u tensor e_L. Direct differentiation
shows bar-partial_L dagger a=0, equivalently D_z a=0.
The map is antilinear and isometric up to the common fixed form
normalization. It is the metric adjoint identity, not a flat or
unitary-monodromy assumption.

The complete cusp metric in a disc coordinate u has
h_K comparable to |u|^2(log|u|)^2 in the frame du. Thus
h_L^-1 is comparable to |u|^(2k)(log|u|)^(2k).
A pole of order p0 in b gives squared norm comparable to

    integral_0^epsilon r^(2k-2p0+1)|log r|^(2k) dr.

This is finite iff p0<=k. At p0=k+1 it is the divergent
integral r^-1 |log r|^(2k)dr; the logarithmic endpoint is retained.
For p0<=k the orthonormal squared norm is at most a constant times
r^2 |log r|^(2k+2), so it tends to zero and its fourth power is
integrable against the cusp volume. All modes are smooth on the compact
core. Complete cutoffs put them in the first-order graph domain because
the only new errors are d chi times a, tending to zero in L2. Their
quartic commutator norm is finite, so the actual finite-energy path above
is admissible. This is stronger than an abstract sheaf dimension.

Choose the puncture as origin on the elliptic curve. A nowhere-zero
holomorphic differential omega and Weierstrass functions x,y have
pole orders0,2,3 respectively, with y^2=4x^3-g2*x-g3 on a nonsingular
cubic. For k>=1 the functions

    1; x^a with2a<=k,a>=1; x^a*y with2a+3<=k,a>=0

have distinct pole orders0,2,3,...,k. There are k of them.
Multiply by omega^(k+1) to obtain k independent sections of
K_C^(k+1)(k p). Each maps to a distinct admitted negative direction.
For the first n=1 example they are1,x,y,x^2,xy.
Distinct pole orders prove independence; the standard elliptic
Weierstrass model supplies existence. No Riemann--Roch dimension is
needed to claim this LOWER BOUND. Finite checks of the semigroup
enumeration do not replace the explicit all-k construction.

Hence there are at least6k=30|n| complex negative directions in this
same global background. This is not its full Morse index or a number
of particles/generations. n<0 uses the conjugate roots and gives the
same instability. At n=0 the coefficient vanishes and no negative
claim follows. A further flat Wilson line is NOT part of this witness;
no assertion about arbitrary extra holonomy lifting these modes is needed.

## A changed fermion end is not a computed chiral spectrum

In this gauge-root j=0 sector, the normalized gauge derivative from the
pinned parent calculation is shifted from partial_t+1/2 to
partial_t+1/2+nq. Thus its singular threshold is(1/2+nq)^2;
the conjugate root has(1/2-nq)^2. At n=1,q=5 these are121/4 and81/4.
Both are positive and different from the previous1/4. The central
connection change is not a compact-core-only perturbation in the
orthonormal end operator, despite the identical limiting peripheral p.
This is why its inquiry was not disposed of by the previous homotopy.

This one charged block is not the whole four-slot Weyl mass matrix,
nor its global index. In particular, row/column/trace conjugations
must be rederived before assigning a charged Weyl index. The bosonic
negative direction already prevents using THIS background as the
stable physical SM phase. No fermion-count shortcut is used to decide it.

The positive family and its instability are specific to this supplied
bare action and global magnetic ansatz. Added boundary/source response,
different asymptotics, Higgs backgrounds, embeddings or a different
parent need separate tests. Non-BPS critical points have not been
classified generally. The physical SM/TOE goal remains unachieved.
