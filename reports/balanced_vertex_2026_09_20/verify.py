"""F09 exact tensor controls. No global modes or quantum phase computation."""
import importlib.util
from pathlib import Path
from functools import lru_cache
from itertools import combinations
from math import comb
import sympy as s


def sibling(name, directory):
    path = Path(__file__).parent.parent / directory / 'verify.py'
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


f08 = sibling('f09_f08', 'balanced_parent_2026_09_20')
f05 = f08.f05
PAIRS = tuple(combinations(range(4), 2))


def clean(m):
    return m.applyfunc(lambda a: s.simplify(s.expand(a)))


def volume_pairing():
    return s.Matrix(6, 6, lambda i, j: s.LeviCivita(*PAIRS[i], *PAIRS[j]))


def induced_j():
    return f05.exterior_group(f08.lorentz_j())


def internal_s():
    return volume_pairing()*induced_j()


def six_connection():
    return tuple(f05.exterior_lie(c) for c in f08.connection())


def six_boosts():
    return tuple(f05.exterior_lie(c) for c in f08.boosts())


def t_matrix(p):
    return sum((s.kronecker_product(f05.wedge(i, p), b)
                for i, b in enumerate(six_boosts())),
               s.zeros(comb(3, p+1)*6, comb(3, p)*6))


@lru_cache(None)
def bochner(p):
    out = s.zeros(comb(3, p)*6)
    if p < 3:
        up = t_matrix(p)
        out += up.H*up
    if p > 0:
        down = t_matrix(p-1)
        out += down*down.H
    return clean(out)


def exterior(u, v):
    return s.Matrix([u[a]*v[b]-u[b]*v[a] for a, b in PAIRS])


def current(u, v):
    # Input rows are the three form components, each a 4-vector.
    return tuple(clean(sum((s.LeviCivita(i, j, k)*
                    (exterior(u.row(i), v.row(j))+exterior(v.row(i), u.row(j)))/2
                    for i, j in combinations(range(3), 2)), s.zeros(6, 1)))
                 for k in range(3))


def vertex(u, v, w):
    return s.expand(sum((q.T*volume_pairing()*w.row(k).T)[0]
                        for k, q in enumerate(current(u, v))))


def codazzi_profile(b):
    return s.zeros(3, 1).row_join(b)


def cross_rows(q):
    return s.Matrix([[v[5], -v[4], v[3]] for v in q])


def symmetric_tracefree(real=False):
    a, b, c, d, e = s.symbols('a b c d e', real=real)
    return s.Matrix([[a, c, d], [c, b, e], [d, e, -a-b]])


def anti4(u):
    return u.conjugate()*f08.lorentz_j().T


def anti6_dual(w):
    return w.conjugate()*induced_j().T


def trilinear_matrix(w):
    # Coefficient for the full ordered epsilon sum, hence 2*vertex.
    def entry(row, col):
        i, a = divmod(row, 4)
        j, b = divmod(col, 4)
        return sum(s.LeviCivita(i, j, k)*s.LeviCivita(a, b, c, d)*w[k, n]
                   for k in range(3) for n, (c, d) in enumerate(PAIRS))
    return s.Matrix(12, 12, entry)


def lie_basis():
    result = []
    for i in range(4):
        for j in range(4):
            if i != j:
                m = s.zeros(4)
                m[i, j] = 1
                result.append(m)
    for i in range(3):
        m = s.zeros(4)
        m[i, i], m[i+1, i+1] = 1, -1
        result.append(m)
    return tuple(result)


def response(k, j):
    return s.simplify((j.H*k.inv()*j)[0])
