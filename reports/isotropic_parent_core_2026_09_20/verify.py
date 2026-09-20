"""F06 exact local jets; no global background or spectral fit."""
from functools import lru_cache
from itertools import combinations, product
from math import comb
import sympy as s

v, a = s.symbols('v a', positive=True)
dv = s.symbols('v1:4', real=True)
ddv_symbols = s.symbols('v11 v12 v13 v22 v23 v33', real=True)
ddv = s.Matrix([[ddv_symbols[0], ddv_symbols[1], ddv_symbols[2]],
                [ddv_symbols[1], ddv_symbols[3], ddv_symbols[4]],
                [ddv_symbols[2], ddv_symbols[4], ddv_symbols[5]]])
U = s.diag(3, -1, -1, -1)


def clean(expression):
    return expression.applyfunc(s.simplify) if isinstance(expression, s.MatrixBase) else s.simplify(expression)


def derivative(expression, i):
    return s.diff(expression, v)*dv[i]+sum((s.diff(expression, dv[j])*ddv[j, i]
                                          for j in range(3)), s.zeros(*expression.shape) if isinstance(expression, s.MatrixBase) else 0)


def nilpotents():
    out = []
    for i in range(3):
        matrix = s.zeros(4)
        matrix[0, i+1] = 1
        out.append(matrix)
    return tuple(out)


def connection(count=3):
    return tuple(dv[i]*U/(8*v)+(a/s.sqrt(v)*n if i < count else s.zeros(4))
                 for i, n in enumerate(nilpotents()))


def flatness(c):
    return tuple(clean(derivative(c[j], i)-derivative(c[i], j)+c[i]*c[j]-c[j]*c[i])
                 for i, j in combinations(range(3), 2))


def moment(c):
    divergence = sum((derivative(v*(matrix+matrix.H), i) for i, matrix in enumerate(c)), s.zeros(4))/v**3
    commutator = sum((matrix*matrix.H-matrix.H*matrix for matrix in c), s.zeros(4))/v**2
    return clean(divergence+commutator)


def split():
    c = connection()
    return tuple((m-m.H)/2 for m in c), tuple((m+m.H)/2 for m in c)


@lru_cache(None)
def christoffel():
    metric, inverse = v**2*s.eye(3), s.eye(3)/v**2
    return [[[clean(sum(inverse[k, l]*(derivative(metric[l, j], i)+derivative(metric[l, i], j)
                            -derivative(metric[i, j], l)) for l in range(3))/2)
               for j in range(3)] for i in range(3)] for k in range(3)]


@lru_cache(None)
def ricci():
    gamma = christoffel()
    return s.Matrix(3, 3, lambda i, j: clean(sum(
        derivative(gamma[k][i][j], k)-derivative(gamma[k][i][k], j)
        +sum(gamma[k][k][l]*gamma[l][i][j]-gamma[k][j][l]*gamma[l][i][k] for l in range(3))
        for k in range(3))))


def higgs_tensor():
    _, psi = split()
    return s.Matrix(3, 3, lambda i, j: clean(s.trace(psi[i]*psi[j])))


def covariant_higgs_derivatives():
    connection_a, psi = split()
    gamma = christoffel()
    return tuple(clean(derivative(psi[j], i)+connection_a[i]*psi[j]-psi[j]*connection_a[i]
                 -sum((gamma[k][i][j]*psi[k] for k in range(3)), s.zeros(4)))
                 for i, j in product(range(3), repeat=2))


def center_substitution():
    return {v: 1, a: 1, **dict.fromkeys(dv, 0),
            **{ddv[i, j]: -s.Rational(4, 3) if i == j else 0 for i in range(3) for j in range(i, 3)}}


def wedge(i, degree):
    source = list(combinations(range(3), degree))
    target = list(combinations(range(3), degree+1))
    matrix = s.zeros(len(target), len(source))
    for column, subset in enumerate(source):
        if i not in subset:
            row = target.index(tuple(sorted((i,)+subset)))
            matrix[row, column] = (-1)**sum(j < i for j in subset)
    return matrix


def center_t(degree):
    return sum((s.kronecker_product(wedge(i, degree), (n+n.T)/2)
                for i, n in enumerate(nilpotents())), s.zeros(4*comb(3, degree+1), 4*comb(3, degree)))


def center_h(degree):
    out = s.zeros(4*comb(3, degree))
    if degree < 3:
        t = center_t(degree)
        out += t.H*t
    if degree > 0:
        t = center_t(degree-1)
        out += t*t.H
    return out
