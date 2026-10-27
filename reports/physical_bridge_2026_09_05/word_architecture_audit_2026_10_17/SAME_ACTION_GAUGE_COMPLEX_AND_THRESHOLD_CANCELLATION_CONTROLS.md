# Gauge-complex recovery before a physical one-loop threshold

October 27, 2026. UNREVIEWED author hand derivation. No science import,
producer, numerical solver, CAS or test execution. The supplied curved
spin-field action and stationary SM gauge phase retain their exact
hypotheses. This is a zero-angular homogeneous-tail cochain calculation,
not the complete physical gauge-fixed path integral or its beta function.

## 1. Recover the normalized maps from the actual source

Personally reread weave_curved_action_2026_10_08/PROOF and the complete
weave_graded_condensate and weave_sm_parallel proofs. The source fixes
positive kinetic metrics, superpotential and moment map BEFORE the
linear mass block. It retains all four physical Weyl species, including
the gaugino, and the bosonic residual-square Hessian. A gaugino is not
a gauge ghost, and a complex holomorphic gauge quotient is not by
itself a quantized compact-gauge fixing prescription.

The source's paired zero-angular end block has real constants a,k,
D=partial_t+a and formal adjoint Ddag=-partial_t+a on the stated radial
L2 measure. Its infinitesimal normalized gauge map and holomorphic
linearized residual map are

  d0 u=(D u,-k u),
  d1(z1,z2)=k z1+D z2,
  d1 d0=0.                                               (1)

The last equality uses the constant k and the stationary background;
it is not true for a guessed independently varying k(t) with the same
formula. The source already derived (1) from the SAME kinetic gauge
map and W Hessian. The new calculation is the complete cochain Laplacian
and its use as a rejecting control for a naive determinant, not a new
origin claim for (1).

## 2. The positive cochain Laplacians and their projectors

On smooth compactly supported radial fields put L=-partial_t^2+a^2+k^2.
Then direct ordered multiplication gives

  Delta0=d0dag d0=L,
  Delta2=d1 d1dag=L,
  Delta1=d0 d0dag+d1dag d1=diag(L,L).                    (2)

For example d0 d0dag has off-diagonals -kD,-kDdag and d1dag d1
has +kD,+kDdag, so they cancel rather than being dropped. D and Ddag
commute in this constant tail, as do k and both derivatives. This
would need new terms if a or k varies. The same B=(d0,d1dag) obeys
Bdag B=diag(Delta0,Delta2) and B Bdag=Delta1, recovering the prior
fermionic singular blocks without identifying a boson with a fermion.

On the whole radial line with mu^2=a^2+k^2>0, L has bounded inverse.
The operators

  P_g=d0 L^-1 d0dag,
  P_F=d1dag L^-1 d1                                     (3)

are bounded orthogonal projectors with P_g+P_F=I and P_g P_F=0.
Proof: d1d0=0, d0dag d0=L, d1 d1dag=L; substitution into (3)
gives idempotence and zero product, and (2) gives their sum after
commuting the scalar L through the constant maps. Functional calculus
or the Fourier transform justifies the products on L2. The normalized
map B diag(L^-1/2,L^-1/2) is unitary there.

Thus, for this exact tail, connection/Higgs linear modes separate into
a gauge-complex direction and a residual direction using the derived
operator; no arbitrary middle-plane projector is needed. This is a
conditional reduction of an auxiliary linear decomposition. It does not
supply a physical boundary condition on a cut half-line, eliminate a
physical gaugino, or justify dropping any full-parent field.

## 3. Heat cancellations are controls, not an automatic zero beta function

Per unit length on this homogeneous full line, each scalar L has heat
density H(s)=(4pi s)^-1/2 exp(-s mu^2). Equation (2) gives

  Tr_0 exp(-s Delta0) : Tr_1 exp(-s Delta1) : Tr_2 exp(-s Delta2)
       =1:2:1,
  sum_p (-1)^p Tr_p exp(-s Deltap)=0,
  sum_p (-1)^p p Tr_p exp(-s Deltap)=0.                  (4)

These are exact cochain identities under this convention. They prove
that neither a raw positive fermionic heat trace nor an arbitrary
alternating trace can be labelled a physical gauge threshold. The
actual functional integral has species/real/ghost weights fixed by
the real source action and the gauge-fixing construction, and an
external weak-field insertion couples to their spacetime spin too.
Equation (4) computes neither that insertion nor the full vacuum energy.
Ordinary supersymmetric theories can have nonzero gauge beta functions
even when their uninserted vacuum traces cancel; no contrary claim is
made here. Changing from an internal identity to a charged observable
requires deriving the operator perturbation, not only copying T(R).

The exceptional unpaired source extremes MUST also be retained. In
the preceding weak-weighted histogram, the paired singular-channel
factor and extreme factor separate explicitly as

  F_pair=2e^(-5s/4)+6e^(-9s/4)+6e^(-13s/4)
                  +4e^(-21s/4)+2e^(-25s/4),
  F_ext=6e^(-s/4)+4e^(-9s/4),
  F_pair+F_ext=Fweak.                                    (5)

Their s=0 weights are20 and10, totaling30. These are weak representation
weights, not numbers of particle families or a net index. A paired
1:2:1 argument cannot delete the extremes or assign them an anomaly.
They need the actual scalar/spin slots and boundary/gauge law of the
same complete source before a physical supertrace is assembled.

## 4. Half-line/core domains are part of the calculation

Equations (1)-(2) hold on the common compactly supported core. Their
selfadjoint realizations need boundary conditions such that each map
has the stated adjoint/domain and the complex is respected. Imposing
independent Dirichlet conditions on every degree generally fails this:
a derivative of a Dirichlet function need not be Dirichlet. In the full
programme phase, an artificial end cut must inherit the exterior/core
response already derived from its actual operator, not create a new
physical boundary. A per-unit-length identity is not an identity of
finite or renormalized global heat traces without that domain proof.

A simple analytic determinant control exposes the noncompact issue.
For positive scalar masses mu,nu, on a homogeneous radial line,

  integral_R dp/(2pi) log[(p^2+mu^2)/(p^2+nu^2)]=mu-nu.    (6)

Differentiate in mu: the integrand derivative has integral1, and fix the
constant at mu=nu. The integral is convergent, but it is a difference
PER UNIT LENGTH. Integrating along an infinite tail still diverges when
mu!=nu. A subtraction reference must match the actual asymptotic
charged structures or include an explicitly justified density subtraction.
A gap at zero does not by itself choose the finite subtraction.
This is a scalar determinant control, not the physical loop answer.

At a fixed actual asymptotic background, the compact-core Wilson family
has the SAME tail operators: differences in that family may admit a
relative determinant with appropriate trace-class/zero-mode controls.
Such a determinant could determine a relative Wilson potential or
coupling difference. It would not automatically determine the absolute
4D gauge coupling: a common finite local kinetic normalization can
remain. Proving the relevant relative trace conditions for the actual
full operator is a named duty, not asserted complete by compact support.
The spectrum can have discrete zero crossings even with a fixed gapped
end; split these modes from the heavy determinant rather than continue
through log zero as though it were smooth.

## 5. A precise next source-complete physical packet

The next calculation must use the real source action to derive all
second-order external-background operators about the stationary phase:
connection and reduced scalars, physical spinors, gauge fixing and FP
ghosts, with the exact compact positive pairing and spin/R connection.
Introduce a weak external connection in the unbroken algebra, verify
that its background commutes with the internal vacuum where claimed,
and retain the full curvature coupling to spacetime spin. Recover
(1)-(5) at zero external curvature as exact controls.

Then derive the coefficient quadratic in the external field strength
from the COMBINED trace. Separate zero/light modes and heavy/continuous
spectrum, state physical scales and matching convention, and prove that
the regulator and allowed counterterms preserve the actual gauge law.
The earlier free-word real Hessian has curvature terms; it cannot be
replaced by scalar Laplacians for every component because the end
singular values look similar. Likewise the source seven-dimensional
and ten-dimensional convention/field maps retain their scope; no
new identification is inferred from this cochain calculation.

Before executing a new producer, seal all actual sources and controls,
obtain the required independent review/exact acceptance and use custody.
This note is not such a completed execution package. No past review
is extended by its existence, and no target is used to choose a finite
normalization or correction. Preserve both outcomes if the full charged
trace differs from the suggested coefficient or the determinant retains
a physical input. That is progress toward input reduction, not a reason
to overwrite a failed fit with another assigned correction.

## 6. Dependency account

Derived within the fixed source tail: the cochain gauge/residual
projectors, bosonic cochain Laplacians, paired cancellations and the
separate extreme contribution. Retained physical dependencies: action/
background/metric/domain, real gauge-fixed measure, external-field spin
insertions, compact spectral data and the end/renormalization law.
No SM coupling, three-family spectrum, anomaly cancellation or gravity
is certified. Full generated physical reality remains the goal; a
correct conditional recovery calculation does not complete it.
