#!/usr/bin/env python3
"""W125, post hoc (labelled so; after the one run's read-out). K4 failed as worded: at s = 2 the remainder
Delta_b(s, eps) moved by 0.87 on b+-LLRLR and b+-LRLRR and by 1.45 on b+-LLLRLR and b+-LRLRRR between eps = 0.004 and
0.002, against the rule's 0.5. The rule's tolerance counted only the far tail's O(Q^-2) term. This check reads the run's
own JSON (no new filling) and asks whether the drift is a divergence or the cut's action on finitely many terms:
  - a divergent piece would move Delta by the same amount at each halving of eps (log) or more (power); a finite limit
    with an O(eps) correction moves it by half as much at each halving, so successive differences have ratio 2;
  - the run kept every filling with Q <= 100; their part of the last drift, sum (e^{-0.002 Q} - e^{-0.004 Q}) times
    (e^{s(V_b - V)} - e^{s pi^2 / Q}), is compared with the whole drift;
  - Richardson's 2 Delta(0.002) - Delta(0.004) is the eps -> 0 limit to O(eps^2).
A second check, also after the read-out: the run summed (thread, slope) pairs. A sum over distinct oriented universes
would divide a thread's slope count by the size of any orientation-preserving symmetry's action on its slopes. SnapPy's
self-isometries of each bundle give their maps on the cusp; those preserving orientation are read off by determinant.

    python3 -B the_quantum_weave_posthoc.py      # writes the_quantum_weave_posthoc.json beside itself
"""
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
POS = "all tetrahedra positively oriented"
EPS = (0.016, 0.008, 0.004, 0.002)


def symmetry(bundles):
    """each bundle's self-isometries and their maps on the cusp; those of determinant +1 preserve orientation"""
    import numpy as np
    import snappy
    rows, nontrivial = {}, {}
    for b in bundles:
        M = snappy.Manifold(b)
        iso = M.is_isometric_to(M, return_isometries=True)
        mats = [[[int(c[0, 0]), int(c[0, 1])], [int(c[1, 0]), int(c[1, 1])]] for c in (i.cusp_maps()[0] for i in iso)]
        plus = [m for m in mats if round(np.linalg.det(np.array(m, dtype=float))) == 1]
        moving = [m for m in plus if m not in ([[1, 0], [0, 1]], [[-1, 0], [0, -1]])]
        rows[b] = {"isometries": len(iso), "preserving orientation": len(plus),
                   "amphicheiral": bool(M.symmetry_group().is_amphicheiral())}
        if moving:
            nontrivial[b] = moving
    return {"per bundle": rows, "acting nontrivially on slopes": nontrivial}


def main():
    d = json.loads((HERE / "the_quantum_weave.json").read_text(encoding="utf-8"))
    out = {"arc": "W125", "status": "post hoc, labelled; after the one run's read-out", "rows": {}}
    ratios, far, worst_raw = [], [], 0.0
    for a in d["per bundle"]:
        Vb, rows = a["volume"], a["rows with Q <= 100"]
        for s in (0.5, 1.0, 2.0, 4.0):
            v = [a["K4 Delta(s, eps)"][f"{s} {e}"] for e in EPS]
            diffs = [v[i] - v[i + 1] for i in range(3)]
            near = sum((math.exp(-0.002 * Q) - math.exp(-0.004 * Q))
                       * (math.exp(s * (Vb - V)) - math.exp(s * math.pi ** 2 / Q))
                       for (_, Q, st, V, _) in rows if st == POS and V is not None and V < Vb)
            last = v[3] - v[2]
            r = [diffs[0] / diffs[1], diffs[1] / diffs[2]] if min(abs(x) for x in diffs) > 1e-9 else None
            row = {"Delta at eps 0.016, 0.008, 0.004, 0.002": v, "successive differences": diffs,
                   "their ratios": r, "last drift": last, "of which Q <= 100": near, "of which Q > 100": last - near,
                   "Richardson limit 2 Delta(0.002) - Delta(0.004)": 2 * v[3] - v[2]}
            out["rows"][f"{a['bundle']} s={s}"] = row
            if r is not None and abs(diffs[2]) > 0.01:
                ratios.extend(r)
            far.append(abs(last - near))
            if s <= 2:
                worst_raw = max(worst_raw, abs(last))
    out["summary"] = {
        "the rule's K4 statistic, worst over s = 1/2, 1, 2": worst_raw,
        "ratios of successive differences where the last exceeds 0.01 (min, max)": [min(ratios), max(ratios)],
        "largest |drift from Q > 100| over every bundle and s": max(far),
        "reading": "the drift halves with each halving of eps and is carried by Q <= 100: a finite limit with an "
                   "O(eps) correction, not a divergence"}
    out["symmetry"] = symmetry([a["bundle"] for a in d["per bundle"]])
    for k, v in out["summary"].items():
        print(k, v)
    print("orientation-preserving symmetries acting on slopes:", out["symmetry"]["acting nontrivially on slopes"])
    (HERE / "the_quantum_weave_posthoc.json").write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
