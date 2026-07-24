"""P2W5-ORGAN auxiliary: is the organ count CONVENTION-ROBUST?

The sealed L98 runner normalises the dominant MST gap by the BOUNDING-BOX
DIAGONAL (diam = hypot(ptp x, ptp y)).  The banked R3 mechanism-candidate
reported a g-hump maximal at kappa=1.2 with values 0.041..0.063, whereas the
sealed convention gives 0.070..0.079 -- i.e. the two are NOT the same
functional.  WORKING_RULES #4 (declare every choice; undeclared choice drift is
this program's most recurrent error class) demands the peak structure be checked
against the normalisation convention rather than assumed invariant.

This script recomputes, at depths 13 and 14 over the extended grid, BOTH
  g_bbox(kappa) = e1 / hypot(ptp x, ptp y)      [the sealed convention]
  g_diam(kappa) = e1 / max pairwise distance    [the set-diameter convention]
  g_raw(kappa)  = e1                            [no normalisation at all]
and applies the SAME imported sealed peak rule to each.  Deterministic; no RNG.
"""
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from compute import (W34, EXT_GRID, hierarchy, diam_bbox, dec_margin,  # noqa: E402
                     bound_hugging, clusters_at_gap1)

sys.path.insert(0, W34)
from l98_lib import metallic_word, spectrum, mst_edges  # noqa: E402
from l98_falsifier import peak_regions, consistent_organs  # noqa: E402

DEPTHS = (13, 14)


def diam_maxpair(ev, chunk=256):
    P = np.c_[ev.real, ev.imag]
    best = 0.0
    for i in range(0, len(P), chunk):
        d = np.sqrt(((P[i:i + chunk, None, :] - P[None, :, :]) ** 2).sum(-1))
        best = max(best, float(d.max()))
    return best


def main():
    print("== P2W5-ORGAN aux: normalisation-convention robustness ==")
    curves = {c: {d: [] for d in DEPTHS} for c in ("bbox", "diam", "raw")}
    for d in DEPTHS:
        w = metallic_word(d, 1)
        for kap in EXT_GRID:
            ev = spectrum(w, 1j * np.sqrt(2.0 - kap), periodic=True)
            e1 = max(e[0] for e in mst_edges(ev))
            db, dp = diam_bbox(ev), diam_maxpair(ev)
            curves["bbox"][d].append(e1 / db)
            curves["diam"][d].append(e1 / dp)
            curves["raw"][d].append(e1)
            print(f"  d={d} kappa={kap:.2f}: e1={e1:.6f} bbox={db:.4f} "
                  f"maxpair={dp:.4f} g_bbox={e1/db:.6f} g_diam={e1/dp:.6f}",
                  flush=True)
    out = {}
    print("\n-- peak structure under each convention (same sealed peak rule) --")
    for c in ("bbox", "diam", "raw"):
        reps = {d: peak_regions(curves[c][d]) for d in DEPTHS}
        # 2-depth consistency (this aux uses depths 13/14 only)
        org = [(a, b) for a in reps[DEPTHS[0]] for b in reps[DEPTHS[1]]
               if abs(a - b) <= 1]
        keep = [o for o in org if not bound_hugging(o, len(EXT_GRID))]
        cl = clusters_at_gap1([o[1] for o in keep])
        m = min(dec_margin(curves[c][d]) for d in DEPTHS)
        out[c] = dict(peaks={str(d): [EXT_GRID[i] for i in reps[d]] for d in DEPTHS},
                      identifiable_organs=[[EXT_GRID[i] for i in o] for o in keep],
                      clusters=[[EXT_GRID[i] for i in g] for g in cl],
                      n_clusters=len(cl), dec_margin=m,
                      curves={str(d): curves[c][d] for d in DEPTHS})
        print(f"  {c:5s}: peaks {[[EXT_GRID[i] for i in reps[d]] for d in DEPTHS]}"
              f"  identifiable organs at kappa "
              f"{[[EXT_GRID[i] for i in o] for o in keep]}  -> {len(cl)} cluster(s)"
              f"  dec_margin={m:.3e}")
    ns = {c: out[c]["n_clusters"] for c in out}
    robust = len(set(ns.values())) == 1
    print(f"\n  organ-cluster count by convention: {ns}")
    print(f"  CONVENTION-ROBUST: {robust}")
    out["convention_robust"] = robust
    out["n_clusters_by_convention"] = ns
    json.dump(out, open(os.path.join(HERE, "aux_convention.json"), "w"),
              separators=(",", ":"))
    print("written: aux_convention.json")


if __name__ == "__main__":
    main()
