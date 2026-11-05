# Independent F1/F2 disposition — 2026-11-05

Exact review seal: `1f11431e74f40f868f237d1ca65fa736d9c0ccae`.

**F1 and F2 are addressed in the exact source at this seal.** No new concrete error was found in these two corrections. The original R1/R2 repairs and R3 coverage assessment are retained from the preceding review. The outstanding source findings from these reviews are therefore resolved within their stated scope; this is not a scientific pass, runtime certificate or execution acceptance.

The first review against `bfcff0e80` and the blocked follow-up against `fca1ce32c`, preserved at `dc4f2ba56` and `3d3277f86` respectively, remain unchanged. Their historical bytes do not acquire a later acceptance verdict.

## F1: carrier metric and the full source-binding matrix

Disposition: **ADDRESSED IN SOURCE / HAND CHECKED / UNRUN**.

At `verification_transport_end_2026_11_04/checks.py:467–480`, the probe now constructs the source trace Gram from the actual E,F,H matrices. It is diag(1,1,2). The displayed S=diag(1,1,sqrt(2)) satisfies S-dagger*S=G and maps source coefficient coordinates to an orthonormal carrier. Both probe Lie operators are transported by S, and the old complete source mass matrix is conjugated by the same isometry on every one of its four slots.

This is the required correction. In source coordinates the compact-adjoint identity is

    ad(q dagger) = G^-1 ad(q) dagger G.

Since G=S^2 with S real positive diagonal, it follows that

    (S ad(q) S^-1) dagger = S ad(q dagger) S^-1.

The new assertion at lines 474–475 checks that equality for the actual probe. The old wrong-adjoint comparison is retained as an unequal-matrix control at line 476; it still discriminates the non-orthonormal E,F,H basis from an orthonormal one.

Every derivative-only block is a scalar multiple of the carrier identity and commutes with S. Every Higgs block is transported by the same similarity, including the blocks involving compact adjoints. Therefore the new helper matrix agrees block by block with the four-slot conjugation of `OLD.physical_mass`, which is the equality now asserted at line 480. The correction transports the target as well as the source and does not discard any of the gaugino or trace-dual spin couplings. The unequal scalar/form/spin density factors commute with this carrier isometry and remain in their original slots.

Ordinary dagger on the actual orthonormal E8 summands remains appropriate. Those carriers and their full-word comparison loop were not changed by this correction.

## F2: independent coefficient and profile norms

Disposition: **ADDRESSED IN SOURCE / HAND CHECKED / UNRUN**.

At `verification_transport_end_2026_11_04/checks.py:561–562`, the actual E8 trace projection now keeps the name `coefficient_norm`. The later radial profile uses the distinct `bump_norm` at lines 578–582. The charge quotient at lines 604–605 divides by `60*coefficient_norm`; the profile integral at line 609 divides by `bump_norm`.

For the same actual colour coefficient, the reviewed representation data give coefficient_norm=1 and [X,T]=2T. The corrected trace quotient is consequently 120/(60*1)=2. The bump s^2(1-s)^2 has squared integral 1/630, which now enters only the radial profile normalization and derivative residual. The explicit inequality at line 607 makes that distinction visible. The normalized overlap is the charge times the integral of bump^2/bump_norm, hence two, and the stated vertex normalization remains 2*g6/sqrt(area).

The previous accidental factor 630 no longer enters the charge. No global trace normalization, radial measure or physical interaction was changed to force this repair.

## Envelope and remaining admission

The exact diff from `fca1ce32c`, the changed source ranges, `ADJOINT_AND_NORM_REPAIRS.md` and `SOURCE_REVIEW_INVENTORY_V3.json` were inspected. The receipt records that only the transport science source changed between the two seals; the geometric source and prior proof/review artifacts retain their pinned bytes. Source hashes and the thirteen method names were checked with standard-library tools only. No scientific module was imported, no test was collected or run, and no CAS or numerical calculation was executed.

No outstanding F1/F2 source blocker remains at this seal. The eight-method transport and five-method geometric packages both remain **UNRUN / NOT ADMITTED**. The earlier conditional mathematical scope, supplied physical inputs and global proof qualifications are unchanged. Main's exact separate acceptance, runtime and infrastructure closure, and strict prospective admission are still required before scientific execution.

The prospective wrapper engineering design has no implementation or fixture result in this review and is expressly outside this F1/F2 disposition. No wrapper or execution-readiness verdict is inferred.

No authored code/proof or Git staging was changed by this reviewer. This report and its distinct receipt are the only new reviewer outputs for this follow-up.
