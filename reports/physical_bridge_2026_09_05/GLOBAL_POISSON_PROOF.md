# R31 candidate: uniform wells for the compact normalized source family

Pre-execution analytic argument. Finite controls test identities and
comparators, not every geometry, a mesh solution of m202, or independent
proof review. This is a continuation of R29/R30, not a new source model
or a general chirality obstruction.

## 1. Quantifiers and the equation actually being solved

Fix a connected smooth compact domain Q with nonempty boundary in a
complete hyperbolic three-manifold, with curvature length one. Fix k
pairwise disjoint, neatly properly embedded geodesic arcs Gamma_j in Q,
with disjoint contractible regular neighborhoods. The arcs, truncation,
metric and neighborhoods do not vary with epsilon. Pick epsilon_0
below their fixed tubular and local injectivity radii. Let U_(j,epsilon)
be their metric epsilon-neighborhoods, clipped to Q. On any compact
interior portion these are the exact Fermi tubes r<epsilon; the endpoint
caps are included, not deleted. Set

    rho_epsilon = sum_j 2 beta_j/sinh(epsilon)^2 1_(U_(j,epsilon)),
    Delta F_epsilon = rho_epsilon,   F_epsilon|boundary Q = f,
    Delta = div grad,   beta_j>0,

where f is fixed smooth Dirichlet data. This is R29's uniform normalized
subfamily sigma=1/(pi sinh(epsilon)^2), beta_j=kappa q_source,j v_j^2/(4pi).
The source charge is not the fermion coupling q used below. Arbitrary
epsilon-dependent weights in R29's larger model are not covered.

At each epsilon>0 the usual coercive Dirichlet problem has a unique
weak solution, W^(2,p) for every finite p; F and dF are bounded at that
width. A sharp source indicator is not a smooth-density assertion.
The question here is a bound UNIFORM as epsilon tends to zero.

For an arc of length L, an upper bound for the neighborhood volume is

    pi L sinh(epsilon)^2 + 2 V_ball(epsilon),
    V_ball(epsilon)=pi(sinh(2 epsilon)-2 epsilon).

The cylindrical part and two endpoint balls overcount harmlessly.
Multiplying by the density gives 2pi beta L+O(beta epsilon), uniformly
for epsilon<epsilon_0. Thus ||rho_epsilon||_L1 is uniformly bounded.
Clipping to Q can only reduce this upper bound. The exact source per
unit interior axis length is 2pi beta. Endpoints carry no extra fixed
point charge. A bounded-L1 endpoint modification supported near the
endpoints would also leave the interior argument below intact.

## 2. The local kernel and a bounded global correction

Write P=-Delta. On H3 its positive fundamental solution is

    g(d)=(coth d-1)/(4pi)=1/[2pi(exp(2d)-1)].

Directly, g''+2 coth(d)g'=0 off the pole and
-4pi sinh(d)^2 g'=1. Its singularity is 1/(4pi d)+O(1), and its tail
decays as exp(-2d)/(2pi). These fix sign, delta normalization and the
decaying choice. Cohl--Kalnins, theorem 3.1 and section 3.2, supply the
same kernel; their section 4 distinguishes a normalized fundamental
solution from one plus an arbitrary harmonic function.[1]

Here is the needed compact-domain bound, without identifying the
quotient's Dirichlet Green function with g. Let D be a fixed smooth
compact domain and K a compact subset of its interior. For every y in K
choose the SAME sufficiently small radius a below the local injectivity
radius and distance to the boundary. A fixed radial smooth cutoff chi,
one near zero and supported in d<a, gives

    Gamma_y(x)=chi(d(x,y))g(d(x,y)),
    P Gamma_y = delta_y + e_y.

The error e_y lies on a fixed-radius annulus. Its L-infinity norm is
uniform in y: all derivatives of chi are fixed, and g and its derivatives
are bounded there. The radius is small enough that this annulus is
embedded and the hyperbolic radial formula applies. Let b solve
P b=1 with zero Dirichlet boundary data. It is nonnegative and bounded.
The Dirichlet solution of P w_y=-e_y obeys, by comparison with
plus/minus ||e_y||_infinity b,

    ||w_y||_infinity <= ||e_y||_infinity ||b||_infinity.

Uniqueness identifies the Dirichlet Green function as
G_D(x,y)=Gamma_y(x)+w_y(x). Consequently G_D-g is bounded uniformly
near the interior diagonal, and G_D is uniformly bounded when its
arguments are a fixed positive distance apart, with y in K.
This argument uses only the compact Dirichlet inverse and maximum
principle; it is not a quotient image-series convergence assumption.

The poles in the actual source may approach the OUTER boundary.
Choose a fixed smooth compact enlargement Q+ in the ambient complete
manifold, with closure(Q) inside interior(Q+). Positivity and the maximum
principle give domain monotonicity

    0 <= G_Q(x,y) <= G_(Q+)(x,y).

For the last Green function, all y in Q are uniformly interior poles.
The preceding construction therefore bounds G_Q uniformly whenever
d(x,y)>=delta>0, including x or y near the original outer boundary.
No uniformity in an expanding cusp truncation has been established.

With H_f the bounded harmonic extension of f,

    F_epsilon(x)=H_f(x)-integral_Q G_Q(x,y)rho_epsilon(y)dvol_y.

Uniform total source mass now implies a uniform bound for F_epsilon
on any closed set a fixed distance from ALL arcs, even where that set
meets the outer boundary. This proves the cutoff-support bound required
by R30; a merely interior Green estimate would not have done so.

## 3. An infinite tube used only as a local comparator

In the Fermi metric

    dr^2+sinh(r)^2 dtheta^2+cosh(r)^2 dz^2,

extend one normalized tube along an infinite geodesic of H3. Convolve
its density with g and put F_infinite=-g*rho. For fixed epsilon this
integral converges: the local 1/d singularity is integrable against
bounded three-dimensional density, and the axial tail is exponential.
For coordinates (r,0,0) and (s,theta,z),

    cosh d=cosh r cosh s cosh z-sinh r sinh s cos theta
           >=cosh(r-s)cosh z >=cosh z.

With mass 2pi beta per unit z the discarded tails |z|>Z are bounded by

    4pi beta integral_Z^infinity g(z) dz
       = -beta log(1-exp(-2Z)).

The convolution is rotationally and axially invariant. It tends to zero
as r tends to infinity: for r>=epsilon+1, g(d) is bounded by a constant
times sech(r-epsilon)^2 sech(z)^2, whose z integral is finite. It is
regular at the axis and solves the radial source equation in the weak
sense. Integrating (sinh r cosh r F')'=rho sinh r cosh r, with regular
axis and zero-at-infinity normalization, determines it uniquely:

    F_infinite(r) = beta log(tanh r),                      r>=epsilon,
    F_infinite(r) = beta [log(tanh epsilon)
       +(log cosh r-log cosh epsilon)/sinh(epsilon)^2],     r<=epsilon.

The value and first radial derivative join. This is R29/R30's radial
field with a different, irrelevant additive normalization, not a new
global identification. The volume measure is sinh r cosh r dr dtheta dz;
replacing it by the normal-disc area measure sinh r dr dtheta would
change the prescribed linear charge and is an invalid shortcut.

## 4. Transfer to the actual compact solution

Choose for each arc a positive-length interior subsegment and a short
embedded Fermi cylinder B around a larger interior subsegment. The
observation cylinder K0 (including r=0) lies compactly inside B. Make
its radius R0 and all cylinders small enough that only this source
meets B, and K0 is a fixed distance from Q minus B. Shrink epsilon_0
once if needed; all choices are independent of subsequent epsilon.

Split the actual Green integral into source points in B and outside B,
and the infinite comparator integral into its matching B and its rest.

* In B the two source densities and volume measures agree exactly.
  The difference G_Q-g is bounded for observation points in K0 and
  source points in B: use the interior parametrix near the diagonal,
  and the off-diagonal bounds elsewhere. Its integral is bounded by
  that constant times the uniformly finite mass in B.
* Actual source points outside B are a fixed distance from K0, so the
  Q+ Green bound times the total actual mass controls their contribution.
* The comparator's remaining bounded-z pieces are likewise separated
  from K0. Its unbounded-z tail is controlled by the explicit tail bound
  above (after shifting the observation z by a fixed bounded amount).
* H_f is uniformly bounded by its fixed boundary supremum.

Thus, on K0, including its finite-width core,

    |F_epsilon-F_infinite| <= C,

with C independent of epsilon. In particular,

    |F_epsilon-beta_j log r| <= C_j,  2epsilon<=r<=R0,

since log(tanh r)-log r is bounded on (0,R0]. This is the uniform
global-to-local estimate, not a fitted finite-epsilon extrapolation.
Constants may depend on Q, its compact enlargement, the arc geometry,
beta_j and boundary data; no numerical m202 constant is claimed.

Endpoint qualification: F=0 at a Dirichlet endpoint is incompatible
with a uniform beta log r description all the way to that endpoint.
We have asserted the latter only on interior subsegments. R30's cutoff
is nevertheless one near the WHOLE proper arc, including its endpoints;
its derivative lies off all sources, where section 2 gives the other
needed bound. An axial cutoff through a core is still invalid for the
vanishing Rayleigh quotient. The proof does not change that domain.

## 5. Consequence in the already specified fermion model

Retain R30's positive bulk L2, extending flat unitary line L, exact h=dF,
maximal differential d_q=d_A+q dF wedge, and absolute outer realization.
For q>0, a_j=q beta_j>=1, a local parallel unit section s_j and disjoint
whole-arc cutoffs chi_j, the scalar H1 trial functions

    u_j=exp(-qF_epsilon)chi_j s_j

have bounded energy ||d_q u_j||^2 and norm squared bounded below by
a positive constant times integral_(2epsilon)^R0 r^(1-2a_j)dr.
Section 2 supplies the numerator estimate and section 4 the denominator.
Consequently the R30 min-max conclusion now applies to this actual
global Poisson family: at least k scalar eigenvalues tend to zero.
For equal a, their upper bounds are

    lambda <= C epsilon^(2a-2) if a>1,
    lambda <= C/log(1/epsilon) if a=1.

For unequal a_j use the largest of the k individual bounds on their
disjoint span. When L is nontrivial, H0(Q;L)=0, so these eigenvalues
are positive at each width. The closed Hilbert complex supplies the
odd partner d_q u/sqrt(lambda) for every exact positive scalar
eigenfunction. The declared four-dimensional action therefore has at
least k light Dirac PAIRS, with masses sqrt(lambda), not k unpaired
Weyl generations. No exactly-k count or lower mass bound follows.
For a trivial line some min-max states can be zero; the positive-pair
count just stated cannot be copied without subtracting H0.

For the selected three arcs this gives at least three light pairs in
the stated strong-source regime. Finite-width ordinary cohomology and
R19's singular relative three/zero result remain different domains.
The compact estimate is not uniform in cusp length and does not identify
the complete singular or noncompact limiting kinetic space.

## 6. Independent comparators and explicit limits of the result

A line-kernel antiderivative, useful without a radial PDE solver, is

    A_r(t)=[asinh(coth r sinh t)-t]/(4pi),
    A_r'(t)=g(arcosh(cosh r cosh t)),  r>0.

Its two infinite limits give integral_R g(d)dt=-log(tanh r)/(2pi).
Finite segments and reflection across the totally geodesic plane z=0
give a separate hyperbolic Dirichlet control. For a source on 0<s<L,
subtract the reflected kernel at -s; the potential vanishes exactly
at z=0 while retaining the interior logarithm. This is an H3 half-space
CONTROL, not a compact m202 Green function or a fermion end spectrum.

Finite-width three-dimensional convolution independently tests the
radial comparator. With t=sinh(s)^2/sinh(epsilon)^2 the source measure
is beta dt dtheta dz. Two transverse resolutions and the analytic axial
tail bound are specified in the design. Numerical integration errors
are not interval certificates and do not prove the uniform theorem.

Fixed-height shrinking tubes instead have beta_epsilon=O(epsilon^2);
their transverse well depth tends to zero. Wrong sign or subcritical
q beta likewise does not satisfy the stated light-scalar argument.
No claim about all R29 weights, a selected physical width, full-parent
interactions, anomaly completion, gravity, or empirical masses follows.
The useful physical finding is a design constraint on one proposed
completion: resolving these sources alone does not make the compensating
fermions heavy as the width shrinks. Other kinetic spaces, derived end
conditions, nontrivial gauge/Higgs topology or interactions remain live
questions, not excluded programs.

## Sources and transfer boundary

1. H. S. Cohl and E. G. Kalnins, [Fundamental solution of the Laplacian in the hyperboloid model of hyperbolic geometry](https://arxiv.org/abs/1201.4406), arXiv:1201.4406v1, theorem 3.1, section 3.2 and proposition 4.1. The entire 20-page supplied-by-arXiv PDF was personally read. Only the H3 kernel and its normalized choice are used; a global quotient Green bound is proved separately above.
2. I. G. Gjerde, K. Kumar, J. M. Nordbotten and B. Wohlmuth, [Splitting method for elliptic equations with line sources](https://arxiv.org/abs/1810.12979), arXiv:1810.12979v1, sections 3.1--3.4 and 4--5. The entire 26-page PDF was personally read. Singularity subtraction is prior art, not claimed as novel here. Their Euclidean scalar-permeability theorem is not imported as a hyperbolic, finite-width or active-boundary-endpoint theorem.
