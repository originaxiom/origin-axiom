import pathlib
import pickle, math
from fractions import Fraction as Fr
P = pickle.load(open(str(pathlib.Path(__file__).resolve().parent / "slope25.pkl"), "rb"))
rows = P["rows"]; M = pickle.load(open(str(pathlib.Path(__file__).resolve().parent / "lmin.pkl"), "rb"))
lmin, order = M["lmin"], M["order"]
strip = sorted({lmin[b][1][:2] for b in lmin if lmin[b][0] < 16.75})
S = P["S"]
def d6(b1, b2):
    """over the strip apexes, reading (St, S), L_max: max |dlog| of the four quark ratios, and the max sigma-weighted shift"""
    w, ws = 0.0, 0.0
    for (re, im) in strip:
        r1, r2 = rows[(b1, re, im)]["L_max"], rows[(b2, re, im)]["L_max"]
        q1 = r1["upSt"] + r1["downS"]; q2 = r2["upSt"] + r2["downS"]
        dd = [abs(p - q) for p, q in zip(q1, q2)]
        w = max(w, max(dd)); ws = max(ws, max(x / s for x, s in zip(dd, S[:4])))
    return w, ws
for o in (10, 20):
    for b in sorted([b for b in order if order[b] == o], key=Fr):
        if lmin[b][0] >= 16.75: continue
        for s in (str((Fr(b) + Fr(1, 3)) % 1), str((Fr(b) + Fr(2, 3)) % 1)):
            w, ws = d6(b, s)
            print("  %2d %-5s (%.2f) -> %-6s (%.2f): strip, L_max, (St,S): max |dlog quark| %.2f = %.1f sigma" % (o, b, lmin[b][0], s, lmin[s][0], w, ws))
# the two shift partners of one base, against each other
print("partners against each other (b+1/3 vs b+2/3):")
for o in (10, 20):
    for b in sorted([b for b in order if order[b] == o], key=Fr):
        if lmin[b][0] >= 16.75: continue
        s1, s2 = str((Fr(b) + Fr(1, 3)) % 1), str((Fr(b) + Fr(2, 3)) % 1)
        w, ws = d6(s1, s2); print("  %-6s vs %-6s %.2f = %.1f sigma" % (s1, s2, w, ws))
