# F07 first-run failure, retained

Scientific sources sealed at `e4bd5190` before execution. No edits were
made during either this run or the concurrent antecedent suite.

Command: `python3.12 -m pytest -q reports/core_gluing_invariance_2026_09_20/test_verify.py`

Session 92252, initial chunk `52983a`: `..F........`
Final chunk `76f969`, exit 1 (returned text transcribed below):

```text
......                                                        [100%]
=================================== FAILURES ===================================
______________ test_new_adjoint_and_laplacian_use_the_new_metric _______________

    def test_new_adjoint_and_laplacian_use_the_new_metric():
        d, g = m.acyclic_complex(), m.metric()
        star = m.adjoint(d, g)
>       assert g*star == d.H*g
E       assert Matrix([\n[0, ...          0]]) == Matrix([\n[0, ...     0,   0]])
E         
E         Use -v to get more diff

reports/core_gluing_invariance_2026_09_20/test_verify.py:32: AssertionError
=========================== short test summary info ============================
FAILED reports/core_gluing_invariance_2026_09_20/test_verify.py::test_new_adjoint_and_laplacian_use_the_new_metric
1 failed, 16 passed in 1.10s
```

The rest of that function was not reached. This is not a green initial run.

## Post-failure diagnostic, before the correction seal

An in-memory calculation with the unchanged producer returned chunk
`1e1dab`, exit 0. The only unevaluated residual entry was

    (-1/16 - I/16)*(1 - I) + 1/8.

Entrywise exact simplification returned the zero matrix. The diagnostic
also inspected the later, previously unreached claims: metric self-adjointness
residual zero; characteristic polynomial
`(8*lambda - 1)^2*(9*lambda - 2)^2/5184`; determinant `1/1296`.
These values agree with the frozen expectation, but this diagnostic is
post-failure evidence, not a preregistered second run.

The issue is structural expression equality on unsimplified exact complex
arithmetic. The comparison repair and a deliberately wrong-adjoint control
are separately sealed before execution; no numerical tolerance is introduced.
The original failed file and all four original scientific hashes remain.
