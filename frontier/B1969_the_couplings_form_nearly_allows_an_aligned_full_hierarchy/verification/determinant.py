"""B1969: the determinant of B1736's coupling in its own variables (exact, sympy): det Y = (h.h)(w^2 + u.u)(u.h).
This is B1659's determinant law, det Y = 4 det S det M tr(eps S M^T), in B1736's variables: the Higgs's nullity, the
channel quaternion's nullity and their overlap.
    python3 determinant.py > determinant_run.txt"""
import sympy as sp
h = sp.Matrix(sp.symbols("h1:4")); u = sp.Matrix(sp.symbols("u1:4")); w = sp.symbols("w")
cross = lambda x: sp.Matrix([[0, -x[2], x[1]], [x[2], 0, -x[0]], [-x[1], x[0], 0]])
Y = u * h.T + h * u.T - (u.T * h)[0] * sp.eye(3) + w * cross(h)
print("det Y - (h.h)(w^2 + u.u)(u.h) =", sp.expand(Y.det() - (h.T * h)[0] * (w ** 2 + (u.T * u)[0]) * (u.T * h)[0]))
