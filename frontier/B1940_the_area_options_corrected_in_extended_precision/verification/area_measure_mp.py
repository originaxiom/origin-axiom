"""The area options corrected (P-853): measure (b) as B1932's area_measure.py defines it -- (3/pi) times the integral of
F-bar over the fundamental domain against dx dy / y^2, the canonical end above Im tau = 6 in two brackets (held at its
height-6 value; continued on the trend A + B/y) -- with F-bar above height 6 computed by the extended-precision frame
(frame_mp.py), on B1932's own heights and on a refined set, five columns as before. Below height 6 B1932's grid and
quadrature are kept (the double-precision frame passes the tau -> tau + 1 check there to 2.5e-10). Exact weight only.
Writes area_measure_mp.json; prints only differences and timing."""
import sys, json, math, time, pathlib
import numpy as np
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import frame_mp as FM
EB = FM.EB
sys.argv = ["x"]
import importlib.util
spec = importlib.util.spec_from_file_location("am", EB / "area_measure.py"); AM = importlib.util.module_from_spec(spec); spec.loader.exec_module(AM)
KEYS = FM.KEYS
assert KEYS == AM.KEYS
CR = FM.CR
ys_fit = np.array([3.0, 3.5, 4.0, 4.5, 5.0, 6.0]); L2s = np.array([CR.canon(complex(0.0, y))["L_2"] for y in ys_fit])
A = np.vstack([np.ones_like(ys_fit), 1 / ys_fit]).T; (a0, b0), *_ = np.linalg.lstsq(A, L2s, rcond=None)
L2_6 = CR.canon(complex(0.0, 6.0))["L_2"]
H1 = [6, 7, 8, 10, 13, 17, 22, 30, 45]
H2 = [6, 6.5, 7, 7.5, 8, 9, 10, 11.5, 13, 15, 17, 19.5, 22, 26, 30, 37, 45]
low = AM.lower(AM.build(EB / "fiber_grid_t90.json"))
cache = {}
def fb(y, bracket):
    key = (y, bracket)
    if key not in cache:
        L2 = L2_6 if bracket == "held" else a0 + b0 / y
        acc = None
        for x in (-0.5, -0.25, 0.0, 0.25, 0.5):
            f = np.array([float(v) for v in FM.flat(FM.fbar(x, y, L2=L2))]); acc = f / 5 if acc is None else acc + f / 5
        cache[key] = acc
    return cache[key]
out = {"keys": KEYS, "trend": [a0, b0], "L2_at_6": L2_6, "H1": H1, "H2": H2}
t0 = time.time()
for name, H in (("H1", H1), ("H2", H2)):
    for bracket in ("held", "trend"):
        F = [fb(y, bracket) for y in H]
        tail = sum(0.5 * (F[i] / H[i] ** 2 + F[i + 1] / H[i + 1] ** 2) * (H[i + 1] - H[i]) for i in range(len(H) - 1)) + F[-1] / H[-1]
        out["exact|%s|%s" % (bracket, name)] = ((3 / math.pi) * (low + tail)).tolist()
        print("%s %s done (%.0f s)" % (name, bracket, time.time() - t0), flush=True)
out["fbar_at_heights_held"] = {str(y): cache[(y, "held")].tolist() for y in H2}
old = json.loads((EB / "area_measure.json").read_text())
for k in ("held", "trend"):
    d = np.log(np.array(out["exact|%s|H1" % k]) / np.array(old["exact|%s" % k]))
    print("corrected (B1932's heights) against B1932, %s: max |d ln| %.4f at %s" % (k, np.max(np.abs(d)), int(np.argmax(np.abs(d)))))
d = np.log(np.array(out["exact|held|H2"]) / np.array(out["exact|held|H1"]))
print("refined heights against B1932's heights (held): max |d ln| %.2e" % np.max(np.abs(d)))
d = np.log(np.array(out["exact|trend|H2"]) / np.array(out["exact|held|H2"]))
print("the end's two brackets (refined): max |d ln| %.2e" % np.max(np.abs(d)))
(pathlib.Path(__file__).resolve().parent / "area_measure_mp.json").write_text(json.dumps(out, indent=1))
