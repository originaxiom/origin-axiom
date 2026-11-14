#!/usr/bin/env python3
"""W-F22, the output-level half (the author's approval, 2026-11-14, evening): is the frame periodic along the golden
thread, reading by reading? This seat's own implementation of B1656's frame (the formulas of B1723's b1656_funcs.py,
re-typed, not imported) with this seat's own triplet (wf22_checks.py's theta series and Serre derivative). Only
DEVIATIONS are printed (B1724's compare: the largest |log ratio| over a reading's outputs, CKM pairs included); no output
of the frame is printed or kept.

    python3 -I -u wf22_outputs.py

THE TEST (B1922's): the frame at (tau, line (a, b), end L) against the frame at (g tau, the same line, end transported),
with g = gamma = [[2, 1], [1, 1]] (L -> L + log|tau + 1|) or g = gamma^3 (the shift summed over the three steps). The
end is B1922's: L_max = 1.3, L_2 = 0.9 at tau. Base points on the thread tau = z(s) = (phi i e^s - 1/phi) / (i e^s + 1)
(B1922's zt), gamma z(s) = z(s + l), l = 2 log(phi^2). Readings: S, St = eps conj(S) eps^T, conjS = conj(S); a key
counts as S*'s when either of its readings is conjS (B1922's split).

EXPECTATIONS, written before the run:
  O1  Own line (2/5, 4/5), gamma, at s = -l/2, -l/2 + 0.15, 0: S and St repeat (deviation below 1e-6); S* does not
      (above 1e-3). B1922's negative half, recomputed.
  O2  Line (1/5, 2/5), fixed by gamma up to sign (W-F22's L1), gamma, same points: S and St repeat (below 1e-6); S* does
      not (above 1e-3). R82-1's item 12: "periodic at no other line" is false here.
  O3  Line (1/5, 3/5), not fixed, gamma: every reading deviates (above 1e-3).
  O4  Own line, gamma^3, at s = -3l/2 (tau and gamma^3 tau equally high, Im about 0.12) and s = -3l/2 + 0.1: S, St AND S*
      repeat (below 1e-4; looser, the points are low). S* repeats after three turns because gamma^3 is in Gamma(2),
      under which S* is covariant (W-F22's C1). If S and St fail here too, the height is out of the frame's reach and O4
      is inconclusive, not refuted.
  Plant: the end left untransported (L at g tau = L at tau) makes S and St deviate at the own line under gamma (above
  1e-3).
"""
import importlib.util
import math
import os

import mpmath as mp
import numpy as np
from numpy.polynomial.legendre import leggauss

HERE = os.path.dirname(os.path.abspath(__file__))
_s = importlib.util.spec_from_file_location("wf22c", os.path.join(HERE, "wf22_checks.py"))
_src = open(os.path.join(HERE, "wf22_checks.py")).read()
ns = {}
exec(_src.split("# ---------------- L1, L2")[0], ns)        # imports and say() only
exec(_src[_src.index("# ---------------- the triplet"):_src.index("GS = {")], ns)  # theta series, Rv, E2f, av, mob


def say(*a):
    print(*a, flush=True)


av = ns["av"]

# ---------------- B1656's frame, re-typed
QI = np.array([[1j, 0], [0, -1j]])
QJ = np.array([[0, 1], [-1, 0]], dtype=complex)
QK = QI @ QJ
EPS = QJ
UNITS = {"1": np.eye(2, dtype=complex), "i": QI, "j": QJ, "k": QK}
BLOCKS = [QJ, QI, QK]
SIXY = {"Q": 1, "u": -4, "d": 2, "L": -3, "e": 6}
SECT = {"up": ("Q", "u"), "down": ("Q", "d"), "lep": ("L", "e")}
NK = 30


def thc(a, b, u, T):
    n = np.arange(-NK, NK + 1) + a
    u = np.asarray(u, dtype=complex)[..., None]
    return np.sum(np.exp(1j * np.pi * T * n * n + 2j * np.pi * n * (u + b)), -1)


def th1(u, t):
    k = np.arange(-NK, NK + 1)
    h = k + 0.5
    u = np.asarray(u, dtype=complex)[..., None]
    return -1j * np.sum((-1.0) ** k * np.exp(1j * np.pi * t * h * h + 1j * np.pi * (2 * k + 1) * u), -1)


def bil(x, y, u, t):
    (ax, bx), (ay, by) = x, y
    T = 2 * t
    t1 = th1(u, t)
    den = 1j * np.exp(-1j * np.pi * t / 2) * np.exp(-1j * np.pi * u) * t1
    X0, X1, Y0, Y1 = thc(ax, bx, u, T), thc(ax, bx, u + t, T), thc(ay, by, u, T), thc(ay, by, u + t, T)
    return np.array([[X0 * Y0 / t1, np.exp(1j * np.pi * by) * X0 * Y1 / den],
                     [np.exp(1j * np.pi * bx) * X1 * Y0 / den, np.exp(1j * np.pi * (bx + by)) * X1 * Y1 / th1(u + t, t)]])


def pairs(x, y, u, t):
    M = bil(x, y, u, t)
    return {s: np.einsum('mn,mn...->...', EPS @ C, M) for s, C in UNITS.items()}


def twist_of(w, t):
    a = w.imag / t.imag
    return (a, 2 * (w.real - a * t.real))


def residues(x, y, t, rad=0.01, N=256):
    u = rad * np.exp(2j * np.pi * np.arange(N) / N)
    P = pairs(x, y, u, t)
    return {s: complex(np.mean(P[s] * u)) for s in UNITS}


def rmax_np(th, t):
    d = np.exp(1j * th)
    y1 = d.imag / t.imag
    x1 = d.real - y1 * t.real
    return 0.5 / np.maximum(abs(x1), abs(y1))


def vangles(t):
    v = [0.5 + 0.5 * t, -0.5 + 0.5 * t, -0.5 - 0.5 * t, 0.5 - 0.5 * t]
    br = sorted(float(np.mod(np.angle(z), 2 * np.pi)) for z in v)
    return br + [br[0] + 2 * np.pi]


def a0_of(x, y, t, R, rad=0.05, N=128):
    u = rad * np.exp(2j * np.pi * np.arange(N) / N)
    P = pairs(x, y, u, t)
    return {s: (complex(np.mean(P[s] / R[s] - 1 / u)) if abs(R[s]) > 1e-12 else None) for s in UNITS}


def cA(x, y, t, R, eps=1e-5, nth=96, ns_=64):
    A0 = a0_of(x, y, t, R)
    br = vangles(t)
    xg, wg = leggauss(nth)
    xs, ws = leggauss(ns_)
    tot = {s: 0.0 for s in UNITS}
    for a, b in zip(br[:-1], br[1:]):
        th = 0.5 * (b - a) * xg + 0.5 * (b + a)
        wt = 0.5 * (b - a) * wg
        hi = np.log(rmax_np(th, t))
        lo = math.log(eps)
        sg = 0.5 * (hi - lo)[:, None] * xs[None, :] + 0.5 * (hi + lo)[:, None]
        w2 = 0.5 * (hi - lo)[:, None] * ws[None, :]
        rr = np.exp(sg)
        z = rr * np.exp(1j * th)[:, None]
        P = pairs(x, y, z, t)
        for s in UNITS:
            if abs(R[s]) > 1e-12:
                tot[s] += np.sum(wt[:, None] * w2 * np.abs(P[s] / R[s]) ** 2 * rr ** 2)
    return {s: (float(tot[s] - 2 * np.pi * math.log(1 / eps) + np.pi * eps ** 2 * abs(A0[s]) ** 2)
                if abs(R[s]) > 1e-12 else None) for s in UNITS}


EC = {s: (EPS @ C) for s, C in UNITS.items()}
_G = np.array([[np.sum(EC[t] * UNITS[s]) for s in UNITS] for t in UNITS])
_Gi = np.linalg.inv(_G)
_K = list(UNITS)
EDUAL = {_K[a]: sum(_Gi[b, a] * UNITS[_K[b]] for b in range(4)) for a in range(4)}


def weighted_M(u):
    return sum(u[s] * EDUAL[s] for s in UNITS)


def coupling(S, M):
    return np.array([[np.sum((Ca.T @ EPS @ S @ Cb) * M) for Cb in BLOCKS] for Ca in BLOCKS])


RD = ("S", "St", "conjS")


def frame(t, a, b, Ls):
    c3 = [complex(v) for v in av(mp.mpc(t.real, t.imag))]
    S = c3[0] * QI + c3[1] * QJ + c3[2] * QK
    reading = {"S": S, "St": EPS @ np.conj(S) @ EPS.T, "conjS": np.conj(S)}
    w = a * t + b
    out, Y = {}, {}
    for sec, (lf, rf) in SECT.items():
        x, yy = twist_of(SIXY[lf] * w, t), twist_of(SIXY[rf] * w, t)
        R = residues(x, yy, t)
        c = cA(x, yy, t, R)
        for h in ("L_max", "L_2"):
            L = Ls[h]
            u = {s: (math.sqrt(2 * math.pi * L + c[s]) * R[s] if c[s] is not None and 2 * math.pi * L + c[s] > 0 else 0)
                 for s in UNITS}
            Mw = weighted_M(u)
            for rn in RD:
                Ym = coupling(reading[rn], Mw)
                Y[(sec, h, rn)] = Ym
                sv = np.linalg.svd(Ym, compute_uv=False)
                out["%s|%s|%s" % (sec, h, rn)] = [float(sv[1] / sv[0]), float(sv[2] / sv[0])]
    for h in ("L_max", "L_2"):
        for ru in RD:
            for rd in RD:
                Uu = np.linalg.svd(Y[("up", h, ru)])[0][:, ::-1]
                Ud = np.linalg.svd(Y[("down", h, rd)])[0][:, ::-1]
                V = np.conj(Uu.T) @ Ud
                out["ckm|%s|%s|%s" % (h, ru, rd)] = [float(abs(V[0, 1])), float(abs(V[1, 2])), float(abs(V[0, 2]))]
    return out


def dev(x, y):
    return max((abs(math.log(p / q)) for p, q in zip(x, y) if p > 1e-10 and q > 1e-10), default=0.0)


def split(base, other):
    cov = star = 0.0
    for k in base:
        d = dev(base[k], other[k])
        if "conjS" in k:
            star = max(star, d)
        else:
            cov = max(cov, d)
    return cov, star


phi = (1 + 5 ** 0.5) / 2
ell = 2 * math.log(phi ** 2)
LS0 = {"L_max": 1.3, "L_2": 0.9}


def zt(s):
    return complex((phi * 1j * math.exp(s) - 1 / phi) / (1j * math.exp(s) + 1))


def gam(t):
    return (2 * t + 1) / (t + 1)


def test(s0, line, power, transport=True):
    t = zt(s0)
    g, shift = t, 0.0
    for _ in range(power):
        shift += math.log(abs(g + 1))
        g = gam(g)
    assert abs(g - zt(s0 + power * ell)) < 1e-9
    Lg = {h: LS0[h] + (shift if transport else 0.0) for h in LS0}
    a, b = line
    cov, star = split(frame(t, a, b, LS0), frame(g, a, b, Lg))
    return t.imag, g.imag, cov, star


if __name__ == "__main__":
    ok = {}
    pts = (-ell / 2, -ell / 2 + 0.15, 0.0)
    for key, line, want_cov, want_star in (("O1", (0.4, 0.8), "rep", "dev"), ("O2", (0.2, 0.4), "rep", "dev"),
                                           ("O3", (0.2, 0.6), "dev", "dev")):
        good = True
        for s0 in pts:
            yi, yg, cov, star = test(s0, line, 1)
            good &= (cov < 1e-6 if want_cov == "rep" else cov > 1e-3) and (star < 1e-6 if want_star == "rep" else star > 1e-3)
            say("%s line %s gamma: Im tau %.3f, Im gamma tau %.3f | S, St %.1e | S* %.1e" % (key, line, yi, yg, cov, star))
        ok[key] = good
    good4, reach = True, True
    for s0 in (-3 * ell / 2, -3 * ell / 2 + 0.1):
        yi, yg, cov, star = test(s0, (0.4, 0.8), 3)
        reach &= cov < 1e-4
        good4 &= cov < 1e-4 and star < 1e-4
        say("O4 own line gamma^3: Im tau %.3f, Im gamma^3 tau %.3f | S, St %.1e | S* %.1e" % (yi, yg, cov, star))
    ok["O4"] = good4 if reach else "inconclusive (S and St fail at this height)"
    yi, yg, cov, star = test(-ell / 2, (0.4, 0.8), 1, transport=False)
    say("plant (end untransported), own line gamma: S, St %.1e | caught: %s" % (cov, cov > 1e-3))
    say("holds:", ok)
