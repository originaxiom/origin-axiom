"""Normal Gaussian safeguards; no full-cusp completion claim."""
import importlib.util
from pathlib import Path
BASE=Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/weave_end_gaussian_2026_10_09'
def load(name):
    spec=importlib.util.spec_from_file_location('test_end_gaussian_'+name,BASE/(name+'.py'))
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
p=load('probe');r=load('reference')
def check(*names):return all(p.run()['facts'][n] for n in names)
def test_actual_normal_operator_and_hamiltonian():
    assert check('actual_normal_source_target_signs','radial_hamiltonian_hermitian_and_square')
def test_boundary_admission_is_for_normal_model():
    assert check('tangential_principal_anticommutes_boundary_chirality','normal_boundary_complementing_controls','lorentzian_boundary_flux_zero')
def test_exact_complex_vacuum_overlap():
    assert check('mass_anchored_ground_spinors','complex_overlap_is_one_chiral_factor','absolute_value_and_unit_phase_mutants_fail')
    assert p.run()['overlap_examples']==r.run()['overlap_examples']
def test_independent_canonical_fock_quantization():
    assert r.run()['predicates']['canonical_anticommutators']
    assert r.run()['predicates']['fock_spectrum_and_unique_ground']
    assert r.run()['predicates']['gaussian_transfer_projects_to_ground']
def test_weyl_zero_is_not_a_discardable_modulus():
    assert check('boundary_overlap_has_single_zero','opposite_vacuum_overlap_zero_not_pure_phase')
def test_profile_sign_norm_and_finite_collar():
    assert check('normal_mode_and_normalization','finite_collar_tail_retained','sign_and_opposite_normal_controls','cusp_kinetic_measure_and_constant_gauge_overlap')
def test_balanced_reference_and_complete_spectrum():
    assert check('balanced_reference_opposes_actual_index','all_actual_horizontal_slots_retained','first_flux_zero_and_exotic_controls')
    assert p.run()['boundary_net_profiles']==r.run()['boundary_net_profiles']
def test_full_anomaly_not_just_a_color_number():
    assert check('full_end_anomaly_opposes_interior')
    assert p.run()['boundary_anomaly_vectors']==r.run()['boundary_anomaly_vectors']
def test_horizontal_projection_does_not_supply_local_full_lift():
    assert check('horizontal_projection_is_not_pointwise_local')
    for key in ('full_cusp_boundary_lift_derived','mirror_free_cancellation_derived','global_determinant_derived','nonauthor_acceptance','physical_goal_achieved'):
        assert p.run()[key] is False
def test_all_native_and_reference_predicates():
    for data,key in ((p.run(),'facts'),(r.run(),'predicates')):
        assert data[key] and all(data[key].values())
        assert data['predicates_passed']==len(data[key])
