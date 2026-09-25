"""F05 exact operator and central-twist controls; no global eigenvalue fit."""
from functools import lru_cache
from itertools import combinations, product
from math import comb

import sympy as s

x, y = s.symbols('x y', real=True)
z = s.symbols('z', positive=True)
COORDS = (x, y, z)


def clean(matrix):
    return matrix.applyfunc(s.simplify)


def algebraic_clean(matrix):
    return matrix.applyfunc(lambda value: s.simplify(s.expand_complex(value)))


def lie(power=3):
    n = power+1
    e = s.zeros(n)
    for j in range(1, n):
        e[j-1, j] = s.sqrt(j*(n-j))
    return e, e.T, s.diag(*(power-2*j for j in range(n)))


def connection():
    e, _, h = lie()
    return (e/z, s.I*e/z, h/(2*z))


def split():
    c = connection()
    return (tuple((matrix-matrix.H)/2 for matrix in c),
            tuple((matrix+matrix.H)/2 for matrix in c))


@lru_cache(None)
def gamma():
    metric = s.eye(3)/z**2
    inverse = metric.inv()
    return [[[s.simplify(sum(inverse[k, l]*(s.diff(metric[l, j], COORDS[i])
                    +s.diff(metric[l, i], COORDS[j])-s.diff(metric[i, j], COORDS[l]))
                    for l in range(3))/2) for j in range(3)] for i in range(3)] for k in range(3)]


def parallel_residual(omit_connection=False, omit_christoffel=False):
    a, psi = split()
    result = []
    for i, j in product(range(3), repeat=2):
        entry = psi[j].diff(COORDS[i])
        if not omit_connection:
            entry += a[i]*psi[j]-psi[j]*a[i]
        if not omit_christoffel:
            entry -= sum((gamma()[k][i][j]*psi[k] for k in range(3)), s.zeros(4))
        result.append(clean(entry))
    return result


def hermitian_triple(power=3):
    e, f, h = lie(power)
    return ((e+f)/2, s.I*(e-f)/2, h/2)


def wedge(i, degree):
    source = list(combinations(range(3), degree))
    target = list(combinations(range(3), degree+1))
    matrix = s.zeros(len(target), len(source))
    for column, subset in enumerate(source):
        if i not in subset:
            row = target.index(tuple(sorted((i,)+subset)))
            matrix[row, column] = (-1)**sum(j < i for j in subset)
    return matrix


def total_wedges():
    subsets = [subset for p in range(4) for subset in combinations(range(3), p)]
    result = []
    for i in range(3):
        matrix = s.zeros(8)
        for column, subset in enumerate(subsets):
            if i not in subset:
                row = subsets.index(tuple(sorted((i,)+subset)))
                matrix[row, column] = (-1)**sum(j < i for j in subset)
        result.append(matrix)
    return tuple(result)


def t_matrix(degree, power=3, scale=1):
    n = power+1
    return sum((s.kronecker_product(wedge(i, degree), scale*matrix)
                for i, matrix in enumerate(hermitian_triple(power))),
               s.zeros(comb(3, degree+1)*n, comb(3, degree)*n))


@lru_cache(None)
def bochner(degree, power=3, scale=1):
    result = s.zeros(comb(3, degree)*(power+1))
    if degree < 3:
        up = t_matrix(degree, power, scale)
        result += up.H*up
    if degree > 0:
        previous = t_matrix(degree-1, power, scale)
        result += previous*previous.H
    return clean(result)


def block_bochner(degree):
    triple = hermitian_triple()
    casimir = sum((matrix*matrix for matrix in triple), s.zeros(4))
    result = s.kronecker_product(s.eye(comb(3, degree)), casimir)
    if degree:
        for i, j in product(range(3), repeat=2):
            result += s.kronecker_product(wedge(i, degree-1)*wedge(j, degree-1).T,
                                         triple[i]*triple[j]-triple[j]*triple[i])
    return clean(result)


def geometric_matrices():
    omega = (-1+s.I*s.sqrt(3))/2
    return s.Matrix([[1-omega, 1], [-1, 0]]), s.Matrix([[0, -1], [1, -2*omega]])


def symmetric_cube(matrix):
    a, b, c, d = list(matrix)
    xx, yy = s.symbols('xx yy')
    out = s.zeros(4)
    for j in range(4):
        polynomial = s.Poly(s.expand((a*xx+c*yy)**(3-j)*(b*xx+d*yy)**j), xx, yy)
        for i in range(4):
            out[i, j] = polynomial.coeff_monomial(xx**(3-i)*yy**i)
    basis = s.diag(1, s.sqrt(3), s.sqrt(3), 1)
    return algebraic_clean(basis.inv()*out*basis)


@lru_cache(None)
def twisted_matrices(phase=s.I):
    a, b = geometric_matrices()
    return symmetric_cube(a), phase*symmetric_cube(b)


def word(text, generators):
    a, b = generators
    letters = {'a': a, 'b': b, 'A': a.inv(), 'B': b.inv()}
    result = s.eye(a.rows)
    for letter in text:
        result = algebraic_clean(result*letters[letter])
    return result


def character(text, phase=s.I):
    return s.simplify(phase**sum((letter == 'b')-(letter == 'B') for letter in text))


def invariant_j():
    matrix = s.zeros(4)
    for i in range(4):
        matrix[i, 3-i] = (-1)**i
    return matrix


def exterior_lie(matrix):
    pairs = list(combinations(range(4), 2))
    out = s.zeros(6)
    for column, (i, j) in enumerate(pairs):
        for k in range(4):
            for a, b, coefficient in ((k, j, matrix[k, i]), (i, k, matrix[k, j])):
                if a != b:
                    row = pairs.index(tuple(sorted((a, b))))
                    out[row, column] += (1 if a < b else -1)*coefficient
    return out


def exterior_group(matrix):
    pairs = list(combinations(range(4), 2))
    return s.Matrix(6, 6, lambda row, column: matrix.extract(pairs[row], pairs[column]).det())


def e8_roots():
    roots = set()
    for i, j in combinations(range(8), 2):
        for a, b in product((-1, 1), repeat=2):
            root = [s.Integer(0)]*8
            root[i], root[j] = s.Integer(a), s.Integer(b)
            roots.add(tuple(root))
    for signs in product((-1, 1), repeat=8):
        if signs.count(-1) % 2 == 0:
            roots.add(tuple(s.Rational(sign, 2) for sign in signs))
    return roots


def center_exponent(root):
    # The fourth SU4 weight is (1,1,-1)/2. Minus that weight exponentiates
    # to i*I4, not to a primitive cube root or an independent extra group.
    cartan = s.Matrix([-s.Rational(1, 2), -s.Rational(1, 2), s.Rational(1, 2)])
    exponent = 4*s.Matrix(root[5:]).dot(cartan)
    assert exponent.is_Integer
    return int(exponent) % 4
