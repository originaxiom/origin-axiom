#!/usr/bin/env python3
"""GRID FRESHNESS (data-free; no target is read).  The tau points of every value grid on record that chat1 knows of, closed
under the mirror symmetry R4 (Re tau -> 1 - Re tau, mod 1), and the smallest distance |tau - tau'| from each point of a
candidate grid to each record set.  The sets (sources in brackets):
  main          Re {0, 0.1, 1/4, 0.4, 1/2} x Im on multiples of 0.05 in [1, 4]           [READING_TEST_RULE.md]
  B1726         Re {0.05, 0.2, 0.35, 0.55, 0.7, 0.85} x Im multiples of 0.05 in [1, 4]     [READING_TEST_RULE.md]
  chat1 lattice Re multiples of 0.1 or 1/16 x Im on tenths in [1, 4] (the zero-free census, TWO_INGREDIENTS, TWO_HIGGS,
                the selection map's scans, GJ_WALL, B1698's CP lines)                       [READING_TEST_RULE.md]
  ZFH           ZERO_FREE_HOLOMORPHIC: Re {0.15, 0.30, ..., 0.90} x Im {2.05, 2.15, ..., 3.45}
  TICK          TICK_LINE_HIGGS: Re {0.025, 0.075, ..., 0.975} x Im {2.025, 2.125, ..., 3.425}
  READING       THE READING TEST: Re {0.1146, 0.6354} and its mirror set 0.8854 x Im {2.1146, 2.5271, 2.9396, 3.3521}
  HOLO          THE HOLOMORPHIC READING TEST: Re {0.275, 0.775} and its mirror set 0.725 x Im {2.075, 2.375, ..., 3.275}
  RIGID         RIGID_TAU's points: B1720's thread-class apexes (family A) and the tick's two moduli (family B), as stored
                in rigid_tau_index.json, Re tau taken mod 1
  TICKOPT       chat1's tick_line_optimum.py (A1 at fixed directions, read-out of TICK_LINE_HIGGS): its three optima tau*
                (F_22 on (2/5, 1/5), L_max; F_22 and F_6 on (2/5, 4/5), L_2) and the 5 x 5 grid of +-0.05, step 0.025, around
                each (tick_line_optimum.json); its Nelder-Mead paths are not recorded
  B1748         main's sealed B1748 (2026-10-24): the apex points of the thread words of length 10 and 11 with apex height in
                [2.0, 3.6], 98 points, recomputed with B1720's thread_geometry.py exactly as B1748's census.apex_points()
                does (b1748_apex_points.json; positions only, no value)
    python3 -B grid_freshness.py [--re 0.x 0.y --im a b c ...]   # prints the scan of candidates, or one grid's distances"""
import json, math, sys, pathlib
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent


def lattice(res, ims):
    return [(r % 1.0, y) for r in res for y in ims]


def mult(step, lo, hi):
    n0, n1 = math.ceil(lo / step - 1e-9), math.floor(hi / step + 1e-9)
    return [round(k * step, 10) for k in range(n0, n1 + 1)]


IM05, IM10 = mult(0.05, 1.0, 4.0), mult(0.1, 1.0, 4.0)
RIGID = [(p[2] % 1.0, p[3]) for p in json.loads((HERE.parent / "chat1_2026-10-23_rigid_tau" / "rigid_tau_index.json").read_text())["points"]]
REC = {
    "main": lattice([0, 0.1, 0.25, 0.4, 0.5], IM05),
    "B1726": lattice([0.05, 0.2, 0.35, 0.55, 0.7, 0.85], IM05),
    "chat1 lattice": lattice(sorted(set(mult(0.1, 0, 1) + mult(0.0625, 0, 1))), IM10),
    "ZFH": lattice([0.15, 0.30, 0.45, 0.60, 0.75, 0.90], [round(2.05 + 0.1 * j, 10) for j in range(15)]),
    "TICK": lattice([round(0.025 + 0.05 * i, 10) for i in range(20)], [round(2.025 + 0.1 * j, 10) for j in range(15)]),
    "READING": lattice([0.1146, 0.6354, 0.8854], [2.1146, 2.5271, 2.9396, 3.3521]),
    "HOLO": lattice([0.275, 0.775, 0.725], [2.075, 2.375, 2.675, 2.975, 3.275]),
    "RIGID": RIGID,
    "B1748": [tuple(x) for x in json.loads((HERE / "b1748_apex_points.json").read_text())],
    "TICKOPT": [((v["tau*"][0] + dr) % 1.0, v["tau*"][1] + dy)
                for v in json.loads((HERE.parent / "chat1_2026-10-23_tick_line" / "tick_line_optimum.json").read_text()).values()
                if isinstance(v, dict) and "tau*" in v
                for dr in (-0.05, -0.025, 0.0, 0.025, 0.05) for dy in (-0.05, -0.025, 0.0, 0.025, 0.05)],
}
REC = {k: np.array(sorted(set(v + [((1.0 - r) % 1.0, y) for r, y in v]))) for k, v in REC.items()}


def dist(pts, rec):
    """Smallest distance from each point (Re mod 1) to the record set, Re taken on the circle."""
    P = np.array(pts)
    dx = np.abs(P[:, None, 0] - rec[None, :, 0]); dx = np.minimum(dx, 1.0 - dx)
    return np.sqrt(dx ** 2 + (P[:, None, 1] - rec[None, :, 1]) ** 2).min(axis=1)


def report(res, ims):
    pts = lattice(res, ims)
    return {k: float(dist(pts, v).min()) for k, v in REC.items()}


if __name__ == "__main__":
    if "--re" in sys.argv:
        i, j = sys.argv.index("--re"), sys.argv.index("--im")
        res = [float(x) for x in sys.argv[i + 1:j]]; ims = [float(x) for x in sys.argv[j + 1:]]
        r = report(res, ims)
        print(json.dumps({"Re": res, "Im": ims, "smallest distance to each record set (mirrors included)": r,
                          "smallest overall": min(r.values())}, indent=1))
    else:
        ALL = np.concatenate(list(REC.values()))
        print("per Re tau (step 0.0025 over [0, 0.5]; each Re stands for itself and its mirror): the best Im offset's smallest distance"
              " (offsets over the whole 0.3 period)")
        rows = []
        for r in np.arange(0.0, 0.5001, 0.0025):
            best = (0, None)
            for off in np.arange(0.0, 0.3, 0.0025):
                ims = [2.0 + off + 0.3 * k for k in range(5)]
                d = float(dist(lattice([r], ims), ALL).min())
                if d > best[0]:
                    best = (d, round(off, 4))
            rows.append((round(r, 4), best[0], best[1]))
        for r, d, off in rows:
            if d >= 0.025:
                print(f"  Re {r:.4f}  Im offset {off}  smallest distance {d:.4f}")
