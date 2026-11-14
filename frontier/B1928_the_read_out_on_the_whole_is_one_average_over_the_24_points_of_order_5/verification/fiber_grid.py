"""The limit theorem's prediction, step 1 (written before the run): F-bar, the frame averaged over all 24 points of order
5 on the fibre, on a grid of the fundamental domain.

The prediction (main's draft proof, DRAFT.md beside this file): the read-out on the whole is the integral of F-bar
against the path measure (uniform letters, lifted to the geodesic flow), the same for the mark, its twin and every point
of order 5, because SL(2, Z) acts transitively on the 24 points and SL(2, F_5) is perfect (the level-5 extension is
mixing). F-bar is SL(2, Z)-invariant, so it is a function on the modular surface and needs no constraint on the words.
This step tabulates F-bar at the grid points with both ends B1924 used (the constant ends 1.3 and 0.9 in L + 1/2 log Im
tau) and with the canonical end (B1667, point by point). Values: the json only."""
import json, math, pathlib, sys
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
sys.path.insert(0, str(next((ROOT / "frontier").glob("B1927_*")) / "verification"))
import canon_readout as CR          # loads the frame (closed-form channel norm) and the canonical end
T, C = CR.T, CR.C
POINTS = [(i / 5, j / 5) for i in range(5) for j in range(5) if (i, j) != (0, 0)]
LT = {"L_max": 1.3, "L_2": 0.9}


def fbar(t):
    acc = {"const": None, "canon": None}
    Lc = CR.canon(t); Lc.pop("_extrapolated")
    Lk = {h: LT[h] - 0.5 * math.log(t.imag) for h in LT}
    for a, b in POINTS:
        for mode, L in (("const", Lk), ("canon", Lc)):
            o = C.frame(t, a, b, L)
            o = {k: np.array(v) for k, v in o.items() if "conjS" not in k}
            if acc[mode] is None:
                acc[mode] = {k: v / len(POINTS) for k, v in o.items()}
            else:
                for k in acc[mode]:
                    acc[mode][k] += o[k] / len(POINTS)
    return {m: {k: v.tolist() for k, v in d.items()} for m, d in acc.items()}


if __name__ == "__main__":
    FINE = "--fine" in sys.argv          # added after the first grid's interpolation check (P1) failed its bar
    xs = np.round(np.linspace(-0.5, 0.5, 41 if FINE else 21), 4)
    ys_top = ([1.0, 1.05, 1.1, 1.15, 1.2, 1.275, 1.35, 1.425, 1.5, 1.625, 1.75, 1.875, 2.0, 2.25, 2.5, 2.75, 3.0, 3.5, 4.0, 4.5, 5.0, 6.0]
              if FINE else [1.0, 1.1, 1.2, 1.35, 1.5, 1.75, 2.0, 2.5, 3.0, 3.5, 4.0, 5.0, 6.0])
    grid = []
    for x in xs:
        lo = math.sqrt(max(0.0, 1 - x * x))
        near = [0.002, 0.015, 0.03, 0.05, 0.08] if FINE else [0.002, 0.03, 0.08]
        ys = sorted(set([round(lo + d, 4) for d in near] + [y for y in ys_top if y > lo + 0.1]))
        for y in ys:
            grid.append({"tau": [float(x), float(y)], "F": fbar(complex(x, y))})
        print("x = %+.3f: %d points" % (x, len(ys)), flush=True)
        (HERE / ("fiber_grid_fine.json" if FINE else "fiber_grid.json")).write_text(json.dumps(grid))
    print("grid: %d points" % len(grid), flush=True)
