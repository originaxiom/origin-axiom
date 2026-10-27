"""B1789 after its referee (data-free): the frame's own double ratio D_frame = R2 R1 (R2 = (m2/m3)_e/(m2/m3)_d,
R1 = (m1/m3)_d/(m1/m3)_e; the seat's readings: down S, leptons S; no c) on the slope-2/5 rows of B1786's census (orders 25,
30) and B1755's (orders 13-20): its range at the band's height.  Exact c = 3 multiplies D by 9, so 9 D_frame is what an
exact Georgi-Jarlskog factor gives here.  No measured value is read.  (B1786's raw census: gunzip -k census.jsonl.gz.)"""
import json, pathlib
import numpy as np
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
HERE = pathlib.Path(__file__).resolve().parent
CEN = {"B1786": ROOT / "frontier/B1786_the_slope_principle_out_of_sample/verification/census.jsonl",
       "B1755": ROOT / "frontier/B1755_the_six_on_the_lines_of_order_13_to_20/verification/census.jsonl"}
out = {}
for tag, p in CEN.items():
    R2s, R1s = [], []
    with open(p, encoding="utf-8") as fh:
        for l in fh:
            r = json.loads(l)
            if r["alpha"] != "2/5": continue
            for h in ("L_max", "L_2"):
                d, e = r["down|%s|S" % h], r["lep|%s|S" % h]
                if min(d + e) <= 0: continue
                R2s.append(e[0] / d[0]); R1s.append(d[1] / e[1])
    R2, R1 = np.array(R2s), np.array(R1s); D = R2 * R1
    q = lambda v: [round(float(x), 3) for x in np.quantile(v, [0, .01, .1, .5, .9, .99, 1])]
    out[tag] = dict(rows=int(len(D)), R2_quantiles_0_1_10_50_90_99_100=q(R2), R1_quantiles=q(R1), D_quantiles=q(D),
                    nine_D_quantiles=[round(9 * x, 2) for x in q(D)], R1_above_2=int((R1 > 2).sum()))
    print(tag, json.dumps(out[tag]))
json.dump(out, open(HERE / "d_frame_band.json", "w"), indent=1)
