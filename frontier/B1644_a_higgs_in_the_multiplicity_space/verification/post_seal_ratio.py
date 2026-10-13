#!/usr/bin/env python3
"""B1644, post-seal (labelled): the middle ratio m = s2/s1 of Y(a) = sum a_r Y(r) with the weave's own R's (the closed
forms S1 confirmed exactly), over real and complex directions and tau across the fundamental domain and toward the cusp."""
import json, math, pathlib
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent


def thetas(t, K=40):
    n = np.arange(-K, K + 1)
    q = lambda x: np.exp(1j * np.pi * t * x)
    th2 = np.sum(q((n + 0.5) ** 2)); th3 = np.sum(q(n * n)); th4 = np.sum((-1.0) ** n * q(n * n))
    return th2, th3, th4


def Ys(t):
    th2, th3, th4 = thetas(t); den = np.pi * th2 * th3 * th4
    Ri, Rj, Rk = -th2 ** 2 / den, -th4 ** 2 / den, 1j * th3 ** 2 / den
    return [np.array([[-Ri, Rj, 0], [Rj, Ri, Rk], [0, Rk, -Ri]]), np.array([[Rj, Ri, Rk], [Ri, -Rj, 0], [Rk, 0, -Rj]]),
            np.array([[-Rk, 0, Rj], [0, -Rk, Ri], [Rj, Ri, Rk]])], (Ri, Rj, Rk)


rng = np.random.default_rng(16441)
out = {}
for label, ts in (("fundamental domain", [complex(x, y) for x in np.linspace(-0.5, 0.5, 7) for y in np.linspace(0.9, 2.0, 7) if x * x + y * y >= 1]),
                  ("toward the cusp", [complex(0.0, y) for y in (2.5, 3.0, 4.0, 5.0, 6.0)])):
    res = {"real": [], "complex": []}; isotropy = []
    for t in ts:
        Y, R = Ys(t); isotropy.append(abs(sum(r * r for r in R)) / sum(abs(r) ** 2 for r in R))
        for kind in ("real", "complex"):
            for _ in range(600):
                a = rng.normal(size=3) + (1j * rng.normal(size=3) if kind == "complex" else 0)
                s = np.linalg.svd(a[0] * Y[0] + a[1] * Y[1] + a[2] * Y[2], compute_uv=False); s = s / s[0]
                res[kind].append((float(s[1]), float(s[2])))
    out[label] = {"isotropy_max_rel": float(max(isotropy)),
                  **{k: {"m_min": min(m for m, _ in v), "m_max": max(m for m, _ in v), "smallest_max": max(z for _, z in v)} for k, v in res.items()}}
json.dump(out, open(HERE / "post_seal_ratio.json", "w"), indent=1)
print(json.dumps(out, indent=1))
