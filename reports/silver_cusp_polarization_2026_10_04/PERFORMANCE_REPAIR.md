# Exact conversion performance repair

The first native run, sealed in ec523543a, passed the peripheral comparator
cell. It was intentionally interrupted after 4 minutes 57 seconds at full
CPU use while converting entries in the first member's exterior-square
cup pairing. Exit code 130 and the complete partial output and traceback
remain in NATIVE_FIRST.jsonl. This is not a scientific failure or a result
for the four-member population. No member receipt had yet been printed.

Before the interruption, a small profile of ten conversions of a 2 by 2
matrix found 0.860 of 0.873 seconds inside conversion, repeatedly computing
field isomorphisms and minimal polynomials. CONVERSION_PROFILE.txt preserves
that diagnostic. The interrupted stack independently locates the same
generic conversion. A restricted process-list request initially failed;
an authorized read confirmed the exact process and CPU use before it was
interrupted. No other process was signaled.

The repair explicitly converts an entry a+b sqrt(2)+ci+di sqrt(2) into
the already fixed algebraic field, caching entry conversions. Real and
imaginary parts are rationalized and rational coefficients asserted; this
is not a floating-point recognition step. Add 84 exact comparisons with
the original generic converter, including reciprocals, before any member
is tested. Add one progress event per member. No mathematical criterion,
source matrix, expected count, dual convention or proof is changed.

Seal the repaired code and tests before rerunning. The initial science
hashes remain in ARTIFACT_HASHES.txt; the replacement hashes are recorded
separately. All previous global-profile and covariance controls remain.
