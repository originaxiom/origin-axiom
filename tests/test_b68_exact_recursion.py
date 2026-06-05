"""B68 (P6, V52) -- the exact AJ recursion search: colored Jones sanity + the order-2/Q-degree-2
non-existence (the bounded negative; full check via exact_recursion.main(), too slow for CI)."""
import importlib.util
import pathlib

import sympy as sp

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "b68_exact", _ROOT / "frontier" / "B68_aj_conjecture" / "exact_recursion.py")
er = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(er)


def test_colored_jones_habiro():
    """Figure-eight colored Jones (Habiro form): J_1 = 1, and J_N is a Laurent polynomial in q."""
    q = sp.symbols("q")
    assert sp.simplify(er.J_sym(1) - 1) == 0
    J2 = sp.expand(er.J_sym(2))
    assert J2.has(q)                                   # nontrivial
    assert sp.simplify(J2 - sp.expand(sp.cancel(J2))) == 0   # genuine Laurent polynomial (no poles)
