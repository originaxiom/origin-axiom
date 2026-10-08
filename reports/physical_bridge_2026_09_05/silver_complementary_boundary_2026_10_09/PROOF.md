# A strict complementary boundary and its physical cost

Authored proof with finite implementation controls; nonauthor acceptance
pending. The domain below is supplied, not derived from genesis.

## Setup and the complementary complex

Let C=Omega*(Sigma;ad E8_C) on the compact boundary torus, with the
unchanged flat differential D and invariant bilinear integrated pairing
B(u,v)=integral Tr(u wedge v). Use the compatible positive auxiliary
metric and cyclic Hodge contraction (h,P) of the cyclic-transfer packet:

    Dh+hD=1-P, h^2=0, Ph=hP=0.

Pairing compatibility gives B(im h,im h)=0 and B(im h,H)=0. Here H=im P
is harmonic; no unitarity of the nonsplit holonomy is assumed. The full
E8 gauge factor k=sl5_C is parallel. Its compact form preserves the
auxiliary metric, so k commutes with D, adjoints, Green operators, h and
P, by complexifying that compact equivariance. Let L subset H1 be the
same k-stable harmonic Lagrangian as in the earlier finite cone. Define

    A0=k, A1=im h2 direct-sum L, A2=ann_B(k) subset C2.

Because k is harmonic, A2=im D1 direct-sum ann_B(k) in H2. Hodge
decomposition gives im h2=im D1*. D1:im h2 -> im D1 is a bijection
with inverse h2: D1 h2=1-P2 and h2 D1 is the coexact projector. Thus
A is a subcomplex and inclusion Ah=(k,L,ann_H2 k) -> A is a chain
quasi-isomorphism. The extra two-term complex is acyclic, in degrees
one and two. It cannot create new harmonic classes.

A is maximal isotropic: its degree-zero and degree-two pieces are
annihilators; in degree one, im h2 is isotropic, pairs nondegenerately
with im D0, and is orthogonal to H1. Adding L gives exactly half that
symplectic space. These are integrated, generally nonlocal conditions.

## Exact nonlinear closure

Degree zero closes since k is a Lie algebra. Its action preserves all
three A pieces: h is equivariant, L is k-stable, and invariance preserves
ann(k). For u,v in A1 and c in k,

    B(c,[u,v]) = B([c,u],v) = 0.

The last equality uses [c,u] in A1 and isotropy, not a zero bulk bracket.
Hence [A1,A1] subset A2. Higher degrees vanish on a surface. These
statements prove A is a strict cyclic DG Lie subalgebra, for the entire
E8 bracket. The argument is representation-independent after its actual
k-equivariance and cyclic hypotheses have been established.

The boundary BFV Hamiltonian

    S = integral Tr(c D a + c[a,a]/2 + [c,c]b/2)

restricts identically to zero on c in A0, a in A1, b in A2. Indeed Da
and [a,a] are in A2 while [c,c] is in k. All terms are polynomial;
no formal infinite series or convergence of a canonical transformation
is needed for THIS boundary. Its zero restriction does not set the bulk
interaction to zero. BFV c and b are ghost coordinates, not particles.
The earlier exact completion remains a different, non-strict boundary.

## Elliptic Hodge domain and reality

Write the full collar trace as alpha + dr wedge beta. Impose alpha in A,
beta in its Hermitian orthogonal complement. At a nonzero real tangent
covector xi=(x,y), the principal symbols are

    alpha = span((-y dx+x dy), dx wedge dy),
    beta  = span(1, x dx+y dy).

They are complementary orthogonal planes in boundary forms. The
tangential Clifford symbol q=i(epsilon_xi-iota_xi) preserves each plane,
has q^2=|xi|^2, and its restriction has determinant -|xi|^4 in these
unnormalized bases. The full normal symbol gamma exchanges the slots.
The adapted symbol -gamma diag(q,-q) exchanges the allowed full trace
with its Hermitian complement. Its square is |xi|^2, so projection from
either of its sign eigenspaces to the allowed trace is an isomorphism.
This proves the pseudodifferential ellipticity criterion at EVERY
nonzero covector; sampled reference matrices are only controls.

The normal Green form is zero on this half-dimensional trace; degree
parity preserves it. Signed three-dimensional Hodge conjugation with
the E8 dual pairing also preserves it: cyclic annihilation maps the
tangential plane to the required normal complement. In the harmonic
sector this is exactly the previous paired Ah law, not an additional
requirement that each charged L be separately real. The finite matrix
test checks the high symbol; the full assertion uses compatible Hodge
duality and the same harmonic polarization.

The projectors are classical order zero plus harmonic smoothing terms.
On a smooth compact core, Bär--Ballmann Theorems 3.9, 3.11 and 3.15
give smooth kernels and a selfadjoint elliptic realization of D+D*.
This is an application of their hypotheses, not an identification of
that auxiliary metric with the physical background metric.
[Primary source](https://arxiv.org/html/1307.3021v1).

## Why the same cone survives

Use the graph-closed differential on forms whose smooth tangential
trace lies in A. The closed Hilbert-complex and elliptic-extension
argument in spectral-completion PROOF section 3 applies unchanged:
only the tangential subcomplex and its symbol have changed, both now
checked above. The short exact restriction sequence identifies its
smooth cohomology with Cone(Omega(X) plus A -> C)[-1].

The inclusion Ah -> A commutes literally with their inclusions in C.
Consequently the map of these cones, identity on the two ambient
complexes, is a quasi-isomorphism. The same inclusion Ah -> Aold gives
a zigzag between the old and new cones. This proves equality in ALL
cohomological degrees, not only Euler characteristics. It is not a
unitary equivalence of spectra or of nonlinear boundary theories.
Thus the earlier full charged cone tables carry to this graded Hodge
operator, conditionally on the stated setup; all 35 choices remain.
The old formula J(W)=ellW-2, J(exterior-square W)=ellF-3 and its
conditional SU5 anomaly relation are unchanged. No new physical
particle identification follows from that cohomology equivalence.

## The affine holomorphic boundary primitive

Fix a flat reference connection Astar and let a=A-Astar. With outward
boundary orientation and W(A)=integral Tr(A dA/2+A^3/3), direct graded
integration by parts gives

    W(A)-W(Astar)
      = integral Tr(a Dstar a/2 + a^3/3) - integral_boundary Tr(Astar a)/2.

The relative functional therefore includes the explicit reference
counterterm +integral_boundary Tr(Astar a)/2. Its variation is

    delta Wrel = integral Tr(delta a (Dstar a+a^2))
                  - integral_boundary Tr(a delta a)/2.

For a and delta a in A1 the boundary term vanishes exactly. The affine
reference term in the unmodified functional does not in general vanish;
the fixed reference and its counterterm are priced inputs. This result
is for the holomorphic Chern-Simons sector. It is not the full real
bosonic/fermion action, a source equation, or a large-gauge anomaly test.

## The changed scalar and superfield obligation

The new A1 intersects im D0 only in zero, by Hodge decomposition.
Therefore Dchi in A1 if and only if Dchi=0. Unlike Aold, this law
rejects all nonzero exact auxiliary gradients. At nonzero xi the
coexact projector kills xi, and the rejected gradient norm is |xi|^2.
This is a real cost, not a universal chirality obstruction.

If physical scalar/gaugino boundary traces are restricted to k, this
particular interacting term is allowed: Dstar chi=0 and [a,chi] in A1.
Preservation also requires the vector multiplet's A_mu and real D-field
to have compatible traces and their normal equations to follow from
the same action. No BFV ghost-to-gaugino identification is presumed.
Braun et al. Appendix B.1 equations B.1-B.7 explicitly contains the
internal covariant derivative of the conjugate gaugino in the auxiliary
variation; its vector-multiplet variation also constrains D. These
equations motivate this necessary check, not a sufficiency theorem.
[Primary source](https://arxiv.org/html/1812.06072v2#A2.SS1).

Next derive those full real variations and their boundary response.
The previous fixed-Dirichlet harmonic metric remains a positive result
but does not automatically solve the new boundary law. Stationarity,
stability, a physical chiral spectrum, boundary anomaly accounting and
generated selection remain to be established on one construction.
