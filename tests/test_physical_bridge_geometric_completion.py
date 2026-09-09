"""R22: same-source mode supply, finite norm, current and curvature controls."""
import importlib.util
from pathlib import Path

import pytest
import sympy as sp

SOURCE = Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/geometric_completion.py'
SPEC = importlib.util.spec_from_file_location('physical_bridge_geometric_completion', SOURCE)
gc = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(gc)


@pytest.mark.parametrize('q', [-6, -3, -2, -1, 1, 2, 3, 6])
def test_source_index_comes_from_cochains_and_reverses_with_charge(q):
    r = gc.source_pair(q)
    assert r['net_H1'] == r['independent_euler'] == 3*(1 if q > 0 else -1)
    assert r['betti'][0] == r['betti'][3] == 0
    small, large = (1, 4) if q % 3 == 0 else (0, 3)
    assert r['betti'][1:3] == ([large, small] if q > 0 else [small, large])
    assert r['betti'] == gc.source_pair(-q)['conjugate_betti']


def test_component_controls_do_not_force_three_or_hide_the_pair():
    for k in (1, 2, 4):
        for q in (-3, -2, -1, 1, 2, 3):
            r = gc.source_pair(q, k)
            assert r['net_H1'] == k*sp.sign(q)
            assert min(r['betti'][1:3]) == int(q % 3 == 0)


def test_actual_added_fields_are_not_the_same_source_modes():
    r = gc.supply()
    assert r['original_added_field_polynomial'] == 0
    assert r['bulk_anomaly'] != 0 and r['full_polynomial_match']
    assert (r['mixed_gravity_trace'], r['cubic_u_trace'], r['mixed_spin10_u']) == (120, 480, 12)
    assert r['mixed_matrix_match']
    assert r['mixed_gravity_trace'] == r['absolute_charge_trace']
    assert r['cubic_u_trace'] == r['absolute_cubic_trace']
    assert gc.source_pair(-2)['betti'][1] == 0


def test_cpt_representative_is_not_double_counted_and_scope_has_a_positive_escape():
    r = gc.supply()
    assert r['CPT_representative_invariance'] and r['reversed_source']
    assert r['independent_vector_source_restores_zero']
    assert gc.source_pair(-2, source_orientation=-1)['betti'][1] == 3


def test_peripheral_phases_are_computed_from_words_in_the_same_basis():
    r = gc.peripheral(4)
    assert r['relator_exponents'] == (0, 0)
    assert r['classes'] == [[(-2, 3), (1, 2)], [(-1, 3), (-3, 2)]]
    assert r['phases'] == [[sp.Rational(1, 3), sp.Rational(2, 3)],
                           [sp.Rational(2, 3), sp.Rational(1, 3)]]
    assert r['nontrivial_cusps'] == [True, True]
    assert r['square_torus_gap_over_4pi2'] == [sp.Rational(2, 9)]*2
    assert r['nearest_lattice_control']
    for q in (0, 12):
        assert gc.peripheral(q)['nontrivial_cusps'] == [False, False]


def test_cusp_energy_uses_the_correct_metric_and_actual_source_growth():
    r = gc.cusp_identities()
    assert r['radial_change'] and r['norm_change'] and r['transverse_change']
    assert r['no_cusp_volume_factor_transverse']
    assert all(r['elementary_tail_checks'])
    assert sp.simplify(r['logarithm_ratio_at_max']-4/sp.exp(2)) == 0
    # Omitting the transverse inverse metric would falsely make a constant tail finite.
    s = next(iter(r['constant_amplitude_transverse_primitive'].free_symbols))
    assert sp.diff(r['constant_amplitude_transverse_primitive'], s) == 1
    assert sp.limit(r['constant_amplitude_transverse_primitive'], s, sp.oo) == sp.oo


def test_finite_trial_norm_bounds_have_both_charge_sign_controls():
    rows = gc.cusp_integral_controls()
    assert {sp.sign(r['q']) for r in rows} == {-1, 0, 1}
    assert all(r['controls_pass'] for r in rows)
    assert all(all(v > 0 for v in r['integrals']) for r in rows)


def test_maxwell_equation_is_not_omitted_after_charged_condensation():
    r = gc.current_controls()
    assert r['equation_match'] and r['single_current_nonzero']
    assert r['neutral_current'] == r['compatible_phase_current'] == 0
    assert r['nonreal_order_three_holonomy']


def test_real_holonomy_and_multiple_current_controls_prevent_a_wider_kill():
    r = gc.current_controls()
    assert r['real_wave_current'] == 0
    assert r['real_wave_antiperiodic'] and r['real_wave_nonparallel']
    assert r['real_wave_elliptic_equation']
    assert all(j != 0 for j in r['two_field_opposite_currents'])
    assert r['two_field_current_cancels']


def test_curvature_changes_the_differential_in_every_degree():
    r = gc.curved_differential()
    assert len(r['rows']) == 8
    assert all(x['curvature_identity'] for x in r['rows'])
    assert r['zero_form_square_nonzero'] and r['flat_all_degrees']


def test_uncovered_neutral_weak_or_nonintegral_domains_are_not_silently_classified():
    for q in (0, .5, sp.Rational(1, 2)):
        with pytest.raises(ValueError):
            gc.source_pair(q)
    with pytest.raises(ValueError):
        gc.source_pair(1, k=0)
    with pytest.raises(ValueError):
        gc.source_pair(1, source_orientation=0)
