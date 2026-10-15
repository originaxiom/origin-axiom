"""EXPLORATION (main): B1656's coupling Y_ab(S, M) = sum (C_a^T eps S C_b) o M written as a bilinear tensor in the quaternion
components S = s0 + s.(i, j, k), M = m0 + m.(i, j, k); fit to Y = A(s, m) with a quaternion-product ansatz."""
import numpy as np, itertools, sympy as sp
QI = np.array([[1j, 0], [0, -1j]]); QJ = np.array([[0, 1], [-1, 0]], dtype=complex); QK = QI @ QJ; EPS = QJ
E = [np.eye(2, dtype=complex), QI, QJ, QK]; BLOCKS = [QJ, QI, QK]
def coupling(S, M): return np.array([[np.sum((Ca.T @ EPS @ S @ Cb)*M) for Cb in BLOCKS] for Ca in BLOCKS])
T = np.zeros((3, 3, 4, 4), dtype=complex)
for al in range(4):
    for be in range(4):
        T[:, :, al, be] = coupling(E[al], E[be])
s = sp.symbols("s0:4"); m = sp.symbols("m0:4")
Ysym = sp.zeros(3, 3)
for a in range(3):
    for b in range(3):
        Ysym[a, b] = sp.nsimplify(sum(sp.nsimplify(T[a, b, al, be].real) + sp.I*sp.nsimplify(T[a, b, al, be].imag) for al, be in [(0, 0)])*0)
        Ysym[a, b] = sp.expand(sum((sp.nsimplify(T[a, b, al, be].real) + sp.I*sp.nsimplify(T[a, b, al, be].imag))*s[al]*m[be] for al in range(4) for be in range(4)))
sp.pprint(Ysym)
print("det S =", sp.expand(sp.Matrix(2, 2, list(sum((sp.Matrix(E[al].tolist())*s[al] for al in range(4)), sp.zeros(2, 2)))).det()))

def adj3(Y):
    return np.array([[np.linalg.det(np.delete(np.delete(Y, j, 0), i, 1))*(-1)**(i+j) for j in range(3)] for i in range(3)])
rng = np.random.default_rng(5)
qn = lambda c: sum(c[k]*E[k] for k in range(4))
for trial in range(3):
    mvec = rng.normal(size=4) + 1j*rng.normal(size=4); mvec[0] = 1j*np.sqrt(mvec[1]**2 + mvec[2]**2 + mvec[3]**2)  # null: m0^2 + m.m = 0
    M = qn(mvec); assert abs(np.linalg.det(M)) < 1e-12
    ratios = []
    for _ in range(4):
        sv_ = rng.normal(size=4) + 1j*rng.normal(size=4); S = qn(sv_)
        A = adj3(coupling(S, M)); ratios.append(A/np.linalg.det(S))
    spread = max(np.abs(r - ratios[0]).max() for r in ratios)/np.abs(ratios[0]).max()
    print(f"trial {trial}: adj Y(S, M)/det S is independent of S? relative spread {spread:.2e}")

vals = []
for trial in range(8):
    mvec = rng.normal(size=4) + 1j*rng.normal(size=4); mvec[0] = 1j*np.sqrt(mvec[1]**2 + mvec[2]**2 + mvec[3]**2)
    M = qn(mvec); S = qn(rng.normal(size=4) + 1j*rng.normal(size=4))
    A = adj3(coupling(S, M))/np.linalg.det(S); vals.append(np.linalg.norm(A)/np.linalg.norm(M)**2)
print("||A(M)||/||M||^2 over 8 null M:", np.round(vals, 6))

from scipy.optimize import minimize
def null_from(z):                      # a normalised null quaternion from 3 complex numbers (s1, s2, s3), s0 = i sqrt(s.s)
    s = z[:3] + 1j*z[3:]; c = np.concatenate([[1j*np.sqrt(s @ s)], s]); M = qn(c); return M/np.linalg.norm(M)
def f(x, sign):
    S, M = null_from(x[:6]), null_from(x[6:]); return sign*np.linalg.norm(coupling(S, M))**2
lo, hi = [], []
for t in range(30):
    x0 = rng.normal(size=12)
    lo.append(minimize(f, x0, args=(1,), method="Nelder-Mead", options={"maxiter": 20000, "xatol": 1e-10, "fatol": 1e-12}).fun)
    hi.append(-minimize(f, x0, args=(-1,), method="Nelder-Mead", options={"maxiter": 20000, "xatol": 1e-10, "fatol": 1e-12}).fun)
print("||Y(S, M)||^2 over unit null S, M: min %.6f  max %.6f  => k = 2/||Y||^2 in [%.4f, %.4f], ratio <= %.4f" % (min(lo), max(hi), 2/max(hi), 2/min(lo), max(hi)/min(lo)))
