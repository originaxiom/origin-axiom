#!/usr/bin/env python3
"""Audit B, part 3.
(a) Reading B, both condensates on one leg (rank 3): can it reproduce the whole first row (|U_e1|^2, |U_e3|^2) and the
    ratio dm21^2/dm31^2 at leading order, with the electron along R (charged leptons without condensates) or along e_t?
    This is not a prediction (free parameters); it tests whether 'the escape is closed' holds without the hook.
(b) How big a neutrino-side correction moves |U_e1|^2 from 1 to 0.675, starting from the hook (m1 = 0) with nature's
    m2/m3 = sqrt(dm21/dm31): the size relative to m3 and to m2."""
import math, numpy as np
from scipy.optimize import least_squares
rng = np.random.default_rng(99)

def thetas(t, K=60):
    n = np.arange(-K, K + 1); q = lambda x: np.exp(1j * np.pi * t * x)
    return np.sum(q((n + .5) ** 2)), np.sum(q(n * n)), np.sum((-1.0) ** n * q(n * n))
def R_of(t):
    th2, th3, th4 = thetas(t); return np.array([-th2 ** 2, -th4 ** 2, 1j * th3 ** 2]) / (np.pi * th2 * th3 * th4)
def Yc(a, R): return np.outer(a, R) + np.outer(R, a) - (a @ R) * np.eye(3)
def svd_sorted(M):
    W, s, Vh = np.linalg.svd(M); o = np.argsort(s); return Vh.conj().T[:, o], s[o]
targ = {"Ue1": (1 - 0.3092) * (1 - 0.02248), "Ue3": 0.02248, "r": 7.49e-5 / 2.513e-3}

def model(p, R, ti):
    a = p[0:3] + 1j * p[3:6]; dr, ds = complex(p[6], p[7]), 1.0
    r, s = [x for x in range(3) if x != ti]
    D = np.zeros((3, 3), complex); D[r, r] = dr; D[s, s] = ds
    M = Yc(a, R) @ D; M = (M + M.T) / 2
    V, m = svd_sorted(M)
    return V, m

for electron in ("R", "e_t"):
    for tname, t in (("i", 1j), ("1.5i", 1.5j), ("omega", complex(-.5, math.sqrt(3) / 2))):
        R = R_of(t); best = None
        for ti in range(3):
            e = R / np.linalg.norm(R) if electron == "R" else np.eye(3)[ti].astype(complex)
            def res(p):
                V, m = model(p, R, ti)
                row = np.abs(e.conj() @ V) ** 2
                r_ = (m[1] ** 2 - m[0] ** 2) / (m[2] ** 2 - m[0] ** 2)
                return [row[0] - targ["Ue1"], row[2] - targ["Ue3"], (r_ - targ["r"]) / 0.1]
            for _ in range(40):
                sol = least_squares(res, rng.normal(size=8), xtol=1e-14, ftol=1e-14, gtol=1e-14)
                if best is None or sol.cost < best[0]:
                    V, m = model(sol.x, R, ti); row = np.abs(e.conj() @ V) ** 2
                    best = (sol.cost, ti, row, m / m[2])
        print("(a) electron %-3s tau=%-5s best: cost %.1e, t=%d, first row (%.4f, %.4f, %.4f), m1:m2:m3 = %.4f : %.4f : 1"
              % (electron, tname, best[0], best[1], *best[2], *best[3][:2]))

print()
# (b) from the hook, with m2/m3 = sqrt(r) (m1 = 0): smallest correction delta*X (X random complex symmetric, ||X||_F = 1)
r = targ["r"]; m2 = math.sqrt(r)
need = []
for _ in range(2000):
    Q, _ = np.linalg.qr(rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3)))
    M0 = Q.conj() @ np.diag([0, m2, 1.0]) @ Q.conj().T          # Takagi form with null vector Q[:,0] (plays R)
    X = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3)); X = X + X.T; X /= np.linalg.norm(X)
    e = Q[:, 0]
    lo, hi = 0.0, 3.0
    def ue1(d):
        V, m = svd_sorted(M0 + d * X); return abs(np.vdot(e, V[:, 0])) ** 2
    if ue1(hi) > targ["Ue1"]: continue
    for _ in range(60):
        mid = (lo + hi) / 2
        if ue1(mid) > targ["Ue1"]: lo = mid
        else: hi = mid
    V, m = svd_sorted(M0 + hi * X)
    need.append((hi, m[0] / m[2], m[1] / m[2]))
need = np.array(need)
print("(b) from the hook (m1 = 0, m2/m3 = %.3f): random correction delta*X reaching |U_e1|^2 = 0.675" % m2)
print("    delta/m3: 10th pct %.3f, median %.3f; delta/m2: median %.2f; resulting m1/m3 median %.3f, m2/m3 median %.3f (n=%d)"
      % (np.percentile(need[:, 0], 10), np.median(need[:, 0]), np.median(need[:, 0]) / m2, np.median(need[:, 1]), np.median(need[:, 2]), len(need)))
# the same with the correction confined to the light 2x2 block (best case)
d12 = []
for th in np.linspace(0.01, 1.5, 300):
    pass
# analytic: block [[0, x],[x, m2]] -> tan(2 theta) = 2x/m2; theta = acos(sqrt(0.6753))
theta = math.acos(math.sqrt(targ["Ue1"])); x = math.tan(2 * theta) * m2 / 2
lam = np.linalg.eigvalsh(np.array([[0, x], [x, m2]]))
print("    best case, correction only in the nu1-nu2 entry: x = %.3f m2 = %.3f m3; light masses become %.3f, %.3f (x m3)"
      % (x / m2, x, *sorted(abs(lam))))
