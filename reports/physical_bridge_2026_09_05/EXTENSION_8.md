# R10 — finite hard alignment and the induced weak triplet

STATUS 2026-09-06: design before the first execution of this instrument.

BANKED IDENTITY: R4--R9 are conditional calculations in the specified
compact-E6, four-scalar-27 plus real adjoint, one-Weyl-27 action. R8 has
the complete leading 19-field EFT; R9 has the exact neutral-favoring
infrared logarithm. Neither is a finite-matching or source/action theorem.
Their sealed bytes, successes, smaller fermion mass and failures remain.

PRIOR ART: fetch now reaches origin/main 69a027eb, ten heads. The regex
`finite.hard|triplet.relax|normal.response|vacuum.alignment|Higgs` is PRESENT
on all ten heads, zero matching deleted paths (not deleted-content absence).
Already-banked terms `finite hard Higgs alignment triplet`: 135 hits, zero
settled arcs matching three of five terms. The two three-term OPEN bodies,
B1206 and B1229, were read completely: tensor-slot counting and a boundary
consistency programme, not this action's finite loop coefficient. Targeted
remote source hits retain B962's literature and B889's frame alignment.
The latest embedding-selector claims are fetched/read as claims, not
merged or counted as independently reproduced. No global absence claim.

Grounding: WORKING_RULES, COMPUTE_THE_PROGRAM, THE_LADDER, THE_FRAMEWORK,
THE_CAMPAIGN read; atlas card, law/lead and kill-graph searches performed.
This follows PB-VACUUM's priced finite task, not a reopening of the older
tensor doublet-existence result or a measurement/value crossing.

P0: compute over the existing chosen action and its fixed high-scale
branch, not the full relational object or all E6 theories. The overall TOE
goal remains uncompleted. No prior on the sign of the finite coefficient;
R9's logarithmic sign is an input, not the answer to this question.

## Renormalization specification and power counting

Use the inherited four-dimensional Landau-gauge one-loop MS-bar potential:
scalar/Weyl/vector weights 1,-2,3 and constants 3/2,3/2,5/6. At the matching
scale mu=sqrt(epsilon), the RENORMALIZED potential equals the stated R7
positive-square polynomial; coefficients of other symmetry-allowed local
operators are set to zero at that scale. This explicitly completes a
boundary prescription that R9 left uncomputed: it is a chosen input, not
a derivation, an RG-stable relation or freedom to tune after execution.
Kinetic and common Yukawa conventions stay pinned. No measured data enter.

Scale all tree coefficients by epsilon and gauge/Yukawa couplings by
sqrt(epsilon), as before; H=sqrt(epsilon)*h, T=epsilon*t. The one-loop
hard determinant is epsilon^2 F_hard(H,T), with masses selected by
continuation from the 209/10/66 positive scalar/Weyl/vector eigenvalues.
The light eigenvalues are EXCLUDED ONLY from this hard determinant; R9's
complete resummed soft determinant is added separately, once.

On the pure-Higgs slice z0+H the tree heavy normal force vanishes, not
merely its leading quadratic term; verify against all 209 positive modes.
The hard quartic on this slice contributes epsilon^4 cB*rU*rD*eta.
The triplet source at the same energy order has TWO pieces: the hard
one-loop cubic T H^2 and the tree quartic delta0*T*H^2 induced by R7's
epsilon*delta0 normal shift. R8 already provides its resummed stiffness
K_T = kappa_T + .02*(rU+rD)/6. Therefore minimizing this triplet piece
adds -epsilon^4*norm(J_T(h))^2/(2*K_T), and T/epsilon=-J_T/K_T.

The zero-momentum hard/soft decomposition needs the heavy stationary
condition, not deletion of heavy fields: Manohar/Nardoni 2010.15806,
sections 2.3--2.4, Eq. (2.17); R9's hard-resummation references remain.
This cell computes the named finite pieces and their combined truncated
orientation curve. It does not certify all higher-loop matching, a
finite-epsilon full vacuum, pole masses, branch-global stability, gauge-
independent observables, a 4d physical dictionary or a TOE.

## Numerical extraction, independent checks and failure conditions

For H=t*h_eta with eta=0,.1,.25,.5,.75,.9,1, use
t=.08,.064,.05,.04,.032,.0256. Build full Hermitian mass polynomials
M0+t*M1+t^2*M2 from the unchanged analytic derivatives. Check them against
direct full matrices at displaced fields. Require the selected hard
eigenvalues positive, the excluded eigenvalues below .85 times the hard
gap, and return both sets' extrema; do not take abs of negative masses.
Non-Hermitian, non-finite, wrong-count and failed-gap controls must error.

Primary quartic estimator: the neutral-minus-charged radial hard gradient
divided by 4*t^3*rU*rD. Independent estimator: corresponding potential
difference divided by t^4*rU*rD. Fit a quadratic in t^2, compare cubic fit
and a fit excluding the largest step; the smallest step is a holdout.
No fit is to measured data. Agreement tolerance for cB is 2e-5, with all
raw estimates and fitted values retained. No physics verdict if this
resolution cannot determine a sign. Synthetic known-polynomial and
deliberately corrupted extraction controls run before model extraction.

For each triplet generator differentiate the actual hard determinant,
subtract the base source and divide by t^2; same step/extrapolation checks
with tolerance 2e-6. Obtain the normal-shift contribution independently
from the exact cubic tree gradient (constraint/Jacobian polarization),
then verify it by a mixed odd/even finite difference, tolerance 2e-8.

Fit the two allowed triplet-Higgs bilinears U^dagger A_T U and
D^dagger A_T D; verify the other five angles against the fitted form
(2e-6). Verify their all-field Fierz identities symbolically, including
nU*nD=(rhoU*rhoD-2*abs(B)^2)/12. This establishes an orientation-linear
triplet relaxation term, with coefficient fU*fD/(6*K_T). Keep its two
source pieces separate; omitting either is a labelled control, never a
changed model. Check all eight color-octet source components vanish at
the neutral test background, including the normal piece (2e-8).

Assemble the seven-angle order-epsilon^4 curve at R9's four epsilons from
its exact logarithm, full finite soft difference, measured hard quartic
and triplet relaxation. Report every term and the numerical resolution;
an endpoint comparison or seven-angle grid is not a proof of a global
minimum. R9's asymptotic positive result is not withdrawn by a competing
finite term, and a finite positive result does not derive any model input.

Seal design, source and tests with hashes and a local commit before first
execution. Serialize before exclusive output open; refuse overwrite;
preserve failed runs and sealed sources; remain quiescent during runs.
