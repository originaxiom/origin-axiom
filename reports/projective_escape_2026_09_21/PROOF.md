# F10 authored application of a known global representation family

Frozen before execution. Published geometry, exact matrix identities and
authored analytic applications carry different verification grades.

## 1. The actual linear bundle, not only its projectivization

Use Ballas' section-6 meridian generators, with t=q/2>0:

    M=[[1,0,1,t-1],[0,1,1,t],[0,0,1,t+1/2],[0,0,0,1]],
    B=[[1,0,0,0],[2+1/t,1,0,0],[2,1,1,0],[1,1,0,1]].

They have determinant one and satisfy M W=W B, W=B M^-1 B^-1 M.
Compute the longitude Lambda=B M^-1 B^-1 M^2 B^-1 M^-1 B from
these generators. It commutes with M and its abelianization is zero.
Its characteristic polynomial is (X-q)^3(X-q^-3), and

    tr Lambda-tr Lambda^-1 = -(q-q^-1)^3.

The paper later replaces Lambda by Lambda/q in PROJECTIVE coordinates.
That is legitimate there, but changes determinant to q^-4 and is not
the same SL4 local system. A scalar character of the knot group is
trivial on the longitude, so it cannot make that replacement while
leaving the underlying generator representation unchanged.

At q=1 the exact simultaneous intertwiner to rho(g)=g tensor bar(g)
is computed using the two parabolic SL2 matrices in DESIGN.md. The
intertwiner is invertible and both equations are checked. This connects
the curve to F08's coefficient, not to the unrelated holomorphic Sym3.
Ballas' theorem supplies nearby properly convex structures of finite
BUSEMANN volume. It supplies no harmonic metric for the adopted gauge
equations on the fixed Riemannian hyperbolic base.

## 2. A genuine escape from the flat bundle pairings

An invertible flat linear map E->E* would imply that Lambda and
Lambda^-T are similar, hence their traces equal. For q>0,q!=1 the
displayed difference forbids it. An invertible flat antilinear map has matrix
equation P conjugate(Lambda)=Lambda^-T P. Since this family is real,
the same trace mismatch forbids that too. This includes every such
bundle isomorphism, not merely a failed trial with F08's J. The conclusion
also survives scalar fourth-root characters: they do not change Lambda.

For a finite cover, a nonzero positive power Lambda^d belongs to each
relevant peripheral subgroup, up to conjugacy. Its trace difference is
-(q^d-q^-d)^3, still nonzero. The same obstruction to flat bundle maps
holds on these pullbacks. It does NOT exclude an isometry of the base
combined with a bundle map, accidental spectral equality, or interacting
symmetries. Breaking a sufficient pairing mechanism is not proof of
spectral chirality.

## 3. An exact local parent solution on the deformed cusp

For q!=1 set N=E02+E23, P=E03, D=diag(1,-3,1,1), H=diag(1,0,0,-1).
The meridian logarithm n=(M-I)-(M-I)^2/2 has n^3=0.
Put a=q^-3-q and Pi=((Lambda-q I)/a)^2. This is the simple-eigenvalue
projector; its complement is the generalized q-eigenspace. With
p3=(I-Pi)e3, p2=n p3, p0=n^2 p3, p1=Pi e0, the column matrix
P0=(p0,p1,p2,p3) is invertible for positive q!=1. Direct exact identities
give

    P0^-1 M P0=exp(N),
    P0^-1 Lambda P0=q^D(I+beta P), beta=6/(q-q^-1).

Here P0 is a basis change, not the symbol P=E03. The nilpotent chain
is nonzero and p1 has the distinct eigenvalue, explaining invertibility.
The construction has a singular coordinate limit at q=1; it is not
used to infer uniform convergence of the cusp fields to F08.

Take the positive metric g=z^-2(dx^2+L^2 dy^2+dz^2), x,y of unit
period and L>0. With k=log(q) and f^2=z^2/4-beta^2/L^2>0, define
Cx=-N/f, Cy=-k D-beta P/f^2, Cz=f'H/f. Every matrix is traceless.
They are single-valued in a positive orthonormal coefficient frame.
They are a real gauge transform, by diag(f,1,1,f^-1), of the flat
constant connection -N dx-(k D+beta P)dy. Thus their parallel
holonomies are exactly conjugate to the preceding cusp pair.

Direct commutators give [N,N^T]=[P,P^T]=H and [D,N]=[D,P]=0.
Consequently the full moment matrix reduces to

    z^2 H {2[(log f)''-(log f)'/z]+1/f^2+beta^2/(L^2 f^4)}.

The stated f makes this identically zero. Flatness is checked without
dropping noncentral equations. Hence A=(C-C^T)/2 and Psi=(C+C^T)/2
solve the complete adopted classical gauge equations on this cusp tail;
embedding in SU4-in-E8 preserves those equations. No scalar source is
inserted. This gives zero residual-square bulk potential there.

The positive defining-four norm per dx dy dz is

    L/(z f^2)+12 k^2/(L z)+beta^2/(2 L z f^4)+2L[(log f)']^2/z.

The second term diverges as log z for k!=0; all other terms are
O(z^-3) or smaller. For the figure-eight rectangular marking one may
choose L=2 sqrt(3), with orientation reversed if necessary. The lower
end z=2|beta|/L is not part of the construction: choose a strictly
larger cutoff and attach no core by assumption. A local solution is
not a complete global parent vacuum or a quantum boundary prescription.

## 4. The norm cost is not removed by another smooth Hermitian metric

Let a primitive cusp loop gamma have holonomy eigenvalue lambda.
For ANY smooth positive h, D=A+Psi and a D-parallel eigenvector obey

    d log ||v||h /dx = -<Psi_x v,v>h/||v||h^2.

Because v(1)=lambda v(0), Cauchy-Schwarz gives
integral_0^1 ||Psi_x||F^2 dx >= |log |lambda||^2. For h0 with
matrix [[a,b],[b,c]] in unit-period torus coordinates (x=gamma),
evaluation bounds |Psi_tan|h0^2 >= ||Psi_x||F^2/a. Slice area cancels
the e^(2r) angular norm in g=dr^2+e^(-2r)h0. Therefore every unit-r
slab has energy at least sqrt(ac-b^2)|log |lambda||^2/a.
No asymptotic bound on h or harmonicity is needed. The eigenvector can
be chosen separately on each loop; no continuous eigenbasis assumption.

Here lambda=q^-3 and x can be chosen as the longitude, so the bound is
strictly positive for q!=1. Every smooth positive metric on this flat
cusp has infinite integral |Psi|^2. This concerns that norm, not the
residual action: section 3 exhibits zero residuals. It also does not
decide normalizable fluctuations or global existence with fixed end data.
The rank-one diagonal control independently demonstrates the distinction.

## 5. Ordinary cohomology has a separate constraint

For q>0,q!=1, Lambda-I is invertible, since none of its four eigenvalues
is one. Write X=M-I, Y=Lambda-I. The torus complex has

    d0=(X,Y)^T, d1=(-Y,X),
    h1=(0,Y^-1), h2=(-Y^-1,0)^T.

Commutativity gives h1 d0=I, d0 h1+h2 d1=I, d1 h2=I: the WHOLE
torus local system is acyclic. The same holds on all finite-cover ends
because their peripheral group contains Lambda^d with no eigenvalue one.

For a connected oriented compact three-core with these torus boundaries,
the long exact sequence identifies ordinary and whole-boundary-relative
cohomology. Boundary duality also gives acyclicity for E*. Interior
invariants vanish by the longitude, H3 vanishes by relative duality,
and chi(core;E)=rank(E)chi(core)=0. Poincare-Lefschetz therefore gives

    dim H1(core;E)=dim H2(core;E)=dim H1(core;E*).

This is a dimension identity, NOT an exhibited bundle pairing and NOT
a claim that either dimension is zero. It is also not an identification
with the physical L2 spectrum or with relative data on selected discs.
One off-unit eigenvalue alone is insufficient for acyclicity; a trivial
direct summand is an explicit countercontrol. No old over-wide torus
chirality closure is reinstated.

## Consequence

There is an actual global holonomy curve escaping F08/F09's flat
pairings, with an exact compatible local cusp solution. The same curve
changes the physical end data, cannot retain finite Higgs norm in the
fixed hyperbolic metric, and has zero ordinary dual-sector H1 difference.
An allowed infinite-norm fixed-end background must still be globally
constructed and tested with the true action, fluctuations and anomaly;
projective Busemann volume alone does not supply those duties. This is
not a physical chiral theory, an object-selected deformation or gravity.
