#!/usr/bin/env python3
"""B1645, post-seal (labelled): T5's minimiser was not along conj(R) (overlap 0.084), so m = 0 holds on more than one
direction.  By hand: on span{a, R} the matrix 1 - (a R^T + R a^T)/(a.R) acts as [[0, -(a.a)/(a.R)], [0, 0]], so Y(a) has
rank one exactly when a.a = 0.  Checked: m = 0 for random isotropic a; m against |a.a| near the cone; the minimiser's a.a."""
import json, pathlib
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent


def R_np(t, K=40):
    n = np.arange(-K, K + 1); q = lambda x: np.exp(1j * np.pi * t * x)
    th2, th3, th4 = np.sum(q((n + 0.5) ** 2)), np.sum(q(n * n)), np.sum((-1.0) ** n * q(n * n))
    den = np.pi * th2 * th3 * th4
    return np.array([-th2 ** 2 / den, -th4 ** 2 / den, 1j * th3 ** 2 / den])


Yf = lambda a, R: np.outer(a, R) + np.outer(R, a) - np.dot(a, R) * np.eye(3)
rng = np.random.default_rng(16451)
out = {"isotropic_m_max": 0.0, "slopes_vs_abs_aa": []}
for t in (complex(0.1, 1.1), complex(-0.3, 1.6), complex(0.0, 3.0)):
    R = R_np(t)
    for _ in range(100):
        u = rng.normal(size=3); v = rng.normal(size=3); v -= u * np.dot(u, v) / np.dot(u, u); v *= np.linalg.norm(u) / np.linalg.norm(v)
        a = (u + 1j * v) * np.exp(1j * rng.uniform(0, 6.28))           # a.a = 0 exactly
        s = np.linalg.svd(Yf(a, R), compute_uv=False); out["isotropic_m_max"] = max(out["isotropic_m_max"], float(s[1] / s[0]))
    a0 = (u + 1j * v); w = rng.normal(size=3) + 1j * rng.normal(size=3)
    eps = [1e-2, 1e-3, 1e-4]; ms, aas = [], []
    for e in eps:
        a = a0 + e * w; s = np.linalg.svd(Yf(a, R), compute_uv=False); ms.append(s[1] / s[0]); aas.append(abs(np.dot(a, a)) / np.dot(a, a.conj()).real)
    out["slopes_vs_abs_aa"].append(float(np.polyfit(np.log(aas), np.log(ms), 1)[0]))
json.dump(out, open(HERE / "post_seal_cone.json", "w"), indent=1)
print(json.dumps(out, indent=1))
