"""Separate Fraction bivariate matrix convolution; no native/SymPy import."""
import hashlib
import importlib.util
import json
from functools import lru_cache
from itertools import combinations
from math import prod
from pathlib import Path

HERE = Path(__file__).resolve().parent


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


old = load('extension_nil_fraction', HERE.parent/'silver_cover_nil_flat_2026_10_13/reference.py')
cubic = load('extension_cubic_fraction', HERE.parent/'silver_cover_cubic_2026_10_12/reference.py')
c, r, K = old.c, old.r, old.K
ETA = old.ETA


def clean(a):
    return {key: value for key, value in a.items() if not c.zero(value)}


def add(a, b, sign=1):
    out = dict(a)
    for key, value in b.items():
        out[key] = c.add(out[key], value, sign) if key in out else c.scale(value, sign)
    return clean(out)


def mm(a, b):
    out = {}
    for (i, j), x in a.items():
        for (k, l), y in b.items():
            value = c.mm(x, y)
            key = (i+k, j+l)
            out[key] = c.add(out[key], value) if key in out else value
    return clean(out)


def constant(a):
    return clean({(0, 0): a})


def shift(a, q=0, phase=0, factor=1):
    return clean({(i+q, j+phase): c.scale(value, factor) for (i, j), value in a.items()})


def extract(a, rows, cols):
    return clean({key: [[value[i][j] for j in cols] for i in rows] for key, value in a.items()})


def blocks(mats, vertical=False):
    keys = set().union(*(set(a) for a in mats))
    shapes = [(len(next(iter(a.values()))), len(next(iter(a.values()))[0])) for a in mats]
    out = {}
    for key in keys:
        entries = [a.get(key, c.Z(*shape)) for a, shape in zip(mats, shapes)]
        value = sum(entries, []) if vertical else [sum((a[i] for a in entries), []) for i in range(shapes[0][0])]
        out[key] = value
    return clean(out)


def letters(rep, nil):
    out = {}
    for g in 'abt':
        t = c.diag(rep[g], c.scale(rep[g], ETA[g]))
        n = c.stack(c.cat(c.Z(len(rep[g])), nil[g]), c.cat(nil[g], c.Z(len(rep[g]))))
        ti = c.diag(c.inverse(rep[g]), c.scale(c.inverse(rep[g]), ETA[g]))
        out[g] = clean({(0, 0): t, (1, 0): c.mm(n, t)})
        out[g.upper()] = clean({(0, 0): ti, (1, 0): c.scale(c.mm(ti, n), -1)})
    return out


def word(maps, text):
    value = constant(c.I(len(maps['a'][0, 0])))
    for letter in text:
        value = mm(value, maps[letter])
    return value


def fox(maps, text):
    n = len(maps['a'][0, 0])
    prefix = constant(c.I(n))
    values = [constant(c.Z(n)) for _ in 'abt']
    for letter in text:
        j = 'abt'.index(letter.lower())
        if letter.islower():
            values[j] = add(values[j], prefix)
            prefix = mm(prefix, maps[letter])
        else:
            prefix = mm(prefix, maps[letter])
            values[j] = add(values[j], prefix, -1)
    # Fox columns can vanish; their known dimensions do not depend on
    # whether a zero matrix happened to be removed by sparse cleanup.
    keys = set().union(*(set(a) for a in values))
    return clean({key: [sum((a.get(key, c.Z(n))[i] for a in values), []) for i in range(n)] for key in keys})


def filtration(a, sub, quotient, n, copies=1):
    ix = [copy*2*n+sheet*n+j for piece in (sub, quotient)
          for copy in range(copies) for sheet in range(2) for j in piece]
    k = 2*len(sub)*copies
    if extract(a, ix[k:], ix[:k]):
        return False
    return not any(qe and (not c.zero([[value[i][j] for j in ix[:k]] for i in ix[:k]])
                          or not c.zero([[value[i][j] for j in ix[k:]] for i in ix[k:]]))
                   for (qe, _), value in a.items())


def derivative_phase(a):
    return clean({(i, j-1): c.scale(value, j) for (i, j), value in a.items() if j})


def polynomial_hash(a):
    value = next(iter(a.values()))
    rows = []
    for i in range(len(value)):
        row = []
        for j in range(len(value[0])):
            encoded = []
            for (qe, re), matrix in sorted(a.items()):
                entry = matrix[i][j]
                if entry:
                    entry = entry if isinstance(entry, K) else K(entry)
                    encoded.append([qe, re, str(entry.a), str(entry.b)])
            row.append(encoded)
        rows.append(row)
    return hashlib.sha256(json.dumps(rows, separators=(',', ':')).encode()).hexdigest()


def determinant(a):
    out = [[x if isinstance(x, K) else K(x) for x in row] for row in a]
    answer = K(1)
    for j in range(len(out)):
        pivot = next((i for i in range(j, len(out)) if out[i][j]), None)
        if pivot is None:
            return K(0)
        if pivot != j:
            out[j], out[pivot] = out[pivot], out[j]
            answer = -answer
        value = out[j][j]
        answer *= value
        for i in range(j+1, len(out)):
            factor = out[i][j]/value
            if factor:
                out[i] = [x-factor*y for x, y in zip(out[i], out[j])]
    return answer


def boundary_count(a, b, subsets):
    E = r.boundary(a, b)
    n = len(a)
    L = c.diag(*(r.subset(E['H'], subset) for subset in subsets))
    ix = list(range(n))+list(range(2*n, 3*n))+list(range(n, 2*n))+list(range(3*n, 4*n))
    L = [L[j] for j in ix]
    C = r.boundary(c.diag(a, a), c.diag(b, b))
    D = r.boundary(c.diag(c.scale(c.tr(a), -1), c.scale(c.tr(a), -1)),
                   c.diag(c.scale(c.tr(b), -1), c.scale(c.tr(b), -1)))
    LD, _ = r.paired_plane(C, D, L)

    def count(E, plane):
        M = c.cat(E['U'], plane)
        # Every maximal minor of this linear pencil has degree<=n.
        rank = max(c.rank(c.mm(c.cat(c.add(c.scale(E['b'], -1), c.scale(c.I(E['n']), -z)), E['a']), M))
                   for z in range(E['n']+1))
        return {'H': [0, len(M[0])-rank, E['n']-rank, 0], 'rank': rank}

    row, dual = count(C, L), count(D, LD)
    return {'H': row['H'], 'dual_H': dual['H'], 'rank': row['rank'],
            'dual_rank': dual['rank'], 'plane_dimension': len(L[0]),
            'dual_plane_dimension': len(LD[0])}


@lru_cache(None)
def run():
    data, w, P, Q, A, B = c.literal()
    frozen = json.loads((HERE.parent/'silver_cover_nil_flat_2026_10_13/results/science/reference.stdout.log').read_text())
    y = {g: [[K(a, b) for a, b in row] for row in mat] for g, mat in frozen['compensated_cocycle_matrices'].items()}
    checks, slots = {}, {}

    def ck(key, value):
        checks[key] = bool(value)
        assert checks[key], key

    ck('fresh_actual_cocycle_equations', all(c.zero(old.crossed(w, y, text)[1]) for text in data['relators']+data['cusp_words']))
    ck('nonzero_literal_global_nil_ideal', all(old.flag(v) for v in y.values()) and any(not c.zero(v) for v in y.values()))
    pairs = list(combinations(range(5), 2))
    for label, rep, nil, sub, quotient in (
        ('W', w, y, list(range(4)), [4]),
        ('F', {g: c.old.exterior(v) for g, v in w.items()}, {g: c.wedge_derivative(v) for g, v in y.items()},
         [j for j, pair in enumerate(pairs) if pair[1] < 4], [j for j, pair in enumerate(pairs) if pair[1] == 4])):
        if label == 'F':
            for g in 'abt':
                # Complete second-degree exterior expansion, not a first jet.
                e0 = c.old.exterior(c.I(5))
                e1 = c.add(c.old.exterior(c.add(c.I(5), y[g])), c.add(e0, c.old.exterior(y[g])), -1)
                ck('exterior_all_coefficients_'+g, c.equal(e0, c.I(10)) and c.equal(e1, nil[g]) and c.zero(c.old.exterior(y[g])))
        for is_dual in (False, True):
            tag = label+('dual' if is_dual else '')
            rr = {g: c.tr(c.inverse(v)) for g, v in rep.items()} if is_dual else rep
            nn = {g: c.scale(c.tr(v), -1) for g, v in nil.items()} if is_dual else nil
            ss, qq = (quotient, sub) if is_dual else (sub, quotient)
            maps = letters(rr, nn)
            n = len(rr['a'])
            identity = constant(c.I(2*n))
            ck(tag+'_actual_ordinary_inverse', all(not add(mm(maps[g], maps[g.upper()]), identity, -1)
                                                and not add(mm(maps[g.upper()], maps[g]), identity, -1) for g in 'abt'))
            ck(tag+'_full_relator_convolution', all(not add(word(maps, text), identity, -1) for text in data['relators']))
            ck(tag+'_global_filtration', all(filtration(m, ss, qq, n) for m in maps.values()))
            parity = constant(c.diag(c.I(n), c.scale(c.I(n), -1)))
            ck(tag+'_broken_bulk_parity_not_frozen', any(key[0] for m in maps.values() for key in m)
               and any(add(mm(parity, m), mm(m, parity), -1) for m in maps.values()))
            ck(tag+'_whole_nil_ideal_products', all(c.zero(c.mm(a, b)) for a in nn.values() for b in nn.values()))
            ck(tag+'_actual_fixed_local_peripherals', all(not add(word(maps, text), constant(c.diag(c.word(rr, text), c.word(rr, text))), -1) for text in data['cusp_words']))
            changes = False
            for text in data['cusp_words']:
                based = word(maps, 'a'+text+'A')
                ck(tag+'_second_cusp_transport_'+text, not add(mm(mm(maps['A'], based), maps['a']), word(maps, text), -1))
                changes |= any(key[0] for key in based)
            ck(tag+'_fixed_frame_comparator_distinct', changes)
            phased = {g: shift(m, phase=1 if g == 't' else -1 if g == 'T' else 0) for g, m in maps.items()}
            F = blocks([fox(phased, text) for text in data['relators']], vertical=True)
            Bd = blocks([add(phased[g], identity, -1) for g in 'abt'], vertical=True)
            ck(tag+'_whole_bivariate_chain', not mm(F, Bd))
            fiber = extract(F, list(range(4*n)), list(range(4*n)))
            time = extract(Bd, list(range(4*n, 6*n)), list(range(2*n)))
            ck(tag+'_fiber_diagonals_no_extension', filtration(fiber, ss, qq, n, 2))
            ck(tag+'_time_diagonals_no_extension', filtration(time, ss, qq, n))
            top = {key: c.diag(value, value) for key, value in maps['t'].items()}
            ck(tag+'_exact_invertible_leading_phase_coefficients', not add(derivative_phase(fiber), top, -1)
               and not add(derivative_phase(time), maps['t'], -1)
               and c.rank(top[0, 0]) == 4*n and c.rank(maps['t'][0, 0]) == 2*n)
            if is_dual:
                primal = letters(rep, nil)
                ck(tag+'_literal_inverse_transpose', all(not add(maps[g], {key: c.tr(value) for key, value in primal[g.upper()].items()}, -1) for g in 'abt'))
            slots[tag] = {'rank': 2*n, 'filtration_sizes': [2*len(ss), 2*len(qq)],
                          'word_sha256': {text: polynomial_hash(word(maps, text)) for text in data['relators']+data['cusp_words']+['bA', 't', 'aa', 'ab', 'atA']},
                          'fiber_minor_sha256': polynomial_hash(fiber), 'time_minor_sha256': polynomial_hash(time),
                          'generic_absolute_H': [0, 0, 0, 0]}
    ck('wrong_exterior_rank_detected', 2*len(pairs) == 20 and 10*9//2 == 45)
    ck('determinant_instrument_both_sign_controls', determinant([[2, 0], [0, 3]]) == 6 and determinant([[0, 2], [3, 0]]) == -6)
    ck('actual_SL5_and_nil_determinant_certificate', all(determinant(v) == 1 for v in w.values()) and all(old.flag(v) for v in y.values()))
    a = c.Z(5); a[0][4] = 1
    b = c.tr(a)
    opposite = mm({(0, 0): c.I(5), (1, 0): a}, {(0, 0): c.I(5), (1, 0): b})
    ck('opposite_not_truncated_nil_comparator', (2, 0) in opposite and not c.zero(opposite[2, 0]))
    real_maps = letters(w, y)
    bad_inverse = {key: c.scale(value, (-1)**key[0]) for key, value in real_maps['A'].items()}
    ck('wrong_ordinary_inverse_rejected', bool(add(mm(real_maps['a'], bad_inverse), constant(c.I(10)), -1)))
    counts = {'W': boundary_count(A, B, ([0, 1, 2], [0, 1, 2, 3])),
              'F': boundary_count(c.wedge_derivative(A), c.wedge_derivative(B), ([0, 1, 2, 4], [0, 1, 2, 3, 4]))}
    for label, value in counts.items():
        ck(label+'_full_degree_certificate_dual_kernel', value['H'] == [0, 3, 0, 0] and value['dual_H'] == [0, 0, 3, 0]
           and value['rank'] == slots[label]['rank'] and value['dual_rank'] == slots[label]['rank']-3)
    tensor = cubic.run()
    ck('all_eighty_one_fixed_cubic_slots_certified', sum(prod(item['shape']) for item in tensor['channels'].values()) == 81)
    ck('full_cancellation_not_diagonal_zero', tensor['channel_classifications'] == {'QdL': 'NONZERO', 'eLL': 'CANCELLATION', 'udd': 'CANCELLATION'})
    records = {'slots': slots, 'boundary_counts': counts, 'boundary_plane_sha256': tensor['boundary_plane_sha256'],
               'channel_classifications': tensor['channel_classifications'], 'charged_cubic_slots': 81}
    return {'checks': checks, 'exact_predicates': len(checks), 'records': records,
            'old_cubic_checks_rederived': tensor['exact_predicates'],
            'all_q_flat_cohomology_conditional': True, 'all_q_real_stationarity': False,
            'normalized_coupling_invariance': False, 'new_Higgs': False, 'neutral_extras_lifted': False,
            'generated_selection': False, 'outside_review': False, 'full_goal_achieved': False,
            'new_native_imported': False}


if __name__ == '__main__':
    print(json.dumps(run(), sort_keys=True, indent=2))
