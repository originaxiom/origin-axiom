"""Closed-form check: the window failures at higher Im tau (10, 12, 14), same instrument (L clamped as in B1726's compute)."""
import sys, math, json, numpy as np
from fractions import Fraction as Fr
import layers as L, tropical as T
L.H = (10.0, 12.0, 14.0)
X = np.array([2*math.pi*y for y in L.H])
def fit(v):
    Y = np.log(np.maximum(np.abs(np.asarray(v)),1e-300)); A = np.vstack([X,np.ones(3)]).T
    (s,c),*_ = np.linalg.lstsq(A,Y,rcond=None); return float(-s)
P = {rd: T.polys(rd) for rd in ("S","St")}
cases = [tuple(c.split(":")) for c in sys.argv[1].split(",")]
out = []
for a, b, sec, rd in cases:
    hs = [L.one(Fr(a), Fr(b), sec, y) for y in L.H]
    e2 = fit([h[rd][0] for h in hs]); e3 = fit([h[rd][1] for h in hs])
    lf, rf = T.SECTORS[sec]; p2, p3 = T.predict(P[rd], T.E(T.SIXY[lf]*Fr(a), T.SIXY[rf]*Fr(a)))
    out.append((a, b, sec, rd, round(e2,3), str(p2), round(e3,3), str(p3)))
    print(a, b, sec, rd, "m2/m3 high-fit %.3f closed %s | m1/m3 high-fit %.3f closed %s" % (e2, p2, e3, p3), flush=True)
json.dump(out, open("high_%s.json" % sys.argv[2], "w"))
