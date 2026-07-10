"""B516 locks — golden 3d is golden-specific (only phi gives Pisot via self-reference)."""
import sympy as sp
x = sp.symbols('x')


def _pisot(val):
    mp = sp.minimal_polynomial(val, x)
    mags = sorted(abs(complex(sp.N(r, 20))) for r in sp.Poly(mp, x).all_roots())
    return mags[-1] > 1.0001 and all(m < 0.9999 for m in mags[:-1])


def test_only_golden_gives_pisot_3d():
    results = {}
    for m in range(1, 5):
        met = (m + sp.sqrt(m*m + 4))/2
        results[m] = _pisot(met*(1 + sp.sqrt(met)))
    assert results[1] is True                         # golden: Pisot 3d
    assert all(results[m] is False for m in (2, 3, 4))  # silver+ : not Pisot


def test_golden_minimality_mechanism():
    # the binding conjugate x(sqrt x - 1) < 1 only for golden
    phi = (1 + sp.sqrt(5))/2
    silver = 1 + sp.sqrt(2)
    assert sp.N(phi*(sp.sqrt(phi) - 1)) < 1
    assert sp.N(silver*(sp.sqrt(silver) - 1)) > 1
