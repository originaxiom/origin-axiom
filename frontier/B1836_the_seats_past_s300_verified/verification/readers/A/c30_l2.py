"""S301-A check c30 (value-free inputs; MAIN's code only: B1667's the_canonical_cusp.py, imported, its run not executed).
Theorem 30 (agy, c5c9236df) re-implements B1667's construction (Lame equation y'' + (wp/4 + c) y = 0, real monodromy,
L_2 = pi - (2 pi / lam) Im B) and claims (i) a hexagonal control L_2(omega) - L_max(omega) = 2 pi/3 and (ii) L_2 at
tau_Golden = 1/sqrt5 + i phi^2 and at its tau*.  Questions for P-663 (B08) and for the scoreboard's frame A:
  (a) B1667's own L_2, L_max at tau_Golden (L is an input, not a firewalled quantity);
  (b) how far the Re tau = 1/4 column read (B1726's compute(), cm_zero_line.radii: np.interp in Im tau) is from B1667's
      L(tau) at the actual Re tau -- main's frame A reads L that way too;
  (c) the omega control from B1667's disclosed eta^4 constants.
Optional argv: extra tau points 're,im' (e.g. the tau* found by c29)."""
import os
for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ.setdefault(v, "1")
import importlib.util, json, math, pathlib, sys
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[5]
P = ROOT / "frontier/B1667_the_canonical_cusp/verification/the_canonical_cusp.py"
spec = importlib.util.spec_from_file_location("b1667", P)
K = importlib.util.module_from_spec(spec)
spec.loader.exec_module(K)
col = sorted((p["tau"][1], p["L_max"], p["L_2"]) for p in json.loads((P.parent / "the_canonical_cusp.json").read_text())["points"] if abs(p["tau"][0] - 0.25) < 1e-9)


def L_pair(tau):
    tau = complex(tau)
    c = K.track(tau)
    c, res = K.solve_accessory(tau, c)
    lat, z0, Aa, Ab = K.monodromy(tau, c)
    P0 = K.mobius_of(K.puncture_loop(lat, c, z0, 0.05))
    g, Ra, Rb, RP, lam = K.normalise(Aa, Ab, P0)
    lam = abs(lam.real)
    mc8 = K.min_c(Ra, Rb, 8)
    al, be = K.frobenius(lat, c)
    ib = float(K.local_B(lat, c, z0, g, lam, al, be, 0.05))
    L_max = (2 * np.pi / lam) * (1.0 / mc8 - ib)
    L_2 = np.pi - (2 * np.pi / lam) * ib
    return float(L_max), float(L_2), float(np.max(np.abs(res)))


def col_read(im):
    return (float(np.interp(im, [q[0] for q in col], [q[1] for q in col])), float(np.interp(im, [q[0] for q in col], [q[2] for q in col])))


if __name__ == "__main__":
    print("c30: L_2 and L_max on B1667's own solver")
    print("  (c) omega control (B1667's disclosed eta^4 constants): L_2 - L_max - 2pi/3 = %.1e" % (K.L_2_ETA - K.L_MAX_ETA - 2 * math.pi / 3))
    # the stored column itself, re-run at two stored points (instrument check)
    stored = {round(p["tau"][1], 4): p for p in json.loads((P.parent / "the_canonical_cusp.json").read_text())["points"] if abs(p["tau"][0] - 0.25) < 1e-9}
    for im in (2.5, 3.0):
        lm, l2, res = L_pair(complex(0.25, im))
        print("  instrument: at 0.25 + %.2fi re-run vs stored: L_max %.1e, L_2 %.1e (residual %.0e)" % (im, abs(lm - stored[im]["L_max"]), abs(l2 - stored[im]["L_2"]), res))
    # L_2 - L_max is not 2pi/3 off omega: at i (stored)
    pi_ = [p for p in json.loads((P.parent / "the_canonical_cusp.json").read_text())["points"] if p["tau"] == [0.0, 1.0]][0]
    print("  at tau = i (stored): L_2 - L_max - 2pi/3 = %.3f  (the 2pi/3 is omega's, not a general identity)" % (pi_["L_2"] - pi_["L_max"] - 2 * math.pi / 3))
    phi = (1 + 5 ** 0.5) / 2
    pts = [("tau_Golden = 1/sqrt5 + i phi^2", complex(1 / 5 ** 0.5, phi * phi))]
    for a in sys.argv[1:]:
        re_, im_ = (float(x) for x in a.split(","))
        pts.append(("extra point %s" % a, complex(re_, im_)))
    for label, t in pts:
        lm, l2, res = L_pair(t)
        cm, c2 = col_read(t.imag)
        lm4, l24, _ = L_pair(complex(0.25, t.imag))
        print("  %s: B1667 L_max = %.10f, L_2 = %.10f (accessory residual %.0e)" % (label, lm, l2, res))
        print("      the Re tau = 1/4 column read (np.interp, as B1726/cm_zero_line do): L_max %.6f, L_2 %.6f -> off by %.2e, %.2e"
              % (cm, c2, cm - lm, c2 - l2))
        print("      B1667 at 0.25 + i Im tau exactly: L_max %.6f, L_2 %.6f -> Re-tau dependence %.2e, %.2e; interpolation error %.1e, %.1e"
              % (lm4, l24, lm4 - lm, l24 - l2, cm - lm4, c2 - l24))
