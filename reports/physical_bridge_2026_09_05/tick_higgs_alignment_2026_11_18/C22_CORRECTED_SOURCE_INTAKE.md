# C22 source refresh: the narrowed negative, roster and numerical precision

2026-11-18. Bounded continuation of the existing C8 source review.
SM source: `d88ea8e8a34190bd82a132d9ff7ddf41facc2b30`.
Main source: `7d3776b67c6832c99506e334e7e4e45df155d580`.
No scientific source was imported or executed, and no new model or
numerical campaign was started. This reading does not independently
recompute the reported spectra, finite scan or alignment statistics.

## Corrections received

The dated amendments on SM-C19 through SM-C22 preserve the useful
results and now distinguish the following:

- S6 is a unitary exchange of the two ground eigenlines while reversing
  the act transport. The former antiunitary-only headline is withdrawn.
- The coordinate reflection z -> bar z includes the mode parity; the
  two antiunitary lifts agree on the even ground plane but not everywhere.
- The ground space is a complex plane, with no earned restriction to
  two eigenlines. The flux construction's eigenline cusp negative does
  not apply to every direction in that plane or to every realization.
- The coherent h* has three nonzero coefficients and retains a hierarchy
  in the declared overlap contraction. The one-or-two-modes exclusion is
  explicitly refuted. It is not a selected physical Higgs or an SM fit.
- The C22 scan is a finite test at specified heights, torsion points and
  lift. Its reported lack of a candidate meeting both thresholds is not
  an all-vector or full physical exclusion. The correction says so.

The old statements remain below the dated amendments. They are historical
text, not new evidence against the corrected scope. Main already records
the universal C22 conclusion as PARTIAL (`sm-c22-04`). No new discovery
or additional refutation of that conclusion is claimed here.

## C22-S01: the declared candidate count is 5018, not 5021

The corrected C22 page at lines 12 and 16, and its result at lines 26
and 46, still say 5021. `sm-c22-02.json` on main also says 5021.

But the source's `relays/sm_c22/run_c22.py:65-76` constructs:

    6 basis vectors + 6 act eigenvectors + 3*2 pair vectors
                    + 5000 random vectors = 5018 candidates.

The sealed card at lines 25-30 names these same categories. The committed
JSON has exactly eighteen named entries: six modes, six eigenvectors and
six pairs. The random loop is `range(5000)`. All eighteen named keys in
the receipt are distinct. There are no extra three candidate vectors in
that script or its named output. In particular h* is outside this scan.

This is a source/receipt roster correction, not a rerun of the scan.
The absence-of-both count is received from its author run; the denominator
must describe the declared producer. If another three candidates were
run, their producer, vector definitions and output need to be supplied.
Until then please record 5018. This does not turn a sample into a census.

## C22-S02: sixty-digit theta input does not make the decomposition sixty-digit

The SM producer's `run_c22.py:31-35` calls `Y_mp(...,dps=60)` and then
assigns `complex(v)` to a NumPy array with `complex` dtype. Its statistics
use `np.linalg.svd` on those arrays at lines 81-88. The singular vectors,
singular values, their ratios and endpoint-slope estimates are therefore
formed after the extended-precision values have been rounded to ordinary
complex precision. This is the same method distinction already found for
C21; it must be carried to this new run separately.

Main's C22 driver has the same precision boundary:
`verification/checks/sm_c22.py:19-22` converts the 60-digit theta entries
to `complex`, and lines 31-36 use NumPy SVD and ordinary logarithms.
The header at lines 1-4 and M45's introduction should therefore be read
as **60-digit theta evaluation followed by ordinary-complex contraction
and SVD**, not an extended-precision decomposition. This is a request to
state the method accurately, not a claim that a particular printed value
is false. Main's earlier C8 exact leading-term proof and the separate
extended-precision C21 check are not invalidated by this source finding.

The candidate count needs no scientific rerun. For a later, admitted
precision check of spectral claims, retain the extended-precision
contraction through the decomposition and report the precision dependence
and spectral gaps. A numerical hierarchy or a chosen singular vector
should not become an asymptotic theorem through the input precision alone.
No such new run is performed or proposed as already authorized here.

## An observed limit on the agreement claim

The two committed outputs do not have identical single-mode alignment
shares. In the original JSON the shares for modes 1, 4 and 5 are
respectively 0.333333..., 0.166666... and 0.291666.... Main's new output
prints 0.292, 0.208 and 0.250. The common upper bound 0.375 and the
printed median hierarchy summaries survive this difference. Thus M45's
particular summary claims are not refuted by it; exact pointwise or
all-share agreement is not shown.

This source comparison does not diagnose the difference. Before using
individual singular-vector alignments as physical discriminators, the
actual kinetic metric, basis transport and any degenerate singular
subspaces must be retained. No degeneracy is asserted from these rounded
outputs alone, and no alternate alignment statistic is silently supplied.

## T1's role and the next physical duty

The algebraic positive is the anticommutation of Z3 and X3. It rules out
a common eigenvector of these two invertible matrices. The accompanying
coupling argument is made with a fixed coefficient vector and the stated
half-lift comparison. This is not a calculation of a covariantly varying
Higgs section, its equation of motion, a boundary response or a selected
vacuum. The existing C8 note already retains those separate duties.

The finite overlap construction remains a recovery control. To turn its
remaining directions into a physical candidate, the same action must
derive the fields' transport, kinetic metric, stationary state and full
fermion operator/domain. Neither a sampled exclusion nor a specially
chosen coherent vector pays that connection. No new foundational input
reduction, chiral SM3 construction, vacuum selection or gravity is counted.

Exact source hashes, reading ranges and the quoted evidence are in
`C22_INTAKE_CUSTODY.json`. This intake is a source reading, not independent
scientific verification of C22.
