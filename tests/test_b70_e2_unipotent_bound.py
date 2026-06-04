"""B70 (V45) -- lock the e_2-sector two-block bound on the CORRECT (unipotent) fixed-line object.

At c=n every trace is n, so A is unipotent with (A-I)^n=0; A^a = sum_{j<n} C(a,j) N^j has a-degree
<= n-1, so tr(A^a B A^b B) has bidegree <= (n-1,n-1) = (3,3). This locks the corrected V42 bound
(the generic-eps-series object grows unbounded -- it is NOT what bounds the closure)."""
import importlib.util
import pathlib

import sympy as sp

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "b70_unipotent", _ROOT / "frontier" / "B70_trace_ring" / "e2_unipotent_bound.py")
ub = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ub)


def test_unipotent_two_block_bidegree_capped_at_3_3():
    """Generic full-index nilpotent A (n=4) gives tr(A^a B A^b B) bidegree exactly (3,3)."""
    for seedA, seedB in [(1, 2), (5, 7), (11, 13), (4, 9)]:
        (da, db), _nsmax, _idx = ub.bidegree(seedA, seedB)
        assert da <= ub.n - 1 and db <= ub.n - 1     # <= (3,3)


def test_full_index_nilpotent_is_tight():
    """For a full nilpotency index (n=4), the bidegree is exactly (n-1,n-1)=(3,3) (tight)."""
    (da, db), _nsmax, idx = ub.bidegree(1, 2)
    assert idx == ub.n          # full index 4
    assert (da, db) == (ub.n - 1, ub.n - 1)


def test_unipotent_pow_caps_at_degree_n_minus_1():
    """A^a = (I+N)^a has entries of a-degree <= n-1 (the algebraic source of the bound)."""
    a = sp.symbols("a")
    N = ub.nilpotent(3, lower=False)
    Aa = ub.unipotent_pow(a, N)
    assert max((sp.Poly(e, a).degree() if e.has(a) else 0) for e in Aa) <= ub.n - 1
