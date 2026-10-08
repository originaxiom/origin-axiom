"""Twelve nonvacuous algebra locks; global proof and acceptance kept separate."""
import importlib.util
from pathlib import Path
import sympy as s

BASE = Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/weave_magnetic_stationarity_2026_10_08'
def load(name):
    spec = importlib.util.spec_from_file_location('magnetic_test_'+name, BASE/(name+'.py'))
    module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
    return module
p = load('probe'); r = load('reference')

def test_full_root_and_abstract_weight_agreement():
    assert p.root_profile() == r.root_profile() and len(p.roots()) == 240
    assert all(p.dot(a, a) == 2 for a in p.roots())

def test_primitive_cocharacter_and_same_old_peripheral():
    assert p.cocharacter(p.Z) and not p.cocharacter(tuple(x/2 for x in p.Z))
    assert all(p.dot(p.W, a) % 2 == p.dot(p.V, a) % 2 for a in p.roots())
    assert min(abs(p.dot(p.Z, a)) for a in p.roots() if p.dot(p.Z, a)) == 1

def test_gauge_centralizer_and_zero_flux_control():
    a = p.root_profile()
    assert a['gauge_roots'] == 20 and a['SM_roots'] == 8
    assert a['unstable_root_multiplicity_per_sign'] == 6 and a['adjoint_trace_Z2'] == 1800

def test_full_stationarity_conditions_and_failure_controls():
    a = p.run()['facts']
    assert a['spin_derivative_cancels'] and a['moment_nonzero_parallel_central']
    assert a['wrong_amplitude_fails_matter_variation'] and a['nonconstant_central_flux_fails_connection_variation']

def test_actual_quadratic_curvature_and_full_polynomial():
    a = p.variation()
    assert p.zero(a['f2']-p.comm(a['a'], a['a'].adjoint())/2)
    assert a['dv'].coeff(a['t'], 2) != 0 and a['dv'].coeff(a['t'], 4) != 0
    assert p.run()['facts']['full_energy_polynomial']

def test_physical_mass_sign_kinetic_and_opposite_charge():
    a = p.variation()
    assert a['mass2'] == -a['n']*a['q']
    assert a['mass2'].subs({a['n']: -2, a['q']: -5}) == -10
    assert a['mass2'].subs({a['n']: 1, a['q']: -5}) == 5
    assert a['mass2'].subs(a['n'], 0) == 0

def test_harmonic_fluctuation_is_not_pure_gauge():
    a = p.run()['facts']
    assert a['harmonic_condition_is_divergence_and_curl'] and a['charged_pure_gauge_changes_curvature']
    assert a['Hermitian_Hodge_adjoint_identity']

def test_cusp_endpoint_log_and_quartic_not_just_L2():
    for k in (1, 5, 10, 25):
        good, bad = p.radial_exponents(k, k), p.radial_exponents(k, k+1)
        assert p.integrable_power_log(good['L2_power'], good['L2_log'])
        assert not p.integrable_power_log(bad['L2_power'], bad['L2_log'])
        assert good['point_power'] == 2 and p.integrable_power_log(good['quartic_power'], good['quartic_log'])
    assert p.integrable_power_log(-1, -2) and not p.integrable_power_log(-1, -1)

def test_global_basis_lower_bound_on_both_flux_signs():
    for k in range(1, 101):
        assert p.pole_orders(k) == r.pole_orders(k) and len(set(p.pole_orders(k))) == k
    assert p.pole_orders(5) == [0, 2, 3, 4, 5]
    assert all(a['negative_complex_lower_bound'] == 30*abs(a['n']) for a in p.sample_profile())

def test_spin_signs_and_trace_normalization():
    assert all(sign**(-2*k) == 1 for sign in (-1, 1) for k in range(1, 41))
    assert sum(p.dot(p.Z, a)**2 for a in p.roots()) == 60*p.dot(p.Z, p.Z)

def test_one_fermion_drift_changes_without_claiming_index():
    a = next(a for a in p.sample_profile() if a['n'] == 1)
    assert s.Rational(a['threshold']) == s.Rational(121, 4)
    assert s.Rational(a['conjugate_threshold']) == s.Rational(81, 4)
    assert not p.run()['full_fermion_index_computed']

def test_separate_reference_and_unearned_promotions():
    a, b = p.run(), r.run()
    assert all(a['facts'].values()) and all(b['predicates'].values())
    assert a['root_profile'] == b['root_profile'] and a['sample_profile'] == b['sample_profile']
    assert not any(a[k] for k in ('full_Morse_index_computed', 'full_fermion_index_computed', 'stable_SM_phase_achieved', 'physical_chirality_achieved', 'genesis_selection_derived', 'physical_goal_achieved', 'nonauthor_acceptance'))
