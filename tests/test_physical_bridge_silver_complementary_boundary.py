"""Finite controls for the authored strict-boundary proof, not physical acceptance."""
import importlib.util
from pathlib import Path
BASE=Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/silver_complementary_boundary_2026_10_09'
def load(name):
    sp=importlib.util.spec_from_file_location('test_complement_'+name,BASE/(name+'.py'))
    m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
p=load('probe');r=load('reference')
def facts(*keys):return all(p.run()['facts'][k] for k in keys)
def test_literal_coefficients_and_full_parent():
    assert facts('literal_logs_and_relators','full_parent_and_harmonics')
    assert p.run()['full_harmonic_dimensions']==r.run()['full_harmonic_dimensions']==[100,200,100]
def test_complementary_inverse_and_acyclicity():
    for name in ('W','Wdual','F','Fdual','N','gauge'):
        assert facts(name+'_chain_projectors',name+'_contracting_inverse',name+'_acyclic_not_extra_modes')
    assert p.run()['block_profiles']==r.run()['block_profiles']
def test_actual_cyclic_pairings_and_harmonic_separation():
    assert facts('W_actual_dual_cyclicity','F_actual_dual_cyclicity','N_actual_trace_cyclicity','gauge_actual_trace_cyclicity')
    assert all(p.run()['facts'][name+'_harmonic_and_exact_separation'] for name in p.run()['block_profiles'])
def test_all_frequency_ellipticity_and_green_form():
    assert facts('symbol_projector','maximal_green_current','adapted_clifford','elliptic_exchange_all_covectors','restricted_symbol_determinant')
    assert r.run()['predicates']['symbol_and_derivative_controls_all_48']
def test_combined_reality_grading_and_wrong_complement():
    assert facts('combined_reality','graded_domain','wrong_normal_complement_rejected')
def test_nonlinear_bracket_not_deleted():
    assert facts('bulk_cubic_retained','nonzero_coexact_bracket_has_zero_gauge_moment','old_exact_boundary_still_not_strict')
    assert r.run()['predicates']['noncommutative_cubic'] and r.run()['predicates']['nonzero_bracket_zero_mean']
def test_auxiliary_cost_and_parallel_control():
    assert facts('all_nonzero_auxiliary_gradients_rejected','parallel_scalar_derivative_admitted')
    assert all(p.run()['facts'][name+'_auxiliary_derivative_control'] for name in p.run()['block_profiles'])
def test_affine_counterterm_not_discarded():
    assert facts('affine_reference_counterterm_sign') and r.run()['predicates']['affine_sign_control']
def test_all_predicates_and_unearned_physics():
    for out,key in ((p.run(),'facts'),(r.run(),'predicates')):
        assert out[key] and all(out[key].values()) and out['predicates_passed']==len(out[key])
    for key in ('full_E8_structure_constants_recomputed','boundary_selected','full_real_action_completed',
                'physical_spectrum_identified','stationary_chiral_completion','nonauthor_acceptance','physical_goal_achieved'):
        assert p.run()[key] is False
