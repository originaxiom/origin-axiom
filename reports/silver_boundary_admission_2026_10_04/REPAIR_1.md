# Trivial relative control correction

The first sealed native run stopped before any silver candidate at the
trivial-coefficient control. Its expected relative H1 dimension was wrong
in the preregistration and test: for these one-cusped bundles b1=1, b0=1,
and b2=0, so Poincare-Lefschetz gives h1_relative=b2=0, not 1.
The exact pair-sequence formula already printed in PROOF.md gives the same
answer: 1-1+0=0. Absolute H1=1 and interior H1=0 remain the controls.

NATIVE_FIRST.jsonl preserves the failure. No candidate result was observed.
The repair changes only this expected control and adds diagnostic values to
the native assertion. It does not change any matrix, differential, rank,
input or candidate criterion. The original design remains as sealed; this
dated addendum supersedes its trivial relative expectation. Seal the repaired
source and tests in a new local commit before the second native run.
