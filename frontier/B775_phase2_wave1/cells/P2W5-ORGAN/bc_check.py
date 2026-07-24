"""P2W5-ORGAN auxiliary 2: the BOUNDARY-CONDITION provenance check.

The sealed L98 prereg motivates its statistic with a banked premise:
  "the exact functional g(kappa) = mst_max_edge/diam (banked B163 machinery)
   peaks at kappa = 1.2 and is UNIMODAL on the banked coarse grid
   (r3_results.json scan_mst_gap_F1597: 0.0413 ... 0.0330 on 0.8..1.5)"
The sealed runner, however, computes g on metallic_word(d,1) with
periodic=True, while R3's banked scan computed it on L.fib_word(16) with
periodic=FALSE (r3_peak_check.py line 235).  The main cell reproduces neither
0.0413 nor a 1.2 argmax -- it finds peaks at 0.95 and 1.60.

WORKING_RULES #4: declare every choice; undeclared choice drift is this
program's most recurrent error class.  So instead of ASSERTING that the
boundary condition explains the gap, this script COMPUTES it:

 (1) reproduces R3's exact recipe (fib_word(16), periodic=False,
     max_gap_over_diam) at R3's own 10 kappa points and diffs against the
     banked r3_results.json values;
 (2) runs the same word with periodic=True at the same points;
 (3) re-derives the organ structure under OPEN boundary conditions over this
     cell's extended grid at two depths, with the SAME imported sealed peak
     rule -- i.e. asks whether the TWO-ORGANS conclusion is boundary-condition
     robust, exactly as aux_convention.py asked whether it is
     normalisation-robust.
"""
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
R3 = os.path.abspath(os.path.join(
    HERE, "..", "..", "..", "B646_wave2_integration", "cc2_packets",
    "residuals", "residuals_loop", "r3_peak"))
sys.path.insert(0, HERE)
from compute import EXT_GRID, dec_margin, bound_hugging, clusters_at_gap1, W34  # noqa: E402

sys.path.insert(0, R3)
import lib_banked as L  # noqa: E402
sys.path.insert(0, W34)
from l98_lib import metallic_word  # noqa: E402
from l98_falsifier import peak_regions  # noqa: E402

R3_GRID = [0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.8]
DEPTHS = (13, 14)


def lam_of(k):
    return 1j * float(np.sqrt(2.0 - k))


def main():
    out = {}
    banked = json.load(open(os.path.join(R3, "r3_results.json")))
    ref = banked["scan_mst_gap_F1597"]["values"]

    w16 = L.fib_word(16)
    w15m = metallic_word(15, 1)
    same = (w16 == w15m)
    print(f"fib_word(16) length {len(w16)}; metallic_word(15,1) length {len(w15m)}; "
          f"identical string: {same}")
    out["word_identical"] = same

    print("\n(1)+(2) R3's recipe (periodic=False) vs periodic=True, R3's own grid")
    open_vals, per_vals, diffs = [], [], []
    for kap, rv in zip(R3_GRID, ref):
        lam = lam_of(kap)
        ev_o = L.H_eig(w16, lam, periodic=False)
        ev_p = L.H_eig(w16, lam, periodic=True)
        go = L.max_gap_over_diam(ev_o)
        gp = L.max_gap_over_diam(ev_p)
        open_vals.append(go)
        per_vals.append(gp)
        diffs.append(abs(go - rv))
        print(f"  kappa={kap:.2f}: open={go:.8f}  banked_R3={rv:.8f}  "
              f"|diff|={abs(go-rv):.2e}   periodic={gp:.8f}", flush=True)
    print(f"  MAX |open - banked_R3| over the 10 points = {max(diffs):.2e}  "
          f"=> R3's scan reproduced: {max(diffs) < 1e-9}")
    print(f"  max |periodic - open| = {max(abs(a-b) for a, b in zip(per_vals, open_vals)):.4e}"
          f"   (the undeclared switch)")
    out["r3_reproduced"] = bool(max(diffs) < 1e-9)
    out["r3_max_abs_diff"] = max(diffs)
    out["open_vals_r3grid"] = open_vals
    out["periodic_vals_r3grid"] = per_vals
    out["banked_r3_vals"] = ref

    print("\n(3) organ structure under OPEN BC on this cell's extended grid")
    curves = {}
    for d in DEPTHS:
        w = metallic_word(d, 1)
        vals = []
        for kap in EXT_GRID:
            ev = L.H_eig(w, lam_of(kap), periodic=False)
            vals.append(L.max_gap_over_diam(ev))
            print(f"  open d={d} kappa={kap:.2f}: g={vals[-1]:.6f}", flush=True)
        curves[d] = vals
    reps = {d: peak_regions(curves[d]) for d in DEPTHS}
    org = [(a, b) for a in reps[DEPTHS[0]] for b in reps[DEPTHS[1]] if abs(a - b) <= 1]
    keep = [o for o in org if not bound_hugging(o, len(EXT_GRID))]
    cl = clusters_at_gap1([o[1] for o in keep])
    m = min(dec_margin(curves[d]) for d in DEPTHS)
    print(f"\n  OPEN-BC peaks: {[[EXT_GRID[i] for i in reps[d]] for d in DEPTHS]}")
    print(f"  OPEN-BC identifiable organs: {[[EXT_GRID[i] for i in o] for o in keep]}"
          f"  -> {len(cl)} cluster(s);  dec_margin={m:.3e}")
    out["open_bc_peaks"] = {str(d): [EXT_GRID[i] for i in reps[d]] for d in DEPTHS}
    out["open_bc_organs"] = [[EXT_GRID[i] for i in o] for o in keep]
    out["open_bc_clusters"] = [[EXT_GRID[i] for i in g] for g in cl]
    out["open_bc_n_clusters"] = len(cl)
    out["open_bc_dec_margin"] = m
    out["open_bc_curves"] = {str(d): curves[d] for d in DEPTHS}
    bc_robust = len(cl) >= 2
    print(f"  BC-ROBUST (>=2 identifiable organs under open BC too): {bc_robust}")
    out["bc_robust_two_organs"] = bc_robust
    json.dump(out, open(os.path.join(HERE, "bc_check.json"), "w"),
              separators=(",", ":"))
    print("written: bc_check.json")


if __name__ == "__main__":
    main()
