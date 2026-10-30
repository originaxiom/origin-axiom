#!/usr/bin/env python3
"""STEP B, the census's structural zeros per direction (data-free; aggregate-only; refused unless the refined census's
manifest is committed and pushed).  An output below the roundoff floor 1e-12 is a structural zero (cells.FLOOR: m1 = 0 where
the coupling has rank 2, B1653, P-151; J = 0 where the CKM is real).  On the mini patch (line (2/5, 1/10)) the directions R
and t = -5/288 carried m1/m3 and J at roundoff everywhere (P-543); this counts, per direction and output, the fraction of
rows at the floor over the whole census, and the number of choices whose four are physical.  Prints and writes counts only.
    python3 -I census_structure.py <refined dir> <manifest.json> <manifest sha256> <out.json>"""
import json, math, pathlib, sys

GEN = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(GEN))
import numpy as np

from census_io import load_compact
from guard import require_pushed_manifest
from cells import FLOOR

NAMES = ["c/t", "u/t", "s/b", "d/b", "mu/tau", "e/tau", "|V_us|", "|V_cb|", "|V_ub|", "|J|"]
DIRS = ["DR", "a0", "R", "t=-5/288", "F_-10", "F_-6", "F_-2", "F_6", "F_10", "F_14", "F_18", "F_22", "F_26"]


def main(refined, manifest, expected, out):
    g = require_pushed_manifest(manifest, expected)
    cen, info = load_compact(refined, g["per_file"], n_cfg_expected=g["files"] * 991)
    lf = math.log(FLOOR); rep = {"rows": int(len(cen.F)), "floor": FLOOR, "by_direction": {}}
    for d in sorted(set(int(x) for x in np.unique(cen.d))):
        sel = (cen.d == d) & cen.vdef
        Fd = cen.F[sel]
        below = ~(np.isfinite(Fd) & (Fd >= lf))
        rep["by_direction"][DIRS[d]] = {"rows_defined": int(sel.sum()), "rows_undefined": int(((cen.d == d) & ~cen.vdef).sum()),
                                        "fraction_at_floor": {NAMES[k]: round(float(below[:, k].mean()), 6) for k in range(10)}}
    pathlib.Path(out).write_text(json.dumps(rep, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(rep, indent=1))


if __name__ == "__main__":
    if len(sys.argv) != 5: sys.exit(__doc__)
    main(*sys.argv[1:])
