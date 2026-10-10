"""Canonical auxiliary/static-energy controls, not a physical kernel lock."""
import importlib.util
from pathlib import Path
BASE=Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/silver_static_energy_2026_10_10'
def load(name):
    spec=importlib.util.spec_from_file_location('static_energy_'+name,BASE/(name+'.py'))
    obj=importlib.util.module_from_spec(spec);spec.loader.exec_module(obj);return obj
p=load('probe');r=load('reference')
def facts(*keys):return all(p.run()['facts'][k] for k in keys)
def test_direct_canonical_K_and_W():
    assert facts('canonical_adjoints','full_static_Z_expansion','twisted_Z_reality',
                 'direct_kinetic_coefficient_half','W_direct_left_derivative','gauge_D_coefficient_half')
    assert r.run()['predicates']['operator_kinetic_half']
    assert r.run()['predicates']['operator_gauge_half']
    assert p.run()['normalizations']==r.run()['normalizations']
def test_normalization_controls_can_fail():
    assert facts('wrong_F_coefficient_two_rejected','wrong_top_measure_sign_rejected','wrong_bartheta_sign_rejected',
                 'noncommuting_fixture','actual_F_complex')
    assert r.run()['predicates']['wrong_kinetic_changes_physical_scale']
def test_holomorphic_source_retains_surface_and_interaction():
    assert facts('CS_direct_source_and_divergence','CS_surface_omission_detected','nonzero_holomorphic_cubic_retained')
    assert r.run()['predicates']['cubic_CS_source_operator']
def test_real_surface_requires_parallel_D_and_integrated_response():
    assert facts('covariant_IBP_keeps_surface','dropping_real_surface_detected','parallel_D_zero_mean_flux_cancels',
                 'not_pointwise_flux_zero','nonparallel_D_breaks_cancellation','constant_gauge_flux_rejected',
                 'structure_flux_nonzero_but_orthogonal','A1_pairing_integrated_not_pointwise')
    assert r.run()['predicates']['omitted_surface_is_not_same_action']
def test_actual_auxiliary_conjugate_and_energy_squares():
    assert facts('real_auxiliary_variation','F_conjugate_solution','wrong_F_no_dagger_rejected',
                 'completed_real_squares','onshell_exact_positive_potential','auxiliary_real_hessian_positive')
    assert r.run()['predicates']['positive_potential_from_real_elimination']
def test_gauge_jets_and_bulk_interactions_remain():
    assert facts('moment_gauge_Ward_with_jets','omitting_derivative_jets_rejected','curvature_gauge_Ward_with_jets',
                 'nonzero_cubic_static_term','nonzero_quartic_static_term','nonlinear_moment_not_dropped')
def test_static_Hessian_is_not_a_gap_or_kernel_census():
    assert facts('residual_hessian_positive','positive_non_gauge_direction',
                 'nonzero_gauge_tangent_null_at_flat_background','zero_residual_has_no_mass_gap_certificate')
    assert r.run()['predicates']['positive_and_zero_residual_directions']
def test_complete_predicates_and_scoped_flags():
    assert all(p.run()['facts'].values()) and p.run()['predicates_passed']==len(p.run()['facts'])
    assert all(r.run()['predicates'].values()) and r.run()['predicates_passed']==len(r.run()['predicates'])
    assert p.run()['static_energy_derived'] is True
    assert p.run()['matrix_controls_are_not_silver_PDE'] is True
    for key in ('coefficient_recomputed','full_E8_structure_constants_recomputed','full_dynamical_stability_proved',
                'physical_kernel_computed','boundary_selected','nonauthor_analytic_review','physical_goal_achieved'):
        assert p.run()[key] is False
