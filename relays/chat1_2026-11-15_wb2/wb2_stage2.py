#!/usr/bin/env python3
"""W-B2, stage 2 (committed before its run; designed after stage 1's post hoc 1 was read, so not blind to it).

Stage 1 found the Higgs's twist in the triplet (K1, K3) not covariant under tau -> tau + 1, and the twist in the kernel's
Szegoe factor (K2, h = c q_H w) covariant for every c tried. Tau -> tau + 1 does not see h, which is unchanged by the
transport. This stage asks two things, at residue level (unit weights; the two non-zero singular values, as in post hoc 1):

  (S) covariance under tau -> -1/tau with the line (a, b) -> (-b, a) (B1724's rule), w -> w / tau, so h -> h / tau.
      dev = max(|r2(-1/tau) / r2(tau) - 1|) over sectors, points and moduli (r2 = s2/s1; s1 itself carries the weight
      factor and is not compared).
  (R) the reading against the Higgs's sign: whether K2's coupling in reading S at h has the same r2 as in reading St at
      -h (and, reported, as in St at +h). If S at h equals St at -h, the sign of q_H acts as the reading, and the sectors'
      readings follow from their charges (up +3, down and leptons -3).

    python3 -I -u wb2_stage2.py

Points: (2/5, 4/5), (1/5, 2/5), (0, 3/5), (3/5, 1/5). Moduli near |tau| = 1, so both tau and -1/tau stay above
Im 0.85: 0.3 + 0.97i, -0.2 + 1.0i, 0.1 + 1.1i.

EXPECTATIONS:
  W0  c = 0 (frame C's kernel) is S-covariant in S and St (dev below 1e-8): the control.
  W1  (a hypothesis) the S-test separates the c: not all of +1, -1, +2, -2 are S-covariant.
  W2  (a hypothesis) for every c != 0 and every sector, S at h and St at -h have the same r2 (relative difference below
      1e-8).
  Plant: the S-test with the line not moved ((a, b) kept) fails (some deviation above 1e-3) at c = 0.
"""
import os, sys
from fractions import Fraction as Fr
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import wb2_stage1 as K  # noqa: E402

TAUS = [complex(0.3, 0.97), complex(-0.2, 1.0), complex(0.1, 1.1)]


def r2(t, a, b, sec, kc, rd, hsign=1):
    w = float(a) * t + float(b)
    lf, rf = K.SECT[sec]
    x, y = K.twist_of(K.SIXY[lf] * w, t), K.twist_of(K.SIXY[rf] * w, t)
    R = K.residues_h(x, y, t, hsign * kc * K.QH[sec] * w)
    c = K.comps(t, 0.0, 0.0)
    S = c[0] * K.QI + c[1] * K.QJ + c[2] * K.QK
    if rd == "St":
        S = K.EPS @ np.conj(S) @ K.EPS.T
    sv = np.linalg.svd(K.NS["coupling"](S, K.NS["weighted_M"](R)), compute_uv=False)
    return sv[1] / sv[0]


def s_dev(kc, rd, move=True, secs=("up", "down", "lep")):
    wv = 0.0
    for sec in secs:
        for a, b in K.POINTS:
            for t in TAUS:
                a1, b1 = ((-b) % 1, a) if move else (a, b)
                wv = max(wv, abs(r2(-1 / t, a1, b1, sec, kc, rd) / r2(t, a, b, sec, kc, rd) - 1))
    return float(wv)


def main():
    sres = {(c, rd): s_dev(c, rd) for c in (0, 1, -1, 2, -2) for rd in ("S", "St")}
    for (c, rd), v in sres.items():
        K.say("S-test  c %+d  %-2s  dev %.1e" % (c, rd, v))
    w0 = sres[(0, "S")] < 1e-8 and sres[(0, "St")] < 1e-8
    cov = [(c, rd) for (c, rd), v in sres.items() if c != 0 and v < 1e-8]
    w1 = len(set(c for c, _ in cov)) < 4
    rres = {}
    for c in (1, -1, 2, -2):
        for sec in ("up", "down", "lep"):
            d_m = d_p = 0.0
            for a, b in K.POINTS:
                for t in K.TAUS:
                    base = r2(t, a, b, sec, c, "S")
                    d_m = max(d_m, abs(r2(t, a, b, sec, c, "St", hsign=-1) / base - 1))
                    d_p = max(d_p, abs(r2(t, a, b, sec, c, "St", hsign=1) / base - 1))
            rres[(c, sec)] = (d_m, d_p)
            K.say("R-test  c %+d  %-4s  S(h) vs St(-h): %.1e   S(h) vs St(+h): %.1e" % (c, sec, d_m, d_p))
    w2 = all(v[0] < 1e-8 for v in rres.values())
    plant = s_dev(0, "S", move=False, secs=("up",)) > 1e-3
    K.say("W0 holds:", w0, "| S-covariant (c, reading), c != 0:", cov, "| W1 holds:", w1, "| W2 holds:", w2,
          "| plant fails:", plant)


if __name__ == "__main__":
    main()
