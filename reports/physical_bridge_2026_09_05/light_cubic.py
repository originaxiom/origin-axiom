"""R56 exact direct-cubic controls; not a profile integral or full EFT."""
from collections import Counter
from functools import lru_cache
from itertools import combinations_with_replacement, permutations
from pathlib import Path
import importlib.util
import json
import sympy as s


def load(name, filename):
    spec = importlib.util.spec_from_file_location(name, Path(__file__).with_name(filename))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


mi = load('r56_clifford_prior', 'mirror_interaction.py')
pb = load('r56_parent_prior', 'parent_background.py')
so = load('r56_twojet_prior', 'neutral_second_order.py')


def zero(m):
    return all(s.simplify(x) == 0 for x in m)


@lru_cache(None)
def representation():
    parent = pb.branching()
    sectors = mi.clifford_data()['sectors']
    matching = [sign for sign in (1, -1) if set(sectors[sign]['weights']) == parent['spin']]
    if len(matching) != 1:
        raise ValueError('Actual parent weight identification failed')
    v = sectors[matching[0]]
    weights = v['weights']
    dual = [tuple(-x for x in w) for w in weights]
    slots = [('S', (0,)*5)] + [('Q', tuple(int(2*x) for x in w)) for w in weights]
    slots += [('T', tuple(int(2*x) for x in w)) for w in dual]
    surviving = Counter()
    total = 0
    for indices in combinations_with_replacement(range(33), 3):
        total += 1
        if all(sum(slots[j][1][k] for j in indices) == 0 for k in range(5)):
            surviving[''.join(slots[j][0] for j in indices)] += 1
    generators = list(v['generators'].values())
    edges = {(i, j) for t in generators for i in range(16) for j in range(i+1, 16)
             if t[i, j] != 0 or t[j, i] != 0}
    seen = {0}
    while True:
        new = seen | {j for i, j in edges if i in seen} | {i for i, j in edges if j in seen}
        if new == seen:
            break
        seen = new
    incidence = s.Matrix([[int(k == i)-int(k == j) for k in range(16)] for i, j in sorted(edges)])
    eye = s.eye(16)
    wrong = s.diag(2, *([1]*15))
    checks = {
        'actual_parent_branching': parent['actual'] == parent['expected'] and parent['actual_spinor'],
        'actual_halfspin_identification': len(matching) == 1 and len(set(weights)) == 16,
        'actual_opposite_set_is_dual': set(dual) == set(sectors[-matching[0]]['weights']),
        'exhaustive_coordinate_cubic_population': total == s.binomial(35, 3),
        'only_SSS_and_SQT_zero_weights': surviving == Counter(SSS=1, SQT=16),
        'forty_five_generators': len(generators) == 45,
        'unitary_compact_generators': all(zero(t.H+t) for t in generators),
        'cartan_is_declared_distinct_weights': all(
            -s.I*v['generators'][(2*k, 2*k+1)] == s.diag(*[w[k] for w in weights]) for k in range(5)),
        'generator_graph_connected': len(seen) == 16,
        'diagonal_commutant_one_dimensional': incidence.rank() == 15,
        'literal_dual_Ward_all': all(zero(t.T*eye+eye*(-t.T)) for t in generators),
        'noninvariant_pairing_rejected': any(not zero(t.T*wrong-wrong*t.T) for t in generators),
        'same_chirality_no_opposite': not (set(weights) & set(dual)),
    }
    return dict(checks=checks, candidate_monomials=total,
                zero_weight_monomials=dict(surviving), graph_vertices=len(seen),
                graph_edges=len(edges), commutant_dimension=16-incidence.rank(),
                parent_clifford_sign=matching[0])


def neutral_controls():
    c, p, sigma = [so.atom(x) for x in ('c', 'p', 'sigma')]
    alpha = so.add(c, so.scale(-1, p))
    b = so.add(so.atom('c2'), so.mul(sigma, c), so.scale(-1, so.mul(c, sigma)),
               so.scale(so.F(1, 2), so.add(so.mul(p, sigma), so.scale(-1, so.mul(sigma, p)))))
    cube = so.mul(alpha, so.mul(alpha, alpha))
    residual = so.add(so.differential(so.mul(alpha, b)), so.scale(-1, cube))
    a = s.diag(1, -1, 0, 0)
    bmat, cmat = s.zeros(4), s.zeros(4)
    bmat[0, 1], cmat[1, 0] = 1, 1
    mats = [a, bmat, cmat]
    trace_cube = 0
    for order in permutations(range(3)):
        sign = (-1)**sum(order[i] > order[j] for i in range(3) for j in range(i+1, 3))
        trace_cube += sign*s.trace(mats[order[0]]*mats[order[1]]*mats[order[2]])
    r, start = s.symbols('r start', positive=True)
    aa, bb = s.Rational(1, 8), s.Rational(1, 7)
    tail = s.integrate(s.exp((aa+bb-1)*r), (r, start, s.oo))
    return {
        'inherited_flat_primitive_identity': not so.formal_flat_residual(),
        'graded_primitive_of_cube': not residual,
        'neutral_form_closed': not so.differential(alpha),
        'cube_not_free_algebra_zero': bool(cube),
        'missing_half_term_rejected': bool(so.formal_flat_residual(half=0)),
        'wrong_commutator_rejected': bool(so.formal_flat_residual(commutator_sign=-1)),
        'noncommuting_pointwise_trace_cube': trace_cube == 6 and s.trace(a*(bmat*cmat-cmat*bmat)) == 2,
        'scalar_tail_control_decays': s.limit(tail, start, s.oo) == 0,
        'tail_control_L2_L4_margins': 4*aa < 1 and 2*bb < 1 and aa+bb < 1,
        'uncontrolled_endpoint_not_integrable': s.integrate(s.Integer(1), (r, start, s.oo)) == s.oo,
    }


def normalization_controls():
    # Exact coordinate fixtures; these numbers are NOT physical couplings/norms.
    y = 2+3*s.I
    ks, kq, kt = s.Integer(2), s.Integer(3), s.Integer(5)
    a, b, c = 2*s.I, s.Integer(3), s.Integer(5)
    lam = y/s.sqrt(ks*kq*kt)
    changed = a*b*c*y/s.sqrt(ks*kq*kt*abs(a*b*c)**2)
    u, v = s.Matrix([[1, s.I], [0, 2]]), s.Matrix([[2, 1], [s.I, 3]])
    gq, gt, pairing = u.H*u, v.H*v, u.T*v
    metric_square = s.simplify(gq.T.inv()*pairing*gt.inv()*pairing.H)
    mutated = pairing.copy(); mutated[0, 0] += 1
    bad = s.simplify(gq.T.inv()*mutated*gt.inv()*mutated.H)
    S, coupling = s.symbols('S coupling', nonzero=True)
    q, t = s.symbols('q0:16'), s.symbols('t0:16')
    w = coupling*S*sum(x*z for x, z in zip(q, t))
    mixed = s.Matrix(16, 16, lambda i, j: s.diff(w, q[i], t[j]))
    hessian = s.zeros(16).row_join(mixed).col_join(mixed.T.row_join(s.zeros(16)))
    return {
        'profile_rescaling_changes_only_phase': s.simplify(changed-s.I*lam) == 0,
        'magnitude_profile_invariant': s.simplify(changed*s.conjugate(changed)-lam*s.conjugate(lam)) == 0,
        'positive_actual_oblique_Grams': gq.is_positive_definite and gt.is_positive_definite,
        'oblique_pairing_metric_spectrum_preserved': metric_square == s.eye(2),
        'ordinary_oblique_spectrum_wrong': pairing*pairing.H != s.eye(2),
        'changed_tensor_not_hidden_by_metric': bad != s.eye(2),
        'mixed_hessian_pairing': mixed == coupling*S*s.eye(16),
        'formal_pairing_rank_sixteen': mixed.rank() == 16,
        'formal_charged_hessian_rank_thirty_two': hessian.rank() == 32,
        'formal_mass_zero_at_origin': hessian.subs(S, 0) == s.zeros(32),
        'no_pure_neutral_cubic_in_polynomial': s.diff(w, S, S, S) == 0,
        'mutation_pure_neutral_detected': s.diff(w+S**3, S, S, S) == 6,
    }


@lru_cache(None)
def report():
    rep = representation()
    groups = {'representation': rep['checks'], 'neutral': neutral_controls(),
              'normalization': normalization_controls()}
    groups = {g: {k: bool(v) for k, v in row.items()} for g, row in groups.items()}
    total = sum(len(row) for row in groups.values())
    passed = sum(sum(row.values()) for row in groups.values())
    return dict(checks=groups, passed=passed, total=total, all_checks_pass=passed == total,
                representation={k: v for k, v in rep.items() if k != 'checks'},
                conditional_direct_cubic='lambda S Q.Qtilde; lambda finite nonzero but unevaluated',
                grade='Finite controls plus conditional authored complete-domain argument',
                global_analytic_proof_machine_verified=False,
                numerical_physical_coupling_computed=False,
                full_EFT_or_nearby_pole_mass_derived=False,
                physical_chirality_derived=False)


if __name__ == '__main__':
    result = report()
    print(json.dumps(result, sort_keys=True))
    raise SystemExit(0 if result['all_checks_pass'] else 1)
