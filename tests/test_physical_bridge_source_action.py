"""R28 mathematical controls; no source selection or quantum completion claim."""
import importlib.util
from pathlib import Path
import sympy as sp


PATH = Path(__file__).resolve().parents[1] / 'reports/physical_bridge_2026_09_05/source_action.py'
SPEC = importlib.util.spec_from_file_location('physical_bridge_source_action', PATH)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


def test_exact_hyperbolic_metric_and_harmonic_tube():
    t = M.tube()
    assert (t['ricci'] + 2 * t['metric']).applyfunc(M.clean) == sp.zeros(3)
    assert M.zero(t['radial'] - t['beta'] / t['w'])
    assert t['divergence'] == 0


def test_actual_residue_kinetic_norm_and_zero_residue_control():
    t = M.tube()
    assert M.zero(sp.diff(t['primitive'], t['r'])
                  - 2 * sp.pi * t['length'] * t['w'] * t['radial']**2)
    assert M.zero(t['leading'] - 2 * sp.pi * t['length'] * t['beta']**2)
    assert t['norm'].subs(t['beta'], 0) == 0


def test_hessian_uses_both_tangential_connection_terms():
    t = M.tube()
    r, f = t['r'], t['radial']
    assert M.zero(t['hessian'][0, 0] - sp.diff(f, r))
    assert M.zero(t['hessian'][1, 1] / sp.sinh(r)**2 - sp.coth(r) * f)
    assert M.zero(t['hessian'][2, 2] / sp.cosh(r)**2 - sp.tanh(r) * f)


def test_bochner_boundary_cannot_be_dropped():
    t = M.tube()
    assert M.zero(t['bochner_residual'])
    assert not M.zero(t['hnorm'])
    assert not M.zero(sp.diff(t['boundary'], t['r']))
    assert not M.zero(t['wrong_div'])


def test_smooth_core_cauchy_schwarz_bound_and_saturation():
    t, c = M.tube(), M.core()
    assert M.zero(c['flux'] - 2 * sp.pi * t['length'] * t['beta'])
    assert M.zero(c['volume'] - sp.pi * t['length'] * sp.sinh(t['eps'])**2)
    assert M.zero(c['bound'] - c['flux']**2 / c['volume'])
    assert M.zero(c['cost'] - c['bound'])


def test_core_axis_side_and_inverse_square_limit():
    t, c = M.tube(), M.core()
    assert c['matching'] == 0
    assert M.zero(c['axis_slope'] - t['beta'] / sp.sinh(t['eps'])**2)
    assert M.zero(c['core_limit'] - 4 * sp.pi * t['length'] * t['beta']**2)
    assert c['cost'].subs(t['beta'], 0) == 0


def test_nonuniform_core_is_strictly_more_expensive_and_has_same_flux():
    t, c = M.tube(), M.core()
    assert M.zero(c['shape_residual'])
    assert M.zero((c['phi_k'] - c['phi']).subs(t['r'], t['eps']))
    assert M.zero(c['nonuniform_cost'] - 1 - c['k']**2 / 3)
    assert c['nonuniform_cost'].subs(c['k'], 1) == sp.Rational(4, 3)


def test_external_moment_map_is_a_changed_action_not_no_source():
    c = M.core()
    assert c['shifted_residual'] == 0
    assert not M.zero(c['div'])
    assert not M.zero(c['wrong_shift'])


def test_cusp_radial_and_tangential_laplacians_cancel():
    h = M.cusp()
    assert h['laplace'] == 0
    s = h['s']
    assert not M.zero(sp.diff(h['H'], s, 2) - 2 * sp.diff(h['H'], s))
    assert h['mode_equation'] == 0


def test_cusp_exact_parameter_norm_primitive():
    h = M.cusp()
    assert M.zero(h['antiderivative_residual'])
    assert M.zero(h['density'] - h['area'] * sp.exp(2 * h['s'])
                  * (2 * h['db'] * h['s'] + h['db'] + 2 * h['dc'])**2)


def test_through_flux_alone_diverges_but_zero_lower_bound_is_not_a_verdict():
    h = M.cusp()
    assert M.zero(h['through'] - 4 * h['area'] * h['dc']**2 * sp.exp(2 * h['s']))
    assert h['density'].subs({h['db']: 0, h['dc']: 0}) == 0
    assert h['tangent_norm_density'] == h['area']


def test_finite_norm_cusp_control_is_not_stationary():
    h = M.cusp()
    assert M.zero(h['finite_residual_density'] - 9 * h['finite_norm_density'])
    assert M.zero(sp.integrate(h['finite_norm_density'], (h['s'], 0, sp.oo)) - h['area'] / 4)


def test_zero_residual_stationarity_has_a_failable_control():
    a = M.action_controls()
    assert a['first'] == 0
    assert a['second'] == 2 * a['a']**2
    assert a['nonzero_first'] == 2
    assert a['convention_residual'] == 0


def test_zero_potential_and_finite_norm_can_coexist():
    a = M.action_controls()
    assert a['const_norm'] == 8 * sp.pi**3
    assert a['sin_norm'] == a['sin_residual'] == 4 * sp.pi**3


def test_gauge_compensation_cannot_remove_cartan_source_velocity():
    a = M.action_controls()
    assert a['gauge_projection'] == 0
    assert M.zero(a['gauge_norm'] - 1 - 4 * a['lam']**2)


def test_actual_trace_map_anti_poisson_positive_is_preserved():
    d = M.discrete_controls()
    assert d['invariant_residual'] == 0
    assert d['bracket_residual'] == 0
    assert d['determinant'] == -1
    assert d['conjugacy_residual'] == sp.zeros(2)
    assert d['square'].det() == 1


def test_preserving_area_density_does_not_mean_unit_coordinate_jacobian():
    d = M.discrete_controls()
    assert M.zero(d['area_residual'])
    assert M.zero(d['jacobian'] - sp.exp(d['a'] - d['b']))
    assert not M.zero(d['jacobian'].subs({d['a']: 1, d['b']: 0}) - 1)


def test_regular_time_dependent_action_generates_half_step():
    d = M.discrete_controls()
    assert d['alternating_del'] == d['c'] - d['b'] - d['a']
    assert d['mixed_alternating'] == 1
    assert d['alternating_del'].subs(d['c'], d['a'] + d['b']) == 0
    assert sp.expand(d['autonomous_del'].subs(d['c'], d['a'] + d['b'])) == 2 * d['a']


def test_multiplier_action_generates_full_map_not_only_a_linearized_leaf():
    d = M.discrete_controls()
    assert d['multiplier_x_residual'] == sp.zeros(3, 1)
    assert d['multiplier_p_residual'] == sp.zeros(3, 1)
    point = {q: sp.Rational(3, 2) for q in d['xyz']}
    assert d['inv'].subs(point) == -1
    assert d['inv'].subs(dict(zip(d['xyz'], d['T'])), simultaneous=True).subs(point) == -1


def test_native_verdict_checks_all_modules():
    checks = M.checks()
    assert len(checks) == 27
    assert all(checks.values()), checks
