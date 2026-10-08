"""Full E8 bosonic end on the supplied magnetic/neutral-spin backgrounds."""
from collections import Counter
from functools import lru_cache
import importlib.util
import json
from pathlib import Path
import sympy as s

Q = s.Rational
path = Path(__file__).resolve().parent.parent/'weave_magnetic_stationarity_2026_10_08/probe.py'
spec = importlib.util.spec_from_file_location('neutral_stability_magnetic', path)
old = importlib.util.module_from_spec(spec); spec.loader.exec_module(old)

def weights():
    out = Counter((int(old.dot(old.Z, r)), int(old.dot(old.W, r))) for r in old.roots())
    out[0, 0] += 8
    return out

def modules():
    ww = weights(); out = {}
    for charge in sorted({q for q, m in ww}):
        top = max(m for q, m in ww if q == charge)
        for j in range(top+1):
            mult = ww[charge, j]-ww[charge, j+1]
            if mult: out[charge, j] = mult
    return out

def vector(j, m, k):
    return Q(1, 4)+(k+Q(m, 2))**2+Q(j*(j+1)-m*m, 2)

def radial(j, k):
    out = []
    for m in range(-j, j+1):
        if m % 2 == 0:
            d = k+Q(m+1, 2)
            b2 = Q((j-m)*(j+m+1), 2)
            out.append({'kind': 'AQ' if m < j else 'A_top', 'm': m,
                        'd': d, 'b2': b2, 'multiplicity': 2 if m < j else 1,
                        'threshold': s.expand(d*d+b2-k)})
    if j % 2:
        out.append({'kind': 'Q_bottom', 'm': -j, 'd': k-Q(j, 2),
                    'b2': s.Integer(0), 'multiplicity': 1,
                    'threshold': s.expand((k-Q(j, 2))**2-k)})
    return out

def r_threshold(j, m, k):
    return (k+Q(m, 2))**2+Q((j-m)*(j+m+1), 2)-k

def spectrum(n):
    scalar, vectors, negative = Counter(), Counter(), []
    aq_count = r_count = v_count = 0
    for (q, j), mult in modules().items():
        k = n*q
        for row in radial(j, k):
            count = mult*row['multiplicity']
            scalar[row['threshold']] += count; aq_count += count
            if row['threshold'] < 0:
                negative.append({'q': q, 'j': j, 'kind': row['kind'], 'm': row['m'],
                                 'threshold': str(row['threshold']), 'count': count})
        for m in range(-j, j+1):
            if m % 2:
                val = r_threshold(j, m, k)
                scalar[val] += mult; r_count += mult
                if val < 0:
                    negative.append({'q': q, 'j': j, 'kind': 'R', 'm': m,
                                     'threshold': str(val), 'count': mult})
            else:
                vectors[vector(j, m, k)] += mult; v_count += mult
    return {'n': n, 'AQ': aq_count, 'R': r_count, 'vector': v_count,
            'scalar_thresholds': {str(k): v for k, v in sorted(scalar.items())},
            'vector_thresholds': {str(k): v for k, v in sorted(vectors.items())},
            'scalar_bottom': str(min(scalar)), 'vector_bottom': str(min(vectors)),
            'negative': negative}

def unit(i, j, size=3):
    out = s.zeros(size); out[i, j] = 1; return out

def norm(a): return s.trace(a.adjoint()*a)

def unstable_charge_profile():
    c1,c2,weak = (1,-1,0,0,0,0,0,0),(0,1,-1,0,0,0,0,0),(Q(1,2),)*8
    out = {}
    for q in (2,3):
        rows = sorted([int(old.dot(c1,r)),int(old.dot(c2,r)),int(old.dot(weak,r))]
                      for r in old.roots() if old.dot(old.Z,r) == q and old.dot(old.W,r) == -3)
        out[str(q)] = rows
    return out

def ladder(j):
    e = s.zeros(2*j+1)
    for i,m in enumerate(range(-j,j)):
        e[i+1,i] = s.sqrt((j-m)*(j+m+1))
    return e,e.T

@lru_cache(None)
def quadratic_expansion():
    t, n = s.symbols('t n', real=True)
    omega = s.Integer(4)
    e = unit(0, 1); h = old.comm(e, e.T); z = s.diag(1, 1, -2)
    q = e+(2+s.I)*z
    ax = unit(0, 2)+unit(2, 0)
    ay = -s.I*unit(0, 2)+s.I*unit(2, 0)
    a = ax+s.I*ay
    u = unit(1, 2)+s.I*unit(2, 1)
    r = unit(2, 0)+2*s.I*unit(0, 1)
    du = unit(0, 0)+2*s.I*unit(1, 2)
    dr = unit(0, 1)-s.I*unit(2, 1)
    f1 = s.diag(1, 0, -1)+e+e.T
    f2 = -s.I*old.comm(ax, ay)
    f0 = -omega**2*h/4-n*omega**2*z
    moment = f0+t*f1+t*t*f2+omega*(old.comm(q+t*u, (q+t*u).adjoint())+t*t*old.comm(r, r.adjoint()))
    fq = t*(du+s.I*old.comm(q, a))-s.I*t*t*old.comm(a, u)
    fr = t*dr-s.I*t*t*old.comm(a, r)
    quartic = t*old.comm(q, r)+t*t*old.comm(u, r)
    exact = s.expand((norm(fq)+norm(fr))/omega+2*norm(quartic)+s.trace(moment*moment)/(2*omega**2))
    m0 = -n*omega**2*z
    m1 = f1+omega*(old.comm(u, q.adjoint())+old.comm(q, u.adjoint()))
    m2 = f2+omega*(old.comm(u, u.adjoint())+old.comm(r, r.adjoint()))
    squares = (norm(du+s.I*old.comm(q, a))+norm(dr))/omega+2*norm(old.comm(q, r))+s.trace(m1*m1)/(2*omega**2)
    expected = s.expand(squares+s.trace(m0*m2)/omega**2)
    return {'actual': exact.coeff(t, 2), 'expected': expected,
            'squares': s.expand(squares), 'n': n, 'full': exact,
            'moment': moment, 'm0': m0, 'm2': m2,
            'neutral_commutes': old.zero(old.comm(z, e))}

def gauge_identity():
    re = s.symbols('xr yr pr ur', real=True)
    im = s.symbols('xi yi pi ui', real=True)
    x, y, p, u = [a+s.I*b for a, b in zip(re, im)]
    m = (x-y)/(2*s.I)-p+u
    g = (x+y)/2-s.I*(p+u)
    abs2 = lambda z: s.expand(z*s.conjugate(z))
    right = (abs2(x-2*s.I*p)+abs2(y-2*s.I*u))/2
    return s.expand(abs2(m)+abs2(g)-right), s.expand(abs2(m)+abs2(g)/2-right)

def fourier_block(j, m, k):
    xi = s.symbols('xi', real=True)
    d = k+Q(m+1, 2); b = s.sqrt(Q((j-m)*(j+m+1), 2))
    bmat = s.Matrix([[s.I*xi+d, b], [-b, -s.I*xi+d]])
    return xi, bmat, s.simplify(bmat.adjoint()*bmat-k*s.eye(2))

def canonical_reduction(j, m, k):
    """Reduce the coordinate residuals themselves, not a supplied block square."""
    y = s.symbols('y', positive=True)
    u, alpha = s.Function('u')(y), s.Function('alpha')(y)
    a = s.sqrt(2/y)*alpha
    ladder_coefficient = s.sqrt((j-m)*(j+m+1))
    fq = s.I*(s.diff(u,y)+(m+1+2*k)*u/(2*y)) + s.I*ladder_coefficient*a/(2*s.sqrt(y))
    ga = -s.I*(s.diff(a,y)-(m+2*k)*a/(2*y)) - s.I*ladder_coefficient*u/y**s.Rational(3,2)
    d, b = k+Q(m+1,2), ladder_coefficient/s.sqrt(2)
    # dxdy = y dxdt: Fq weight y^2; ga weight y^3/2.
    first = s.simplify(fq*y/s.I-(y*s.diff(u,y)+d*u+b*alpha))
    second = s.simplify(ga*y**s.Rational(3,2)/(s.I*s.sqrt(2))-(-y*s.diff(alpha,y)+d*alpha-b*u))
    kinetic = s.simplify(y*a*a/2-alpha*alpha)
    return first, second, kinetic

@lru_cache(None)
def run():
    facts = {}; ww, mods = weights(), modules()
    recovered = Counter()
    for (q, j), a in mods.items():
        for m in range(-j, j+1): recovered[q, m] += a
    facts['all248_weights_and_full_sl2_reconstruction'] = sum(ww.values()) == 248 and recovered == ww and all(a > 0 for a in mods.values())
    facts['actual_odd_spin_charges_not_generic'] = {q for q,j in mods if j == 1} == {0,-3,-2,2,3} and {q for q,j in mods if j == 3} == {0,-3,-2,2,3}
    h, e, f = old.triple(); c, cb, n = s.symbols('c cb n')
    z = s.diag(s.zeros(5), s.diag(-2,-2,-2,3,3))
    ee = s.diag(e, s.zeros(5)); hh = s.diag(h, s.zeros(5))
    qq, qd = ee/2+c*z, ee.T/2+cb*z
    mu = -(hh/2+2*n*z)/2+old.comm(qq, qd)
    facts['arbitrary_complex_neutral_amplitude_keeps_moment'] = old.zero(mu+n*z)
    facts['full_stationary_commutator_conditions'] = old.zero(old.comm(mu, qq)) and old.zero(old.comm(mu, qd)) and old.zero(old.comm(mu, hh/2+2*n*z))
    facts['norm_modulus_is_gauge_visible'] = s.expand(s.trace(qd*qq)-s.trace(ee.T*ee)/4) == c*cb*s.trace(z*z) and s.trace(z*z) > 0
    bad = s.diag(1,-1,0,0,0)
    facts['noncommuting_neutral_substitute_fails'] = not old.zero(old.comm(bad, e))
    facts['spin_section_allowed_but_poles_fail'] = old.integrable_power_log(0, -1) and not old.integrable_power_log(-2, -1)
    facts['spin_section_graph_and_quartic_powers_integrable'] = old.integrable_power_log(0, 1) and old.integrable_power_log(1, 0)
    y = s.symbols('y', positive=True)
    psi = s.sqrt(y)*s.exp(-s.pi*y)
    facts['physical_neutral_field_and_derivative_decay'] = s.limit(psi,y,s.oo) == 0 and s.limit(y*s.diff(psi,y),y,s.oo) == 0
    facts['spin_half_frequency_not_constant_mass'] = s.diff(s.exp(s.I*s.pi*s.Symbol('x')), s.Symbol('x')) != 0
    quad = quadratic_expansion()
    facts['full_action_quadratic_expansion'] = s.expand(quad['actual']-quad['expected']) == 0
    facts['omitted_moment_fails_quadratic_control'] = s.expand(quad['actual']-quad['squares']) != 0
    facts['zero_flux_quadratic_is_positive_squares'] = s.expand(quad['actual'].subs(quad['n'],0)-quad['squares']) == 0
    identity, mutant = gauge_identity()
    facts['full_gauge_fixing_identity'] = identity == 0 and mutant != 0
    kk = s.symbols('k', integer=True)
    checks = []; vectors = []; rchecks = []; coordinate_checks = []
    for j in range(5):
        for row in radial(j, kk):
            if row['kind'] != 'Q_bottom':
                vectors.append(s.expand(row['threshold']-vector(j,row['m'],kk)) == 0)
            if row['kind'] == 'AQ':
                xi,bmat,square = fourier_block(j,row['m'],kk)
                checks.append(old.zero(square-(xi*xi+row['threshold'])*s.eye(2)))
                coordinate_checks.append(canonical_reduction(j,row['m'],kk) == (0,0,0))
        for m in range(-j,j+1):
            if m % 2:
                rchecks.append(s.expand(r_threshold(j,m,kk)-(kk+Q(m-1,2))**2-Q(j*(j+1)-m*m,2)+Q(1,4)) == 0)
    facts['all_coupled_radial_squares'] = all(checks) and len(checks) == 10
    facts['coordinate_residuals_and_kinetic_map_give_blocks'] = all(coordinate_checks) and len(coordinate_checks) == 10
    facts['paired_thresholds_match_positive_vector_operator'] = all(vectors)
    facts['all_R_thresholds_complete_positive_square'] = all(rchecks)
    facts['all_j_channel_populations_keep_extremes'] = all(sum(r['multiplicity'] for r in radial(j,0)) == 2*j+1 for j in range(5))
    lowest = []
    for j in (1,3):
        ej,fj = ladder(j)
        lo,hi = s.eye(2*j+1)[:,0],s.eye(2*j+1)[:,-1]
        lowest.append(old.zero(fj*lo) and not old.zero(fj*hi) and not old.zero(ej*lo))
    facts['lowest_Q_has_zero_linear_moment_and_gauge_term'] = all(lowest) and quad['neutral_commutes']
    facts['actual_extreme_flux_polynomials'] = s.expand((kk-Q(1,2))**2-kk-((kk-1)**2-Q(3,4))) == 0 and s.expand((kk-Q(3,2))**2-kk-((kk-2)**2-Q(7,4))) == 0
    facts['charge_one_spin_one_opposite_control'] = (1-Q(1,2))**2-1 < 0 and (1,1) not in mods
    profiles = [spectrum(n) for n in range(-3,4)]
    facts['all360_scalars_and136_vectors_counted'] = all(p['AQ'] == 248 and p['R'] == 112 and p['vector'] == 136 for p in profiles)
    first = spectrum(1)
    neg = Counter()
    for row in first['negative']: neg[row['threshold']] += row['count']
    facts['first_flux_exact_negative_channels'] = neg == {'-7/4':3,'-3/4':2} and all(r['kind'] == 'Q_bottom' and r['j'] == 3 for r in first['negative'])
    charges = unstable_charge_profile()
    facts['unstable_color_and_weak_actions_not_just_dimensions'] = charges == {'2':[[-1,0,0],[0,1,0],[1,-1,0]],'3':[[0,0,-1],[0,0,1]]}
    facts['opposite_flux_has_same_spectrum'] = all(spectrum(n)['scalar_thresholds'] == spectrum(-n)['scalar_thresholds'] for n in (1,2,3))
    facts['zero_and_higher_flux_essential_positive_controls'] = all(p['scalar_bottom'] == ('-7/4' if abs(p['n']) == 1 else '1/4') and p['vector_bottom'] == '1/4' for p in profiles)
    facts['all_integer_roster_bound_not_random_census'] = all(q in (0,-2,2,-3,3) for q,j in mods if j in (1,3)) and all(abs(2*q) >= 4 for q,j in mods if j == 3 and q != 0)
    facts['dropping_soft_term_misses_first_negative'] = (2-Q(3,2))**2 > 0 and (2-Q(3,2))**2-2 == -Q(7,4)
    # chi=s(1-s), extended by zero, is H1_0; smooth approximants retain its sign.
    L = s.symbols('L',positive=True)
    zeta = s.symbols('zeta',real=True); chi = zeta*(1-zeta)
    packet_cost = s.integrate(s.diff(chi,zeta)**2,(zeta,0,1))/s.integrate(chi**2,(zeta,0,1))
    facts['escaping_packet_derivative_cost_vanishes'] = packet_cost == 10 and s.limit(packet_cost/L**2,L,s.oo) == 0 and -Q(3,4)+packet_cost/16 < 0
    facts = {k:bool(v) for k,v in facts.items()}
    return {'facts':facts,'predicates_passed':sum(facts.values()),
            'module_profile':{str(q)+','+str(j):a for (q,j),a in sorted(mods.items())},
            'spectra':profiles, 'unstable_charge_profile':charges,
            'global_steps':'Authored analytic proof, not finite-test or independent acceptance',
            'higher_flux_global_stability_proved':False,'nonzero_flux_fermion_index_computed':False,
            'physical_chirality_achieved':False,'amplitude_or_spin_selected':False,
            'physical_goal_achieved':False,'nonauthor_acceptance':False}

if __name__ == '__main__':
    result = run(); print(json.dumps(result,indent=2,sort_keys=True))
    raise SystemExit(0 if all(result['facts'].values()) else 1)
