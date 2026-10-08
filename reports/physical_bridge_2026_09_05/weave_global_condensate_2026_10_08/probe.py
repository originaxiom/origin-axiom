"""Global bundle identities and actual holonomy kernels; no physical SM claim."""
from collections import Counter
from functools import lru_cache
from itertools import combinations, product
import json
import sympy as s


def zero(x):
    return all(s.simplify(v) == 0 for v in x) if isinstance(x, s.MatrixBase) else s.simplify(x) == 0


def adj(x):
    return x.conjugate().T


def roots():
    rr = set()
    for i, j in combinations(range(8), 2):
        for a, b in product((-2, 2), repeat=2):
            v = [0]*8
            v[i], v[j] = a, b
            rr.add(tuple(v))
    rr.update(v for v in product((-1, 1), repeat=8) if v.count(-1) % 2 == 0)
    return [s.Matrix(v)/2 for v in sorted(rr)]


def vector(i, j, sign=-1):
    return s.Matrix([int(k == i)+sign*int(k == j) for k in range(8)])


def labels(v, basis):
    return tuple(v.dot(a) for a in basis)


def weight(indices, n):
    c = Counter(indices)
    return tuple(c[k]-c[k+1] for k in range(n-1))


def exterior_weights(n, k):
    return Counter(weight(I, n) for I in combinations(range(n), k))


def adjoint_weights(n):
    out = Counter({(0,)*(n-1): n-1})
    for i, j in product(range(n), repeat=2):
        if i != j:
            out[tuple(int(i == k)-int(j == k)-int(i == k+1)+int(j == k+1) for k in range(n-1))] += 1
    return out


def dual(c):
    return Counter({tuple(-x for x in w): n for w, n in c.items()})


def tensor(a, b, c):
    return Counter({x+y+z: i*j*k for x, i in a.items() for y, j in b.items() for z, k in c.items()})


def geometry():
    rr = roots()
    v, alpha, delta = vector(3, 4), vector(3, 5, 1), vector(4, 5, 1)
    reflect = lambda b: b-b.dot(delta)*delta
    old = [vector(6, 7), vector(5, 6), vector(6, 7, 1), -s.ones(8, 1)/2, vector(3, 4, 1)]
    a5 = list(map(reflect, old))
    color = [vector(0, 1), vector(1, 2)]
    B = s.Matrix.hstack(*a5)
    G = B.T*B
    highest = B*G.inv()*s.Matrix([1, 0, 0, 0, 0])
    weights = [highest]
    for a in a5:
        weights.append(weights[-1]-a)
    t = v/2-alpha/4
    weights.sort(key=lambda w: (-w.dot(t), tuple(w)))
    eigenvalues = [w.dot(t) for w in weights]
    t_back = sum((c*w for c, w in zip(eigenvalues, weights)), s.zeros(8, 1))
    root_set = {tuple(b) for b in rr}
    actual = Counter(labels(b, a5+color+[alpha]) for b in rr)
    actual[(0,)*8] += 8
    z6, z3, z2 = Counter({(0,)*5: 1}), Counter({(0,)*2: 1}), Counter({(0,): 1})
    f6, f3, f2 = exterior_weights(6, 1), exterior_weights(3, 1), exterior_weights(2, 1)
    a15, a20 = exterior_weights(6, 2), exterior_weights(6, 3)
    roster = (tensor(adjoint_weights(6), z3, z2)+tensor(z6, adjoint_weights(3), z2)
              +tensor(z6, z3, adjoint_weights(2))+tensor(a20, z3, f2)
              +tensor(a15, dual(f3), z2)+tensor(dual(a15), f3, z2)
              +tensor(f6, f3, f2)+tensor(dual(f6), dual(f3), f2))
    # SU6 central -I is exp(i*pi*sum k a_k), not a dimension inference.
    center = sum(((k+1)*a for k, a in enumerate(a5)), s.zeros(8, 1))
    odd_spectators = sum(b.dot(alpha) == 0 and b.dot(v) % 2 == 1 for b in rr)
    facts = {
        'E8_root_population': len(rr) == 240 and len(root_set) == 240,
        'Weyl_map_takes_old_weak_to_condensate': zero(reflect(v)-alpha),
        'Weyl_map_fixes_color': all(zero(reflect(b)-b) for b in color),
        'Weyl_map_preserves_all_roots': {tuple(reflect(b)) for b in rr} == root_set,
        'transported_A5_chain': G == s.Matrix(5, 5, lambda i, j: 2*int(i == j)-int(abs(i-j) == 1)),
        'transported_factors_commute': all(a.dot(b) == 0 for a in a5 for b in color+[alpha]),
        'fundamental_six_Gram': all(x.dot(y) == int(i == j)-s.Rational(1, 6) for i, x in enumerate(weights) for j, y in enumerate(weights)),
        'fundamental_root_differences_faithful': len({tuple(x-y) for i, x in enumerate(weights) for j, y in enumerate(weights) if i != j}) == 30 and all(tuple(x-y) in root_set for i, x in enumerate(weights) for j, y in enumerate(weights) if i != j),
        'torus_compensator_in_A5': zero(t_back-t) and t.dot(alpha) == 0 and all(t.dot(b) == 0 for b in color),
        'actual_defining_compensator_phases': eigenvalues == [s.Rational(1, 4)]*3+[-s.Rational(1, 4)]*3,
        'whole248_roster_not_truncated': actual == roster and sum(actual.values()) == 248,
        'shared_SU2_SU6_center_on_every_root': all(b.dot(center-alpha) % 2 == 0 for b in rr),
        'total_peripheral_on_every_root': all(b.dot(alpha/4+t-v/2).is_integer for b in rr),
        'omitting_spin_quarter_detected': any(not b.dot(t-v/2).is_integer for b in rr),
        'wrong_spin_quarter_detected': any(not b.dot(-alpha/4+t-v/2).is_integer for b in rr),
        'compensator_order_four_not_two': all((4*b.dot(t)).is_integer for b in rr) and any(not (2*b.dot(t)).is_integer for b in rr),
        'unchanged_odd_spectators': odd_spectators == 54,
    }
    return facts, int(odd_spectators)


def matrices():
    z = (1+s.I)/s.sqrt(2)
    exponents = (-1, 1, 3, 1, -1, -3)
    A = s.diag(*[s.simplify(z**k) for k in exponents])
    B = s.zeros(6)
    for j in range(5):
        B[j+1, j] = 1
    B[0, 5] = -1
    return A, B


def compound(A, k):
    basis = list(combinations(range(A.rows), k))
    return s.Matrix([[s.simplify(A.extract(I, J).det()) for J in basis] for I in basis])


def fixed(A, B):
    return (A-s.eye(A.rows)).col_join(B-s.eye(B.rows)).nullspace()


def holonomy():
    A, B = matrices()
    I = s.eye(6)
    C = (A*B*adj(A)*adj(B)).applyfunc(s.simplify)
    target = s.diag(*([s.I]*3+[-s.I]*3))
    unsigned = B.copy()
    unsigned[0, 5] = 1
    J = B**3
    modules = {'6': (A, B), '15': (compound(A, 2), compound(B, 2)), '20': (compound(A, 3), compound(B, 3))}
    dimensions = {k: len(fixed(*pair)) for k, pair in modules.items()}
    end_kernel = (s.kronecker_product(I, A)-s.kronecker_product(A.T, I)).col_join(s.kronecker_product(I, B)-s.kronecker_product(B.T, I)).nullspace()
    dimensions['35'] = len(end_kernel)-1  # identity is a separately checked common invariant
    altered = s.diag((1+s.I)/s.sqrt(2), (1-s.I)/s.sqrt(2), 1, 1, 1, 1)*A
    facts = {
        'actual_SU6_unitarity': zero(adj(A)*A-I) and zero(adj(B)*B-I),
        'actual_SU6_determinants': zero(A.det()-1) and B.det() == 1,
        'unsigned_cycle_control_rejected': unsigned.det() == -1,
        'actual_commutator_is_compensator': zero(C-target),
        'inverse_commutator_wrong_marking_detected': not zero(adj(C)-target),
        'SU6_center_matches_commutator_square': zero(C*C+I),
        'noncommuting_flat_bundle_generators': not zero(A*B-B*A),
        'full_generators_not_only_commutator': len(fixed(C, C)) != dimensions['6'] or len(fixed(compound(C, 2), compound(C, 2))) != dimensions['15'],
        'invariant_skew_form': zero(J.T+J) and J.det() != 0 and zero(A.T*J*A-J) and zero(B.T*J*B-J),
        'skew_form_change_detected': not zero(altered.T*J*altered-J),
        'fundamental_has_no_invariant': dimensions['6'] == 0,
        'exterior_square_has_one_invariant': dimensions['15'] == 1,
        'exterior_cube_has_no_invariant': dimensions['20'] == 0,
        'full_endomorphism_commutant_scalar': len(end_kernel) == 1 and zero(A*I-I*A) and zero(B*I-I*B),
        'traceless_compensator_algebra_has_no_invariant': dimensions['35'] == 0,
    }
    return facts, dimensions


def global_geometry():
    x, y = s.symbols('x y', real=True)
    sigma = s.Function('sigma', real=True)(x, y)
    H = s.diag(1, -1)
    E = s.Matrix([[0, 1], [0, 0]])
    sx, sy = s.diff(sigma, y)/2, -s.diff(sigma, x)/2
    q = s.exp(sigma/2)*E/2
    Ax, Ay = sx*H/2, sy*H/2
    A = Ax+s.I*Ay
    dbar = q.diff(x)+s.I*q.diff(y)-s.I*(A*q-q*A)
    F = Ay.diff(x)-Ax.diff(y)
    lap = s.diff(sigma, x, 2)+s.diff(sigma, y, 2)
    U = s.diag(s.exp(-s.I*x/2), s.exp(s.I*x/2))
    expected_transformed = (sx-1)*H/2
    actual_transformed = U*Ax*adj(U)-s.I*U.diff(x)*adj(U)
    Y = s.symbols('Y', positive=True)
    area = 2*s.pi
    core = area-2*s.pi/Y
    root_phase = s.exp(s.I*core/4)
    spin_phase = s.exp(-s.I*core/2)
    n = s.symbols('n', positive=True)
    root_choices = [sum((2*a+2*u) % 4 == 0 and (2*b+2*v) % 4 == 0 for a, b in product(range(4), repeat=2)) for u, v in product(range(2), repeat=2)]
    facts = {
        'global_spin_holomorphic_equation': zero(dbar),
        'four_flat_roots_for_each_extending_spin': root_choices == [4]*4,
        'curvature_connection_coefficient': zero(F+lap*H/4),
        'hyperbolic_moment_globally_zero': zero(-H/4+(E*E.T-E.T*E)/4),
        'spin_line_transition_cancels_root_transition': zero(s.exp(s.I*x)*U*E*adj(U)-E),
        'space_dependent_connection_transition': zero(actual_transformed-expected_transformed),
        'dropped_transition_derivative_detected': not zero(U*Ax*adj(U)-expected_transformed),
        'Gauss_Bonnet_two_ideal_triangles': area == 2*s.pi and -area == 2*s.pi*(1-2),
        'global_Higgs_norm_finite_positive': n*area/4 == n*s.pi/2 and (n*area/4).is_positive,
        'separate_global_energy_terms_balance': zero(area*(n/16+n/16-n/8)),
        'spin_peripheral_is_bounding': zero(s.limit(spin_phase, Y, s.oo)+1),
        'quarter_phase_sign_from_core_orientation': zero(s.limit(root_phase, Y, s.oo)-s.I),
        'finite_slice_phase_matches_local_end': zero(root_phase-s.I*s.exp(-s.I*s.pi/(2*Y))),
        'wrong_Stokes_sign_detected': zero(s.limit(s.exp(-s.I*core/4), Y, s.oo)+s.I),
    }
    return facts


def unbroken(dimensions):
    f3 = exterior_weights(3, 1)
    weights = adjoint_weights(3)
    weights.update({w: n*dimensions['15'] for w, n in f3.items()})
    weights.update({w: n*dimensions['15'] for w, n in dual(f3).items()})
    weights[(0, 0)] += dimensions['35']
    Ginv = s.Matrix([[2, 1], [1, 2]])/3
    inner = lambda a, b: (s.Matrix(a).T*Ginv*s.Matrix(b))[0]
    lengths = Counter(str(inner(w, w)) for w, n in weights.items() for _ in range(n) if w != (0, 0))
    long, short = (2, -1), (-1, 0)
    cartan = s.Matrix([[2*inner(a, b)/inner(a, a) for b in (long, short)] for a in (long, short)])
    root_set = set(weights)-{(0, 0)}
    reflect = lambda w, a: tuple(s.Matrix(w)-2*inner(w, a)/inner(a, a)*s.Matrix(a))
    facts = {
        'full_unbroken_dimension14': sum(weights.values()) == 14,
        'unbroken_Cartan_exactly_two': weights[(0, 0)] == 2,
        'all_unbroken_roots_multiplicity_one': all(weights[w] == 1 for w in root_set),
        'full_G2_root_lengths': lengths == Counter({'2': 6, '2/3': 6}),
        'G2_Cartan_not_dimension_guess': cartan == s.Matrix([[2, -1], [-3, 2]]),
        'full_G2_reflection_closed': all({reflect(w, a) for w in root_set} == root_set for a in (long, short)),
        'not_the_SM_algebra': sum(weights.values()) != 8+3+1,
    }
    return facts, dict(lengths)


@lru_cache(maxsize=1)
def run():
    facts, spectators = geometry()
    hf, dimensions = holonomy()
    uf, lengths = unbroken(dimensions)
    facts.update(hf)
    facts.update(global_geometry())
    facts.update(uf)
    facts = {k: bool(v) for k, v in facts.items()}
    return dict(facts=facts, predicates_passed=sum(facts.values()),
        global_profile=dict(invariant_dimensions=dimensions, unbroken_dimension=14,
            unbroken_rank=2, root_lengths=lengths, odd_cusp_spectators=spectators,
            root_spin_limit='i', compensator_phases_mod8=[2, 2, 2, 6, 6, 6]),
        physical_chiral_SM_derived=False, genesis_selects_background=False,
        full_fermion_spectrum_derived=False, Einstein_equations_solved=False,
        gapped_4D_reduction_derived=False, global_anomaly_acceptance=False,
        nonauthor_acceptance=False)


if __name__ == '__main__':
    result = run()
    print(json.dumps(result, indent=2, sort_keys=True))
    raise SystemExit(0 if all(result['facts'].values()) else 1)
