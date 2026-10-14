"""Checks of the load-bearing steps behind chat1's note THE PASSAGE TO THE FIELD (2026-10-14).

These are checks of identities and of known mathematics, run BEFORE the note was written. They are not sealed
predictions; the sealed arc the note proposes is separate. Conventions are main's (B1642/B1645): QI = diag(i, -i),
QJ = [[0, 1], [-1, 0]], QK = QI QJ; the units' labels (i, j, k); R = (-th2^2, -th4^2, i th3^2)/(pi th2 th3 th4);
Y(a) = a R^T + R a^T - (a.R) 1 (B1645's closed form, which main verified against the residue to 1e-15).

  C1  Fricke: tr[A,B] = x^2 + y^2 + z^2 - xyz - 2 (x = tr A, y = tr B, z = tr AB); the common point A = QI, B = QJ
      has (x, y, z) = (0, 0, 0) and [A, B] = -1.
  C2  On the SU(2) box [-2, 2]^3, x^2 + y^2 + z^2 - xyz >= 0 with equality only at the origin (the common point is the
      only unitary point with kappa = -2): the discriminant identity, and a Haar sample.
  C3  The tangent cone: deforming the common point by cocycles u(a), u(b) in M_C, kappa + 2 = c eps^2 (h.h) + O(eps^3)
      with h = (u_i(a), u_j(b), u_k(a) - u_k(b)), the H^1 coordinates one per parity.
  C4  Nilpotent <=> isotropic: (a_i QI + a_j QJ + a_k QK)^2 = -(a.a) 1.
  C5  B1645 with a null Higgs: Y(a) has the null vectors R and a and the third eigenvector R x a with eigenvalue -(a.R),
      so rank one (one heavy, two massless); with a(xi) = (1 - xi^2, i(1 + xi^2), -2 xi), a(xi).a(eta) = -2 (xi - eta)^2.
  C6  tau parametrises the conic: for random null directions a there is tau with [R(tau)] = [a] (residual reported).
  C7  The local model behind Simpson's table: residue eigenvalue b + ic, weight alpha -> monodromy exp(-2 pi i alpha +
      4 pi c), flat-section growth |z|^(-2b); for SL(2) at weights (1/2, 1/2): kappa = -2 cosh(4 pi c).
  C8  Near the cone, B1645's m = m2/m3 against the isotropy defect |a.a|/|a|^2: the slope, at several tau and directions.

    python3 -B checks.py     # prints, and writes checks.json beside itself
"""
import json, math, pathlib
import numpy as np
import sympy as sp
import mpmath as mp
from scipy.optimize import minimize

HERE = pathlib.Path(__file__).resolve().parent
rng = np.random.default_rng(20261014)
out = {}

QI = np.array([[1j, 0], [0, -1j]]); QJ = np.array([[0, 1], [-1, 0]], dtype=complex); QK = QI @ QJ
I2 = np.eye(2)
def sig(a): return a[0] * QI + a[1] * QJ + a[2] * QK
def inv2(M): return np.array([[M[1, 1], -M[0, 1]], [-M[1, 0], M[0, 0]]]) / (M[0, 0] * M[1, 1] - M[0, 1] * M[1, 0])
def comm(A, B): return A @ B @ inv2(A) @ inv2(B)

# ---------------------------------------------------------------- C1
def rand_sl2():
    M = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2)); return M / np.sqrt(np.linalg.det(M))
c1 = 0.0
for _ in range(200):
    A, B = rand_sl2(), rand_sl2(); x, y, z = np.trace(A), np.trace(B), np.trace(A @ B)
    c1 = max(c1, abs(np.trace(comm(A, B)) - (x * x + y * y + z * z - x * y * z - 2)))
cp = (np.trace(QI), np.trace(QJ), np.trace(QI @ QJ)); cc = comm(QI, QJ)
out["C1"] = {"fricke_max_abs": float(c1), "common_point_traces": [complex(v).real for v in cp],
             "common_point_commutator_is_minus_one": bool(np.allclose(cc, -I2))}

# ---------------------------------------------------------------- C2
X, Yv, Z = sp.symbols("x y z", real=True)
disc = sp.expand((Yv * Z) ** 2 - 4 * (Yv ** 2 + Z ** 2))
identity = sp.simplify(disc - ((Yv ** 2 - 4) * (Z ** 2 - 4) - 16)) == 0
def haar_su2():
    q = rng.normal(size=4); q /= np.linalg.norm(q)
    return q[0] * I2 + q[1] * QI + q[2] * QJ + q[3] * QK
fmin, near = 1e9, 0
for _ in range(100000):
    A, B = haar_su2(), haar_su2(); x, y, z = (np.trace(A).real, np.trace(B).real, np.trace(A @ B).real)
    f = x * x + y * y + z * z - x * y * z
    fmin = min(fmin, f)
    if f < 1e-3: near += 1
out["C2"] = {"disc_identity_(y^2-4)(z^2-4)-16": bool(identity), "haar_min_f": float(fmin),
             "samples_with_f_below_1e-3": near,
             "argument": "for |y|,|z| <= 2 the discriminant of x^2 - yz x + (y^2+z^2) is (y^2-4)(z^2-4) - 16 <= 0, "
                         "with equality only at y = z = 0, where f = x^2; so f >= 0 on the box, = 0 only at the origin"}

# ---------------------------------------------------------------- C3 (exact, sympy)
eps = sp.symbols("eps")
ua = sp.symbols("ua_i ua_j ua_k"); ub = sp.symbols("ub_i ub_j ub_k")
sQI = sp.Matrix([[sp.I, 0], [0, -sp.I]]); sQJ = sp.Matrix([[0, 1], [-1, 0]]); sQK = sQI * sQJ
def U(v): return v[0] * sQI + v[1] * sQJ + v[2] * sQK
def exp2(M):  # exp of eps*M to order eps^3, M traceless: M^2 = -(v.v) 1
    return sp.eye(2) + eps * M + eps ** 2 * M * M / 2 + eps ** 3 * M * M * M / 6
A = sQI * exp2(U(ua)); B = sQJ * exp2(U(ub))
def adj(M): return sp.Matrix([[M[1, 1], -M[0, 1]], [-M[1, 0], M[0, 0]]])   # inverse for det 1 (up to O(eps^4))
detA = sp.expand((A[0, 0] * A[1, 1] - A[0, 1] * A[1, 0]).series(eps, 0, 3).removeO())
kap = sp.expand((A * B * adj(A) * adj(B)).trace())
kap2 = sp.expand(sp.series(kap, eps, 0, 3).removeO())
h = (ua[0], ub[1], ua[2] - ub[2])
Q = sp.expand(sum(v * v for v in h))
ratio = sp.simplify(sp.expand(kap2 + 2) / (eps ** 2 * Q))
out["C3"] = {"det_A_to_eps2": str(detA), "kappa_plus_2_to_eps2": str(sp.factor(sp.expand(kap2 + 2))),
             "equals_c_times_eps2_h.h_with_c": str(ratio),
             "h": "(u_i(a), u_j(b), u_k(a) - u_k(b))"}

# ---------------------------------------------------------------- C4
a_s = sp.symbols("a_i a_j a_k")
S = U(a_s)
out["C4"] = {"sigma_a_squared_plus_(a.a)": str(sp.simplify(S * S + (a_s[0] ** 2 + a_s[1] ** 2 + a_s[2] ** 2) * sp.eye(2)))}

# ---------------------------------------------------------------- the record's R and Y (B1645)
def R_np(t, K=60):
    n = np.arange(-K, K + 1); q = lambda x: np.exp(1j * np.pi * t * x)
    th2, th3, th4 = np.sum(q((n + 0.5) ** 2)), np.sum(q(n * n)), np.sum((-1.0) ** n * q(n * n))
    den = np.pi * th2 * th3 * th4
    return np.array([-th2 ** 2 / den, -th4 ** 2 / den, 1j * th3 ** 2 / den])
def Yf(a, R): return np.outer(a, R) + np.outer(R, a) - np.dot(a, R) * np.eye(3)
def anull(xi): return np.array([1 - xi * xi, 1j * (1 + xi * xi), -2 * xi])

# ---------------------------------------------------------------- C5
taus = [0.13 + 1.07j, 1j, -0.31 + 0.82j, 0.5 + 0.866j, 0.2 + 1.6j]
c5 = {"R.R_max": 0.0, "Ya_max": 0.0, "YR_max": 0.0, "Ycross_max": 0.0, "sv_ratio_2nd_over_1st_max": 0.0, "xi_identity_max": 0.0}
for t in taus:
    R = R_np(t); c5["R.R_max"] = max(c5["R.R_max"], abs(np.dot(R, R)) / np.linalg.norm(R) ** 2)
    for _ in range(40):
        xi = complex(rng.normal(), rng.normal()); a = anull(xi) * complex(rng.normal(), rng.normal())
        Y = Yf(a, R); w = np.cross(R, a); nY = np.linalg.norm(Y)
        c5["Ya_max"] = max(c5["Ya_max"], np.linalg.norm(Y @ a) / (nY * np.linalg.norm(a)))
        c5["YR_max"] = max(c5["YR_max"], np.linalg.norm(Y @ R) / (nY * np.linalg.norm(R)))
        c5["Ycross_max"] = max(c5["Ycross_max"], np.linalg.norm(Y @ w + np.dot(a, R) * w) / (nY * np.linalg.norm(w)))
        s = np.linalg.svd(Y, compute_uv=False); c5["sv_ratio_2nd_over_1st_max"] = max(c5["sv_ratio_2nd_over_1st_max"], s[1] / s[0])
        eta = complex(rng.normal(), rng.normal())
        c5["xi_identity_max"] = max(c5["xi_identity_max"], abs(np.dot(anull(xi), anull(eta)) + 2 * (xi - eta) ** 2) / (1 + abs(xi - eta) ** 2))
out["C5"] = {k: float(v) for k, v in c5.items()}

# ---------------------------------------------------------------- C6: tau parametrises the conic
def proj_res(t, a):
    R = R_np(t); return np.linalg.norm(np.cross(R, a)) / (np.linalg.norm(R) * np.linalg.norm(a))
grid = [complex(x, y) for x in np.linspace(-2, 2, 81) for y in np.linspace(0.12, 2.5, 48)]
Rg = {g: R_np(g) for g in grid}
c6 = []
for _ in range(20):
    xi = complex(rng.normal(), rng.normal()); a = anull(xi)
    g0 = min(grid, key=lambda g: np.linalg.norm(np.cross(Rg[g], a)) / (np.linalg.norm(Rg[g]) * np.linalg.norm(a)))
    best = None
    for start in (g0, g0 + 0.05, g0 - 0.05j * 0.5):
        f = lambda v: proj_res(complex(v[0], max(v[1], 0.05)), a) ** 2
        r = minimize(f, [start.real, start.imag], method="Nelder-Mead", options={"xatol": 1e-13, "fatol": 1e-28, "maxiter": 4000})
        t = complex(r.x[0], max(r.x[1], 0.05)); res = proj_res(t, a)
        if best is None or res < best[1]: best = (t, res)
    c6.append({"xi": [xi.real, xi.imag], "tau": [best[0].real, best[0].imag], "residual": float(best[1])})
out["C6"] = {"max_residual": max(c["residual"] for c in c6), "cases": c6}

# ---------------------------------------------------------------- C7: the local model (diagonal case)
def local(alpha, lam, N=4000):
    # flat connection on one line: omega = (alpha + lam) dz/z + conj(lam) dzbar/zbar; transport s' = -omega s
    th = np.linspace(0, 2 * np.pi, N + 1); dth = th[1] - th[0]
    # on |z| = 1: dz/z = i dth, dzbar/zbar = -i dth
    integrand = (alpha + lam) * 1j - np.conj(lam) * 1j
    mono = np.exp(-integrand * 2 * np.pi)
    # growth: |s|_h = |z|^alpha |exp(-(alpha+lam) log z - conj(lam) log zbar)| on the ray arg z = 0
    r = np.array([1e-1, 1e-2]); grow = np.log(np.abs(r ** alpha * np.exp(-(alpha + lam) * np.log(r) - np.conj(lam) * np.log(r))))
    slope = (grow[1] - grow[0]) / (np.log(r[1]) - np.log(r[0]))
    return mono, slope
c7 = []
for (al, b, c) in [(0.5, 0.0, 0.0), (0.5, 0.2, 0.0), (0.5, 0.0, 0.03), (0.3, -0.1, 0.07), (0.5, 0.11, -0.05)]:
    lam = complex(b, c); m, s = local(al, lam)
    c7.append({"alpha": al, "b": b, "c": c, "monodromy": [m.real, m.imag],
               "simpson_exp(-2pi i alpha + 4 pi c)": [complex(np.exp(-2j * np.pi * al + 4 * np.pi * c)).real, complex(np.exp(-2j * np.pi * al + 4 * np.pi * c)).imag],
               "growth_slope": float(s), "simpson_-2b": -2 * b})
# SL(2), weights (1/2, 1/2), eigenvalues +-(b + ic): kappa = trace = -exp(4 pi c) - exp(-4 pi c)
kap_tab = [{"a.a": aa, "c": math.sqrt(aa), "kappa": -2 * math.cosh(4 * math.pi * math.sqrt(aa)),
            "kappa+2": -2 * (math.cosh(4 * math.pi * math.sqrt(aa)) - 1), "-16pi^2 a.a": -16 * math.pi ** 2 * aa}
           for aa in (1e-6, 1e-4, 1e-3, 4e-3)]
out["C7"] = {"lines": c7, "sl2_unfiltered_kappa_vs_a.a": kap_tab}

# ---------------------------------------------------------------- C8: m against the isotropy defect near the cone
c8 = []
for t in taus:
    R = R_np(t)
    for _ in range(6):
        xi = complex(rng.normal(), rng.normal()); a0 = anull(xi); a0 = a0 / np.linalg.norm(a0)
        d = rng.normal(size=3) + 1j * rng.normal(size=3); d /= np.linalg.norm(d)
        pts = []
        for e in (1e-4, 3e-4, 1e-3, 3e-3):
            a = a0 + e * d; s = np.linalg.svd(Yf(a, R), compute_uv=False)
            pts.append((abs(np.dot(a, a)) / np.linalg.norm(a) ** 2, s[1] / s[0]))
        slopes = [p[1] / p[0] for p in pts]
        c8.append({"tau": [t.real, t.imag], "slope_m_over_defect": [float(v) for v in slopes]})
allsl = [v for c in c8 for v in c["slope_m_over_defect"]]
out["C8"] = {"slope_min": float(min(allsl)), "slope_max": float(max(allsl)),
             "slope_constant_along_each_ray": float(max(max(c["slope_m_over_defect"]) / min(c["slope_m_over_defect"]) for c in c8)),
             "rows": c8}

print(json.dumps({k: (v if k not in ("C6", "C8") else {kk: vv for kk, vv in v.items() if kk not in ("cases", "rows")}) for k, v in out.items()}, indent=1, default=str))
json.dump(out, open(HERE / "checks.json", "w"), indent=1, default=str)
