"""R29 mathematical controls, distinct from physical completion or empirical validation."""
import importlib.util
from pathlib import Path

import numpy as np
import pytest
from scipy.linalg import eigh
import sympy as sp


PATH = Path(__file__).resolve().parents[1] / 'reports/physical_bridge_2026_09_05/defect_gauge.py'
SPEC = importlib.util.spec_from_file_location('physical_bridge_defect_gauge', PATH)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


def test_allowed_character_is_primitive_four_not_an_imported_parent_27():
    d = M.character()
    assert d['t'] == sp.Matrix([[4,3,5,6,4,2]])
    assert d['gcd'] == 1
    assert [q for q, ok in d['allowed'].items() if ok] == [4,8,12]
    assert d['phase4'] != 1 and d['phase12'] == 1


def test_all_local_first_variations_vanish_at_the_coupled_point():
    a = M.local_action()
    assert a['stationary'] == sp.zeros(8,1)
    assert a['density'].subs(a['point']) == 0


def test_full_hessian_is_a_positive_residual_square_not_a_claim_of_strictness():
    a = M.local_action()
    assert a['hessian_residual'] == sp.zeros(8)
    H = sp.hessian(a['density'], a['variables']).subs(a['point'])
    assert H.det() == 0


def test_scalar_source_density_is_varied_not_fixed():
    a = M.local_action()
    assert a['q_equation_residual'] == 0
    assert M.zero(a['source_response'] + 2*a['kap']*a['q']*a['sig']*a['x'])
    assert a['missing_source_cost'] != 0
    assert a['wrong_amplitude_force'] != 0


def test_connection_variation_has_the_actual_charged_current():
    a = M.local_action()
    assert a['current_residual'] == 0
    assert sp.diff(a['density'], a['A']) != 0
    assert sp.diff(a['density'], a['A']).subs(a['point']) == 0


def test_local_gauge_covariance_includes_the_phase_derivative():
    c = M.covariance()
    assert c['residual'] == sp.zeros(2,1)
    assert c['norm_residual'] == 0
    assert M.zero(c['mutant_norm'] - c['q']**2*c['omega']**2*(c['x']**2+c['y']**2))


def test_tube_source_normalization_and_residue():
    t = M.core_and_cutoff()
    assert t['normalization'] == 1
    assert M.zero(t['beta'] - t['kap']*t['q']*t['v']**2/(4*sp.pi))
    assert t['divergence_residual'] == 0
    assert M.zero(t['integrated_source']-t['kap']*t['q']*t['v']**2*t['L']/2)


def test_core_is_regular_matches_and_has_harmonic_exterior():
    t = M.core_and_cutoff()
    assert t['matching'] == t['exterior_divergence'] == 0
    assert M.zero(t['axis_slope']-t['beta']/sp.sinh(t['eps'])**2)
    assert M.zero(t['side_flux']-t['integrated_source'])


def test_fixed_integrated_mass_is_not_a_spectral_computation():
    t = M.core_and_cutoff()
    assert t['eps'] not in t['bulk_mass_integral'].free_symbols
    assert M.zero(t['bulk_mass_integral']-t['g']**2*t['q']**2*t['v']**2*t['L'])
    assert t['beta_v_derivative'] != 0


def test_vector_mass_and_phase_mixing_come_from_the_quadratic_action():
    v = M.vector_quadratic()
    assert M.zero(v['mass']-v['g']**2*v['q']**2*v['v']**2*v['sig'])
    assert v['transverse_dot'] == 0
    assert sp.diff(v['quadratic'], v['a'], v['dtheta']) != 0
    assert v['mass'].subs(v['v'], 0) == 0


def test_finite_width_poincare_bound_is_nonzero_only_with_potential():
    v = M.vector_quadratic()
    assert v['lower_identity'] == 0
    assert v['lower'].subs({v['mu']:1,v['gap']:2,v['K']:3}) == sp.Rational(2,11)
    assert v['lower'].subs(v['mu'],0) == 0


def test_hyperbolic_cutoff_uses_the_actual_volume_weight():
    t = M.core_and_cutoff()
    assert t['endpoints'] == [0,1]
    assert t['harmonic_residual'] == t['primitive_residual'] == 0
    assert t['wrong_euclidean_residual'] != 0


@pytest.mark.parametrize('eps,radius',[(.01,.2),(.003,.4)])
def test_cutoff_integral_independent_quadrature(eps,radius):
    row = M.cutoff_quadrature(eps,radius)
    assert row['relative_error'] < 2e-10
    assert row['quadrature'] > 0


def test_cusp_exhaustion_really_has_vanishing_energy_and_tail():
    c = M.cusp_cutoff()
    assert M.zero(c['energy']-c['expected'])
    assert M.zero(c['tail']-c['area']*sp.exp(-2*c['S'])/2)
    assert c['energy_limit'] == c['tail_limit'] == 0


def test_line_trace_sequence_retains_trace_while_costs_vanish():
    rows = [M.line_sequence(n) for n in (2,3,4,6,8,12)]
    assert all(r['trace_squared_per_unit_axial_norm'] == 1 for r in rows)
    assert all(b['l2_upper'] < a['l2_upper'] and b['radial_energy'] < a['radial_energy']
               for a,b in zip(rows,rows[1:]))
    assert rows[-1]['l2_upper'] < 2e-10
    # The all-n and smooth approximation proof is not this finite sample.
    assert rows[-1]['radial_energy'] < .06


def test_exact_two_dimensional_shell_bound_has_all_modes():
    for N in range(1,9):
        S,H,shells = M.shell_sums(N)
        assert S >= 4*H
        assert sum(s['count'] for s in shells) == (2*N+1)**2-1
        for s in shells:
            assert s['count'] == 8*s['k']
            assert s['squared_norm_max'] == 2*s['k']**2


@pytest.mark.parametrize('eta',[.25,1.])
def test_full_matrix_and_independent_secular_equation(eta):
    rows = [M.fourier_witness(N,eta) for N in (1,2,4,8)]
    for row in rows:
        assert row['difference'] < 3e-10
        assert row['eigenvector_residual'] < 3e-10
        assert 0 < row['eigenvalue'] <= row['upper_bound']+3e-10
        assert row['eigenvalue'] < eta
    assert all(b['eigenvalue'] < a['eigenvalue'] for a,b in zip(rows,rows[1:]))


def test_codimension_one_has_a_uniform_positive_bound():
    bound = 1/(4+4/(1-.25))
    for N in (1,2,4,8,16,32):
        row = M.fourier_witness(N,.25,1)
        assert row['difference'] < 3e-10
        assert bound <= row['eigenvalue'] <= .25
        assert row['sum0'] <= 4


def test_zero_higgs_and_uniform_mass_are_opposite_controls():
    zero = M.fourier_operator(4,0)
    uniform = M.fourier_operator(4,.25,uniform=True)
    assert np.min(eigh(zero,eigvals_only=True)) == 0
    assert np.min(eigh(uniform,eigvals_only=True)) == .25
    assert np.min(eigh(M.fourier_operator(4,.25),eigvals_only=True)) < .25


def test_positive_bare_renormalization_and_its_escape_are_distinguished():
    r = M.renormalization()
    assert r['inverse_residual'] == 0
    assert r['positive_bare_limit'] == 0
    assert M.zero(r['sign_after_pole']+r['r'])
    assert float(r['bound_difference'].subs({r['b']:1,r['L']:3,r['alpha']:1})) > 0


def test_instrument_rejects_out_of_domain_inputs():
    with pytest.raises(ValueError):
        M.cutoff_quadrature(.2,.1)
    with pytest.raises(ValueError):
        M.fourier_operator(0,1)
    with pytest.raises(ValueError):
        M.secular_root(1,0)
    with pytest.raises(ValueError):
        M.line_sequence(1)


def test_native_modules_all_discriminate():
    checks = M.checks()
    assert len(checks) == 29
    assert all(checks.values()), checks
