"""Independent Fraction crossed-cochain and weighted proof-case reconstruction."""
import hashlib
import importlib.util
import json
from collections import Counter
from functools import lru_cache
from itertools import combinations, combinations_with_replacement, product
from math import factorial
from pathlib import Path

HERE = Path(__file__).resolve().parent


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    return mod


d = load('cover_neutral_fraction_literal', HERE.parent/'silver_cover_domain_2026_10_12/reference.py')
old = load('cover_neutral_fraction_chart', HERE.parent/'silver_charged_cubic_2026_10_11/reference.py')
c = d.c; r = d.r; K = c.K
ETA = (-1, -1, 1)


def space_hash(a):
    return old.plane_hash(a) if a[0] else hashlib.sha256(b'[]').hexdigest()


def relative(E, ck, tag):
    Z = c.null(c.stack(E['F'], E['R'])); parallel = c.null(E['D'])
    connecting = r.cols(c.mm(E['B'], parallel))
    combined = c.cat(connecting, Z); piv = c.reduced(combined)[1]
    extra = r.subset(combined, [j for j in piv if j >= len(connecting[0])])
    ck(tag+'_full_relative_cocycle_equations', c.zero(c.mm(E['F'], Z)) and c.zero(c.mm(E['R'], Z))
       and c.rank(Z) == len(Z[0]))
    ck(tag+'_nonzero_connecting_image_not_primitive_column_count', c.zero(c.mm(E['D'], parallel))
       and c.zero(c.mm(E['F'], connecting)) and c.zero(c.mm(E['R'], connecting))
       and c.rank(connecting) == len(connecting[0]))
    ck(tag+'_actual_absolute_quotient_outside_coboundaries', c.rank(c.cat(E['B'], extra)) == c.rank(E['B'])+len(extra[0])
       and c.rank(combined) == len(connecting[0])+len(extra[0]) == len(Z[0]))
    rank2 = c.rank(c.cat(E['G'], E['R2']))-c.rank(E['G'])
    ck(tag+'_degree_two_global_parallel_cokernel', rank2+E['absolute_H'][0] == E['boundary_H'][2]
       and rank2 <= E['absolute_H'][2])
    return {'relative_dimension': len(Z[0]), 'connecting_dimension': len(connecting[0]),
            'absolute_direction_dimension': len(extra[0]),
            'relative_space_sha256': space_hash(Z), 'connecting_space_sha256': space_hash(connecting),
            'absolute_H': E['absolute_H'], 'boundary_H': E['boundary_H'],
            'degree_two_restriction_rank': rank2,
            'degree_two_interior_kernel': E['absolute_H'][2]-rank2}, extra


def coefficient_matrix(v, basis, offset):
    out = c.Z(5)
    for j, b in enumerate(basis):
        out = c.add(out, c.scale(b, v[offset+j][0]))
    return out


def pair_matrix(a):
    return [[[str((x if isinstance(x, K) else K(x)).a), str((x if isinstance(x, K) else K(x)).b)] for x in row] for row in a]


def neutral_reason(triple, deck=True, trace_zero=True):
    odd = sum(item[0] for item in triple) % 2
    if deck and odd:
        return 'DECK'
    if trace_zero and any(item[1] for item in triple):
        return 'STOKES'
    return 'UNDETERMINED'


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def vector(i, j, sign=-1):
    return tuple(2*(int(k == i)+sign*int(k == j)) for k in range(8))


@lru_cache(None)
def run():
    data, w, P, Q, A, B = c.literal(); checks = {}; neutral = {}; gauges = {}; odd_cocycle = None
    def ck(key, value):
        checks[key] = bool(value); assert checks[key], key
    basis = c.basis5(); rn = {g: c.ad_group(x, basis) for g, x in w.items()}; T = c.gram(basis)
    for sector, eta in (('plus', (1, 1, 1)), ('minus', ETA)):
        E = d.complex_data({g: c.scale(rn[g], eta[j]) for j, g in enumerate('abt')}, data)
        row, extra = relative(E, ck, 'N_'+sector)
        R, H = E['restriction'], E['H']; b = E['boundary_H'][0]
        S = c.mm(E['J'], c.diag(T, T)); pair = c.mm(c.mm(c.tr(R), S), H)
        piv = c.reduced(pair)[1]; U0 = c.mm(r.subset(H, piv), c.inverse(r.subset(pair, piv)))
        U = c.add(U0, c.scale(c.mm(R, c.mm(c.mm(c.tr(U0), S), U0)), K(1)/2))
        ck('N_'+sector+'_same_full_trace_transverse_plane', c.zero(c.mm(c.mm(c.tr(R), S), R))
           and c.zero(c.mm(c.mm(c.tr(U), S), U)) and c.equal(c.mm(c.mm(c.tr(R), S), U), c.I(b))
           and c.rank(c.cat(R, U)) == 2*b)
        ck('N_'+sector+'_equal_plane_is_opposite', c.rank(c.cat(R, R)) < c.rank(c.cat(R, U)))
        ck('N_'+sector+'_physical_H2_to_absolute_iso_premises', len(R[0])+len(U[0]) == c.rank(c.cat(R, U))
           and row['relative_dimension'] == E['absolute_H'][2] and E['boundary_H'][2] == b)
        row.update(plane_sha256=space_hash(U), restriction_rank=len(R[0]),
                   physical_H1=row['relative_dimension'], physical_H2=E['absolute_H'][2])
        neutral[sector] = row
        if sector == 'minus':
            ck('odd_absolute_actual_representative_not_global_exact', len(extra[0]) == 1)
            matrices = [coefficient_matrix(extra, basis, j*24) for j in range(3)]
            ck('odd_values_are_nonzero_traceless_matrices', all(sum(x[j][j] for j in range(5)) == 0 for x in matrices)
               and any(not c.zero(x) for x in matrices))
            odd_cocycle = {g: pair_matrix(x) for g, x in zip('abt', matrices)}
    ck('thirteen_not_all_exact_and_one_absolute_retained', neutral['plus']['absolute_direction_dimension'] == 0
       and neutral['minus']['absolute_direction_dimension'] == 1
       and neutral['plus']['connecting_dimension'] == neutral['minus']['connecting_dimension'] == 6
       and sum(row['relative_dimension'] for row in neutral.values()) == 13)
    for sector, eta in (('plus', (1, 1, 1)), ('minus', ETA)):
        E = d.complex_data({g: [[eta[j]]] for j, g in enumerate('abt')}, data)
        row, extra = relative(E, ck, 'g_'+sector)
        L = [[0], [1]] if sector == 'plus' else [[1], [1]]
        if sector == 'plus':
            omega = [[0], [0], [1]]
            ck('g_plus_nonexact_ordinary_period_kept', c.zero(c.mm(E['F'], omega))
               and c.equal(c.mm(E['R'], omega), [[0], [1]])
               and c.rank(c.cat(E['B'], omega)) > c.rank(E['B'])
               and c.rank(c.cat(E['restriction'], L)) == 1)
        else:
            ck('g_minus_physical_connecting_zero_trace', row['relative_dimension'] == row['connecting_dimension'] == 1
               and row['absolute_direction_dimension'] == 0 and c.rank(c.cat(E['restriction'], L)) == 2)
        row['physical_H1'] = 1; row['nonexact_ordinary_direction_dimension'] = int(sector == 'plus')
        gauges[sector] = row
    modes = [(0, True)]*neutral['plus']['connecting_dimension']
    modes += [(1, True)]*neutral['minus']['connecting_dimension']
    modes += [(1, False)]*neutral['minus']['absolute_direction_dimension']
    # Independent coverage: enumerate unordered profile multisets and
    # weight by their number of ordered permutations, rather than13^3 loop.
    reasons = Counter()
    for indices in combinations_with_replacement(range(len(modes)), 3):
        mult = factorial(3)
        for count in Counter(indices).values():
            mult //= factorial(count)
        reasons[neutral_reason(tuple(modes[j] for j in indices))] += mult
    ck('all_ordered_neutral_triples_from_weighted_multisets', sum(reasons.values()) == 13**3 and 'UNDETERMINED' not in reasons)
    ck('wrong_ungraded_or_nontransverse_premise_rejected', neutral_reason(((1, False),)*3, deck=False) == 'UNDETERMINED'
       and neutral_reason(((0, True), (1, False), (1, False)), trace_zero=False) == 'UNDETERMINED')
    x, y, zz = c.Z(5), c.Z(5), c.Z(5); x[0][1] = y[1][2] = zz[2][0] = 1
    comm = c.add(c.mm(y, zz), c.mm(zz, y), -1); dens = c.mm(x, comm)
    ck('actual_neutral_density_nonzero_control', sum(dens[j][j] for j in range(5)) == 1)
    ck('even_obstruction_injectivity_and_odd_higher_slot', neutral['plus']['degree_two_interior_kernel'] == 0
       and neutral['minus']['degree_two_interior_kernel'] == 1 and neutral['plus']['degree_two_restriction_rank'] == 6)
    # Independent E8 roots:112 vector plus128 even-sign spinor roots.
    roots = set()
    for i, j in combinations(range(8), 2):
        for a, b in product((-2, 2), repeat=2):
            root = [0]*8; root[i] = a; root[j] = b; roots.add(tuple(root))
    roots.update(signs for signs in product((-1, 1), repeat=8) if sum(x < 0 for x in signs) % 2 == 0)
    gr = [vector(i, i+1) for i in range(4)]
    sr = [vector(6, 7), vector(5, 6), vector(6, 7, 1), (-1,)*8]
    gauge_roots = [root for root in roots if all(dot(root, b) == 0 for b in sr)]
    structure_roots = [root for root in roots if all(dot(root, b) == 0 for b in gr)]
    ck('all_E8_gauge_structure_cross_brackets_zero', len(roots) == 240 and len(gauge_roots) == len(structure_roots) == 20
       and all(dot(a, b) == 0 and tuple(x+y for x, y in zip(a, b)) not in roots
               and a != tuple(-x for x in b) for a in gauge_roots for b in structure_roots)
       and all(dot(a, b) == 0 for a in gr for b in sr)
       and all(dot(a, b) == 0 for a in gr for b in structure_roots)
       and all(dot(a, b) == 0 for a in sr for b in gauge_roots))
    weights = {'Q': -1, 'u': 4, 'e': -6, 'd': -2, 'L': 3, 'N': 0, 'G': 0}
    # Enumerate ordered triples then quotient names, independently.
    mixed = sorted({tuple(sorted(names)) for names in product(weights, repeat=3)
                    if any(key in ('N', 'G') for key in names) and sum(weights[key] for key in names) == 0})
    mixed = [list(row) for row in mixed]
    ck('complete_actual_charge_mixed_catalogue', mixed == [['G', 'G', 'G'], ['G', 'G', 'N'], ['G', 'N', 'N'], ['N', 'N', 'N']])
    expanded = {**weights, 'Qdual': -weights['Q']}
    extra_mixed = {tuple(sorted(names)) for names in product(expanded, repeat=3)
                   if any(key in ('N', 'G') for key in names) and sum(expanded[key] for key in names) == 0}
    ck('conjugate_LEFT_insertion_changes_problem', len(extra_mixed) > len(mixed)
       and tuple(sorted(('Q', 'Qdual', 'N'))) in extra_mixed)
    gauge_reasons = {''.join(map(str, parity)): ('DECK' if sum(parity) % 2 else 'ONE_FORM' if sum(parity) == 0 else 'STOKES')
                     for parity in product((0, 1), repeat=3)}
    return {'checks': checks, 'exact_predicates': len(checks), 'neutral': neutral, 'gauge': gauges,
            'odd_absolute_cocycle_matrices': odd_cocycle, 'neutral_proof_case_counts': dict(reasons),
            'gauge_proof_cases': gauge_reasons, 'mixed_charge_catalogue': mixed,
            'new_native_imported': False, 'remaining_direct_cubic_zero_conditional': True,
            'odd_absolute_mode_retained': True, 'quadratic_flatness_obstruction_zero_conditional': True,
            'higher_odd_obstruction_computed': False, 'quadratic_response_computed': False,
            'real_moment_vacuum_derived': False, 'global_normalized_profiles_computed': False,
            'generated_selection': False, 'global_quantum_anomaly': False,
            'outside_review': False, 'full_goal_achieved': False}


if __name__ == '__main__':
    print(json.dumps(run(), sort_keys=True, indent=2))
