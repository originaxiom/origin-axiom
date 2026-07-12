"""Locks for B542 — the dictionary as two tau-ladders (exact)."""
import sympy as sp

t = sp.Symbol('t')
MIN = t**4 - t**2 - 1


def red(e):
    return sp.rem(sp.expand(e), MIN, t)


def inv(e):
    s, _, h = sp.gcdex(sp.Poly(red(e), t, domain='QQ'),
                       sp.Poly(MIN, t, domain='QQ'))
    return red(s.as_expr() / h.as_expr())


COMPS = [(0,-1,1,0),(-1,1,0,0),(1,1,0,-1),(1,-1,-1,1),(0,0,-1,1),(1,-2,1,0),
         (-1,3,1,-2),(0,-3,0,2),(2,-1,1,-1),(-2,2,-4,3),(2,-2,3,-2),
         (-2,1,-2,2),(1,0,2,-2),
         (sp.Rational(1,2),sp.Rational(1,2),-sp.Rational(1,2),0),
         (sp.Rational(1,2),-1,0,sp.Rational(1,2)),
         (1,-sp.Rational(1,2),sp.Rational(1,2),-sp.Rational(1,2)),(0,1,-2,1)]
PI = -2*t**3 + t**2 + 3*t - 1


def _ex(c):
    return red(sum(ci*t**k for k, ci in enumerate(c)))


def test_b1_ladder_is_freqs_and_lambda2():
    """tau^a (tau-1), a=-2..2 are exactly {f_b, f_B, f_a, f_A, |lambda2|}."""
    lad = []
    for a in range(-2, 3):
        ta = red(t**a) if a >= 0 else inv(t**(-a))
        lad.append(red(ta * (t - 1)))
    targets = [_ex(c) for c in [(1,-1,-1,1),(1,1,0,-1),(-1,1,0,0),
                                (0,-1,1,0),(0,0,-1,1)]]
    for L, T in zip(lad, targets):
        assert red(L - T) == 0


def test_b2_ladder_is_t4_t6_components():
    """tau^a (tau-1)^2, a=0..5 are the six T4/T6 components."""
    targets = [_ex(c) for c in [(1,-2,1,0),(0,1,-2,1),(1,0,2,-2),
                                (-2,1,-2,2),(2,-2,3,-2),(-2,2,-4,3)]]
    for a, T in enumerate(targets):
        assert red(red(t**a * (t-1)**2) - T) == 0


def test_t3_component_is_pi():
    assert red(_ex((-1,3,1,-2)) - red(PI)) == 0


def test_tau_minus5():
    assert red(_ex((0,-3,0,2)) - inv(t**5)) == 0


def test_all_17_decompose():
    """Every component is +- tau^a (tau-1)^b pi^{-1,0,1}."""
    pi_r, pi_i = red(PI), inv(red(PI))
    for c in COMPS:
        e = _ex(c)
        ok = False
        for pe in (1, pi_r, pi_i):
            for b in range(0, 3):
                for a in range(-6, 7):
                    ta = red(t**a) if a >= 0 else inv(t**(-a))
                    if red(e - red(ta * (t-1)**b * pe)) == 0:
                        ok = True
                        break
                if ok:
                    break
            if ok:
                break
        assert ok, c
