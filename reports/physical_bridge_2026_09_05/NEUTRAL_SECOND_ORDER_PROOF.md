# R50 authored proof: a finite-action two-jet, not a full branch

September 27, 2026. Conditional on R42/R44 canonical geometry and its
all-jet/end/core conclusions, R45 complete domains and density input,
R46 supplied action, R47 flat tangent, and R49 spectral/regularity
argument. Their authored/external-input grades are unchanged. Finite
controls do not independently certify the analysis below.

## 1. The exact question

On the SAME fixed complete background (g,H,C) at q0>0, q0!=1, put
d=d_C. Its complete Hilbert complex has finite harmonic spaces and
closed ranges by R49. Let Pi_j project to harmonic degree j and G_j
be Delta_j inverse on the orthogonal complement, zero on the kernel.
These are global operators, not the model end inverse or an asserted
numerical spectral gap. Standard Hilbert-complex orthogonal
decomposition follows here directly from closed ranges and d^2=0.

R47 constructs an actual flat curve on this fixed smooth bundle,

    C(s)=C+s c+s^2 c2+O(s^3),  s=k-k0, k=log q,
    d c=0,                  d c2=-c wedge c.                (1)

It does NOT assert the whole curve is moment-map zero with fixed H.
The parameterwise bundle identification in R47 can be chosen smooth
to every finite order and equal to its explicit normal frame on the
deep end. On that end,

    c=(D+b P/R)dt,      c2=(b2 P/(2R))dt,
    b=d_k beta, b2=d_k^2 beta, beta=6/(q-q^-1).

Both have bounded covariant jets in the normalized end charts for
each fixed q0; derivatives on the compact core are smooth and bounded.
The dt norm is bounded in the canonical metric. Thus c,c2 are Lp for
every finite p>=2 and satisfy all exponential L2 weights epsilon<1/2
in r=log(R)/2. No uniform estimate as q0 approaches 1 is claimed.

Let alpha=Pi_1 c, the nonzero R47 harmonic projection. R49 places
alpha in the nonlinear space X=Dom(Q) intersect L4. Its proof and
local homogeneous elliptic estimates also give, for every delta>0
and finite j,

    |nabla^j alpha| <= C_(delta,j) exp(delta r).             (2)

Indeed lift a fixed ball, use the harmonic equation and all-jet
coefficient bounds, and retain the same exp(r/2) multiplicity factor
as for its zeroth derivative. Epsilon can approach, but not equal,
1/2. This is subexponential growth, NOT uniform boundedness.

## 2. Inhomogeneous extension of the R49 estimate

Lemma in this SAME geometry: if u is in the complete L2 Q domain,
Q u=f, and every finite jet of f is subexponential as in (2), then
u has that property too and lies in every finite Lp, p>=2.

For any epsilon<1/2, the forcing satisfies exp(epsilon r) f in L2:
choose delta>0 with 2(epsilon+delta)<1 and use dvol asymp exp(-r).
For a deep-tail cutoff chi, let w_T=chi exp(epsilon min(r,T))u.
The complete multiplier rule and R49 exterior estimate give

    sqrt(gamma)||w_T||_2 <= ||Qw_T||_2
      <= ||chi exp(epsilon min(r,T)) f||_2
         + C_chi ||u||_(compact annulus)
         + epsilon sup_tail |dr| ||w_T||_2.                (3)

Choose gamma<1/3 sufficiently near 1/3 and the tail sufficiently deep
that sqrt(gamma)>epsilon sup_tail|dr|; |dr| tends to sqrt(4/3).
The compact-annulus term is independent of T. Absorb and take T to
infinity. This proves the same weighted L2 estimate for u as for alpha.
It uses a first-order norm inequality, not an unjustified claim that
G is bounded on every unweighted Lp space.

Local inhomogeneous elliptic regularity on an unwrapped fixed ball
bounds each jet of u by its lifted L2 norm and finitely many lifted
Sobolev norms of f. The former is bounded by
C_epsilon exp((1/2-epsilon)r); the latter by C_delta exp(delta r),
using the assumed jet bounds and bounded lifted-ball volume. The
projection covers at most C exp(r) meridian cells, exactly as in R49.
Taking epsilon sufficiently near 1/2 and delta arbitrarily small
proves (2) for u. Compact-core regularity completes the result.
Integrating exp(p delta r-r) with delta<1/p proves finite Lp.

No L-infinity assertion, positive injectivity-radius assumption or
all-orders nonlinear Banach-space inverse theorem is hidden here.

## 3. Transport the FLAT two-jet to the harmonic representative

Because Ran(d_0) is closed, R47's c-alpha is now an actual exact
form, not just in the closure. Choose the unique minimal L2 primitive
sigma perpendicular to ker(d_0):

    d sigma=c-alpha=:p.

This zero-form is in Dom(Q), with Qsigma=p. The lemma applies, since
c and alpha have subexponential jets. Thus sigma has the same property;
in particular sigma,c,p are in L4 and all their pairwise products in L2.

The FORMAL two-jet of transformation by exp(-s sigma) of (1) has
first coefficient alpha=c-p and second coefficient

    b_flat=c2-[c,sigma]+(1/2)[p,sigma].                    (4)

Brackets with a zero-form are ordinary matrix commutators, with form
degree carried along. Applying the graded Leibniz rule, d c=d p=0,
d sigma=p and d c2=-c^2 gives exactly

    d b_flat=-(c-p)^2=-alpha wedge alpha.                  (5)

The free graded-algebra control expands this identity without a
matrix evaluation that might accidentally commute its variables.
The one-half term is essential. Products in (4) are L2, so b_flat is
L2; (5) is an L2 distributional derivative since alpha is L4.
Maximal equals complete d domain by the inherited cutoff/Friedrichs
argument. Therefore (5) is genuinely exact in the L2 complex and

    Pi_2(alpha wedge alpha)=0.                            (6)

This is stronger than ordinary representation-variety smoothness,
and is exactly where the actual end regularity is used. It is NOT
a claim that exp(-s sigma) is a bounded admissible finite gauge
transformation: sigma need not be bounded, and no such exponentiation
is needed to obtain the finite polynomial primitive (4).

## 4. Also cancel the moment-map residual

Use the R46 real compact/Hermitian decomposition u=a+psi. In its
fixed convention the exact residuals are

    F(C+u)=d u+u wedge u,
    mu(C+u)=M(u)-sum_i[a_i,psi_i],
    d^dagger u=G(u)+M(u),                                 (7)

with compact background gauge G and Hermitian M. Index contraction
uses g, and the split uses H. These are the local nonabelian equations
of the supplied action, not the later abelian examples in its source:
[Braun et al. (2.9)--(2.18), (B.12)--(B.14)](https://arxiv.org/html/1812.06072v2).
The parent and product spacetime remain inputs, not derived gravity.

Set j2=alpha wedge alpha, j0=sum_i[a_i,psi_i]. Both have
subexponential jets and are in all finite Lp. The source j0 is
Hermitian and trace-free. Equation (6) removes the curvature harmonic
obstruction. Degree zero has no harmonic obstruction: an End0(E)
harmonic zero-form is d-parallel, hence an invariant endomorphism.
R45's SL4(R) density input for every q!=1 gives only scalar global
endomorphisms, and trace-free removes them. Thus Pi_0=0. The three
cusp-invariant matrices are NOT global parallel sections.

Define

    beta2=-d^dagger G_2 j2, beta0=d G_0 j0,
    beta=beta2+beta0.                                     (8)

Closed-range Hodge theory gives d beta2=-j2, d^dagger beta2=0:
j2 is d-closed (indeed exact), and (6) removes its harmonic part.
Similarly d beta0=0 and d^dagger beta0=j0 because Pi_0=0.
These statements hold in the complete graph domains, not just on
compactly supported forms. In particular Q beta=-j2+j0 in degrees
two and zero, and beta is L2 and perpendicular to harmonic degree one.
The inhomogeneous lemma now gives beta in X and all finite Lp with
subexponential jets. Equation (7) implies

    d beta=-j2, G(beta)=0, M(beta)=j0.                     (9)

No separate modification of the base or coefficient metric was made.
The Hermitian part of the ADDITIVE connection correction is an allowed
parent scalar field. Complex gauge was used only for the exactness
identity in section 3, not as a physical gauge redundancy.

## 5. What the action actually does after relaxation

For u(s)=s alpha+s^2 beta, the curvature and moment residuals in (7)
have no terms of orders zero, one or two. Their remaining terms are
finite L2 polynomials starting at s^3. Products alpha beta and beta^2
are L2 by their L4 bounds. Hence in the SAME supplied action

    V(u(s))=(2/g7^2)(||F(C+u(s))||_2^2+||mu(C+u(s))||_2^2)
            =O(s^6).                                     (10)

Thus the nonnegative order-s^4 coefficient after allowing second-order
field relaxation is ZERO along this particular harmonic q direction.
This does not require, compute or deny a positive straight-line quartic
V(s alpha). It does not determine the sixth-order coefficient, and
cannot turn an O(s^6) error into an exact branch. The result is a
finite-action BPS TWO-JET, not a full stationary solution for s!=0.

For a generic tangent, the analogous curvature harmonic obstruction
Pi_2 j2 need not vanish. If H0 is nonzero, Pi_0 j0 must also be checked.
If j2 is not closed, its harmonic projection alone is insufficient.
The finite Hilbert-complex tests explicitly distinguish these cases.

Next: an all-orders/convergence argument in an appropriate weighted
nonlinear space or a genuine higher obstruction, full harmonic census
and normalized interaction tensors. R48 pairing, source/end/parent
selection, physical chirality, anomaly/quantum completion, scales and
gravity remain duties. No universal no-go or independent global proof
acceptance follows from this conditional two-jet construction.
