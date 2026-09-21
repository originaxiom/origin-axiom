"""Post-failure, separately sealed R42 polynomial equality controls."""
import importlib.util
from pathlib import Path

import sympy as s

PATH = Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/affine_ricci_control_v2.py'
spec = importlib.util.spec_from_file_location('r42_ricci_control',PATH)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def test_same_generic_ricci_identity_as_canonical_and_polynomial_zero():
    ric, gram, variables = m.contraction()
    residual = ric+2*s.eye(3)-gram
    assert m.original.clean(residual) == s.zeros(3)
    assert m.polynomial_zero(residual,variables)
    assert not m.polynomial_zero(s.eye(3),variables)


def test_wrong_constant_curvature_sign_is_detected():
    ric, gram, variables = m.contraction()
    residual = ric-2*s.eye(3)-gram
    assert m.original.clean(residual) == -4*s.eye(3)
    assert not m.polynomial_zero(residual,variables)


def test_wrong_cubic_sign_is_detected_away_from_the_quadric():
    ric, gram, variables = m.contraction()
    residual = ric+2*s.eye(3)+gram
    assert not m.polynomial_zero(residual,variables)
    point = dict(zip(variables,range(1,8)))
    assert residual.subs(point) != s.zeros(3)
    assert (ric+2*s.eye(3)-gram).subs(point) == s.zeros(3)


def test_three_exact_specializations_include_the_quadric_and_nonzero_cubics():
    ric, gram, variables = m.contraction()
    for values in ([0]*7, [1,0,0,0,0,0,0],
                   [s.Rational(-1,2),2,-3,s.Rational(4,3),-5,6,s.Rational(7,4)]):
        point = dict(zip(variables,values))
        assert ric.subs(point) == -2*s.eye(3)+gram.subs(point)
    assert ric.subs(dict.fromkeys(variables,0)) == -2*s.eye(3)


def test_corrected_native_report_rechecks_all_failable_groups():
    result = m.run()
    assert result['checks']
    assert result['all_checks_pass']
    assert all(result['checks'].values())
