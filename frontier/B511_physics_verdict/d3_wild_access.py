#!/usr/bin/env python3
"""B511/D3.3 — wild-register accessibility under the stationary measure.
Wild fields (S4..S11) live at irreducible kappa!=2; classical kappa=2 is the abelian torsion factory.
The measure's mass near kappa!=2 = how often a typical history can birth wild arithmetic."""
import numpy as np


def haar(n, rng):
    q = rng.normal(size=(n, 4)); q /= np.linalg.norm(q, axis=1, keepdims=True)
    a, b, c, d = q.T
    M = np.zeros((n, 2, 2), complex)
    M[:, 0, 0] = a + 1j*b; M[:, 0, 1] = c + 1j*d; M[:, 1, 0] = -c + 1j*d; M[:, 1, 1] = a - 1j*b
    return M


def run(seed, n, steps, mix):
    rng = np.random.default_rng(seed); A, B = haar(n, rng), haar(n, rng)
    for t in range(steps):
        r = rng.random(n); ev_m = r < mix[0]; ev_d = (r >= mix[0]) & (r < mix[0] + mix[1])
        AB = A @ B
        Bn = np.where(ev_m[:, None, None], B @ A, np.where(ev_d[:, None, None], B @ B, A))
        An = np.where(ev_d[:, None, None], A @ A, AB); A, B = An, Bn
        if t % 20 == 19:
            for Mt in (A, B):
                d = np.sqrt(np.abs(np.linalg.det(Mt))); Mt /= d[:, None, None]
    x = np.real(np.trace(A, axis1=1, axis2=2)); y = np.real(np.trace(B, axis1=1, axis2=2))
    z = np.real(np.trace(A @ B, axis1=1, axis2=2))
    return x*x + y*y + z*z - x*y*z - 2


def accessibility(seed=11, n=4000, steps=3000, mix=(0.10, 0.10)):
    k = run(seed, n, steps, mix)
    classical = float(np.mean(np.abs(k - 2) < 0.05))
    wild = float(np.mean((np.abs(k - 2) > 0.5) & (k >= -2) & (k <= 2)))
    return classical, wild


if __name__ == "__main__":
    for mix, name in [((0.10, 0.10), "M10/D10/F80"), ((0.20, 0.0), "M20/F80"), ((0.0, 0.20), "D20/F80")]:
        c, w = accessibility(mix=mix)
        print("%-14s classical=%.3f wild-accessible=%.3f" % (name, c, w))
