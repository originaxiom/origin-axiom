"""Locks on the actual physical dictionary and complete perturbative traces."""
import importlib.util
from pathlib import Path

BASE=Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/weave_physical_mass_2026_10_08'
def load(name):
    spec=importlib.util.spec_from_file_location('physical_mass_'+name,BASE/(name+'.py'))
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);return mod
native=load('probe')
reference=load('reference')

def facts():return native.run()['facts']

def test_W_hessian_from_full_functional():
    assert facts()['full_W_hessian'] and facts()['symmetric_bilinear']

def test_mixed_commutator_and_nonzero_vertex():
    assert facts()['wrong_mixed_sign_fails'] and facts()['nonzero_vertex']
    assert facts()['boundary_profiles_zero']

def test_actual_mass_map_all_entries():
    assert facts()['map']

def test_input_isometry_uses_gaugino_metric():
    assert facts()['input_unitary'] and facts()['wrong_metric_fails']

def test_output_isometry_uses_trace_dual_metrics():
    assert facts()['output_unitary']

def test_variable_metric_derivative_not_dropped():
    assert facts()['variable_metric_derivative_cancels']
    assert facts()['derivative_before_metric_cancellation_is_wrong']

def test_formal_transpose_uses_dual_charge_and_momentum():
    assert facts()['transpose'] and facts()['wrong_dual_fails']

def test_both_R_couplings_retained():
    assert facts()['no_R_fails']

def test_input_phase_not_slot_matching():
    assert facts()['wrong_input_phase_fails']

def test_complete_mass_square_intertwined():
    assert facts()['norm_square']

def test_physical_neutral_gaugino_is_retained():
    assert facts()['neutral_gaugino_not_quotiented_out']

def test_entire_root_population_and_conjugates():
    assert facts()['full248_and_all_charge_pairs']
    assert sum(row[-1] for row in native.run()['weight_roster'])==248

def test_actual_color_weak_representations_not_dimensions():
    assert facts()['every_charged_weight_has_actual_representation']

def test_higher_flux_physical_indices_and_sign():
    assert facts()['higher_flux_full_net_multiplicities']
    assert facts()['opposite_flux_reverses_net']
    assert facts()['physical_index_matches_whole_Hodge_index']

def test_first_flux_endpoint_is_not_erased():
    assert facts()['first_flux_endpoint_retained']

def test_zero_flux_positive_control_keeps_zero_index():
    assert facts()['zero_flux_charged_index_zero']

def test_all_integer_scope_has_actual_weight_bound():
    assert facts()['all_integer_scope_weight_bound']

def test_all_five_anomaly_coefficients():
    assert facts()['higher_flux_anomaly_vector']
    assert facts()['first_flux_anomaly_vector']
    assert facts()['opposite_and_zero_anomaly_controls']

def test_charge_pair_counting_is_not_doubled():
    assert facts()['one_per_conjugate_pair_not_double']
    assert facts()['wrong_double_count_fails']

def test_exotic_sector_cannot_be_omitted():
    assert facts()['exotic_cannot_be_deleted']

def test_anomaly_free_and_vector_pair_controls():
    assert facts()['one_standard_generation_anomaly_control']
    assert facts()['vector_pair_anomaly_control']

def test_separate_tensor_route_and_no_goal_promotion():
    n,r=native.run(),reference.run()
    assert all(r['predicates'].values())
    for key in ('net_multiplicities','anomaly_vectors','weight_roster'):
        assert n[key]==r[key]
    assert n['physical_mass_identification_derived']
    assert n['conditional_charged_index_computed']
    for key in ('full_kernel_multiplicities_computed','anomaly_completion_derived',
                'stable_magnetic_vacuum_derived','genesis_selection_derived',
                'nonauthor_acceptance','physical_goal_achieved'):
        assert n[key] is False
