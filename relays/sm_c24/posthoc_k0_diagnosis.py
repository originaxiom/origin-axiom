#!/usr/bin/env python3
"""SM-C24, post hoc (after the sealed run, disclosed): K0 failed (the frozen end moves rates by up to 0.12).  Which
rates move, at which points, and whether a channel of the coupling switches on or off (main's parts sets a channel to 0
when its argument 2 pi L + c is not positive).  Same 12 points as K0.
    python3 -B posthoc_k0_diagnosis.py MAIN_CHECKOUT"""
import run_c24 as R
L0 = R.TABLE_CANON(complex(0.13, 6.0))["L_2"]
def zeros(a, b, y, L):
    R.CR.canon = lambda z: {"L_2": L, "L_max": L, "_extrapolated": False}
    try:
        return {s: tuple(k for k, v in R.DL.parts(R.X, y, a, b, s)[3].items() if v == 0) for s in R.SECS}
    finally:
        R.CR.canon = R.TABLE_CANON
print("L0 (the frozen end) = %.6f" % L0)
for (a, b) in R.REPS[::24]:
    base = R.rates(a, b, 40.0, 50.0)
    moved = {}
    for dL in (-0.05, 0.05):
        r = R.rates(a, b, 40.0, 50.0, L=L0 + dL)
        for k in R.K:
            if r[k] is not None and base[k] is not None and abs(r[k] - base[k]) > 1e-3:
                moved[(k, dL)] = round(r[k] - base[k], 4)
    zs = {dL: zeros(a, b, 50.0, L0 + dL) for dL in (-0.05, 0.0, 0.05)}
    switch = zs[-0.05] != zs[0.0] or zs[0.05] != zs[0.0]
    print("(%s, %s): rates moved %s; zero channels at L0 %s; switch under +-0.05: %s" % (a, b, moved or "none",
          zs[0.0], switch))
