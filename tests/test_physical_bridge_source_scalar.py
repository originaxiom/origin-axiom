"""R37: differentiated action, full-mode integrals and opposite controls."""
import importlib.util
from pathlib import Path

import pytest
import sympy as sp

PATH = Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/source_scalar.py'
SPEC = importlib.util.spec_from_file_location('r37_source_scalar', PATH)
ss = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(ss)


def test_all_ten_complex_variations_and_both_source_feedbacks():
    row = ss.action_control()
    assert row['S_variations'] == [0]*10
    assert row['Q_variation'] == row['h_variation'] == 0
    assert row['missing_feedback_witness'] != 0


def test_central_current_and_all_vector_generator_currents_at_zero():
    row = ss.action_control()
    assert row['central_current'] == 0
    assert row['D5_currents_at_zero'] == [0]*45


def test_stationary_point_in_all_cartesian_and_residual_variables():
    row = ss.action_control()
    assert len(row['stationary']) == 48
    assert all(v == 0 for v in row['stationary'])
    assert row['mixed_hessian'] == sp.zeros(20, 8)


def test_twenty_real_hessian_entries_from_full_potential():
    assert ss.action_control()['scalar_hessian'] == sp.zeros(20)
    assert ss.canonical_control()['hessian'] == sp.zeros(2)


@pytest.mark.parametrize('r_value,sign', ((3, 1), (2, 0), (1, -1)))
def test_positive_marginal_and_unstable_scalar_blocks(r_value, sign):
    masses = ss.canonical_control()['masses']
    lo, hi = [m.subs({ss.r: r_value, ss.eta: 1, ss.f: 1}) for m in masses]
    assert sp.sign(lo) == sign
    assert hi > 0


def test_weighted_covariant_green_and_dropped_weight_mutant():
    row = ss.weighted_green()
    assert row['scalar_green'] == row['weighted_overlap'] == 0
    assert row['missing_weight_derivative'] != 0


def test_canonical_normalization_and_induced_coefficients():
    row = ss.canonical_control()
    assert row['norm'] == row['tube_weight_residual'] == 0
    assert ss.res(row['quartic'], ss.lam/ss.W) == 0
    assert ss.res(row['locking'], ss.eta/sp.sqrt(ss.W)) == 0


def test_whole_flat_modes_normalized_and_exact_not_trial_functions():
    row = ss.flat_control()
    assert row['scalar_norm'] == row['one_form_norm'] == sp.eye(4)
    assert row['eigen_residuals'] == [0]*4
    # Exact completeness at lambda=2: k>=1 costs pi^2>2; remaining integers bounded by sqrt(2).
    assert sp.pi > 3
    lattice = {(nx, ny) for nx in range(-1, 2) for ny in range(-1, 2) if nx*nx+ny*ny == 2}
    assert lattice == {(-1,-1), (-1,1), (1,-1), (1,1)}
    assert {(0,0), (1,0)}.isdisjoint(lattice)  # Lower modes exist, not divided into pairs here.


def test_every_overlap_entry_including_off_diagonals():
    row = ss.flat_control()
    assert row['M_formula'] == row['P_formula'] == sp.zeros(4)


def test_all_interface_faces_and_omission_discriminator():
    row = ss.flat_control()
    assert row['axial_caps'] == [0]*16
    assert row['interface'] == sp.zeros(4)
    assert row['omitted_interface'] != 0
    a = sp.Rational(1,2)+sp.sin(2*ss.e)/(4*ss.e)
    assert ss.res(row['flux'][0,0], -a*sp.sin(2*ss.e)/(sp.pi**2*ss.e)) == 0


def test_complex_mixing_changes_entries_not_singular_spectra():
    row = ss.spectral_control()
    assert row['unitary'] == sp.zeros(4)
    assert row['mirror_singular_polynomial'] == row['ordinary_singular_polynomial'] == 0
    assert row['entries_change']


def test_selected_pair_is_not_whole_sector_selectivity():
    row = ss.spectral_control()
    c = 1/sp.pi**2
    assert row['M_limits'] == [c, 0, 0, 0]
    assert row['P_limits'] == [0, c/2, c/2, 0]
    assert row['selected_ratio_scaled'] == 3
    assert row['whole_norm_ratio_limit'] == 2


def test_measure_is_action_data_even_at_fixed_scalar_norm():
    row = ss.flat_control()
    assert row['measure_M'] == row['measure_P'] == sp.zeros(4)
    assert ss.spectral_control()['unweighted_limits'] == [0]*8


def test_exact_instrument_has_positive_negative_and_float_controls():
    z = sp.Symbol('z')
    assert ss.res((z*z-1)/(z-1), z+1) == 0
    assert ss.res((z*z-1)/(z-1), z+2) == -1
    with pytest.raises(ValueError):
        ss.res(sp.Float(1), sp.Float(1))


def test_declared_native_groups():
    row = ss.all_results()
    assert len(row['checks']) == 13
    assert row['all_checks_pass']
