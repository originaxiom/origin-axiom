"""LIVE canonical vector, all-rank-strata cone and conditional multiplets."""
import importlib.util
from pathlib import Path
from itertools import product
BASE=Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/silver_physical_multiplets_2026_10_11'
def load(name):
    spec=importlib.util.spec_from_file_location('multiplet_tests_'+name,BASE/(name+'.py'))
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
p=load('probe');r=load('reference')
def f(*names):return all(p.run()['facts'][name] for name in names)
def c():return p.run()['census']
def rc():return r.run()['census']
def test_direct_canonical_vector_and_mixed_kinetics():
    assert f('canonical_vector_real_and_exact_exponential','actual_even_chirality_with_external_second_jets','direct_mixed_boson_coefficient_and_retained_divergence','direct_Yang_Mills_coefficient_all_components','nonabelian_vector_quartic_retained','complex_norm_is_real_mixed_norm')
    assert f('omitted_external_divergence_rejected','wrong_mixed_coefficient_rejected','wrong_spacetime_metric_rejected','wrong_vector_coefficient_rejected')
def test_actual_mixed_response_and_normal_gauge_jets():
    assert f('actual_projected_mixed_response_keeps_normal_scalar_derivative','normal_scalar_derivative_not_an_essential_zero_law','mixed_compact_gauge_Ward_with_spacetime_and_normal_jets','frozen_internal_parameter_derivatives_rejected')
    for name in ('normal_response_gauge_invariance_with_external_jets','false_linear_vector_cannot_supply_required_flux','actual_mixed_boundary_flux_after_slice'):
        assert r.run()['predicates'][name]
def test_real_vector_mass_and_Gauss_modes_are_not_family_counts():
    assert f('positive_real_vector_mass_kernel_not_flat_complex_H0','off_shell_Maxwell_Gauss_gauge_kernel','on_shell_two_vector_polarizations_after_Gauss')
    assert r.run()['predicates']['real_block_mass_Gram_matches_complex_D_adjoint']
    assert all(v for k,v in r.run()['predicates'].items() if k.startswith('independent_null_Gauss_'))
def test_full_248_joint_weights_reject_wrong_same_dimension():
    assert f('all_240_roots_and_248_joint_weights','dimension_preserving_wrong_conjugates_rejected','whole_SU5_cubic_weight_identity','real_adjoint_and_singlet_cubic_zero')
    assert all(r.run()['predicates'][name] for name in ('different_248_joint_weight_enumeration','wrong_same_dimension_roster_rejected','full_cubic_multinomial_identity','adjoint_cubic_all_monomials_zero'))
def test_all_charged_intersection_strata_not_one_flag():
    for name,row in c()['charged'].items():
        t=row['boundary_H'][1];q=row['restriction_rank']
        expected={(ell,j) for ell in range(t+1) for j in range(max(0,ell+q-t),min(ell,q)+1)}
        assert {(a['ell'],a['intersection']) for a in row['strata']}==expected
        for a in row['strata']:
            assert a['E']['H']==a['dual']['H'][::-1] and a['E']['H'][0]==a['E']['H'][3]==0
            assert a['E']['J']==a['ell']-row['boundary_H'][0]
            dims,ranks=a['E']['dimensions'],a['E']['ranks']
            assert a['E']['H']==[dims[j]-([0]+ranks)[j]-(ranks+[0])[j] for j in range(4)]
        assert any(a['ell']==b['ell'] and a['E']['H']!=b['E']['H'] and a['E']['J']==b['E']['J'] for a,b in product(row['strata'],repeat=2))
def test_exact_cones_match_separate_fraction_LES():
    for name,a in c()['charged'].items():
        b=rc()['charged'][name]
        for key in ('absolute_H','boundary_H','restriction_rank'):assert a[key]==b[key]
        aa={(x['ell'],x['intersection']):x for x in a['strata']}
        bb={(x['ell'],x['intersection']):x for x in b['strata']}
        assert aa.keys()==bb.keys()
        for key in aa:
            for side in ('E','dual'):assert aa[key][side]['H']==bb[key][side]['H']
def test_independent_neutral_all_strata_and_split_replay():
    assert c()['neutral_profile']==rc()['neutral_profile']
    assert [a['H'] for a in c()['neutral']]==[a['H'] for a in rc()['neutral']]
    assert c()['neutral'][-1]['H']==[0,12,12,0]
    assert c()['split_neutral_restriction_cone']['H']==rc()['split_neutral_restriction_cone']['H']==[0,13,13,0]
    assert all(a['H']==a['H'][::-1] and a['J']==0 for a in c()['neutral'])
    assert len({a['H'][1] for a in c()['neutral']})==len(c()['neutral'])
    assert f('neutral_wrong_positive_unitary_shortcut_rejected')
def test_both_gauge_line_strata_retain_endpoints():
    assert c()['gauge_profile']==rc()['gauge_profile']
    assert [a['H'] for a in c()['gauge']]==[a['H'] for a in rc()['gauge']]==[[1,0,0,1],[1,1,1,1]]
def test_complete_pattern_census_and_no_double_conjugates():
    a,b=c()['aggregate'],rc()['aggregate']
    assert a==b
    assert a['patterns_computed']==len(c()['charged']['W']['strata'])*len(c()['charged']['F']['strata'])*len(c()['neutral'])*len(c()['gauge'])
    assert a['boson_fermion_on_shell_dof_match'] and a['wrong_H2_doublecount_rejected']
    assert sum(a['local_cubic_anomaly_histogram'].values())==a['patterns_computed']
def test_cubic_anomaly_both_outcomes_and_family_scope():
    a=c()['aggregate']
    assert 0 in a['local_cubic_anomaly_histogram'] and any(k!=0 for k in a['local_cubic_anomaly_histogram'])
    assert set(a['anomaly_free_common_index_histogram'])=={-2,-1,0,1,2}
    assert sum(a['anomaly_free_common_index_histogram'].values())==a['local_cubic_anomaly_histogram'][0]
    assert f('no_three_common_index_in_THIS_menu_not_architecture')
def test_all_exact_predicates_nonvacuous():
    assert all(p.run()['facts'].values()) and all(r.run()['predicates'].values())
    assert p.run()['predicates_passed']==len(p.run()['facts'])
    assert r.run()['predicates_passed']==len(r.run()['predicates'])
def test_conditional_scope_not_quantum_vacuum_or_full_goal():
    assert p.run()['conditional_linear_massless_dictionary'] and p.run()['all_rank_strata_not_all_continuous_vacua']
    for key in ('global_PDE_solved_numerically','full_Hamiltonian','full_quantum_anomaly','interactions_normalized','boundary_or_vacuum_selected','outside_review','full_goal_achieved'):assert p.run()[key] is False
    for key in ('new_native_imported','reference_superspace_expansion','global_PDE_certificate','full_Hamiltonian','full_quantum_anomaly','interactions_normalized','generated_selection','outside_review','full_goal_achieved'):assert r.run()[key] is False
