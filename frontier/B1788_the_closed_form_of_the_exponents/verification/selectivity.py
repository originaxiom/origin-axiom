"""How selective is the near-tie flag: the fraction of agreeing vs disagreeing cases (non-degenerate) whose tropical minima
have a competitor within the gap G, for several G."""
import json
from fractions import Fraction as Fr
import tropical as T, classify as C
import pathlib
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
P = {rd: T.polys(rd) for rd in ("S", "St")}
d = json.load(open(ROOT / "frontier/B1785_the_slope_sets_the_exponents/verification/exponents.json"))
rec = []
for r in d:
    a, b = Fr(r["alpha"]), Fr(r["b"])
    for sec, (lf, rf) in T.SECTORS.items():
        ql, qr = T.SIXY[lf], T.SIXY[rf]
        if C.torsion_deg(a, b, ql, qr): continue
        mu = T.E(ql * a, qr * a)
        for rd in ("S", "St"):
            e2, e3 = T.predict(P[rd], mu); g1, g12, g3 = C.gaps(P[rd], mu)
            for nm, pe, rel in (("m2/m3", e2, (g1, g12)), ("m1/m3", e3, (g1, g12, g3))):
                obs = r["%s|L_max|%s|%s" % (sec, rd, nm)]["exponent"]
                rec.append([abs(obs - float(pe)) <= 0.05, float(min(rel)), sec, rd, nm, r["alpha"], round(obs - float(pe), 3)])
for G in (0.01, 0.02, 0.03, 0.04, 0.06):
    ok = [x for x in rec if x[0]]; bad = [x for x in rec if not x[0]]
    print("gap < %.2f: agreeing %d/%d near-tie (%.0f%%); disagreeing %d/%d (%.0f%%)" % (
        G, sum(x[1] < G for x in ok), len(ok), 100 * sum(x[1] < G for x in ok) / len(ok), sum(x[1] < G for x in bad), len(bad), 100 * sum(x[1] < G for x in bad) / len(bad)))
print("disagreeing: sign of (obs - closed):", sum(x[6] < 0 for x in rec if not x[0]), "below,", sum(x[6] > 0 for x in rec if not x[0]), "above")
for a0 in ("2/5", "1/10"):
    print(a0, "seat reading:", sorted(set((x[2], x[3], x[4], round(x[1], 3), x[0]) for x in rec if x[5] == a0 and (x[2], x[3]) in (("up", "St"), ("down", "S"), ("lep", "S")))))
json.dump(rec, open("selectivity.json", "w"))
