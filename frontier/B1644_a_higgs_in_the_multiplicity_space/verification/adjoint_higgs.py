#!/usr/bin/env python3
"""B1644 -- A HIGGS IN THE MULTIPLICITY SPACE (sealed before this runs; PREREGISTRATION.md).

The coupling of the zero modes F_p = C_p F (C_p = j, i, k) to a Higgs in the adjoint of the quaternion structure, read at
the fibre's puncture: Y(a)_pq = Res_{z=0} F^T C_p^T eps sigma_a C_q F, with sigma_a = i, j, k (the units as 2x2 matrices).
B1642's sealed definitions (the theta series, the zero mode, the residue) are reused unchanged: the text of its instrument
before its first cell is executed here.

  S1  Y(i), Y(j), Y(k) against the hand table (B1642's R's); symmetric; non-zero diagonal
  S2  linearity in the direction
  S3a the spectra over 400 real directions and 8 values of tau; the distance to 1 : 1/phi : 1/phi^2
  S3b along a = i near the cusp: the slope of ln(s_min/s_max) against Im tau over y = 2, 3, 4, 5
  S3c at tau = 4i: directions with three distinct masses and a hierarchy; the rank of (a, tau) -> spectrum

    python3 -B adjoint_higgs.py      # writes adjoint_higgs.json beside itself
"""
import json, math, os, pathlib
import mpmath as mp
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
FRONTIER = pathlib.Path(os.environ.get("OA_FRONTIER", HERE.parents[1]))
B1642 = FRONTIER / "B1642_the_golden_coupling_as_the_zero_modes_residue" / "verification" / "residue_coupling.py"
src = open(B1642).read().split("rng = np.random.default_rng(1642)")[0]
ns = {"__file__": str(B1642)}
exec(compile(src, "residue_coupling_defs", "exec"), ns)
th, residue, BLOCKS, EPS, QI, QJ, QK = ns["th"], ns["residue"], ns["BLOCKS"], ns["EPS"], ns["QI"], ns["QJ"], ns["QK"]
mp.mp.dps = 30
UNITS = {"i": QI, "j": QJ, "k": QK}
out = {}


def Y_unit(S, t):
    Y = np.zeros((3, 3), dtype=complex)
    for a, (_, Ca) in enumerate(BLOCKS):
        for b, (_, Cb) in enumerate(BLOCKS):
            Y[a, b] = complex(residue(Ca.T * EPS * S * Cb, t))
    return Y


def R_closed(t):
    den = mp.pi * th(2, 0, t) * th(3, 0, t) * th(4, 0, t)
    return (complex(-th(2, 0, t) ** 2 / den), complex(-th(4, 0, t) ** 2 / den), complex(1j * th(3, 0, t) ** 2 / den))


def table(t):
    Ri, Rj, Rk = R_closed(t)
    return {"i": np.array([[-Ri, Rj, 0], [Rj, Ri, Rk], [0, Rk, -Ri]]),
            "j": np.array([[Rj, Ri, Rk], [Ri, -Rj, 0], [Rk, 0, -Rj]]),
            "k": np.array([[-Rk, 0, Rj], [0, -Rk, Ri], [Rj, Ri, Rk]])}


def sv(A):
    s = np.linalg.svd(A, compute_uv=False); return s / s[0]


rng = np.random.default_rng(1644)
rt = lambda: mp.mpc(rng.uniform(-0.5, 0.5), rng.uniform(0.7, 1.8))

# S1, S2
S1 = {"max_rel_vs_table": 0.0, "max_asym_rel": 0.0, "min_abs_diag_rel": 1.0}
S2 = {"max_rel_linearity": 0.0}
for _ in range(10):
    t = rt(); tab = table(t); Ys = {u: Y_unit(M, t) for u, M in UNITS.items()}
    for u in UNITS:
        Y = Ys[u]; nrm = np.abs(Y).max()
        S1["max_rel_vs_table"] = max(S1["max_rel_vs_table"], float(np.abs(Y - tab[u]).max() / nrm))
        S1["max_asym_rel"] = max(S1["max_asym_rel"], float(np.abs(Y - Y.T).max() / nrm))
        S1["min_abs_diag_rel"] = min(S1["min_abs_diag_rel"], float(np.abs(np.diag(Y)).min() / nrm))
    a = rng.normal(size=3); a /= np.linalg.norm(a)
    Sa = a[0] * QI + a[1] * QJ + a[2] * QK
    Ya = Y_unit(Sa, t); Yl = a[0] * Ys["i"] + a[1] * Ys["j"] + a[2] * Ys["k"]
    S2["max_rel_linearity"] = max(S2["max_rel_linearity"], float(np.abs(Ya - Yl).max() / np.abs(Ya).max()))
out["S1"], out["S2"] = S1, S2

# S3a
phi = (1 + 5 ** 0.5) / 2; gold = np.array([1, 1 / phi, 1 / phi ** 2])
golden_ratio = 1 / phi
N = 400
dirs = []
for n in range(N):
    zc = 1 - 2 * (n + 0.5) / N; r = math.sqrt(1 - zc * zc); ph = n * math.pi * (3 - math.sqrt(5))
    dirs.append(np.array([r * math.cos(ph), r * math.sin(ph), zc]))
taus = {"i": mp.mpc(0, 1), "omega": mp.mpc(-0.5, math.sqrt(3) / 2)}
for k, thv in enumerate((0.6, 1.2, 1.9)):
    taus[f"tick_axis_{thv}"] = mp.mpf(1) / 2 + mp.sqrt(5) / 2 * mp.exp(1j * thv)
for y in (1.5, 2.5, 4.0):
    taus[f"iy_{y}"] = mp.mpc(0, y)
S3a = {}
best = (9.0, None)
for name, t in taus.items():
    Ys = [Y_unit(UNITS[u], t) for u in "ijk"]
    dmin = 9.0; amin = None; spectra = []
    for a in dirs:
        s = sv(a[0] * Ys[0] + a[1] * Ys[1] + a[2] * Ys[2]); spectra.append(s)
        d = float(np.max(np.abs(s - gold)))
        if d < dmin: dmin, amin = d, a
    S3a[name] = {"min_dist_to_golden": round(dmin, 6), "at_direction": [round(float(x), 4) for x in amin],
                 "smallest_ratio_range": [round(float(min(s[2] for s in spectra)), 8), round(float(max(s[2] for s in spectra)), 6)]}
    if dmin < best[0]: best = (dmin, name)
S3a["overall_min_dist_to_golden"] = {"dist": round(best[0], 6), "tau": best[1]}
out["S3a"] = S3a

# S3b
ys = [2.0, 3.0, 4.0, 5.0]; vals = []
for y in ys:
    s = sv(Y_unit(QI, mp.mpc(0, y))); vals.append(math.log(float(s[2])))
slope = float(np.polyfit(ys, vals, 1)[0])
out["S3b"] = {"ys": ys, "ln_smin_over_smax": vals, "slope": slope, "slope_over_minus_pi": slope / (-math.pi)}

# S3c
t = mp.mpc(0, 4.0); Ys = [Y_unit(UNITS[u], t) for u in "ijk"]
hier = []
for a in dirs:
    s = sv(a[0] * Ys[0] + a[1] * Ys[1] + a[2] * Ys[2])
    distinct = (s[0] - s[1]) > 0.05 and (s[1] - s[2]) > 0.05 * s[1]
    if distinct and s[2] < 1e-2: hier.append([round(float(x), 4) for x in a] + [round(float(v), 8) for v in s])
def spec_of(p):
    a = np.array([math.sin(p[0]) * math.cos(p[1]), math.sin(p[0]) * math.sin(p[1]), math.cos(p[0])])
    tt = mp.mpc(p[2], p[3]); Yt = [Y_unit(UNITS[u], tt) for u in "ijk"]
    return sv(a[0] * Yt[0] + a[1] * Yt[1] + a[2] * Yt[2])[1:]
p0 = np.array([1.1, 0.7, 0.1, 1.3]); h = 1e-5; f0 = spec_of(p0)
J = np.array([(spec_of(p0 + h * e) - f0) / h for e in np.eye(4)]).T
out["S3c"] = {"tau": "4i", "hierarchical_distinct_count": len(hier), "examples": hier[:5],
              "rank_of_spectrum_map": int(np.linalg.matrix_rank(J, tol=1e-6)), "jacobian_sv": [float(x) for x in np.linalg.svd(J, compute_uv=False)]}

json.dump(out, open(HERE / "adjoint_higgs.json", "w"), indent=1, default=str)
print(json.dumps(out, indent=1, default=str))
