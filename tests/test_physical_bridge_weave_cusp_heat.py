"""Exact local identities and finite roster controls, not global analytic certification."""
import importlib.util
from pathlib import Path
import sympy as s

BASE=Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/weave_cusp_heat_2026_10_08'
def load(name):
    spec=importlib.util.spec_from_file_location('test_cusp_heat_'+name,BASE/(name+'.py'))
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);return mod
p=load('probe');r=load('reference')
def check(*names):
    facts=p.run()['facts']
    return all(facts[name] for name in names)

def test_actual_cutoff_sign():
    assert check('actual_cutoff_current_trace','outward_cutoff_integral_is_minus_one')
def test_gaussian_and_derivative():
    assert check('radial_gaussian_normalization','erf_derivative_equals_end_current')
def test_wrong_cyclic_and_sign_controls():
    assert check('wrong_sign_and_cyclic_zero_both_fail')
def test_scattering_orientation_and_mixing():
    assert check('scattering_density_sign_and_normalization','incoming_outgoing_norms_equal','mixed_channel_scattering_determinant')
def test_continuum_formula_endpoints():
    assert check('continuum_derivative_and_limits','continuum_plus_index_is_erf')
def test_direct_integrals():
    data=r.run();assert data['predicates']['all18_direct_continuum_integrals']
    assert not data['quadrature_is_interval_certificate']
def test_coupled_pair_and_slot_population():
    assert check('coupled_pairs_cancel_all_odd_functions','full248_and496_channels_retained')
def test_independent_entire_gauge_characters():
    assert p.run()['odd_mass_characters']==r.run()['odd_mass_characters']
def test_independent_all_odd_moments():
    assert p.run()['odd_moments']==r.run()['odd_moments']
def test_ir_index_and_five_anomalies():
    assert check('half_signature_reproduces_prior_every_gauge_weight','all_five_ir_anomalies_recovered')
    assert p.run()['ir_anomaly_vectors']==r.run()['ir_anomaly_vectors']
def test_first_flux_and_exotic_sector():
    assert check('first_flux_endpoint_and_exotic_retained')
def test_zero_opposite_flux():
    assert check('zero_flux_every_character_zero','opposite_flux_character_reversal')
def test_ultraviolet_does_not_truncate_continuum():
    assert check('ultraviolet_all_weight_traces_zero','finite_heat_not_zero_mode_truncation')
def test_exact_color_small_time_coefficient():
    assert check('color_first_moment_zero','color_cubic_moment_exact_polynomial','polynomial_matches_actual_full_weight_traces','erf_series_color_coefficient')
    n=s.symbols('n',integer=True)
    assert s.expand(-p.symbolic_color_moment(3)/3+16*n*(7*n*n-2))==0
def test_actual_graded_product():
    assert check('euclidean_clifford_and_grading','total_operator_is_odd','product_square_has_no_cross_term','curvature_gamma_trace_not_scalar_laplacian')
def test_even_density_is_not_supertrace():
    assert check('positive_ungraded_end_density_diverges','opposite_pair_zero_odd_nonzero_even')
def test_all_predicates_nonvacuous():
    for data,key in ((p.run(),'facts'),(r.run(),'predicates')):
        assert data[key] and all(data[key].values())
        assert data['predicates_passed']==len(data[key])
def test_physical_scope_not_promoted():
    data=p.run()
    for key in ('consistent_ward_identity_derived','determinant_phase_derived',
       'parity_even_quantum_action_renormalized','full_quantum_completion_derived',
       'stable_chiral_vacuum_derived','genesis_selection_derived','nonauthor_acceptance','physical_goal_achieved'):
        assert data[key] is False
    assert data['continuum_retained'] is True
