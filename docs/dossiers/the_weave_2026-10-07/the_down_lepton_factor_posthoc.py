#!/usr/bin/env python3
"""W179 post hoc 1 (labelled; written after the output 0b3702114 was read, committed before its run).

G2 failed as worded on two lines, (1/2, 1/5) and (1/2, 3/10), whose cusp D at Im tau 48 is 10.4075, inside the 3-sigma
window; but G0 flagged both as not settled (D falls from 14.48 at 24 through 12.26 at 32 to 10.41 at 48).  This reads D
further up on those two lines, at Re tau 1/8, with W178's own point function unchanged (its two precisions, no cut, the
theta-zero rule): Im tau 64, 96 and 128.  Read-out only: D per height, and a fit D = A + B/y + C/y^2 over the stored
heights 32 and 48 and these three, with its residuals.

    python3 -B docs/dossiers/the_weave_2026-10-07/the_down_lepton_factor_posthoc.py
"""
import contextlib
import io
import json
import math
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(HERE))
with contextlib.redirect_stdout(io.StringIO()):
    import the_six_at_the_cusp as W178          # noqa: E402
OUT = HERE / "the_down_lepton_factor_posthoc.json"
LINES = (("1/2", "1/5"), ("1/2", "3/10"))
NEW = (64.0, 96.0, 128.0)
STORED = (32.0, 48.0)


def lnD(six):
    return (six[3] - six[5]) - (six[2] - six[4])


def fit(ys, ds):
    """least squares D = A + B/y + C/y^2"""
    import numpy as np
    X = np.array([[1.0, 1.0 / y, 1.0 / y ** 2] for y in ys])
    coef, *_ = np.linalg.lstsq(X, np.array(ds), rcond=None)
    return [float(c) for c in coef], [float(r) for r in (X @ coef - np.array(ds))]


def main():
    t0 = time.time()
    W178._init(str(ROOT))
    lines = W178._G["lines"]
    w178 = json.loads((HERE / "the_six_at_the_cusp.json").read_text(encoding="utf-8"))
    out = {"arc": "W179 post hoc 1", "lines": [list(l) for l in LINES], "Re tau": 0.125, "per line": []}
    for line in LINES:
        k = [i for i, l in enumerate(lines) if (str(l[0]), str(l[1])) == line][0]
        stored = w178["per line"][k]["per Re tau"][0]["six per height"]
        ys, ds, rows = [], [], []
        for y in STORED:
            ys.append(y)
            ds.append(math.exp(lnD(stored[str(y)])))
            rows.append([y, ds[-1], "stored (W178)"])
        for y in NEW:
            r = W178.point((k, 0.125, y, False))
            if "failed" in r or any(s != "resolved" for s in r["status"]):
                rows.append([y, None, r.get("failed", r.get("status"))])
                continue
            ys.append(y)
            ds.append(math.exp(lnD(r["six"])))
            rows.append([y, ds[-1], "computed", r["digits"], r["seconds"]])
        coef, res = fit(ys, ds)
        out["per line"].append({"line": list(line), "D per height": rows, "fit A, B, C": coef, "fit residuals": res})
    out["seconds"] = round(time.time() - t0, 1)
    OUT.write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    print("written", OUT.name, "in", out["seconds"], "s")


if __name__ == "__main__":
    main()
