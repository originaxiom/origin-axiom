#!/usr/bin/env python3
"""The status page's section 17: M56's question on the constant under T. Data-free. Computed once.

    python3 -I -u rv57_constant.py <a checkout of main at 364ce101e>

M56: with one real R on both sides, B1953's law leaves under tau -> tau + 1 a constant of a quarter turn in the reading S
and none in the reading S~, at the points a = 0; the web seat's note W-A2, line 110, has an eighth (its referee's algebra,
"with the Higgs and the channels moving as B1724 and B1935 section 1 record"). Are they one statement?

What this seat expects, from main's code before this run: frame C's coupling at a point is a bilinear in the Higgs
quaternion Sr and the channels' matrix Mw (B1945's determinant_law.parts, line 36), with Sr = S in the reading S and
Sr = EPS conj(S) EPS^T in the reading S~ (line 17), and the same Mw in both. If the Higgs triplet moves under T as
c3(tau + 1) = h Q c3(tau), with Q a real rotation and h a unit scalar (B1724: h = e^(i pi/4)), then the law's constant is
c_ch h in S and c_ch conj(h) in S~, with c_ch the channels' part, the same in both. The referee's algebra moves the Higgs
with its own phase, so its constant is c_ch. Expected: h = e^(i pi/4); main's constants i and 1 (M56); c_ch = e^(i pi/4)
in both readings, the eighth of W-A2's line 110.

Computed here, on main's own routines (B1945's frame_mp and determinant_law, B1953's weyl_operator; none edited):
  H  the Higgs triplet c3 = [te.ev(cc, tau) for cc in te.B[1]] at six values of tau and at tau + 1; the 3 x 3 matrix M with
     c3(tau + 1) = M c3(tau), fitted on all six; its factor M = h Q with Q real of determinant +1; h in turns; the fit's
     residual and the size of Q's imaginary part.
  K  for both base points, both sectors and both readings: main's constant under T at the points a = 0 (with one real R
     on both sides, as web_wa2_readout.py computes it), in turns; and that constant over h (reading S) or over conj(h)
     (reading S~), in turns.
"""
import pathlib
import sys

import numpy as np

MAIN = pathlib.Path(sys.argv[1]).resolve()
sys.path.insert(0, str(next((MAIN / "frontier").glob("B1953_*")) / "verification"))
import weyl_operator as WO                                                   # noqa: E402

DL = WO.DL; FM = DL.FM; mp = FM.mp; te = FM.te
turns = lambda z: (float(np.angle(complex(z))) / (2 * np.pi)) % 1.0

# H: the Higgs triplet under T
taus = [mp.mpc(x, y) for x, y in (("0.13", "1.7"), ("0.31", "1.2"), ("-0.22", "1.45"), ("0.05", "2.1"), ("0.41", "1.05"),
                                  ("-0.37", "1.9"))]
mp.mp.dps = 40
A = np.array([[complex(te.ev(cc, t)) for cc in te.B[1]] for t in taus])        # rows: c3(tau)
Bm = np.array([[complex(te.ev(cc, t + 1)) for cc in te.B[1]] for t in taus])   # rows: c3(tau + 1)
Mt, *_ = np.linalg.lstsq(A, Bm, rcond=None); M = Mt.T                          # c3(tau+1) = M c3(tau)
fit = float(np.abs(A @ Mt - Bm).max() / np.abs(Bm).max())
d = np.linalg.det(M)
best = None
for k in range(3):
    h = abs(d) ** (1 / 3) * np.exp(1j * (np.angle(d) + 2 * np.pi * k) / 3)
    Q = M / h
    im = float(np.abs(Q.imag).max())
    if best is None or im < best[1]:
        best = (h, im, Q)
h, imQ, Q = best
print("H: c3(tau + 1) = M c3(tau) on six tau, residual %.1e; M = h Q with Q real to %.1e, det Q = %.6f, Q^T Q = 1 to %.1e; "
      "|h| = %.12f, h = %.6f of a turn; Q rounded: %s"
      % (fit, imQ, float(np.linalg.det(Q.real)), float(np.abs(Q.real.T @ Q.real - np.eye(3)).max()), abs(h), turns(h),
         Q.real.round(6).tolist()))


# K: main's constant under T at a = 0, with one real R on both sides, and the constant over the Higgs's own phase
def realise(U):
    ph = U[np.abs(U) > 0.5]
    return U / (ph[0] / abs(ph[0]))


rows = []
for (tx, ty) in WO.BASES:
    for sec in ("down", "up"):
        Ys, _ = WO.images(tx, ty, sec)
        for rd in ("S", "St"):
            l = WO.law(Ys["t"][rd], Ys["T"][rd], "T")
            RL, RR = realise(l["UL"]), realise(l["UR"])
            if np.abs(RL - RR).max() > 1e-6:
                RR = -RR
            tr = WO.TRANS["T"][0]
            cs = [np.vdot(RL @ Ys["t"][rd][tr(*w)] @ RR.T, Ys["T"][rd][w]) for w in WO.PTS if w[0] == 0]
            c = np.mean([x / abs(x) for x in cs]); spread = max(abs(x / abs(x) - c / abs(c)) for x in cs)
            hh = h if rd == "S" else np.conj(h)
            rows.append((tx, sec, rd, turns(c), turns(c / hh), spread))
for r in rows:
    print("K: base %s %-4s %-2s: main's constant %.6f of a turn (spread over the points a = 0: %.1e); over the Higgs's own "
          "phase in this reading: %.6f of a turn" % (r[0], r[1], r[2], r[3], r[5], r[4]))
print("K: the constant over the Higgs's own phase, in all eight cases: %s of a turn"
      % sorted({round(r[4], 6) % 1.0 for r in rows}))
