"""Planted control for level15.py: with the lepton charges shifted to (-2, 6) (6Y no longer divisible by 3 on L) the
lepton average over order 15 must stop equalling the down average over order 5."""
import sys, pathlib
exec(open(str(pathlib.Path(__file__).resolve().parent / "level15.py")).read().split("for t in (complex")[0])
B.SIXY["L"] = -2
t = complex(0.13, 1.5); a5, a15 = avg(t, P5), avg(t, P15)
d5, l15 = a5[0:2], a15[2:4]
d = float(np.max(np.abs(l15 - d5) / np.abs(d5)))
print("CONTROL lepton charges (-2, 6): lepton(15) vs down(5) %.2e -> %s" % (d, "CAUGHT" if d > 1e-6 else "MISSED"))
