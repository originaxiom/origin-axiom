"""The web seat, 2026-11-05: THE PRINCIPLED ENDS (cc's ask 1, P-685/P-687), the levels' instrument. Data-free.

Computes, from B1667's own geometry only (its sealed instrument the_canonical_cusp.py, imported unchanged, and its json's
54 points (tau, c)), each candidate cut level L at each tau, and the geometric checks behind the list's readings. No mass,
no ratio, no chi2, no comparison with data. The level is L = log(1/|z|) - Re g(z) on the horocycle, B1667's convention:
the horoball {L(z) > L} with g the Frobenius ratio (y2 = y1 log z + z^1/2 sum beta z^m).

Per point:
  control  B1667's L_max, L_2, cusp area and Im B recomputed here against its json (must agree to 1e-8);
  E1  L_2 = pi - (2 pi/lam) Im B, with the length lam/h_2 of its horocycle (2 by construction) and the cusp area;
  E3  L_max = (2 pi/lam)(1/min|c| - Im B), and the Weierstrass check: the level of the horocycle through each half-period
      p with |p| < 0.9 (where the Frobenius series converges well), L_W(p) = log(1/|p|) - Re g(p); max_p L_W(p) against
      L_max. Expected before the run: equal, since the maximal horoball first touches its translate by the shortest
      lattice vector, and the rotation by pi about that vector's midpoint (an isometry: the elliptic involution composed
      with the translation) fixes the contact point, which is therefore the half-period;
  E2  ln 2, the largest round flat disc in the Dirichlet cell (the shortest lattice vector, found by search, and the
      cell's inradius are printed), and its offset ln 2 - L_max against Re g(1/2);
  X   the density note's cancelling radius as a level, L_c = (1/2) log|G2(tau)| (G2 by its q-series), against L_max.

    python3 principled_levels.py <main checkout>     (main at c70b356f0)
"""
import importlib.util
import io
import contextlib
import json
import math
import pathlib
import sys
from multiprocessing import Pool

import numpy as np

ROOT = pathlib.Path(sys.argv[1]).resolve()
SRC = ROOT / "frontier" / "B1667_the_canonical_cusp" / "verification" / "the_canonical_cusp.py"
_spec = importlib.util.spec_from_file_location("b1667", SRC)
C = importlib.util.module_from_spec(_spec)
with contextlib.redirect_stdout(io.StringIO()):
    _spec.loader.exec_module(C)
POINTS = json.loads((SRC.parent / "the_canonical_cusp.json").read_text())["points"]


def g2(tau, n=60):
    q = np.exp(2j * np.pi * tau)
    s = sum(sum(d for d in range(1, k + 1) if k % d == 0) * q ** k for k in range(1, n))
    return np.pi ** 2 / 3 * (1 - 24 * s)


def shortest(tau, n=6):
    return min(abs(a + b * tau) for a in range(-n, n + 1) for b in range(-n, n + 1) if (a, b) != (0, 0))


def work(p):
    tau = complex(*p["tau"]); c = complex(*p["c"])
    with contextlib.redirect_stdout(io.StringIO()):
        lat, z0, Aa, Ab = C.monodromy(tau, c)
        P0 = C.mobius_of(C.puncture_loop(lat, c, z0, 0.05))
        g, Ra, Rb, RP, lam = C.normalise(Aa, Ab, P0)
        lam = abs(lam.real)
        mc8 = C.min_c(Ra, Rb, 8)
        al, be = C.frobenius(lat, c)
        imB = float(C.local_B(lat, c, z0, g, lam, al, be, 0.05))
    L_max = (2 * np.pi / lam) * (1.0 / mc8 - imB)
    L_2 = np.pi - (2 * np.pi / lam) * imB
    h_2 = (lam / (2 * np.pi)) * L_2 + imB
    halves = {"1/2": 0.5, "tau/2": tau / 2, "(1+tau)/2": (1 + tau) / 2, "(tau-1)/2": (tau - 1) / 2}
    LW = {k: float(np.log(1 / abs(v)) - C.g_local(al, be, v).real) for k, v in halves.items() if abs(v) < 0.9}
    kmax = max(LW, key=LW.get)
    G2 = g2(tau)
    return dict(tau=tau, L_max=float(L_max), L_2=float(L_2), A=float(lam * mc8), imB=imB, len2=float(lam / h_2),
                ctrl=max(abs(L_max - p["L_max"]), abs(L_2 - p["L_2"]), abs(lam * mc8 - p["cusp_area"]), abs(imB - p["imB"][1])),
                LW=LW, kmax=kmax, LWmax=LW[kmax], reg_half=float(C.g_local(al, be, 0.5).real),
                short=shortest(tau), L_c=float(0.5 * np.log(abs(G2))), G2=complex(G2))


if __name__ == "__main__":
    with Pool(4) as pool:
        R = pool.map(work, POINTS, chunksize=1)
    print("THE PRINCIPLED ENDS: B1667's 54 points; levels L = log(1/|z|) - Re g(z) on the horocycle (data-free)")
    for r in R:
        print("tau %.4f%+.4fi | ctrl %.1e | E1 L_2 %.5f (length %.12f, cusp area %.4f) | E3 L_max %.6f, L_W max %.6f at %s, "
              "diff %.1e; L_W %s | E2 ln2 - L_max %.6f, Re g(1/2) %.6f, shortest vector %.6f | X L_c %.5f, e^-L_c %.4f vs e^-L_max %.4f"
              % (r["tau"].real, r["tau"].imag, r["ctrl"], r["L_2"], r["len2"], r["A"], r["L_max"], r["LWmax"], r["kmax"],
                 r["LWmax"] - r["L_max"], {k: round(v, 5) for k, v in r["LW"].items()}, math.log(2) - r["L_max"], r["reg_half"],
                 r["short"], r["L_c"], math.exp(-r["L_c"]), math.exp(-r["L_max"])))
    d = [abs(r["LWmax"] - r["L_max"]) for r in R]
    print("SUMMARY")
    print("  control (B1667's json recomputed): largest deviation %.1e" % max(r["ctrl"] for r in R))
    print("  E1: horocycle length at L_2 within %.1e of 2 at every point; cusp area range %.3f-%.3f" % (
        max(abs(r["len2"] - 2) for r in R), min(r["A"] for r in R), max(r["A"] for r in R)))
    print("  E3: |max_p L_W(p) - L_max| largest %.1e, median %.1e; the contact half-period: %s" % (
        max(d), float(np.median(d)), {k: sum(1 for r in R if r["kmax"] == k) for k in sorted(set(r["kmax"] for r in R))}))
    print("  E2: shortest vector range %.6f-%.6f (inradius = half of it); ln 2 - L_max range %.5f-%.5f; "
          "|(ln 2 - L_max) - Re g(1/2)| largest %.1e" % (
        min(r["short"] for r in R), max(r["short"] for r in R), min(math.log(2) - r["L_max"] for r in R),
        max(math.log(2) - r["L_max"] for r in R), max(abs(math.log(2) - r["L_max"] - r["reg_half"]) for r in R)))
    print("  X: L_c range %.5f-%.5f; L_c < L_max at %d of %d points; e^-L_c range %.4f-%.4f" % (
        min(r["L_c"] for r in R), max(r["L_c"] for r in R), sum(1 for r in R if r["L_c"] < r["L_max"]), len(R),
        min(math.exp(-r["L_c"]) for r in R), max(math.exp(-r["L_c"]) for r in R)))
