#!/usr/bin/env python3
"""W-B2, stage 3 (committed before its run; NOT blind: the referee's read of stages 1-2 computed this placement, unsealed).

Stage 1's K2 shifted the matter doublets' factors as well as the Szegoe zero. Frame C's bilinear factorises,
bil(x, y, u) = v_x(u) v_y(u)^T / th1(u, tau), v = (th[a, b](u, 2 tau), -i th[a + 1/2, b](u, 2 tau)) (the referee's
reading; U0 checks it here). The corrected placement moves the Szegoe zero alone:
    M_alt(h)(u) = v_x(u) v_y(u)^T / th1(u + h, tau),   residue at u0 = -h,   h = c q_H w.
Residue level, unit weights, the two non-zero singular values (as stage 1's post hoc 1); triplet untwisted; readings S, St.

    python3 -I -u wb2_stage3.py

TESTS (sectors up, down, lep; points (2/5, 4/5), (1/5, 2/5), (0, 3/5), (3/5, 1/5)):
  T  tau -> tau + 1, (a, b) -> (a, b - a) exactly (no reduction mod 1), at stage 1's moduli; also with the reduction.
  S  tau -> -1/tau, (a, b) -> (-b, a) exactly, at stage 2's moduli; also with -b reduced mod 1.
  P  periodicity in the Higgs's point: w -> w + 1 and w -> w + tau (the line (a, b) -> (a, b + 1) and (a + 1, b)).
  E  M_alt(c) against frame C's kernel at the shifted charges q' = q - c q_H / 2 (both legs), r2 compared.
  R  reading S at h against St at -h.
dev = the largest relative deviation of r2 = s2/s1 (and, for T and P, of s1).

EXPECTATIONS (written after the referee's unsealed computation was read):
  U0  the factorisation holds (relative difference below 1e-12 at 20 random u, h = 0).
  U1  c = +2 and -2: T-, S- and P-covariant (below 1e-8), with and without the reductions.
  U2  c = +1 and -1: S-covariant without the reduction; not P-covariant under w -> w + 1 (above 1e-3).
  U3  E holds for c = +2 and -2 (below 1e-8); for c = -2 the shifted charges are (-q_R, -q_L).
  U4  R: S at h and St at -h differ (above 1e-3) for c = +2.
  Plant: the S-test with h kept at tau's value (not transported to h / tau) fails for c = +2 (above 1e-3).
"""
import os, sys, random
from fractions import Fraction as Fr
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import wb2_stage1 as K  # noqa: E402
import wb2_stage2 as K2  # noqa: E402
thc, th1, NS = K.thc, K.th1, K.NS


def v(ch, u, t):
    a, b = ch
    return np.array([thc(a, b, u, 2 * t), -1j * thc(a + 0.5, b, u, 2 * t)])


def M_alt(x, y, u, t, h):
    return np.einsum("i...,j...->ij...", v(x, u, t), v(y, u, t)) / th1(u + h, t)


def res_alt(x, y, t, h, rad=0.01, N=256):
    d = rad * np.exp(2j * np.pi * np.arange(N) / N)
    M = M_alt(x, y, -h + d, t, h)
    return {s: complex(np.mean(np.einsum('mn,mn...->...', NS["EPS"] @ C, M) * d)) for s, C in NS["UNITS"].items()}


def sv_of(t, a, b, sec, c, rd, hsign=1, h_override=None, charges=None):
    w = a * t + b
    lf, rf = K.SECT[sec]
    ql, qr = charges if charges is not None else (K.SIXY[lf], K.SIXY[rf])
    x, y = K.twist_of(ql * w, t), K.twist_of(qr * w, t)
    h = h_override if h_override is not None else hsign * c * K.QH[sec] * w
    R = res_alt(x, y, t, h)
    cc = K.comps(t, 0.0, 0.0)
    S = cc[0] * K.QI + cc[1] * K.QJ + cc[2] * K.QK
    if rd == "St":
        S = K.EPS @ np.conj(S) @ K.EPS.T
    return np.linalg.svd(NS["coupling"](S, NS["weighted_M"](R)), compute_uv=False)


def d2(s0, s1, with_s1=True):
    r = abs((s1[1] / s1[0]) / (s0[1] / s0[0]) - 1)
    return max(r, abs(s1[0] / s0[0] - 1)) if with_s1 else r


PTS = [(0.4, 0.8), (0.2, 0.4), (0.0, 0.6), (0.6, 0.2)]


def run(kind, c, rd, reduce=False):
    wv = 0.0
    for sec in ("up", "down", "lep"):
        for a, b in PTS:
            for t in (K.TAUS if kind in ("T", "P1", "Pt") else K2.TAUS):
                s0 = sv_of(t, a, b, sec, c, rd)
                if kind == "T":
                    b1 = b - a
                    if reduce:
                        b1 %= 1
                    wv = max(wv, d2(s0, sv_of(t + 1, a, b1, sec, c, rd)))
                elif kind == "S":
                    a1 = -b
                    if reduce:
                        a1 %= 1
                    wv = max(wv, d2(s0, sv_of(-1 / t, a1, a, sec, c, rd), with_s1=False))
                elif kind == "Splant":
                    h0 = c * K.QH[sec] * (a * t + b)
                    wv = max(wv, d2(s0, sv_of(-1 / t, -b, a, sec, c, rd, h_override=h0), with_s1=False))
                elif kind == "P1":
                    wv = max(wv, d2(s0, sv_of(t, a, b + 1, sec, c, rd)))
                elif kind == "Pt":
                    wv = max(wv, d2(s0, sv_of(t, a + 1, b, sec, c, rd)))
                elif kind == "E":
                    lf, rf = K.SECT[sec]
                    qs = (K.SIXY[lf] - c * K.QH[sec] / 2, K.SIXY[rf] - c * K.QH[sec] / 2)
                    wv = max(wv, d2(s0, sv_of(t, a, b, sec, 0, rd, charges=qs), with_s1=False))
                elif kind == "R":
                    wv = max(wv, d2(s0, sv_of(t, a, b, sec, c, "St", hsign=-1), with_s1=False))
    return float(wv)


def main():
    rng = random.Random(3)
    u0 = 0.0
    for _ in range(20):
        u = complex(rng.uniform(-0.4, 0.4), rng.uniform(-0.4, 0.4))
        t = complex(0.13, 1.7)
        x, y = (0.4, 1.6), (-1.6, -6.4)
        A = K.bil_h(x, y, u, t, 0.0)
        B = M_alt(x, y, u, t, 0.0)
        u0 = max(u0, float(np.max(np.abs(A - B)) / np.max(np.abs(A))))
    K.say("U0 factorisation, largest relative difference: %.1e | holds: %s" % (u0, u0 < 1e-12))
    res = {}
    for c in (2, -2, 1, -1):
        for rd in ("S", "St"):
            row = {k: run(k, c, rd) for k in ("T", "S", "P1", "Pt", "E")}
            row["T mod 1"] = run("T", c, rd, reduce=True)
            row["S mod 1"] = run("S", c, rd, reduce=True)
            res[(c, rd)] = row
            K.say("c %+d %-2s  " % (c, rd) + "  ".join("%s %.1e" % (k, v_) for k, v_ in row.items()))
    u1 = all(max(res[(c, rd)][k] for k in ("T", "S", "P1", "Pt", "T mod 1", "S mod 1")) < 1e-8 for c in (2, -2) for rd in ("S", "St"))
    u2 = all(res[(c, rd)]["S"] < 1e-8 and res[(c, rd)]["P1"] > 1e-3 for c in (1, -1) for rd in ("S", "St"))
    u3 = all(res[(c, rd)]["E"] < 1e-8 for c in (2, -2) for rd in ("S", "St"))
    sh = {sec: (K.SIXY[l] + K.QH[sec], K.SIXY[r] + K.QH[sec]) for sec, (l, r) in K.SECT.items()}
    rev = {sec: (-K.SIXY[r], -K.SIXY[l]) for sec, (l, r) in K.SECT.items()}
    u4 = all(run("R", 2, rd) > 1e-3 for rd in ("S",))
    plant = run("Splant", 2, "S") > 1e-3
    K.say("U1 holds:", u1, "| U2 holds:", u2, "| U3 holds:", u3, "(c = -2 charges %s; equal to (-q_R, -q_L): %s)" % (sh, sh == rev),
          "| U4 holds:", u4, "| plant fails:", plant)


if __name__ == "__main__":
    main()
