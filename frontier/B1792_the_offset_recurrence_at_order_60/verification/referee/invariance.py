import pathlib
import pickle, math
from fractions import Fraction as Fr
from collections import defaultdict
P = pickle.load(open(str(pathlib.Path(__file__).resolve().parent / "slope25.pkl"), "rb"))
rows = P["rows"]; M = pickle.load(open(str(pathlib.Path(__file__).resolve().parent / "lmin.pkl"), "rb"))
lmin, order = M["lmin"], M["order"]
apx = sorted({(k[1], k[2]) for k in rows})
strip = sorted({lmin[b][1][:2] for b in lmin if lmin[b][0] < 16.75})
print("apexes", len(apx), "; strip apexes (where some slope-2/5 carrier's best row sits):", len(strip), strip)
def diff(b1, b2, sec, pts, rd=("S", "St")):
    w = 0.0
    for (re, im) in pts:
        r1, r2 = rows[(b1, re, im)], rows[(b2, re, im)]
        for h in ("L_max", "L_2"):
            for x in rd:
                w = max(w, max(abs(p - q) for p, q in zip(r1[h][sec + x], r2[h][sec + x])))
    return w
print("max |dlog| base vs shift, (all apexes) / [strip apexes, L_max+L_2, both readings]")
for o in (5, 10, 20):
    for b in sorted([b for b in order if order[b] == o], key=Fr):
        for s in (str((Fr(b) + Fr(1, 3)) % 1), str((Fr(b) + Fr(2, 3)) % 1)):
            print("  %2d %-5s -> %-6s up %.2f [%.2f] down %.2f [%.2f] lep %.1e [%.1e]" % (o, b, s, diff(b, s, "up", apx), diff(b, s, "up", strip), diff(b, s, "down", apx), diff(b, s, "down", strip), diff(b, s, "lep", apx), diff(b, s, "lep", strip)))
