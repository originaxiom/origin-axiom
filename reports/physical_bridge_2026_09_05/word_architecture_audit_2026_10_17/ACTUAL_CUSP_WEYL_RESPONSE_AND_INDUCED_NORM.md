# The actual cusp response also determines its exterior norm

October 24, 2026. Authored conditional analytical derivation, UNREVIEWED.
No scientific source, test, symbolic engine or numerical check was
imported, collected or executed. This is not an execution design or
an amendment to a frozen verification package.

Scope: the finite-dimensional ZERO-ANGULAR constant tail already derived
from the supplied graded cusp background. The background, action and
L2 end remain hypotheses. No full angular response, physical generation
count or foundational origin of this background is claimed.

## 1. Recover the same operator and use a nonsingular chart

Reuse [the actual graded-cusp derivation](ACTUAL_GRADED_CUSP_RESPONSE_AND_STATE_SCOPE.md),
including its metric normalization and both scalar extremes. In its
unitarily transported coordinates the actual block is

    D = -i sigma1 partial_t - sigma2 tensor K,
    K=K dagger, K invertible, t>=T, measure dt.                 (1)

K is the specified mass matrix derived from that background, not a new
adjustable boundary mass. The preceding response projector is generally
nonorthogonal at nonzero spectral parameter; do not use it as a Hilbert
orthogonal projection to calculate norms.

Let P+ and P- be K's positive/negative spectral projectors,
H=|K| and J=sign(K). On the full pair (x,v) define

    a=P+ x+P- v,  b=P+ v+P- x.                                (2)

This is a constant unitary involution on the two-slot Hilbert space,
not a deletion of the original negative-mass or adjoint slots.
It commutes with sigma1 and sends sigma2 tensor K to sigma2 tensor H.
For example, on the negative spectral subspace it swaps the two slots,
flipping sigma2 and the sign of K together. Hence

    D_new = -i sigma1 partial_t - sigma2 tensor H, H>0.        (3)

The original chirality grading does NOT become an arbitrary new
grading: Gamma_old=diag(I,-I) is transported to diag(J,-J).
Consequently the a slot is not automatically the original PLUS slot.
This is essential when interpreting a rank at the cut.

## 2. Exact response in the gap

Let h_min be H's smallest eigenvalue and take real |lambda|<h_min.
Functional calculus gives commuting positive matrices

    Q(lambda)=(H squared-lambda squared I)^(1/2),
    M(lambda)=lambda (H+Q(lambda))^-1.                       (4)

M(0)=0 by this formula; no division by lambda is needed.
Every square-integrable solution of (D-lambda)psi=0 is uniquely

    gamma(lambda) a0 =
       exp[-Q(lambda)(t-T)] (a0, -i M(lambda) a0).           (5)

To verify the sign, the two component equations after substitution are

    i(Q+H)b=lambda a,  i(Q-H)a=lambda b.

They give b=-i lambda(H+Q)^-1 a. The identity
(H-Q)(H+Q)=lambda squared I checks the other equation.
These are all decaying solutions: each H eigenvalue supplies precisely
one negative and one positive radial exponent, and the growing
coefficient must vanish in the dt norm.

Define the trace pair

    Gamma0 psi=a(T),  Gamma1 psi=i b(T).                    (6)

Then Gamma1 gamma(lambda)=M(lambda) Gamma0 gamma(lambda).
For the exterior orientation, direct integration by parts gives

    <psi,D phi>-<D psi,phi>
      = i psi(T) dagger sigma1 phi(T)
      = (Gamma0 psi) dagger Gamma1 phi
        -(Gamma1 psi) dagger Gamma0 phi.                   (7)

Inner products are conjugate-linear in their first argument.
Changing the outward-normal convention changes the trace convention
with it, not the positive bulk norm.

## 3. The norm is the derivative of the response

For two real gap parameters lambda and mu, apply (7) to their decaying
solutions. The boundary at infinity vanishes exponentially. This gives

    M(lambda)-M(mu)
       = (lambda-mu) gamma(mu) dagger gamma(lambda).        (8)

The dagger on gamma includes integration over the exterior dt measure.
Taking mu to lambda gives

    M'(lambda)=gamma(lambda) dagger gamma(lambda)
      = (I+M(lambda) squared)/(2 Q(lambda))
      = H/[Q(lambda)(H+Q(lambda))] > 0.                     (9)

There are two independent hand derivations here: differentiating (4),
and directly integrating the norm of (5). In a single H eigenchannel,
with q=sqrt(h squared-lambda squared), the latter is

    integral_0^infinity exp(-2q s)(1+m squared) ds
      = (1+m squared)/(2q) = h/[q(h+q)].

Thus (8) is not an assumption about a new boundary kinetic term.
It expresses the norm already present in the same complete fermion
operator. At zero,

    M(0)=0,  M'(0)=(2H)^-1,                                (10)
    M(lambda)=lambda/(2H)+lambda cubed/(8 H cubed)+...

Equation (10) recovers the preceding exterior norm on its stable
traces. A zero value of the response at zero energy does NOT imply
that the exterior has zero norm or no spectral feedback.

This is the elementary constant-tail case of the Weyl-function
identity. For comparison, the general Green identity and
M(lambda)-M(mu)*=(lambda-conjugate(mu)) gamma(mu)* gamma(lambda)
are stated in Behrndt, Holzmann and Mas, “Self-Adjoint Dirac Operators
on Domains in R3,” §2, Definitions 2.1–2.2 and the paragraph following
Definition 2.2:
https://link.springer.com/article/10.1007/s00023-020-00925-1
(accessed October 24, 2026). Those HTML passages were personally read.
Their three-dimensional realization is not identified with our cusp;
(2)–(10) were derived above for the actual retained tail.

### Existing E6-tail roster: the induced weights are already fixed

The graded-condensate source's retained singular thresholds are
mu squared = 1/4 (133 channels), 5/4 (110), 9/4 (3), 13/4 (2).
Applying (10) to this already specified roster gives the exterior
zero-energy norm matrix eigenvalues

    1 (133), 1/sqrt(5) (110), 1/3 (3), 1/sqrt(13) (2).       (10a)

Its stable trace dimension is 248, not a particle count. In the stated
canonical trace coordinates,

    (1/sqrt(13)) ||a0|| squared
       <= ||gamma(0)a0|| squared <= ||a0|| squared.          (10b)

This is a fixed exterior contribution, not the full compact-plus-tail
kinetic matrix. The source's adjoint roster and its canonical curvature
unit are conditional inputs. These weights are neither fitted flavour
coefficients nor measured masses, and cannot be transferred to the
paper's triplet/quaternion channels without their actual field map.

## 4. Joining retains this norm, not only the zero-energy plane

Suppose a compact-side problem has the same identified trace coordinates,
its prescribed remote conditions, and a uniquely solvable trace chart
on the spectral interval considered. Give it the opposite normal:

    Gamma0_core=a,  Gamma1_core=-i b_core.

Let its actual solution map be gamma_core(lambda), and its response
M_core(lambda)=Gamma1_core gamma_core(lambda). These objects are
hypotheses here; the full compact-core solution has not been computed.

Same-field, same-action transmission is

    a_core=a_ext=a0,
    Gamma1_core+Gamma1_ext=0,

so the reduced spectral equation is

    F(lambda) a0=0, F=M_core(lambda)+M(lambda).              (11)

Where both solution maps are differentiable and the remote domains
are fixed independently of lambda, their Green identities give

    ||psi_joined|| squared
       = a0 dagger [M_core'(lambda)+M'(lambda)] a0.         (12)

The right side is positive for a nonzero reconstructed eigenstate.
It is the full interior-plus-exterior norm, not a new freely fitted
boundary metric. Throwing away M'(lambda) would keep a candidate
zero-energy equation while losing the exterior part of its normalization.

If a trace chart has a pole, or an eliminated remote problem has
unretained kernel data, use its full Cauchy relation and retained
modes instead. Equations (11)–(12) do not license an inverse at such
a point. Nonzero angular modes, trace Sobolev regularity and the full
compact response remain separate analytic duties.

## 5. Thresholds are a concrete limit on elimination

In an eigenchannel h, as lambda tends to +h or -h from the gap,
m(lambda) tends to +1 or -1. The graph in (5) therefore has a finite
algebraic limit while

    m'(lambda)=h/[q(h+q)] -> +infinity.                    (13)

The limiting threshold profile in that channel is not L2. A finite
limiting trace relation is not a finite-norm boundary particle.

There is a second limit: at lambda=0 a tail eigenvalue h->0 makes
M'(0)=1/(2h) diverge. Taking lambda->0 and closing the gap therefore
does not justify replacing the disappearing exterior inverse by a
regular finite metric. This recovers the earlier threshold duty with
an explicit normalization diagnostic.

Other channels with larger h may remain decaying at a first threshold.
The claim is channelwise, not that every trace of a multiblock problem
vanishes when its first threshold is reached.

## 6. Covariance and information preserved

For a constant unitary coefficient change V, transport K, P+/P-, H
and all trace coordinates together. Then M transforms by V M V dagger
and its norm matrix by the same rule. A nonunitary frame change instead
requires transporting the kinetic metric and trace pairing. Arbitrary
independent rescalings cannot be treated as new predictions.

If V also preserves the original grading, (2) still carries that
grading as diag(J,-J). In particular the graph M(0)=0 cannot be relabelled
as an original all-PLUS extreme. The actual normal/spin identification
with the six-dimensional puncture coefficient model remains unpaid.

For the registering relation, retaining only L_ext(0) loses information:
changing h without changing its sign keeps that plane fixed but changes
(10), the thresholds and the finite-energy response. The sufficient
record for this duty must retain at least the response as a function
of spectral parameter and its metric/normal conventions, not just an
index or zero-energy subspace. This is a precise conditional example
of the owner's concern about losing interactions by retaining only
the resulting object.

## 7. Honest input ledger and verification boundary

Derived here: the stable-slot chart, exact gap response, its positive
norm derivative, conditional joined normalization and the threshold
diagnostic, all within the already supplied tail. No extra adjustable
boundary norm has been introduced.

Not derived here: the foundational action/field content, chosen global
condensate, physical curvature scale, actual compact-core response,
full angular operator, gauge/normal/spin map or observed masses.
Lambda remains the operator's spectral parameter; identifying it with
a four-dimensional physical energy or mass requires the actual kinetic
and separation map. Positive L2 norm alone is not a quantum unitarity,
anomaly, supersymmetry or physical spectrum certificate.

This is not a newly paid foundational input or a full P210 closure.
It is a reusable restriction on a future physical end law: it must
reproduce both the response and the norm of its eliminated fields.

A separately sealed successor should test both signs of K, scalar
extremes and paired blocks; the unitary chart and transported grading;
(5) in both differential equations; two-energy Green signs; derivative
against direct norm; zero-energy recovery; positive norm and threshold
divergence; opposite-normal joining; and retention of singular-chart
kernel data. Negative controls must detect a dropped adjoint slot,
a sign-changed response with unchanged trace conventions, a frozen
energy-independent response used for norms, and relabelling a as the
original PLUS space. None of these tests has been run here.

Prior-art scope: already_banked.py was run on “Weyl response norm
derivative”; its four settled metadata hits concern premise audit,
Cartan metric/descent, the E6 coset leg and the SM specification ledger.
Their findings openings/scope sections were inspected; none is being
replaced or claimed refuted. A literal Git search on fetched main for
“Weyl function”, “response derivative”, “boundary response metric”
returned no hits in the searched docs/frontier/report paths. This
does not establish literature novelty or exhaustive repository absence.
The Green/Weyl identity is established mathematics.
