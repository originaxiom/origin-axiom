# Fermion boundary choices on the logarithmic background

Science sealed and executed September 30, 2026; record completed
October 1. Path-local R68 advances the same-action boundary
obligation in [PHYSICS_MISSION](PHYSICS_MISSION.md). The actual
logarithmic connection retains a neutral sector with nonzero apex
boundary data. It does not automatically select a self-adjoint fermion
operator. Explicit reality-compatible linear choices do exist.

The next obstruction is concrete, not an absence claim: complementary
matrix channels source this neutral sector through their bracket.
Their boundary laws must therefore be checked together. No global
particle spectrum or physical chirality follows from this local result.

## What is established on the actual background

The [authored proof](CONE_FERMION_PROOF.md) derives the normalized
matrix-valued differential, its positive-metric formal adjoint and the
full radial form operator. The finite test derives its 32-component
fundamental realization independently from coordinate metric calculus.
The representation formula also applies to the adjoint with its trace
pairing; that transfer is explicitly checked, not inferred from rank.

The radial connection and the derivative of the nilpotent tangential
coefficient are essential to flatness. Treating that coefficient as
constant or deleting the radial part fails the controls. The actual
operator is not replaced by its limiting normal matrix.

For Z=diag(1,-3,1,1), the coefficient projection is

    Pi(X)=Z tr(Z X)/12.

It reduces both the twisted differential and its adjoint exactly at
every positive radius. Z is the unique constant traceless reducing
direction. The holonomy-only commutant instead has three traceless
directions: Z,N,P. Its extra nilpotent directions are not orthogonally
reducing. R66 already knew the commuting matrices; R68 establishes
their operator-domain consequence. R61's complex-line algebra and
R63's radial normalization are reused, not claimed as new general laws.

## A boundary choice survives and linear choices exist

Z-valued harmonic torus one-forms and their radial partners give four
complex apex traces with a nondegenerate Green pairing. Cutoffs of the
constant traces belong to the maximal graph domain but not to the
compact-support closure. Hence the minimal first-order operator is
not self-adjoint at this apex, even if a regular outer boundary
condition is already fixed. This gives a lower bound on the full
boundary data, not a census of the remaining coefficient channels.

On this exact neutral block, every complex line W gives the trace
space W plus its positive Hermitian complement. It is maximal
current-isotropic and invariant under the combined anti-linear
fermion reality map. With separated endpoint conditions, the authored
interval argument proves a self-adjoint block operator. Its closed
differential complex has the usual two linear internal supercharges.

In particular, the distinct lines span(1,-i alpha) and
span(1,+i alpha) both pass. Reality does not mean requiring the line
itself to be real. This is not a full interacting supersymmetry result,
a selected physical handedness, or a self-adjoint/Fredholm certificate
for every coefficient channel. The artificial collar count with the
same line at both ends is paired; it is not a particle count on the
actual global core.

## Why the domains must be tested together

For X=E01 and Y=E10, Pi(X)=Pi(Y)=0 but

    Pi([X,Y])=Z/3.

Thus independent linear sectors are not independent under the actual
nonlinear bracket. A choice for this block cannot simply be combined
with arbitrary choices elsewhere.

A second control separates action admission from fixed holonomy.
Adding c Z dx with real nonzero c keeps both residuals zero but has
divergent L4 norm. It also changes meridian eigenvalues by exp(c) and
exp(-3c), so it is not a fluctuation preserving the fixed peripheral
conjugacy class. L4 is a sufficient nonlinear norm, not a necessary
condition for every zero-action family; zero action is not permission
to change the physical problem.

## Relation to the other branch

The September 30 fetch found no new origin heads. The SM branch was at
67c864c95f89fd7ed81308e06d75b6f315e00b6a. Its B1505 FINDINGS body was
read during the regression run. It studies candidate ambient G2
orbifold links and explicitly restricts its claimed exclusion to a
named class. That claim has not been independently certified by this
probe and is not used as a premise here.

The October 1 fetch advanced that branch to
ad64b558b2e42f14e58347c6bef385114c66aaf0, adding B1506's level/index
analysis. Its sealed design and findings have been read; implementation
inspection is ongoing.
It is received evidence, not independently accepted physical matter,
and does not alter the sealed inputs of this completed calculation.

The duties are complementary: a consistent local gauge-model domain
does not construct its ambient geometry, while a candidate ambient
geometry does not by itself determine the coupled analytic domain.
The supplied action and cone metric remain inputs on this lane.

## Execution and limits

The five science paths were committed, pushed and server-confirmed at
24356ebd541823f7098b82254f281e2e94d206c3 before execution.
See [design](CONE_FERMION_DESIGN.md),
[source pins](CONE_FERMION_INPUTS.json), [producer](cone_fermion.py) and
[tests](../../tests/test_physical_bridge_cone_fermion.py).

The first producer run passes 65/65 exact checks and all eight new
tests pass. The fixed ten-file combined run has 72 passes and the same
four original R63/R64 failures.
No original scientific source or failing old test was edited.

[Receipts](CONE_FERMION_RECEIPTS.json) preserve first outputs, command
arguments, actual exits and hashes for six terminal captures. The
[custody checker](cone_fermion_receipt_check.rb) checks frozen paths,
twelve input pins and exact populations. This is focused verification,
not a full repository suite, independent proof acceptance or main-bank
certification.

The cumulative custody run verifies 1,045 artifact digests, 379 latest
distinct seals and 200 selected legacy relative links, retaining all
24 older failed/error IDs. It does not rerun that scientific suite.
Both governance captures retain 26 PASS rows and the same four historical
failure categories: attribution, test vacuity, seal provenance and relay
debt. The October 1 relay ages advance from 39/35 to 40/36 days;
only those age fields are normalized when comparing captured failure
rows. Historical governance and independent-review debts remain.

Next derive compatible complementary-channel, gauge and full
superfield boundary laws on this same background; then solve the
core matching problem. The full physics mission remains active.
