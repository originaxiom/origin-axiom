import json, math, pickle
from fractions import Fraction as Fr
R = str(next(q for q in __import__("pathlib").Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())) + "/"
allrows = pickle.load(open(str(__import__("pathlib").Path(__file__).resolve().parent) + "/allrows.pkl", "rb"))
# allrows: (x, b, apex, Re, Im, h, cfg, c, parts, m)
by = {}
for rec in allrows:
    key = (rec[1], rec[2], rec[5])
    if key not in by or rec[0] < by[key][0]: by[key] = rec
def show(b, apex, h="L_max"):
    x = by[(b, apex, h)]
    p = x[8]
    reW = float(Fr(2, 5)) * x[3] + float(Fr(b))
    print("  %-6s apex %3d (Re %.4f) %s %-9s c=%d chi %.2f  up %.2f down %.2f lep %.2f  [%s]  3ReW mod1 %.4f" % (b, apex, x[3], h, "/".join(x[6]), x[7], x[0], p[0] + p[1], p[2] + p[3], p[4] + p[5], " ".join("%.2f" % q for q in p), (3 * reW) % 1))
for apex in (101, 102, 103, 104, 106):
    print("apex", apex)
    for b in ("1/60", "41/60", "7/12", "11/12", "7/60", "47/60", "29/60", "49/60"):
        show(b, apex)
# 1/60's top rows overall
print("1/60's ten best (apex, horocycle) rows")
L = sorted([v for k, v in by.items() if k[0] == "1/60"], key=lambda v: v[0])[:10]
for x in L: print("  %.2f apex %d Re %.4f Im %.4f %s %s c=%d parts %s" % (x[0], x[2], x[3], x[4], x[5], "/".join(x[6]), x[7], [round(q, 2) for q in x[8]]))
for h in ("L_max", "L_2"):
    print("1/60 best on", h, "%.2f" % min(v[0] for k, v in by.items() if k[0] == "1/60" and k[2] == h), " 41/60:", "%.2f" % min(v[0] for k, v in by.items() if k[0] == "41/60" and k[2] == h))
