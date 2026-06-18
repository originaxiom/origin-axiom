"""B177 -- the metabolism test (H3 to the knife; V171). Fast locks.

The decisive facts: the trace-map first integral I is conserved across 'generations' (kappa cannot
starve -> H3 original form dead); the real Sturmian gap converges/freezes as the chain grows (held by
structure not flux -> H3 revised form dead); the trace map is invertible (reversible -> no metabolic
arrow); and a frozen fixed point exists (the active set is the cited horseshoe B163/B165). Verdict:
crystal/horseshoe, not cell -- life relocates external. Full probe in metabolism_test.py.
"""
import numpy as np
from scipy.linalg import eigvalsh_tridiagonal


def T(p):
    x, y, z = p; return np.array([2*x*y - z, x, y])


def Tinv(p):
    xp, yp, zp = p; return np.array([yp, zp, 2*yp*zp - xp])


def I(p):
    x, y, z = p; return x*x + y*y + z*z - 2*x*y*z - 1


def test_kappa_is_conserved_not_starved():
    p = np.array([0.6, 0.7, 0.35]); I0 = I(p); drift = 0.0
    for _ in range(40):
        p = T(p)
        if np.max(np.abs(p)) > 1e6:
            p = np.array([0.6, 0.7, 0.35])
        drift = max(drift, abs(I(p) - I0))
    assert drift < 1e-8                                   # conserved invariant cannot decay under starvation


def test_trace_map_is_reversible():
    q = np.array([0.41, 0.62, 0.23])
    assert np.max(np.abs(Tinv(T(q)) - q)) < 1e-12         # invertible -> no dissipation/arrow


def test_frozen_fixed_point_exists():
    fp = np.array([1.0, 1.0, 1.0])
    assert np.max(np.abs(T(fp) - fp)) < 1e-12             # frozen order is a real state of the dynamics


def test_sturmian_gap_freezes_not_metabolizes():
    phi = (1 + 5**0.5) / 2; alpha = 1/phi; lam = 1.5; theta = 0.137

    def gap(N, target=0.381966):
        n = np.arange(1, N + 1); V = lam * (((n*alpha + theta) % 1.0) >= 1.0 - alpha).astype(float)
        e = np.sort(eigvalsh_tridiagonal(V, np.ones(N - 1)))
        d = np.diff(e); ids = np.arange(1, N) / N
        m = np.abs(ids - target) < 0.004
        return d[m].max() if m.any() else 0.0

    ws = [gap(N) for N in (377, 987, 2584)]
    assert ws[-1] > 0.05                                  # the gap stays open (does not close)
    assert abs(ws[-1] - ws[-2]) < 5e-3                    # it converges/freezes (held by structure, not flux)
