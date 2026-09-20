# F06 execution and scope receipt

2026-09-20. Command-tool outcomes are transcribed below, not independently
saved raw terminal captures. No scientific source was changed during any
test run. All science uses Python 3.12.1 and SymPy 1.14.0 from the existing
`/Users/dri/.pyenv/versions/3.12.1/bin/python3.12` interpreter.

## First execution and retained failed expectation

Initial source commit: `5ff91aff`, four scientific hashes in SEAL.json.

```
python3.12 -m pytest -q reports/isotropic_parent_core_2026_09_20/test_verify.py
```

Session 72925, initial chunk `694d2f`, final chunk `679e1c`, exit 1:
**1 failed, 16 passed in 4.03 s**. Full returned failure text is retained
in FIRST_RUN.md. The characteristic-polynomial expectation was wrong;
the later assertions in that function were not executed. This is not
described as a wholly successful initial prediction.

The written derivation omitted a term in the positive adjoint norm, not
in the background equations. The producer is unchanged. Correction design,
proof addendum and version-two tests were sealed and committed at
`a06e9423` AFTER the failure and BEFORE the corrected execution.

```
python3.12 -m pytest -q reports/isotropic_parent_core_2026_09_20/test_verify_v2.py
```

Session 63219, initial chunk `aef5c1`, final chunk `864288`, exit 0:
**19 passed in 4.02 s**. Sixteen unchanged original tests are explicitly
enumerated and rerun; the new polynomial/kernel test includes every
unreached old assertion and verifies that the discarded polynomial still
fails. A general complex-component derivation separately constructs both
T and T* actions. A unit-component witness isolates the omitted 1/4 term.

The original failed test file remains sealed and failing by design. It
has not been silently skipped in a claimed repository-wide green run.

## Unchanged antecedent test run

```
python3.12 -m pytest -q --import-mode=importlib \
  reports/nonsplit_admissibility_2026_09_20/test_verify_v2.py \
  reports/complete_domain_2026_09_20/test_verify.py \
  reports/nonsplit_cusp_growth_2026_09_20/test_verify.py \
  reports/full_flag_growth_2026_09_20/test_verify.py \
  reports/parent_twist_gap_2026_09_20/test_verify.py
```

Session 9220, final chunk `412f96`, exit 0:
**86 passed, 1 warning in 23.89 s**. The warning is optional Plink tkinter
GUI availability. The run was live when F06's failure arrived; edits waited
until this handle reported exit 0. Historical F01-v1/R16 failures were not
rerun or erased. No all-suite/gate certificate is claimed.

Post-correction hashes (`b047a7`) match all seven distinct F06 scientific
files across both seals. `git diff --exit-code 28c87f5a` for the five prior
F01--F05 report directories returned exit 0 (`c672d6`). Reporting edits to
the living audit follow these checks; no antecedent science is changed.

## What the controls cover

Full arbitrary-jet matrix flatness and moment residuals; actual parent
charges; isotropic and rank-deficient current comparators; sign duality;
constant-field negative; directly derived Ricci tensor and scalar; a
hyperbolic metric that fails the candidate equations; positive Higgs norm;
the tensor Einstein comparison and its trace-free-Hessian counterexample;
finite proper distance, divergent maximal norm and nonzero boundary flux;
corrected local algebraic operator and nonparallel Higgs tensor.

An ansatz identity valid for arbitrary jets is stronger than testing a
finite set of points. Nevertheless its geometric interpretation, domain
claims and relation to physics are authored arguments, not independent
acceptance. No numerical global PDE, physical eigenvalue computation,
metric matching, four-dimensional gravity, quantum phase or empirical
fit is hidden in these tests.

## Retrieval and reading

The exact queries and reading grades are in DESIGN.md. The already-banked
tool gave broad incidental hits for the first query and no settled result
matching two of three terms in `isotropic coframe conformal`; neither
result is a corpus-wide absence certificate. R39's exact isotropic-Gram
hatch was found and read. The first Git grep used an unquoted shell glob
and failed; a quoted retry returned the intended three R39 references.
The older atlas card is navigation only. No fresh all-head claim is made
given the previous authenticated-fetch failure.

Primary HTML was used for the adopted full equations; no PDF was used and
no agent supplied a summary. No new literature novelty claim, independent
factual review, external publication, push, shared B allocation or other
seat's source edit occurred.
