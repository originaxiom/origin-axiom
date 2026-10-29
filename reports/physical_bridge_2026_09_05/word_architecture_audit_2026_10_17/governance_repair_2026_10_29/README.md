# October 29 governance metadata repair

This package repairs three navigation citations and records 49 named
escalations of still-OPEN relay duties. It changes no scientific verdict,
row date, BANKED/DECLINED/OPEN disposition, frozen P210 source or checker.
Historical seal failures are retained. The exact-reference repair was
committed separately at db1d44b69; this package does not alter its policy.

REPAIR_RECEIPT.json binds the original and repaired document bytes and
the immutable target blobs. STALE_RELAY_ESCALATIONS_2026_10_29.json names
all 49 debts with original-row hashes and next actions; it does not assert
that all their proofs or later dispositions have been re-verified.

The ledger already has staged work. An alternate Git index commits only
the authored metadata delta; the ordinary index and worktree retain their
prior data. index_preservation_fixture.py tests that operation on an
isolated synthetic Git repository, including rejecting missing/ambiguous/
already-modified rows. The successful fixture proves inverse recovery of
all original bytes, preservation of unrelated staged data, and unchanged
staged hunks apart from expected blob identities. Preliminary attempts
are disclosed in the receipt: a syntax error before execution and a
synthetic-only assertion about unchanged Git diff bytes. Neither touched
the real ledger. No scientific imports or computations occur in the fixture.

Working-tree diagnostics are metadata evidence, not a clean-clone
execution certificate. The independently accepted P210 package still needs
a fresh quiescent strict preflight and its literal source-bound command.
No scientific test pass or global governance-green result is claimed here.
