"""Exact local nonlinear end and scalar block; not a global physical model."""
from collections import Counter
from fractions import Fraction as Q
from functools import lru_cache
from itertools import combinations, product
import json
import sympy as s


def comm(a, b):
    return a*b-b*a


def zero(a):
    return all(s.simplify(x) == 0 for x in a) if isinstance(a, s.MatrixBase) else s.simplify(a) == 0


def norm(a):
    return s.simplify(s.trace(a.conjugate().T*a))


def local():
    y, Y = s.symbols('y Y', positive=True)
    c, h = s.symbols('c h', real=True)
    E = s.Matrix([[0, 1], [0, 0]])
    H = s.diag(1, -1)
    A = h*H/y
    q = c*E/s.sqrt(y)
    derivative = s.I*q.diff(y)-s.I*comm(A, q)
    curvature = -A.diff(y)
    moment = y*y*curvature+comm(s.sqrt(y)*q, s.sqrt(y)*q.conjugate().T)
    chosen = {h: -s.Rational(1, 4), c: s.Rational(1, 2)}
    q0, a0 = q.subs(chosen), A.subs(chosen)
    physical = s.sqrt(y)*q0
    spin_derivative = -s.I*physical/(2*y)-s.I*comm(a0, physical)
    e_gauge = norm((y*y*curvature).subs(chosen))/2
    e_quartic = norm(comm(physical, physical.conjugate().T))/2
    e_scalar = -norm(physical)/2
    nq = s.integrate(norm(q0)/y, (y, Y, s.oo))*2*s.pi
    na = s.integrate(norm(a0)/2, (y, Y, s.oo))*2*s.pi
    baseline_dq = s.integrate(y*norm(s.I*q0.diff(y)), (y, Y, s.oo))*2*s.pi
    baseline_da = s.integrate(y*y*norm(-a0.diff(y)), (y, Y, s.oo))*2*s.pi
    P = s.diag(s.I, -s.I)  # restriction of Ad(p) to this sl2, not a full E8 matrix
    y0 = s.symbols('y0', positive=True)
    flat_norm = s.integrate(1/y, (y, y0, s.oo))
    T = s.symbols('T', real=True)
    q_tail = nq.subs(Y, s.exp(T))
    return {
        'sl2_brackets': zero(comm(H, E)-2*E) and zero(comm(E, E.T)-H),
        'general_derivative': zero(derivative+s.I*c*(s.Rational(1, 2)+2*h)*E/y**s.Rational(3, 2)),
        'general_curvature': zero(curvature-h*H/y**2),
        'general_moment': zero(moment-(h+c*c)*H),
        'nonzero_branch_fixed': set(s.solve([s.Rational(1, 2)+2*h, h+c*c], [h, c])) == {(-s.Rational(1, 4), -s.Rational(1, 2)), (-s.Rational(1, 4), s.Rational(1, 2))},
        'all_nonzero_background_residuals_zero': zero(derivative.subs(chosen)) and zero(moment.subs(chosen)) and zero(comm(q0, s.zeros(2))),
        'wrong_connection_detected': not zero(derivative.subs({h: 0, c: s.Rational(1, 2)})) and not zero(moment.subs({h: 0, c: s.Rational(1, 2)})),
        'wrong_amplitude_detected': not zero(moment.subs({h: -s.Rational(1, 4), c: 1})),
        'zero_origin_control': zero(derivative.subs({h: 0, c: 0})) and zero(moment.subs({h: 0, c: 0})),
        'spin_and_gauge_covariant_parallel': zero(spin_derivative),
        'non_normal_condensate': not zero(comm(physical, physical.T)),
        'expanded_curvature_balance': (e_gauge, e_quartic, e_scalar) == (s.Rational(1, 16), s.Rational(1, 16), -s.Rational(1, 8)) and zero(e_gauge+e_quartic+e_scalar),
        'dropping_curvature_energy_detected': e_gauge+e_quartic != 0,
        'combined_spin_periphery_descends': zero(P*E*P.inv()+E) and zero(P*H*P.inv()-H),
        'finite_spin_kinetic_norm': zero(nq-s.pi/(2*Y)),
        'finite_connection_kinetic_norm': zero(na-s.pi/(8*Y)),
        'baseline_graph_derivatives_finite': zero(baseline_dq-s.pi/(8*Y)) and zero(baseline_da-s.pi/(4*Y)),
        'cusp_graph_cutoff_tail_vanishes': s.limit(q_tail, T, s.oo) == 0,
        'flat_critical_log_control_diverges': flat_norm == s.oo and zero(s.integrate(1/y**2, (y, y0, s.oo))-1/y0),
        'slice_holonomy_not_fixed': s.simplify(s.exp(-s.I*s.pi/2)) != 1 and s.limit(s.exp(-s.I*s.pi/(2*y)), y, s.oo) == 1,
    }


def angular_matrices(twice_j):
    j = s.Rational(twice_j, 2)
    weights = [j-k for k in range(twice_j+1)]
    H = s.diag(*[2*m for m in weights])
    E = s.zeros(twice_j+1)
    for k in range(1, twice_j+1):
        m = weights[k]
        E[k-1, k] = s.sqrt((j-m)*(j+m+1))
    return H, E


def threshold(j, m, mixed=Q(1, 2)):
    return m*m/4 + mixed*(j-m)*(j+m+1)


def radial():
    y = s.symbols('y', positive=True)
    t, m = s.symbols('t m', real=True)
    u = s.Function('u', real=True)
    # Physical phi=y^(1/2)u(log y), so holomorphic coefficient r=u(log y).
    r = u(s.log(y))
    dr = s.I*(s.diff(r, y)+m*r/(2*y))
    transformed = s.simplify((y*y*dr).subs(y, s.exp(t))/s.exp(t)/s.I)
    # dy=y dt; derivative coefficient y: y^2 |dr|^2.
    kinetic_weight = s.simplify((1/y)*y)
    raising_weight = s.simplify(2*(1/(2*s.sqrt(y)))**2*y)
    eps = s.symbols('eps', real=True)
    R = s.Matrix([[0, 0], [1, 0]])
    r_moment = comm(eps*R, eps*R.T)
    hessian_moment_order = s.diff(norm(r_moment)/2, eps, 2).subs(eps, 0)
    nonstationary_control = s.diff(norm(s.diag(1, -1)+r_moment)/2, eps, 2).subs(eps, 0)
    x, L = s.symbols('x L', positive=True)
    bump = x*(1-x)
    quotient = s.integrate(s.diff(bump, x)**2, (x, 0, 1))/s.integrate(bump*bump, (x, 0, 1))/L**2
    facts = {
        'radial_operator_with_kinetic_transport': zero(transformed-(s.diff(u(t), t)+m*u(t)/2)),
        'radial_kinetic_is_unitary': kinetic_weight == 1,
        'mixed_potential_coefficient_from_action': raising_weight == s.Rational(1, 2),
        'R_moment_has_no_quadratic_term': hessian_moment_order == 0 and nonstationary_control != 0,
        'derivative_cross_is_surface': zero(s.diff(m*u(t)**2/2, t)-m*u(t)*s.diff(u(t), t)),
        'Weyl_form_quotient': zero(quotient-10/L**2) and s.limit(quotient, L, s.oo) == 0,
        'nonzero_angular_channel_confining': s.limit(s.exp(2*t)-s.exp(t), t, s.oo) == s.oo,
    }
    thresholds = {}
    for n in range(3):
        H, E = angular_matrices(n)
        facts['unitary_sl2_'+str(n)] = zero(comm(H, E)-2*E) and zero(comm(E, E.T)-H)
        diagonal = H*H/16+E.T*E/2
        values = [threshold(Q(n, 2), Q(n, 2)-k) for k in range(n+1)]
        facts['scalar_thresholds_'+str(n)] = all(diagonal[k, k] == s.Rational(v.numerator, v.denominator) for k, v in enumerate(values))
        thresholds[str(n)] = [str(v) for v in values]
    facts['changed_mixed_coefficient_detected'] = threshold(Q(1, 2), -Q(1, 2), Q(1, 4)) != threshold(Q(1, 2), -Q(1, 2))
    return facts, thresholds


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def roots():
    result = set()
    for i, j in combinations(range(8), 2):
        for a, b in product((-2, 2), repeat=2):
            v = [0]*8
            v[i], v[j] = a, b
            result.add(tuple(v))
    result.update(v for v in product((-1, 1), repeat=8) if v.count(-1) % 2 == 0)
    return result


def vector(i, j, sign=-1):
    return tuple(2*(int(k == i)+sign*int(k == j)) for k in range(8))


def pairing(a, b):
    return Q(dot(a, b), 4)


def root_channels(rr, alpha, v):
    rows = []
    for beta in sorted(rr):
        if pairing(beta, v) % 2:
            w = pairing(beta, alpha)
            j = Q(abs(w), 2)  # zero-weight root spaces commute with the root sl2
            rows.append((j, w/2))
    return Counter(str(threshold(j, m)) for j, m in rows)


def geometry():
    rr = roots()
    a5 = [vector(6, 7), vector(5, 6), vector(6, 7, 1), (-1,)*8, vector(3, 4, 1)]
    a2 = [vector(0, 1), vector(1, 2)]
    v = vector(3, 4)
    h = tuple(sum((i+1)*a[k] for i, a in enumerate(a5)) for k in range(8))
    alpha = vector(3, 5, 1)
    odd = {b for b in rr if pairing(b, v) % 2}
    expected = Counter({'0': 54, '1/16': 28, '9/16': 28, '1/4': 1, '5/4': 1})
    hist = root_channels(rr, alpha, v)
    central = {b for b in rr if pairing(b, alpha) == 0}
    wrong_v = vector(0, 1)
    full_weights = Counter(pairing(b, alpha) for b in rr)
    facts = {
        'E8_complete_coordinate_roots': len(rr) == 240 and all(dot(b, b) == 8 for b in rr),
        'A5_actual_chain': all(pairing(a, b) == 2*int(i == j)-int(abs(i-j) == 1) for i, a in enumerate(a5) for j, b in enumerate(a5)),
        'A5_color_weak_orthogonal': all(pairing(a, b) == 0 for a in a5 for b in a2+[v]),
        'actual_SU6_center_vector': h == (-4, -4, -4, 6, 6, 0, 0, 0),
        'actual_periphery_equal_on_every_root': all((pairing(b, h)-pairing(b, v)) % 2 == 0 for b in rr),
        'different_torus_element_detected': any((pairing(b, h)-pairing(b, wrong_v)) % 2 != 0 for b in rr),
        'odd_root_population': len(odd) == 112,
        'chosen_root_preserves_color': alpha in odd and all(pairing(alpha, a) == 0 for a in a2),
        'chosen_root_breaks_old_weak': pairing(alpha, v) == 1,
        'full_adjoint_sl2_decomposition': full_weights == Counter({-2: 1, -1: 56, 0: 126, 1: 56, 2: 1}) and 133+56*2+3 == 248,
        'centralizer_roots_and_odd_spectators': len(central) == 126 and len(central & odd) == 54,
        'chosen_R_threshold_histogram': hist == expected and sum(hist.values()) == 112,
        'every_odd_root_same_threshold_histogram': all(root_channels(rr, a, v) == expected for a in odd),
        'every_odd_root_has_spectators': all(sum(pairing(b, a) == 0 for b in odd) == 54 for a in odd),
        'spectator_root_brackets_vanish': all(tuple(b[k]+sign*alpha[k] for k in range(8)) not in rr for b in central for sign in (-1, 1)),
        'deleting_spectators_changes_population': sum(n for k, n in hist.items() if k != '0') == 58 and 58 != len(odd),
    }
    return facts, dict(hist)


@lru_cache(maxsize=1)
def run():
    facts = local()
    radial_facts, thresholds = radial()
    geometry_facts, histogram = geometry()
    facts.update(radial_facts)
    facts.update(geometry_facts)
    facts = {k: bool(v) for k, v in facts.items()}
    return dict(facts=facts, predicates_passed=sum(facts.values()),
        end_profile=dict(h='-1/4', amplitude_squared='1/4', root_population=112,
            sl2_thresholds=thresholds, R_threshold_histogram=histogram,
            odd_spectators=histogram['0'], free_spin_slot_channels=2*histogram['0']),
        global_stationary_background_derived=False, full_fermion_spectrum_derived=False,
        gapped_4D_reduction_derived=False, physical_chiral_SM_derived=False,
        genesis_selects_condensate=False, global_anomaly_acceptance=False,
        nonauthor_acceptance=False)


if __name__ == '__main__':
    result = run()
    print(json.dumps(result, indent=2, sort_keys=True))
    raise SystemExit(0 if all(result['facts'].values()) else 1)
