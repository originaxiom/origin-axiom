# R42 authored bridge, with external analytic hypotheses explicit

This is a proof for a specified mathematical background, not an
independent theorem certification or a physical identification.
The source/version/reading scopes are in AFFINE_BACKGROUND_PRIOR.md
and AFFINE_BACKGROUND_INPUTS.json. Dimension n below is arbitrary;
the finite matrix controls specialize to n=3.

## 1. What geometry supplies

Let M=Omega/Gamma be an oriented properly convex real projective
n-manifold. The Cheng-Yau affine sphere in the cone over Omega is
unique after fixing affine mean curvature -1. It is asymptotic to
the cone boundary and has complete positive Blaschke metric h.
Use its cone-preserving volume-normalized lift of holonomy in
SL(n+1,R). Its equivariant immersion f identifies the flat bundle
with R direct-sum TM by (s,Y) -> s f + df(Y). No global trivialization
of TM or preferred coordinate system is assumed.

These statements are the general-dimensional content of Loftin's
2001 construction and Benoist-Hulin sections 2--3. In particular,
Benoist-Hulin Corollary 3.5 is still all-dimensional; the subsequent
restriction to surfaces must not be imported backwards or forwards
without checking it. Surface holomorphic cubic differentials are
not premises of the argument below.

Let nabla^B be the induced Blaschke connection and K=nabla^B-nabla^h.
With curvature R(X,Y)=[nabla_X,nabla_Y]-nabla_[X,Y] and affine normal
f, the ambient flat derivative is

    D_X(s,Y) = (Xs+h(X,Y), nabla^h_X Y+K_X Y+sX).

The positive coefficient metric is

    H((s,Y),(t,Z)) = st+h(Y,Z).

The Blaschke volume normalization identifies the volume of the frame
(f,df(e1),...,df(en)) with the h volume of (e1,...,en). Thus an oriented
h-orthonormal frame gives determinant-one H in the flat volume. In a
general coordinate frame H need not have numerical determinant one;
the comparison is against that frame's flat volume, not a coordinate
shortcut. Complexification gives a positive Hermitian determinant-one
metric and A takes values in su(n+1), with a real so(n+1) reduction.

## 2. Full equations, not a scalar projection

In the preceding orthogonal splitting, the metric/skew and symmetric
pieces of D are

    A_X = diag(d,nabla^h_X),
    Psi_X = [[0,X^flat],[X,K_X]].

Affine-sphere structure equations imply that

    C(X,Y,Z)=h(K_X Y,Z)

is totally symmetric and trace-free, nabla^h C is totally symmetric,
and

    R^h(X,Y)+[K_X,K_Y] = -(X tensor Y^flat-Y tensor X^flat).

The tensor convention C=nabla^B h instead gives -2 times this C;
Loftin's 2001 difference-tensor convention also has the opposite
sign. These are fixed here, not combined by their shared name.

Symmetry makes Psi self-adjoint; apolarity makes tr Psi=0. Flatness
of D splits into its skew and symmetric parts:

    F_A+Psi wedge Psi=0,   d_A Psi=0.

There is also a direct check: the tangent block is precisely the
displayed Gauss equation, the off-blocks vanish by the symmetry of C,
and the exterior derivative uses Codazzi. For the missing moment
equation take an h-normal frame at a point. The identity inclusions
in the two off-blocks are parallel. The tangent divergence is

    sum_i (nabla_i C)_(i j k)
       = sum_i (nabla_j C)_(i i k) = 0,

by complete symmetry and differentiated apolarity. Consequently
d_A^* Psi=0, with its full endomorphism-valued content retained.

This is the affine-sphere harmonic metric. It is not a newly discovered
harmonicity theorem: Rungi, arXiv:2512.09569v2, Theorem 4.11 and
Corollary 4.12, give the all-dimensional harmonic Blaschke lift.
The direct block proof here fixes conventions and avoids depending
on a surface-only argument or on a homogeneous-space decomposition.

For n=3, complexification and an invariant embedding of this SU4
connection into the adopted compact gauge algebra preserve these
local equations. This is a gauge-background statement only. It does
not derive the physical embedding, full fluctuation content or action.

## 3. A global finite-energy consequence

Using the positive defining-representation trace norm,

    tr(Psi_X Psi_Y) = 2h(X,Y)+tr(K_X K_Y),
    |Psi|^2_h,H = 2n+|C|^2_h.

There is a dimension-dependent finite bound B_n for |C|^2 on ALL
pointed properly convex domains with their normalized affine-sphere
metrics. Here is the precise external-to-authored chain. Benzećri
compactness, stated as Benoist-Hulin Theorem 2.7, gives a compact set
of representatives of pointed domains modulo projective maps. Their
Corollary 3.3 gives continuity of every finite jet of the Cheng-Yau
solution on these pointed domains. The affine metric and difference
tensor are constructed from the derivatives through order three;
their invariant norm is continuous, since the metric is positive.
It is projectively invariant, so compactness bounds it by B_n.
No sharp numerical value of B_n or original Calabi estimate is used.

Benoist-Hulin Proposition 2.6 (equivalently the uniform comparison
in Proposition 3.4) identifies finite Hilbert/Busemann volume with
finite Blaschke volume in every dimension. Therefore

    integral_M |Psi|^2 dvol_h <= (2n+B_n) Vol_h(M) < infinity.

Completeness and equivariance were not supplied by the finite tensor
test: they enter through the cited general-dimensional existence and
comparison results. The same proof applies on every finite cover,
with the pulled-back geometric data and finite covering volume.

The gauge equations have zero residual-square static potential on
this background. The positive integral above is a DIFFERENT
functional. Neither is silently identified with a derived physical
gravitational or quantum action.

## 4. Applying it to the actual linear projective family

Take Ballas' literal meridian generators M,N at t=q/2>0, frozen in
affine_background.py. Both are unipotent of determinant one. The
word Lambda=N M^-1 N^-1 M^2 N^-1 M^-1 N is computed, never copied
from a projectively rescaled displayed longitude. The exact checks
are

    M W=W N,  W=N M^-1 N^-1 M,
    [M,Lambda]=0,
    char_Lambda(X)=(X-q)^3 (X-q^-3),
    tr Lambda-tr Lambda^-1 = -(q-q^-1)^3.

Ballas establishes nearby finite-volume properly convex structures
around q=1. The rational representation identities hold more widely;
this is NOT evidence that every positive q has that geometric model.

The actual given SL4 lift, not a different central character, preserves
the proper cone. To see this, any generator U preserving Omega
projectively takes the chosen cone C either to C or to -C. If a
unipotent U exchanged the cones, for v in C and a linear functional
ell strictly positive on C, ell(U^m v) would alternate sign for every
nonnegative integer m. But U=I+N0 with nilpotent N0 makes U^m a
finite polynomial in m. A nonzero real polynomial has an eventually
constant sign. This contradiction fixes the cone-preserving lift for
each generator, hence for the representation. Orientation fixes its
positive volume. No unearned projective-to-linear identification is
left in this step.

Thus this same actual real four, and its complexification, admit the
complete finite-energy background on h_q wherever the proper convex
finite-volume structure is established. This is not the holomorphic
Sym3 representation or the R40 nonsplit coefficient. At q=1 it is
the balanced geometric coefficient already identified in F10/F08.

For q!=1 the trace mismatch also forbids an invertible flat linear
map E->E* on the same base. An invertible flat antilinear map is
forbidden by the same argument because the matrices are real.
A finite-cover peripheral subgroup contains a positive power
Lambda^d up to conjugation, whose trace mismatch is
-(q^d-q^-d)^3, still nonzero. Projective duality can change the
projective structure/representation and is not such a flat self-map.
None of this proves chirality or denies base-changing symmetries.

## 5. What changes, what remains true

Incoming F10 proves that these off-unit peripheral eigenvalues force
infinite positive Psi norm on the FIXED complete hyperbolic base
g0, for every positive coefficient metric. R42 uses h_q instead.
There is no contradiction and no coefficient-only repair of F10.
Indeed h_q cannot be globally uniformly equivalent to g0 for q!=1:
uniform equivalence of base metrics would make one-form norms and
volume densities comparable, giving finite g0 energy for this H,
contrary to that holonomy bound. The end change is essential.

The boundary acyclicity and ordinary dual-sector H1 equality in F10
depend on holonomy and topology, not on the choice of base metric,
so they remain true. Identifying ordinary cohomology with physical
L2 modes on h_q needs its OWN complete operator and domain argument.
The newer fixed-g0 F11 design cannot be reused as that argument.

The Ricci contraction gives one further exact internal identity:

    Ric_h = -(n-1)h+tr(K_X K_Y)
          = tr(Psi_X Psi_Y)-(n+1)h.

This is the internal Riemannian affine-sphere curvature relation,
not the four-dimensional Lorentzian Einstein equation or a measured
cosmological constant. No physical normalization is inferred from it.

R42 therefore advances the positive-domain/background gate for a
specified DIFFERENT metric model. Selection of q and of the base
dynamics, all-form normalizable modes, chirality, interactions and
physical anomaly remain separate obligations. The nonsplit R40/R41
source and boundary route is neither replaced nor killed.
