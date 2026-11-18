#!/usr/bin/env python3
"""The status page's section 13: M52's question on agy-exp's level-5 phase law for this seat's frame D1 (B1945 § 6,
register row P-871). Data-free. Computed once, on this seat's own code (main's is not run or imported).

    python3 -I -u rv52_phase.py

The residue of frame D1 at its pole is v_x(-h) v_y(-h)^T / theta_1'(0), with v_x(u) = (th[x](u, 2 tau),
-i th[x + (1/2, 0)](u, 2 tau)), x = (q_L a, 2 q_L b), y = (q_R a, 2 q_R b), h = c q_H (a tau + b), at the 24 points
(a, b) = (i/5, j/5) of order 5 (W-B2's note; th[al, be](u, T) = sum_n exp(pi i (n + al)^2 T + 2 pi i (n + al)(u + be))).
For each sector (charges up (1, -4, 3), down (1, 2, -3), leptons (-3, 6, -3)) and c = 0, +-1, +-2, each entry at
tau + 5 and at tau + 25 over the same entry at tau, the same representatives on both sides, divided by that ratio at
the reference point (0, 1/5). theta_1'(0) is the same at every point and drops out.

The law tested, derived by hand from the series before this run: under tau + 5 the (0, 0) entry changes by
zeta^(E i^2), E = q_L^2 + q_R^2 + c q_H^2 mod 5 (using q_L + q_R + q_H = 0), the off-diagonal entries by
(-1)^(i c q_H) more, the (1, 1) entry as the (0, 0); under tau + 25 by 1, with the same signs.
Printed: per sector and c, E, the largest deviation from the law over the 24 points, and whether the sector closes.
"""
import cmath
import math
from fractions import Fraction as Fr

import mpmath as mp

mp.mp.dps = 30
I = mp.mpc(0, 1)
SEC = {"up": (1, -4, 3), "down": (1, 2, -3), "lepton": (-3, 6, -3)}
ZETA = mp.exp(2 * mp.pi * I / 5)


def th(al, be, u, T, N=12):
    return mp.fsum(mp.exp(mp.pi * I * (n + al) ** 2 * T + 2 * mp.pi * I * (n + al) * (u + be)) for n in range(-N, N + 1))


def resid(t, a, b, q, c):
    ql, qr, qh = q; h = c * qh * (a * t + b); u = -h
    vx = [th(ql * a, 2 * ql * b, u, 2 * t), -I * th(ql * a + mp.mpf(1) / 2, 2 * ql * b, u, 2 * t)]
    vy = [th(qr * a, 2 * qr * b, u, 2 * t), -I * th(qr * a + mp.mpf(1) / 2, 2 * qr * b, u, 2 * t)]
    return [[vx[m] * vy[n] for n in range(2)] for m in range(2)]


PTS = [(mp.mpf(i) / 5, mp.mpf(j) / 5, i) for i in range(5) for j in range(5) if (i, j) != (0, 0)]
t0 = mp.mpc("0.13", "1.7")
closes = {}
for c in (0, 1, -1, 2, -2):
    for sec, q in SEC.items():
        ql, qr, qh = q; E = (ql * ql + qr * qr + c * qh * qh) % 5
        assert ql + qr + qh == 0
        worst = 0
        base = {p: resid(t0, p[0], p[1], q, c) for p in PTS}
        for shift in (5, 25):
            new = {p: resid(t0 + shift, p[0], p[1], q, c) for p in PTS}
            ref = [[new[PTS[0]][m][n] / base[PTS[0]][m][n] for n in range(2)] for m in range(2)]  # (0, 1/5)
            for p in PTS:
                i = p[2]
                for m in range(2):
                    for n in range(2):
                        r = new[p][m][n] / base[p][m][n] / ref[m][n]
                        law = (ZETA ** (E * i * i) if shift == 5 else 1) * ((-1) ** (i * c * qh) if m != n else 1)
                        worst = max(worst, abs(r - law))
        closes[(c, sec)] = (E == 0)
        print("c = %+d, %-6s: E = %d; largest deviation from the law at tau + 5 and tau + 25, all 24 points, all four "
              "entries: %s" % (c, sec, E, mp.nstr(worst, 3)))
print("sectors that close at level 5 (E = 0), by c: %s" % {c: [s for s in SEC if closes[(c, s)]] for c in (0, 1, -1, 2, -2)})
print("residues c mod 5 closing up and down together: %s" % [c for c in range(5) if (17 + 9 * c) % 5 == 0 and (5 + 9 * c) % 5 == 0])
