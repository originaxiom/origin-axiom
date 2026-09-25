"""R45 exact parent/end controls; not a global analytic or physical certificate."""
from collections import Counter
from functools import lru_cache
import importlib.util
import itertools
import json
from pathlib import Path

import sympy as s


def load(name, file):
    spec = importlib.util.spec_from_file_location(name, Path(__file__).with_name(file))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


cc = load('r45_cusp_input', 'canonical_cusp.py')
pb = load('r45_parent_input', 'parent_background.py')
KINDS = ('4', 'dual4', '6', '15')
BASIS = pb.endomorphism_basis(4)
OFF = list(itertools.permutations(range(4), 2))


def coordinates(x):
    if s.simplify(s.trace(x)) != 0:
        raise ValueError('traceless endomorphism required')
    return s.Matrix([x[i,j] for i,j in OFF]+[x[i,i] for i in range(3)])


def action(kind, x):
    if kind == '4':
        return x
    if kind == 'dual4':
        return -x.T
    if kind == '6':
        return pb.exterior_action(x)
    if kind == '15':
        return s.Matrix.hstack(*[coordinates(cc.comm(x,b)) for b in BASIS])
    raise ValueError(kind)


def group_action(kind, g):
    if kind == '4':
        return g
    if kind == 'dual4':
        return g.inv().T
    if kind == '6':
        pairs = list(itertools.combinations(range(4),2))
        return s.Matrix(6,6,lambda a,b:g.extract(pairs[a],pairs[b]).det())
    if kind == '15':
        gi = g.inv()
        return cc.clean(s.Matrix.hstack(*[coordinates(g*b*gi) for b in BASIS]))
    raise ValueError(kind)


@lru_cache(None)
def operators(kind):
    return tuple(action(kind,x) for x in (cc.D,cc.N0,cc.P,cc.J))


def weight_indices(kind, nonzero=True):
    d = operators(kind)[0]
    assert d.is_diagonal()
    return [i for i in range(d.rows) if (d[i,i] != 0) == nonzero]


def select(a, indices):
    return a.extract(indices,indices)


def exp_nilpotent(a):
    term = result = s.eye(a.rows)
    for j in range(1,a.rows+1):
        term = cc.clean(term*a/j)
        if term == s.zeros(a.rows):
            return cc.clean(result)
        result += term
    raise ValueError('not nilpotent within dimension bound')


def inverse(kind, include_zero=False):
    d,n,p,j = operators(kind)
    ids = list(range(d.rows)) if include_zero else weight_indices(kind)
    d,p = select(d,ids),select(p,ids)
    if any(d[i,i] == 0 for i in range(d.rows)):
        raise ValueError('zero longitudinal weight is outside this inverse')
    a = s.I*cc.W*s.eye(d.rows)+cc.K*d
    ai = s.diag(*[1/a[i,i] for i in range(a.rows)])
    nil = cc.BETA*p/cc.R
    term = result = ai
    for degree in range(1,d.rows+1):
        term = cc.clean(-ai*nil*term)
        if term == s.zeros(d.rows):
            return a+nil,cc.clean(result)
        result += term
    raise ValueError('nilpotent inverse did not terminate')


def flat_residuals(kind):
    d,n,p,j = operators(kind)
    bx,bt,br = n/s.sqrt(cc.R),cc.K*d+cc.BETA*p/cc.R,j/cc.R
    return tuple(cc.clean(a) for a in (cc.comm(bx,bt),
        bx.diff(cc.R)+cc.comm(br,bx),bt.diff(cc.R)+cc.comm(br,bt)))


def koszul(a,b):
    c0 = a.col_join(b)
    c1 = (-b).row_join(a)
    ranks = c0.rank(),c1.rank()
    return {'ranks':ranks, 'dims':(a.rows-ranks[0],2*a.rows-sum(ranks),a.rows-ranks[1]),
            'chain':cc.clean(c1*c0) == s.zeros(a.rows)}


@lru_cache(None)
def zero_sector():
    ids = weight_indices('15',False)
    d,n,p,j = [select(x,ids) for x in operators('15')]
    logs = koszul(n,p)
    ident = s.eye(len(ids))
    exp = koszul(exp_nilpotent(n)-ident,exp_nilpotent(2*p)-ident)
    inv = s.Matrix.hstack(*[coordinates(x).extract(ids,[0]) for x in (cc.D,cc.N0,cc.P)])
    return {'dimension':len(ids),'longitude_rank':p.rank(),
            'longitude_nilpotent':p**3 == s.zeros(len(ids)),
            'log':logs,'exp':exp, 'invariants_rank':inv.rank(),
            'invariants_killed':n*inv == s.zeros(len(ids),3) and p*inv == s.zeros(len(ids),3)}


def parallel_controls():
    matrices = (cc.D,cc.N0,cc.P)
    powers = (s.S(0),s.Rational(1,2),s.S(1))
    bx,bt,br,_ = cc.connection()
    residuals = []
    for mat,power in zip(matrices,powers):
        section = cc.R**(-power)*mat
        residuals.append(tuple(cc.clean(x) for x in
            (cc.comm(bx,section),cc.comm(bt,section),section.diff(cc.R)+cc.comm(br,section))))
    return residuals,[-s.Rational(3,2)-2*a for a in powers]


@lru_cache(None)
def lie_invariants():
    return {kind:len(pb.common_kernel(tuple(action(kind,x) for x in BASIS))) for kind in KINDS}


@lru_cache(None)
def literal_invariants(q):
    m,n = cc.prior.generators(q)
    answer = {}
    for kind in KINDS:
        acts = [group_action(kind,g) for g in (m,n)]
        answer[kind] = len(pb.common_kernel(tuple(a-s.eye(a.rows) for a in acts)))
    return answer


def full_weights():
    answer = Counter({0:45})
    for kind,multiplicity in (('15',1),('6',10),('dual4',16),('4',16)):
        d = operators(kind)[0]
        answer.update({int(k):multiplicity*v for k,v in Counter(d.diagonal()).items()})
    return dict(sorted(answer.items()))


def direct_root_weights():
    branch = pb.branching()
    cartan = sum((v*cc.D[i,i] for i,v in enumerate(branch['weights'])),s.zeros(3,1))
    result = Counter()
    for root,multiplicity in branch['actual'].items():
        result[int(s.Matrix(root[5:]).dot(cartan))] += multiplicity
    return dict(sorted(result.items()))


def run():
    b,z = pb.branching(),zero_sector()
    par,powers = parallel_controls()
    inverses = {}
    for kind in KINDS:
        t,ti = inverse(kind)
        inverses[kind] = all(cc.clean(a) == s.zeros(t.rows)
            for a in (t*ti-s.eye(t.rows),ti*t-s.eye(t.rows)))
    old_e,old_f,old_h = pb.generators()
    old_wedge = len(pb.common_kernel(tuple(pb.exterior_action(x) for x in (old_e,old_f,old_h))))
    actual_m,_ = cc.prior.generators(s.S(1))
    checks = {
        'actual_parent_map':b['actual'] == b['expected'] and b['actual'] != b['wrong'],
        'whole_root_weights':full_weights() == direct_root_weights(),
        'trace_ratio':b['trace_ratio'] == 60,
        'no_sl4_invariants':all(n == 0 for n in lie_invariants().values()),
        'literal_holonomy_controls':all(all(n == 0 for n in literal_invariants(q).values())
            for q in (s.S(2),s.Rational(1,2))),
        'different_Sym3_input':old_wedge == 1 and old_e**3 != s.zeros(4)
            and (actual_m-s.eye(4))**3 == s.zeros(4) and (actual_m-s.eye(4))**2 != s.zeros(4),
        'full_radial_flatness':all(all(x == s.zeros(x.rows) for x in flat_residuals(kind)) for kind in KINDS),
        'all_nonzero_inverses':all(inverses.values()),
        'zero_sector_complex':z['log']['dims'] == (3,6,3) and z['exp']['dims'] == (3,6,3)
            and z['log']['chain'] and z['exp']['chain'] and z['invariants_killed'] and z['invariants_rank'] == 3,
        'zero_longitude_singular':z['dimension'] == 9 and z['longitude_rank'] == 4 and z['longitude_nilpotent'],
        'radial_parallel_sections':all(all(x == s.zeros(4) for x in row) for row in par),
        'tail_norm_powers':powers == [-s.Rational(3,2),-s.Rational(5,2),-s.Rational(7,2)]}
    return {'checks':checks,'all_checks_pass':all(checks.values()), 'weights':full_weights(),
        'lie_invariants':lie_invariants(), 'zero_sector':z,
        'parent_peripheral_cohomology':[a+45*b for a,b in zip(z['log']['dims'],(1,2,1))],
        'compact_gauge_kernel_dimension':45+lie_invariants()['15']+10*lie_invariants()['6']
            +16*(lie_invariants()['4']+lie_invariants()['dual4']),
        'grade':'Authored application of external density and R44 global proof; finite algebra controls.',
        'neutral_global_H1_computed':False,'physical_chirality_derived':False}


if __name__ == '__main__':
    result = run()
    print(json.dumps(result,sort_keys=True))
    raise SystemExit(0 if result['all_checks_pass'] else 1)
