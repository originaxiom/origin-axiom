"""Locks for B554 — the seven-station meditation verification."""
import numpy as np
import sympy as sp

SUB = {'a': 'abAAB', 'b': 'aAB', 'A': 'abAB', 'B': 'aA'}


def _word(n=60000):
    w = 'a'
    while len(w) < n:
        w = ''.join(SUB[c] for c in w)
    return w[:n]


def test_station4_species_not_forward_bitpair():
    """REFUTED: struct/tunnel != successor old/new bit; forward bigram ambiguous."""
    w = _word()
    shadow = w.translate(str.maketrans({'a': '0', 'b': '0', 'A': '1', 'B': '1'}))
    st = w.translate(str.maketrans({'a': '0', 'A': '0', 'b': '1', 'B': '1'}))
    # struct/tunnel = successor bit? massively fails
    defects = sum(1 for i in range(len(w)-1) if st[i] != shadow[i+1])
    assert defects > 0.5 * (len(w)-1)          # >50% mismatch -> refuted
    # forward bigram not single-valued
    from collections import defaultdict
    fmap = defaultdict(set)
    for i in range(len(w)-1):
        fmap[(shadow[i], shadow[i+1])].add(w[i])
    assert not all(len(v) == 1 for v in fmap.values())   # ambiguous -> not bit-pairs
    assert fmap[('0', '1')] == {'a', 'b'}                 # the ambiguous cases
    assert fmap[('1', '0')] == {'A', 'B'}


def test_station1_gap_labels_are_degree4():
    """Gap labels = dictionary = degree-4 (tau), NOT degree-2 (phi)."""
    t = sp.Symbol('t')
    f_a = sp.sqrt((1 + sp.sqrt(5)) / 2) - 1
    assert sp.degree(sp.minimal_polynomial(f_a, t)) == 4


def test_station5_disc_is_2_and_5_only():
    t = sp.Symbol('t')
    d = sp.discriminant(t**4 - t**2 - 1, t)
    assert d == -400
    assert set(sp.factorint(400).keys()) == {2, 5}


def test_station6_7_grounding():
    """B551 boundary + B545 elliptic-lock are the grounded readings (smoke)."""
    # old/new complexity is non-Sturmian (B551) -> inflation, not winding
    w = _word()
    on = w.translate(str.maketrans({'a': 'x', 'b': 'x', 'A': 'y', 'B': 'y'}))
    comp = [len(set(on[i:i+n] for i in range(len(on)-n))) for n in range(1, 4)]
    assert comp == [2, 4, 7]
