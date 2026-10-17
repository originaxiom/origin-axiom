"""The determinant identity (Theorem 2 of the note), symbolically. Y(S,M)_ab = sum_mn (C_a^T eps S C_b)_mn M_mn with
eps = [[0,1],[-1,0]] and (C_1, C_2, C_3) = (eps, diag(i,-i), diag(i,-i) eps). Checks det Y = 4 det S det M tr(eps S M^T),
adj Y = det S A(M) + det M P A(S) with P = diag(1,-1,-1), the symmetric form Y(S, N eps^-1) = Y(N, S eps^-1) with N = M eps,
tr(eps S M^T) = -(det(S+N) - det S - det N), and the geometric masses m1 m3 = m2^2 at N = S (numerically)."""
import sympy as sp
import numpy as np
s = sp.symbols("s0:4"); m = sp.symbols("m0:4")
S = sp.Matrix([[s[0], s[1]], [s[2], s[3]]]); M = sp.Matrix([[m[0], m[1]], [m[2], m[3]]])
I = sp.I; eps = sp.Matrix([[0, 1], [-1, 0]]); d = sp.diag(I, -I)
C = [eps, d, d * eps]
def Y(S, M):
    return sp.Matrix(3, 3, lambda a, b: sum(((C[a].T * eps * S * C[b])[p, q] * M[p, q]) for p in range(2) for q in range(2)))
def A(M):
    m0, m1, m2, m3 = M[0, 0], M[0, 1], M[1, 0], M[1, 1]
    return sp.Matrix([[m0**2 + m1**2 + m2**2 + m3**2, 2*I*(m0*m2 + m1*m3), -I*(m0**2 + m1**2 - m2**2 - m3**2)],
                      [2*I*(m0*m1 + m2*m3), -4*m1*m2, 2*(m0*m1 - m2*m3)],
                      [-I*(m0**2 - m1**2 + m2**2 - m3**2), 2*(m0*m2 - m1*m3), -m0**2 + m1**2 + m2**2 - m3**2]])
P = sp.diag(1, -1, -1)
Yv = Y(S, M)
r1 = sp.expand(Yv.det() - 4 * S.det() * M.det() * (eps * S * M.T).trace())
r2 = (Yv.adjugate() - (S.det() * A(M) + M.det() * P * A(S))).applyfunc(sp.expand)
N = M * eps
r3 = (Y(S, N * eps.inv()) - Y(N, S * eps.inv())).applyfunc(sp.expand)
r4 = sp.expand((eps * S * M.T).trace() + ((S + N).det() - S.det() - N.det()))
print("det law residual:", r1); print("adjugate law residual zero:", r2 == sp.zeros(3, 3))
print("symmetric form residual zero:", r3 == sp.zeros(3, 3)); print("polar identity residual:", r4)
assert r1 == 0 and r2 == sp.zeros(3, 3) and r3 == sp.zeros(3, 3) and r4 == 0
rng = np.random.default_rng(7); worst = 0.0
for _ in range(20):
    Sn = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
    Mn = Sn @ np.linalg.inv(np.array([[0, 1], [-1, 0]]))       # N = M eps = S
    Yn = np.array(Y(sp.Matrix(Sn), sp.Matrix(Mn)).evalf(), dtype=complex)
    sv = np.sort(np.linalg.svd(Yn, compute_uv=False))
    worst = max(worst, abs(sv[0] * sv[2] / sv[1] ** 2 - 1))
print(f"geometric masses at N = S: max |m1 m3 / m2^2 - 1| = {worst:.1e} over 20 random S")
assert worst < 1e-10
print("all checks pass")
