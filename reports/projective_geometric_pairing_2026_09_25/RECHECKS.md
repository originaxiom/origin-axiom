# F14 execution and custody receipt

September 25, 2026. Branch audit/fork-2026-09-20. The previous goal
turn made concrete progress: F13 committed at 0ab31a59. Current state
was rechecked clean in 3008c3 before F14 work; no inherited live job.

## Original seal and instrument failure

Hash receipt 111b61 sealed four new scientific files and five imports.
Explicit staging and whitespace check preceded **32864821** (b5aa7d).
The tree was clean before first execution.

```
python3.12 -m pytest -q reports/projective_geometric_pairing_2026_09_25/test_verify.py
```

Session 12515 began in 969cce. Nine geometric controls passed; all
eighteen executed field tests failed with the SAME AttributeError:
an ImmutableDenseMatrix from the new Kronecker adapter was passed to
the unchanged mutating field reducer. It never produced field ranks.
An independent invocation of the same sealed candidate_certificate
reproduced the exception, session 10195 (85fdc6/c038a7), exit 1.
This was diagnosis of an observed failure, not a duplicate replacement
of the still-live suite or an unsealed mathematical experiment.

While the original suite continued in generic expression nullspace,
read-only process inspection confirmed exact PID 4663 and its command,
CPU usage and elapsed time (09ed92). SIGINT was sent only to that
verified process (0c26da). It was observed live again (12be35); a
subsequent attempted SIGTERM found no such process (7c39ef) and did
nothing. The original handle returned **exit 2, KeyboardInterrupt**,
with full failure diagnostics and **18 failed, 9 passed in 248.08s**
(cf1275). This was an INCOMPLETE FAILED run; remaining tests were not
counted. FIRST_EXECUTION.json records all observed chunks and terminal
states. No observation timeout was equated with process completion.

FIRST_RUN_REDACTED.txt and DIAGNOSTIC_REDACTED.txt preserve complete
emitted output, with explicitly marked repository/home-prefix privacy
substitution only. Pytest's trailing whitespace is deliberately retained.
The original producer, tests, proof and design were not edited.

## Unchanged antecedents

```
python3.12 -m pytest -q --import-mode=importlib \
  reports/projective_fluctuations_2026_09_25/test_verify.py \
  reports/projective_global_metric_2026_09_21/test_verify.py \
  reports/projective_escape_2026_09_21/test_verify.py \
  reports/balanced_vertex_2026_09_20/test_verify.py
```

Session 24170: 97e29a/9d05b9/2f3f85/5b5844/997f87, exit 0.
**75 passed in 114.35s**, preserved in ANTECEDENT_OUTPUT.txt. These
sources were unchanged before and after the adapter repair. This is
a focused four-file suite, not the full repo, slow lane or governance
certificate. F13's separate 149-pass receipt remains preserved.

## Correction seal, before rerun

Only after all original sessions terminated were new correction/output
files added. CORRECTION.md describes both implementation changes:
explicit mutable conversion and rational-function-field generic
nullspace instead of general expression simplification. The installed
DomainMatrix method signature/documentation was read (00dd2a); basis
row convention gets a new control. EVERY original test is re-exported
unchanged, including the fallible theta hypothesis and all parameter
decorators. No expected answer, scope or analytic claim was weakened.

Receipt 709adf hashed the three correction files and all nine unchanged
original/import sources. The first whitespace check correctly flagged
only the byte-preserved pytest transcript (dab63c). Rather than alter
that record, a check excluding ONLY that raw transcript passed; local
commit **5fbf33bd** (b369cb) sealed the correction before execution.
All scientific files passed ordinary whitespace checking.

## Complete corrected execution

```
python3.12 -m pytest -q reports/projective_geometric_pairing_2026_09_25/test_verify_v2.py
python3.12 -u reports/projective_geometric_pairing_2026_09_25/verify_v2.py
```

Corrected tests, session 82251: ef4199/e7d363/b44f86/e0f6ee/a0a9f1.
**40 passed in 158.14s**, final exit 0. The progress line in e0f6ee
was not treated as terminal; a0a9f1 confirmed termination separately.
Corrected witness producer, session 47108:
f24813/ceb77d/5b4c45/bc59fa, final exit 0. It printed all eight exact
base certificates, all sixteen field cases and the symbolic theta
matrix/determinant. This is display of the sealed instrument's output,
not a third independent proof implementation.

CORRECTED_EXECUTION.json records the chunks. CORRECTED_TEST_OUTPUT.txt
and EXACT_WITNESSES.txt concatenate the actual tool-returned stdout.
No source edit occurred during either run; 8f9b1a confirmed no diff.
After BOTH corrected sessions terminated, 02b786 rehashed the original
nine and corrected twelve scientific/source entries, all unchanged.
Only then were new reports/output files created.

## Interpretation and verification limits

Already-banked query and the complete flagged B1208 body read are in
DESIGN. B1279's historic report and relevant producer code were read
personally; its floating arithmetic was not accepted as this exact
certificate. The analytic comparison reuses the stated F10--F13
hypotheses; it is not an independent review of their infinite-domain
proofs. No subagents, full-new-paper claim or latest-all-head absence
assertion. No new shared number, main edit, push or PR.

The explicit theta matrix is a stronger algebraic parameter statement
than the exceptional field sample: its determinant formula never
vanishes for q>0. The global unitary/spectral/interaction statement
is scoped to F12's earned exceptional backgrounds and F13's uniqueness
class, not arbitrary q, all covers or quantum states. F10's fiberwise
negative and all constructive positives remain valid with that scope.

Final report check 53b69f independently rehashed both seals (9 original,
12 corrected entries), resolved 19 local links, reconciled retained
progress dots with the 40/75 terminal pass counts, and counted all 18
original adapter tracebacks plus the interruption in the preserved
record. The new reporting diff passes whitespace checking. Only named
result/receipt and living-report files enter the reporting checkpoint.
