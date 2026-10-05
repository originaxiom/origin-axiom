# What the fixed compact coefficient can and cannot count

Authored before execution. Conditional mathematical argument, same-author
verification; no full interacting physical construction or independent review.

## 1. Literal flat coefficient and marked pair

Use candidate.json's literal matrices and cocycle, not a newly chosen kernel
pivot. Hermitian2 transport is H -> g H g dagger / |det g|. Its determinant
is one, and it preserves x1 x2-x3 squared-x4 squared. Multiply by nu, then
extend by c to W=[[V,c],[0,1]]. The cocycle must have zero evaluation on
both cusp words and both relation words, but cannot be a coboundary. This
proves the extension is nonsplit. It does not mean W is compact/unitary.

The marked mapping torus has a finite two-dimensional bundle spine: one
vertex, three edges, two two-cells, with the given monodromy words. Thus
for rank d, B:C0->C1 and F:C1->C2 compute H0,H1,H2; H3 absolute vanishes.
H2=d*2-rank(F). The peripheral Fox map R and D=(P-I,Q-I) give the cone
M=[[F,0],[R,-D]]. The existing fork formulas compute H1 relative and the
restriction/interior ranks. Poincare--Lefschetz duality gives
H2_rel(E)=H1_abs(Evee)* and H3_rel(E)=H0_abs(Evee)*; H0_rel=0.
These are mathematical equalities for this compact oriented marked pair,
not an assumed physical boundary condition. Euler zero follows from the
spine and also chi(X)=chi(T2)/2=0, as R30 already records.

## 2. A positive metric makes a Hodge operator, not a chosen particle law

For a smooth positive metric H on a flat bundle over the fixed compact
core, write D=A+Psi, A unitary and Psi self-adjoint. Q=d_D+d_D* is an
elliptic formally symmetric first-order operator. Its principal Green
matrix is c(n)=epsilon(n)-iota(n); Psi is order zero. Absolute traces
iota(n)u=0 and relative traces pullback(u)=0 are each half-dimensional
maximal Green-isotropic. The squares impose the corresponding covariant
Robin conditions. Standard compact Hilbert-complex Hodge theory realizes
absolute and relative cohomology, respectively; it requires no unitary
monodromy. This is a specified compact regulator, not a derived cusp law.

Odd/even kernels include ALL degrees: odd=H1+H3, even=H0+H2. In the
adopted twisted fermion packaging those degrees matter; they are not
optional endpoint ghosts to discard by convention. Braun et al. section2.3
and appendixB give the supplied field dictionary. Their boundary-domain
discussion does not derive a nonsplit silver physical boundary law.

Hodge star combined with metric conjugation carries E to Evee and exchanges
absolute and relative traces. A uniform absolute condition on the entire
real parent is therefore not automatically Majorana-invariant. A domain
must be checked under the COMBINED reality map, not its factors separately
(R61). This observation excludes neither mixed Lagrangian domains nor
boundary fields, nor any noncompact/singular end completion.

In particular, comparing H1_absolute(E) with H1_absolute(Evee) is not yet
the same as counting the opposite chiralities of a single reality-compatible
fermion domain. The interior image is an image in cohomology; it specifies
neither a local trace subspace nor an adjoint/Fredholm domain. The fork's
interior asymmetry is preserved, not pronounced physically impossible.

## 3. The boundary term separating Hodge H0 from gauge energy

For a zero-form s, define G(s)=||d_A s|| squared+||Psi s|| squared.
At d_A*Psi=0 integration by parts gives

    ||d_D s|| squared = G(s) + integral_boundary <s,Psi(n)s>.

Indeed the cross term is integral of div(<s,Psi s>) minus the contraction
with div_A(Psi), which vanishes at the harmonic metric. Pointwise the
formal scalar operators agree: d_D*d_D=d_A*d_A+sum Psi_i squared.
But the natural quadratic-form boundary laws differ:

    twisted: (nabla_n^A+Psi(n))s=0;
    positive gauge: nabla_n^A s=0.

Thus a D-parallel s is a zero of the twisted form while G(s) can be positive,
balanced by a negative boundary pairing. Equality of differential expressions
does NOT identify operators with different domains or quadratic forms.

If G(s)=0, both d_A s and Psi s vanish. Metric duality then gives a
parallel section in the dual bundle as well. Hence a nonzero positive
gauge zero mode in a coefficient requires nonzero H0 in BOTH it and its
dual. For this fixed W, the received H0 pair is (0,1); if reproduced,
neither member has a nonzero positive gauge zero mode. Its dual invariant
line is not a reducing unitary trivial summand. For exterior-square W,
both H0 are zero. This addresses only these charged coefficients of R40's
roster; neutral End0(W), the trivial gauge factor and the full boundary
gauge transformations are not enumerated by this inference.

Explicit opposite control: unit-area T2 times [-L,L], A=0,Psi=k dr,
s=exp(-kr), real k!=0,L>0. Then Ds=0 and

    G(s)=2k sinh(2kL)>0,
    boundary pairing=-2k sinh(2kL).

Both signs of k give the same positive G and negative pairing. The
ordinary Neumann law fails; the twisted Robin law holds. These are finite
norms on a smooth compact slab. This is NOT the silver geometric solution,
a full supersymmetric boundary sector, or a derived physical parameter.

## 4. Same-action stationarity does not generate this response

Keep the bare positive potential V=c integral (|F_D| squared+|mu| squared),
c>0. Its first variation is 2c Re(<F,delta F>+<mu,delta mu>).
At F=mu=0 it is zero, including integrated-by-parts boundary terms, for
every regular allowed variation. The compact fixed-Dirichlet harmonic
metric positive is retained. As the fork normal-response proof already
states, its nonzero flag flux is not the derivative of this zero-valued
potential; adding harmonic-map energy would change the action.

These facts do not forbid a stationary chiral theory. They require its
actual boundary sector/domain to supply what the bare Dirichlet admission
does not select. R40's E8 embedding fixes both charged coefficients and
all conjugate/neutral sectors; no single favorable cohomology row licenses
anomaly cancellation. Brackets, real gauge freedom and the derivative
term D_i bar(chi) in the auxiliary-field variation must be tested on the
same full trace law, not separately transplanted from other constructions.

## 5. Mission consequence and scope

A reproduced compact paired baseline is a control, not a whole-program
kill. A reproduced interior asymmetry is an asset, not yet a physical
generation. The next construction must preserve the positive admitted
background and close the same action's boundary/fermion/superfield problem.
Supply or derive every additional boundary functional or field explicitly.
No exhaustive end-law classification, physical anomaly calculation,
three-family selection, normalized parameters, gravity or TOE is proved.

Primary passages personally consulted: Braun et al.,
https://arxiv.org/html/1812.06072v2 (2.34--44), (4.9--18), appendix B.1/C;
Pantev--Wijnholt, https://arxiv.org/html/0905.1968v1 section3.1. The scalar
identity and application to this frozen coefficient are the authored
argument above, not a stronger boundary theorem quoted from those works.
