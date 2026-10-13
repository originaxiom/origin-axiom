import importlib.util
from pathlib import Path
import sympy as s

spec = importlib.util.spec_from_file_location('flag_transport', Path(__file__).with_name('verify.py'))
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)


def test_exact_controls():
    result = v.run()
    assert result['passed'] == len(result['checks'])
    assert result['passed'] > 60
    assert not result['global_mode_count_computed']


def test_wrong_exponent_rejected():
    r, c = s.symbols('r c', real=True)
    ell, b = s.symbols('ell b', positive=True)
    assert v.translated_log_difference(r, ell, b, c, 1/ell, 1) == 0
    assert v.translated_log_difference(r, ell, b, c, 1/ell, 1, 1) != 0


def test_adjoint_is_not_fixed_by_equal_domains():
    d0, d1, gram, adj0, adj1, lap, old, h, changed = v.finite_comparator()
    assert v.zero(adj0*h)
    assert not v.zero(d0.T*h)
    assert not v.zero(lap-old)


def test_differential_change_is_not_norm_comparison():
    d0, d1, *_, changed = v.finite_comparator()
    assert v.zero(d1*d0) and v.zero(changed*d0)
    assert d1.rank() != changed.rank()


def test_lie_and_group_exterior_are_distinct():
    xi = s.diag(1, 1, 1, 1, -4)
    assert v.exterior_lie(xi)[0, 0] == 2
    assert v.exterior_group(xi)[0, 0] == 1
    assert v.exterior_lie(xi)[3, 3] == -3


def test_tracefree_wall_cannot_be_all_positive():
    xi = s.diag(1, 1, 1, 1, -4)
    assert s.trace(xi) == 0
    assert v.exterior_lie(xi).trace() == 0
    assert s.trace(s.eye(5)) != 0
