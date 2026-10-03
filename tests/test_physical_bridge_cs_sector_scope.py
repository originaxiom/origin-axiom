"""R82 scope controls; a nonconstant action is not a quantum or SM result."""
import importlib.util
from pathlib import Path

import sympy as s


ROOT = Path(__file__).resolve().parents[1]


def load(name):
    path = ROOT/'reports/physical_bridge_2026_09_05'/f'{name}.py'
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


N = load('cs_sector_scope')
R = load('cs_sector_scope_control')


def test_scalar_identity_survives_but_has_narrow_scope():
    data = N.run()
    assert data['checks']['scalar_geometric_identity']
    assert data['checks']['scalar_value_blind_at_CS0']
    assert data['checks']['k_derivative_off_shell']


def test_contact_density_retains_all_bump_derivatives():
    c = N.contact()
    assert s.expand(c['density'] - c['expected']) == 0
    assert c['cubic'] == 0


def test_zero_value_stationary_background_has_nonzero_hessian():
    c = N.contact()
    assert c['density'].subs(c['eps'], 0) == 0
    assert s.diff(c['density'], c['eps']).subs(c['eps'], 0) == 0
    assert s.diff(c['density'], c['eps'], 2) != 0


def test_curvature_excludes_gauge_copy_of_flat_reference():
    assert any(A != s.zeros(2) for A in N.contact()['curvature'].values())


def test_orientation_pairs_nonzero_fields():
    c = N.contact()
    z = c['xyz'][2]
    assert s.expand(c['mirror_density'] + c['density'].subs(z, -z)) == 0
    assert c['density'] != 0


def test_nonabelian_cubic_and_transgression_are_retained():
    t = N.transgression()
    assert s.expand(t['difference'] - t['target']) == 0
    assert t['cubic'] != 0 and t['boundary'] != 0


def test_known_wrong_sign_and_deleted_cubic_fail():
    checks = N.run()['checks']
    assert checks['omitted_cubic_rejected'] and checks['reversed_boundary_rejected']


def test_periodic_positive_and_pure_gauge_zero_controls():
    checks = N.run()['checks']
    assert all(checks[k] for k in ('periodic_density', 'periodic_integral',
                                  'pure_gradient_flat', 'pure_gradient_zero'))


def test_separate_rational_reference_population():
    result = R.run()
    assert result['all_checks_pass']
    assert result['checks'] == result['passed'] == 195
    assert len(result['contact_fixtures']) == 36
    assert result['principal_trace'] == '-7488'


def test_scientific_scope_and_effective_native_population():
    result = N.run()
    assert result['all_checks_pass'] and len(result['checks']) == 24
    assert 'no physical contour or SM' in result['scope']
