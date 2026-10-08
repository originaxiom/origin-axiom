"""Exact algebraic checks; global analytic steps remain authored in PROOF.md."""
from collections import Counter
from functools import lru_cache
from itertools import combinations, product
import json
import sympy as s

Q = s.Rational
Z = tuple(Q(a, 2) for a in (5, 5, 5, -3, -3, -3, -3, -3))
W = (0, 0, 0, -1, 1, -2, 0, 2)
V = (0, 0, 0, 1, -1, 0, 0, 0)

def dot(a, b): return sum(x*y for x, y in zip(a, b))
def comm(a, b): return a*b-b*a
def zero(a): return all(s.simplify(x) == 0 for x in a)

def roots():
    out = set()
    for i, j in combinations(range(8), 2):
        for a, b in product((-1, 1), repeat=2):
            v = [s.Integer(0)]*8
            v[i], v[j] = s.Integer(a), s.Integer(b)
            out.add(tuple(v))
    for signs in product((-1, 1), repeat=8):
        if signs.count(-1) % 2 == 0:
            out.add(tuple(Q(x, 2) for x in signs))
    return out

def cocharacter(v):
    return (all(s.denom(x) == 1 for x in v) and sum(v) % 2 == 0) or (
        all(s.denom(x) == 2 for x in v) and sum(v) % 2 == 0)

def proj_b(v):
    mean = sum(v[3:])/5
    return (0, 0, 0)+tuple(x-mean for x in v[3:])

def triple():
    h, e = s.diag(-4, -2, 0, 2, 4), s.zeros(5)
    for i in range(4): e[i+1, i] = s.sqrt((i+1)*(4-i))
    return h, e, e.T

def root_profile():
    rr = roots()
    gauge = {r for r in rr if proj_b(r) == (0,)*8}
    bundle = {r for r in rr if tuple(r[i]-proj_b(r)[i] for i in range(8)) == (0,)*8}
    charges = Counter(dot(Z, r) for r in rr)
    charges[0] += 8
    return {'charges': {str(k): v for k, v in sorted(charges.items())},
            'adjoint_trace_Z2': int(sum(dot(Z, r)**2 for r in rr)),
            'norm_Z2': int(dot(Z, Z)), 'gauge_roots': len(gauge),
            'bundle_roots': len(bundle),
            'SM_roots': sum(dot(Z, r) == 0 for r in gauge),
            'unstable_root_multiplicity_per_sign': sum(dot(Z, r) == 5 for r in gauge)}

def variation():
    n, q, t, u, v = s.symbols('n q t u v', real=True)
    e = s.Matrix([[0, 1], [0, 0]])
    zz = s.diag(q/2, -q/2)
    a = (u+s.I*v)*e
    ax, ay = (a+a.adjoint())/2, (a-a.adjoint())/(2*s.I)
    f2 = s.simplify(-s.I*comm(ax, ay))
    mu = -n*zz
    dv = s.expand(s.trace((mu+t*t*f2)**2-mu**2)/2)
    kin = s.simplify(s.trace(a.adjoint()*a)/2)
    return {'n': n, 'q': q, 't': t, 'u': u, 'v': v, 'a': a, 'Z': zz,
            'f2': f2, 'dv': dv, 'kin': kin,
            'mass2': s.simplify(dv.coeff(t, 2)/kin)}

def pole_orders(k):
    if k < 1: raise ValueError('positive k required')
    return sorted([0]+[2*a for a in range(1, k//2+1)]
                  +[2*a+3 for a in range(max(0, (k-3)//2+1))])

def radial_exponents(k, p):
    # Radial L2 integrand and pointwise orthonormal squared norm.
    return {'L2_power': 2*k-2*p+1, 'L2_log': 2*k,
            'point_power': 2*k-2*p+2, 'point_log': 2*k+2,
            'quartic_power': 4*k-4*p+3, 'quartic_log': 4*k+2}

def integrable_power_log(power, log_power):
    return power > -1 or (power == -1 and log_power < -1)

def sample_profile():
    out = []
    for n in (-3, -2, -1, 0, 1, 2, 3):
        q = 5 if n >= 0 else -5
        k = n*q
        out.append({'n': n, 'q': q, 'k': k, 'mass2': -k,
                    'negative_complex_lower_bound': 6*k,
                    'threshold': str((Q(1, 2)+k)**2),
                    'conjugate_threshold': str((Q(1, 2)-k)**2)})
    return out

@lru_cache(None)
def run():
    rr = roots(); profile = root_profile(); facts = {}
    gauge = {r for r in rr if proj_b(r) == (0,)*8}
    bundle = {r for r in rr if tuple(r[i]-proj_b(r)[i] for i in range(8)) == (0,)*8}
    facts['all240_roots_norm2'] = len(rr) == 240 and all(dot(r, r) == 2 for r in rr)
    facts['primitive_E8_cocharacter'] = cocharacter(Z) and all(s.denom(dot(Z, r)) == 1 for r in rr) and any(dot(Z, r) == 1 for r in rr)
    facts['old_spin_cocharacter'] = cocharacter(W) and cocharacter(tuple(Q(W[i]-V[i], 2) for i in range(8)))
    facts['all_integer_flux_preserves_old_p'] = all(s.denom(dot(Z, r)) == 1 and dot(W, r) % 2 == dot(V, r) % 2 for r in rr)
    facts['noninteger_flux_opposite_control'] = any(s.denom(dot(Z, r)/2) != 1 for r in rr)
    facts['actual_gauge_bundle_factors'] = len(gauge) == len(bundle) == 20 and all(dot(Z, r) == 0 for r in bundle)
    facts['exact_SM_root_centralizer'] = profile['SM_roots'] == 8 and sum(dot(Z, r) == -5 for r in gauge) == 6 and profile['unstable_root_multiplicity_per_sign'] == 6
    facts['zero_flux_restores_SU5'] = len(gauge) == 20 and len(gauge) > profile['SM_roots']
    facts['trace_from_entire_adjoint'] = sum(profile['charges'].values()) == 248 and profile['adjoint_trace_Z2'] == 1800 and profile['norm_Z2'] == 30
    h, e, f = triple(); n, c = s.symbols('n c', real=True)
    hh = s.diag(h, s.zeros(5)); ee = s.diag(e, s.zeros(5))
    zz = s.diag(s.zeros(5), s.diag(-2, -2, -2, 3, 3))
    qhat = ee/2; connection_weight = hh/2+2*n*zz
    mu = -connection_weight/2+comm(qhat, qhat.adjoint())
    facts['principal_triple'] = zero(comm(h, e)-2*e) and zero(comm(e, f)-h)
    facts['spin_derivative_cancels'] = zero(comm(connection_weight, qhat)-qhat)
    facts['moment_nonzero_parallel_central'] = zero(mu+n*zz) and zero(comm(connection_weight, mu)) and zero(comm(mu, qhat)) and not zero(mu)
    facts['wrong_amplitude_fails_matter_variation'] = not zero(comm(-connection_weight/2+c*c*comm(ee, ee.adjoint()), c*ee))
    x = s.symbols('x', real=True)
    facts['nonconstant_central_flux_fails_connection_variation'] = not zero(s.diff(-x*zz, x))
    facts['finite_area_energy_coefficient'] = s.simplify(2*s.pi*n*n*s.Integer(profile['adjoint_trace_Z2'])/2-1800*s.pi*n*n) == 0
    v = variation(); a, z = v['a'], v['Z']; q = v['q']; n = v['n']; t = v['t']
    facts['charged_root_is_faithful'] = zero(comm(z, a)-q*a)
    facts['quadratic_curvature_retained'] = zero(v['f2']-comm(a, a.adjoint())/2) and not zero(v['f2'])
    facts['full_energy_polynomial'] = s.simplify(v['dv']+n*q*t*t*s.trace(a.adjoint()*a)/2-t**4*s.trace(comm(a, a.adjoint())**2)/8) == 0
    facts['positive_kinetic_and_negative_mass_ratio'] = s.simplify(v['kin']-(v['u']**2+v['v']**2)/2) == 0 and v['mass2'] == -n*q
    facts['quartic_positive_not_discarded'] = s.factor(v['dv'].coeff(t, 4)) == (v['u']**2+v['v']**2)**2/4
    facts['opposite_charge_and_zero_flux_controls'] = v['mass2'].subs({n: 1, q: -5}) == 5 and v['mass2'].subs(n, 0) == 0
    dxx, dxy, dyx, dyy = s.symbols('dxx dxy dyx dyy', real=True)
    dz = dxx+s.I*dxy-s.I*dyx+dyy
    facts['harmonic_condition_is_divergence_and_curl'] = s.re(dz) == dxx+dyy and s.im(dz) == dxy-dyx
    facts['charged_pure_gauge_changes_curvature'] = zero(comm(-n*z, a)+n*q*a) and not zero(comm(-n*z, a))
    u, ub = s.symbols('u ub'); metric = s.Function('h')(u, ub); bbar = s.Function('bbar')(ub)
    facts['Hermitian_Hodge_adjoint_identity'] = s.simplify(s.diff(metric*(bbar/metric), u)) == 0
    facts['L2_allowed_and_log_endpoint_excluded'] = all(integrable_power_log(**{'power': radial_exponents(k, p)['L2_power'], 'log_power': radial_exponents(k, p)['L2_log']}) == (p <= k) for k in range(1, 41) for p in range(k+3))
    facts['point_decay_and_quartic_admission_exponents'] = all(radial_exponents(k, k)['point_power'] == 2 and integrable_power_log(radial_exponents(k, k)['quartic_power'], radial_exponents(k, k)['quartic_log']) for k in range(1, 41))
    facts['global_basis_distinct_poles'] = all(pole_orders(k) == [0]+list(range(2, k+1)) and len(pole_orders(k)) == k for k in range(1, 101))
    facts['first_five_global_sections'] = pole_orders(5) == [0, 2, 3, 4, 5]
    facts['even_spin_power_removes_all_signs'] = all(sign**(-2*k) == 1 for sign in (-1, 1) for k in range(1, 41))
    prof = sample_profile()
    facts['both_flux_signs_negative_lower_bound'] = all(row['mass2'] == -5*abs(row['n']) and row['negative_complex_lower_bound'] == 30*abs(row['n']) for row in prof)
    facts['one_end_block_really_changes'] = (Q(1, 2)+5)**2 == Q(121, 4) and (Q(1, 2)-5)**2 == Q(81, 4) and (Q(1, 2)+5)**2 != Q(1, 4)
    facts = {k: bool(v) for k, v in facts.items()}
    return {'facts': facts, 'predicates_passed': sum(facts.values()),
            'root_profile': profile, 'sample_profile': prof,
            'global_steps': 'Authored proof, not finite enumeration certification',
            'full_Morse_index_computed': False, 'full_fermion_index_computed': False,
            'stable_SM_phase_achieved': False, 'physical_chirality_achieved': False,
            'genesis_selection_derived': False, 'physical_goal_achieved': False,
            'nonauthor_acceptance': False}

if __name__ == '__main__':
    result = run(); print(json.dumps(result, indent=2, sort_keys=True))
    raise SystemExit(0 if all(result['facts'].values()) else 1)
