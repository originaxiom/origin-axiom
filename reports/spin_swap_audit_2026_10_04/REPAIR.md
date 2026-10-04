# Exact expression comparison repair

The first native run after seal d2852f96e passed the full symbolic m003
representation and Fox calculation, then stopped at the literal equality
of two SymPy expressions for 2i sqrt(3). Its complete output remains in
NATIVE_FIRST.jsonl, exit code 1. No later cells ran in that invocation.

A post-failure diagnostic, preserved in FAILURE_DIAGNOSIS.txt, printed
the returned form 2(sqrt(3)+3i)/(sqrt(3)-i), verified that subtracting
2i sqrt(3) simplifies to zero, and printed the expanded complex form.
The repair uses expand_complex followed by expand before the equality
test. It changes the expression representation, not the formula, expected
answer, or scope. Reseal this one-line correction before retrying. The
initial hashes are retained unchanged in ARTIFACT_HASHES.txt.
