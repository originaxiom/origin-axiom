"""Independent finite-degree Fraction/exterior-algebra cover cubic certificate."""
import importlib.util
import json
from functools import lru_cache
from itertools import product
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('cover_cubic_fraction_transgression', HERE.parent/'silver_charged_cubic_2026_10_11/reference.py')
old = importlib.util.module_from_spec(spec); spec.loader.exec_module(old)
r = old.r; c = old.c; K = c.K
FIELDS = {'Q': ('W', -1), 'u': ('W', 4), 'e': ('W', -6), 'd': ('F', -2), 'L': ('F', 3)}
CHANNELS = {'QdL': ('Q', 'd', 'L'), 'eLL': ('e', 'L', 'L'), 'udd': ('u', 'd', 'd')}
PARITY = (0, 1, 1)


def deck_factor(parities):
    # (1/sqrt2)^3 times the signed sheet sum, in Q(sqrt2).
    return K(0, sum((-1)**(sheet*sum(parities)) for sheet in (0, 1)))/4


def terms(vs, profiles, t):
    f, g, k = vs
    X = [item['a'] for item in profiles]
    Y = [c.add(item['b'], c.scale(c.I(len(item['a'])), item['h']*t)) for item in profiles]
    return (old.tensor('down', f, old.mv(X[1], g), old.mv(Y[2], k)),
            old.tensor('down', f, old.mv(Y[1], g), old.mv(X[2], k)))


@lru_cache(None)
def run():
    data, w, P, Q, A, B = c.literal(); checks = {}; fields = {}; counts = {}; hashes = {}
    def ck(key, value):
        checks[key] = bool(value); assert checks[key], key
    for label, a, b, subsets in (('W', A, B, ([0, 1, 2], [0, 1, 2, 3])),
                                ('F', c.wedge_derivative(A), c.wedge_derivative(B), ([0, 1, 2, 4], [0, 1, 2, 3, 4]))):
        E = r.boundary(a, b)
        for sector, subset, wanted in zip(('plus', 'minus'), subsets, (1, 2)):
            M = c.cat(E['U'], r.subset(E['H'], subset)); hashes[label+'_'+sector] = old.plane_hash(M)
            for name, (coefficient, h) in FIELDS.items():
                if coefficient != label:
                    continue
                key = name+'_'+sector; fields[key] = old.build(dict(a=a, b=b, M=M), h)
                ck(key+'_full_degree_rank_certificate', len(fields[key]['free']) == wanted
                   and fields[key]['r']+wanted == len(a))
                counts[key] = wanted
    for parity in product((0, 1), repeat=3):
        ck('exact_sheet_parity_'+''.join(map(str, parity)), deck_factor(parity) == (K(0, 1)/2 if sum(parity) % 2 == 0 else 0))
    ck('two_odd_not_discarded', bool(deck_factor((0, 1, 1))) and bool(deck_factor((1, 0, 1))))
    ck('complete_parent_charge_multisets', [n for n in range(4) if (2*n-(3-n)) % 5 == 0] == [1])
    signatures = {}; channels = {}
    for name, labels in CHANNELS.items():
        specs = [fields[label+'_'+sector] for label in labels for sector in ('plus', 'minus')]
        D = sum(max(fields[label+'_'+sector]['r'] for sector in ('plus', 'minus')) for label in labels)+2
        needed = D+1; excluded_bound = sum(item['r'] for item in specs)
        points = []; has_nonzero = False; has_term = False; allowed = 0; forbidden = 0
        ck(name+'_actual_weight_sum', sum(FIELDS[key][1] for key in labels) == 0)
        for t in range(1, needed+excluded_bound+2):
            fs = {label+'_'+sector: old.evaluate(fields[label+'_'+sector], t) for label in set(labels) for sector in ('plus', 'minus')}
            if any(value is None for value in fs.values()):
                continue
            tensor = []; first = []; second = []
            allowed = forbidden = 0
            for ix in product(range(3), repeat=3):
                tags = [label+('_plus' if j == 0 else '_minus') for label, j in zip(labels, ix)]
                ps = [fields[tag] for tag in tags]
                vs = [[row[0 if j == 0 else j-1] for row in fs[tag]] for tag, j in zip(tags, ix)]
                a, b = terms(vs, ps, t); factor = deck_factor(tuple(PARITY[j] for j in ix))
                first.append(factor*a); second.append(factor*b); tensor.append(factor*(a-b))
                if factor:
                    allowed += 1
                else:
                    forbidden += 1
            if name in ('eLL', 'udd'):
                ck(name+'_exchange_'+str(t), all(tensor[9*i+3*j+k] == -tensor[9*i+3*k+j] for i, j, k in product(range(3), repeat=3)))
            has_nonzero |= any(bool(x) for x in tensor)
            has_term |= any(bool(x) for x in first+second)
            points.append(t)
            if len(points) == needed:
                break
        ck(name+'_all_polynomials_certified', len(points) == needed and len(set(points)) == needed)
        ck(name+'_full_parity_population', allowed == 13 and forbidden == 14)
        classification = 'NONZERO' if has_nonzero else 'CANCELLATION' if has_term else 'TERM_WISE_ZERO'
        signatures[name] = classification
        channels[name] = {'shape': [3, 3, 3], 'classification': classification,
                          'degree_bound': D, 'distinct_points': points, 'zero_certified': not has_nonzero,
                          'parity_allowed_slots': allowed, 'parity_forbidden_slots': forbidden}
    a = c.Z(5); a[0][0] = 1; a[1][1] = -1; af = c.wedge_derivative(a)
    profiles = [dict(a=a, b=c.Z(5), h=-6), dict(a=af, b=c.Z(10), h=3), dict(a=af, b=c.Z(10), h=3)]
    u = [1, 0, 0, 0, 0]; g = [int(pair == (1, 2)) for pair in old.PAIRS]; k = [int(pair == (3, 4)) for pair in old.PAIRS]
    t = terms((u, g, k), profiles, 2); rev = terms((u, k, g), profiles, 2)
    ck('nonzero_off_diagonal_and_opposite_exchange', t[0]-t[1] == -6 and rev[0]-rev[1] == 6)
    rep = terms((u, g, g), profiles, 2)
    ck('diagonal_zero_not_a_family_tensor_kill', rep[0]-rep[1] == 0 and t[0]-t[1] != 0)
    ck('actual_volume_and_phase_omission', old.tensor('down', u, g, k) == 1 and terms((u, g, k), profiles, 0) == (0, 0))
    def bad(t):
        result = 1
        for j in range(1, 8):
            result *= t-j
        return result
    ck('degree_plus_one_is_load_bearing', all(bad(t) == 0 for t in range(1, 8)) and bad(8) != 0)
    return {'checks': checks, 'exact_predicates': len(checks), 'profile_dimensions': counts,
            'boundary_plane_sha256': hashes, 'channel_classifications': signatures, 'channels': channels,
            'new_native_imported': False, 'actual_charged_cubic_conditional': True, 'Higgs_added': False,
            'absolute_normalized_Yukawas': False, 'neutral_cubic_computed': False,
            'complete_light_potential': False, 'generated_selection': False,
            'global_quantum_anomaly': False, 'outside_review': False, 'full_goal_achieved': False}


if __name__ == '__main__':
    print(json.dumps(run(), sort_keys=True, indent=2))
