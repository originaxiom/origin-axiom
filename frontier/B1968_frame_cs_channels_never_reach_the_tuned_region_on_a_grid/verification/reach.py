"""B1968 (P-879 restated; main, 2026-11-19; data-free): do frame C's own channels ever reach the tuned region?

At each point, frame C's code gives each sector's channel matrix Mw (B1945's split, unchanged).  Its quaternion
components give B1736's channels (u, w), and Y(h) = u h^T + h u^T - (u.h) 1 + w [h]_x for any Higgs triplet h (checked
against the frame's code to 1e-33 at B1966).  Under the charge rule (up: conj(h), down: h) an adversary searches h in
C^3 (unit, global phase fixed; Nelder-Mead, 8 starts, 2000 evaluations each) for an aligned mixing with a hierarchy.
A COUNTEREXAMPLE is: smallest diagonal |V| >= 0.9, both sectors' m2/m3 in [1e-6, 1e-2], both m1/m2 <= 0.5.
Objective: log10(max m2/m3) + 20 max(0, 0.9 - diag) + 20 max(0, -6 - log10(min m2/m3)) + 20 max(0, log10(max m1/m2 / 0.5)).
Grid: the 24 points of order 5 and the 48 of order 7; columns x = 0, 0.13, 0.25, 0.5; heights 1, 1.5, 2, 3, 4, 6, 10.

EXPECTATIONS, written before the run (main, 2026-11-19):
 Q1  no point of the grid admits a counterexample; prior 0.6.
 Q2  if any does, it is at height 1.5 or below; prior 0.7 given one exists.
 Q3  the least max m2/m3 at alignment 0.9, over the grid, is above 0.1 at every height from 3; prior 0.6.
    python3 -B reach.py > reach_run.txt"""
import sys, pathlib, json
from fractions import Fraction as Fr
import numpy as np
from scipy.optimize import minimize
ROOT = next((q for q in [*pathlib.Path(__file__).resolve().parents, pathlib.Path.cwd()] if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file()))
sys.path.insert(0, str(next((ROOT / "frontier").glob("B1945_*")) / "verification"))
import determinant_law as DL


def channels(x, y, a, b, sec):
    Mw = DL.parts(x, y, a, b, sec)[1]
    m0 = complex((Mw[0, 0] + Mw[1, 1]) / 2); m1 = complex((Mw[0, 0] - Mw[1, 1]) / 2j); m2 = complex((Mw[0, 1] - Mw[1, 0]) / 2); m3 = complex((Mw[0, 1] + Mw[1, 0]) / 2j)
    f = np.array([m0, -m3, m1]); mu = m2
    return -2 * f, -2 * mu          # u, w with Y = u h^T + h u^T - (u.h) 1 + w [h]_x  (h in frame C's generation order)


def cross(v): return np.array([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]])
def Y(h, u, w): return np.outer(u, h) + np.outer(h, u) - (u @ h) * np.eye(3) + w * cross(h)
def U(M):
    Uu, s, _ = np.linalg.svd(M); o = np.argsort(s); return Uu[:, o], s[o]


def h_of(p):
    h = np.array([p[0] + 0j, p[1] + 1j * p[2], p[3] + 1j * p[4]]); return h / np.linalg.norm(h)


def score(p, ch):
    h = h_of(p); (uu, wu), (ud, wd) = ch
    Uu, su = U(Y(np.conj(h), uu, wu)); Ud, sd = U(Y(h, ud, wd))
    V = Uu.conj().T @ Ud; diag = min(abs(V[k, k]) for k in range(3))
    r2 = (su[1] / su[2], sd[1] / sd[2]); r1 = max(su[0] / max(su[1], 1e-300), sd[0] / max(sd[1], 1e-300))
    f = np.log10(max(max(r2), 1e-300)) + 20 * max(0.0, 0.9 - diag) + 20 * max(0.0, -6 - np.log10(max(min(r2), 1e-300))) + 20 * max(0.0, np.log10(max(r1, 1e-300) / 0.5))
    return f, diag, r2, r1, abs(h @ h)


if __name__ == "__main__":
    rng = np.random.default_rng(1968)
    pts = [(Fr(i, n), Fr(j, n)) for n in (5, 7) for i in range(n) for j in range(n) if (i, j) != (0, 0)]
    found, rows = [], []
    for x in ("0", "0.13", "0.25", "0.5"):
        for y in (1.0, 1.5, 2.0, 3.0, 4.0, 6.0, 10.0):
            least = []
            for (a, b) in pts:
                ch = (channels(x, y, a, b, "up"), channels(x, y, a, b, "down"))
                best = None
                for s in range(8):
                    res = minimize(lambda p: score(p, ch)[0], rng.normal(size=5), method="Nelder-Mead", options={"maxfev": 2000, "xatol": 1e-7, "fatol": 1e-9})
                    sc = score(res.x, ch)
                    if best is None or sc[0] < best[0]: best = sc + (list(res.x),)
                f, diag, r2, r1, rr, px = best
                ce = diag >= 0.9 and all(1e-6 <= v <= 1e-2 for v in r2) and r1 <= 0.5
                if ce: found.append((x, y, str(a), str(b), diag, r2, r1, rr, px))
                if diag >= 0.9: least.append(max(r2))
            rows.append((x, y, len(pts), len(least), min(least) if least else None))
            print("x %4s height %4.1f: %d points; alignment 0.9 reached at %d; least max m2/m3 there %s; counterexamples so far %d" % (
                x, y, len(pts), len(least), ("%.2e" % min(least)) if least else "none", len(found)), flush=True)
    print("COUNTEREXAMPLES: %d" % len(found))
    for c in found[:20]: print("  ", c[:8])
    json.dump([[str(v) if not isinstance(v, (int, float, list, tuple)) else v for v in c] for c in found], open(pathlib.Path(__file__).with_name("reach_found.json"), "w"), indent=1, default=str)
