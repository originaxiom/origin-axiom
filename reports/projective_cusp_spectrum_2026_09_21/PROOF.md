# F11 authored cusp contraction and global L2 comparison

Frozen before finite tests. No global harmonic-metric existence claim.

## 1. The coefficient and its longitudinal inverse

Keep F10's exact Cx=-N/sqrt(u), Cy=-kD-beta P/u,
Cz=u'H/(2u), u=z^2/4-beta^2/L^2>0, k=log(q)!=0. Coordinate periods
are one and g=z^-2(dx^2+L^2dy^2+dz^2). The Hermitian fiber metric is
identity in this frame. All coefficients depend only on z. Define
T=partial_y+Cy. Fourier transformation along y replaces partial_y by
i omega, omega=2pi n (or a real phase-shifted frequency).

With S=i omega I-kD and gamma=beta/u,

    T^-1=S^-1+gamma S^-1 P S^-1.

This is an EXACT inverse, since P^2=0 and [D,P]=0. Every diagonal
entry of S has real part -k or 3k, so ||S^-1||<=1/|k| uniformly in
ALL frequencies, not a finite-mode truncation. Since ||P||=1,

    ||T^-1|| <= B(z)=1/|k|+|beta|/(u |k|^2).

It preserves smoothness locally and acts boundedly on torus L2.
The dual connection -C^T has the same bound, with the nilpotent term
transposed and its sign changed. A unitary phase shifts omega but does
not change its real-part bound.

## 2. Full differential homotopy, including the radial direction

The covariant Cartan formula gives

    {d_C,iota_y}=T,       [d_C,T]=0.

The second identity uses FLATNESS and y-independence. It includes
Cy'+[Cz,Cy]=0; an invertible family of torus matrices alone is not
sufficient. Thus, on smooth forms,

    K=iota_y T^-1,       d_C K+K d_C=I.

In the actual hyperbolic form norm, contraction by partial_y has norm
|partial_y|=L/z in all relevant degrees. On a tail z>=Z beyond the
lower cutoff, u is increasing, so

    ||K|| <= b(Z):=L B(Z)/Z -> 0 as Z->infinity.

Distributional extension of the identity shows that K takes the maximal
d_C graph domain to itself: d_C K u=u-K d_Cu. This is a bounded
chain homotopy on the cusp, not merely ordinary algebraic acyclicity.
Completeness and the bounded cutoff commutator give minimal=maximal
d_C domains on the full manifold, just as in F02; local mollification
for a first-order differential operator supplies the graph approximation.
On a cusp considered by itself we use its maximal domain at the artificial
lower edge, without installing that edge as a physical boundary.

## 3. Compact resolvent and a valid global Hodge problem

For a compactly supported form a above Z, integrate the homotopy:

    ||a||^2 = <d_C^* a,K a> + <a,K d_C a>
       <= sqrt(2)b(Z)||a|| (||d_C a||^2+||d_C^*a||^2)^(1/2).

Consequently the tail quadratic form satisfies

    ||Q a||^2 >= [2b(Z)^2]^-1 ||a||^2,
    Q=d_C+d_C^*.

Flatness makes ||Q a||^2 the sum of the two squared differential norms.
F02 gives the unique complete-space self-adjoint realization. For a
smooth radial cutoff equal to one above eZ, zero below Z and with
uniformly bounded |d chi|, ||Q(chi a)||<=||Qa||+C||a||. The inequality
therefore bounds the L2 norm above eZ of any graph-norm bounded family
by a constant times b(Z), tending to zero. On each compact truncation,
interior elliptic regularity and Rellich give compactness. These two
facts prove compact embedding of the Q graph domain into L2, hence
compact resolvent of Q and its square. The argument covers every degree
and the dual bundle separately. It does not equate their nonzero spectra.

The associated Hilbert complex has closed ranges and finite-dimensional
cohomology; its harmonic spaces represent unreduced cohomology. This is
the standard Hilbert-complex consequence, not a cusp-specific theorem
borrowed without hypotheses. Compare Arnold--Falk--Winther, section 3.1.3:
https://arxiv.org/html/0906.4325v3#S3.SS1.SSS3

Uniformly equivalent smooth positive norms in every degree preserve the
bounded homotopy, with b(Z) multiplied by at most sqrt(M/m). They also
preserve the same distributional complex and graph domains. The same
tail and local-compactness argument applies, allowing compact-core
metric changes. An unbounded change of norm or changed differential is
not covered. No uniform estimate as q->1 is asserted.

## 4. The actual maps to compactly supported and ordinary cohomology

Extend a smooth cutoff chi, equal to one high on every cusp and zero
on the compact core, and set H=chi K on each end. Then

    R=I-d_C H-H d_C=(1-chi)I-dchi wedge K

is a chain map with compactly supported output. Smooth harmonic L2 forms
a therefore have a compact representative Ra=a-d_C(Ha) in the same
L2 class. Ha belongs to the graph domain by the bounded homotopy.
This proves surjectivity of compactly supported cohomology onto L2.

For injectivity, suppose a smooth compactly supported closed a is
d_C v with v in the global L2 domain. Closed-range Hodge theory and
elliptic regularity allow a smooth minimum-norm primitive v. Above the
support of a, d_Cv=0, so v=d_CKv. Choose chi supported there. Then
v'=v-d_C(chi Kv) has compact support and d_Cv'=a. Thus a was already
compactly supported exact. For degree-one a the primitive is degree
zero; K vanishes on it, and the contraction identity directly forces
the closed degree-zero v to vanish on the high cusp. This also covers
that endpoint of the argument.

We have therefore EXHIBITED the cohomology isomorphism

    H^p_(2)(M;E) = H_c^p(M;E) = H^p(core,whole boundary;E).

F10's peripheral acyclicity, and the long exact sequence, further identify
this with ordinary H^p(core;E). The same applies to E*. F10's Euler and
Poincare--Lefschetz argument now DOES transfer to the actual ordinary-L2
degree-one zero modes:

    dim ker Delta_E^1 = dim ker Delta_E*^1.

This holds for every smooth completion in the declared norm class,
whether or not it solves the global moment equation. It therefore
constrains any BPS completion there, without assuming one exists.

For a finite cover, use the closed longitude-flow circles on each
lifted cusp. Their period is a positive integer d; frequencies become
2pi n/d, and the same inverse bound holds. The lifted lattice need not
be rectangular: the original vector field and its length L/z pull back.
The contraction, compactness and whole-boundary arguments survive on
all finite-cover pullbacks, with optional scalar unitary characters.
These are not all members of the arithmetic class with arbitrary data.

## 5. The member's exact coefficient cohomology test

For r=m w n^-1 w^-1, w=n m^-1 n^-1 m, use the word
r='mnMNmNMnmN'. A cocycle has arbitrary generator values in E^2 subject
to its evaluated Fox row J; coboundaries are columns of
B=(rho(m)-I,rho(n)-I)^T. Directly from the derivation rule,

    dim H1(pi1;E)=8-rank J-rank B,       J B=0.

This H1 formula needs no assertion about a presentation's H2. Compare
two implementations: prefix Fox derivatives and affine 5-by-5 block
lifts. Evaluate the ACTUAL defining four, not the adjoint tangent module.
For rho_chi=chi rho, chi in {1,-1,i,-i}, test the relation and every
maximal minor. Since entries have only powers of q in denominators,
positive-q rank drops are exactly the common positive real roots of
the real and imaginary numerator polynomials of those minors. An exact
polynomial gcd and Sturm root count certify the parameter scope; sample
ranks alone do not. The expected zero and geometric-point counts await
execution; they are not used in sections 1--4.

## 6. q is fixed end data, not a normalizable scalar in this family

At fixed base L, varying k=log q in the explicit F10 family gives
tr(D delta Psi_y)=-12 delta k, because tr(DP)=0. Since tr(D^2)=12,
the Frobenius norm inequality gives ||delta Psi_y||^2>=12|delta k|^2.
Its contribution to the kinetic norm is at least

    (12 |delta k|^2/L) integral_Z^infinity dz/z = infinity.

A smooth unitary gauge variation acts on Psi_y by [Psi_y,epsilon].
Since [D,Psi_y]=0, its trace against D is zero pointwise; the displayed
projection cannot be removed by such a gauge variation. This statement
concerns this family's fixed-base modulus and ordinary kinetic norm,
not gravitationally mixed modes or an alternate end action. It does
not reject a fixed-q background with zero residual potential.

## Scope and next duty

This is a whole-end statement for an explicit norm/differential class,
not a no-go for sources, partial boundary conditions, nonflat fields,
different asymptotic growth, or a quantum interacting mirror gap.
Even if free modes pair in number, positive spectra/couplings need not
be equal. Their dynamics, the source/end completion and gravity remain
separate tasks; no physical mass value or completed TOE follows.
