#!/usr/bin/env python3
"""POST HOC, not a cell: W120's A3 and A4 failed as worded, because the rule read SnapPy's b-+w as the orientable
bundle with monodromy -w. The run shows b-+LR is m001, which is non-orientable. This check reads SnapPy's notation from
the manifolds themselves: is_orientable() for b++, b+-, b-+ and b-- at LR. It then takes the orientable bundles of
both trace signs over the same census words (length 2 to 10) and finds where the least volume sits. Written and run
after the W120 output was read; labelled post hoc throughout.

    python3 -B the_three_to_four_posthoc.py      # writes the_three_to_four_posthoc.json beside itself
"""
import json
from pathlib import Path

import snappy

HERE = Path(__file__).resolve().parent
run = json.loads((HERE / "the_three_to_four.json").read_text(encoding="utf-8"))
words = sorted({r["word"] for r in run["census"]}, key=lambda w: (len(w), w))

notation = {}
for p in ("b++", "b+-", "b-+", "b--"):
    M = snappy.Manifold(p + "LR")
    notation[p + "LR"] = {"orientable": M.is_orientable(), "volume": float(M.volume()),
                          "identify": [str(m) for m in M.identify()],
                          "trace of the monodromy's sign read from the name": p[2]}

rows = []
for w in words:
    for p in ("b++", "b+-"):
        M = snappy.Manifold(p + w)
        v = float(M.volume())
        rows.append({"word": w, "name": p + w, "orientable": M.is_orientable(), "solution": M.solution_type(),
                     "volume": v, "high precision agrees": abs(v - float(M.high_precision().volume())) < 1e-10})
good = [r for r in rows if r["orientable"] and r["solution"] == "all tetrahedra positively oriented"
        and r["high precision agrees"]]
vmin = min(r["volume"] for r in good)
at_min = sorted(r["name"] for r in good if abs(r["volume"] - vmin) < 1e-9)
vals = sorted({round(r["volume"], 9) for r in good})
cls = {}
for r in good:
    cls.setdefault(round(r["volume"], 9), []).append(r["name"])
out = {"status": "post hoc, not a cell", "notation at LR": notation, "orientable census": {
    "words": len(words), "manifolds": len(rows), "orientable, geometric and checked": len(good),
    "least volume": vmin, "attained at": at_min, "five smallest": [[v, sorted(cls[v])] for v in vals[:5]],
    "gap above the minimum": vals[1] - vals[0],
    "the two trace signs agree in volume for every word": all(
        abs(a["volume"] - b["volume"]) < 1e-9 for a in good for b in good
        if a["word"] == b["word"] and a["name"] != b["name"])}, "rows": rows}
(HERE / "the_three_to_four_posthoc.json").write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
