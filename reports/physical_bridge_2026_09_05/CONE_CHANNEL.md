# R71 — full cone channels, without a false spectrum

October 1, 2026. The exact coefficient split and leading logarithmic
critical matrix pass. This is necessary boundary/operator progress for
[the physics mission](PHYSICS_MISSION.md), not a derived physical spectrum.

The actual trace-free sl4 coefficient reduces into charges 0,+4,-4
with dimensions 9,3,3. The charge-zero sector includes sl3 as well as
the single Z direction previously studied. Those sl3 coefficients are
NOT trivial just because they commute with Z. The full changing
128-component End4 form matrix (including the discarded identity for
the coefficient check) is checked, with its adjoints and radial term.
The physical trace-free form coefficient has dimension120, not128.

On the zero-Fourier neutral limiting critical kernel, the formal
leading logarithmic generator has paired nonzero eigenvalues
+/-1/2,+/-1,+/-3/2,+/-3,+/-7/2, with per-sign multiplicities2,4,4,4,2.
Only four zero eigenvalues remain, the exactly reducing Z slots.
Schur elimination and an independent principal-sl2/Casimir calculation
agree. Dropping either the off-critical Schur term or radial transport
fails its control. This does NOT yet prove 36 actual boundary traces,
nor their maximal/minimal domains.

The all-Fourier limiting-window bound is a bounded ellipse for any
fixed supplied aspect ratio. Three rationally certified fixtures have
limiting critical angular dimensions36,60,300. Those numbers change
with the supplied link aspect/connection data; they are not physical
families. The approximation's logarithmic powers can be L2, while a
nonzero polynomial-log residual divided by r has divergent graph norm.
Neither a frozen kernel nor a finite log expansion is an admission test.

## Evidence and first failure

Initial science seal:1aa3bd5c4eb5414ee246c5f75d6b6c7978a10108.
Separately sealed control:4164fa2039080aeb5d313009c868222dd09c5207.
Both were committed, pushed and server-confirmed before execution.

First native run:55/56 checks passed, terminal1. Its scalar polynomial
comparison used the requested real symbol, while PurePoly supplied its
own generator with different assumptions. The first focused regression
has21 passes and two failures, retained unchanged:

- tests/test_physical_bridge_cone_channel.py::test_scalar_limiting_symbol_and_threshold_control
- tests/test_physical_bridge_cone_channel.py::test_all_two_sided_frozen_identities

The new control normalizes only the generator, not the mathematical
eigenvalue target. It recovers the original failed comparison, checks
a direct rational-matrix determinant and rejects a shifted mass.
Final native:60 exact controls passed, terminal0.
R68/R70 plus seven control tests:23 passed, terminal0.
The original R71 files were not repaired in place. Older R63/R64/R69
failures were not rerun and remain separate historical debts.

Final governance retains26 PASS and the same four historical FAIL
rows. The first precommit run also caught a LAW_MAP header/provenance
format error in these new rows:25 PASS/five FAIL. Its raw capture is
retained; the header and explicit B1504 context-only lineage were fixed
in metadata, without changing the frozen science. Cumulative prior
custody and the new local receipt checker are
scoped byte/population checks, not independent mathematical review.
No full suite, full-main bank or complete physics certificate.
A pre-seal metadata comparison first hit a US-ASCII regex error; the
UTF-8 rerun was guarded and matched the old rows before commit. No
scientific execution or change was authorized by that failed helper.

The first cumulative custody run stopped at GOAL_VERDICT's old digest,
before the newly edited reader hashes had been appended. That failed
capture is retained; refreshed latest metadata digests are checked in a
new run. A reader-update patch was also rejected for duplicate path
operations without applying edits; the valid single-operation patch landed.

## What this changes, and what comes next

R70's four neutral traces remain exactly justified. R71 prevents
extending their constant trace law to other channels by a limiting
dimension match. It also prevents killing log channels from L4 or
finite-order graph estimates alone. The actual changing operator is
the next analytic object, with the metric/end assumptions still visible.

PB-BOUNDARY must establish exact graph domains/generalized traces,
including nonzero Fourier and threshold channels, then test products,
compact gauge and all superfield maps in one common end law.
PB-ACTION must derive or explicitly price that end law and the metric.
PB-TRANSITIONS must match the actual core and full parent; a rank-two
D0 system does not inherit this rank-four cone by an index match.
Physical chiral SM interactions, observables, quantum consistency and
gravity remain the full mission, not conclusions of this calculation.

Received B1507 and the new SM path document at76d98eba were personally
read as context. Their cited audit horizon predates R69/R70; none is
blanket-certified or imported as a scientific premise here. No universal
repository absence, physical no-go or selected vacuum is asserted.

[Frozen design](CONE_CHANNEL_DESIGN.md),
[authored proof](CONE_CHANNEL_PROOF.md),
[input pins](CONE_CHANNEL_INPUTS.json),
[original producer](cone_channel.py),
[separate repair design](CONE_CHANNEL_CONTROL_DESIGN.md),
[control producer](cone_channel_control.py),
[raw-capture receipts](CONE_CHANNEL_RECEIPTS.json).
