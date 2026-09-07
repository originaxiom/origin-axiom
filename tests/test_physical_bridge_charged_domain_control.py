"""Recheck R16's exact assertions with separately sealed instrument repairs."""
import importlib.util
from pathlib import Path

import sympy as sp

_ROOT = Path(__file__).resolve().parents[1]


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


control = _load('charged_control', _ROOT / 'reports/physical_bridge_2026_09_05/charged_domain_control.py')
original_tests = _load('charged_original_assertions', Path(__file__).with_name('test_physical_bridge_charged_domain.py'))
# Only this private test-module instance is rebound; the collected original
# test file and its immutable source retain their first-run behavior.
original_tests.cd = control.base


def test_exact_modes_and_two_sided_zero_simplification():
    cd = control.base
    assert all(row['d'] == row['delta'] == {} for row in cd.line_modes())
    assert control.simplify(1+sp.sinh(cd.r)**2) != 0
    radial = next(row for row in cd.line_modes() if row['basis'] == (0,))
    bad = cd.HYP.deltaq({(0,): radial['coefficient'].subs(cd.a, 2)}, {(0,): 3/cd.HYP.volume})
    assert bad != {}
    original_tests.test_all_eight_exact_hyperbolic_zero_branches()
    original_tests.test_hodge_square_and_twisted_differential_square()
    original_tests.test_wrong_volume_and_wrong_norm_measure_are_detected()


def test_capacity_by_differentiated_primitive_and_original_assertions():
    out = control.boundary_identities()
    assert out['primitive_derivative'] == 0
    assert out['energy_primitive_derivative'] == 0
    assert out['capacity_energy_identity'] == 0
    assert out['cutoff_normalization'] == 1
    original_tests.test_nonzero_green_form_and_distinct_complex_domains()


def test_scaled_quadrature_meets_original_unchanged_tolerances():
    rows = control.numerical_norm_controls()
    assert len(rows) == 168
    assert max(row['quadrature_relative_error'] for row in rows) < 5e-12
    assert max(row['hyperbolic_relative_correction'] for row in rows) < 1e-3
    original_tests.test_independent_quadrature_and_actual_hyperbolic_measure()


def test_real_log_identity_keeps_both_signs_and_neutral_case():
    out = control.cusp_identities()
    assert out['exponential_log_identity'] == 0
    C, q = sp.Symbol('C', positive=True), sp.Symbol('q', real=True)
    for value in (-2, 0, 2):
        assert out['leading_log_density'].subs(q, value) == -2*C*value
    original_tests.test_general_zero_and_top_solutions_and_cusp_separation()
    original_tests.test_global_extreme_degrees_do_not_confuse_cusp_decay_with_line_l2()


def test_angular_and_critical_controls_are_unchanged():
    cd = control.base
    assert cd.hyperbolic_indicial_matrix() == cd.angular_matrix()
    assert cd.critical_eigenvalues(sp.Rational(1, 2), 0) == [0, 0]
    assert cd.critical_eigenvalues(1, 0) == []
    original_tests.test_generic_angular_matrix_derived_from_d_and_hodge()
    original_tests.test_half_density_normalization_and_critical_window()
