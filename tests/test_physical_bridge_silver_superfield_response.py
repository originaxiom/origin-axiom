"""Boundary action/linear-jet controls, not a physical family count."""
import importlib.util
from pathlib import Path
BASE=Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/silver_superfield_response_2026_10_10'
def load(name):
    spec=importlib.util.spec_from_file_location('response_'+name,BASE/(name+'.py'))
    obj=importlib.util.module_from_spec(spec);spec.loader.exec_module(obj);return obj
p=load('probe');r=load('reference')
def facts(*keys):return all(p.run()['facts'][k] for k in keys)
def test_actual_surface_identity_and_bulk_commutator():
    assert facts('universal_nonlinear_variation','matrix_nonlinear_variation',
                 'cyclic_Z_commutator_zero','other_bulk_commutator_not_zero','missing_Phi_commutator_rejected')
    assert r.run()['predicates']['t_jet_matches_variation']
def test_real_surface_pairing_not_arbitrary_complex_variations():
    assert facts('twisted_Z_reality','real_eta_twisted_reality','surface_pair_real',
                 'real_pairing_nondegenerate','variations_are_real')
def test_projection_is_integrated_not_pointwise():
    assert facts('integrated_not_pointwise','constant_gauge_flux_rejected',
                 'tangential_total_derivative_projects_zero')
    assert r.run()['predicates']['zero_mean_not_pointwise']
def test_normal_gauge_jets_are_not_deleted():
    assert facts('normal_gauge_jet_cancels','normal_gauge_jet_is_nonzero',
                 'freezing_transformed_normal_vector_jet_fails')
def test_every_superspace_component_and_actual_conjugate():
    assert facts('all_superspace_slots_present','full_linear_response_real','chiral_actual_conjugate',
                 'odd_product_opposing_control','lowest_normal_scalar','mixed_gauge_normal_response',
                 'normal_auxiliary_slots','highest_normal_auxiliary_jet')
    assert p.run()['component_polynomial']==r.run()['component_polynomial']
def test_secondary_fermion_jets_have_an_on_shell_not_offshell_status():
    assert facts('secondary_chi_jets_after_primary','primary_trace_not_whole_offshell_law',
                 'secondary_redundant_on_linear_solutions','secondary_independent_offshell')
def test_commuting_factors_not_a_dimensional_identification():
    assert facts('all_24_gauge_generators_tracefree','commuting_factor_background_response',
                 'nonzero_structure_flux_retained','gauge_flux_opposing_control')
def test_complete_predicates_and_unearned_physical_scope():
    assert all(p.run()['facts'].values()) and p.run()['predicates_passed']==len(p.run()['facts'])
    assert all(r.run()['predicates'].values()) and r.run()['predicates_passed']==len(r.run()['predicates'])
    for key in ('coefficient_recomputed','full_E8_structure_constants_recomputed',
                'nonlinear_component_domain_completed','quadratic_energy_derived',
                'physical_kernel_computed','boundary_selected','nonauthor_analytic_review','physical_goal_achieved'):
        assert p.run()[key] is False
