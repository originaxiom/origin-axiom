"""The web seat, 2026-11-05: the agy lane's Theorem 94 (Stage 14, 881538c8e) and its two new levels, checked. Data-free.

Theorem 94 (toe_closure.py 16107-16247 at 881538c8e) evaluates B1840's E1-E3 at tau = 0.25 + 2.75i and registers two
further levels:
  "E_4 = L(+-i/2) = ln 2 - Re g(i/2)", "the unique horocycle inscribed inside the flat Dirichlet incircle |z| <= 1/2,
  tangent at the imaginary semi-axis points z = +-i/2 (whereas E_3 = L(1/2) is circumscribed around |z| = 1/2 and tangent
  at z = 1/2)"; and "E_5 = L_pi = L_max + 2 - 2 pi/A_cusp", the horocycle of area pi ("Gauss-Bonnet equipartition").
Its own check evaluates the L(i/2) horocycle's radius at theta = pi/2 and theta = 0 only.

Checked here at all 54 of B1667's points (B1667's sealed instrument imported unchanged: frobenius, g_local and
horocycle_radius, on its json's (tau, c)):
  (1) the L(i/2) horocycle: its largest radius over theta (720 rays, then a local refinement), against 1/2;
  (2) the L(1/2) horocycle: its smallest radius over theta, against 1/2; and L(1/2) against the json's L_max;
  (3) the levels of the circle |z| = 1/2 itself: L_in = ln 2 - min_t Re g(e^{it}/2), the largest horoball inside the
      incircle, and L_out = ln 2 - max_t Re g(e^{it}/2), the smallest containing it, with their angles; and arg c;
  (4) E_5: L_pi - L_max = 2 - 2 pi/A_cusp (the level at h = lambda/pi), against B1840's E4, L_4 - L_max = pi/2 - 2 pi/A_cusp.
Expected before the run, from g(z) = (c/4) z^2 + O(z^4): (1) and (2) hold exactly where c is real and positive; where c
is not real, the L(i/2) horocycle leaves the incircle and the L(1/2) horocycle passes inside it.

    python3 agy_stage14_ends_check.py <main checkout>     (main at c70b356f0 for B1667)
"""
import contextlib
import importlib.util
import io
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
RHI = 0.9


def extreme(f, sense, n=720):
    """the max (sense = 1) or min (sense = -1) of f on [0, 2 pi): a grid, then two local refinements"""
    t = np.linspace(0, 2 * np.pi, n, endpoint=False)
    v = np.array([sense * f(x) for x in t])
    k = int(np.argmax(v)); t0, w = t[k], 2 * np.pi / n
    for _ in range(2):
        tt = np.linspace(t0 - w, t0 + w, 201)
        vv = np.array([sense * f(x) for x in tt])
        k = int(np.argmax(vv)); t0, w = tt[k], 2 * w / 200
    return sense * float(vv[k]), float(t0 % (2 * np.pi))


def work(p):
    tau = complex(*p["tau"]); c = complex(*p["c"])
    with contextlib.redirect_stdout(io.StringIO()):
        lat = C.Lattice(tau)
        al, be = C.frobenius(lat, c)
    reg = lambda z: float(C.g_local(al, be, z).real)
    L_half = math.log(2) - reg(0.5)
    L_ihalf = math.log(2) - reg(0.5j)
    r_i = lambda th: float(C.horocycle_radius(al, be, L_ihalf, th, RHI))
    r_h = lambda th: float(C.horocycle_radius(al, be, L_half, th, RHI))
    rmax_i, th_i = extreme(r_i, 1)
    rmin_h, th_h = extreme(r_h, -1)
    gmin, t_in = extreme(lambda t: reg(0.5 * np.exp(1j * t)), -1)
    gmax, t_out = extreme(lambda t: reg(0.5 * np.exp(1j * t)), 1)
    A = float(p["cusp_area"]); Lmax = float(p["L_max"])
    return dict(tau=tau, argc=float(np.angle(c)), c=c, L_half=L_half, L_ihalf=L_ihalf, Lmax=Lmax,
                rmax_i=rmax_i, th_i=th_i, r_i_pi2=r_i(np.pi / 2), rmin_h=rmin_h, th_h=th_h,
                L_in=math.log(2) - gmin, t_in=t_in, L_out=math.log(2) - gmax, t_out=t_out,
                d5=2 - 2 * np.pi / A, d4=np.pi / 2 - 2 * np.pi / A, A=A)


if __name__ == "__main__":
    with Pool(4) as pool:
        R = pool.map(work, POINTS, chunksize=1)
    print("THEOREM 94's LEVELS, CHECKED at B1667's 54 points (data-free; radii on the horocycle, B1667's horocycle_radius)")
    for r in R:
        print("tau %.4f%+.4fi | arg c %+.5f | L(i/2) %.6f: r at pi/2 %.12f, largest r %.9f at theta %.4f | L(1/2) %.6f "
              "(- L_max %+.1e): smallest r %.9f at theta %.4f | L_in %.6f at t %.4f, L_out %.6f at t %.4f | "
              "L(i/2) - L_max %.5f | delta_5 %.5f, delta_4 %.5f" % (
                  r["tau"].real, r["tau"].imag, r["argc"], r["L_ihalf"], r["r_i_pi2"], r["rmax_i"], r["th_i"],
                  r["L_half"], r["L_half"] - r["Lmax"], r["rmin_h"], r["th_h"], r["L_in"], r["t_in"], r["L_out"],
                  r["t_out"], r["L_ihalf"] - r["Lmax"], r["d5"], r["d4"]))
    real = [r for r in R if abs(r["argc"]) < 1e-9]
    nonreal = [r for r in R if abs(r["argc"]) >= 1e-9]
    print("SUMMARY")
    print("  points with c real: %d; with c not real: %d; |arg c| range %.2e-%.2e" % (
        len(real), len(nonreal), min(abs(r["argc"]) for r in R), max(abs(r["argc"]) for r in R)))
    print("  (1) the L(i/2) horocycle inside |z| <= 1/2 (largest r <= 1/2 + 1e-9) at %d of %d points; "
          "largest r - 1/2: range %.2e to %.2e" % (
              sum(1 for r in R if r["rmax_i"] <= 0.5 + 1e-9), len(R), min(r["rmax_i"] - 0.5 for r in R),
              max(r["rmax_i"] - 0.5 for r in R)))
    print("  (2) the L(1/2) horocycle outside |z| = 1/2 (smallest r >= 1/2 - 1e-9) at %d of %d points; "
          "1/2 - smallest r: range %.2e to %.2e; |L(1/2) - L_max| largest %.1e" % (
              sum(1 for r in R if r["rmin_h"] >= 0.5 - 1e-9), len(R), min(0.5 - r["rmin_h"] for r in R),
              max(0.5 - r["rmin_h"] for r in R), max(abs(r["L_half"] - r["Lmax"]) for r in R)))
    print("  (3) L_in - L(i/2): range %.2e to %.2e; L(1/2) - L_out: range %.2e to %.2e" % (
        min(r["L_in"] - r["L_ihalf"] for r in R), max(r["L_in"] - r["L_ihalf"] for r in R),
        min(r["L_half"] - r["L_out"] for r in R), max(r["L_half"] - r["L_out"] for r in R)))
    print("  (4) delta_5 = 2 - 2 pi/A_cusp: range %.5f-%.5f; delta_5 - delta_4 = 2 - pi/2 = %.6f at every point "
          "(largest deviation %.1e); L(i/2) - L_max range %.5f-%.5f" % (
              min(r["d5"] for r in R), max(r["d5"] for r in R), 2 - np.pi / 2,
              max(abs(r["d5"] - r["d4"] - (2 - np.pi / 2)) for r in R), min(r["L_ihalf"] - r["Lmax"] for r in R),
              max(r["L_ihalf"] - r["Lmax"] for r in R)))
