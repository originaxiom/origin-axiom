#!/usr/bin/env python3
"""W175, a labelled post hoc read-out (written after W175's output was read; not a cell). W175's control failed on the
counted class (2/5, 1/10): at Im tau 1.5 and 2.0 the potential's X-minimum left the mirror's fixed points (X = 1, 3.5).
This locates where: on the counted class, at Im tau 1.20-2.60 in steps of 0.05, the global X-minimum (W175's method),
the X-curvature at both fixed points, and J at the minimum (own_point, L_max, (St, S)). The same at the order-5 class
(2/5, 0) at Im tau 1.20-1.50, for comparison. No target is read.

    python3 -B docs/dossiers/the_weave_2026-10-07/the_potential_off_the_mirror_posthoc.py
"""
import contextlib
import io
import json
import sys
import time
import traceback
from fractions import Fraction as Fr
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
with contextlib.redirect_stdout(io.StringIO()):
    import the_potential_off_the_mirror as W75     # noqa: E402  (W175: the profile, the minimum, the frame)
W72, W67, W66, T8 = W75.W72, W75.W67, W75.W66, W75.T8
OUT = HERE / "the_potential_off_the_mirror_posthoc.json"


def scan(b, heights, wv, frame):
    col, W93, W89 = frame
    psi = np.asarray(W67.psi_of(W75.A, b))
    rows = []
    for y in heights:
        m, _vals = W75.x_minimum(b, y, wv)
        o, _d = T8.own_point(W93, W89, col, (W75.A, b), m["X*"], y)
        fixed = {}
        for X0 in (0.0, 1.0, 3.5):
            dxx, _dyy = W72.curvatures(X0, y, W75.S, psi, wv)
            fixed[str(X0)] = {"V": float(W72.kq(X0, y, W75.S, psi) @ wv), "X-curvature": dxx}
        rows.append({"Im tau": y, "X*": m["X*"], "V*": m["V*"], "J at X*": float(o[W75.KEY][3]), "fixed points": fixed})
    return rows


def main():
    root = T8.repo_root()
    out = {"arc": "W175 post hoc", "status": "post hoc, labelled", "head": T8.resolve(root, "HEAD")}
    t0 = time.time()
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            col, _sha, W93, W89, _L = W66.frame(root)
        wv = W72.weights(1.0)
        hs = [round(1.2 + 0.05 * k, 2) for k in range(29)]
        out["counted class (2/5, 1/10)"] = scan(Fr(1, 10), hs, wv, (col, W93, W89))
        out["order-5 class (2/5, 0)"] = scan(Fr(0), hs[:7], wv, (col, W93, W89))
    except Exception:  # noqa: BLE001
        out["run_failed"] = traceback.format_exc()[-3000:].replace(str(root), "<repo>")
    out["seconds"] = round(time.time() - t0, 1)
    OUT.write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
    print("done" if "run_failed" not in out else "run failed")


if __name__ == "__main__":
    main()
