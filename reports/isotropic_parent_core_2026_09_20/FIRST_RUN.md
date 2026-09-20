# F06 first execution: retained failure

Sealed source commit `5ff91aff`. Python 3.12.1, SymPy 1.14.0.
Command: `python3.12 -m pytest -q reports/isotropic_parent_core_2026_09_20/test_verify.py`.
Session 72925. Initial chunk `694d2f` contained `..`. Final chunk `679e1c`
reported exit 1. The final output is transcribed below, without correcting
its assertion. This is a command-tool transcription, not an independently
saved raw terminal file.

```
.............F.                                                        [100%]
=================================== FAILURES ===================================
_ test_center_algebraic_operator_has_exact_kernel_but_is_not_the_full_Laplacian _

    def test_center_algebraic_operator_has_exact_kernel_but_is_not_the_full_Laplacian():
        h = m.center_h(1)
        lam = s.symbols('lam')
        assert h == h.H
>       assert s.factor(h.charpoly(lam).as_expr()-lam**5*(lam-s.Rational(1, 2))**6*(lam-s.Rational(3, 4))) == 0
E       AssertionError: assert -lam**5*(2*lam - 1)**3*(4*lam - 3)*(48*lam**2 - 60*lam + 19)/2048 == 0
E        +  where -lam**5*(2*lam - 1)**3*(4*lam - 3)*(48*lam**2 - 60*lam + 19)/2048 = <function factor at 0x111f86840>((lam**12 - 9*lam**11/2 + 69*lam**10/8 - 73*lam**9/8 + 1473*lam**8/256 - 1107*lam**7/512 + 459*lam**6/1024 - 81*lam**5/2048 - (((lam ** 5) * ((lam - 1/2) ** 6)) * (lam - 3/4))))
E        +    where <function factor at 0x111f86840> = s.factor
E        +    and   lam**12 - 9*lam**11/2 + 69*lam**10/8 - 73*lam**9/8 + 1473*lam**8/256 - 1107*lam**7/512 + 459*lam**6/1024 - 81*lam**5/2048 = as_expr()
E        +      where as_expr = PurePoly(lam**12 - 9/2*lam**11 + 69/8*lam**10 - 73/8*lam**9 + 1473/256*lam**8 - 1107/512*lam**7 + 459/1024*lam**6 - 81/2048*lam**5, lam, domain='QQ').as_expr
E        +        where PurePoly(lam**12 - 9/2*lam**11 + 69/8*lam**10 - 73/8*lam**9 + 1473/256*lam**8 - 1107/512*lam**7 + 459/1024*lam**6 - 81/2048*lam**5, lam, domain='QQ') = charpoly(lam)
E        +          where charpoly = Matrix([\n[3/4,   0,    0,    0,   0,    0,   0,   0,   0,   0,   0,   0],\n[  0, 1/4,    0,    0,   0,    0, 1/4,   ...   0,   0,    0,   0, -1/4,   0,    0,  1/4,   0],\n[  0, 1/4,    0,    0,   0,    0, 1/4,    0,   0,    0,    0, 1/4]]).charpoly
E        +    and   1/2 = <class 'sympy.core.numbers.Rational'>(1, 2)
E        +      where <class 'sympy.core.numbers.Rational'> = s.Rational
E        +    and   3/4 = <class 'sympy.core.numbers.Rational'>(3, 4)
E        +      where <class 'sympy.core.numbers.Rational'> = s.Rational

reports/isotropic_parent_core_2026_09_20/test_verify.py:140: AssertionError
=========================== short test summary info ============================
FAILED reports/isotropic_parent_core_2026_09_20/test_verify.py::test_center_algebraic_operator_has_exact_kernel_but_is_not_the_full_Laplacian
1 failed, 16 passed in 4.03s
```

The failed polynomial assertion prevented later assertions in that function
from executing. In particular, the kernel dimension and explicit kernel
vectors were not certified by the first run. Sixteen other tests passed,
including the full BPS residual and curvature/boundary controls.

The independent antecedent run was already live when this result arrived;
no file edits occurred until it terminated. Session 9220, final chunk
`412f96`, exit 0: 86 passed, 1 optional Plink GUI warning in 23.89 s.

The analytic diagnosis and changed expectation are POST-FAILURE, in
CORRECTION_DESIGN.md and PROOF_V2_ADDENDUM.md. The original design, proof,
producer and failing test remain unchanged. No whole-suite green claim.
