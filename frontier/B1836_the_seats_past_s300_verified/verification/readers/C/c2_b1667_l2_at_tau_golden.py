"""C2 (P-663, B08): B1667's L_2 at the lane's cell tau_Golden = 1/sqrt5 + i phi^2, computed with B1667's own functions
(track -> solve_accessory -> monodromy/normalise/frobenius/local_B; L_2 = pi - (2 pi/lam) Im B), against
(a) main's convention: cm_zero_line.radii (B1667's Re tau = 1/4 column, np.interp in Im tau, as B1726 does), which equals
    np.interp on the five consecutive nodes 2.0..3.0 of that column (the lane's table, if C1's fingerprint is right);
(b) the literal 2.3577376878276057 (B1832 c11: Theorems 23/25/26).  Controls: two committed grid points re-solved.
Main's code only; single-threaded."""
import os
for v in ("OMP_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"): os.environ[v] = "1"
import importlib.util, json, math, pathlib, sys
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[5]
V = ROOT / "frontier/B1667_the_canonical_cusp/verification"
spec = importlib.util.spec_from_file_location("b1667", V / "the_canonical_cusp.py"); M = importlib.util.module_from_spec(spec)
sys.argv = ["x"]; spec.loader.exec_module(M)
pts = json.loads((V / "the_canonical_cusp.json").read_text())["points"]

def L2_at(tau, start=(1j, 0.0)):
    c = M.track(tau, start=start); c, res = M.solve_accessory(tau, c)
    lat, z0, Aa, Ab = M.monodromy(tau, c)
    P0 = M.mobius_of(M.puncture_loop(lat, c, z0, 0.05))
    g, Ra, Rb, RP, lam = M.normalise(Aa, Ab, P0); lam = abs(lam.real)
    al, be = M.frobenius(lat, c)
    ib = float(M.local_B(lat, c, z0, g, lam, al, be, 0.05))
    return math.pi - (2 * math.pi / lam) * ib, float(np.max(np.abs(res)))

out = []
for (x, y) in ((0.25, 2.5), (0.45, 2.75)):                     # controls against the committed table
    L2, r = L2_at(complex(x, y)); ref = [p for p in pts if abs(p["tau"][0]-x) < 1e-9 and abs(p["tau"][1]-y) < 1e-9][0]["L_2"]
    out.append("control (%.2f, %.2f): |L2 - committed| = %.2e (residual %.1e)" % (x, y, abs(L2 - ref), r))
phi = (1 + math.sqrt(5)) / 2; tg = complex(1 / math.sqrt(5), phi * phi)
L2g, r = L2_at(tg)
col = sorted((p["tau"][1], p["L_2"]) for p in pts if abs(p["tau"][0] - 0.25) < 1e-9)
radii = float(np.interp(tg.imag, [c[0] for c in col], [c[1] for c in col]))
five = [c for c in col if 2.0 - 1e-9 <= c[0] <= 3.0 + 1e-9]
interp5 = float(np.interp(tg.imag, [c[0] for c in five], [c[1] for c in five]))
lit = 2.3577376878276057
out.append("tau_Golden exact B1667 L_2 = %.12f (accessory residual %.1e)" % (L2g, r))
out.append("main's radii() column interpolation = %.12f ; five-node [2.0..3.0] interpolation = %.12f ; identical: %s" % (radii, interp5, radii == interp5))
out.append("exact - interpolation = %.3e ; exact - 2.3577376878276057 = %.3e" % (L2g - radii, L2g - lit))
print("\n".join(out)); pathlib.Path(__file__).with_name("c2_run.txt").write_text("\n".join(out) + "\n")
