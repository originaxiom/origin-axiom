"""Separate Fraction crossed-homomorphism and LES ranks; no native import."""
import importlib.util
import json
from itertools import combinations
from pathlib import Path

HERE = Path(__file__).resolve().parent
OLD = HERE.parent
spec = importlib.util.spec_from_file_location('flag_fraction_seed',
    OLD/'silver_operator_gate_2026_10_05/reference.py')
b = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b)
K = b.K
mul, add, tr, inv, rank = b.mul, b.add, b.transpose, b.inverse, b.rank
hc, vc, z, eye = b.hcat, b.vcat, b.zeros, b.eye


def ker(a):
    reduced, pivots = b.elimination(a, True)
    free = [j for j in range(len(a[0])) if j not in pivots]
    out = z(len(a[0]), len(free))
    for k, j in enumerate(free):
        out[j][k] = 1
        for i, pivot in enumerate(pivots):
            out[pivot][k] = -reduced[i][j]
    return out


def diagonal(a, c):
    return vc(hc(a, z(len(a), len(c[0]))), hc(z(len(c), len(a[0])), c))


def model(rep, data, indices):
    core = b.Complex(rep, data)
    n, m = core.n, len(indices)
    select = [eye(n)[j] for j in indices]
    include = tr(select)
    p, q = [core.word(word)[0] for word in data['cusp_words']]
    pp, qq = [mul(mul(select, x), include) for x in (p, q)]
    assert all(mul(select, x) == mul(y, select) for x, y in ((p, pp), (q, qq)))
    dt = vc(add(pp, eye(m), -1), add(qq, eye(m), -1))
    gt = hc(add(eye(m), qq, -1), add(pp, eye(m), -1))
    r0, r1 = select, mul(diagonal(select, select), core.R)
    fox = core.word('abAB')[1]
    first = [row[:2*n] for row in fox]
    r2 = [[-x for x in row] for row in mul(mul(select, q),
          mul(first, diagonal(inv(rep['t']), inv(rep['t']))))]
    assert mul(r1, core.B) == mul(dt, r0)
    assert mul(r2, core.F) == mul(gt, r1)
    assert mul(gt, dt) == z(m)
    absolute = [n-rank(core.B), 3*n-rank(core.B)-rank(core.F), 2*n-rank(core.F), 0]
    bh = [m-rank(dt), 2*m-rank(dt)-rank(gt), m-rank(gt)]
    # Induced map ranks modulo exact boundary classes, not full-cone elimination.
    map_ranks = [rank(mul(r0, ker(core.B))),
                 rank(hc(dt, mul(r1, ker(core.F))))-rank(dt),
                 rank(hc(gt, r2))-rank(gt)]
    h = [absolute[0]-map_ranks[0],
         bh[0]-map_ranks[0]+absolute[1]-map_ranks[1],
         bh[1]-map_ranks[1]+absolute[2]-map_ranks[2],
         bh[2]-map_ranks[2]]
    dims = [n, 3*n+m, 2*n+2*m, m]
    cone_ranks = [dims[0]-h[0], 0, 0]
    cone_ranks[1] = dims[1]-cone_ranks[0]-h[1]
    cone_ranks[2] = dims[2]-cone_ranks[1]-h[2]
    assert dims[3]-cone_ranks[2] == h[3]
    return dict(H=h, J=h[1]+h[3]-h[0]-h[2], dimensions=dims,
                cone_ranks=cone_ranks, absolute_H=absolute,
                positive_boundary_H=bh, positive_rank=m,
                restriction_H_ranks=map_ranks)


def run():
    data = json.loads((OLD/'silver_operator_gate_2026_10_05/candidate.json').read_text())
    v = b.four(data)
    c = [K(x, y) for x, y in data['cocycle_Qsqrt2_pairs']]
    pairs = list(combinations(range(5), 2))
    w = [1, 1, 1, 1, -4]
    weights = {'W': w, 'F': [w[i]+w[j] for i, j in pairs]}
    checks, records = {}, {}
    def ck(name, value):
        assert name not in checks, name
        checks[name] = bool(value)
        assert checks[name], name
    for amplitude in (0, 1):
        wrep = b.extension(v, [amplitude*x for x in c])
        for label, rep in [('W', wrep), ('F', {g: b.exterior(x) for g, x in wrep.items()})]:
            for dual in (False, True):
                rr = b.dual(rep) if dual else rep
                ww = [-x for x in weights[label]] if dual else weights[label]
                for sign in (1, -1):
                    indices = [j for j, weight in enumerate(ww) if sign*weight > 0]
                    row = model(rr, data, indices)
                    row.update(positive_indices=indices, weights=ww)
                    key = f'{amplitude}:{label}{"dual" if dual else ""}:{sign}'
                    records[key] = row
                    ck(key+'_LES_nonnegative', min(row['H']) >= 0)
                    ck(key+'_zero_full_Euler_index', row['J'] == 0)
    for amplitude in (0, 1):
        for label in ('W', 'F'):
            for sign in (1, -1):
                ck(f'{amplitude}_{label}_{sign}_dual_all_degrees',
                   records[f'{amplitude}:{label}:{sign}']['H']
                   == records[f'{amplitude}:{label}dual:{sign}']['H'][::-1])
    ck('actual_wedge_rank_and_signs', len(pairs) == 10
       and weights['F'].count(2) == 6 and weights['F'].count(-3) == 4)
    ck('quadratic_field_nontrivial', K(1, 1)*K(-1, 1) == 1
       and K(0, 1)*K(0, 1) == 2 and K(0, 1) != K(1))
    return dict(checks=checks, passed=len(checks), records=records,
                scope='same supplied coefficient; independent exact LES ranks, not PDE certification',
                physical_goal_achieved=False)


if __name__ == '__main__':
    print(json.dumps(run(), indent=2, sort_keys=True))
