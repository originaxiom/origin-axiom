"""Faithful four-Weyl/Hodge map controls, not a complete physical model."""
import importlib.util
from pathlib import Path
BASE=Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/silver_fermion_action_2026_10_11'
def load(name):
    spec=importlib.util.spec_from_file_location('fermion_action_'+name,BASE/(name+'.py'))
    obj=importlib.util.module_from_spec(spec);spec.loader.exec_module(obj);return obj
p=load('probe');r=load('reference')
def facts(*names):return all(p.run()['facts'][k] for k in names)
def test_direct_parent_with_actual_odd_conjugates():
    assert facts('V_actual_reality','G_exact_inverse','Phi_actual_chirality','Z_twisted_reality','odd_adjoints_involutive')
def test_connections_are_distinguished_not_named():
    assert facts('direct_K_raw_plus_connection','wrong_gaugino_connection_rejected','nonzero_B_gaugino_interaction',
                 'direct_CS_holomorphic_curl','wrong_curl_connection_rejected')
    assert r.run()['predicates']['tuple_internal_plus_connection']
    assert r.run()['predicates']['tuple_all_epsilon_CS_curl']
def test_integration_by_parts_does_not_drop_boundary():
    assert facts('gaugino_IBP_retains_surface','gaugino_surface_nonzero')
    assert r.run()['predicates']['tuple_IBP_surface']
def test_equal_nonzero_canonical_kinetic_norms():
    assert facts('direct_gauge_kinetic_norm','kinetic_norm_nonzero','wrong_relative_kinetic_norm_rejected')
    assert p.run()['normalizations']==r.run()['normalizations']
    assert all(r.run()['predicates']['tuple_chiral_kinetic_mu'+str(mu)] and r.run()['predicates']['tuple_gauge_kinetic_mu'+str(mu)] for mu in range(4))
def test_full_operator_and_adjoint_not_only_symbol():
    assert facts('coefficient_A_skew_B_Hermitian','actual_connection_adjoint','component_maps_isometric',
                 'full_operator_intertwining','full_adjoint_intertwining','B_zero_order_not_discarded','wrong_chi_degree_rejected')
    assert r.run()['predicates']['reference_full_Hodge_intertwiner']
def test_maximal_Green_and_all_covector_ellipticity_controls():
    assert all(r.run()['predicates'][k] for k in ('creation_Clifford_all_pairs','physical_normal_Green_isotropic',
        'principal_quaternion_norm','physical_trace_high_rank','doubled_normal_Green_maximal',
        'adapted_symbol_maps_to_complement','adapted_symbol_exact_square','unrestricted_chi_trace_rejected'))
def test_scope_flags_and_complete_predicates():
    assert p.run()['physical_operator_identified_conditionally'] is True
    assert p.run()['native_matrix_controls_not_global_PDE'] is True
    for k in ('physical_kernel_census_recomputed','nonlinear_full_domain_closed','boundary_selected','nonauthor_analytic_review','physical_goal_achieved'):
        assert p.run()[k] is False
    assert all(p.run()['facts'].values()) and all(r.run()['predicates'].values())
    assert p.run()['predicates_passed']==len(p.run()['facts'])
    assert r.run()['predicates_passed']==len(r.run()['predicates'])
