"""Referee: reading S~ = eps S* eps^T for down and leptons on slope 2/5, two lines, three heights (own pipeline)."""
import sys, math, json
from multiprocessing import Pool
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))
import numpy as np
from fractions import Fraction as Fr
import recompute as RC

def one(task):
    import mpmath as mp
    B, te, col = RC.mods()
    re_t, im_t, a, b = task
    t = complex(re_t, im_t); w = float(Fr(a)) * t + float(Fr(b))
    hv = [complex(te.ev(c, mp.mpc(t.real, t.imag))) for c in te.B[1]]
    S = hv[0] * B.QI + hv[1] * B.QJ + hv[2] * B.QK; St = B.EPS @ np.conj(S) @ B.EPS.T
    L = float(np.interp(im_t, [q[0] for q in col], [q[1] for q in col]))
    res = {}
    for sec, (lf, rf) in (("down", ("Q", "d")), ("lep", ("L", "e"))):
        x, y = B.twist_of(B.SIXY[lf] * w, t), B.twist_of(B.SIXY[rf] * w, t)
        R = B.residues(x, y, t); c = B.cA(x, y, t, R)
        u = {s: (math.sqrt(2 * math.pi * L + c[s]) * R[s] if c[s] is not None and 2 * math.pi * L + c[s] > 0 else 0) for s in B.UNITS}
        sv = np.linalg.svd(B.coupling(St, B.weighted_M(u)), compute_uv=False); res[sec] = (sv[1] / sv[0], sv[2] / sv[0])
    R2 = res["lep"][0] / res["down"][0]; R1 = res["down"][1] / res["lep"][1]
    return (a, b, re_t, im_t, R2, R1, R2 * R1)

if __name__ == "__main__":
    T = [(0.3, y, "2/5", b) for b in ("1/10", "23/30") for y in (3.0, 6.0, 8.0)]
    with Pool(4) as P:
        for r in P.map(one, T): print("S~  a %s b %-5s tau %.2f+%.1fi  R2 %.4f R1 %.4f D %.4f" % r)
