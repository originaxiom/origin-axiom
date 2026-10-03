#!/usr/bin/env python3
"""B1527 post-run check X1b (written after X1 was read; disclosed in FINDINGS).

Why. X1 brackets the type-one frames as sign changes of b between converged neighbours on its 5-degree grid. On
-LLLLRLRRRLRR its grid converged on 40 of 72 frames and bracketed four type-one frames (0.95, 60.95, 180.95 and 240.95
degrees). It did not converge at 120 degrees or from 300 to 330, so if the other two frames are where the weight-3 law puts
them (120.95 and 300.95), X1 had no converged neighbours to bracket them with.

What X1b does. It needs no bracketing. For every manifold, at the six frames alpha_1 + 60 k (alpha_1 is X1's first frame) it
solves the type-one system itself (b = 0, a = 1e-5; no frame pinned), by X1's Gauss-Newton, from the hyperbolic seed in that
frame. That is a second system and a second solve, independent of X1's b-free scan and bisection.
  - where X1 found the frame, X1b's solution is compared with X1's (alpha, beta);
  - where X1 did not, the solution is passed to the sealed polish_point exactly as X1 does (60 digits, X1's polish_gn), and
    read as X1 reads its points;
  - as a control on what "a solution" means, the same solve is started 3 degrees to either side of every frame; it is
    expected to fail there (at fixed a the type-one frames are isolated), which shows the solve finds frames rather than
    returning wherever it starts.
Writes x1b_<name>.json and x1b.json; prints one line per manifold.
Usage: python3 post_run_x1b.py --all  (four at a time)  or  python3 post_run_x1b.py SIGN WORD"""
import json
import sys
import time
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import numpy as np  # noqa: E402

import family_lib as FL  # noqa: E402
import post_run_x1 as X1  # noqa: E402  (a = 1e-5; the sealed polish_point polishing by X1's polish_gn)
import run as R  # noqa: E402
import scan_lib as S  # noqa: E402

OFF = 3.0        # the control's offset (degrees)
MATCH = 0.01     # degrees: X1b's alpha within this of X1's frame counts as the same frame


def type_one_at(P, frame_deg):
    """the type-one system solved from the hyperbolic seed in the frame frame_deg (X1's Gauss-Newton; no pin)"""
    th = np.radians(frame_deg) - np.angle(P.z0)
    G, img, W, u0, orient = S.hyperbolic_seed(P.sign, P.word, th, P.cache)
    floor = float(np.linalg.norm(S.residual(u0, 0.0, W, False).real))
    thr = max(R.CONVERGED_FLOOR, R.CONVERGED_FACTOR * floor)
    u1, f1, it = X1.gauss_newton(lambda v: S.residual(v, X1.A, W, False).real,
                                 lambda v: S.jacobian(v, X1.A, W, False), u0, 0.3 * thr)
    r = S.frame_reading(u1, False)
    alpha = float(np.degrees(np.angle(r["zl"])) % 360)
    return {"seed frame": frame_deg % 360, "converged": bool(f1 < thr), "|F|": float(f1), "threshold": thr, "iterations": it,
            "alpha": alpha, "beta": S.line_angle_from_l(1j, r["zl"], P.orient), "|z_l| / R0": float(abs(r["zl"]) / P.R0),
            "u": u1}


def run_one(sign, word):
    t0 = time.time()
    name = R.name_of(sign, word)
    x1 = json.loads((HERE / ("x1_" + name + ".json")).read_text(encoding="utf-8"))
    found = x1["type-one frames"]
    a1 = found[0]
    P = X1.Pinned(sign, word)
    G, img = FL.word_group(sign, word)
    chars, _ = R.characters(img)
    rows, controls, new_points = [], [], []
    for k in range(6):
        fr = (a1 + 60 * k) % 360
        rec = type_one_at(P, fr)
        near = [f for f in found if R.circ_dist(f, fr) < 1.0]
        row = {k_: v for k_, v in rec.items() if k_ != "u"}
        if near:
            match = [p for p in x1["points"] if R.circ_dist(p["frame alpha0"], near[0]) < 1e-6]
            row["X1 frame"] = near[0]
            row["|alpha - X1's alpha| (deg)"] = R.circ_dist(rec["alpha"], match[0]["alpha"]) if match else None
            row["|beta - X1's beta| (deg)"] = R.circ_dist(rec["beta"], match[0]["beta"], 180.0) if match else None
            row["same frame as X1"] = bool(rec["converged"] and match and row["|alpha - X1's alpha| (deg)"] < MATCH)
        else:
            row["X1 frame"] = None
            if rec["converged"]:
                rep = {"u": [float(x) for x in rec["u"]], "alpha": rec["alpha"], "beta": rec["beta"],
                       "threshold": rec["threshold"]}
                new_points.append({"frame alpha0": fr, "type-one |F|": rec["|F|"], "alpha": rec["alpha"],
                                   "beta": rec["beta"], "converged": True,
                                   "point": R.polish_point(sign, word, rep, chars)})
        rows.append(row)
        for d in (-OFF, OFF):
            c = type_one_at(P, fr + d)
            controls.append({k_: v for k_, v in c.items() if k_ != "u"})
    out = {"manifold": sign + word, "a": X1.A, "alpha_1 (X1's first frame)": a1, "frames": rows,
           "frames converged": sum(1 for r in rows if r["converged"]),
           "frames X1 had": sum(1 for r in rows if r["X1 frame"] is not None),
           "agree with X1": sum(1 for r in rows if r.get("same frame as X1")),
           "new points": new_points,
           "controls (3 degrees off)": controls,
           "controls converged": sum(1 for c in controls if c["converged"]),
           "seconds": round(time.time() - t0)}
    (HERE / ("x1b_" + name + ".json")).write_text(json.dumps(out, indent=1, default=str))
    print(f"{sign}{word}: {out['seconds']} s; type-one frames solved {out['frames converged']}/6; X1 had "
          f"{out['frames X1 had']}, agreeing {out['agree with X1']}; new points {len(new_points)}; controls converged "
          f"{out['controls converged']}/12", flush=True)
    return name


def main():
    args = sys.argv[1:]
    if args == ["--all"]:
        from multiprocessing import Pool
        with Pool(4) as pool:
            names = pool.starmap(run_one, R.MANIFOLDS)
        summ = {}
        for n in names:
            d = json.loads((HERE / ("x1b_" + n + ".json")).read_text(encoding="utf-8"))
            summ[d["manifold"]] = {k: d[k] for k in ("frames converged", "frames X1 had", "agree with X1",
                                                     "controls converged")} | {"new points": len(d["new points"])}
        (HERE / "x1b.json").write_text(json.dumps(summ, indent=1))
        print(json.dumps(summ, indent=1))
    else:
        for sign, word in zip(args[0::2], args[1::2]):
            run_one(sign, word)


if __name__ == "__main__":
    main()
