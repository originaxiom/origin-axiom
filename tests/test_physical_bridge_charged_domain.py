"""R16 mathematical controls; local normal-domain results are not global H1."""
import importlib.util
from pathlib import Path

import pytest
import sympy as sp

_SOURCE = Path(__file__).resolve().parents[1] / 'reports/physical_bridge_2026_09_05/charged_domain.py'
_SPEC = importlib.util.spec_from_file_location('physical_bridge_charged_domain', _SOURCE)
cd = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(cd)


def test_hodge_square_and_twisted_differential_square():
    for j in cd.BASIS:
        form = {j: cd.r**2*sp.cos(cd.theta)*(1+cd.t)}
        assert cd.HYP.star(cd.HYP.star(form)) == cd.clean(form)
        dH = {(0,): cd.a/cd.HYP.volume}
        assert cd.HYP.dq(cd.HYP.dq(form, dH), dH) == {}


def test_all_eight_exact_hyperbolic_zero_branches():
    rows = cd.line_modes()
    assert len(rows) == 8 and {r['basis'] for r in rows} == set(cd.BASIS)
    for row in rows:
        assert row['d'] == {} and row['delta'] == {}
    expected = [-cd.a, cd.a-1, -cd.a-1, -cd.a, cd.a, cd.a-1, -cd.a-1, cd.a]
    assert [row['exponent'] for row in rows] == expected


def test_wrong_volume_and_wrong_norm_measure_are_detected():
    radial = next(row for row in cd.line_modes() if row['basis'] == (0,))
    c = radial['coefficient'].subs(cd.a, 2)
    wrong = cd.MetricForms((1, 1, 1))
    assert wrong.deltaq({(0,): c}, {(0,): 2/cd.HYP.volume}) != {}
    assert cd.integrable(-sp.Rational(3, 4))
    assert not cd.integrable(-sp.Rational(3, 4), measure_power=0)
    assert not cd.integrable(-1)


@pytest.mark.parametrize('charge,expected', [
    (-2, [(), (1,), (2,), (1, 2)]),
    (-1, [(), (1,), (2,), (1, 2)]),
    (-sp.Rational(1, 2), [(), (1,), (2,), (0, 1), (1, 2), (0, 1, 2)]),
    (0, [(), (2,), (0, 1), (0, 1, 2)]),
    (sp.Rational(1, 2), [(), (0,), (2,), (0, 1), (0, 2), (0, 1, 2)]),
    (1, [(0,), (0, 1), (0, 2), (0, 1, 2)]),
    (2, [(0,), (0, 1), (0, 2), (0, 1, 2)]),
])
def test_thresholds_keep_every_form_degree(charge, expected):
    assert cd.integrable_components(charge) == expected
    dual = {tuple(i for i in range(3) if i not in j) for j in expected}
    assert dual == set(cd.integrable_components(-charge))


def test_generic_angular_matrix_derived_from_d_and_hodge():
    l, a, m, I = cd.lam, cd.a, cd.m, sp.I
    expected = sp.Matrix([[0, -l-1+a, -I*m, 0],
                          [l+a, 0, 0, I*m],
                          [I*m, 0, 0, -l+a],
                          [0, -I*m, l+1+a, 0]])
    full = cd.angular_matrix()
    assert full == sp.diag(expected, expected)
    assert cd.hyperbolic_indicial_matrix() == full
    assert sp.factor(full[:4, :4].det()) == sp.factor((a*a+m*m-l*l)*(a*a+m*m-(l+1)**2))
    assert expected.subs(m, 0).det().subs({a: sp.Rational(3, 2), l: 0}) != expected.det().subs({a: sp.Rational(3, 2), l: 0, m: 1})


def test_half_density_normalization_and_critical_window():
    J, A = cd.normalized_tangential()
    assert J*J == -sp.eye(4) and J.H == -J
    assert A == A.H and J*A+A*J == sp.zeros(4)
    x = sp.Symbol('x')
    nu2 = cd.a**2+cd.m**2
    target = ((x-sp.Rational(1, 2))**2-nu2)*((x+sp.Rational(1, 2))**2-nu2)
    assert sp.expand(A.charpoly(x).as_expr()-target) == 0
    assert cd.critical_eigenvalues(sp.Rational(1, 2), 0) == [0, 0]
    for charge in (-2, -1, 0, 1, 2):
        assert cd.critical_eigenvalues(charge, 0) == []
    for charge in (-2, -sp.Rational(1, 2), 0, sp.Rational(1, 2), 2):
        for m in (-3, -2, -1, 1, 2, 3):
            assert cd.critical_eigenvalues(charge, m) == []
    # Failing to transform the r dr density shifts the spectrum incorrectly.
    wrong = A+sp.eye(4)/2
    assert wrong.subs({cd.a: 0, cd.m: 0}).det() == 0
    assert A.subs({cd.a: 0, cd.m: 0}).det() != 0


def test_nonzero_green_form_and_distinct_complex_domains():
    out = cd.boundary_identities()
    assert out['green_pair'] == 1
    assert out['radial_d_cutoff'] == {} and out['scalar_delta_cutoff'] == {}
    assert out['scalar_d_cutoff'] != {} and out['radial_delta_cutoff'] != {}
    assert out['capacity_energy_identity'] == 0
    assert out['cutoff_normalization'] == 1
    # At a=1/2 both paired modes have lambda=-1/2: norm converges,
    # but their D graph-cutoff capacity tends to 1/R, not zero.
    assert cd.integrable(-sp.Rational(1, 2))
    assert cd.capacity(-0.5, 1e-8, 0.01) == pytest.approx(1/(0.01-1e-8))
    # Critical lambda=0 has logarithmic zero capacity, no finite trace debt.
    assert cd.capacity(0, 1e-8, 0.01) < cd.capacity(0, 1e-4, 0.01)


def test_independent_quadrature_and_actual_hyperbolic_measure():
    rows = cd.numerical_norm_controls()
    assert len(rows) == 7*8*3
    assert max(r['quadrature_relative_error'] for r in rows) < 5e-12
    assert max(r['hyperbolic_relative_correction'] for r in rows) < 1e-3
    # Critical scalar at a=1 diverges logarithmically with shrinking tube.
    critical = [r for r in rows if r['a'] == 1 and r['basis'] == ()]
    assert not any(r['integrable'] for r in critical)
    assert critical[-1]['hyperbolic_quad'] > 2.9*critical[0]['hyperbolic_quad']


def test_general_zero_and_top_solutions_and_cusp_separation():
    out = cd.cusp_identities()
    assert out['scalar_equation'] == {} and out['top_equation'] == {}
    assert out['separated_norm_identity'] == 0
    C = sp.Symbol('C', positive=True)
    q = sp.Symbol('q', real=True)
    assert out['leading_log_density'] == -2*C*q


def test_global_extreme_degrees_do_not_confuse_cusp_decay_with_line_l2():
    density = ((1, 1, 1), (1, 1, 1))
    assert cd.extreme_l2(sp.Rational(1, 2), density) == dict(scalar=True, top=False)
    assert cd.extreme_l2(-sp.Rational(1, 2), density) == dict(scalar=False, top=True)
    assert cd.extreme_l2(0, density) == dict(scalar=True, top=True)
    for q in (-2, -1, 1, 2):
        assert cd.extreme_l2(q, density) == dict(scalar=False, top=False)
    assert cd.extreme_l2(sp.Rational(1, 2), ((1, 2, 1), (1, 1, 2)))['scalar'] is False
    for bad in ((), ((),), ((1, 0),), ((1, -1),)):
        with pytest.raises(ValueError):
            cd.extreme_l2(1, bad)
