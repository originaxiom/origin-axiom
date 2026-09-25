# R44: canonical type-one cusp and its defining-bundle complex

2026-09-25. Authored proof, frozen before finite controls; not an
independently accepted theorem. No finite test proves sections 2--6.
Predecessors: [R42](AFFINE_BACKGROUND_PROOF.md),
[R43 reception](PROJECTIVE_MODE_RECEPTION.md). Literal code and controls
are in canonical_cusp.py and the dedicated test file.

## 1. Literal peripheral algebra

Use R42's actual SL4 matrices M,N and word
Lambda=N M^-1 N^-1 M^2 N^-1 M^-1 N. Set

    n=log M=(M-I)-(M-I)^2/2, a=q^-3-q,
    Pi=((Lambda-q I)/a)^2,
    p3=(I-Pi)e3, p2=n p3, p0=n^2 p3, p1=Pi e0.

For q>0, q!=1 the ordered matrix P0=(p0,p1,p2,p3) is invertible and

    P0^-1 M P0=exp N0, N0=E02+E23, P=E03,
    P0^-1 Lambda P0=q^D(I+beta P),
    D=diag(1,-3,1,1), beta=6/(q-q^-1).

These are F10's received algebra, checked again against the literal R42
input, not original discovery. All displayed matrices commute where
needed: [N0,D]=[N0,P]=[D,P]=0. N0^2=P and P^2=0.
Write k=log q and c=beta/(4k)>0. In the affine fourth-coordinate chart,
the projective actions are

    M:      (x0,z,y) -> (x0+y+1/2,z,y+1),
    Lambda: (x0,z,y) -> (x0+beta, exp(-4k)z,y).

Thus r=x0+c log z-y^2/2 is invariant. The full commuting real flow is

    g(x,t)=exp(x N0) exp(t(kD+beta P)),
    g(x,t).(R,1,0)=(R+x^2/2+beta t,exp(-4kt),x).

Its SL4 determinant is one. The complex scalar character does not
change this real projective developing domain.

## 2. Sandwich for any invariant proper convex domain

Ballas--Long Theorem 3.3 supplies discrete faithfulness and an invariant
proper convex domain Omega for every q>0. We use that published theorem
as an input; we do NOT silently upgrade its definition to finite volume.
R42's unipotent-generator argument fixes the actual cone-preserving lift.

Here is a direct argument for the required all-q end control. In the
peripheral basis, M^j=I+jN0+j^2 P/2. Its leading limit on an interior
cone vector is the ray e0; the corresponding dual-cone limit is e3*.
Choose an interior vector/functional with nonzero leading coefficient.
Both limits lie in the respective closed cones. Their pairing is zero,
so e0 is a boundary ray and H={v3=0} is supporting. Orient the cone so
v3>0 and e0 is its positive boundary ray. Consequently Omega lies in
the v3=1 affine chart and is closed under positive vertical translation.
An entire vertical line would contradict proper convexity.
The initial constant basis P0 can be volume-normalized once for each
q; its nonunit determinant contributes only a constant to coefficient
norm comparisons. Every R-dependent rescaling below has determinant one.

Omega cannot contain a point with z=0: its Lambda iterates would
contain an entire affine vertical line by convexity, since beta!=0.
Connectedness gives a fixed sign for z; flip the second coordinate if
necessary, a constant change commuting with both peripheral matrices.
The projection U of Omega onto (z,y) is an open convex invariant set
in {z>0}. The projected orbit of any point contains the rectangular
grid (exp(-4km)z,y+n). Its convex hull is the whole half-plane z>0.
Hence U is that half-plane. Every vertical fiber is a nonempty upward
ray with finite endpoint. Its endpoint is a continuous convex function
f(z,y); Omega is its strict epigraph.

The function g0(z,y)=y^2/2-c log z has exactly the same affine
equivariance as f under M and Lambda. Therefore f-g0 is periodic on
the compact (log z,y) torus and is bounded. For constants b_-<b_+,

    B_(b_+) subset Omega subset B_(b_-),
    B_b={z>0, x0+c log z-y^2/2>b}.

This argument uses the actual group, not invariance of Omega under the
entire continuous flow. The constants can depend on q and Omega; no
uniform q->1 assertion is made. It extends the mechanism in Ballas
Lemma 6.2 by supplying its graph and projected-base hypotheses directly.

## 3. Embedded end and compact complement

For clarity these are separate steps, not consequences of a picture of
the domain. The properly convex Margulis lemma gives a dimension-three
constant mu. Hilbert displacement of M in a fixed model B_b tends to
zero uniformly on deeper horospheres: the continuous model flow commutes
with M and acts transitively on each horosphere; at (R,1,0), the
rescaling of section 4 sends M to I+O(R^-1/2). Hilbert distance is
continuous on pointed proper convex domains. Domain monotonicity bounds
the Omega displacement by the B_b displacement.

Choose d so deep that this displacement is <mu throughout B_d. If
gamma B_d intersects B_d, at an intersection point both M and
gamma M gamma^-1 have displacement <mu. They generate a virtually
nilpotent subgroup. Via the faithful marking by the original
finite-volume hyperbolic knot group, any such subgroup containing the
nontrivial meridian parabolic fixes its cusp point. Thus gamma preserves
that point and belongs to its maximal peripheral subgroup Delta.
This uses the original group's parabolic stabilizer, not a claim that
all projective parabolics share a point. It is the group-theoretic step
in Ballas Lemma 6.3; the subgroup need not have rank two (it may be
cyclic). Hence B_d/Delta embeds in Omega/Gamma.

This embedding is proper: its torus cross-sections are compact, and
as R->infinity the nontrivial meridian displacement tends to zero.
Injectivity radius has a positive lower bound on a compact subset of a
free properly discontinuous Hilbert quotient. The deep end therefore
cannot accumulate in a compact subset. A slightly closed truncation
gives an embedded end T^2 times [0,infinity).

Write X for its complement, including the boundary torus T. X is
connected and deformation retracts the whole quotient. The quotient
has contractible universal cover Omega, so it is aspherical; it is
orientable because the cone lift has determinant one. It is irreducible
(a smooth sphere lifts to a sphere in the convex open three-ball and
bounds a ball; distinct deck translates of that ball cannot be nested,
since iteration would contradict proper discontinuity in a compact
ball, so the ball projects embedded). Removing the proper end preserves irreducibility: a
bounding ball cannot contain the entire noncompact proper end. T is
incompressible and pi1 X is the figure-eight knot group Gamma.

Apply the relative compact-core theorem to X with its compact boundary
T included. The precise input is McCullough's relative version of
Scott's theorem: a prescribed compact subsurface of the boundary can
be included as the intersection of a compact core with that boundary.
Its statement is used explicitly in Harris--Scott (1996), p.149.
The original McCullough paper's proof has NOT been personally checked
here; the cited theorem is an external input, not a new in-repo proof.

The relative core may be chosen irreducible while retaining T. One way
to see the relevant reduction is the compact-core chunk decomposition:
compress and split a core along disks and spheres, retaining the unique
nontrivial chunk for the freely indecomposable, noncyclic group Gamma;
T cannot be lost into a simply connected piece because it is pi1-
injective. Cap spherical boundary components by the balls they bound
in X. These balls cannot contain the nontrivial core or T. This is the
usual irreducible-core reduction (Harris--Scott section 1). Let K be
the resulting compact aspherical relative core. Inclusion gives
pi1 K=Gamma, hence H2(K;R)=H2(Gamma;R)=0, the latter from the original
aspherical knot exterior. The oriented pair exact sequence contains

    H3(K,partial K;R)=R -> H2(partial K;R) -> H2(K;R)=0.

Consequently partial K has exactly one component. It already contains
T as a whole component, so partial K=T. There is no interior boundary
separating K from the rest of X; since X is connected, X=K is compact.
No tameness theorem for an arbitrary projective quotient is assumed.
No diffeomorphism with the original marked knot exterior is needed for
the cohomology statement: both are K(Gamma,1), with the actual same
peripheral subgroup. A smooth marked-homeomorphism assertion would
require its own topological identification and is not made here.

## 4. Actual canonical metrics, not just Hilbert lengths

At p_R=(R,1,0), R>0, use the determinant-one linear map

    S_R=diag(R^(-5/8),R^(3/8),R^(-1/8),R^(3/8)).

Projectively it sends (x0,z,y) to (x0/R,z,y/sqrt R), and p_R to p=(1,1,0).
The image of B_b satisfies

    z>0, X0-Y^2/2+(c/R) log z>b/R.

Its pointed projective limit is the proper domain

    Omega_inf={z>0, X0-Y^2/2>0},

the projectivization of a positive ray times the three-dimensional
Lorentz cone. This is projective Hausdorff convergence, not merely
pointwise convergence inside a chart. In homogeneous coordinates the
inequality is

    X0 v3-Y^2/2+(c/R)v3^2 log(z/v3)>(b/R)v3^2.

On a normalized bounded homogeneous slice, the positive part of
v3^2 log(z/v3) is bounded, including at v3=0. Thus any limit point has
z>=0, v3>=0, X0 v3-Y^2/2>=0. The sheet is also fixed: dividing by
v3>0 and using v3 log(z/v3)<=z/e gives
X0 >= -c z/(e R)+(b/R)v3, so X0>=0 in the limit, even at v3=0.
Conversely every interior point of this
product cone eventually satisfies the inequality; its interior is
dense in its closure. This proves convergence of the closed projective
domains. The sandwich gives the SAME limit for S_R Omega.

More generally S_R g(x,t)^-1 Omega obeys the same sandwich because
the continuous flow preserves every B_b. This proves uniformity for
(x,t) in a compact period rectangle, without assuming g-invariance of
Omega. Move all these pointed domains by one fixed projective map
to a bounded affine chart containing the limit closure. Benoist--Hulin
Corollary 3.3 applies to every finite jet of the normalized Cheng--Yau
solution there. Therefore both the base metric and the positive
ambient coefficient metric H=1 direct-sum h in the affine-sphere
splitting converge to positive limits at p. The normalization of S_R
matters: an unnormalized GL rescaling would alter the ambient metric.

An explicit positive control for this limit is

    u=-A z^(1/4)(X0-Y^2/2)^(3/8), A^8=2048/27,
    h_inf=-u^-1 Hess u,
    h_inf(p)=[[15/64,-3/32,0],[-3/32,3/16,0],[0,0,3/8]]

in coordinate order (X0,z,Y). It solves det Hess u=(-1/u)^5, is
negative and convex, and its radial graph is the complete product-cone
affine sphere. The formula is checked symbolically, but the actual
domain comparison is the argument above plus the external jet theorem.
For uniqueness here, transform to a bounded affine section of the
product cone: the degree-one homogenization -u*v3 is a constant times
z^(1/4)(X0*v3-Y^2/2)^(3/8), hence tends to zero on every boundary face.
It is therefore the Cheng--Yau Dirichlet solution, not merely a local
solution of its equation in the unbounded chart.

In the moving SL4 frame F=g(x,t) S_R^-1 the actual coefficient norm is
uniformly equivalent to a fixed Euclidean norm. Pulled-back coordinate
vectors at p have sizes/directions

    partial_R -> (1/R,0,0),
    partial_x -> (0,0,1/sqrt R),
    partial_t -> (beta/R,-4k,0).

Consequently on a sufficiently deep end, with q fixed !=1,

    h_B asymp dR^2/R^2 + dx^2/R + dt^2,
    dvol_h_B asymp R^(-3/2) dR dx dt.

Here asymp is two-sided quadratic-form comparison, including cross
terms. It extends to every exterior degree and to dual coefficients.
The radial distance is infinite and the end volume finite. With the
compact complement of section 3, the whole Blaschke volume is finite;
Benoist--Hulin also gives finite Hilbert volume. R42 then supplies a
complete, positive, finite-Higgs-energy harmonic-flat background for
this actual defining coefficient. Twisting by a unitary scalar line
and dualizing preserve that assertion. It is NOT the old base metric.

## 5. Full-complex bounded homotopy and its domain

In F, the flat connection has matrices

    Bx=N0/sqrt R, Bt=kD+beta P/R,
    BR=J/R, J=diag(5,-3,1,-3)/8.

All curvature components vanish, including partial_R Bt+[BR,Bt]=0
and partial_R Bx+[BR,Bx]=0. A unitary line adds imaginary scalar
constants to Bx and Bt (or, equivalently, Fourier phases). Define

    T=partial_t+Bt, K=i_(partial_t) T^-1.

At frequency omega in the appropriate real shifted Fourier lattice,
A=i omega I+kD is invertible and

    T^-1=A^-1-(beta/R) A^-1 P A^-1,
    norm(T^-1)<=1/abs(k)+abs(beta)/(R abs(k)^2).

This is a uniform bound in the comparison norm. The actual metric
depends on (x,t), but its uniform equivalence to the comparison norms
on the period rectangle makes the Fourier multiplier bounded on the
actual L2 spaces in every degree. The vector partial_t has bounded
length, so K is bounded. For the dual use -B^T; the same bounds hold.

Flatness gives [d_B,T]=0 and the covariant Cartan formula
{d_B,i_(partial_t)}=T. Hence d_B K+K d_B=I on the WHOLE end complex.
The radial identity, not a tangential-only calculation, is essential.
K preserves radial support. Smooth compactly radially supported forms
are a core for the needed local arguments. On maximal distributional
domains the identity extends by approximation; if d_B alpha is L2,
d_B K alpha=alpha-K d_B alpha is L2 as well.

For a smooth form supported in the deep end, pairing the identity
with itself gives

    norm(alpha)<=C (norm(d_B alpha)+norm(d_B^* alpha)).

The complete smooth base admits exhausting cutoffs with vanishing
gradient bounds. The Leibniz commutator of d_B and its adjoint uses
only this gradient, not bounds on the zero-order coefficients. The
usual cutoff/Friedrichs argument therefore identifies the complete
minimal and maximal complex and the self-adjoint Hodge--Dirac domain;
no artificial boundary condition is imposed at infinity. Local elliptic
compactness plus the displayed exterior estimate gives finite kernel
and a gap above zero, hence closed ranges. For example a normalized
approximate zero sequence orthogonal to the kernel has a locally
convergent subsequence; applying the exterior estimate to a fixed
cutoff of differences makes it globally Cauchy. Its limit would be a
nonzero kernel vector orthogonal to the kernel, a contradiction.

This bound is NOT decaying: norm(partial_t) tends to sqrt(3)*abs(k).
On the constant longitudinal Fourier mode, a nonzero semisimple
eigenvector and a dt factor give a nonzero limiting K norm. Thus F11's
decaying-homotopy compact-resolvent argument cannot simply be copied.
We neither assert compact resolvent nor determine the essential
spectrum here. A positive continuous spectrum is compatible with the
finite-dimensional zero-mode claim.

## 6. Cohomology comparison and received exceptional counts

If d_B alpha=0 and alpha is L2, subtract d_B(chi K alpha), with chi=1
far out, to obtain a compactly supported representative. This primitive
is in the complete graph domain by boundedness and the product rule.
Conversely if a compact closed alpha=d_B eta in L2, eta is closed on
the tail. Subtract d_B(chi K eta) to make the primitive compactly
supported. In degree zero the closed tail primitive is already zero,
by the same contraction identity. Compactly supported distributional
de Rham and smooth cohomology agree by local regularization. Thus

    H_L2^j(N_q;E)=H_c^j(N_q;E).

On the peripheral torus Lambda-I is invertible for q!=1, also after
unitary twisting and on the dual: all longitude eigenvalue moduli are
q or q^-3, never 1. The torus Koszul complex is acyclic. The compact
pair exact sequence therefore identifies H_c^j with ordinary H^j.
Since N_q is K(Gamma,1), this is exactly the representation cohomology
received in R43, not a new rank computation. Finite covers have the
same end estimates and positive powers of the off-unit longitude;
their counts must be computed for their own group, not copied from N_q.

For the four F11 meridian twists, the conditional-on-cited-inputs
authored conclusion is one defining-sector and one dual-sector
harmonic H1 mode at q=17+/-12 sqrt(2) for chi=-1, and at
q=7+/-4 sqrt(3) for chi=+i or -i. Generic q!=1 has no H1 for these
four twists. q=1 is deliberately outside the inverse argument.
These put the received paired classes on R42's SAME finite-energy
background; they are not selected 4D chiral particles or net chirality.
The choice of q, scalar twist, parent field/action, symmetry breaking,
interactions, neutral/whole-parent spectrum and gravity remain separate
physical duties. R40's nonsplit coefficient is a different model.

## Sources and exact reception limits

- Ballas--Long (2015), AGT 15, 3009--3022, Theorem 3.3 and appendix:
  https://msp.org/agt/2015/15-5/agt-v15-n5-p16-s.pdf . Full text read at R43.
- Ballas, 2014 author version, sections 2.2, 5, 6 (full paper read R42):
  https://web.math.ucsb.edu/~sballas/research/documents/propconvfig8.pdf .
  Its small-parameter volume theorem is not itself an all-q theorem.
- Benoist--Hulin (2013), sections 2--3, especially Corollary 3.3 and
  Proposition 3.4: https://msp.org/gt/2013/17-1/gt-v17-n1-p16-s.pdf .
  Full text read R42. These particular estimates apply in general dimension.
- Cooper--Long--Tillmann (2018), GT 22, 1349--1404:
  https://msp.org/gt/2018/22-3/gt-v22-n3-p02-s.pdf . Selected introduction,
  definitions 6.1--6.6, proofs 6.28--6.30 and section 7 read; printed
  pp.1393--1394 visually checked. Theorem 6.29 is an OPENNESS theorem,
  not an independently sufficient all-parameter finite-volume argument.
- Harris--Scott (1996), PJM 172, 139--150:
  https://msp.org/pjm/1996/172-1/pjm-v172-n1-p07-s.pdf . Whole article
  read; p.149 visually checked. Relative core statement there credits
  McCullough (1986), QJM 37, 299--307, DOI 10.1093/qmath/37.3.299.
  Original McCullough full text was not accessible; its proof is not
  claimed personally reconstructed. The sphere/core reductions and the
  global application in section 3 remain authored, not externally reviewed.

Source citations and finite controls are different evidence grades.
