"""S304 (value-free; main's b1656_funcs): the web seat's cross-kernel identity on MAIN's channel kernels:
K_down,s(u) * K_up,s(u) = wp(u) - wp(v_s), v_s = A_s tau - B_s from K_down,s's multipliers (K(u+1) = e^{2 pi i A} K, K(u+tau) = e^{2 pi i B} K).
    OPENBLAS_NUM_THREADS=1 nice -n 10 python3 -B p3b_cross_kernel_on_main.py"""
import os
for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ.setdefault(v, "1")
import sys, io, contextlib, pathlib
import numpy as np, mpmath as mp
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parents[4]) + "/frontier/B1723_the_golden_valley/verification"); _a = sys.argv; sys.argv = ["x"]
with contextlib.redirect_stdout(io.StringIO()):
    import b1656_funcs as B
sys.argv = _a
mp.mp.dps = 25
def th1d(z, t, k): return mp.pi ** k * mp.jtheta(1, mp.pi * z, mp.exp(1j * mp.pi * t), derivative=k)
def wp(z, t):
    t0, t1, t2 = th1d(z, t, 0), th1d(z, t, 1), th1d(z, t, 2)
    return complex(-(t2 / t0 - (t1 / t0) ** 2) + th1d(0, t, 3) / (3 * th1d(0, t, 1)))
worst, n = 0.0, 0
for t in (complex(0.31, 2.05), complex(0.13, 1.30)):
    for a, b in ((1 / 7, 3 / 7), (2 / 9, 1 / 3), (5 / 12, 1 / 4)):
        w = a * t + b
        xd, yd = B.sector_twists(w, t, B.SIXY["Q"], B.SIXY["d"]); Rd = B.residues(xd, yd, t)
        xu, yu = B.sector_twists(w, t, B.SIXY["Q"], B.SIXY["u"]); Ru = B.residues(xu, yu, t)
        us = np.array([0.11 + 0.07j, -0.2 + 0.15j, 0.05 - 0.31j])
        for s in B.UNITS:
            if abs(Rd[s]) < 1e-12 or abs(Ru[s]) < 1e-12: continue
            Kd = B.pairs(xd, yd, us, t)[s] / Rd[s]; Ku = B.pairs(xu, yu, us, t)[s] / Ru[s]
            A = np.angle((B.pairs(xd, yd, us[:1] + 1, t)[s] / Rd[s])[0] / Kd[0]) / (2 * np.pi)
            Bm = np.angle((B.pairs(xd, yd, us[:1] + t, t)[s] / Rd[s])[0] / Kd[0]) / (2 * np.pi)
            v = A * t - Bm
            for k, u in enumerate(us):
                d = abs(Kd[k] * Ku[k] - (wp(mp.mpc(u.real, u.imag), mp.mpc(t.real, t.imag)) - wp(mp.mpc(v.real, v.imag), mp.mpc(t.real, t.imag))))
                worst = max(worst, d / abs(Kd[k] * Ku[k])); n += 1
print("K_down,s K_up,s = wp(u) - wp(A tau - B) on main's kernels: max relative dev %.1e over %d (tau, line, channel, u) cases" % (worst, n))
