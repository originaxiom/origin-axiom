# Fermions through resolved source cores

This is a pre-execution analytic candidate for R30's declared added
model. Finite tests verify its algebraic and normalization controls,
not a global PDE solve or independent proof review.

## 1. An action with an explicit domain

Fix a compact smooth connected oriented Riemannian three-manifold Q
with nonempty boundary. Keep R29's H bundle, flat central connection
A, tube fields and a finite-width stationary h=dF. Bounded density in
the compact smooth Dirichlet Poisson problem gives F in W^(2,p) for
every finite p, hence bounded F and dF. A sharp tube indicator does
not give a C-infinity join. The following argument needs W^(1,infinity),
not that stronger assertion. A smooth density is also admissible.

Use R23's single charged representative R=16_(1). The form coefficients
have unitary line transport L; its conjugate representative is already
accounted for by the parent reality convention. On odd left and even
right profiles declare the quadratic four-dimensional action

    S_f = integral d4x [ i<L,bar-sigma D4 L> + i<R,sigma D4 R>
                        - <R,D_oe L> - <L,D_eo R> ],
    D = d_q+d_q*,  d_q=d_A+q h wedge,  D_eo=D_oe*.

The inner products use ordinary bulk L2. The mass/Yukawa symbol is
exactly q(h wedge+iota_h), the one mapped in R23, not a dimension-only
identification with a fermion. The minimal kinetic action and the
omission of additional allowed couplings are declared model choices.
For general varied h,A the same Hermitian odd operator exists; it
need not define a cochain complex. At the stationary flat/exact point
d_q squared is zero. Varying A or h gives the corresponding bilinear
fermion currents. They vanish at L=R=0, so the coupled zero-fermion
classical stationary point of R29 remains stationary. This does not
construct supersymmetric tube partners, a full-parent lift or a
radiatively stable vacuum.

For c(n)=n wedge-iota_n the Green boundary pairing is
<c(n)u,v> integrated on the boundary (up to the fixed inner-product
ordering). The bounded Hermitian mass has no derivative boundary term.
Choose the absolute subspace iota_n psi=0. Its trace is half-dimensional,
isotropic and its own annihilator for that pairing. Equivalently take
the maximal closed differential and its Hilbert adjoint. On smooth
forms the first-order domain has iota_n psi=0; its square also requires
iota_n d_q psi=0. Scalars thus satisfy

    (nabla_n^A + q partial_n F) psi=0,

not undeformed Neumann data. The quadratic-form domain for scalar
trial functions is H1, with no imposed scalar trace restriction.
The usual elliptic absolute Hodge realization is self-adjoint with
compact resolvent; a bounded Witten term retains this first-order
domain and compactness. The square's Robin data depend on F.^1

If a core tube is merely cut out for bookkeeping, its two outward
normals are opposite. Matching both tangential and normal form data
under the bundle identification cancels the Green terms. In local
outward-normal coordinates the normal components have opposite signs.
Matching just the tangential pullbacks does not suffice. An independent
boundary condition at that artificial cut changes the theory.^2

The absolute condition is a specified compact regulator, NOT the
object's derived physical cusp condition. None of this transfers it
to the complete noncompact space without a separate end analysis.

## 2. Exact finite-width kernels, not merely their Euler difference

At every fixed finite width and fixed Q,

    d_q = exp(-qF) d_A exp(qF).

The two multipliers are bounded, invertible and preserve the maximal
graph domains. They give a chain isomorphism with ordinary flat
cohomology. They are not unitary on the unchanged L2 norm; D itself
is not conjugated to the undeformed self-adjoint D_A. Thus kernels,
not all eigenvalues or norms, have the ordinary dimensions. Hodge
theory for the absolute realization gives ker(D)|degree p=H^p(Q;L).
This also follows by transporting to the bounded positive weighted
metric and applying the elliptic Hodge decomposition. No Morse
critical-point hypothesis is needed for this statement.^1

For the actual R19 compact m202 core, its frozen two-generator Fox
complex has dimensions (1,2,1,0), v=(x-1,y-1)^t and

    P=x^2*y+x^2+x*y^2+x*y+x+y^2+y,
    f=(-(y-1)*P/x,(x-1)*P/x),   f v=0.

Consequently its exact base Betti numbers are:

| extending unitary character | H0,H1,H2,H3 | odd/even kernel |
|---|---|---|
| nontrivial, P!=0 | 0,0,0,0 | 0/0 |
| nontrivial, P=0 | 0,1,1,0 | 1/1 |
| trivial | 1,2,1,0 | 2/2 |

The counts are per R, not per individual spinor weight. They are
independent of finite source width/strength under the stated hypotheses.
They do not contradict R19's three/zero or four/one on a DIFFERENT
singular weighted domain. As width tends to zero, multiplication by
exp(-qF) need not stay bounded; there is no uniform-domain argument.

More generally any extending flat rank-r system on a compact oriented
three-manifold with torus boundary has Euler characteristic zero,
because chi(Q)=chi(boundary Q)/2=0 and twisted Euler characteristic
is r times the ordinary one. This constrains the net graded kernel
of this absolute realization, not every defect theory or closed-space
claim about the ungraded H1 alone.

## 3. Where the relative classes meet their core states

Let N be k disjoint contractible proper arc neighborhoods. R19's
restriction mapping cone is C_rel with d0=(v,r)^t, d1=(f,0), where
r in C^k records unitary local fibre identifications. Reintroduce N's
degree-zero cochains, and define

    C0=C^(1+k), C1=C^(2+k), C2=C,
    d0(t)(c,s)=(v c, r c+t s),  d1(a,b)=f a.

At t=0 this is C_rel plus k independent even states. At t!=0 choose
i0(c)=(c,-r c/t), i1(a)=(a,0), i2=id and projections p onto the
base coordinates. The homotopy H:C1->C0 sends (a,b) to (0,b/t).
Directly, p i=id and id-i p=dH+Hd in every degree. Thus the resolved
complex is chain-homotopy equivalent to the BASE, not the relative
complex. This is an explicit algebraic attachment; t is not a derived
PDE coupling. An arbitrary invertible attachment matrix works by the
same argument with its inverse. A singular matrix can retain pairs.

On an acyclic base the connecting map H0(N;L)->H1(Q,N;L) is an
isomorphism. At k=3 the relative three odd classes therefore have
three even core partners in the split complex; nonzero attachment
can remove all six zero states. The trivial and exceptional controls
retain their ordinary paired base modes. The relative source topology
is an asset, but the connecting map cannot be discarded when attaching
the core. This does not assert actual mode wavefunctions or masses.

## 4. A stronger test: light partners in shrinking logarithmic wells

The exact compact cohomology does not decide the low-energy limit.
For a useful variational statement impose the following quantitative
conditions, explicitly in addition to finite-width boundedness:

1. Around each of k disjoint proper arcs there is a fixed contractible
   neighborhood, with a smooth cutoff chi_j equal to one near the
   ENTIRE arc including its boundary endpoints. Its derivative stays
   a fixed distance from every arc. F_epsilon is uniformly bounded
   on that derivative support.
2. On a fixed interior subsegment of positive length, for
   2 epsilon <= r <= R0,
   |F_epsilon-beta_j log r| <= C, uniformly in epsilon, beta_j>0.
   The volume measure there is comparable to r dr dtheta dz.
3. A and L extend flatly through these neighborhoods. Fixed q>0
   satisfies a_j=q beta_j>=1.

For a local parallel unit section s_j, extend by zero outside the
cutoff support the admissible scalar trial function

    u_j=exp(-qF_epsilon) chi_j s_j.

Its differential is exp(-qF_epsilon) dchi_j s_j. The numerator
||d_q u_j||^2 is uniformly bounded. The denominator is at least a
positive constant times integral_(2 epsilon)^R0 r^(1-2a_j) dr.
Therefore its Rayleigh quotient is bounded above by

    C epsilon^(2a_j-2),   a_j>1,
    C/log(1/epsilon),     a_j=1.

The supports are disjoint, so the same bound holds on their k-dimensional
span with the largest of those bounds. Min-max gives at least k
eigenvalues of the scalar Witten Laplacian tending to zero. A nontrivial
unitary line on connected Q has H0=0, so these eigenvalues are positive
at each finite width. For every exact scalar eigenfunction u with
eigenvalue lambda>0, d_q u/sqrt(lambda) is a normalized odd eigenform
of the same eigenvalue. This follows from the closed Hilbert complex,
not an assumed pairing of numerical eigenvalues. Each pair is a 4D
Dirac mass sqrt(lambda) under the declared action. We have a bound
on at least k light PAIRS, not exactly k eigenvalues or a selected
three-generation spectrum.

This is an all-small-width analytic implication of conditions 1--3.
It is NOT a certified global Poisson asymptotic for the actual m202
solution. The local R29 radial field realizes the needed logarithmic
behavior, but transferring its uniform remainder to a chosen global
solution requires a Green-kernel/gluing estimate. That duty remains
explicit rather than assuming the local formula holds globally.

For the exact hyperbolic radial comparator, fixing F(R)=0 gives

    F_out=beta log(tanh(r)/tanh(R)),
    F_in=beta log(tanh(epsilon)/tanh(R))
          + beta [log cosh(r)-log cosh(epsilon)]/sinh(epsilon)^2.

This is regular at the axis with the actual R29 continuous join.
Its exterior norm per 2*pi*axis-length is

    tanh(R)^(2a) integral_(tanh epsilon)^(tanh R)
                              t^(1-2a)/(1-t^2)^2 dt.

At a=1 the primitive is log(t)-log(1-t^2)/2+1/[2(1-t^2)].
At a=2 it is 2 log(t)-log(1-t^2)-1/(2t^2)+1/[2(1-t^2)].
These diverge logarithmically and quadratically, respectively, at
the lower limit. At a<1 the transverse singular norm need not diverge.
Reversing q reverses the weight and does not prove the same scalar
bound. The strong-source qualifier is essential.

An axial cutoff is a real trap. Multiplying by zeta(z) whose derivative
meets the core gives both axial energy and norm the same divergent
transverse factor; their ratio need not vanish. On a product cylinder
zeta=sin(pi z/L) gives pi^2/L^2. The whole-proper-arc cutoff and the
absolute scalar FORM domain avoid that trap. Dirichlet caps, infinite
axes or other end domains need their own argument. No interchange of
width->0 and cusp length->infinity is claimed.

## 5. Gauge currents and the physical consequence

For an unbroken D5 generator with constant normalized gauge profile,
the kinetic normalization gives, exactly,

    g_ij=g7 integral psi_i* (T/sqrt(Vol Q)) psi_j
        =g7 T delta_ij/sqrt(Vol Q).

Thus even a normalized core-concentrating profile has no suppressed
coupling merely because its support becomes small. This is R25's
already-banked normalization identity in the present model. It does
not apply without modification to R29's extra-U1 nonconstant eigenmode.
Each massive left/right pair in the same representation has cancelling
four-dimensional perturbative anomaly; this is not a complete global
anomaly or source determinant construction.

The finite-width extension therefore tests a concrete proposed bridge:
smooth extending flat/exact bulk fermions with absolute outer data do
not inherit R19's unpaired compact zero modes. Under the additional
well conditions, shrinking a core does not make its compensating
partners heavy. A physical completion must change or derive the
relevant ingredients: source/end degrees of freedom and their kinetic
space, nontrivial gauge/Higgs topology, allowed interactions, or actual
boundary conditions, while retaining quantum consistency. None of
those other routes is excluded here; no TOE or empirical fit follows.

## Sources

1. Wen Lu, [A Thom-Smale-Witten theorem on manifolds with boundary](https://intlpress.com/site/pub/files/_fulltext/journals/mrl/2017/0024/0001/MRL-2017-0024-0001-a006.pdf), Mathematical Research Letters 24 (2017), 119--151, section 4, equations (53)--(61), pp. 133--135. Used for the absolute Hilbert-complex realization; its Morse asymptotic theorem is NOT applied to our non-Morse family. Extension to flat coefficients and bounded F here is the stated local/chain argument, not a quote of a stronger theorem.
2. Colette Anne and Junya Takahashi, [Partial collapsing and the spectrum of the Hodge--de Rham operator](https://msp.org/apde/2015/8-5/apde-v8-n5-p01-p.pdf), Analysis & PDE 8 (2015), 1025--1054, section 2.1, p. 1028. Used for whole-form transmission; their different metric-collapse spectral theorems are NOT imported.
