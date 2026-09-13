# R28 — a stationary bulk field is not yet a dynamical source

2026-09-13. **The prescribed chiral background is a stationary, zero-
potential solution of the adopted twisted bulk theory on the source
complement.** Its source strengths and through-flux parameters are
nevertheless nonnormalizable in that theory's four-dimensional kinetic
metric. Resolving a specified commuting core has a sharp bare cost.
These facts distinguish a useful classical background from a complete
source theory; they neither discard R19's conditional modes nor complete
the physical goal.

Design, proof, producer and tests were sealed and pushed in **b3c7892c**
before first execution. [Design](SOURCE_ACTION_DESIGN.md),
[full argument](SOURCE_ACTION_PROOF.md), [producer](source_action.py),
[prior and branch intake](SOURCE_ACTION_PRIOR.md).

## 1. Which action, and what is now established

The adopted physical framework already has an action: the partially
twisted seven-dimensional Yang--Mills theory. Its Higgs variable is the
adjoint ONE-FORM phi, not the auxiliary potential F. In its commuting
sector, with the form-norm convention including 1/p!, the static term is

    V = (2/g7^2) integral (|d phi|^2+|delta phi|^2+|d W|^2).

This is standard input, not an object-derived action or a measured
coupling. The four-dimensional scalar kinetic term instead contains
(1/g7^2) integral |partial_t phi|^2 for a varying parameter t.
[Braun et al., (2.13), (2.18), (2.22)--(2.24)](https://arxiv.org/pdf/1812.06072).
Their off-shell construction, printed pages 71--73, was also read
directly after execution. It supports the stated bulk functional,
not a derived boundary or source sector.

R15's phi=u dF and commuting flat W set every bulk BPS residual to zero
off the source lines. The potential is zero on every finite excision
and on its open-complement limit. Its first variation vanishes for all
regular compactly supported variations; this follows by differentiating
the residual squares at zero. It is a minimum of this nonnegative bulk
functional, not just a field satisfying an unrelated equation.

That establishes fixed-background STATIC BULK compatibility. It does
not evaluate a delta-function squared on the unexcised space, fix end
variation laws, derive the fermion domain, include defect dynamics, or
prove supersymmetry of an unspecified boundary completion. Rewriting
another action by dropping boundary terms would not discharge those
duties. All admissible prescribed R15 source configurations have this
same zero bulk value, including different source data; this minimization
does not select the desired configuration.

The geometric inverse to a complete G2 construction is also not supplied
by this calculation. The literature's noncompact flavour-source mechanism
is an available framework, not a proof that our sources are those branes.
[Pantev--Wijnholt, section 2.5 and the preceding geometric dictionary](https://arxiv.org/pdf/0905.1968).

## 2. A background can be allowed without its parameters being 4D fields

The exact local geodesic tube has metric

    dr^2+sinh(r)^2 dtheta^2+cosh(r)^2 dell^2,
    phi_r=beta/(sinh(r)cosh(r)).

On a segment of central-axis length L, the kinetic norm of a residue
variation is, to its leading singular part,

    2*pi*L*(delta_beta)^2
       [log(tanh R)-log(tanh epsilon)].

It diverges as 2*pi*L*(delta_beta)^2 log(1/epsilon). Smooth global
correctors cannot cancel that leading term on a compact segment.

In a cusp, write F=V+exp(2s)(bs+c)+v, with torus area A. The L2 harmonic
corrector v has constant torus average; its nonzero Fourier modes have
zero average. Jensen's inequality gives the exact radial lower bound

    ||partial_t phi||^2 >=
      (A/2) [exp(2s)(4(delta_b*s+delta_c)^2+delta_b^2)]_S^R.

It diverges for every nonzero pair (delta_b,delta_c), including a pure
homogeneous through-flux change. If both coefficients vanish, this lower
bound is zero, not a normalizability certificate for all other variations.
The tube calculation separately detects nonzero individual residues,
even when their cusp totals cancel.

Multiply these formulas by the positive algebra norm |u|^2/g7^2 for
the physical kinetic coefficient. Compact gauge compensation cannot
remove their Cartan component: <u,[epsilon,u]>=0. The explicit matrix
control makes the compensated norm larger, not smaller.

Thus, in this FIXED metric/action, these parameters are frozen end/source
data, not ordinary finite-kinetic-norm four-dimensional scalar moduli.
This does not forbid the static backgrounds, exclude new boundary kinetic
terms, or settle a gravitational/UV renormalization. Smooth compactly
supported fluctuations are finite-norm controls. A harmonic constant
one-form on a compact torus has both zero potential and finite norm:
zero potential does not force the divergent-norm conclusion.

## 3. A sharp local constraint on resolving the source

Consider a geodesic cylinder of radius epsilon, length L, fixed total
radial flux 2*pi*L*beta and ZERO axial-cap flux. Its volume is
pi*L*sinh(epsilon)^2. For a smooth commuting core in the unshifted bulk
theory, Stokes and Cauchy--Schwarz give

    integral_core |div phi|^2 >=
        4*pi*L*beta^2/sinh(epsilon)^2.

This is a bound on the bare D-residual, before the positive action and
algebra factors. It applies to the stated flux/cap/commuting class,
not every possible resolution. The explicit core

    phi_r=beta*tanh(r)/sinh(epsilon)^2

attains it, is regular at the axis, has constant divergence
2*beta/sinh(epsilon)^2 and matches the exterior value at the side.
The joined field is continuous and piecewise smooth, not globally
C-infinity. A same-flux nonuniform profile costs a factor 1+kappa^2/3,
providing a strict sharpness control. Zero beta removes the cost.

For nonzero beta the lower bound grows as epsilon^-2. A bounded-cost
zero-radius completion cannot therefore use only this bare commuting
D-square with those fluxes. It must change a declared input: source
moment map, boundary subtraction, core/field theory, cap flux or finite
radius. This is not a universal defect kill.

The opposite control is constructive: a PRESCRIBED external density
rho changes the residual to delta phi+rho. The displayed core has zero
shifted residual for rho=2*beta/sinh(epsilon)^2. That is a stationary
minimum of a changed, regulated source functional; rho is still input,
not a source field derived from the object. Both outcomes are retained.

An independent check also prevents a false shortcut in the other
direction. The tube has nonzero rough derivative energy, but the exact
metric-derived Hessian and Ricci tensor satisfy

    w*(|Hess F|^2-2|dF|^2) = (w*F'*F'')',
    w=sinh(r)cosh(r).

The integrated rough-plus-curvature expression is a boundary term;
the actual Hodge residual is zero. Dropping the boundary and curvature
pieces and declaring the static background infinitely energetic would
test a different functional.

## 4. The new “no action” claim also needs its scope

The new paper-review B1341 establishes the trace map's anti-Poisson
property, but expands a regular autonomous discrete-Lagrangian argument
into a statement that its half-step has NO stationary action. That
expansion fails. The valid restricted obstruction is retained.
[Received statement, fixed commit](https://github.com/originaxiom/origin-axiom/blob/f52e7e6f82a1c738c79afbabebcbd56fbb5dfa1e/frontier/B1341_the_action_of_the_object/FINDINGS.md).

Three independent exact checks distinguish the claims:

- A regular autonomous DEL map preserves its L_12-dependent area form;
  its coordinate Jacobian need not equal one. L(a,b)=exp(a)*b gives
  (a,b) -> (b,-exp(a-b)), with Jacobian exp(a-b), preserving that form.
- The regular TIME-DEPENDENT action
  L_n(a,b)=(-1)^n*(a*b-a^2/2) has DEL equation c-b-a=0, the actual
  Fibonacci half-step. Removing the alternating sign fails.
- For the FULL nonlinear map, the enlarged multiplier action
  sum p_(n+1).(x_(n+1)-T(x_n)) gives the map and its cotangent recurrence.
  Every orbit lifts with p=0, including the actual Markov leaf.

These are stationary actions, not minima, regular autonomous actions on
the original state alone, or physical field dynamics. The trace-map
invariant, anti-Poisson identity and exact half-step conjugacy all pass.
Its square remains the geometric monodromy. A properly scoped
same-state autonomous obstruction stands; unrestricted action existence
does not itself select a physical clock.

This is a standard-action-class correction, not a novel theory or a
retraction of the useful monodromy mathematics.

## 5. Mission movement and the next discriminating construction

The stationary BULK sub-duty is now established in the adopted fixed-data
theory. The coupled physical source/end sub-duty is not. This result
refines the earlier task; it does not revive the nonstationary R26 bump
as a solution or claim that a spectral index solves field equations.

R19's conditional three/zero charged kernel remains on its original
strong maximal domain. R26's perturbative stability does not license
changing singular end data or the domain; the divergent parameter
directions above are not compactly supported perturbations. Freezing
source parameters also does not remove the extra U(1) gauge symmetry:
an internally constant transformation commuting with u preserves those
data. Its standalone four-dimensional anomaly remains the R19/R23 duty,
not cancelled by this classical energy calculation.

NEXT: specify one gauge-covariant source/end functional. State its
regulator/counterterms, allowed end gauge transformations and which
fields generate its moment-map density. Derive its boundary/defect
equations; then test the resulting background and fermion domain
against R18/R19/R26 and compute its FULL gauge anomaly and spectrum.
An external density is a useful reference control, not the answer.
Nonabelian cores, genuinely dynamical end fields and compatible massive-
U1 mechanisms remain live, subject to the same global-form constraints.

Source activation/count selection, the neutral four-dimensional limit,
SM breaking, gravity and empirical predictions remain distinct tasks.
There is no complete physical TOE or defensible completion probability
in this round.

## 6. Verification and custody

The native first run exits zero in 8.507 s: all 27 exact identity and
scope controls pass. The 20 new tests plus R26's 13 give **33 passed**
in 76.43 s. First outputs: [native](SOURCE_ACTION_NATIVE_FIRST.json),
[focused](SOURCE_ACTION_FOCUSED_FIRST.txt). No scientific source,
proof, design or test was changed after the seal.

The 50-file regression is the EXACT R27 population plus the new test
file: **404 passed, 16 failed, 8 errors**, one optional-GUI warning,
365.51 s, exit one. Its 24 distinct failed/error IDs are exactly R27's:
zero added and zero missing. No old assertion, failure, tolerance or
baseline was changed. [Complete regression](SOURCE_ACTION_REGRESSION.txt).
This is not the full-repository suite or an all-green result.

The [run receipts](SOURCE_ACTION_RUN_RECEIPTS.json) preserve exit
statuses, timing, command populations and original digests. Public
copies redact environment prefixes only; the raw captures remain
byte-faithfully outside the repository. The full history receipt is
likewise retained with its digest and a public population summary.

The [reporting check](SOURCE_ACTION_FINAL_CHECKS.txt) has **26 passing
gates and four failing gates**. The three older failure detail strings
are unchanged. The additional relay-debt failure is date-dependent:
`CC_TO_CC3_2026-08-22_NEEDS_SPECIALIST_LIT_SEARCH.md` crossed the 21-day
open-debt threshold. Its main-owned reading duty is not closed here.
Review is also due at 151 merges. No baseline, clock or disposition was
changed to hide either duty.

All 62 recorded design seals match. The pre-receipt artifact manifest
has 378 paths with zero mismatches; all 215 checked local links resolve.
The final receipt and updated reporting hashes are rechecked before
commit. No green or independent acceptance is inferred from these checks.

This is a pushed local research checkpoint, not an independent banking
review, main merge, full-repository green certificate or completed goal.
No reserved B number, PR or external relay is used.
