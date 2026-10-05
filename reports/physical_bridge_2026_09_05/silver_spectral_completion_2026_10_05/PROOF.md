# Conditional analytic completion and its exact limits

Authored proof, nonauthor analytic acceptance pending. This is NOT a
stationary interacting chiral Standard Model or parameter-free selection.
Sources: our operator/smooth gates; R40 COEFFICIENT_PARENT_PROOF.md; R61
FERMION_END.md; fork silver_global_boundary / silver_boundary_complex /
silver_cyclic_boundary_2026_10_04. The fork owns the finite cone and cup
construction; this packet tests a particular smooth spectral lift of it.

## 1. Why the uniform local baseline has zero index

Let X be the compact oriented core, E a complex determinant-one flat
bundle, H a supplied smooth positive metric. The mapping-torus core has a
two-dimensional CW spine. SL(n,C) retracts onto SU(n), whose pi0 and pi1
vanish: SU2=S3 and the fibration SU(n-1)->SU(n)->S^(2n-1) gives the
induction. Extend a frame over cells to trivialize E topologically. This
does NOT trivialize its flat monodromy or the nonsplit extension.

In a global H-unitary frame, Q_D=d_D+d_D^* differs from ordinary Q_d by
a smooth odd symmetric zeroth-order term. For the coefficient-independent
uniform complex-line trace law of silver_smooth_boundary_gate, the
selfadjoint elliptic H1 domain is fixed. Q_s=Q_d+s(Q_D-Q_d) is Fredholm
with fixed graded domain; its graded index is constant. At s=0 the signed
three-dimensional Hodge map combined with conjugation exchanges parities,
anticommutes with Q_d (hence preserves its kernel), and preserves that
domain. Thus dim odd-dim even=0.
The probe checks the symbol/domain prerequisites, not the global theorem
by finite sampling. This scopes that law only; changing the domain by a
finite harmonic polarization is not this homotopy.

## 2. Spectral exact block

On closed Sigma=T2 use twisted de Rham d_t and H to decompose smooth
forms into harmonic, exact and coexact parts. Let Ah be a graded harmonic
subspace realizing the fork's finite cyclic Lagrangian: Ah0=k=sl5 gauge,
Ah2 its trace-pair annihilator, Ah1 a paired polarization. Then define

    Ainf0 = (H0)^perp,H + Ah0
    Ainf1 = im d_t^0 + Ah1
    Ainf2 = Ah2.

The high block (H0)^perp -> im d0 is acyclic: d0 is bijective there,
with smooth inverse from the boundary Green operator. Thus Ainf is a
subcomplex quasi-isomorphic to Ah. The complementary coexact1->exact2
block is acyclic as well. This includes primitives, unlike a naive
closed-preimage lift that retains exact1 without scalar primitives.

These are classical order-zero pseudodifferential projections with finite
harmonic modifications. At real xi=(x,y)!=0, alpha spans (1,xi), beta
spans (xi_perp,area). Restricted i(epsilon_xi-iota_xi) on alpha has
determinant -(x*x+y*y)^2, in the unnormalized basis. Hence the full trace
domain alpha in Ainf, beta in Ainf^perp,H has zero maximal Hermitian
Green current and satisfies the elliptic principal-symbol criterion.
The trace is graded. By Bär--Ballmann sections3.2-3.6, especially
Theorems3.11 and3.15, its compact Hodge--Dirac realization is selfadjoint,
elliptic, with compact resolvent and smooth zero modes.
[Primary text](https://arxiv.org/html/1307.3021v1).

For the trace bilinear pairing, exact1/exact1 and exact1/closed1 integrate
to zero by Stokes and invariance. The Hodge identification between the
dual complex and the Hermitian adjoint complex makes nonharmonic0
orthogonal to the paired harmonic2. Ah is cyclic maximal by the paired
cup construction. Thus Ainf is cyclic maximal and combined E8
reality/Hodge conjugation preserves the full trace law. This does NOT
make a fixed linear space closed under all smooth nonlinear brackets.

## 3. Smooth cohomology is the finite cone

Let Omega_A(X) consist of smooth forms with tangential restriction in
Ainf. Take its graph closure degree by degree for d_D. Since d maps
the smooth domain to itself and d^2=0, graph approximation gives a closed
Hilbert complex (d u is approximated by d u_j, with d(d u_j)=0).
Its adjoint Green boundary condition is precisely normal trace in
Ainf^perp,H. The combined elliptic Hodge realization above regularizes
its harmonics and has finite-dimensional kernel and closed ranges.

Collar extension makes restriction Omega(X)->Omega(Sigma) surjective.
The short exact sequence of complexes

    0 -> Omega_A(X) -> Omega(X) -> Omega(Sigma)/Ainf -> 0

identifies its cohomology with Cone(Omega(X) plus Ainf -> Omega(Sigma))[-1].
Replacing Ainf by its quasi-isomorphic harmonic Ah and both de Rham
complexes by marked cellular complexes yields the fork's full cone K.
This is a cohomology comparison, not a literal equality of cochain
harmonic representatives and unknown PDE wavefunctions. Hodge theory
then identifies H^j(K) with the degree-j kernel of THIS graded operator.
All norms are finite and positive on compact X with smooth positive H.

Matthias Lesch's four-page primary seminar report (1991), pp116-118,
personally read fully including formulas and references, explains ideal
closed extensions, the strong Hodge decomposition and the smooth-domain
cohomology theorem for Hilbert complexes. It reports joint work with
Jochen Brüning, but is NOT the full 1992 joint journal paper.
[Primary report](https://www.numdam.org/item/TSG_1991__S9__115_0.pdf).
Its theorem does not choose our Ainf or verify the nonlinear theory.

## 4. Exact charged index and conditional anomaly

Use R40's full roster:
248=(24,1)+(1,24)+(10,5)+(bar10,bar5)+(5,bar10)+(bar5,10).
Gauge10 has coefficient W, gaugebar5 has F=exterior-square W.
For charged E, Ah0=0 and Ah2=full boundary H2. Let ell=dim Ah1(E),
and choose Ah1(Edual) as its cup annihilator. All four cone degrees,
the global H0 restriction and degree-two restriction map are retained.
H0(K)=H3(K)=0: H0 restriction injects and Ah2 surjects onto H2boundary.
Since chi(X;E)=chi(Sigma;E)=0,

    J(E)=dim H1(K)-dim H2(K)=ell-dim H0(Sigma;E).

For this literal coefficient the dimensions are2 for W and3 for F;
the native and separate reference must reproduce them, not assume them.
Thus J(W)=ellW-2, J(F)=ellF-3, and both dual indices are opposite.
Individual H1/H2 depend on intersection ranks; the index does not.

Under the declared four-dimensional Weyl dictionary, SU5 cubic anomaly
is J(W)-J(F). The probe derives Tr_10 H^3=Tr_5 H^3 for traceless H,
retaining conjugates and neutral real adjoints. Anomaly-free dimensions
are ellF=ellW+1, giving common index -2,-1,0,1,2. No common index3 in
THIS rank-five coefficient/domain family; this says nothing about larger
covers/coefficients or another boundary sector. Integer-dimension census
is complete (35); prescribed flags are only witnesses in each dimension.
No inflow or hidden boundary particles are silently introduced. Even an
anomaly-free nonzero J is conditional operator content, not genesis
selection, an interacting family, observed masses or SM breaking.

Neutral End0W is self-dual for trace and Ah1=restriction image, a half
polarization. Native multiplicities are computed; reference only checks
the neutral index-zero implication. Trivial gauge adjoint Ah0=H0,
Ah1 a supplied nonreal harmonic line, Ah2=0 yields H=(1,0,0,1) per
coefficient: all gauge endpoint modes retained. Gauge/scalar equations
of the full parent are not inferred from this fermion trace alone.

## 5. Necessary supersymmetry positive and nonlinear mismatch

Ainf1 contains every exact d_t chi. The auxiliary derivative term that
escaped the earlier rigid line is now admitted, including all nonzero
boundary modes. This discharges that particular linear derivative test,
not all external/normal/D-term or superfield transformations.

In the trivial gauge block take epsilon=sin x E12 in Ainf0, and
a=d(sin y) E23 in Ainf1. Their bracket is sin x cos y dy E13,
whose derivative is cos x cos y dx wedge dy E13, not zero. Since
Ainf1 consists of closed forms, it is NOT closed under this gauge action.
The fixed linear lift therefore does NOT yet define the nonlinear
interacting boundary theory. A field-dependent covariant projection,
nonlinear gauge-orbit completion or an explicitly priced boundary action
can change that verdict; none is excluded here. The surviving bulk cubic
and finite harmonic cyclic bracket are not discarded by this test.

## 6. Research status

This is a conditional analytic proposal supported by exact finite
certificates and primary functional theory, not a numerical global PDE
solution or a nonauthor theorem certificate. Publish measured results
and failures separately in FINDINGS. Exact nonzero indices, if obtained,
are preserved along with selection, nonlinear action, anomalies, full
physical spinor identification and full-suite review duties. No whole
architecture negative, no full Standard Model/TOE or qualia derivation.
