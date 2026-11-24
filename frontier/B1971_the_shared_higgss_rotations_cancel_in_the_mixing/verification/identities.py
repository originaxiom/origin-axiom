"""B1971 (main, 2026-11-24; data-free): the exact identities of B1736's coupling used here (sympy).
 I1  Y h = (h.h) u and h^T Y = (h.h) u^T, for every h, u, w (B1966's E1, restated).
 I2  with w = 0 (the up sector of frame C, whose '1' channel vanishes): Y u = (u.u) h, and Y (u x h) = -(u.h) (u x h).
 I3  with w = 0, on span(h, u) Y acts as h -> (h.h) u, u -> (u.u) h, so its eigenvalues there are +-sqrt((h.h)(u.u)),
     and det Y = (u.h)(h.h)(u.u) (B1969's law at w = 0: the pair's product -(h.h)(u.u) times -(u.h)).
 I4  the null basis n = (1, 0, i)/sqrt2, nb = conj(n), e = (0, 1, 0) is unitary, n.n = nb.nb = 0, n.nb = 1, e.e = 1.
    python3 identities.py > identities_run.txt"""
import sympy as sp
h = sp.Matrix(sp.symbols("h1:4")); u = sp.Matrix(sp.symbols("u1:4")); w = sp.symbols("w")
cross = lambda x: sp.Matrix([[0, -x[2], x[1]], [x[2], 0, -x[0]], [-x[1], x[0], 0]])
dot = lambda a, b: (a.T * b)[0]
Y = u * h.T + h * u.T - dot(u, h) * sp.eye(3) + w * cross(h)
Y0 = Y.subs(w, 0)
z = lambda M: sp.expand(M) == sp.zeros(*M.shape)
print("I1  Y h - (h.h) u = 0:", z(Y * h - dot(h, h) * u), "; h^T Y - (h.h) u^T = 0:", z(h.T * Y - dot(h, h) * u.T))
k = u.cross(h)
print("I2  (w = 0) Y u - (u.u) h = 0:", z(Y0 * u - dot(u, u) * h), "; Y (u x h) + (u.h)(u x h) = 0:", z(Y0 * k + dot(u, h) * k))
print("    (w != 0) Y u - (u.u) h = w (h x u):", z(Y * u - dot(u, u) * h - w * h.cross(u)))
print("I3  (w = 0) det Y - (u.h)(h.h)(u.u) = 0:", sp.expand(Y0.det() - dot(u, h) * dot(h, h) * dot(u, u)) == 0)
s = 1 / sp.sqrt(2); n = sp.Matrix([s, 0, sp.I * s]); nb = sp.Matrix([s, 0, -sp.I * s]); e = sp.Matrix([0, 1, 0])
P = sp.Matrix.hstack(n, nb, e)
print("I4  P unitary:", sp.simplify(P.H * P) == sp.eye(3), "; n.n, nb.nb, n.nb, e.e =", [sp.simplify(dot(n, n)), sp.simplify(dot(nb, nb)), sp.simplify(dot(n, nb)), dot(e, e)])
