"""F07 exact complex/norm controls, not a global gluing solver."""
import sympy as s


def acyclic_complex():
    d = s.zeros(4)
    d[1, 0] = 1
    d[3, 2] = 1
    return d


def metric():
    return s.diag(s.Matrix([[9]]), s.Matrix([[2, 1+s.I], [1-s.I, 3]]), s.Matrix([[s.Rational(1, 4)]]))


def adjoint(operator, gram):
    return gram.inv()*operator.H*gram


def laplacian(d, gram):
    star = adjoint(d, gram)
    return s.simplify(d*star+star*d)


def chain_change(d, t):
    return t.inv()*d*t


def circle_dirac(n, alpha):
    c = s.I*(n+alpha)
    return s.Matrix([[0, -c], [c, 0]])


def form_norm_density(metric, fiber_weight, degree):
    """Diagonal-coordinate norm density for a coordinate wedge in 3D."""
    from itertools import combinations
    inverse = metric.inv()
    return tuple(s.simplify(fiber_weight*s.sqrt(metric.det())*
                           s.prod(inverse[i, i] for i in indices))
                 for indices in combinations(range(3), degree))
