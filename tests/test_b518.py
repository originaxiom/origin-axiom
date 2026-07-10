"""B518 locks — confirming K025: universality (A), the prediction (B), the derivation (C)."""
import numpy as np
import sympy as sp
from scipy.linalg import eigh_tridiagonal

x = sp.symbols('x')


def test_A_trace_map_universal():
    E, lam = sp.symbols('E lambda')
    TA = sp.Matrix([[E - lam, -1], [1, 0]]); TB = sp.Matrix([[E + lam, -1], [1, 0]])
    xx, yy, zz = TA.trace(), TB.trace(), (TB*TA).trace()
    assert sp.expand(xx**2 + yy**2 + zz**2 - xx*yy*zz - 2 - 2 - 4*lam**2) == 0  # kappa-2=4lambda^2


def test_C_faces_from_root():
    R = sp.Matrix([[1, 1], [0, 1]]); L = sp.Matrix([[1, 0], [1, 1]])
    sigma = sp.Matrix([[1, 1], [1, 0]])
    assert sigma**2 == R*L                                    # sigma^2 = A = RL
    assert (R*L).trace() == 3                                 # product end -> Q(sqrt5)
    assert (-R*L.inv()).trace() == -1                         # ratio end -> Q(sqrt-3)
    assert sp.discriminant((R*L).charpoly(x).as_expr(), x) == 5
    assert sp.discriminant((-R*L.inv()).charpoly(x).as_expr(), x) == -3


def test_B_mixed_chain_discriminator():
    phi = (1 + 5**0.5)/2
    def fib(w): return ''.join('ab' if c == 'a' else 'a' for c in w)
    def tm(w): return ''.join('ab' if c == 'a' else 'ba' for c in w)
    def build(direc, cap=6000):
        w = 'a'
        for s in direc:
            w = s(w)
            if len(w) > cap: break
        return w[:cap]
    def labs(w, thr=0.03):
        V = np.array([1.0 if c == 'a' else -1.0 for c in w]); N = len(w)
        E = eigh_tridiagonal(V, np.ones(N - 1), eigvals_only=True); g = np.diff(E)
        return [(i + 1)/N for i in range(N - 1) if g[i] > thr]
    def near(L, t): return any(abs(l - t) < 0.01 for l in L)
    Lf = labs(build([fib]*20)); Lt = labs(build([tm]*13))
    Lm = labs(build([fib, fib, tm, fib, fib, fib, tm, fib, fib, tm, fib, fib, fib, fib, tm]))
    assert not near(Lf, 0.5) and near(Lf, phi - 1)      # pure Fib: golden only
    assert near(Lt, 0.5) and not near(Lt, phi - 1)      # pure TM: dyadic only
    assert near(Lm, 0.5) and near(Lm, phi - 1)          # mixed: BOTH
