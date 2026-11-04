"""S301-A check c29b (first principles; reuses c29's rebuilt potential).  With the fermion terms at the sign of a fermion loop's
free energy (-log det instead of the lane's +log det), does V have any stationary point?  Scan dV/dy and dV/dx on a grid over
one x-period (5) and Im tau in [0.4, 12]: a stationary point needs both to change sign.  Same scan for the lane's sign as control."""
import os, sys
for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ.setdefault(v, "1")
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import c29_vcover as C
xs = np.arange(-2.5, 2.5, 0.125); ys = np.concatenate([np.arange(0.4, 4.0, 0.1), np.arange(4.0, 12.01, 0.5)])
for label, fs in (("lane's sign (+log det)", 1.0), ("fermion-loop sign (-log det)", -1.0)):
    h = 1e-5
    gy = np.array([[(C.V(x, y + h, fsign=fs) - C.V(x, y - h, fsign=fs)) / (2 * h) for x in xs] for y in ys])
    gx = np.array([[(C.V(x + h, y, fsign=fs) - C.V(x - h, y, fsign=fs)) / (2 * h) for x in xs] for y in ys])
    # cells where both gradient components change sign (candidate stationary points)
    cand = 0
    for i in range(len(ys) - 1):
        for j in range(len(xs) - 1):
            sy = np.sign(gy[i:i + 2, j:j + 2]); sx = np.sign(gx[i:i + 2, j:j + 2])
            if sy.min() < 0 < sy.max() and sx.min() < 0 < sx.max():
                cand += 1
    print("c29b %-30s: dV/dy > 0 on %d of %d grid points, < 0 on %d; cells where both components change sign: %d"
          % (label, int((gy > 0).sum()), gy.size, int((gy < 0).sum()), cand))
    print("      dV/dy range by row (min, max): Im tau 0.4: (%.2f, %.2f); 2.4: (%.2f, %.2f); 6.0: (%.2f, %.2f); 12: (%.2f, %.2f)"
          % tuple(v for y0 in (0.4, 2.4, 6.0, 12.0) for v in (gy[np.argmin(abs(ys - y0))].min(), gy[np.argmin(abs(ys - y0))].max())))
