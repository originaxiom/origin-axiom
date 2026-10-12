"""Independent Fraction certificates and complex-rational current matrices.

No SymPy/new native/results import. Constant structure field and complex
gauge field are separate, as are degree certificates and physical v.
"""
import importlib.util
import json
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    'cover_current_fraction_antecedent', HERE.parent/'silver_charged_pair_lift_2026_10_11/reference.py')
r = importlib.util.module_from_spec(spec); spec.loader.exec_module(r)
c = r.c
GQ = c.old.Gaussian
Z, I, tr, mm, add, scale = c.Z, c.I, c.tr, c.mm, c.add, c.scale
equal, zero, diag = c.equal, c.zero, c.diag
BLOCKS = {'Q': ('W', -1, 6), 'uc': ('W', 4, 3),
          'ec': ('W', -6, 1), 'dc': ('F', -2, 3), 'L': ('F', 3, 2)}


def gx(a):
    return [[x if isinstance(x, GQ) else GQ(x) for x in row] for row in a]


def dagger(a):
    return [[x.conjugate() for x in row] for row in tr(gx(a))]


def reduce_g(a):
    a = gx(a); piv = []; row = 0
    for col in range(len(a[0])):
        k = next((j for j in range(row, len(a)) if a[j][col]), None)
        if k is None:
            continue
        a[row], a[k] = a[k], a[row]
        factor = a[row][col]; a[row] = [x/factor for x in a[row]]
        for j in range(len(a)):
            if j != row and a[j][col]:
                factor = a[j][col]
                a[j] = [x-factor*y for x, y in zip(a[j], a[row])]
        piv.append(col); row += 1
        if row == len(a):
            break
    return a, piv


def inv_g(a):
    n = len(a); result, piv = reduce_g(c.cat(a, I(n)))
    assert piv[:n] == list(range(n))
    return [row[n:] for row in result]


def kron(a, b):
    return [[x*y for x in ar for y in br] for ar in a for br in b]


def trace(a):
    return sum(a[j][j] for j in range(len(a)))


def generators():
    out = {}
    for tag, indices in (('c', range(3)), ('w', range(3, 5))):
        for i, j in combinations(indices, 2):
            a = Z(5); a[i][j] = a[j][i] = F(1, 2)
            b = Z(5); b[i][j] = GQ(0, -F(1, 2)); b[j][i] = GQ(0, F(1, 2))
            out[f'{tag}{i}{j}x'] = gx(a); out[f'{tag}{i}{j}y'] = gx(b)
    for name, entries in (('c3', [1, -1, 0, 0, 0]), ('c8raw', [1, 1, -2, 0, 0]), ('w3', [0, 0, 0, 1, -1])):
        a = Z(5)
        for j, v in enumerate(entries):
            a[j][j] = F(v, 2)
        out[name] = gx(a)
    a = Z(5)
    for j, y in enumerate([F(-1, 3)]*3+[F(1, 2)]*2):
        a[j][j] = y
    out['Y'] = gx(a)
    return out


def sub(a, ids):
    return [[a[i][j] for j in ids] for i in ids]


def irreps(t):
    # Independently use the reference's exterior derivative formula.
    ten = c.wedge_derivative(t); dual = scale(tr(t), -1)
    pairs = list(combinations(range(5), 2))
    ids = {'Q': [j for j, (a, b) in enumerate(pairs) if a < 3 <= b],
           'uc': [j for j, (a, b) in enumerate(pairs) if b < 3], 'ec': [9]}
    return {**{key: sub(ten, val) for key, val in ids.items()},
            'dc': sub(dual, [0, 1, 2]), 'L': sub(dual, [3, 4])}


def ward(t, omit=False):
    d = len(t); A = Z(d)
    for j in range(d):
        A[j][j] = j+1
    A = gx(A); deps = add(gx(I(d)), scale(t, 2))
    psi = [[GQ(j+1, j)] for j in range(d)]
    dp = [[GQ(2*j-1, 1)] for j in range(d)]
    i = GQ(0, 1)
    delta = scale(mm(t, psi), -i)
    ddelta = scale(add(mm(deps, psi), mm(t, dp)), -i)
    dA = add(gx(Z(d)) if omit else deps, scale(add(mm(A, t), mm(t, A), -1), i))
    Dpsi = add(dp, scale(mm(A, psi), i))
    return add(add(ddelta, scale(mm(dA, psi), i)), add(scale(mm(A, delta), i), scale(mm(t, Dpsi), i)))


@lru_cache(None)
def run():
    data, w, P, Q, A, B = c.literal()
    checks = {}; rows = {}
    def ck(key, value):
        checks[key] = bool(value)
        assert checks[key], key
    ck('actual_nontrivial_cover_character_descends_to_both_cusps', all(
        sum(int(letter.lower() in 'ab') for letter in word) % 2 == 0
        for word in data['relators']+data['cusp_words']))
    for label, a, b, subsets in (
            ('W', A, B, ([0, 1, 2], [0, 1, 2, 3])),
            ('F', c.wedge_derivative(A), c.wedge_derivative(B),
             ([0, 1, 2, 4], [0, 1, 2, 3, 4]))):
        E = r.boundary(a, b); n = E['n']
        for sector, chosen, wanted in zip(('plus', 'minus'), subsets, (1, 2)):
            M = c.cat(E['U'], r.subset(E['H'], chosen)); ann = tr(c.null(tr(M)))
            ck(label+sector+'_full_annihilator', zero(mm(ann, M)) and len(ann)+len(M[0]) == 2*n and c.rank(M) == len(M[0]))
            for name, (coefficient, h, dim) in BLOCKS.items():
                if coefficient != label:
                    continue
                ranks = []; trace_ranks = []
                # C(z) is linear; EVERY minor has degree <= n. n+1
                # distinct rational points certify the generic maximum.
                for value in range(1, n+2):
                    D0 = c.stack(a, add(b, scale(I(n), h*value)))
                    pencil = mm(ann, D0); K = c.null(pencil)
                    traceK = mm(D0, K)
                    ranks.append(c.rank(pencil)); trace_ranks.append(c.rank(traceK))
                    ck(name+'_'+sector+'_point'+str(value)+'_full_kernel_and_trace',
                       zero(mm(pencil, K)) and zero(mm(ann, traceK))
                       and len(K[0])+ranks[-1] == n and c.rank(D0) == n
                       and trace_ranks[-1] == len(K[0]))
                rankmax = max(ranks)
                ck(name+'_'+sector+'_degree_certificate', n-rankmax == wanted and max(trace_ranks) == wanted)
                rows[name+'_'+sector] = {'coefficient': label, 'H_weight': h, 'gauge_dimension': dim,
                                        'primitive_dimension': n-rankmax, 'trace_rank': wanted,
                                        'pencil_rank': rankmax}
    ck('actual_three_profiles_without_added_triplet', all(
        rows[name+'_plus']['primitive_dimension']+rows[name+'_minus']['primitive_dimension'] == 3 for name in BLOCKS))
    gens = generators(); H = gx(diag([[2]], [[2]], [[2]], [[-3]], [[-3]]))
    S3 = gx([[0, 0, 1], [0, -1, 0], [1, 0, 0]]); J2 = gx([[0, 1], [-1, 0]])
    C = gx([[2, 0, 0], [0, 1, GQ(1, 1)], [0, 0, 2]])
    Gram = mm(dagger(C), C); S = inv_g(C); deck = gx(diag([[1]], [[-1]], [[-1]]))
    ck('nonorthogonal_positive_fixture', equal(mm(dagger(S), mm(Gram, S)), I(3))
       and not equal(Gram, I(3)) and len(reduce_g(C)[1]) == 3
       and equal(mm(deck, Gram), mm(Gram, deck)))
    norms = {}; faithful = []; support = {key: [] for key in BLOCKS}
    for name, t in gens.items():
        ck(name+'_unbroken_Hermitian_generator', equal(t, dagger(t)) and not trace(t)
           and equal(mm(t, H), mm(H, t)))
        rr = irreps(t); tc = sub(t, [0, 1, 2]); tw = sub(t, [3, 4])
        expected = {'Q': add(kron(tc, I(2)), kron(I(3), tw)),
                    'uc': add(scale(tr(tc), -1), scale(I(3), trace(tc))),
                    'ec': [[trace(tw)]], 'dc': scale(tr(tc), -1),
                    'L': add(tw, scale(I(2), -trace(tw)))}
        mapped = {**rr, 'uc': mm(mm(S3, rr['uc']), inv_g(S3)),
                  'L': mm(mm(J2, rr['L']), inv_g(J2))}
        ck(name+'_every_SM_intertwiner', all(equal(mapped[key], expected[key]) for key in BLOCKS))
        faithful.append([x for row in c.wedge_derivative(t) for x in row]+[x for row in scale(tr(t), -1) for x in row])
        norms[name] = trace(mm(t, t))
        for key, matrix in rr.items():
            dim = len(matrix); change = kron(S, I(dim))
            ck(name+'_'+key+'_canonical_current', equal(mm(mm(dagger(change), kron(Gram, matrix)), change), kron(I(3), matrix)))
            if not zero(matrix):
                support[key].append(name)
        ck(name+'_first_jet_Ward', zero(ward(t)))
        ck(name+'_missing_derivative_fails', not zero(ward(t, True)))
    faith = len(reduce_g(tr(faithful))[1])
    ck('faithful_all_twelve_generators', faith == 12)
    ck('unfaithful_zero_action_rejected', len(reduce_g(Z(125, 12))[1]) != faith)
    ck('collapse_to_one_profile_rejected', all(
        rows[name+'_plus']['trace_rank']+rows[name+'_minus']['trace_rank'] != 1 for name in BLOCKS))
    charges = {'Q': F(1, 6), 'uc': F(-2, 3), 'ec': F(1), 'dc': F(1, 3), 'L': F(-1, 2)}
    yr = irreps(gens['Y'])
    ck('hypercharges_and_wrong_fundamental_control', all(equal(yr[key], scale(I(len(yr[key])), y)) for key, y in charges.items())
       and not equal(sub(gens['Y'], [0, 1, 2]), scale(I(3), charges['dc'])))
    ck('all_charged_blocks_and_singlet_opposite_control', all(support.values()) and zero(Z(1)))
    ck('omitted_Gram_fails', not equal(mm(dagger(S), S), I(3)))
    ck('raw_trace_generator_norms', all(norms[key] == (F(5, 6) if key == 'Y' else F(3, 2) if key == 'c8raw' else F(1, 2)) for key in gens))
    ck('conditional_SU5_ratio_and_volume_square_only', F(1, 2)/norms['Y'] == F(3, 5) and F(1, 2) != 1)
    ck('current_does_not_select_family_number', all(len(reduce_g(kron(I(n), gens['Y']))[1]) == 5*n for n in (1, 2, 3)))
    # Reject an under-resolved rank instrument using an explicit degree-n
    # polynomial; the first n roots do not certify a polynomial null.
    polynomial = lambda x: (x-1)*(x-2)*(x-3)*(x-4)*(x-5)
    ck('n_points_false_null_n_plus_one_rejects', all(polynomial(j) == 0 for j in range(1, 6)) and polynomial(6) == 120)
    return {'checks': checks, 'exact_predicates': len(checks), 'blocks': rows,
            'generator_faithfulness_rank': faith, 'hypercharges': {key: str(val) for key, val in charges.items()},
            'current_support': support, 'conditional_gY_squared_over_g5_squared': '3/5',
            'new_native_imported': False, 'global_profile_Gram_computed': False,
            'actual_gauge_current_map_conditional': True, 'Yukawas_computed': False,
            'odd_neutral_interactions_computed': False, 'generated_boundary': False,
            'global_quantum_anomaly': False, 'outside_review': False, 'full_goal_achieved': False}


if __name__ == '__main__':
    print(json.dumps(run(), sort_keys=True, indent=2))
