# Exact cohomology and conditional admission

## Algebra on the marked pair

The signed LLRR automorphism of the free group on (a,b) specifies an oriented
once-punctured torus bundle X. L sends a to ab, R sends b to ba. The negative
row composes a to a inverse and b to b inverse. Both preserve orientation on
the fibre. The standard presentation complex is a spine of X. Its cochains
have dimensions d,3d,2d over K. The cusp words are the fibre commutator and
t for the positive row, or abt for the negative row. The free-word check
verifies the correcting conjugation, not just the matrices' commutation.

Write B for stacked rho(g)-1 and F for the Fox relation map. Then
H1(X;E)=ker F/im B. On the boundary torus write P,Q for the commuting
holonomies, D=[P-1;Q-1], and R for evaluation on the two cusp words.
The mapping cone in degree one is C1(X;E) plus C0(boundary;E), with

    cone differential = [[F,0],[R,-D]],   cone degree zero = [B;1].

Thus if M is this differential and ranks are over K,

    h1_abs = 3d-rank F-rank B,
    h1_rel = 3d-rank M,
    restriction_rank = rank M-rank F-rank D,
    h1_int = h1_abs-restriction_rank.

The last formula counts ker(H1(X)->H1(boundary)), equivalently the image
of H1(X,boundary)->H1(X). The exact pair sequence independently gives
h1_rel=h0_boundary-h0_absolute+h1_int. Absolute and relative are candidate
domains of the de Rham complex, whereas the image alone does not specify
a fermion operator domain. A physical dictionary must still be derived.

For an oriented compact three-manifold with torus boundary, duality gives
h2_absolute(E)=h1_relative(E dual). Since the spine has Euler characteristic
zero, h2_absolute(E)=h1_absolute(E)-h0_absolute(E). These identities provide
cross-checks with actual dual coefficients. They do not identify an arbitrary
degree-one dimension difference with the net chirality of physical fields.

## Exact implementation and cocycle gauge

Restricting K=Q(sqrt(2)) to Q doubles all dimensions. Multiplication by a+b
sqrt(2) is [[a,2b],[b,a]]. The trace pairing has Gram matrix T=diag(2,4), so
Res(A inverse transpose)=T inverse Res(A) inverse transpose T. The exterior
square is formed over K first; exterior squaring the rational restriction
would produce a different representation and is forbidden here.

A vector (c,w) in ker M obeys Fc=0 and Rc=Dw. Replacing c by c-Bw makes
Rc=0 and leaves its absolute cohomology class unchanged. Its class is
nonzero exactly when adjoining c to B increases the rank. Then
W(g)=[[V(g),c(g)],[0,1]] is a nonsplit extension, with a literally split
peripheral restriction. For a one-dimensional interior space every nonzero
class is lambda c modulo a coboundary. Scaling the V block by lambda and
a triangular change of splitting give isomorphic W. This establishes the
nonzero-class scope once the interior dimension is independently verified.

## Conditional harmonic admission

Wu and Zhang, Proposition 3.3, applies to a smooth flat vector bundle on
a connected compact Riemannian X with nonempty smooth boundary and supplied
positive smooth Hermitian boundary metric K. It gives a unique harmonic
metric with that boundary value. The proof uses heat flow, a scalar Dirichlet
barrier and elliptic regularity; uniqueness follows from the nonnegative
Laplacian of the metric distance and the maximum principle. No semisimplicity
condition is imposed on this compact boundary problem. This application is
already identified in physical R81. We read the primary proposition and
proof, surrounding setup and Corollary 2.1, not the entire paper:
https://arxiv.org/html/2109.01776v1 (accessed October 4, 2026).

Given a verified SL(5) W, its determinant has a flat trivialization. If det K=1
there, tracing the harmonic equation makes log det H harmonic with zero
boundary values, hence det H=1. Both W and its dual are admitted in this
conditional sense. This does not pick one order, derive K, or identify the
metric boundary condition with a fermion boundary condition.

For the invariant rank-four V in W, let P be the H-orthogonal projector,
xi=5P-4I and eta the off-diagonal block of D relative to V and its orthogonal
complement. With D=A+Psi, I=-2 d_A^*Psi, outward normal n, the integrated
projector identity is

    integral tr(xi I) = 5 integral |eta|^2
                       +2 boundary integral tr(xi Psi(n)).

It follows by integrating tr(xi d_A^*Psi), using the invariant upper block
form and metric compatibility of A. The algebraic commutator contraction
contributes -5|eta|^2/2 before multiplication by -2. For harmonic H the
left side vanishes; a nonsplit extension has eta not identically zero for
any smooth metric, so the boundary flux is strictly negative. This is a
necessary balance, not a separate equation determining the boundary law.
R81 already gives the rank-five identity; no numerical flux is transferred
from its different carrier or claimed here. On this compact pair smooth
fields have finite integrals; no complete-cusp finite-energy limit follows.

The mathematical admission is a genuine retained positive. Physical progress
requires a principle producing the boundary law and the domain of charged
fermions from one action. This calculation tests the latter sensitivity;
it supplies neither that action nor a parameter-free state-selection rule.
