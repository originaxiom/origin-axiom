# F14 post-failure implementation correction, before rerun

September 25, 2026. Original scientific seal 32864821 is unchanged.
The first run ended with **18 failed, 9 passed, KeyboardInterrupt**
after 248.08s, exit 2. It is an INCOMPLETE FAILED run, not a certificate.
FIRST_RUN_REDACTED.txt retains its full emitted output with only the
explicitly marked runtime-path redactions. No scientific negative is
inferred from those failures.

All eighteen executed failures had the same implementation cause:
SymPy's Kronecker construction produced an ImmutableDenseMatrix, but
F11's reused exact reducer mutates rows. The independent diagnostic
reproduced AttributeError at row_swap. The adapter did not reach a
rank verdict. F11/F12/F13's earlier mutable-matrix inputs are unchanged.

The generic expression nullspace was still using CPU after the known
failures. The exact process PID/command was verified before SIGINT.
It subsequently returned KeyboardInterrupt and all failure diagnostics.
A later attempted SIGTERM found no such process and did nothing. The
original run was deliberately interrupted, not silently counted green.
The independent four-file antecedent run completed: 75 passed in 114.35s.

The correction is in new files only:

1. Convert the new equation adapter explicitly to a mutable matrix before
   passing it to the unchanged field reducer.
2. Compute the generic nullspace in the exact rational-function field
   Q(q) using DomainMatrix, instead of general expression simplification.
   Its installed method documentation and signature were inspected;
   its basis vectors are rows. All original entrywise and exceptional-
   specialization checks are retained.
3. Re-export EVERY original test unchanged with its parameterization,
   pointing only its producer to the corrected adapter. Add two controls
   for mutability and the rational-field nullspace convention.

No expected pairing, rank, determinant, geometric certificate, analytic
claim or scope is weakened. No completed scientific prior result was
available to fit. No predecessor scientific file is edited. Seal these
new files and the unchanged inputs before execution, then leave the
source tree read-only again.
