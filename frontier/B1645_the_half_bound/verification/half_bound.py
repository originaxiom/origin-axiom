#!/usr/bin/env python3
"""B1645 -- THE HALF BOUND (sealed before this runs; PREREGISTRATION.md).

Y(a) = a R^T + R a^T - (a.R) 1 in the units' labels (i, j, k), with R = (R_i, R_j, R_k) = (-th2^2, -th4^2, i th3^2)/(pi th2 th3 th4)
(B1644's table).  B1642's sealed definitions (theta series, zero mode, residue) are reused unchanged.

  T1  the residue coupling at 6 tau x 6 complex a against a R^T + R a^T - (a.R) 1
  T2  Y(a) R = 0
  T3  real a: s1 s2 = |R|^2 |a|^2, s1^2 + s2^2 = 2 |R|^2 |a|^2 + |a.R|^2
  T4  real a: m from t^2 - (4 + u) t + 4 = 0; m >= 1/2; the two extremes
  T5  complex a: Y(conj R) rank one; inf m = 0 at a ~ conj R; m linear in the distance near it

    python3 -B half_bound.py      # writes half_bound.json beside itself
"""
import json, math, os, pathlib
import mpmath as mp
import numpy as np
from scipy.optimize import minimize

HERE = pathlib.Path(__file__).resolve().parent
FRONTIER = pathlib.Path(os.environ.get("OA_FRONTIER", HERE.parents[1]))
B1642 = FRONTIER / "B1642_the_golden_coupling_as_the_zero_modes_residue" / "verification" / "residue_coupling.py"
ns = {"__file__": str(B1642)}
exec(compile(open(B1642).read().split("rng = np.random.default_rng(1642)")[0], "residue_coupling_defs", "exec"), ns)
th, residue, BLOCKS, EPS, QI, QJ, QK = ns["th"], ns["residue"], ns["BLOCKS"], ns["EPS"], ns["QI"], ns["QJ"], ns["QK"]
mp.mp.dps = 30
BLOCK_OF_UNIT = [1, 0, 2]                      # BLOCKS are (j, i, k); the units' labels are (i, j, k)
out = {}


def R_mp(t):
    den = mp.pi * th(2, 0, t) * th(3, 0, t) * th(4, 0, t)
    return np.array([complex(-th(2, 0, t) ** 2 / den), complex(-th(4, 0, t) ** 2 / den), complex(1j * th(3, 0, t) ** 2 / den)])


def Y_residue(a, t):
    S = mp.mpc(complex(a[0])) * QI + mp.mpc(complex(a[1])) * QJ + mp.mpc(complex(a[2])) * QK
    Yb = np.zeros((3, 3), dtype=complex)
    for p, (_, Cp) in enumerate(BLOCKS):
        for q, (_, Cq) in enumerate(BLOCKS):
            Yb[p, q] = complex(residue(Cp.T * EPS * S * Cq, t))
    return Yb[np.ix_(BLOCK_OF_UNIT, BLOCK_OF_UNIT)]


def Y_formula(a, R):
    return np.outer(a, R) + np.outer(R, a) - np.dot(a, R) * np.eye(3)


rng = np.random.default_rng(1645)
taus = [mp.mpc(rng.uniform(-0.5, 0.5), rng.uniform(0.7, 1.8)) for _ in range(6)]

# T1, T2
T1, T2 = 0.0, 0.0
for t in taus:
    R = R_mp(t)
    for _ in range(6):
        a = rng.normal(size=3) + 1j * rng.normal(size=3)
        Y = Y_residue(a, t); F = Y_formula(a, R)
        T1 = max(T1, float(np.abs(Y - F).max() / np.abs(F).max()))
        T2 = max(T2, float(np.linalg.norm(Y @ R) / (np.linalg.norm(Y) * np.linalg.norm(R))))
out["T1_max_rel"], out["T2_max_rel"] = T1, T2


# the closed form R from numpy series (B1644's S1 held exactly; T1 checks it again)
def R_np(t, K=40):
    n = np.arange(-K, K + 1); q = lambda x: np.exp(1j * np.pi * t * x)
    th2, th3, th4 = np.sum(q((n + 0.5) ** 2)), np.sum(q(n * n)), np.sum((-1.0) ** n * q(n * n))
    den = np.pi * th2 * th3 * th4
    return np.array([-th2 ** 2 / den, -th4 ** 2 / den, 1j * th3 ** 2 / den])


tnp = [complex(t.real, t.imag) for t in taus]
T3 = {"prod_max_rel": 0.0, "sumsq_max_rel": 0.0}; T4 = {"formula_max_abs": 0.0, "m_min": 1.0, "m_in_plane": [], "m_normal": []}
for t in tnp:
    R = R_np(t); x, y = R.real, R.imag
    r = np.linalg.norm(x); e1 = x / r; e2 = y / np.linalg.norm(y); e3 = np.cross(e1, e2)
    for _ in range(200):
        a = rng.normal(size=3)
        s = np.linalg.svd(Y_formula(a, R), compute_uv=False)
        R2, a2, aR = np.linalg.norm(R) ** 2, np.dot(a, a), abs(np.dot(a, R)) ** 2
        T3["prod_max_rel"] = max(T3["prod_max_rel"], abs(s[0] * s[1] - R2 * a2) / (R2 * a2))
        T3["sumsq_max_rel"] = max(T3["sumsq_max_rel"], abs(s[0] ** 2 + s[1] ** 2 - (2 * R2 * a2 + aR)) / (2 * R2 * a2 + aR))
        u = aR / (r * r * a2)
        tp = ((4 + u) + math.sqrt((4 + u) ** 2 - 16)) / 2; tm = ((4 + u) - math.sqrt((4 + u) ** 2 - 16)) / 2
        T4["formula_max_abs"] = max(T4["formula_max_abs"], abs(s[1] / s[0] - math.sqrt(tm / tp)))
        T4["m_min"] = min(T4["m_min"], float(s[1] / s[0]))
    for a, key in ((math.cos(0.7) * e1 + math.sin(0.7) * e2, "m_in_plane"), (e3, "m_normal")):
        s = np.linalg.svd(Y_formula(a, R), compute_uv=False); T4[key].append(float(s[1] / s[0]))
out["T3"], out["T4"] = T3, T4

# T5
T5 = {"rank_one_sv": [], "inf_m": None, "inf_m_overlap_with_conjR": None, "slopes": []}
for t in tnp:
    R = R_np(t); s = np.linalg.svd(Y_formula(np.conj(R), R), compute_uv=False)
    T5["rank_one_sv"].append([float(s[1] / s[0]), float(s[2] / s[0])])
R = R_np(tnp[0])
def m_of(p):
    a = p[:3] + 1j * p[3:]; s = np.linalg.svd(Y_formula(a, R), compute_uv=False); return s[1] / s[0]
best = (9, None)
for _ in range(50):
    res = minimize(m_of, rng.normal(size=6), method="Nelder-Mead", options={"xatol": 1e-12, "fatol": 1e-14, "maxiter": 20000})
    if res.fun < best[0]: best = (res.fun, res.x)
a = best[1][:3] + 1j * best[1][3:]
T5["inf_m"] = float(best[0])
T5["inf_m_overlap_with_conjR"] = float(abs(np.vdot(a, np.conj(R))) / (np.linalg.norm(a) * np.linalg.norm(R)))
for _ in range(3):
    w = rng.normal(size=3) + 1j * rng.normal(size=3); w /= np.linalg.norm(w)
    eps = [1e-2, 1e-3, 1e-4]; ms = []
    for e in eps:
        s = np.linalg.svd(Y_formula(np.conj(R) / np.linalg.norm(R) + e * w, R), compute_uv=False); ms.append(s[1] / s[0])
    T5["slopes"].append(float(np.polyfit(np.log(eps), np.log(ms), 1)[0]))
out["T5"] = T5

json.dump(out, open(HERE / "half_bound.json", "w"), indent=1, default=str)
print(json.dumps(out, indent=1, default=str))
