"""Lock for B546 — exact-grade IDS labels (reduced N for CI)."""
import numpy as np
import pytest

scipy = pytest.importorskip("scipy")
from scipy.linalg import eigh_tridiagonal

SUB = {'a': 'abAAB', 'b': 'aAB', 'A': 'abAB', 'B': 'aA'}
PHI = (1 + np.sqrt(5)) / 2
TAU = np.sqrt(PHI)
S = PHI + 1 + PHI*TAU + TAU
F = {'a': PHI/S, 'b': 1/S, 'A': PHI*TAU/S, 'B': TAU/S}


def test_sturm_ids_hits_dictionary_at_2e5():
    N = 200_000
    w = 'a'
    while len(w) < N:
        w = ''.join(SUB[c] for c in w)
    w = w[:N]
    coup = {'a': 1.0, 'b': 0.8, 'A': 0.6, 'B': 0.4}
    hop = np.array([coup[c] for c in w[:-1]])

    def ids(E):
        d = -E
        n = 1 if d < 0 else 0
        for t in hop:
            d = -E - t*t/d
            if d < 0:
                n += 1
        return n / N

    for E, val in [(-0.2396, F['a'] + F['b']), (-0.6300, F['A']),
                   (-0.9155, F['a'])]:
        assert abs(ids(E) - val) < 5e-6
