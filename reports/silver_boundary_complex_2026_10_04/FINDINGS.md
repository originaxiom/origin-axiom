# The silver degree one positive survives one full boundary completion

October 4, 2026. The cone-shaped finite cochain completion preserves the
previous interior degree-one pair (-1,-1) on all four silver candidates.
It also retains nonzero degree-zero and degree-three classes in the
fundamental sector. Counting all odd versus even degrees gives (0,-1),
not the degree-one pair. Neither count is yet a derived physical spectrum.

The native run passes unchanged on seal da9628c7450380cbac30cfe9fadf0a616f61af8e.
All **13 focused tests pass in 50.67 seconds**: seven new tests and six
retained normal-response tests. There were no scientific failures, repairs
or source edits during the tests. This is a fork-local result, not a
full-repository, independent analytic or shared-bank certificate.

## What was computed

The exact producer reconstructs the four marked silver coefficients,
their literal duals, exterior squares and split comparators. It adds an
explicit degree-two boundary restriction derived from the mapping-torus
relator identity. The chain identity is checked on every cochain, and
the induced H2 restriction ranks are computed, not supplied by duality.
The m135/m136 names are the saved carrier labels; this run does not
independently certify their SnapPy census identification or geometry.

The same chosen degree-one complement L is then completed in two ways:

| Attached boundary cohomology in degrees 0, 1, 2 | H1 differences on W and exterior-square W | Total odd-minus-even on W and exterior-square W |
|---|---|---|
| Cone-shaped (H0, L, 0) | (-1,-1) | (0,-1) |
| Reversed endpoint (0, L, H2) | (0,-1) | (0,-1) |

Every entry in this table holds for each of the four nonsplit inputs.
All corresponding split differences and alternating counts are zero.
The complex is the full homotopy fiber of C(X) plus the attached boundary
subcomplex mapping to C(T). Its boundary cochains are retained. On the
dual side L is replaced by its full cup annihilator, not an independently
chosen Hermitian complement.

For the cone-shaped completion the actual nonsplit cohomology is identical
for all four candidates:

| Coefficient | H0 | H1 | H2 | H3 |
|---|---|---|---|---|
| W | 0 | 0 | 1 | 1 |
| W dual | 1 | 1 | 0 | 0 |
| Exterior-square W | 0 | 0 | 1 | 0 |
| Exterior-square W dual | 0 | 1 | 0 | 0 |

Both chosen completions satisfy the degree-reversed dual dimension check.
The total alternating counts agree with the alternating chain dimensions.
Changing to a tilted complement on the first nonsplit candidate preserves
every reported dimension in both sectors. Wrong-sign restriction and
broken-chain-map controls fail as intended.

## The positive and the limitation are different statements

B1509 Proposition E already proves the degree-one complement formula.
This test supplies its complete finite-complex realization on the silver
inputs, with the previously unused two-cell restriction and end degrees.
The positive is therefore retained rather than dismissed as inherently
incompatible with a cochain completion.

The reversed endpoint model alone would have changed the degree-one
fundamental count to zero. Its extra classes are the cokernel of global
H0 restriction to boundary H0. Attaching the boundary H0 instead removes
those connecting classes; the cone-shaped model then recovers the original
H1 count. The opposite controls demonstrate both mechanisms. This is why
one cannot select an endpoint convention silently and use its answer as a
universal chirality kill.

The converse error would be to drop the surviving H0 and H3 and advertise
the cone-shaped H1 result as a physical generation. The adopted literature
dictionary includes fermions in all four degrees: its H1 and H3 have one
Weyl chirality, H0 and H2 the other. This follows from the equations and
Hodge dualization in [Braun et al., sections 2.3 and 2.4](https://arxiv.org/html/1812.06072v2).
Applying that dictionary here still requires an actual analytic domain
and its adjoint/reality maps. The finite model has not supplied them.
Ordinary flat H0 is not automatically a physical vector, a ghost, or an
expendable mode; R40 COEFFICIENT_PARENT already makes that distinction.

## What remains conditional

The cone-shaped pattern is motivated by [ALMP Proposition 7.1](https://arxiv.org/html/1307.5473v3),
not certified by it for the actual nonunitary coefficient and metric.
Neither of our two algebraic models is proved to be the physical cusp
domain, a Cheeger ideal domain for this bundle, or an OA-selected end law.
No global chain pairing, positive continuum realization, Fredholm property,
spectral gap, bosonic boundary equation or interaction closure is inferred
from a match of finite dimensions. The supplied metric and global
complement remain inputs.

Prior credit matters: R30 RESOLVED_FERMION_PROOF already constructs a
mapping-cone attachment and its compensating core states. R61 FERMION_END
already distinguishes combined fermion reality from imposing conjugation
and Hodge star independently. Those mechanisms are reused, not rediscovered.
Their reports and R40 were reread, without rerunning their foreign producers.
No additional branch outcome or missing-work claim was inferred this turn.

## Next physical test

The actionable next step is the common-parent boundary problem, not another
search for a favorable isolated count. Read the existing R59 nonlinear
tensor maps and R61 variation conditions against these actual trace spaces.
Then test the same parent's bracket/tensor couplings, gauge transformations
and reality operation together, including the degree-zero sector.
Independent projectors for W and its exterior square are not a derived
interacting theory even when both individual counts look favorable.

A successful completion must derive or explicitly price its end law,
admit the background under the same action, and compute its full charged
spectrum and anomalies. If this supplied complement fails that test,
preserve its exact algebraic result and identify the precise failed
condition; do not extend it to all singular or interacting completions.
The full parameter-free Standard Model and physical-theory goal is still
unachieved. No three-generation, observable-value or gravity claim follows.

Evidence: [design](PREREGISTRATION.md), [argument](PROOF.md),
[producer](verify.py), [tests](test_verify.py),
[native capture](NATIVE_FIRST.jsonl), [focused capture](FOCUSED_FIRST.txt),
[receipt](EXECUTION_RECEIPT.json).
