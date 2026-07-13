"""B579 — the July-14 session handoff: the two locks.

  (1) the theta-odd dimension sequence at E6 levels 1-4 is {1, 3, 8, 17}
      (integrable counts 3, 9, 20, 42) — the handoff's corrected sequence holds;
  (2) T(F) (the rung-1 escalator 4x4): det = -1 (GL(4,Z)), hyperbolic, and its
      char poly is x^4 - 2x^3 - 5x^2 - 4x - 1 — the BANKED rung-1 tower quartic,
      NOT the handoff's x^4-6x^3-7x^2+8x-1.
See frontier/B579_session_handoff/FINDINGS.md.
"""
from itertools import product

import sympy as sp


def test_theta_odd_dimension_sequence():
    marks = [1, 2, 2, 3, 2, 1]
    theta = lambda w: (w[5], w[1], w[4], w[3], w[2], w[0])
    expected = {1: (3, 1), 2: (9, 3), 3: (20, 8), 4: (42, 17)}
    for k, (n_int, n_odd) in expected.items():
        lev = [w for w in product(range(k + 1), repeat=6)
               if sum(n * a for n, a in zip(w, marks)) <= k]
        assert len(lev) == n_int
        assert sum(1 for w in lev if theta(w) > w) == n_odd


def test_tf_quartic_is_the_banked_tower_quartic():
    F = sp.Matrix([[1, 1], [1, 0]])
    T = sp.Matrix(sp.BlockMatrix([[F, F], [F**2, F]]))
    assert T.det() == -1                                   # GL(4,Z), not SL(4,Z)
    x = sp.Symbol('x')
    cp = sp.expand(T.charpoly(x).as_expr())
    assert cp == x**4 - 2 * x**3 - 5 * x**2 - 4 * x - 1     # the banked rung-1 quartic
    assert cp != x**4 - 6 * x**3 - 7 * x**2 + 8 * x - 1     # the handoff's (wrong)
    evs = [complex(e) for e in T.eigenvals()]
    assert all(abs(abs(z) - 1) > 1e-9 for z in evs)         # hyperbolic
