# Local cone solutions require the right global holonomy

September 30, 2026. Path-local R65. The existing nonzero normal-helicity
cone family cannot simply be attached to either the two rank-five
monomial families or the canonical rank-four projective family. The
actual peripheral words give different obstructions. A positive abelian
control DOES admit nonzero matching data, and singular transport falls
outside the bounded obstruction. These are necessary matching results,
not a universal cone exclusion or a completed physical model.

**117 exact controls and all eight new tests pass.** The seven-file
combined run has **48 passes and the same four original R63/R64 failed
IDs**. Those failures and their already published repairs remain intact.
The analytic extension is authored analysis, not independent review.

## The actual global data distinguish the cases

Let P be the permutation with images (1,2,0,3,4) in zero-based notation.
Both copied seed families have zero exponent vectors on BOTH marked
peripheral periods for every nonzero complex parameter t. Independent
permutation/exponent arithmetic and dense Laurent matrices agree on
the group relators, periods and actual cover inclusion words.

| Existing family | Meridian and longitude | Consequence for this proposed end |
|---|---|---|
| Rank-five monomial seed 0 on M2 | P, P | Both spectra have unit modulus, excluding nonzero normal X in C_link=wX |
| Rank-five monomial seed 1 on M2 | P, P inverse | The same modulus obstruction, not the same representation |
| Actual M6 pullbacks | I, P or P inverse | Killing meridian holonomy does not kill longitude holonomy; nonzero X remains excluded |
| Canonical rank-four projective family | Meridian has nontrivial Jordan block of size three | It cannot match a normal limiting peripheral pair under bounded radial transport |

The two rank-five families are not relabeled as the rank-four family.
Their existing complete-metric constructions are not invalidated by
failure to match this different end. No physical generation count or
global harmonic PDE claim is imported from the source branch.

## Why logarithm choices and finite covers do not rescue these joins

For each eigenvalue xi of a normal X, the two logarithmic eigenvalue
moduli are Re(w1 xi) and Re(w2 xi). On the square and hexagonal links,
the corresponding real two-by-two maps have determinants 1 and
sqrt(3)/2. Both moduli being one forces xi=0, then X=0 by normality.
This does not choose a principal logarithm. Compatible commuting
unitary twists change phases only; invertible marking changes and
finite-index sublattices preserve the argument.

At X=0, the nontrivial finite peripheral representation can instead be
retained as a flat unitary local system. That is not the untwisted
integer-Fourier problem and does not supply R64's nonzero background.
Vanishing-trace bulk fields are not excluded.

For the projective meridian, the exact arbitrary-power identity keeps
its nonzero nilpotent square. Duality, central twists and finite
peripheral covers do not remove it. A radial coefficient
B/r+O(r^(-1+delta)), with B anti-Hermitian and delta>0, has uniformly
bounded parallel transport and inverse after removing its unitary
part. Such transport cannot make a fixed Jordan part disappear at
the limit. R64's own nonlinear transformation tends to the identity
and therefore preserves its original peripheral conjugacy class.

## The positive control prevents an overwide negative

Take X=2pi i diag(1,0,-1,0,0), and send both generators of the actual
knot presentation to exp(w1 X). The determinant and relator tests pass;
the preferred longitude is I=exp(w2 X). This global abelian SL5
representation matches a nonzero flat and moment-flat local cone end.
It is not an irreducible Standard-Model candidate and does not establish
a global harmonic extension on a chosen metric.

Its nonzero root charges do not enter R63's critical window at the
declared unit-area scale. Their zero-Fourier lower bounds are 8pi squared
and 4sqrt(3)pi squared; nonzero Fourier lower bounds are 2pi squared
and 4pi squared/sqrt(3). All exceed 3/4. Neutral and zero-charge
channels remain. A changed link scale changes this conclusion and must
be treated as a changed physical input. This imaginary-root example
does not reuse R64's real-positive-a nonlinear radial proof.

## A singular limiting matrix can conceal nontrivial holonomy

The logarithmic control G=diag(s^(-1/4),s^(1/4)), s=-log r, sends
I+E12 to I+s^(-1/2)E12. The limit is I, but the holonomy is nontrivial
unipotent at every positive radius. Its radial term is
diag(1,-1)/(4r log r), whose norm is not integrable; its condition
number diverges. It is outside every positive-power remainder class
used in the bounded argument, even though its leading trace vanishes.

Flatness of this control is verified. Moment-flatness, finite action
and physical-domain admission are NOT asserted. This identifies a
precise next test rather than an invented successful escape. A limit
alone cannot be used to erase the global data.

## Provenance and the pre-execution correction

Original seal 22d99b1f3717c40bfde6a0e31e2833aa51a38e03 and execution
revision fd72b0ebacd3c4a13c109c174830fb24ba84acb2 are pushed; the
execution revision was server-confirmed before scientific execution.
Six original science files are unchanged. The revised test and its
explanation are pinned by the second seal. Sixteen source inputs are
pinned; the two data copies are byte-identical to the source commit.

The first governance run added one test-vacuity flag because it did not
follow assertions inside a helper. The command orchestration mistakenly
committed that initial seal after the baseline comparison failed.
No scientific run had occurred. The pre-execution revision adds direct
assertions and corrects the prose file count from seven to six old
files, retaining the exact 44-test population. The revised governance
captures recover precisely the four historical failure rows. Neither
this correction nor the old failures is hidden behind the new passes.

The first inherited custody check also detected a stale ARTIFACT_HASHES
entry for the append-only SEAL_LEDGER. Its diagnostic is retained.
Refreshing that metadata digest does not change any science file; the
corrected custody run is reported separately. Full-suite and independent
review debts remain; this is not a full main-bank certificate.

The corrected inherited custody check verifies 1,021 artifact hashes,
364 latest distinct seal entries and 200 selected relative Markdown
links, retaining the same 24 historical failed/error IDs in its older
population. It does not rerun that old science. The dedicated R65
checker verifies eight frozen paths, sixteen source pins, two received
copies, nine captures and all eleven links from this report.

[Design](CONE_MATCH_DESIGN.md), [pre-execution revision](CONE_MATCH_PREEXEC_REVISION.md),
[authored proof](CONE_MATCH_PROOF.md), [input pins](CONE_MATCH_INPUTS.json),
[topology data](CONE_MATCH_TOPOLOGY.json), [seed data](CONE_MATCH_SEEDS.json),
[producer](cone_match.py), [tests](../../tests/test_physical_bridge_cone_match.py),
[receipts](CONE_MATCH_RECEIPTS.json), [custody checker](cone_match_receipt_check.rb).

## Progress toward the physical mission

This resolves a necessary same-model question before spending more
effort on unmatched local mode counts. It preserves the valid local
and complete-metric positives, while preventing their unsupported join.
Next test actual nilpotent/logarithmic or finite-unitary end data in
the same residual action and common boson/fermion domain. Coordinate
with the existing global-family work rather than repeat its census.
The cone, parent and end law still require physical justification.

The [full mission](PHYSICS_MISSION.md) remains active: a chiral spectrum,
normalized dynamics, quantum consistency, gravitational dynamics and
testable predictions are not supplied by this matching calculation.
