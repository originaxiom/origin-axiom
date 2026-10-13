"""Exact charged full-cone computation, not a machine-certified PDE proof."""
import importlib.util
import json
from functools import lru_cache
from itertools import combinations
from pathlib import Path
import sympy as s

HERE = Path(__file__).resolve().parent
OLD = HERE.parent


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


alg = load('flag_exact_algebra', OLD/'silver_spectral_completion_2026_10_05/probe.py')
seed = load('flag_exact_seed', OLD/'silver_operator_gate_2026_10_05/probe.py')
mm, inv, rank, zero = alg.mul, alg.inv, alg.rank, alg.zero


class Cell:
    def __init__(self, rep, data):
        self.n = n = rep['a'].rows
        self.rep = rep
        self.letters = {**rep, **{g.upper(): inv(x) for g, x in rep.items()}}
        assert all(self.word(w) == s.eye(n) for w in data['relators'])
        self.P, self.Q = [self.word(w) for w in data['cusp_words']]
        assert zero(mm(self.P, self.Q)-mm(self.Q, self.P))
        self.B = s.Matrix.vstack(*(rep[g]-s.eye(n) for g in 'abt'))
        self.F = s.Matrix.vstack(*(self.fox(w) for w in data['relators']))
        self.R = s.Matrix.vstack(*(self.fox(w) for w in data['cusp_words']))
        self.R2 = -mm(mm(self.Q, self.fox('abAB')[:, :2*n]),
                      s.diag(inv(rep['t']), inv(rep['t'])))

    def word(self, w):
        out = s.eye(self.n)
        for letter in w:
            out = mm(out, self.letters[letter])
        return out

    def fox(self, w):
        pre = s.eye(self.n)
        blocks = [s.zeros(self.n) for _ in 'abt']
        for letter in w:
            j = 'abt'.index(letter.lower())
            if letter.islower():
                blocks[j] += pre
                pre = mm(pre, self.letters[letter])
            else:
                pre = mm(pre, self.letters[letter])
                blocks[j] -= pre
        return s.Matrix.hstack(*blocks).applyfunc(s.expand)


def selector(n, indices):
    return s.eye(n)[indices, :], s.eye(n)[:, indices]


def cone(cell, projection, inclusion):
    n, m = cell.n, projection.rows
    assert zero(mm(projection, inclusion)-s.eye(m))
    pp, qq = [mm(mm(projection, x), inclusion) for x in (cell.P, cell.Q)]
    assert all(zero(mm(projection, x)-mm(y, projection))
               for x, y in ((cell.P, pp), (cell.Q, qq)))
    dt = (pp-s.eye(m)).col_join(qq-s.eye(m))
    gt = (s.eye(m)-qq).row_join(pp-s.eye(m))
    r1 = mm(s.diag(projection, projection), cell.R)
    r2 = mm(projection, cell.R2)
    dims = [n, 3*n+m, 2*n+2*m, m]
    d0 = cell.B.col_join(projection)
    d1 = cell.F.row_join(s.zeros(2*n, m)).col_join(r1.row_join(-dt))
    d2 = r2.row_join(-gt)
    assert zero(mm(cell.F, cell.B)) and zero(mm(gt, dt))
    assert zero(mm(r1, cell.B)-mm(dt, projection))
    assert zero(mm(r2, cell.F)-mm(gt, r1))
    assert zero(mm(d1, d0)) and zero(mm(d2, d1))
    ranks = [rank(x) for x in (d0, d1, d2)]
    h = [dims[j]-([0]+ranks)[j]-(ranks+[0])[j] for j in range(4)]
    maps = [rank(mm(projection, alg.kernel(cell.B))),
            rank(dt.row_join(mm(r1, alg.kernel(cell.F))))-rank(dt),
            rank(gt.row_join(r2))-rank(gt)]
    return dict(H=h, J=h[1]+h[3]-h[0]-h[2], dimensions=dims,
                cone_ranks=ranks,
                absolute_H=[n-rank(cell.B), 3*n-rank(cell.B)-rank(cell.F),
                            2*n-rank(cell.F), 0],
                positive_boundary_H=[m-rank(dt), 2*m-rank(dt)-rank(gt),
                                     m-rank(gt)],
                positive_rank=m, restriction_H_ranks=maps), (d0, d1, d2, r1, r2, dt, gt)


def analytic_controls(ck):
    r = s.symbols('r', nonnegative=True)
    ell, b, kappa = s.symbols('ell b kappa', positive=True)
    a = s.symbols('a', real=True)
    w = s.symbols('w', nonzero=True, real=True)
    for j in range(3):
        rho_log = (2*j-2)*r/ell-2*a*r+ell*b*w*(s.exp(2*r/ell)-1)
        ck('density_log_derivative_'+str(j), s.diff(rho_log, r)
           == (2*j-2)/ell-2*a+2*b*w*s.exp(2*r/ell))
        ck('positive_tail_derivative_'+str(j),
           s.limit(s.diff(rho_log, r).subs(w, 1), r, s.oo) == s.oo)
        ck('negative_tail_derivative_'+str(j),
           s.limit(s.diff(rho_log, r).subs(w, -1), r, s.oo) == -s.oo)
    t = s.symbols('t', nonnegative=True)
    ck('volterra_kernel_integral', s.integrate(s.exp(-kappa*t), (t, 0, s.oo)) == 1/kappa)
    # Actual exterior/interior form operations, not only scalar wall labels.
    eps = []
    for j in range(3):
        op = s.zeros(8)
        for mask in range(8):
            if not mask & (1 << j):
                op[mask | (1 << j), mask] = (-1)**((mask & ((1 << j)-1)).bit_count())
        eps.append(op)
    hat = eps[0]+eps[0].T
    ck('radial_wall_square', zero(hat*hat-s.eye(8)))
    for j, op in enumerate(eps):
        cliff = op-op.T
        ck('wall_anticommutes_principal_'+str(j), zero(cliff*hat+hat*cliff))
    ck('neutral_wall_control', s.zeros(8)*s.zeros(8) == s.zeros(8)
       and rank(s.zeros(8)) == 0 and rank(hat) == 8)
    # Finite control against mistaking complete-space closure for zero index.
    disk_boundary_map = s.Matrix([0, 1])
    toy_h = [1-rank(disk_boundary_map), 2-rank(disk_boundary_map)]
    ck('nonzero_euler_boundary_control', toy_h == [0, 1]
       and toy_h[0]-toy_h[1] == -1)


@lru_cache(None)
def run():
    checks, records = {}, {}
    def ck(name, value):
        assert name not in checks, name
        checks[name] = bool(value)
        assert checks[name], name
    data = json.loads((OLD/'silver_operator_gate_2026_10_05/candidate.json').read_text())
    v = seed.four(data)
    c = s.Matrix([s.Rational(x)+s.sqrt(2)*s.Rational(y)
                  for x, y in data['cocycle_Qsqrt2_pairs']])
    ck('same_literal_marking', data['relators'] == seed.marked_relators()
       and data['cusp_words'] == ['abAB', 'abt'])
    pairs = list(combinations(range(5), 2))
    weights = {'W': [1, 1, 1, 1, -4],
               'F': [([1, 1, 1, 1, -4][i]+[1, 1, 1, 1, -4][j]) for i, j in pairs]}
    ck('actual_induced_wedge_weights', weights['F'].count(2) == 6
       and weights['F'].count(-3) == 4)
    for amplitude in (0, 1):
        wrep = seed.extension(v, amplitude*c)
        ck('core_flag_not_global_split_'+str(amplitude),
           any(not zero(mm(s.diag(1, 1, 1, 1, -4), x)
                        -mm(x, s.diag(1, 1, 1, 1, -4))) for x in wrep.values()) == bool(amplitude))
        for label, rep in [('W', wrep), ('F', {g: seed.wedge(x) for g, x in wrep.items()})]:
            for dual in (False, True):
                rr = {g: inv(x).T for g, x in rep.items()} if dual else rep
                ww = [-x for x in weights[label]] if dual else weights[label]
                cell = Cell(rr, data)
                ck(f'{amplitude}_{label}_{dual}_field_dual',
                   all(zero(mm(x.T, rr[g])-s.eye(x.rows)) for g, x in rep.items()) if dual
                   else all(s.simplify(x.det()) == 1 for x in rep.values()))
                for sign in (1, -1):
                    indices = [j for j, weight in enumerate(ww) if sign*weight > 0]
                    projection, inclusion = selector(cell.n, indices)
                    row, mats = cone(cell, projection, inclusion)
                    key = f'{amplitude}:{label}{"dual" if dual else ""}:{sign}'
                    row['positive_indices'] = indices
                    row['weights'] = ww
                    records[key] = row
                    ck(key+'_all_degrees_nonnegative', min(row['H']) >= 0)
                    ck(key+'_full_zero_euler_index', row['J'] == 0)
                    d0, d1, d2, r1, r2, dt, gt = mats
                    ck(key+'_wrong_R2_sign_or_zero_map_control',
                       not zero(mm(-r2, cell.F)-mm(gt, r1)) if not zero(mm(gt, r1))
                       else zero(mm(gt, r1)) and zero(mm(r2, cell.F)))
                # Full non-diagonal frame transport, including the selected end flag.
                u = s.eye(cell.n)
                u[0, cell.n-1] = 2
                transported = Cell({g: mm(mm(inv(u), x), u) for g, x in rr.items()}, data)
                indices = [j for j, weight in enumerate(ww) if weight > 0]
                projection, inclusion = selector(cell.n, indices)
                target, _ = cone(transported, mm(projection, u), mm(inv(u), inclusion))
                old = records[f'{amplitude}:{label}{"dual" if dual else ""}:1']
                ck(f'{amplitude}_{label}_{dual}_whole_frame_transport',
                   all(old[k] == target[k] for k in ('H', 'cone_ranks', 'absolute_H', 'positive_boundary_H')))
    for amplitude in (0, 1):
        for label in ('W', 'F'):
            for sign in (1, -1):
                left = records[f'{amplitude}:{label}:{sign}']
                right = records[f'{amplitude}:{label}dual:{sign}']
                ck(f'{amplitude}_{label}_{sign}_full_dual_degree_reversal', left['H'] == right['H'][::-1])
    # At least one coordinate plane fails to reduce nonabelian peripheral transport.
    cell = Cell(wrep, data)
    bad_planes = []
    for index in range(5):
        bad, inc = selector(5, [index])
        bad_planes.append(any(not zero(mm(bad, x)-mm(mm(mm(bad, x), inc), bad))
                              for x in (cell.P, cell.Q)))
    ck('noninvariant_cusp_selection_rejected', any(bad_planes))
    analytic_controls(ck)
    return dict(checks=checks, passed=len(checks), records=records,
                analytic_proof_machine_certified=False, neutral_spectrum_computed=False,
                physical_end_or_parent_selected=False, physical_goal_achieved=False,
                compact_three_family_result_retracted=False)


if __name__ == '__main__':
    print(json.dumps(run(), indent=2, sort_keys=True))
