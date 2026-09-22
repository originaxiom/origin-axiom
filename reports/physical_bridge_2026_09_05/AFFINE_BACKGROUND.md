# R42: a complete finite-energy background on the canonical projective metric

Science executed September 21; report completed September 22, 2026.
Own branch audit/physical-bridge-2026-09-05. No shared B allocation.

## Outcome and verification grade

There is a positive mathematical bridge for the chosen properly convex
projective structure: its complete Blaschke metric and canonical positive
coefficient metric solve the full adopted harmonic-flat gauge equations.
Finite Hilbert volume implies finite positive Higgs norm. This applies
to the actual defining-four holonomy of Ballas' nearby projective family
and its finite covers, without a scalar repair of the linear bundle.

The all-dimensional existence/harmonicity inputs are credited to the
literature, not claimed as discoveries. Global descent and the finite-
energy consequence are an authored application with stated hypotheses;
the finite symbolic checks are not an independent analytic certification.
The geometry chooses the metric CONDITIONAL ON a projective structure.
Neither that structure nor its deformation parameter has been selected
by physical dynamics here.

**The change is the BASE METRIC.** The fixed-hyperbolic-base infinite-
norm result from F10 remains true. A positive result on a different
metric is not a coefficient-gauge repair or a refutation of F10.
Nor can R40's chiral interior index be carried onto this different
flat bundle. Physical chirality and the complete TOE remain unproved.

Sources and reproducibility: [sealed design](AFFINE_BACKGROUND_DESIGN.md),
[authored proof](AFFINE_BACKGROUND_PROOF.md),
[prior and primary reading scopes](AFFINE_BACKGROUND_PRIOR.md),
[frozen inputs](AFFINE_BACKGROUND_INPUTS.json),
[receipt inventory](AFFINE_BACKGROUND_RECEIPTS.json),
[original producer](affine_background.py), and
[separately sealed Ricci diagnostic](AFFINE_RICCI_CONTROL_V2_DESIGN.md).

## 1. The construction and the exact content of the advance

For an oriented properly convex n-manifold, the normalized affine sphere
identifies the actual cone-holonomy bundle with R direct-sum TM. Write
K=nabla^B-nabla^h and C(X,Y,Z)=h(K_X Y,Z). In this splitting,

    H = 1 direct-sum h,
    A = diag(d,nabla^h),
    Psi_X = [[0,X^flat],[X,K_X]],
    D=A+Psi.

H is positive and has determinant one relative to the flat volume.
The trace-free symmetric cubic and its Codazzi equation give

    F_A+Psi wedge Psi=0,   d_A Psi=0,   d_A^* Psi=0.

These are all endomorphism-valued equations, not only their central
projection. The positive defining-trace norm satisfies

    |Psi|^2 = 2n+|C|^2.

Pointed-domain projective compactness and all-jet continuity bound
|C| uniformly in each dimension. General-dimensional volume comparison
then gives finite integral |Psi|^2 for finite-Hilbert-volume quotients.
No fitted profile, sharp numerical cubic constant or numerical global
PDE solve enters. The proof explicitly separates the all-n results
from surface-only holomorphic-cubic statements in the same papers.

In dimension three the quadric comparator has norm density 6. An
explicit nonquadric simplex comparator has cubic norm squared 6 and
Higgs norm density 12; its immersion, volume normalization and flat
connection are checked. The simplex is a control, NOT a claimed
formula for Ballas' actual developing domain or Blaschke metric.

The internal curvature relation is also exact:

    Ric_h(X,Y) = tr(Psi_X Psi_Y)-(n+1)h(X,Y).

This is a Riemannian affine-sphere identity. Calling it a derived
four-dimensional Einstein equation or cosmological constant would
be an unearned physical identification.

## 2. The actual representation and the end change

The literal Ballas SL4 generators are unipotent. A unipotent generator
cannot interchange the positive and negative cones: a positive linear
functional applied to its integer powers would alternate sign, whereas
those powers are polynomial in the exponent. Thus the canonical cone
lift is the actual given linear lift, not a projectively equivalent
representation with altered determinant or central character.

The literal longitude word has characteristic polynomial
(X-q)^3(X-q^-3) and trace difference

    tr Lambda-tr Lambda^-1 = -(q-q^-1)^3.

For positive q different from one, this forbids same-base invertible
flat linear and antilinear maps to the dual. It does not forbid all
spectral pairings or prove a chiral fermion spectrum. At q=1 the
coefficient is the previously checked balanced geometric four, not
the holomorphic Sym3 used elsewhere. Geometric existence is only
claimed in the nearby family established by Ballas, even though
the rational matrix identities hold more widely.

F10's off-unit-holonomy lower bound forces infinite positive Higgs norm
on the fixed complete hyperbolic base for EVERY positive coefficient
metric. The Blaschke solution therefore cannot be globally uniformly
equivalent to that base when q differs from one. The cusp geometry
has materially changed. Finite Hilbert volume alone did not prove
this result; the affine-sphere construction and norm estimate did.

F10's whole-boundary acyclicity and ordinary dual-sector H1 equality
are topological statements and are retained. Whether ordinary
cohomology describes the physical L2 modes on this NEW metric needs
its own proof with all form degrees and domains. F11's design fixes
the OLD hyperbolic base; only that design was read here, and none of
its proposed spectral outcomes is received as a theorem for h.

Report-completion intake: local pin
08ff88e0ed841b25274c46ec2490a410729639c2 now carries F11 FINDINGS,
read on September 22 but NOT yet independently reproduced here. It
reports exceptional centrally twisted parameters with one normalizable
mode in each dual sector in the fixed-hyperbolic-base class, correcting
its earlier generic-vanishing expectation. Its own report explicitly
does not establish global harmonicity or proper convex geometry at
those distant parameters. This is a lead for the next checked join,
not a premise of R42 or permission to combine these two constructions.

## 3. First failure, separate diagnostic, and unaltered regression

Original six-file seal ecd6e70eaaa5012e0b1879892909da3e6ebc30b1 was
pushed and server-confirmed BEFORE its first execution. Every original
scientific byte is unchanged. The first native process exited zero
but contained ricci=false: process success was NOT scientific success.
The first new test file had 24 passes and one failure. The fixed
seventeen-file run had 276 passes and five failures: the four previous
IDs plus test_generic_tensor_identity[ricci]. All logs are preserved.

The source used structural equality for two differently factored
polynomial matrices, despite correctly normalizing another equivalent
Ricci residual. This was diagnosed by a NEW four-file packet, not by
editing the failed instrument. Its seal
8b256763ef0d3a48249f8e3ffa55d1d18c9b14f2 was likewise pushed and
server-confirmed before execution. It checks every residual both by
rational normalization and as an expanded zero polynomial, three exact
specializations, and wrong-curvature/wrong-cubic-sign controls.

The successor native checks all pass, and its five tests pass. Thus
the failure is adjudicated as a representation-sensitive comparison
bug, not a false Ricci identity. The original false flag and failed
test remain unchanged. The expanded eighteen-file population reports
281 passes and the SAME five failed IDs. This is not an all-green
suite and the original failure is not retroactively counted as a pass.

Incoming F10's seven sealed source files were hash-checked and its
unchanged snapshot gives 20 passing tests. That is same-implementation
reuse with the proof read personally, not independent global proof.
The original preseal governance run retained the four known failure
categories; final reporting checks are separately recorded. No full
suite, independent banking review, PR or main merge is claimed.
The September 22 all-head/tag fetch completed without ref changes.
The final governance run has 26 passes and four failed categories;
relay aging increases stale items from 25 to 29. The unchanged category
count must not be read as an unchanged debt inventory.

## 4. Strategic verdict: useful bridge, not a destination

This is relevant because an algebraic holonomy is now equipped with
a complete positive global background satisfying the adopted equations.
It reduces an arbitrary metric choice conditional on projective data.
It does NOT make those data physical, and its generality across proper
convex structures is not evidence selecting this programme's object.

The next priority is therefore a bounded PHYSICAL-MODE/DOMAIN test:
derive or bound the full relevant normalizable spectrum on this actual
metric, track gauge constraints and dual sectors, and keep the base
action and parameter-selection input explicit. Do not insert a mode
count from the old hyperbolic metric or from R40's nonsplit bundle.
If a justified pairing/acyclicity theorem applies here, record its
exact scope and return effort to the sourced nonsplit route; do not
declare a universal chirality kill or add rescue fields automatically.

In parallel as a registered duty, NOT a completed simultaneous
construction, R40/R41 still needs its noncentral source or boundary
variation law, complete positive background and physical domain in
one action. Its verified interior-index positive is retained.

Progress toward the goal must now be measured by what one common
model derives: admissible fields, physical modes, interactions,
anomaly consistency and an eventual discriminating prediction.
More geometric correspondences without reducing these duties would
be drift. Gravity, scale, quantum completion and observations remain
open requirements; neither background existence nor a spin/group
label alone satisfies them.
