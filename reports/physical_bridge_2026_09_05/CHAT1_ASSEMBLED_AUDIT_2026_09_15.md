# Chat1 and the arithmetic parent: useful structure, uncompleted physical joins

2026-09-15. Owner-supplied packet and subsequent parent-object proposal.
The assembled document and every one of its 28 scripts were personally
read. No agent summaries were used and no supplied script was executed.
Independent controls below are separate from R31's completed compact
Poisson calculation and use no shared R/B allocation.

## Verdict first

The parent/cover viewpoint helps. The proposed PSL(2,O_3) cover indices
12,24,36 are verified for m004,m202,s959. The parent contains geometric
tetrahedral isotropy whose binary lift is 2T, checked by explicit exact
matrices. Missing order-three isometries of one manifold do not imply
missing order-three structure in its arithmetic parent or family.

But subgroup index alone does not decide which symmetry descends:
s958 is also an index-36 cover and has no order-three isometry. Nor do
these facts establish three unpaired generations. The packet conflates
a 27-dimensional adjoint grade with the fundamental 27 matter module.
That specific identification fails an exact color-representation test.
Retain the geometry and the class strategy; do not adopt the assembled
Standard-Model headline or the universal amphichirality no-go.

## 1. What the covering claim now actually has behind it

Write G=PSL(2,O_3), with O_3=Z[z], z=(1+sqrt(-3))/2. For each named
triangulation the new control checks inverse face identifications,
connectedness and the complete logarithmic gluing equations with all
shapes z. Since z'=z''=z, the edge sums must be 6 and the peripheral
sums 0. Positivity is exact, Im(z)>0; this does not use rounded volume
ratios as a geometric certificate. The face-pairing graph is then
two-colored explicitly.

Fominykh et al., Remark 5.5, identify the two-colored orientable regular
tessellations as covers of the PSL Bianchi orbifold. A regular ideal
tetrahedron has 24 barycentric chambers. The PSL orbifold covers the
full reflection orbifold with degree four, so its covolume is v3/6 and
an n-tetrahedron cover has index 6n. The named objects pass the actual
covering criterion, not merely that final division.[^1]

Separately, Sage/SnapPy certified each canonical cell decomposition and
exhausted its combinatorial self-isomorphisms with exact cusp actions.

| Manifold | Regular tetrahedra | PSL index | Cusps | Full isometry count | Cusp-rotating order-three isometries |
|---|---:|---:|---:|---:|---:|
| m004 | 2 | 12 | 1 | 8 | 0 |
| m202 | 4 | 24 | 2 | 12 | 2 |
| s959 | 6 | 36 | 2 | 12 | 2 |
| s958, control | 6 | 36 | 1 | 2 | 0 |

The last column counts cusp-fixing maps whose integral torus matrices
have determinant one and trace -1. Their affine cube is identity because
I+A+A^2=0. The full counts 8 and 2 separately rule out any order-three
isometry in m004 and s958; a matrix-only search would otherwise miss
pure translations. No unverified symmetry-group call supplies this table.

Original triangulation isosigs, colorings and all cusp matrices are in
the output receipts. For example s959's regular isosig is
gLLPQceefeffpupuupa and its certified canonical isosig is
jLLzzQQccdffihhiiqffofafoqq. The distinction matters: a tetrahedral
triangulation can hide symmetries that its canonical decomposition sees.

A second control, the paper's otet06_0000 tessellation, has six regular
tetrahedra but fails two-colorability. Its given map covers the PGL
orbifold, not PSL. This is not a claim about every possible embedding
or alternative tessellation of that manifold.

These are cover-existence and degree certificates. They are not yet
explicit coset presentations for simultaneous embeddings or a lift
identifying each observed symmetry with a particular parent matrix.
The indices describe covers of the same orbifold, not a proved nested
tower m004 -> m202 -> s959.

## 2. The parent really contains the missing finite structure

In exact O_3 arithmetic use

    A = [[0,1],[-1,1]],       B = [[0,1-z],[-z,0]].

Both determinants are one and A^3=B^2=-I. Their closure has exactly 24
matrices with center {I,-I}. Acting on the actual regular tetrahedron
vertices {0,1,z,infinity} gives exactly its 12 even permutations. Thus
the projective stabilizer is A4 and the determinant-one binary lift is
2T. In particular [A] is an order-three elliptic of G before choosing
any manifold cover. A finite subgroup fixes the tetrahedron's center;
its compact spin lift supplies the geometric interpretation of 2T.

This is a concrete geometric entrance to the already known McKay E6
label. It does not require pretending the torsion-free fundamental
group of a manifold contains finite-order rotations. B727 already
discusses Bianchi torsion and the McKay correspondence; neither is
rediscovered here and the different ADE faces are not independent
statistical evidence. Conversely, genericity of a construction does
not make that construction invalid or prove that it cannot occur in a
physical theory. An E6 label is still not an E6 Yang-Mills action.

For M=H3/Gamma the relevant formula is

    Isom^+(M) = N_PSL(2,C)(Gamma)/Gamma.

A parent element acts as an isometry of this particular cover only
when it normalizes Gamma. All four manifold groups are torsion-free,
including the ones whose isometry group contains C3. The s958/s959
comparison proves that index/depth alone does not determine visibility.
The certified symmetry calculation has not identified its specific
elliptics with the displayed parent A, so that descent is not asserted.

There is still a useful family-level action when normalization fails:
Gamma intersect g Gamma g^-1 is a common finite-index subgroup for
g in G. Its two covering maps give a correspondence between covers.
That is a mathematical route to retaining parent structure beyond one
manifold's isometries, not automatically a unitary order-three action
on the old physical Hilbert space. Fields and operators must be carried
through those maps explicitly.

Strictly, G and the commensurability class are not identical objects.
G is a natural chosen lattice/parent orbifold in that class. The class
contains other orbifolds, with no universal minimal member; the cited
paper explicitly distinguishes its category of covers from any one
quotient. A physical theory based on G must justify that choice or
specify how its observables transform between representatives.[^1]

## 3. The two 27s do not carry the same particles

In a consistent convention under SU(3)_C x SU(3)_L x SU(3)_R,

    78 = (8,1,1)+(1,8,1)+(1,1,8)+(3,3,3)+(3bar,3bar,3bar),
    27_E6 = (3,3bar,1)+(1,3,3bar)+(3bar,1,3).

The first 27-dimensional grade is a tensor product; the fundamental 27
is the sum of three bifundamentals. Equation (35) of Donagi et al. gives
both on the same page, with bars checked visually in the PDF.[^2]

If the grade (3,3,3) is treated as the proposed four-dimensional left-
Weyl matter with the first factor color, it contains nine color triplets,
no color antitriplets and no color singlets. Its SU(3)_C cubic anomaly
coefficient is +9 when one fundamental has coefficient +1. Taking
T=diag(1,1,-2), the exact control gives trace_grade(T^3)=-54. The true
fundamental 27 instead contains three triplets, three antitriplets and
nine singlets, with trace(T^3)=0. The conjugate grade has coefficient
-9; retaining both cancels the anomaly while retaining conjugate matter.

This does not say that an adjoint Lie grading is itself an anomalous
theory, or that anomaly-free trinification is impossible. It says that
its grade cannot be relabeled as the anomaly-free matter 27. Nor does
a complex representation by itself count left-minus-right zero modes
of a four-dimensional fermion operator. R15/R19's charged 16 sector is
another specified representation, not silently three fundamental 27s.
The separate B960 central-character restriction was also reread: its
fundamental-27/global-form distinction is relevant background, not a
proof of this branching calculation or all of its broader no-go wording.

## 4. Other joins to retain or narrow

- **Three fixed loci:** det(A-I)=3 on a torus gives three fixed points
  for the corresponding affine rotation, hence fixed cusp rays. It does
  not alone establish the global arc pairing, a bundle representation
  on those arcs or one unpaired normalizable generation on each.
- **Mirror negatives:** I(V*)=-I(V) implies zero only if the mirror
  identifies the complete chosen operator/bundle/domain data with their
  conjugates. A mirror of the bare manifold need not preserve a selected
  Higgs field, defect or boundary condition. Geometric CS or one eta
  value cannot prove the vanishing of every twisted physical index.
- **Arithmetic:** the general cusped criterion needs integral traces
  as well as an imaginary-quadratic invariant trace field. Here the
  tetrahedral cover certificates supply arithmetic membership; that
  positive survives the packet's insufficient field-only shortcut.[^3]
- **Rank and scales:** reducing a candidate gauge group to the Standard
  Model requires specified fields, charges, VEVs and a viable potential.
  A one-loop crossing inferred from measured couplings and assumed
  matter/threshold content is conditional matching, not an absolute
  scale predicted by the object. The packet's detailed scale and Z-prime
  claims have not been independently reproduced in this intake and are
  not promoted to this model's outputs. The supplied verification scripts
  do not resolve the representation or operator identifications above.

## 5. What this changes in the ongoing path

R31 has just supplied the compact normalized-source logarithmic estimate
behind R30's light-pair bound. On that explicit strong-source, extending-
flat, absolute domain, shrinking resolved cores gives light partners,
not heavy mirrors. R19's singular three/zero kernel remains on its
different domain. Choosing a geometrically chiral member does not by
itself change either calculation.

The class insight supplies a useful next formulation: construct the
parent-equivariant bundle and source/end action, state the restriction
or projection to a chosen cover, and compute the representation-valued
fermion index AND its compensating modes in that same theory. Track
normalized currents and the complete anomaly through the same maps.
If an orbifold or correspondence changes the kinetic domain, derive
that change; do not use it silently to drop R30/R31's partners. This
extends the current sourced route rather than abandoning it for a
new list of coincidences. It is a plan, not an executed chiral completion.

## 6. Execution, custody and the consolidation relay

**Later fetch, September 16:** main's B1413 now records the R21--R31
harvest. Its full findings and corrected relay have been read; this
updates the pre-fetch main-status sentence below. See the subsequent
[boundary-table audit](BOUNDARY_TABLE_AUDIT_2026_09_16.md), which also
corrects a newly received conflation of the source exterior and the
undrilled core. It does not change any packet/control result above.

Original seal: 5b6391c368a7695fef4b86a7c7bf8bfee7f8a309.
Original native: exit 1, unsupported otet06_0000 name; original tests:
eight fixture errors. Those failed runs and source files are preserved.
Independent certified canonical mode: all four expected rows pass.
Separate alias seal: 5e063851358bc1b8016d93df426eb975a1665d89. It uses
the exact Table 2 signature gLLPQccdfeefqjsqqjj without altering the
original science or expected predicates. Follow-on native: 10/10 checks;
new follow-on tests: eight passed. Both seals were pushed before their
respective executions. Repository read-only during every scientific run.
This is not full-repository green or independent main banking. R31's
508/16/8 broad result predates these two separate test files; it is not
advertised as covering them. The original eight new fixture errors
would remain in a suite that includes their unchanged original file.

[Packet and run custody](CHAT1_ASSEMBLED_RECEIPTS.json) identifies every
read packet member, all five runs and their unredacted raw digests.
Public outputs only redact declared machine/environment prefixes.
[Original design](CHAT1_CLASS_CONTROL_DESIGN.md) and
[alias follow-on design](CHAT1_CLASS_ALIAS_CONTROL_DESIGN.md) are frozen.
[Reporting checks](CHAT1_ASSEMBLED_FINAL_CHECKS.txt) retain the initial
provenance-gate failure and its citation-only correction, as well as
the outstanding inherited gate and test failures.

The owner's consolidation relay was read completely. It addresses the
older codex/seat-r001 at R040, not this checkout. Its harvest coverage
and ahead/behind counts are received claims, not newly audited facts.
This lane remains audit/physical-bridge-2026-09-05; it is not frozen by
that relay, allocates no B numbers, and has neither merged main nor
switched to the other seat's numbering. No external relay was sent.
The new scientific scripts use repository-relative paths. Existing
historical custody utilities are not thereby certified portable for
main's harvest guard.

Five-line seat answer, held here rather than sent:

    Active: yes, physical-bridge audit/research lane.
    Branch: audit/physical-bridge-2026-09-05.
    Numbering: path-local R1--R31, plus named packet/alias controls; no B allocation.
    Roadmap: MISSION_ROADMAP_2026_09_13.md in this report directory; one sourced quantum-consistent model.
    Main acceptance: not established here for R29--R31 or these new controls; no claimed independent main bank.

[^1]: Fominykh et al., [A census of tetrahedral hyperbolic manifolds](https://people.mpim-bonn.mpg.de/stavros/publications/census.tetrahedral.manifolds.pdf), Table 2, section 3.1, sections 5.1--5.4, especially Remark 5.5. Used for the covering criterion and type distinctions, not as a particle-physics theorem.
[^2]: Donagi et al., [The Spectra of Heterotic Standard Model Vacua](https://openaccess.city.ac.uk/id/eprint/853/1/0411156v1.pdf), section 2, equation (35). Only the relevant sections, not the entire paper, were read for this intake.
[^3]: Neumann and Reid, [Arithmetic of Hyperbolic Manifolds](https://www.math.columbia.edu/department/neumann/preprints/nrarith.pdf), Proposition 4.4. The relevant source sections were inspected; no full-paper reading or new arithmeticity theorem is claimed.
