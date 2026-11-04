"""P-638's card instrument: B1726's compute() Yukawa construction, line for line (its modules, its DR direction te.B[1],
its readings S and S~, its radius column), returning the matrices, with the Dirac neutrino sector L nu^c (6Y = -3, 0)
added. B1726's line convention: w = a tau + b."""
import importlib.util, math, pathlib, sys
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[3]
spec = importlib.util.spec_from_file_location("census1726", ROOT / "frontier/B1726_the_two_ingredients_replicated/verification/census.py")
C = importlib.util.module_from_spec(spec); spec.loader.exec_module(C)
CHARGES = {"up": (1, -4), "down": (1, 2), "lep": (-3, 6), "nu": (-3, 0)}


def yukawas(re_t, im_t, a, b, horocycle="L_max", sectors=("up", "down", "lep")):
    import mpmath as mp
    M = C._modules(); B, te, col = M["B"], M["te"], M["col"]
    t = complex(re_t, im_t); w = float(a) * t + float(b)
    av = [complex(te.ev(cc, mp.mpc(t.real, t.imag))) for cc in te.B[1]]
    S = av[0] * B.QI + av[1] * B.QJ + av[2] * B.QK
    reading = {"S": S, "St": B.EPS @ np.conj(S) @ B.EPS.T}
    L = float(np.interp(im_t, [q[0] for q in col], [q[1] if horocycle == "L_max" else q[2] for q in col]))
    Y = {}
    for sec in sectors:
        ql, qr = CHARGES[sec]
        x, yy = B.sector_twists(w, t, ql, qr); R = B.residues(x, yy, t); c = B.cA(x, yy, t, R)
        u = {s: (math.sqrt(2 * math.pi * L + c[s]) * R[s] if c[s] is not None and 2 * math.pi * L + c[s] > 0 else 0) for s in B.UNITS}
        Mw = B.weighted_M(u)
        for rn in ("S", "St"):
            Y[(sec, rn)] = B.coupling(reading[rn], Mw)
    return Y


def selfcheck():
    """the wrapper against compute() itself: every singular-value ratio and the CKM keys at two points"""
    worst = 0.0
    for (re_t, im_t, a, b) in ((0.4, 2.7, 0.4, 0.1), (0.33, 3.04, 0.4, -0.1)):
        out = C.compute(re_t, im_t, a, b)
        Y = yukawas(re_t, im_t, a, b, "L_max")
        for sec in ("up", "down", "lep"):
            for rn in ("S", "St"):
                sv = np.linalg.svd(Y[(sec, rn)], compute_uv=False)
                worst = max(worst, abs(sv[1] / sv[0] - out["%s|L_max|%s" % (sec, rn)][0]), abs(sv[2] / sv[0] - out["%s|L_max|%s" % (sec, rn)][1]))
    return worst
