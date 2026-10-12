"""Live actual cochain/trace/obstruction premises with opposing controls."""
import importlib.util
from functools import lru_cache
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/silver_cover_neutral_2026_10_12'


@lru_cache(None)
def both():
    out = []
    for name in ('probe', 'reference'):
        spec = importlib.util.spec_from_file_location('cover_neutral_test_'+name, BASE/(name+'.py'))
        mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
        out.append(mod.run())
    return out


def test_actual_full_relative_spaces_and_trace_planes_agree():
    a, b = both()
    assert a['neutral'] == b['neutral']
    assert a['gauge'] == b['gauge']
    for sector in ('plus', 'minus'):
        assert a['neutral'][sector]['restriction_rank'] == 6
        assert a['neutral'][sector]['connecting_dimension'] == 6


def test_actual_nonexact_odd_cocycle_equations_and_matrices():
    a, b = both()
    assert a['odd_absolute_cocycle_matrices'] == b['odd_absolute_cocycle_matrices']
    assert set(a['odd_absolute_cocycle_matrices']) == {'a', 'b', 't'}
    assert a['facts']['N_minus_full_relative_cycles']
    assert a['facts']['N_minus_absolute_direction_not_bulk_exact']
    assert b['checks']['N_minus_actual_absolute_quotient_outside_coboundaries']


def test_thirteen_neutral_modes_not_thirteen_globally_exact_modes():
    a, b = both()
    assert a['neutral']['plus']['relative_dimension'] == 6
    assert a['neutral']['minus']['relative_dimension'] == 7
    assert a['neutral']['plus']['absolute_direction_dimension'] == 0
    assert a['neutral']['minus']['absolute_direction_dimension'] == 1
    assert a['neutral']['minus']['physical_H2'] == 7


def test_actual_transverse_domain_and_equal_plane_opposite():
    a, b = both()
    for sector in ('plus', 'minus'):
        assert a['facts']['N_'+sector+'_same_actual_trace_polarization']
        assert a['facts']['N_'+sector+'_equal_plane_changes_trace_premise']
        assert b['checks']['N_'+sector+'_equal_plane_is_opposite']


def test_complete_neutral_proof_cases_with_nonzero_density_control():
    a, b = both()
    assert a['neutral_proof_case_counts'] == b['neutral_proof_case_counts']
    assert sum(a['neutral_proof_case_counts'].values()) == 13**3
    assert set(a['neutral_proof_case_counts']) == {'STOKES', 'DECK'}
    assert a['facts']['same_neutral_Lie_density_has_nonzero_opposite']
    assert b['checks']['actual_neutral_density_nonzero_control']


def test_ungraded_or_changed_trace_cannot_inherit_this_zero_proof():
    a, b = both()
    assert a['facts']['removing_deck_or_trace_does_not_prove_false_zero']
    assert b['checks']['wrong_ungraded_or_nontransverse_premise_rejected']


def test_unbroken_adjoint_ordinary_and_connecting_profiles_kept():
    a, b = both()
    assert a['gauge_proof_cases'] == b['gauge_proof_cases']
    assert a['gauge']['plus']['nonexact_ordinary_direction_dimension'] == 1
    assert a['gauge']['plus']['connecting_dimension'] == 0
    assert a['gauge']['minus']['relative_dimension'] == a['gauge']['minus']['connecting_dimension'] == 1
    assert a['facts']['g_plus_nonexact_longitude_not_connecting_or_gauge_deleted']
    assert b['checks']['g_minus_physical_connecting_zero_trace']


def test_all_E8_mixed_roots_and_actual_charged_neutral_catalogue():
    a, b = both()
    assert a['facts']['full_E8_gauge_structure_commute_and_are_trace_orthogonal']
    assert b['checks']['all_E8_gauge_structure_cross_brackets_zero']
    assert a['mixed_charge_catalogue'] == b['mixed_charge_catalogue']
    assert a['facts']['false_conjugate_left_field_changes_catalogue']
    assert b['checks']['conjugate_LEFT_insertion_changes_problem']


def test_actual_degree_two_restriction_removes_quadratic_not_higher_slot():
    a, b = both()
    assert a['neutral']['plus']['degree_two_restriction_rank'] == 6
    assert a['neutral']['plus']['degree_two_interior_kernel'] == 0
    assert a['neutral']['minus']['degree_two_restriction_rank'] == 6
    assert a['neutral']['minus']['degree_two_interior_kernel'] == 1
    assert a['facts']['N_plus_physical_degree_two_map_is_iso']
    assert b['checks']['N_minus_physical_H2_to_absolute_iso_premises']


def test_limited_analytic_conclusions_after_live_mathematics():
    a, b = both()
    assert all(a['facts'].values()) and all(b['checks'].values())
    for row in (a, b):
        assert row['odd_absolute_mode_retained'] is True
        assert row['remaining_direct_cubic_zero_conditional'] is True
        assert row['quadratic_flatness_obstruction_zero_conditional'] is True
        for key in ('higher_odd_obstruction_computed', 'quadratic_response_computed',
                    'real_moment_vacuum_derived', 'global_normalized_profiles_computed',
                    'generated_selection', 'global_quantum_anomaly', 'outside_review', 'full_goal_achieved'):
            assert row[key] is False
