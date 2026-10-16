"""W95, POST HOC (labelled; written after the read-out of the_traces_by_discriminant.json, committed before its run).
It reads the committed output and evaluates no instrument value.

  PH1  V4's rank law at the instrument's floor: V3 puts the pointwise sigma2/sigma1 at 1.0e-37, so a ratio above 1e-33
       is read as a mass. Count how many D < 0 then follow rank = min(3, n_D), apart from omega and i.
  PH2  the classes' true heights: H_true = sqrt(D) / (2 m), with m the least |Q(x, y)| over primitive (x, y) in a box
       (the least |a| over the class). Which classes had H (from the Zagier cycle) below H_true, and is V6's one
       failure among them?
  PH3  V8 with the true heights: compare each D-trace (D in [100, 300], two or more classes) with a class of the
       largest H_true. This is valid when those classes are one geodesic in two orientations (equal masses), which
       is checked.
  PH4  the law in D against the data: the least Euclidean distance, over D > 0, from the D-trace's
       (ln m1/m3, ln m2/m3) to each sector's data point; kappa at the largest D. A read-out, no claim.

Run: python3 the_traces_by_discriminant_posthoc.py  ->  the_traces_by_discriminant_posthoc.json beside it.
"""
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
d = json.loads((HERE / "the_traces_by_discriminant.json").read_text(encoding="utf-8"))
OUT = HERE / "the_traces_by_discriminant_posthoc.json"


def least_value(a, b, c, box=400):
    best = None
    for x in range(-box, box + 1):
        for y in range(0, box + 1):
            if (x, y) == (0, 0) or math.gcd(x, y) != 1 or (y == 0 and x < 0):
                continue
            v = abs(a * x * x + b * x * y + c * y * y)
            if v and (best is None or v < best):
                best = v
    return best


def main():
    out = {"status": "POST HOC, labelled; reads the committed output only"}
    # PH1
    rows, ok = [], 0
    for D, r in d["V4"]["by D"].items():
        if "K rank" in r:
            rows.append({"D": int(D), "n_D": r["n_D"], "K rank": r["K rank"], "law": "masses undefined"})
            continue
        r1, r2 = float(r["m1/m3"]), float(r["m2/m3"])
        rank = 1 + (r2 > 1e-33) + (r1 > 1e-33)
        good = rank == min(3, r["n_D"])
        ok += good
        rows.append({"D": int(D), "n_D": r["n_D"], "rank at 1e-33": rank, "law holds": bool(good)})
    out["PH1"] = {"D < 0 with masses defined": sum(1 for x in rows if "law holds" in x), "law holds": ok,
                  "failures": [x for x in rows if x.get("law holds") is False], "undefined": [x for x in rows
                                                                                  if "K rank" in x]}
    # PH2
    under = []
    for c in d["classes"]:
        m = least_value(*c["form"])
        c["H_true"] = math.sqrt(c["D"]) / (2 * m)
        if c["H_true"] > c["H"] * (1 + 1e-12):
            under.append({"D": c["D"], "form": c["form"], "H used": c["H"], "H_true": c["H_true"],
                          "r_calc": c.get("r_calc")})
    worst = max(d["classes"], key=lambda c: c.get("r_calc", 0))
    out["PH2"] = {"classes with H below H_true": len(under), "of": len(d["classes"]),
                  "V6's worst class": {"D": worst["D"], "form": worst["form"], "H used": worst["H"],
                                       "H_true": worst["H_true"], "r_calc": worst["r_calc"]},
                  "V6's worst class under-resolved": bool(worst["H_true"] > worst["H"] * (1 + 1e-12)),
                  "under-resolved classes with r_calc > 1e-6": [u for u in under if (u["r_calc"] or 0) > 1e-6],
                  "largest r_calc among correctly sized classes": max((c.get("r_calc", 0) for c in d["classes"]
                                                                       if c["H_true"] <= c["H"] * (1 + 1e-12)))}
    # PH3
    ph3, held, tested, twins_ok = [], 0, 0, True
    for D, r in d["D-traces"].items():
        idx = [c for c in d["classes"] if c["D"] == int(D)]
        if not (100 <= int(D) and len(idx) >= 2) or "ln m1/m3" not in r:
            continue
        hmax = max(c["H_true"] for c in idx)
        top = [c for c in idx if abs(c["H_true"] - hmax) < 1e-12 * hmax]
        same = all(abs(float(c["ln m1/m3"]) - float(top[0]["ln m1/m3"])) < 1e-20 and
                   abs(float(c["ln m2/m3"]) - float(top[0]["ln m2/m3"])) < 1e-20 for c in top)
        twins_ok = twins_ok and same
        dd = max(abs(float(top[0]["ln m1/m3"]) - float(r["ln m1/m3"])),
                 abs(float(top[0]["ln m2/m3"]) - float(r["ln m2/m3"])))
        tested += 1
        held += dd < 1e-3
        ph3.append({"D": int(D), "classes": len(idx), "highest (true)": len(top), "one geodesic": same,
                    "|trace - highest|": dd})
    out["PH3"] = {"tested": tested, "within 1e-3": held, "highest classes one geodesic in every D": twins_ok,
                  "largest gap": max(x["|trace - highest|"] for x in ph3), "rows": ph3}
    # PH4
    data = d["read-outs"]["data (seen; sector-blind frame; no null; no claim)"]
    pts = [(int(D), float(r["ln m1/m3"]), float(r["ln m2/m3"])) for D, r in d["D-traces"].items() if "ln m1/m3" in r]
    ph4 = {}
    for sec, v in data.items():
        best = min(pts, key=lambda p: math.hypot(p[1] - v["ln m1/m3"], p[2] - v["ln m2/m3"]))
        ph4[sec] = {"data": [v["ln m1/m3"], v["ln m2/m3"]], "nearest D": best[0], "its point": [best[1], best[2]],
                    "distance": math.hypot(best[1] - v["ln m1/m3"], best[2] - v["ln m2/m3"]), "data kappa": v["kappa"]}
    top_d = max(pts)
    ph4["kappa at the largest D"] = {"D": top_d[0], "kappa": top_d[1] / top_d[2]}
    out["PH4"] = ph4
    OUT.write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
    print({"PH1": [out["PH1"]["law holds"], out["PH1"]["D < 0 with masses defined"]],
           "PH2": [out["PH2"]["classes with H below H_true"], out["PH2"]["V6's worst class under-resolved"]],
           "PH3": [held, tested, twins_ok],
           "PH4": {k: round(v["distance"], 2) for k, v in ph4.items() if "distance" in v}})


if __name__ == "__main__":
    main()
