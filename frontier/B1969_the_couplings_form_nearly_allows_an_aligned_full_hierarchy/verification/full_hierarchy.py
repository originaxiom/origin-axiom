"""B1969 (P-879; main, 2026-11-19; data-free): does an aligned charge-consistent mixing allow a FULL hierarchy, for any
channels at all?

B1736's coupling Y(h; u, w) = u h^T + h u^T - (u.h) 1 + w [h]_x; the charge rule (up: conj(h) with (u_u, w_u); down: h
with (u_d, w_d)); every channel free in C^4 per sector; h = (cos t, i sin t, 0), reality r = cos 2t.  B1967 found aligned
mixings with m2/m3 near 1e-3 at reality 0.003, but always with the light pair unsplit (m1/m2 driven to its allowed 0.5).
The heuristic: at small r the light vectors move away from conj(h) only if m2 is about r |u|, and m1 <= r |u| always
(the test vector conj(h)), so m1 and m2 are pushed to one scale.
A FULL-HIERARCHY COUNTEREXAMPLE: smallest diagonal |V| >= 0.9, both m2/m3 in [1e-6, 1e-2], both m1/m2 in [1e-6, 0.1].
Objective: log10(max m2/m3) + log10(max m1/m2) + 20 max(0, 0.9 - diag) + 20 max(0, -6 - log10(min m2/m3))
           + 20 max(0, -6 - log10(min m1/m2)) + 20 max(0, log10(max m1/m2 / 0.1)).
Nelder-Mead, 60 starts of 8,000 evaluations per r.

EXPECTATIONS, written before the run (main, 2026-11-19):
 F1  no r in the list admits a full-hierarchy counterexample; prior 0.65.
 F2  at every r the best result either misses alignment or has max m1/m2 near its 0.1 bound (the light pair pushed
     together); prior 0.7.
    python3 full_hierarchy.py > full_hierarchy_run.txt"""
import json
import numpy as np
from scipy.optimize import minimize
def cross(v): return np.array([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]])
def Y(h, u, w): return np.outer(u, h) + np.outer(h, u) - (u @ h) * np.eye(3) + w * cross(h)
def U(M):
    Uu, s, _ = np.linalg.svd(M); o = np.argsort(s); return Uu[:, o], s[o]
def h_of(r):
    t = 0.5 * np.arccos(r); return np.array([np.cos(t), 1j * np.sin(t), 0])
def evaluate(p, h):
    uu = p[0:3] + 1j * p[3:6]; wu = p[6] + 1j * p[7]; ud = p[8:11] + 1j * p[11:14]; wd = p[14] + 1j * p[15]
    Uu, su = U(Y(np.conj(h), uu, wu)); Ud, sd = U(Y(h, ud, wd))
    V = Uu.conj().T @ Ud; diag = min(abs(V[k, k]) for k in range(3))
    r2 = (su[1] / su[2], sd[1] / sd[2]); r1 = (su[0] / max(su[1], 1e-300), sd[0] / max(sd[1], 1e-300))
    L = lambda v: np.log10(max(v, 1e-300))
    f = L(max(r2)) + L(max(r1)) + 20 * max(0.0, 0.9 - diag) + 20 * max(0.0, -6 - L(min(r2))) + 20 * max(0.0, -6 - L(min(r1))) + 20 * max(0.0, L(max(r1) / 0.1))
    return f, diag, r2, r1
if __name__ == "__main__":
    rng = np.random.default_rng(1969); found = {}
    for r in (0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 0.6, 1.0):
        h = h_of(r); best = None
        for s in range(60):
            res = minimize(lambda p: evaluate(p, h)[0], rng.normal(size=16), method="Nelder-Mead", options={"maxiter": 8000, "maxfev": 8000, "xatol": 1e-9, "fatol": 1e-11})
            ev = evaluate(res.x, h)
            if best is None or ev[0] < best[0]: best = ev + (list(res.x),)
        f, d, r2, r1, px = best
        ce = d >= 0.9 and all(1e-6 <= v <= 1e-2 for v in r2) and all(1e-6 <= v <= 0.1 for v in r1)
        if ce: found[str(r)] = px
        print("r %.3f: best %.3f; smallest diagonal %.3f; m2/m3 up %.1e down %.1e; m1/m2 up %.2e down %.2e -> %s" % (r, f, d, r2[0], r2[1], r1[0], r1[1], "FULL-HIERARCHY COUNTEREXAMPLE" if ce else "none"), flush=True)
    json.dump(found, open("full_hierarchy_found.json", "w"), indent=1)
