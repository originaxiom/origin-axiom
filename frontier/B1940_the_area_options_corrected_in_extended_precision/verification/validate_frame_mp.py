"""V1: the extended-precision frame against the record's double-precision frame where the latter is sound (heights 1.5
to 6); V2: the T-check (tau against tau + 1) high in the cusp; V3: a planted low precision must fail V2."""
import sys, time
import numpy as np, mpmath as mp
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent)); import frame_mp as FM
worst = 0
for tx, ty in ((0.13, 1.5), (-0.31, 3.0), (0.27, 6.0)):
    t0 = time.time(); a = np.array([float(v) for v in FM.flat(FM.fbar(tx, ty))]); t1 = time.time() - t0
    f = FM.G90.fbar_t90(complex(tx, ty)); b = np.array([v for k in FM.KEYS for v in f[k]])
    d = float(np.max(np.abs(a - b) / np.abs(b))); worst = max(worst, d)
    print("V1 tau %+.2f%+.1fi: max rel diff mp vs double %.2e  (mp %.0f s)" % (tx, ty, d, t1), flush=True)
print("V1 worst %.2e" % worst)
for ty in (12, 20, 45):
    a = FM.flat(FM.fbar(0.13, ty)); b = FM.flat(FM.fbar(1.13, ty))
    d = max(abs(p - q) / abs(p) for p, q in zip(a, b))
    print("V2 y %d: T-check %s ; seven of W-: %s" % (ty, mp.nstr(d, 3), " ".join(mp.nstr(v, 5) for v in [a[0], a[1], a[4], a[5], a[8], a[9], a[10]])), flush=True)
a = FM.flat(FM.fbar(0.13, 20, dps=15)); b = FM.flat(FM.fbar(1.13, 20, dps=15))
d = max(abs(p - q) / abs(p) for p, q in zip(a, b))
print("V3 planted 15 digits at y 20: T-check %s -> %s" % (mp.nstr(d, 3), "CAUGHT" if d > 1e-6 else "MISSED"))
