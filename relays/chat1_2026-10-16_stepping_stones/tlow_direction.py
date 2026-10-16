"""Which way T-low misses (a scoreboard on the sealed low-thread run's output, 09f41b453; the data were seen).

For the Standard Model's accepted configuration-cells in each reading: the median, over cells, of
ln(predicted ratio / observed ratio) for m1/m3 and m2/m3 in each sector (negative: the predicted hierarchy is
stronger than the observed one), the fraction of cells where it is positive, and the ratio of the predicted to the
observed log-ratio (ln m_i/m_3 predicted over observed: above 1 means too strong).
Usage: python3 -B tlow_direction.py <decompressed twisted_units_seal_output.json> > tlow_direction_run.txt
"""
import json, math, statistics as st, sys
o = json.load(open(sys.argv[1]))
tg = o["score"]["targets"]
d = o["score"]["SM per configuration-cell"]
for rd in ("per-field", "minimal"):
    xs = [x for x in d if x["reading"] == rd and x["accepted"]]
    print(f"{rd}: {len(xs)} accepted configuration-cells of the Standard Model")
    for sec in ("up", "down", "lepton"):
        row = []
        for i, key in ((1, "R1"), (2, "R2")):
            obs = tg[sec][key][0]
            lr = [math.log(x["z"][sec][key]) - math.log(obs) for x in xs]
            ratio = [math.log(x["z"][sec][key]) / math.log(obs) for x in xs]
            row.append(f"m{i}/m3: median ln(pred/obs) {st.median(lr):+.2f}, weaker in {sum(v > 0 for v in lr) / len(lr):.2f} "
                       f"of cells, median ln-ratio pred/obs {st.median(ratio):.2f}")
        print(f"  {sec:6s} " + "; ".join(row))
heights = sorted({r["height"] for r in o["records"]})
print(f"T-low's heights: {heights[0]:.3f} .. {heights[-1]:.3f}")
