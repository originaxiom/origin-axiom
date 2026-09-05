"""B1252 — the Cartan metric on the B854 basis, and the descent to one SM generation.

Pins the TWO validations that were not imposed when solving for the metric, and the
unique hypercharge assignment.
"""
import importlib.util, pathlib
from fractions import Fraction as F
_SRC = (pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1252_metric_and_descent"
        / "verification" / "cartan_metric_and_descent.py")
_s = importlib.util.spec_from_file_location("b1252", _SRC)
md = importlib.util.module_from_spec(_s); _s.loader.exec_module(md)
_M = md.cartan_metric()


def test_the_naive_dot_product_is_NOT_the_metric():
    """The error this arc exists to prevent: 7 root lengths in a simply-laced algebra."""
    import collections
    lens = collections.Counter(sum(x * x for x in a) for a in md.roots().values())
    assert len(lens) > 1, "if this ever passes, the basis became orthonormal and the arc is moot"


def test_metric_is_unique_and_validates_on_conditions_not_imposed():
    assert not _M.free_symbols, "no free parameters"
    rl, wl = md.validate_metric(_M)
    assert list(rl) == [2] and sum(rl.values()) == 72, f"simply-laced: one root length, got {rl}"
    assert len(wl) == 1 and sum(wl.values()) == 27, f"minuscule 27: one weight length, got {wl}"


def test_the_descent_yields_one_SM_generation_with_correct_hypercharges():
    y, gr, nsub = md.descent()
    assert y is not None, "no Y reproducing the SM hypercharges"
    assert gr == {F(1, 6): 6, F(-2, 3): 3, F(1, 3): 3, F(-1, 2): 2, F(1): 1, F(0): 1}
    assert nsub > 0
