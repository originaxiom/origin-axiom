"""Actual cusp signature controls, distinct from uncomputed quantum inflow."""
import importlib.util
from pathlib import Path

BASE=Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/weave_cusp_anomaly_2026_10_08'
def load(name):
    spec=importlib.util.spec_from_file_location('cusp_anomaly_test_'+name,BASE/(name+'.py'))
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);return mod
native=load('probe');reference=load('reference')
def facts():return native.run()['facts']

def test_actual_virtual_bundle_local_density():
    assert facts()['virtual_rank_and_two_form_zero']
    assert facts()['missing_spin_field_changes_virtual_density']

def test_global_line_bulk_and_end_not_degree_substitution():
    assert facts()['global_line_equals_bulk_plus_end']
    assert facts()['bulk_only_misses_actual_index']

def test_parity_and_logarithmic_endpoints():
    assert facts()['angular_parity_and_log_endpoints_retained']

def test_four_physical_slots_cancel_bulk_not_end():
    assert facts()['four_slot_bulk_density_cancels']
    assert facts()['line_end_combination_is_physical_index']

def test_radial_matrix_from_actual_first_order_operator():
    assert facts()['radial_factor_is_actual_hermitian_matrix']

def test_principal_homotopy_paired_signs_cancel():
    assert facts()['paired_masses_are_opposite_for_all_amplitudes']
    assert facts()['all_actual_drifts_nonzero_half_integral']

def test_adjoint_orientation_is_not_optional():
    assert facts()['adjoint_reverses_end_orientation']
    assert facts()['wrong_second_orientation_fails']

def test_every_extreme_and_both_shifts_retained():
    assert facts()['two_shifts_keep_every_slot']
    assert facts()['full248_and496_population']

def test_module_end_signatures_match_global_indices():
    assert facts()['every_module_signature_equals_global_index']
    assert facts()['extreme_closed_formula_has_both_sides']

def test_first_flux_endpoint_survives():
    assert facts()['endpoint_not_uniform_higher_flux']

def test_full_gauge_representations_and_anomalies():
    assert facts()['full_gauge_weight_index_from_actual_end']
    assert facts()['all_five_end_anomalies_match_physical']

def test_end_term_is_not_an_added_cancellation():
    assert facts()['anomaly_is_not_its_own_compensation']
    assert facts()['zero_and_opposite_flux_controls']

def test_gauge_graph_cutoffs_are_admitted_not_zero_by_fiat():
    assert facts()['gauge_cutoff_graph_errors_vanish']
    assert facts()['gauge_cutoff_not_an_assumed_zero_error']

def test_constant_gauge_norm_has_finite_coupling():
    assert facts()['constant_gauge_norm_and_coupling']

def test_gap_does_not_make_heat_trace_finite():
    assert facts()['escaping_bump_norm_and_bounded_energy']
    assert facts()['positive_heat_trace_bound_diverges']

def test_pair_lifting_keeps_net_index_control():
    assert facts()['pairing_control_changes_kernel_not_index']
    assert facts()['end_sign_change_requires_zero_crossing']

def test_separate_tensor_end_route():
    n,r=native.run(),reference.run()
    assert all(r['predicates'].values())
    for k in ('end_index_profiles','end_anomaly_vectors','module_end_indices'):
        assert n[k]==r[k]

def test_no_quantum_or_goal_promotion():
    n=native.run()
    assert n['physical_index_located_in_end']
    for k in ('regulated_parent_determinant_computed','anomaly_compensation_derived',
              'stable_chiral_vacuum_derived','genesis_selection_derived',
              'nonauthor_acceptance','physical_goal_achieved'):
        assert n[k] is False
