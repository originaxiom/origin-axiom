"""Actual relative neutral cocycles and the remaining cubic/obstruction premises.

No scientific execution before this complete packet is published/sealed.
Authored analytic consequences are distinguished from finite algebra.
"""
import importlib.util
import json
from collections import Counter
from functools import lru_cache
from itertools import combinations_with_replacement, product
from pathlib import Path
import sympy as s

HERE = Path(__file__).resolve().parent


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    return mod


d = load('cover_neutral_literal', HERE.parent/'silver_cover_domain_2026_10_12/probe.py')
oldc = load('cover_neutral_chart', HERE.parent/'silver_charged_cubic_2026_10_11/probe.py')
pt = oldc.pt; p = d.p; cy = p.cy
ETA = (-1, -1, 1)


def neutral_reason(triple, deck=True, trace_zero=True):
    if deck and sum(parity for parity, exact in triple) % 2:
        return 'DECK'
    if trace_zero and any(exact for parity, exact in triple):
        return 'STOKES'
    return 'UNDETERMINED'


def coefficient_matrix(v, basis, offset):
    return sum((v[offset+j, 0]*b for j, b in enumerate(basis)), s.zeros(5))


def pair_matrix(a):
    return [[oldc.pair(x) for x in row] for row in a.tolist()]


def relative(E, ck, tag):
    n = E['n']; Z = d.ker(E['F'].col_join(E['R']))
    parallel = d.ker(E['D']); connecting = d.cols(p.mm(E['B'], parallel))
    combined = connecting.row_join(Z); piv = list(p.dm(combined).rref()[1])
    extra = combined[:, [j for j in piv if j >= connecting.cols]]
    ck(tag+'_full_relative_cycles', p.zero(p.mm(E['F'], Z)) and p.zero(p.mm(E['R'], Z))
       and p.rank(Z) == Z.cols)
    ck(tag+'_connecting_primitives_retained', p.zero(p.mm(E['D'], parallel))
       and p.zero(p.mm(E['F'], connecting)) and p.zero(p.mm(E['R'], connecting))
       and p.rank(connecting) == connecting.cols)
    ck(tag+'_absolute_direction_not_bulk_exact', p.rank(E['B'].row_join(extra)) == p.rank(E['B'])+extra.cols
       and p.rank(combined) == connecting.cols+extra.cols == Z.cols)
    rank2 = p.rank(E['G'].row_join(E['R2']))-p.rank(E['G'])
    ck(tag+'_degree_two_restriction_with_global_parallel_cokernel', rank2+E['absolute_H'][0] == E['boundary_H'][2]
       and rank2 <= E['absolute_H'][2])
    return {'relative_dimension': Z.cols, 'connecting_dimension': connecting.cols,
            'absolute_direction_dimension': extra.cols,
            'relative_space_sha256': oldc.plane_hash(Z),
            'connecting_space_sha256': oldc.plane_hash(connecting),
            'absolute_H': E['absolute_H'], 'boundary_H': E['boundary_H'],
            'degree_two_restriction_rank': rank2,
            'degree_two_interior_kernel': E['absolute_H'][2]-rank2}, extra


@lru_cache(None)
def run():
    _, data, w, P, Q, A, B = cy.literal(); facts = {}; neutral = {}; gauges = {}
    def ck(key, value):
        facts[key] = bool(value); assert facts[key], key
    basis = cy.adjoint_basis(); rn = {g: cy.adjoint_group(x, basis) for g, x in w.items()}
    T = s.Matrix([[s.trace(x*y) for y in basis] for x in basis]); odd_cocycle = None
    for sector, eta in (('plus', (1, 1, 1)), ('minus', ETA)):
        E = d.bulk({g: eta[j]*rn[g] for j, g in enumerate(p.GEN)}, data)
        row, extra = relative(E, ck, 'N_'+sector)
        R, H = E['restriction'], E['H']; b = E['boundary_H'][0]
        S = p.mm(E['J'], s.diag(T, T)); pair = p.mm(p.mm(R.T, S), H)
        piv = list(p.dm(pair).rref()[1]); U0 = p.mm(H[:, piv], cy.inv(pair[:, piv]))
        U = U0+p.mm(R, p.mm(p.mm(U0.T, S), U0))/2
        ck('N_'+sector+'_same_actual_trace_polarization', p.zero(p.mm(p.mm(R.T, S), R))
           and p.zero(p.mm(p.mm(U.T, S), U)) and p.mm(p.mm(R.T, S), U) == s.eye(b)
           and p.rank(R.row_join(U)) == 2*b)
        ck('N_'+sector+'_equal_plane_changes_trace_premise', p.rank(R.row_join(R)) < p.rank(R.row_join(U)))
        ck('N_'+sector+'_physical_degree_two_map_is_iso', R.cols+U.cols == p.rank(R.row_join(U))
           and row['relative_dimension'] == E['absolute_H'][2]
           and E['boundary_H'][2] == b)
        row.update(plane_sha256=oldc.plane_hash(U), restriction_rank=R.cols,
                   physical_H1=row['relative_dimension'], physical_H2=E['absolute_H'][2])
        neutral[sector] = row
        if sector == 'minus':
            ck('odd_absolute_is_one_actual_nonexact_class', extra.cols == 1)
            matrices = [coefficient_matrix(extra, basis, j*24) for j in range(3)]
            ck('odd_generator_values_are_actual_traceless_matrices', all(s.trace(x) == 0 for x in matrices)
               and any(not p.zero(x) for x in matrices))
            odd_cocycle = {g: pair_matrix(x) for g, x in zip(p.GEN, matrices)}
    ck('exact_neutral_even_and_odd_split_not_thirteen_exact', neutral['plus']['absolute_direction_dimension'] == 0
       and neutral['minus']['absolute_direction_dimension'] == 1
       and neutral['plus']['connecting_dimension'] == neutral['minus']['connecting_dimension'] == 6
       and sum(row['relative_dimension'] for row in neutral.values()) == 13)
    for sector, eta in (('plus', (1, 1, 1)), ('minus', ETA)):
        E = d.bulk({g: s.Matrix([[eta[j]]]) for j, g in enumerate(p.GEN)}, data)
        row, extra = relative(E, ck, 'g_'+sector)
        L = s.Matrix([0, 1]) if sector == 'plus' else s.Matrix([1, 1])
        if sector == 'plus':
            omega = s.Matrix([0, 0, 1])
            ck('g_plus_nonexact_longitude_not_connecting_or_gauge_deleted', p.zero(E['F']*omega)
               and E['R']*omega == s.Matrix([0, 1]) and p.rank(E['B'].row_join(omega)) > p.rank(E['B'])
               and p.rank(E['restriction'].row_join(L)) == 1)
        else:
            ck('g_minus_physical_class_connecting_and_zero_trace', row['relative_dimension'] == row['connecting_dimension'] == 1
               and row['absolute_direction_dimension'] == 0 and p.rank(E['restriction'].row_join(L)) == 2)
        row['physical_H1'] = 1
        row['nonexact_ordinary_direction_dimension'] = int(sector == 'plus')
        gauges[sector] = row
    # This is exact proof-case coverage using the ACTUALLY reconstructed
    # dimensions; it is not a numerical integral or a free exactness label.
    modes = [(0, True)]*neutral['plus']['connecting_dimension']
    modes += [(1, True)]*neutral['minus']['connecting_dimension']
    modes += [(1, False)]*neutral['minus']['absolute_direction_dimension']
    reasons = Counter(neutral_reason(triple) for triple in product(modes, repeat=3))
    ck('complete_neutral_cubic_proof_cases', sum(reasons.values()) == 13**3 and 'UNDETERMINED' not in reasons)
    ck('removing_deck_or_trace_does_not_prove_false_zero',
       neutral_reason(((1, False),)*3, deck=False) == 'UNDETERMINED'
       and neutral_reason(((0, True), (1, False), (1, False)), trace_zero=False) == 'UNDETERMINED')
    x, y, zz = s.zeros(5), s.zeros(5), s.zeros(5)
    x[0, 1] = y[1, 2] = zz[2, 0] = 1
    ck('same_neutral_Lie_density_has_nonzero_opposite', s.trace(x*(y*zz-zz*y)) == 1)
    ck('quadratic_flatness_premise_and_higher_hatch', neutral['plus']['degree_two_interior_kernel'] == 0
       and neutral['minus']['degree_two_interior_kernel'] == 1
       and neutral['plus']['degree_two_restriction_rank'] == 6)
    gr, sr = pt.bases(); roots = pt.roots(); zero4 = (0,)*4
    gauge_roots = [root for root in roots if pt.labels(root, sr) == zero4]
    structure_roots = [root for root in roots if pt.labels(root, gr) == zero4]
    ck('full_E8_gauge_structure_commute_and_are_trace_orthogonal', len(gauge_roots) == len(structure_roots) == 20
       and all(pt.dot(a, b) == 0 and pt.add(a, b) not in roots and a != pt.neg(b)
               for a in gauge_roots for b in structure_roots)
       and all(pt.dot(a, b) == 0 for a in gr for b in sr)
       and all(pt.dot(a, b) == 0 for a in gr for b in structure_roots)
       and all(pt.dot(a, b) == 0 for a in sr for b in gauge_roots))
    weights = {'Q': -1, 'u': 4, 'e': -6, 'd': -2, 'L': 3, 'N': 0, 'G': 0}
    mixed = [list(names) for names in combinations_with_replacement(sorted(weights), 3)
             if any(key in ('N', 'G') for key in names) and sum(weights[key] for key in names) == 0]
    ck('complete_neutral_mixed_charge_catalogue', mixed == [['G', 'G', 'G'], ['G', 'G', 'N'], ['G', 'N', 'N'], ['N', 'N', 'N']])
    expanded = {**weights, 'Qdual': -weights['Q']}
    extra_mixed = [names for names in combinations_with_replacement(sorted(expanded), 3)
                   if any(key in ('N', 'G') for key in names) and sum(expanded[key] for key in names) == 0]
    ck('false_conjugate_left_field_changes_catalogue', len(extra_mixed) > len(mixed)
       and tuple(sorted(('Q', 'Qdual', 'N'))) in extra_mixed)
    gauge_reasons = {''.join(map(str, parity)): ('DECK' if sum(parity) % 2 else 'ONE_FORM' if sum(parity) == 0 else 'STOKES')
                     for parity in product((0, 1), repeat=3)}
    return {'facts': facts, 'exact_predicates': len(facts), 'neutral': neutral, 'gauge': gauges,
            'odd_absolute_cocycle_matrices': odd_cocycle, 'neutral_proof_case_counts': dict(reasons),
            'gauge_proof_cases': gauge_reasons, 'mixed_charge_catalogue': mixed,
            'remaining_direct_cubic_zero_conditional': True, 'odd_absolute_mode_retained': True,
            'quadratic_flatness_obstruction_zero_conditional': True,
            'higher_odd_obstruction_computed': False, 'quadratic_response_computed': False,
            'real_moment_vacuum_derived': False, 'global_normalized_profiles_computed': False,
            'generated_selection': False, 'global_quantum_anomaly': False,
            'outside_review': False, 'full_goal_achieved': False}


if __name__ == '__main__':
    print(json.dumps(run(), indent=2, sort_keys=True))
