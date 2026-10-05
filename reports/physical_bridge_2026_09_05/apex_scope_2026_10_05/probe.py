"""Exact scoped apex audit. No foreign producer imports or physics verdict."""
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations, product
import json
import sympy as s
from sympy.matrices.normalforms import hermite_normal_form


def cubic_blocks():
    q = s.Matrix(3, 3, s.symbols('q:9'))
    qc = s.Matrix(3, 3, s.symbols('c:9'))
    l = s.Matrix(3, 3, s.symbols('l:9'))
    poly = q.det() + qc.det() + l.det() + s.trace(q*l*qc)
    n, nu = l[2, 2], l[2, 1]
    hu, hd, ll = list(l[:2, 0]), list(l[:2, 1]), list(l[:2, 2])
    dd, db, dc = list(q[:, 2]), list(qc[2, :]), list(qc[1, :])
    at = {x: 0 for x in list(q)+list(qc)+list(l) if x not in (n, nu)}
    md = s.Matrix([[s.diff(poly, a, b).subs(at) for b in hd+ll] for a in hu])
    mt = s.Matrix([[s.diff(poly, a, b).subs(at) for b in db+dc] for a in dd])
    return n, nu, md, mt


def generation_blocks(g, gn):
    if g.shape != gn.shape or g.rows != g.cols:
        raise ValueError('square equal generation blocks required')
    j = s.Matrix([[0, 1], [-1, 0]])
    md = s.kronecker_product(g, j.row_join(s.zeros(2)))
    md += s.kronecker_product(gn, s.zeros(2).row_join(-j))
    mt = s.kronecker_product(g, s.eye(3).row_join(s.zeros(3)))
    mt += s.kronecker_product(gn, s.zeros(3).row_join(s.eye(3)))
    return md, mt


def dot(x, y):
    return sum(a*b for a, b in zip(x[:5], y[:5])) + F(3, 4)*x[5]*y[5]


def roots_weights():
    roots = []
    for a, b in combinations(range(5), 2):
        for u, v in product((-1, 1), repeat=2):
            w = [F(0)]*6
            w[a], w[b] = F(u), F(v)
            roots.append(tuple(w))
    weights = []
    for signs in product((-1, 1), repeat=5):
        w = tuple(F(x, 2) for x in signs)
        if signs.count(-1) % 2 == 0:
            r = w+(F(1),)
            roots += [r, tuple(-x for x in r)]
        else:
            weights.append(w+(F(1, 3),))
    for a in range(5):
        for u in (-1, 1):
            w = [F(0)]*5
            w[a] = F(u)
            weights.append(tuple(w)+(F(-2, 3),))
    weights.append((F(0),)*5+(F(4, 3),))
    return roots, weights


@lru_cache(None)
def torus():
    roots, weights = roots_weights()
    y = (F(-1, 3),)*3+(F(1, 2),)*2+(F(0),)
    gamma = (F(1, 2),)*5+(F(-5, 3),)
    beta = (F(1, 2),)*5+(F(1),)
    pairs = [(dot(y, r), dot(gamma, r)) for r in roots]
    den = s.ilcm(*[x.denominator for p in pairs for x in p])
    h = hermite_normal_form(s.Matrix([[int(a*den) for a, _ in pairs],
                                     [int(b*den) for _, b in pairs]]))
    lattice = h.T/den
    dual = lattice.inv()
    sm = {r for r in roots if r[5] == 0 and sum(r[:5]) == 0 and
          ((r[3] == r[4] == 0) or (r[0] == r[1] == r[2] == 0))}
    w15 = [w for w in weights if dot(beta, w) == 0]
    w6 = [w for w in weights if dot(beta, w) == 1]
    out = []
    for m, n in product(range(4), repeat=2):
        st = dual*s.Matrix([s.Rational(m, 4), s.Rational(n, 4)])
        v = tuple(F(st[0])*y[k]+F(st[1])*gamma[k] for k in range(6))
        if {r for r in roots if dot(beta, r) == 0 and dot(v, r).denominator == 1} != sm:
            continue
        raw = [dot(v, w) % 1 for w in weights]
        defect = {(4*p) % 1 for p in raw}
        if len(defect) != 1 or next(iter(defect))*3 % 1:
            raise ValueError('noncentral fourth power')
        shifts = [F(j, 3) for j in range(3)
                  if all((4*(p+F(j, 3))) % 1 == 0 for p in raw)]
        if len(shifts) != 1:
            raise ValueError('no unique genuine order-four lift')
        shift = shifts[0]
        p15 = tuple(int(4*((dot(v, w)+shift) % 1)) for w in w15)
        p6bar = tuple(int(4*((dot(v, w)+shift) % 1)) for w in w6)
        six = tuple(sorted((-p) % 4 for p in p6bar))
        if sum(six) % 4:
            raise ValueError('SU6 determinant is not one')
        exterior = Counter((a+b) % 4 for a, b in combinations(six, 2))
        if Counter(p15) != exterior:
            raise ValueError('27 exterior-square consistency fails')
        out.append({'adjoint_key': [m, n], 'central_defect': str(next(iter(defect))),
                    'central_shift': str(shift), 'six': six,
                    'p15': p15, 'p6bar': p6bar})
    return out


ONE = (1, 0, 0, 0)
Q8 = [tuple(sign if j == k else 0 for j in range(4))
      for k in range(4) for sign in (-1, 1)]


def qm(p, q):
    a, b, c, d = p
    e, f, g, h = q
    return (a*e-b*f-c*g-d*h, a*f+b*e+c*h-d*g,
            a*g-b*h+c*e+d*f, a*h+b*g-c*f+d*e)


def qi(p):
    return (p[0], -p[1], -p[2], -p[3])


def phi(w):
    images = {'a': 'aab', 'b': 'ab', 'A': 'BAA', 'B': 'BA'}
    return ''.join(images[x] for x in w)


def qw(w, a, b):
    r = ONE
    d = {'a': a, 'b': b, 'A': qi(a), 'B': qi(b)}
    for x in w:
        r = qm(r, d[x])
    return r


@lru_cache(None)
def lines():
    pa, pb = phi(phi(phi('a'))), phi(phi(phi('b')))
    return [(a, b) for a, b in product(Q8, repeat=2)
            if qm(a, b) != qm(b, a) and qw(pa, a, b) == a and qw(pb, a, b) == b]


def reduced_words(bound):
    words, level = [], ['']
    for _ in range(bound):
        level = [w+x for w in level for x in 'aAbB'
                 if not w or w[-1] != x.swapcase()]
        words += level
    return words


PHASE = ((1, 0), (0, 1), (-1, 0), (0, -1))


def trace27(row, line, char, w):
    k = sum(char[0]*(1 if x == 'a' else -1) if x.lower() == 'a'
            else char[1]*(1 if x == 'b' else -1) for x in w) % 4
    tr2 = 2*qw(w, *line)[0]
    return tuple(sum(PHASE[k*p % 4][j] for p in row['p15']) +
                 tr2*sum(PHASE[k*p % 4][j] for p in row['p6bar']) for j in (0, 1))


@lru_cache(None)
def deck_census():
    chars = [c for c in product(range(4), repeat=2) if c[0] % 2 or c[1] % 2]
    words = reduced_words(6)
    out = []
    for row in torus():
        for a, b in lines():
            dl = (qw(phi('a'), a, b), qw(phi('b'), a, b))
            for x, y in chars:
                dc = ((2*x+y) % 4, (x+y) % 4)
                # Relations must hold both in Q8 and on every torus phase.
                for rel in (phi(phi(phi('a')))+'A', phi(phi(phi('b')))+'B'):
                    if qw(rel, a, b) != ONE or trace27(row, (a, b), (x, y), rel) != (27, 0):
                        raise ValueError('invalid full-27 relator')
                witness = next((w for w in words if trace27(row, (a, b), (x, y), w) !=
                                trace27(row, dl, dc, w)), None)
                out.append({'six': list(row['six']), 'a': list(a), 'b': list(b),
                            'char': [x, y], 'witness': witness,
                            'trace': list(trace27(row, (a, b), (x, y), witness)) if witness else None,
                            'deck_trace': list(trace27(row, dl, dc, witness)) if witness else None})
    return out


def selection():
    charges = {'triplet_mass': 2+2, 'Higgs_mass': 2+3,
               'up_Yukawa': 2+2*1, 'down_Yukawa': 3+1+0,
               'neutrino_operator': 2*(2+0), 'H_bar5_bilinear': 2+0,
               '10_bar5_bar5': 1+2*0, '10_10_10_bar5': 3*1+0}
    w = s.diag(-1, -1, -1, s.I, s.I)
    p = sum(((-w)**k for k in range(4)), s.zeros(5))/4
    opposite = sum(((-s.I*w)**k for k in range(4)), s.zeros(5))/4
    return {k: v % 4 for k, v in charges.items()}, w, p, opposite


def run():
    checks = {}
    def ck(key, value):
        checks[key] = bool(value)
    n, nu, md, mt = cubic_blocks()
    j = s.Matrix([[0, 1], [-1, 0]])
    ck('cubic/actual_doublet_Hessian', md == (n*j).row_join(-nu*j))
    ck('cubic/actual_triplet_Hessian', mt == (n*s.eye(3)).row_join(nu*s.eye(3)))
    cases = []
    for size in range(1, 5):
        for kind in ('zero', 'identity', 'ones', 'singular', 'noncommuting'):
            g = {'zero': s.zeros(size), 'identity': s.eye(size), 'ones': s.ones(size),
                 'singular': s.diag(*([1]*(size-1)+[0])),
                 'noncommuting': s.Matrix(size, size, lambda i,j: int(j == i+1))}[kind]
            gn = s.diag(*range(size))
            a, b = generation_blocks(g, gn)
            rank = g.row_join(gn).rank()
            ck(f'rank/{size}/{kind}', a.rank() == 2*rank and b.rank() == 3*rank)
            cases.append([size, kind, rank])
    roots, weights = roots_weights()
    ck('torus/complete_roots_weights', len(set(roots)) == 72 and len(set(weights)) == 27)
    ck('torus/integral_pairings', all(dot(w,r).denominator == 1 for w in weights for r in roots))
    ck('torus/four_SM_classes', len(torus()) == 4)
    ck('torus/distinct_SU6_lifts', len({r['six'] for r in torus()}) == 4)
    ck('group/24_Q8_lines', len(lines()) == 24)
    half = (F(1,2),)*4
    normalizer = Q8 + [qm(q, h) for q in Q8 for h in (half, qm(half, half))]
    ck('deck/Q8_only_compact_lifts', all(any(
        qm(qm(c, a), qi(c)) == qw(phi('a'), a, b) and
        qm(qm(c, b), qi(c)) == qw(phi('b'), a, b) for c in normalizer) for a,b in lines()))
    rows = deck_census()
    keys = {(tuple(r['six']), tuple(r['a']), tuple(r['b']), tuple(r['char'])) for r in rows}
    ck('deck/exhaustive_1152_keys', len(rows) == len(keys) == 4*24*12)
    ck('deck/all_exact_obstructions', all(r['witness'] and r['trace'] != r['deck_trace'] for r in rows))
    phases, w, p, op = selection()
    ck('selection/SU5_W', w.det() == 1 and w.conjugate().T*w == s.eye(5) and w**4 == s.eye(5))
    ck('selection/actual_mass_projector', p == s.diag(1,1,1,0,0) and p.rank() == 3)
    ck('selection/opposite_control', op == s.diag(0,0,0,1,1))
    ck('selection/all_operator_phases', phases == {'triplet_mass':0,'Higgs_mass':1,'up_Yukawa':0,
        'down_Yukawa':0,'neutrino_operator':0,'H_bar5_bilinear':2,'10_bar5_bar5':1,'10_10_10_bar5':3})
    ck('selection/not_invertible_basis_change', p.det() == 0 and all(((-w)**k).det() != 0 for k in range(4)))
    ck('selection/trivial_control', sum((s.eye(5)**k for k in range(4)), s.zeros(5))/4 == s.eye(5))
    mixed = s.zeros(5); mixed[0,3] = 1
    ck('selection/not_SU5_invariant', p*mixed != mixed*p)
    failed = [k for k,v in checks.items() if not v]
    return {'checks':checks, 'passed':len(checks)-len(failed), 'total':len(checks), 'failed':failed,
            'torus':torus(), 'rank_cases':cases, 'rows':rows, 'operator_phases':phases,
            'physical_goal_achieved':False, 'non_author_acceptance':False}


if __name__ == '__main__':
    result = run()
    print(json.dumps(result, indent=2))
    raise SystemExit(bool(result['failed']))
