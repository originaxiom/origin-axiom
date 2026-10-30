import math
import numpy as np
from fractions import Fraction as Fr
from frame_lib import *
E = EPS
for im in (2.5, 6.0):
    t = complex(1/3, im)
    S, _ = S_of(t)
    base = sector_M(t, Fr(1, 8), 0.0, "down")
    def sv(Y): return np.linalg.svd(Y, compute_uv=False)
    pairs = [
        ("lep(1/8) vs down(1/8; e^T S e)", sector_M(t, Fr(1, 8), 0.0, "lep"), E.T @ S @ E),
        ("down(3/8) vs down(1/8; e^T S)", sector_M(t, Fr(3, 8), 0.0, "down"), E.T @ S),
        ("lep(3/8) vs down(1/8; S e)", sector_M(t, Fr(3, 8), 0.0, "lep"), S @ E),
    ]
    print("Im tau", im, "base c:", {k: round(v, 6) for k, v in base["c"].items()})
    for name, P, S2 in pairs:
        a = sv(Ymat(S, P["M"])); b_ = sv(Ymat(S2, base["M"]))
        print("  ", name, "max rel diff of singular values:", float(np.max(np.abs(a - b_) / np.abs(a))), " c:", {k: round(v, 6) for k, v in P["c"].items()})
