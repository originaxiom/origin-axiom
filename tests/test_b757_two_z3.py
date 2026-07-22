"""Locks for B757 -- the two-Z/3 identity (L108): dissolution facts."""
from itertools import product

import sympy as sp


def test_g_order_three_and_phi3():
    g = sp.Matrix([[0, -1], [1, -1]])
    x = sp.symbols("x")
    assert g**3 == sp.eye(2)
    assert sp.expand(g.charpoly(x).as_expr()) == x**2 + x + 1


def test_deck_matrix_equals_g_mod_4():
    t = sp.symbols("t")
    assert sp.Poly(t**2 - 3 * t + 1, t, modulus=4).as_expr() == sp.Poly(t**2 + t + 1, t, modulus=4).as_expr()
    deck = sp.Matrix([[0, -1], [1, 3]]).applyfunc(lambda v: v % 4)
    g4 = sp.Matrix([[0, -1], [1, -1]]).applyfunc(lambda v: v % 4)
    assert deck == g4


def test_gl2_z4_has_one_order3_class():
    els = [sp.Matrix([[a, b], [c, d]]) for a, b, c, d in product(range(4), repeat=4)
           if (a * d - b * c) % 4 in (1, 3)]
    assert len(els) == 96
    mmul = lambda A, B: (A * B).applyfunc(lambda v: v % 4)
    order3 = [M for M in els if mmul(mmul(M, M), M) == sp.eye(2) and M != sp.eye(2)]
    assert len(order3) == 8
    M0 = order3[0]
    cls = set()
    for P in els:
        det = (P[0, 0] * P[1, 1] - P[0, 1] * P[1, 0]) % 4
        inv_det = 1 if det == 1 else 3
        Padj = sp.Matrix([[P[1, 1], -P[0, 1]], [-P[1, 0], P[0, 0]]])
        Pinv = (inv_det * Padj).applyfunc(lambda v: v % 4)
        cls.add(tuple(mmul(mmul(P, M0), Pinv)))
    assert all(tuple(M) in cls for M in order3)            # ONE class
