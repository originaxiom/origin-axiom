"""Locks for B549 — E7 ladder + cosmic-ratio null."""
import numpy as np


def test_e7_ladder_first_ratio():
    C = np.array([
        [2,0,-1,0,0,0,0],[0,2,0,-1,0,0,0],[-1,0,2,-1,0,0,0],
        [0,-1,-1,2,-1,0,0],[0,0,0,-1,2,-1,0],[0,0,0,0,-1,2,-1],
        [0,0,0,0,0,-1,2]])
    w, v = np.linalg.eigh(C)
    m = np.sort(np.abs(v[:, np.argmin(w)]))
    m = m / m[0]
    phi = (1 + np.sqrt(5)) / 2
    assert abs(m[1] - 1.285575) < 1e-5       # E7 first ratio
    assert abs(m[1] - phi) > 0.05            # discriminable from E8


def test_cosmic_ratios_null():
    TAU = np.sqrt((1 + np.sqrt(5)) / 2)
    T = np.array([1, TAU, TAU**2, TAU**3])
    r = np.arange(-8, 9, dtype=float)
    N = len(r)
    lat = np.sort((r.reshape(N,1,1,1)*T[0] + r.reshape(1,N,1,1)*T[1]
                 + r.reshape(1,1,N,1)*T[2] + r.reshape(1,1,1,N)*T[3]).ravel())
    def be(v):
        i = np.searchsorted(lat, v)
        return min(abs(lat[j]-v) for j in (i-1, i) if 0 <= j < len(lat))
    # both time-independent cosmic constants miss Z[tau] at >1e-5 (no exact hit)
    assert be(5.3643) > 1e-5
    assert be(6.12) > 1e-5
