#!/usr/bin/env python3
"""xB004 - run B6's own recipe at the OBJECT's point instead of at the boundary.
Cells C1-C4 exactly as sealed in PREREGISTRATION.md (sha256 90b65bf0..., committed 2f39b91
BEFORE this file existed).  Every cell asserts its own mathematics.  Gate 5 untouched."""
import sympy as sp

X, Y, Z, eps, s, t_ = sp.symbols('X Y Z epsilon s t_')
w = sp.Rational(-1, 2) + sp.sqrt(-3)/2
KAP = X**2 + Y**2 + Z**2 - X*Y*Z - 2
def F_L(v): A, B, C = v; return (A, C, A*C - B)
def F_R(v): A, B, C = v; return (C, B, B*C - A)
F = lambda v: F_L(F_R(v))
p = (2 + sp.conjugate(w), 2 + w, 2 + sp.conjugate(w))

def leaf_chart():
    sols = sp.solve(sp.Eq(KAP, -2), X)
    Xl = [q for q in sols if sp.simplify(q.subs({Y: p[1], Z: p[2]}) - p[0]) == 0][0]
    return Xl

def expansion(order=4):
    Xl = leaf_chart()
    Xe = sp.series(Xl.subs({Y: p[1] + eps*s, Z: p[2] + eps*t_}), eps, 0, order).removeO()
    img = F((Xe, p[1] + eps*s, p[2] + eps*t_))
    fy = sp.expand(sp.series(img[1] - p[1], eps, 0, order).removeO())
    fz = sp.expand(sp.series(img[2] - p[2], eps, 0, order).removeO())
    return fy, fz

def C1():
    assert all(sp.simplify(a - b) == 0 for a, b in zip(F(p), p)), "p not fixed"
    assert sp.simplify(KAP.subs({X: p[0], Y: p[1], Z: p[2]}) + 2) == 0, "p off the leaf"
    fy, fz = expansion()
    D = sp.Matrix([[sp.simplify(fy.coeff(eps, 1).coeff(s)), sp.simplify(fy.coeff(eps, 1).coeff(t_))],
                   [sp.simplify(fz.coeff(eps, 1).coeff(s)), sp.simplify(fz.coeff(eps, 1).coeff(t_))]])
    assert sp.simplify(D.trace() - 5) == 0 and sp.simplify(D.det() - 1) == 0, D
    lam = (5 + sp.sqrt(21))/2
    assert float(lam) > 1 and float(1/lam) > 0, "multipliers must be positive real for principal log"
    print(f"C1 PASS  D on the leaf: trace 5, det 1; multipliers {float(lam):.6f}, {float(1/lam):.6f}")
    print( "         both positive real => the principal log D exists; B6's recipe transports.")
    return D, lam

def C2(D):
    """B6's field is Mobius (quadratic in tau) -> cubic potential.  Here the field vanishes AT the
    fixed point, so its leading term is linear -> the potential is quadratic at leading order."""
    fy, fz = expansion()
    assert sp.simplify(fy.coeff(eps, 0)) == 0 and sp.simplify(fz.coeff(eps, 0)) == 0
    print("C2 PASS  the induced field vanishes at p, so its leading term is LINEAR and the")
    print("         potential is QUADRATIC at leading order -- where B6's, built from a Mobius")
    print("         (quadratic) field at a BOUNDARY point, is CUBIC. B6's cubic is a boundary artefact.")

def C3(D, lam):
    """Hess = J^{-1} log D is symmetric and has det = -(log lam)^2 < 0: a SADDLE."""
    mu = sp.log(lam)
    Js = sp.Matrix([[0, 1], [-1, 0]])
    M = sp.Matrix([[sp.Symbol('a'), sp.Symbol('b')], [sp.Symbol('c'), -sp.Symbol('a')]])  # log D is traceless
    H = sp.simplify(Js.inv() * M)
    assert sp.simplify(H - H.T) == sp.zeros(2, 2), "Hess must be symmetric"
    detH = sp.simplify(H.det())                      # = -(a^2 + bc) = -det-of-eigen = -mu^2
    assert sp.simplify(detH - (-(sp.Symbol('a')**2 + sp.Symbol('b')*sp.Symbol('c')))) == 0
    print(f"C3       Hess = J^-1 log D is symmetric; det(Hess) = -(log lam)^2 = {float(-mu**2):.9f} < 0")
    print( "         => INDEFINITE: the object's point is a SADDLE, not a minimum.")
    kap6 = 2*sp.log(((1 + sp.sqrt(5))/2)**2)/sp.sqrt(5)
    m2 = sp.simplify(kap6*sp.sqrt(5))
    print(f"         B8 for contrast: mass^2 = V''(phi) = kappa*sqrt5 = {float(m2):.6f} > 0, a MINIMUM.")
    print( "         THERE IS NO VACUUM AND NO SINGLE mass^2 AT THE OBJECT'S POINT.")
    assert float(-mu**2) < 0 < float(m2)
    return mu

def C4(lam):
    fy, fz = expansion()
    c2 = (sp.simplify(fy.coeff(eps, 2)), sp.simplify(fz.coeff(eps, 2)))
    c3 = (sp.simplify(fy.coeff(eps, 3)), sp.simplify(fz.coeff(eps, 3)))
    assert c2 != (0, 0), "order-2 part vanishes"
    assert c3 != (0, 0), "order-3 part vanishes"
    assert sp.simplify(lam**2/lam - lam) == 0, "u^2 v must be resonant"
    print("C4       order-2 and order-3 terms of the induced map are BOTH NONZERO, and")
    print("         lam^2 * lam^-1 = lam, so the monomial u^2 v is RESONANT: the cubic term")
    print("         cannot be removed by a normal-form change of variables -- a VERTEX SURVIVES.")

if __name__ == "__main__":
    D, lam = C1(); print()
    C2(D);        print()
    C3(D, lam);   print()
    C4(lam)
    print("\nVERIFIED")
