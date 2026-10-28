"""B1795, post hoc (labelled; after the sealed outputs were committed and read once): the D pair against the H pair, row by
row -- the lightest state's ratio sv3/sv1 for each (point, horocycle, reading), the better slot order of each pair; at the
strip on the six's carriers and on all lines; and Dn's ratio.  Reads split_rows.jsonl only.
    python3 -B pair_compare.py"""
import json, math, pathlib, statistics
HERE = pathlib.Path(__file__).resolve().parent
rows = [json.loads(l) for l in (HERE.parent / "split_rows.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
CARR = {("2/5", "11/12"), ("2/5", "29/60"), ("2/5", "41/60"), ("2/5", "47/60"), ("2/5", "49/60"), ("2/5", "7/60")}
def light(r, ps, h, rn): return min(r[p]["sv|%s|%s" % (h, rn)][2] / r[p]["sv|%s|%s" % (h, rn)][0] for p in ps)
for label, sel in (("strip, the six's carriers", lambda r: r["point"] == "strip" and (r["a"], r["b"]) in CARR),
                   ("strip, all 286 lines", lambda r: r["point"] == "strip"),
                   ("generic points, all lines", lambda r: r["point"] != "strip")):
    rs = [r for r in rows if sel(r)]; lr = []
    for r in rs:
        for h in ("L_max", "L_2"):
            for rn in ("S", "St"):
                lD, lH = light(r, ("D", "Dc"), h, rn), light(r, ("H", "Hc"), h, rn)
                lr.append(math.log10(lH / lD))
    dn = [math.log10(max(r["H"]["Dn"], r["Hc"]["Dn"]) / max(r["D"]["Dn"], r["Dc"]["Dn"])) for r in rs]
    print("%-28s rows %4d | log10(light_H / light_D): median %+.3f, 5%% %+.3f, 95%% %+.3f, min %+.3f, max %+.3f | log10(Dn_H/Dn_D) median %+.3f" % (
        label, len(rs), statistics.median(lr), sorted(lr)[int(0.05 * len(lr))], sorted(lr)[int(0.95 * len(lr)) - 1], min(lr), max(lr), statistics.median(dn)))
st = [r for r in rows if r["point"] == "strip" and (r["a"], r["b"]) in CARR]
for r in sorted(st, key=lambda r: r["b"]):
    print("  carrier (%s, %s): light_H %s | light_D %s  (L_max S, L_max St, L_2 S, L_2 St)" % (r["a"], r["b"],
          " ".join("%.1e" % light(r, ("H", "Hc"), h, rn) for h in ("L_max", "L_2") for rn in ("S", "St")),
          " ".join("%.1e" % light(r, ("D", "Dc"), h, rn) for h in ("L_max", "L_2") for rn in ("S", "St"))))
print("pair_compare exit 0")
