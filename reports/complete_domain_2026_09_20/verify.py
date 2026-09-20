"""Exact F02 controls. No global PDE solve, spectral census or physical fit."""
import sympy as s


def creators(n):
    out = []
    for i in range(n):
        e = s.zeros(2**n)
        for mask in range(2**n):
            if not mask & (1 << i):
                sign = (-1)**((mask & ((1 << i)-1)).bit_count())
                e[mask | (1 << i), mask] = sign
        out.append(e)
    return out


def clifford(n):
    e = creators(n)
    return e, [v.T for v in e], [v-v.T for v in e], [v+v.T for v in e]


def norm_integral(expr, x, lo=-s.oo, hi=s.oo):
    return s.simplify(s.integrate(s.conjugate(expr)*expr, (x, lo, hi)))


def q_line(vector, x, potential):
    c = s.Matrix([[0, -1], [1, 0]])
    h = s.Matrix([[0, 1], [1, 0]])
    return c*vector.diff(x)+potential*h*vector


def cusp_data():
    r, R, S, area = s.symbols('r R S area', positive=True)
    c = s.symbols('c', real=True)
    F = c*s.exp(2*r)
    return {
        'symbols': (r, R, S, area, c),
        'residual': s.simplify(s.diff(F, r, 2)-2*s.diff(F, r)),
        'norm': s.simplify(s.integrate(area*s.exp(-2*r)*s.diff(F, r)**2, (r, S, R))),
    }
