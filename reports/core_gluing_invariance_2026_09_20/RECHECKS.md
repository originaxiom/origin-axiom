# F07 execution, coverage and reading receipt

2026-09-20. Scientific interpreter: Python 3.12.1, SymPy 1.14.0, from the
same existing environment used for F05/F06. Commands below abbreviate its
absolute interpreter path as python3.12. Returned output is transcribed,
not an independently saved raw terminal log.

## Execution chronology

1. `env LC_ALL=C LANG=C shasum -a 256` on DESIGN.md, PROOF.md, verify.py,
   test_verify.py returned the original four seal hashes (`7629d5`).
2. Sources and SEAL.json committed at `e4bd5190` before execution.
   Initial staged whitespace check passed (`f4903f`).
3. `python3.12 -m pytest -q reports/core_gluing_invariance_2026_09_20/test_verify.py`
   returned **1 failed, 16 passed in 1.10 s**, exit 1; session 92252,
   initial chunk `52983a`, final `76f969`. See FIRST_RUN.md.
4. In-memory diagnostic (`1e1dab`, exit 0) expanded the exact residual to
   zero and inspected the polynomial and determinant. This happened AFTER
   the failure and BEFORE the correction design/seal; it is not blinded.
5. The concurrent antecedent run below completed before any file edits.
6. Correction design and test hashes were computed (`37d2e7`), then
   committed with SEAL_V2.json and the first failure at `7fe4e822`.
   `git diff --cached --check` returned exit 2 (`bde1bb`) for the retained
   pytest transcript's whitespace-only `E` line in FIRST_RUN.md. That
   transcript whitespace was preserved; this is not a claimed green check.
7. `python3.12 -m pytest -q reports/core_gluing_invariance_2026_09_20/test_verify_v2.py`
   returned **18 passed in 0.98 s**, exit 0; session 98747, initial chunk
   `1c19ef`, final `627f6f`. No source was edited during a test run.

## Unchanged antecedent run

```
python3.12 -m pytest -q --import-mode=importlib \
  reports/nonsplit_admissibility_2026_09_20/test_verify_v2.py \
  reports/complete_domain_2026_09_20/test_verify.py \
  reports/nonsplit_cusp_growth_2026_09_20/test_verify.py \
  reports/full_flag_growth_2026_09_20/test_verify.py \
  reports/parent_twist_gap_2026_09_20/test_verify.py \
  reports/isotropic_parent_core_2026_09_20/test_verify_v2.py
```

Session 75473, initial `13e217`, intermediate `c6c0e0`, final `84143c`:
exit 0, **105 passed, 1 warning in 23.28 s**. The warning concerns optional
Plink tkinter GUI availability. Retained F01-v1, R16 and F06-v1 failures
are not included or erased. This selected regression suite is not the
full repository suite or governance-gate certification.

Post-run hashes for all six scientific files match their seals (`bd72e5`).
`git diff --exit-code 81980ab2 --` the six F01--F06 report directories
returned exit 0 (`bba2f3`) before their living findings were updated.

## Reading and evidence boundaries

Personally read F05's complete proof and F06's corrected findings; the
earlier research segment read R26's index-stability proof, R27's finite-
twist proof, R32's source-C3 proof, R18's closed-range section and R30's
resolved-fermion sections 1--3. R30's full proof was then reread here.
No subagent summary was used. Existing governance readings are prior;
WORKING_RULES.md was reread before execution.

The report-guided all-history search remains the earlier pinned inventory,
not a new enumeration this checkpoint. The targeted already_banked query
`bounded homotopy equivalent norm` returned 131 broad hits and 11 settled
hits matching at least two terms; it supplied navigation, not an absence
certificate. Code, report bodies and LAW_MAP/OPEN_LEADS searches recovered
the credited R18/R26/R27/R30 antecedents. No novelty claim is made.

Primary HTML: [Holt--Piovani arXiv:2310.08993v2](https://arxiv.org/html/2310.08993v2),
section 4 through Lemma 4.3 and its proof, personally read and rechecked.
Only the elementary Hilbert-space decomposition/closed-range results are
used. No full-paper reading, PDF inspection, complex-geometric theorem
transfer, or arbitrary unbounded self-adjoint sum assertion is claimed.

The global norm/holonomy comparison and van Kampen gluing application
are authored analytic arguments. Finite controls verify exact algebra,
nonunitary-adjoint distinctions, failure mechanisms and norm scaling;
they do not certify a global PDE, a physical spectrum or the proof by an
independent expert. No empirical input or measured physical constant is used.
