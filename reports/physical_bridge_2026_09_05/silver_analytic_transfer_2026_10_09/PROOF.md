# Analytic transfer at the fixed silver cusp

Authored pre-execution argument, October 9, 2026. Exact finite controls are
specified in DESIGN.md; they do not replace independent analytic review.
The coefficient and physical-parent inputs remain those of the earlier
silver packets. This is a local analytic improvement to their formal
interaction model, not a completed real boundary theory.

## The unchanged coefficient and norm

Write D=d+A dx+B dy on the period-one torus in the earlier logarithmic
trivialization. A and B are the induced actions of the two commuting
nilpotent logarithms of the literal rank-five coefficient W. Include
24 trivial +10W+10Wdual+5Lambda2W+5Lambda2Wdual+End0W, dimension 248.

Use the earlier compatible positive coefficient metric. On End0W the
coordinate Gram is diag(I20,I4+ones4); on the other displayed blocks it
is Euclidean, up to harmless positive scalar factors. Keep this metric
separate from a physical harmonic bulk metric. The constant Hodge SDR
has Dh+hD=1-P, h²=hP=Ph=0 and the earlier cyclic trace identities.

For a real quadratic-field entry z=a+b sqrt2 put q(z)=|a|+2|b|.
Thus |z|<=q(z). The sum of q over matrix entries bounds its Euclidean
operator norm. Passing to the End0W metric costs at most sqrt5<3;
using the factor 3 on every block is a conservative common bound.
Repeated gauge multiplicities do not increase the maximum operator norm
on an orthogonal direct sum.

Let C0=3 max_blocks sum_entries q(h0). This is a rational upper bound
for the constant Fourier homotopy. It is not a spectral gap measurement.

## A bound for all nonzero Fourier modes

At frequency (m,n), put X=A+2pi i m I and Y=B+2pi i n I. If m!=0,
nilpotence of order N gives the exact identity

    X^-1 = sum_(j=0)^(N-1) (-A)^j / (2pi i m)^(j+1).

The analogous identity holds for Y. Choose a coordinate with absolute
frequency M=max(|m|,|n|)>0. Since 2pi>6,

    ||X^-1||_metric <= (3/M) sum_(j=0)^(N-1)
                       sum_entries q(A^j) / 6^(j+1),

or the same bound using B. Let C1 be the maximum of these rational
constants over both logs and all blocks. No finite frequency scan
establishes this estimate; the finite geometric identity does.

The algebraic contraction Q=coordinate contraction times X^-1 satisfies
DQ+QD=1. This proves acyclicity of each nonzero Fourier complex.
Its degree-one component is a left inverse for D0; its degree-two
component is a right inverse for D1. The Hodge h1 is the inverse on
im D0 followed by orthogonal projection, and h2 is the minimum-norm
right inverse of D1. Consequently ||h_k||<=||Q_k||<=C1/M.
No normality or unitary holonomy has been assumed.

On coefficient-valued forms use the weighted Fourier norm
sum_k (1+max(|k1|,|k2|))^s ||v_k||, with s>=0 and the finite-dimensional
metric on exterior-degree components. The weight is submultiplicative.
The E8 wedge bracket is a bounded bilinear operation, with some fixed
finite constant b>0 in this norm; it has not been replaced by an abelian
bracket or by the neutral sl5 bracket. Its finite-dimensional norm
depends on the supplied parent/normalization. This proof does not
compute b numerically or identify it with a physical coupling.

The full cyclic Hodge h is bounded by c=max(1,C0,C1); P has norm<=1
and selects constant harmonic modes. Also h gains one Fourier weight
with bound max(C0,2C1). D itself is unbounded on a fixed such space:
we do not apply a Banach DG Lie theorem by ignoring this derivative.
The nonlinear fixed-point map below uses h and the bracket, not D.

## Convergent Kuranishi lift and the curvature left over

For eta in harmonic degree one, define

    a = i eta - (1/2) h[a,a],       rho=c b.

If epsilon=||eta||<=1/(8rho), the map on the ball ||a||<=2epsilon
maps the ball into itself and has Lipschitz constant at most
2rho epsilon<=1/4. It has a unique solution in that ball, analytic
in eta. Its power-series norm is majorized by the solution

    u=epsilon+(rho/2)u²,
    u=sum_(r>=1) Catalan_(r-1) (rho/2)^(r-1) epsilon^r.

The majorant has radius 1/(2rho). The smaller ball is used for a
simple quantitative contraction and derivative bound, not optimality.
Uniqueness and translation invariance show a is constant in this
trivialization whenever eta is harmonic: the entire harmonic lift
already lies in the finite constant differential graded Lie algebra.

For a=a_x dx+a_y dy, [a,a]/2=[a_x,a_y] dx dy. Since the torus has
dimension two, D on degree two is identically zero. The SDR then gives

    h a=0,  P a=eta,
    F(a)=D a+(1/2)[a,a]=(1/2)P[a,a]=:kappa(eta).

There is no hidden degree-three remainder here. Thus the lift is
flat exactly on the analytic zero locus of kappa. The actual neutral
jet test uses a1=eta and, at r>=2,

    q_r=sum_(i+j=r) [a_i,x,a_j,y],
    a_r=-h2 q_r,  kappa_r=P2 q_r,
    D1 a_r+q_r=kappa_r.

The trivial gauge block provides an important opposite control:
eta=E12 dx+E21 dy has kappa=(E11-E22) dx dy!=0 and h=0.
Existence and convergence of its lift do not make this input flat.
Eta=E12 dx+E13 dy has zero curvature. Both retain the original bracket.

## Symplectic harmonic embedding

Let omega be the integrated invariant wedge pairing on degree-one
forms, with its inherited pairing on H1. Differentiate the fixed-point
equation: dPhi_eta(v)=i v + w_v with w_v in im h2. Cyclicity and
Ph=0 give omega(iH,im h)=0; cyclicity and h²=0 give
omega(im h,im h)=0. Therefore

    Phi* omega = omega_H

exactly, not only at a finite jet. The map is injective locally since
P Phi=identity. It is equivariant under the retained compact gauge k:
i, P, h and the bracket commute with this action, and uniqueness
carries the action through the fixed-point equation.

Each previously admitted k-stable harmonic Lagrangian plane L in H1
therefore lifts to an analytic isotropic submanifold Phi(L). The
component of kappa paired with k vanishes there. One direct proof uses
the gauge moment map: contraction of omega with [k,a] is the derivative
of <k,[a,a]/2>. Equivariance and the exact symplectic pullback identify
this function with <k,[eta,eta]/2> on H1, with zero constant at eta=0.
The latter is zero on k-stable isotropic L. This is only the k-component
of kappa, not all of kappa or all flatness equations.

Here dim H1=200 and dim L=100. Constant full boundary one-forms have
dimension 496, with Lagrangian dimension 248. Even before restoring
nonconstant modes, Phi(L) by itself is not a full boundary Lagrangian.
The missing directions cannot be called solved by changing this name.

## Analytic minimal interactions without a full canonical boundary claim

The earlier cyclic transfer uses bounded binary brackets, internal
edges h and harmonic leaves, so the same binary-tree majorant proves
local absolute convergence of its Taylor-normalized minimal brackets.
One may use a smaller radius than above if choosing a different tree
normalization. Factorial symmetrizations are cancelled by the Taylor
factorial; the remaining planar binary tree count is Catalan, at most
4^(r-1). Differentiation on a smaller ball preserves convergence.
The finite harmonic supercoordinates and their Grassmann expansions
thus define an analytic reduced BFV Hamiltonian.

The previous strict k-leaf proof is unchanged: hi=0, h²=0, Ph=0 and
k-equivariance kill each higher tree with one k input. Cyclicity rotates
a ghost k input to such a leaf. The cubic vanishes on
Ah=(k,L,ann(k)); the quadratic vanishes on cohomology. Consequently
the earlier formal statement S_min|Ah=0 holds as an actual local
analytic identity of this reduced model. Higher interactions away
from Ah are not deleted. The full roster H=(100,200,100) and
Ah=(24,100,76) is retained.

Related primary mathematics is Schuhmacher, Analytic decomposition of
differential graded Lie algebras, math/0607764, sections 3 and 4,
especially 4.8 through 4.10. Those results concern analytic DG/L-infinity
decompositions; they do not state that a chosen decomposition is cyclic
or symplectic. We use our bounds above and the earlier cyclic identities,
not a bare appeal to that theorem for the physical boundary.
Source: https://arxiv.org/html/math/0607764 (accessed October 9, 2026).

## What this advances and what it does not

The reduced nonlinear interactions and harmonic lift cease to be only
formal. This removes that particular convergence uncertainty while
preserving every older charged-cone/polarization choice. It does not
prove convergence of the full canonical transformation that adds the
acyclic boundary directions. Its analytic inverse, actual full
Lagrangian and boundary primitive still need construction or proof.

Reality, normal/D-term/source boundary variations, compatible bosonic
and fermionic domains, a stationary stable positive-kinetic background,
the complete interacting charged spectrum and quantum anomalies remain
duties of one and the same physical theory. Auxiliary norm radii and
supplied polarizations are not genesis-selected parameters. No three
physical generations, observer/qualia, normalized SM or gravity is
derived here. The parameter-free SM and TOE goal remains unachieved.
