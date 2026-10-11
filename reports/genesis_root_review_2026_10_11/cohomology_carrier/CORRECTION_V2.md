# Exact equality correction before the second run

2026-10-11. The first sealed execution exited 1 at the check that the relation annihilates coboundaries. The raw matrix contained unexpanded Gaussian-integer products. Entrywise polynomial expansion gave the exact zero matrix; the normalized relation remained exactly 4I. This was diagnosed after failure, before changing the instrument. It is an expression-comparison defect, not a changed mathematical criterion.

The original verify.py, preregistration and proof remain unchanged. verify_v2.py changes matrix and pair-of-matrix comparisons to exact entrywise polynomial expansion before comparison. All original cases and expected outcomes remain; two explicit controls require the expanded zero to pass and an added nonzero entry to fail. No tolerance, numerical approximation or sample removal is introduced. Hash this correction and the new source before its first execution.

NATIVE_FIRST.txt is retained locally byte-for-byte and ignored only because its traceback contains a private absolute path. NATIVE_FIRST_PUBLIC.txt is a mechanically path-redacted copy; the failure text and line numbers otherwise remain. Both hashes are recorded. The corrected execution must be reported as a second run, never as first-pass success.
