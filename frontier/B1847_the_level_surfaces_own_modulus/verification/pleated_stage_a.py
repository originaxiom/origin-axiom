"""Stage A (data-free): tau -> the Fricke traces (x, y, z) of the hyperbolic punctured torus with conformal modulus tau
(B1667's uniformising monodromy at the Fuchsian accessory parameter), and its inverse by a 2D Newton on (Re tau, Im tau).
Round-trip check on known tau."""
import sys, pathlib, cmath, math, time
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "frontier/B1842_the_closure_instruments/verification"))
import exact_card_instrument as X
C = X.mods()["C"]
def traces_of(tau):
    c, res = X.accessory(tau)
    _, _, Aa, Ab = C.monodromy(tau, c)
    ta, tb, tab = C.traces(Aa, Ab)
    v = np.array([ta, tb, tab], dtype=complex)
    return v, c, res
def markov(v):
    x, y, z = v; return x*x + y*y + z*z - x*y*z
def invert(target_xy, tau0, tol=1e-10, maxit=30):
    tau = complex(tau0)
    for it in range(maxit):
        v, _, _ = traces_of(tau); F = np.array([v[0].real - target_xy[0], v[1].real - target_xy[1]])
        if np.max(np.abs(F)) < tol: return tau, it
        h = 1e-6; J = np.zeros((2, 2))
        for j, d in enumerate((h, 1j * h)):
            vd, _, _ = traces_of(tau + d); J[:, j] = [(vd[0].real - v[0].real) / h, (vd[1].real - v[1].real) / h]
        step = np.linalg.solve(J, -F); d = step[0] + 1j * step[1]
        if abs(d) > 0.15: d *= 0.15 / abs(d)
        tau = tau + d
    return tau, maxit
if __name__ == "__main__":
    t0 = time.time()
    for tau0, start in [(complex(0.23, 1.41), complex(0.0, 1.2)), (complex(-0.31, 1.07), complex(-0.2, 1.15))]:
        v, c, res = traces_of(tau0)
        print("tau0 %s: traces %s  imag parts %.1e  Markov x^2+y^2+z^2-xyz = %s  (accessory residual %.1e)" % (
            tau0, ["%.8f" % t.real for t in v], max(abs(t.imag) for t in v), "%.3e%+.3ei" % (markov(v).real, markov(v).imag), float(np.max(np.abs(res)))), flush=True)
        tau_r, it = invert((v[0].real, v[1].real), start)
        print("   inverted from %s in %d steps -> %s  |error| %.2e  (%.0f s)" % (start, it, tau_r, abs(tau_r - tau0), time.time() - t0), flush=True)
