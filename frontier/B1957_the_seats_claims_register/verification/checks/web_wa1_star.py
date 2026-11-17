"""B1957, check 3: the web seat's W-A1 statements on the third reading S* (the conjugate triplet, B1922's "conjS")."""
import pathlib, sys
from fractions import Fraction as Fr
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import web_wa1_part3 as W
DL = W.DL; mp = W.mp
I_, QI, QJ, QK, EPS, U_, ED, BLOCKS = DL.FM.setup()


def ratios_star(tx, ty, w):
    out = {}
    for sec in ("up", "down"):
        RD, Mw, Ys, u, cs, ds = DL.parts(tx, ty, w[0], w[1], sec); S = RD["S"]
        Sr = mp.matrix([[mp.conj(S[i, j]) for j in range(S.cols)] for i in range(S.rows)])
        Y = mp.matrix([[sum(((Ca.T * EPS * Sr * Cb)[m, n] * Mw[m, n] for m in range(2) for n in range(2)), mp.mpc(0)) for Cb in BLOCKS] for Ca in BLOCKS])
        s = sorted((abs(v) for v in mp.svd_c(Y, compute_uv=False)), reverse=True); out[sec] = (float(s[1] / s[0]), float(s[2] / s[0]))
    return out


if __name__ == "__main__":
    a = ratios_star("0", 1.0, W.MARK); b = ratios_star("0", 1.0, (Fr(2, 5), Fr(1, 5)))
    rm, _ = W.out("0", 1.0, W.MARK); s = {sec: rm[(sec, "S")] for sec in ("up", "down")}
    rel = lambda x, y: max(abs(x[k][i] / y[k][i] - 1) for k in x for i in (0, 1)); ab = lambda x, y: max(abs(x[k][i] - y[k][i]) for k in x for i in (0, 1))
    print("in S* the two crossings (i, mark) and (i, (2/5, 1/5)) differ: relative %.2f, absolute %.2f in the ratios" % (rel(a, b), ab(a, b)))
    print("(i, (2/5, 1/5)) in S* against (i, mark) in S: relative %.2f, absolute %.2f in the ratios" % (rel(b, s), ab(b, s)))
    print("(i, mark) in S* against (i, mark) in S: relative %.2f, absolute %.2f" % (rel(a, s), ab(a, s)))
