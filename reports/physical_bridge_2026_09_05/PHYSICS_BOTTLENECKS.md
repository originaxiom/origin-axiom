# Biggest bottlenecks toward physics: a scoped strategy

2026-09-08, updated after R19 and the named partial-filling verification.
This ranks remaining duties of the constructions audited here. It is
not a theorem that the repository, its other branches, or the object
cannot supply them. All remote heads were fetched again; latest main
c78003cd, physics 659487bb, SM d1a91c7a, outside-bench 8a5d6e6f.
Newer received conclusions are not accepted merely because fetched.

## 1. A common physical theory and its genuine inputs

**Asset:** R4--R10 are an executable four-dimensional compact-E6 model:
a classical SM stabilizer, masses and quantum alignment effects.
R11 supplies an actual family action, not just a matching group name.
The repository also has genuine 3d action/state-integral and 4d duality
constructions. "No action" or "no physics" would erase actual work.

**Bottleneck:** the tested R4 action explicitly chooses Lorentzian 4d
spacetime, compact real form, field content, family number, coefficients
and scales. R14--R19 choose a sourced twisted-reduction background,
parent adjoint, maximal domain and now a flat connection. R19 shows
that nonzero abelian holonomy deformations are non-normalizable boundary
data in the canonical metric. The partial filling chooses a marked cover/cusp/slope.
Combining their headlines is not yet one theory deriving those choices.

**Strategy:** list the actual maps from source data to fields, kinetic
terms, interactions, boundary data and observables. For each apparent
choice, quotient by gauge/field redefinitions FIRST. B1232's recovered
third column is essential: an unselected representative need not be a
physical parameter. For choices that survive in normalized observables,
either derive a selection principle, or price them as inputs of a
conditional physical theory. Inputs do not prevent physics; they prevent
calling that theory uniquely derived from the source.

**Success test:** one declared action, domain and observable dictionary
reproduces the claimed gauge/matter/gravity constructions without
switching incompatible parents, real forms or manifolds between steps.
Its remaining observable input count is explicit, not assumed zero.
Source: [R4 action](VACUUM_MODEL.md), [R11](FAMILY_ACTION.md),
[B1232](../../frontier/B1232_codex_r031_verified_and_three_columns/FINDINGS.md).

## 2. Physical chirality: the complete charged operator

**Asset:** the annular case is understood; the singular route is not
killed by it. R15 gives a global prescribed background and full finite
four/one cohomology. R16 derives the local amplitude-dependent trace
criterion. R17 supplies a uniform charged cusp-tail energy barrier
for a fixed tangential Hilbert complex, including puncture concentration.
R18 now establishes closed range and complete normalizable four/one
cohomology in the specified maximal complex when every abs(q)*beta_a>=1,
under R15's three-arc hypotheses at trivial gauge transport. R19 extends
this to flat unitary transport: the exact Alexander polynomial gives
three/zero at generic holonomy, with four/one retained at the trivial
and explicit exceptional characters. Separately, the partial filling is
certified geometrically chiral with two complete cusps.

**Bottleneck:** geometric chirality, a relative Euler characteristic,
finite cohomology and normalizable four-dimensional chiral fermions
are distinct. The physical defect/domain law and the joint cusp/line
limit must connect them. At weak effective charge, L2 alone demonstrably
does not choose the domain. R18 supplies the previously owed global
comparison in the declared strong maximal class. Its complete kernel
does not select that class physically. R19 removes the extra pair in
an explicitly changed flat background, not by deriving that background.
The net-three extra-U(1) anomaly remains unchanged. The neutral cusp
low-energy channel also remains: a finite charged kernel is not a
decoupling theorem for a finite four-dimensional effective theory.

**Strategy:** keep the sourced m202 path as the immediate calculational
priority. Compute which flat characters the actual source symmetries
permit, with the compact gauge lift and its charge lattice retained.
Derive the defect boundary condition, including a=q beta, and determine
whether it selects this strong maximal class or another domain. Then
construct the required anomaly/inflow or massive-U(1) mechanism from
actual source fields in the same action, not from the label "E6".
Check the neutral-sector 4D limit and physical Lorentz/gauge assignment.
An arbitrary pair mass inside the unchanged W=0 operator is not R19's
mechanism, and no physical mass scale has been obtained. Compact resolvent was not needed
for R18's closed-range proof and is not silently claimed.

**Success test:** a cutoff-independent normalizable charged spectrum,
with correct physical chirality and identified gauge representations,
not just net Euler three. A failure in one amplitude/domain class
closes that class, not all singular or cusped backgrounds.
Sources: [R15](GLOBAL_SINGULAR.md), [R16](CHARGED_DOMAIN.md),
[R17](CUSP_TAIL.md), [R18](WEIGHTED_COHOMOLOGY.md),
[R19](HOLONOMY_SPECTRUM.md).

## 3. Gravity in the same four-dimensional dynamical theory

**Asset:** genuine hyperbolic Einstein geometry, 3d CS/state-integral
content, spin-two representation slots and the earned principal-CS
containment. The old attached 122-order Lambda "miss" was withdrawn
for a concrete wrong identification; it is not reinstated here.

**Bottleneck:** these audited results do not by themselves give a
propagating, positive-norm four-dimensional massless graviton with
universal coupling to the matter theory above. Containment of a spin-two
sector is not equality of full theories or a physical propagator.

**Strategy:** declare a concrete reduction/emergence hypothesis and
derive its quadratic action and constraints. Count physical modes,
test kinetic signs, and derive the coupling to the common stress tensor.
Compute the effective Einstein coefficient and cosmological term in
that same normalization before addressing their measured values.
Quantum consistency/UV completion remains a separate higher bar.

**Success test:** an explicit common low-energy gravity-plus-matter
action with the correct propagating graviton and controlled unwanted
modes. Then a quantum consistency argument; no dimension/level
identifications borrowed from a different construction.
Sources: [recovered scopes](RECOVERED_PHYSICAL_STEPS.md),
[B980](../../frontier/B980_k3_conflation/FINDINGS.md),
[identification ledger I-15/I-19](../../docs/IDENTIFICATION_LEDGER.md).

## 4. A predictive physical quantity, with an honest input budget

**Asset:** exact charge/cubic data, conditional mass/threshold
calculations and the repaired gauge-crossing instrument.
The historical 16-sigma assertion is not a calibrated global exclusion.

**Bottleneck:** a compatible group or trace ratio does not automatically
produce a distinctive measured coupling or mass. Hypercharge
normalization, physical charge identification, scales, thresholds and
flavor data must be handled consistently; matching an adjustable target
does not test the source.

**Strategy:** after canonical normalization, map the genuine surviving
inputs to invariant observables and identify relations insensitive to
those inputs. Select one discriminating dimensionless relation not used
to choose parameters, propagate controlled approximation/threshold
uncertainties, and compare against both observations and alternative
constructions. A predictive effective theory is a worthwhile physics
milestone even before every input is derived or a TOE is established.

**Success test:** at least one independently reproducible, falsifiable
physical consequence beyond fitted inputs; later broaden to flavor,
mixing, neutrinos and cosmology. This is a strategy, not a promised result.
Sources: [physical model](PHYSICAL_MODEL.md), [audit](AUDIT.md),
[I-23](../../docs/IDENTIFICATION_LEDGER.md).

## 5. Cumulative verification without false closure

**Asset:** seals, preserved failures, actual producers and explicit
scope corrections already exist. The current successful interval
certificate and 29 focused passing checks are durable receipts.

**Bottleneck:** a scope change in summaries can still throw away a live
route, while nominal positives can omit the map needed for composition.
Fresh example: outside-bench 879869ca's producer tests covers only through
degree 12. Even granting its census, it does not exclude higher degrees,
nor prove central charge six requires six geometric cusps. The reported
route-wide kill is not licensed. This is a logical scope finding, not
a rerun of that census.

**Strategy:** every important claim keeps object/domain, actual input
choices, producing code, exact or interval certificate, two-sided
controls, and downstream maps beside it. Preserve and classify
instrument failures separately from mathematical counterexamples.
Use whole-branch/history retrieval before universal absence language.

**Success test:** a new reader can reproduce both the positive and the
negative within their stated domain and can see precisely which next
claim they license. Full-suite and independent banking debts are not
hidden by a green focused subset.

## Immediate order, preserving both live paths

1. Carry R19's complete conditional three/zero generic-holonomy kernel
   into the source/amplitude/defect/fibre derivation. Compute source-
   symmetry-compatible flat choices and the actual anomaly/extra-U(1)
   completion in that same action. Retain R18 at trivial holonomy and
   R19's nontrivial exceptional locus. The strong maximal cohomology
   join is supplied; do not restart from another Euler argument or
   call a non-normalizable Wilson parameter a selected physical modulus.
2. On the certified partial filling, construct the actual boundary
   sector and its level/anomalies/partition function. Nonzero CS(M)
   alone neither fixes k nor identifies the desired c=6 theory.
   Establish any map carrying the arithmetic/gauge/family data through
   the filling before composing this path with other results.
3. Reduce both to a common explicit input-to-observable account,
   then earn a discriminating prediction and the common gravity sector.

These are bounded research targets with honest failure outcomes, not
a guarantee that the present axioms yield a complete TOE. The goal
remains active; mathematical and conditional-physics progress is retained.

## Retrieval scope for this assessment

The required already-banked queries were run on "physical action selection",
"normalizable chirality domain", "four dimensional gravity", and
"predictivity normalization". They returned existing work, not a blank
slate. Flagged B1232, B1105 and B1194 bodies were read, together with
the actual local producers, input ledger, ladder/framework, B139 and
the incoming degree-bounded producer. Earlier complete cross-branch
sweeps and the current R16 search receipts are retained.

This status assessment does not claim an exhaustive new re-certification
of every arc or every newly fetched branch; statements of an unpaid
requirement are scoped to the audited construction.
