"""Locks for B552 — the Z/11 conserved charge."""
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

SUB = {'a': 'abAAB', 'b': 'aAB', 'A': 'abAB', 'B': 'aA'}
M = sp.Matrix([[SUB[c].count(r) for c in 'abAB'] for r in 'abAB'])


def test_coker_is_z11():
    S = smith_normal_form(sp.eye(4) - M)
    assert [S[i, i] for i in range(4)] == [1, 1, 1, 11]


def test_charge_is_conserved():
    chi = sp.Matrix([[1, 3, 6, 7]])
    assert list((chi * M).applyfunc(lambda v: v % 11)) == list(chi)


def test_images_carry_source_charge():
    Q = {'a': 1, 'b': 3, 'A': 6, 'B': 7}
    for g, img in SUB.items():
        assert sum(Q[c] for c in img) % 11 == Q[g]
