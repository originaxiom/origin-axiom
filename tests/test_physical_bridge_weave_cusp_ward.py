"""Finite safeguards for the scoped cusp phase-current argument."""
import importlib.util
from pathlib import Path
BASE=Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/weave_cusp_ward_2026_10_08'
def load(name):
    spec=importlib.util.spec_from_file_location('test_cusp_ward_'+name,BASE/(name+'.py'))
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);return mod
p=load('probe');r=load('reference')
def check(*names):return all(p.run()['facts'][n] for n in names)
def test_actual_graded_ward_identity():
    assert check('finite_control_has_actual_grading','finite_gauge_variation_includes_end')
def test_omitted_end_and_wrong_sign_fail():
    assert check('dropping_end_fails_nonzero_control','outward_sign_reversal_fails')
def test_independent_phase_block_counting():
    assert p.run()['graded_control_phase_over_i']==r.run()['graded_control_phase_over_i']=='-5/2'
    assert check('ordinary_full_cutoff_control_zero','exact_control_value')
def test_end_resolvent_integral():
    assert check('end_propagator_laplace_transform','integrable_end_derivative_has_index_limit')
    assert r.run()['predicates']['all28_end_resolvent_integrals']
def test_complete_color_mass_coefficients():
    assert p.run()['color_end_coefficients']==r.run()['color_end_coefficients']
def test_ir_indices_and_first_endpoint():
    assert p.run()['color_response_at_zero']==r.run()['color_response_at_zero']
    assert check('all_color_end_responses_recover_ir','first_flux_not_high_flux')
def test_zero_and_opposite_flux():
    assert check('opposite_flux_and_zero_kept')
def test_uv_heat_is_not_entire_ward_current():
    assert check('heat_uv_and_propagator_end_are_distinct','end_product_keeps_chiral_external_trace')
def test_external_background_is_gapped_at_finite_scale():
    assert check('all_parent_color_generator_norms_bounded','strict_external_gap_control','external_dilation_preserves_finite_L_gap')
    assert check('positive_spectrum_shell_bound_control')
def test_zero_topology_nonzero_weighted_current():
    assert check('smooth_gauge_insertion_is_nonzero','global_topological_integral_zero')
    assert p.run()['weighted_color_integral_over_pi4_h2']==r.run()['weighted_color_integral_over_pi4_h2']
def test_actual_nonabelian_gauge_bracket():
    assert check('nonabelian_bracket_is_actual_color_generator','gauge_covariance_has_factor_two')
    assert p.run()['bracket_integral_over_pi4_h2']==r.run()['bracket_integral_over_pi4_h2']
def test_integrability_not_covariance():
    assert check('consistency_curl_is_nonzero','commuting_parameters_curl_control_zero')
def test_all_predicates_pass_without_vacuity():
    for data,key in ((p.run(),'facts'),(r.run(),'predicates')):
        assert data[key] and all(data[key].values())
        assert data['predicates_passed']==len(data[key])
def test_no_parent_no_go_or_completion_claim():
    data=p.run()
    for key in ('candidate_phase_is_integrable','all_quantum_completions_excluded',
       'consistent_quantum_action_derived','full_loop_renormalization_derived',
       'stable_chiral_vacuum_derived','genesis_selection_derived','nonauthor_acceptance','physical_goal_achieved'):
        assert data[key] is False
    assert data['covariant_heat_positive_retained'] is True
