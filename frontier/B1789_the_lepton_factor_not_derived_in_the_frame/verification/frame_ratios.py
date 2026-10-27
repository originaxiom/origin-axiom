"""P-294 design study (data-free): the frame's OWN lepton-to-down ratios, no lepton factor, on B1786's census (B1749's 125
apexes x the 588 lines of order 25 and 30) and on B1755's (orders 13, 14, 15, 20), the seat's reading for both sectors (S):
    R2 = (m2/m3)_lep / (m2/m3)_down,  R1 = (m1/m3)_down / (m1/m3)_lep,  D_frame = R2 * R1.
Georgi-Jarlskog's structure would be R2 = 3, R1 = 3, D = 9 (the lepton factor c = 3 supplies exactly that by hand).
No measured value is read.  Writes frame_ratios.json."""
import json, gzip, math, pathlib, statistics
from fractions import Fraction as Fr
from collections import defaultdict
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
HERE = pathlib.Path(__file__).resolve().parent
CENSUSES = {"B1786": ROOT / "frontier/B1786_the_slope_principle_out_of_sample/verification/census.jsonl",
            "B1755": ROOT / "frontier/B1755_the_six_on_the_lines_of_order_13_to_20/verification/census.jsonl"}


def rows(p):
    with open(p, encoding="utf-8") as fh:
        for l in fh:
            if l.strip(): yield json.loads(l)


def q(v, ps=(0.1, 0.25, 0.5, 0.75, 0.9)):
    v = sorted(v); n = len(v); return [round(v[min(n - 1, int(p * n))], 3) for p in ps]


out = {}
for name, path in CENSUSES.items():
    by = defaultdict(lambda: {"lR2": [], "lR1": [], "lD": []}); per_line = defaultdict(list); n = 0
    for r in rows(path):
        a = str(r["alpha"]); cls = "a2/5" if a == "2/5" else ("a1/10" if a == "1/10" else "rest")
        for h in ("L_max", "L_2"):
            d2, d1 = r["down|%s|S" % h]; e2, e1 = r["lep|%s|S" % h]
            if min(d2, d1, e2, e1) <= 1e-300: continue
            lR2 = math.log(e2 / d2); lR1 = math.log(d1 / e1); lD = lR2 + lR1
            for k in (cls, "all"):
                by[k]["lR2"].append(lR2); by[k]["lR1"].append(lR1); by[k]["lD"].append(lD)
            if cls == "a2/5": per_line[(r["order"], str(r["b"]))].append((lR2, lR1))
        n += 1
    res = {"rows": n}
    for k, v in by.items():
        res[k] = {"n": len(v["lR2"]),
                  "log_R2_q10_25_50_75_90": q(v["lR2"]), "log_R1_q10_25_50_75_90": q(v["lR1"]), "log_D_q10_25_50_75_90": q(v["lD"]),
                  "frac_R2_and_R1_within_10pc_of_3": round(sum(1 for x, y in zip(v["lR2"], v["lR1"]) if abs(x - math.log(3)) < 0.0953 and abs(y - math.log(3)) < 0.0953) / len(v["lR2"]), 6),
                  "frac_D_within_10pc_of_1": round(sum(1 for x in v["lD"] if abs(x) < 0.0953) / len(v["lD"]), 4),
                  "frac_D_within_10pc_of_9": round(sum(1 for x in v["lD"] if abs(x - math.log(9)) < 0.0953) / len(v["lD"]), 4)}
    res["a2/5_per_line_median_R2_R1"] = {"%s %s" % k: [round(math.exp(statistics.median(x for x, _ in v)), 4), round(math.exp(statistics.median(y for _, y in v)), 4),
                                                       round(max(abs(x) for x, _ in v), 6), round(max(abs(y) for _, y in v), 6)]
                                         for k, v in sorted(per_line.items(), key=lambda kv: (kv[0][0], Fr(kv[0][1])))}
    out[name] = res
    print("==", name, "rows", n)
    for k in ("a2/5", "a1/10", "rest", "all"):
        if k in res: print("  %-6s" % k, {kk: vv for kk, vv in res[k].items()})
    print("  slope-2/5 lines: line -> [median R2, median R1, max |log R2|, max |log R1|]")
    for k, v in res["a2/5_per_line_median_R2_R1"].items(): print("    ", k, v)
json.dump(out, open(HERE / "frame_ratios.json", "w"), indent=1)
