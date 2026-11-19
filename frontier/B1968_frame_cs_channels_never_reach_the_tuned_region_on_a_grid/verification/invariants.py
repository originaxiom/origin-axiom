"""B1968: frame C's channel invariants at sixteen (point, height, column) cases (main, 2026-11-19; data-free).
Per sector: |u.u|/|u|^2, |w|^2/|u|^2, the channel quaternion's nullity |w^2 + u.u|/(|w|^2 + |u|^2); and the overlap of
the up and down channel vectors.  Read: none is constant across the cases.
    python3 -B invariants.py > invariants_run.txt"""
import sys, pathlib
import numpy as np
from fractions import Fraction as Fr
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import reach as R
for x in ("0", "0.25"):
    for y in (1.0, 3.0, 6.0):
        for (a, b) in ((Fr(1, 5), Fr(2, 5)), (Fr(3, 7), Fr(1, 7)), (Fr(2, 5), Fr(0)), (Fr(1, 7), Fr(6, 7))):
            out = []
            for sec in ("up", "down"):
                u, w = R.channels(x, y, a, b, sec); nu = np.vdot(u, u).real
                out.append((abs(u @ u) / nu, abs(w) ** 2 / nu, abs(w * w + u @ u) / (abs(w) ** 2 + nu)))
            (uu, _), (ud, _) = R.channels(x, y, a, b, "up"), R.channels(x, y, a, b, "down")
            ov = abs(np.vdot(uu, ud)) / np.sqrt(np.vdot(uu, uu).real * np.vdot(ud, ud).real)
            print("x %4s y %3.0f %-8s up: %.3f %.3e %.3f; down: %.3f %.3e %.3f; overlap %.3f" % (x, y, str(a) + "," + str(b), *out[0], *out[1], ov))
