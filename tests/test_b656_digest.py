"""B656 — digest-queue integration locks (G1 + G4, independently verified).

G4: the conductor-clock law — clock(kappa) = ord(A1 mod 3*kappa) on the
law rows, with the two anomaly-zone rows locked as anomalies.
G1: the sign-hears-the-discriminant theorem on a Weyl group OUTSIDE the
discovery battery (W(D4)) with a word outside it (t=7's even prime).
See frontier/B656_digest_integration/FINDINGS.md.
"""
import importlib.util
import itertools
import os

import numpy as np

_ROOT = os.path.join(os.path.dirname(__file__), "..")
_spec = importlib.util.spec_from_file_location(
    "b238m9", os.path.join(_ROOT, "frontier", "B238_su32_levelrank", "su32_wrt.py"))
b238 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b238)


def _clock(k, cap=200):
    w, S, T, c = b238.su3_data(k)
    Si, Ti = np.linalg.inv(S), np.linalg.inv(T)
    M = T @ (Si @ Ti @ S)
    prs = [(i, w.index((wt[1], wt[0]))) for i, wt in enumerate(w)
           if (wt[1], wt[0]) > wt]
    odd = np.zeros((len(w), len(prs)))
    for j, (a, b) in enumerate(prs):
        odd[a, j], odd[b, j] = 1 / np.sqrt(2), -1 / np.sqrt(2)
    B = odd.T @ M @ odd
    P = np.eye(len(prs), dtype=complex)
    for m in range(1, cap + 1):
        P = P @ B
        if np.allclose(P, np.eye(len(prs)), atol=1e-8):
            return m
    return None


def _ord(m, cap=100000):
    """Order of A1 = [[2,1],[1,1]] in GL(2, Z/m) — fresh code."""
    idm = (1 % m, 0, 0, 1 % m)
    cur = idm
    for k in range(1, cap + 1):
        cur = ((cur[0] * 2 + cur[1]) % m, (cur[0] + cur[1]) % m,
               (cur[2] * 2 + cur[3]) % m, (cur[2] + cur[3]) % m)
        if cur == idm:
            return k
    return None


def test_g4_conductor_clock_law_rows():
    # law rows (kappa = 6, 7, 11): clock = ord(A1 mod 3*kappa)
    assert _clock(3) == 12 == _ord(18)
    assert _clock(4) == 8 == _ord(21)
    assert _clock(8) == 20 == _ord(33)


def test_g4_anomaly_zone_rows():
    # kappa = 4: order destroyed (clock 1 vs ord 12);
    # kappa = 5: exactly the half-period (clock 10 vs ord 20)
    assert _clock(1) == 1 and _ord(12) == 12
    assert _clock(2) == 10 and _ord(15) == 20


def _wd4():
    out = []
    for perm in itertools.permutations(range(4)):
        for signs in itertools.product((1, -1), repeat=4):
            if signs.count(-1) % 2:
                continue
            M = np.zeros((4, 4), dtype=int)
            for i, j in enumerate(perm):
                M[i, j] = signs[i]
            out.append(M)
    return out


def _agree_count(t, p):
    n = 0
    for w in _wd4():
        Bw = t * np.eye(4, dtype=int) - w - np.linalg.inv(w).astype(int)
        db = abs(int(round(np.linalg.det(Bw.astype(np.float64)))))
        v = 0
        while db % p == 0:
            db //= p
            v += 1
        if int(round(np.linalg.det(w.astype(np.float64)))) == (-1) ** v:
            n += 1
    return n


def test_g1_sign_hears_discriminant_on_wd4():
    # t=5, disc 21 = 3*7: both odd-valuation primes track 192/192
    assert _agree_count(5, 3) == 192
    assert _agree_count(5, 7) == 192
    # t=7, disc 45 = 3^2*5: even v_3 -> exactly half; odd v_5 -> tracks
    assert _agree_count(7, 3) == 96
    assert _agree_count(7, 5) == 192
