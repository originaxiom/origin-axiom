#!/usr/bin/env python3
"""Failing control for Card A2-PEER-SM-R612 (100% self-contained, exits 1 with 0 stderr bytes under python3 -I).

Plants the unshifted T-law violation (tau -> tau + 1 without shifting b -> b - a) at delta = inf
on line (1/10, 3/10), verifying that the independent Frame A theta-kernel evaluation catches it cleanly.
"""
import math
import sys
from fractions import Fraction as Fr

import numpy as np

I_UNIT = complex(0, 1)
PI = math.pi
TWO_PI = 2 * PI
HALF = 1 / 2
QI = np.array([[I_UNIT, 0], [0, -I_UNIT]], dtype=complex)
QJ = np.array([[0, 1], [-1, 0]], dtype=complex)
QK = QI @ QJ
EPS = QJ.copy()
UNIT_KEYS = ("1", "i", "j", "k")
UNITS = {"1": np.eye(2, dtype=complex), "i": QI, "j": QJ, "k": QK}
EC = {s: (EPS @ UNITS[s]) for s in UNIT_KEYS}
BLOCKS = [QJ, QI, QK]
_G = np.array([[np.sum(EC[t] * UNITS[s]) for s in UNIT_KEYS] for t in UNIT_KEYS], dtype=complex)
_GI = np.linalg.inv(_G)
EDUAL = {UNIT_KEYS[a]: sum(_GI[b, a] * UNITS[UNIT_KEYS[b]] for b in range(4)) for a in range(4)}

NK = 24
_N = np.arange(-NK, NK + 1, dtype=float)
_K = np.arange(-NK, NK + 1, dtype=float)
_H = _K + HALF
_SGN = np.where((np.arange(-NK, NK + 1) % 2) == 0, 1, -1)


def _thc(a, b, u, T):
    n = _N + a
    u = np.asarray(u, dtype=complex)[..., None]
    return np.sum(np.exp(I_UNIT * PI * T * (n * n) + I_UNIT * TWO_PI * n * (u + b)), axis=-1)


def _th1(u, t):
    u = np.asarray(u, dtype=complex)[..., None]
    return -I_UNIT * np.sum(_SGN * np.exp(I_UNIT * PI * t * (_H * _H) + I_UNIT * PI * (2 * _K + 1) * u), axis=-1)


def _residues(w, t, ql, qr):
    def tw(z):
        a = z.imag / t.imag
        return (a, 2 * (z.real - a * t.real))
    (ax, bx), (ay, by) = tw(ql * w), tw(qr * w)
    rad = 1 / 100
    u = rad * np.exp(I_UNIT * TWO_PI * np.arange(128) / 128)
    T = 2 * t
    t1 = _th1(u, t)
    den = I_UNIT * np.exp(-I_UNIT * PI * t / 2) * np.exp(-I_UNIT * PI * u) * t1
    X0, X1 = _thc(ax, bx, u, T), _thc(ax, bx, u + t, T)
    Y0, Y1 = _thc(ay, by, u, T), _thc(ay, by, u + t, T)
    m00 = X0 * Y0 / t1
    m01 = np.exp(I_UNIT * PI * by) * X0 * Y1 / den
    m10 = np.exp(I_UNIT * PI * bx) * X1 * Y0 / den
    m11 = np.exp(I_UNIT * PI * (bx + by)) * X1 * Y1 / _th1(u + t, t)
    out = {}
    for s in UNIT_KEYS:
        C = EC[s]
        p = C[0, 0] * m00 + C[0, 1] * m01 + C[1, 0] * m10 + C[1, 1] * m11
        out[s] = complex(np.mean(p * u))
    return out


def _dr_vec(tau):
    # Branch-free Halphen-Serre closed form for DR(tau)
    n = np.arange(0, 24)
    m = np.arange(1, 24)
    t2 = 2 * np.exp(I_UNIT * PI * tau / 4) * np.sum(np.exp(I_UNIT * PI * tau * n * (n + 1)))
    t3 = 1 + 2 * np.sum(np.exp(I_UNIT * PI * tau * m * m))
    t4 = 1 + 2 * np.sum(((-1) ** m) * np.exp(I_UNIT * PI * tau * m * m))
    eta = np.exp(I_UNIT * PI * tau / 12) * np.prod(1 - np.exp(I_UNIT * TWO_PI * tau * m))
    den = 24 * (eta ** 3)
    return np.array([-(t2 ** 2) * (t3 ** 4 + t4 ** 4) / den,
                     (t4 ** 2) * (t2 ** 4 + t3 ** 4) / den,
                     I_UNIT * (t3 ** 2) * (t2 ** 4 - t4 ** 4) / den], dtype=complex)


def _down_ln_r23(tau, a_fr, b_fr):
    w = (a_fr.numerator / a_fr.denominator) * tau + (b_fr.numerator / b_fr.denominator)
    R = _residues(w, tau, 1, 2)
    u = {s: (R[s] if abs(R[s]) > 10 ** (-12) else 0) for s in UNIT_KEYS}
    Mw = sum(u[s] * EDUAL[s] for s in UNIT_KEYS)
    av = _dr_vec(tau)
    S = av[0] * QI + av[1] * QJ + av[2] * QK
    Y = np.array([[np.sum((Ca.T @ EPS @ S @ Cb) * Mw) for Cb in BLOCKS] for Ca in BLOCKS], dtype=complex)
    sv = np.linalg.svd(Y, compute_uv=False)
    return math.log(float(sv[1] / sv[0]))


def main():
    tau = complex(21 / 100, 297 / 100)
    a, b = Fr(1, 10), Fr(3, 10)
    v_src = _down_ln_r23(tau, a, b)
    # Planted fault: omit b -> b - a under T: tau -> tau + 1
    v_bad = _down_ln_r23(tau + 1, a, b)
    diff = abs(v_src - v_bad)
    ok = diff < 10 ** (-10)
    print(f"CONTROL_FAIL: planted_unshifted_T_violates_PL5 diff={diff:.6g} ok={ok}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
