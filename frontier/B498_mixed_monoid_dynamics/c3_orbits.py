#!/usr/bin/env python3
"""B498 C3 — bounded reproduction of the drift table (E-data).

Group-side SU(2) simulation (Haar pairs via unit quaternions; substitutions on matrices;
periodic re-unitarization). Bounded protocol: 200 orbits x 300 steps, seeds {11, 42}.
Reproduces the handoff's ordering and magnitudes (the handoff ran 500x400):
units never classicalize (0%); F80/D20 the strongest classicalizer; M broad/critical.

  python3 c3_orbits.py
"""
import numpy as np


def haar_su2(rng):
    q = rng.normal(size=4); q /= np.linalg.norm(q)
    a, b, c, d = q
    return np.array([[a + 1j*b, c + 1j*d], [-c + 1j*d, a - 1j*b]])


def unitarize(U):
    q, r = np.linalg.qr(U)
    return q @ np.diag(np.diag(r)/np.abs(np.diag(r)))


def kappa(A, B):
    C = A @ B @ np.linalg.inv(A) @ np.linalg.inv(B)
    return np.real(np.trace(C))


def run(mix, seed, orbits=200, steps=300):
    rng = np.random.default_rng(seed)
    finals = []
    for _ in range(orbits):
        A, B = haar_su2(rng), haar_su2(rng)
        for t in range(steps):
            r = rng.random(); acc = 0.0; applied = False
            for verb, p in mix:
                acc += p
                if r < acc:
                    if verb == 'F':   A, B = A @ B, A
                    elif verb == 'M': A, B = A @ B, B @ A
                    else:             A, B = A @ A, B @ B
                    applied = True
                    break
            if not applied:
                A, B = A @ B, A
            if t % 20 == 19:
                A, B = unitarize(A), unitarize(B)
        finals.append(abs(kappa(A, B) - 2.0))
    fin = np.array(finals); fin[fin < 1e-300] = 1e-300
    return float(np.median(np.log10(fin))), float(np.mean(fin < 1e-6))


MIXES = {
    'units only (F)': [('F', 1.0)],
    'F80/M20':        [('F', 0.8), ('M', 0.2)],
    'F80/D20':        [('F', 0.8), ('D', 0.2)],
    'F80/M10/D10':    [('F', 0.8), ('M', 0.1), ('D', 0.1)],
}

if __name__ == "__main__":
    for name, mix in MIXES.items():
        m1, f1 = run(mix, 11)
        m2, f2 = run(mix, 42)
        print("%-16s seed11: %+6.2f/%.3f   seed42: %+6.2f/%.3f" % (name, m1, f1, m2, f2))
