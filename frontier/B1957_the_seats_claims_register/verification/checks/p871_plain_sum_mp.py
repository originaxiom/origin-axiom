"""P-871 at 80 digits: the plain sum of frame D1's unit-weight residues, summed WITHOUT casting each point's matrix to double
precision (main's couple() casts with complex(); this copies its formula and keeps mpmath), at tau = 0.13 + 1.7i and tau + 5,
c = +2 and -2, three sectors, both readings: the singular-value ratios and their change."""
import sys, functools
from fractions import Fraction as Fr
print = functools.partial(print, flush=True)
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))
import web_wb2_d1 as D
mp = D.mp; mp.mp.dps = 80
def couple_mp(Sr, M):     # D.couple's formula, without complex()
    return mp.matrix([[sum(((Ca.T * D.EPS * Sr * Cb)[m, n] * M[m, n] for m in range(2) for n in range(2)), mp.mpc(0)) for Cb in D.BLOCKS] for Ca in D.BLOCKS])
def d1_mp(t, a, b, sec, c, rd):
    ql, qr, qh = D.SEC[sec]; h = c * qh * (D.f2m(a) * t + D.f2m(b))
    return couple_mp(D.readings(t)[rd], D.vvec(D.chars(ql, a, b), -h, t) * D.vvec(D.chars(qr, a, b), -h, t).T / D.t1p(t))
PTS = [(Fr(i, 5), Fr(j, 5)) for i in range(5) for j in range(5) if (i, j) != (0, 0)]
def ratios(M):
    s = sorted((abs(x) for x in mp.svd_c(M, compute_uv=False)), reverse=True); return s[1] / s[0], s[2] / s[0]
for c in (2, -2):
    for sec in ("up", "down", "lepton"):
        ql, qr, qh = D.SEC[sec]; E = (ql * ql + qr * qr + c * qh * qh) % 5; out = []
        for rd in ("S", "St"):
            S = {}
            for tx in ("0.13", "5.13"):
                t = mp.mpc(tx, "1.7"); S[tx] = sum((d1_mp(t, a, b, sec, c, rd) for a, b in PTS), mp.zeros(3, 3))
            r0, r5 = ratios(S["0.13"]), ratios(S["5.13"]); d = max(abs(x - y) for x, y in zip(r0, r5))
            out.append("%s: ratios (%s, %s), change %s" % (rd, mp.nstr(r0[0], 6), mp.nstr(r0[1], 6), mp.nstr(d, 3)))
        print("M c = %+d, %s (E = %d): %s" % (c, sec, E, " | ".join(out)))
