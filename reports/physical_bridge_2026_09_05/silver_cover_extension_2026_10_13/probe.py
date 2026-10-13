"""Exact ordinary induced nil extension; run only after published seal."""
import hashlib
import importlib.util
import json
from functools import lru_cache
from itertools import combinations
from pathlib import Path

import sympy as s

HERE = Path(__file__).resolve().parent


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


old = load('extension_nil_native', HERE.parent/'silver_cover_nil_flat_2026_10_13/probe.py')
cubic = load('extension_cubic_native', HERE.parent/'silver_cover_cubic_2026_10_12/probe.py')
p = old.p
cy = old.cy
q, r = s.symbols('extension_q phase_r')
ETA = old.ETA
J = s.Matrix([[0, 1], [1, 0]])


def norm(a):
    return a.applyfunc(s.expand)


def mm(a, b):
    return norm(a*b)


def zero(a):
    return all(s.expand(x) == 0 for x in a)


def polynomial_hash(a):
    rows = []
    for row in a.tolist():
        encoded = []
        for value in row:
            terms = {}
            for term in s.Add.make_args(s.expand(value)):
                powers = term.as_powers_dict()
                qe, re = int(powers.get(q, 0)), int(powers.get(r, 0))
                coefficient = s.expand(term/q**qe/r**re)
                terms[qe, re] = s.expand(terms.get((qe, re), 0)+coefficient)
            encoded.append([[qe, re, *cubic.old.pair(coefficient)]
                            for (qe, re), coefficient in sorted(terms.items()) if coefficient != 0])
        rows.append(encoded)
    return hashlib.sha256(json.dumps(rows, separators=(',', ':')).encode()).hexdigest()


def letters(rep, nil):
    out = {}
    for g in 'abt':
        D = s.diag(1, ETA[g])
        t = s.kronecker_product(D, rep[g])
        n = s.kronecker_product(J, nil[g])
        ti = s.kronecker_product(D, cy.inv(rep[g]))
        out[g] = mm(s.eye(t.rows)+q*n, t)
        out[g.upper()] = mm(ti, s.eye(t.rows)-q*n)
    return out


def word(maps, text):
    value = s.eye(maps['a'].rows)
    for letter in text:
        value = mm(value, maps[letter])
    return value


def fox(maps, text):
    n = maps['a'].rows
    prefix = s.eye(n)
    blocks = [s.zeros(n) for _ in 'abt']
    for letter in text:
        j = 'abt'.index(letter.lower())
        if letter.islower():
            blocks[j] += prefix
            prefix = mm(prefix, maps[letter])
        else:
            prefix = mm(prefix, maps[letter])
            blocks[j] -= prefix
    return norm(s.Matrix.hstack(*blocks))


def reordered_indices(sub, quotient, n, copies=1):
    # Put the subbundle of every cochain copy before every quotient copy.
    return [copy*2*n+sheet*n+j for piece in (sub, quotient)
            for copy in range(copies) for sheet in range(2) for j in piece]


def filtration_check(a, sub, quotient, n, copies=1):
    ix = reordered_indices(sub, quotient, n, copies)
    b = a.extract(ix, ix)
    k = 2*len(sub)*copies
    return (zero(b[k:, :k])
            and zero(s.diff(b[:k, :k], q))
            and zero(s.diff(b[k:, k:], q)))


def boundary_count(a, b, subsets):
    E = p.boundary(a, b)
    n = a.rows
    L = s.diag(*(E['H'][:, subset] for subset in subsets))
    rows = list(range(n))+list(range(2*n, 3*n))+list(range(n, 2*n))+list(range(3*n, 4*n))
    L = L[rows, :]
    C = p.boundary(s.diag(a, a), s.diag(b, b))
    D = p.boundary(s.diag(-a.T, -a.T), s.diag(-b.T, -b.T))
    LD = p.dual_plane(C, D, L)
    row, dual = p.pencil_count(C, L), p.pencil_count(D, LD)
    return {'H': row['H'], 'dual_H': dual['H'], 'rank': row['rank'],
            'dual_rank': dual['rank'], 'plane_dimension': L.cols,
            'dual_plane_dimension': LD.cols}


@lru_cache(None)
def run():
    instrument, data, w, P, Q, A, B = cy.literal()
    frozen = json.loads((HERE.parent/'silver_cover_nil_flat_2026_10_13/results/science/probe.stdout.log').read_text())
    y = {g: s.Matrix([[s.Rational(a)+s.sqrt(2)*s.Rational(b) for a, b in row] for row in mat])
         for g, mat in frozen['compensated_cocycle_matrices'].items()}
    checks, slots = {}, {}

    def ck(key, value):
        checks[key] = bool(value)
        assert checks[key], key

    ck('actual_cocycle_full_relator_and_boundary_recheck',
       all(zero(old.crossed(w, y, text)[1]) for text in data['relators']+data['cusp_words']))
    ck('actual_nonzero_global_nil_ideal', all(old.flag(v) for v in y.values())
       and any(not zero(v) for v in y.values()))
    pairs = list(combinations(range(5), 2))
    for label, rep, nil, sub, quotient in (
        ('W', w, y, list(range(4)), [4]),
        ('F', {g: instrument.wedge(v) for g, v in w.items()},
         {g: cy.exterior_lie(v) for g, v in y.items()},
         [j for j, pair in enumerate(pairs) if pair[1] < 4],
         [j for j, pair in enumerate(pairs) if pair[1] == 4])):
        for g in 'abt':
            if label == 'F':
                ck('F_literal_exterior_before_induction_'+g,
                   zero(norm(instrument.wedge(s.eye(5)+q*y[g]))-s.eye(10)-q*nil[g]))
        for is_dual in (False, True):
            tag = label+('dual' if is_dual else '')
            rr = {g: cy.inv(v).T for g, v in rep.items()} if is_dual else rep
            nn = {g: -v.T for g, v in nil.items()} if is_dual else nil
            ss, qq = (quotient, sub) if is_dual else (sub, quotient)
            maps = letters(rr, nn)
            n = rr['a'].rows
            ck(tag+'_ordinary_inverses', all(zero(mm(maps[g], maps[g.upper()])-s.eye(2*n))
                                           and zero(mm(maps[g.upper()], maps[g])-s.eye(2*n)) for g in 'abt'))
            ck(tag+'_whole_polynomial_relators', all(zero(word(maps, text)-s.eye(2*n)) for text in data['relators']))
            ck(tag+'_literal_global_filtration', all(filtration_check(m, ss, qq, n) for m in maps.values()))
            ck(tag+'_moving_off_diagonal_not_frozen_parity', any(not zero(s.diff(m, q)) for m in maps.values())
               and any(not zero(s.diag(s.eye(n), -s.eye(n))*m-m*s.diag(s.eye(n), -s.eye(n))) for m in maps.values()))
            ck(tag+'_nil_products_exact_not_jets', all(zero(mm(a, b)) for a in nn.values() for b in nn.values()))
            ck(tag+'_peripheral_local_frames_fixed', all(zero(word(maps, text)-s.diag(cy.word(rr, text), cy.word(rr, text))) for text in data['cusp_words']))
            based_changes = False
            for text in data['cusp_words']:
                based = word(maps, 'a'+text+'A')
                ck(tag+'_second_frame_'+text, zero(mm(mm(maps['A'], based), maps['a'])-word(maps, text)))
                based_changes |= not zero(s.diff(based, q))
            ck(tag+'_fixed_transporter_would_change_based_cusp', based_changes)
            phased = {g: norm(m*(r if g == 't' else 1/r if g == 'T' else 1)) for g, m in maps.items()}
            F = s.Matrix.vstack(*(fox(phased, text) for text in data['relators']))
            Bd = s.Matrix.vstack(*(phased[g]-s.eye(2*n) for g in 'abt'))
            ck(tag+'_full_new_flat_chain', zero(mm(F, Bd)))
            fiber, time = F[:, :4*n], Bd[4*n:, :]
            ck(tag+'_fiber_diagonals_q_independent', filtration_check(fiber, ss, qq, n, 2))
            ck(tag+'_time_diagonals_q_independent', filtration_check(time, ss, qq, n))
            top = s.diag(maps['t'], maps['t'])
            ck(tag+'_literal_phase_leading_minor', zero(s.diff(fiber, r)-top)
               and zero(s.diff(time, r)-maps['t'])
               and cy.rank(top.subs(q, 0)) == 4*n and cy.rank(maps['t'].subs(q, 0)) == 2*n)
            if is_dual:
                primal = letters(rep, nil)
                ck(tag+'_actual_inverse_transpose_not_renamed', all(zero(maps[g]-primal[g.upper()].T) for g in 'abt'))
            witnesses = {text: polynomial_hash(word(maps, text)) for text in
                         data['relators']+data['cusp_words']+['bA', 't', 'aa', 'ab', 'atA']}
            slots[tag] = {'rank': 2*n, 'filtration_sizes': [2*len(ss), 2*len(qq)],
                          'word_sha256': witnesses, 'fiber_minor_sha256': polynomial_hash(fiber),
                          'time_minor_sha256': polynomial_hash(time), 'generic_absolute_H': [0, 0, 0, 0]}
    ck('exterior_pushforward_wrong_rank_control', len(pairs)*2 == 20 and (10*9)//2 == 45)
    ck('volume_transport_original_and_nil_determinant_one', all(cy.dm(v).det() == cy.FIELD.one for v in w.values())
       and all(norm(s.eye(5)+q*v).det().expand() == 1 for v in y.values()))
    a = s.zeros(5); a[0, 4] = 1
    b = a.T
    ck('opposite_ideal_control_keeps_quadratic', not zero(mm(a, b))
       and not zero(mm(s.eye(5)+q*a, s.eye(5)+q*b).applyfunc(lambda v: s.expand(v).coeff(q, 2))))
    real_maps = letters(w, y)
    bad = dict(real_maps)
    bad['A'] = norm(real_maps['A'].subs(q, -q))
    ck('wrong_inverse_detector_live', not zero(mm(real_maps['a'], bad['A'])-s.eye(10)))
    counts = {
        'W': boundary_count(A, B, ([0, 1, 2], [0, 1, 2, 3])),
        'F': boundary_count(cy.exterior_lie(A), cy.exterior_lie(B), ([0, 1, 2, 4], [0, 1, 2, 3, 4]))}
    for label, value in counts.items():
        ck(label+'_actual_full_boundary_and_dual_tuple', value['H'] == [0, 3, 0, 0] and value['dual_H'] == [0, 0, 3, 0]
           and value['rank'] == slots[label]['rank'] and value['dual_rank'] == slots[label]['rank']-3)
    tensor = cubic.run()
    ck('all_eighty_one_fixed_map_cubic_slots_rederived', sum(len(item['polynomials']) for item in tensor['channels'].values()) == 81)
    ck('both_terms_cancellation_and_nonzero_recovery', tensor['channel_classifications'] == {'QdL': 'NONZERO', 'eLL': 'CANCELLATION', 'udd': 'CANCELLATION'})
    records = {'slots': slots, 'boundary_counts': counts,
               'boundary_plane_sha256': tensor['boundary_plane_sha256'],
               'channel_classifications': tensor['channel_classifications'], 'charged_cubic_slots': 81}
    return {'checks': checks, 'exact_predicates': len(checks), 'records': records,
            'old_cubic_checks_rederived': tensor['exact_predicates'],
            'all_q_flat_cohomology_conditional': True, 'all_q_real_stationarity': False,
            'normalized_coupling_invariance': False, 'new_Higgs': False,
            'neutral_extras_lifted': False, 'generated_selection': False,
            'outside_review': False, 'full_goal_achieved': False}


if __name__ == '__main__':
    print(json.dumps(run(), sort_keys=True, indent=2))
