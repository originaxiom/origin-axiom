"""B1095 lock: the mirror-isospectral split."""
import numpy as np
from math import floor
import pytest

PHI = (1 + 5 ** 0.5) / 2
ALPHA = 2 - PHI

def _bi(n, rho):
    return 1.0 if floor((n + 1) * ALPHA + rho) - floor(n * ALPHA + rho) else 0.0

def _spec(w):
    from scipy.linalg import eigh_tridiagonal
    E, V = eigh_tridiagonal(np.array(w), np.ones(len(w) - 1))
    return E, (V[:20, :] ** 2).sum(axis=0)

def test_reversal_identity_at_987_and_failure_at_1597():
    r987 = [_bi(n, ALPHA) for n in range(987)]
    l987 = [_bi(-n - 1, ALPHA) for n in range(987)]
    assert l987 == r987[::-1]
    r = [_bi(n, ALPHA) for n in range(1597)]
    l = [_bi(-n - 1, ALPHA) for n in range(1597)]
    diffs = [i for i in range(1597) if l[i] != r[::-1][i]]
    assert diffs == [0, 1]

def test_exact_isospectrality_at_987():
    Er, _ = _spec([_bi(n, ALPHA) for n in range(987)])
    El, _ = _spec([_bi(-n - 1, ALPHA) for n in range(987)])
    assert np.max(np.abs(np.sort(Er) - np.sort(El))) < 1e-12

def test_eleven_shared_energies_split_5_6():
    Er, bwr = _spec([_bi(n, ALPHA) for n in range(987)])
    El, bwl = _spec([_bi(-n - 1, ALPHA) for n in range(987)])
    er = sorted(Er[i] for i in range(987) if bwr[i] > 0.5)
    el = sorted(El[i] for i in range(987) if bwl[i] > 0.5)
    assert (len(er), len(el)) == (5, 6)                 # odd family, parity remainder
    Br = np.array([Er[i] for i in range(987) if bwr[i] <= 0.5])
    Bl = np.array([El[i] for i in range(987) if bwl[i] <= 0.5])
    for e in el:
        assert np.min(np.abs(Br - e)) < 1e-10           # left edges live in right bulk
    for e in er:
        assert np.min(np.abs(Bl - e)) < 1e-10           # right edges live in left bulk
