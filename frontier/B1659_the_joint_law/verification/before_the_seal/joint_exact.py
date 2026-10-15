"""EXPLORATION (main, firewalled; P-168): is the joint law exact? B1658's coupling Y(S, M) (bilinear, 3x3).
(b) null S => adj Y(S, M) = det M * At(S) for EVERY M (the mirror of B1658's T1)?
(c) det Y(S, M) = det S det M * l(S, M) with l BILINEAR (fit 16 coefficients, test on fresh draws)?
(d) adj Y = det S A(M) + det M At(S) + det S det M K exactly, K constant (fit, test)?"""
import numpy as np
QI = np.array([[1j, 0], [0, -1j]]); QJ = np.array([[0, 1], [-1, 0]], dtype=complex); QK = QI @ QJ; EPS = QJ; BLOCKS = [QJ, QI, QK]
def Y(S, M): return np.array([[np.sum((Ca.T @ EPS @ S @ Cb)*M) for Cb in BLOCKS] for Ca in BLOCKS])   # B1658's coupling, verbatim
def adj3(A): return np.array([[np.linalg.det(np.delete(np.delete(A, j, 0), i, 1))*(-1)**(i+j) for j in range(3)] for i in range(3)])
rng = np.random.default_rng(1659); c2 = lambda: rng.normal(size=2) + 1j*rng.normal(size=2); R = lambda: rng.normal(size=(2, 2)) + 1j*rng.normal(size=(2, 2))
# (b)
worst = 0
for _ in range(200):
    S0 = np.outer(c2(), c2()); M1, M2 = R(), R()
    a1, a2 = adj3(Y(S0, M1))/np.linalg.det(M1), adj3(Y(S0, M2))/np.linalg.det(M2)
    worst = max(worst, np.abs(a1 - a2).max()/np.abs(a1).max())
print(f"(b) null S: adj Y(S0, M)/det M independent of M: worst relative spread {worst:.1e}")
# (c) l bilinear: det Y/(det S det M) = sum L[i,k] s_i m_k (s, m the 4 entries)
def feats(S, M): return np.outer(S.ravel(), M.ravel()).ravel()
X, y = [], []
for _ in range(64):
    S, M = R(), R(); X.append(feats(S, M)); y.append(np.linalg.det(Y(S, M))/(np.linalg.det(S)*np.linalg.det(M)))
L, *_ = np.linalg.lstsq(np.array(X), np.array(y), rcond=None)
err = max(abs(feats(S, M) @ L - np.linalg.det(Y(S, M))/(np.linalg.det(S)*np.linalg.det(M)))/abs(np.linalg.det(Y(S, M))/(np.linalg.det(S)*np.linalg.det(M)))
          for S, M in ((R(), R()) for _ in range(200)))
print(f"(c) l(S, M) bilinear: fresh-draw relative error {err:.1e}; L (4x4) =\n", np.round(L.reshape(4, 4), 6))
# (d) A(M) := adj Y(S, M) at det S = 1 minus ... : fit adj Y = dS*A(M) + dM*At(S) + dS*dM*K, with A, At quadratic, K constant.
# Quadratic features: monomials of degree 2 in the 4 entries (10 each). Unknowns per matrix entry: 10 + 10 + 1 = 21.
def q2(Z):
    z = Z.ravel(); return np.array([z[i]*z[j] for i in range(4) for j in range(i, 4)])
rows, rhs = [], []
for _ in range(120):
    S, M = R(), R(); dS, dM = np.linalg.det(S), np.linalg.det(M)
    rows.append(np.concatenate([dS*q2(M), dM*q2(S), [dS*dM]])); rhs.append(adj3(Y(S, M)).ravel())
C, res, rk, _ = np.linalg.lstsq(np.array(rows), np.array(rhs), rcond=None)
err = 0
for _ in range(200):
    S, M = R(), R(); dS, dM = np.linalg.det(S), np.linalg.det(M)
    pred = np.concatenate([dS*q2(M), dM*q2(S), [dS*dM]]) @ C; tru = adj3(Y(S, M)).ravel()
    err = max(err, np.abs(pred - tru).max()/np.abs(tru).max())
print(f"(d) adj Y = dS A(M) + dM At(S) + dS dM K: fit rank {rk} of 21, fresh-draw relative error {err:.1e}")
# the gauge freedom: A -> A + dM*K', At -> At - dS*K'... (dS dM K is absorbable); report K in the gauge where A has no det M part
