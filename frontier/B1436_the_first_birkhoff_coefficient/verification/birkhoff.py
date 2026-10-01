#!/usr/bin/env python3
"""The first Birkhoff coefficient of m004's monodromy trace map at its fixed character on the kappa = -2 leaf.

F(X, Y, Z) = (Z, YZ - X, Z(YZ - X) - Y) preserves kappa = X^2 + Y^2 + Z^2 - XYZ - 2 and the area form
Omega = dX ^ dY / (d kappa / dZ) = dX ^ dY / (2Z - XY) on each leaf.  At a hyperbolic fixed point with multipliers
lam, 1/lam an area-preserving map is conjugate to (q, p) -> (q L(qp), p / L(qp)), L(s) = lam (1 + a s + ...), in
coordinates with dq ^ dp = Omega.  The number a is the first Birkhoff coefficient.

WHY NO DARBOUX CHART IS NEEDED.  In linear eigen-coordinates (x, y) the quadratic terms are removed by a unique
near-identity change (no quadratic monomial is resonant), and the coefficient c21 of x^2 y in the x-component is then
unchanged by any cubic change (x^2 y is resonant).  So c21 depends only on the linear frame, through dx ^ dy at the
fixed point:  a = c21 / lam  with the frame normalised to Omega(e+, e-) = 1.   Omega -> c Omega sends a -> a / c.

Own code, no computer algebra system: exact arithmetic in K = Q(sqrt(-3), sqrt(21)) on rational 4-tuples, truncated
bivariate polynomials, the leaf as an implicit series, two charts, and controls.
"""
import json, pathlib
from fractions import Fraction as Fr
HERE = pathlib.Path(__file__).resolve().parent

class K:
    """a + b A + c B + d AB,  A^2 = -3, B^2 = 21"""
    __slots__ = ("c",)
    def __init__(self, a=0, b=0, c=0, d=0): self.c = (Fr(a), Fr(b), Fr(c), Fr(d))
    @staticmethod
    def of(v): return v if isinstance(v, K) else K(v)
    def __add__(s, o): o = K.of(o); return K(*[x + y for x, y in zip(s.c, o.c)])
    __radd__ = __add__
    def __neg__(s): return K(*[-x for x in s.c])
    def __sub__(s, o): return s + (-K.of(o))
    def __rsub__(s, o): return K.of(o) - s
    def __mul__(s, o):
        o = K.of(o); a, b, c, d = s.c; e, f, g, h = o.c
        return K(a * e - 3 * b * f + 21 * c * g - 63 * d * h, a * f + b * e + 21 * (c * h + d * g),
                 a * g + c * e - 3 * (b * h + d * f), a * h + d * e + b * g + c * f)
    __rmul__ = __mul__
    def conjA(s): a, b, c, d = s.c; return K(a, -b, c, -d)
    def conjB(s): a, b, c, d = s.c; return K(a, b, -c, -d)
    def inv(s):
        t = s * s.conjA()                                   # in Q(B)
        n = t * t.conjB()                                   # rational
        assert n.c[1:] == (0, 0, 0) and n.c[0] != 0
        return s.conjA() * t.conjB() * K(1 / n.c[0])
    def __truediv__(s, o): return s * K.of(o).inv()
    def __rtruediv__(s, o): return K.of(o) * s.inv()
    def __eq__(s, o): return s.c == K.of(o).c
    def __hash__(s): return hash(s.c)
    def iszero(s): return s.c == (0, 0, 0, 0)
    def __repr__(s):
        names = ["", "*sqrt(-3)", "*sqrt(21)", "*sqrt(-3)*sqrt(21)"]
        return " + ".join("%s%s" % (x, n) for x, n in zip(s.c, names) if x) or "0"
    def __complex__(s):
        a, b, c, d = [float(x) for x in s.c]; A = complex(0, 3 ** .5); B = 21 ** .5
        return a + b * A + c * B + d * A * B
A_ = K(0, 1); B_ = K(0, 0, 1)

DEG = 3
class P:
    """bivariate polynomial truncated at total degree DEG, coefficients in K"""
    def __init__(s, t=None): s.t = {k: v for k, v in (t or {}).items() if not v.iszero() and sum(k) <= DEG}
    @staticmethod
    def of(v): return v if isinstance(v, P) else P({(0, 0): K.of(v)})
    def __add__(s, o):
        o = P.of(o); t = dict(s.t)
        for k, v in o.t.items(): t[k] = t.get(k, K()) + v
        return P(t)
    __radd__ = __add__
    def __neg__(s): return P({k: -v for k, v in s.t.items()})
    def __sub__(s, o): return s + (-P.of(o))
    def __rsub__(s, o): return P.of(o) - s
    def __mul__(s, o):
        o = P.of(o); t = {}
        for (i, j), v in s.t.items():
            for (k, l), w in o.t.items():
                if i + j + k + l <= DEG: t[(i + k, j + l)] = t.get((i + k, j + l), K()) + v * w
        return P(t)
    __rmul__ = __mul__
    def co(s, i, j): return s.t.get((i, j), K())
    def subs(s, pu, pv):
        out = P(); pw = {}
        def power(base, n, tag):
            if (tag, n) not in pw: pw[(tag, n)] = P.of(1) if n == 0 else power(base, n - 1, tag) * base
            return pw[(tag, n)]
        for (i, j), v in s.t.items(): out = out + power(pu, i, "u") * power(pv, j, "v") * v
        return out
U = P({(1, 0): K(1)}); V = P({(0, 1): K(1)})

def leaf_series(X0, Y0, Z0, solve_for):
    """the third coordinate as a series in the two chart coordinates, on X^2 + Y^2 + Z^2 - XYZ = 0"""
    if solve_for == "Z":
        G = lambda w: (U + X0) * (U + X0) + (V + Y0) * (V + Y0) + w * w - (U + X0) * (V + Y0) * w; w0 = Z0; slope = 2 * Z0 - X0 * Y0
    else:
        G = lambda w: (U + X0) * (U + X0) + w * w + (V + Z0) * (V + Z0) - (U + X0) * w * (V + Z0); w0 = Y0; slope = 2 * Y0 - X0 * Z0
    ser = P.of(w0); s_inv = slope.inv()
    for _ in range(DEG + 2): ser = ser - G(ser) * s_inv
    assert not G(ser).t, "implicit series solves the leaf to the truncation degree"
    return ser, slope

def first_birkhoff(f1, f2, omega0, lam):
    """a for the planar map (u, v) -> (f1, f2) (fixed point at 0), area density omega0 at the fixed point"""
    A = [[f1.co(1, 0), f1.co(0, 1)], [f2.co(1, 0), f2.co(0, 1)]]
    det = A[0][0] * A[1][1] - A[0][1] * A[1][0]; tr = A[0][0] + A[1][1]; li = lam.inv()
    assert det == 1, "area-preserving at the fixed point"; assert tr == lam + li, "multipliers"
    def eigvec(mu):
        r = [A[0][0] - mu, A[0][1]]                         # (A - mu) e = 0
        e = (-r[1], r[0]) if not (r[0].iszero() and r[1].iszero()) else (-(A[1][1] - mu), A[1][0])
        assert (A[0][0] * e[0] + A[0][1] * e[1]) == mu * e[0] and (A[1][0] * e[0] + A[1][1] * e[1]) == mu * e[1]
        return e
    e1, e2 = eigvec(lam), eigvec(li)
    nrm = omega0 * (e1[0] * e2[1] - e1[1] * e2[0]); e2 = (e2[0] / nrm, e2[1] / nrm)        # Omega(e1, e2) = 1
    d = e1[0] * e2[1] - e1[1] * e2[0]; Pi = [[e2[1] / d, -e2[0] / d], [-e1[1] / d, e1[0] / d]]
    pu = U * e1[0] + V * e2[0]; pv = U * e1[1] + V * e2[1]
    F1, F2 = f1.subs(pu, pv), f2.subs(pu, pv)
    g1 = F1 * Pi[0][0] + F2 * Pi[0][1]; g2 = F1 * Pi[1][0] + F2 * Pi[1][1]
    assert g1.co(1, 0) == lam and g1.co(0, 1).iszero() and g2.co(1, 0).iszero() and g2.co(0, 1) == li
    mult = (lam, li); h = [P(), P()]
    def lampow(n):
        r = K(1)
        for _ in range(abs(n)): r = r * (lam if n > 0 else li)
        return r
    for k, g in enumerate((g1, g2)):
        for i in range(3):
            j = 2 - i; den = lampow(i - j) - mult[k]
            h[k] = h[k] + P({(i, j): g.co(i, j) / den})
    Hx, Hy = U + h[0], V + h[1]
    gH1 = g1.subs(Hx, Hy)
    lhs = gH1 - h[0].subs(U * lam, V * li)
    assert all(lhs.co(i, 2 - i).iszero() for i in range(3)), "quadratic terms removed"
    return lhs.co(2, 1) / lam

def fixed_point(sign):
    X0 = (K(3) + sign * A_) / 2; Y0 = (K(3) - sign * A_) / 2; return X0, Y0, X0
LAM = (K(5) + B_) / 2

def Fmap(X, Y, Z): return Z, Y * Z - X, Z * (Y * Z - X) - Y

def chart_XY(sign=1, iterate=1, scale=1):
    X0, Y0, Z0 = fixed_point(sign); Zs, slope = leaf_series(X0, Y0, Z0, "Z")
    pt = (U + X0, V + Y0, Zs)
    assert not (pt[0] * pt[0] + pt[1] * pt[1] + pt[2] * pt[2] - pt[0] * pt[1] * pt[2]).t
    lam = K(1)
    for _ in range(iterate): pt = Fmap(*pt); lam = lam * LAM
    assert pt[0].co(0, 0) == X0 and pt[1].co(0, 0) == Y0 and pt[2].co(0, 0) == Z0, "fixed point"
    return first_birkhoff(pt[0] - X0, pt[1] - Y0, K(scale) / slope, lam)

def chart_XZ(sign=1):
    """second chart: (X, Z) coordinates, Y implicit;  Omega = dX ^ dY / kappa_Z = - dX ^ dZ / kappa_Y"""
    X0, Y0, Z0 = fixed_point(sign); Ys, slope = leaf_series(X0, Y0, Z0, "Y")
    pt = Fmap(U + X0, Ys, V + Z0)
    return first_birkhoff(pt[0] - X0, pt[2] - Z0, -K(1) / slope, LAM)

def wrong_leaf(sign=1):
    """bite: the same computation with the leaf's curvature dropped (Z linear in u, v) must give a different number"""
    X0, Y0, Z0 = fixed_point(sign); Zs, slope = leaf_series(X0, Y0, Z0, "Z")
    Zlin = P({k: v for k, v in Zs.t.items() if sum(k) <= 1})
    pt = Fmap(U + X0, V + Y0, Zlin)
    return first_birkhoff(pt[0] - X0, pt[1] - Y0, K(1) / slope, LAM)

if __name__ == "__main__":
    target = K(0, Fr(16, 63)); res = {}
    a = chart_XY(); print("chart (X,Y):   a =", a, "  equals 16 sqrt(-3)/63:", a == target)
    b = chart_XZ(); print("chart (X,Z):   a =", b, "  equal:", a == b)
    c = chart_XY(sign=-1); print("conjugate fixed point:  a =", c, "  equals -a:", c == -a)
    d = chart_XY(iterate=2); print("F o F:   a =", d, "  equals 2a:", d == a + a)
    e = chart_XY(scale=Fr(7, 3)); print("Omega -> (7/3) Omega:   a =", e, "  equals a/(7/3):", e == a / K(Fr(7, 3)))
    lin = first_birkhoff(U * LAM, V * LAM.inv(), K(1), LAM); print("linear control:  a =", lin)
    w = wrong_leaf(); print("bite (leaf curvature dropped):  a =", w, "  differs:", w != a)
    ok = (a == target and a == b and c == -a and d == a + a and e == a / K(Fr(7, 3)) and lin.iszero() and w != a)
    res = dict(a=repr(a), a_chart_XZ=repr(b), a_conjugate_point=repr(c), a_double_iterate=repr(d), a_form_scaled_7_3=repr(e),
               linear_control=repr(lin), bite_wrong_leaf=repr(w), value="16*sqrt(-3)/63", numeric=[complex(a).real, complex(a).imag],
               multiplier="(5 + sqrt(21))/2", all_checks=bool(ok))
    json.dump(res, open(HERE / "birkhoff.json", "w"), indent=1)
    print("ALL CHECKS:", ok)
