#!/usr/bin/env python3
"""The status page's section 17, after its referee read: a direct test of the channels' part of the constant under T.
Data-free. Computed once, on main's own routines (B1945's frame_mp and determinant_law; none edited).

    python3 -I -u rv57_linear.py <a checkout of main at 364ce101e>

rv57_constant.py divided main's constant by the Higgs's own phase. That is a consistency check, not a test of the
decomposition. Here the Higgs input is a free vector x, with the channels' matrix Mw that determinant_law.parts returns
at tau and at tau + 1 (its line 36: Y = sum over m, n of (Ca^T EPS Sr Cb)[m, n] Mw[m, n], Sr = x0 QI + x1 QJ + x2 QK).
Tested at the points a = 0 (where the point transport under T is the identity), both base points of B1953 and both
sectors: Y(tau + 1; Q x) = c R Y(tau; x) R^T, with R = [[0, 0, 1], [0, 1, 0], [-1, 0, 0]] (main's read-out, det +1)
and Q the real rotation of determinant +1 with c3(tau + 1) = h Q c3(tau) (rv57_constant.py), for x = e1, e2, e3 and two
fixed complex vectors. Printed: c in turns and |c|, and the largest relative residual; and the same with R -> -R and
with Q of determinant -1 (h then 5/8 of a turn), to show which choices are conventions.
"""
import pathlib
import sys

import numpy as np

MAIN = pathlib.Path(sys.argv[1]).resolve()
sys.path.insert(0, str(next((MAIN / "frontier").glob("B1953_*")) / "verification"))
import weyl_operator as WO                                                   # noqa: E402

DL = WO.DL; FM = DL.FM; mp = FM.mp; te = FM.te
turns = lambda z: (float(np.angle(complex(z))) / (2 * np.pi)) % 1.0
I, QI, QJ, QK, EPS, U, ED, BLOCKS = FM.setup()
qn = lambda M: np.array([[complex(M[i, j]) for j in range(M.cols)] for i in range(M.rows)])
QIn, QJn, QKn, EPSn = qn(QI), qn(QJ), qn(QK), qn(EPS)
BL = [qn(C) for C in BLOCKS]


def Y_of(x, Mw):
    Sr = x[0] * QIn + x[1] * QJn + x[2] * QKn
    return np.array([[sum((Ca.T @ EPSn @ Sr @ Cb)[m, n] * Mw[m, n] for m in range(2) for n in range(2)) for Cb in BL]
                     for Ca in BL])


# Q from the Higgs triplet, as in rv57_constant.py
mp.mp.dps = 40
taus = [mp.mpc(x, y) for x, y in (("0.13", "1.7"), ("0.31", "1.2"), ("-0.22", "1.45"), ("0.05", "2.1"), ("0.41", "1.05"),
                                  ("-0.37", "1.9"))]
A = np.array([[complex(te.ev(cc, t)) for cc in te.B[1]] for t in taus])
Bm = np.array([[complex(te.ev(cc, t + 1)) for cc in te.B[1]] for t in taus])
M = np.linalg.lstsq(A, Bm, rcond=None)[0].T
d = np.linalg.det(M)
hs = [abs(d) ** (1 / 3) * np.exp(1j * (np.angle(d) + 2 * np.pi * k) / 3) for k in range(3)]
h = min(hs, key=lambda hh: np.abs((M / hh).imag).max())
Qp = (M / h).real                      # determinant +1
Qm, hm = -Qp, -h                       # the same M with Q of determinant -1
R = np.array([[0, 0, 1], [0, 1, 0], [-1, 0, 0]], float)
rng = np.random.default_rng(57)
XS = [np.eye(3)[k].astype(complex) for k in range(3)] + [rng.normal(size=3) + 1j * rng.normal(size=3) for _ in range(2)]
print("Q (det %+.0f) with h = %.4f of a turn; the other choice: Q (det %+.0f) with h = %.4f of a turn"
      % (np.linalg.det(Qp), turns(h), np.linalg.det(Qm), turns(hm)))
for (tx, ty) in WO.BASES:
    for sec in ("down", "up"):
        for (a, b) in [(0, 1), (0, 2), (0, 3), (0, 4)]:
            Mw0 = qn(DL.parts(tx, ty, 0, mp.mpf(b) / 5, sec)[1])
            Mw1 = qn(DL.parts(mp.nstr(mp.mpf(tx) + 1, 30), ty, 0, mp.mpf(b) / 5, sec)[1])
            for label, Q, RR in (("det Q +1, R", Qp, R), ("det Q +1, -R", Qp, -R), ("det Q -1, R", Qm, R)):
                cs, res = [], 0.0
                for x in XS:
                    Z = RR @ Y_of(x, Mw0) @ RR.T; Y1 = Y_of(Q @ x, Mw1)
                    c = np.vdot(Z, Y1) / np.vdot(Z, Z); cs.append(c)
                    res = max(res, float(np.abs(Y1 - c * Z).max() / np.abs(Y1).max()))
                spread = max(abs(c - cs[0]) for c in cs)
                print("base %s %-4s point (0, %d/5), %s: c = %.6f of a turn, |c| = %.12f, spread over the five x %.1e, "
                      "residual %.1e" % (tx, sec, b, label, turns(cs[0]), abs(cs[0]), spread, res))
