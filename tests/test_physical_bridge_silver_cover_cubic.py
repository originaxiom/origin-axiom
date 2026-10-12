"""Actual three-family tensor recomputation, not a preset negative verdict."""
import importlib.util
from functools import lru_cache
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/silver_cover_cubic_2026_10_12'


@lru_cache(None)
def both():
    out = []
    for name in ('probe', 'reference'):
        spec = importlib.util.spec_from_file_location('cover_cubic_test_'+name, BASE/(name+'.py'))
        mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
        out.append(mod.run())
    return out


def test_actual_trace_planes_and_full_physical_profile_dimensions():
    a, b = both()
    assert a['boundary_plane_sha256'] == b['boundary_plane_sha256']
    assert len(a['boundary_plane_sha256']) == 4
    assert a['profile_dimensions'] == b['profile_dimensions']
    assert len(a['profile_dimensions']) == 10
    assert all(n == (1 if key.endswith('plus') else 2) for key, n in a['profile_dimensions'].items())


def test_independent_complete_channel_classifications_agree():
    a, b = both()
    assert a['channel_classifications'] == b['channel_classifications']
    assert set(a['channel_classifications']) == {'QdL', 'eLL', 'udd'}
    assert set(a['channel_classifications'].values()) <= {'NONZERO', 'CANCELLATION', 'TERM_WISE_ZERO'}


def test_all_eighty_one_physical_tensor_coordinates_retained():
    a, b = both()
    assert sum(len(row['polynomials']) for row in a['channels'].values()) == 81
    assert all(row['shape'] == [3, 3, 3] for row in b['channels'].values())


def test_every_primitive_satisfies_all_rows_closed_trace_and_dimension():
    a, b = both()
    for key in a['profile_dimensions']:
        assert a['facts'][key+'_whole_pencil_kernel']
        assert a['facts'][key+'_actual_fixed_trace_plane']
        assert a['facts'][key+'_closed_trace']
        assert b['checks'][key+'_full_degree_rank_certificate']


def test_even_deck_vertices_include_two_odd_profiles():
    a, b = both()
    assert a['facts']['two_odd_vertices_are_retained'] and b['checks']['two_odd_not_discarded']
    assert all(sum(row['parity_forbidden']) == 14 for row in a['channels'].values())
    assert all(row['parity_allowed_slots'] == 13 for row in b['channels'].values())


def test_multifamily_exchange_with_nonzero_off_diagonal_comparator():
    a, b = both()
    assert a['facts']['eLL_all_family_exchange_and_diagonal']
    assert a['facts']['udd_all_family_exchange_and_diagonal']
    assert a['facts']['nonzero_off_diagonal_family_comparator']
    assert b['checks']['nonzero_off_diagonal_and_opposite_exchange']
    assert b['checks']['diagonal_zero_not_a_family_tensor_kill']


def test_degree_certificates_exhaust_polynomial_nulls_not_sampling():
    a, b = both()
    for key, row in b['channels'].items():
        assert len(row['distinct_points']) == row['degree_bound']+1
        assert len(set(row['distinct_points'])) == len(row['distinct_points'])
        assert row['zero_certified'] == (a['channel_classifications'][key] != 'NONZERO')
    assert b['checks']['degree_plus_one_is_load_bearing']


def test_actual_volume_tensor_and_phase_rejecting_controls():
    a, b = both()
    assert a['facts']['nonzero_volume_tensor_and_phase_omission_control']
    assert b['checks']['actual_volume_and_phase_omission']
    assert a['facts']['only_10_bar5_bar5_center_neutral']
    assert b['checks']['complete_parent_charge_multisets']


def test_termwise_diagnosis_does_not_confuse_parity_with_cancellation():
    a, b = both()
    for row in a['channels'].values():
        assert len(row['first_terms']) == len(row['second_terms']) == 27
        if row['classification'] == 'TERM_WISE_ZERO':
            assert set(row['first_terms']+row['second_terms']) == {'0'}
        if row['classification'] == 'CANCELLATION':
            assert set(row['polynomials']) == {'0'}
            assert any(x != '0' for x in row['first_terms']+row['second_terms'])


def test_scope_limits_after_mathematics_not_preset_result():
    a, b = both()
    assert all(a['facts'].values()) and all(b['checks'].values())
    for row in (a, b):
        assert row['actual_charged_cubic_conditional'] is True
        for key in ('Higgs_added', 'absolute_normalized_Yukawas', 'neutral_cubic_computed',
                    'complete_light_potential', 'generated_selection', 'global_quantum_anomaly',
                    'outside_review', 'full_goal_achieved'):
            assert row[key] is False
