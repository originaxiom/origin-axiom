#!/usr/bin/env python3
"""B1646 -- THE DIRECTION IS THE MASS MATRIX (sealed before this runs; PREREGISTRATION.md).

B1645: Y(a) = a R^T + R a^T - (a.R) 1, R = (-th2^2, -th4^2, i th3^2)/(pi th2 th3 th4), R.R = 0 (Jacobi).
In the unitary basis U = (R/|R|, conj(R)/|R|, n), n = Re R x Im R / |.|, the derivation by hand gives
    U^dag Y(a) U = [[0, 2 a.conj(R), |R| a.n], [0, 0, 0], [0, |R| a.n, -a.R]].

  D1  the block form, at 9 tau x 20 complex a
  D2  a -> M2(a) is a linear bijection C^3 -> Sym_2(C); the masses of Y(L^-1 K) are those of K
  D3  complex a: s1 s2 = |R|^2 |a.a|, s1^2 + s2^2 = 2|R|^2|a|^2 + 2|a.conj(R)|^2 - |a.R|^2
  D4  V = -|a|^2 + l1 |a|^4 + l2 |a.a|^2: minima on the cone (l2 > 0) or the real locus (l2 < 0), never in between
  D5  f(S, P) = sum s^4 ln s^2 at s1^2 + s2^2 = S, s1 s2 = P: [f(S,P) - f(S,0)]/P^2 -> -(2 ln S + 1)
  D6  the units as Higgs directions on tau = iy: m(e_k) = 1/2 exactly; m(e_i), m(e_j) -> 1, 1/2 at the cusp

Tolerances are 1e-12 relative (double precision; B1645's E82 instance).
    python3 -B direction_mass_matrix.py      # writes direction_mass_matrix.json beside itself
"""
import json, math, pathlib
import numpy as np
from scipy.optimize import minimize

HERE = pathlib.Path(__file__).resolve().parent
out = {}


def R_np(t, K=40):
    n = np.arange(-K, K + 1); q = lambda x: np.exp(1j * np.pi * t * x)
    th2, th3, th4 = np.sum(q((n + 0.5) ** 2)), np.sum(q(n * n)), np.sum((-1.0) ** n * q(n * n))
    den = np.pi * th2 * th3 * th4
    return np.array([-th2 ** 2 / den, -th4 ** 2 / den, 1j * th3 ** 2 / den])


def Y_of(a, R):
    return np.outer(a, R) + np.outer(R, a) - np.dot(a, R) * np.eye(3)


def frame(R):
    nR = np.linalg.norm(R); n = np.cross(R.real, R.imag); n = n / np.linalg.norm(n)
    return np.column_stack([R / nR, np.conj(R) / nR, n]), n, nR


def M2(a, R):
    _, n, nR = frame(R)
    return np.array([[2 * np.dot(a, np.conj(R)), nR * np.dot(a, n)], [nR * np.dot(a, n), -np.dot(a, R)]])


def m_of(Y):
    s = np.linalg.svd(Y, compute_uv=False); return float(s[1] / s[0])


def m_of_u(u):
    tp = ((4 + u) + math.sqrt((4 + u) ** 2 - 16)) / 2; tm = ((4 + u) - math.sqrt((4 + u) ** 2 - 16)) / 2
    return math.sqrt(tm / tp)


rng = np.random.default_rng(1646)
taus = [complex(rng.uniform(-0.5, 0.5), rng.uniform(0.8, 2.0)) for _ in range(6)] + [1j, complex(-0.5, math.sqrt(3) / 2), 4j]

# D1
D1 = {"unitarity_max": 0.0, "block_max_rel": 0.0}
for t in taus:
    R = R_np(t); U, n, nR = frame(R)
    D1["unitarity_max"] = max(D1["unitarity_max"], float(np.abs(U.conj().T @ U - np.eye(3)).max()))
    for _ in range(20):
        a = rng.normal(size=3) + 1j * rng.normal(size=3)
        B = U.conj().T @ Y_of(a, R) @ U
        P = np.array([[0, 2 * np.dot(a, np.conj(R)), nR * np.dot(a, n)], [0, 0, 0], [0, nR * np.dot(a, n), -np.dot(a, R)]])
        D1["block_max_rel"] = max(D1["block_max_rel"], float(np.abs(B - P).max() / np.abs(P).max()))
out["D1"] = D1

# D2
D2 = {"min_sv_ratio_of_L": 1.0, "masses_max_rel": 0.0}
for t in taus:
    R = R_np(t)
    L = np.column_stack([np.array([M2(e, R)[0, 0], M2(e, R)[0, 1], M2(e, R)[1, 1]]) for e in np.eye(3)])
    sv = np.linalg.svd(L, compute_uv=False); D2["min_sv_ratio_of_L"] = min(D2["min_sv_ratio_of_L"], float(sv[-1] / sv[0]))
    for _ in range(20):
        k = rng.normal(size=3) + 1j * rng.normal(size=3); K = np.array([[k[0], k[1]], [k[1], k[2]]])
        a = np.linalg.solve(L, k)
        sY = np.linalg.svd(Y_of(a, R), compute_uv=False); sK = np.linalg.svd(K, compute_uv=False)
        D2["masses_max_rel"] = max(D2["masses_max_rel"], float(np.abs(sY[:2] - sK).max() / sK[0]), float(sY[2] / sK[0]))
out["D2"] = D2

# D3
D3 = {"prod_max_rel": 0.0, "sumsq_max_rel": 0.0}
for t in taus:
    R = R_np(t); R2 = np.linalg.norm(R) ** 2
    for _ in range(200):
        a = rng.normal(size=3) + 1j * rng.normal(size=3)
        s = np.linalg.svd(Y_of(a, R), compute_uv=False)
        p = R2 * abs(np.dot(a, a)); q = 2 * R2 * np.linalg.norm(a) ** 2 + 2 * abs(np.dot(a, np.conj(R))) ** 2 - abs(np.dot(a, R)) ** 2
        D3["prod_max_rel"] = max(D3["prod_max_rel"], float(abs(s[0] * s[1] - p) / p))
        D3["sumsq_max_rel"] = max(D3["sumsq_max_rel"], float(abs(s[0] ** 2 + s[1] ** 2 - q) / q))
out["D3"] = D3

# D4
D4 = {"by_l2": {}}
R_i, R_r = R_np(1j), R_np(taus[0])
for l2 in (-0.5, -0.1, 0.1, 0.5, 1.0):
    def V(p, l2=l2):
        a = p[:3] + 1j * p[3:]; A = np.vdot(a, a).real
        return -A + A * A + l2 * abs(np.dot(a, a)) ** 2
    rows = []
    for _ in range(30):
        res = minimize(V, rng.normal(size=6), method="BFGS", options={"gtol": 1e-12, "maxiter": 10000})
        a = res.x[:3] + 1j * res.x[3:]; A = np.vdot(a, a).real
        rows.append([float(abs(np.dot(a, a)) / A), m_of(Y_of(a, R_i)), m_of(Y_of(a, R_r)), float(res.fun)])
    rows = np.array(rows)
    D4["by_l2"][str(l2)] = {"defect_range": [float(rows[:, 0].min()), float(rows[:, 0].max())],
                            "m_range_tau_i": [float(rows[:, 1].min()), float(rows[:, 1].max())],
                            "m_range_tau_0": [float(rows[:, 2].min()), float(rows[:, 2].max())],
                            "V_range": [float(rows[:, 3].min()), float(rows[:, 3].max())],
                            "in_between": int(np.sum((rows[:, 1:3] > 1e-3) & (rows[:, 1:3] < 0.45)))}
out["D4"] = D4


# D5
def f(S, P):
    d = math.sqrt(S * S - 4 * P * P); x1, x2 = (S + d) / 2, (S - d) / 2
    return x1 * x1 * math.log(x1) + (x2 * x2 * math.log(x2) if x2 > 0 else 0.0)


D5 = []
for S in (0.3, 1.0, 3.0):
    for r in (1e-3, 1e-4):
        P = r * S; c = (f(S, P) - f(S, 0.0)) / (P * P); D5.append([S, r, c, -(2 * math.log(S) + 1), abs(c + 2 * math.log(S) + 1) / abs(2 * math.log(S) + 1)])
out["D5"] = {"rows_S_ratio_coeff_predicted_relerr": D5, "max_relerr": max(r[-1] for r in D5)}

# D6
D6 = {"tau_i": None, "iy": []}
for y in (1.0, 2.0, 4.0, 8.0):
    R = R_np(1j * y); ms = [m_of(Y_of(e, R)) for e in np.eye(3)]
    D6["iy"].append([y] + ms)
D6["tau_i"] = D6["iy"][0][1:]; D6["m_of_u_half"] = m_of_u(0.5)
out["D6"] = D6

json.dump(out, open(HERE / "direction_mass_matrix.json", "w"), indent=1, default=str)
print(json.dumps(out, indent=1, default=str))
