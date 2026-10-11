"""Exact WZ/normal Ward controls; not a complete physical multiplet."""
import importlib.util
from pathlib import Path
BASE=Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/silver_superfield_covariance_2026_10_11'
def load(name):
    spec=importlib.util.spec_from_file_location('superfield_covariance_'+name,BASE/(name+'.py'))
    obj=importlib.util.module_from_spec(spec);spec.loader.exec_module(obj);return obj
p=load('probe');r=load('reference')
def facts(*names):return all(p.run()['facts'][k] for k in names)
def refs(*names):return all(r.run()['predicates'][k] for k in names)
def test_actual_real_even_supersymmetry():
    assert facts('actual_WZ_reality','real_supertranslation','even_supertranslation_product_rule')
    assert refs('tuple_real_vector_and_inverse')
def test_all_external_covectors_and_chirality():
    assert all(p.run()['facts']['Q_barQ_algebra_'+str(a)+str(b)] and p.run()['facts']['Q_barD_anticommutes_'+str(a)+str(b)] for a in range(2) for b in range(2))
    assert refs('operator_Q_algebra_all_covectors','operator_Q_barD_all_covectors','operator_same_chirality_algebra')
    assert facts('compensator_chiral_zero_scalar','normal_Phi_is_chiral')
def test_canonical_nonlinear_WZ_recovery():
    assert facts('nonzero_V_square_retained','exact_nonabelian_exponential_inverse','uncompensated_WZ_slots_nonzero','canonical_compensated_WZ_slots_zero','full_exponential_linearization','wrong_compensator_sign_rejected','abelian_deltaV_rule_rejected')
    assert refs('tuple_nonzero_nonlinearity','tuple_forbidden_slots_recovered','tuple_inverse_exponential_not_abelian','tuple_wrong_sign_rejected')
    assert facts('abelian_rule_can_preserve_forbidden_slots')
    assert refs('tuple_abelian_variation_forbidden_slots_blind')
def test_whole_normal_response_keeps_actual_jets():
    assert facts('normal_WZ_jet_admitted','normal_compensator_jet_nonzero','full_normal_compensated_Ward_identity','normal_WZ_recovery','every_projected_response_slot_preserved')
    assert refs('tuple_full_eta_response_Ward','tuple_normal_WZ_recovered','tuple_nonzero_normal_compensation','tuple_integrated_entire_response')
def test_Ward_identity_alone_is_not_a_jet_certificate():
    assert facts('consistent_jet_omission_is_Ward_blind','frozen_compensator_normal_WZ_rejected','inconsistent_jet_omission_Ward_rejected','inconsistent_jet_omission_projection_rejected')
    assert refs('tuple_consistent_omission_Ward_blind','tuple_frozen_normal_WZ_rejected','tuple_inconsistent_omission_rejected')
def test_fixed_integrated_projection_not_pointwise_deletion():
    assert facts('compensator_boundary_in_k','fixed_projection_commutes_with_SUSY','fixed_projection_equivariant','external_dependent_projection_rejected','zero_mean_gauge_flux_not_pointwise_zero','nonzero_structure_flux_retained','averaging_does_not_discard_squared_flux')
    assert refs('tuple_compensator_stays_in_gauge_factor','tuple_pointwise_flux_would_change_law','tuple_nonzero_structure_flux','tuple_external_dependent_projector_rejected','tuple_genuine_averaging')
def test_supplied_twist_map_acts_not_only_counts():
    assert facts('explicit_twist_singlet_and_norm','explicit_twist_triplet_complement','wrong_diagonal_twist_rejected')
    assert refs('twist_character_split','twist_singlet_tensor_action','non_singlet_control_rejected')
def test_complete_predicates_and_honest_scope():
    assert p.run()['off_shell_superfield_boundary_covariance'] and r.run()['off_shell_superfield_covariance']
    assert p.run()['normal_compensator_jets_retained'] and p.run()['twist_supplied_not_generated']
    assert all(p.run()['facts'].values()) and all(r.run()['predicates'].values())
    assert p.run()['predicates_passed']==len(p.run()['facts']) and r.run()['predicates_passed']==len(r.run()['predicates'])
    for k in ('full_E8_structure_constants_recomputed','well_posed_multiplet_boundary_proved','physical_kernel_recomputed','nonauthor_analytic_review','boundary_selected','full_goal_achieved'):
        assert p.run()[k] is False
    for k in ('native_imported','outside_review','well_posed_multiplet_proved','physical_census_recomputed','generated_selection','full_goal_achieved'):
        assert r.run()[k] is False
