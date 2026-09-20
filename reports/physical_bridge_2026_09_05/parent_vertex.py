"""R38: exact H-to-E8 weights and local classical-parent tensor tests.

This is not object selection of E8, a source action, global mode matching,
a quantum no-go, or physical chirality. See the pre-execution design.
"""
from __future__ import annotations

from collections import Counter
from functools import lru_cache
import importlib.util
import itertools
import json
from pathlib import Path
import time

import sympy as sp

SPEC = importlib.util.spec_from_file_location(
    'r38_interaction_prior', Path(__file__).with_name('mirror_interaction.py'))
mi = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(mi)
ac = mi.ac
HALF = sp.Rational(1, 2)
EPS = sp.Matrix([[0, 1], [-1, 0]])


def tup(v):
    return tuple(v)


def e8_direct():
    roots = set()
    for i, j in itertools.combinations(range(8), 2):
        for a, b in itertools.product((-1, 1), repeat=2):
            r = [sp.Integer(0)]*8
            r[i], r[j] = sp.Integer(a), sp.Integer(b)
            roots.add(tuple(r))
    for signs in itertools.product((-1, 1), repeat=8):
        if signs.count(-1) % 2 == 0:
            roots.add(tuple(HALF*s for s in signs))
    return tuple(sorted(roots))


def e8_basis():
    ee = sp.eye(8)
    roots = [sp.Matrix([1, -1, -1, -1, -1, -1, -1, 1])/2,
             ee[:, 0]+ee[:, 1]]
    roots += [-ee[:, j]+ee[:, j+1] for j in range(6)]
    return sp.Matrix.hstack(*roots)


def reflection_closure(basis):
    simple = [tup(basis[:, j]) for j in range(basis.cols)]
    seen, todo = set(simple), list(simple)
    while todo:
        r = todo.pop()
        for a in simple:
            pairing = sum(x*y for x, y in zip(r, a))
            s = tuple(x-pairing*y for x, y in zip(r, a))
            if s not in seen:
                seen.add(s)
                todo.append(s)
    return seen


@lru_cache(maxsize=1)
def root_data():
    d = ac.data()
    C, Ci, u = (d[k] for k in ('C', 'Ci', 'u'))
    B = sp.Matrix([[0, 0, 0, 1, 1], [0, 0, 0, 1, -1],
                   [0, 0, 1, -1, 0], [0, 1, -1, 0, 0],
                   [1, -1, 0, 0, 0]])
    p = sp.eye(6)-sp.Rational(3, 4)*u*sp.eye(6)[0, :]
    U = sp.Matrix([0, 0, 0, 0, 0, -2, 2, 2])
    T0 = (B.T*p[1:, :]).col_join(sp.zeros(3, 6))
    central = sp.Rational(3, 4)*U*sp.eye(6)[0, :]
    T = T0+central
    A = e8_basis()
    K = A.inv()*T*Ci
    roots = e8_direct()
    pulled = {r: Ci*T.T*sp.Matrix(r) for r in roots}
    f1 = sp.Matrix([0, 0, 0, 0, 0, 1, 1, 0])
    f2 = sp.Matrix([0, 0, 0, 0, 0, 0, -1, 1])
    family = {r: (sp.Matrix(r).dot(f1), sp.Matrix(r).dot(f2))
              for r in roots}
    return dict(C=C, Ci=Ci, u=u, B=B, U=U, T=T, A=A, K=K,
                small_K=A.inv()*(T0+central/3)*Ci, roots=roots,
                pulled=pulled, family=family, f1=f1, f2=f2)


@lru_cache(maxsize=1)
def embedding_controls():
    d, old = root_data(), ac.data()
    A, K, C, Ci, T, U = (d[k] for k in ('A', 'K', 'C', 'Ci', 'T', 'U'))
    roots = set(d['roots'])
    full = Counter(tup(w) for w in d['pulled'].values())
    full[(0,)*6] += 8
    d5 = [w for w in old['roots'] if w[0] == 0]
    expected = Counter(tup(w) for w in d5)
    expected[(0,)*6] += 14  # eight Cartans and six A2 roots
    for w in old['spinor']:
        expected[tup(w-3*d['u'])] += 1
        expected[tup(-w+3*d['u'])] += 1
    for w in old['pullback']:
        expected[tup(w)] += 3
        expected[tup(-w)] += 3
    charge_dims = Counter()
    for w, multiplicity in full.items():
        charge_dims[w[0]] += multiplicity
    minors = [K.extract(rows, range(6)).det()
              for rows in itertools.combinations(range(8), 6)]
    actual_spin = {tup(w) for w in d['pulled'].values() if w[0] == 1}
    actual_vector = {tup(w) for w in d['pulled'].values() if w[0] == 2}
    actual_Q = {tup(w) for w in d['pulled'].values() if w[0] == 4}
    euclidean_spin = {tup(d['B'].inv()*(C*w)[1:, :]) for w in old['spinor']}
    q1_euclidean = {r[:5] for r, w in d['pulled'].items() if w[0] == 1}
    wrong_spin = {r[:4]+(-r[4],) for r in q1_euclidean}
    omitted_root = T[:, 0]
    return dict(e8_root_count=len(roots), e8_basis=A, e8_gram=A.T*A,
                e8_basis_det=A.det(), e8_gram_det=(A.T*A).det(),
                roots_norm_two=all(sum(x*x for x in r) == 2 for r in roots),
                reflection_complete=reflection_closure(A) == roots,
                e8_roots_integral=all(ac.integral(A.inv()*sp.Matrix(r)) for r in roots),
                H_map=T, cocharacter_map=K, cocharacter_rank=K.rank(),
                cocharacter_integral=ac.integral(K), maximal_minors=minors,
                saturation_index=sp.igcd(*minors), central_direction=T*d['u'],
                d5_gram=d['B']*d['B'].T,
                d5_metric_correct=d['B']*d['B'].T == C[1:, 1:],
                d5_roots_preserved=all(tup(T*w) in roots for w in d5),
                all_restricted_weights_integral=all(ac.integral(w) for w in d['pulled'].values()),
                total_dimension=sum(full.values()), charge_dimensions=dict(sorted(charge_dims.items())),
                full_weight_multiset_matches=full == expected,
                same_actual_spinor=actual_spin == ac.tuples(old['spinor']),
                same_actual_vector=actual_vector == ac.tuples(-w for w in old['vector']),
                same_actual_Q=actual_Q == ac.tuples(old['singlet']),
                same_euclidean_spinor=q1_euclidean == euclidean_spin,
                wrong_spinor_same_dimension=len(wrong_spin) == len(euclidean_spin),
                wrong_spinor_different=wrong_spin != euclidean_spin,
                original_adjoint_charge_dims=dict(sorted(Counter(w[0] for w in old['roots']+[sp.zeros(6, 1)]*6).items())),
                old_simple_image=omitted_root, old_simple_image_norm=omitted_root.dot(omitted_root),
                old_simple_image_not_root=tup(omitted_root) not in roots,
                central_division_mutant_integral=ac.integral(d['small_K']),
                central_division_mutant=d['small_K'])


def tensor_action(generators, degree):
    n = generators[0].rows
    actions = []
    for g in generators:
        action = sp.zeros(n**degree)
        for slot in range(degree):
            factors = [sp.eye(n)]*degree
            factors[slot] = g
            action += sp.kronecker_product(*factors)
        actions.append(action)
    return sp.Matrix.vstack(*actions)


@lru_cache(maxsize=1)
def family_controls():
    d = root_data()
    triplet = {(1, 0), (-1, 1), (0, -1)}
    blocks = {f: {tup(d['pulled'][r]) for r in d['roots'] if d['family'][r] == f}
              for f in sorted(triplet)}
    fam = sorted(r for r in d['roots'] if d['family'][r] in triplet)
    famset = set(fam)
    triples = []
    for i, r in enumerate(fam):
        for s in fam[i+1:]:
            t = tuple(-a-b for a, b in zip(r, s))
            if t in famset and t > s:
                triples.append((r, s, t))
    internal = Counter(tuple(sorted(tup(d['pulled'][r]) for r in tri)) for tri in triples)
    gens = []
    for i, j in ((0, 1), (1, 2), (1, 0), (2, 1)):
        g = sp.zeros(3)
        g[i, j] = 1
        gens.append(g)
    action = tensor_action(gens, 3)
    epsilon = sp.Matrix([sp.LeviCivita(i, j, k)
                         for i, j, k in itertools.product(range(3), repeat=3)])
    r1 = sp.Matrix([-1, 1, 1, 1, 1, 1, 1, -1])/2
    r2 = sp.Matrix([-1, -1, -1, -1, -1, 1, -1, 1])/2
    scalar = -r1-r2
    witness = [r1, r2, scalar]
    return dict(family_blocks={str(f): len(b) for f, b in blocks.items()},
                each_full_H_27=all(b == ac.tuples(ac.data()['pullback']) for b in blocks.values()),
                family_roots=len(fam), zero_sum_triples=len(triples),
                all_distinct_families=all(len({d['family'][r] for r in tri}) == 3 for tri in triples),
                internal_triples=len(internal), family_assignment_multiplicities=sorted(set(internal.values())),
                family_invariant_dimension=len(action.nullspace()),
                epsilon_invariant=action*epsilon == sp.zeros(action.rows, 1),
                family_zero_roots=sum(f == (0, 0) for f in d['family'].values()),
                charged_root_witness=witness,
                witness_all_roots=all(tup(r) in d['pulled'] for r in witness),
                witness_charges=[r.dot(d['U']) for r in witness],
                witness_nonzero_bracket_root=tup(r1+r2) in d['pulled'],
                witness_actual_fields=(all(tup(d['Ci']*d['T'].T*r) in ac.tuples(-w for w in ac.data()['spinor']) for r in (r1, r2))
                                       and tup(d['Ci']*d['T'].T*scalar) in ac.tuples(-w for w in ac.data()['vector'])))


@lru_cache(maxsize=1)
def internal_controls():
    gens = []
    for i, j in itertools.combinations(range(3), 2):
        g = sp.zeros(3)
        g[i, j], g[j, i] = 1, -1
        gens.append(g)
    acts = {k: tensor_action(gens, k) for k in (1, 2, 3)}
    delta = sp.Matrix([int(i == j) for i, j in itertools.product(range(3), repeat=2)])
    epsilon = sp.Matrix([sp.LeviCivita(i, j, k)
                         for i, j, k in itertools.product(range(3), repeat=3)])
    fixed_vector = sp.Matrix([0, 0, 1])
    return dict(invariant_dimensions={str(k): len(a.nullspace()) for k, a in acts.items()},
                delta_invariant=acts[2]*delta == sp.zeros(acts[2].rows, 1),
                epsilon_invariant=acts[3]*epsilon == sp.zeros(acts[3].rows, 1),
                fixed_vector_not_invariant=acts[1]*fixed_vector != sp.zeros(acts[1].rows, 1),
                delta_not_alternating=delta[0] != 0,
                epsilon_not_symmetric=epsilon[5] == -epsilon[7] != 0)


def grassmann_coefficients(matrix):
    if matrix.rows != matrix.cols:
        raise ValueError('square quadratic coefficient matrix required')
    return {(i, j): sp.expand(matrix[i, j]-matrix[j, i])
            for i in range(matrix.rows) for j in range(i+1, matrix.cols)
            if sp.expand(matrix[i, j]-matrix[j, i]) != 0}


@lru_cache(maxsize=1)
def statistics_controls():
    color = EPS
    zero_raw = sp.kronecker_product(color, EPS)
    internal = sp.Matrix(3, 3, lambda i, j: sp.LeviCivita(i, j, 2))
    one_raw = sp.kronecker_product(color, internal, EPS)
    cross = sp.kronecker_product(color, EPS)
    mixed_raw = sp.BlockMatrix([[sp.zeros(4), cross], [sp.zeros(4), sp.zeros(4)]]).as_explicit()
    family = sp.Matrix(3, 3, lambda i, j: sum(sp.LeviCivita(i, j, k)*(k+1) for k in range(3)))
    yy = mi.clifford_data()['sectors'][-1]['yukawa']
    eft_counts, parent_counts = [], []
    for Y in yy:
        eft_counts.append(len(grassmann_coefficients(sp.kronecker_product(Y, EPS))))
        parent_counts.append(len(grassmann_coefficients(sp.kronecker_product(family, Y, EPS))))
    return dict(color_antisymmetric=color.T == -color,
                zero_form_matrix_symmetric=zero_raw.T == zero_raw,
                zero_form_coefficients=len(grassmann_coefficients(zero_raw)),
                one_form_matrix_antisymmetric=one_raw.T == -one_raw,
                one_form_coefficients=len(grassmann_coefficients(one_raw)),
                mixed_species_coefficients=len(grassmann_coefficients(mixed_raw)),
                family_matrix_antisymmetric=family.T == -family,
                all_ten_Y_symmetric=all(Y.T == Y for Y in yy),
                added_EFT_coefficients=eft_counts,
                parent_family_zero_form_coefficients=parent_counts)


def contraction_controls():
    dx, dy, dz = (sp.eye(3)[:, j] for j in range(3))
    return dict(equal_dot=dx.dot(dx), equal_wedge=sp.Matrix.hstack(dx, dz, dx).det(),
                orthogonal_dot=dx.dot(dy), orthogonal_wedge=sp.Matrix.hstack(dx, dz, dy).det())


def report():
    e, f, i, s, c = embedding_controls(), family_controls(), internal_controls(), statistics_controls(), contraction_controls()
    checks = dict(
        complete_e8_lattice=(e['e8_root_count'] == 240 and e['e8_gram_det'] == 1 and abs(e['e8_basis_det']) == 1
                            and e['roots_norm_two'] and e['reflection_complete'] and e['e8_roots_integral']),
        faithful_H_map=(e['cocharacter_integral'] and e['cocharacter_rank'] == 6 and e['saturation_index'] == 1
                        and e['central_direction'] == root_data()['U'] and e['d5_metric_correct'] and e['d5_roots_preserved']),
        complete_weight_roster=(e['total_dimension'] == 248 and e['full_weight_multiset_matches'] and e['all_restricted_weights_integral']
                                and e['charge_dimensions'] == {-4: 3, -3: 16, -2: 30, -1: 48, 0: 54, 1: 48, 2: 30, 3: 16, 4: 3}),
        actual_fields=(e['same_actual_spinor'] and e['same_actual_vector'] and e['same_actual_Q'] and e['same_euclidean_spinor']),
        original_parent_scope=(e['original_adjoint_charge_dims'] == {-1: 16, 0: 46, 1: 16}
                               and e['old_simple_image_norm'] == 8 and e['old_simple_image_not_root']),
        map_mutants_discriminate=(not e['central_division_mutant_integral'] and e['wrong_spinor_same_dimension'] and e['wrong_spinor_different']),
        family_recovery=(f['each_full_H_27'] and f['family_roots'] == 81 and f['family_zero_roots'] == 72
                         and f['zero_sum_triples'] == 270 and f['internal_triples'] == 45 and f['family_assignment_multiplicities'] == [6]
                         and f['all_distinct_families'] and f['family_invariant_dimension'] == 1 and f['epsilon_invariant']),
        nonzero_root_channel=(f['witness_all_roots'] and f['witness_nonzero_bracket_root'] and f['witness_actual_fields'] and f['witness_charges'] == [-1, -1, 2]),
        internal_tensor_census=(i['invariant_dimensions'] == {'1': 0, '2': 1, '3': 1} and i['delta_invariant'] and i['epsilon_invariant']
                                and i['fixed_vector_not_invariant'] and i['delta_not_alternating'] and i['epsilon_not_symmetric']),
        zero_form_statistics=(s['color_antisymmetric'] and s['zero_form_matrix_symmetric'] and s['zero_form_coefficients'] == 0
                              and s['parent_family_zero_form_coefficients'] == [0]*10),
        positive_parent_vertices=(s['one_form_matrix_antisymmetric'] and s['one_form_coefficients'] > 0 and s['mixed_species_coefficients'] > 0),
        added_EFT_not_retracted=(s['all_ten_Y_symmetric'] and all(n > 0 for n in s['added_EFT_coefficients'])),
        overlap_operations_distinct=(c['equal_dot'] == 1 and c['equal_wedge'] == 0 and c['orthogonal_dot'] == 0 and c['orthogonal_wedge'] == -1))
    return dict(embedding=e, family=f, internal=i, statistics=s, contractions=c,
                checks=checks, all_checks_pass=all(checks.values()),
                scope='Exact candidate compact H embedding and classical local tensors; no parent/source selection, global matching, quantum gap or TOE.')


if __name__ == '__main__':
    started = time.monotonic()
    result = report()
    result['elapsed_seconds'] = time.monotonic()-started
    print(json.dumps(ac.serial(result), indent=2))
    raise SystemExit(0 if result['all_checks_pass'] else 1)
