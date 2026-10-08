"""Exact roots and matrices for the matched-grading stationary background."""
from collections import Counter
from itertools import combinations, product
from functools import lru_cache
import json
import sympy as s

Q = s.Rational
V = (0, 0, 0, 2, -2, 0, 0, 0)
BETA = (0, 0, 0, 2, 0, 2, 0, 0)
GAMMA = (0, 0, 0, 0, -2, -2, 0, 0)
FOUR = (BETA, (0, 0, 0, 2, 0, -2, 0, 0),
        (0, 0, 0, 0, -2, 0, 2, 0), (0, 0, 0, 0, -2, 0, -2, 0))


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def add(a, b):
    return tuple(x+y for x, y in zip(a, b))


def neg(a):
    return tuple(-x for x in a)


def roots():
    rr = set()
    for i, j in combinations(range(8), 2):
        for a, b in product((-2, 2), repeat=2):
            r = [0]*8
            r[i], r[j] = a, b
            rr.add(tuple(r))
    rr |= {r for r in product((-1, 1), repeat=8) if sum(x < 0 for x in r) % 2 == 0}
    return rr


def comm(a, b):
    return a*b-b*a


def zero(a):
    return all(s.simplify(x) == 0 for x in a)


def triple():
    E = s.sqrt(2)*s.Matrix([[0, 1, 0], [0, 0, 1], [0, 0, 0]])
    return s.diag(2, 0, -2), E, E.T


def e6_data(rr):
    rr6 = {a for a in rr if dot(a, BETA) == dot(a, GAMMA) == 0}
    pos = {a for a in rr6 if a > (0,)*8}
    simple = sorted(a for a in pos if not any(add(b, c) == a for b in pos for c in pos))
    cartan = s.Matrix([[Q(dot(a, b), 4) for b in simple] for a in simple])
    graph = {i: [j for j in range(len(simple)) if i != j and cartan[i, j] != 0] for i in range(len(simple))}
    junctions = [i for i, adj in graph.items() if len(adj) == 3]
    arms = []
    if len(junctions) == 1:
        center = junctions[0]
        for nxt in graph[center]:
            prev, cur, length = center, nxt, 1
            while len(graph[cur]) == 2:
                nxt = next(k for k in graph[cur] if k != prev)
                prev, cur, length = cur, nxt, length+1
            arms.append(length)
    return rr6, simple, cartan, sorted(arms)


def project_e6(a):
    u, w = Q(dot(a, BETA), 4), Q(dot(a, GAMMA), 4)
    x, y = (2*u+w)/3, (u+2*w)/3
    return tuple(a[k]-x*BETA[k]-y*GAMMA[k] for k in range(8))


def orbit(seed, simples):
    seen, queue = {seed}, [seed]
    for a in queue:
        for b in simples:
            c = tuple(a[k]-Q(dot(a, b), 4)*b[k] for k in range(8))
            if c not in seen:
                seen.add(c)
                queue.append(c)
    return seen


def weight_and_spins(rr):
    weights = Counter({0: 8})
    weights.update(dot(a, V)//2 for a in rr)  # H=2v, roots are doubled.
    spins = {j: weights[2*j]-weights[2*j+2] for j in range(max(weights)//2+1)}
    return weights, {j: n for j, n in spins.items() if n}


def radial_blocks(j):
    result = []
    xi = s.symbols('xi', real=True)
    for m in range(-j-1, j+1):
        if m % 2:
            continue
        has_a, has_q = -j <= m <= j, -j <= m+1 <= j
        if not (has_a or has_q):
            continue
        d = Q(m+1, 2)
        k2 = Q((j-m)*(j+m+1), 2) if has_a and has_q else Q(0)
        k = s.sqrt(k2)
        mat = s.Matrix([[s.I*xi+d, k], [-k, -s.I*xi+d]]) if has_a and has_q else s.Matrix([[s.I*xi+d if has_a else -s.I*xi+d]])
        result.append(dict(m=m, has_A=has_a, has_Q=has_q,
                           matrix=mat, square=s.simplify(mat.conjugate().T*mat),
                           threshold=d*d+k2, channels=mat.rows, xi=xi))
    return result


def spectrum(spins):
    full, rhist = Counter(), Counter()
    for j, n in spins.items():
        for block in radial_blocks(j):
            full[str(block['threshold'])] += n*block['channels']
        for m in range(-j, j+1):
            if m % 2:
                rhist[str(Q(m*m, 4)+Q((j-m)*(j+m+1), 2))] += n
    return dict(full), dict(rhist)


def normalized_coefficients():
    y, m = s.symbols('y m', positive=True)
    u = s.Function('u')(y)
    # Dbar / i = d/dy + weight/(2y).
    gauge = s.simplify(s.sqrt(y)*(s.diff(s.sqrt(y)*u, y)+m/(2*y)*s.sqrt(y)*u))
    spin = s.simplify(y*(s.diff(u, y)+(m+1)/(2*y)*u))
    wrong = s.simplify(y*(s.diff(u, y)+m/(2*y)*u))
    gauge_matter = s.sqrt(2)*s.sqrt(y)/(2*s.sqrt(y))
    w_cubic = y/(2*s.sqrt(y))*s.sqrt(2/y)
    return dict(y=y, m=m, u=u, gauge=gauge, spin=spin, wrong=wrong,
                gauge_matter=s.simplify(gauge_matter), w_cubic=s.simplify(w_cubic))


@lru_cache(None)
def run():
    rr = roots()
    H, E, F = triple()
    rr6, simple, cartan, arms = e6_data(rr)
    weights, spins = weight_and_spins(rr)
    full, rhist = spectrum(spins)
    labels = Counter((dot(a, BETA)//4, dot(a, GAMMA)//4) for a in rr)
    defining = {(1, 0), (-1, 1), (0, -1)}
    dual = {(-a, -b) for a, b in defining}
    a2roots = {(2, -1), (-1, 2), (1, 1), (-2, 1), (1, -2), (-1, -1)}
    charged = {project_e6(a) for a in rr if (dot(a, BETA)//4, dot(a, GAMMA)//4) == (1, 0)}
    conjugate = {project_e6(a) for a in rr if (dot(a, BETA)//4, dot(a, GAMMA)//4) == (-1, 0)}
    J = s.Matrix([[0, 0, 1], [0, -1, 0], [1, 0, 0]])
    z = s.symbols('z', nonzero=True)
    transition = s.diag(z, 1, 1/z)
    p = s.diag(-1, 1, -1)
    Tbad = s.diag(1, -1, 0)
    y = s.symbols('y', positive=True)
    Ax, q = -H/(4*y), E/(2*s.sqrt(y))
    dbq = s.I*s.diff(q, y)-s.I*comm(Ax, q)
    f = -s.diff(Ax, y)
    c = normalized_coefficients()
    xi = s.symbols('xi', real=True)
    D = s.I*xi+Q(1, 2)
    wrong_B = s.Matrix([[D, 1], [-1, D]])
    good_B = radial_blocks(1)[1]['matrix']
    x, length = s.symbols('x length', real=True, positive=True)
    bump = x*(1-x)
    rayleigh = s.integrate(s.diff(bump, x)**2, (x, 0, 1))/s.integrate(bump**2, (x, 0, 1))/length**2
    t, nu, drift = s.symbols('t nu drift', real=True)
    u = s.Function('u')(t)
    dvar = drift+nu*s.exp(t)
    angular_square = -s.diff(s.diff(u,t)+dvar*u,t)+dvar*(s.diff(u,t)+dvar*u)
    angular_target = -s.diff(u,t,2)+(nu**2*s.exp(2*t)+nu*(2*drift-1)*s.exp(t)+drift**2)*u
    lower_identity = s.expand(x*x-4*x-(x*x/2-8)-(x-4)**2/2)
    Y = s.symbols('Y', positive=True)
    root_alpha = FOUR[0]
    old_spectators = [a for a in rr if dot(a, V)//4 % 2 and dot(a, root_alpha) == 0]
    facts = {
        'E8_240_distinct_norm2_roots': len(rr) == 240 and all(dot(a, a) == 8 for a in rr),
        'regular_A2_roots': BETA in rr and GAMMA in rr and add(BETA, GAMMA) == V and V in rr and dot(BETA, GAMMA) == -4,
        'regular_A2_not_commuting_A1s': add(BETA, GAMMA) in rr and add(BETA, neg(GAMMA)) not in rr,
        'compact_triple_relations': zero(comm(H, E)-2*E) and zero(comm(E, F)-H) and E.conjugate().T == F,
        'four_root_cross_brackets_zero': all(dot(a, b) == 0 and add(a, b) not in rr and add(a, neg(b)) not in rr for a, b in combinations(FOUR, 2)),
        'four_root_H_is_2v': tuple(sum(a[k] for a in FOUR) for k in range(8)) == tuple(2*a for a in V),
        'all_condensate_roots_odd': all((dot(a, V)//4) % 2 == 1 for a in FOUR+(BETA, GAMMA)),
        'color_commutes': all(dot(a, color) == 0 for a in (BETA, GAMMA) for color in ((2,-2,0,0,0,0,0,0),(0,2,-2,0,0,0,0,0))),
        'integral_v_cocharacter': all(dot(a, V) % 4 == 0 for a in rr),
        'SO3_center_kernel_on_full_E8': all((dot(a, V)//2) % 2 == 0 for a in rr),
        'peripheral_is_actual_old_p': all(dot(a, tuple(V[k]-(-4,-4,-4,6,6,0,0,0)[k] for k in range(8))) % 8 == 0 for a in rr),
        'spin_gauge_weights_cancel': (H*E-E*H)/2 == E,
        'Dbar_q_vanishes': zero(dbq),
        'curvature_moment_vanishes': zero(y*y*f+comm(E/2, F/2)),
        'flat_connection_control_fails': not zero(s.I*s.diff(q, y)) and not zero(comm(E/2, F/2)),
        'wrong_amplitude_control_fails': not zero(y*y*f+comm(E, F)),
        'trace_norm_positive_four_roots': s.trace(F*E) == 4 and s.trace(H*H) == 8,
        'finite_positive_end_norm': s.integrate(s.trace(F*E)/(4*y*y),(y,Y,s.oo))*2*s.pi == 2*s.pi/Y,
        'peripheral_area_limit': all(s.limit(s.exp(s.I*m*(s.pi-s.pi/y)),y,s.oo)==(-1)**m for m in range(3)),
        'full_adjoint_weight_profile': weights == Counter({-4:1,-2:56,0:134,2:56,4:1}),
        'sl2_decomposition_exact': spins == {0:78,1:55,2:1} and sum((2*j+1)*n for j,n in spins.items()) == 248,
        'E6_root_rank_and_population': len(rr6) == 72 and s.Matrix(list(rr6)).rank() == 6,
        'E6_simple_Cartan_graph': len(simple) == 6 and arms == [1,2,2] and cartan.det() == 3,
        'E6_root_reflection_closure': all(tuple(a[k]-dot(a,b)//4*b[k] for k in range(8)) in rr6 for a in rr6 for b in simple),
        'E6_commutes_with_full_A2': all(add(a,b) not in rr and add(a,neg(b)) not in rr for a in rr6 for b in (BETA,GAMMA,V)),
        'E6_saturates_sl2_commutant': len(rr6)+6 == spins[0],
        'A2_full_branching': labels[(0,0)] == 72 and all(labels[k] == 27 for k in defining|dual) and all(labels[k] == 1 for k in a2roots) and set(labels) == defining|dual|a2roots|{(0,0)},
        'charged_27_single_Weyl_orbit': len(charged) == 27 and orbit(next(iter(charged)), simple) == charged,
        'conjugate_27_is_distinct': conjugate == {neg(a) for a in charged} and charged != conjugate,
        'kinetic_rescalings_to_dt': s.simplify(y*y**-2*s.sqrt(y)**2) == 1 and s.simplify(y*Q(1,2)*s.sqrt(2/y)**2) == 1 and y/y == 1,
        'gauge_and_F_derivative_normalization': s.simplify(c['gauge']-c['spin']) == 0,
        'density_shift_control_fails': s.simplify(c['gauge']-c['wrong']) == c['u']/2,
        'both_Yukawa_routes_agree': c['gauge_matter'] == c['w_cubic'] == 1/s.sqrt(2),
        'full_block_squares_diagonal': all(zero(b['square']-(b['xi']**2+b['threshold'])*s.eye(b['channels'])) for j in spins for b in radial_blocks(j)),
        'wrong_adjoint_control_fails': not zero(wrong_B.conjugate().T*wrong_B-(xi**2+Q(5,4))*s.eye(2)),
        'missing_Yukawa_control_fails': not zero(s.diag(D,s.conjugate(D)).conjugate().T*s.diag(D,s.conjugate(D))-good_B.conjugate().T*good_B),
        'R_trace_pairing_matches_old_Hessian': all(Q((m+1)**2,4)+Q((j-m)*(j+m+1),2) == Q((-m-1)**2,4)+Q((j+m+1)*(j-m),2) for j in spins for m in range(-j,j)),
        'full_zero_angular_threshold_profile': full == {'1/4':133,'5/4':110,'9/4':3,'13/4':2},
        'R_zero_angular_threshold_profile': rhist == {'5/4':55,'1/4':55,'13/4':1,'9/4':1},
        'all_full_singular_channels_accounted': sum(full.values()) == 248,
        'old_odd_spectators_retained_as_control': len(old_spectators) == 54,
        'new_no_odd_spin0_spectators': all(dot(a,V) == 0 for a in rr6),
        'positive_essential_threshold_not_zero': min(s.Rational(v) for v in full) == Q(1,4),
        'escaping_form_sequence_excess': s.simplify(rayleigh-10/length**2) == 0,
        'nonzero_angular_square_exact': s.simplify(angular_square-angular_target)==0,
        'uniform_angular_coefficient_bound': max(abs(m+1+sign) for j in spins for m in range(-j-1,j+1) for sign in (-1,1))==4,
        'confining_lower_bound_identity': lower_identity==0,
        'dual_intertwiner_unitary': J.T*J == s.eye(3) and J.det() != 0,
        'dual_intertwines_H_E_F': all(zero(J*T+T.T*J) for T in (H,E,F)),
        'dual_intertwines_spin_transitions': zero(J*transition-transition.inv().T*J),
        'dual_intertwines_peripheral': J*p == p.inv().T*J,
        'outside_SO3_pairing_control_fails': not zero(J*Tbad+Tbad.T*J),
        'all_four_spin_choices_preserve_pair_map': all(zero(J*t-t.inv().T*J) for a,b in product((-1,1), repeat=2) for t in (s.diag(a,1,a),s.diag(b,1,b))),
    }
    for name, ok in facts.items():
        if not bool(ok):
            raise AssertionError(name)
    return dict(facts={k:bool(v) for k,v in facts.items()}, predicates_passed=len(facts),
        root_profile=dict(root_count=len(rr), H_weights={str(k):weights[k] for k in sorted(weights)},
            spin_multiplicities={str(k):spins[k] for k in sorted(spins)}, E6_roots=len(rr6),
            E6_simple_roots_doubled=[list(a) for a in simple],
            E6_Cartan=[list(map(int,cartan.row(i))) for i in range(6)]),
        spectrum_profile=dict(full_squared_thresholds=full,R_squared_thresholds=rhist,
            singular_channels=sum(full.values()),first_order_essential_gap_radius='1/2'),
        pairing_profile=dict(J=[list(map(int,J.row(i))) for i in range(3)],
            complex_charged_pair=[27,27],net_27_chirality=0),
        physical_chirality_achieved=False,global_zero_counts_computed=False,
        genesis_selection_derived=False,physical_goal_achieved=False,nonauthor_acceptance=False)


if __name__ == '__main__':
    print(json.dumps(run(),indent=2,sort_keys=True))
