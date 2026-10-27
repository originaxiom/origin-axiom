"""B1788: the 40-digit runs (mpframe.py / run_high.py, the referee's independent code) against the closed form: for each
(line, sector) the last local exponent (Im tau 14-16, or the highest pair run) beside tropical.predict, both readings."""
import json, math, sys, pathlib
from fractions import Fraction as Fr
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import tropical as T
P = {rd: T.polys(rd) for rd in ("S", "St")}
rows = [json.loads(l) for f in ("high_main.jsonl", "high_ext.jsonl", "high_tie.jsonl", "h211.jsonl") for l in open(HERE / f)]
keys = sorted({(r["a"], r["b"], r["sec"]) for r in rows if r["nth"] == 96})
out = []
for k in keys:
    rs = {}
    for r in rows:
        if (r["a"], r["b"], r["sec"]) == k and r["nth"] == 96: rs[r["y"]] = r
    ys = sorted(rs)
    a = Fr(k[0]); ql, qr = (T.SIXY[f] for f in T.SECTORS[k[2]]); mu = T.E(ql * a, qr * a)
    for rd in ("S", "St"):
        e2, e3 = T.predict(P[rd], mu)
        for idx, nm, pe in ((0, "m2/m3", e2), (1, "m1/m3", e3)):
            v = [math.log(float(rs[y][rd][idx])) for y in ys]
            last = -(v[-1] - v[-2]) / (2 * math.pi * (ys[-1] - ys[-2]))
            out.append(dict(line=list(k[:2]), sector=k[2], reading=rd, ratio=nm, heights=[ys[-2], ys[-1]], local=round(last, 4), closed=str(pe), diff=round(last - float(pe), 4)))
            print("(%s, %s) %-4s %-2s %s  Im tau %g-%g  local %.4f  closed %s = %.4f  diff %+.4f" % (k[0], k[1], k[2], rd, nm, ys[-2], ys[-1], last, pe, float(pe), last - float(pe)))
json.dump(out, open(HERE / "compare_closed.json", "w"), indent=1)
