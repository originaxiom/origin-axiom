"""Locks for B537 — the classical-surface phantom (1,1,5) at c = 22."""
import sympy as sp


def test_level_correction():
    x, y, z = 1, 1, 5
    assert x*x + y*y + z*z - x*y*z == 22
    assert 4*4 + 4*4 + 16*16 - 4*4*16 == 32


def test_elliptic_reductions_exact():
    a, b = sp.symbols('a b', integer=True)
    Q1 = a**2 + a*b + b**2 - a - 5*b + 1
    Q2 = a**2 + a*b + b**2 - 5*a - b + 1
    assert sp.simplify(4*Q1 - ((2*a + b - 1)**2 + 3*(b - 3)**2 - 24)) == 0
    assert sp.simplify(4*Q2 - ((2*a + b - 5)**2 + 3*(b + 1)**2 - 24)) == 0


def test_24_not_represented():
    assert not [(U, V) for V in range(-2, 3) for U in range(-6, 7)
                if U*U + 3*V*V == 24]


def test_mod3_obstruction_trace5_slot():
    a = sp.Symbol('a', integer=True)
    disc = sp.expand((1 - 5*a)**2 + 4*(a*(1 - a) - 1))
    assert sp.simplify(disc - 3*(7*a**2 - 2*a - 1)) == 0
    assert 0 not in {int((7*t*t - 2*t - 1) % 3) for t in range(3)}


def test_derivation_from_detB():
    a, bb, c, d = sp.symbols('a bb c d', integer=True)
    A = sp.Matrix([[1, -1], [1, 0]])
    B = sp.Matrix([[a, bb], [c, d]])
    for (y, z, Qref) in [(1, 5, a**2 + a*bb + bb**2 - a - 5*bb + 1),
                         (5, 1, a**2 + a*bb + bb**2 - 5*a - bb + 1)]:
        d_sol = y - a
        c_sol = sp.solve(sp.Eq((A * B.subs(d, d_sol)).trace(), z), c)[0]
        Q = sp.expand(B.subs([(d, d_sol), (c, c_sol)]).det() - 1)
        assert sp.simplify(Q + Qref) == 0 or sp.simplify(Q - Qref) == 0


def test_markov_sanity_realizable():
    def realizable(x, y, z, bound=100):
        for a in range(-bound, bound + 1):
            dd = (z - x*a)**2 + 4*(a*(y - a) - 1)
            if dd >= 0 and sp.integer_nthroot(dd, 2)[1]:
                return True
        return False
    for tri in [(3, 3, 3), (3, 3, 6), (3, 6, 15)]:
        assert realizable(*tri)
    # and the phantom's companion slots are all empty in a modest window
    for (x, y, z) in [(1, 1, 5), (1, 5, 1), (5, 1, 1)]:
        assert not realizable(x, y, z, 500)
