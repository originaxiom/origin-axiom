"""Tests for B61: SL(5) via stable high-precision SVD pinv.

Fast checks only: the stable SVD-pinv property, the matrix exponential, and the
SL(3) high-precision validation (the credibility anchor).  The full SL(4)
regression (~30s) and the SL(5) 22/24 resolution (~100s) are exercised by the
probe's __main__, not the unit suite.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import mpmath as mp


ROOT = Path(__file__).resolve().parents[1]
PROBE_PATH = ROOT / "frontier" / "B61_sl5_high_precision" / "probe.py"


def load_probe():
    spec = importlib.util.spec_from_file_location("b61_sl5_high_precision", PROBE_PATH)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_svd_pinv_stable_on_illconditioned_complex():
    """SVD-pinv loses only ~log10(cond) digits, not 2*log10(cond) (normal eqns)."""
    probe = load_probe()
    mp.mp.dps = 50
    # 6x4 tall complex matrix with EXACT singular values spanning cond=1e12
    base = mp.matrix([[mp.mpc(mp.cos(i + 2 * j), mp.sin(2 * i - j)) for j in range(4)]
                      for i in range(6)])
    U, _, V = mp.svd(base)
    A = mp.zeros(6, 4)
    for k in range(4):
        for i in range(6):
            for j in range(4):
                A[i, j] += U[i, k] * (mp.mpf(10) ** (-4 * k)) * V[k, j]  # sv 1..1e-12
    P = probe.svd_pinv(A)
    PA = P * A  # -> I_4
    err = max(abs(PA[i, j] - (1 if i == j else 0)) for i in range(4) for j in range(4))
    assert err < mp.mpf("1e-30")  # cond 1e12 at dps 50 leaves ~38 digits


def test_svd_pinv_handles_wide_matrix():
    """Our Dx is wide ((n^2-1) x 2(n^2-1)); pinv must go through the tall transpose."""
    probe = load_probe()
    mp.mp.dps = 40
    A = mp.matrix([[mp.mpf(i + 1) / (j + 2) + (1 if i == j else 0) for j in range(8)]
                   for i in range(4)])  # 4x8 wide, full row rank
    P = probe.svd_pinv(A)
    assert P.rows == 8 and P.cols == 4
    AP = A * P  # -> I_4
    err = max(abs(AP[i, j] - (1 if i == j else 0)) for i in range(4) for j in range(4))
    assert err < mp.mpf("1e-30")


def test_expm_mp_matches_scipy():
    probe = load_probe()
    mp.mp.dps = 40
    M = mp.matrix([[mp.mpf("0.3"), mp.mpf("0.5")], [mp.mpf("-0.2"), mp.mpf("0.1")]])
    E = probe.expm_mp(M)
    # cross-check against scipy double precision
    import numpy as np
    from scipy.linalg import expm
    Enp = expm(np.array([[0.3, 0.5], [-0.2, 0.1]]))
    err = max(abs(complex(E[i, j]) - Enp[i, j]) for i in range(2) for j in range(2))
    assert err < 1e-12


def test_sl3_high_precision_reproduces_b55():
    """The method reproduces the SL(3) c=3 factorization to high precision."""
    probe = load_probe()
    epss = ("0.01", "0.02", "0.03", "0.04", "0.05", "0.06")
    spec = probe.fixed_line_spectrum(3, (10,), epss, dps=40, deg=5)
    target = (probe._q(1, 1, -1) + probe._q(1, -3, 1) + probe._q(1, -4, -1)
              + [mp.mpf(1), mp.mpf(-1)])
    worst = probe._max_match(spec, target)
    assert worst < mp.mpf("1e-6")


def test_sl5_word_set_is_rank_24():
    """The inverse-word SL(5) coordinate set is full rank (B60's forward set was 23)."""
    probe = load_probe()
    mp.mp.dps = 40
    assert len(probe.SL5_WORDS) == 24
    P, Q = probe._random_PQ(5, 20)
    eps = mp.mpf("0.05")
    A, B = probe.expm_mp(eps * P), probe.expm_mp(eps * Q)
    h = mp.mpf(10) ** (-14)
    pp, pm = probe._perts(5, h)
    dx = probe._diff_matrix(A, B, 5, False, pp, pm, h)
    # smallest singular value is genuinely nonzero (not the dps floor ~1e-40)
    _, S, _ = mp.svd(dx.H)
    assert S[23] > mp.mpf("1e-10")
