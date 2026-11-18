"""(2026-11-18, at the physical lane's C22 intake: main's sm_c22.py evaluates the theta entries at 60 digits and casts them to double
before its SVD; this is the same S3 with the SVD at 60 digits.) main's checks/sm_c22.py, S3, for h* with the SVD at 60 digits (the committed check casts the 60-digit entries to double
before its SVD): the median exponents E(s3/s1) over the 24 points, down and up, from heights 8 -> 10, and (E2, E3) at the mark."""
import sys, math, functools
from fractions import Fraction as Fr
print = functools.partial(print, flush=True)
HERE = __import__("pathlib").Path(__file__).resolve().parent; sys.path.insert(0, str(HERE))
import importlib.util
spec = importlib.util.spec_from_file_location("smc22src", str(HERE / "sm_c22.py"))
src = open(spec.origin).read(); head = src[:src.index("def Ymp(")]          # the imports and the point list only
g = {"__name__": "smc22src", "__file__": spec.origin}; exec(compile(head, spec.origin, "exec"), g)
CC, P5, MARK = g["CC"], g["P5"], g["MARK"]
import mpmath as mp
mp.mp.dps = 60
hs = [mp.mpf(1) / mp.sqrt(2), mp.exp(1j * mp.pi / 12) / 2, 0, 0, 0, mp.exp(1j * mp.pi / 12) / 2]; nrm = mp.sqrt(sum(abs(x) ** 2 for x in hs)); hs = [x / nrm for x in hs]
E3 = {"up": [], "down": []}; Em = {}
for idx, (a, b) in enumerate(P5):
    sv = {}
    for hy in (8, 10):
        tau = mp.mpc("0.13", hy); wv = mp.mpf(a.numerator) / a.denominator * tau + mp.mpf(b.numerator) / b.denominator
        for s, xi in (("up", mp.mpf(5) / 2 * wv), ("down", -wv / 2)):
            d = CC.Y_mp(tau, xi, dps=60)
            M = mp.matrix([[sum(d.get((i, j, k), 0) * hs[k] for k in range(6)) for j in range(3)] for i in range(3)])
            sv[(hy, s)] = sorted((abs(x) for x in mp.svd_c(M, compute_uv=False)), reverse=True)
    for s in ("up", "down"):
        E = [float(-(mp.log(sv[(10, s)][r] / sv[(10, s)][0]) - mp.log(sv[(8, s)][r] / sv[(8, s)][0])) / (2 * mp.pi)) for r in (1, 2)]
        E3[s].append(E[1])
        if idx == MARK: Em[s] = [round(x, 4) for x in E]
med = lambda v: sorted(v)[len(v) // 2 - 1: len(v) // 2 + 1]
print("S3mp: h* with the SVD at 60 digits: median E(s3/s1) down %.4f, up %.4f; at the mark (E2, E3): %s" % (sum(med(E3["down"])) / 2, sum(med(E3["up"])) / 2, Em))
