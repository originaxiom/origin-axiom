"""Locks for B543 — species-chain gap labels carry the dictionary (deg-4)."""
import numpy as np
import pytest

scipy = pytest.importorskip("scipy")
from scipy.linalg import eigh_tridiagonal

SUB = {'a': 'abAAB', 'b': 'aAB', 'A': 'abAB', 'B': 'aA'}
PHI = (1 + np.sqrt(5)) / 2
TAU = np.sqrt(PHI)
S = PHI + 1 + PHI*TAU + TAU
F = {'a': PHI/S, 'b': 1/S, 'A': PHI*TAU/S, 'B': TAU/S}


def _labels(coup, N=3000, top=12):
    w = 'a'
    while len(w) < N:
        w = ''.join(SUB[c] for c in w)
    w = w[:N]
    hop = np.array([coup[c] for c in w[:-1]])
    ev = eigh_tridiagonal(np.zeros(N), hop, eigvals_only=True)
    gaps = np.diff(ev)
    idx = np.argsort(gaps)[::-1][:top]
    out = []
    for i in idx:
        ids = (i + 1) / N
        out.append(min(ids, 1 - ids))
    return out


def test_dictionary_values_are_gap_labels():
    labels = _labels({'a': 1.0, 'b': 0.8, 'A': 0.6, 'B': 0.4})
    for name, val in [('A', F['A']), ('a', F['a']),
                      ('ab', F['a'] + F['b']), ('B', F['B'])]:
        assert min(abs(l - val) for l in labels) < 3e-4, name


def test_labels_are_degree_4():
    """The f_A and f_a labels sit far off the golden lattice Z+Z/phi."""
    labels = _labels({'a': 1.0, 'b': 0.8, 'A': 0.6, 'B': 0.4})
    for val in (F['A'], F['a']):
        lab = min(labels, key=lambda l: abs(l - val))
        d_gold = min(abs((P + Q/PHI) % 1 - lab)
                     for P in range(-6, 7) for Q in range(-6, 7))
        assert d_gold > 1e-2, f"label {lab} too close to golden lattice"


def test_coupling_invariance():
    l1 = _labels({'a': 1.0, 'b': 0.8, 'A': 0.6, 'B': 0.4})
    l2 = _labels({'a': 1.0, 'b': 0.55, 'A': 0.75, 'B': 0.35})
    for val in (F['A'], F['a'], F['a'] + F['b']):
        assert min(abs(l - val) for l in l1) < 3e-4
        assert min(abs(l - val) for l in l2) < 3e-4
