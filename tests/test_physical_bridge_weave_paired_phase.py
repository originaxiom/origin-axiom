"""Finite checks support the explicit supplied paired phase, not full completion."""
import importlib.util
from pathlib import Path
BASE=Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/weave_paired_phase_2026_10_08'
def load(name):
    spec=importlib.util.spec_from_file_location('test_paired_phase_'+name,BASE/(name+'.py'))
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);return mod
p=load('probe');r=load('reference')
def check(*names):return all(p.run()['facts'][n] for n in names)
def test_polar_map_and_both_projectors():
    assert check('actual_rectangular_polar_factorization','both_kernel_projectors_retained','target_positive_square_intertwines')
def test_unpaired_not_massive_pair_count():
    assert check('kernel_minus_cokernel_not_pair_count')
    assert p.run()['polar_kernel_dimensions']==r.run()['polar_kernel_dimensions']==[1,2]
def test_complete_gauge_intertwining():
    assert check('polar_map_keeps_complete_gauge_representation')
def test_mass_compression_is_actual_and_positive():
    assert check('paired_compression_comes_from_mass_action','compression_positive_not_commuting_assumption','unmatched_target_compression_detected')
def test_gaussian_determinant_not_current_renaming():
    assert check('massive_actual_gaussian_block','positive_mass_has_no_gauge_phase')
    assert p.run()['massive_gaussian_polynomial']==r.run()['massive_gaussian_polynomial']
def test_vector_invariance_and_unpaired_control():
    assert check('vector_gauge_similarity_preserves_gaussian','one_spectral_sign_is_not_a_dirac_pair')
def test_exterior_instrument_signs():
    assert check('d_squared_and_signed_cyclic_controls')
def test_consistent_anomaly_has_exact_witness():
    assert check('consistent_nonabelian_residual_is_exact')
    wit={tuple(k.split()):p.s.sympify(v) for k,v in p.run()['exact_form_witness'].items()}
    assert p.trace(p.derivative(wit))==p.residual()
def test_wrong_cubic_fails_same_criterion():
    assert check('wrong_cubic_coefficient_fails')
def test_covariance_is_not_consistency():
    assert check('covariant_polynomial_is_not_consistent')
def test_full_representation_coefficients():
    assert check('full248_gauge_weight_population','exotic_cannot_be_discarded')
    assert p.run()['anomaly_vectors']==r.run()['anomaly_vectors']
def test_first_zero_and_opposite_flux():
    assert check('color_nonzero_with_first_flux_endpoint','all_opposite_and_zero_indices_kept')
def test_all_native_and_reference_checks():
    for data,key in ((p.run(),'facts'),(r.run(),'predicates')):
        assert data[key] and all(data[key].values())
        assert data['predicates_passed']==len(data[key])
def test_scope_not_full_parent_completion():
    data=p.run();assert data['phase_prescription_is_supplied'] is True
    for k in ('internally_local_regulator_derived','gauge_invariant_nonzero_flux_phase','full_quantum_action_derived','all_quantum_completions_excluded','nonauthor_acceptance','physical_goal_achieved'):
        assert data[k] is False
