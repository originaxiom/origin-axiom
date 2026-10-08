"""Finite safeguards for a scoped quantum-current continuity argument."""
import importlib.util
from pathlib import Path
BASE=Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/weave_gauge_limit_2026_10_08'
def load(name):
    spec=importlib.util.spec_from_file_location('test_gauge_limit_'+name,BASE/(name+'.py'))
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);return mod
p=load('probe');r=load('reference')
def check(*names):return all(p.run()['facts'][n] for n in names)
def test_actual_mass_principal_map():
    assert check('actual_metric_normalized_principal_slots','omitted_kinetic_metric_fails')
def test_actual_higgs_potential_structure():
    assert check('actual_Q_R_are_off_block','actual_potential_has_zero_two_traces')
def test_arbitrary_matrix_local_heat_identity():
    assert check('arbitrary_matrix_heat_identity','connection_square_trace_cancels')
def test_potential_inclusion_and_mutant():
    assert check('off_block_potential_first_jets_do_not_shift_density','diagonal_potential_mutant_is_detected')
def test_all_physical_curvature_slots():
    assert check('full_virtual_rank_and_curvature_cancel','lost_physical_slot_fails')
    assert p.run()['virtual_rank_degree']==r.run()['virtual_rank_degree']==[0,0]
def test_independent_differential_expansion():
    assert r.run()['predicates']['direct_operator_heat_trace_matches']
    assert r.run()['predicates']['differential_coefficients_reproduce_action']
    assert r.run()['predicates']['nonzero_diagonal_connection_control']
def test_cutoff_norm_and_endpoint_control():
    assert check('transition_joins_value_and_first_derivative','graph_cost_positive_with_tail')
    assert p.run()['cutoff_norm_constant']==r.run()['cutoff_norm_constant']
def test_classical_limit_does_not_set_end_value():
    assert check('graph_cost_decays_not_end_value')
def test_distinct_cutoffs_and_overlap_control():
    assert check('separated_trace_shell_has_zero_parameter','overlapping_shell_is_not_zero')
    assert p.run()['overlap_integral']==r.run()['overlap_integral']=='-1/2'
def test_full_old_anomaly_profiles_are_preserved():
    assert check('nonzero_color_and_first_flux_kept','zero_and_opposite_flux_kept','complete_roster_not_a_selected_subsector')
    assert p.run()['anomaly_vectors']==r.run()['anomaly_vectors']
def test_all_native_and_separate_predicates():
    for data,key in ((p.run(),'facts'),(r.run(),'predicates')):
        assert data[key] and all(data[key].values())
        assert data['predicates_passed']==len(data[key])
def test_no_local_action_or_universal_negative_inferred():
    data=p.run()
    for key in ('local_gaussian_phase_derived','anomaly_cancellation_derived','all_quantum_completions_excluded','nonauthor_acceptance','physical_goal_achieved'):
        assert data[key] is False
