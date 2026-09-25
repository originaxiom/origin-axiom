# F15 custody and reproduction

September 25, 2026. Local branch audit/fork-2026-09-20. Initial state
46f42302 was clean (3915bf); no inherited live scientific session.

## Seal and original failure

DESIGN/PROOF/producer/tests plus the actual F10 import were hashed by
OpenSSL in 55be57 and committed as **8fb4cbcd** (4a8306) before execution.
The initial shasum command failed in Perl locale initialization (c8a920);
it produced no hash and was not used as a seal. No science ran in it.

    python3.12 -m pytest -q reports/projective_deformation_tangent_2026_09_25/test_verify.py

Session 84962: 6b4858 / 12915e, terminal exit 1, **13 failed / 1 passed
in 2.83s**. FIRST_RUN.txt concatenates all actual returned stdout and
tracebacks; FIRST_EXECUTION.json records the chunk/exit metadata.
Only the final newline was normalized when adding the text file.
The rational-field trivial control passed; every exceptional point
failed at the same field-zero trace guard before any actual rank.
Installed ANP equality implementation was read in 48944d; its unsupported
integer comparison explains the failure. It is not a physical negative.

## Corrected seal and complete executions

New correction files only, hashed a297c1, local seal **c3384646**
(1dcc74). The original producer/tests/design/proof remain unchanged.
All original tests are re-exported with the fixed adapter; two explicit
controls reproduce the old guard failure and check the corrected one.

    python3.12 -m pytest -q reports/projective_deformation_tangent_2026_09_25/test_verify_v2.py
    python3.12 -u reports/projective_deformation_tangent_2026_09_25/verify_v2.py

Tests: session 17926, c81e65 / bd7f4e, **16 passed in 25.80s**, exit 0.
Witness producer: session 18196, 137680 / 08ade9, all four exact cases,
exit 0. This producer displays the sealed computation; it is not a
third independent implementation. CORRECTED_TEST_OUTPUT.txt and
EXACT_WITNESSES.jsonl retain the returned stdout. EXECUTION.json carries
the complete tool chunk/exit record without duplicating stdout.

Unchanged antecedents, concurrently read-only:

    python3.12 -m pytest -q --import-mode=importlib \
      reports/projective_geometric_pairing_2026_09_25/test_verify_v2.py \
      reports/projective_fluctuations_2026_09_25/test_verify.py \
      reports/projective_global_metric_2026_09_21/test_verify.py

Session 89664, from 3bd627 through 822d80, **76 passed in 226.10s**,
final exit 0. The intermediate 50-second wait returned a STILL LIVE
session, not completion. The complete concatenated output is retained
in ANTECEDENT_OUTPUT.txt. This is not a whole-repository certificate.
A read-only process-list attempt was sandbox-denied (a7399f); no signal,
source change, permission expansion or process interruption followed.
The normal terminal handle subsequently completed successfully.

No source-tree edits during ANY live scientific run. The eight sealed
scientific/import files rehashed unchanged in ad3340. The full tree was
clean at 44f6a4 while the antecedents ran. After all terminal exits,
9cda2d again confirmed unchanged producer/test/import hashes; only then
were output/report files added. The JSONL witness is explicitly staged
despite the repository's generic JSONL ignore rule; it must not be lost.

No new paper's full-text reading, independent review, fresh all-head
coverage, common B allocation, main mutation, push or external publication.
Living updates are confined to the fork audit, report-guided resweep,
and F14's successor pointer. The old failed files are never overwritten.

Final receipt check 558d00 rehashed all 5 original and 8 corrected seal
entries, reconciled all four witness rows and 30x3 quotient bases with
the reported dimensions, confirmed every corrected run's terminal exit,
verified the preserved 13-failure summary and resolved all 3 local
report links. The exact JSONL ignore rule was identified before staging.
No mathematical expectation was added to the frozen tests after results.
