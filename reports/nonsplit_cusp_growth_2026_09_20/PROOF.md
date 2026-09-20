# F03 authored argument: an infinite-energy candidate must be angularly wild

This is a pre-execution analytic candidate with explicit scope. It does
not assert new mathematics in the literature or independent expert review.

## 1. Global positive flux, without a total-energy assumption

Use DESIGN's rank-two representation and coordinates. Every image element
acts by z -> a^2 z+a c with |a|=1, leaving b=-log y invariant. Thus b composed
with an equivariant map descends to a smooth function on M. The target
Hessian identity Hess b=g-db tensor db, already checked in F01, gives

    Delta b = q,   q=exp(2b)|dz|_M^2 >= 0.                 (1)

No integrability at infinity is assumed. Stokes is applied only to finite
compact truncations M_R. With A0 the reference torus area,

    Q(R)=integral_(M_R) q=A0 exp(-2R) Bbar'(R).            (2)

Peripheral translation is nonzero, so z cannot be locally constant
everywhere; q is positive somewhere. Choose R0 with Q0=Q(R0)>0. Since q>=0,

    Bbar'(r)>=Q0 exp(2r)/A0,
    Bbar(r)>=Bbar(R0)+Q0/(2A0)*(exp(2r)-exp(2R0)).         (3)

In particular Bbar is increasing and tends to positive infinity. This is
the old F01 flux mechanism, now used without the finite-energy conclusion.
The one-cusp and source-free hypotheses matter: no unknown second flux
or defect current appears on the right of (2).

## 2. What the translation forces on each torus

Write z=-x1+x2+zeta with zeta periodic, possibly complex. Let < > denote
average in the fixed flat metric h0. The derivative of zeta has zero mean,
so the cross term with (-1,1) integrates to zero. Therefore

    <|d_T z|^2_(h0)> = K+<|d_T zeta|^2_(h0)> >= K>0.

This uses the actual period, not the dimension of a character space. Define
Omega(r)=Bbar(r)-min_T b(r,.). The cusp Laplacian is
partial_r^2-2 partial_r+exp(2r)Delta_T. Averaging (1), including the
nonnegative radial z derivative, gives

    Bbar''-2Bbar'
      = <exp(2b)(|z_r|^2+exp(2r)|d_T z|^2)>
      >= K exp(2r+2Bbar-2Omega).                         (4)

The minimum, not the mean, is the justified lower bound on exp(2b).
Replacing it by exp(2Bbar) is generally false; section 5 supplies a smooth
countercontrol. No claim that periodicity bounds Omega is made.

## 3. The differential inequality that cannot exist on a whole half-line

Lemma. If u is C2 for all r>=r0, u'>0, and u''>=kappa exp(pu) with kappa,p>0,
then there is a contradiction. Multiplication by 2u'>0 yields

    u'(r)^2 >= v0^2+(2kappa/p)*(exp(pu(r))-exp(pu0)).      (5)

If the solution existed on the whole half-line, u''>=kappa exp(pu0)>0
would force u to infinity. But the time needed is bounded above by

    integral_(u0)^infinity du /
      sqrt(v0^2+(2kappa/p)*(exp(pu)-exp(pu0)))
    <= pi exp(-p*u0/2)/sqrt(2*kappa*p) < infinity.        (6)

For the last bound, replace v0 by zero and substitute
t=exp(-p*(u-u0)/2); the remaining integral is integral_0^1
(1-t^2)^(-1/2) dt=pi/2. A global C2 solution cannot reach infinite u at a
finite r. The zero-initial-slope comparison is explicit:

    u=u0-(2/p)log cos(sqrt(kappa*p/2)*exp(p*u0/2)*(r-r0)).

This elementary blow-up argument is supplied directly. No multidimensional
Keller-Osserman theorem with unverified hypotheses is being applied.

## 4. Necessary angular growth for any hypothetical global map

Suppose limsup_(r->infinity) Omega(r)/Bbar(r)<1. Bbar is eventually positive
by (3), so there exist epsilon>0 and r1 such that min_T b>=epsilon Bbar
for all r>=r1. Equations (3)--(4) imply

    Bbar'' >= K exp(2r1) exp(2epsilon Bbar),   Bbar'>0.

Section 3 rules this out. Thus every hypothetical smooth global harmonic
map in the stated rank-two class must satisfy

    limsup Omega/Bbar >= 1,
    limsup exp(-2r)*Omega(r) >= Q0/(2A0)>0               (7)

for each fixed R0 with Q0>0. The second assertion follows by taking a
sequence with Omega/Bbar approaching at least one and using (3). This is
a necessary condition, NOT existence of a map satisfying it.

Consequently there is NO such global map with Omega=o(exp(2r)). This
excludes bounded angular oscillation, polynomial growth in r, and the
entire angularly constant/affine radial ansatz, even if its radial energy
is infinite. It does not exclude arbitrary angularly wild solutions.

There is also a pointwise geometric cost. If D0 is the diameter of the
reference flat torus, integration along a shortest torus path gives
Omega <= D0 sup_T |d_T b|_(h0). The physical transverse covector norm is
exp(r) times the h0 norm. Since |df|>=|db|, (7) entails

    limsup exp(-3r) sup_(T_r)|df| >= Q0/(2A0 D0)>0.      (9)

This is a necessary growth bound along a sequence, not a uniform lower
bound at every large r or a computed solution. It specifies what a proposed
physical completion must handle; no UV or backreaction exclusion is inferred
merely from the word 'unbounded'.

For the radial affine ansatz z=-x1+x2, b=B(r), the exact equation is

    B''-2B'=K exp(2r+2B).                               (8)

Positive outward Busemann flux forces B'>0 and hence finite-r blow-up.
The familiar local cusp B=-r+log(2/K)/2 instead has B'=-1: its outer flux
is negative. Its inner boundary supplies the required positive flux. It
is a valid local solution but cannot provide the sole end of the smooth
source-free compact core in (2). This is consistent with F01, not a new
rejection of that local positive.

## 5. Why the remaining angular loophole cannot be silently discarded

On the flat unit circle, extended trivially in x2, set theta=2*pi*x1,

    w=1+(3/5)cos(theta),
    b=-(1/2)log w,
    z=x1+(3/(10*pi))sin(theta).

All fields and derivatives are smooth, w>=2/5, and z has unit additive
period. Since z_x=w and exp(2b)=1/w,

    average exp(2b)|z_x|^2=average w=1.

But w=(9/10)|1+(1/3)exp(i theta)|^2. The absolutely convergent logarithm
series on |(1/3)exp(i theta)|<1 has zero mean real part. Therefore

    average b=(1/2)log(10/9),   exp(2*average b)=10/9>1.

Thus the putative bound weighted energy >= exp(2*mean b)*period^2 fails
even for smooth fields. This slice is NOT a harmonic map on M or a global
escape example. It is an exact falsifier for an invalid proof step that
would incorrectly close the unrestricted infinite-energy case.

## 6. A generic local linearization, not a new golden prediction

For a dimension-d hyperbolic cusp with an affine translation, the radial
operator is partial_r^2-(d-1)partial_r. The local solution is
B=-r+log((d-1)/K)/2. Put B=B_local+delta. Linearization gives

    delta''-(d-1)delta'-2(d-1)delta=0.

At d=3 the characteristic exponents are 1+sqrt(5) and 1-sqrt(5). They do
not depend on m010, an arithmetic trace, a special cusp shape, or the
normalization K. A square-root-five occurrence here is generic to this
dimension/curvature/translation ansatz, not independent evidence of a
physical golden constant. At d=2 the exponents are 2 and -1, providing
an exact dimension countercontrol.

## 7. Physical scope and next test

This closes a controlled asymptotic subclass, not the full physical mission.
No finite-energy assumption was used in sections 1--4. Conversely, none of
those sections derives a physical rule excluding the angular growth (7).
The fixed-metric action, backreaction, source sectors and UV validity still
have to decide what is admissible; calling growth 'wild' is not a physical
exclusion criterion.

The rank-four coefficient system Sym^3(rho) tensor chi retains its algebraic
index. An arbitrary harmonic metric for that system need not be induced
from a rank-two metric. F03 therefore cannot exclude all rank-four metrics.
It rules out this rank-two construction and a proposed realization that
specifically requires that same controlled rank-two harmonic map. F01's
finite-energy theorem has its own
direct rank-four argument and is not broadened by analogy.

The next alternatives are concrete: analyze genuinely angle-dependent end
data with the necessary lower growth bound; test the rank-four harmonic
equation directly; or derive the compensating current from the coupled
parent/source action. A semisimplified replacement from a length-spectrum
theorem would change the representation and lose the index mechanism.
