"""Data-free: B1736's coupling in rho(T)'s eigenframe (f1 = conj h0, f2 = e1, f3 = h0) for h = f3 + delta f2 + eps f1 and
u = a3 f3 + a2 f2 + a1 f1 is exactly the matrix written in THE_NEXT_ATTACK.md section 1.1 (linear in delta and eps);
checked on 200 random draws of size O(1) (numpy default_rng(3))."""
import math
import numpy as np
rng = np.random.default_rng(3)
f1 = np.array([0, 1, -1j]) / math.sqrt(2); f2 = np.array([1, 0, 0], dtype=complex); f3 = np.array([0, 1, 1j]) / math.sqrt(2)
F = np.stack([f1, f2, f3], axis=1)
def cross(v): return np.array([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]])
worst = 0.0
for _ in range(200):
    u = rng.normal(size=3) + 1j * rng.normal(size=3); w = complex(*rng.normal(size=2))
    d = complex(*rng.normal(size=2)); e = complex(*rng.normal(size=2))
    h = f3 + d * f2 + e * f1
    Y = np.outer(u, h) + np.outer(h, u) - (u @ h) * np.eye(3) + w * cross(h)
    a1, a2, a3 = np.vdot(f1, u), np.vdot(f2, u), np.vdot(f3, u)
    Yh = np.array([[d * (1j * w - a2), d * a1 + e * (a2 - 1j * w), 2 * e * a1],
                   [a2 - 1j * w + d * a3, d * a2 - e * a3 - a1, d * a1 + e * (a2 + 1j * w)],
                   [2 * a3, a2 + 1j * w + d * a3, -d * (a2 + 1j * w)]])
    worst = max(worst, float(np.max(np.abs(F.conj().T @ Y @ F - Yh))))
print("max |F^dag Y F - the canonical matrix| over 200 draws:", worst)
