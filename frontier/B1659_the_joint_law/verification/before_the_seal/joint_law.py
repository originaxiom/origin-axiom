"""EXPLORATION (main, firewalled): the joint law -- both the Higgs S and the matter M slightly off null. Test
(i) det Y(S, M) = c det S det M <S, M> (a bilinear pairing), (ii) adj Y(S, M) = det S A(M) + det M A~(S)."""
import numpy as np
QI = np.array([[1j, 0], [0, -1j]]); QJ = np.array([[0, 1], [-1, 0]], dtype=complex); QK = QI @ QJ; EPS = QJ; BLOCKS = [QJ, QI, QK]
def coupling(S, M): return np.array([[np.sum((Ca.T @ EPS @ S @ Cb)*M) for Cb in BLOCKS] for Ca in BLOCKS])
def adj3(Y): return np.array([[np.linalg.det(np.delete(np.delete(Y, j, 0), i, 1))*(-1)**(i+j) for j in range(3)] for i in range(3)])
rng = np.random.default_rng(8); R = lambda: rng.normal(size=(2, 2)) + 1j*rng.normal(size=(2, 2))
# (i): det Y / (det S det M) bilinear?  test linearity in S and in M
S1, S2, M1, M2 = R(), R(), R(), R()
g = lambda S, M: np.linalg.det(coupling(S, M))/(np.linalg.det(S)*np.linalg.det(M))
print("g(S,M) values:", np.round([g(S1, M1), g(S2, M1), g(S1, M2)], 6))
# a bilinear candidate: tr(S^T eps M eps^T)? compare
cands = {"tr(S M^T)": lambda S, M: np.trace(S @ M.T), "tr(S eps M^T eps^T)": lambda S, M: np.trace(S @ EPS @ M.T @ EPS.T),
         "tr(S M)": lambda S, M: np.trace(S @ M), "tr(S eps M eps)": lambda S, M: np.trace(S @ EPS @ M @ EPS),
         "tr(S^T M)": lambda S, M: np.trace(S.T @ M), "tr(S adjM)": lambda S, M: np.trace(S @ np.array([[M[1,1], -M[0,1]], [-M[1,0], M[0,0]]]))}
for n, c in cands.items():
    vals = [g(S, M)/c(S, M) for S, M in ((S1, M1), (S2, M1), (S1, M2), (S2, M2))]
    print(f"  g / {n:22s}", np.round(vals, 6))
# (ii): adj decomposition: fit adj Y(S, M) - det S A(M) where A(M) defined from a null-projection? test symmetry: A~(S) = A(S) transposed?
def Aof(M):  # A(M) := adj Y(S, M)/det S for a null M only; for general M define by linearity in the symmetric square? use limit
    return None
S0n = np.outer(rng.normal(size=2)+1j*rng.normal(size=2), rng.normal(size=2)+1j*rng.normal(size=2))   # null S
M0n = np.outer(rng.normal(size=2)+1j*rng.normal(size=2), rng.normal(size=2)+1j*rng.normal(size=2))   # null M
AM = adj3(coupling(R(), M0n))/1.0
Sx = R(); AM = adj3(coupling(Sx, M0n))/np.linalg.det(Sx)                 # A(M0n)
My = R(); AS = adj3(coupling(S0n, My))/np.linalg.det(My)                 # A~(S0n), by the a <-> v reading
print("adj Y(S0n, M0n) (both null):", np.abs(adj3(coupling(S0n, M0n))).max())
X, Z = R(), R()
for eps in (1e-3, 1e-4):
    S = S0n + eps*X; M = M0n + eps*Z
    lhs = adj3(coupling(S, M)); rhs = np.linalg.det(S)*adj3(coupling(Sx, M))/np.linalg.det(Sx) + np.linalg.det(M)*adj3(coupling(S, My))/np.linalg.det(My)
    print(f"eps={eps}: |adj Y - (det S A(M) + det M A~(S))| / |adj Y| = {np.abs(lhs - rhs).max()/np.abs(lhs).max():.3e}")
