#!/usr/bin/env python3
"""W-B2, stage 4 (M36's data-free check; committed before its run; NOT blind: W-B2's second referee read found, unsealed,
that off the pole M_alt(u - h) is frame C at q' times a scalar of modulus varying like e^(k Im u)).

Does the identity E (stage 3: at residue level, frame D1 with the Szegoe zero moved to the Higgs's point h = c q_H w is
frame C at q' = q - c q_H / 2) extend to the full frame, with the channel norms? Frame D1's full frame: the norms are
B1656's quadrature (the transcription's cA and a0_of), re-centred on the moved pole: the integrand is M_alt's channels at
-h + z over the same cell about the pole; Theorem 90's weight; the end L_2 = 0.9 held fixed (a bounded end, as in W-F25's
post hoc 1). Frame C at q' uses the transcription's frame unchanged at the shifted charges, with the same end.
Compared: the two singular-value ratios of each sector in reading S, at c = +2 and -2, at the mark and the twin, at three
bulk moduli.

    python3 -I -u wb2_stage4.py

EXPECTATIONS:
  N1  (a prediction from the second referee read) E does not reach the norms: for c = +2 some ratio differs from frame C
      at q' by more than 1e-3.
  N2  reported: the same for c = -2, and the size of the difference.
  N3  control: with the norms switched off (unit weights) the difference is below 1e-8 (stage 3's E).
"""
import math, os, sys
import numpy as np
from numpy.polynomial.legendre import leggauss
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import wb2_stage3 as W3  # noqa: E402
K = W3.K
NS = K.NS
L2 = 0.9


def chan(x, y, z, t, h):
    M = W3.M_alt(x, y, z, t, h)
    return {s: np.einsum('mn,mn...->...', NS["EPS"] @ C, M) for s, C in NS["UNITS"].items()}


def a0_alt(x, y, t, R, h, rad=0.05, N=128):
    d = rad * np.exp(2j * np.pi * np.arange(N) / N)
    P = chan(x, y, -h + d, t, h)
    return {s: (complex(np.mean(P[s] / R[s] - 1 / d)) if abs(R[s]) > 1e-12 else None) for s in NS["UNITS"]}


def cA_alt(x, y, t, R, h, eps=1e-5, nth=96, ns_=64):
    A0 = a0_alt(x, y, t, R, h)
    br = NS["vangles"](t)
    xg, wg = leggauss(nth)
    xs, ws = leggauss(ns_)
    tot = {s: 0.0 for s in NS["UNITS"]}
    for a, b in zip(br[:-1], br[1:]):
        th = 0.5 * (b - a) * xg + 0.5 * (b + a)
        wt = 0.5 * (b - a) * wg
        hi = np.log(NS["rmax_np"](th, t))
        lo = math.log(eps)
        sg = 0.5 * (hi - lo)[:, None] * xs[None, :] + 0.5 * (hi + lo)[:, None]
        w2 = 0.5 * (hi - lo)[:, None] * ws[None, :]
        rr = np.exp(sg)
        zz = rr * np.exp(1j * th)[:, None]
        P = chan(x, y, -h + zz, t, h)
        for s in NS["UNITS"]:
            if abs(R[s]) > 1e-12:
                tot[s] += np.sum(wt[:, None] * w2 * np.abs(P[s] / R[s]) ** 2 * rr ** 2)
    return {s: (float(tot[s] - 2 * np.pi * math.log(1 / eps) + np.pi * eps ** 2 * abs(A0[s]) ** 2)
                if abs(R[s]) > 1e-12 else None) for s in NS["UNITS"]}


def weights(R, c, a0):
    u = {}
    for s in NS["UNITS"]:
        if c[s] is None or a0[s] is None:
            u[s] = 0
            continue
        N = 2 * math.pi * L2 + c[s] - math.pi * abs(a0[s]) ** 2 * math.exp(-2 * L2)
        u[s] = math.sqrt(N) * R[s] if N > 0 else 0
    return u


def ratios(Y):
    sv = np.linalg.svd(Y, compute_uv=False)
    return np.array([sv[1] / sv[0], sv[2] / sv[0]])


def both(t, a, b, sec, cc, norms=True):
    w = a * t + b
    lf, rf = K.SECT[sec]
    S3 = K.comps(t, 0.0, 0.0)
    S = S3[0] * K.QI + S3[1] * K.QJ + S3[2] * K.QK
    h = cc * K.QH[sec] * w
    x, y = K.twist_of(K.SIXY[lf] * w, t), K.twist_of(K.SIXY[rf] * w, t)
    R = W3.res_alt(x, y, t, h)
    if norms:
        uD = weights(R, cA_alt(x, y, t, R, h), a0_alt(x, y, t, R, h))
    else:
        uD = R
    qs = (K.SIXY[lf] - cc * K.QH[sec] / 2, K.SIXY[rf] - cc * K.QH[sec] / 2)
    x2, y2 = K.twist_of(qs[0] * w, t), K.twist_of(qs[1] * w, t)
    R2 = NS["residues"](x2, y2, t)
    if norms:
        uC = weights(R2, NS["cA"](x2, y2, t, R2), NS["a0_of"](x2, y2, t, R2))
    else:
        uC = R2
    rD = ratios(NS["coupling"](S, NS["weighted_M"](uD)))
    rC = ratios(NS["coupling"](S, NS["weighted_M"](uC)))
    return float(np.max(np.abs(rD / rC - 1)))


def main():
    taus = [complex(0.13, 1.7), complex(-0.31, 1.25), complex(0.4, 1.2)]
    pts = [(0.4, 0.8), (0.2, 0.4)]
    res = {}
    for cc in (2, -2):
        for norms in (True, False):
            wv = 0.0
            for sec in ("up", "down", "lep"):
                for a, b in pts:
                    for t in taus:
                        wv = max(wv, both(t, a, b, sec, cc, norms))
            res[(cc, norms)] = wv
            K.say("c %+d  norms %-5s  largest relative difference in r2, r3 against frame C at q': %.2e" % (cc, norms, wv))
    K.say("N1 holds:", res[(2, True)] > 1e-3, "| N3 holds:", res[(2, False)] < 1e-8 and res[(-2, False)] < 1e-8)


if __name__ == "__main__":
    main()
