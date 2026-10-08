"""Live algebra/local controls, not nonauthor nonlinear PDE or full SM proof."""
from pathlib import Path
import importlib.util
import pytest
import sympy as s

PACKET=Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/weave_curved_action_2026_10_08'


def load(name):
    spec=importlib.util.spec_from_file_location('curved_parent_'+name,PACKET/(name+'.py'))
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module


@pytest.fixture(scope='module')
def native():return load('probe')


def test_native_live_predicates(native):
    r=native.run()
    assert r['facts'] and all(r['facts'].values())
    assert r['predicates_passed']==len(r['facts'])


def test_separate_reference(native):
    r=load('reference').run()
    assert all(r['predicates'].values())
    assert r['action_profile']==native.run()['action_profile']


def test_cyclic_trace_instrument(native):
    a,b,c=map(native.atom,('a','b','c'))
    assert native.trace(native.comm(a,b))=={}
    assert native.eq(native.trace(native.mul(a,native.mul(b,c))),native.trace(native.mul(c,native.mul(a,b))))
    assert native.trace(native.mul(a,native.comm(b,c)))!={}


def test_all_scalar_commutators(native):
    f=native.run()['facts']
    assert f['universal_quartic_identity']
    assert f['omitting_mixed_commutator_detected'] and f['omitting_R_moment_source_detected']


def test_moment_cross_cancels_gauge_curvature(native):
    f=native.run()['facts']
    assert f['moment_cross_coefficient'] and f['derivative_curvature_cross_cancels']
    assert f['connection_moment_from_half_kinetic_metric'] and f['matter_moment_from_spin_kinetic_metric']
    assert f['wrong_connection_metric_detected'] and f['wrong_matter_metric_detected']


def test_parent_reduction_keeps_surface_primitive(native):
    f=native.run()['facts']
    assert f['ten_dimensional_six_cubic_permutations']
    assert f['ten_to_six_superpotential_with_boundary'] and f['dropping_derivative_primitive_detected']


def test_first_variation_keeps_surface_pairing(native):
    f=native.run()['facts']
    assert f['superpotential_variation_with_surface_term'] and f['dropping_variation_surface_detected']
    assert f['stokes_dxdy_to_dz_phase'] and f['omitting_stokes_phase_detected']


def test_full_cubic_yukawa_hessian(native):
    f=native.run()['facts']
    assert f['full_cubic_Hessian_six_terms'] and f['retained_family_cubic_vertex_nonzero']
    assert f['commuting_cubic_control_zero']


def test_space_dependent_gauge_control(native):
    f=native.run()['facts']
    assert f['gauge_transform_unitary'] and f['space_dependent_gauge_covariance']
    assert f['omitted_derivative_compensator_detected']


def test_curvature_gauge_surface_identity(native):
    f=native.run()['facts']
    assert f['curved_spin_identity_with_gauge_and_surface']
    assert f['spin_curvature_is_scalar_curvature_quarter']


def test_rough_energy_is_not_residual_energy(native):
    f=native.run()['facts']
    assert f['flat_holomorphic_patch_Dirac_residual_zero']
    assert f['flat_patch_rough_energy_two'] and f['flat_patch_boundary_cancels_rough']
    assert f['dropping_surface_changes_patch_energy']


def test_stationary_origin_full_boson_hessian(native):
    f=native.run()['facts']
    assert f['zero_background_potential_zero'] and f['zero_background_first_variation_zero']
    assert f['full_boson_quadratic_positive_norm_sum'] and f['interacting_potential_not_just_quadratic']


def test_scalar_quartic_reference_positive_and_negative_controls():
    r=load('reference')
    x,y,z=(1,0,0),(0,1,0),(0,0,1)
    assert r.quartic(x,x,x,x)[:3]==(0,0,0)
    d,f,v,w=r.quartic(x,y,x,z)
    assert d+f==v and v>0
    assert any(r.quartic(x,y,u,z)[0]!=r.quartic(x,y,u,z)[2] for u in (x,y,z))


def test_cusp_gap_not_created_by_stability(native):
    f=native.run()['facts']
    assert f['unchanged_spin_continuum_threshold_zero']
    assert f['inserted_mass_comparator_changes_threshold']


def test_complete_domain_bound(native):
    assert native.run()['facts']['complete_graph_cutoff_error_bound_vanishes']


def test_physical_scope_flags(native):
    r=native.run()
    for key in ('genesis_selects_action','gapped_4D_reduction_derived','physical_chiral_SM_derived','global_anomaly_acceptance','full_nonlinear_domain_theorem','nonauthor_acceptance'):
        assert r[key] is False
