"""B1966 (main, 2026-11-19; exact, sympy; data-free): the trade-off's two ends, from B1736's closed form of the coupling,
Y = u h^T + h u^T - (u.h) 1 + u1 [h]_x (h0 = 0: a pure triplet Higgs, as frame C's).
 E1  for every h, u, u1:  Y h = (h.h) u  and  h^T Y = (h.h) u^T.
 E2  so for a null Higgs (h.h = 0), for every channel (u, u1): Y h = 0 and h^T Y = 0: m1 = 0, the left null vector is
     conj(h); under the conjugate reading (h -> conj(h), the channels unchanged) it is h; <conj(h), h> = conj(h.h) = 0:
     the two readings' light states are orthogonal, exactly, whatever the channels.
 E3  for a real unit Higgs h and every channel: Y (1 - 2 h h^T) = c 1 + [a]_x with c = -(u.h), a = u1 h - (u x h) ... read
     off below; so B1727's sharp bound sigma_1 <= 3 sigma_2 applies: m2/m3 >= 1/3, for every channel.
 E4  the null case's heavy pair: with h = (1, i, 0) (h.h = 0, |h|^2 = 2), the two non-zero singular values satisfy
     m2 m3 = 2 |u1^2 + u.u| ... checked as the product of the non-zero singular values against |u1^2 + u.u| up to a fixed
     factor, so the heavy pair's hierarchy is the channel quaternion's near-nullity (B1659's det M).
    python3 endpoints.py > endpoints_run.txt"""
import sympy as sp, itertools, random
h1, h2, h3, v1, v2, v3, w = sp.symbols("h1 h2 h3 u_1 u_2 u_3 u1w")
h = sp.Matrix([h1, h2, h3]); u = sp.Matrix([v1, v2, v3])
cross = lambda x: sp.Matrix([[0, -x[2], x[1]], [x[2], 0, -x[0]], [-x[1], x[0], 0]])
Y = u * h.T + h * u.T - (u.T * h)[0] * sp.eye(3) + w * cross(h)
hh = (h.T * h)[0]
print("E1: Y h - (h.h) u = %s; h^T Y - (h.h) u^T = %s" % ((Y * h - hh * u).applyfunc(sp.expand).T, (h.T * Y - hh * u.T).applyfunc(sp.expand)))
# E3: real unit h = e1 by rotation invariance (Y is covariant: R Y(h, u) R^T = Y(Rh, Ru) for R in SO(3)); check that too
R = sp.Matrix([[sp.cos(w), -sp.sin(w), 0], [sp.sin(w), sp.cos(w), 0], [0, 0, 1]])
a1, a2, a3, b1, b2, b3, c = sp.symbols("a1 a2 a3 b1 b2 b3 c")
hv = sp.Matrix([a1, a2, a3]); uv = sp.Matrix([b1, b2, b3])
Yf = lambda hh_, uu_, s: uu_ * hh_.T + hh_ * uu_.T - (uu_.T * hh_)[0] * sp.eye(3) + s * cross(hh_)
cov = sp.simplify(R * Yf(hv, uv, c) * R.T - Yf(R * hv, R * uv, c))
print("E3 (covariance): R Y(h, u) R^T - Y(Rh, Ru) = 0 for a rotation R:", cov == sp.zeros(3))
e1 = sp.Matrix([1, 0, 0]); Ye = Yf(e1, uv, c); Rf = sp.eye(3) - 2 * e1 * e1.T; Z = Ye * Rf
sym = (Z + Z.T) / 2
print("E3: for h = e1, Y (1 - 2 e1 e1^T) = %s; its symmetric part is a multiple of 1: %s (= %s 1)" % (Z.tolist(), sp.simplify(sym - sym[0, 0] * sp.eye(3)) == sp.zeros(3), sp.simplify(sym[0, 0])))
# E4: null h numerically exact enough with sympy at random rational channels
rnd = random.Random(1966); worst = 0
for k in range(5):
    vals = {s: sp.Rational(rnd.randint(-9, 9), rnd.randint(1, 5)) + sp.I * sp.Rational(rnd.randint(-9, 9), rnd.randint(1, 5)) for s in (v1, v2, v3, w)}
    Yn = Y.subs({h1: 1, h2: sp.I, h3: 0}).subs(vals)
    import mpmath as mpm; mpm.mp.dps = 40
    Mn = mpm.matrix([[mpm.mpc(complex(Yn[i, j].evalf(40))) for j in range(3)] for i in range(3)])
    sv = sorted(float(x) for x in mpm.svd_c(Mn, compute_uv=False))
    target = abs(complex((vals[w] ** 2 + vals[v1] ** 2 + vals[v2] ** 2 + vals[v3] ** 2).evalf(30)))
    print("E4 sample %d: m1 = %.1e; m2 m3 = %.12f; |u1^2 + u.u| = %.12f; ratio %.12f" % (k, sv[0], sv[1] * sv[2], target, sv[1] * sv[2] / target))
