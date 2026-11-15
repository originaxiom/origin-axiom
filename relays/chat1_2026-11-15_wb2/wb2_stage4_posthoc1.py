#!/usr/bin/env python3
"""W-B2, stage 4, post hoc 1 (committed before its run; NOT blind: stage 4's output has been read).

Stage 4's control N3 failed on the harness flaw of stage 1: with the norms off (unit weights) the coupling has rank 2, so
s3/s1 is rounding noise and its relative difference meaningless. This run repeats stage 4 with r2 and r3 reported
separately, and the control on r2 alone.
  N3' with the norms off, r2 differs from frame C at q' by less than 1e-8 (c = +2 and -2).
  N1' with the norms on, r2 or r3 differs by more than 1e-3 for c = +2 (reported separately).

    python3 -I -u wb2_stage4_posthoc1.py
"""
import os, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import wb2_stage4 as S4  # noqa: E402
K, W3, NS = S4.K, S4.W3, S4.NS


def pair(t, a, b, sec, cc, norms):
    w = a * t + b
    lf, rf = K.SECT[sec]
    c3 = K.comps(t, 0.0, 0.0)
    S = c3[0] * K.QI + c3[1] * K.QJ + c3[2] * K.QK
    h = cc * K.QH[sec] * w
    x, y = K.twist_of(K.SIXY[lf] * w, t), K.twist_of(K.SIXY[rf] * w, t)
    R = W3.res_alt(x, y, t, h)
    uD = S4.weights(R, S4.cA_alt(x, y, t, R, h), S4.a0_alt(x, y, t, R, h)) if norms else R
    qs = (K.SIXY[lf] - cc * K.QH[sec] / 2, K.SIXY[rf] - cc * K.QH[sec] / 2)
    x2, y2 = K.twist_of(qs[0] * w, t), K.twist_of(qs[1] * w, t)
    R2 = NS["residues"](x2, y2, t)
    uC = S4.weights(R2, NS["cA"](x2, y2, t, R2), NS["a0_of"](x2, y2, t, R2)) if norms else R2
    rD = S4.ratios(NS["coupling"](S, NS["weighted_M"](uD)))
    rC = S4.ratios(NS["coupling"](S, NS["weighted_M"](uC)))
    return np.abs(rD / rC - 1)


taus = [complex(0.13, 1.7), complex(-0.31, 1.25), complex(0.4, 1.2)]
pts = [(0.4, 0.8), (0.2, 0.4)]
res = {}
for cc in (2, -2):
    for norms in (True, False):
        d = np.zeros(2)
        for sec in ("up", "down", "lep"):
            for a, b in pts:
                for t in taus:
                    d = np.maximum(d, pair(t, a, b, sec, cc, norms))
        res[(cc, norms)] = d
        K.say("c %+d  norms %-5s  largest relative difference against frame C at q':  r2 %.2e   r3 %.2e" % (cc, norms, d[0], d[1]))
K.say("N3' holds:", all(res[(cc, False)][0] < 1e-8 for cc in (2, -2)), "| N1' holds:", bool(max(res[(2, True)]) > 1e-3))
