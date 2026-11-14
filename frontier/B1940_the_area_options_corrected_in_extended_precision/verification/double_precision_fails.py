"""Is main's double-precision F-bar (exact weight, canonical end) stable high in the cusp? For each height y, F-bar at x
and at x + 1 (T-invariance makes them equal exactly) and its smoothness in y. Prints the seven claimed outputs of W- and
the T-check's largest relative difference."""
import sys, pathlib, time, math
import numpy as np
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
EB = next((ROOT / "frontier").glob("B1932_*")) / "verification"
sys.path.insert(0, str(EB)); sys.argv = ["x"]
import fiber_grid_t90 as G
KW = ["up|L_2|St", "down|L_2|S", "ckm|L_2|St|S"]
for y in [6, 9, 12, 15, 20, 25, 30, 45]:
    t0 = time.time(); rows = []
    for x in (0.13, 1.13, -0.31):
        f = G.fbar_t90(complex(x, y)); rows.append(np.concatenate([np.array(f[k]) for k in KW]))
    rows = np.array(rows)
    tdiff = np.max(np.abs(rows[0] - rows[1]) / np.maximum(np.abs(rows[0]), 1e-300))
    xdiff = np.max(np.abs(rows[0] - rows[2]) / np.maximum(np.abs(rows[0]), 1e-300))
    print("y %5.1f  T-check %.1e  x-variation %.1e  W- seven at x=0.13: %s  (%.0f s)" % (y, tdiff, xdiff, " ".join("%.4g" % v for v in rows[0]), time.time() - t0), flush=True)
