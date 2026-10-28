import pathlib
"""stream every committed census at B1749's apexes, keep slope-2/5 rows, store per (b, apex, horocycle) the seat-menu best and the logs"""
import json, math, pickle, sys
R = str(next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file()) / "frontier/")
SRC = {"B1749": R + "B1749_the_six_at_fresh_apexes/verification/census.jsonl",
       "B1755": R + "B1755_the_six_on_the_lines_of_order_13_to_20/verification/census.jsonl",
       "B1786": R + "B1786_the_slope_principle_out_of_sample/verification/census.jsonl",
       "B1792": R + "B1792_the_offset_recurrence_at_order_60/verification/census.jsonl"}
d = json.load(open(R + "B1637_fits_on_the_ruled_branch/received/HZ2021_running_masses_MZ.json"))["masses_GeV"]
v, e = d["value"], d["sigma"]
pr = [("c", "t"), ("u", "t"), ("s", "b"), ("d", "b"), ("mu", "tau"), ("e", "tau")]
T = [math.log(v[a] / v[b]) for a, b in pr]
S = [math.sqrt((e[a] / v[a]) ** 2 + (e[b] / v[b]) ** 2 + 0.01) for a, b in pr]
L3 = math.log(3)
out = {}
for name, path in SRC.items():
    n = 0
    with open(path) as fh:
        for l in fh:
            if '"alpha": "2/5"' not in l: continue
            r = json.loads(l)
            if r.get("alpha") != "2/5": continue
            n += 1
            key = (r["b"], round(r["Re_tau"], 9), round(r["Im_tau"], 9))
            rec = {"order": r["order"], "src": name}
            for h in ("L_max", "L_2"):
                rec[h] = {sec + rd: [math.log(max(x, 1e-300)) for x in r[f"{sec}|{h}|{rd}"]] for sec in ("up", "down", "lep") for rd in ("S", "St")}
            out[key] = rec
    print(name, "slope-2/5 rows", n, flush=True)
pickle.dump({"rows": out, "T": T, "S": S}, open(str(pathlib.Path(__file__).resolve().parent / "slope25.pkl"), "wb"))
