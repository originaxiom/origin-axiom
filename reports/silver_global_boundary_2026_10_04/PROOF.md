# Global complement and the split limit

## Recovery is an existing result

Write H=H1(T;E), R=im[H1(M;E)->H], and H*,R* for the dual. The torus
cup pairing is perfect and R*=ann R. Let L be any complement to R. Then
R intersect L=0 and R* intersect ann L=ann(R+L)=0. Consequently both
allowed global H1 spaces, paired using L and ann L, are exactly their
interior kernels. This is B1509 Proposition E's stated complement consequence,
not a new theorem. Orthogonality for a supplied positive metric gives one
explicit complement; it does not derive that metric or a physical action.

## Group cup and cochain representatives

For crossed homomorphisms c and d with coefficients E and E*, the cup
evaluation on the torus cycle [p|q]-[q|p] is
c(p)^T P^(-T)d(q)-c(q)^T Q^(-T)d(p). This is the matrix J in the design.
Closedness of either argument shows exacts in the other pair to zero.
In the program the nondegeneracy of the induced quotient pairing and
agreement with the logarithmic model are additional checks, not assumptions
that a raw cochain pairing is symplectic on all cochains.

In a supplied positive cochain metric M, let B span ker F intersect
ker(D^dagger M). Its columns give all cohomology classes. The projector is
B(B^dagger M B)^-1 B^dagger M. Project restriction cocycles and take their
span C; its projector has the same formula. Their difference is the
orthogonal projection onto L, since C lies in B. All these projectors are
finite-dimensional objects; they are not continuum Cauchy-data operators.

## The degeneration is explicit

W_t(g)=[[V(g),t c(g)],[0,1]] is a flat representation for all complex t
because c is a cocycle. For t nonzero,
W_t=G_t W_1 G_t^-1, G_t=diag(t I4,1). Thus the global cohomology dimensions
and restriction ranks are constant on the punctured parameter line.
At t=0 the coefficient splits. The peripheral cocycle is literally zero,
so the boundary matrices, differential and harmonic representative space
are independent of t, including zero. Exterior powers preserve these facts.

The saved exact ranks give, for m135, dim H=6 and dim R=4 nonsplit versus
3 split in the exterior sector; for m136, dim H=4 and dim R=3 versus 2.
The complement ranks are therefore 2 versus 3 and 1 versus 2. On W the
complement ranks are unchanged (2 on m135, 1 on m136); its count difference
comes instead from unequal global H0. The producer must reproduce these
data before they are used.

Let P_t and P_0 be the orthogonal complement projectors in the fixed
positive boundary metric. Since rank P_0=rank P_t+1, range P_0 intersects
ker P_t nontrivially. For such a vector v, (P_0-P_t)v=v. For orthogonal
projectors the operator norm of their difference is at most one: for all
unit vectors x, -1 <= <x,(P_0-P_t)x> <= 1, and the difference is
self-adjoint. Hence ||P_0-P_t||=1 for EVERY t nonzero, not merely for the
sampled amplitudes. This finite prescription has no norm-continuous
extension to its assigned split value. Any continuous positive metric
family also forbids continuity of finite projectors whose ranks differ;
the displayed exact norm statement uses one fixed metric.

G_t is not an invertible gauge transformation at t=0. Transporting a
metric along G_t generally gives singular limiting metric data. Nonzero
isomorphism is not a license to call the split system gauge equivalent.
Conversely, a nonunitary change of frame at fixed t must transport M;
otherwise a coordinate Euclidean projector need not be covariant.

## What the jump does not prove

For v(t)=(1,t), the full projector v v^T/(1+t^2) is continuous at zero.
Project its image onto the second coordinate: this compressed image is
the whole line for t nonzero, zero at zero. Its own image projector jumps.
Thus a continuous full boundary operator may have a discontinuous
finite-dimensional compression or harmonic intersection. Our rank jump
alone is not a theorem that every full analytic domain must jump.

Similarly C --t--> C has H0=H1=0 away from zero and H0=H1=C at zero;
its Euler index stays zero. A degree-one count may change without a
chiral Fredholm index changing. Neither example is an OA physical model;
both prevent invalid extrapolation of our measured finite ranks.

Theorem 1.2 of Booss-Bavnbek et al., arXiv:2012.03329v1, states sufficient
conditions for continuity of full orthogonal Calderon projections,
including constant inner-solution dimensions. It is not applied here.
Our finite restriction image is not the space of full traces of solutions
of a specified elliptic operator. Connecting them requires the actual
operator, metric, Green form, trace map, nonzero boundary modes and domain.
This is precisely the physical construction still to earn.

The constructive positive is that global data do supply a cohomological
complement recovering the original classes. The constraint is that this
choice cannot simply be advertised as one smooth finite boundary projector
through the split limit. A physical completion must account for the missing
channel, enlarged operator system or changed hypotheses, not conceal it.
