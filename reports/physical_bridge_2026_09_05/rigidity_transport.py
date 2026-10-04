"""R84 exact local review. No target census or computations on import."""
from itertools import combinations, product
import json
import sympy as s


def adjoint(z):
    u = s.Matrix([[1, z], [0, 1]])
    basis = [s.Matrix([[0, 1], [0, 0]]), s.diag(1, -1),
             s.Matrix([[0, 0], [1, 0]])]
    cols = []
    for b in basis:
        t = u*b*u.inv()
        cols.append(s.Matrix([t[0, 1], t[0, 0], t[1, 0]]))
    return s.Matrix.hstack(*cols)


def wedge_lie(a):
    pairs = list(combinations(range(a.rows), 2))
    out = s.zeros(len(pairs))
    for col, (i, j) in enumerate(pairs):
        for k in range(a.rows):
            if k != j:
                out[pairs.index(tuple(sorted((k, j)))), col] += (1 if k < j else -1)*a[k, i]
            if k != i:
                out[pairs.index(tuple(sorted((i, k)))), col] += (1 if i < k else -1)*a[k, j]
    return out


def logs(p, q):
    n = s.Matrix([[0, 1], [0, 0]])
    x, y = s.zeros(5), s.zeros(5)
    x[:4, :4] = s.kronecker_product(n, s.eye(2))
    y[:4, :4] = s.kronecker_product(s.eye(2), n)
    x[2, 4], y[1, 4] = p, q
    return x, y


def cohom(x, y):
    d0 = x.col_join(y)
    d1 = (-y).row_join(x)
    if d1*d0 != s.zeros(x.rows, x.cols):
        raise ValueError('not commuting: no cochain complex')
    r0, r1 = d0.rank(), d1.rank()
    return [x.rows-r0, 2*x.rows-r0-r1, x.rows-r1]


def checks():
    out = {}
    def keep(key, value):
        out[key] = bool(value)
    def equal(a, b):
        return all(s.simplify(v) == 0 for v in a-b)
    e = s.Matrix([1, 0, 0])
    for z in (1, s.I, 1+s.I, 2+3*s.I):
        a = adjoint(z)
        d = a-s.eye(3)
        keep(f'fixed-image:{z}', d*e == s.zeros(3, 1) and d.rank() == 2 and d.row_join(e).rank() == 2)
        for phase, m in ((1, 3), (-1, 2), (s.I, 4), (-s.I, 4)):
            t = phase*a
            norm = sum((t**j for j in range(m)), s.zeros(3))
            keep(f'power:{z}:{phase}', equal(norm*(t-s.eye(3)), t**m-s.eye(3)) and equal(t**m, adjoint(m*z)))
    a, b = adjoint(1), adjoint(s.I)
    x, y = a-s.eye(3), b-s.eye(3)
    keep('adjoint-torus', cohom(x, y) == [1, 2, 1])
    c = s.zeros(6, 1); c[3] = 1
    keep('local-positive-not-common-boundary', x.col_join(y).row_join(c).rank() == x.col_join(y).rank()+1)
    keep('local-positive-is-cocycle', (-y).row_join(x)*c == s.zeros(3, 1))
    for r, t in product(range(-2, 3), repeat=2):
        if not (r or t):
            continue
        d = adjoint(r+s.I*t)-s.eye(3)
        keep(f'cyclic:{r}:{t}', d.row_join(t*e).rank() == d.rank())
    keep('nu-minus-one-square-not-acyclic', cohom(x, y) != [0, 0, 0] and
         cohom(-a-s.eye(3), b-s.eye(3)) == [0, 0, 0])
    for p, q in ((0, 0), (1, 0), (0, 1), (1, 1), (1, -1), (2, 3)):
        x, y = logs(p, q)
        keep(f'W:{p}:{q}', cohom(x, y) == ([1, 3, 2] if p or q else [2, 4, 2]))
        keep(f'L2W:{p}:{q}', cohom(wedge_lie(x), wedge_lie(y)) == ([2, 5, 3] if p or q else [3, 6, 3]))
    lx, ly = logs(0, 0)
    sx, sy = wedge_lie(lx[:4, :4]), wedge_lie(ly[:4, :4])
    d0, d1 = sx.col_join(sy), (-sy).row_join(sx)
    w1, w2 = s.zeros(12, 1), s.zeros(12, 1)
    w1[1], w2[6] = 1, 1
    keep('wedge-cusp-dimensions', cohom(sx, sy) == [2, 4, 2])
    keep('wedge-map-injective', d1*w1 == s.zeros(6, 1) and d1*w2 == s.zeros(6, 1)
         and d0.row_join(w1).row_join(w2).rank() == d0.rank()+2)
    for p, q in ((1, 0), (0, 1), (1, 1), (1, -1), (2, 3)):
        keep(f'wedge-class:{p}:{q}', d0.row_join(p*w1+q*w2).rank() == d0.rank()+1)
    x, y = logs(1, 1)
    for z in (s.I, 1+s.I, 2+3*s.I):
        keep(f'nonreal-shape:{z}', cohom(x+y, z*x+s.conjugate(z)*y) == [1, 3, 2])
    keep('real-shape-opposite', cohom(x+y, 2*(x+y)) != [1, 3, 2])
    hS,hQ,aS,aQ,tS,tQ,r0,r1,rP = s.symbols('hS hQ aS aQ tS tQ r0 r1 rP')
    hE, aE, tE = hS+hQ-r0-r1, aS+aQ-r0, tS+tQ-rP
    keep('LES-signs', s.expand(hE-2*aE+tE-(hS-2*aS+tS+hQ-2*aQ+tQ+r0-r1-rP)) == 0)
    return out


if __name__ == '__main__':
    result = checks()
    print(json.dumps({'checks': result, 'total': len(result), 'all': all(result.values())}, sort_keys=True))
    raise SystemExit(0 if all(result.values()) else 1)
