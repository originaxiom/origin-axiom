# R49 post-failure spectrum-comparator diagnostic

September 26, 2026. Seal this design, producer and tests before their
first import/execution. Original scientific seal: f593a2a591ef14aa8070a788eda2176b3d3ff5a3.
No original scientific file or first output is changed.

## Failure and hypothesis

The original native run returned 25 true and two false controls:
potential_full_spectrum and zero_weight_restriction. The displayed
factorizations equal the predictions as printed. Dedicated tests gave
13 passed / 1 failed; the fixed six-file regression gave 79 passed /
2 failed, retaining the separate R47 inverse/dual structural-zero failure.
These are failures, not retroactively green runs.

Read-only inspection of the installed symbolic library found that
charpoly returns a PurePoly whose generator need not be the supplied
symbol. Its generator-selection helper constructs a name through str
and then a new symbol. R49 supplies real=True on Z but subtracts an
expression using the returned generator without identifying them.
Hypothesis: the expressions contain distinct symbols that print as z.
The diagnostic must determine this, not assume it from the output.

## Two-outcome computation

Reconstruct T and its zero-longitude restriction from the unchanged
literal connection matrices and positive Gram metric. Record the
requested and returned generators, their assumptions, equality, and
the original residual predicate. Require rational matrix entries.

Compare characteristic polynomials by their ordered exact QQ
coefficient lists, and independently by expressing the target in the
RETURNED generator. Do not merge general symbols by printed name.
Check the target spectra (0,2,6) with multiplicities (1,3,11) and
(1,3,5) through exact kernel dimensions. Construct the three spectral
projectors as polynomials in T; check their sum, mutual orthogonality,
idempotence, ranks, and reconstruction of T. These matrix identities
do not use the characteristic-polynomial expression comparator.

Two-sided controls: a two-by-two diagonal rational matrix with a
real-assumed requested variable must recover its correct polynomial;
changing one coefficient or changing an eigenvalue 6 to 7 in the
actual T must fail. Different symbols with the same printed name
remain distinct in the ordinary expression predicate. Reject a
polynomial with a genuinely symbolic coefficient instead of treating
it as an exact QQ polynomial by renaming symbols.

If coefficient/rank/projector checks disagree with the predicted
spectra, retain a mathematical discrepancy and do not promote R49's
analytic conclusion. If they agree and the symbol diagnosis is
confirmed, report a corrected COMPARISON in this separate diagnostic,
not a changed original run or a new physical result.

## Execution and scope

Commit/push/server-confirm the three diagnostic files before execution.
Run native and dedicated tests with separate first-run receipts, then
the unchanged original six-file population plus the diagnostic file.
Keep the worktree read-only throughout. The two original failed test
IDs remain visible. No numerical tolerance, new spectrum, new PDE
proof, physical particle count, full-suite-green or independent review
is authorized by this diagnostic.
