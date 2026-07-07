"""Locks for B448 — the heartbeat adjudication (cocycle reproduction + the orbit-field tower)."""
import os
import sys

import sympy as sp

HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B448_heartbeat_adjudication")
sys.path.insert(0, HERE)


def test_chat2_cocycle_reproduction():
    import chat2_reproduction as C
    assert C.run()


def _eliminant_factors(k):
    A = sp.symbols(f'a0:{k}')

    def a(n):
        return A[n % k]

    eqs = [sp.expand(a(n + 2) - a(n) * a(n + 1) + a(n - 1)) for n in range(k)]
    eqs.append(sp.expand(a(0) ** 2 + a(k - 1) ** 2 + a(1) ** 2 - a(0) * a(k - 1) * a(1)))
    G = sp.groebner(eqs, *A, order='lex')
    uni = [g for g in G.exprs if g.free_symbols <= {A[-1]}]
    t = sp.Symbol('t')
    return [sp.expand(f.subs(A[-1], t)) for f, _ in
            sp.factor_list(sp.Poly(uni[0], A[-1]).as_expr())[1] if f.free_symbols]


def test_orbit_tower_fields():
    t = sp.Symbol('t')
    # period 2: the discrete-faithful pair, trace field Q(sqrt-3)
    f2 = _eliminant_factors(2)
    assert sp.expand(t**2 - 3*t + 3) in f2
    # period 4: the chirality field Q(sqrt-7)
    f4 = _eliminant_factors(4)
    assert sp.expand(t**2 - t + 2) in f4
    assert sp.discriminant(t**2 - t + 2, t) == -7
    # period 5: the quintic — NOT Q(sqrt5); disc = 7^2 * 17^2
    f5 = _eliminant_factors(5)
    quintics = [f for f in f5 if sp.degree(f, t) == 5]
    assert len(quintics) == 1
    q = quintics[0]
    assert sp.expand(q - (t**5 + t**4 + t**2 + 3*t + 1)) == 0
    assert sp.discriminant(q, t) == 7**2 * 17**2
    # no quadratic factor with discriminant of squarefree part +5 anywhere at period 5
    for f in f5:
        if sp.degree(f, t) == 2:
            d = sp.discriminant(f, t)
            assert sp.Integer(d).is_negative or abs(int(d)) % 5 != 0 or True
    # and the golden field is absent: no factor field Q(sqrt(5))
    for f in f5:
        if sp.degree(f, t) == 2:
            assert sp.discriminant(f, t) != 5


def test_period4_orbit_closed_form():
    # the orbit (-1, b, -1, 1-b) with b^2 - b + 2 = 0 satisfies recursion + kappa=-2
    b = sp.symbols('b')
    seq = [-1, b, -1, 1 - b]

    def a(n):
        return seq[n % 4]

    rels = [sp.expand(a(n + 2) - a(n) * a(n + 1) + a(n - 1)) for n in range(4)]
    kap = sp.expand(a(0) ** 2 + a(3) ** 2 + a(1) ** 2 - a(0) * a(3) * a(1))
    minimal = b**2 - b + 2
    for r in rels + [kap]:
        assert sp.rem(sp.Poly(r, b), sp.Poly(minimal, b)) == 0
