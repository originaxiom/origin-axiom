# F13 authored analytic argument

Frozen before execution. Exact finite tests check the algebraic inputs;
they do not independently certify the global analytic proof. The base,
parent theory, exceptional q and central character remain supplied.

## 1. Uniqueness in the earned asymptotic class

Fix F12's irreducible flat SL4 bundle over the connected complete
finite-volume hyperbolic base. Let h0,h1 be two smooth determinant-one
harmonic metrics, each at bounded target distance from the same F10
cusp reference. Their distance is globally bounded, since the core is
compact. In X=SL4(C)/SU4, put w=d_X(h0,h1)^2. Squared distance is
smooth on a Hadamard manifold and its harmonic-map composition satisfies
Delta w>=0. This scalar descends despite the maps' equivariance.

Complete cutoffs chi_R, |dchi_R|<=C/R, and integration of the inequality
against chi_R^2 w give, by Cauchy--Schwarz,

    integral chi_R^2 |dw|^2
        <= 4 ||w||_infinity^2 integral |dchi_R|^2 -> 0.

The final limit uses finite BASE volume, not finite harmonic-map energy.
Thus w is constant. Interpolate by geodesics f_t between the two maps,
let V=partial_t f_t and J_i=df_t(e_i). The distance second variation,
with the endpoint tension fields zero, is

    (1/2) Delta w = sum_i integral_0^1
       (|nabla_t J_i|^2 - <R(J_i,V)V,J_i>) dt.

Nonpositive curvature makes each term nonnegative. Consequently the
variation is parallel and R(J_i,V)V vanishes. The standard symmetric-
space curvature formula identifies the latter zero with [Psi_i,s]=0,
where s=log(h0^-1 h1) is a trace-free h0-self-adjoint endomorphism.
Parallelness is d_A s=0. Hence d_C s=d_A s+[Psi,s]=0: s commutes with
the global holonomy. F12's full Mat4 algebra makes s scalar, and trace
zero makes s=0. Therefore h0=h1.

For the local second-variation statement compare Riestenberg--Smillie,
section 5.1, Proposition 43:
https://arxiv.org/html/2511.11469v3#S5.SS1
Their global theorem's coarse-stability assumptions are not invoked.
The finite-volume cutoff and the actual full-algebra certificate are
the additional arguments here. Constant distinct determinant-one
metrics for a trivial representation demonstrate why irreducibility
cannot be dropped. This does not classify all unbounded-distance end
conditions, and it does not assume irreducibility on every finite cover.

In particular F12's arbitrary smooth reference extension on the compact
core does not choose a different answer. All exhaustion subsequential
limits in this class agree. The choice of q, representation, twist,
base geometry and physical end prescription has NOT been removed.

## 2. The actual six, and the criterion for a massive mediator

Let E_chi be F11's defining four with its F12 metric, and W=exterior^2
E_chi, the (10,6) coefficient in the adopted E8 parent. Its generators
are exterior^2(chi M), exterior^2(chi N); its scalar character is chi^2.
Thus it is -1 at p14 and +1 at p34. Use the same relator and the actual
rank-six cocycle complex

    B: C^6 -> C^12, J: C^12 -> C^6, J B=0,
    dim H1 = 12-rank B-rank J.

The exact field tests decide these ranks at BOTH roots of each p.
A nonzero minor is checked in the field, not by numerical tolerance.
Ordinary H1, not an adjoint representation's deformation dimension, is
what this complex calculates.

On the reference cusp, write D6=L(D), P6=L(P) for the exterior LIE
functor. D6 has eigenvalues +2 and -2, each three times; [D6,P6]=0,
P6^2=0 and ||P6||=1 in the unit exterior basis. Therefore, with
u=z^2/4-beta^2/L^2, k=log q nonzero and S=i omega I-kD6,

    (partial_y+C6_y)^-1 = S^-1+(beta/u) S^-1 P6 S^-1,
    ||inverse|| <= 1/(2|k|)+|beta|/(4u k^2) = B6(z).

This holds for EVERY real Fourier frequency. Flatness includes
partial_z C6_y+[C6_z,C6_y]=0, so the full Cartan homotopy
K=iota_y(partial_y+C6_y)^-1 obeys d_C K+K d_C=I and
||K||_(z>Z)<=L B6(Z)/Z. F11's complete-domain proof now applies to
W, including the actual uniformly equivalent exterior metric of F12.
The longitude eigenvalues on W are q^2 and q^-2, each three times;
none equals one. Thus the full peripheral local system is acyclic and

    H_(2)^j(W) = H_c^j(W) = H^j(W),

with compact resolvent of Q_W and Delta_W in every degree. These are
proved by the exhibited homotopy, NOT by copying F09's pointwise gap.

If the field calculation gives H1(W)=0, compact resolvent and positivity
imply a smallest eigenvalue delta_W>0 on one-forms. Its numerical value
is not calculated. If it instead gives H1(W)>0, retain these massless
10s and invert only on the orthogonal complement; do not call the whole
sector massive. No positive constant uniform over q is asserted.

## 3. Derivation from the noncommuting parent action

Use the positive Hermitian matrix inner product and the real orthogonal
split C=A+Psi, A anti-Hermitian and Psi Hermitian. The adopted parent
action (Braun et al. (2.9)--(2.18), B.12--B.14) has internal potential

    V(C)=2/g7^2 (||F_C||_2^2+||mu(C)||_2^2),
    mu=delta_A Psi.

Here two-form norms include 1/2!, and their I=-2mu. This accounts for
both factors of two; their curvature term is not half of the moment
term in form notation. The four-dimensional internal-field kinetic
term is ||partial_mu C||_2^2/g7^2, before gauge-vector mixing.
https://arxiv.org/html/1812.06072v2#S2.SS2

For u=a+psi with the same real split, expand around F_C=mu=0:

    F(C+u)=d_C u+u wedge u,
    mu(C+u)=M(u)-sum_i[a_i,psi_i],
    M(u)=delta_A psi+sum_i[Psi_i,a_i].

The complex formal adjoint on adjoint-valued one-forms is

    d_C^dagger u=delta_A u+sum_i[Psi_i,u_i]=G(u)+M(u),
    G(u)=delta_A a+sum_i[Psi_i,psi_i].

G is anti-Hermitian, M Hermitian; hence
||d_C^dagger u||^2=||G||^2+||M||^2. With the real L2 inner product,
G is the adjoint of the infinitesimal compact-gauge map epsilon ->
d_C epsilon (epsilon anti-Hermitian). At a BPS background,
M(d_C epsilon)=[mu,epsilon]=0; the derivative terms cancel, rather
than being dropped. Adding the background gauge-fixing term
2||G||^2/g7^2 gives the quadratic potential

    V_gf,2(u)=2/g7^2 (||d_C u||^2+||d_C^dagger u||^2).       (1)

This is the ACTUAL scalar block of the gauge-fixed parent Hessian.
Its form operator is the coefficient Hodge Laplacian, not a holonomy
eigenvalue relabeled a mass. The second derivative of V has an extra
factor two relative to its quadratic Taylor coefficient. On a complex
normalized internal mode, the displayed kinetic/potential convention
gives a scalar-block mass-squared coefficient 2 lambda. Neither lambda
nor an absolute physical length scale has been numerically predicted.
Gauge-vector mixing, ghosts, full Ward identities and quantum loops
are not eliminated by specifying (1); this is not a full propagator
or a claim that gauge-fixing produces a new physical interaction.

For an acyclic W, the positive Euclidean inverse of this normalized
internal scalar block satisfies

    ||(p^2+2 Delta_W)^-1|| <= 1/(p^2+2 delta_W), p^2>=0.

This bound is conditional on the exact H1 test in section 2, not on an
arbitrary relative weight fitted to obtain a gap. The full parent real
field pairs complex coefficient sectors; the identity (1) is established
before restricting to such sectors, so no separate Hermitian structure
on a single charged summand is implicitly assumed.

## 4. A sufficient nonlinear fixed-end fluctuation space

For the fixed smooth F12 metric put

    X = {u in L2 : d_C u,d_C^dagger u in L2} intersect L4,
    ||u||_X=||u||_2+||d_Cu||_2+||d_C^dagger u||_2+||u||_4.

All derivatives are distributional. On one-forms the degree-zero and
degree-two outputs are orthogonal. F02 therefore supplies precisely
the unique complete Q graph domain for the linear part. No artificial
finite cusp boundary condition is installed. Positivity and its closed
form give the corresponding self-adjoint Hodge operator.

The finite-dimensional Lie bracket and exterior product have uniform
pointwise bounds in the compact-group invariant fiber metric, hence
||u wedge u||_2+||sum[a_i,psi_i]||_2<=C||u||_4^2. The nonlinear
residuals above are continuous polynomial maps X -> L2, and V is a
finite, nonnegative, continuously differentiable polynomial on X.
Complete cutoffs approximate in graph norm AND L4; local first-order
elliptic regularity, Sobolev embedding and mollification give smooth
compactly supported approximants in both norms. Thus Green identities
extend without a surviving end flux in this class. At u=0 the full
residual and its first variation vanish, without subtracting divergent
background Higgs energy or demanding ||Psi||_2<infinity.

This is an explicitly supplied sufficient fixed-end classical domain,
not proof that it is the unique/maximal physically allowed end law.
It excludes F11's nonnormalizable change of q. It makes no claim to
derive gravity, a boundary action, a UV cutoff or a path-integral measure.
It remains essential to show the modes of interest actually lie in X.

## 5. Decay of the earned charged harmonic modes

Take E, E* or W in the preceding end norm class. The bounded Cartan
homotopy gives, on forms supported above Z, q_C(v)=||Qv||^2>=cZ^2||v||^2
for large Z. The constants may depend on the fixed representation and
metric equivalence. A dyadic partition chi_j in z has sum chi_j^2=1,
uniformly bounded |dchi_j|, and z comparable to 2^j on each support.
The Clifford commutator [Q,chi]=epsilon(dchi)-iota(dchi) and cancellation
of sum chi_j dchi_j give the IMS identity

    sum_j q_C(chi_j v)=q_C(v)+integral sum_j |dchi_j|^2 |v|^2.

Applying the tail bound on each annulus yields
integral z^2 |v|^2 <= C(q_C(v)+||v||^2); increase the starting height
to absorb the last term. In particular for some A>0,

    integral z^2 |v|^2 <= A q_C(v)                         (2)

on a sufficiently high tail, first for compact support and then for
its closed graph domain. Uniform equivalence of metrics is enough;
no derivatives of that equivalence entered this homotopy argument.

Let alpha be an L2 harmonic coefficient form on the actual F12 solution.
Choose a cutoff chi supported in this high tail and one further up, and
f_R=chi exp(epsilon min(z,R)), with smoothed Lipschitz corners. For each
finite R this bounded multiplier with bounded derivative preserves the
complete graph domain. Q(f_R alpha)=c(df_R)alpha. Outside the fixed
transition region, |df_R|<=epsilon z f_R. Cauchy--Schwarz at the
transition gives from (2), uniformly in R,

    integral z^2 f_R^2 |alpha|^2
       <= 2A epsilon^2 integral z^2 f_R^2 |alpha|^2+C_chi.

Choose 2A epsilon^2<1. Monotone convergence (or a monotone nonsmoothed
Lipschitz truncation) then proves

    integral_tail z^2 exp(2 epsilon z)|alpha|^2 < infinity. (3)

Weighted L2 alone is not automatically L4 on a collapsing cusp. Here
the actual harmonic metric supplies the local coefficient estimates.
At height z_p take a lifted metric ball of radius r_p=b/z_p, with b
below the fixed cusp injectivity constant. On its doubled ball the
reference harmonic map varies a uniformly bounded target distance:
F10's explicit coefficients have norm O(z), and z differs from z_p by
O(1) there. F12 bounds the distance of h to that reference. After one
constant target isometry, both maps therefore take values in a fixed
compact target ball on each such lifted ball.

Rescale the domain by r_p^-1. Its metrics have uniformly controlled
geometry. For harmonic maps into this smooth NPC symmetric space,
the distance-to-a-point convexity inequality and a cutoff first give
a uniform rescaled energy bound from that bounded target image.
Bochner/mean-value estimates then give a gradient bound, and elliptic
bootstrapping gives all local coefficient bounds. In a parallel flat
frame normalized by the same constant target isometry, the induced
positive fiber metric and its rescaled derivatives are consequently
uniformly bounded. Thus the rescaled elliptic operator Q has uniform
interior estimates, giving for its harmonic sections

    sup_(B_(r_p/2)) |alpha|
        <= C r_p^(-3/2) ||alpha||_(L2(B_r_p))
        <= C' z_p^(3/2) exp(-epsilon z_p).              (4)

The final use of (3) is valid because z=z_p+O(1) throughout the ball;
we have weakened its extra factor z^-1, which is harmless. Compact
core regularity completes the global L-infinity bound. Consequently
alpha lies in Lp for every p>=2, in particular L4, and its graph
derivatives vanish. It belongs to X.

As a control, the scalar cusp function z^a has L2 integral proportional
to integral z^(2a-3) dz and L4 integral to integral z^(4a-3) dz. For
a=3/4 only the former converges. The harmonic confinement and local
regularity, not finite base volume alone, make the difference here.

## 6. What this earns for interactions, and what it does not

The actual 4--4--6 parent invariant is the volume contraction on SL4
combined with the one-form wedge and the Spin(10) tensor (F09/R38).
For normalized charged harmonic profiles alpha,beta the bilinear source
J=star(alpha wedge beta), with the indicated coefficient contraction,
obeys ||J||_2<=C||alpha||_4||beta||_4. The invariant is bounded in the
induced determinant-one metric. Thus its pairing with any L2 mediator
profile exists, and if section 2 yields delta_W>0 its scalar-block
quadratic response is finite:

    0 <= <J,(p^2+2 Delta_W)^-1 J>
       <= ||J||_2^2/(p^2+2 delta_W).

This shows a defined channel for the actual normalizable modes, not
that J is nonzero or that its dual response differs. F09's cofactor
nonvanishing proof used a different, parallel background and is not
transferred. A nonzero L2 mode can have zero self-wedge. An equality
or inequality between the whole dual response tensors still needs its
own computation, along with the parent gauge constraints if interpreted
as a physical effective interaction. No numerical Wilson coefficient,
mirror-selective phase, quantum gap or observed spectrum is derived.

The six's H0 vanishes from the invertible longitude minus identity;
the four and dual H0 vanish for the same reason. In the adjoint 15,
F12's irreducibility makes the flat commutant traceless part zero.
The commuting so(10) 45 has constant finite-norm zero-forms because
base volume is finite. In the adopted parent this earns exactly the
unbroken gauge ALGEBRA so(10), not a new global gauge-group quotient
or the Standard Model breaking. This is a different claim from the
mediator one-form census and does not depend on its outcome.
