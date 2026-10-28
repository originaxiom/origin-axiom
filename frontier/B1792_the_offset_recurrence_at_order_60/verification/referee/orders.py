import pathlib
import pickle, math
from fractions import Fraction as Fr
from collections import defaultdict
P = pickle.load(open(str(pathlib.Path(__file__).resolve().parent / "slope25.pkl"), "rb"))
rows, T, S = P["rows"], P["T"], P["S"]
L3 = math.log(3)
SEAT = [("St", "S", "S"), ("St", "St", "St")]
def best_at(rec):
    best = (math.inf, None)
    for h in ("L_max", "L_2"):
        for u, dn, l in SEAT:
            m = rec[h]["up" + u] + rec[h]["down" + dn] + rec[h]["lep" + l]
            for k in (0.0, L3):
                mm = m[:4] + [m[4] + k, m[5] - k]
                x = sum(((mm[i] - T[i]) / S[i]) ** 2 for i in range(6))
                if x < best[0]: best = (x, (h, u, dn, l, k))
    return best
lmin = defaultdict(lambda: (math.inf, None)); order = {}; src = {}
for (b, re, im), rec in rows.items():
    x, cfg = best_at(rec); order[b] = rec["order"]; src[b] = rec["src"]
    if x < lmin[b][0]: lmin[b] = (x, (re, im) + cfg)
byord = defaultdict(list)
for b in lmin: byord[order[b]].append(b)
print("order: lines, carriers(<16.75), rate; carriers")
for o in sorted(byord):
    bs = sorted(byord[o], key=Fr); car = [b for b in bs if lmin[b][0] < 16.75]
    npts = sum(1 for k in rows if k[0] in bs)
    print(" %2d (%s): %2d lines (%d pts), %d carry (%.0f%%): %s" % (o, src[bs[0]], len(bs), npts, len(car), 100 * len(car) / len(bs), car))
print("\nshift inheritance: base line (order N) -> b+1/3, b+2/3 (order 3N)")
for o in (5, 10, 20):
    for b in sorted(byord[o], key=Fr):
        s1, s2 = str((Fr(b) + Fr(1, 3)) % 1), str((Fr(b) + Fr(2, 3)) % 1)
        print("  %2d %-5s %6.2f %s -> %-6s %6.2f %s, %-6s %6.2f %s" % (o, b, lmin[b][0], "C" if lmin[b][0] < 16.75 else ".", s1, lmin[s1][0], "C" if lmin[s1][0] < 16.75 else ".", s2, lmin[s2][0], "C" if lmin[s2][0] < 16.75 else "."))
pickle.dump({"lmin": dict(lmin), "order": order}, open(str(pathlib.Path(__file__).resolve().parent / "lmin.pkl"), "wb"))
