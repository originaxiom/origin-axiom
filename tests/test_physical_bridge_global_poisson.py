"""R31 checks of necessary identities and independent explicit comparators.

These do not enumerate all compact domains or certify a global PDE proof.
"""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import math

import numpy as np
import pytest

SOURCE = Path(__file__).resolve().parents[1] / 'reports/physical_bridge_2026_09_05/global_poisson.py'
SPEC = spec_from_file_location('physical_bridge_global_poisson', SOURCE)
m = module_from_spec(SPEC)
SPEC.loader.exec_module(m)


@pytest.fixture(scope='module')
def exact():
    return m.exact_controls()


@pytest.fixture(scope='module')
def numeric():
    return m.numerical_controls()


@pytest.mark.parametrize('name', [
    'fermi_distance', 'kernel_radial_equation', 'kernel_flux_minus_one',
    'kernel_stable_identity', 'inside_poisson', 'outside_poisson',
    'value_join', 'derivative_join', 'axis_derivative', 'linear_source_mass',
    'ball_volume_derivative', 'two_cap_mass_limit', 'line_primitive_derivative',
    'line_distance_radicand', 'fixed_height_center_limit', 'sign_reversal',
])
def test_exact_residuals(exact, name):
    assert exact['zero_residuals'][name] == '0'


def test_metric_and_point_normalization(exact):
    assert exact['zero_residuals']['fermi_metric'] == ['0']*9
    assert exact['point_kernel_singular_coefficient'] == '1/(4*pi)'
    assert exact['correct_linear_mass'] == '2*pi*beta'
    assert exact['endpoint_two_ball_mass_slope'] == '16*pi*beta/3'


def test_wrong_kernel_and_transverse_measure_really_fail(exact):
    assert exact['euclidean_wrong_h3_residual_at_one'] < -.01
    assert .7 < exact['normal_disc_wrong_ratio_at_one'] < .9


@pytest.mark.parametrize('index', range(4))
def test_independent_axis_integral(numeric, index):
    row = numeric['line_integrals'][index]
    assert abs(row['error']) < 8e-10+row['positive_tail_bound']
    assert row['positive_tail_bound'] > 0
    assert row['estimated_quadrature_error'] < 8e-10


@pytest.mark.parametrize('index', range(6))
def test_independent_finite_width_convolution(numeric, index):
    row = numeric['tube_convolutions'][index]
    tol = 5e-8*max(1, abs(row['expected']))
    for resolution in ('low', 'high'):
        result = row[resolution]
        assert abs(result['value']-row['expected']) < tol
        assert result['estimated_quadrature_error'] < tol
        assert 0 < result['positive_axial_tail_bound'] < tol
        assert result['interval_certified'] is False
    assert abs(row['resolution_difference']) < tol


def test_boundary_control_does_not_fake_global_log_law(numeric):
    for row in numeric['reflected_line']:
        assert abs(row['error']) < 8e-10
        assert abs(row['boundary_value']) < 1e-13
    discrepancies = [r['boundary_log_discrepancy'] for r in numeric['reflected_line']]
    assert discrepancies[2] > discrepancies[1] > discrepancies[0] > 2
    assert abs(numeric['interior_log_slope']-1) < 2e-5


def test_fixed_height_loses_the_prescribed_residue(numeric):
    rows = numeric['fixed_height']
    assert all(a['beta'] > b['beta'] for a, b in zip(rows, rows[1:]))
    assert all(abs(a['central_field']) > abs(b['central_field']) for a, b in zip(rows, rows[1:]))
    assert abs(rows[-1]['central_field']) < 1e-6
    assert abs(rows[0]['central_field']) > 100*abs(rows[-1]['central_field'])


def test_zero_strength_and_opposite_sign():
    assert m.tube_green_integral(.1, .02, beta=0)['value'] == 0
    assert m.radial_field(0, .02, -1) == -m.radial_field(0, .02, 1)
    assert m.radial_field(0, .02, 1) < 0
    tails = [m.axial_tail_bound(1, z) for z in (4, 8, 14)]
    assert tails[0] > tails[1] > tails[2] > 0


def test_stable_kernel_matches_point_formula():
    distances = np.array([.001, .1, 1.0, 8.0])
    actual = m.green_from_cosh_minus_one(2*np.sinh(distances/2)**2)
    expected = 1/(2*math.pi*np.expm1(2*distances))
    assert np.allclose(actual, expected, rtol=3e-14, atol=0)


@pytest.mark.parametrize('args', [
    (0, .1), (.1, 0), (.1, -.1), (.1, .1), (math.inf, .1),
])
def test_invalid_convolution_geometry_rejected(args):
    with pytest.raises(ValueError):
        m.tube_green_integral(*args)


@pytest.mark.parametrize('options', [{'beta': -1}, {'beta': math.nan},
                                     {'radial_order': 1}, {'angular_order': 2}, {'cutoff': 0}])
def test_invalid_convolution_parameters_rejected(options):
    with pytest.raises(ValueError):
        m.tube_green_integral(.1, .02, **options)


@pytest.mark.parametrize('bad', [0, -1, math.nan, math.inf])
def test_invalid_point_kernel_rejected(bad):
    with pytest.raises(ValueError):
        m.green_from_cosh_minus_one(bad)


def test_native_checks_derive_from_the_rows(exact, numeric):
    checks = m.control_checks(exact, numeric)
    assert len(checks) == 12
    assert all(checks.values())
    damaged = dict(numeric)
    damaged['interior_log_slope'] = 2
    assert not m.control_checks(exact, damaged)['interior_log_coefficient']
