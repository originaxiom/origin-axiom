"""P-039's escalated check (R76-1; data-free): is B345's anti-diagonal texture the order-3 cyclic structure? A symmetric
bilinear coupling covariant under a 3-cycle P (P Y P^T = Y), written in P's eigenbasis (the Z/3 charges k = 0, 1, 2),
has Y_kl != 0 only where k + l = 0 mod 3 -- entries (0,0), (1,2), (2,1): B345's texture. So the texture is the cyclic
structure in its charge basis, generic to every Z/3-covariant symmetric coupling. Checked on random couplings."""
import numpy as np
rng = np.random.default_rng(20261106)
P = np.roll(np.eye(3), 1, axis=0)
w = np.exp(2j * np.pi / 3); F = np.array([[w ** (i * k) for k in range(3)] for i in range(3)]) / np.sqrt(3)
eig = [complex(np.vdot(F[:, k], P @ F[:, k])) for k in range(3)]
assert all(abs(eig[k] - w ** (-k)) < 1e-12 for k in range(3))
worst_off, least_on = 0.0, np.inf
for _ in range(200):
    A = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3)); A = A + A.T
    Y = sum(np.linalg.matrix_power(P, k) @ A @ np.linalg.matrix_power(P, k).T for k in range(3))
    assert np.allclose(P @ Y @ P.T, Y)
    Yc = F.T @ Y @ F
    for k in range(3):
        for l in range(3):
            if (k + l) % 3: worst_off = max(worst_off, abs(Yc[k, l]) / np.abs(Yc).max())
            else: least_on = min(least_on, abs(Yc[k, l]) / np.abs(Yc).max())
print(f"200 random 3-cycle-covariant symmetric couplings in the charge basis: entries with k + l != 0 mod 3 at most "
      f"{worst_off:.1e} of the largest; entries (0,0), (1,2), (2,1) at least {least_on:.2e} -> the anti-diagonal texture")
