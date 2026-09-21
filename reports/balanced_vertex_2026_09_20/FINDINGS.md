# F09: a genuine parent vertex, but no built-in mirror-selective hierarchy

2026-09-20. Local branch audit/fork-2026-09-20. This joins F08's
balanced classical background to R38's ACTUAL one-form interaction.
It does not compute a quantum mirror gap or complete the physical TOE.

## Constructive result: the tensor profiles can interact

The parent already contains the (10,6) channel, where 6 is the exterior
square of F08's rank-four bundle. Its invariant one-form interaction
with two spinor profiles is nonzero for explicit tensor profiles. This
uses the wedge/bracket vertex of the adopted action, not the scalar
metric-overlap coupling from the separate added-field model.
[Primary action, equation 2.13 and B.29](https://arxiv.org/html/1812.06072v2).

There is a compact exact dictionary. If the possible massless profile
is represented by the symmetric trace-free tensor b of F08, its local
bilinear source is the cofactor matrix of b. In the declared normalization,

    Q(b,b) = b^2 - tr(b^2) I/2,
    |Q(b,b)|^2 = |b|^4/4 for REAL symmetric trace-free b.

Thus a nonzero real tensor profile does not lose the vertex merely
because both fermions use the same profile. The bundle coefficients
make the wedge nontrivial. The actual Grassmann statistics are checked.
The positive example b=diag(1,-1,0) gives normalized vertex -1 with
the displayed mediator component. A complex nonzero rank-one null
tensor instead gives zero, so the reality qualifier cannot be dropped.

These are pointwise interaction statements. F08 has NOT established
that a nonzero global normalizable Codazzi profile exists on a selected
member or cover. No generation count or physical Yukawa value follows.

## An actual spectral bound in the interacting channel

Inducing the balanced flat connection on the six preserves the full
classical equations and covariantly parallel Higgs field. Its algebraic
Hodge terms have exact spectra

    degree 0 or 3: 2 (six times),
    degree 1 or 2: 1 (ten times), 3 (six times), 4 (twice).

The complete positive-L2 operator therefore satisfies Delta6^1>=1
in curvature-radius-one units. The proof uses the global domain and
positive form identity, not an inference from finite matrices alone.
There are no L2 zero modes in this coefficient one-form sector, and
its Hodge Green operator is bounded by 1/(1+p^2) at Euclidean p^2>=0.

This does not set a physical mass scale. Nor does it by itself give
the full gauge-fixed bosonic propagator, a four-fermion matching
coefficient, or an interacting phase. Those require their own action
reduction and normalization. A massless ten-sector Higgs multiplet
cannot simply be assumed from this representation's presence.

## What stops automatic mirror selectivity here

The new calculation extends F08's operator pairing to the normalized
4--4--6 wedge tensor. With the displayed antiunitary maps,

    V_dual(paired profiles) = -conjugate(V(original profiles)).

Consequently whole paired normalized coupling tensors have equal
norms and corresponding singular values. The equality holds whenever
the integrals exist and the same complete domains are used. It includes
F08's fourth-root scalar twists. It does NOT equate arbitrary unpaired
chosen modes or different vacua.

The six also has an explicit internal antiunitary square-minus-one
symmetry. That fact is not named physical time reversal. It controls
the Hodge resolvent and equal paired quadratic responses for L2
sources. L2 matter profiles alone do not ensure their products are L2;
L4 is a sufficient additional condition for this response calculation.

Two controls prevent a misleading verdict: a chosen mediator can have
zero coupling to one profile and nonzero coupling to its partner while
the complete paired spaces agree; a positive operator deliberately
breaking the intertwiner gives unequal whole responses. Neither control
is asserted to be the actual global spectrum or a new BPS background.

## What this changes toward the goal

The positive is more than a representation label: a faithful local
profile-to-interaction map and a global coefficient-operator bound now
belong to the same classical background. The limiting result is more
than free isospectrality: the tested parent vertex itself has no derived
mirror preference in the unchanged vacuum.

Accordingly, do not spend the next step fitting a selected-profile
hierarchy here or importing the added H-theory's scalar overlap. A
chirality candidate must identify a change to the actual intertwining
background, end/domain data or interacting phase, then show that the
full equations, gauge symmetry, normalizable spectrum and anomalies
survive. A nonzero vector condensate is not automatically acceptable;
R33 already records its gauge breaking.

This result is NOT a no-go for every interaction or for spontaneous
symmetry breaking. The other parent channels, quantum measure and
nonperturbative phases were not solved. The nonsplit/source and added-
field positives retain their own scope. Global mode multiplicity,
selected chiral vacuum, complete SM interactions, dynamical gravity
and measured predictions remain unachieved by this checkpoint.

**Follow-through F10:** the [real-projective family test](../projective_escape_2026_09_21/FINDINGS.md)
now gives an actual global holonomy change that removes F08's flat dual
isomorphisms, with an exact compatible local cusp solution. It does not
yet supply asymmetric physical coupling tensors: the complete vacuum,
normalizable spectrum and all end/action conditions remain to be
established, and ordinary dual-sector H1 dimensions still agree. The
new infinite-background-norm/zero-residual-potential example reinforces
the need to test those conditions separately. F09's fixed-background
interaction result and sealed science are unchanged.

## Verification and custody

Science sealed before first execution at **a077d5fc**. **19 new checks
passed on their first run**, and **157 unchanged antecedent/parent-vertex
checks passed** with one optional-GUI warning. All four scientific and
three transitive producer hashes match. Earlier failed versions remain
preserved and are not included in a claim of a fully green repository.

[Design](DESIGN.md), [proof](PROOF.md), [producer](verify.py),
[test/read receipt](RECHECKS.md). These are authored analytic arguments
with exact local controls, not independent theorem acceptance. No shared
B number, main edit, new all-head fetch, full-suite/gate certification,
push, external publication or complete TOE is claimed.
