# R17 — uniform charged cusp-tail estimate through the line/cusp joint end

2026-09-07. Pre-execution design, path-local under physical_bridge_2026_09_05.
No global B allocation, empirical comparison, or completed physical spectrum.

BANKED IDENTITY: R14's exact cusp field, R15's prescribed global scalar
extension and R16's local source-line domain analysis. Reuse their actual
Hodge/exterior engine and radial source producer without editing them.

PRIOR ART: deformed de Rham complexes and warped-product Dirac splitting
are standard analytic tools, not new physical laws. The geometric
reduction is Pantev--Wijnholt (0905.1968, sections 3.1--3.3); its
physical parent remains an assumption here. For closed Hilbert complexes
and their adjoints see Arnold--Falk--Winther, Bulletin AMS 47 (2010),
section 3.1, https://www-users.cse.umn.edu/~arnold/papers/bulletin.pdf.
Bruning--Lesch (1992) was located; publisher full text returned 403, so
no unread theorem from it is transferred. Scalar versus one-form cusp
thresholds are distinguished by Golenia--Moroianu 0705.3559, section 5.
Bessel derivatives/asymptotics: https://dlmf.nist.gov/10.29 and
https://dlmf.nist.gov/10.40, read 2026-09-07.

## Scope and grounding

P0: the charged deformed-form operator on exact rank-two hyperbolic
cusps with a real separated logarithmic-source potential, in a fixed
graded closed tangential Hilbert-complex realization, plus a bounded
zeroth-order perturbation. This quantifies over this stated end/domain
class, not all manifolds, gauge bundles, physical defects or fields.

P1/P4: continue PB-BOUNDARY / X33 and R16's explicit joint-end duty.
The smooth annular and closed-double results do not settle this different
sourced operator. The kill-graph's cut/deformation hatch remains scoped.
The framework, ladder/campaign, compute protocol and CC banking receipt
were reread. No reserved/shared B number is used.

P2/P3: atlas chirality card consulted, epoch-blind 1161-arc inventory.
already_banked("Witten cusp coercivity") returns 105 hits, zero settled
arcs matching two of three words. absence_sweep("coercivity") enumerates
11 heads and reports no exact-word hit, including matching deleted paths.
This is lexical scope only, not a literature novelty proof. Source-code
search finds R16 and unrelated Witten/CS usages; actual R14--R16 code and
full reports were read. An initial rg call named two guessed wrong arc
directories; their real B1086_spectrum_law/B1087_charge_grading paths
were resolved. Its error is not an absence finding.

All remote heads and tags fetched, unchanged since the last report.
Pins: main c78003cd, physics 659487bb, SM d1a91c7a,
outside-bench 879869ca. No newly fetched claim used without verification.

P6: expect the growing radial source term to forbid charged low-energy
escape even arbitrarily close to a puncture. Expect uncharged one-form
escape to survive. An omitted cross term, degree weight, or incompatible
domain would invalidate the proposed estimate; preserve that outcome.

## Operator and domain assumptions before testing

Use s=log z, metric ds^2+exp(-2s)(dx^2+dy^2), orientation dx dy ds.
Let H=qF=V(x,y)+h(s), where V may have logarithmic punctures,
h(s)=q exp(2s)(b s+c), b=pi Q/A>0, q real nonzero. The z0 convention
is one; a different z0 is absorbed in c. Neither q nor beta is inferred
from an integer root label.

Choose a closed tangential differential d_V of degrees 0,1,2 with
d_V^2=0, delta_V its HILBERT adjoint, D_T=d_V+delta_V, and degree N.
The boundary realization is independent of s and respects degrees.
It can be a fixed minimal or maximal complex on the punctured torus.
This does not select the physical one or prove the global domain.
No lower bound or spectral gap for D_T is assumed.
Here closed refers to the differential operators and their graphs.
Closed RANGE (the additional AFW meaning of a closed Hilbert complex)
is not assumed, and no Poincare estimate is borrowed from that hypothesis.

Write a 3d form as alpha+ds wedge beta; each tangential degree-j
coefficient is exp((1-j)s) times the new coefficient. This must be
unitary into L2(ds dx dy), not merely an algebraic conjugation.
The candidate operator in these variables is

  D0 = [ exp(s)D_T    -partial_s+h'+1-N ]
       [ partial_s+h'+1-N    -exp(s)D_T ].

The candidate square is diagonal -partial_s^2+exp(2s)D_T^2+
(h'+1-N)^2 with -h'' on alpha and +h'' on beta, PLUS off-diagonal
2 exp(s)d_V above and 2 exp(s)delta_V below. Those terms must be
derived and retained; squaring while commuting N through d_V is wrong.

On a dense joint core with the chosen tangential adjoints, put
S=[0,d_V;delta_V,0]. S^2<=diag(D_T^2,D_T^2) because their difference
is diag(delta_V d_V,d_V delta_V). Young's inequality with epsilon=1/2
then proposes

 ||D0 psi||^2 >= ||partial_s psi||^2 + (1/2)||exp(s)D_T psi||^2
 + integral {max(|h'|-1,0)^2-|h''|-2} |psi|^2.

This is an INTEGRATED operator estimate, not a pointwise lower bound
on the singular Hessian. First prove it on the core and its graph
closure. Any use on another realization must justify the tangential
adjoint relation and the same closed-complex core. Spectral regularization
by the degree-preserving D_T^2 is the intended core extension argument.

## Explicit high-tail sufficient bound and controls

For K(s)=b(2s+1)+2c, require K>=2b and t=|h'|>=8.
Then |h''|<=3t and (t-1)^2-3t-2>=t^2/4.
An explicit sufficient starting height is

 S0=max(0, 1/2-c/b, (1/2)log(4/(|q|b))).

This is a conservative estimate, not a sharp onset height.
For s>=S0 the proposed form bound is at least integral |h'|^2/4
times |psi|^2, independently of proximity to any source puncture.
Test both signs of q, unequal positive source densities and large
positive/negative through-flux c against the actual R14 radial producer.

R15's harmonic corrector v contributes the Clifford multiplication
q(dv wedge+i_grad v), norm |q dv|. If bounded by K_v on a tail, then
||D psi||^2 >= (1/2)||D0 psi||^2-K_v^2||psi||^2.
The decaying z K1 Fourier modes of the smooth L2 corrector have bounded,
decaying orthonormal derivatives; derive the derivative and keep the
constant Fourier mode separate. No computed m202 value of K_v is claimed.

Two-sided controls before execution:
1. Metric Hodge-star derivation of every first-order coefficient equals
   the proposed block form, with exact all-degree norm weights.
   Dropping the degree shift or unitary weight must fail.
2. Independent second-order operator composition equals the full square;
   dropping/reversing the cross block must fail. Verify nilpotency and
   graded commutators, not a hardcoded trace.
3. Exact factorization proves the t>=8 algebraic inequality; test actual
   radial derivatives for beta=(1,1,1),(1,2,3), c=-20,0,20 and both q signs.
4. Independent integrated energy: frozen finite exterior Hilbert complexes,
   complex mixed-degree test functions with nonzero cross terms; direct
   first-order norm versus full expanded form, Gauss orders 64 and 128.
   Relative agreement <2e-11; nonnegative lower-bound margins. These
   are controls of the analytic proof, not a discretized m202 spectrum.
5. Uncharged flat-torus harmonic tangential one-form with sin^2 profile
   of support length L has Rayleigh 4 pi^2/(3 L^2), tending to zero;
   the scalar has 1 plus that quotient. Exact integration plus numerical
   quadrature must distinguish them. A scalar-gap substitution fails.
6. Exact Clifford square and bounded-perturbation identity; actual Bessel
   derivative/PDE checks and 50-digit numerical derivative controls.

## What passing would and would not establish

Passing supplies a uniform high-cusp energy barrier for the specified
charged realization, including concentration toward a line at infinity.
It narrows the complete-operator task but does not prove compactness at
finite-height line singularities, choose the defect boundary law, count
the full H1 kernel or remove the finite four/one pair. No physical
chirality, TOE, empirical prediction or new parent identification follows.

Hash/commit design, new source and tests before first execution. Do not
edit while a scientific/certifying run is live. Preserve original failures;
any necessary instrument repair is a separate sealed artifact.
