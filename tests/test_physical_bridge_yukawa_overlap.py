"""R36 charged overlaps: exactness, metric/connection covariance and boundary bite."""
import importlib.util
from pathlib import Path

import pytest
import sympy as sp

PATH = Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/yukawa_overlap.py'
SPEC = importlib.util.spec_from_file_location('physical_bridge_yukawa_overlap', PATH)
yo = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(yo)


@pytest.mark.parametrize('charges', ((1, 1), (1, -1)))
def test_arbitrary_volume_connection_and_functions_product_and_green(charges):
    row = yo.local_identity(charges)
    assert row['product'] == row['green'] == 0
    assert row['missing_drift'] != 0


def test_local_gauge_covariance_and_wrong_charge_discriminator():
    row = yo.gauge_controls()
    assert all(row[k] == 0 for k in ('first', 'scalar', 'coefficient'))
    assert row['mirror_charge'] == row['ordinary_charge'] == 0
    assert row['wrong_unconjugated_charge'] == 4


def test_interval_modes_scalar_and_exact_overlap_integrals():
    row = yo.interval_control()
    assert all(row[k] == 0 for k in ('u_norm', 'v_norm', 's_norm', 'eigen', 'partner'))
    assert row['endpoints'] == [0, 0]
    assert row['M_formula'] == row['P_formula'] == 0


def test_boundary_term_is_required_despite_absolute_fermion_condition():
    row = yo.interval_control()
    assert row['identity'] == 0
    assert row['omitted_boundary_at_two'] == row['boundary_at_two'] != 0


def test_large_ratio_does_not_mean_nonzero_absolute_coupling():
    row = yo.interval_control()
    assert yo.residual(row['ratio'], (yo.t**2+2)/2) == 0
    assert row['M_limit'] == 2*sp.sqrt(2)/sp.pi
    assert row['P_limit'] == 4*sp.sqrt(2)/sp.pi
    assert sp.limit(row['M'], yo.t, sp.oo) == 0
    assert sp.limit(row['P'], yo.t, sp.oo) == 0


def test_localization_cost_and_constant_profile_prior():
    row = yo.interval_control()
    assert row['gradient'] == 0
    assert row['M_zero_limit'] == row['P_zero_limit'] == 1/sp.sqrt(sp.pi)


def test_nonzero_witten_field_uses_robin_not_undeformed_neumann():
    row = yo.robin_control()
    assert row['eigen'] == row['partner'] == row['u_norm'] == row['v_norm'] == 0
    assert row['robin'] == [0, 0]
    assert all(z != 0 for z in row['undeformed_neumann'])
    assert row['identity'] == 0
    assert row['wrong_no_drift'] != 0
    assert row['boundary'] == -sp.Rational(2, 5)


def test_nontrivial_circle_fourier_products_and_both_momentum_signs():
    row = yo.circle_control()
    assert row['eigenvalues'] == [sp.Rational(4, 9), sp.Rational(1, 9), sp.Rational(16, 9)]
    assert row['scalar_norm'] == 0
    assert row['fermion_norms'] == row['partner_residuals'] == [0, 0, 0]
    assert row['coefficient_residual'] == sp.zeros(3)


def test_nonconstant_scalar_does_not_select_in_flat_circle_control():
    row = yo.circle_control()
    assert row['congruence'] == sp.zeros(3)
    assert row['same_singular_polynomial'] == row['basis_spectrum'] == 0
    assert row['M_scaled'] != row['P_scaled']  # Equal singular values, not equal matrices.


def test_true_order_three_character_has_no_parallel_charge_two_section():
    row = yo.circle_control()
    assert yo.residual(row['squared_holonomy']**3, 1) == 0
    assert row['squared_holonomy_nontrivial']


def test_complex_bilinear_can_vanish_at_positive_norm():
    assert yo.tensor_type_control() == dict(bilinear=0, hermitian=1)


def test_zero_momentum_cannot_be_divided_into_a_normalized_partner():
    with pytest.raises(ValueError):
        yo.fourier_pair(0, 0)
    with pytest.raises(ValueError):
        yo.fourier_pair(sp.Rational(1, 2))


def test_normal_form_is_exact_and_float_guard_precedes_subtraction():
    z = sp.Symbol('z')
    assert yo.residual((z*z-1)/(z-1), z+1) == 0
    assert yo.residual((z*z-1)/(z-1), z+2) == -1
    with pytest.raises(ValueError):
        yo.residual(sp.Float(1), sp.Float(1))


def test_declared_native_check_population():
    row = yo.all_results()
    assert len(row['checks']) == 11
    assert row['all_checks_pass']
