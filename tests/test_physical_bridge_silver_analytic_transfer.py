"""Analytic-transfer finite controls; the functional argument lives in PROOF.md."""
import importlib.util
from pathlib import Path
BASE=Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/silver_analytic_transfer_2026_10_09'
def load(name):
    sp=importlib.util.spec_from_file_location('test_silver_analytic_'+name,BASE/(name+'.py'))
    m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
p=load('probe');r=load('reference')
def facts(*keys):return all(p.run()['facts'][key] for key in keys)
def test_literal_full_parent():
    assert facts('literal_peripheral_logs_and_relators','full_248_and_harmonic_roster')
    assert p.run()['full_harmonic_dimensions']==r.run()['full_harmonic_dimensions']==[100,200,100]
def test_actual_cyclic_contractions():
    assert all(p.run()['facts'][name+'_exact_SDR'] for name in ('W','Wdual','F','Fdual','N','gauge'))
    assert facts('W_cyclic_for_actual_dual','F_cyclic_for_actual_dual','N_cyclic_for_actual_trace','gauge_cyclic_for_actual_trace')
    assert r.run()['predicates']['all_actual_cyclic_pairings']
def test_nonvacuous_sign_and_inverse_controls():
    assert all(p.run()['facts'][name+'_wrong_homotopy_sign_rejected'] and
               p.run()['facts'][name+'_finite_inverse_last_term_is_needed']
               for name in ('W','Wdual','F','Fdual','N','gauge'))
def test_exact_bounds_and_literal_nilpotence():
    assert facts('neutral_metric_bound_is_earned','positive_finite_uniform_homotopy_bound')
    for key in ('nilpotence_orders','homotopy_bounds','inverse_bounds','global_bounds'):
        assert p.run()[key]==r.run()[key]
def test_majorant_has_two_independent_counts_and_radius_control():
    assert p.catalans(32)==r.catalans(32)
    assert facts('catalan_recursion_matches_closed_formula','tree_majorant_geometric_bound',
                 'contraction_ball_and_lipschitz_margin','oversized_ball_is_not_certified')
def test_nonlinear_curvature_and_slice():
    assert facts('neutral_jets_obey_Kuranishi_slice','neutral_curvature_is_harmonic_through_order4')
    assert r.run()['predicates']['nonlinear_slice'] and r.run()['predicates']['curvature_obstruction_identity']
def test_actual_symplectic_jet_pairings():
    assert facts('neutral_jet_pairings_preserve_harmonic_form')
    assert r.run()['predicates']['symplectic_jet_pairings']
def test_convergent_lift_is_not_automatically_flat():
    assert facts('analytic_lift_is_not_automatically_flat','commuting_flat_control_retains_bracket')
    assert r.run()['predicates']['nonflat_and_flat_opposite_controls']
def test_exact_nonlinear_profiles_not_only_signs():
    assert p.run()['neutral_jets']==r.run()['neutral_jets']
    assert p.run()['some_neutral_nonlinear_correction']==r.run()['some_neutral_nonlinear_correction']
    assert len(p.run()['neutral_jets'])==4
def test_all_predicates_and_uneared_physics():
    for obj,key in ((p.run(),'facts'),(r.run(),'predicates')):
        assert obj[key] and all(obj[key].values()) and obj['predicates_passed']==len(obj[key])
    for key in ('full_canonical_boundary_convergence','all_harmonic_inputs_flat','boundary_selected',
                'stationary_chiral_completion','full_E8_structure_constants_recomputed',
                'nonauthor_acceptance','physical_goal_achieved'):
        assert p.run()[key] is False
