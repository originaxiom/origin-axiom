"""R40 exact coefficient-to-parent test. Run with sage -python.

Interior restriction cohomology is reported as such, never as a physical
L2 spectrum. Existing R27/R38 producers are reused and credited.
"""
from collections import Counter
import importlib.util
from itertools import combinations, product
import json
from pathlib import Path

from sage.all import (QQ, CyclotomicField, PolynomialRing, matrix, vector,
                      identity_matrix, zero_matrix, block_diagonal_matrix)
from sage.env import SAGE_VERSION


def prior(name, filename):
    spec = importlib.util.spec_from_file_location(name, Path(__file__).with_name(filename))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


r27 = prior('r40_r27_reuse', 'finite_twist_reductivity.py')
r38 = prior('r40_r38_reuse', 'parent_vertex.py')


def wedge2(a):
    pairs = list(combinations(range(a.nrows()), 2))
    return matrix(a.base_ring(), [[a[k, i]*a[l, j]-a[k, j]*a[l, i]
                                 for i, j in pairs] for k, l in pairs])


def wedge_lie(a):
    n, ring = a.nrows(), a.base_ring()
    pairs = list(combinations(range(n), 2))
    result = zero_matrix(ring, len(pairs))
    for col, (i, j) in enumerate(pairs):
        for k in range(n):
            if k != j:
                result[pairs.index(tuple(sorted((k, j)))), col] += (1 if k < j else -1)*a[k, i]
            if k != i:
                result[pairs.index(tuple(sorted((i, k)))), col] += (1 if i < k else -1)*a[k, j]
    return result


def end0(rho):
    first = next(iter(rho.values()))
    ring, n = first.base_ring(), first.nrows()
    off = [(i, j) for i in range(n) for j in range(n) if i != j]
    basis = []
    for i, j in off:
        x = zero_matrix(ring, n)
        x[i, j] = 1
        basis.append(x)
    for i in range(n-1):
        x = zero_matrix(ring, n)
        x[i, i], x[n-1, n-1] = 1, -1
        basis.append(x)
    result = {}
    for g, a in rho.items():
        cols = []
        ai = a.inverse()
        for x in basis:
            y = a*x*ai
            coords = [y[i, j] for i, j in off]+[y[i, i] for i in range(n-1)]
            rebuilt = sum((v*b for v, b in zip(coords, basis)), zero_matrix(ring, n))
            assert y.trace() == 0 and rebuilt == y
            cols.append(coords)
        result[g] = matrix(ring, cols).transpose()
    return result


def setup():
    k = CyclotomicField(12)
    z = k.gen()
    u, imaginary = z**2, z**3
    rho = {'a': matrix(k, [[0, 1], [-1, 1]]),
           'b': matrix(k, [[0, u**2], [u, -2]])}
    chi = {'a': u, 'b': -k.one()}
    p = matrix(k, [[1, 0], [u, 1]])
    tri = {g: p.inverse()*a*p for g, a in rho.items()}
    assert tri['a'] == matrix(k, [[u, 1], [0, 1-u]])
    assert tri['b'] == matrix(k, [[-1, u**2], [0, -1]])
    v = {g: chi[g]*r27.sy(a, 3) for g, a in rho.items()}
    line = {g: matrix(k, [[a.det()**-1]]) for g, a in v.items()}
    w = {g: block_diagonal_matrix(v[g], line[g]) for g in r27.GENS}
    return dict(k=k, u=u, imaginary=imaginary, rho=rho, chi=chi, p=p,
                V=v, L=line, W=w)


def compact_pair(rho):
    data = r27.paired(rho)
    assert all(data['identities'].values())
    keys = ('a0', 'a1', 'a2', 't0', 't1', 'r1', 'n')
    out = {'index': data['index'], 'dimension': next(iter(rho.values())).nrows(),
           'identities': data['identities']}
    for label in ('V', 'dual'):
        assert all(data[label]['checks'].values())
        out[label] = {key: data[label][key] for key in keys}
        out[label]['checks'] = data[label]['checks']
    return out


def coefficient_map(d):
    k, v, line, w = (d[key] for key in ('k', 'V', 'L', 'W'))
    p3 = r27.sy(d['p'], 3)
    vt = {g: p3.inverse()*a*p3 for g, a in v.items()}
    complement = r27.complement_to_first_line(vt)
    wrong = {g: block_diagonal_matrix(v[g], matrix(k, [[v[g].det()]])) for g in r27.GENS}
    return dict(V=v, W=w, detV={g: a.det() for g, a in v.items()},
                detW={g: a.det() for g, a in w.items()},
                det_character=all(v[g].det() == d['chi'][g]**4 for g in r27.GENS),
                line_is_chi2=all(line[g][0, 0] == d['chi'][g]**2 for g in r27.GENS),
                nontrivial_det=v['a'].det() != 1,
                exact_original_block=all(w[g][:4, :4] == v[g] for g in r27.GENS),
                wrong_line_fails=wrong['a'].det() != 1,
                relator=all(r27.ev(word, w) == identity_matrix(k, 5) for word in r27.RELS),
                peripheral_blocks=all(r27.ev(word, w) == block_diagonal_matrix(
                    r27.ev(word, v), r27.ev(word, line)) for word in r27.PERIPH),
                retained_nonsplit=not complement['invariant_complement'],
                complement_ranks=[complement['equation_rank'], complement['augmented_rank']])


def scalar_repairs(d):
    rows = []
    k = d['k']
    for aa, bb in product((k.one(), -k.one()), (k.one(), d['imaginary'], -k.one(), -d['imaginary'])):
        delta = {'a': aa, 'b': bb}
        rho = {g: delta[g]*r27.sy(a, 3) for g, a in d['rho'].items()}
        row = compact_pair(rho)
        row.update(delta=delta, cusp_character=[aa**-3*bb, bb**2],
                   determinants=[a.det() for a in rho.values()])
        rows.append(row)
    return rows


def cg_control(d):
    k = d['k']
    e, f = zero_matrix(k, 4), zero_matrix(k, 4)
    for j in range(3):
        e[j, j+1], f[j+1, j] = j+1, 3-j
    ee, ff = wedge_lie(e), wedge_lie(f)
    highest = vector(k, [1, 0, 0, 0, 0, 0])
    columns, denom, current = [], k.one(), highest
    for j in range(5):
        columns.append(current/denom)
        current = ff*current
        denom *= 4-j
    singlets = ee.stack(ff).right_kernel()
    assert singlets.dimension() == 1
    columns.append(singlets.basis()[0])
    intertwiner = matrix(k, columns).transpose()
    checks = {}
    for g, a in d['rho'].items():
        left = wedge2(r27.sy(a, 3))
        right = block_diagonal_matrix(r27.sy(a, 4), identity_matrix(k, 1))
        checks[g] = left*intertwiner == intertwiner*right
    return dict(intertwiner=intertwiner, determinant=intertwiner.det(),
                singlet_dimension=singlets.dimension(), actual_generator_equations=checks)


def weights():
    roots = [vector(QQ, [QQ(str(x)) for x in r]) for r in r38.e8_direct()]
    e = list(identity_matrix(QQ, 8).rows())
    gauge = [e[j]-e[j+1] for j in range(4)]
    structure = [e[6]-e[7], e[5]-e[6], e[6]+e[7], -sum(e)/2]
    a4 = matrix(QQ, [[2 if i == j else -1 if abs(i-j) == 1 else 0 for j in range(4)] for i in range(4)])
    all_simple = matrix(QQ, gauge+structure).transpose()
    eb = matrix(QQ, [[QQ(str(r38.e8_basis()[i, j])) for j in range(8)] for i in range(8)])
    lattice = eb.inverse()*all_simple
    f = [tuple(int(j == i)-int(j == i+1) for i in range(4)) for j in range(5)]
    neg = lambda w: tuple(-x for x in w)
    add = lambda x, y: tuple(a+b for a, b in zip(x, y))
    ten = [add(f[i], f[j]) for i, j in combinations(range(5), 2)]
    adj = [add(f[i], neg(f[j])) for i in range(5) for j in range(5) if i != j]+[(0,)*4]*4
    reps = {'1': [(0,)*4], '5': f, 'bar5': [neg(x) for x in f],
            '10': ten, 'bar10': [neg(x) for x in ten], '24': adj}
    actual = Counter(tuple(r.dot_product(a) for a in gauge+structure) for r in roots)
    actual[(0,)*8] += 8
    branches = [('24', '1'), ('1', '24'), ('10', '5'), ('bar10', 'bar5'), ('5', 'bar10'), ('bar5', '10')]
    def branch_counter(roster):
        return Counter(x+y for first, second in roster for x in reps[first] for y in reps[second])
    expected = branch_counter(branches)
    wrong = branch_counter(branches[:4]+[('5', '10'), ('bar5', 'bar10')])
    center_charge = lambda w: sum((j+1)*w[j] for j in range(4))
    kernel = [(a, b) for a, b in product(range(5), repeat=2)
              if all((a*center_charge(w[:4])+b*center_charge(w[4:])) % 5 == 0 for w in actual)]
    poly = PolynomialRing(QQ, names=('q0', 'q1', 'q2', 'q3'))
    q = poly.gens()
    tr5 = sum(sum(x*y for x, y in zip(w, q))**2 for w in f)
    tr248 = sum(mult*sum(x*y for x, y in zip(w[4:], q))**2 for w, mult in actual.items())
    return dict(root_count=len(roots), total=sum(actual.values()),
                cartan_gauge=matrix(QQ, gauge)*matrix(QQ, gauge).transpose(),
                cartan_structure=matrix(QQ, structure)*matrix(QQ, structure).transpose(),
                correct_cartans=matrix(QQ, gauge)*matrix(QQ, gauge).transpose() == a4 and
                    matrix(QQ, structure)*matrix(QQ, structure).transpose() == a4,
                orthogonal=(matrix(QQ, gauge)*matrix(QQ, structure).transpose()).is_zero(),
                actual_simple_roots=all(x in roots for x in gauge+structure),
                lattice_integral=all(x.denominator() == 1 for x in lattice.list()),
                lattice_index=abs(lattice.det()), euclidean_index=abs(all_simple.det()),
                branches=branches, all_joint_weights=actual == expected,
                wrong_bars_rejected=actual != wrong, wrong_bars_dimension=sum(wrong.values()),
                center_kernel=kernel, kernel_expected=kernel == [(j, (-2*j) % 5) for j in range(5)],
                separate_factor_injective=all((a == 0) == (b == 0) for a, b in kernel),
                defining_trace=tr5, adjoint_trace=tr248, trace_factor_60=tr248 == 60*tr5)


def sector_systems(d):
    k, v, line, w = (d[key] for key in ('k', 'V', 'L', 'W'))
    return {'trivial': {g: identity_matrix(k, 1) for g in r27.GENS},
            'V': v, 'L': line, 'W': w,
            'wedgeV': {g: wedge2(a) for g, a in v.items()},
            'VL': {g: line[g][0, 0]*a for g, a in v.items()},
            'wedgeW': {g: wedge2(a) for g, a in w.items()},
            'VLinv': {g: line[g][0, 0]**-1*a for g, a in v.items()},
            'End0V': end0(v), 'End0W': end0(w),
            'chi2Sym4': {g: d['chi'][g]**2*r27.sy(a, 4) for g, a in d['rho'].items()}}


def sums_match(sectors, target, pieces):
    for side in ('V', 'dual'):
        for key in ('a0', 'a1', 'a2', 't0', 't1', 'r1', 'n'):
            if sectors[target][side][key] != sum(sectors[name][which][key] for name, which in pieces[side]):
                return False
    return True


def diagnostic(sectors):
    poly = PolynomialRing(QQ, names=('h0', 'h1', 'h2', 'h3'))
    h = list(poly.gens())
    h.append(-sum(h))
    ten = [h[i]+h[j] for i, j in combinations(range(5), 2)]
    c5, c10 = sum(x**3 for x in h), sum(x**3 for x in ten)
    t5, t10 = sum(x*x for x in h), sum(x*x for x in ten)
    idx = {name: a['index'] for name, a in sectors.items()}
    iv, il, ie, ivl, ising = (idx[key] for key in ('V', 'L', 'wedgeV', 'VL', 'VLinv'))
    return dict(conditional_dictionary='interior indices as left-Weyl multiplicities; NOT a physical spectrum',
                quadratic_identity=t10 == 3*t5, cubic_identity=c10 == c5,
                conjugate_cubic_sign=sum((-x)**3 for x in h) == -c5,
                anomaly_free_control=c10-c5 == 0,
                anomalous_control=c10+c5 != 0,
                indices=idx, SU5_cubic=idx['W']-idx['wedgeW'],
                SU5_squared_U1=3*(iv-4*il)+2*ie-3*ivl,
                gravity_squared_U1=10*(iv-4*il)+5*(2*ie-3*ivl)+5*ising,
                U1_cubic=10*(iv-64*il)+5*(8*ie-27*ivl)+125*ising)


def metric_control():
    poly = PolynomialRing(QQ, names=('h0', 'h1', 'h2', 'h3', 'x0', 'x1', 'x2', 'x3'))
    frac = poly.fraction_field()
    h, x = list(poly.gens())[:4], list(poly.gens())[4:]
    det4 = h[0]*h[1]*h[2]*h[3]
    det5 = det4/frac(det4)
    trace4 = sum(a*a for a in x)
    trace5 = trace4+sum(x)**2
    a = matrix(QQ, [[2, 1, 0, 0], [1, 3, 0, 0], [0, 0, 4, 1], [0, 0, 1, 2]])
    b = matrix(QQ, [[1, 2, 0, 0], [0, 1, 0, 0], [0, 0, 1, 1], [0, 0, 0, 1]])
    j = lambda z: block_diagonal_matrix(z, matrix(QQ, [[1/z.det()]]))
    tangent = lambda z: block_diagonal_matrix(z, matrix(QQ, [[-z.trace()]]))
    h5 = j(a)
    transformed = b.transpose()*a*b
    return dict(det_metric=det5, norm_difference=trace5-trace4,
                positive_principal_minors=[h5[:i, :i].det() for i in range(1, 6)],
                metric_equivariance=j(transformed) == j(b).transpose()*h5*j(b),
                group_homomorphism=j(a*b) == j(a)*j(b),
                bracket_map=tangent(a*b-b*a) == tangent(a)*tangent(b)-tangent(b)*tangent(a),
                dagger_map=tangent(b.transpose()) == tangent(b).transpose(),
                current_trace_zero=tangent(a).trace() == 0,
                identity_source_image=tangent(identity_matrix(QQ, 4)))


def emit(part, result):
    print(json.dumps({'part': part, 'result': r27.serial(result)}), flush=True)


def run():
    emit('environment', {'sage': SAGE_VERSION, 'field': 'Q(zeta_12)',
                         'interpretation': 'algebraic interior cohomology, not physical L2 modes'})
    d = setup()
    cm = coefficient_map(d)
    emit('coefficient_map', cm)
    assert all(cm[key] for key in ('det_character', 'line_is_chi2', 'nontrivial_det',
        'exact_original_block', 'wrong_line_fails', 'relator', 'peripheral_blocks', 'retained_nonsplit'))
    assert all(v == 1 for v in cm['detW'].values())
    cg = cg_control(d)
    emit('clebsch_gordan', cg)
    assert cg['determinant'] != 0 and all(cg['actual_generator_equations'].values())
    wd = weights()
    emit('whole_parent', wd)
    assert all(wd[key] for key in ('correct_cartans', 'orthogonal', 'actual_simple_roots',
        'lattice_integral', 'all_joint_weights', 'wrong_bars_rejected', 'kernel_expected',
        'separate_factor_injective', 'trace_factor_60'))
    assert wd['root_count'] == 240 and wd['total'] == 248 and wd['lattice_index'] == wd['euclidean_index'] == 5
    repairs = scalar_repairs(d)
    emit('scalar_repairs', repairs)
    assert len(repairs) == 8 and all(row['index'] == 0 for row in repairs)
    sectors = {}
    for name, rho in sector_systems(d).items():
        sectors[name] = compact_pair(rho)
        emit('sector_'+name, sectors[name])
    normal_pieces = lambda names: {side: [(name, side) for name in names] for side in ('V', 'dual')}
    end_pieces = {side: [('End0V', side), ('trivial', side), ('VLinv', 'V'), ('VLinv', 'dual')]
                  for side in ('V', 'dual')}
    sums = dict(W=sums_match(sectors, 'W', normal_pieces(['V', 'L'])),
                wedgeW=sums_match(sectors, 'wedgeW', normal_pieces(['wedgeV', 'VL'])),
                wedgeV=sums_match(sectors, 'wedgeV', normal_pieces(['chi2Sym4', 'L'])),
                End0W=sums_match(sectors, 'End0W', end_pieces))
    emit('direct_sum_checks', sums)
    assert all(sums.values())
    assert sectors['V']['index'] == 1 and sectors['L']['index'] == 0 and sectors['W']['index'] == 1
    assert sectors['VL']['index'] == 0 and sectors['VLinv']['index'] == -1
    anomalies = diagnostic(sectors)
    emit('conditional_anomalies', anomalies)
    assert all(anomalies[key] for key in ('quadratic_identity', 'cubic_identity',
        'conjugate_cubic_sign', 'anomaly_free_control', 'anomalous_control'))
    metric = metric_control()
    emit('metric_and_current', metric)
    assert metric['det_metric'] == 1 and all(v > 0 for v in metric['positive_principal_minors'])
    assert all(metric[key] for key in ('metric_equivariance', 'group_homomorphism',
        'bracket_map', 'dagger_map', 'current_trace_zero'))
    emit('conclusion', {'algebraic_map_checked': True, 'physical_spectrum_claimed': False,
                        'source_action_derived': False, 'goal_complete': False})


if __name__ == '__main__':
    run()
