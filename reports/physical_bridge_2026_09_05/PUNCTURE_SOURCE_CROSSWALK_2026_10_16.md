# Reuse the puncture results; audit the identification before another count

Source-specification reading on October 16, not a new scientific run or
an end-law verdict. Main is pinned at 562882d15; the initial audit proof
inventory is pinned separately. Existing positives below retain their
own verification grades. They are not made independently verified by
being read here.

## Four distinct questions already have different answers

| Source | Actual input and operation | Reusable result | What is not paid by it |
|---|---|---|---|
| Main B1606 P1–P3 | Three parity blocks, each the quaternion doublet; specified move lifts with block identifications u_p. The six-matrix action is assembled explicitly. | Recorded move group 2O with pieces of dimensions two and four; invariant dimensions zero, two, four, six give indices minus three, minus one, plus one, plus three under the imported index formula. | Which transformations preserve a physical background and act on the actual closed operator/domain. |
| Main B1606 P4 | The same moves PLUS the block-diagonal parity sign operators. | Recorded graded action is irreducible on all six; only the two extreme invariant subspaces remain, giving plus/minus three. This conditional positive must not be lost. | Why an admissible physical end must preserve these additional parity operators, rather than only the moves or a smaller stabilizer. |
| Main B1641 W1–W3, with its scope addendum | The actual six local-solution matrices from the ruled moves and chosen modular identifications; numerical commutants and dimension formula. | Reproduces two-plus-four and the conditional cusp index table. Its O1/O2 additionally distinguish the uniform record lift from the geometric point-pushing lift. | A unique coherent lift is not proved by one Delta-four comparison; the addendum retains that limitation. The table is not a physical end selection. |
| Audit fork puncture_symmetry and puncture_fredholm | Specified finite-distance ordinary-spin operator, coefficient, trace data, chirality and self-adjoint domains. | Reusable analytic realization of the critical quotient and index; conditional symmetry restrictions are already investigated, not to be rediscovered. | Identification of the full physical symmetry with the actual induced trace action; the complete cusp is a different end/operator. |

Thus main's latest V2-plus-V4 pointer is useful prior work, not a reason
to repeat its decomposition or forget its stronger parity-graded case.
The new question is the admissibility and actual action of the symmetry,
not whether a six-dimensional vector space can be given a desired action.

### Recovered before any new restriction calculation: B1609 E4

Main's latest P-184 says the V4 restriction to 2T is not computed.
The same main head's B1609 E4 already restricts B1606's six-coefficient
model to the even-word subgroup: its recorded order is24, commutant3,
and the pieces are three inequivalent doublets. Its recorded invariant
dimensions are0,2,4,6; with parity grading it again keeps only0 and6.
The deck fixes one piece and exchanges two. GENESIS v1.30 already
summarizes this as the spinor and its two omega twists.

Personally read the complete FINDINGS, producing code and test, and
inspected its stored E4 output. The producer and stored output match
main's recorded SHA256s. Byte-faithful copies and SOURCE.json live in
specification_audit_2026_10_16/received_B1609, recovered by the metadata-only
recover_b1609.rb. This is verified retrieval of an existing computation,
not a fresh execution or independent mathematical acceptance.

Therefore a blanket "the restriction was not computed" is not current
for this coefficient model. The exact basis/lift identification with
B1641's presentation, and then with the physical critical trace quotient,
still needs to be shown. Reuse E4 and check those maps; do not repeat its
restriction merely because the latest task register forgot it. The
retained graded positive and the ungraded alternatives both survive.

## What the personally read instruments actually check

Read in full: B1606 FINDINGS and puncture_condition.py; B1641 FINDINGS,
its Review63 addendum, w46_on_main.py and both associated test files.
These are source readings, not executions here.

B1606 explicitly builds the coefficient action with the quaternion
intertwiners u_p and the move's parity permutation. Its index formula is
declared as the incoming Riemann–Roch assertion. Although FINDINGS calls
the calculation exact linear algebra, this producer uses NumPy complex
matrices, allclose, SVD thresholds and rounded eigenvalue clusters. Its
lock reads stored results. That describes the evidence route, not a
refutation of the decomposition. The fork's existing proofs and
checks should be reused where they cover the same matrices.

B1641 has two separate actions in one instrument: group-cohomology
actions for O1/O2 and local coefficient matrices for W1–W3. The latter
are block permutations with quaternion lifts; their decomposition uses
SVD/eigenvalue grouping. Its live test rechecks the central-sign and
point-pushing comparison, not the entire local-domain/index construction.
The generator matrices and bases must therefore be matched explicitly;
cohomology, local coefficients and operator traces are not synonymous.

No source reading in this pass is reported as a new numerical replay,
an exact new certificate or an exhaustive search of the repository.

## Specification for the identification check

For each transformation admitted by the foundational architecture,
write its map on the punctured carrier, coefficient bundle and spin/frame
data at the same time. Track the metric, connection and other background
fields. A map between different moduli can establish covariance of a
family; it does not automatically establish a fixed background's symmetry.

Then exhibit its map on the actual operator's maximal and minimal graph
domains and on the quotient of their boundary traces. Include coordinate
and spin factors, not just the coefficient matrix. Check the actual Green
pairing and chiral grading, including whether an action exchanges the two
chiral trace spaces. Only after this map is known is it legitimate to
ask which self-adjoint domains are invariant. State which transformation
group an end law is required to preserve and why that requirement follows
from the admitted data rather than the desired index.

This is a list of verification obligations, not a statement that no file
in the full history contains their answer. Existing fork proofs, W45/W46
sources and the main lift-coherence work are the first retrieval targets.

Even a restriction to certain index values does not choose a nonzero
index, a unique boundary subspace or a representation-resolved physical
generation count. The physical fermion action, conjugates, gauge sector,
interactions and anomaly accounting still have to share this domain.

## Canonical cusp versus finite-distance puncture

Main B1667's full FINDINGS and relay are now read. It computes two
canonical-cut prescriptions on the hyperbolically uniformized fibre,
over a disclosed informed grid. Its own final scope excludes a proof
between grid points, a physical-frame selection and selection of either
horocycle as the physical end. Preserve that positive geometric result
without treating the two examples as an exhaustive classification of
physical end laws.

That complete cusp is not automatically the fork's finite-distance
spin Dirac problem. A conformal relation between metrics is not a free
identification of their completed Hilbert/graph domains or their physical
norm scale. The map and limiting prescription have to be recorded.
Keep four quantities distinct: the domain subspace Lambda; GENESIS's
I-31 field postulate Lambda; a logarithmic cutoff/normalization L; and
an admitted geometric cusp unit. No supplied number is chosen here.

## Next step under P-181/P-184

Complete the specification coverage and governance resolution first.
Retrieve the existing operator/coefficient/lift maps, and preregister
one discriminating question about their induced critical action. A
valid failure is scoped to that map, symmetry and operator, not to the
generated architecture. A valid positive removes an input only when
the admissibility requirement is itself derived. No extension of the
supplied compact-E8 parent is resumed by this source crosswalk.

## Further source reading: the cutoff and domain concern different fields

After the first crosswalk landing, personally read main B1651's complete
FINDINGS and second Szego addendum, and B1654's complete FINDINGS, at
the same pinned main head. These three readings supplement, rather than
alter, the nine external-source records in the initial reconciliation.
No producer in those three sources was rerun by this reading.

B1651's addendum describes the holomorphic doublet's half-pole at the
puncture and its bilinear pairing's simple pole. B1654 explicitly assigns
the finite common L2 norm to the modes called matter in its dictionary,
and the logarithmically cutoff-dependent norm to the Higgs boundary
class. Thus its L is not already the matter-domain subspace Lambda.
This is a banked distinction to reuse, not a new integrability discovery.

A proposed common end law must identify which field's operator, domain,
norm and boundary response it constrains, and exhibit any coupling that
links those constraints. Neither the shared puncture nor a shared word
"end" supplies that link. The positive opportunity is to derive that
relationship from admitted structures, not to insert one boundary
condition separately for the index and another for the desired masses.
The source readings do not decide physical field admission or establish
a universal obstruction to such a joint law.
