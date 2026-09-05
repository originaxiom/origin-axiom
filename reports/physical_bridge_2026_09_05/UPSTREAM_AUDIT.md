# Upstream a8fd2460: the construction survives, the scope sharpens

Merged locally as 93292799, preserving both histories and both independently
written B1242 point-of-use addenda. The old clean-clone absence inventory and
5-failure full-suite record remain true of **f06d3405**, not this updated main.
No push or publication is implied by the local merge.

Pre-run seal: 182c27ea. Exact instrument and eight upstream test files ran to
completion: **59 passed in 253.64 seconds**, plus the independent exact checks.
Raw result: `upstream_first_run.json`. This is not a full-suite certificate.
The raw command metadata contains the local interpreter path; retain the raw
artifact and make a labelled portable derivative before public distribution.

## What is verified and worth carrying forward

- The affine D2 decode holds on all 27 weights. Recovering every matrix entry's
  root shift, then constructing simple roots of its even-root subalgebra, gives
  the D5 Cartan diagram (determinant 4), not merely the number 40. The actual
  invariant blocks have sizes 1,10,16 and the singlet is weight 13.
- The reported B1252 hypercharge witness has the actual A2+A1 action on the 16.
  Its connected multiplets are (3,2,1/6), (3,1,-2/3), (3,1,1/3), (1,2,-1/2),
  (1,1,1), (1,1,0). The two color singlet-under-weak triplets have opposite
  color cubic trace to Q's triplets, so conjugacy is checked by action, not
  assigned from their names.
- All mixed/abelian anomaly traces vanish on these actual matrices. A generic
  color Cartan has nonzero cubic trace on individual triplets, cancelling in
  the whole 16. A root coroot alone would have been a vacuous SU3-cubic test;
  that trap was anticipated in the sealed instrument. Four actual SU2
  doublets give the even Witten count. Perturbing e-c's charge breaks the test.
  All 45 cubic terms conserve the derived hypercharge.
- An explicit orthogonal Weyl matrix transports R4's S line to weight 13 and
  its 1+10 / 16 grading to D2, preserving every nonzero cubic-tensor entry.
  Simple-root reflection indices, zero-based: 0,2,3,1,4,3,2,5. Thus the new
  grading and our conditional model are connected by an exhibited action.
- The upstream B1253 geometry and its own correction pass their original
  locks. Counting overlapping Weyl-conjugate subspaces is not counting
  independent fermion fields. This does not adjudicate other count mechanisms.

## What the tests did not establish

**Metric provenance.** B1252's solution is exactly the inverse Bourbaki Cartan
matrix already constructed in B970 `exotics_levi.py` and used explicitly in R4.
Its recovery from the representation is a valid independent check, but the
repository-wide phrase “the metric did not exist” loses prior work. B1252's
equations impose root length squared 2; their successful recheck is not an
independent prediction. Weight length squared 4/3 *is* an independent consequence.
None of this invalidates the corrected use of the metric instead of naive dot
products. An invariant weight metric is also not a derived spacetime metric.

**Uniqueness.** B1252 returns its first SM-histogram match. It does not count
all matches. Our deterministic [-6,6]^3 enumeration in the charge-functional
nullspace for the fixed color/weak subsystem returns two distinct normalized
directions:

```text
(-1/2, -5/6, -1, -5/6, -2/3, -1/6)
(-1/2,  1/6,  0,  1/6,  1/3, -1/6).
```

This is a finite-box result in the specified basis, not a classification of all
real solutions or a claim that the directions are inequivalent under every
normalizer. The full E6 centralizer is three-dimensional. Restricting Y to a
particular SU5 is a narrower problem and may restore the usual one-dimensional
answer. An existence witness is retained even when uniqueness is unproved.

**Anomaly-test provenance.** B1253's anomaly routine defaults to a hard-coded
SM multiplet table; its other tests separately derive the Y histogram. Our new
trace/action check closes that separation for the published witness. A green
test suite alone would not reveal this difference in what was tested.

**Physical selection.** D2 selects a grading conditional on the supplied
twist; this is valuable structure. It does not by itself supply a scalar
potential, its ground state, chiral field multiplicity, measured couplings,
or four-dimensional gravity. The explicit R4 action remains a declared
physical extension, now with a verified connection to the new grading.

## Continuation

Use the full R4 spectrum for the quantum vacuum calculation, preserving the
upstream construction and all earlier results. Existing radiative-potential
hits were read in B962, the B796 mechanism catalog on a fetched branch, and
the separate heterotic/Kähler-scale question map. They do not justify a
repository-wide absence claim. The next cell tests **this explicit action**.

That continuation has now run: [R5](QUANTUM_VACUUM.md) gives independently
verified positive leading angular masses. The upstream action instrument is
also locked by `tests/test_physical_bridge_upstream.py` (post-result regression
tests, hashed and committed before their first execution).
