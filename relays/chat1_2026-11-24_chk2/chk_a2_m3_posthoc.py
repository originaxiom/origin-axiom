#!/usr/bin/env python3
"""Post hoc, labelled: written after chk_a2_m3.py's output, whose adversarial search ended at the trivial corner
rho = F = 0 (t = 0, S = 0). This run asks how sharp M3 is away from that corner: it minimises rho / F over points with
F >= 1e-3, from 200 random starts. A ratio below 1 would be a violation; a ratio near 1 means the bound is close to
sharp. Expected before the run: the least ratio lies between 1 and 3 (60 %). Data-free.
"""
import numpy as np
from scipy.optimize import minimize

src = open(__file__.replace("_posthoc", "")).read().split("N = 240000")[0]
ns = {}
exec(src, ns)  # the committed definitions of chk_a2_m3.py: Ymat, Ffloor, evaluate, sample
rng = np.random.default_rng(20261126)


def unpack(p):
    return p[0:3] + 1j * p[3:6], (p[6:10] + 1j * p[10:14]).reshape(2, 2), (p[14:18] + 1j * p[18:22]).reshape(2, 2)


def obj(p):
    h, Mu, Md = unpack(p)
    if min(np.linalg.norm(h), np.linalg.norm(Mu), np.linalg.norm(Md)) < 1e-8:
        return 10.0
    rho, F, *_ = ns["evaluate"](h, Mu, Md)
    return rho / F if F >= 1e-3 else 10.0 + (1e-3 - F)


best, rec, viol = np.inf, None, 0
for s in range(200):
    p0 = rng.normal(size=22)
    res = minimize(obj, p0, method="Nelder-Mead", options={"maxiter": 5000, "xatol": 1e-10, "fatol": 1e-12})
    if res.fun < 1 - 1e-9:
        viol += 1
    if res.fun < best:
        best, rec = res.fun, ns["evaluate"](*unpack(res.x))
print("ratio search: 200 starts, ending below 1: %d; least rho / F = %.6f at (rho, F, t, s_L, a) = %s"
      % (viol, best, tuple(round(float(v), 6) for v in rec)))
