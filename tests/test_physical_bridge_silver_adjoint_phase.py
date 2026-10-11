"""LIVE local algebra/operator controls; analytic proof and scope separate."""
from pathlib import Path
import importlib.util

BASE=Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/silver_adjoint_phase_2026_10_11'
def load(name):
    spec=importlib.util.spec_from_file_location('phase_tests_'+name,BASE/(name+'.py'))
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
p=load('probe');r=load('reference')
def test_actual_parent_cubic_and_phased_Weyl_Hessian():
    a,b=p.run(),r.run()
    for k in (1,9):
        for key in (f'direct_parent_Berezin_cubic_kappa_{k}',f'wrong_standard_fermion_phase_rejected_kappa_{k}',f'wrong_cubic_factor_rejected_kappa_{k}',f'scalar_cubic_and_physical_Hessian_kappa_{k}'):
            assert a['facts'][key]
        assert b['predicates'][f'tuple_parent_matches_independent_scalar_Hessian_{k}']
        assert b['predicates'][f'correct_orthonormal_action_scaling_{k}']
    assert [(x['kappa'],x['Y_distinct'],x['fermion_monomials']) for x in a['local_cubic_controls']]==[(x['kappa'],x['Y_distinct'],x['fermion_monomials']) for x in b['local_cubic_controls']]
def test_actual_fixed_boundary_not_closed_holonomy_kernel():
    f=p.run()['facts'];g=r.run()['predicates']
    for n in (1,5):
        assert f[f'closed_periodic_parallel_broken_positive_control_{n}']
        assert f[f'fixed_old_constant_boundary_rejects_that_section_{n}']
        assert g[f'periodic_but_not_old_boundary_constant_{n}']
    assert f['identity_full_holonomy_comparator_retained'] and f['unbroken_constant_section_passes_fixed_boundary']
def test_deformation_does_not_change_old_curvature_or_moment():
    f=p.run()['facts']
    assert f['structure_and_gauge_commutation_not_identical_dimensions']
    assert f['Cartan_addition_preserves_full_old_curvature_brackets']
    assert f['Cartan_addition_preserves_old_moment_commutators']
def test_full_actual_adjoint_and_projected_gauge_Higgs_mixing():
    a,b=p.run(),r.run()
    assert a['facts']['SM_centralizer_12_with_v_zero_24_and_generic_4']
    assert a['facts']['actual_projected_fermion_mixing_rank24']
    assert a['facts']['projected_squared_singular_values_24_zero_24_positive']
    for key in ('centralizer_real_dimension','leading_Weyl_rank','squared_singular_value_multiplicities'):
        assert a['adjoint_control'][key]==b['adjoint_control'][key]
    assert a['facts']['pure_one_profile_adjoint_F_cubic_zero'] and a['facts']['wrong_F_cubic_only_mass_rejected']
def test_massive_complement_not_dropped_or_all_v_extrapolated():
    f=p.run()['facts']
    assert f['massive_complement_Schur_retained'] and f['Schur_same_leading_not_same_exact_mass']
    assert f['small_v_does_not_license_all_v_no_crossing']
    assert r.run()['predicates']['Schur_keeps_massive_correction_and_small_v_scope']
def test_full_representation_anomalies_wrong_bar_and_dropped_modes():
    a,b=p.run(),r.run()
    assert a['branchings_6Y']==b['branchings_6Y']
    for key in ('full_SM_restriction_cubic_anomaly_polynomial_zero','wrong_bar_anomaly_is_detected','dropping_complete_charged_component_is_detected','mixed_gravitational_hypercharge_trace_zero','six_element_group_kernel_actual_embedding'):
        assert a['facts'][key]
    assert b['predicates']['all64_SM_Cartan_anomaly_tensor_coefficients_zero']
def test_all_predicates_recomputed_with_opposing_controls():
    assert all(p.run()['facts'].values()) and all(r.run()['predicates'].values())
    assert p.run()['predicates_passed']==len(p.run()['facts'])
    assert r.run()['predicates_passed']==len(r.run()['predicates'])
def test_extra_fields_and_full_goal_are_not_erased():
    a,b=p.run(),r.run()
    assert a['unbroken_adjoint_chiral_profiles_small_v']==12
    assert a['conditional_same_action_phase']
    for key in ('global_harmonic_overlaps_evaluated','finite_v_charged_census','generated_selection','outside_review','full_goal_achieved'):
        assert a[key] is False and b[key] is False
    assert a['global_PDE_solved'] is False and b['global_PDE_certificate'] is False
    assert b['new_native_imported'] is False
