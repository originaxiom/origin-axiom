"""Data-free: the determinant of B1736's coupling Y = u h^T + h u^T - (u.h) 1 + w [h]_x."""
import sympy as sp
u = sp.symbols('u1:4'); h = sp.symbols('h1:4'); w = sp.symbols('w')
U = sp.Matrix(u); H = sp.Matrix(h)
def cross(v):
    return sp.Matrix([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]])
Y = U * H.T + H * U.T - (U.dot(H)) * sp.eye(3) + w * cross(H)
d = sp.factor(sp.expand(Y.det()))
print("det Y =", d)
cand = (H.dot(H)) * (U.dot(H)) * (U.dot(U) + w**2)        # corrected 2026-10-23 after the referee: the sign is +
print("det Y - (h.h)(u.h)(u.u + w^2) =", sp.simplify(sp.expand(Y.det() - cand)))
# the 2x2 minors' sum (sum of principal 2x2 minors = e2 of eigenvalues) and trace, for the record
print("trace Y =", sp.factor(Y.trace()))
