# Publication and verification scope

The first run used pushed seal dd2e5cdc654a02bef6fba0d3c3321884d12b1398 and failed as recorded in FIRST_FAILURE.md. The second used pushed repair seal 4e6a88577cd53581d66882f2dba155b4c8ae2ca8; both remote hashes were confirmed before execution. It completed the native producer, separate-method replay and eight tests with unchanged source hashes. Every published successful output agrees with the wrapper's recorded SHA256. The original failed source remains byte-identical in verify_FIRST.py; failed stdout and receipt are preserved, with only stderr's private path prefixes redacted in its explicitly labelled publication copy.

The second native execution took about 194.28 seconds, the reference 0.73 seconds and the tests process 1.24 seconds. No assertion, expected core control, fixed prime or scientific formula was relaxed after seeing the first partial result. The added normalization guard rejects coefficients outside Q(sqrt(2)). A seal-writing helper was rejected at JavaScript parse time before any tool action; its corrected invocation successfully wrote the repair seal before the second scientific run.

The repository governance runner was checked after staging the result: 25 pass, five fail. The failures are the same existing attribution, path-refs, test-vacuity, seal-provenance and relay-debt categories, with no new packet path cited. The missing B1530 members path, two earlier tests, five earlier seal documents and 42 stale relay debts are not repaired by this work. Seal digests and identification register pass. The runner exits one; a whole-repository green certificate is not claimed. The full test suite was not rerun. Staged whitespace checks pass, and unrelated dirty reports remain unstaged.

This is publication to the audit branch, not a main merge, B-number allocation or canonical proof promotion. Independent review of the radial and global analytic identification remains an explicit duty even though all finite algebraic controls pass. The full physical objective remains active and unachieved.

To replay in a new output directory, use a Python environment with SymPy and pytest:

    python3 reports/genesis_root_review_2026_10_11/weighted_global_complex/execute.py NEW_OUTPUT_DIRECTORY

The wrapper refuses an existing directory and preserves every attempted run, stopping at the first failed process. For a rank-only replay of the published matrices, copy MATRICES.json and RESULTS.json into a new directory and pass that directory to reference.py; it will refuse to overwrite an existing REFERENCE_RESULTS.json. These commands reproduce mathematical checks, not a solved four-dimensional physical theory.
