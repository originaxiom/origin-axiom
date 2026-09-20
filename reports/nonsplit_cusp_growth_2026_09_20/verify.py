"""F03 exact controls. No global PDE solver or unrestricted no-go certificate."""
import sympy as s


def flag_matrices():
    u = (1+s.I*s.sqrt(3))/2
    return s.Matrix([[u, 1], [0, 1-u]]), s.Matrix([[-1, u*u], [0, -1]])


def word(text):
    a, b = flag_matrices()
    letters = {'a': a, 'b': b, 'A': a.inv(), 'B': b.inv()}
    out = s.eye(2)
    for c in text:
        out = s.simplify(out*letters[c])
    return out


def radial_residual(B, r, K, dimension=3):
    return s.simplify(s.diff(B, r, 2)-(dimension-1)*s.diff(B, r)-K*s.exp(2*r+2*B))


def comparison_solution(t, kappa, p, initial=0):
    rate = s.sqrt(kappa*p/2)*s.exp(p*initial/2)
    return initial-2*s.log(s.cos(rate*t))/p


def slice_control(x):
    w = 1+s.Rational(3, 5)*s.cos(2*s.pi*x)
    b = -s.log(w)/2
    z = x+s.Rational(3, 10)*s.sin(2*s.pi*x)/s.pi
    return w, b, z
