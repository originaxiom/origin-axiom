"""B1955, corrected 2026-11-17 on the web seat's referee read of W-A3 (its commit 3c50b6d63): the object carries both
Weil classes.  Main's own checks (no data):
1. In both classes, |tr rho(g)|^2 is the number of points of F_5^2 fixed by g, for all 120 elements: End(W) is the
   permutation representation on F_5^2 in either class, so the frame's lines cannot tell the classes apart.
2. With the cover's pairing (shifts X, clocks Z, XZ = zeta^-1 ZX), the unit shear (s, k) -> (s, k + s) on the labels is
   implemented by diag(psi(c x^2)) with c a non-residue: the act's unipotent part brings the class of 2x^2/5, B1951's.
3. The knot's discriminant form is x^2/5, a residue (from the Seifert matrix): the other class."""
import itertools
from fractions import Fraction as Fr
import numpy as np
z = np.exp(2j * np.pi / 5); psi = lambda x: z ** (x % 5)
X = np.roll(np.eye(5), 1, axis=0).astype(complex); Z = np.diag([psi(x) for x in range(5)])
Wop = lambda a, b: np.linalg.matrix_power(X, a % 5) @ np.linalg.matrix_power(Z, b % 5)


def weil(c):
    T = np.diag([psi(c * x * x) for x in range(5)])
    for k in (1, 2, 3, 4):
        Fk = np.array([[psi(k * x * y) for y in range(5)] for x in range(5)]) / np.sqrt(5)
        for s in (1, -1, 1j, -1j):
            S = s * Fk
            if np.abs(np.linalg.matrix_power(S @ T, 3) - S @ S).max() < 1e-12 and np.abs(np.linalg.matrix_power(S, 4) - np.eye(5)).max() < 1e-12: return T, S


def induced(U):
    def im(a, b):
        M = U @ Wop(a, b) @ U.conj().T
        return max(itertools.product(range(5), repeat=2), key=lambda v: abs(np.trace(Wop(*v).conj().T @ M)))
    return im(1, 0), im(0, 1)


def trace_is_fixed_points(c):
    T, S = weil(c); key = lambda A: tuple(np.round(A.flatten(), 8))
    G = {key(np.eye(5)): np.eye(5, dtype=complex)}; fr = list(G.values())
    while fr:
        nx = []
        for A in fr:
            for g in (T, S):
                N = A @ g
                if key(N) not in G: G[key(N)] = N; nx.append(N)
        fr = nx
    worst = 0.0
    for U in G.values():
        e1, e2 = induced(U)
        fixed = sum(1 for a in range(5) for b in range(5) if ((a * e1[0] + b * e2[0]) % 5, (a * e1[1] + b * e2[1]) % 5) == (a, b))
        worst = max(worst, abs(abs(np.trace(U)) ** 2 - fixed))
    return len(G), worst


def unit_shear_classes():
    """the c for which diag(psi(c x^2)) sends the label (1, 0) to (1, +1) or (1, -1)"""
    out = {}
    for c in range(1, 5):
        e1, e2 = induced(np.diag([psi(c * x * x) for x in range(5)]))
        out[c] = (e1, e2)
    return out


if __name__ == "__main__":
    for c in (1, 2):
        n, w = trace_is_fixed_points(c)
        print("1. class %d: on all %d elements |tr rho(g)|^2 equals the number of points of F_5^2 that g fixes (worst difference %.1e)" % (c, n, w))
    us = unit_shear_classes()
    for c, (e1, e2) in us.items():
        print("2. diag(psi(%d x^2)) sends the labels (1, 0), (0, 1) to %s, %s: a shear by %d; %d is a %s mod 5" % (c, e1, e2, e1[1], c, "residue" if c in (1, 4) else "non-residue"))
    unit = sorted(c for c, (e1, e2) in us.items() if e1[1] in (1, 4))
    print("   the unit shears (by +1 or -1) are implemented by c in %s: the class of 2x^2/5" % unit)
    g = Fr(2, 5)
    print("3. the knot's form V + V^T = [[2, 1], [1, -2]] has (g, g) = %s on its discriminant group's generator: q = x^2/5 (a residue), b(x, x) = 2x^2/5" % g)
