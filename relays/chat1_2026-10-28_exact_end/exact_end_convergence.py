"""chat1, 2026-10-28: THE EXACT END, the quadrature's convergence and the horoball's shape, after the relay's read-only
referee. Post hoc, labelled, data-free; committed before its one run. (A scratch run of the same refinement was made
before the look; this commits it.)
At exact_end.py's row R1, (2/5, 23/30) at 0.269 + 3.037i, the down sector: the exact twisted norms at L_max with
(nth, ns) = (96, 64), the instrument's, then (144, 96) and (192, 128); and the horoball's radius along the cell's angles
against the round disc e^(-L_max) and the cell's inner radius.
Run:  python3 -B exact_end_convergence.py <main_checkout>"""
import sys, math, pathlib, importlib.util, time
from fractions import Fraction as Fr
import numpy as np
ROOT = pathlib.Path(sys.argv[1]).resolve(); HERE = pathlib.Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("ee", HERE / "exact_end.py")
ee = importlib.util.module_from_spec(_spec); sys.argv = [sys.argv[0], str(ROOT)]; _spec.loader.exec_module(ee)
C, B, K = ee.C, ee.B, ee.K
tau, b = complex(0.269, 3.037), Fr(23, 30)
t0 = time.time(); c = C.track(complex(0.25, 3.0)); c, _ = C.solve_accessory(complex(0.25, 3.0), c); c, _ = C.newton_walk(complex(0.25, 3.0), c, tau)
G = ee.geometry(tau, c); w = float(Fr(2, 5)) * tau + float(b)
lf, rf = K.SECT["down"]; x, yy = B.sector_twists(w, tau, B.SIXY[lf], B.SIXY[rf]); R = B.residues(x, yy, tau)
print("R1 at %s: L_max %.6f" % (tau, G["L_max"]))
prev = None
for nth, ns in ((96, 64), (144, 96), (192, 128)):
    N, mg = ee.twisted_norms(tau, G["al"], G["be"], G["L_max"], x, yy, R, nth=nth, ns=ns)
    dev = None if prev is None else max(abs(N[s] / prev[s] - 1) for s in N if prev[s])
    print("  (nth, ns) = (%d, %d): exact N %s; margin %.2e%s (%.0f s)" % (nth, ns, {s: round(N[s], 7) for s in N}, mg,
          "" if dev is None else "; largest relative change from the previous %.1e" % dev, time.time() - t0))
    prev = N
br, rmaxf = C.voronoi(tau); th = np.linspace(br[0], br[-1], 721)
rh = np.array([C.horocycle_radius(G["al"], G["be"], G["L_max"], t_, min(0.95, 1.1 * rm)) for t_, rm in zip(th, rmaxf(th))], dtype=float)
print("  the horoball's radius over the cell's angles: %.4f-%.4f (mean %.4f); round disc e^(-L_max) %.4f; the cell's inner radius %.4f"
      % (rh.min(), rh.max(), rh.mean(), math.exp(-G["L_max"]), float(np.min(rmaxf(th)))))
print("exact_end_convergence exit 0")
