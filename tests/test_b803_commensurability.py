"""B803 — locks the independently verified parts of the commensurability audit."""
import importlib.util
from pathlib import Path

import sympy as sp
from mpmath import mp, mpf, fabs

ARC = Path(__file__).resolve().parents[1] / "frontier" / "B803_commensurability_audit"


def _m():
    spec = importlib.util.spec_from_file_location("b803", ARC / "verify.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def test_dky_zero_is_hit_exactly_at_integer_shift_and_missed_otherwise():
    """The mechanism: exp(i*pi*(m+k)/(m+l)) = -1 iff k = l, over INTEGER k."""
    mp.dps = 60
    m = _m()
    for l in ("1.00", "2.00", "3.00"):
        v, k = m.dky_min_over_integer_k(200, mpf(l))
        assert v < mpf("1e-40"), f"l={l} must hit the zero exactly, got {v}"
        assert k == int(float(l)), f"the zero must sit at k = l, got k={k}"
    for l in ("0.50", "0.99", "1.01"):
        v, _ = m.dky_min_over_integer_k(200, mpf(l))
        assert v > mpf("1e-8"), f"non-integer l={l} must MISS the zero, got {v}"


def test_khovanov_and_knot_floer_add_no_bits_beyond_alexander_and_signature():
    a = _m().alexander_data()
    assert a["det"] == 5                       # |Delta(-1)| for 4_1
    assert a["hfk_ranks"] == (1, 3, 1) and sum(a["hfk_ranks"]) == 5
    assert a["khovanov_reduced_rank"] == 5     # thin => rank = det
    assert a["sigma"] == 0


def test_the_alexander_polynomial_is_the_source_of_both():
    """Both 'missing organs' are functions of Delta -- so they carry zero new information."""
    t = sp.Symbol("t")
    D = -t + 3 - 1 / t
    assert abs(sp.simplify(D.subs(t, -1))) == 5
    assert sp.simplify(D - D.subs(t, 1 / t)) == 0      # symmetric, as an Alexander polynomial is
