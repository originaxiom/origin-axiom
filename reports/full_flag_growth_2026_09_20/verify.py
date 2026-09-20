"""F04 exact identities, not a global PDE solver or a physical index producer."""
from functools import lru_cache

import sympy as s


def clean(matrix):
    return matrix.applyfunc(lambda x: s.simplify(s.expand_complex(x)))


def sym3(matrix):
    x, y = s.symbols('x y')
    a, b, c, d = list(matrix)
    columns = []
    for j in range(4):
        polynomial = s.Poly(s.expand((a*x+c*y)**(3-j)*(b*x+d*y)**j), x, y)
        columns.append(s.Matrix([
            polynomial.coeff_monomial(x**(3-i)*y**i) for i in range(4)
        ]))
    return clean(s.Matrix.hstack(*columns))


@lru_cache(maxsize=1)
def generators():
    u = (1+s.I*s.sqrt(3))/2
    a = s.Matrix([[u, 1], [0, 1-u]])
    b = s.Matrix([[-1, u*u], [0, -1]])
    basis = s.diag(1, s.sqrt(3), s.sqrt(3), 1)
    return (clean(basis.inv()*(u*sym3(a))*basis),
            clean(basis.inv()*(-sym3(b))*basis))


def word(text):
    a, b = generators()
    letters = {'a': a, 'b': b, 'A': a.inv(), 'B': b.inv()}
    out = s.eye(4)
    for letter in text:
        out = clean(out*letters[letter])
    return out


def jordan_generator():
    matrix = s.zeros(4)
    for i, coefficient in enumerate((s.sqrt(3), s.Integer(2), s.sqrt(3))):
        matrix[i, i+1] = coefficient
    return matrix


def nil_exp(matrix):
    """Caller checks nilpotence of order <=4; no spectral approximation."""
    return s.eye(4)+matrix+matrix**2/2+matrix**3/6


def generic_cholesky_data():
    n = s.Matrix([[1, 1+s.I, s.Rational(1, 2), -s.I],
                  [0, 1, 2, 1-s.I], [0, 0, 1, 3*s.I], [0, 0, 0, 1]])
    dn = s.Matrix([[0, 2, s.I, 1], [0, 0, 3*s.I, -2],
                   [0, 0, 0, 1-s.I], [0, 0, 0, 0]])
    d = s.diag(2, 3, 5, s.Rational(1, 30))
    dt = s.Matrix([1, -2, 3, -2])
    return n, dn, d, dt


def root_metric(d, dt, theta):
    result = sum(x*x for x in dt)
    for i in range(4):
        for j in range(i+1, 4):
            result += 2*d[i, i]/d[j, j]*theta[i, j]*s.conjugate(theta[i, j])
    return s.simplify(s.expand_complex(result))


def root_potential():
    t = s.symbols('t1:5', real=True)
    roots = {(i, j): s.Symbol(f'R{i+1}{j+1}', nonnegative=True)
             for i in range(4) for j in range(i+1, 4)}
    potential = sum(s.exp(t[i]-t[j])*coefficient
                    for (i, j), coefficient in roots.items())
    return t, roots, potential


def local_cusp_tension(r, k, slope=-1):
    """Full matrix tension conjugated by N^-dagger and N^-1.

    N=exp(-zJ), z=-x1+x2, b=slope*r+log(2/K)/2. The flat torus norm
    of dz is K. This conjugation leaves no residual z dependence.
    """
    b = slope*r+s.log(2/k)/2
    d = s.diag(*(s.exp(weight*b) for weight in (3, 1, -1, -3)))
    j = jordan_generator()
    dr, drr = d.diff(r), d.diff(r, 2)
    hz = -j.T*d-d*j
    hzz = j.T**2*d+2*j.T*d*j+d*j**2
    tension = drr-2*dr+s.exp(2*r)*k*hzz
    tension -= dr*d.inv()*dr+s.exp(2*r)*k*hz*d.inv()*hz
    return tension.applyfunc(s.simplify)
