"""B1651 controls (run before the seal; no cell computed): the helpers on known or banked cases only."""
import json, os, pathlib
HERE = pathlib.Path(__file__).resolve().parent
src = (HERE / "where_a_higgs_couples.py").read_text().split("rng = np.random.default_rng(1651)")[0]
ns = {"__file__": str(HERE / "where_a_higgs_couples.py"), "__name__": "controls"}
exec(compile(src, "defs", "exec"), ns)
mp, np = ns["mp"], ns["np"]
out = {}

# 1. the contour coefficient on a known Laurent series
f = lambda w: 1 / w + 2 + 3 * w
out["laurent_residue_err"] = abs(complex(ns["contour_coeff"](f, -1)) - 1)
out["laurent_constant_err"] = abs(complex(ns["contour_coeff"](f, 0)) - 2)

# 2. the explicit-root thetas: equal to mpmath's where the principal branch is right (|Re tau| < 1/2), and equal to the
#    direct series sum exp(i pi tau (n + 1/2)^2) exp(i (2n + 1) z) (times -i (-1)^n for th1) at Re tau > 1
t = mp.mpc(0.11, 1.17); q = mp.exp(1j * mp.pi * t)
out["theta_vs_mpmath_max"] = max(float(abs(ns["th"](n, z, t) - mp.jtheta(n, z, q)))
                                for n in (1, 2, 3, 4) for z in (mp.mpc(0.3, 0.1), mp.mpc(-0.7, 0.4), mp.mpf(1.1)))
t1 = mp.mpc(1.37, 0.91)
def series(n, z, tt, N=40):
    s = 0
    for k in range(-N, N + 1):
        term = mp.exp(1j * mp.pi * tt * (k + mp.mpf(1) / 2) ** 2) * mp.exp(1j * (2 * k + 1) * z)
        s += term if n == 2 else -1j * (-1) ** k * term
    return s
out["theta12_vs_direct_series_at_Re_tau_1.37_max"] = max(float(abs(ns["th"](n, z, t1) - series(n, z, t1)))
                                                         for n in (1, 2) for z in (mp.mpc(0.3, 0.1), mp.mpf(1.1)))

# 3. the puncture triplet is B1644's R (up to scale); its isotropy in mpmath is Jacobi's identity (banked)
R_banked = np.array([complex(-mp.jtheta(2, 0, q) ** 2), complex(-mp.jtheta(4, 0, q) ** 2), complex(1j * mp.jtheta(3, 0, q) ** 2)])
out["puncture_triplet_is_banked_R"] = ns["ov"](ns["triplet"](t, 0), R_banked)
out["puncture_isotropy_mp_jacobi"] = ns["isotropy_mp"](t, 0)

# 4. the two-torsion class of constructed points (lattice arithmetic only)
pts = {"1/2": mp.pi * (mp.mpf(3) / 2 + 2 * t), "tau/2": mp.pi * (-1 + 3 * t / 2), "(1+tau)/2": mp.pi * (mp.mpf(1) / 2 - t / 2),
       "0": mp.pi * (2 - t)}
out["class_of_constructed_points"] = {k: ns["two_torsion_class"](z, t)[0] == k for k, z in pts.items()}

# 5. the joint-eigenspace finder on pairs known by construction
AL = ns["AL"]; Rx_pi = np.diag([1.0, -1.0, -1.0])
out["common_lines_AL_AL"] = len(ns["common_lines"](AL, AL)[0])            # 3: every eigenline of AL
out["common_lines_Rxpi_AL"] = len(ns["common_lines"](Rx_pi, AL)[0])       # 3: e_x, and (0, 1, +-i) in the -1 plane
out["common_lines_diag_vs_swap"] = len(ns["common_lines"](np.diag([1.0, 2.0, 3.0]),
                                                          np.array([[0.0, 1, 0], [1, 0, 0], [0, 0, 1]]))[0])   # 1: e_z
out["common_dims_Rxpi_Rxpi"] = sorted({d for *_, d in ns["common_lines"](Rx_pi, Rx_pi)[0]})   # [1, 2]: axis, then the plane
out["eig_clusters_of_Rxpi"] = len(ns["eig_clusters"](Rx_pi))              # 2 distinct: 1 and -1

# 6. Ad((1 + i)/sqrt2) turns e_j to e_k (quaternion conjugation by hand); a constructed tie for best_v4
out["ad_gL_ej"] = [round(float(x), 12) for x in AL @ np.array([0, 1, 0])]
w = np.array([0, 1, 1j])
out["best_v4_ties_on_constructed_yz_isotropic_line"] = ns["best_v4"](w, w)[1]   # ['1', 'i']: the half-turn about e_i fixes it
print(json.dumps(out, indent=1, default=str))
