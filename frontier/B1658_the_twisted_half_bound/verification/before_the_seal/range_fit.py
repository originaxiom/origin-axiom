"""EXPLORATION: fit ||Y(u v^T, p q^T)||^2 (unit vectors) to the SU(2) invariants x = |u^dag p|^2, y = |v^dag q|^2 (and the
symplectic ones 1 - x, 1 - y), random complex vectors."""
import numpy as np
QI = np.array([[1j, 0], [0, -1j]]); QJ = np.array([[0, 1], [-1, 0]], dtype=complex); QK = QI @ QJ; EPS = QJ; BLOCKS = [QJ, QI, QK]
def coupling(S, M): return np.array([[np.sum((Ca.T @ EPS @ S @ Cb)*M) for Cb in BLOCKS] for Ca in BLOCKS])
rng = np.random.default_rng(9); rows = []
unit = lambda: (lambda z: z/np.linalg.norm(z))(rng.normal(size=2) + 1j*rng.normal(size=2))
for _ in range(400):
    u, v, p, q = unit(), unit(), unit(), unit()
    Y2 = np.linalg.norm(coupling(np.outer(u, v), np.outer(p, q)))**2
    x, y = abs(np.vdot(u, p))**2, abs(np.vdot(v, q))**2
    x2, y2 = abs(np.vdot(u.conj(), p))**2, abs(np.vdot(v.conj(), q))**2      # bilinear overlaps u^T p, v^T q
    rows.append((Y2, x, y, x2, y2))
R = np.array(rows)
for name, cols in (("1, x, y, xy", lambda r: [1, r[1], r[2], r[1]*r[2]]), ("1, x2, y2, x2 y2", lambda r: [1, r[3], r[4], r[3]*r[4]]),
                   ("1, x, y2, x y2", lambda r: [1, r[1], r[4], r[1]*r[4]]), ("1, x2, y, x2 y", lambda r: [1, r[3], r[2], r[3]*r[2]])):
    A = np.array([cols(r) for r in R]); c, res, *_ = np.linalg.lstsq(A, R[:, 0], rcond=None)
    print(f"{name:18s} coeffs {np.round(c, 6)}  max residual {np.abs(A @ c - R[:, 0]).max():.2e}")
print("observed range of ||Y||^2:", R[:, 0].min(), R[:, 0].max())
