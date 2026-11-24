"""B1973: main's own check of A2-P879's T3 (2026-11-24): sup over unit xi of |<v(l_u, eps conj xi) | v(l_d, xi)>| / norms vs (1+s)/(3-s).
v(l, xi) = Pauli coordinates (sigma_x, sigma_y, sigma_z) of the 2x2 rank-one matrix xi l^T -- the traceless part; tried with both
orders (xi l^T and l xi^T) and with and without eps, to see which convention gives the card's ||v||^2 = 2 - |l^T xi|^2."""
import numpy as np
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.array([[1, 0], [0, -1]], complex)
eps = np.array([[0, 1], [-1, 0]], complex)
def vcoords(M): return np.array([np.trace(P.conj().T @ M) for P in (sx, sy, sz)])
def v(l, xi, order): M = np.outer(xi, l) if order == 0 else np.outer(l, xi); return vcoords(M)
rng = np.random.default_rng(1)
for order in (0, 1):
    l = rng.normal(size=2) + 1j * rng.normal(size=2); l /= np.linalg.norm(l); xi = rng.normal(size=2) + 1j * rng.normal(size=2); xi /= np.linalg.norm(xi)
    print("order %d: ||v||^2 = %.6f ; 2 - |l.xi|^2 = %.6f ; 1 + |l^T eps xi|^2 = %.6f" % (order, np.linalg.norm(v(l, xi, order)) ** 2, 2 - abs(l @ xi) ** 2, 1 + abs(l @ eps @ xi) ** 2))
def best(s, order, n=400):
    ld = np.array([1, 0], complex); lu = np.array([np.sqrt(1 - s * s), s], complex)
    m = 0
    for t in np.linspace(0, np.pi, n):
        for ph in np.linspace(0, 2 * np.pi, 2 * n // 5):
            xi = np.array([np.cos(t), np.sin(t) * np.exp(1j * ph)])
            a = v(lu, eps @ xi.conj(), order); b = v(ld, xi, order)
            m = max(m, abs(np.vdot(a, b)) / (np.linalg.norm(a) * np.linalg.norm(b)))
    return m
for order in (0, 1):
    print("order %d:" % order, [(s, round(best(s, order), 5), round((1 + s) / (3 - s), 5)) for s in (0.0, 0.25, 0.5, 0.75, 17 / 19, 1.0)])
