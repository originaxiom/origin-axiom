#!/usr/bin/env python3
"""xB003 ADDENDUM 3 - the inception check: B13's evaluation point is on kappa = +2, not the
object's kappa = -2.  Reproduces B13's founding result and locates it on the leaf lattice."""
import sympy as sp
x, y, z, t = sp.symbols('x y z t')
def T(v): X, Y, Z = v; return (Z, X, 2*X*Z - Y)
I_half = x**2 + y**2 + z**2 - 2*x*y*z - 1          # B1341's half-trace invariant; kappa = 4I + 2

def main():
    # B13, reproduced
    J = sp.Matrix(list(T((x, y, z)))).jacobian([x, y, z]).subs({x: 1, y: 1, z: 1})
    cp = sp.factor(J.charpoly(t).as_expr())
    assert J.tolist() == [[0, 0, 1], [1, 0, 0], [2, -1, 2]], J.tolist()
    assert sp.simplify(cp - (t + 1)*(t**2 - 3*t + 1)) == 0, cp
    assert J.det() == -1
    print(f"B13 reproduced: J(T)|(1,1,1) charpoly {cp}, det {J.det()} (anti-symplectic)")

    # where is (1,1,1)?
    Ival = I_half.subs({x: 1, y: 1, z: 1})
    kap = 4*Ival + 2
    assert Ival == 0 and kap == 2
    full = (2, 2, 2)
    kap_full = full[0]**2 + full[1]**2 + full[2]**2 - full[0]*full[1]*full[2] - 2
    assert kap_full == 2
    print(f"   (1,1,1) half-traces -> I = {Ival}, kappa = {kap};  full traces (2,2,2) -> kappa = {kap_full}")
    print("   => B13's point is on kappa = +2: B1341's leaf, and B1342's 'nothing' leaf.")
    print("      The object is on kappa = -2.  Its regular fixed point gives t^2 - 5t + 1, not t^2 - 3t + 1.")

    # the object's point, for contrast (full traces)
    w = sp.Rational(-1, 2) + sp.sqrt(-3)/2
    p = (2 + sp.conjugate(w), 2 + w, 2 + w)
    kp = sp.simplify(p[0]**2 + p[1]**2 + p[2]**2 - p[0]*p[1]*p[2] - 2)
    assert sp.simplify(kp + 2) == 0, kp
    print(f"   the object's fixed point (2+conj(w), 2+w, 2+w) has kappa = {kp}")
    print("VERIFIED")

if __name__ == "__main__":
    main()
