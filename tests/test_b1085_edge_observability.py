"""B1085 lock: the two hands of one cut — bulk-blind, edge 5-vs-6."""
import numpy as np
from math import floor
import pytest

PHI = (1 + 5 ** 0.5) / 2
ALPHA = 2 - PHI

def _bi(n, rho):
    return 1.0 if floor((n + 1) * ALPHA + rho) - floor(n * ALPHA + rho) else 0.0

def _run(diag):
    from scipy.linalg import eigh_tridiagonal
    E, V = eigh_tridiagonal(np.array(diag), np.ones(len(diag) - 1))
    bw = (V[:20, :] ** 2).sum(axis=0)
    return E, bw

@pytest.fixture(scope="module")
def hands():
    N = 987
    right = [_bi(n, ALPHA) for n in range(N)]
    left = [_bi(-n - 1, ALPHA) for n in range(N)]
    return _run(right), _run(left)

def test_bulk_hand_blind(hands):
    (Ea, _), (Eb, _) = hands
    allE = np.sort(np.concatenate([Ea, Eb]))
    ca = np.searchsorted(Ea, allE, side="right")
    cb = np.searchsorted(Eb, allE, side="right")
    assert int(np.max(np.abs(ca - cb))) <= 1

def test_edge_sees_the_hand_5_vs_6(hands):
    (Ea, bwa), (Eb, bwb) = hands
    ea = [e for e, w in zip(Ea, bwa) if w > 0.5]
    eb = [e for e, w in zip(Eb, bwb) if w > 0.5]
    assert (len(ea), len(eb)) == (5, 6)

def test_right_hand_energies(hands):
    (Ea, bwa), _ = hands
    got = sorted(e for e, w in zip(Ea, bwa) if w > 0.5)
    expect = [-1.5305, -0.9160, -0.5039, +0.4704, +2.0303]
    assert all(abs(g - x) < 2e-3 for g, x in zip(got, expect))
