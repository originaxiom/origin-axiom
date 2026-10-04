# Pure form boundary subspaces and their counts

This authored argument is finite-dimensional topology and linear algebra.
It does not identify a physical Dirac domain or a self-adjoint extension.

## From peripheral monodromy to logarithms

Let P,Q commute. On the joint eigenvalue-(1,1) primary space they are
unipotent. Set X=log P, Y=log Q, by finite nilpotent series. The logarithmic
complex is

    E --(X,Y)--> E+E --(-Y,X)--> E.

Put T_X=(exp X-I)/X, defined as the entire power series with constant
term I, and similarly T_Y. These are invertible finite polynomials here.
The maps I, diag(T_X,T_Y), T_X T_Y intertwine this complex with the
group-cochain complex (P-I,Q-I), (I-Q,P-I). Thus they induce isomorphisms
in cohomology, with no unjustified substitution of logarithms for periods.
Every other joint primary sector is acyclic because P-I or Q-I is
invertible there. In the actual finite sign-primary inputs we check the
entire decomposition and its ranks.

## Dimension of the pure form subspace

For a finite complex tau let K=ker(Y-tau X). Define L_tau(E) as the image
in H1 of closed logarithmic cocycles (u,tau u), u in K. An exact cocycle
(Xv,Yv) has this form precisely when v is in K, and its first component
is Xv. Since X and Y commute, X preserves K. Therefore

    dim L_tau(E) = dim K - rank(X|K)
                 = dim(ker X intersect ker Y) = h0(T;E).

This holds for every finite tau, not just the intrinsic period ratio.
Closed representatives need not inject into H1; quotienting them is
essential. On the dual system the same statement gives dim L_tau(E*)=t0*.
The two spaces pair to zero because the wedge of dx+tau dy with itself
is zero. Boundary duality gives dim H1(T;E)=t0+t0*, so they are full
annihilators, not just an orthogonal subpair.

The word polarization here denotes this explicitly defined cohomological
subspace. Its dimensions need not be half of H1 on each coefficient when
t0 differs from t0*. No Hodge theorem or analytic domain classification is
inferred from the word. The exact cup checks use the dual's original
linear pairing, not an assumed Euclidean identification of E with E*.

## Global allowed count

Write a0=h0(M;E), a0*=h0(M;E*), t0=h0(T;E). B1509 Proposition E gives,
for L and its annihilator,

    N_L = h1_allowed(E) - h1_allowed(E*)
        = dim L - t0 + a0 - a0*.

For completeness: if R,R* are the boundary restriction images, they are
mutual annihilators. Allowed dimensions equal n+dim(R intersect L) and
n*+dim(R* intersect Lperp). The latter intersection has dimension
h1(T)-dim(R+L). Subtracting and using the pair exact sequence yields the
displayed formula, including global invariants. This credits the existing
formula instead of presenting it as a new theorem.

It follows for the pure-form prescription that

    N_L_tau = a0-a0*.

The verified silver coefficients have (a0,a0*)=(0,1) for W and (0,0)
for exterior-square W. Hence this rule predicts (-1,0) for their paired
degree-one differences. It does not reproduce the interior (-1,-1).
It also does not compute a complete fermion index: other degrees, end
states and analytic spectrum cannot be suppressed by this definition.

Removing one class from exterior L changes dim L from t0 to t0-1.
The annihilator correspondingly grows by one, and Proposition E predicts
-1 instead of 0. This control illustrates that the limitation is the
specific uniform rule, not every possible cohomological subspace. Choosing
that deletion to obtain a generation-shaped count is not a physical law.

## Geometry and covariance

For two commuting nontrivial parabolics with the same fixed point, scaling
their matrices to trace two gives P=I+N and Q=I+tau N with N^2=0. After a
simultaneous projective conjugation to translations, tau is their period
ratio. The recorded silver matrices supply these identities exactly; this
does not independently certify discreteness or complete geometry.

Under p'=p, q'=pq, the ratio becomes tau+1. A group cocycle transforms
(c(p),c(q)) to (c(p),c(p)+P c(q)). Applying this to both the pure-form
subspace and coboundaries must recover the recomputed subspace in the new
marking. Constant fibre conjugations likewise transport the log complex
and inverse-transpose dual pairing. These are naturality controls, not
invariance under a change of physical completion.

## Why the physical question remains

Finite torus cohomology specifies neither the boundary term of a physical
action nor the domain of its charged operator. R74 explicitly demonstrates
why cone operator domains can contain more information than this finite
space. A real completion must also account for the background's flux,
all field variations, finite norms, gauge symmetry and superfield maps.
The present calculation rules on one candidate prescription and leaves
those broader requirements untouched.
