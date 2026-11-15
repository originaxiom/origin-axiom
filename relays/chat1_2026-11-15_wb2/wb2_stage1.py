#!/usr/bin/env python3
"""W-B2, stage 1: where frame D1's Higgs twist can enter, tested by covariance under tau -> tau + 1 only. Data-free (the
author's ruling of 2026-11-15); no mixing is computed.

    python3 -I -u wb2_stage1.py

The kernel: this seat's transcription of B1656's bilinear (W-F22's wf22_outputs.py: thc, th1), re-typed here with one
change, a shift h of the Szegoe denominators: th1(u, t) -> th1(u + h, t), th1(u + t, t) -> th1(u + h + t, t), and den's
exp(-i pi u) th1(u, t) -> exp(-i pi (u + h)) th1(u + h, t). Its residues are taken around u0 = -h (radius 0.01, 256
nodes). With h = 0 it is frame C's kernel. Channels: pairs() as in the transcription, the residue matrix weighted by unit
weights (u_s = R_s; the norms do not enter). Coupling: the transcription's coupling(S, weighted_M(R)).
The triplet: R = (-th2/(th3 th4), -th4/(th2 th3), i th3/(th2 th4)), th2 = th[1/2 + ta, tb](0, tau), th3 = th[ta, tb](0, tau),
th4 = th[ta, 1/2 + tb](0, tau) (B1947's R_tw with its '+' representative), (ta, tb) = (q_H a, q_H b) when twisted (B1947's
amendment A1), (0, 0) for frame C; S's components = D R = (1/2 pi i) dR/dtau + E2 R / 24 (central difference, step 1e-6).
Readings: S = sum_k c_k Q_k and St = eps conj(S) eps^T.
q_H = -(q_L + q_R) in 6Y: up +3, down -3, leptons -3 (frame C's SIXY: Q 1, u -4, d 2, L -3, e 6).
The point: w = a tau + b; under tau -> tau + 1 the line moves (a, b) -> (a, b - a), so w as a complex number is unchanged
and h = c q_H w is unchanged too.

CANDIDATES: K0 frame C; K1 B1947's twisted triplet, kernel untwisted; K2(c) kernel shifted by h = c q_H w,
c in {+1, -1, +2, -2}, triplet untwisted; K3(c) K2(c) with K1's triplet.
TEST: the coupling's ratios s2/s1, s3/s1 at (tau, (a, b)) against (tau + 1, (a, b - a)), every sector, points (2/5, 4/5),
(1/5, 2/5), (0, 3/5), (3/5, 1/5), moduli 0.13 + 1.7i, -0.31 + 1.25i, 0.4 + 1.2i; the largest relative deviation.

EXPECTATIONS (card W-B2, committed with this script before any of its output):
  V0  K0 is covariant (largest deviation below 1e-8) in S and in St.
  V1  K1 is not covariant (some deviation above 1e-3) in S and in St.
  V2  (a hypothesis) for at least one c, K2(c) is covariant in every sector (in S, or in St, or both).
  V3  K3 reported.
  Plant: K0 with the line not moved ((a, b) kept at tau + 1) has some deviation above 1e-3.
"""
import math
import os
from fractions import Fraction as Fr

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(os.path.dirname(HERE), "chat1_2026-11-14_wf22", "wf22_outputs.py")
_s = open(SRC).read()
NS = {"__file__": SRC}
exec(_s[:_s.index("def dev(x, y):")], NS)
thc, th1 = NS["thc"], NS["th1"]
QI, QJ, QK, EPS, UNITS = NS["QI"], NS["QJ"], NS["QK"], NS["EPS"], NS["UNITS"]
SIXY = {"Q": 1, "u": -4, "d": 2, "L": -3, "e": 6}
SECT = {"up": ("Q", "u"), "down": ("Q", "d"), "lep": ("L", "e")}
QH = {s: -(SIXY[l] + SIXY[r]) for s, (l, r) in SECT.items()}
assert QH == {"up": 3, "down": -3, "lep": -3}


def say(*a):
    print(*a, flush=True)


def twist_of(w, t):
    a = w.imag / t.imag
    return (a, 2 * (w.real - a * t.real))


def bil_h(x, y, u, t, h):
    (ax, bx), (ay, by) = x, y
    T = 2 * t
    v = u + h
    t1 = th1(v, t)
    den = 1j * np.exp(-1j * np.pi * t / 2) * np.exp(-1j * np.pi * v) * t1
    X0, X1, Y0, Y1 = thc(ax, bx, u, T), thc(ax, bx, u + t, T), thc(ay, by, u, T), thc(ay, by, u + t, T)
    return np.array([[X0 * Y0 / t1, np.exp(1j * np.pi * by) * X0 * Y1 / den],
                     [np.exp(1j * np.pi * bx) * X1 * Y0 / den, np.exp(1j * np.pi * (bx + by)) * X1 * Y1 / th1(v + t, t)]])


def residues_h(x, y, t, h, rad=0.01, N=256):
    d = rad * np.exp(2j * np.pi * np.arange(N) / N)
    M = bil_h(x, y, -h + d, t, h)
    return {s: complex(np.mean(np.einsum('mn,mn...->...', EPS @ C, M) * d)) for s, C in UNITS.items()}


def theta(a, b, t):
    return complex(thc(a, b, 0.0, t))


def R_tw(t, ta, tb):
    t2, t3, t4 = theta(0.5 + ta, tb, t), theta(ta, tb, t), theta(ta, 0.5 + tb, t)
    return np.array([-t2 / (t3 * t4), -t4 / (t2 * t3), 1j * t3 / (t2 * t4)])


def E2(t):
    q = np.exp(2j * np.pi * t)
    n = np.arange(1, 400)
    return 1 - 24 * np.sum(n * q ** n / (1 - q ** n))


def comps(t, ta, tb, st=1e-6):
    dR = (R_tw(t + st, ta, tb) - R_tw(t - st, ta, tb)) / (2 * st) / (2j * np.pi)
    return dR + E2(t) * R_tw(t, ta, tb) / 24


def ratios(t, a, b, sec, kernel_c, twist_triplet, reading):
    w = float(a) * t + float(b)
    lf, rf = SECT[sec]
    x, y = twist_of(SIXY[lf] * w, t), twist_of(SIXY[rf] * w, t)
    h = kernel_c * QH[sec] * w
    R = residues_h(x, y, t, h)
    Mw = NS["weighted_M"](R)
    ta, tb = (QH[sec] * float(a), QH[sec] * float(b)) if twist_triplet else (0.0, 0.0)
    c = comps(t, ta, tb)
    S = c[0] * QI + c[1] * QJ + c[2] * QK
    if reading == "St":
        S = EPS @ np.conj(S) @ EPS.T
    sv = np.linalg.svd(NS["coupling"](S, Mw), compute_uv=False)
    return np.array([sv[1] / sv[0], sv[2] / sv[0]])


POINTS = [(Fr(2, 5), Fr(4, 5)), (Fr(1, 5), Fr(2, 5)), (Fr(0), Fr(3, 5)), (Fr(3, 5), Fr(1, 5))]
TAUS = [complex(0.13, 1.7), complex(-0.31, 1.25), complex(0.4, 1.2)]


def worst(kernel_c, twist_triplet, reading, move=True, secs=("up", "down", "lep")):
    out = {}
    for sec in secs:
        wv = 0.0
        for a, b in POINTS:
            for t in TAUS:
                r0 = ratios(t, a, b, sec, kernel_c, twist_triplet, reading)
                b1 = (b - a) % 1 if move else b
                r1 = ratios(t + 1, a, b1, sec, kernel_c, twist_triplet, reading)
                wv = max(wv, float(np.max(np.abs(r1 - r0) / np.abs(r0))))
        out[sec] = wv
    return out


def fmt(d):
    return "  ".join("%s %.1e" % (k, v) for k, v in d.items())


def main():
    res = {}
    for rd in ("S", "St"):
        res[("K0", rd)] = worst(0, False, rd)
        res[("K1", rd)] = worst(0, True, rd)
        for c in (1, -1, 2, -2):
            res[("K2(%+d)" % c, rd)] = worst(c, False, rd)
            res[("K3(%+d)" % c, rd)] = worst(c, True, rd)
    for (k, rd), d in res.items():
        say("%-7s %-2s  %s" % (k, rd, fmt(d)))
    v0 = all(max(res[("K0", rd)].values()) < 1e-8 for rd in ("S", "St"))
    v1 = all(max(res[("K1", rd)].values()) > 1e-3 for rd in ("S", "St"))
    v2 = [c for c in (1, -1, 2, -2) if any(max(res[("K2(%+d)" % c, rd)].values()) < 1e-8 for rd in ("S", "St"))]
    v3 = [(c, rd) for c in (1, -1, 2, -2) for rd in ("S", "St") if max(res[("K3(%+d)" % c, rd)].values()) < 1e-8]
    plant = max(worst(0, False, "S", move=False, secs=("up",)).values()) > 1e-3
    say("V0 holds:", v0, "| V1 holds:", v1, "| V2 holds:", bool(v2), "(covariant K2 choices: %s)" % v2,
        "| V3 covariant K3 choices:", v3, "| plant (the line not moved) fails:", plant)


if __name__ == "__main__":
    main()
