"""P-542 (2026-11-19): THE RADII BETWEEN B1667's GRID POINTS, MEASURED.  B1726's census evaluator (and B1821's, which
reuses it) reads the end radii L_max and L_2 off B1667's column at Re tau = 1/4 (Im tau = 1.0 to 4.0 in steps of 0.25) by
linear interpolation in Im tau.  P-542 bounded the error from the column's slope jumps.  This script measures it: B1667's
own sealed instrument (imported unchanged, its sha256 checked) computes L_max and L_2 at the 13 grid points and at the 12
midpoints between them along Re tau = 1/4, by B1667's own continuation (track to the first point, then Newton walks along
Im tau); the error at each midpoint is the measured radius minus the linear interpolant of its two neighbours.  The grid
points are compared with B1667's committed column, so the run checks its own reproduction.  Data-free.
    python3 -B radius_midpoints.py > radius_midpoints_run.txt      (one process; a few minutes)"""
import os
for _v in ("OMP_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")
import sys, json, hashlib, pathlib, importlib.util, time
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
B1667 = ROOT / "frontier" / "B1667_the_canonical_cusp" / "verification"
SRC_SHA = "dd5fe6893fd2d403c066c4635f3d2bbde25c855674ea031a02495e2642506f6b"
assert hashlib.sha256((B1667 / "the_canonical_cusp.py").read_bytes()).hexdigest() == SRC_SHA
_spec = importlib.util.spec_from_file_location("b1667_cusp", B1667 / "the_canonical_cusp.py")
C = importlib.util.module_from_spec(_spec); sys.modules["b1667_cusp"] = C; _spec.loader.exec_module(C)

X = 0.25
GRID = [1.0 + 0.25 * k for k in range(13)]
MIDS = [1.125 + 0.25 * k for k in range(12)]


def radii(tau, c):
    """L_max and L_2 exactly as B1667's point() computes them (its lines for lam, h_max and Im B), without the lifts"""
    lat, z0, Aa, Ab = C.monodromy(tau, c)
    P0 = C.mobius_of(C.puncture_loop(lat, c, z0, 0.05))
    g, Ra, Rb, RP, lam = C.normalise(Aa, Ab, P0)
    lam = abs(lam.real); mc8 = C.min_c(Ra, Rb, 8)
    al, be = C.frobenius(lat, c)
    ib = float(C.local_B(lat, c, z0, g, lam, al, be, 0.05))
    return (2 * C.np.pi / lam) * (1.0 / mc8 - ib), C.np.pi - (2 * C.np.pi / lam) * ib


def main():
    t0 = time.time()
    committed = {round(r[0], 6): (r[1], r[2]) for r in json.loads((B1667 / "the_canonical_cusp.json").read_text())["readout"]["column_025"]}
    ys = sorted(GRID + MIDS); tau = complex(X, ys[0]); c = C.track(tau); c, res = C.solve_accessory(tau, c)
    out = {}
    for k, y in enumerate(ys):
        if k:
            c, r = C.newton_walk(tau, c, complex(X, y), step=0.04); tau = complex(X, y)
        out[y] = radii(tau, c)
    rep = max(max(abs(out[y][0] - committed[round(y, 6)][0]), abs(out[y][1] - committed[round(y, 6)][1])) for y in GRID)
    print("grid points reproduced against B1667's committed column: largest difference %.2e" % rep)
    print("   Im tau   L_max(mid)  interp. error   L_2(mid)  interp. error")
    em, e2 = [], []
    for y in MIDS:
        lo, hi = y - 0.125, y + 0.125
        im = 0.5 * (out[lo][0] + out[hi][0]); i2 = 0.5 * (out[lo][1] + out[hi][1])
        em.append(out[y][0] - im); e2.append(out[y][1] - i2)
        print("   %.3f   %.6f   %+.2e      %.6f   %+.2e" % (y, out[y][0], em[-1], out[y][1], e2[-1]))
    print("largest |interpolation error| at the midpoints: L_max %.2e, L_2 %.2e" % (max(map(abs, em)), max(map(abs, e2))))
    print("largest |interpolation error| in 2 pi L: L_max %.2e, L_2 %.2e" % (2 * C.np.pi * max(map(abs, em)), 2 * C.np.pi * max(map(abs, e2))))
    print("(%.0f s)" % (time.time() - t0))


if __name__ == "__main__":
    main()
