"""Live cochain, full polynomial and opposing controls; no stored-status lock."""
import importlib.util
from functools import lru_cache
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/silver_cover_nil_flat_2026_10_13'


@lru_cache(None)
def both():
    out = []
    for name in ('probe', 'reference'):
        spec = importlib.util.spec_from_file_location('nil_flat_test_'+name, BASE/(name+'.py'))
        mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
        out.append(mod.run())
    return out


def test_actual_compensated_cocycle_and_connecting_values_agree():
    a, b = both()
    assert a['compensated_cocycle_matrices'] == b['compensated_cocycle_matrices']
    assert a['connecting_cocycle_matrices'] == b['connecting_cocycle_matrices']
    assert a['facts']['compensated_relative_class_rechecked']
    assert b['checks']['new_relative_cocycle_equations']


def test_nonexactness_in_whole_adjoint_not_flag_only():
    a, b = both()
    assert a['ranks'] == b['ranks']
    assert a['ranks']['with_compensated'] == a['ranks']['bulk_coboundary']+1
    assert a['facts']['genuine_coboundary_rejected_as_nonexact']
    assert b['checks']['exact_coboundary_not_new_absolute_mode']


def test_basis_change_keeps_two_distinct_physical_relative_vectors():
    a, b = both()
    assert a['ranks']['two_physical_vectors'] == b['ranks']['two_physical_vectors'] == 2
    assert a['facts']['same_absolute_class_distinct_retained_relative_vectors']
    assert b['checks']['basis_change_not_physical_gauge_deletion']
    assert a['connecting_direction_deleted'] is b['connecting_direction_deleted'] is False


def test_global_nil_ideal_and_actual_membership():
    a, b = both()
    assert a['facts']['global_invariant_flag_not_a_bulk_splitting']
    assert a['facts']['entire_nil_ideal_products_vanish']
    assert b['checks']['literal_global_flat_invariant_n']
    assert b['checks']['actual_nonzero_n_valued_relative_class']


def test_nonparallel_and_wrong_sign_primitive_opposites():
    a, b = both()
    assert a['facts']['nonparallel_primitive_changes_actual_relative_trace']
    assert a['facts']['wrong_sign_cannot_inherit_nil_proof']
    assert b['checks']['changed_primitive_has_nonzero_boundary_cocycle']
    assert b['checks']['opposite_sign_fails_nil_hypothesis']


def test_full_word_polynomials_agree_not_only_first_jets():
    a, b = both()
    assert a['curve_words'] == b['curve_words']
    for word in ('taTbba', 'tbTbbabbab', 'abAB', 'abt'):
        assert len(a['curve_words'][word]['coefficients']) == 1
        assert a['curve_words'][word]['eta'] == 1
    assert a['facts']['full_parent_bracket_and_higher_polynomial_opposite']
    assert b['checks']['nonzero_parent_bracket_and_untruncated_quadratic_control']


def test_connected_cover_has_nontrivial_actual_polynomial():
    a, b = both()
    words = ('bA', 't', 'aa', 'ab', 'atA')
    assert all(a['curve_words'][word]['eta'] == 1 for word in words)
    assert any(len(a['curve_words'][word]['coefficients']) == 2 for word in words)
    assert b['checks']['nontrivial_ordinary_kernel_representation_witness']


def test_second_boundary_keeps_transport_record():
    a, b = both()
    assert a['based_second_peripheral_polynomials'] == b['based_second_peripheral_polynomials']
    assert a['globally_based_second_peripheral_changes'] == b['globally_based_second_peripheral_changes']
    for word in ('abAB', 'abt'):
        assert a['facts']['second_cusp_actual_moving_frame_'+word]
        assert b['checks']['second_cusp_transported_frame_'+word]


def test_trace_null_does_not_zero_Hermitian_density_or_real_moment():
    a, b = both()
    assert a['facts']['trace_null_not_zero_positive_local_density']
    assert a['facts']['nil_flatness_does_not_imply_zero_Hermitian_commutator']
    assert b['checks']['actual_nil_does_not_zero_Hermitian_commutator']
    assert b['checks']['trace_null_is_not_positive_norm_zero']


def test_conditional_conclusions_only_after_live_algebra():
    a, b = both()
    assert all(a['facts'].values()) and all(b['checks'].values())
    for row in (a, b):
        assert row['all_order_holomorphic_line_conditional'] is True
        for key in ('all_neutral_directions_flat', 'global_harmonic_profile_computed',
                    'global_positive_Gram_computed', 'real_moment_vacuum_derived',
                    'generated_selection', 'global_quantum_anomaly', 'outside_review', 'full_goal_achieved'):
            assert row[key] is False
