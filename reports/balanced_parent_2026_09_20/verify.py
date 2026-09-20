"""F08 exact balanced-parent controls; no global eigenfunction computation."""
import importlib.util
from pathlib import Path
from functools import lru_cache
from itertools import combinations, product
from math import comb
import sympy as s


def load_sibling(name, dirname):
    path = Path(__file__).parent.parent / dirname / 'verify.py'
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


f05 = load_sibling('f08_f05', 'parent_twist_gap_2026_09_20')
f06 = load_sibling('f08_f06', 'isotropic_parent_core_2026_09_20')
x, y, z = f05.COORDS
COORDS = (x, y, z)


def clean(matrix):
    return matrix.applyfunc(lambda value: s.simplify(s.expand_complex(value)))


def basis():
    return s.Matrix([[1, 0, 0, 1], [0, 1, s.I, 0],
                     [0, 1, -s.I, 0], [1, 0, 0, -1]])/s.sqrt(2)


def lorentz_j():
    return s.diag(-1, 1, 1, 1)


def balanced_group(g):
    return clean(basis().H*s.kronecker_product(g, g.conjugate())*basis())


def boosts():
    result = []
    for i in range(3):
        n = s.zeros(4)
        n[0, i+1] = n[i+1, 0] = 1
        result.append(n)
    return tuple(result)


@lru_cache(None)
def connection():
    e, _, h = f05.lie(1)
    c0 = (e/z, s.I*e/z, h/(2*z))
    return tuple(clean(basis().H*(s.kronecker_product(c, s.eye(2))
                          +s.kronecker_product(s.eye(2), c.conjugate()))*basis()) for c in c0)


def split():
    return (tuple(clean((c-c.H)/2) for c in connection()),
            tuple(clean((c+c.H)/2) for c in connection()))


def scaled_connection(t):
    a, psi = split()
    return tuple(a[i]+t*psi[i] for i in range(3))


def flat_residual(c):
    return tuple(clean(c[j].diff(COORDS[i])-c[i].diff(COORDS[j])
                         +c[i]*c[j]-c[j]*c[i]) for i, j in combinations(range(3), 2))


def moment(c):
    div = sum((z**3*((c[i]+c[i].H)/z).diff(COORDS[i]) for i in range(3)), s.zeros(4))
    bracket = z*z*sum((c[i]*c[i].H-c[i].H*c[i] for i in range(3)), s.zeros(4))
    return clean(div+bracket)


def coframe_connection():
    return tuple(s.Matrix(3, 3, lambda a, b: s.simplify(
        f05.gamma()[a][i][b]+int(i == 2 and a == b)/z)) for i in range(3))


def parallel_residual():
    a, psi = split()
    return tuple(clean(psi[j].diff(COORDS[i])+a[i]*psi[j]-psi[j]*a[i]
        -sum((f05.gamma()[k][i][j]*psi[k] for k in range(3)), s.zeros(4)))
        for i, j in product(range(3), repeat=2))


def t_matrix(degree):
    return sum((s.kronecker_product(f05.wedge(i, degree), v)
                for i, v in enumerate(boosts())),
               s.zeros(comb(3, degree+1)*4, comb(3, degree)*4))


def bochner(degree):
    result = s.zeros(comb(3, degree)*4)
    if degree < 3:
        t = t_matrix(degree)
        result += t.H*t
    if degree > 0:
        t = t_matrix(degree-1)
        result += t*t.H
    return clean(result)


def commutant_equations():
    entries = s.symbols('v0:16')
    v = s.Matrix(4, 4, entries)
    equations = [entry for b in boosts() for entry in b*v-v*b]
    return s.linear_eq_to_matrix(equations, entries)[0]


def covariant_cusp_derivative(b, i):
    # Components in the orthonormal frame, derivative along e_i=z partial_i.
    omega = z*coframe_connection()[i]
    partial = z*b.diff(z) if i == 2 else s.zeros(3)
    return (partial-omega.T*b-b*omega).applyfunc(s.simplify)


def cusp_codazzi(b):
    deriv = [covariant_cusp_derivative(b, i) for i in range(3)]
    return tuple(s.simplify(deriv[i][j, k]-deriv[j][i, k])
                 for i, j in combinations(range(3), 2) for k in range(3))


def cusp_solution(c, d, e):
    return s.Matrix([[(c*z**3+d*z)/2, e*z, 0],
                     [e*z, (c*z**3-d*z)/2, 0], [0, 0, -c*z**3]])
