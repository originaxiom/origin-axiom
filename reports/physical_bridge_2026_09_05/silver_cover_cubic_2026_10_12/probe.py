"""Whole actual charged three-profile tensor; execution requires published seal."""
import importlib.util
import json
from functools import lru_cache
from itertools import product
from pathlib import Path
import sympy as s

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('cover_cubic_old_transgression', HERE.parent/'silver_charged_cubic_2026_10_11/probe.py')
old = importlib.util.module_from_spec(spec); spec.loader.exec_module(old)
p = old.p; cy = p.cy; z = p.z
FIELDS = {'Q': ('W', -1), 'u': ('W', 4), 'e': ('W', -6), 'd': ('F', -2), 'L': ('F', 3)}
CHANNELS = {'QdL': ('Q', 'd', 'L'), 'eLL': ('e', 'L', 'L'), 'udd': ('u', 'd', 'd')}
PARITY = (0, 1, 1)


def deck_factor(parities):
    return s.simplify(sum(s.prod(((-1)**sheet)**e/s.sqrt(2) for e in parities) for sheet in (0, 1)))


def terms(f, g, k, X, Y):
    return (s.expand(old.down(f, X[1]*g, Y[2]*k)),
            s.expand(old.down(f, Y[1]*g, X[2]*k)))


@lru_cache(None)
def run():
    _, data, w, P, Q, A, B = cy.literal(); facts = {}; fields = {}; counts = {}; hashes = {}
    def ck(key, val):
        facts[key] = bool(val); assert facts[key], key
    for label, a, b, subsets in (('W', A, B, ([0, 1, 2], [0, 1, 2, 3])),
                                ('F', cy.exterior_lie(A), cy.exterior_lie(B), ([0, 1, 2, 4], [0, 1, 2, 3, 4]))):
        E = p.boundary(a, b)
        for sector, subset, wanted in zip(('plus', 'minus'), subsets, (1, 2)):
            M = E['U'].row_join(E['H'][:, subset]); hashes[label+'_'+sector] = old.plane_hash(M)
            for name, (coefficient, h) in FIELDS.items():
                if coefficient != label:
                    continue
                key = name+'_'+sector
                fields[key] = old.primitives(dict(a=a, b=b, M=M), h, ck, key)
                ck(key+'_actual_dimension_and_generic_rank', fields[key]['F'].cols == wanted
                   and p.rank(fields[key]['F'], z) == wanted)
                counts[key] = wanted
    for parity in product((0, 1), repeat=3):
        ck('exact_deck_'+''.join(map(str, parity)), s.simplify(deck_factor(parity)-(1/s.sqrt(2) if sum(parity) % 2 == 0 else 0)) == 0)
    ck('two_odd_vertices_are_retained', deck_factor((0, 1, 1)) != 0 and deck_factor((1, 0, 1)) != 0)
    ck('only_10_bar5_bar5_center_neutral', [n for n in range(4) if (2*n-(3-n)) % 5 == 0] == [1])
    channels = {}; signatures = {}
    for name, labels in CHANNELS.items():
        tensor = []; first = []; second = []; forbidden = []; degrees = []
        ck(name+'_actual_weight_sum', sum(FIELDS[key][1] for key in labels) == 0)
        for ix in product(range(3), repeat=3):
            ps = [fields[label+('_plus' if j == 0 else '_minus')] for label, j in zip(labels, ix)]
            vs = [item['F'][:, 0 if j == 0 else j-1] for item, j in zip(ps, ix)]
            a, b = terms(*vs, [item['a'] for item in ps], [item['Y'] for item in ps])
            D = sum(item['r'] for item in ps)+2; factor = deck_factor(tuple(PARITY[j] for j in ix))
            ck(name+str(ix)+'_degree_bound', all(s.degree(term, z) <= D for term in (a, b) if term != 0))
            # Exact quadratic-field normalization; do not structurally
            # compare factored and distributed symbolic expressions.
            aa = p.dm(s.Matrix([[factor*a]]), z).to_Matrix()[0]
            bb = p.dm(s.Matrix([[factor*b]]), z).to_Matrix()[0]
            tensor.append(s.expand(aa-bb)); first.append(aa); second.append(bb)
            forbidden.append(factor == 0); degrees.append(D)
        if name in ('eLL', 'udd'):
            ck(name+'_all_family_exchange_and_diagonal', all(
                s.expand(tensor[9*i+3*j+k]+tensor[9*i+3*k+j]) == 0 for i, j, k in product(range(3), repeat=3)))
        coeff_nonzero = any(x != 0 for x in tensor)
        term_nonzero = any(x != 0 for x in first+second)
        ck(name+'_not_a_parity_only_instrument', sum(forbidden) == 14 and len(forbidden)-sum(forbidden) == 13)
        classification = 'NONZERO' if coeff_nonzero else 'CANCELLATION' if term_nonzero else 'TERM_WISE_ZERO'
        signatures[name] = classification
        channels[name] = {'shape': [3, 3, 3], 'classification': classification,
                          'degree_bounds': degrees, 'polynomials': list(map(str, tensor)),
                          'first_terms': list(map(str, first)), 'second_terms': list(map(str, second)),
                          'parity_forbidden': forbidden}
    a = s.diag(1, -1, 0, 0, 0); af = cy.exterior_lie(a)
    u = s.eye(5)[:, 0]; g = s.eye(10)[:, old.PAIRS.index((1, 2))]; k = s.eye(10)[:, old.PAIRS.index((3, 4))]
    X = [a, af, af]; Y = [-6*z*s.eye(5), 3*z*s.eye(10), 3*z*s.eye(10)]
    t = terms(u, g, k, X, Y); reverse = terms(u, k, g, X, Y)
    ck('nonzero_off_diagonal_family_comparator', s.expand(t[0]-t[1]+3*z) == 0
       and s.expand(reverse[0]-reverse[1]-3*z) == 0)
    repeated = terms(u, g, g, X, Y)
    ck('diagonal_zero_does_not_imply_off_diagonal_zero', s.expand(repeated[0]-repeated[1]) == 0 and s.expand(t[0]-t[1]) != 0)
    omitted = terms(u, g, k, X, [s.zeros(5), s.zeros(10), s.zeros(10)])
    ck('nonzero_volume_tensor_and_phase_omission_control', old.down(u, g, k) == 1 and omitted == (0, 0))
    ck('all_eighty_one_actual_tensor_slots', sum(len(item['polynomials']) for item in channels.values()) == 81)
    return {'facts': facts, 'exact_predicates': len(facts), 'profile_dimensions': counts,
            'boundary_plane_sha256': hashes, 'channel_classifications': signatures, 'channels': channels,
            'actual_charged_cubic_conditional': True, 'Higgs_added': False,
            'absolute_normalized_Yukawas': False, 'neutral_cubic_computed': False,
            'complete_light_potential': False, 'generated_selection': False,
            'global_quantum_anomaly': False, 'outside_review': False, 'full_goal_achieved': False}


if __name__ == '__main__':
    print(json.dumps(run(), sort_keys=True, indent=2))
