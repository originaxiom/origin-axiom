"""B469 — locks: the two-register breath law and the family Gieseking theorem."""
import os
import sys
from itertools import product

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "frontier", "B469_breath_campaign"))

from br1_br2 import perm_sign_of_map


def test_two_register_breath_law():
    for N in (15, 45, 75):
        pred = (-1) ** ((N - 1) // 2)
        assert perm_sign_of_map(lambda j: (-j) % N, list(range(N))) == pred
        dom = list(product(range(N), repeat=2))
        assert perm_sign_of_map(lambda v: ((v[0] + v[1]) % N, v[0]), dom) == pred


def test_family_gieseking_theorem():
    m = sp.Symbol('m', integer=True)
    X = sp.Matrix([[m, 1], [1, 0]])
    A = sp.Matrix([[m * m + 1, m], [m, 1]])
    assert sp.simplify(X * X - A) == sp.zeros(2, 2)
    assert sp.simplify(X.det()) == -1
