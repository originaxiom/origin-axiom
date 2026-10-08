"""Live algebraic locks; authored global/index proof remains separately graded."""
import importlib.util
from pathlib import Path
import sympy as s

BASE=Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/weave_sm_parallel_2026_10_08'
def load(name):
    spec=importlib.util.spec_from_file_location('smparallel_test_'+name,BASE/(name+'.py'))
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module
p=load('probe');r=load('reference')

def test_two_full_root_enumerations():
    assert p.roots()=={tuple(s.Rational(x,2) for x in a) for a in r.old.weyl_roots()}

def test_two_faithfully_identified_A4_factors():
    a=p.run()['facts']
    assert a['two_actual_A4_systems'] and a['defining_weights_faithful']

def test_entire248_includes_correct_conjugates():
    rr,rb,rg,fb,fg=p.frame();actual,want,tb,tg=p.actual_branch(rr,rb,rg,fb,fg)
    assert actual==want and sum(actual.values())==248 and len(tb)==len(tg)==10

def test_actual_global_quotient_and_centre_trade():
    a=p.run()['facts']
    assert a['correct_central_quotient'] and a['individual_gauge_SU5_faithful']
    assert a['bundle_center_equals_gauge_Y']

def test_SM_roots_and_full_SM_centralizer():
    a=p.run()['facts']
    assert a['full_SM_centralizer_roots'] and a['torus_centralizer_has_no_mixed_roots']
    assert a['weak_color_Y_embedding'] and a['actual_SM_root_system']

def test_SM_global_form_and_opposite_Wilson_control():
    a=p.run()['facts']
    assert a['six_distinct_global_kernel_roots'] and a['gauge_five_Y_eigenblocks']
    assert a['central_holonomy_opposite_control'] and a['SM_representation_labels_not_generations']

def test_principal_triple_actual_grading_and_old_p():
    h,e,f=p.triple()
    assert p.comm(h,e)==2*e and p.comm(e,f)==h
    assert p.run()['facts']['integral_spin_induction_and_old_p']
    assert p.run()['facts']['root_chain_matches_cartan']

def test_same_action_stationarity_not_just_gauge_labels():
    assert p.run()['facts']['all_vacuum_residuals_zero']
    assert p.run()['facts']['wrong_amplitude_fails']

def test_finite_positive_background_norm():
    h,e,f=p.triple()
    assert s.trace(f*e)==20 and s.trace(h*h)==40

def test_entire_sl2_content_and_commutant_saturation():
    assert p.run()['spectrum_profile']['spins']=={'0':24,'1':11,'2':21,'3':11,'4':1}
    assert p.run()['facts']['SU5_saturates_compact_commutant']

def test_complete_operator_blocks_through_spin_four():
    for j in range(5):
        blocks=p.old.radial_blocks(j)
        assert sum(b['channels'] for b in blocks)==2*j+1
        assert all(p.zero(b['square']-(b['xi']**2+b['threshold'])*s.eye(b['channels'])) for b in blocks)

def test_complete_threshold_and_R_populations():
    a=p.run()['spectrum_profile']
    assert sum(a['full'].values())==248 and sum(a['R'].values())==112
    assert min(s.Rational(k) for k in a['full'])==s.Rational(1,4)
    assert a['full']['37/4']==4 and a['full']['41/4']==2

def test_new_angular_bound_replaces_old_bound():
    assert p.run()['spectrum_profile']['angular_bound']==6
    assert p.run()['facts']['correct_angular_bound_not_old4']

def test_five_dual_form_and_spin_descent():
    a=p.run()['facts']
    assert a['five_dual_form_unitary'] and a['dual_descends_through_spin_line']
    assert r.run()['predicates']['polynomial_metric_dual_form']

def test_exterior_dual_form_in_actual_ten():
    h,e,f=p.triple()
    assert p.comm(p.wedge_lie(e),p.wedge_lie(f))==p.wedge_lie(h)
    assert p.run()['facts']['exterior_dual_form_unitary']

def test_Wilson_map_failure_and_closed_compact_representative():
    a=p.run()['facts']
    assert a['generic_Wilson_literal_J_control_fails']
    assert a['compact_support_representative_closed'] and a['cutoff_without_exact_correction_fails']

def test_exhaustive_grade_patterns_not_sampling():
    assert p.grade_table()==r.grade_table() and len(p.grade_table())==16
    assert p.run()['grade_profile']['accepted']==[[1,1,1,1,1],[1,3,1]]

def test_wrong_order_two_class_is_not_old_p():
    a=p.run()['grade_profile']
    assert a['old_involution_fixed_dimension']==136 and a['four_minus_fixed_dimension']==120

def test_nonproportional_pair_is_kept_with_extra_U1():
    h,e,g,u=p.middle_pair()
    assert p.comm(e,g)==s.zeros(5) and p.comm(e,e.T)+p.comm(g,g.T)==h
    assert p.run()['facts']['nonproportional_middle_stationary_control']
    assert p.run()['facts']['middle_trivial_summand_and_extra_U1']
    assert p.run()['facts']['arbitrary_middle_two_column_rank_bound']

def test_edge_commutation_and_moment_equations():
    assert p.run()['facts']['all_edge_commutators_are_adjacent_minors']
    assert p.run()['grade_profile']['principal_edge_norms']==[4,6,6,4]

def test_flavor_rotation_preserves_W_not_just_norms():
    assert p.run()['facts']['actual_SU2_flavor_symmetry']

def test_single_type_cases_and_gapless_zero_field_control():
    assert p.run()['facts']['single_isotypic_type_prime_dimension']
    assert p.run()['facts']['zero_field_flat_end_control']

def test_separate_reference_and_no_physical_promotion():
    a,b=p.run(),r.run()
    assert all(a['facts'].values()) and all(b['predicates'].values())
    for name in ('root_profile','spectrum_profile','grade_profile'):
        assert a[name]==b[name]
    assert not any(a[name] for name in ('actual_zero_counts_computed','physical_chirality_achieved','genesis_selection_derived','all_parallel_frames_classified','physical_goal_achieved','nonauthor_acceptance'))
