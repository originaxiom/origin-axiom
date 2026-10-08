"""Compact boundary algebra; analytic index is proved separately, not a census."""
import importlib.util
from pathlib import Path
BASE=Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/weave_boundary_index_2026_10_09'
def load(name):
    sp=importlib.util.spec_from_file_location('test_boundary_index_'+name,BASE/(name+'.py'))
    m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
p=load('probe');r=load('reference')
def check(*keys):return all(p.run()['facts'][k] for k in keys)
def test_actual_density_and_metric_green_identity():
    assert check('density_derivative_is_formally_transpose_symmetric','actual_normal_bilinear_symbol')
    assert r.run()['predicates']['variable_metric_green_identity_including_surface']
    assert r.run()['predicates']['dropping_surface_term_is_detected']
def test_actual_adjoint_domain_and_surface_pairing():
    assert check('boundary_bilinear_vanishes_without_zero_trace','correct_adjoint_trace_is_complementary','same_trace_adjoint_control_rejected')
def test_antilinear_sign_not_assumed_self_adjoint():
    assert check('collar_antilinear_map_squares_to_minus_one','normal_endpoint_antilinear_intertwining_with_minus','wrong_intertwining_plus_sign_rejected')
    assert r.run()['predicates']['differential_antilinear_kernel_pairing_sign']
    assert r.run()['predicates']['opposite_sign_control_fails']
def test_local_ellipticity_and_bundle_seam():
    assert check('dirac_principal_clifford_relations','source_and_adjoint_local_ellipticity','spin_descent_is_retained')
def test_interactions_and_lower_order_homotopy():
    assert check('actual_full_interacting_trace_dual_transpose','higgs_deformation_is_order_zero','wrong_dual_transpose_is_detected')
def test_formal_trace_symmetry_does_not_kill_every_index():
    assert check('symmetric_bilinear_does_not_force_sector_zero')
    assert p.run()['rectangular_control']==r.run()['rectangular_control']==[[3,0,3],[0,3,-3]]
def test_representation_sensitive_winding_escape_is_local():
    assert check('changed_pair_remains_unitary_elliptic','changed_pair_retains_spin_seam','changed_pair_retains_physical_conjugation','changed_pair_cross_boundary_bilinear_vanishes')
    assert r.run()['predicates']['laurent_seam_adjoint_and_cross_sector_pairing']
def test_winding_changes_the_equal_endpoint_hypothesis():
    assert check('relative_windings_are_opposite_integers','changed_pair_is_not_identical_endpoint')
    assert p.run()['winding_samples']==r.run()['winding_samples']
def test_full_248_and_exotic_are_retained():
    assert check('full_charged_multiplicity_and_conjugate_roster')
    for key in ('multiplicity_ranks','charged_neutral_dimensions'):
        assert p.run()[key]==r.run()[key]
def test_complete_controls_and_unearned_claims():
    for data,key in ((p.run(),'facts'),(r.run(),'predicates')):
        assert data[key] and all(data[key].values()) and data['predicates_passed']==len(data[key])
    for key in ('full_kernel_census','changed_boundary_index_computed','boundary_law_selected',
                'stationary_chiral_completion','nonauthor_acceptance','physical_goal_achieved'):
        assert p.run()[key] is False
