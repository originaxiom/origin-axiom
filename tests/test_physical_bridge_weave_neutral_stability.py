"""Sixteen algebra/operator safeguards, not certification of global analysis."""
import importlib.util
from pathlib import Path
import sympy as s

BASE = Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/weave_neutral_stability_2026_10_08'
def load(name):
    spec = importlib.util.spec_from_file_location('neutral_stability_test_'+name,BASE/(name+'.py'))
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod
p,r = load('probe'),load('reference')

def test_entire_E8_charge_weight_roster_two_routes():
    assert p.weights() == r.weights() and sum(p.weights().values()) == 248

def test_all_actual_sl2_modules_and_extreme_vectors():
    assert p.modules() == r.modules() and p.modules()[2,3] == 3 and p.modules()[3,3] == 2
    for j in (1,3):
        e,f = p.ladder(j); lo = s.eye(2*j+1)[:,0]
        assert p.old.zero(f*lo) and not p.old.zero(e*lo)

def test_neutral_deformation_moment_and_full_variation_conditions():
    a = p.run()['facts']
    assert a['arbitrary_complex_neutral_amplitude_keeps_moment'] and a['full_stationary_commutator_conditions']
    assert a['noncommuting_neutral_substitute_fails']

def test_neutral_spin_norm_poles_and_decay():
    a = p.run()['facts']
    assert a['spin_section_allowed_but_poles_fail'] and a['spin_section_graph_and_quartic_powers_integrable']
    assert a['physical_neutral_field_and_derivative_decay'] and a['spin_half_frequency_not_constant_mass']

def test_amplitude_is_not_silently_quotiented_away():
    assert p.run()['facts']['norm_modulus_is_gauge_visible']
    assert r.run()['predicates']['distinct_positive_kinetic_cost_of_amplitude']

def test_full_interacting_action_expansion_includes_second_curvature():
    a = p.quadratic_expansion()
    assert s.expand(a['actual']-a['expected']) == 0
    assert s.expand(a['actual']-a['squares']) != 0

def test_gauge_fixing_identity_and_wrong_coefficient():
    good,bad = p.gauge_identity()
    assert good == 0 and bad != 0

def test_all_canonical_coupled_blocks_with_actual_adjoint():
    k = s.symbols('k',integer=True)
    for j in range(1,5):
        for row in p.radial(j,k):
            if row['kind'] == 'AQ':
                xi,b,square = p.fourier_block(j,row['m'],k)
                assert p.old.zero(square-(xi*xi+row['threshold'])*s.eye(2))
                assert p.canonical_reduction(j,row['m'],k) == (0,0,0)
    assert r.run()['predicates']['exact_weighted_adjoint_blocks']

def test_R_and_vector_positive_square_remainders():
    for j in range(5):
        for m in range(-j,j+1):
            if m%2:
                assert s.Rational(j*(j+1)-m*m,2)-s.Rational(1,4) >= s.Rational(1,4)
            else:
                assert p.vector(j,m,-s.Rational(m,2)) >= s.Rational(1,4)

def test_full_scalar_vector_populations_and_extremes():
    for n in (-2,-1,0,1,2):
        a = p.spectrum(n)
        assert a['AQ'] == 248 and a['R'] == 112 and a['vector'] == 136
        assert sum(a['scalar_thresholds'].values()) == 360
    assert sum(x['multiplicity'] for x in p.radial(3,0)) == 7

def test_first_flux_negative_channels_are_physical_Q_extremes():
    a = p.spectrum(1)['negative']
    assert {(x['threshold'],x['count'],x['q']) for x in a} == {('-7/4',3,2),('-3/4',2,3)}
    assert all(x['kind'] == 'Q_bottom' and x['m'] == -3 for x in a)
    assert p.unstable_charge_profile() == {'2':[[-1,0,0],[0,1,0],[1,-1,0]],'3':[[0,0,-1],[0,0,1]]}

def test_higher_flux_and_opposite_sign_controls():
    for n in (-3,-2,-1,0,1,2,3):
        a = p.spectrum(n)
        assert a['scalar_bottom'] == ('-7/4' if abs(n) == 1 else '1/4')
        assert a['scalar_thresholds'] == p.spectrum(-n)['scalar_thresholds']

def test_actual_charge_roster_matters_to_all_integer_argument():
    assert {q for q,j in p.modules() if j in (1,3)} == {0,-2,2,-3,3}
    assert (1,1) not in p.modules() and (1-s.Rational(1,2))**2-1 < 0
    assert all(abs(2*q) >= 4 for q,j in p.modules() if j%2 and q)

def test_negative_moment_and_escaping_packet_controls():
    assert (2-s.Rational(3,2))**2 > 0
    assert (2-s.Rational(3,2))**2-2 == -s.Rational(7,4)
    assert p.run()['facts']['escaping_packet_derivative_cost_vanishes']

def test_zero_flux_is_full_positive_square_control_not_chirality():
    a = p.quadratic_expansion()
    assert s.expand(a['actual'].subs(a['n'],0)-a['squares']) == 0
    assert not p.run()['physical_chirality_achieved']

def test_separate_reference_and_no_unearned_stability_promotion():
    a,b = p.run(),r.run()
    assert all(a['facts'].values()) and all(b['predicates'].values())
    assert a['module_profile'] == b['module_profile'] and a['spectra'] == b['spectra']
    assert a['unstable_charge_profile'] == b['unstable_charge_profile']
    assert not any(a[k] for k in ('higher_flux_global_stability_proved','nonzero_flux_fermion_index_computed','physical_chirality_achieved','amplitude_or_spin_selected','physical_goal_achieved','nonauthor_acceptance'))
