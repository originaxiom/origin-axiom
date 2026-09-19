# Working continuation after R35: the charged overlap, not a density proxy

2026-09-19. UNSEALED ANALYTIC PREPARATION, not an executed R36 result.
Starting checkpoint: `1b7d3b9f19a1d221980ba34b94f032460105cb61`.
The calculations below were worked out by hand during preparation.
They are observed analytic priors for a future seal, not blind forecasts.
No new scientific producer or test has been run. No B number or
physical identification is earned by this note. Preserve it so the
next turn does not lose the reasoning or present it as unanticipated.

## The actual question and the supplied interaction

Continue R29--R34 on fixed compact Q with the absolute outer domain,
positive bulk L2, flat unitary L, bounded finite-width F, and

    Q_q = d_A + q dF wedge,     H0 = Q_q^* Q_q.

For exact normalized scalar eigenfunctions u_i with lambda_i>0 put
v_i=Q_q u_i/sqrt(lambda_i). These are the one-form partners actually
used in R30/R31, not their cutoff trial functions. They describe a
subsector, not every odd/even form in the full kinetic operator.

Keep R33's left-Weyl charges psi=16_1 and chi=conjugate(16)_-1.
The profile of chi is conjugate(u_i), while psi has profile v_i.
Let an ADDED S=10_2 scalar have a normalized internal profile s in
L^2 (here L^2 means tensor square of the line bundle, not the Hilbert
space), with integral |s|^2 dvol=1. Contract equal internal form
degrees by the Riemannian bilinear metric, without conjugating one
argument. Together with R33's epsilon and Y_a this defines a local
gauge- and rotation-invariant candidate interaction.

This form contraction and S profile remain choices. It is NOT yet
derived from the PW superpotential, from a seven-dimensional covariant
source action, or from the object's geometry. The two local coupling
constants need not be equal. Subject to those explicit choices, the
reduced overlap matrices would be

    M_ij = integral s conjugate(u_i) conjugate(u_j) dvol,
    P_ij = integral conjugate(s) g(v_i,v_j) dvol.

The physical couplings include their respective local coefficients.
These bilinears are not integral w |u|^2 or integral w |v|^2.
Replacing them by positive densities loses phases and can change rank.
Their gauge charges cancel pointwise. A constant scalar profile in a
local trivialization is not necessarily a globally parallel section.

## Candidate exact identity for those overlaps

Use Delta=div grad, b=conjugate(s), w_ij=u_i u_j and the induced
connections on L and its tensor powers. In a local unitary frame
D_A=d+iA. The scalar operator is

    H0 = -Delta_A + q^2 |dF|^2 - q Delta F.

The covariant product rule gives, before imposing either eigen-equation,

    g(Q_q u_i,Q_q u_j)
      = div_(2A) [ (1/2) D_(2A)(u_i u_j) + q dF u_i u_j ]
        + (1/2) [u_i H0 u_j + u_j H0 u_i].

On eigenfunctions, two integrations by parts should therefore give

    sqrt(lambda_i lambda_j) P_ij
      = (lambda_i+lambda_j)/2 conjugate(M_ij)
        + integral u_i u_j [ (1/2) Delta_(-2A) b
                            - q <dF,D_(-2A)b> ] dvol
        - (1/2) integral_boundary u_i u_j D_n^(-2A)b darea.

The last term uses the ACTUAL absolute scalar Robin condition
D_n^A u_i + q (partial_n F) u_i=0. It is absent if b is supported
away from the boundary or has vanishing normal covariant derivative,
not merely because the fermions satisfy their Robin condition.
Regularity of b must justify these integrations; a sharp indicator
must instead be treated with its interface/distributional terms.

For comparison, a real neutral weight a and one eigenpair should obey

    lambda integral a (|v|^2-|u|^2)
      = integral |u|^2 [(1/2) Delta a-q <dF,da>]
        - (1/2) integral_boundary (partial_n a)|u|^2.

At a=1 this recovers equality of normalized gauge-current factors,
but not equality of the charged bilinears above. Conversely, the
1/sqrt(lambda_i lambda_j) in the first identity prevents discarding
the derivative/end term without an estimate uniform at small width.
These claims require exact symbolic and boundary controls before
being used as a verified local result.

## Two different controls to prevent opposite false conclusions

### A. No automatic selectivity in a flat, nontrivially twisted comparator

On a length-2pi circle times a unit-area flat two-torus, set F=0 and
A=alpha dx with alpha=1/3. For the constant-transverse modes,

    u_n = exp(i n x)/sqrt(2pi),
    lambda_n=(n+alpha)^2,
    v_n=i sign(n+alpha) u_n dx.

For ANY smooth periodic scalar profile s and any finite set of these
paired modes, direct substitution predicts

    P = -D conjugate(M) D,    D_nn=sign(n+alpha).

Their singular values coincide before the independent local coupling
constants. This is a specified flat control, not m202 or the sourced
F_epsilon family. There is no zero scalar mode at this alpha.
The square bundle has nontrivial holonomy, so a nonzero globally
parallel s is unavailable even though the line bundle is topologically
trivial. Our true order-three characters likewise cannot be replaced
by a parallel charge-two scalar without checking that holonomy.

### B. A prescribed profile can select relatively, without producing a gap

On [0,pi] times a unit-area flat two-torus with A=0,F=0, the absolute
positive pair u=sqrt(2/pi) cos x, v=-sqrt(2/pi) sin x dx has lambda=1.
This trivial-bundle control also has zero modes; it is not a spectrum
census or a proposed replacement for the actual nontrivial line.
Prescribe, rather than solve for, the normalized scalar

    s_t=N_t exp(-t x),  N_t=sqrt(2t/(1-exp(-2pi t))),  t>0.

Straight integration predicts

    M = (2 N_t/pi) (1-exp(-pi t)) (t^2+2)/(t(t^2+4)),
    P = (2 N_t/pi) (1-exp(-pi t)) 2/(t(t^2+4)).

Thus M/P=(t^2+2)/2, but BOTH overlaps tend to zero for fixed local
couplings: M is of order t^(-1/2), P of order t^(-5/2).
The scalar's internal gradient norm squared is t^2. Its nonzero
boundary derivative is precisely a control of the boundary term
in the proposed identity. This s_t is not asserted to solve any
source/scalar boundary problem. A large ratio is not a finite mirror
gap, and prescribing this profile has not derived selectivity.

## What remains before an important probe

The standing compute protocol was reread to its end. The atlas card
was generic; it is not an absence certificate. LAW_MAP, OPEN_LEADS,
the current ladder entries and B960/B1086 kill-graph hatches were
consulted. Those old kills do not establish a no-go for this added
charged interaction. R30/R31/R33/R34 proof bodies were reread fully.
B1036/B1039/B1148 FINDINGS and the located addenda were read; their
cup-product/carrier calculations are not silently identified with the
positive-metric overlap. Selected producer docstrings were inspected,
not those producers rerun in this preparation.

The already-banked query “Yukawa overlap normalized source” gives
166 hits and 13 settled threshold hits. Its full capture is
`oa_r36_banked_first`, exit 1 meaning settled hits, not execution error;
3,280 bytes, SHA256
`c4a16b8e550ba408274431f2cd0a1c19f5a8797900bac75dab926e8cf96ed2fd`.
It prints only its first twelve hits and does not search papers.
Not all settled-hit bodies have yet been read for this proposed probe;
that is an explicit remaining preparation duty, not a novelty claim.
The first guessed query-script path was wrong; the actual script is
scripts/checks/already_banked.py. No absence was inferred.

Before execution: complete the relevant prior-art/body/code reads,
declare the quantifier as this ADDED compact source model and the
named controls, seal a producer/tests/proof/prior with field-normalization
and boundary hypotheses, and push the seal. Test the charged product
rule, both forms of the integration identity, genuine scalar and
fermion normalization, phase covariance, failure when the boundary
term or conjugation is removed, and both controls above. No truncated
count, density overlap or trial-function mass should answer the test.

Most importantly, success of these identities would only give the
correct instrument. The actual duty remains to derive s and its
coupling from the SAME source action, obtain actual global profiles
or bounds strong enough for their overlaps, and demonstrate a
controlled selective quantum phase with the end/anomaly sector.
None of that is finished by this working note or its exact comparators.

## Preparation custody, not scientific validation

The reporting-only checks give 26 governance passes and the same four
failure detail lines as R35; the review counter is 179. The preparation
gate capture `oa_r36_preparation_gates_first` exits 1, 2,095 bytes,
SHA256 `80a63acb476a3ba6d3ba1bdf490a79c5503018cef53e5777384a292e5be2e3d4`.
The cumulative custody capture `oa_r36_preparation_custody_first`
exits 0, 616 bytes, SHA256
`2a9f324fa0b0ee174dd00325ac6dad379aa7e5dbb40c52eddf149561d4040f5b`:
544 artifact paths, 134 latest distinct seals, unchanged R30/R31
science and historical failed/error inventory. Its 113 relative links
belong to this preparation's smaller staged/prior document population,
not R35's different 222-link population. Strict staged whitespace passes.
These checks do not execute or validate the proposed overlap calculation.
