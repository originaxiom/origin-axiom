import importlib.util
from pathlib import Path

spec=importlib.util.spec_from_file_location('silver_normal_response',Path(__file__).with_name('verify.py'))
m=importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def test_full_metric_linearization():
    assert m.jacobi()['full_connection_variation']
    assert m.jacobi()['omitted_variation_detected']


def test_fixed_dirichlet_comparator():
    r=m.comparator()
    assert r['fixed_boundary_metric'] and r['full_flatness_and_moment']
    assert r['nonsplit_periodic_loop']


def test_split_limit_flux():
    r=m.comparator()
    assert r['split_smooth'] and r['small_amplitude_coefficient']=='-5*L'
    assert m.jacobi()['positive_commutator_form']


def test_opposite_controls():
    r=m.comparator()
    assert all(r[k] for k in ('radial_sign_failure_detected','normal_sign_failure_detected','frozen_metric_failure_detected'))


def test_response_is_not_a_selector_or_bare_energy():
    r=m.comparator()
    assert r['dual_same_scalar_flux'] and r['bare_residual_potential']==0


def test_scopes_and_input_custody():
    r=m.comparator()
    assert not r['silver_PDE_solved_numerically']
    assert not r['comparator_peripheral_matrices_constant']
    assert m.custody()=={'pinned_previous_members':4,'replay_here':False}
