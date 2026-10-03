#!/usr/bin/env python3
"""B1527 post-run diagnosis (not sealed; written after the sealed run was read): why the sealed type-one scan converged on 2 of
72 frames on +LR and on none elsewhere.

The sealed scan seeds the solver at the hyperbolic point (a = b = 0) in a frame rotated by theta, sets a = A_SCAN and runs
scan_lib.solve (Levenberg-Marquardt, 80 iterations).  At a = 0 every rotation of the frame solves the system; at a != 0 only
the type-one frames do, so the solver has to turn the frame along a direction the equations hardly see.  This script measures
the cost of that turn: it seeds the sealed solver at a chosen offset from two of +LR's type-one frames (300 deg, where the sealed
run converged, and 0 deg, where it did not) and counts the iterations to the sealed run's own convergence threshold, with the
budget raised to 600.  The sealed grid's seeds sit 0.32 deg from +LR's frames (theta = 5k deg; the seed's alpha is theta plus
the angle of l at theta = 0), and 2.5 deg is the largest offset a 5-deg grid can leave.

Writes post_run_diagnosis.json; prints one line per probe."""
import json
import sys
import time
import warnings
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
warnings.filterwarnings("ignore")
import scan_lib as S  # noqa: E402
from run import A_SCAN, CONVERGED_FLOOR, CONVERGED_FACTOR, circ_dist  # noqa: E402

SIGN, WORD = "+", "LR"
FRAMES = (300.0, 0.0)
OFFSETS = (0.0, 0.32, 1.0, 2.5)
BUDGET = 600


def probe(cache, z0_angle, frame, offset):
    th = np.radians(frame + offset - z0_angle)
    G, img, W, u0, orient = S.hyperbolic_seed(SIGN, WORD, th, cache)
    seed_alpha = float(np.degrees(np.angle(S.frame_reading(u0, False)["zl"])) % 360)
    floor = float(np.linalg.norm(S.residual(u0, 0.0, W, False).real))
    thresh = max(CONVERGED_FLOOR, CONVERGED_FACTOR * floor)
    t = time.time()
    u, f, it = S.solve(u0, A_SCAN, W, False, tol=0.3 * thresh, maxit=BUDGET)
    out = {"frame": frame, "offset (deg)": offset, "seed alpha": seed_alpha, "|F|": float(f), "threshold": thresh,
           "converged": bool(f < thresh), "iterations": int(it), "seconds": round(time.time() - t, 1)}
    if f < thresh:
        a_end = float(np.degrees(np.angle(S.frame_reading(u, False)["zl"])) % 360)
        out["alpha reached"] = a_end
        out["distance to the frame (deg)"] = circ_dist(a_end, frame)
    return out


def main():
    cache = {}
    _, _, _, u00, _ = S.hyperbolic_seed(SIGN, WORD, 0.0, cache)
    z0_angle = float(np.degrees(np.angle(S.frame_reading(u00, False)["zl"])))
    rows = []
    for frame in FRAMES:
        for off in OFFSETS:
            r = probe(cache, z0_angle, frame, off)
            rows.append(r)
            print(json.dumps(r), flush=True)
    rec = {"manifold": SIGN + WORD, "a": A_SCAN, "sealed budget": 80, "budget here": BUDGET,
           "angle of l at theta = 0 (deg)": z0_angle, "probes": rows}
    (HERE / "post_run_diagnosis.json").write_text(json.dumps(rec, indent=1))


if __name__ == "__main__":
    main()
