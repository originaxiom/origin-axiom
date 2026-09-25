# F12 execution and custody receipt

Draft September 21; resumed, sealed and executed September 25, 2026.
Branch audit/fork-2026-09-20. F11 reporting committed locally as
08ff88e0 (fcdd1e), before any F12 science execution.

## Resume and pre-run review

94f03e confirmed HEAD 08ff88e0 and only the new untracked F12 draft
directory. No inherited scientific process had been started. Manual
pre-seal review corrected the upper-bound polynomial to
4c^2+26cw+18w^2 and ran the real-root counter over Q, not Q(i). The
reciprocal identity was explicitly cancelled before polynomial
reduction. No test output had been inspected; DESIGN records these
pre-execution draft changes.

The first shasum command (a713f8) failed because Perl rejected the
inherited C.UTF-8 locale. No seal or scientific conclusion used it.
A command-scoped C locale succeeded in 586aaa. Seven source/import
hashes were parsed directly from that output into SEAL.json. Explicit
staging and whitespace checking preceded **5579cfb4** (22be4b), leaving
a clean tree.

## First execution, unchanged

Existing Python 3.12.1, SymPy 1.14.0; no installed dependency changes.

```
python3.12 -m pytest -q reports/projective_global_metric_2026_09_21/test_verify.py
```

Session 47794: 5fb5b7, 3ac831, final 80265d, exit 0:
**15 passed in 46.93s**. TEST_OUTPUT.txt concatenates tool-returned
stdout. No failed science run or post-result correction was needed.
This does not erase F11's original three failures or retained earlier
versions of predecessor tests.

The unchanged sealed producer was separately run for actual witnesses:

```
python3.12 -u reports/projective_global_metric_2026_09_21/verify.py
```

Session 57378: df898c, e9f690, final 1856dd, exit 0.
EXACT_WITNESSES.txt concatenates stdout: both fields give dimension 16,
the displayed nonzero reduced determinant, and direct word reconstruction.
The actual matrix norm, excess and tail integral are also retained.
This displays the same sealed instrument's witnesses; it is not an
independent implementation or a numerical global PDE solve.

## Unchanged predecessor and parent checks

```
python3.12 -m pytest -q --import-mode=importlib \
  reports/nonsplit_admissibility_2026_09_20/test_verify_v2.py \
  reports/complete_domain_2026_09_20/test_verify.py \
  reports/nonsplit_cusp_growth_2026_09_20/test_verify.py \
  reports/full_flag_growth_2026_09_20/test_verify.py \
  reports/parent_twist_gap_2026_09_20/test_verify.py \
  reports/isotropic_parent_core_2026_09_20/test_verify_v2.py \
  reports/core_gluing_invariance_2026_09_20/test_verify_v2.py \
  reports/balanced_parent_2026_09_20/test_verify.py \
  reports/balanced_vertex_2026_09_20/test_verify.py \
  reports/projective_escape_2026_09_21/test_verify.py \
  reports/projective_cusp_spectrum_2026_09_21/test_verify_v2.py \
  tests/test_physical_bridge_parent_vertex.py
```

Session 56325: 3a21f2, c0be23, 0bee4a, 248c48, ef77cb, a495b6,
8f6d7b, 94fccf, 4eaae1, final e2688f; exit 0:
**236 passed, 1 warning in 228.52s**. Plink's optional tkinter GUI
was unavailable; these are non-GUI checks. The output file explicitly
marks replacement of the runtime user-home prefix; remaining stdout
is unchanged. This is a focused twelve-file run, not the full repo
or governance certificate. Original failing versions remain preserved.

All runs shared the sealed, read-only source tree. 532997, 466795 and
435612 found no tracked modifications; 466795 returned all seven
unchanged hashes. After every scientific session terminated, 773e5d
rechecked all source/import hashes and clean status before output files
or reporting edits were created. No live process was abandoned or
duplicated. One later multi-file reporting patch failed on an unmatched
context; b2dea8 confirmed it had made no partial report edits. It did
not affect the scientific files or any run.

## Reading and proof assurance

WORKING_RULES was read to its end; grounding/campaign navigation and
already-banked queries are recorded in DESIGN. Both flagged multi-term
settled findings, B1220 and B896, were read completely. B149's code was
inspected directly, including its scalar-commutant warning. Relevant
R28 source-action and F08 parent arguments were reread at interpretation.
Truncated broad outputs were not counted as complete reads or absence
certificates. No fresh remote-head population claim.

Personally read the primary HTML sections listed in DESIGN/FINDINGS,
including the general-dimensional CAT(0) hypotheses and the surface
restriction on Sagman's main theorem. One malformed exploratory URL
returned an internal error and was not evidence. PDF skill instructions
were inspected as a possible fallback, but no PDF was opened or used;
HTML sufficed. No skill-driven artifact action, full-paper reading
claim, new subagent or peer review.

Finite symbolic tests check irreducibility, end energy and elementary
norm identities. The global Dirichlet, compactness, maximum-principle
and Hilbert-complex applications remain an authored analytic argument
with explicit hypotheses. No spatial profile, measured coupling,
quantum gap, dynamical end prescription or gravity solution was
computed. Reports must retain that verification grade.

Final reporting check 81121f found clean whitespace, no scientific diff
from 5579cfb4 and no user-home, temporary-path, TODO or tool-citation
tokens in the F12 files (the last rg returned its normal no-match code).
cd3c65 independently rehashed all seven sealed sources and resolved
25 local links across the F12 and predecessor reports. Only explicit
report/output paths are staged for the reporting checkpoint.
