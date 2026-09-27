# Authored analytic construction on the fixed hyperbolic background

2026-09-27, before execution. Finite controls discharge the literal
algebraic hypotheses; they do not independently certify global analysis.
Standard local-coefficient de Rham theory, local elliptic regularity,
Rellich compactness and complete cutoff theory are explicit mathematical
inputs. Metric, parent, spacetime and positive coupling remain supplied.

## 1. A real interior class in the correct structure algebra

Write E_t(g)=diag(t^v_g)P_g for a declared family. P_g is a real even
permutation matrix, hence lies in SU5. Let A0 be the corresponding finite
unitary flat connection on E_1. Its associated real trace-free diagonal
bundle a_R is preserved by conjugation by P_g. It is not a globally
trivial four-dimensional coefficient system.

In coordinates H(x)=diag(x0,x1,x2,x3,-sum x), the invariant inner product
is tr(H(x)H(y))=x^T G y, G=I+ones. Each matrix R_g of this action is
derived independently and checked against actual diagonal conjugation.
The logarithmic derivative c_g=v_g is a group one-cocycle in this module:
c_gh=c_g+R_g c_h. Trace zero, relators and peripheral periods are checked
as exact identities. In the chosen marked peripheral gauge c_mu=c_lambda=0.

The producer verifies H0(M2;a_R)=0 and that c is not an ordinary
coboundary: adjoining it to the d0 columns raises rank. It also checks
that its class is in the kernel of restriction to the cusp. Pullback to
M6 is checked using the actual inclusion words, not an assumed factor
of three. These are hypotheses to be discharged by the native run.

By the de Rham theorem with local coefficients and the exact sequence of
the compact core and its boundary, this nonzero interior class has a smooth
compactly supported closed real representative alpha0 on M2. The end is
a collar, so a representative exact there can be cut off by subtracting
the differential of its cusp primitive. This step creates no physical
source: it changes the representative, not the closed cohomology class.

## 2. The ZERO-form inverse exists; no one-form gap is assumed

On the exact hyperbolic cusp g=dr^2+exp(-2r)h_T the finite unitary bundle
has a parallel radial frame. For a compactly supported section f on the
open tail, set v=exp(-r)f. Fiberwise integration gives

    integral |partial_r f|^2 exp(-2r) dr
      = integral (|partial_r v|^2+|v|^2) dr
      >= integral |f|^2 exp(-2r) dr.                 (1)

Boundary terms vanish for these supported test sections; tangential energy
is nonnegative. The same estimate holds with finite peripheral monodromy,
or on a finite torus cover and then by descent. This is exterior Dirichlet
coercivity in DEGREE ZERO, not a global bound of one on all sections.

For completeness, suppose there were no positive global Poincare constant.
Take smooth compactly supported f_j with L2 norm one and ||d_A0 f_j||_2 -> 0.
Local H1 bounds, Rellich and a diagonal subsequence give a globally parallel
local limit. It vanishes because H0(a_R)=0, so f_j -> 0 in L2 on every
compact set. Apply (1) to chi f_j with chi=0 below a fixed height and
chi=1 on a deeper tail. Its derivative term on the fixed transition collar
also tends to zero. Both tail and core norms therefore tend to zero,
contradicting normalization. Thus

    ||f||_2 <= C ||d_A0 f||_2.                       (2)

The nonnegative self-adjoint zero-form Laplacian Delta0=d_A0^dagger d_A0
has a bounded inverse G0. We use its Friedrichs/complete realization;
no boundary condition at a finite cutoff is inserted. The numerical gap
or value of C is NOT computed. The scalar trivial local system would have
constant L2 zero modes, showing why the checked H0 hypothesis matters.

Set f=-G0 d_A0^dagger alpha0 and

    beta=alpha0+d_A0 f.                              (3)

Then f and d_A0 f are L2, elliptic regularity makes them smooth,
d_A0 beta=0, and d_A0^dagger beta=0. The ordinary class of beta equals
the nonzero class of alpha0, so 0<||beta||_2^2<infinity. This also proves
that beta is not removed by a globally defined ordinary diagonal gauge
parameter. The metric and this period normalization fix beta; no attempt
is made to tune its norm to a measured value.

## 3. Full cusp decay, L4 and complete domain

Above the compact support of alpha0, f is harmonic and beta=d_A0 f.
Pass to the finite torus cover which trivializes the permutation monodromy.
Each component of f has a Fourier series. If lambda is a flat torus
eigenvalue, the radial equation is

    f_lambda''-2 f_lambda'-lambda exp(2r) f_lambda=0. (4)

The zero mode is A+B exp(2r). L2 excludes B; its remaining derivative
is zero. For lambda>0 the two modes are proportional to
exp(r) I1(sqrt(lambda) exp(r)) and exp(r) K1(sqrt(lambda) exp(r)).
L2 excludes I1. NIST's differential equation, derivative and asymptotics
give the decaying K1 branch and its differentiated estimates.[1]

This is not an inference from a single mode. On a fixed slice r0 the
smooth trace has rapidly decreasing Fourier coefficients. Express every
mode at r>=r0+1 as its trace coefficient times

    exp(r-r0) K1(sqrt(lambda)exp(r))
                  / K1(sqrt(lambda)exp(r0)).          (5)

For nonzero torus eigenvalues lambda>=lambda_min>0, numerator and inverse
denominator asymptotics give polynomial factors times
exp[-sqrt(lambda)(exp(r)-exp(r0))]. Derivatives introduce only further
polynomial factors. The trace coefficient decay and the two-dimensional
lattice count make these series uniformly summable on the higher tail.
Consequently beta and every fixed-order orthonormal derivative decay
at least C_j exp(-c exp(r)) there, after decreasing c>0 to absorb powers.
Finite descent changes no conclusion. The zero Fourier part of beta is
exactly zero, not merely small.

On the compact core smoothness supplies boundedness. Therefore beta is
in Lp for every finite p>=1 and in L-infinity, in particular L4. Complete
cutoffs approximate it in the graph norm of Q0=d_A0+d_A0^dagger and in
L4; cutoff commutators are bounded by |d chi| |beta|. Thus beta belongs
to the complete nonlinear fluctuation space Dom(Q0) intersect L4.
No finite end boundary condition or defect extension was chosen.

## 4. Exact nonlinear fields and the literal holonomy family

The diagonal algebra is commutative in every parallel chart and preserved
by all transition permutations. Hence beta wedge beta=0 and all pointwise
commutators of its components vanish. For ANY finite z=s+i tau define

    A_z=A0+i tau beta,  Psi_z=s beta,
    C_z=A_z+Psi_z=A0+z beta.                         (6)

A_z preserves the fixed positive metric and Psi_z is Hermitian. Directly,

    F_Az+Psi_z wedge Psi_z=0,
    d_Az Psi_z=0,  d_Az^dagger Psi_z=0.              (7)

The derivative terms vanish by (3), and the nonlinear terms by diagonal
commutativity. These are global equations, not a first-order solution or
a formal infinite series. The differences z beta are in the same complete
Dom(Q0) intersect L4 space for every finite z. The diagonal restriction of
Q_z also equals Q0, since brackets with beta vanish.

Here is an explicit matching to the original flat bundles, avoiding an
unexamined logarithmic-holonomy assertion. On the universal cover choose
a primitive F with dF=beta. Use the associated-bundle convention in which
sections transform by P_gamma. The integration cocycle of beta represents
c_gamma; adjusting F by a constant makes

    F(gamma x)=Ad(P_gamma)F(x)+v_gamma.

Put g_z(x)=exp(z F(x)) and t=exp(z). Then

    g_z(gamma x) P_gamma
        = diag(t^v_gamma) P_gamma g_z(x).            (8)

Thus g_z intertwines the two associated bundles. Pulling the flat
connection back from the literal E_t gives g_z^-1 d g_z=z beta, exactly
(6). A path-holonomy inverse convention reverses BOTH descriptions, not
just the coefficient used in the cohomology engine. This identification
does not assert that g_z is a globally defined gauge of E_1 or a physical
complex gauge symmetry. F need not be bounded on the universal cover.

The integer period cocycle makes z -> z+2 pi i a compact gauge equivalence
by exp(2 pi i F); no claim that these are the only identifications or that
the displayed parameter space is the full moduli space is needed.

## 5. Physical kinetic norm, non-gauge tangent and zero classical potential

Use the supplied twisted gauge action with C=A+Psi and the fixed positive
parent trace. Its scalar kinetic term has coefficient 1/g7^2 and its
potential in form norms is 2/g7^2 times the curvature and moment residual
norm squares.[2] This is a chosen local gauge parent, NOT a proof of a
global G2/M-theory embedding or gravitational dynamics.

Under the regular E8 embedding beta belongs to the structure sl5 adjoint,
which is gauge-SU5 neutral. Let c5>0 denote the parent trace restricted to
tr_5. In RAW adjoint-E8 trace the branching gives c5=60; the producer
checks this polynomial identity. Other trace conventions rescale g7 and
must not be advertised as a derived coupling.

For z promoted as a fluctuation amplitude the integrated quadratic
kinetic coefficient is

    K = (c5/g7^2) integral_M2 tr_5(beta wedge *beta),
    L_kin = -K partial_mu conjugate(z) partial^mu z,
    0 < K < infinity.                               (9)

This is an expression and finiteness/positivity theorem, not a computed
numerical coupling or a full nonlinear low-energy truncation. The actual
pullback metric on M6 multiplies the integral by three; this geometric
volume factor is not three generations. At constant z the residual-square
potential vanishes IDENTICALLY to all orders. It does not select z.

The variation u=delta z beta satisfies d_Cz u=d_Cz^dagger u=0, including
the compact background-gauge condition. It is not a full-sl5 gauge
artifact: the diagonal projection commutes with d_Cz, while its projection
of a putative gauge primitive would make beta an ordinary diagonal
coboundary, contradicting section 1. The argument applies at every z,
including the finite permutation point; extra tangents there are not
being counted. This is a finite-norm neutral classical flat direction,
not a proof that the charged cohomology already equals the physical spectrum.

## 6. The SAME hyperbolic model has no positive neutral one-form gap

R17 already recorded the scalar/form threshold distinction; the new duty
is to check it on the present full background. Its peripheral diagonal
invariant space is computed to have dimension two. Choose a nonzero
parallel invariant diagonal H on the cusp and a constant torus one-form
xi. The adjoint bracket with beta vanishes. For u=f(r) H xi,

    delta_Cz u=0,
    ||u||^2=C integral |f|^2 dr,
    ||Q_z u||^2=C integral |f'|^2 dr,
    Delta_z u=-f'' H xi.                             (10)

For any fixed flat torus metric C>0 is constant: the inverse metric
exp(2r) cancels the volume exp(-2r). This differs from degree zero's
threshold one. u is in the compact gauge slice, not a longitudinal
gauge mode; it has nonzero tangential periods when f is nonzero.

Let b(x)=x^2(1-x)^2 on [0,1], extended by zero, and normalize
f_L(r)=(L integral b^2)^(-1/2) b((r-R)/L). It is H2, with value and
first derivative zero at the support ends; smooth approximation is
available. The exact controls give

    ||Q u_L||^2/||u_L||^2 = 12/L^2,
    ||Delta u_L||^2/||u_L||^2 = 504/L^4.             (11)

Choose disjoint supports tending down the cusp and L -> infinity.
They are normalized, converge weakly to zero and Delta u_L -> 0,
so zero is in the essential spectrum of this actual neutral one-form
Laplacian. No artificial boundary of the support is a physical defect.
The rapidly decaying beta has no zero Fourier part on the end; it is
orthogonal to these particular escaping torus-harmonic profiles.

Thus (9) remains valid but does NOT give a separated finite-dimensional
four-dimensional EFT. An isolated-mode truncation or a claim that the
whole neutral sector is gapped would be false here. This is not a
quantum instability proof and does not negate the nonlinear background.

## 7. Limits and sources

The exact common-line ordinary-index result remains unchanged. No physical
chiral matter, preferred vacuum, numerical metric profile, mass/coupling
prediction, anomaly completion, gravity or TOE follows from (6)-(11).
The positive advances a dynamics/admissibility step in the correct rank-five
structural slot; the gapless sector prices its dimensional-reduction limit.
Other metrics, sources and end laws require separate justified tests.

[1] NIST DLMF [10.25](https://dlmf.nist.gov/10.25),
[10.29](https://dlmf.nist.gov/10.29) and
[10.40](https://dlmf.nist.gov/10.40), read 2026-09-27. The Bessel argument
is also prior art in R17 CUSP_TAIL.md; no novelty is claimed for it.

[2] Braun et al., [Higgs Bundles for M-theory on G2-Manifolds](https://arxiv.org/html/1812.06072v2),
equations 2.9-2.21 and B.12-B.14, personally checked sectionally. The
source supplies the local parent conventions, not this noncompact global
application. R46's authored action split was read as a cross-check; its
canonical-metric decay/closed-range assertions are not imported.
